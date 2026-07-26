**Authoritative Representation:**  
This Markdown document is the canonical human-readable approved representation of this KEP artifact.

# KEP-COM-001 — Engineering Communication Standard

| Document Control | Value |
| --- | --- |
| Document ID | KEP-COM-001 |
| Title | Engineering Communication Standard |
| Domain | COM |
| Artifact Class | Subordinate standard |
| Status | Effective |
| Version | 1.0 |
| Governing Authority | KEP-002 — Engineering Constitution |
| Foundational Sources | KEP-000, KEP-001, KEP-001A, KEP-GOV-002, KEP-PO-001, KEP-REV-001 |
| Accountable Owner | Governance Steward |
| Approval Authority | Founding Authority |
| Effective Date | July 25, 2026 |
| Review Cadence | Every six months and immediately upon a material communication, review, authority, AI-operating, or decision-routing change |
| Amendment Path | Controlled amendment under applicable KEP governance |
| Supersedes | None |
| Related Standards | KEP-GOV-002; KEP-PO-001; KEP-REV-001; planned KEP-AI and KEP-DOC standards |
| Deferred-Decision Dependencies | UD-010 may affect future retention of intermediate AI execution records; this standard does not resolve that boundary |

Product-independent. Technology-neutral. Evidence-governed. Decision-focused.

## Normative Language

MUST and SHALL express mandatory obligations. MUST NOT and SHALL NOT express prohibitions. SHOULD expresses the expected default and requires recorded rationale for material deviation. MAY expresses permission within applicable authority and constraints. Material retains the meaning established by KEP-002.

# 1. Purpose

1.1. This standard SHALL define how material engineering information, findings, recommendations, decisions, approvals, risks, assumptions, status, and required actions are communicated under KEP.

1.2. This standard SHALL operationalize KEP requirements for direct, precise, structured, evidence-based, truthful, decision-focused, and risk-aware communication.

1.3. This standard SHALL establish final-answer readiness, communication status, information classification, recommendation closure, action clarity, self-reference limits, terminology consistency, and AI-assisted presentation requirements.

1.4. This standard SHALL govern presentation of reviewed results produced under KEP-REV-001 and Product Owner interactions governed by KEP-PO-001.

1.5. This standard SHALL NOT redefine review approval, Product Owner authority, constitutional authority, evidence-retention boundaries, or private internal reasoning requirements.

# 2. Authority and Precedence

2.1. This standard derives its authority from KEP-002 and SHALL be interpreted consistently with KEP-000, KEP-001, KEP-001A, KEP-GOV-002, KEP-PO-001, and KEP-REV-001.

2.2. Applicable law and binding contractual obligations SHALL retain superior authority.

2.3. Communication MUST NOT alter, waive, expand, or imply authority that has not been granted by an applicable governing instrument.

2.4. A communication format, template, model behavior, tool default, repeated practice, or recipient preference MUST NOT override higher-authority requirements.

2.5. A communication that conflicts with a higher authority SHALL identify the conflict and MUST NOT present the lower-level position as controlling.

# 3. Scope

3.1. This standard SHALL apply to material engineering communication, including:

- Requirements and specification communication.
- Architecture recommendations and decisions.
- Review findings and outcomes.
- Product Owner decision requests.
- Risk and compliance communication.
- Implementation instructions.
- Status reports.
- Release and operational communication.
- Incident and corrective-action communication.
- AI-assisted engineering responses.
- Approval, rejection, blocking, and deferral notices.

3.2. This standard SHALL apply to human-to-human, human-to-AI, AI-to-human, and AI-assisted communication within KEP-governed work.

3.3. Communication depth SHALL scale with materiality, risk, audience, decision need, and artifact type.

3.4. This standard SHALL NOT require every communication category or heading for every message.

3.5. Trivial or purely administrative communication MAY use a reduced form when no material fact, decision, risk, approval, or engineering consequence is obscured.

# 4. Core Communication Principles

