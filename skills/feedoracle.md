# FeedOracle MiCA Compliance Intelligence

## Quick Start
FeedOracle provides 18 tools for MiCA regulatory compliance analysis. All responses are cryptographically signed and audit-ready.

## Key Tools

### Stablecoin Compliance (use token symbol: USDC, EURC, USDT, etc.)
- **mica_status** — Quick MiCA classification (compliant/non-compliant/exempt)
- **peg_deviation** — Art.35 real-time peg monitoring
- **significant_issuer** — Art.45/58 €5B threshold & EBA oversight check
- **interest_check** — Art.23/52 prohibited yield detection
- **document_compliance** — Art.29/30/55 recovery plans & audit freshness
- **reserve_quality** — Art.24/25/53 reserve asset eligibility
- **mica_full_pack** — Complete evidence pack (12 articles, all checks combined)

### RWA & Protocol Risk (use protocol slug: aave-v3, blackrock-buidl, etc.)
- **evidence_profile** — Full risk profile across 9 dimensions
- **custody_risk** — Art.26/27/54 custody & counterparty assessment
- **market_liquidity** — DEX/CEX liquidity depth analysis
- **evidence_leaderboard** — Top protocols ranked by evidence quality

### Macro & Market
- **macro_risk** — 86 FRED indicators for systemic risk context
- **rlusd_integrity** — Ripple RLUSD cross-chain integrity check

### Reports
- **generate_report** — PDF/JSON compliance report with blockchain anchoring

## Usage Tips
- All tools return a unified `evidence_pack` schema with `verdict`, `risk_codes`, and `data`
- Free tier: 100 calls/day, Pro: 5,000/day — no API key needed for free tier
- Append `?signed=true` to REST endpoints for HMAC verification
- For due diligence: start with `mica_full_pack` for comprehensive single-token analysis
- For market overview: use `mica_market_overview` for all 105+ stablecoins at once
