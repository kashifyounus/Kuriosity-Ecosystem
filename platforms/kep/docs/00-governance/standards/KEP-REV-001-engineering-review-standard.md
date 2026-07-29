**Authoritative Representation:**  
This Markdown document is the canonical human-readable approved representation of this KEP artifact.

# KEP-REV-001 — Engineering Review Standard

| Document Control | Value |
| --- | --- |
| Document ID | KEP-REV-001 |
| Title | Engineering Review Standard |
| Domain | REV |
| Artifact Class | Subordinate standard |
| Status | Effective |
| Version | 1.0 |
| Governing Authority | KEP-002 — Engineering Constitution |
| Foundational Sources | KEP-000, KEP-001, KEP-001A, KEP-GOV-002, KEP-PO-001 |
| Accountable Owner | Governance Steward |
| Approval Authority | Founding Authority |
| Effective Date | July 25, 2026 |
| Review Cadence | Every six months and immediately upon a material review, quality-gate, authority, evidence, or risk-governance change |
| Amendment Path | Controlled amendment under applicable KEP governance |
| Supersedes | None |
| Related Standards | KEP-GOV-002; KEP-PO-001; planned KEP-COM-001 and KEP-QUAL standards |
| Deferred-Decision Dependencies | UD-009, UD-010, UD-011, and UD-014 remain unresolved within their stated boundaries |

Product-independent. Technology-neutral. Evidence-governed. Risk-proportional.

## Normative Language

MUST and SHALL express mandatory obligations. MUST NOT and SHALL NOT express prohibitions. SHOULD expresses the expected default and requires recorded rationale for material deviation. MAY expresses permission within applicable authority and constraints. Material retains the meaning established by KEP-002.

# 1. Purpose

1.1. This standard SHALL define how KEP-governed engineering artifacts are reviewed for completeness, requirement fidelity, architecture, dependencies, duplication, security, compliance, consistency, evidence, and presentation readiness.

1.2. This standard SHALL convert existing constitutional and foundational review duties into a consistent, executable, risk-proportional review process.

1.3. This standard SHALL establish review dimensions, review states, reviewer duties, finding requirements, approval meaning, escalation boundaries, and minimum review records.

1.4. This standard SHALL treat every material specification as a production engineering artifact subject to appropriate review before approval, implementation authorization, release, or authoritative use.

1.5. This standard SHALL NOT redefine constitutional authority, replace the R0–R4 risk model, establish numeric thresholds reserved under UD-011, or silently resolve evidence-retention, agent-log, or appeal matters reserved under UD-009, UD-010, and UD-014.

# 2. Authority and Precedence

2.1. This standard derives its authority from KEP-002 and SHALL be interpreted consistently with KEP-000, KEP-001, KEP-001A, KEP-GOV-002, and KEP-PO-001.

2.2. Applicable law and binding contractual obligations SHALL retain superior authority.

2.3. A review SHALL identify the governing authority applicable to the artifact under review.

2.4. A reviewer MUST NOT approve a lower-level artifact that conflicts with a higher authority.

2.5. Review approval SHALL NOT amend, waive, supersede, or reinterpret higher authority unless an authorized governance mechanism expressly permits that effect.

2.6. Product Owner acceptance under KEP-PO-001 SHALL NOT substitute for independently required architecture, security, quality, legal, release, governance, or operational review.

# 3. Scope

3.1. This standard SHALL apply to material:

- Governance artifacts.
- Requirements.
- Specifications.
- Architecture decisions and designs.
- Source code and configuration.
- Data models and migrations.
- Interfaces and integrations.
- Infrastructure and deployment artifacts.
- Tests and verification evidence.
- Security controls.
- Release records.
- Runbooks and operational procedures.
- AI-generated engineering artifacts.
- Exceptions and nonconformance dispositions where review is required.

3.2. This standard SHALL apply throughout intent, requirements, architecture, implementation, verification, release, operation, migration, incident learning, retirement, and decommissioning.

3.3. Review depth SHALL scale with artifact type, materiality, assigned R0–R4 risk, uncertainty, reversibility, and affected authority.

3.4. This standard SHALL NOT require every review dimension for every artifact.

3.5. A review record SHALL identify each applicable dimension and its result.

