# KEP Framework v1.0.1 — Authoritative Release Manifest

## Manifest Control

| Field | Value |
|---|---|
| Release | KEP Framework v1.0.1 |
| Manifest Status | Approved Release Candidate |
| Release Status | Not Yet Effective |
| Approval Date | 2026-07-29 |
| Canonical Repository | `kashifyounus/Kuriosity-Ecosystem` |
| Canonical Platform Root | `platforms/kep/` |
| Authoritative Branch | `main` |
| Contractual Adoption Identifier | `v1.0.1` after effectiveness |
| Prior Release | KEP Framework v1.0.0 |

## 1. Manifest Authority

Upon release effectiveness, this manifest is the complete repository-controlled definition of KEP Framework v1.0.1.

Until then, it is an approved release candidate and shall not be represented as product-adoptable.

## 2. Normative Governance Baseline

All paths are relative to `platforms/kep/`.

| Identifier | Title | Version | Lifecycle State | Canonical Path |
|---|---|---:|---|---|
| KEP-000 | Founding Charter | 1.0 | Foundational; Effective | `docs/00-governance/KEP-000-founding-charter.md` |
| KEP-001 | Platform Scope, Boundaries, and Operating Model | 1.0 | Ratified; Effective | `docs/00-governance/KEP-001-platform-scope-boundaries-operating-model.md` |
| KEP-001A | Founding Decisions and Ratification Record | 1.0 | Ratified; Effective | `docs/00-governance/KEP-001A-founding-decisions-ratification-record.md` |
| KEP-002 | Engineering Constitution | 1.0 | Ratified; Effective | `docs/00-governance/KEP-002-engineering-constitution.md` |
| KEP-GOV-002 | Standards Taxonomy and Naming Standard | 1.0 | Effective | `docs/00-governance/standards/KEP-GOV-002-standards-taxonomy-and-naming-standard.md` |
| KEP-PO-001 | Product Owner Interaction Standard | 1.0 | Effective | `docs/00-governance/standards/KEP-PO-001-product-owner-interaction-standard.md` |
| KEP-REV-001 | Engineering Review Standard | 1.0 | Effective | `docs/00-governance/standards/KEP-REV-001-engineering-review-standard.md` |
| KEP-COM-001 | Engineering Communication Standard | 1.0 | Effective | `docs/00-governance/standards/KEP-COM-001-engineering-communication-standard.md` |

The inventory and normative meaning are unchanged from v1.0.0.

## 3. Release Evidence

All paths are repository-root relative.

| Artifact | State | Path |
|---|---|---|
| v1.0.1 Release Declaration | Approved Release Candidate | `platforms/kep/docs/00-governance/releases/KEP-v1.0.1-release-declaration.md` |
| v1.0.1 Manifest | Approved Release Candidate | `platforms/kep/docs/00-governance/releases/KEP-v1.0.1-release-manifest.md` |
| Publication Approval Record | Conditional Approval | `platforms/kep/docs/00-governance/approvals/KEP-v1.0.1-publication-approval-record.md` |
| Relocation Verification | Conditional Pass | `platforms/kep/docs/00-governance/verification/KEP-v1.0.1-relocation-verification.md` |
| SNS_GATEWAY Secondary Validation | Final; Pass | `platforms/kep/docs/00-governance/verification/KEP-v1.0.1-SNS_GATEWAY-secondary-context-validation.md` |
| Upgrade and Rollback Guidance | Approved | `platforms/kep/docs/00-governance/releases/KEP-v1.0.1-upgrade-and-rollback-guidance.md` |

## 4. Adoption Coordinates

After effectiveness, a product adoption contract shall use:

| Coordinate | Required Value |
|---|---|
| Framework | Kuriosity Engineering Platform |
| Canonical Repository | `kashifyounus/Kuriosity-Ecosystem` |
| Platform Root | `platforms/kep/` |
| Adopted Release | `v1.0.1` |
| Manifest | `platforms/kep/docs/00-governance/releases/KEP-v1.0.1-release-manifest.md` |
| Standards | Explicit identifiers and versions selected from Section 2 |
| Deviations | Explicitly approved and product-controlled |
| Upgrade | Controlled product decision |
| Rollback | Controlled reversion under the approved guidance |

## 5. Exclusions

v1.0.1 does not:

- change the normative meaning or version of any v1.0.0 instrument;
- change product-domain authority;
- automatically upgrade any adopting product;
- delete, archive, or rewrite the standalone v1.0.0 repository;
- approve deferred KEP-001A decisions UD-008 through UD-015; or
- become effective merely because candidate files exist on a publication branch.

## 6. Change Control

Any later change to normative inventory, document version, lifecycle state, or adoption coordinates requires a controlled successor release. Silent mutation is prohibited.
