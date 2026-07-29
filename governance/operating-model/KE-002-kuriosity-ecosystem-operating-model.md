# KE-002 — Kuriosity Ecosystem Operating Model

## Metadata

| Field | Value |
|---|---|
| Identifier | KE-002 |
| Title | Kuriosity Ecosystem Operating Model |
| Artifact Type | Operating Model |
| Version | 1.1 |
| Lifecycle Status | Effective |
| Approval Status | Ratified |
| Verification Status | Pass |
| Authority | KE-000 and KE-001 |
| Owner | Kuriosity Ecosystem Founding Authority |
| Effective Date | 2026-07-29 |
| Scope | KE operating units and engineering, platform, product-conformance, change, release, exception, and automation lifecycles |
| Amendment Path | KE-007 |
| Supersession State | Current; supersedes KE-002 Version 1.0 |

## 1. Purpose

This model defines how KE governs engineering, platforms, repositories, and product conformance without assuming product-domain authority.

## 2. Operating Units

KE operates through:

- Ecosystem Authority — constitutional, portfolio, cross-platform, and ecosystem-wide engineering authority;
- Platform Authorities — reusable capability authority within ratified mandates;
- Product Authorities — business-domain and product-lifecycle authority;
- Verification Authorities — evidence evaluation without implied approval authority; and
- Repository Maintainers — preservation and publication of approved records.

## 3. Engineering Lifecycle

Every material product or platform change shall follow the applicable parts of this sequence:

1. establish intent, authority, scope, and expected outcome;
2. define and approve requirements and constraints;
3. model the domain and ownership boundaries;
4. select architecture from requirements and quality attributes;
5. define data, security, interface, failure, and operational contracts;
6. plan implementation and migration;
7. implement within approved boundaries;
8. verify requirements, architecture, quality, security, and operations;
9. obtain risk-appropriate approval;
10. release with evidence and rollback or recovery provisions;
11. operate with ownership and observability; and
12. learn and evolve through controlled change.

Implementation shall not silently settle an unresolved requirement, authority question, architecture decision, or governance matter.

## 4. Platform Lifecycle

A platform moves through `Proposed`, `Recognized`, `Admitted`, `Active`, `Deprecated`, `Retired`, and `Archived` states.

Admission requires an approved identity, purpose, mandate, exclusions, owner, dependencies, adoption relationship, version model, evidence requirements, and effective date.

Retirement requires an impact assessment, replacement or absorption decision, consumer migration plan, evidence preservation, dependency verification, approval, and final state record.

## 5. Product Conformance

A product claims KE conformance through a repository-controlled record identifying:

- the KE release and applicable standards;
- product-owned extensions;
- platform releases adopted, if any;
- approved deviations and compensating controls;
- evidence and verification state;
- upgrade and rollback policy; and
- adoption history.

KE conformance does not transfer product-domain ownership to KE.

## 6. Change and Release

Changes shall be classified by the highest authority affected and by risk. Breaking changes require explicit impact analysis, migration guidance, approval, and versioning. Release claims require durable evidence and shall never be inferred from implementation completion.

## 7. Exceptions

An exception shall identify the rule, reason, scope, risk, compensating controls, owner, approver, effective period, review or expiry, and exit condition. An undocumented deviation is nonconformance.

## 8. Automation and AI

Automation and AI may analyze, draft, implement, test, review, and operate within assigned boundaries. They shall not fabricate access or evidence, create governing authority, approve material decisions, or replace accountable human judgment.

## 9. Ratification

Version 1.1 is ratified on 2026-07-29 through `governance/approvals/KE-APR-002-ke-only-authority-and-retirement-approval.md`.
