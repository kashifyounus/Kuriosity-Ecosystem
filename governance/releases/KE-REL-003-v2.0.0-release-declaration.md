# KE-REL-003 — KE v2.0.0 Corrective Release Declaration

| Field | Value |
|---|---|
| Identifier | KE-REL-003 |
| Title | KE v2.0.0 Corrective Release Declaration |
| Artifact Type | Release Declaration |
| Version | 2.0.0 |
| Lifecycle Status | Effective |
| Approval Status | Approved |
| Verification Status | Pass |
| Authority | KE-007 and KE-APR-003 |
| Owner | Release Authority |
| Effective Date | 2026-07-29 |
| Scope | Corrective KE v2.0.0 foundation baseline |
| Amendment Path | KE-007 |
| Supersession State | Supersedes KE v1.1.0 as the current KE release |

## Release Purpose

KE v2.0.0 corrects the release classification of the KE-only authority transition. KE v1.1.0 introduced a breaking governance and adoption change but used a minor identifier. Repository history is preserved; v1.1.0 is not rewritten or backdated.

## Included Foundation Changes

- corrective major-release classification;
- canonical metadata and lifecycle normalization;
- repository-controlled ownership and deterministic validation;
- KE-ARCH-001 architecture-description and conformance-review governance;
- explicit migration and compatibility treatment; and
- benchmark-to-change traceability through KE-RPT-005.

## Compatibility and Migration

KE v2.0.0 preserves the substantive KE-only governance introduced by v1.1.0. It is breaking relative to consumers of the earlier separate engineering-platform adoption model. Products shall use a versioned KE v2.0.0 conformance record and remove active references to retired adoption coordinates through their own controlled repository changes.

No platform is admitted by this release. Product business-domain authority is unchanged.

## Deferred Matters

Security, data, AI, detailed release evidence, platform mandates, governed templates, public-repository licensing, and product-repository migrations remain outside this corrective package.

## Effectiveness Gate

The effectiveness gate passed on 2026-07-29. PR #6 merged the verified candidate to `main` at `de0615c4221ca78e8db1cd4a5438f508fd80984c`; authoritative-tree verification confirmed manifest parity, metadata integrity, zero content delta from the verified candidate, and no reintroduced retired dependency.
