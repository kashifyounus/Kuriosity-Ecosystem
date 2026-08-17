# KE Repository Agent Instructions

## Authority

Repository-controlled KE authority governs every agent. Read in this order before material work:

1. `governance/constitution/KE-000-kuriosity-ecosystem-constitution.md`
2. `governance/charter/KE-001-kuriosity-ecosystem-founding-charter.md`
3. `governance/operating-model/KE-002-kuriosity-ecosystem-operating-model.md`
4. `governance/authority/KE-003-ecosystem-authority-and-responsibility-model.md`
5. applicable KE governance, standards, decisions, and the current release manifest
6. `engineering-harness/manifest.json`
7. `engineering-harness/work-queue.json`
8. `engineering-harness/execution-register.json` and the latest checkpoint for the claimed work

Conversation, memory, automation output, repository proximity, and implementation precedent do not create authority.

## Autonomous Workflow

Use this sequence for released work:

`READ -> RECONCILE -> SELECT -> CLAIM -> IMPLEMENT -> VALIDATE -> FIX/RETEST -> CHECKPOINT -> PR -> STOP`

- Synchronize authoritative `main` and record its SHA before claiming work.
- Select only a `Ready` work item whose hard dependencies are satisfied.
- Use `python tools/ke_harness.py claim` before the first write.
- Work only within the claimed scope and branch.
- Run the KE repository validator, harness validator, and applicable tests.
- Checkpoint material progress and blockers in repository state.
- Create or update one reviewable PR for the claimed tranche.
- Stop at human-reserved approval or merge gates.

## Allowed Autonomous Actions

Within an authorized work item, agents may inspect, analyze, draft, implement, test, repair deterministic failures, update non-normative operational projections, and prepare review evidence.

## Mandatory Stop and Escalation

Stop affected writes and record the exact decision required when work would:

- change constitutional or normative meaning, lifecycle, approval, or effective status;
- admit, activate, release, deprecate, or retire a platform;
- invent a product, platform mandate, requirement, accountable owner, legal conclusion, or material evidence;
- make an unresolved R3/R4 architecture, security, data, AI, compliance, or residual-risk decision;
- perform a destructive or irreversible migration;
- broaden the released work-package scope;
- resolve conflicting authority by implementation;
- retry an ambiguous merge or bypass a required gate; or
- merge to authoritative `main` without explicit competent authority.

## Integrity Rules

- The harness is an executor, never an authority.
- One active write lease is permitted per work item.
- A stale baseline requires reconciliation before continued writes.
- Claims, checkpoints, PRs, gates, merges, and post-merge authority must be reconstructable.
- Deterministic checks take precedence over repeated AI interpretation.
- Metro-X Precision is excluded from the current KE product-conformance workstream.
- Product business knowledge remains in product repositories.

Completion means the bounded deliverables, tests, evidence, checkpoint, commit, and PR are ready for the next authorized gate. It does not imply approval, release, admission, or merge.
