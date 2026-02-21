# FeedOracle MCP Server v2.3.1

Enterprise MiCA compliance and RWA risk intelligence for AI agents. Real-time monitoring of **18 MiCA articles** across 80+ stablecoins and RWA protocols — cryptographically signed, machine-readable, enterprise-ready.

🔗 **Landing Page:** [feedoracle.io/mcp](https://feedoracle.io/mcp)  
📋 **Discovery:** [feedoracle.io/mcp/.well-known/mcp/server.json](https://feedoracle.io/mcp/.well-known/mcp/server.json)  
📖 **Docs:** [feedoracle.io/docs](https://feedoracle.io/docs)

---

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

Free tier: 20 calls/day — no API key required to start.

---

## Tools (18)

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
| `evidence_leaderboard` | 36, 37, 45 | Top 80+ RWA protocols ranked by evidence grade |
| `macro_risk` | — | US macro composite from 86 FRED series (recession, inflation, Fed) |

### 🔴 HEAVY — API key required

| Tool | MiCA Articles | Description |
|------|--------------|-------------|
| `mica_full_pack` | 22–58 (12 articles) | Complete MiCA evidence for one token in one call. `articles_covered` + `overall_mica_compliant` |
| `mica_market_overview` | All | Market-wide: peg alerts, significant issuers, interest violations, audit status |
| `generate_report` | All | Signed PDF (MiCA, DORA, RWA Risk, CSRD), XRPL-anchored |

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
  "jurisdiction": "EU",
  "status": "COMPLIANT",
  "reason_codes": ["MICA_COMPLIANT"],
  "mica_articles": ["35"],
  "confidence": 0.9,
  "asset": {
    "input_symbol": "EURC",
    "resolved_slug": "eurc",
    "confidence": 1.0
  },
  "evidence": { ... },
  "sources": [
    {
      "registry": "Peg Monitor",
      "evidence_class": "MARKET_DATA",
      "fetched_at": "2026-02-21T18:00:00Z"
    }
  ],
  "meta": {
    "cost_class": "LIGHT",
    "requires_key": false,
    "data_freshness": "LIVE",
    "jurisdiction_scope": "EU",
    "disclaimer": "Based on available evidence. Not legal advice."
  },
  "signature": { "alg": "HMAC-SHA256", "payload_hash": "..." },
  "verify_url": "https://feedoracle.io/verify"
}
```

### Status Taxonomy

| Context | Values |
|---------|--------|
| **MiCA regulatory tools** | `COMPLIANT` · `PENDING` · `NOT_AUTHORIZED` · `UNKNOWN` · `SIGNIFICANT` |
| **compliance_preflight only** | `PASS` · `WARN` · `BLOCK` |

### Evidence Classes

`REGISTER` · `NCA_NOTICE` · `ISSUER_DISCLOSURE` · `ATTESTATION` · `MARKET_DATA` · `ONCHAIN_INFERENCE`

---

## MiCA Coverage

**19 articles covered** across 18 tools:

```
Art. 16/48 — Authorization (ESMA register)
Art. 22    — Issuer revenue threshold
Art. 23/52 — Interest prohibition (18,000+ DeFi pools scanned)
Art. 24/25 — Reserve management policy
Art. 26/27 — Custody & segregation
Art. 28    — Own funds requirements
Art. 29/30 — Recovery & redemption plans
Art. 35    — Peg stability (live FX-corrected)
Art. 36    — Reserve stress test proxy
Art. 37/55 — Independent audit freshness
Art. 45/58 — Significant issuer thresholds (€5B)
Art. 51    — Redemption at par
Art. 53    — Reserve asset quality (Art.53 eligibility %)
Art. 66    — Sustainability disclosures (50+ chains)
```

**Not covered** (process/legal, not data-trackable): Art. 6, 9, 18, 21

---

## Transports

| Transport | URL |
|-----------|-----|
| Streamable HTTP | `https://feedoracle.io/mcp/` |
| SSE (legacy) | `https://feedoracle.io/mcp/sse` |
| Discovery | `https://feedoracle.io/mcp/.well-known/mcp/server.json` |

---

## Pricing

| Tier | Calls/day | HEAVY Tools | Reports | Price |
|------|-----------|-------------|---------|-------|
| Anonymous | 20 | — | — | Free |
| Free (key) | 50 | — | — | Free |
| Pro | 500 | ✓ | ✓ | $299/mo |
| Enterprise | Unlimited | ✓ | ✓ | [Contact](mailto:enterprise@feedoracle.io) |

---

## Examples

See [`examples/`](./examples/) for ready-to-use configs:

- **[claude_desktop_config.json](./examples/claude_desktop_config.json)** — Claude Desktop
- **[cursor_mcp.json](./examples/cursor_mcp.json)** — Cursor / Windsurf
- **[python_client.py](./examples/python_client.py)** — Python SDK client
- **[health_check.sh](./examples/health_check.sh)** — Quick server test
- **[sample_prompts.md](./examples/sample_prompts.md)** — Copy-paste prompts

---

## Links

- 🌐 [feedoracle.io](https://feedoracle.io)
- 🏥 [Health Check](https://feedoracle.io/mcp/health)
- 📋 [server.json](https://feedoracle.io/mcp/.well-known/mcp/server.json)
- 📖 [Docs](https://feedoracle.io/docs)
- 📄 [Terms](https://feedoracle.io/terms)

## License

Proprietary — © 2026 FeedOracle. API usage subject to [Terms of Service](https://feedoracle.io/terms).
