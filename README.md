<div align="center">

# FeedOracle — Compliance Evidence Infrastructure

**Signed evidence for every AI compliance decision. MiCA · DORA · AMLR.**

102 MCP oracles · 1,235 tools · Execute pipeline · Neural routing · On-chain proof

[![Server Status](https://img.shields.io/badge/server-live-10B898?style=flat-square)](https://feedoracle.io/mcp/health)
[![Oracles](https://img.shields.io/badge/oracles-102-3B82F6?style=flat-square)](https://tooloracle.io/oraclenet/cockpit.json)
[![Tools](https://img.shields.io/badge/tools-1%2C235-3B82F6?style=flat-square)](https://tooloracle.io/assets/catalog.json)
[![Soak Test](https://img.shields.io/badge/soak_test-12%2F12-10B898?style=flat-square)](https://tooloracle.io/oraclenet/soak.json)
[![Free Tier](https://img.shields.io/badge/free_tier-100_calls%2Fday-10B898?style=flat-square)](https://feedoracle.io/pricing.html)

[Website](https://feedoracle.io) · [OracleNet](https://github.com/ToolOracle/oraclenet) · [Docs](https://feedoracle.io/docs.html) · [Trust](https://feedoracle.io/trust/) · [Pricing](https://feedoracle.io/pricing.html)

</div>

---

## What changed in v6.0

FeedOracle is no longer just a compliance server. It's now the compliance layer within **OracleNet** — an autonomous mesh of 102 specialized oracles that understand, execute, prove, and learn.

**New in v6.0:**
- **Execute Pipeline**: `quantum_ask` takes a natural language question, routes it to the right oracle, executes the call, and returns a signed result with content hash — one call
- **Neural Learning**: Every execution is logged as a synapse. Routing weights update automatically. Better oracles get preferred.
- **On-Chain Settlement**: 104 deals settled on Base Mainnet via escrow smart contract
- **90 Oracles**: From 11 servers to 102, covering compliance, blockchain (13 chains), finance, business, payments, and more
- **Hardening**: Idempotency, circuit breaker, rate limiting, replay protection
- **Soak Testing**: 12 queries across 6 categories, running every 5 minutes, 24/7

## Quick start

```bash
claude mcp add --transport http feedoracle https://feedoracle.io/mcp/
```

```json
{
  "mcpServers": {
    "feedoracle": {
      "url": "https://feedoracle.io/mcp/"
    },
    "oraclenet": {
      "url": "https://tooloracle.io/quantum/mcp/"
    }
  }
}
```

Then ask:

```
Is USDT compliant for trading in the EU under MiCA?
What is the current Fed rate?
Bitcoin network overview
Run a DORA readiness check
```

## Architecture

```
Agent → quantum_ask("Is USDT compliant?")
  → Intent Parse (EN/DE)
    → Oracle found (ComplianceOracle, weight 2.55)
      → MCP Execute (SSE + session handshake)
        → Result: BLOCK, confidence 100%
          → Content Hash (SHA-256)
            → Neural Synapse + Reward
              → Escrow Settlement (Base, USDC)
                → BaseScan verifiable
```

## Compliance Layer (FeedOracle Core)

| Server | Tools | Purpose |
|--------|-------|---------|
| **Compliance Oracle** | 29 | MiCA preflight, evidence packs, sanctions, AML |
| **DORA Ampel** | 50 | All 26 articles, traffic-light scoring, board reports |
| **MiCA Ampel** | 24 | Stablecoin authorization, peg monitoring |
| **Macro Oracle** | 22 | 86 FRED + ECB indicators, regime classification |
| **Risk Oracle** | 13 | 7-signal stablecoin risk scoring, 105+ tokens |
| **AML Oracle** | 12 | Sanctions screening (EU+OFAC+UN), PEP checks |
| **AgentGuard** | 20 | AI agent governance, policy enforcement |

## OracleNet Layer (90 Oracles)

| Category | Oracles | Tools |
|----------|---------|-------|
| Compliance & Regulation | 40 | 521 |
| Trust & Agent Infrastructure | 10 | 107 |
| Finance & Markets | 10 | 116 |
| Business Intelligence | 10 | 97 |
| Travel & Lifestyle | 8 | 79 |
| Blockchain & DeFi | 14 | 150 |
| Payment & Settlement | 4 | 48 |

Full details: [github.com/ToolOracle/oraclenet](https://github.com/ToolOracle/oraclenet)

## On-Chain Proof

| Chain | Type | Reference |
|-------|------|-----------|
| Base | Escrow (104 deals settled) | [0x330F...051F](https://basescan.org/address/0x330F99f34246EA375333b9C01Ed6BB49190B051F) |
| Polygon | Evidence hash | Block 84,921,488 |
| XRPL | Beacon pulse | [rJffix...pzD](https://xrpscan.com/account/rJffixdE2JGWGf12Rh9D9kjDgd6jVxVpzD) |
| Hedera | Smart contract | [0.0.10420310](https://hashscan.io/mainnet/contract/0.0.10420310) |

## Verify

```bash
# Get signed evidence
curl -s -X POST https://feedoracle.io/ai/query \
  -H "Content-Type: application/json" \
  -d '{"question":"Is USDC MiCA compliant?"}'

# Verify signature
curl -s https://feedoracle.io/.well-known/jwks.json

# Check live mesh
curl -s https://tooloracle.io/oraclenet/cockpit.json
```

## Pricing

| Tier | Price | Included |
|------|-------|----------|
| **Free** | €0 | 100 calls/day, no key needed |
| **Starter** | €49/mo | All tools, signed evidence |
| **Growth** | €199/mo | PDF reports, webhooks |
| **Pro** | €499/mo | MiCA + DORA + AI queries |
| **Enterprise** | €1,499/mo | Dedicated infra, SLA, SEPA |

## x402 — AI Agent Micropayments (USDC on Base)

AI agents can pay per tool call automatically via the x402 protocol. No API key, no signup, no subscription.

```bash
# Agent calls any tool → gets HTTP 402 with payment requirements
curl https://tooloracle.io/x402/rank/mcp/ \
  -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"check_ranking","arguments":{"domain":"example.com"}},"id":1}'

# Agent sends USDC on Base, retries with tx hash → tool executes
# Pricing: $0.01-$0.15 per call depending on tool complexity
```

| | |
|---|---|
| Gateway | [tooloracle.io/x402/](https://tooloracle.io/x402/) |
| Wallet | `0x4a4B1F45a00892542ac62562D1F2C62F579E4945` |
| Network | Base Mainnet (USDC) |
| Products | 35 |
| Tools | 254 |
| Discovery | [.well-known/x402](https://tooloracle.io/.well-known/x402) |

## Links

| | |
|---|---|
| OracleNet | [github.com/ToolOracle/oraclenet](https://github.com/ToolOracle/oraclenet) |
| Website | [feedoracle.io](https://feedoracle.io) |
| Soak Test | [tooloracle.io/oraclenet/soak.json](https://tooloracle.io/oraclenet/soak.json) |
| Cockpit | [tooloracle.io/oraclenet/cockpit.json](https://tooloracle.io/oraclenet/cockpit.json) |
| Trust | [feedoracle.io/trust](https://feedoracle.io/trust/) |
| JWKS | [feedoracle.io/.well-known/jwks.json](https://feedoracle.io/.well-known/jwks.json) |

---

<div align="center">

**DORA deadline: July 2026. MiCA is already in force.**

🇩🇪 Built in Germany · 🔐 ES256K signed · ⛓️ 4-chain anchored · 🧠 Neural routing · 📊 24/7 soak-tested

</div>
