<div align="center">

# FeedOracle — DORA Operating System

**The first compliance operating system for DORA, MiCA & AMLR.**

Continuous monitoring. Signed evidence. Audit-ready reports.

[![Server Status](https://img.shields.io/badge/server-live-10B898?style=flat-square)](https://feedoracle.io/mcp/health)
[![MCP Servers](https://img.shields.io/badge/MCP_servers-11-3B82F6?style=flat-square)](https://feedoracle.io/mcp.html)
[![Tools](https://img.shields.io/badge/tools-50-3B82F6?style=flat-square)](https://feedoracle.io/mcp.html)
[![DORA Articles](https://img.shields.io/badge/DORA_articles-26/26-10B898?style=flat-square)](https://feedoracle.io/dora/)
[![Free Tier](https://img.shields.io/badge/free_tier-100_calls%2Fday-10B898?style=flat-square)](https://feedoracle.io/pricing.html)

[Website](https://feedoracle.io) · [DORA OS](https://feedoracle.io/dora/) · [Dashboard](https://feedoracle.io/ampel/) · [Docs](https://feedoracle.io/docs.html) · [Trust](https://feedoracle.io/trust/) · [Pricing](https://feedoracle.io/pricing.html)

</div>

---

## The problem

DORA and MiCA require **continuous proof** — not one-time documentation. But most compliance teams still prepare evidence manually before each audit: spreadsheets, email chains, unsigned PDFs, unclear timestamps.

When the regulator asks "Can you prove this?", the answer is silence.

## What FeedOracle does

FeedOracle is the **operating layer** for regulatory compliance. It continuously monitors your DORA and MiCA obligations, generates cryptographically signed evidence, and delivers audit-ready reports — before the regulator asks.

```
Compliance Team              FeedOracle DORA OS              Regulator
      |                            |                              |
      |-- Entity anlegen --------->|                              |
      |                            |-- 39 automated checks/day    |
      |                            |-- Sign every finding (ES256K)|
      |                            |-- Anchor on-chain            |
      |<-- Dashboard: 97% GREEN --|                              |
      |                            |                              |
      |    Audit day...            |                              |
      |                            |                              |
      |-- "Generate Report" ------>|                              |
      |<-- Signed PDF + evidence --|-- Verify independently ----->|
      |                            |         Audit passed         |
```

## Quick start

One command. No API key needed.

```bash
claude mcp add --transport http feedoracle https://feedoracle.io/mcp/
```

<details>
<summary>Claude Desktop / Cursor / Windsurf config</summary>

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

Then ask:

```
Is USDC compliant for trading in the EU under MiCA?
What is our DORA readiness score?
Generate a board report for our entity.
```

## 11 MCP servers · 50 tools (main server)

| Server | Tools | Purpose |
|--------|-------|---------|
| **Compliance Oracle** | 33 | MiCA preflight, evidence packs, DORA artifacts, audit trail, AI queries |
| **DORA Ampel** | 46 | All 26 articles, traffic-light scoring, finding lifecycle, board reports |
| **MiCA Ampel** | 24 | Stablecoin authorization, peg monitoring, whitepaper validation |
| **AML Oracle** | 12 | Sanctions screening (EU+OFAC+UN), PEP checks, adverse media |
| **AgentGuard** | 20 | AI agent governance: pre-checks, output scanning, kill-switch |
| **Research Oracle** | 11 | Semantic Scholar, arXiv, regulatory research |
| **EULaw Oracle** | 8 | EU regulatory text search and analysis |
| **RegWatch Oracle** | 6 | Regulatory change monitoring |
| **ESMA Oracle** | 8 | ESMA register queries, MiCA authorization lookup |
| **Macro Oracle** | 22 | 86 FRED + ECB indicators, regime classification, yield curve |
| **Risk Oracle** | 13 | 7-signal stablecoin risk scoring, 105+ tokens |
| **Governance** | 3 | policy_explain, price_quote, agent_reputation_score |
| **DetectiveOracle** | 5 | Fraud detection, anomaly analysis, case management |
| **SupportOracle** | 8 | Auto-diagnostics, health checks, onboarding, tickets |
| **Trust Passport** | 1 | Signed agent trust document |

### The closed loop

Every compliance check follows one path:

```
Check → Evidence → Finding → Owner → Remediation → Re-Test → Closure → Signed Report
```

Automated daily via 5-stage cron pipeline. SHA-256 audit chain. 3-level escalation (Owner → CISO → Board).

## DORA OS — 6 layers, full coverage

| Layer | What it covers | Articles |
|-------|---------------|----------|
| **Governance & Reporting** | Board packs, KPIs, framework review, annual review | Art. 5–6 |
| **Resilience & Recovery** | BIA, RTO/RPO, DR tests, crisis plans, scenarios | Art. 11–12 |
| **Asset & Dependency Mapping** | Asset inventory, blast radius, SPOF, impact simulation | Art. 8 |
| **Register & Contracts** | Register of Information, 15 Art. 30 clauses, exit plans | Art. 28–30 |
| **Third-Party Risk & AML** | Provider risk, sanctions, PEP, KYC, NatCat, GLEIF | Art. 28–44 |
| **Threat Intel & Incident** | CVE/KEV, CERT-Bund, MITRE ATT&CK, incident timeline | Art. 6–27 |

> Most compliance tools cover only the bottom layer (threat intel). DORA demands operational proof across all 6 layers — from CVE patches to board-level governance reports.


## Agent Trust Runtime

Complete trust infrastructure for autonomous agents:

| Layer | What it does | Tools |
|-------|-------------|-------|
| **AgentGuard** | Identity (KYA), policy enforcement, kill-switch | 20 |
| **DetectiveOracle** | Fraud scoring, anomaly detection, case management | 5 |
| **SupportOracle** | Self-healing diagnostics, onboarding, ticket system | 8 |
| **Governance** | Policy explain, pricing, reputation scoring | 3 |
| **Trust Passport** | Signed agent reputation document | 1 |

Agent lifecycle — no human needed:

```
Register → Preflight → Execute → Prove → Rate → Monitor → Support → Passport
```

## What makes this different

| | Traditional compliance | FeedOracle DORA OS |
|---|---|---|
| **Approach** | Checklists & templates | Closed-loop automation |
| **Evidence signing** | None | ES256K on every artifact |
| **On-chain anchoring** | None | Polygon + XRPL |
| **AI agent integration** | None | 203 MCP tools, Claude/Cursor native |
| **Automated escalation** | Manual workflows | 3-level auto (Owner → CISO → Board) |
| **Cross-regulation** | DORA only | DORA + MiCA + AMLR simultaneous |
| **BaFin incident reporting** | Templates | ITS 2024/1772 draft + 4-eyes approval |
| **Self-service trial** | "Book a demo" | 5 min, no login, instant score |
| **Pricing** | €1,500–25,000/mo | Free tier · Starter €49/mo |

## Verify in 30 seconds

No account needed. No trust required.

```bash
# 1. Get signed evidence
curl -s -X POST https://feedoracle.io/ai/query \
  -H "Content-Type: application/json" \
  -d '{"question":"Is USDC MiCA compliant?"}'

# 2. Verify the signature
curl -s https://feedoracle.io/.well-known/jwks.json

# 3. Check on-chain proof
curl -s https://feedoracle.io/proof/
```

## Pricing

| Tier | Price | Best for |
|------|-------|----------|
| **Free** | €0 | First DORA assessment — 100 calls/day, no key needed |
| **Starter** | €49/mo | Evaluation — all tools, signed evidence |
| **Growth** | €199/mo | Production — PDF reports, webhooks |
| **Pro** | €499/mo | Compliance teams — MiCA + DORA + AI queries |
| **Enterprise** | €1,499/mo | Regulated institutions — dedicated infra, SLA, SEPA |

## Links

| | |
|---|---|
| Website | [feedoracle.io](https://feedoracle.io) |
| DORA OS | [feedoracle.io/dora](https://feedoracle.io/dora/) |
| Dashboard | [feedoracle.io/ampel](https://feedoracle.io/ampel/) |
| Trust | [feedoracle.io/trust](https://feedoracle.io/trust/) |
| Docs | [feedoracle.io/docs](https://feedoracle.io/docs.html) |
| Uptime | [uptime.feedoracle.io](https://uptime.feedoracle.io) |
| Health | [feedoracle.io/mcp/health](https://feedoracle.io/mcp/health) |
| JWKS | [.well-known/jwks.json](https://feedoracle.io/.well-known/jwks.json) |
| On-chain proof | [feedoracle.io/proof](https://feedoracle.io/proof/) |

---

<div align="center">

**DORA deadline: July 2026. MiCA is already in force.**

*Evidence by Design.*

🇩🇪 Built in Germany · 🔐 ES256K signed · ⛓️ Polygon + XRPL anchored · 📄 BaFin-ready

</div>
