# FeedOracle MCP Server v4.0

**Enterprise MiCA compliance, RWA risk intelligence, AI Evidence Layer, and Enterprise Trust Layer for AI agents.**

Real-time monitoring of 18 MiCA articles across 105+ stablecoins and RWA protocols — cryptographically signed (JWS RFC 7515), machine-readable, enterprise-ready. Every response includes SLA quality signals, trust metadata, and is logged in an append-only Evidence Registry.

> **New in v4.0:** Unit-Based Billing, Know Your Agent (KYA) trust framework, Audit Trail for agent decisions. **v3.1:** Enterprise Trust Layer — JWS signing, versioned schemas, evidence registry, SLA layer, agent trust management, streaming evidence (SSE), deterministic replay, and zero-trust validation SDK.

🔗 **Landing Page:** [feedoracle.io/mcp](https://feedoracle.io/mcp)
📋 **Discovery:** [feedoracle.io/mcp/.well-known/mcp/server.json](https://feedoracle.io/mcp/.well-known/mcp/server.json)
📖 **Docs:** [feedoracle.io/docs](https://feedoracle.io/docs)
🛡️ **Trust Proof:** [feedoracle.io/trust](https://feedoracle.io/trust)

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

Free tier: 300 units/day — no API key required to start.

---

## Agent M2M Auth (no browser, no human)

Agents register and authenticate autonomously using `client_credentials`:

```bash
# 1. Register client (once)
curl -s -X POST https://feedoracle.io/mcp/register \
  -H "Content-Type: application/json" \
  -d '{"client_name":"my-agent","grant_types":["client_credentials"],"redirect_uris":["https://localhost"]}'
# Response: {"client_id": "fo_client_...", "client_secret": "fo_secret_..."}

# 2. Get Bearer token
curl -s -X POST https://feedoracle.io/mcp/token \
  -d "grant_type=client_credentials&client_id=fo_client_...&client_secret=fo_secret_...&scope=mcp:read"
# Response: {"access_token": "fo_cc_...", "token_type": "Bearer", "expires_in": 3600}

# 3. Connect to MCP
curl -N -H "Authorization: Bearer fo_cc_..." https://feedoracle.io/mcp/sse

# 4. Revoke when done (RFC 7009)
curl -s -X POST https://feedoracle.io/mcp/revoke \
  -d "token=fo_cc_...&client_id=fo_client_...&client_secret=fo_secret_..."
```

OAuth discovery: [feedoracle.io/.well-known/oauth-authorization-server](https://feedoracle.io/.well-known/oauth-authorization-server)

---

## Autonomous USDC Upgrade (Polygon)

Agents can upgrade tier without human intervention:

```bash
# 1. Get pricing
curl -s https://feedoracle.io/usdc/pricing

# 2. Create payment intent
curl -s -X POST https://feedoracle.io/usdc/intent \
  -d '{"tier":"starter","client_id":"fo_client_..."}'
# Response: {"payment_id": "fo_pay_...", "amount_usdc": 99, "payment_wallet": "0x9f59...", "chain_id": 137}

# 3. Send USDC on Polygon
#    Native USDC (0x3c499c) and USDC.e (0x2791) both accepted.

# 4. Submit TX hash -> API key issued automatically
curl -s -X POST https://feedoracle.io/usdc/verify \
  -d '{"payment_id":"fo_pay_...","tx_hash":"0x..."}'
# Response: {"status": "fulfilled", "api_key": "fo_p_...", "tier": "starter"}

# Recovery: key is permanent, retrievable by payment_id or tx_hash
curl -s https://feedoracle.io/usdc/recover/{tx_hash}
```

**Tested in production:** [TX 0x2be6dd...f95905](https://polygonscan.com/tx/0x2be6dd56aed6e45f5bacb0af53b95e7cded8b36885aabba12cb7bac282f95905) — Polygon mainnet, 67 confirmations, key issued automatically.

---

## Public Verification Script

```bash
# 38 independent checks. No account, no API key, no FeedOracle trust.
curl -O https://feedoracle.io/feedoracle_agent_verify.py
python3 feedoracle_agent_verify.py
# 38/38 checks passed
```


---

## Tools (27)

### 🤖 AI Evidence Layer — 4 tools

| Tool | Description |
|------|-------------|
| `ai_query` | Natural language → signed evidence bundle. Ask "Is USDC MiCA-compliant?" and receive a structured, cryptographically signed response |
| `evidence_bundle` | Aggregated evidence pack for a token: MiCA status, peg, reserves, custody, macro context — one call replaces 23 API calls |
| `ai_explain` | Grade explanation engine. "Why does EURC score B? What would make it Grade A?" |
| `ai_provenance` | Full data lineage graph — from FRED series IDs and ESMA register entries to chain hash. 17 nodes, 17 individual hashes |

### 🟢 LIGHT — No key, instant

| Tool | MiCA Articles | Description |
|------|---------------|-------------|
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
|------|---------------|-------------|
| `peg_history` | 35 | 30-day peg history, stability score 0–100, depeg event count |
| `interest_check` | 23, 52 | Interest prohibition scan. Scans 18,000+ DeFi pools for issuer yield |
| `evidence_profile` | 36, 37, 45 | 9-dimension evidence grade A–F (governance, custody, reserves…) |
| `market_liquidity` | 45, 51 | DEX liquidity depth and redemption exit channels |
| `evidence_leaderboard` | 36, 37, 45 | Top 61 RWA protocols & 105+ stablecoins ranked by evidence grade |
| `macro_risk` | — | US macro composite from 86 FRED series (recession, inflation, Fed) |

### 🔴 HEAVY — API key required

| Tool | MiCA Articles | Description |
|------|---------------|-------------|
| `mica_full_pack` | 22–58 (12 articles) | Complete MiCA evidence for one token in one call |
| `mica_market_overview` | All | Market-wide: peg alerts, significant issuers, interest violations, audit status |
| `generate_report` | All | Signed PDF (MiCA, DORA, RWA Risk, Macro Risk), XRPL-anchored |

---

## Enterprise Trust Layer (New in v3.1)

Every response from the MCP server now includes 6 trust layers:

```
evidence{}    → SHA-256 content hash + pack_id + blockchain anchor reference
jws{}         → RFC 7515 ES256K compact token (kid: fo-ecdsa-v1)
sla{}         → confidence (0-1), freshness_seconds, per-source health, tier
trust{}       → signature_present, schema_valid, registry_logged, replayable
schema_ref    → Versioned JSON Schema reference (e.g. "mica/v1")
```

### 8 Trust Components

| Component | Endpoint | Description |
|-----------|----------|-------------|
| **JWS Signing** | `/.well-known/jwks.json` | RFC 7515 ES256K signatures on every response. Verify via JWKS. |
| **Versioned Schemas** | `GET /schemas/` | 8 JSON Schemas (Draft 2020-12): mica, dora, rwa, macro, stablecoin-risk, amlr, sla, evidence-envelope |
| **Evidence Registry** | `GET /evidence/registry` | Append-only Compliance Transparency Log. Filters: framework, asset, date, limit |
| **Evidence SLA** | _(in every response)_ | Machine-readable quality: freshness, confidence, per-source latency/status |
| **Agent Trust** | `POST /ai/agent/register` | Agent registration with 90-day keys, reputation scoring (0-100), key rotation |
| **Streaming Evidence** | `GET /evidence/stream` | SSE events: peg_deviation, regime_change, market_stress. State-change-only. |
| **Deterministic Replay** | `GET /evidence/replay/{id}` | Byte-identical reconstruction from snapshot. `hash_match: true` = audit proof |
| **Validation SDK** | `GET /verify/self-test` | Client-side verification: `pip install feedoracle-verify` — 7 independent checks |

### Trust Layer Endpoints (15)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/schemas/` | GET | Schema registry index |
| `/schemas/v1/{framework}` | GET | Individual JSON Schema |
| `/evidence/registry` | GET | Compliance Transparency Log (paginated, 8 filters) |
| `/evidence/registry/{pack_id}` | GET | Single evidence pack detail |
| `/evidence/registry/stats` | GET | Registry statistics |
| `/evidence/stream` | GET | SSE real-time events |
| `/evidence/stream/status` | GET | Stream poller status |
| `/evidence/replay/{pack_id}` | GET | Deterministic audit replay |
| `/evidence/snapshots/stats` | GET | Snapshot archive statistics |
| `/ai/agent/register` | POST | Register AI agent |
| `/ai/agent/{id}/trust` | GET | Agent trust status |
| `/ai/agent/{id}/rotate-key` | POST | Key rotation |
| `/ai/agent/leaderboard` | GET | Agent reputation ranking |
| `/verify/sdk` | GET | SDK installation info |
| `/verify/self-test` | GET | Live 7-check self-test |

---

## Response Schema (v4.0)

Every tool returns the same envelope, now with JWS, SLA, trust metadata:

```json
{
  "schema_version": "3.0",
  "tool": "peg_deviation",
  "request_id": "fo-abc123",
  "timestamp": "2026-03-06T10:00:00Z",
  "status": "COMPLIANT",
  "reason_codes": ["MICA_COMPLIANT"],
  "mica_articles": ["35"],
  "confidence": 0.9,
  "data": { "..." },
  "evidence": {
    "pack_id": "FO-AIG-ABC123",
    "content_hash": "sha256:4b0552da...",
    "anchor_ref": { "chain": "polygon", "status": "pending" }
  },
  "jws": {
    "jws": "eyJhbGciOiJFUzI1NksiLCJraWQiOiJmby1lY2RzYS12MSJ9...",
    "jws_header": { "alg": "ES256K", "kid": "fo-ecdsa-v1", "typ": "evidence+jwt" },
    "jws_verification": { "jwks_url": "https://feedoracle.io/.well-known/jwks.json" }
  },
  "sla": {
    "confidence": 0.87,
    "freshness_seconds": 0,
    "freshness_met": true,
    "sources": { "available": 2, "total": 3 },
    "staleness_flag": false,
    "tier": "free"
  },
  "trust": {
    "signature_present": true,
    "signature_algorithm": "ES256K",
    "content_hash_present": true,
    "schema_valid": true,
    "registry_logged": true,
    "replayable": true,
    "sla_confidence": 0.87,
    "verify_url": "https://feedoracle.io/verify/self-test",
    "sdk": "pip install feedoracle-verify"
  },
  "schema_ref": "mica/v1",
  "schema_url": "https://feedoracle.io/schemas/v1/mica"
}
```

---

## AI Gateway Example

```json
{
  "tool": "ai_query",
  "input": {
    "query": "Is EURC MiCA-compliant and what is its reserve quality?"
  }
}

// Response: signed evidence bundle with JWS + SLA + trust metadata
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
  },
  "jws": { "alg": "ES256K", "kid": "fo-ecdsa-v1", "..." },
  "sla": { "confidence": 0.87, "freshness_met": true },
  "trust": { "signature_present": true, "registry_logged": true, "replayable": true }
}
```

---

## MiCA Coverage

19 articles covered across 22 regulatory tools (Art. 16/48, 22, 23/52, 24/25, 26/27, 28, 29/30, 35, 36, 37/55, 45/58, 51, 53, 66).

Not covered (process/legal, not data-trackable): Art. 6, 9, 18, 21

---

## Transports

| Transport | URL |
|-----------|-----|
| Streamable HTTP | `https://feedoracle.io/mcp/` |
| SSE (legacy) | `https://feedoracle.io/mcp/sse` |
| Discovery | `https://feedoracle.io/mcp/.well-known/mcp/server.json` |
| Evidence Stream | `https://feedoracle.io/evidence/stream` |

---

## Pricing

Unit-based billing — pay for tool complexity, not raw calls.

| Tier | Price | Included | Overage |
|------|-------|----------|---------|
| **Free** | €0/mo | 300 units/day | Hard limit |
| **Pro** | €49/mo | 15,000 units/mo | €0.005/unit |
| **Agent** | €299/mo | 150,000 units/mo | €0.003/unit |
| **Enterprise** | Custom | Unlimited | Negotiated |

Tool weights: Light (1 unit) · Medium (3 units) · Heavy (10 units). See [docs/BILLING.md](docs/BILLING.md) for full weight table.

Pricing page: [feedoracle.io/pricing.html](https://feedoracle.io/pricing.html)
Weights API: `GET /api/billing/weights`


## Know Your Agent (KYA)

Agent identity and trust scoring for autonomous AI systems. Agents register metadata (name, purpose, org, jurisdiction) and receive a trust score (0-100) that unlocks progressively more tools.

| Trust Level | Score | Access |
|-------------|-------|--------|
| UNVERIFIED | <25 | Light tools only |
| KNOWN | 25-54 | + evidence packs, provenance |
| TRUSTED | 55-79 | + generate_report |
| CERTIFIED | 80+ | + guaranteed SLA |

MCP tools: `kya_register`, `kya_status`. See [docs/KYA.md](docs/KYA.md).

---

## Audit Trail — Decision Logging

Tamper-proof, chain-linked decision log for agent accountability. Every tool call is cached as evidence; agents log decisions referencing prior evidence via `request_id`. Chain integrity is SHA256-verified.

```
Agent calls peg_deviation (fo-abc123)
Agent calls compliance_preflight (fo-def456)
Agent decides: PASS
Agent calls audit_log with evidence_request_ids: [fo-abc123, fo-def456]
→ chain-linked entry with trail_id, evidence_hash, chain_hash
```

MCP tools: `audit_log` (3 units), `audit_query` (1 unit), `audit_verify` (1 unit). See [docs/AUDIT_TRAIL.md](docs/AUDIT_TRAIL.md).

---

## The FeedOracle MCP Ecosystem

| Server | URL | Purpose |
|--------|-----|---------|
| **Compliance Oracle** (this) | `https://feedoracle.io/mcp/` | MiCA/DORA regulatory data + AI Evidence Layer + Enterprise Trust Layer |
| **Macro Oracle** | `https://feedoracle.io/mcp/macro/` | Fed/ECB economic indicators, 86 FRED + 20 ECB series, regime classification |
| **Stablecoin Risk** | `https://feedoracle.io/mcp/risk/` | 7-signal stablecoin operational risk (SAFE/CAUTION/AVOID) |

> "May your agent trade this?" → **Compliance Oracle**
> "Should your agent trade right now?" → **Macro Oracle**
> "Is this stablecoin safe for settlement?" → **Stablecoin Risk**

---

## Verify in 30 Seconds

```bash
# 1. Fetch evidence
curl -s -X POST https://feedoracle.io/ai/query \
  -H "Content-Type: application/json" \
  -d '{"question":"Is USDC MiCA compliant?"}'

# 2. Verify JWS signature via JWKS
curl https://feedoracle.io/.well-known/jwks.json

# 3. Check Evidence Registry
curl https://feedoracle.io/evidence/registry?limit=5

# 4. Replay for audit
curl https://feedoracle.io/evidence/replay/FO-AIG-{pack_id}
# → hash_match: true = deterministic proof

# 5. SDK verification
pip install feedoracle-verify
python -c "from feedoracle_verify import verify_evidence; ..."

# 6. Live Trust Proof Page
open https://feedoracle.io/trust/
```

---

🌐 [feedoracle.io](https://feedoracle.io) · 📖 [Docs](https://feedoracle.io/docs) · 🏥 [Health](https://feedoracle.io/mcp/health) · 🛡️ [Trust](https://feedoracle.io/trust) · 📊 [Uptime](https://uptime.feedoracle.io)

**License:** Proprietary — © 2026 FeedOracle.

---

## Setup

1. Visit the [Anthropic MCP Directory](https://claude.com/connectors)
2. Find **FeedOracle Compliance & Risk Intelligence** and click Connect
3. Complete OAuth authentication (or use free tier without auth)
4. Start querying — no configuration required

**Direct connection (Claude Code):**
```bash
claude mcp add --transport http feedoracle https://mcp.feedoracle.io/mcp
```

**Claude Desktop** (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "feedoracle": {
      "url": "https://mcp.feedoracle.io/mcp"
    }
  }
}
```

---

## Examples

### Example 1: MiCA Compliance Check for a Stablecoin

**User prompt:** "Is USDC compliant under EU MiCA regulation?"

**Expected behavior:**
- Calls `mica_status` with `token_symbol: "USDC"`
- Returns authorization status (COMPLIANT/PENDING/NOT_AUTHORIZED), ESMA/EBA register cross-reference, applicable MiCA articles
- Includes cryptographic evidence pack with JWS signature for audit trail

**Example response summary:**
```
USDC — MiCA Status: COMPLIANT (Art. 48 EMT)
Issuer: Circle Internet Financial
ESMA Register: Verified
Evidence Pack: FO-AIG-XXXX | Signed: ES256K
```

---

### Example 2: Stablecoin Risk Assessment Before Settlement

**User prompt:** "Is USDT safe to use for DeFi settlement right now? Check peg stability and operational risk."

**Expected behavior:**
- Calls `peg_deviation` for real-time peg status
- Calls `risk_assessment` from Stablecoin Risk MCP for 7-signal risk score
- Returns SAFE/CAUTION/AVOID verdict with confidence score, peg deviation %, and risk breakdown

**Example response summary:**
```
USDT Peg: 0.03% deviation — STABLE ✅
Risk Score: 42/100 — CAUTION ⚠️
Signals: Custody concentration HIGH, Redemption 24h OK, Cross-chain NORMAL
Recommendation: Acceptable for settlement under 100k USD
```

---

### Example 3: Macro Regime Check for Trading Agent

**User prompt:** "What is the current macro regime? Should my DeFi agent be risk-on or risk-off?"

**Expected behavior:**
- Calls `macro_regime` from Macro MCP (premium) or `market_stress` + `recession_risk` (free)
- Returns RISK_ON/NEUTRAL/RISK_OFF/STRESS classification with 7 weighted signals
- Includes Fed rate outlook, yield curve status, VIX, credit spreads

**Example response summary:**
```
Macro Regime: RISK_OFF (confidence: 0.78)
Risk Score: 67/100
Signals: Yield curve INVERTED, VIX ELEVATED, Credit spreads WIDE
Fed: HOLD — next FOMC: 2026-03-19
Recommendation: Reduce DeFi exposure, favor stablecoins
```

---

### Example 4: Full DORA Compliance Evidence for a Protocol

**User prompt:** "Generate a DORA compliance evidence report for Aave. I need it for our regulatory audit next week."

**Expected behavior:**
- Calls `evidence_bundle` with framework DORA
- Calls `generate_report` (API key required) to produce signed PDF
- PDF is XRPL-anchored with deterministic replay proof
- Returns download link + Evidence Registry entry

**Example response summary:**
```
DORA Evidence Pack: Aave
Art. 28 (ICT Third Party): 3 custodians identified, concentration risk: LOW
Art. 30 (Contractual arrangements): 2/3 verified
PDF Report: Signed (ES256K), XRPL anchor: rXXX...
Registry Entry: FO-DORA-AAVE-20260313
Replay URL: /evidence/replay/FO-DORA-AAVE-20260313
```

---

## Authentication

This server supports OAuth 2.0 (Authorization Code + PKCE) for user-facing flows and `client_credentials` for autonomous agent-to-agent authentication.

- **Free tier:** No authentication required (20 calls/day anonymous, 100/day with free key)
- **OAuth Discovery:** `https://mcp.feedoracle.io/.well-known/oauth-authorization-server`
- **Scopes:** `mcp:read`, `mcp:compliance:read`, `mcp:risk:read`, `mcp:macro:read`, `mcp:verified-reports:read`

For testing accounts or enterprise evaluation access, contact: [mcp@feedoracle.io](mailto:mcp@feedoracle.io)

---

## Privacy Policy

FeedOracle collects minimal data necessary to operate the service.

**Data collected:**
- OAuth tokens (stored encrypted, auto-expire after 1 hour)
- API usage metrics (call count, tool name, timestamp) — no query content stored
- Evidence packs (compliance evidence only — no personal data)

**Data NOT collected:**
- User query content is not stored or logged
- No personal identifiers beyond email (optional, for paid accounts)
- No data sold or shared with third parties

**Data retention:** Usage metrics retained 90 days. Evidence registry entries retained indefinitely (compliance audit requirement).

**Full Privacy Policy:** [feedoracle.io/privacy](https://feedoracle.io/privacy)

**GDPR:** FeedOracle is operated from Germany. Data processed under GDPR Art. 6(1)(b) — contract performance.

---

## Support

- **Email:** [mcp@feedoracle.io](mailto:mcp@feedoracle.io)
- **Documentation:** [feedoracle.io/docs](https://feedoracle.io/docs)
- **Status / Uptime:** [uptime.feedoracle.io](https://uptime.feedoracle.io)
- **Issues:** [feedoracle.io/support](https://feedoracle.io/support)