## 4.1 Truthful Classification

4.1.1. Material communication SHALL distinguish applicable categories, including:

- Verified fact.
- Source-derived statement.
- Analysis.
- Inference.
- Assumption.
- Recommendation.
- Decision.
- Approval.
- Risk.
- Uncertainty.
- Open question.
- Deferred work.
- Blocked work.
- Verified result.

4.1.2. A recommendation, assumption, inference, draft, unexecuted check, or incomplete artifact MUST NOT be represented as an approved decision or verified result.

4.1.3. A source-derived statement SHALL identify or reference its authoritative source when material.

4.1.4. An inference SHALL be presented as an inference and SHALL identify the supporting facts or sources where material.

## 4.2 Evidence Before Assertion

4.2.1. Claims of completion, correctness, security, compatibility, compliance, performance, readiness, or approval SHALL reference appropriate evidence or authority.

4.2.2. Confidence, seniority, fluency, length, or persuasive tone MUST NOT substitute for evidence.

4.2.3. A check that was not performed MUST NOT be stated or implied as passed.

4.2.4. A communication SHALL disclose material evidence limitations.

## 4.3 Decision and Outcome Focus

4.3.1. Material communication SHALL focus on the intended outcome, decision, risk, action, or verified status.

4.3.2. Background information SHOULD be included only when it changes understanding, supports evidence, explains a trade-off, preserves traceability, or enables action.

4.3.3. A response MUST NOT bury the required decision or action beneath unnecessary narrative.

4.3.4. A communication SHALL identify whether the recipient is expected to approve, decide, review, correct, execute, acknowledge, or take no action.

## 4.4 High Information Density

4.4.1. Communication SHALL use the shortest form that preserves material correctness, context, evidence, authority, risk, and decision clarity.

4.4.2. Concision MUST NOT remove information required for safe engineering action or accountable approval.

4.4.3. Repetition SHALL be limited to information required for:

- Decision clarity.
- Risk emphasis.
- Legal or contractual notice.
- Security or operational safety.
- Cross-reference integrity.
- Required action separation.

4.4.4. Repetition that adds no new information, decision value, evidence, or safety value SHOULD be removed.

## 4.5 Stable Terminology

4.5.1. Communication SHALL use terminology established by authoritative product, domain, architecture, repository, and governance sources.

4.5.2. A communicator MUST NOT silently replace established terminology with an approximate synonym when the substitution could change meaning, authority, scope, or traceability.

4.5.3. A new term SHALL be defined when it is materially necessary and no authoritative term exists.

4.5.4. Conflicting terminology SHALL be identified and resolved or explicitly recorded.

# 5. Communication Status Model

5.1. Material communication SHALL use one of the following statuses when status is not otherwise self-evident:

| Status | Meaning |
| --- | --- |
| Final for Scope | Reviewed communication is complete for the approved request and current evidence |
| Decision Required | A named authority must make a defined decision before dependent work can proceed or close |
| Review Required | The artifact or conclusion is prepared but requires applicable review before approval or authoritative use |
| Blocked | Progress or conclusion is prevented by a missing dependency, authority, access, evidence, or decision |
| Deferred | Work or decision is intentionally postponed under a defined boundary |
| Draft Requested | Unreviewed or collaboratively evolving material is being presented because a draft was explicitly requested |
| Informational | No decision or action is required unless otherwise stated |
| Superseded | The communication has been replaced by a later authoritative communication or artifact |

5.2. Status SHALL be truthful and consistent with KEP-REV-001 review state and approval outcome.

5.3. Final for Scope SHALL NOT mean defect-free, permanently immutable, or guaranteed correct.

5.4. A communication MUST NOT use Final for Scope while a known mandatory review, decision, or evidence requirement remains silently incomplete.

5.5. A blocked or deferred status SHALL identify the blocking condition or deferral boundary when material.

5.6. Draft Requested SHALL NOT imply approval, implementation authorization, or authoritative status.