# 4. Review Principles

## 4.1 Review Before Authority Claim

4.1.1. A material artifact SHALL receive an internal completeness review before it is represented as approved, implementation-authorized, ratification-ready, release-ready, production-ready, or authoritative.

4.1.2. Review-ready SHALL NOT mean approved.

4.1.3. Approval SHALL NOT mean defect-free.

## 4.2 Evidence Before Confidence

4.2.1. Review conclusions SHALL be based on available evidence, governing requirements, and observable artifact content.

4.2.2. Reviewer confidence, seniority, familiarity, or AI-generated explanation MUST NOT substitute for evidence.

4.2.3. A required check that was not performed MUST NOT be implied as passed.

## 4.3 Scope-Bounded Review

4.3.1. Every review SHALL declare its scope.

4.3.2. A reviewer SHALL NOT imply review of artifacts, versions, environments, evidence, or concerns outside the declared scope.

4.3.3. A partial review MAY be performed when clearly labeled and when no broader approval is implied.

## 4.4 Independence and Accountability

4.4.1. The artifact owner SHALL remain accountable after review and approval.

4.4.2. Review independence SHALL scale with risk and applicable authority.

4.4.3. R3 and R4 reviews SHALL identify whether independent review was required, available, performed, unavailable, or replaced by an approved compensating control.

4.4.4. This standard SHALL NOT create the formal conflict-of-interest or appeal process reserved under UD-014.

## 4.5 Constructive and Actionable Review

4.5.1. Review SHALL focus on the artifact, requirement, decision, risk, contract, and evidence.

4.5.2. Review MUST NOT become personal, retaliatory, territorial, or performative.

4.5.3. Material findings SHALL be actionable and traceable.

# 5. Review Inputs

5.1. Before review begins, the reviewer SHALL identify, as applicable:

1. Artifact identifier and version.
2. Artifact owner.
3. Review objective.
4. Declared scope.
5. Governing authority.
6. Applicable requirements.
7. Assigned or proposed R0–R4 risk class.
8. Required review dimensions.
9. Required evidence.
10. Approval authority.
11. Known exceptions.
12. Deferred-decision dependencies.
13. Related artifacts and dependencies.
14. Product Owner decisions required under KEP-PO-001.

5.2. Missing review inputs SHALL be classified as a finding, blocked condition, or approved limitation according to materiality.

5.3. A review MAY proceed with incomplete inputs only when the limitation is explicit and no unsupported approval is produced.

# 6. Review States

6.1. Each required review dimension SHALL use one of the following states:

| State | Meaning |
| --- | --- |
| Pass | The reviewed concern satisfies applicable requirements within the declared scope and accepted risk |
| Fail | A material unmet requirement, defect, conflict, or unacceptable risk was identified |
| Blocked | The review could not be completed because required input, evidence, access, authority, or dependency was unavailable |
| Not Performed | The review was required or contemplated but was not executed |
| Not Applicable | The concern does not apply to the artifact within the declared scope |

6.2. Review states SHALL be explicit.

6.3. Not Performed MUST NOT be converted to Pass through assumption.

6.4. Blocked MUST NOT be converted to Pass solely because no defect was observed.

6.5. Not Applicable SHALL include a rationale when applicability is not self-evident.

6.6. A failed mandatory review SHALL block progression unless an authorized exception or higher-authority disposition permits otherwise.

# 7. Core Review Dimensions

## 7.1 Scope and Completeness Review

7.1.1. Review SHALL verify that the artifact satisfies its declared scope and definition of done.

7.1.2. Review SHALL identify omitted sections, placeholders, unresolved decisions, missing owners, missing evidence, and incomplete dependencies.

7.1.3. A material omission MUST NOT be hidden by formatting completeness or template population.

## 7.2 Requirement Fidelity Review

7.2.1. Review SHALL verify alignment with approved requirements and acceptance methods.

7.2.2. Review SHALL identify requirements that are missing, contradicted, weakened, silently discarded, or not traceable to implementation or evidence.

7.2.3. Where requirements conflict, the artifact SHALL NOT be approved until the conflict is authoritatively resolved or explicitly bounded.

## 7.3 Decision and Authority Review

7.3.1. Review SHALL verify that material decisions are owned by the correct authority.

