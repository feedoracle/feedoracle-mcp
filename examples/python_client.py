"""
FeedOracle MCP Python Client — v2.3.1
Examples for all 18 tools via direct HTTP (Streamable HTTP transport).
"""
import httpx, json, asyncio

MCP_URL = "https://feedoracle.io/mcp/"
API_KEY  = "your_api_key_here"  # optional for LIGHT/MEDIUM tools

async def call_tool(tool_name: str, arguments: dict = None, api_key: str = None) -> dict:
    """Call any FeedOracle MCP tool."""
    args = arguments or {}
    if api_key:
        args["api_key"] = api_key
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": args}
    }
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(MCP_URL, json=payload, headers={"Content-Type": "application/json"})
        data = r.json()
        content = data.get("result", {}).get("content", [{}])
        return json.loads(content[0].get("text", "{}"))


async def main():

    # ── LIGHT Tools (no key) ──────────────────────────────────────────

    # 1. MiCA Authorization Status
    r = await call_tool("mica_status", {"token_symbol": "EURC"})
    print(f"EURC MiCA status: {r.get('status')} — {r.get('reason_codes')}")

    # 2. Real-time peg deviation (Art. 35)
    r = await call_tool("peg_deviation", {"token_symbol": "EURC"})
    ev = r.get("evidence", {})
    print(f"EURC peg: {ev.get('deviation_pct', '?')}% — {r.get('status')}")

    # 3. Significant issuer check (Art. 45/58)
    r = await call_tool("significant_issuer", {"token_symbol": "USDT"})
    print(f"USDT significant: {r.get('status')} — EBA: {r.get('evidence',{}).get('eba_oversight')}")

    # 4. Document compliance (Art. 29/30/55)
    r = await call_tool("document_compliance", {"token_symbol": "EURC"})
    print(f"EURC docs compliance: {r.get('status')} — score: {r.get('evidence',{}).get('compliance_score')}")

    # 5. Reserve quality (Art. 24/25/53)
    r = await call_tool("reserve_quality", {"token_symbol": "EURCV"})
    print(f"EURCV reserves: {r.get('status')} — Art.53 eligible: {r.get('evidence',{}).get('art53',{}).get('eligible_pct')}%")

    # 6. Transaction preflight (PASS/WARN/BLOCK)
    r = await call_tool("compliance_preflight", {"token_symbol": "USDC", "action": "swap", "jurisdiction": "EU"})
    print(f"USDC swap preflight: {r.get('decision')} — {r.get('reason_codes')}")

    # ── MEDIUM Tools (no key) ─────────────────────────────────────────

    # 7. 30-day peg history
    r = await call_tool("peg_history", {"token_symbol": "EURC"})
    ev = r.get("evidence", {})
    print(f"EURC peg history: stability_score={ev.get('summary',{}).get('stability_score')} depeg_events={ev.get('summary',{}).get('depeg_events')}")

    # 8. Interest prohibition scan (Art. 23/52)
    r = await call_tool("interest_check", {"token_symbol": "EURC"})
    print(f"EURC interest check: {r.get('status')} — risk: {r.get('evidence',{}).get('risk_level')}")

    # 9. Evidence leaderboard
    r = await call_tool("evidence_leaderboard", {"top_n": 5})
    lb = r.get("evidence", {}).get("leaderboard", [])
    print(f"Top 5 RWA: {[p.get('name') for p in lb]}")

    # ── HEAVY Tools (API key required) ───────────────────────────────

    # 10. Full MiCA evidence pack (12 articles in one call)
    r = await call_tool("mica_full_pack", {"token_symbol": "EURC"}, api_key=API_KEY)
    print(f"EURC full MiCA: compliant={r.get('overall_mica_compliant')} articles={r.get('articles_covered')} flags={r.get('compliance_flags')}")

    # 11. Market overview
    r = await call_tool("mica_market_overview", {}, api_key=API_KEY)
    ev = r.get("evidence", {})
    print(f"Market: significant={ev.get('significant_alerts',{}).get('significant')} peg_alerts={ev.get('peg_alerts',{}).get('alert_count')}")

    # 12. Generate compliance report
    r = await call_tool("generate_report", {"report_type": "mica"}, api_key=API_KEY)
    print(f"Report: {r.get('evidence',{}).get('report_id')} — {r.get('evidence',{}).get('download_url')}")


if __name__ == "__main__":
    asyncio.run(main())
