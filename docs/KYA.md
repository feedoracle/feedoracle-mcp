# Know Your Agent (KYA)

Agent identity, trust scoring, and access control for autonomous AI agents.

## Why KYA?

As AI agents make autonomous financial decisions, regulators need to know: Who is this agent? What is its purpose? Who is accountable? KYA answers these questions with a verifiable trust framework.

Relevant regulation:
- **EU AI Act Art. 14** — Human oversight of high-risk AI systems
- **DORA Art. 11** — ICT-related incident management
- **MiCA Art. 83** — Competent authority record requests

## Trust Levels

| Level | Name | Score | Access |
|-------|------|-------|--------|
| 0 | UNVERIFIED | <25 | Light tools only |
| 1 | KNOWN | 25-54 | All tools except `generate_report` |
| 2 | TRUSTED | 55-79 | All tools including reports |
| 3 | CERTIFIED | 80+ | All tools + guaranteed SLA (requires manual verification) |

## Trust Score (0-100)

Computed from 6 dimensions:

| Dimension | Max Points | How to Earn |
|-----------|-----------|-------------|
| Registration completeness | 20 | Fill all profile fields |
| Account age | 15 | 30+ days = full score |
| Usage consistency | 15 | Regular daily usage |
| Compliance rate | 20 | No rate limit violations |
| Behavioral signals | 15 | Purpose declared, compliance contact, responsible risk appetite, website |
| Manual boost | 15 | Admin verification |

## Trust-Gated Tools

| Tool | Minimum Trust Level |
|------|-------------------|
| `mica_full_pack` | KNOWN (1) |
| `ai_provenance` | KNOWN (1) |
| `ai_explain` | KNOWN (1) |
| `evidence_bundle` | KNOWN (1) |
| `mica_market_overview` | KNOWN (1) |
| `generate_report` | TRUSTED (2) |

## MCP Tools

### `kya_register`

Register your agent identity. Returns trust score and level.

```json
{
  "name": "kya_register",
  "arguments": {
    "agent_name": "MiCA Compliance Bot",
    "agent_purpose": "Automated MiCA compliance monitoring",
    "owner_org": "DeFi Risk GmbH",
    "owner_email": "compliance@defirisk.de",
    "owner_jurisdiction": "DE",
    "compliance_contact": "cto@defirisk.de",
    "website_url": "https://defirisk.de",
    "risk_appetite": "conservative"
  }
}
```

Response includes trust score, level, and a breakdown of which gated tools are now accessible.

### `kya_status`

Check your current trust level and tool access.

```json
{
  "name": "kya_status",
  "arguments": {
    "client_id": "your-oauth-client-id"
  }
}
```

## REST API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/billing/kya/register` | POST | Register agent profile |
| `/api/billing/kya/profile?client_id=...` | GET | Get full profile + trust score |
| `/api/billing/kya/check?client_id=...&tool=...` | GET | Check tool access |
| `/api/billing/kya/summary` | GET | Overview stats |
| `/api/billing/kya/agents` | GET | List all registered agents |

## Example: Full Registration Flow

```bash
# 1. Register OAuth client
curl -s -X POST https://feedoracle.io/mcp/register \
  -H "Content-Type: application/json" \
  -d '{"client_name":"my-agent","grant_types":["client_credentials"]}'

# 2. Register KYA profile
curl -s -X POST https://feedoracle.io/api/billing/kya/register \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": "your-client-id",
    "agent_name": "My Compliance Agent",
    "agent_purpose": "Portfolio MiCA monitoring",
    "owner_org": "Acme GmbH",
    "owner_email": "agent@acme.de",
    "owner_jurisdiction": "DE",
    "compliance_contact": "compliance@acme.de"
  }'

# 3. Check trust level
curl -s "https://feedoracle.io/api/billing/kya/profile?client_id=your-client-id"
```
