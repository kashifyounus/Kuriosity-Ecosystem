# KE-RPT-007 — Horizontal Controls Audit

| Field | Value |
|---|---|
| Identifier | KE-RPT-007 |
| Title | Horizontal Controls Audit |
| Artifact Type | Audit Report; non-normative |
| Lifecycle Status | Review Required |
| Approval Status | Not Applicable |
| Verification Status | Pass with Conditions |
| Date | 2026-07-29 |
| Scope | Administrative repository controls and security, data, release-depth, and AI governance after KE v2.0.0 |
| Authoritative Baseline | KE v2.0.0 on `main` |
| Authority | KE-005 through KE-007 and KE-REV-001 |

## 1. Executive Summary

KE v2.0.0 closes the corrective-foundation gaps but does not yet provide sufficient horizontal operational controls for platform admission or dependable product conformance. Security, data, release-depth, and AI obligations remain high-level. Repository-controlled validation exists, but administrative branch enforcement could not be verified through the connected repository interface.

Three unblocked proposed standards are prepared: KE-SEC-001, KE-DATA-001, and KE-AI-001. They are non-normative pending review and approval. The release-depth standard is blocked by an identifier collision: KE-GOV-001 reserves `KE-REL-*` for release standards while KE-REL-001 through KE-REL-004 already identify release declarations and manifests.

## 2. Repository Assessment

| Area | Current state | Audit determination |
|---|---|---|
| Repository authority | Effective | Canonical repository and PR workflow defined |
| Repository validation | Implemented | Workflow validates manifest and normative metadata |
| Administrative protection | Not verified | Ruleset/branch protection evidence not available through current connector |
| Security | Broad KE-005 principles only | Operational assurance standard required |
| Data | Broad KE-005 and KE-ARCH-001 principles only | Ownership, quality, lifecycle, and evidence standard required |
| Release | KE-007 release requirements | Provenance, integrity, reproducibility, vulnerability, promotion, and rollback depth incomplete |
| AI | KE-005 task-level principles | Lifecycle, evaluation, oversight, supplier, and operational assurance incomplete |
| Templates | Missing | Shall follow approved controlling standards |
| Platforms | Recognized; mandates pending | Correctly blocked until horizontal controls are effective |

## 3. Benchmark Findings

| Source | Evidence used | KE position | Classification |
|---|---|---|---|
| [GitHub rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) and [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | Pull-request gates, required status checks, branch update and bypass controls | Require PR publication, successful KE validation, blocked force-push/deletion, and explicit bypass governance; verify administratively | Adopt |
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Govern, Identify, Protect, Detect, Respond, Recover outcomes | Use as outcome taxonomy without copying its complete catalog | Adapt |
| [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) | Secure practices integrated into any SDLC | Use risk-scaled secure-engineering lifecycle outcomes | Adopt |
| [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/) | Verifiable application-security requirements | Allow as product-selected evidence; do not impose on non-application platforms | Reference |
| [ISO 8000-1:2022](https://www.iso.org/standard/81745.html) and [ISO 8000-150:2022](https://www.iso.org/standard/80753.html) | Data-quality principles, roles, responsibilities, and evidence | Use explicit accountability and measurable fitness-for-use outcomes | Adapt |
| [NIST Privacy Framework](https://www.nist.gov/privacy-framework) | Privacy-risk identification and management | Integrate into data governance without making legal conclusions | Adapt |
| [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) | Govern, Map, Measure, Manage and trustworthy-AI characteristics | Use as AI risk lifecycle; preserve KE authority and review rules | Adapt |
| [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) | Generative and dual-use AI risks and secure-development practices | Apply only where relevant | Reference |
| [SLSA 1.2](https://slsa.dev/spec/v1.2/) | Incremental source/build provenance and integrity levels | Use provenance concepts as risk-scaled evidence; do not mandate one universal level | Adapt |

## 4. Gap Analysis

### HC-001 — Administrative publication enforcement is unverified

Repository files declare CODEOWNERS and validation, but no durable evidence confirms that `main` requires pull requests and the KE validation check or blocks destructive bypass. A repository report cannot substitute for live settings.

### HC-002 — Security outcomes are not operational

KE-005 requires security throughout the lifecycle but does not define security governance, threat and asset identification, protection, detection, response, recovery, secure development, supply-chain assurance, or risk-scaled release gates.

### HC-003 — Data outcomes are not operational

KE lacks a canonical rule for data accountability, semantic contracts, quality dimensions, lineage, lifecycle, privacy-risk handling, consistency, migration, recovery, and evidence.

### HC-004 — Release-depth controls are incomplete

KE-007 defines release records but not artifact provenance, integrity, reproducibility, dependency/vulnerability state, environment promotion, attestation, rollback verification, or residual-risk evidence.

### HC-005 — AI governance is incomplete

KE-005 establishes human authority and task boundaries but not AI lifecycle governance, context mapping, evaluation, supplier/model changes, meaningful oversight, operational monitoring, incident response, or transparency records.

### HC-006 — Release identifier namespace is ambiguous

`KE-REL-*` is simultaneously reserved for a normative standard domain and used for release declarations/manifests. The next `KE-REL` identifier cannot truthfully communicate its artifact type.

## 5. Risks

| Risk | Rating | Required treatment |
|---|---|---|
| Policy is bypassable despite repository-controlled checks | High | Verify and record live ruleset/branch protection |
| Platforms proceed with inconsistent security or data controls | High | Keep admission blocked until horizontal standards are effective |
| AI use exceeds defined authority or evidence | High | Approve risk-scaled AI engineering standard before material platform AI capability |
| Release claims lack provenance and integrity depth | High | Resolve identifier model, then publish release assurance standard |
| Standards duplicate external catalogs | Medium | Preserve outcome-based KE rules and reference detailed catalogs selectively |
| Proposed standards are mistaken as effective | Medium | Keep Proposed/Pending metadata and exclude from effective release manifest |

## 6. Recommendations

1. Resolve the `KE-REL` identifier collision before authoring the release-depth standard.
2. Review KE-SEC-001, KE-DATA-001, and KE-AI-001 as one horizontal-control set.
3. Verify administrative protection for `main`; if unavailable, record a blocker rather than fabricated compliance.
4. After approval, publish the compatible standards in a KE v2.1.0 release.
5. Then publish controlled templates for ADR, architecture review, security review, data contract, AI assessment, release evidence, deviation, product conformance, and platform mandate.
6. Define platform admission and maturity criteria only after these horizontal controls are effective.
7. Evaluate KEC first.

## 7. Repository Impact

This audit and the three proposed standards create no effective obligation. They do not change KE v2.0.0, admit a platform, claim product conformance, or select product technology. The release-depth standard remains uncreated to prevent identifier ambiguity.

## 8. Verification Results

| Check | Result |
|---|---|
| Effective KE v2.0.0 baseline reviewed | Pass |
| KE-005 through KE-007 reviewed | Pass |
| KE-GOV-001, KE-REV-001, and KE-ARCH-001 reviewed | Pass |
| Effective manifest and artifact register reviewed | Pass |
| Current authoritative external benchmarks reviewed | Pass |
| Duplicate normative subject check | Pass for SEC, DATA, and AI |
| Release identifier uniqueness | Fail; decision required |
| Proposed artifacts excluded from effective manifest | Pass |
| Platform admission or product conformance introduced | No |
| Administrative ruleset state verified | Not Reviewed; connector limitation |

## 9. Next Audit Scope

After the identifier decision and horizontal-standard approval, complete the release assurance standard, controlled templates, platform admission criteria, and KEC mandate audit.
