# KE-004 — Platform Portfolio and Responsibility Map

## Metadata

| Field | Value |
|---|---|
| Identifier | KE-004 |
| Title | Platform Portfolio and Responsibility Map |
| Version | 1.0 |
| Status | Ratified; Effective |
| Authority Level | Portfolio governance; subordinate to KE-000 through KE-003 |
| Owner | Kuriosity Ecosystem Founding Authority |
| Effective Date | 2026-07-29 |
| Applies To | Current and future KE platforms |

## 1. Purpose

This map records the recognized KE platform portfolio and the current maturity of each platform mandate.

It deliberately does not invent capability boundaries where no ratified platform authority exists.

## 2. Portfolio

| Identifier | Platform | Current lifecycle state | Mandate status | Canonical location |
|---|---|---|---|---|
| KEC | Kuriosity Ecosystem Core | Recognized; not admitted | Boundary pending | `platforms/kec/` |
| KEM | Kuriosity Ecosystem Management | Recognized; not admitted | Boundary pending | `platforms/kem/` |
| KKP | Kuriosity Knowledge Platform | Recognized; not admitted | Boundary pending | `platforms/kkp/` |
| KEP | Kuriosity Engineering Platform | Existing founding platform | Ratified KEP governance exists; KE adoption and relocation require reconciliation | `platforms/kep/` |
| KES | Kuriosity Engineering Services | Recognized; not admitted | Boundary pending | `platforms/kes/` |
| KDS | Kuriosity Developer Services | Recognized; not admitted | Boundary pending | `platforms/kds/` |
| KTP | Kuriosity Testing Platform | Recognized; not admitted | Boundary pending | `platforms/ktp/` |
| KSP | Kuriosity Security Platform | Recognized; not admitted | Boundary pending | `platforms/ksp/` |
| KDP | Kuriosity Data Platform | Recognized; not admitted | Boundary pending | `platforms/kdp/` |
| KOP | Kuriosity Operations Platform | Recognized; not admitted | Boundary pending | `platforms/kop/` |
| KAS | Kuriosity AI Services | Recognized; not admitted | Boundary pending | `platforms/kas/` |

## 3. Admission Requirements

Before a recognized platform becomes admitted and operational under KE, its authoritative governance shall define:

- official identity and purpose;
- reusable capability mandate;
- explicit exclusions;
- accountable Platform Owner;
- authority and architecture boundaries;
- dependencies on other platforms;
- product adoption relationship;
- release and compatibility model;
- verification and evidence requirements; and
- lifecycle state and effective date.

## 4. Boundary Rules

- The KE repository root represents the ecosystem and does not silently replace KEC.
- A platform name or directory does not establish a mandate.
- A platform shall own only reusable capabilities within its ratified boundary.
- Products shall retain business-domain authority.
- Cross-platform capabilities shall have one accountable owner.
- KEP governs engineering and shall remain product-independent.
- No placeholder platform shall be represented as released, effective, or adoptable.

## 5. KEP Reconciliation Boundary

KEP v1.0.0 is a historical approved KEP release. Its original release identity and adoption coordinates shall not be silently changed.

Migration of KEP content into `platforms/kep/` establishes a proposed new canonical location. The relocation becomes product-adoptable only through a controlled successor KEP release and KE publication approval.

## 6. Ratification Record

| Field | Value |
|---|---|
| Ratified By | Kuriosity Ecosystem Founding Authority |
| Authority | Kuriosity Ecosystem Founding Authority |
| Effective Date | 2026-07-29 |
| Approval Record | `governance/approvals/KE-foundation-v1.0-ratification-and-relocation-approval-record.md` |

