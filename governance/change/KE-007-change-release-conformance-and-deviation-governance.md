# KE-007 — Change, Release, Conformance, and Deviation Governance

## Metadata

| Field | Value |
|---|---|
| Identifier | KE-007 |
| Title | Change, Release, Conformance, and Deviation Governance |
| Artifact Type | Governance Policy |
| Version | 1.1 |
| Lifecycle Status | Effective |
| Approval Status | Approved |
| Verification Status | Pass |
| Authority | KE-000 through KE-006 |
| Owner | Ecosystem Governance Authority |
| Effective Date | 2026-07-29 |
| Scope | KE change classification, versioning, release, conformance, deviation, correction, and retirement |
| Amendment Path | KE-000 Section 7 when constitutional authority is affected; otherwise this instrument |
| Supersession State | Current; supersedes KE-007 Version 1.0 |

## 1. Change Classification

Every material change shall identify the highest affected authority, risk class, compatibility effect, consumers, migration need, evidence, owner, approver, and effective date.

Changes are:

- editorial — no change in meaning or obligation;
- compatible — adds or clarifies without breaking existing conformance;
- breaking — removes, contradicts, or changes an existing obligation or coordinate; or
- emergency — temporary control required to prevent material harm.

## 2. Versioning

KE uses semantic release identifiers:

- major — breaking constitutional, governance, standard, or adoption change;
- minor — compatible normative addition or material clarification; and
- patch — non-normative, editorial, or evidence correction without changed obligation.

Individual instruments retain their own controlled versions.

### 2.1 Corrective Release

When an effective release identifier is discovered to understate a breaking change, KE shall not rewrite or backdate repository history. The next release shall use the correct major identifier, explicitly supersede the misclassified release, preserve the compatibility and migration record, and identify the correction authority and evidence.

## 3. Release

A KE release requires:

- declaration and manifest;
- exact normative inventory;
- compatibility and migration statement;
- verification result;
- approval authority and effective date;
- known limitations and deferred matters; and
- rollback or successor guidance when material.

## 4. Product Conformance

A product conformance record shall identify the KE release, applicable instruments, locally owned extensions, adopted platforms, deviations, evidence, approval, upgrade policy, and history. Conformance shall not be claimed by repository proximity or informal agreement.

## 5. Deviation

A deviation requires exact rule, justification, scope, risk, compensating controls, owner, approver, expiry or review, and exit condition. Repeated deviations trigger review of the rule or architecture.

## 6. Retirement

Retirement of a platform, authority, standard, or repository requires:

1. dependency and consumer audit;
2. absorption, replacement, or removal decision;
3. migration of unique active obligations;
4. cancellation of pending releases and exceptions;
5. preservation of sufficient internal evidence;
6. removal of active coordinates and adoption claims;
7. zero-dependency verification; and
8. explicit approval and effective date.

After these gates pass, an external retired repository may be archived or deleted without remaining a KE dependency.

## 7. Approval

Version 1.1 approved by the Kuriosity Ecosystem Founding Authority on 2026-07-29 through KE-APR-003.