7.3.2. Product, engineering, governance, and cross-authority decisions SHALL be evaluated consistently with KEP-PO-001.

7.3.3. Review SHALL identify missing approvals, unauthorized decisions, approval-by-silence assumptions, and authority substitutions.

7.3.4. Approval by one authority MUST NOT be represented as approval by another.

## 7.4 Architecture Review

7.4.1. Material architecture SHALL be reviewed for:

- Requirement alignment.
- Domain boundaries.
- Quality attributes.
- Separation of concerns.
- Dependency direction.
- Interface contracts.
- Failure modes.
- Security boundaries.
- Data ownership.
- Operational context.
- Replaceability.
- Evolution and migration.
- Reuse justification.
- Architecture decision traceability.

7.4.2. Architecture review SHALL identify architecture drift.

7.4.3. Architecture drift SHALL be corrected, approved through a valid decision, or covered by an authorized exception.

## 7.5 Dependency and Impact Review

7.5.1. Review SHALL evaluate direct and material transitive dependencies where they may affect:

- Compatibility.
- Security.
- Licensing.
- Reliability.
- Performance.
- Deployment.
- Data integrity.
- Operations.
- Maintainability.
- Vendor lock-in.
- Support obligations.

7.5.2. Dependency review depth SHALL be proportional to risk and exposure.

7.5.3. A dependency MUST NOT be approved solely because it is popular, already present, or suggested by an AI agent.

7.5.4. Review SHALL identify downstream consumers and affected integration contracts where applicable.

## 7.6 Duplication and Reuse Review

7.6.1. Review SHALL identify unnecessary duplication of:

- Requirements.
- Decisions.
- Rules.
- Data.
- Interfaces.
- Services.
- Source logic.
- Documentation.
- Templates.
- Evidence.

7.6.2. Review SHALL distinguish justified redundancy from uncontrolled duplication.

7.6.3. Reuse SHALL be accepted only when the abstraction is coherent, owned, supportable, compatible, and demonstrably reduces total cost or risk.

7.6.4. A reviewer MUST NOT force reuse when local clarity and domain correctness would be harmed.

## 7.7 Security and Compliance Review

7.7.1. Security and compliance review SHALL occur when applicable legal, regulatory, contractual, privacy, identity, financial, accessibility, retention, or security obligations may be affected.

7.7.2. Review SHALL identify applicable obligations or explicitly record that applicability remains unresolved.

7.7.3. Review SHALL evaluate, as applicable:

- Authentication and authorization.
- Confidentiality and integrity.
- Data classification and permitted use.
- Least privilege.
- Secret handling.
- Auditability.
- Vulnerability exposure.
- Trust boundaries.
- Retention dependencies.
- Legal or contractual restrictions.
- Accessibility obligations.

7.7.4. Product-specific legal conclusions SHALL require applicable authority or qualified review and MUST NOT be fabricated by engineering or AI.

## 7.8 Data Integrity Review

7.8.1. Review SHALL verify data meaning, ownership, system of record, lifecycle, quality expectations, compatibility, migration, and recovery where applicable.

7.8.2. Data duplication SHALL require a defined purpose, synchronization model, consistency expectation, conflict rule, and exit path.

7.8.3. A data migration SHALL NOT be approved without risk-appropriate validation evidence.

## 7.9 Compatibility and Migration Review

7.9.1. Review SHALL identify backward-compatibility effects, breaking changes, migration requirements, rollback or recovery, downstream consumers, and deprecation implications.

7.9.2. A breaking change SHALL require explicit impact analysis and approval appropriate to risk.

7.9.3. Missing general deprecation windows under UD-013 SHALL be disclosed where materially relevant.

## 7.10 Operations and Recovery Review

7.10.1. Review SHALL evaluate operational ownership, observability, failure handling, support boundaries, deployment, configuration, recovery, rollback, incident response, and decommissioning where applicable.

7.10.2. Production readiness SHALL NOT be inferred from implementation completion alone.

7.10.3. Backup and restoration claims SHALL require evidence where data loss or service interruption creates material risk.

## 7.11 Documentation and Knowledge Consistency Review

7.11.1. Review SHALL compare the artifact with authoritative requirements, architecture, contracts, terminology, data definitions, repository rules, and related approved artifacts.

