# KEP Repository Instructions

These instructions apply to the entire repository.

## Repository purpose

Maintain the Kuriosity Engineering Platform governance and engineering-
knowledge baseline. This repository is not a Metro-X product source tree.

## Published framework release

The current official governance baseline is KEP Framework `v1.0.0`.

Use `docs/00-governance/releases/KEP-v1.0.0-release-manifest.md` to determine
the complete release contents, canonical paths, document versions, lifecycle
states, and product-adoption coordinates.

The framework release identifier is the contractual adoption identifier.
Repository commits are implementation evidence. A Git tag or GitHub Release is
an optional distribution object and must not redefine the repository-controlled
release manifest.

## Authoritative governance order

Use these sources in order:

1. Applicable law and binding contractual obligations.
2. `docs/00-governance/KEP-002-engineering-constitution.md`
3. `docs/00-governance/KEP-000-founding-charter.md`
4. `docs/00-governance/KEP-001-platform-scope-boundaries-operating-model.md`
5. `docs/00-governance/KEP-001A-founding-decisions-ratification-record.md`
6. Effective subordinate standards listed in the authoritative release
   manifest.
7. Ratification, approval, register, review, verification, and release records
   within their stated authority.

The release manifest identifies the contents of a release; it does not change
the precedence established by the included governance instruments.

Do not invent, reconstruct, or silently replace missing authoritative text.
Keep governance documents in their canonical paths under
`docs/00-governance/`.

## Repository boundaries

- Do not add Metro-X product code or product-specific files.
- Do not add consumer reports or consumer-sensitive data.
- Do not commit credentials, secrets, `.env` files, database dumps, or local
  machine state.
- Keep implementation code and CLI tooling out of governance-baseline changes.
- Preserve ratification state and document status exactly as the authoritative
  source records them.
- Keep changes narrowly scoped and reviewable.
- Do not add a document to a published release without a controlled manifest
  change or approved successor release.
- Do not treat an unversioned `main` reference as automatic product adoption.

## Verification

Before committing, inspect the complete diff, scan filenames and content for
sensitive material, confirm that governance documents are canonically placed,
and verify release-manifest consistency when publication metadata changes.

Stop before merge unless merge authority is explicitly granted.
