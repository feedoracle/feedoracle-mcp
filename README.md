# FeedOracle MCP Server

Enterprise-grade evidence infrastructure for regulated tokenized markets. Provides cryptographically verified compliance and risk intelligence via the Model Context Protocol (MCP).

🔗 **Landing Page:** [feedoracle.io/mcp](https://feedoracle.io/mcp)

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

Free tier: 20 calls/day anonymous, 50/day with API key. No auth required to start.

## Tools

| Tool | Description | Type |
|------|-------------|------|
| `compliance_preflight` | PASS/WARN/BLOCK verdict for any token | read |
| `mica_status` | MiCA EU authorization check | read |
| `evidence_profile` | 9-dimension risk scoring (A-F) | read |
| `custody_risk` | SIFI status, concentration analysis | read |
| `market_liquidity` | DEX depth & exit channels | read |
| `evidence_leaderboard` | Top 61 RWA protocols ranked | read |
| `rlusd_integrity` | RLUSD real-time attestation | read |
| `macro_risk` | 86 FRED series risk dashboard | read |
| `generate_report` | Signed PDF, blockchain-anchored | write |

## Examples

See [`examples/`](./examples/) for ready-to-use configs and code:

- **[claude_desktop_config.json](./examples/claude_desktop_config.json)** — Drop into Claude Desktop
- **[cursor_mcp.json](./examples/cursor_mcp.json)** — Cursor / Windsurf config
- **[python_client.py](./examples/python_client.py)** — Python SDK client
- **[health_check.sh](./examples/health_check.sh)** — Quick server test
- **[sample_prompts.md](./examples/sample_prompts.md)** — Copy-paste prompts

## Transports

| Transport | URL | Protocol |
|-----------|-----|----------|
| Streamable HTTP | `https://feedoracle.io/mcp/` | HTTP POST |
| SSE (legacy) | `https://feedoracle.io/mcp/sse` | Server-Sent Events |

## Pricing

| Tier | Calls/day | Reports | Price |
|------|-----------|---------|-------|
| Anonymous | 20 | — | Free |
| Free (key) | 50 | — | Free |
| Pro | 500 | ✓ | $299/mo |
| Enterprise | Unlimited | ✓ | [Contact](mailto:enterprise@feedoracle.io) |

## Links

- 🌐 [feedoracle.io](https://feedoracle.io)
- 📖 [API Documentation](https://feedoracle.io/docs)
- 💡 [Usage Examples](https://feedoracle.io/docs/mcp-examples.html)
- 🏥 [Health Check](https://feedoracle.io/mcp/health)
- 📋 [Privacy Policy](https://feedoracle.io/privacy)

## License

Proprietary — © 2026 FeedOracle. API usage subject to [Terms of Service](https://feedoracle.io/terms).
