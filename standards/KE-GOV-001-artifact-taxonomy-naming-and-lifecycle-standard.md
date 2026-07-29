# KE-GOV-001 — Artifact Taxonomy, Naming, and Lifecycle Standard

| Field | Value |
|---|---|
| Version | 1.0 |
| Status | Effective |
| Authority | KE-005 through KE-007 |
| Owner | Ecosystem Governance Authority |
| Effective Date | 2026-07-29 |

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

## 2. Lifecycle

Allowed states are `Draft`, `Proposed`, `Review Required`, `Approved`, `Ratified`, `Effective`, `Deprecated`, `Superseded`, `Retired`, `Archived`, and `Rejected`. Only Approved, Ratified, or Effective artifacts may create obligations within their stated authority.

## 3. Naming

Paths and filenames shall be lowercase kebab case except approved acronyms in document identifiers. Names shall be stable, descriptive, and unique. A renamed or moved authority shall retain traceability through its register and revision history.

## 4. Authority

Every artifact shall identify its governing authority and shall not claim a level above that authority. Templates, reports, plans, registers, and historical evidence are non-normative unless expressly incorporated by an approved instrument.

## 5. Duplication

One normative topic shall have one canonical source. A new artifact requires evidence that extension of an existing artifact would reduce clarity or violate authority boundaries.

## 6. Approval

Approved by the Kuriosity Ecosystem Founding Authority on 2026-07-29.
