# Audit Trail — Decision Logging for AI Agents

Tamper-proof, chain-linked decision logging that records what an agent decided, based on what evidence, and why.

## Why Audit Trail?

When a regulator asks "Why did your agent approve this swap?" or "What data was available when that decision was made?", you need a verifiable answer. FeedOracle Audit Trail provides it.

Relevant regulation:
- **EU AI Act Art. 14** — Human oversight and explainability
- **MiCA Art. 83** — Competent authorities may request records
- **DORA Art. 11** — ICT-related incident management and traceability

## How It Works

1. **Agent calls FeedOracle tools** (peg_deviation, compliance_preflight, etc.) — each response is automatically cached as evidence with its `request_id`
2. **Agent makes a decision** based on the evidence
3. **Agent calls `audit_log`** with the decision + reasoning + the `request_id`s of the evidence used
4. **FeedOracle creates a chain-linked entry**: SHA256 hash of (previous_chain_hash + trail_id + evidence_hash + decision + timestamp)
5. **Anyone can verify** the chain has not been tampered with using `audit_verify`

## Chain Integrity

Each audit entry is linked to its predecessor via SHA256 chain hashing:

```
genesis → trail-001 (hash₁) → trail-002 (hash₂) → trail-003 (hash₃) → ...
```

If any entry is modified, all subsequent hashes break. `audit_verify` detects this instantly.

## MCP Tools

### `audit_log` — Log a Decision (3 units)

```json
{
  "name": "audit_log",
  "arguments": {
    "decision_type": "compliance_check",
    "decision": "PASS",
    "reasoning": "USDC peg stable at 0.0001% deviation. Compliance preflight passed. Evidence grade A.",
    "action_taken": "Approved USDC for swap pipeline",
    "target_asset": "USDC",
    "jurisdiction": "EU",
    "evidence_request_ids": ["fo-5a0035148dc5", "fo-1ca0828da51d"]
  }
}
```

Response:

```json
{
  "trail_id": "fo-trail-9e4d7ab40cc39405",
  "chain_hash": "sha256:769e1ff424cdb7e0...",
  "prev_trail_id": "genesis",
  "evidence_hash": "sha256:4d23b5f9c190...",
  "evidence_count": 2,
  "evidence_matched": 2,
  "tamper_proof": true,
  "chain_position": 1
}
```

### `audit_query` — Query Trail History (1 unit)

```json
{
  "name": "audit_query",
  "arguments": {
    "client_id": "your-client-id",
    "target_asset": "USDC",
    "limit": 10
  }
}
```

### `audit_verify` — Verify Chain Integrity (1 unit)

```json
{
  "name": "audit_verify",
  "arguments": {
    "client_id": "your-client-id"
  }
}
```

Response:

```json
{
  "valid": true,
  "entries": 2,
  "chain_head": "sha256:4f7e64f2ea5ddb...",
  "broken_at": null
}
```

## REST API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/billing/audit/trail?client_id=...` | GET | Agent's decision trail |
| `/api/billing/audit/verify?client_id=...` | GET | Verify chain integrity |
| `/api/billing/audit/entry?trail_id=...` | GET | Single trail entry with evidence |
| `/api/billing/audit/stats` | GET | Overview statistics |

## Decision Types

| Type | Use Case |
|------|----------|
| `compliance_check` | MiCA/DORA compliance verification |
| `risk_assessment` | Risk scoring and evaluation |
| `trade_signal` | Buy/sell/hold signals |
| `alert` | Threshold breach notifications |
| `recommendation` | Advisory outputs |
| `custom` | Any other decision |

## Example: Full Agent Workflow

```python
# 1. Gather evidence
peg = mcp.call("peg_deviation", {"token_symbol": "USDC"})
preflight = mcp.call("compliance_preflight", {"token_symbol": "USDC"})

# 2. Make decision based on evidence
if peg["status"] == "COMPLIANT" and preflight["decision"] == "PASS":
    decision = "PASS"
    reasoning = f"Peg stable ({peg['evidence']['deviation_pct']}%), preflight passed"
    action = "Approved for swap"
else:
    decision = "BLOCK"
    reasoning = "Failed compliance checks"
    action = "Blocked from pipeline"

# 3. Log decision with evidence chain
trail = mcp.call("audit_log", {
    "decision": decision,
    "reasoning": reasoning,
    "action_taken": action,
    "target_asset": "USDC",
    "evidence_request_ids": [peg["request_id"], preflight["request_id"]]
})

# 4. Verify chain integrity
verify = mcp.call("audit_verify", {"client_id": "my-agent-id"})
assert verify["valid"] == True
```
