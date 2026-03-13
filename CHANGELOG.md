# Changelog

## v4.0 — 2026-03-13

### Unit-Based Billing
- Stripe Billing Meter for automated overage charging (Pro/Agent tiers)
- 39 tools classified by weight: Light (1 unit), Medium (3 units), Heavy (10 units)
- Free tier: 300 units/day hard limit
- Pro tier: 15,000 units/month included, €0.005/unit overage
- Agent tier: 150,000 units/month included, €0.003/unit overage
- `meta.units_consumed` in every tool response
- `/api/billing/weights` public endpoint
- Pricing page updated to unit-based model

### Know Your Agent (KYA)
- Agent identity registration with trust scoring (0-100, 6 dimensions)
- 4 trust levels: UNVERIFIED, KNOWN, TRUSTED, CERTIFIED
- Trust-gated access to 6 sensitive tools
- New MCP tools: `kya_register`, `kya_status`
- 5 REST endpoints: register, profile, check, summary, agents
- KYA profiles linked to OAuth client identities

### Audit Trail
- Tamper-proof, SHA256 chain-linked decision logging
- Automatic evidence capture from all tool responses
- Decision entries reference prior tool calls via `request_id`
- Chain integrity verification (detects any tampering)
- New MCP tools: `audit_log`, `audit_query`, `audit_verify`
- 4 REST endpoints: trail, verify, entry, stats
- Evidence snapshots preserved for regulatory replay

### Infrastructure
- New DB tables: `kya_profiles`, `kya_events`, `audit_decisions`, `audit_evidence_cache`, `stripe_customers`
- `usage_log` table extended with `units` column (backfilled)
- New modules: `kya.py`, `audit_trail.py`
- Stripe objects: 1 Billing Meter, 2 Metered Prices
- Total MCP tools: 27 (was 22)
- Anthropic MCP Directory submission (Anthropic crawling confirmed)

---

## v3.1 — 2026-03-08

### Enterprise Trust Layer
- JWS signing (ES256K, RFC 7515)
- Versioned schemas (v2.3)
- Evidence registry
- SLA layer with freshness targets
- Agent trust management
- Streaming evidence (SSE)
- Deterministic replay
- Zero-trust validation SDK

### OAuth 2.0
- Dynamic Client Registration (RFC 7591)
- PKCE (RFC 7636)
- Token refresh/rotation
- Token revocation (RFC 7009)
- Client credentials grant for M2M agents
- Claude Marketplace compatibility

---

## v2.3.1 — 2026-02-21

- 22 MCP tools
- AI Evidence Layer (ai_query, evidence_bundle, ai_explain, ai_provenance)
- Unified response schema v2.3
- MiCA article mapping for all tools
