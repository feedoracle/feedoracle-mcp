# Reference Workflows

Seven canonical workflows showing how FeedOracle evidence is used in real compliance processes.

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

## Workflow Principles

1. **Every workflow ends with `audit_log`** — no decision without a record
2. **Evidence request_ids chain forward** — each step references the previous
3. **Human-readable summaries** — the `summary` field in every response can be shown to non-technical stakeholders
4. **Temporal reproducibility** — replay any workflow at any past point in time via evidence lifecycle
5. **Independent verification** — any step can be verified via JWKS without trusting FeedOracle