# 6. Final-Answer Principle

6.1. A response presented as Final for Scope SHALL:

1. Address the approved request.
2. Present the reviewed conclusion or deliverable.
3. Identify applicable authority and sources where material.
4. Separate material facts, assumptions, analysis, recommendations, risks, and decisions.
5. Disclose known material limitations and uncertainty.
6. Identify unresolved required decisions.
7. Identify blocked or unverified elements.
8. State the required recipient action or state that no action is required.
9. Avoid introducing a new material recommendation after closure.

6.2. Final for Scope SHALL be determined against the requested scope, governing requirements, current evidence, and completed review.

6.3. A final response MUST NOT be padded with speculative future work, unrelated alternatives, motivational language, or performative assurances.

6.4. A final response MAY identify a separately scoped next phase when that phase is already approved, logically required, or explicitly requested.

6.5. A final response MUST NOT imply that optional future work is required unless a governing requirement, risk, or dependency makes it necessary.

# 7. Recommendation Standard

7.1. A material recommendation SHALL identify:

1. The recommended option.
2. The problem or decision addressed.
3. Governing constraints.
4. Principal rationale.
5. Material trade-offs.
6. Principal risks.
7. Dependencies.
8. Required authority.
9. Reconsideration trigger where applicable.

7.2. Recommendations SHALL be consolidated before presentation.

7.3. A communicator SHOULD present one recommended option when one option is materially superior under approved constraints.

7.4. Multiple alternatives SHALL be presented when they produce materially different product, architecture, risk, cost, legal, operational, or schedule outcomes requiring authorized selection.

7.5. Technically equivalent alternatives MUST NOT be transferred to the Product Owner merely because engineering has not selected among them.

7.6. A recommendation SHALL NOT be represented as a decision until approved by the applicable authority.

# 8. Recommendation and Decision Closure

8.1. A recommendation or decision SHALL be treated as closed within its approved scope when:

- The required authority has decided.
- The scope is clear.
- Material conditions are recorded.
- Required dependent approvals are identified.
- No mandatory unresolved issue prevents closure.

8.2. A closed recommendation or decision MUST NOT be reopened solely because a contributor or AI agent prefers another option.

8.3. Reopening SHALL require at least one valid trigger:

- New material evidence.
- Changed requirement.
- Changed scope.
- Changed risk.
- Higher-authority conflict.
- Recorded reconsideration trigger.
- Material implementation defect.
- Expiry or supersession.

8.4. A final answer MUST NOT append a new material recommendation after closure unless a valid reopening trigger is identified.

8.5. A separate future recommendation MAY be recorded as deferred work when it does not alter the closed decision and is clearly outside the current scope.

# 9. Required Action Clarity

9.1. Material communication SHALL clearly separate, as applicable:

- Decisions required now.
- Recipient actions.
- Product Owner actions.
- Engineering actions.
- Reviewer actions.
- Actions assigned to another authority.
- Information provided for awareness.
- Blocked work.
- Deferred work.
- Completed work.

9.2. A request for information SHALL NOT be represented as a request for approval.

9.3. A request for review SHALL NOT be represented as a request for implementation authorization unless the reviewer has that authority.

9.4. Approval by one authority MUST NOT be represented as approval by another.

9.5. A deadline SHALL be stated only when grounded in an actual dependency, obligation, schedule, expiry, or risk condition.

9.6. Silence MUST NOT be treated as approval unless an approved governance mechanism expressly authorizes that effect.

# 10. Structure and Presentation

10.1. Material communication SHOULD use stable headings or labels appropriate to the task.

10.2. Applicable headings MAY include:

- Status.
- Facts.
- Sources.
- Analysis.
- Assumptions.
- Risks.
- Recommendation.
- Decision.
- Required Action.
- Verification.
- Blockers.
- Deferred Work.

10.3. Headings SHALL be used to improve clarity and MUST NOT become ceremonial duplication.

