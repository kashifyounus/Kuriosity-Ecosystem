# KEP v1.0.1 — Relocation Release Plan

## Control

| Field | Value |
|---|---|
| Artifact Class | Release plan; non-normative |
| Status | Proposed; Blocked |
| Date | 2026-07-29 |
| Owner | KEP Platform Release Authority |
| Proposed Release | KEP Framework v1.0.1 |
| Proposed Canonical Location | `kashifyounus/Kuriosity-Ecosystem` at `platforms/kep/` |

## 1. Purpose

Provide a controlled successor-release path for moving the product-adoptable KEP baseline from its historical standalone repository into the KE repository.

This plan is not a release declaration, manifest, approval record, or adoption authority.

## 2. Historical Integrity

KEP v1.0.0 shall retain the repository coordinates approved by its original release declaration and manifest.

The migration of files into `platforms/kep/` is repository preparation and preservation evidence. It does not silently amend v1.0.0 or make the new location product-adoptable.

## 3. Proposed v1.0.1 Scope

The successor release should:

- preserve the normative meaning and inventory of KEP v1.0.0 unless separately approved changes are identified;
- establish the KE repository and `platforms/kep/` as the new canonical coordinates;
- record the relationship to superior KE authority without transferring product-domain authority;
- include migration parity and post-publication verification evidence;
- provide explicit upgrade and rollback guidance for adopting products; and
- preserve the standalone repository as historical release evidence.

## 4. Blocking Conditions

The release remains blocked until:

1. repository visibility and external-distribution authority are reconciled with KEP-001A UD-016;
2. the secondary validation context required by KEP-001A UD-005 is recorded with repository-controlled evidence;
3. the KE Founding Charter, Operating Model, Authority Model, and Platform Portfolio boundary are ratified or an approved exception is recorded;
4. KEP platform admission and authority within KE are confirmed;
5. a v1.0.1 release manifest, declaration, approval record, and verification package are prepared; and
6. the destination authoritative branch contains the approved migration baseline.

## 5. Required Release Artifacts

- KEP v1.0.1 release declaration;
- KEP v1.0.1 authoritative manifest;
- KEP v1.0.1 publication approval record;
- relocation and parity verification;
- secondary-context validation verification;
- product-adoption verification;
- upgrade and rollback guidance; and
- post-merge repository verification.

## 6. Non-Authorization

Until the blocking conditions are closed and the required release artifacts are approved:

- products shall not claim adoption of KEP v1.0.1;
- products shall not use the proposed KE coordinates as approved v1.0.1 adoption coordinates;
- the historical v1.0.0 manifest shall not be silently edited; and
- the standalone KEP repository shall not be deleted.

