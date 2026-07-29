# KE-ADR-001 — Retire the Separate Engineering Platform and Internalize Engineering Governance

| Field | Value |
|---|---|
| Status | Accepted |
| Decision Date | 2026-07-29 |
| Authority | Kuriosity Ecosystem Founding Authority |
| Supersedes | Proposed engineering-platform relocation and activation |

## Context

KE had migrated a separate engineering-platform baseline and prepared a relocation candidate. That structure required KE to maintain a subordinate platform release, external historical coordinates, activation gates, duplicate authorities, and product adoption dependencies.

The Founding Authority decided that KE shall be the only maintained authority and shall own reusable engineering governance directly.

## Decision

- Retire the separate engineering-platform identity as an active KE platform.
- Cancel its relocation release candidate.
- Absorb its useful product-independent engineering obligations into KE-005 through KE-007 and KE standards.
- Remove its platform directory and active coordinates.
- Replace product platform-adoption references with KE conformance records.
- Preserve only sufficient self-contained history inside KE.
- Permit deletion of the external retired repository after this decision is published and zero-dependency verification passes.

## Consequences

- KE is the sole engineering-governance source of truth.
- The active platform portfolio no longer includes a separate engineering platform.
- Products conform directly to versioned KE releases.
- Historical names and coordinates carry no current authority.
- No KE release, verification, rollback, or adoption process depends on an external repository.

## Alternatives Rejected

- Maintain both authorities: rejected because it duplicates governance and maintenance.
- Archive but retain as a required historical authority: rejected because it leaves an external dependency.
- Activate the relocation candidate: rejected because it preserves the unwanted platform model.
