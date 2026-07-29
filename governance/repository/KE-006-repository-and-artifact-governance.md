# KE-006 — Repository and Artifact Governance

## Metadata

| Field | Value |
|---|---|
| Identifier | KE-006 |
| Title | Repository and Artifact Governance |
| Artifact Type | Governance Policy |
| Version | 1.1 |
| Lifecycle Status | Effective |
| Approval Status | Approved |
| Verification Status | Pass |
| Authority | KE-000 through KE-005 |
| Owner | KE Repository Maintainer |
| Effective Date | 2026-07-29 |
| Scope | Canonical repository, artifact control, publication, integrity, and repository verification |
| Amendment Path | KE-007 |
| Supersession State | Current; supersedes KE-006 Version 1.0 |

## 1. Canonical Repository

`kashifyounus/Kuriosity-Ecosystem` is the sole canonical KE repository. A normative KE artifact shall not depend on an external repository for meaning, authority, validation, adoption, release, rollback, or maintenance.

## 2. Artifact Control

Every normative artifact shall declare identifier, title, version, status, authority, owner, effective date, scope, amendment path, and supersession state.

Markdown is the canonical human-readable representation unless an approved artifact declares another canonical format. Alternate renditions shall identify their source and synchronization state.

## 3. Repository Structure

Artifact placement shall follow the root repository map. One subject shall have one canonical normative source. References, summaries, reports, and templates shall not duplicate or silently redefine that source.

## 4. Change Control

Repository changes shall:

1. identify authority and scope;
2. assess impacted artifacts and consumers;
3. use a controlled branch;
4. preserve unrelated work;
5. update cross-references and registers;
6. undergo applicable review;
7. record approval and evidence;
8. merge through a reviewable pull request; and
9. verify the authoritative branch after merge.

Repository-controlled ownership and deterministic validation shall protect publication. CODEOWNERS and validation workflows are minimum repository evidence; administrative branch or ruleset settings shall be documented and verified separately.

## 5. Source Integrity

Historical artifacts may be retained only when clearly marked non-normative, self-contained, and free of active dependency. Stale drafts, superseded release candidates, duplicate authorities, and empty structures without current purpose should be removed.

## 6. Secrets and Restricted Information

Secrets, credentials, personal data, or restricted records shall not be committed unless an approved security and access model expressly permits it. Public visibility does not create licensing permission or waive confidentiality.

## 7. Verification

Publication verification shall check authority, status, version, links, terminology, duplication, dependency, manifest, branch state, and absence of fabricated evidence.

## 8. Approval

Version 1.1 approved by the Kuriosity Ecosystem Founding Authority on 2026-07-29 through KE-APR-003.
