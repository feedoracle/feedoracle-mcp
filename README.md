<div align="center">

# FeedOracle — Compliance Evidence Infrastructure

**Signed, verifiable evidence for AI-driven compliance decisions. MiCA · DORA · AMLR.**

[![Server Status](https://img.shields.io/badge/server-live-10B898?style=flat-square)](https://feedoracle.io/mcp/health)
[![Oracles](https://img.shields.io/badge/oracles-40_mesh--wide-3B82F6?style=flat-square)](https://feedoracle.io/data/feedoracle-metrics.json)
[![Tools](https://img.shields.io/badge/tools-549_mesh--wide-3B82F6?style=flat-square)](https://feedoracle.io/data/feedoracle-metrics.json)
[![Soak Test](https://img.shields.io/badge/soak_test-12%2F12-10B898?style=flat-square)](https://tooloracle.io/oraclenet/soak.json)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](LICENSE)

*Figures below were verified against the canonical metrics source on 2026-07-22: [feedoracle-metrics.json](https://feedoracle.io/data/feedoracle-metrics.json)*

[Website](https://feedoracle.io) · [Docs](https://feedoracle.io/docs.html) · [Trust](https://feedoracle.io/trust/) · [Pricing](https://feedoracle.io/pricing.html)

</div>

---

## What is FeedOracle?

FeedOracle is compliance-evidence infrastructure for regulated entities and their AI agents. It turns questions like *"Is USDT compliant for trading in the EU under MiCA?"* into signed, sourced, auditable answers instead of an LLM guess.

FeedOracle is the compliance layer of a larger oracle mesh (**OracleNet**, operated by sibling project [ToolOracle](https://github.com/ToolOracle)); this repository is the FeedOracle-branded MCP server itself.

## Who is it for?

- Compliance and risk teams at banks, PSPs, and crypto/RWA firms who need MiCA/DORA/AMLR evidence they can hand to an auditor
- AI agents and agent frameworks that need a machine-checkable "can I do this?" answer before executing a financial action
- Developers building on MCP who want a real, live compliance data source rather than a toy example

## What problem does it solve?

Regulatory questions — "is this token MiCA-authorized", "does this counterparty appear on a sanctions list", "is our DORA posture audit-ready" — are usually answered by a human trawling PDFs, or by an LLM guessing with no source. FeedOracle answers them from live regulatory registers and internal risk models, returns a signed evidence object (source, timestamp, confidence, hash), and lets you verify it independently.

## Try it in 60 seconds

`tools/list` and `ping` are open on this endpoint — no signup required. Note: an anonymous `tools/list` call against this specific endpoint currently surfaces a smaller live subset (observed 2026-07-22: ~25 tools) — the full 549-tool count is the combined catalogue across FeedOracle's own oracles plus the shared mesh it draws on (see "What's actually live" below), not what a single anonymous call returns:

```bash
curl -s -X POST https://feedoracle.io/mcp/ \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"ping","arguments":{}}}'
```

Most compliance tools (e.g. `mica_status`) need a free API key. Register in the same call flow, no card required:

```bash
curl -s -X POST https://feedoracle.io/mcp/ \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"kya_register","arguments":{"agent_name":"my-agent","agent_purpose":"compliance checks","owner_email":"you@example.com","owner_org":"Your Org"}}}'
```

This returns an API key and a starting balance of free units. **Note: this call creates a real registration and issues a secret API key. Store it securely and do not commit it.**

## MCP quickstart

```bash
claude mcp add --transport http feedoracle https://feedoracle.io/mcp/
```

```json
{
  "mcpServers": {
    "feedoracle": {
      "url": "https://feedoracle.io/mcp/"
    }
  }
}
```

Then ask your agent things like:

```
Is USDT compliant for trading in the EU under MiCA?
Run a DORA readiness check
Screen this counterparty for sanctions exposure
```

## Minimal examples

**Python**
```python
import requests

resp = requests.post("https://feedoracle.io/mcp/", json={
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "ping", "arguments": {}}
})
print(resp.json())
```

**Node**
```js
const resp = await fetch("https://feedoracle.io/mcp/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    jsonrpc: "2.0", id: 1, method: "tools/call",
    params: { name: "ping", arguments: {} }
  })
});
console.log(await resp.json());
```

More runnable examples in [`examples/`](examples/), including a full [`python_client.py`](examples/python_client.py) and ready-made [Claude Desktop](examples/claude_desktop_config.json) / [Cursor](examples/) configs.

## What's actually live

FeedOracle's own primary oracles (verified against [live metrics](https://feedoracle.io/data/feedoracle-metrics.json), 2026-07-22):

| Server | Tools | Scope |
|---|---|---|
| AmpelOracle | 50 | DORA — 26 tracked control areas, traffic-light scoring, board reports |
| MiCAOracle | 24 | MiCA stablecoin authorization, peg, reserves |
| FeedOracle Compliance | 29 | Unified preflight, evidence packs, audit trail |
| ReserveOracle | 11 | MiCA Art. 36 reserve quality, attestation verification |
| RiskOracle | 7 | Stablecoin + RWA operational risk scoring |
| PredictionGuard | 28 | Hallucination-layer policy enforcement for compliance agents |

Beyond these 6 FeedOracle-branded servers (149 tools), FeedOracle also draws on a shared compliance-infrastructure mesh (**OracleNet**) of additional oracles covering DORA operational, security/runtime, and blockchain-risk categories — same product, broader shared infrastructure. Combined, mesh-wide: **40 registered oracles · 39 online · 549 catalogued tools · 17 data sources** (as of 2026-07-22, always current at [feedoracle-metrics.json](https://feedoracle.io/data/feedoracle-metrics.json)). Full mesh detail lives in [ToolOracle/oraclenet](https://github.com/ToolOracle/oraclenet) — not duplicated here so it can't drift out of sync.

**A note on these numbers, since they describe different things:** "oracle" here means a registered mesh node, not necessarily a single MCP server process — FeedOracle's own 6 oracles above map 1:1 to servers, but that isn't guaranteed mesh-wide. "549 tools" is the mesh-wide catalogue total; it is not what a single anonymous `tools/list` call against this endpoint returns (see Quickstart above). Use [feedoracle-metrics.json](https://feedoracle.io/data/feedoracle-metrics.json) as the source of truth rather than any number in this README if they ever disagree.

## Free vs. paid

- `tools/list` and `ping` are open, no key required
- `kya_register` (free, no card) issues an API key with a starting balance of free welcome units
- Beyond the free allowance: pay-as-you-go via Stripe (card/SEPA) or the [x402 protocol](https://tooloracle.io/x402/) (USDC on Base, no signup, no subscription)
- Current per-unit pricing is returned live in each tool's `402 payment_required` response rather than reproduced here, so it can't go stale
- There is no fixed monthly subscription bundle at this time; see [feedoracle.io/pricing.html](https://feedoracle.io/pricing.html) for current access options

## Evidence & trust model

Supported evidence responses include signed receipt fields — source, timestamp, confidence, and a content hash. Verify the signature and anchor fields returned by each individual tool response rather than assuming a fixed set applies to every tool; not all tools are evidence-bearing in the same way (e.g. `ping` returns a lighter operational receipt).

```bash
curl -s https://feedoracle.io/.well-known/jwks.json   # public keys to verify signatures
```

Live verification on 2026-07-22 confirmed ES256K and ML-DSA-65 signatures plus NIST and CURBy randomness-beacon anchors on the tested response. Coverage can vary by tool and response type; verify the fields returned with each individual result. Earlier versions of this document described an on-chain escrow-based settlement mechanism on Base; that mechanism is now retired and not accepting new activity — it has not been re-verified as accurate for the period it originally described, so no historical settlement figures are repeated here. For current anchor and verification status, see [Trust](https://feedoracle.io/trust/).

Full docs: [`docs/TRUST_POLICY.md`](docs/TRUST_POLICY.md) · [`docs/AUDIT_TRAIL.md`](docs/AUDIT_TRAIL.md) · [`docs/KYA.md`](docs/KYA.md) · [`docs/BILLING.md`](docs/BILLING.md) · [`docs/WORKFLOWS.md`](docs/WORKFLOWS.md)

**On evidence vs. verdicts:** FeedOracle returns evidence indicators for human/agent review — source, confidence, and status — not a legal compliance verdict. "PASS" means no adverse indicators were found in the checked sources, not a guarantee of compliance.

## Security & responsible use

- Report vulnerabilities privately (see repository Security tab) — please don't open a public issue for security-sensitive findings
- Never commit API keys, wallet credentials, or `.env` files — see [`.gitignore`](.gitignore)
- This server executes real, priced actions (registration, paid tool calls); review [`docs/BILLING.md`](docs/BILLING.md) before wiring up autonomous agents

## Contributing

Issues and PRs are welcome — especially for [`examples/`](examples/), additional client integrations, and documentation fixes. There's no CONTRIBUTING.md yet; for anything beyond a small fix, please open an issue first so we can align on scope before you invest the time.

## License

MIT — see [LICENSE](LICENSE).

## Roadmap

- **Live**: MCP server, MiCA/DORA/AMLR tool set, x402 micropayments, signed evidence objects, KYA self-registration
- **Beta**: mesh-wide routing improvements across OracleNet
- **Planned**: broader regulatory framework coverage (CSRD, NIS2) — tracked in [CHANGELOG.md](CHANGELOG.md)

---

<div align="center">

DORA has applied since 17 January 2025. MiCA is fully applicable; the EU-wide CASP transitional period ended no later than 1 July 2026.

🇩🇪 Built in Germany · 🔐 Signed evidence · 🧾 Verifiable receipts

</div>
