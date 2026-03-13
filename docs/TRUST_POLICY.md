# FeedOracle Evidence Trust Policy v1.0

**Effective:** 2026-03-13
**Scope:** All FeedOracle MCP tool responses, Evidence Packs, and Audit Trail entries
**Status:** Active

---

## 1. What Is FeedOracle Evidence?

FeedOracle Evidence is a **machine-verifiable data artifact** that records a specific claim about a financial instrument at a specific point in time, together with the provenance of that claim.

An evidence artifact is NOT:
- Legal advice or regulatory approval
- A recommendation to buy, sell, or hold any asset
- A guarantee of accuracy, completeness, or timeliness
- A substitute for professional compliance review
- A final regulatory determination by any authority

An evidence artifact IS:
- A structured, signed record of data observed from defined sources
- Independently verifiable via public cryptographic keys (JWKS)
- Time-stamped with source attribution and confidence scoring
- Reproducible: same inputs at same time produce same outputs
- Classified by evidence type, cost class, and freshness

---

## 2. Evidence Classes

Every data point is classified into one of six evidence classes:

| Class | Definition | Example |
|-------|-----------|---------|
| `REGISTER` | Data from an official regulatory register | ESMA MiCA Register entry |
| `NCA_NOTICE` | National Competent Authority notice or decision | BaFin authorization notice |
| `ISSUER_DISCLOSURE` | Publicly available issuer document | Circle transparency report |
| `ATTESTATION` | Third-party audit or attestation | Deloitte reserve attestation |
| `MARKET_DATA` | Real-time or near-real-time market observation | CoinGecko price, DeFiLlama TVL |
| `ONCHAIN_INFERENCE` | Data derived from on-chain observation | Supply changes, contract state |

Evidence class determines the weight given to a data point in composite scores.

---

## 3. Source of Truth Hierarchy

When sources conflict, FeedOracle resolves by hierarchy:

1. **Regulatory registers** (ESMA, EBA, NCA) — highest authority
2. **Issuer disclosures** (white papers, reserve reports) — issuer-attested
3. **Third-party attestations** (auditor reports) — independently verified
4. **Market data** (exchanges, aggregators) — real-time but unattested
5. **On-chain inference** (contract state, supply) — observable but interpretable

Conflicts are flagged in `reason_codes` and `compliance_flags`. FeedOracle does not silently override lower-priority sources.

---

## 4. Normalization Rules

All evidence artifacts follow these normalization rules:

- **Symbols**: Resolved to canonical slug via `asset.resolved_slug` field
- **Prices**: Denominated in USD unless explicitly EUR (EURC, EURI)
- **Timestamps**: UTC (ISO 8601), timezone-naive internally
- **Thresholds**: MiCA-defined where applicable (e.g., EUR 5B significant issuer)
- **Confidence**: 0.0 - 1.0 scale, source-weighted
- **Schema version**: Declared in every response (`schema_version: "2.3"`)

Schema changes follow semantic versioning. Breaking changes increment major version. All schemas are backwards-compatible within a major version.

---

## 5. Signing Rules

Every MCP tool response is cryptographically signed:

- **Algorithm**: ES256K (secp256k1 ECDSA)
- **Key ID**: `feedoracle-mcp-es256k-1`
- **JWKS endpoint**: `https://feedoracle.io/.well-known/jwks.json`
- **Content hash**: SHA256 of the canonical JSON payload (excluding `signature` field)
- **Scope**: `mcp-tool-response`

Verification path: Fetch JWKS -> extract public key by `kid` -> verify signature against `content_hash` -> compare `content_hash` against locally computed hash of the response body.

Key rotation: New keys are added to JWKS before activation. Old keys remain valid for 90 days after deactivation. Key rotation events are logged in the changelog.

---

## 6. Evidence Lifecycle States

Every evidence artifact exists in one of these states:

| State | Meaning |
|-------|---------|
| `CURRENT` | Active and within freshness target |
| `STALE` | Beyond freshness target but not corrected |
| `CORRECTED` | A newer version has replaced this artifact |
| `SUPERSEDED` | Replaced by a structurally different artifact |
| `DISPUTED` | A conflict has been reported against this artifact |
| `RETRACTED` | Withdrawn due to source error or system fault |

