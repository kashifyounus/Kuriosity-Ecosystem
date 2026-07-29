**Authoritative Representation:**  
This Markdown document is the canonical human-readable normative representation of this KEP artifact.

# KEP-GOV-002 — Standards Taxonomy and Naming Standard

| Document Control | Value |
| --- | --- |
| Document ID | KEP-GOV-002 |
| Title | Standards Taxonomy and Naming Standard |
| Domain | GOV |
| Artifact Class | Subordinate standard |
| Status | Effective |
| Version | 1.0 |
| Governing Authority | KEP-002 — Engineering Constitution |
| Foundational Sources | KEP-000, KEP-001, KEP-001A |
| Accountable Owner | Governance Steward |
| Approval Authority | Founding Authority |
| Approved By | Kashif Muhammad Younus |
| Approval Date | July 25, 2026 |
| Effective Date | July 25, 2026 |
| Review Cadence | Every six months and immediately upon a material taxonomy, authority, repository, or standards-lifecycle change |
| Amendment Path | Controlled amendment under applicable KEP governance |
| Supersedes | None |
| Related Artifacts | KEP-GOV-001, KEP-PO-001, KEP-REV-001, KEP-COM-001, KEP-REG-GOV-001 |

Product-independent. Technology-neutral. Evidence-governed.

## Normative Language

MUST and SHALL express mandatory obligations. MUST NOT and SHALL NOT express prohibitions. SHOULD expresses the expected default and requires recorded rationale for material deviation. MAY expresses permission within applicable authority and constraints. Material retains the meaning established by KEP-002.

# 1. Purpose

1.1. This standard SHALL establish the permanent classification, naming, identifier, registration, and lifecycle rules for KEP subordinate standards.

1.2. This standard SHALL prevent inconsistent naming, identifier reuse, namespace collision, artifact-class ambiguity, and uncontrolled creation of standards domains.

1.3. This standard SHALL distinguish binding subordinate standards from audits, reports, specifications, decisions, templates, playbooks, skills, schemas, registers, and other governed artifacts.

1.4. This standard SHALL provide a taxonomy usable consistently by humans, AI agents, repositories, schemas, tools, and verification systems.

1.5. This standard SHALL NOT redefine constitutional authority, precedence, human accountability, or the R0–R4 risk model.

# 2. Authority and Precedence

2.1. This standard derives its authority from KEP-002.

2.2. This standard SHALL remain subordinate to applicable law, binding contractual obligations, KEP-002, KEP-000, and KEP-001 together with KEP-001A.

2.3. A taxonomy rule MUST NOT override a higher authority.

2.4. A repository convention, tool default, AI-generated identifier, template, prototype, or repeated practice MUST NOT create or change an approved KEP artifact class or domain code.

2.5. A conflict with higher authority SHALL be resolved in favor of the higher authority and recorded for controlled correction.

# 3. Scope

3.1. This standard SHALL govern subordinate-standard identifiers, standards-domain codes, artifact-class prefixes, sequential numbering, version relationships, identifier lifecycle, standards registration, domain-code creation and retirement, naming validation, cross-reference naming, and legacy identifier treatment.

3.2. This standard SHALL apply to the canonical KEP repository, KEP platform governance, KEP-adopting projects when publishing or referencing platform-level KEP standards, human contributors, AI-assisted agents, repository automation, validation schemas, documentation generators, and standards catalogs.

3.3. This standard SHALL NOT determine substantive requirements, product-specific naming, source-code namespaces, database naming, API naming, branch naming, or commit-message conventions.

3.4. Product-specific standards SHALL remain outside the KEP namespace unless formally adopted as KEP-wide standards.

# 4. Taxonomy Principles

4.1. An approved identifier SHALL remain stable for the lifetime of its artifact.

4.2. Each approved identifier SHALL be globally unique within its artifact-class namespace.

4.3. An identifier SHALL NOT be reused after withdrawal, rejection, supersession, retirement, deprecation, archival, or formal abandonment.

4.4. Every governed artifact SHALL declare its artifact class.

4.5. The taxonomy MAY be extended only through a demonstrated classification need, defined scope, non-duplication analysis, accountable ownership, governance approval, and registry update.

4.6. Identifiers SHALL use uppercase ASCII letters, digits, and hyphens only and SHALL remain deterministically parseable.

# 5. Subordinate Standard Identifiers

5.1. A subordinate standard SHALL use `KEP-<DOMAIN>-<SEQUENCE>`.

