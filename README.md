# FeedOracle MCP Server

Enterprise-grade evidence infrastructure for regulated tokenized markets. Provides cryptographically verified compliance and risk intelligence via the Model Context Protocol (MCP).

## Quick Start

```bash
# Streamable HTTP (recommended)
claude mcp add --transport http feedoracle https://feedoracle.io/mcp/

# SSE (legacy)
claude mcp add --transport sse feedoracle https://feedoracle.io/mcp/sse
```

Free tier: 100 calls/day, no API key required.

## Tools

| Tool | Description | Read/Write |
|------|-------------|------------|
| `compliance_preflight` | Pre-flight regulatory check → PASS/WARN/BLOCK | Read |
| `mica_status` | MiCA EU authorization status (ESMA/EBA cross-ref) | Read |
| `evidence_profile` | Multi-dimensional evidence scoring across 9 dimensions | Read |
| `custody_risk` | Custody & counterparty risk, SIFI, concentration (DORA Art.28) | Read |
| `market_liquidity` | DEX liquidity depth & exit channels (MiCA Art.45) | Read |
| `evidence_leaderboard` | 61 RWA protocols ranked by evidence grade A-F | Read |
| `rlusd_integrity` | RLUSD real-time integrity & attestation | Read |
| `macro_risk` | US macro risk composite from 86 FRED series | Read |
| `generate_report` | Signed, XRPL-anchored PDF compliance report | Write |

## Coverage

- **61 RWA protocols** with 9-dimension risk assessment
- **40+ stablecoins** with MiCA compliance flags
- **118 FRED economic series** for macro risk
- **50+ blockchain carbon footprints** for ESG

## Authentication

| Tier | Daily Calls | API Key | Reports |
|------|-------------|---------|---------|
| Free | 100 | Not required | ❌ |
| Pro ($299/mo) | 25,000 | Required | ✅ |
| Enterprise | Unlimited | Required | ✅ |

## Safety Annotations

All tools include MCP safety annotations:
- 8 tools: `readOnlyHint: true` — read-only data queries
- 1 tool: `destructiveHint: true` — `generate_report` creates new documents

## Transport

- **Streamable HTTP** (primary): `https://feedoracle.io/mcp/`
- **SSE** (legacy): `https://feedoracle.io/mcp/sse`
- **Health**: `https://feedoracle.io/mcp/health`

## Discovery

- Server metadata: `https://feedoracle.io/.well-known/mcp/server.json`
- OpenAPI spec: `https://feedoracle.io/.well-known/openapi.json`
- AI plugin: `https://feedoracle.io/.well-known/ai-plugin.json`

## Skill

This repository includes a Claude Skill (`SKILL.md`) that teaches Claude when and how to use FeedOracle for compliance queries. The skill triggers on mentions of MiCA, DORA, stablecoin compliance, RWA risk, custody risk, and related regulatory topics.

## Links

- **Website**: [feedoracle.io](https://feedoracle.io)
- **Documentation**: [feedoracle.io/docs](https://feedoracle.io/docs/)
- **Examples**: [feedoracle.io/docs/mcp-examples.html](https://feedoracle.io/docs/mcp-examples.html)
- **Privacy**: [feedoracle.io/privacy](https://feedoracle.io/privacy)
- **Terms**: [feedoracle.io/terms](https://feedoracle.io/terms)

## License

Proprietary. © 2026 FeedOracle. All rights reserved.
