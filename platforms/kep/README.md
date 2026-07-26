# Kuriosity Engineering Platform (KEP)

This repository is the governance and engineering-knowledge baseline for the
Kuriosity Engineering Platform. It contains platform governance, architecture
records, engineering contracts, reusable knowledge, skills, playbooks,
templates, operations guidance, and verification material.

It does not contain Metro-X product implementation, consumer reports,
credentials, environment files, or database dumps.

## Official governance baseline

The first official product-adoptable governance baseline is **KEP Framework
v1.0.0**.

- Release declaration:
  `docs/00-governance/releases/KEP-v1.0.0-release-declaration.md`
- Authoritative release manifest:
  `docs/00-governance/releases/KEP-v1.0.0-release-manifest.md`
- Product-adoption verification:
  `docs/00-governance/verification/KEP-v1.0.0-product-adoption-verification.md`

Products adopt the framework release identifier `v1.0.0` and the standards
and versions listed in its manifest. Repository commits are implementation
evidence. Git tags and GitHub Releases are optional distribution mechanisms and
are not authoritative engineering artifacts.

## Repository structure

```text
kuriosity-engineering-platform/
|-- README.md
|-- AGENTS.md
|-- LICENSE
|-- .gitignore
|-- docs/
|   |-- 00-governance/
|   |-- 01-platform/
|   |-- 02-architecture/
|   |-- 03-engineering-contracts/
|   |-- 04-knowledge/
|   |-- 05-skills/
|   |-- 06-playbooks/
|   |-- 07-templates/
|   |-- 08-operations/
|   `-- 09-verification/
|-- contracts/
|-- skills/
|-- playbooks/
|-- templates/
|-- schemas/
|-- tools/
|-- research/
`-- verification/
```

Canonical governance documents belong in `docs/00-governance/`. The
constitutional baseline documents are:

- `KEP-000-founding-charter.md`
- `KEP-001-platform-scope-boundaries-operating-model.md`
- `KEP-001A-founding-decisions-ratification-record.md`
- `KEP-002-engineering-constitution.md`

KEP-002 Version 1.0 contains its ratification record in Section 21. No separate
KEP-002A document is part of the official v1.0.0 release.

The release manifest is the complete inventory of included constitutional
instruments, subordinate standards, versions, lifecycle states, and supporting
evidence.

## Contribution boundary

Read `AGENTS.md` before changing the repository. Keep governance and knowledge
artifacts platform-level, auditable, and free of product- or consumer-sensitive
material.
