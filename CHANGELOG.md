# Changelog

## v6.0.0 — OracleNet Execute Pipeline (2026-04-07)

### Execute Pipeline
- `quantum_ask`: Natural language → intent → route → execute → deliver → learn
- `quantum_execute`: Direct tool execution with neural learning
- MCP session handshake + SSE parsing for all oracle types
- Auto-settlement with SHA-256 content hash

### Scale
- 90 MCP oracles (was 11), 1,014 capabilities (was 50)
- 7 categories: Compliance, Trust, Finance, Business, Travel, Blockchain, Payment
- 13 blockchain chains: BTC, ETH, XRPL, SOL, ARB, TON, SUI, Hedera, Base, BNB, XLM, Aptos, Flare
- Enterprise suite: CFO, HR, Health, SupplyChain, CyberShield, LegalTech, Tax, CBDC, PSD2

### Neural Layer
- Synapse logging on every execution
- Auto-reward based on success + response time
- Routing weights used for oracle selection
- 96 synapses, 69 weights across 38 oracles

### On-Chain
- 104 escrow deals on Base Mainnet (103 settled)
- First autonomous deal through execute pipeline (Deal #103)
- Contract: 0x330F99f34246EA375333b9C01Ed6BB49190B051F

### Hardening
- Idempotency (request-hash dedup, 5 min TTL)
- Circuit breaker (3 failures → open → 120s cooldown)
- Rate limiting (30/min per caller)
- Replay protection (5 min timestamp window)
- Malformed response guard (1MB, type validation)
- Webhook limits (50 global, 5 per DID)
- Escrow settlement: service-key + 1 USDC cap

### Observability
- Soak test: 12 queries, 6 categories, every 5 min (12/12 pass, 88ms avg)
- Cockpit: oracle health, neural weights, security, soak trends
- All OracleNet DBs in daily backup

### Fixes
- Immune System IntegrityError fixed
- Self-Evolution Telegram approval (/proposals, /approve, /reject)
- AgentGuard false positives rehabilitated
- Catalog categories populated
- Nginx security headers (HSTS, X-Frame, XSS)

## v5.1.0 — DetectiveOracle + SupportOracle (2026-04-03)
- 50 tools on main server
- DetectiveOracle (fraud detection)
- SupportOracle (diagnostics, onboarding)
- Trust Passport (signed agent document)
- Governance tools

## v5.0.0 — DORA OS Positioning (2026-04-02)
- 11 MCP servers, 203 tools total
- DORA Operating System framing
- Updated pricing tiers

## v4.0.0 — Billing + KYA + Audit Trail (2026-03-13)
- Unit-based billing (Stripe Billing Meter)
- Know Your Agent (KYA) registration
- Tamper-proof audit trail (SHA-256 chain)
- Evidence Trust Policy v1.0
- 27 MCP tools

## v3.1 — Enterprise Trust Layer (2026-03-08)
- JWS signing (ES256K)
- Versioned schemas
- Evidence registry
- SLA layer
