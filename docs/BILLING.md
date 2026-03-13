# Unit-Based Billing

FeedOracle uses unit-based billing. Every MCP tool call consumes units based on computational complexity.

## Tool Weights

| Weight | Units | Tools |
|--------|-------|-------|
| Light | 1 | `peg_deviation`, `mica_status`, `macro_risk`, `inflation_monitor`, `recession_risk`, `economic_health`, `consumer_sentiment`, `reserve_quality`, `document_compliance`, `significant_issuer`, `interest_check` |
| Medium | 3 | `compliance_preflight`, `peg_history`, `ai_query`, `custody_risk`, `market_liquidity`, `evidence_profile`, `evidence_leaderboard`, `fed_watch`, `labor_market`, `yield_curve`, `rlusd_integrity` |
| Heavy | 10 | `evidence_bundle`, `generate_report`, `mica_full_pack`, `mica_market_overview`, `ai_provenance`, `ai_explain`, `macro_regime`, `market_stress`, `safe_haven_flows`, `defi_rates`, `gdp_tracker` |
| Free | 0 | `ping`, `kya_register`, `kya_status` |

## Tiers

| Tier | Price | Included Units | Overage |
|------|-------|---------------|---------|
| Free | €0/mo | 300/day (≈9,000/mo) | Hard limit |
| Anonymous | €0 | 60/day (≈1,800/mo) | Hard limit |
| Pro | €49/mo | 15,000/mo | €0.005/unit |
| Agent | €299/mo | 150,000/mo | €0.003/unit |
| Enterprise | Custom | Unlimited | Negotiated |

## How Overage Works

Pro and Agent tiers include a monthly unit allowance. When exceeded, additional usage is automatically metered via Stripe Billing Meter and appears on the next invoice.

Free and Anonymous tiers have hard limits — tool calls are rejected with `DAILY_UNIT_LIMIT_EXCEEDED` when the quota is reached.

## Response Meta

Every tool response includes unit information:

```json
{
  "meta": {
    "cost_class": "LIGHT",
    "units_consumed": 1,
    "trust_level": "free"
  }
}
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/billing/weights` | GET | All tool weights and tier limits |
| `/api/billing/usage?key=...` | GET | Current usage with unit breakdown |
| `/api/billing/register` | POST | Register for free API key |
| `/api/billing/checkout` | POST | Start Stripe checkout for Pro/Agent |
| `/api/billing/claim?session_id=...` | GET | Claim API key after payment |

## Example: Check Weights

```bash
curl -s https://feedoracle.io/api/billing/weights | jq
```

## Example: Usage Cost Estimation

An agent running daily:
- 20× `peg_deviation` = 20 units
- 5× `compliance_preflight` = 15 units
- 1× `mica_full_pack` = 10 units

Total: 45 units/day ≈ 1,350/month → Free tier sufficient.