7.11.2. Conflicting authoritative artifacts SHALL be recorded and reconciled.

7.11.3. Documentation that materially conflicts with governed behavior or contracts SHALL be treated as a defect.

7.11.4. Terminology SHALL remain consistent with authoritative sources.

## 7.12 Verification and Evidence Review

7.12.1. Review SHALL verify that evidence supports the claims being made.

7.12.2. Evidence SHALL be attributable to the reviewed artifact and version where practical.

7.12.3. Evidence MAY include build results, tests, static analysis, security scans, contract validation, runtime checks, migration validation, performance measurements, accessibility evaluation, deployment verification, operational-readiness review, and authorized human approval.

7.12.4. This standard SHALL NOT establish platform-wide evidence storage, retention, integrity, or agent-log boundaries reserved under UD-009 and UD-010.

## 7.13 Product Owner Decision Completeness Review

7.13.1. Review SHALL identify unresolved product decisions required under KEP-PO-001.

7.13.2. Review SHALL verify that routine engineering choices have not been transferred unnecessarily to the Product Owner.

7.13.3. A material product ambiguity SHALL block dependent approval unless validly resolved or bounded.

## 7.14 Presentation Readiness Review

7.14.1. Before an artifact is presented as final for scope, review shall verify:

- Scope completion.
- Truthful status.
- Explicit limitations.
- Resolved or recorded findings.
- Correct authority and approval state.
- Required evidence references.
- Consistent terminology.
- Absence of misleading placeholders.
- Clear unresolved decisions and blocked items.

7.14.2. KEP-COM-001 SHALL govern final communication structure after it becomes effective.

# 8. Specification Review Standard

8.1. Every material specification SHALL be treated as a production engineering artifact.

8.2. A specification review SHALL evaluate, as applicable:

- Purpose and scope.
- Authority.
- Requirements and acceptance criteria.
- Domain terminology.
- Architecture alignment.
- Interfaces and data contracts.
- Security and compliance.
- Dependencies.
- Failure behavior.
- Operations.
- Migration and compatibility.
- Verification approach.
- Assumptions and risks.
- Open decisions.
- Traceability.

8.3. An unreviewed specification MUST NOT be represented as approved, complete, implementation-authorized, ratification-ready, or production-ready.

8.4. A collaborative draft MAY be exposed when explicitly requested, provided its status, limitations, and unresolved matters are clear.

8.5. Review depth SHALL scale with materiality and R0–R4 risk.

# 9. Risk-Proportional Review

9.1. Every material review SHALL identify the applicable R0–R4 risk class or record that classification is pending.

9.2. Review depth, evidence, independence, approval authority, and escalation SHALL scale with risk.

9.3. The following minimum qualitative principles SHALL apply:

| Risk Class | Minimum Review Principle |
| --- | --- |
| R0 | Integrity, metadata, and unintended-meaning review |
| R1 | Localized requirement, correctness, and owner review |
| R2 | Requirement, test, integration, compatibility, dependency, and accountable review |
| R3 | Expanded architecture, security, data, migration, recovery, operational, and release review; independent review where practical |
| R4 | Maximum applicable review, explicit accountable approval, independent evidence, and documented rollback or demonstration that rollback is impossible |

9.4. This standard SHALL NOT establish numeric thresholds reserved under UD-011.

9.5. Risk classification MUST NOT be lowered to reduce review, evidence, independence, approval, or schedule burden.

9.6. A review MAY raise the assigned risk class when evidence shows greater impact or uncertainty.

# 10. Reviewer Responsibilities

10.1. A reviewer SHALL:

- Understand the declared scope.
- Identify applicable authority and requirements.
- Evaluate evidence honestly.
- Record limitations.
- Distinguish fact, inference, assumption, and recommendation.
- Avoid unsupported approval.
- Produce actionable findings.
- Disclose material conflicts of interest or lack of independence.
- Preserve artifact-owner accountability.

10.2. A reviewer MUST NOT:

- Claim checks that were not performed.
- Approve outside assigned authority.
- Conceal material defects.
- Reclassify risk solely for convenience.
- Treat style preference as a binding requirement without authority.
- Require unrelated scope expansion as a condition of approval.
- Substitute AI-generated confidence for evidence.

