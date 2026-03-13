# Reference Workflows

Eight canonical workflows showing how FeedOracle evidence is used in real compliance processes.

---

## 1. Stablecoin Pre-Trade Check

**Persona:** Trading agent before executing a swap
**Tools:** `peg_deviation` → `compliance_preflight` → `audit_log`

```
1. peg_deviation(USDC)       → Is the peg stable right now?
2. compliance_preflight(USDC) → PASS/WARN/BLOCK for this jurisdiction?
3. audit_log(decision, reasoning, [rid1, rid2]) → Log why you traded or didn't
```

**Decision logic:** If peg STABLE + preflight PASS → execute swap. Otherwise hold.

---

## 2. MiCA Status Verification Before Listing

**Persona:** Exchange compliance team evaluating a new listing
**Tools:** `mica_status` → `significant_issuer` → `document_compliance` → `reserve_quality` → `mica_full_pack`

```
1. mica_status(TOKEN)         → Is this token MiCA-authorized?
2. significant_issuer(TOKEN)  → Does the issuer exceed €5B threshold?
3. document_compliance(TOKEN) → Are recovery/redemption plans current?
4. reserve_quality(TOKEN)     → Art.53 eligible reserves?
5. mica_full_pack(TOKEN)      → Full 12-article evidence pack for the record
```

**Output:** A complete MiCA due diligence record. Store the `mica_full_pack` request_id for audit trail.

---

## 3. Issuer Due Diligence Snapshot

**Persona:** Risk team building an issuer profile
**Tools:** `evidence_bundle` → `ai_explain` → `ai_provenance`

```
1. evidence_bundle(TOKEN, ["mica","dora","rwa"]) → Multi-framework evidence
2. ai_explain(TOKEN)       → Why does this token have this grade?
3. ai_provenance(TOKEN)    → Where does every data point come from?
```

**Output:** A complete evidence dossier with grade explanation and full provenance chain. The `ai_explain` summary field is human-readable for non-technical stakeholders.

---

## 4. Audit Replay of Prior Compliance Signal

**Persona:** Internal audit verifying a past agent decision
**Tools:** `audit_query` → `audit_verify`

```
1. audit_query(client_id, target_asset="USDC") → Get all decisions for USDC
2. audit_verify(client_id) → Is the chain intact? Any tampering?
3. For each trail entry: check evidence_snapshot for what was known at decision time
```

**Output:** A verified, tamper-proof record of what the agent decided, when, based on what evidence, and why.

---

## 5. Register Status Verification for Onboarding

**Persona:** Compliance officer onboarding a new stablecoin
**Tools:** `mica_status` → `interest_check` → `custody_risk`

```
1. mica_status(TOKEN)     → Authorization status
2. interest_check(TOKEN)  → Any prohibited yield mechanisms?
3. custody_risk(TOKEN)    → Who holds the reserves? SIFI status?
```

**Decision gate:** All three must pass before onboarding proceeds. Log via `audit_log`.

---

## 6. Evidence Pack for Internal Risk Committee

**Persona:** Risk analyst preparing materials for committee review
**Tools:** `mica_full_pack` → `generate_report`

```
1. mica_full_pack(TOKEN)           → Machine-readable evidence
2. generate_report(type="mica")    → Signed PDF for the committee
```

**Output:** A PDF report anchored to XRPL with all 12 MiCA articles covered. The `summary` field in each tool response provides human-readable context.

---

## 7. Agent Compliance Preflight Before Autonomous Action

**Persona:** Autonomous DeFi agent managing a portfolio
**Tools:** `kya_register` → `compliance_preflight` → `macro_risk` → `audit_log`

```
1. kya_register(agent metadata)    → Establish agent identity + trust level
2. compliance_preflight(TOKEN)     → Is this trade compliant?
3. macro_risk()                    → Any macro headwinds?
4. audit_log(decision, reasoning, [rid1, rid2, rid3]) → Permanent record
```

**Decision logic:** If preflight PASS + macro_risk not RECESSION → proceed. Otherwise defer to human operator.

---


---

## 8. Failure Path — Source Degradation, Dispute, Correction, and Replay

**Persona:** Compliance officer investigating a flagged incident
**Scenario:** An agent made a PASS decision based on evidence that was later found to be sourced from a stale register. The agent traded, and a third party disputes the evidence.

### Step-by-step:

```
Day 1, 09:00 — Agent workflow executes normally:
  1. peg_deviation(TOKEN-X)        -> STABLE (rid: fo-aaa)
  2. compliance_preflight(TOKEN-X)  -> PASS   (rid: fo-bbb)
  3. audit_log(PASS, "peg stable, preflight passed", [fo-aaa, fo-bbb])
     -> trail_id: fo-trail-001, chain_hash: sha256:abc...
  4. Agent executes swap

Day 1, 14:00 — Source degradation detected:
  - ESMA register returns stale data (last updated 48h ago)
  - FeedOracle marks fo-bbb as STALE (staleness_flag: true)
  - Next compliance_preflight call returns reduced confidence (0.6 -> 0.4)
  - Agent receives WARN instead of PASS, defers to human

Day 2 — Third party files dispute:
  1. audit_log(decision_type="dispute", reasoning="ESMA data was 48h stale
     at time of fo-bbb", evidence_request_ids=[fo-bbb])
  2. FeedOracle sets fo-bbb to DISPUTED state
  3. Dispute-SLA clock starts: acknowledge within 4h, classify within 24h

Day 3 — Investigation and correction:
  1. FeedOracle confirms: ESMA register was indeed stale at 09:00 on Day 1
  2. A corrected artifact is created with current register data (rid: fo-ccc)
  3. fo-bbb state transitions: DISPUTED -> CORRECTED (corrected_by: fo-ccc)
  4. Resolution logged in audit trail

Day 5 — Audit replay:
  1. audit_query(client_id, target_asset="TOKEN-X")
     -> Returns trail-001 with original evidence snapshots
  2. Evidence artifact fo-bbb shows:
     - state: CORRECTED
     - corrected_by: fo-ccc
     - state_history: CURRENT -> STALE -> DISPUTED -> CORRECTED
  3. audit_verify(client_id) -> Chain valid (no tampering)
  4. Auditor can see: what was known at decision time, what changed,
     and that the correction was properly logged
```

### What this demonstrates:
- **No silent failures**: Staleness was flagged immediately in response metadata
- **Dispute process works**: Third party filed dispute, artifact state changed, SLA clock started
- **Correction creates new artifact**: Old artifact preserved with full history, linked to replacement
- **Audit replay shows full timeline**: Every state transition visible with timestamps and reasons
- **Chain integrity maintained**: Despite corrections, the audit chain remains valid and verifiable
- **Human-readable trail**: Every step produces a `summary` field a compliance officer can read

---

## Workflow Principles

1. **Every workflow ends with `audit_log`** — no decision without a record
2. **Evidence request_ids chain forward** — each step references the previous
3. **Human-readable summaries** — the `summary` field in every response can be shown to non-technical stakeholders
4. **Temporal reproducibility** — replay any workflow at any past point in time via evidence lifecycle
5. **Independent verification** — any step can be verified via JWKS without trusting FeedOracle
6. **Failure is visible** — any step can be verified via JWKS without trusting FeedOracle
