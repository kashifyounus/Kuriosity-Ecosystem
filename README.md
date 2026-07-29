# Kuriosity Ecosystem (KE)

KE is the single governed source of truth for reusable engineering governance, ecosystem platforms, and product conformance.

## Authority

Repository-controlled approved artifacts are the durable KE authority. Conversation history, automation output, implementation precedent, and repository proximity do not create authority.

The authority order begins with:

1. applicable law and binding legal obligations;
2. binding contracts;
3. [KE-000 — Kuriosity Ecosystem Constitution](governance/constitution/KE-000-kuriosity-ecosystem-constitution.md);
4. ratified subordinate KE governance;
5. approved KE standards and architecture decisions; and
6. approved platform and product governance within their declared boundaries.

## Corrective Release Candidate

KE v2.0.0 is the approved corrective major-release candidate. It preserves the KE-only authority established by v1.1.0 while correcting semantic release classification, normalizing metadata, adding repository enforcement, and establishing architecture-description governance.

| Area | Authority |
|---|---|
| Ecosystem foundation | KE-000 through KE-004 |
| Engineering governance | KE-005 |
| Repository and artifact governance | KE-006 v1.1 |
| Change, release, conformance, and deviation | KE-007 v1.1 |
| Artifact metadata and lifecycle | KE-GOV-001 v2.0 |
| Architecture description and review | KE-ARCH-001 v1.0 |
| Other operational standards | KE-PO-001, KE-REV-001, KE-COM-001 |
| Effective release pending publication | KE v1.1.0 |
| Approved candidate | KE v2.0.0 |

KE v2.0.0 remains non-effective until verified merge to `main` and post-merge verification. KE directly owns reusable engineering governance. No separate engineering platform or external engineering-governance repository is required.

## Repository Map

- `governance/` — constitutional, foundational, authority, policy, approval, and release records.
- `standards/` — binding ecosystem-wide engineering standards.
- `platforms/` — admitted or recognized reusable capability platforms.
- `methodologies/` — reusable methods approved under KE authority.
- `patterns/` — reusable non-mandatory solution patterns.
- `adr/` — KE architecture and governance decisions.
- `templates/` — governed reusable templates.
- `reference/` — registers, terminology, and historical evidence.
- `docs/` — current planning and verification reports.
- `tools/` and `.github/workflows/` — deterministic repository validation.

## Platform and Product Boundary

KE governs ecosystem-wide engineering rules and shared ecosystem concerns. Platforms govern reusable capabilities within ratified mandates. Products govern their business domains and claim KE conformance through explicit, versioned records.

## Publication Rule

Only an Effective artifact with Approved or Ratified approval status may create obligations within its authority. Draft, Proposed, Review Required, Deprecated, Superseded, Retired, Archived, verification, and historical artifacts remain non-normative unless an Effective authority expressly incorporates them.