10.3. AI MAY assist review but SHALL remain subject to the same evidence, scope, truthfulness, and authority constraints.

10.4. AI-generated findings SHALL identify source evidence and MUST NOT fabricate inspection, execution, or verification.

# 11. Review Findings

11.1. A material finding SHALL identify:

1. Finding identifier.
2. Affected artifact or location.
3. Observed condition.
4. Why it matters.
5. Governing requirement.
6. Evidence.
7. Severity.
8. Owner.
9. Required disposition.
10. Status.
11. Dependencies where applicable.

11.2. Findings SHALL use the following severity classes unless a higher or more specific authority applies:

| Severity | Meaning |
| --- | --- |
| Critical | Creates or may create unacceptable legal, contractual, security, financial, safety, identity, regulated-data, irreversible, or constitutional risk |
| High | Materially violates requirements, architecture, security, data, release, or operational obligations, or is likely to cause serious failure |
| Medium | Creates correctness, maintainability, performance, compatibility, or operational risk requiring correction |
| Low | Limited-impact defect or improvement requirement |
| Advisory | Optional improvement or future consideration not shown to violate a binding requirement |

11.3. Severity SHALL be based on impact, scope, reversibility, authority violated, and evidence.

11.4. A finding MUST NOT be closed without correction evidence, accepted risk, authorized exception, valid superseding decision, or evidence that the finding was invalid.

# 12. Review Outcomes

12.1. A review SHALL conclude with one of the following outcomes:

| Outcome | Meaning |
| --- | --- |
| Approved | Applicable mandatory review dimensions passed within accepted scope and risk |
| Approved with Recorded Conditions | Approval is valid subject to explicit, owned, bounded conditions that do not conceal failed mandatory gates |
| Changes Required | Material findings must be corrected before approval |
| Blocked | Required review cannot complete because an input, dependency, authority, or evidence requirement is unavailable |
| Rejected | The artifact is unsuitable for approval within the reviewed scope and requires material rework or replacement |
| Advisory Review Only | The review provides observations but does not grant approval |

12.2. Approved with Recorded Conditions MUST NOT be used to bypass a failed mandatory gate.

12.3. Approval SHALL identify scope, artifact version, accepted risk, reviewer, date, and any conditions.

12.4. Approval SHALL NOT remove owner accountability or prevent later reclassification when new evidence emerges.

# 13. Review Records

13.1. A material review record SHALL include:

- Artifact and version.
- Review scope.
- Reviewer and authority.
- Review date.
- Risk class.
- Applied review dimensions.
- State of each dimension.
- Findings.
- Evidence references.
- Outcome.
- Conditions.
- Required approvals.
- Deferred-decision dependencies.

13.2. Review records SHALL be durable and discoverable according to approved knowledge and evidence controls.

13.3. Until UD-009 and UD-010 are resolved, review records SHALL disclose material dependence on unresolved evidence-storage, retention, integrity, or agent-log boundaries.

13.4. A review record MUST NOT expose restricted or sensitive information beyond authorized need.

# 14. Review Sequencing

14.1. The default review sequence SHALL be:

1. Scope and completeness.
2. Requirement fidelity.
3. Decision and authority.
4. Architecture.
5. Dependencies and impact.
6. Duplication and reuse.
7. Security and compliance.
8. Data integrity.
9. Compatibility and migration.
10. Operations and recovery.
11. Documentation and consistency.
12. Verification and evidence.
13. Product Owner decision completeness.
14. Presentation readiness.

14.2. Review sequence MAY be adapted when risk, artifact type, incident conditions, or dependency order requires another sequence.

14.3. Sequence adaptation SHALL NOT omit an applicable mandatory review dimension.

# 15. Cross-Standard Boundaries

15.1. KEP-PO-001 SHALL govern Product Owner decision routing and interruption boundaries.

15.2. KEP-REV-001 SHALL govern review method, findings, states, and approval readiness.

15.3. KEP-COM-001 SHALL govern presentation of reviewed results after it becomes effective.

15.4. A future KEP-QUAL standard SHALL define broader risk-specific quality-gate profiles, evidence profiles, approver matrices, and related quality mechanisms.

