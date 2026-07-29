# KE-002 — Kuriosity Ecosystem Operating Model

## Metadata

| Field | Value |
|---|---|
| Identifier | KE-002 |
| Title | Kuriosity Ecosystem Operating Model |
| Version | 1.0 |
| Status | Ratified; Effective |
| Authority Level | Foundational operating governance; subordinate to KE-000 and KE-001 |
| Owner | Kuriosity Ecosystem Founding Authority |
| Effective Date | 2026-07-29 |
| Applies To | KE governance, admitted platforms, and products claiming KE adoption |

## 1. Purpose

This Operating Model defines how KE authority is exercised across the ecosystem, platforms, and adopting products.

It does not define platform-specific capabilities, product-domain behavior, technology choices, or implementation procedures.

## 2. Operating Units

KE operates through:

- the ecosystem authority, which governs shared ecosystem concerns;
- platform authorities, which govern reusable capabilities within ratified mandates;
- product authorities, which govern product business domains and product lifecycle;
- verification authorities, which evaluate evidence without assuming approval authority; and
- repository maintainers, who preserve approved records without creating governing authority through publication mechanics.

Roles and accountability are defined in KE-003.

## 3. Ecosystem Lifecycle

### 3.1 Establish

Foundational KE authority is proposed, reviewed, ratified, recorded, and published through explicit human approval.

### 3.2 Admit a Platform

A platform may enter the KE portfolio only when its identity, purpose, mandate, exclusions, accountable owner, dependencies, lifecycle state, and relationship to products are documented and approved.

Directory creation, implementation, repeated use, or naming convention does not admit a platform.

### 3.3 Govern a Platform

Each admitted platform shall maintain:

- a bounded mandate;
- an accountable platform owner;
- approved governance and architecture appropriate to its scope;
- a versioned release and change model;
- adoption coordinates;
- evidence of verification; and
- explicit dependency and deviation rules.

### 3.4 Adopt a Platform

A product adopts a platform through a repository-controlled adoption record that identifies:

- the platform and adopted release;
- the adopted standards or capabilities;
- product-owned extensions;
- approved deviations;
- upgrade and rollback policy; and
- adoption history.

Adoption does not transfer product-domain authority to the platform.

### 3.5 Change

A proposed change shall be classified by the highest authority it affects. Changes shall be reviewed and approved by the competent authority before they are represented as effective.

Lower-level artifacts shall not amend higher authority.

### 3.6 Verify

Claims of conformance, readiness, completion, adoption, release, or migration shall be supported by durable evidence against explicit acceptance criteria.

Verification records report evidence and outcome. They do not independently ratify authority.

### 3.7 Release

A KE or platform release shall have:

- a unique versioned identity;
- an authoritative manifest;
- an explicit normative inventory;
- approval evidence;
- adoption coordinates;
- exclusions and known limitations; and
- a declared effective state.

Historical release manifests shall remain immutable in meaning. A changed inventory, lifecycle state, or adoption coordinate requires a controlled successor release.

### 3.8 Retire

Retirement requires impact analysis, dependent-product review, preservation of historical authority and evidence, transition or rollback guidance, and approval by the competent authority.

Deletion is not equivalent to retirement.

## 4. Decision Flow

Every material KE decision shall:

1. identify the governing authority and scope;
2. state the problem, evidence, and constraints;
3. check whether an existing concept can be extended;
4. assess affected ecosystem, platform, and product boundaries;
5. record alternatives and consequences proportionate to risk;
6. receive explicit approval from the competent human authority;
7. update the canonical repository artifacts; and
8. produce verification evidence before release claims are made.

## 5. Conflict and Escalation

Conflicts are resolved using the KE-000 authority hierarchy.

An unresolved conflict shall be escalated to the next superior competent authority. It shall not be resolved by implementation preference, repository mechanics, automation, or silence.

## 6. Cross-Platform Coordination

A cross-platform dependency shall identify:

- the owning platform for each capability;
- the consuming platform or product;
- the governing contract or adoption record;
- compatibility and change obligations;
- failure and rollback boundaries; and
- the authority responsible for resolving conflict.

Shared use shall not create ambiguous ownership.

## 7. Repository Operating Boundary

The repository is the durable publication and evidence mechanism for KE. It does not replace ratification, approval, accountability, or governance review.

Changes shall be prepared on controlled branches, reviewed against higher authority, and merged to the authoritative branch only after approval and verification.

## 8. Operating Reviews

KE shall perform:

- immediate review upon a material constitutional, legal, contractual, security, ownership, or platform-boundary change;
- release review before any KE or platform release becomes effective;
- periodic governance review at the cadence established by approved KE policy; and
- post-change verification when repository publication or migration changes authoritative coordinates.

## 9. Ratification Record

| Field | Value |
|---|---|
| Ratified By | Kuriosity Ecosystem Founding Authority |
| Authority | Kuriosity Ecosystem Founding Authority |
| Effective Date | 2026-07-29 |
| Approval Record | `governance/approvals/KE-foundation-v1.0-ratification-and-relocation-approval-record.md` |

