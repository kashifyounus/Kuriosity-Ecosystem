import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "ke_harness.py"
SPEC = importlib.util.spec_from_file_location("ke_harness", MODULE_PATH)
HARNESS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HARNESS)


class HarnessValidationTests(unittest.TestCase):
    def make_state(self, items, executions=None):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        directory = root / "engineering-harness"
        directory.mkdir()
        manifest = {
            "schema_version": "1.0", "executor_is_authority": False, "authoritative_branch": "main",
            "selection": {"eligible_status": "Ready", "dependency_satisfied_statuses": ["Approved", "Completed"]}
        }
        for name, data in (
            ("manifest.json", manifest),
            ("work-queue.json", {"schema_version": "1.0", "work_items": items}),
            ("execution-register.json", {"schema_version": "1.0", "executions": executions or []}),
        ):
            (directory / name).write_text(json.dumps(data), encoding="utf-8")
        self.addCleanup(temporary.cleanup)
        return root, manifest, {"work_items": items}

    def bind_state(self, root):
        old = (HARNESS.ROOT, HARNESS.HARNESS, HARNESS.MANIFEST_PATH, HARNESS.QUEUE_PATH, HARNESS.REGISTER_PATH, HARNESS.LOCK_PATH)
        directory = root / "engineering-harness"
        HARNESS.ROOT = root
        HARNESS.HARNESS = directory
        HARNESS.MANIFEST_PATH = directory / "manifest.json"
        HARNESS.QUEUE_PATH = directory / "work-queue.json"
        HARNESS.REGISTER_PATH = directory / "execution-register.json"
        HARNESS.LOCK_PATH = directory / ".state.lock"
        self.addCleanup(lambda: self.restore_state(old))

    @staticmethod
    def restore_state(old):
        HARNESS.ROOT, HARNESS.HARNESS, HARNESS.MANIFEST_PATH, HARNESS.QUEUE_PATH, HARNESS.REGISTER_PATH, HARNESS.LOCK_PATH = old

    def item(self, work_id, status="Ready", priority=10, dependencies=None, active=None):
        return {
            "id": work_id, "status": status, "priority": priority, "dependencies": dependencies or [],
            "objective": "objective", "authorization": "authority", "deliverables": [],
            "completion_criteria": [], "escalation": "none", "active_execution_id": active
        }

    def test_selects_highest_priority_ready_item(self):
        items = [self.item("KE-EWP-002", priority=20), self.item("KE-EWP-001", priority=10)]
        _, manifest, queue = self.make_state(items)
        self.assertEqual(HARNESS.selectable(queue, manifest)[0]["id"], "KE-EWP-001")

    def test_unsatisfied_dependency_blocks_selection(self):
        items = [self.item("KE-EWP-001", status="Review"), self.item("KE-EWP-002", dependencies=["KE-EWP-001"])]
        _, manifest, queue = self.make_state(items)
        self.assertEqual(HARNESS.selectable(queue, manifest), [])

    def test_dependency_cycle_fails_validation(self):
        items = [self.item("KE-EWP-001", dependencies=["KE-EWP-002"]), self.item("KE-EWP-002", dependencies=["KE-EWP-001"])]
        root, _, _ = self.make_state(items)
        self.assertTrue(any("dependency cycle" in error for error in HARNESS.validate_state(root)))

    def test_duplicate_active_claim_fails_validation(self):
        expiry = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat().replace("+00:00", "Z")
        items = [self.item("KE-EWP-001", status="Active", active="KE-X-1")]
        base = {
            "work_id": "KE-EWP-001", "baseline_sha": "a" * 40, "lease_state": "Active",
            "lease_expiry": expiry, "status": "Executing", "gate_state": "Running", "merge_state": "NotReady",
            "checkpoint": None
        }
        executions = [dict(base, execution_id="KE-X-1"), dict(base, execution_id="KE-X-2")]
        root, _, _ = self.make_state(items, executions)
        self.assertTrue(any("multiple active write claims" in error for error in HARNESS.validate_state(root)))

    def test_expired_active_lease_requires_recovery(self):
        expiry = (datetime.now(timezone.utc) - timedelta(minutes=1)).isoformat().replace("+00:00", "Z")
        items = [self.item("KE-EWP-001", status="Active", active="KE-X-1")]
        executions = [{
            "execution_id": "KE-X-1", "work_id": "KE-EWP-001", "baseline_sha": "a" * 40,
            "lease_state": "Active", "lease_expiry": expiry, "status": "Executing",
            "gate_state": "Running", "merge_state": "NotReady", "checkpoint": None
        }]
        root, _, _ = self.make_state(items, executions)
        self.assertTrue(any("requires recovery" in error for error in HARNESS.validate_state(root)))

    def test_claim_checkpoint_release_lifecycle(self):
        items = [self.item("KE-EWP-001")]
        root, _, _ = self.make_state(items)
        manifest_path = root / "engineering-harness" / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["lease"] = {"default_minutes": 60, "maximum_minutes": 180}
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        self.bind_state(root)
        record = HARNESS.claim("KE-EWP-001", "test-agent", "a" * 40, "agent/test")
        HARNESS.checkpoint(record["execution_id"], "verified progress", "Pass", "Review", pr="#1")
        self.assertTrue((root / "engineering-harness" / "checkpoints" / f"{record['execution_id']}.json").is_file())
        released = HARNESS.release(record["execution_id"], "Review", "Review")
        self.assertEqual(released["lease_state"], "Released")
        self.assertEqual(HARNESS.validate_state(root), [])

    def test_recovery_requires_no_writer_confirmation(self):
        with self.assertRaisesRegex(ValueError, "no active writer"):
            HARNESS.recover("KE-X-missing", "agent", "a" * 40, "agent/recovery")

    def test_completed_execution_requires_merged_state(self):
        expiry = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat().replace("+00:00", "Z")
        items = [self.item("KE-EWP-001", status="Active", active="KE-X-1")]
        executions = [{
            "execution_id": "KE-X-1", "work_id": "KE-EWP-001", "baseline_sha": "a" * 40,
            "lease_state": "Active", "lease_expiry": expiry, "status": "Completed",
            "gate_state": "Pass", "merge_state": "NotReady", "checkpoint": None
        }]
        root, _, _ = self.make_state(items, executions)
        self.assertTrue(any("verified merge" in error for error in HARNESS.validate_state(root)))


if __name__ == "__main__":
    unittest.main()
