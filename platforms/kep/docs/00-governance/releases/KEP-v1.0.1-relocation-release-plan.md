# KEP v1.0.1 — Relocation Release Plan

## Control

| Field | Value |
|---|---|
| Artifact Class | Release plan; non-normative |
| Status | Approved; Release Candidate Package Completed |
| Date | 2026-07-29 |
| Owner | KEP Platform Release Authority |
| Proposed Release | KEP Framework v1.0.1 |
| Proposed Canonical Location | `kashifyounus/Kuriosity-Ecosystem` at `platforms/kep/` |

## 1. Purpose

Provide the controlled successor-release path for moving the product-adoptable KEP baseline from its historical standalone repository into the KE repository.

## 2. Historical Integrity

KEP v1.0.0 retains the repository coordinates approved by its original release declaration and manifest. Migration does not amend v1.0.0.

## 3. Approved v1.0.1 Scope

The successor release:

- preserves the normative meaning and inventory of KEP v1.0.0;
- establishes the KE repository and `platforms/kep/` as successor canonical coordinates;
- records the relationship to superior KE authority without transferring product-domain authority;
- includes migration parity, secondary validation, and relocation verification evidence;
- provides explicit upgrade and rollback guidance; and
- preserves the standalone repository as historical release evidence.

## 4. Gate Status

| Gate | Status |
|---|---|
| Private founding repositories | Approved; administrative execution not yet verified |
| SNS_GATEWAY secondary validation context | Completed; Pass |
| KE-001 through KE-004 ratification | Completed; Version 1.0 effective 2026-07-29 |
| KEP authority within KE | Reconciled by ratified KE-004 and this approved relocation scope |
| Release declaration and manifest | Prepared as approved release candidates |
| Publication approval record | Prepared; conditional approval |
| Relocation verification | Conditional Pass |
| Upgrade and rollback guidance | Prepared; approved candidate guidance |
| Destination `main` publication | Pending merge |
| Post-merge verification | Pending merge |

## 5. Release Artifacts

- `KEP-v1.0.1-release-declaration.md`;
- `KEP-v1.0.1-release-manifest.md`;
- `../approvals/KEP-v1.0.1-publication-approval-record.md`;
- `../verification/KEP-v1.0.1-relocation-verification.md`;
- `../verification/KEP-v1.0.1-SNS_GATEWAY-secondary-context-validation.md`;
- `KEP-v1.0.1-upgrade-and-rollback-guidance.md`.

## 6. Remaining Boundary

Products shall not claim adoption of KEP v1.0.1 until privacy, merge, and post-merge gates pass and the declaration and manifest are recorded effective. The standalone v1.0.0 repository shall not be deleted.
