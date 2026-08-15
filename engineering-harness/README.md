# KE Autonomous Engineering Harness

This directory contains operational, machine-readable projections for bounded autonomous execution. It does not contain superior governance and cannot override the current KE release.

## Files

- `manifest.json` — execution, selection, lease, stop, merge, recovery, and cost contract.
- `work-queue.json` — dependency-aware KE Engineering Work Packages (EWPs).
- `execution-register.json` — claims, leases, checkpoints, gates, merges, lineage, and escalation.

## Commands

```text
python tools/ke_harness.py validate
python tools/ke_harness.py status
python tools/ke_harness.py select
python tools/ke_harness.py claim --agent <agent> --baseline-sha <sha> --branch <branch>
python tools/ke_harness.py checkpoint --execution-id <id> --summary <text>
python tools/ke_harness.py renew --execution-id <id>
python tools/ke_harness.py release --execution-id <id> --work-status Review
python tools/ke_harness.py recover --execution-id <expired-id> --agent <agent> --baseline-sha <sha> --branch <branch> --confirm-no-active-writer
python tools/ke_harness.py reconcile --execution-id <id> --pr <url> --merge-sha <sha> --authority-sha <sha>
```

The CLI writes state atomically under a local process lock. Repository branches and pull requests provide cross-machine serialization. Before any merge, the executor must re-read GitHub state, required checks, reviews, threads, dependencies, PR head, and base divergence.

The initial PR is a bootstrap operation because the harness did not exist before its creation. It is recorded in `KE-PLAN-001`; no retrospective lease is fabricated.
