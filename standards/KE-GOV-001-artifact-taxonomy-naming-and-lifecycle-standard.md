# KE-GOV-001 — Artifact Taxonomy, Naming, Metadata, and Lifecycle Standard

| Field | Value |
|---|---|
| Identifier | KE-GOV-001 |
| Title | Artifact Taxonomy, Naming, Metadata, and Lifecycle Standard |
| Artifact Type | Standard |
| Version | 2.0 |
| Lifecycle Status | Effective |
| Approval Status | Approved |
| Verification Status | Pass |
| Authority | KE-005 through KE-007 |
| Owner | Ecosystem Governance Authority |
| Effective Date | 2026-07-29 |
| Scope | KE artifact identifiers, canonical metadata, lifecycle, naming, authority, and duplication control |
| Amendment Path | KE-007 |
| Supersession State | Current; supersedes KE-GOV-001 Version 1.0 |

## 1. Identifier Model

Normative KE artifacts use `KE-{DOMAIN}-{NNN}` or reserved foundation identifiers `KE-000` through `KE-999`.

| Domain | Use |
|---|---|
| GOV | Governance and artifact control standards |
| PO | Product Owner interaction |
| REV | Review and verification |
| COM | Engineering communication |
| SEC | Security |
| DATA | Data |
| ARCH | Architecture |
| REL | Release |
| AI | AI engineering |

Registers use `KE-REG-NNN`, reports `KE-RPT-NNN`, plans `KE-PLAN-NNN`, decisions `KE-ADR-NNN`, approvals `KE-APR-NNN`, exceptions `KE-EXC-NNN`, and history records `KE-HIST-NNN`.

## 2. Canonical Metadata

Every normative artifact shall declare these fields independently:

- Identifier
- Title
- Artifact Type
- Version
- Lifecycle Status
- Approval Status
- Verification Status
- Authority
- Owner
- Effective Date
- Scope
- Amendment Path
- Supersession State

A field shall not combine lifecycle, approval, verification, or effectiveness outcomes. `Not Applicable` or `Pending` shall be used only where truthful and permitted by the controlling process.

## 3. Lifecycle and Outcomes

Allowed lifecycle states are `Draft`, `Proposed`, `Review Required`, `Effective`, `Deprecated`, `Superseded`, `Retired`, and `Archived`.

Allowed approval outcomes are `Pending`, `Approved`, `Ratified`, `Rejected`, and `Not Applicable`.

Allowed verification outcomes are `Not Reviewed`, `Pass`, `Pass with Conditions`, `Fail`, `Blocked`, and `Not Applicable`.

Only an Effective artifact with Approved or Ratified approval status may create obligations within its stated authority. A Proposed or Review Required artifact remains non-normative even when its approval decision has been recorded.

## 4. Naming

Paths and filenames shall be lowercase kebab case except approved acronyms in document identifiers. Names shall be stable, descriptive, and unique. A renamed or moved authority shall retain traceability through its register and revision history.

## 5. Authority

Every artifact shall identify its governing authority and shall not claim a level above that authority. Templates, reports, plans, registers, and historical evidence are non-normative unless expressly incorporated by an Effective instrument.

## 6. Duplication

One normative topic shall have one canonical source. A new artifact requires evidence that extension of an existing artifact would reduce clarity or violate authority boundaries.

## 7. Approval

Version 2.0 approved by the Kuriosity Ecosystem Founding Authority on 2026-07-29 through KE-APR-003.