5.2. `KEP` identifies the Kuriosity Engineering Platform, `<DOMAIN>` is an approved standards-domain code, and `<SEQUENCE>` is a three-digit sequence unique within that domain.

5.3. Valid examples include `KEP-GOV-002`, `KEP-COM-001`, `KEP-REV-001`, `KEP-PO-001`, `KEP-ARCH-001`, and `KEP-SEC-001`.

5.4. Version, lifecycle state, and publication status SHALL NOT appear in the identifier.

5.5. Sequences SHALL contain exactly three digits, SHALL be allocated monotonically within the domain, MAY contain gaps, and SHALL NOT be backfilled through identifier reuse.

5.6. Parallel drafting SHALL reserve identifiers before publication.

5.7. A revised standard SHALL retain its identifier and receive a new version. A materially different standard SHALL receive a new identifier unless a controlled major-version amendment preserves valid continuity.

# 6. Standards Domain Registry

The following domain codes are approved:

| Code | Domain | Scope |
| --- | --- | --- |
| GOV | Governance | Authority, lifecycle, ratification, precedence, taxonomy, ownership, exceptions, and conformance governance |
| COM | Engineering Communication | Communication structure, status, final-answer readiness, closure, and information quality |
| REV | Engineering Review | Review dimensions, findings, reviewer duties, evidence, and approval readiness |
| PO | Product Owner Interaction | Product decision boundaries, routing, escalation, interruption control, and participation |
| DOC | Documentation and Knowledge | Authoritative sources, documentation lifecycle, discoverability, and representation control |
| ARCH | Architecture | Architecture methods, decisions, boundaries, dependency direction, conformance, and evolution |
| AI | AI Engineering | Agent contracts, context, permissions, execution, validation, and AI-specific governance |
| SEC | Security | Security architecture, identity, authorization, confidentiality, vulnerability management, and secure engineering |
| QUAL | Quality and Verification | Quality gates, verification profiles, evidence requirements, and quality controls |
| TMP | Templates | Governed template design, use, ownership, lifecycle, and conformance |
| REQ | Requirements | Requirements engineering, traceability, acceptance criteria, quality, and change control |
| DATA | Data Engineering | Data contracts, ownership, lifecycle, integrity, migration, and consistency |
| REL | Release | Release readiness, authority, evidence, compatibility, rollback, and release records |
| OPS | Operations | Operability, observability, incident response, recovery, and decommissioning |
| INT | Integration | Interface contracts, interoperability, external dependencies, messaging, and resilience |
| EVD | Evidence and Records | Evidence format, provenance, integrity, linkage, retention, and records governance |
| REP | Repository Engineering | Repository structure, contracts, contribution rules, local clarity, and automation |
| COMP | Compliance | Legal, regulatory, contractual, privacy, accessibility, and domain-compliance controls |

6.1. A standard SHALL be assigned to the domain representing its principal normative purpose.

6.2. A standard MAY reference multiple domains but SHALL have one primary domain identifier.

6.3. A standard MUST NOT be duplicated across domains solely because it has cross-domain effects.

6.4. GOV SHALL NOT be used as a default category when another approved domain owns the primary subject.

6.5. Domain reservation SHALL NOT imply approval or implementation of a standard.

6.6. EVD requirements concerning storage, retention, integrity, or agent-record retention SHALL remain subject to UD-009 and UD-010.

# 7. Artifact Classes

| Artifact Class | Purpose | Identifier Pattern |
| --- | --- | --- |
| Constitutional instrument | Foundational or constitutional authority | Existing constitutional numbering |
| Subordinate standard | Binding operational requirements | `KEP-<DOMAIN>-<NNN>` |
| Governance decision | Bounded governance decision | `KEP-GOV-DEC-<NNN>` |
| Architecture decision | Material architecture decision | `KEP-ADR-<NNN>` |
| Audit | Independent assessment and findings | `KEP-AUD-<DOMAIN>-<NNN>` |
| Specification | Detailed engineering or implementation contract | `KEP-SPEC-<DOMAIN>-<NNN>` |
| Template | Governed reusable artifact structure | `KEP-TMP-<NNN>` |
| Playbook | Coordinated recurring workflow | `KEP-PB-<DOMAIN>-<NNN>` |
| Skill | Reusable governed execution capability | `KEP-SKILL-<DOMAIN>-<NNN>` |
| Report | Evidence, status, outcome, or analysis report | `KEP-RPT-<DOMAIN>-<NNN>` |
| Schema | Machine-readable validation contract | `KEP-SCH-<DOMAIN>-<NNN>` |
| Register | Controlled collection of governed records | `KEP-REG-<DOMAIN>-<NNN>` |