10.4. Communication MAY use tables when comparison, traceability, authority, status, or structured findings are clearer in tabular form.

10.5. Tables MUST NOT be used when they obscure narrative reasoning, create excessive width, or reduce accessibility.

10.6. Long communication SHALL use a logical hierarchy and SHALL avoid repeating the same conclusion in multiple sections without a functional reason.

# 11. Self-Reference and Performative Language

11.1. Engineering communication MUST NOT contain performative self-reference that does not contribute evidence, authority, accountability, or decision value.

11.2. Prohibited performative self-reference includes unsupported declarations of:

- Expertise.
- Commitment.
- Confidence.
- Thoroughness.
- Professionalism.
- Personal responsibility not formally assigned.
- Compliance without demonstrated evidence.

11.3. Necessary authorship, reviewer identity, accountable ownership, role assignment, limitation disclosure, or conflict disclosure MAY be stated.

11.4. A communicator MAY explain method when the method is relevant to reproducibility, evidence, auditability, or recipient understanding.

11.5. A communicator MUST NOT use self-description as a substitute for demonstrating quality through the deliverable.

# 12. Draft and Intermediate Material

12.1. Reviewed deliverables SHALL be presented by default.

12.2. Unreviewed intermediate generation, scratch work, private reasoning, or exploratory drafting MUST NOT be presented as a final deliverable.

12.3. A collaborative draft MAY be presented when:

- The recipient explicitly requests a draft.
- The task is an approved working session.
- Material alternatives require collaborative development.
- A decision cannot be made without exposing an incomplete structure.

12.4. A presented draft SHALL identify:

- Draft status.
- Scope.
- Known omissions.
- Unresolved decisions.
- Review not yet performed.
- Prohibited reliance where applicable.

12.5. Draft suppression MUST NOT conceal uncertainty, defects, blocked work, or missing evidence in a reviewed deliverable.

12.6. This standard does not establish retention requirements for intermediate AI execution records reserved under UD-010.

# 13. Facts, Analysis, and Assumptions

13.1. Verified facts SHALL be supported by observed evidence or authoritative sources.

13.2. Analysis SHALL explain the relevant relationship between facts, requirements, constraints, options, or risks.

13.3. Assumptions SHALL be explicit when they materially affect the conclusion, recommendation, decision, estimate, or implementation.

13.4. A material assumption SHALL identify, where applicable:

- Why it is necessary.
- Its owner.
- Its boundary.
- Its risk.
- Its confirmation or reconsideration condition.

13.5. An assumption MUST NOT be silently converted into a product requirement, architecture decision, approval, or verified fact.

13.6. Uncertainty SHALL be stated directly and proportionately.

# 14. Risk Communication

14.1. Material risk communication SHALL identify:

- Risk condition.
- Potential impact.
- Affected scope.
- Likelihood or uncertainty where supportable.
- Reversibility.
- Mitigation or compensating control.
- Owner.
- Required decision or action.

14.2. Risk severity MUST NOT be exaggerated to pressure a decision or understated to avoid review.

14.3. Unsupported urgency MUST NOT be used to obtain approval.

14.4. R3 and R4 communication SHALL identify all independently required authorities and MUST NOT rely on Product Owner approval alone.

14.5. Legal, contractual, security, financial, identity, safety, or regulated-data risks SHALL be communicated without fabricating conclusions outside the communicator's authority or evidence.

# 15. Review Findings and Outcomes

15.1. Communication of review results SHALL conform to KEP-REV-001.

15.2. A material finding communication SHALL identify:

- Finding identifier.
- Affected artifact or location.
- Observed condition.
- Impact.
- Governing requirement.
- Evidence.
- Severity.
- Owner.
- Required disposition.
- Status.

15.3. Review outcome communication SHALL identify:

- Review scope.
- Artifact and version.
- Applied review dimensions.
- Material findings.
- Outcome.
- Conditions.
- Required approvals.
- Deferred-decision dependencies.