State transitions:
```
CURRENT -> STALE        (freshness_target exceeded without refresh)
CURRENT -> CORRECTED    (same tool, same inputs, newer data)
CURRENT -> SUPERSEDED   (schema change or source change)
CURRENT -> DISPUTED     (conflict reported via dispute process)
CURRENT -> RETRACTED    (source error, system fault, or manual withdrawal)
STALE   -> CURRENT      (data refreshed within parameters)
```

Corrected and superseded artifacts remain queryable for audit purposes. The `corrected_by` or `superseded_by` field links to the replacement artifact.

**Distinction between CORRECTED and SUPERSEDED:**
- `CORRECTED`: The same artifact type and factual basis, updated with newer or more accurate data from the same source structure. The input query is identical; the output changed because the underlying data changed.
- `SUPERSEDED`: Replaced by a structurally different artifact — new schema version, new source integration, new normative basis, or fundamentally different methodology. The replacement may not be directly comparable to the original.

### Transition Authority

| Transition | Who May Trigger | Control Process |
|------------|----------------|----------------|
| CURRENT -> STALE | System (automatic) | Freshness timer expiry; no human approval needed |
| CURRENT -> CORRECTED | System (automatic) | New verified response for same input_hash corrects the prior artifact; logged in state_log |
| CURRENT -> SUPERSEDED | Engineering (manual) | Schema migration or source replacement; requires changelog entry |
| CURRENT -> DISPUTED | External party or internal QA | Filed via `audit_log` with `decision_type: "dispute"`; triggers SLA clock |
| CURRENT -> RETRACTED | Operations lead (manual) | Requires documented reason; artifact remains queryable |
| DISPUTED -> CORRECTED/RETRACTED | Operations lead | Resolution within Dispute-SLA; logged in audit trail |

No lifecycle transition may occur without a corresponding entry in `evidence_state_log`.

---

## 7. Freshness Targets

| Tier | Freshness Target | Staleness Threshold |
|------|-----------------|-------------------|
| Free | 60 seconds | 300 seconds |
| Pro | 30 seconds | 120 seconds |
| Enterprise | 15 seconds | 60 seconds |

`sla.freshness_met` indicates whether the current data meets the tier's target. `sla.staleness_flag` indicates source degradation.

---

## 8. Degradation Model

When a data source is unavailable or degraded:

| Condition | Response Behavior |
|-----------|------------------|
| Source temporarily unavailable | Serve cached data, set `staleness_flag: true`, reduce `confidence` |
| Source permanently removed | Return `UPSTREAM` error with explanation |
| Partial data available | Serve partial response, list `sources.available` vs `sources.total` |
| Signing service unavailable | Fall back to HMAC, flag in `signature.alg` |
| Anchoring service unavailable | Generate report without anchor, flag `anchored: false` |

FeedOracle never silently serves stale data as fresh. Every degradation is visible in the response metadata.

---

## 9. Correction, Dispute, and Retraction

### Correction

When FeedOracle identifies an error in prior evidence:
1. A new artifact is created with the corrected data
2. The original artifact's state is set to `CORRECTED`
3. The original artifact gains a `corrected_by` field pointing to the new artifact
4. Both artifacts remain queryable

### Dispute Process and SLA

When a third party reports a conflict:
1. Dispute is logged via `audit_log` with `decision_type: "dispute"`
2. The disputed artifact's state is set to `DISPUTED`
3. FeedOracle investigates and either confirms, corrects, or retracts
4. Resolution is logged in the audit trail

**Dispute-SLA:**

| Stage | Target | Description |
|-------|--------|-------------|
| Acknowledgement | 4 hours | Dispute receipt confirmed, ticket created |
| Classification | 24 hours | Dispute classified as source error, normalization error, system fault, or invalid |
| Resolution | 5 business days | Artifact confirmed, corrected, or retracted; resolution logged in audit trail |
| Escalation | If unresolved after 5 days | Escalated to operations lead; interim `DISPUTED` state remains visible |

All dispute communications are logged. The disputed artifact remains queryable with `DISPUTED` state throughout the process. Resolution always produces an audit trail entry linked to the dispute record.

### Retraction

When evidence must be withdrawn:
1. Artifact state is set to `RETRACTED`
2. `retracted_reason` field explains why
3. The artifact remains queryable but clearly marked
4. No silent deletion ever occurs

---