7.1. An audit SHALL NOT be classified as a standard.

7.2. A report SHALL NOT create binding requirements unless those requirements are separately approved through an authorized standard or higher instrument.

7.3. A template SHALL NOT acquire normative authority through repeated use.

7.4. A specification SHALL NOT supersede a standard unless applicable authority explicitly permits that relationship.

7.5. An architecture decision SHALL govern its approved scope but SHALL NOT amend higher governance.

7.6. A skill, playbook, schema, tool, or register SHALL implement approved rules and SHALL NOT invent binding governance.

# 8. Legacy Identifier Treatment

8.1. `KEP-GOV-001` is already assigned to the Governance Baseline Audit, a non-normative audit artifact.

8.2. KEP-GOV-001 SHALL be recorded as a legacy identifier exception and SHALL NOT establish precedent for future artifact-class mixing.

8.3. This standard SHALL NOT retroactively rename KEP-GOV-001.

8.4. A later document-control standard MAY authorize migration or aliasing only when historical traceability, references, commit history, finding identifiers, status, and evidence provenance are preserved.

8.5. Other pre-standard nonconforming identifiers MAY be retained but SHALL be entered in a legacy register and SHALL NOT be silently normalized.

# 9. Titles and Filenames

9.1. Every subordinate standard SHALL have an official title describing the governed subject without marketing language or implementation-specific branding.

9.2. The identifier and title SHALL appear together at the start of the standard.

9.3. The canonical repository filename SHOULD follow `<document-id>-<normalized-title>.md` using the repository's approved case convention.

9.4. Publication filenames MAY include version and status, but filename text SHALL NOT replace canonical metadata.

# 10. Lifecycle States

A subordinate standard SHALL use one of these states: Proposed, Draft, Review Ready, Approval Pending, Approved, Effective, Suspended, Superseded, Withdrawn, Retired, or Rejected.

10.1. Status SHALL be explicit and truthful.

10.2. A draft MUST NOT be represented as approved or effective.

10.3. Approval SHALL NOT imply effectiveness unless the effective date has occurred.

10.4. Superseded, withdrawn, retired, and rejected artifacts SHALL remain discoverable for traceability unless access must be restricted by superior obligation.

10.5. Status transitions SHALL be recorded in the applicable register.

# 11. Versioning

11.1. Standards SHOULD use `MAJOR.MINOR` document versions.

11.2. A major version SHALL indicate a material normative, scope, authority-interaction, or compatibility change.

11.3. A minor version MAY indicate clarification, compatible new requirements, additional guidance, or non-breaking metadata improvement.

11.4. A meaning-changing revision MUST NOT be represented as editorial only.

11.5. The amendment record SHALL explain whether an identifier was retained or replaced.

# 12. Required Standard Metadata

Every subordinate standard SHALL declare document ID, title, domain, artifact class, status, version, governing authority, foundational sources, accountable owner, approval authority, effective date, applicability, scope, exclusions, review cadence, amendment path, supersession relationships, related standards, deferred-decision dependencies, canonical representation, publication representations, and revision history.

12.1. Missing mandatory metadata SHALL block approval unless an authorized exception applies.

12.2. Metadata SHALL NOT falsely imply approval, ratification, effectiveness, or authority.

12.3. Where multiple representations coexist, the authoritative representation SHALL be declared.

# 13. Standards Register

13.1. KEP SHALL maintain an authoritative standards register.

13.2. The register SHALL record identifier, title, domain, class, status, version, owner, approval authority, effective date, repository path, canonical representation, supersession state, related standards, legacy classification, review date, and deferred-decision dependencies.

13.3. The register SHALL record approved state but MUST NOT independently approve a standard.

13.4. A register entry without approval evidence SHALL NOT make an artifact effective.

13.5. An approved standard omitted from the register SHALL constitute a document-control defect.

13.6. The register SHOULD provide human-readable and machine-readable representations after applicable schemas are approved.

# 14. Domain-Code Governance

14.1. A new domain request SHALL identify the proposed code and name, scope, exclusions, existing domains considered, non-duplication rationale, expected standards, accountable owner, dependencies, migration impact, and approval authority.

14.2. Domain codes SHOULD contain two to five uppercase letters and SHALL be memorable, unambiguous, materially distinct, and non-conflicting with artifact-class prefixes.

