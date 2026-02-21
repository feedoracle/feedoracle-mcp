# FeedOracle MCP — Skill v2.3.1

## What this server does

FeedOracle provides real-time MiCA regulatory compliance and RWA risk intelligence for AI agents. It monitors **18 MiCA articles** across 80+ stablecoins and RWA protocols. Every response uses an identical JSON schema with status taxonomy, evidence classes, HMAC signature, and verify URL.

## When to use this server

Use FeedOracle when the user asks about:
- MiCA compliance status of any stablecoin or token (EURC, USDT, USDC, EURe, RLUSD, etc.)
- Peg stability, depeg events, or Art. 35 monitoring
- Significant issuer thresholds (Art. 45/58) and EBA oversight
- Interest prohibition compliance (Art. 23/52)
- Reserve quality and Art. 53 eligibility
- Recovery/redemption plans and audit freshness (Art. 29/30/55)
- RWA custody risk, evidence grades, or leaderboard rankings
- EU macro risk or RLUSD integrity
- Generating signed compliance PDFs (MiCA, DORA, CSRD)

## Tool selection guide

**Start here for token-level questions:**
1. `mica_status` — authorization check (fast, LIGHT)
2. `peg_deviation` — peg stability now (fast, LIGHT)
3. `mica_full_pack` — all 12 MiCA articles at once (needs API key, HEAVY)

**For specific articles:**
- Art. 35 → `peg_deviation`, `peg_history`
- Art. 45/58 → `significant_issuer`
- Art. 23/52 → `interest_check`
- Art. 29/30/55 → `document_compliance`
- Art. 24/25/53 → `reserve_quality`
- Art. 26/27 → `custody_risk`

**For transaction decisions:**
- `compliance_preflight` → returns PASS/WARN/BLOCK (not COMPLIANT/NOT_AUTHORIZED)

**For market-wide views:**
- `mica_market_overview` → all alerts at once (needs API key)
- `evidence_leaderboard` → top protocols ranked

## Status values

| Field | Values |
|-------|--------|
| `status` (all MiCA tools) | COMPLIANT · PENDING · NOT_AUTHORIZED · UNKNOWN · SIGNIFICANT |
| `decision` (preflight only) | PASS · WARN · BLOCK |

## Response fields always present

`schema_version` · `tool` · `request_id` · `jurisdiction` · `status/decision` · `reason_codes[]` · `mica_articles[]` · `confidence` · `sources[].evidence_class` · `meta.cost_class` · `meta.requires_key` · `signature` · `verify_url`

## Example calls

```
"Is EURC MiCA compliant?" → mica_status(EURC)
"Check USDT peg right now" → peg_deviation(USDT)
"Is USDC a significant issuer?" → significant_issuer(USDC)
"Full MiCA check for RLUSD" → mica_full_pack(RLUSD) [needs key]
"Any peg alerts in the market?" → mica_market_overview() [needs key]
"Top 10 RWA protocols" → evidence_leaderboard(top_n=10)
"Generate MiCA report" → generate_report(report_type=mica) [needs key]
```