15.4. Approved with Recorded Conditions MUST NOT be communicated as unconditional approval.

15.5. Advisory review MUST NOT be communicated as approval.

# 16. Product Owner Communication

16.1. Product Owner communication SHALL conform to KEP-PO-001.

16.2. A Product Owner decision request SHALL identify the exact decision, authority basis, options, recommendation, trade-offs, risks, dependencies, delay consequence, other required authorities, and effect of no decision.

16.3. Product Owner communication SHALL minimize unnecessary interruption by completing bounded engineering analysis before escalation.

16.4. Routine engineering decisions MUST NOT be presented as Product Owner choices.

16.5. Product Owner approval SHALL NOT be represented as sufficient for independently required architecture, security, quality, legal, release, governance, or operational approval.

16.6. Closed Product Owner decisions SHALL be communicated as closed unless a valid reopening trigger exists.

# 17. AI-Assisted Communication

17.1. AI-generated engineering communication SHALL comply with the same truthfulness, evidence, authority, review, risk, and status requirements as human-produced communication.

17.2. An AI agent MUST NOT claim that it:

- Read a source it did not access.
- Executed a command it did not execute.
- Inspected a result it did not inspect.
- Performed a review it did not perform.
- Obtained an approval that was not granted.
- Completed work that remains incomplete.

17.3. AI communication SHALL distinguish verified fact, source-derived statement, inference, assumption, recommendation, uncertainty, and incomplete work.

17.4. AI agents SHALL present the reviewed deliverable rather than expose private internal reasoning or unreviewed intermediate generation.

17.5. AI agents MAY provide a concise reasoning summary, evidence trail, or decision rationale sufficient for review without exposing private internal reasoning.

17.6. AI agents MUST NOT silently resolve a material ambiguity, authority conflict, missing requirement, or deferred decision.

17.7. AI agents SHALL use stable terminology and communication behavior across projects while respecting stricter project-specific rules that do not conflict with higher authority.

17.8. AI-generated confidence, simulated consensus, or persuasive fluency MUST NOT be used as evidence.

# 18. Prohibited Communication Patterns

The following are prohibited:

18.1. Representing incomplete or unverified work as complete.

18.2. Presenting a recommendation as an approved decision.

18.3. Claiming a review or check that was not performed.

18.4. Adding a new material recommendation after a response has been presented as final without a valid reopening trigger.

18.5. Asking an authority to repeat a decision already recorded and closed without a valid trigger.

18.6. Using unnecessary self-reference, motivational language, or declarations of commitment in place of evidence or action.

18.7. Repeating the same conclusion without decision, risk, evidence, legal, operational, or traceability value.

18.8. Concealing uncertainty, assumptions, blocked work, or material limitations.

18.9. Treating silence, attendance, acknowledgement, or lack of objection as approval without governing authority.

18.10. Using technically equivalent alternatives to transfer engineering responsibility to the Product Owner.

18.11. Using unsupported urgency, fear, confidence, or simulated consensus to pressure approval.

18.12. Presenting a draft as approved, authoritative, implementation-ready, or production-ready.

# 19. Communication Conformance

19.1. Material communication conforms to this standard when:

- Its status is truthful.
- Applicable information categories are distinguishable.
- Claims are supported by evidence or authority.
- Assumptions and uncertainty are explicit.
- Recommendations and decisions remain distinct.
- Required action is clear.
- Risks and dependencies are disclosed.
- Terminology is consistent.
- Review state is accurately represented.
- Product Owner and other authority boundaries are preserved.
- Unnecessary repetition and performative self-reference are absent.
- Final-answer closure rules are satisfied.

19.2. A communication that falsely claims completion, verification, review, approval, or authority is materially nonconforming.

19.3. A communication that is structurally imperfect but materially truthful and actionable MAY be corrected without reopening the underlying approved decision.

19.4. Repeated communication nonconformance SHOULD trigger review of templates, agent instructions, training, workflow, or governance controls.

