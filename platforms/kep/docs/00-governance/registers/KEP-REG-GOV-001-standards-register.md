# KEP-REG-GOV-001 — Standards Register

| Register Control | Value |
| --- | --- |
| Register ID | KEP-REG-GOV-001 |
| Title | Standards Register |
| Artifact Class | Register |
| Status | Active |
| Governing Standard | KEP-GOV-002 — Standards Taxonomy and Naming Standard |
| Accountable Owner | Governance Steward |
| Canonical Representation | This Markdown file |
| Last Updated | July 25, 2026 |

This register records KEP subordinate-standard identity and lifecycle state. It does not independently approve or make a standard effective.

## Standards Register

| Identifier | Title | Domain | Artifact Class | Status | Version | Owner | Approval Authority | Effective Date | Canonical Path | Supersession | Deferred-Decision Dependencies | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KEP-GOV-002 | Standards Taxonomy and Naming Standard | GOV | Subordinate standard | Effective | 1.0 | Governance Steward | Founding Authority | July 25, 2026 | `docs/00-governance/standards/KEP-GOV-002-standards-taxonomy-and-naming-standard.md` | None | None | Approved and effective. |
| KEP-PO-001 | Product Owner Interaction Standard | PO | Subordinate standard | Effective | 1.0 | Governance Steward | Founding Authority | July 25, 2026 | `docs/00-governance/standards/KEP-PO-001-product-owner-interaction-standard.md` | None | UD-014 may affect later appeal and conflict procedures | Approved by Founding Authority. Approval record: `docs/00-governance/approvals/KEP-PO-001-v1.0-approval-record.md`. Traceability verified; canonical metadata synchronized. |
| KEP-REV-001 | Engineering Review Standard | REV | Subordinate standard | Effective | 1.0 | Governance Steward | Founding Authority | July 25, 2026 | `docs/00-governance/standards/KEP-REV-001-engineering-review-standard.md` | None | UD-009, UD-010, UD-011, UD-014 | Approved by Founding Authority. Approval record: `docs/00-governance/approvals/KEP-REV-001-v1.0-approval-record.md`. Canonical metadata synchronized. |
| KEP-COM-001 | Engineering Communication Standard | COM | Subordinate standard | Effective | 1.0 | Governance Steward | Founding Authority | July 25, 2026 | `docs/00-governance/standards/KEP-COM-001-engineering-communication-standard.md` | None | UD-010 may affect retention of intermediate AI records | Approved by Founding Authority. Approval record: `docs/00-governance/approvals/KEP-COM-001-v1.0-approval-record.md`. Canonical metadata synchronized. Coordinated review completed. |

## Legacy Identifier Register

| Identifier | Title | Actual Artifact Class | Current Status | Legacy Condition | Migration Status |
| --- | --- | --- | --- | --- | --- |
| KEP-GOV-001 | Governance Baseline Audit | Audit; non-normative | Final audit report; findings open | Identifier predates KEP-GOV-002 and uses the GOV standard-style namespace for an audit | Retained as an approved legacy identifier exception; no migration authorized |

## Package Evidence

- Coordinated review: `docs/00-governance/reviews/KEP-RPT-GOV-001-coordinated-standards-consistency-review.md`
- Completion report: `docs/00-governance/reports/KEP-RPT-GOV-002-governance-package-implementation-completion-report.md`

## Change History

| Date | Change | Authority Basis |
| --- | --- | --- |
| July 25, 2026 | Created register; entered KEP-GOV-002 as Effective; entered KEP-PO-001 as Draft; reserved KEP-REV-001 and KEP-COM-001; recorded KEP-GOV-001 legacy exception. | KEP-GOV-002 Version 1.0 approval and implementation requirements |
| July 25, 2026 | Updated KEP-PO-001 from Draft to Effective; recorded its approval record and traceability verification; advanced KEP-REV-001 from Reserved to Draft. | Founding Authority approval of KEP-PO-001 Version 1.0 and approved implementation sequence |
| July 25, 2026 | Updated KEP-REV-001 from Draft to Effective; recorded its approval record and metadata synchronization; advanced KEP-COM-001 from Reserved to Draft. | Founding Authority approval of KEP-REV-001 Version 1.0 and approved implementation sequence |
| July 25, 2026 | Updated KEP-COM-001 from Draft to Effective and recorded its approval record. | Founding Authority approval of KEP-COM-001 Version 1.0 |
| July 25, 2026 | Recorded canonical metadata synchronization for KEP-PO-001 and KEP-COM-001; linked coordinated review and package completion evidence. | Approved coordinated review and implementation-completion instruction |
