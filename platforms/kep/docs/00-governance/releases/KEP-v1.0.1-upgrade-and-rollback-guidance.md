# KEP Framework v1.0.1 — Upgrade and Rollback Guidance

## Control

| Field | Value |
|---|---|
| Artifact Class | Release adoption guidance |
| Status | Approved for v1.0.1 Candidate |
| Date | 2026-07-29 |
| Applies To | Products adopting KEP v1.0.0 or considering v1.0.1 |

## 1. Upgrade Boundary

Upgrade from v1.0.0 to v1.0.1 is a controlled product decision. No product follows `main` automatically.

The relocation does not require a product to change its business requirements, domain model, architecture, or implementation merely because canonical framework coordinates moved.

## 2. Upgrade Procedure

An adopting product shall:

1. preserve its existing v1.0.0 adoption record;
2. confirm v1.0.1 is effective in its authoritative manifest;
3. compare the v1.0.0 and v1.0.1 normative inventories;
4. verify that the change is coordinate-only for the standards it adopts;
5. update its adoption contract to the v1.0.1 repository, platform root, release identifier, and manifest;
6. preserve existing product extensions and approved deviations;
7. run product-controlled conformance and repository-reference checks;
8. record approval, effective date, evidence, and adoption history; and
9. retain the prior coordinates for rollback.

## 3. Rollback Procedure

If the v1.0.1 location is unavailable, incorrectly published, or inconsistent with the approved manifest, the product may revert its adoption contract to:

- repository: `kashifyounus/kuriosity-engineering-platform`;
- release: `v1.0.0`;
- manifest: `docs/00-governance/releases/KEP-v1.0.0-release-manifest.md`.

Rollback shall be approved and recorded by the product's competent authority. It does not change KE or KEP release history.

## 4. Compatibility Determination

Because v1.0.1 preserves the v1.0.0 normative inventory and meaning, it is intended to be governance-compatible with v1.0.0. Repository-coordinate changes still require explicit product adoption updates and verification.
