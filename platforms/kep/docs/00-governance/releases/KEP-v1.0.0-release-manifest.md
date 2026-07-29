# KEP Framework v1.0.0 — Authoritative Release Manifest

| Manifest Control | Value |
| --- | --- |
| Release | KEP Framework v1.0.0 |
| Manifest Status | Authoritative |
| Release Status | Published and Effective |
| Publication Date | July 25, 2026 |
| Canonical Repository | `kashifyounus/kuriosity-engineering-platform` |
| Authoritative Branch | `main` |
| Release Declaration | `docs/00-governance/releases/KEP-v1.0.0-release-declaration.md` |
| Contractual Adoption Identifier | `v1.0.0` |
| Prior Release | None |

## 1. Manifest Authority

This manifest is the complete repository-controlled definition of KEP Framework v1.0.0.

Only artifacts listed in this manifest are part of the release baseline. Repository commits provide implementation evidence. Git tags, GitHub Releases, rendered copies, archives, and conversation context are not required to identify, interpret, or adopt this release.

## 2. Normative Governance Baseline

| Identifier | Title | Version | Lifecycle State | Canonical Path |
| --- | --- | ---: | --- | --- |
| KEP-000 | Founding Charter | 1.0 | Foundational; Effective | `docs/00-governance/KEP-000-founding-charter.md` |
| KEP-001 | Platform Scope, Boundaries, and Operating Model | 1.0 | Ratified; Effective | `docs/00-governance/KEP-001-platform-scope-boundaries-operating-model.md` |
| KEP-001A | Founding Decisions and Ratification Record | 1.0 | Ratified; Effective | `docs/00-governance/KEP-001A-founding-decisions-ratification-record.md` |
| KEP-002 | Engineering Constitution | 1.0 | Ratified; Effective | `docs/00-governance/KEP-002-engineering-constitution.md` |
| KEP-GOV-002 | Standards Taxonomy and Naming Standard | 1.0 | Effective | `docs/00-governance/standards/KEP-GOV-002-standards-taxonomy-and-naming-standard.md` |
| KEP-PO-001 | Product Owner Interaction Standard | 1.0 | Effective | `docs/00-governance/standards/KEP-PO-001-product-owner-interaction-standard.md` |
| KEP-REV-001 | Engineering Review Standard | 1.0 | Effective | `docs/00-governance/standards/KEP-REV-001-engineering-review-standard.md` |
| KEP-COM-001 | Engineering Communication Standard | 1.0 | Effective | `docs/00-governance/standards/KEP-COM-001-engineering-communication-standard.md` |

These eight instruments form the complete normative governance baseline for v1.0.0. No draft, reserved, proposed, or future standard is included.

## 3. Approval and Lifecycle Evidence

| Artifact | Status | Path |
| --- | --- | --- |
| KEP-GOV-002 Version 1.0 Approval Record | Final | `docs/00-governance/approvals/KEP-GOV-002-v1.0-approval-record.md` |
| KEP-PO-001 Version 1.0 Approval Record | Final | `docs/00-governance/approvals/KEP-PO-001-v1.0-approval-record.md` |
| KEP-REV-001 Version 1.0 Approval Record | Final | `docs/00-governance/approvals/KEP-REV-001-v1.0-approval-record.md` |
| KEP-COM-001 Version 1.0 Approval Record | Final | `docs/00-governance/approvals/KEP-COM-001-v1.0-approval-record.md` |
| Standards Register | Active | `docs/00-governance/registers/KEP-REG-GOV-001-standards-register.md` |
| Product Owner Standard Traceability Verification | Final | `docs/00-governance/verification/KEP-PO-001-v1.0-clause-traceability-verification.md` |
| Coordinated Standards Consistency Review | Final; Approved | `docs/00-governance/reviews/KEP-RPT-GOV-001-coordinated-standards-consistency-review.md` |
| Governance Package Implementation Completion Report | Final | `docs/00-governance/reports/KEP-RPT-GOV-002-governance-package-implementation-completion-report.md` |

## 4. Release Publication Artifacts

| Artifact | Status | Path |
| --- | --- | --- |
| v1.0.0 Release Declaration | Published | `docs/00-governance/releases/KEP-v1.0.0-release-declaration.md` |
| v1.0.0 Release Manifest | Authoritative | `docs/00-governance/releases/KEP-v1.0.0-release-manifest.md` |
| v1.0.0 Publication Approval Record | Final | `docs/00-governance/approvals/KEP-v1.0.0-publication-approval-record.md` |
| v1.0.0 Product-Adoption Verification | Final | `docs/00-governance/verification/KEP-v1.0.0-product-adoption-verification.md` |

README and AGENTS.md provide repository discovery and operating guidance. They do not add normative release contents and do not replace any artifact listed above.

## 5. KEP-002 Ratification Record Resolution

KEP-002 Version 1.0 contains its ratification record within the canonical document under **Section 21 — Ratification Record**. There is no separate `KEP-002A-constitutional-ratification-record.md` artifact in v1.0.0.

The former README reference to KEP-002A was a repository scaffolding expectation created before authoritative KEP-002 text was available. It is corrected by this publication and has no normative or supersession effect.

## 6. Product Adoption Coordinates

A product adoption contract shall use all of the following coordinates:

| Coordinate | Required Value |
| --- | --- |
| Framework | Kuriosity Engineering Platform |
| Canonical Repository | `kashifyounus/kuriosity-engineering-platform` |
| Adopted Release | `v1.0.0` |
| Manifest | `docs/00-governance/releases/KEP-v1.0.0-release-manifest.md` |
| Standards | Explicit identifiers and versions selected from Section 2 |
| Deviations | Explicitly approved and locally recorded |
| Upgrade | Controlled product decision; no automatic tracking of `main` |
| Rollback | Controlled reversion to the product's previously adopted release or pre-adoption state |

A commit SHA may be retained as adoption implementation evidence, but it shall not replace `v1.0.0` as the adopted release identifier.

## 7. Exclusions

The following are not part of v1.0.0:

- KEP-GOV-001 Governance Baseline Audit, which remains a non-normative legacy-identifier audit artifact.
- Draft, reserved, proposed, or unapproved standards.
- Deferred decisions UD-008 through UD-015 except as preserved boundaries in approved instruments.
- Product-specific requirements, architecture, code, data, or operating procedures.
- Templates, schemas, automation, CI enforcement, evidence stores, or agent-execution logging not separately approved.
- Git tags and GitHub Releases as sources of governance authority.
- Ratified DOCX renditions as independent normative instruments; the canonical Markdown paths in Section 2 control human-readable adoption.

## 8. Change Control

Any change to the normative inventory, document version, lifecycle state, or adoption coordinates requires a new controlled release manifest or an approved successor release. Silent mutation of this manifest is prohibited.

Editorial corrections that do not alter release identity or normative meaning shall be recorded through normal repository evidence and must not be represented as a new release.