# 20. Cross-Standard Boundaries

20.1. KEP-PO-001 SHALL govern decision routing, Product Owner interruption, and Product Owner authority.

20.2. KEP-REV-001 SHALL govern review method, findings, review states, outcomes, and presentation-readiness review.

20.3. KEP-COM-001 SHALL govern presentation of reviewed conclusions, decisions, actions, risks, and status.

20.4. A future KEP-AI standard MAY establish broader AI operating controls without weakening communication obligations established here.

20.5. A future KEP-DOC standard MAY establish publication, document lifecycle, and representation synchronization without changing the communication obligations established here unless this standard is amended.

20.6. A future KEP-TMP standard MAY govern templates, but a template MUST NOT replace engineering judgment or create authority.

# 21. Exceptions and Nonconformance

21.1. Exceptions SHALL comply with KEP-002 and applicable subordinate exception standards.

21.2. An exception SHALL identify the exact rule, scope, risk, compensating controls, owner, approving authority, effective period, and exit condition.

21.3. An undocumented communication deviation is not an approved exception.

21.4. Truthfulness, human accountability, higher authority, and evidence integrity MUST NOT be waived through an ordinary communication exception.

21.5. Communication nonconformance SHALL be classified under applicable KEP nonconformance rules.

# 22. Review of This Standard

22.1. Before approval, this standard SHALL undergo:

- Constitutional consistency review.
- Authority and precedence review.
- Duplication review against KEP-000, KEP-001, KEP-001A, and KEP-002.
- Cross-standard review against KEP-GOV-002, KEP-PO-001, and KEP-REV-001.
- Final-answer principle review.
- Recommendation-closure review.
- Product Owner interaction compatibility review.
- AI-operating compatibility review.
- Information-density and usability review.
- Product-independence review.
- UD-010 boundary review.

22.2. Review findings SHALL be resolved, accepted through valid authority, or explicitly recorded before approval.

# 23. Implementation Requirements

23.1. Approval of this standard SHALL establish the communication classifications, statuses, final-answer rules, recommendation rules, closure rules, action clarity, self-reference limits, and AI presentation requirements defined here.

23.2. Approval SHALL NOT by itself create templates, schemas, automation, repository enforcement, agent-instruction updates, or retention policies.

23.3. After approval, KEP MAY separately authorize:

- Communication templates.
- Decision-request templates.
- Status schemas.
- Agent-contract updates.
- Repository guidance.
- Communication linting.
- Automated metadata validation.
- Conformance checklists.

23.4. Implementing artifacts SHALL trace to this standard and MUST NOT add authority or obligations not established by approved governance.

# 24. Approval Conditions

This standard became effective when:

1. Required reviews were completed.
2. No unresolved constitutional conflict remained.
3. KEP-PO-001 and KEP-REV-001 remained effective and correctly referenced.
4. UD-010 boundaries remained preserved.
5. The Founding Authority approved Version 1.0.
6. The approval and effective dates were recorded as July 25, 2026.
7. The canonical representation was published.
8. KEP-REG-GOV-001 was updated from Draft to Effective.

# 25. Approval Record

| Field | Value |
| --- | --- |
| Document | KEP-COM-001 — Engineering Communication Standard |
| Version | 1.0 |
| Approval Authority | Founding Authority |
| Approved By | Kashif Muhammad Younus |
| Approval Date | July 25, 2026 |
| Effective Date | July 25, 2026 |
| Decision | Approved and Effective |
| Durable Approval Record | `docs/00-governance/approvals/KEP-COM-001-v1.0-approval-record.md` |

# 26. Revision History

| Version | Date | Status | Summary |
| --- | --- | --- | --- |
| 1.0 | July 25, 2026 | Effective | Initial engineering communication classifications, status model, final-answer principle, recommendation and closure rules, action clarity, self-reference controls, draft handling, risk communication, AI presentation, prohibited patterns, and conformance requirements. Approved by the Founding Authority. |
