#!/usr/bin/env python3
import argparse
import contextlib
import fcntl
import json
import os
import re
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HARNESS = ROOT / "engineering-harness"
MANIFEST_PATH = HARNESS / "manifest.json"
QUEUE_PATH = HARNESS / "work-queue.json"
REGISTER_PATH = HARNESS / "execution-register.json"
LOCK_PATH = HARNESS / ".state.lock"

WORK_STATES = {"Backlog", "Ready", "Active", "Review", "Approved", "Blocked", "Paused", "Completed", "Archived"}
EXECUTION_STATES = {"Queued", "Claimed", "Executing", "Validating", "Review", "MergeReady", "Merging", "Completed", "Blocked", "Recoverable", "Abandoned"}
LEASE_STATES = {"Unclaimed", "Active", "Renewed", "Released", "Expired", "RecoveryPending"}
GATE_STATES = {"NotStarted", "Running", "Pass", "Fail", "Blocked"}
MERGE_STATES = {"NotApplicable", "NotReady", "Ready", "InProgress", "Merged", "Conflict", "Ambiguous"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def utcnow():
    return datetime.now(timezone.utc)


def iso(value):
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_json(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def atomic_write(path, data):
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


@contextlib.contextmanager
def state_lock():
    HARNESS.mkdir(parents=True, exist_ok=True)
    with LOCK_PATH.open("a+", encoding="utf-8") as stream:
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def validate_state(root=ROOT):
    harness = root / "engineering-harness"
    errors = []
    required = [harness / "manifest.json", harness / "work-queue.json", harness / "execution-register.json"]
    for path in required:
        if not path.is_file():
            errors.append(f"missing harness file: {path.relative_to(root)}")
    if errors:
        return errors

    manifest = load_json(required[0])
    queue = load_json(required[1])
    register = load_json(required[2])
    if manifest.get("schema_version") != "1.0" or queue.get("schema_version") != "1.0" or register.get("schema_version") != "1.0":
        errors.append("unsupported or inconsistent schema version")
    if manifest.get("executor_is_authority") is not False:
        errors.append("manifest must state executor_is_authority=false")
    if manifest.get("authoritative_branch") != "main":
        errors.append("authoritative branch must be main")

    items = queue.get("work_items")
    executions = register.get("executions")
    if not isinstance(items, list) or not isinstance(executions, list):
        return errors + ["work_items and executions must be arrays"]
    item_map = {}
    for item in items:
        work_id = item.get("id")
        if not work_id or work_id in item_map:
            errors.append(f"duplicate or missing work item id: {work_id}")
            continue
        item_map[work_id] = item
        if item.get("status") not in WORK_STATES:
            errors.append(f"{work_id}: invalid work status")
        if not isinstance(item.get("priority"), int):
            errors.append(f"{work_id}: priority must be an integer")
        if not isinstance(item.get("dependencies"), list):
            errors.append(f"{work_id}: dependencies must be an array")
        for field in ("objective", "authorization", "deliverables", "completion_criteria", "escalation"):
            if field not in item:
                errors.append(f"{work_id}: missing {field}")
    for work_id, item in item_map.items():
        for dependency in item.get("dependencies", []):
            if dependency not in item_map:
                errors.append(f"{work_id}: unknown dependency {dependency}")

    visiting, visited = set(), set()
    def visit(work_id):
        if work_id in visiting:
            errors.append(f"dependency cycle includes {work_id}")
            return
        if work_id in visited or work_id not in item_map:
            return
        visiting.add(work_id)
        for dependency in item_map[work_id].get("dependencies", []):
            visit(dependency)
        visiting.remove(work_id)
        visited.add(work_id)
    for work_id in item_map:
        visit(work_id)

    execution_ids = set()
    active_by_work = {}
    now = utcnow()
    for execution in executions:
        execution_id = execution.get("execution_id")
        work_id = execution.get("work_id")
        if not execution_id or execution_id in execution_ids:
            errors.append(f"duplicate or missing execution id: {execution_id}")
        execution_ids.add(execution_id)
        if work_id not in item_map:
            errors.append(f"{execution_id}: unknown work item {work_id}")
        if execution.get("status") not in EXECUTION_STATES:
            errors.append(f"{execution_id}: invalid execution status")
        if execution.get("lease_state") not in LEASE_STATES:
            errors.append(f"{execution_id}: invalid lease state")
        if execution.get("gate_state") not in GATE_STATES:
            errors.append(f"{execution_id}: invalid gate state")
        if execution.get("merge_state") not in MERGE_STATES:
            errors.append(f"{execution_id}: invalid merge state")
        if execution.get("status") == "MergeReady" and execution.get("gate_state") != "Pass":
            errors.append(f"{execution_id}: MergeReady requires passing gates")
        if execution.get("status") == "Completed" and execution.get("merge_state") != "Merged":
            errors.append(f"{execution_id}: Completed requires a verified merge")
        if not SHA_RE.fullmatch(execution.get("baseline_sha", "")):
            errors.append(f"{execution_id}: invalid baseline SHA")
        if execution.get("lease_state") in {"Active", "Renewed"}:
            active_by_work.setdefault(work_id, []).append(execution_id)
            try:
                if parse_time(execution["lease_expiry"]) <= now:
                    errors.append(f"{execution_id}: active lease is expired and requires recovery")
            except (KeyError, ValueError):
                errors.append(f"{execution_id}: invalid lease expiry")
        checkpoint = execution.get("checkpoint")
        if checkpoint and not (root / checkpoint).is_file():
            errors.append(f"{execution_id}: checkpoint does not exist: {checkpoint}")
    for work_id, claims in active_by_work.items():
        if len(claims) > 1:
            errors.append(f"{work_id}: multiple active write claims: {', '.join(claims)}")
        if item_map.get(work_id, {}).get("active_execution_id") not in claims:
            errors.append(f"{work_id}: queue and execution register active claim mismatch")
    for work_id, item in item_map.items():
        active = item.get("active_execution_id")
        if active and active not in active_by_work.get(work_id, []):
            errors.append(f"{work_id}: queue references a non-active execution")
    return sorted(set(errors))


def selectable(queue, manifest):
    satisfied = set(manifest["selection"]["dependency_satisfied_statuses"])
    item_map = {item["id"]: item for item in queue["work_items"]}
    ready = [
        item for item in queue["work_items"]
        if item["status"] == manifest["selection"]["eligible_status"]
        and item.get("active_execution_id") is None
        and all(item_map[dep]["status"] in satisfied for dep in item.get("dependencies", []))
    ]
    return sorted(ready, key=lambda item: (item["priority"], item["id"]))


def claim(work_id, agent, baseline_sha, branch, lease_minutes=None, lineage=None):
    if not SHA_RE.fullmatch(baseline_sha):
        raise ValueError("baseline SHA must contain 40 lowercase hexadecimal characters")
    with state_lock():
        errors = validate_state()
        if errors:
            raise ValueError("invalid harness state: " + "; ".join(errors))
        manifest, queue, register = load_json(MANIFEST_PATH), load_json(QUEUE_PATH), load_json(REGISTER_PATH)
        candidates = selectable(queue, manifest)
        if work_id is None:
            if not candidates:
                raise ValueError("no executable Ready work item")
            work_id = candidates[0]["id"]
        if work_id not in {item["id"] for item in candidates}:
            raise ValueError(f"{work_id} is not executable")
        minutes = lease_minutes or manifest["lease"]["default_minutes"]
        if minutes < 1 or minutes > manifest["lease"]["maximum_minutes"]:
            raise ValueError("lease duration is outside the manifest bounds")
        now = utcnow()
        execution_id = "KE-X-" + now.strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
        record = {
            "execution_id": execution_id,
            "work_id": work_id,
            "agent": agent,
            "baseline_sha": baseline_sha,
            "branch": branch,
            "pr": null_value(),
            "lease_state": "Active",
            "lease_start": iso(now),
            "lease_expiry": iso(now + timedelta(minutes=minutes)),
            "checkpoint": null_value(),
            "gate_state": "NotStarted",
            "merge_state": "NotReady",
            "last_authority_sha": baseline_sha,
            "status": "Claimed",
            "escalation": null_value(),
            "lineage": lineage
        }
        register["executions"].append(record)
        register["updated_at"] = iso(now)
        for item in queue["work_items"]:
            if item["id"] == work_id:
                item["status"] = "Active"
                item["active_execution_id"] = execution_id
        queue["updated_at"] = iso(now)
        atomic_write(REGISTER_PATH, register)
        atomic_write(QUEUE_PATH, queue)
        return record


def null_value():
    return None


def checkpoint(execution_id, summary, gate_state, status, pr=None, escalation=None):
    if gate_state not in GATE_STATES or status not in EXECUTION_STATES:
        raise ValueError("invalid checkpoint gate or execution state")
    with state_lock():
        register = load_json(REGISTER_PATH)
        record = next((entry for entry in register["executions"] if entry["execution_id"] == execution_id), None)
        if not record:
            raise ValueError("execution not found")
        if record["lease_state"] not in {"Active", "Renewed"}:
            raise ValueError("execution does not own an active lease")
        path = HARNESS / "checkpoints" / f"{execution_id}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": "1.0", "execution_id": execution_id, "work_id": record["work_id"],
            "recorded_at": iso(utcnow()), "baseline_sha": record["baseline_sha"], "branch": record["branch"],
            "pr": pr or record.get("pr"), "summary": summary, "gate_state": gate_state,
            "status": status, "escalation": escalation
        }
        atomic_write(path, payload)
        record.update({"checkpoint": str(path.relative_to(ROOT)), "gate_state": gate_state, "status": status, "pr": pr or record.get("pr"), "escalation": escalation})
        register["updated_at"] = iso(utcnow())
        atomic_write(REGISTER_PATH, register)
        return payload


def renew(execution_id, minutes=None):
    with state_lock():
        manifest, register = load_json(MANIFEST_PATH), load_json(REGISTER_PATH)
        record = next((entry for entry in register["executions"] if entry["execution_id"] == execution_id), None)
        if not record or record["lease_state"] not in {"Active", "Renewed"}:
            raise ValueError("only the active execution may renew its lease")
        duration = minutes or manifest["lease"]["default_minutes"]
        if duration < 1 or duration > manifest["lease"]["maximum_minutes"]:
            raise ValueError("lease duration is outside the manifest bounds")
        record["lease_state"] = "Renewed"
        record["lease_expiry"] = iso(utcnow() + timedelta(minutes=duration))
        register["updated_at"] = iso(utcnow())
        atomic_write(REGISTER_PATH, register)
        return record


def release(execution_id, work_status, execution_status, escalation=None):
    if work_status not in WORK_STATES or execution_status not in EXECUTION_STATES:
        raise ValueError("invalid release state")
    if work_status == "Completed" or execution_status == "Completed":
        raise ValueError("use reconcile after verified merge to record completion")
    with state_lock():
        queue, register = load_json(QUEUE_PATH), load_json(REGISTER_PATH)
        record = next((entry for entry in register["executions"] if entry["execution_id"] == execution_id), None)
        if not record:
            raise ValueError("execution not found")
        if record["lease_state"] not in {"Active", "Renewed"}:
            raise ValueError("execution does not own an active lease")
        record.update({"lease_state": "Released", "status": execution_status, "escalation": escalation})
        for item in queue["work_items"]:
            if item["id"] == record["work_id"]:
                if item.get("active_execution_id") != execution_id:
                    raise ValueError("queue claim does not match execution")
                item["active_execution_id"] = None
                item["status"] = work_status
                item["escalation"] = escalation or item.get("escalation")
        now = iso(utcnow())
        queue["updated_at"] = register["updated_at"] = now
        atomic_write(REGISTER_PATH, register)
        atomic_write(QUEUE_PATH, queue)
        return record


def recover(execution_id, agent, baseline_sha, branch, lease_minutes=None, confirm_no_active_writer=False):
    if not confirm_no_active_writer:
        raise ValueError("recovery requires explicit verification that no active writer exists")
    with state_lock():
        register = load_json(REGISTER_PATH)
        old = next((entry for entry in register["executions"] if entry["execution_id"] == execution_id), None)
        if not old:
            raise ValueError("execution not found")
        if old["lease_state"] not in {"Active", "Renewed", "Expired", "RecoveryPending"}:
            raise ValueError("execution is not recoverable")
        if old["lease_state"] in {"Active", "Renewed"} and parse_time(old["lease_expiry"]) > utcnow():
            raise ValueError("active lease has not expired")
        old["lease_state"] = "Expired"
        old["status"] = "Recoverable"
        register["updated_at"] = iso(utcnow())
        atomic_write(REGISTER_PATH, register)
        queue = load_json(QUEUE_PATH)
        for item in queue["work_items"]:
            if item["id"] == old["work_id"]:
                item["active_execution_id"] = None
                item["status"] = "Ready"
        queue["updated_at"] = iso(utcnow())
        atomic_write(QUEUE_PATH, queue)
    return claim(old["work_id"], agent, baseline_sha, branch, lease_minutes, lineage=execution_id)


def reconcile(execution_id, pr, merge_sha, authority_sha):
    if not SHA_RE.fullmatch(merge_sha) or not SHA_RE.fullmatch(authority_sha):
        raise ValueError("merge and authority SHAs must be 40 lowercase hexadecimal characters")
    if merge_sha != authority_sha:
        raise ValueError("post-merge authority SHA must equal the verified merge SHA")
    with state_lock():
        queue, register = load_json(QUEUE_PATH), load_json(REGISTER_PATH)
        record = next((entry for entry in register["executions"] if entry["execution_id"] == execution_id), None)
        if not record:
            raise ValueError("execution not found")
        if record.get("gate_state") != "Pass" or record.get("status") not in {"Review", "MergeReady", "Merging"}:
            raise ValueError("execution is not eligible for completion reconciliation")
        record.update({
            "pr": pr, "lease_state": "Released", "merge_state": "Merged", "status": "Completed",
            "last_authority_sha": authority_sha, "escalation": None
        })
        for item in queue["work_items"]:
            if item["id"] == record["work_id"]:
                if item.get("active_execution_id") not in {None, execution_id}:
                    raise ValueError("queue is owned by another execution")
                item["active_execution_id"] = None
                item["status"] = "Completed"
                item["escalation"] = "None; completion reconciled to authoritative main"
        now = iso(utcnow())
        queue["updated_at"] = register["updated_at"] = now
        atomic_write(REGISTER_PATH, register)
        atomic_write(QUEUE_PATH, queue)
        return record


def command_status():
    manifest, queue, register = load_json(MANIFEST_PATH), load_json(QUEUE_PATH), load_json(REGISTER_PATH)
    selected = selectable(queue, manifest)
    return {
        "valid": not validate_state(),
        "work_status_counts": {state: sum(item["status"] == state for item in queue["work_items"]) for state in sorted(WORK_STATES)},
        "active_executions": [entry["execution_id"] for entry in register["executions"] if entry["lease_state"] in {"Active", "Renewed"}],
        "next_executable": selected[0]["id"] if selected else None
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="KE autonomous engineering harness")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    commands.add_parser("status")
    commands.add_parser("select")
    claim_parser = commands.add_parser("claim")
    claim_parser.add_argument("--work-id")
    claim_parser.add_argument("--agent", required=True)
    claim_parser.add_argument("--baseline-sha", required=True)
    claim_parser.add_argument("--branch", required=True)
    claim_parser.add_argument("--lease-minutes", type=int)
    checkpoint_parser = commands.add_parser("checkpoint")
    checkpoint_parser.add_argument("--execution-id", required=True)
    checkpoint_parser.add_argument("--summary", required=True)
    checkpoint_parser.add_argument("--gate-state", choices=sorted(GATE_STATES), default="Running")
    checkpoint_parser.add_argument("--status", choices=sorted(EXECUTION_STATES), default="Executing")
    checkpoint_parser.add_argument("--pr")
    checkpoint_parser.add_argument("--escalation")
    renew_parser = commands.add_parser("renew")
    renew_parser.add_argument("--execution-id", required=True)
    renew_parser.add_argument("--lease-minutes", type=int)
    release_parser = commands.add_parser("release")
    release_parser.add_argument("--execution-id", required=True)
    release_parser.add_argument("--work-status", choices=sorted(WORK_STATES), required=True)
    release_parser.add_argument("--execution-status", choices=sorted(EXECUTION_STATES), default="Review")
    release_parser.add_argument("--escalation")
    recover_parser = commands.add_parser("recover")
    recover_parser.add_argument("--execution-id", required=True)
    recover_parser.add_argument("--agent", required=True)
    recover_parser.add_argument("--baseline-sha", required=True)
    recover_parser.add_argument("--branch", required=True)
    recover_parser.add_argument("--lease-minutes", type=int)
    recover_parser.add_argument("--confirm-no-active-writer", action="store_true")
    reconcile_parser = commands.add_parser("reconcile")
    reconcile_parser.add_argument("--execution-id", required=True)
    reconcile_parser.add_argument("--pr", required=True)
    reconcile_parser.add_argument("--merge-sha", required=True)
    reconcile_parser.add_argument("--authority-sha", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            errors = validate_state()
            result = {"valid": not errors, "errors": errors}
            print(json.dumps(result, indent=2))
            return 0 if not errors else 1
        if args.command == "status":
            print(json.dumps(command_status(), indent=2)); return 0
        if args.command == "select":
            queue, manifest = load_json(QUEUE_PATH), load_json(MANIFEST_PATH)
            selected = selectable(queue, manifest)
            print(json.dumps({"selected": selected[0] if selected else None}, indent=2)); return 0
        if args.command == "claim":
            result = claim(args.work_id, args.agent, args.baseline_sha, args.branch, args.lease_minutes)
        elif args.command == "checkpoint":
            result = checkpoint(args.execution_id, args.summary, args.gate_state, args.status, args.pr, args.escalation)
        elif args.command == "renew":
            result = renew(args.execution_id, args.lease_minutes)
        elif args.command == "release":
            result = release(args.execution_id, args.work_status, args.execution_status, args.escalation)
        elif args.command == "recover":
            result = recover(
                args.execution_id, args.agent, args.baseline_sha, args.branch,
                args.lease_minutes, args.confirm_no_active_writer
            )
        else:
            result = reconcile(args.execution_id, args.pr, args.merge_sha, args.authority_sha)
        print(json.dumps(result, indent=2)); return 0
    except (ValueError, OSError, json.JSONDecodeError) as error:
        print(json.dumps({"error": str(error)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