15.5. This standard SHALL consume approved quality-gate rules and MUST NOT preempt unresolved quantitative thresholds.

15.6. A future DOC standard MAY define authoritative representation, document lifecycle, and publication synchronization without changing review obligations established here unless this standard is amended.

# 16. Exceptions and Nonconformance

16.1. Exceptions SHALL comply with KEP-002 and applicable subordinate exception standards.

16.2. An exception to a review requirement SHALL identify the exact rule, scope, risk, compensating controls, owner, approving authority, effective period, and exit condition.

16.3. An undocumented omitted review is not an approved exception.

16.4. A constitutional, legal, contractual, or human-accountability obligation MUST NOT be waived through ordinary review approval.

16.5. Review nonconformance SHALL be classified under applicable KEP nonconformance rules.

16.6. Repeated review failures SHOULD trigger process, template, agent-instruction, training, architecture, or governance review.

# 17. Conformance

17.1. A review conforms to this standard when:

- Scope is declared.
- Governing authority is identified.
- Applicable requirements are identified.
- Risk is classified or explicitly pending.
- Required dimensions are identified.
- Every applied dimension has a valid state.
- Findings are actionable and traceable.
- Evidence supports conclusions.
- Approval authority is preserved.
- Deferred-decision dependencies are disclosed.
- Outcome and conditions are explicit.
- Unsupported claims are absent.

17.2. A review that omits a mandatory dimension without approved justification is nonconforming.

17.3. A review that claims unperformed checks is a material truthfulness defect.

17.4. A malformed or incomplete review MAY be returned for correction without reopening the reviewed artifact's underlying product or engineering decisions.

# 18. Review of This Standard

18.1. Before approval, this standard SHALL undergo:

- Constitutional consistency review.
- Authority and precedence review.
- Duplication review against KEP-000, KEP-001, KEP-001A, and KEP-002.
- Cross-standard review against KEP-GOV-002 and KEP-PO-001.
- Risk-proportionality review.
- Evidence-boundary review for UD-009 and UD-010.
- Quantitative-boundary review for UD-011.
- Conflict-and-appeal boundary review for UD-014.
- Product-independence review.
- AI-operating compatibility review.
- Operational usability review.

18.2. Review findings SHALL be resolved, accepted through valid authority, or explicitly recorded before approval.

# 19. Implementation Requirements

19.1. Approval of this standard SHALL establish the review dimensions, states, findings, outcomes, and review duties defined here.

19.2. Approval SHALL NOT by itself create schemas, templates, automation, CI gates, evidence stores, retention policies, reviewer appointments, or approver matrices.

19.3. After approval, KEP MAY separately authorize:

- Review templates.
- Finding schemas.
- Review record schemas.
- Artifact-specific review profiles.
- Risk-specific quality-gate profiles.
- Repository validators.
- AI review instructions.
- CI enforcement.

19.4. Implementing artifacts SHALL trace to this standard and MUST NOT add authority or obligations not established by approved governance.

# 20. Approval Conditions

This standard became effective when:

1. Required reviews were completed.
2. No unresolved constitutional conflict remained.
3. Deferred-decision boundaries were preserved.
4. The Founding Authority approved Version 1.0.
5. The effective date was recorded.
6. The canonical representation was published.
7. KEP-REG-GOV-001 was updated from Draft to Effective.
8. KEP-COM-001 remained sequenced after approval of this standard.

# 21. Approval Record

| Field | Value |
| --- | --- |
| Document | KEP-REV-001 — Engineering Review Standard |
| Version | 1.0 |
| Approval Authority | Founding Authority |
| Approved By | Kashif Muhammad Younus |
| Approval Date | July 25, 2026 |
| Effective Date | July 25, 2026 |
| Decision | Approved |
| Durable Approval Record | `docs/00-governance/approvals/KEP-REV-001-v1.0-approval-record.md` |

# 22. Revision History

| Version | Date | Status | Summary |
| --- | --- | --- | --- |
| 1.0 | July 25, 2026 | Effective | Initial engineering review dimensions, review states, findings, risk-proportional controls, specification review, approval outcomes, records, sequencing, and conformance requirements. Approved by the Founding Authority; metadata synchronized without normative change. |
