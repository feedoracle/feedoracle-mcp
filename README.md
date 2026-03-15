<div align="center">

# FeedOracle MCP Server

**Compliance evidence infrastructure for AI agents.**

Every response cryptographically signed. Every decision audit-ready.

[![Server Status](https://img.shields.io/badge/server-live-10B898?style=flat-square)](https://feedoracle.io/mcp/health)
[![Tools](https://img.shields.io/badge/MCP_tools-53-3B82F6?style=flat-square)](https://feedoracle.io/mcp.html)
[![Stablecoins](https://img.shields.io/badge/stablecoins-105+-8A9DB4?style=flat-square)](https://feedoracle.io)
[![Free Tier](https://img.shields.io/badge/free_tier-100_calls%2Fday-10B898?style=flat-square)](https://feedoracle.io/pricing.html)

[Website](https://feedoracle.io) Â· [Docs](https://feedoracle.io/docs.html) Â· [MCP Tools](https://feedoracle.io/mcp.html) Â· [Trust Policy](https://feedoracle.io/trust/) Â· [Pricing](https://feedoracle.io/pricing.html)

</div>

---

## The problem

AI agents make compliance decisions every day. But nobody can prove what data they used, when they used it, or whether it was tampered with.

Regulators don't accept "trust me." They require **verifiable evidence**.

## What FeedOracle does

FeedOracle is the **evidence layer** for AI compliance decisions. Connect your agent via MCP. Get signed evidence back.

```
Your AI agent                    FeedOracle                     Regulator
     |                               |                              |
     |-- "Is USDC MiCA compliant?" -->|                              |
     |                               |-- Fetch from 7+ sources      |
     |                               |-- Structure evidence          |
     |                               |-- Sign (ECDSA ES256K)         |
     |                               |-- Anchor (Polygon + XRPL)    |
     |<-- Signed evidence pack ------|                              |
     |                               |                              |
     |    6 months later...          |                              |
     |                               |                              |
     |-- "Show proof" -------------------------------------------- >|
     |                               |<-- Replay from registry -----|
     |                               |-- hash_match: true --------->|
     |                               |         Audit passed         |
```

## Quick start

One command. No API key needed.

```bash
claude mcp add --transport http feedoracle https://feedoracle.io/mcp/
```

<details>
<summary>Claude Desktop / Cursor / Windsurf</summary>

```json
{
  "mcpServers": {
    "feedoracle": {
      "url": "https://feedoracle.io/mcp/"
    }
  }
}
```

</details>

Then ask Claude:

```
Is USDC compliant for trading in the EU under MiCA?
```

You get back signed, verifiable, audit-ready evidence:

```json
{
  "decision": "PASS",
  "confidence": 0.95,
  "evidence": {
    "mica": { "status": "compliant", "issuer": "Circle" },
    "grade": "A",
    "pack_id": "FO-AIG-A8C3D2"
  },
  "signature": {
    "alg": "ES256K",
    "independently_verifiable": true,
    "verify": "https://feedoracle.io/.well-known/jwks.json"
  }
}
```

## 3 MCP servers Â· 53 tools

| Server | Tools | Purpose |
|--------|-------|---------|
| **Compliance Oracle** | 27 | MiCA status, evidence packs, DORA artifacts, audit trail |
| **Stablecoin Risk** | 13 | 7-signal risk scoring, peg monitoring, 105+ tokens |
| **Macro Intelligence** | 13 | 86 FRED + 20 ECB indicators, regime classification |

> **"May your agent trade this?"** â†’ Compliance Oracle
> **"Should your agent trade now?"** â†’ Macro Intelligence  
> **"Is this stablecoin safe?"** â†’ Stablecoin Risk

<details>
<summary>All 27 Compliance tools</summary>

| Tool | Speed | Description |
|------|-------|-------------|
| `compliance_preflight` | fast | PASS/WARN/BLOCK verdict for any token |
| `mica_status` | fast | MiCA authorization - ESMA register |
| `peg_deviation` | fast | Real-time peg deviation |
| `significant_issuer` | fast | Significant issuer threshold |
| `interest_check` | fast | Interest prohibition scanner |
| `evidence_profile` | med | 9-dimension risk scoring A-F |
| `custody_risk` | med | SIFI status, concentration risk |
| `market_liquidity` | med | DEX depth and exit channels |
| `reserve_quality` | med | Reserve composition assessment |
| `document_compliance` | med | Document completeness check |
| `evidence_leaderboard` | med | 61 RWA protocols ranked |
| `rlusd_integrity` | med | RLUSD attestation verification |
| `macro_risk` | med | US macro risk composite |
| `peg_history` | med | 30-day peg stability |
| `ai_provenance` | med | Cryptographic provenance chain |
| `ai_explain` | med | AI-powered grade explanation |
| `ai_query` | med | Natural language evidence query |
| `mica_market_overview` | heavy | Full MiCA market - 105 stablecoins |
| `mica_full_pack` | heavy | Complete 12-article MiCA evidence |
| `evidence_bundle` | heavy | Multi-framework evidence pack |
| `generate_report` | heavy | Signed PDF, blockchain-anchored |
| `kya_register` | fast | Register agent identity |
| `kya_status` | fast | Check agent trust level |
| `audit_log` | fast | Log decision to audit trail |
| `audit_query` | med | Query audit trail history |
| `audit_verify` | med | Verify trail integrity |
| `ping` | fast | Connectivity test |

</details>

<details>
<summary>All 13 Stablecoin Risk tools</summary>

`risk_assessment` Â· `peg_status` Â· `peg_history` Â· `supply_flow` Â· `holder_data` Â· `custody_data` Â· `redemption_data` Â· `cross_chain_data` Â· `leaderboard` Â· `compare` Â· `supported_tokens` Â· `methodology` Â· `ping`

Connect: `claude mcp add --transport sse feedoracle-risk https://feedoracle.io/mcp/risk/sse`

</details>

<details>
<summary>All 13 Macro Intelligence tools</summary>

`economic_health` Â· `recession_risk` Â· `inflation_monitor` Â· `labor_market` Â· `gdp_tracker` Â· `fed_watch` Â· `yield_curve` Â· `defi_rates` Â· `consumer_sentiment` Â· `market_stress` Â· `safe_haven_flows` Â· `macro_regime` Â· `ping`

Connect: `claude mcp add --transport sse feedoracle-macro https://feedoracle.io/mcp/macro/sse`

</details>

## Why this is different

| | Traditional | FeedOracle |
|---|---|---|
| **Evidence integrity** | PDF + email | Signed bundle + chain anchor |
| **Timestamp proof** | File metadata | Blockchain-anchored (Polygon + XRPL) |
| **Audit replay** | "We think this is what we had" | Deterministic replay from signed pack |
| **Verification** | "Trust us" | Public key verification - zero trust |
| **AI-native** | Manual API wrappers | 53 MCP tools, works out of the box |

## Verify in 30 seconds

No account needed. No trust required.

```bash
# 1. Get signed evidence
curl -s -X POST https://feedoracle.io/ai/query \
  -H "Content-Type: application/json" \
  -d '{"question":"Is USDC MiCA compliant?"}'

# 2. Verify the signature
curl -s https://feedoracle.io/.well-known/jwks.json

# 3. Check the evidence registry
curl -s https://feedoracle.io/evidence/registry?limit=3

# 4. Replay for audit proof
curl -s https://feedoracle.io/evidence/replay/{pack_id}
```

## Built for

- **Banks and insurers** â€” MiCA + DORA compliance evidence
- **Stablecoin issuers** â€” reserve and peg monitoring, signed proof
- **AI agent builders** â€” 53 MCP tools, every decision auditable
- **Compliance teams** â€” replace manual evidence with automated proof

## Pricing

| Tier | Calls/day | Price |
|------|-----------|-------|
| **Free** | 100 | $0 - no key needed |
| **Pro** | 5,000 | $49/mo |
| **Agent** | 25,000 | $299/mo |
| **Enterprise** | Unlimited | [Contact us](mailto:enterprise@feedoracle.io) |

## Links

| | |
|---|---|
| Website | [feedoracle.io](https://feedoracle.io) |
| Docs | [feedoracle.io/docs](https://feedoracle.io/docs.html) |
| Trust | [feedoracle.io/trust](https://feedoracle.io/trust/) |
| Uptime | [uptime.feedoracle.io](https://uptime.feedoracle.io) |
| Health | [feedoracle.io/mcp/health](https://feedoracle.io/mcp/health) |
| JWKS | [.well-known/jwks.json](https://feedoracle.io/.well-known/jwks.json) |
| Contact | [enterprise@feedoracle.io](mailto:enterprise@feedoracle.io) |

---

<div align="center">

**FeedOracle turns compliance documents into compliance evidence.**

*Evidence by Design.*

</div>