## 10. Liability Boundary

FeedOracle operates as **evidence infrastructure**:

| FeedOracle does | FeedOracle does not |
|-----------------|-------------------|
| Aggregate data from defined sources | Make regulatory determinations |
| Apply normalization rules consistently | Provide legal advice |
| Sign and timestamp every output | Guarantee source accuracy |
| Provide provenance and verification paths | Accept liability for third-party source errors |
| Flag inconsistencies and conflicts | Replace professional compliance review |
| Enable reproducible audit trails | Act as a regulated entity on behalf of users |

Users are responsible for their own compliance decisions. FeedOracle provides the evidence basis; the decision authority remains with the user or their compliance function.

**Downstream use in autonomous systems:** When FeedOracle evidence artifacts are consumed by autonomous agents, trading algorithms, or automated decision pipelines, the operator of that system bears full responsibility for the actions taken. FeedOracle provides machine-verifiable inputs. It does not control, endorse, or accept liability for downstream execution based on those inputs. Users integrating FeedOracle evidence into agentic workflows must implement their own safeguards, human oversight mechanisms, and fallback procedures as required by applicable regulation (including EU AI Act Art. 14 for high-risk AI systems).

---

## 11. Governance

### Change Management
- Schema changes: Announced 30 days before activation for major versions
- Source additions: Reviewed and documented before inclusion
- Source removals: Flagged as `DEPRECATED` for 90 days before removal
- Normalization rule changes: Versioned and documented in changelog

### Incident Handling
- Source outages: Logged, staleness flags activated, status page updated
- Data corrections: Logged in audit trail with `CORRECTED` state
- Security incidents: Reported within 24 hours, keys rotated if compromised

### Release Discipline
- Trust-relevant changes require review before deployment
- Breaking changes require major version increment
- All changes logged in CHANGELOG.md with date and scope

### Operational Roles

| Role | Responsibility | Lifecycle Authority |
|------|---------------|-------------------|
| System (automated) | Freshness monitoring, auto-correction | STALE, CORRECTED (same-input refresh) |
| Engineering | Schema changes, source integration | SUPERSEDED (with changelog) |
| Operations lead | Incident response, dispute resolution | RETRACTED, DISPUTED -> resolution |
| External parties | Report conflicts or inconsistencies | File DISPUTED via audit_log |

---

## 12. Acceptance Targets

FeedOracle Evidence is designed for acceptance by, in priority order:

1. **Compliance officers** verifying stablecoin and RWA regulatory status
2. **Risk teams** assessing counterparty and custody exposure
3. **Internal audit functions** replaying and verifying agent decisions
4. **Enterprise procurement** evaluating evidence infrastructure vendors
5. **External auditors** verifying compliance evidence trails
6. **Agent developers** building autonomous compliance workflows

Each audience has specific needs:

| Audience | Primary Need | FeedOracle Feature |
|----------|-------------|-------------------|
| Compliance officers | Human-readable verdicts, coverage | `ai_explain`, evidence packs, MiCA mapping, `summary` field |
| Risk teams | Provenance, confidence, degradation | `ai_provenance`, SLA metadata, staleness flags |
| Audit functions | Replay, chain integrity, evidence snapshots | `audit_trail`, `audit_verify`, evidence lifecycle |
| Procurement | SLA, governance, policy | This document, SLO targets, CHANGELOG, dispute-SLA |
| External auditors | Independent verification, no trust required | Public JWKS, verify scripts, dispute process |
| Agent developers | Quick start, API clarity, unit economics | MCP tools, OAuth M2M, unit billing, KYA |

---

## 13. Verification Without Trust

A third party can verify any FeedOracle evidence artifact without:
- An account or API key
- Trust in FeedOracle as an organization
- Access to internal systems

Verification path:
1. Obtain the signed response (from the agent or audit trail)
2. Fetch `https://feedoracle.io/.well-known/jwks.json` (public, no auth)
3. Verify ES256K signature using the public key
4. Recompute `content_hash` from the response body
5. Compare computed hash against signed `content_hash`
6. Optionally: call the same tool with same inputs to verify reproducibility

Public verification script: `feedoracle_agent_verify.py` (38 independent checks, no account required)

---

*This policy is maintained by FeedOracle and versioned in the public repository. Changes are logged in CHANGELOG.md.*