14.3. A code MUST NOT be product-specific unless the subject has been generalized and approved as a platform concern.

14.4. A domain MAY be retired through controlled governance. A retired code SHALL remain reserved.

# 15. Standard Classification

Before permanent identifier allocation, a proposed artifact SHALL be evaluated for binding intent, higher-authority coverage, operationalization value, correct artifact class, primary domain, existing-domain fit, constitutional conflict, deferred-decision dependency, overlap, and approval authority.

15.1. A proposal that cannot be classified SHALL NOT receive a permanent identifier.

15.2. A provisional reservation MAY be issued while classification is completed.

# 16. Cross-Standard Coordination

16.1. A standard SHALL identify related standards and define adjacent boundaries.

16.2. A standard MUST NOT reproduce another standard's full requirements where a cross-reference is sufficient.

16.3. A limited restatement MAY be used when needed for local clarity if the controlling source is cited, meaning is preserved, and synchronization risk is controlled.

16.4. A later standard SHALL NOT silently supersede an earlier standard.

16.5. Supersession SHALL be explicit, approved, versioned, and registered.

# 17. Naming Conformance

Before approval, a subordinate standard SHALL pass identifier-format, domain-validity, sequence-uniqueness, artifact-class, title, metadata, collision, legacy-conflict, supersession, and repository-path checks.

17.1. Each check SHALL be Pass, Fail, Blocked, Not Performed, or Not Applicable.

17.2. A check not performed MUST NOT be represented as passed.

17.3. A failed mandatory naming check SHALL block approval unless an authorized exception applies.

17.4. KEP MAY automate taxonomy validation, but automation SHALL enforce approved rules only and MUST NOT invent codes, assign authority, approve standards, or resolve ambiguous classifications.

# 18. Exceptions

18.1. An exception SHALL identify the exact rule, reason, scope, risk, compensating controls, owner, approval authority, review or expiry date, and exit condition.

18.2. An identifier-format exception SHALL NOT create precedent unless this standard is amended.

18.3. An exception SHALL NOT override higher authority, accountability, truthful status, identifier uniqueness, non-reuse, or required approval.

# 19. Conformance

19.1. A subordinate standard conforms only when its class, identifier, domain, sequence, metadata, status, authority, canonical representation, register entry, and exceptions are valid.

19.2. A malformed or unregistered document MUST NOT be represented as an effective KEP standard.

19.3. Taxonomy nonconformance MAY invalidate claimed governance status even when the artifact retains substantive engineering value.

# 20. Implementation

20.1. Upon effectiveness, `KEP-COM-001`, `KEP-REV-001`, and `KEP-PO-001` are reserved for their approved subjects.

20.2. `KEP-GOV-001` SHALL be registered as a legacy non-normative audit identifier.

20.3. New subordinate standards SHALL use this taxonomy.

20.4. Machine-readable schemas, automated validation, registry automation, path migration, legacy renaming, CI enforcement, and publication generators require separately authorized work.

20.5. Existing artifacts SHALL NOT be silently renamed, moved, or reclassified.

# 21. Review and Amendment

21.1. This standard SHALL be reviewed every six months and immediately upon a new artifact class, new or retired domain, material registry failure, identifier collision, relevant repository-topology change, or authority ambiguity.

21.2. A material change to identifier structure, non-reuse rules, artifact classes, or standards-domain authority SHALL require a major version.

# 22. Initial Registry Entries

The standards register SHALL include KEP-GOV-002 as Effective, KEP-PO-001 as Draft after drafting begins, KEP-REV-001 and KEP-COM-001 as Reserved, and KEP-GOV-001 as a legacy non-normative audit identifier.

# 23. Approval Record

| Field | Value |
| --- | --- |
| Document | KEP-GOV-002 — Standards Taxonomy and Naming Standard |
| Version | 1.0 |
| Approved By | Kashif Muhammad Younus |
| Authority | Founding Authority |
| Approval Date | July 25, 2026 |
| Effective Date | July 25, 2026 |
| Decision | Approved |
| Approval Statement | KEP-GOV-002 Version 1.0 is approved as the binding subordinate governance standard for KEP standards taxonomy, naming, classification, registration, and identifier lifecycle. |

# 24. Revision History

| Version | Date | Status | Summary |
| --- | --- | --- | --- |
| 1.0 | July 25, 2026 | Effective | Initial taxonomy, domain registry, artifact classes, identifier lifecycle, legacy treatment, and standards-register requirements. |
