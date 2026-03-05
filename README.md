# FeedOracle MCP Server v2.3.1

Enterprise MiCA compliance, RWA risk intelligence, and AI Evidence Layer for AI agents.

Real-time monitoring of 18 MiCA articles across 105+ stablecoins and RWA protocols — cryptographically signed, machine-readable, enterprise-ready. Now with AI Gateway: natural language → signed evidence bundle in one call.

🔗 **Landing Page:** feedoracle.io/mcp  
📋 **Discovery:** feedoracle.io/mcp/.well-known/mcp/server.json  
📖 **Docs:** feedoracle.io/docs

## Quick Start

```bash
# Claude Code (one command)
claude mcp add --transport http feedoracle https://feedoracle.io/mcp/

# Claude Desktop — add to claude_desktop_config.json
{
  "mcpServers": {
    "feedoracle": {
      "url": "https://feedoracle.io/mcp/"
    }
  }
}
```

Free tier: 100 calls/day — no API key required to start.

---

## Tools (22)

### 🤖 AI Evidence Layer — 4 tools *(New)*

| Tool | Description |
|------|-------------|
| `ai_query` | Natural language → signed evidence bundle. Ask "Is USDC MiCA-compliant?" and receive a structured, cryptographically signed response |
| `evidence_bundle` | Aggregated evidence pack for a token: MiCA status, peg, reserves, custody, macro context — one call replaces 23 API calls |
| `ai_explain` | Grade explanation engine. "Why does EURC score B? What would make it Grade A?" |
| `ai_provenance` | Full data lineage graph — from FRED series IDs and ESMA register entries to chain hash. 17 nodes, 17 individual hashes |

### 🟢 LIGHT — No key, instant

| Tool | MiCA Articles | Description |
|------|--------------|-------------|
| `compliance_preflight` | 5, 16, 17, 48 | Transaction check: PASS/WARN/BLOCK for swap/transfer/custody |
| `mica_status` | 16, 17, 19, 20, 48 | EU authorization status — COMPLIANT/PENDING/NOT_AUTHORIZED/UNKNOWN |
| `peg_deviation` | 35 | Real-time peg deviation. STABLE < 0.1%, WARN < 0.5%, ALERT < 2% |
| `significant_issuer` | 45, 58 | SIGNIFICANT if reserve > €5B or daily tx > €1B. EBA oversight flag |
| `document_compliance` | 29, 30, 37, 55 | Recovery/redemption plans + audit freshness. Score 0–100 |
| `reserve_quality` | 24, 25, 36, 53 | Art. 53 eligibility %, liquidity score, reserve violations |
| `custody_risk` | 26, 27, 54 | Custodian identity, segregation, SIFI status, SPOF detection |
| `rlusd_integrity` | — | Real-time RLUSD reserve attestation |
| `ping` | — | Connectivity test |

### 🟡 MEDIUM — No key, aggregated

| Tool | MiCA Articles | Description |
|------|--------------|-------------|
| `peg_history` | 35 | 30-day peg history, stability score 0–100, depeg event count |
| `interest_check` | 23, 52 | Interest prohibition scan. Scans 18,000+ DeFi pools for issuer yield |
| `evidence_profile` | 36, 37, 45 | 9-dimension evidence grade A–F (governance, custody, reserves…) |
| `market_liquidity` | 45, 51 | DEX liquidity depth and redemption exit channels |
| `evidence_leaderboard` | 36, 37, 45 | Top 61 RWA protocols & 105+ stablecoins ranked by evidence grade |
| `macro_risk` | — | US macro composite from 86 FRED series (recession, inflation, Fed) |

### 🔴 HEAVY — API key required

| Tool | MiCA Articles | Description |
|------|--------------|-------------|
| `mica_full_pack` | 22–58 (12 articles) | Complete MiCA evidence for one token in one call |
| `mica_market_overview` | All | Market-wide: peg alerts, significant issuers, interest violations, audit status |
| `generate_report` | All | Signed PDF (MiCA, DORA, RWA Risk, Macro Risk), XRPL-anchored |

---

## AI Gateway Example

```json
{
  "tool": "ai_query",
  "input": { "query": "Is EURC MiCA-compliant and what is its reserve quality?" }
}

// Response: signed evidence bundle
{
  "intent": "mica_compliance",
  "asset": "EURC",
  "mica_compliant": true,
  "grade": "A",
  "score": 81.7,
  "evidence": {
    "pack_id": "FO-AIG-99F42D062F67",
    "content_hash": "sha256:42738bace3...",
    "verifiable": true
  }
}
```

---

## Response Schema (v2.3 — all tools identical)

Every tool returns the same envelope:

```json
{
  "schema_version": "2.3",
  "tool_version": "2.3.1",
  "tool": "peg_deviation",
  "request_id": "fo-abc123",
  "timestamp": "2026-02-21T18:00:00Z",
  "status": "COMPLIANT",
  "reason_codes": ["MICA_COMPLIANT"],
  "mica_articles": ["35"],
  "confidence": 0.9,
  "evidence": { "..." },
  "signature": { "alg": "HMAC-SHA256", "payload_hash": "..." },
  "verify_url": "https://feedoracle.io/verify"
}
```

---

## MiCA Coverage

19 articles covered across 18 regulatory tools (Art. 16/48, 22, 23/52, 24/25, 26/27, 28, 29/30, 35, 36, 37/55, 45/58, 51, 53, 66).

Not covered (process/legal, not data-trackable): Art. 6, 9, 18, 21

---

## Transports

| Transport | URL |
|-----------|-----|
| Streamable HTTP | https://feedoracle.io/mcp/ |
| SSE (legacy) | https://feedoracle.io/mcp/sse |
| Discovery | https://feedoracle.io/mcp/.well-known/mcp/server.json |

---

## Pricing

| Tier | Calls/day | HEAVY Tools | Reports | Price |
|------|-----------|-------------|---------|-------|
| Anonymous | 20 | — | — | Free |
| Free (key) | 100 | — | — | Free |
| Pro | 500 | ✓ | ✓ | $299/mo |
| Enterprise | Unlimited | ✓ | ✓ | Contact |

---

## The FeedOracle MCP Ecosystem

| Server | URL | Purpose |
|--------|-----|---------|
| **Compliance Oracle** (this) | `https://feedoracle.io/mcp/` | MiCA/DORA regulatory data + AI Evidence Layer |
| **Macro Oracle** | `https://feedoracle.io/mcp/macro/` | Fed/ECB economic indicators, 86 FRED series |
| **Stablecoin Risk** | `https://feedoracle.io/mcp/risk/` | 7-signal stablecoin operational risk (SAFE/CAUTION/AVOID) |

> "May your agent trade this?" → Compliance Oracle  
> "Should your agent trade right now?" → Macro Oracle  
> "Is this stablecoin safe for settlement?" → Stablecoin Risk

---

🌐 [feedoracle.io](https://feedoracle.io) · 📖 [Docs](https://feedoracle.io/docs.html) · 🏥 [Health](https://feedoracle.io/mcp/health)

**License:** Proprietary — © 2026 FeedOracle.
