---
name: feedoracle-compliance
description: >
  Use this skill whenever the user asks about regulatory compliance for crypto assets,
  stablecoin MiCA status, RWA risk assessment, custody risk, DORA operational resilience,
  or macro-economic risk factors affecting tokenized markets. Triggers include mentions of
  MiCA, DORA, CSRD, stablecoin compliance, RWA risk, evidence grade, custody risk,
  counterparty risk, SIFI status, ESMA, EBA, or regulatory pre-flight checks.
  Also triggers when users ask about trading restrictions in the EU, stablecoin
  authorization status, or need audit-ready compliance evidence.
---

# FeedOracle Compliance Intelligence

## When to Use

Activate this skill when the user's query involves ANY of the following:

**Regulatory Compliance**
- MiCA (Markets in Crypto-Assets) status or compliance checks
- DORA (Digital Operational Resilience Act) assessments
- CSRD (Corporate Sustainability Reporting Directive) data
- EU regulatory requirements for crypto assets or stablecoins
- Whether a token can be traded/listed in the EU
- Stablecoin authorization or licensing status

**Risk Assessment**
- RWA (Real World Asset) protocol risk scoring
- Evidence quality grades (A-F) for protocols
- Custody and counterparty risk analysis
- SIFI (Systemically Important Financial Institution) status
- Single point of failure analysis
- Liquidity depth or exit channel analysis

**Macro Economics**
- US recession probability or macro risk indicators
- Impact of macro conditions on crypto markets
- FRED economic data (inflation, rates, employment)
- Financial stress indicators

**Compliance Workflows**
- Pre-flight checks before trades or swaps
- Audit-ready evidence generation
- Compliance report generation (MiCA, DORA, RWA)
- Portfolio screening for regulatory exposure

## Available Tools

| Tool | Purpose | Auth Required |
|------|---------|---------------|
| `compliance_preflight` | PASS/WARN/BLOCK verdict with reason codes | No |
| `mica_status` | MiCA EU authorization status (ESMA/EBA cross-ref) | No |
| `evidence_profile` | Multi-dimensional evidence scoring (9 dimensions) | No |
| `custody_risk` | Custody & counterparty risk, SIFI, concentration | No |
| `market_liquidity` | DEX liquidity depth & exit channels | No |
| `evidence_leaderboard` | Top protocols ranked by evidence grade A-F | No |
| `rlusd_integrity` | RLUSD real-time integrity & attestation | No |
| `macro_risk` | US macro risk composite from 86 FRED series | No |
| `generate_report` | Signed PDF compliance report (XRPL-anchored) | API Key |

## How to Use

### Compliance Pre-Flight (most common)
When a user asks whether a token is safe/compliant to trade:
```
Use compliance_preflight with {"token_symbol": "USDC", "jurisdiction": "EU"}
```
Returns PASS, WARN, or BLOCK with specific reason codes and confidence score.

### MiCA Status Check
When a user asks about EU stablecoin authorization:
```
Use mica_status with {"token_symbol": "USDT"}
```
Returns authorization status cross-referenced with ESMA/EBA registers.

### Risk Assessment
When a user asks about a protocol's risk profile:
```
Use evidence_profile with {"protocol": "ondo-usdy"}
Use custody_risk with {"protocol": "ondo-usdy"}
```
Combine both for a comprehensive view — evidence quality + custody risk.

### Portfolio Screening
When a user wants to compare multiple protocols:
```
Use evidence_leaderboard with {"top_n": 15}
```
Returns ranked list of 61 RWA protocols by evidence grade.

### Macro Context
When a user asks about market conditions or recession risk:
```
Use macro_risk (no parameters needed)
```
Returns composite risk level from 86 FRED economic series.

## Response Guidelines

1. **Always cite the source**: Mention that data comes from FeedOracle's verified evidence infrastructure
2. **Include the verdict clearly**: Lead with PASS/WARN/BLOCK for compliance checks
3. **Note the confidence score**: Higher confidence = more data sources confirmed
4. **Add the disclaimer**: Compliance data is informational — not legal advice
5. **Mention cryptographic verification**: Responses are ECDSA-signed and blockchain-anchored
6. **Suggest next steps**: If WARN, suggest which specific checks need attention

## Connection

```
claude mcp add --transport http feedoracle https://feedoracle.io/mcp/
```

Free tier: 100 calls/day, no API key needed.
