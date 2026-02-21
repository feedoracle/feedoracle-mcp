# FeedOracle MCP — Sample Prompts

Copy-paste into Claude, Cursor, or any MCP-connected AI.

---

## 🔍 Quick Checks (LIGHT — no key needed)

**MiCA Status**
> Is EURC authorized under MiCA? What's the authorization status and which NCA?

> Check if USDT is MiCA compliant for EU trading.

**Peg Stability (Art. 35)**
> What's the current peg deviation for EURC? Is it within MiCA Art. 35 limits?

> Check peg stability for EURe, AEUR and EURI — compare all three.

**Significant Issuer (Art. 45/58)**
> Is USDC a significant issuer under MiCA Art. 45? What additional obligations apply?

> Which stablecoins are approaching the €5B significant issuer threshold? Show projections.

**Document Compliance (Art. 29/30/55)**
> Does USDT have a current recovery plan and audit? Check Art. 29/30/55 compliance.

> Check audit freshness for BUIDL — is the last audit within 365 days?

**Reserve Quality (Art. 24/25/53)**
> What percentage of EURC reserves are Art. 53 eligible?

> Check reserve quality for EURCV — any violations?

---

## 🟡 Analysis (MEDIUM — no key needed)

**Peg History**
> Show me the 30-day peg stability history for USDT. How many depeg events?

> Compare peg stability scores: EURC vs EURe vs EURCV over the last 30 days.

**Interest Prohibition (Art. 23/52)**
> Scan USD0++ for Art. 23/52 interest prohibition risk. Is there issuer-native yield?

> Which stablecoins in FeedOracle's coverage have interest prohibition warnings?

**Evidence Profile**
> Show me the evidence profile for ONDO. Grade and main risk factors?

> Compare USDC vs USDT on evidence quality — custody, governance, reserves.

**Leaderboard**
> Show the top 15 RWA protocols by evidence grade. Any surprises?

**Macro**
> What does the current macro environment look like? Recession probability and Fed signals?

---

## 🔴 Full Analysis (HEAVY — API key required)

**Full MiCA Pack**
> Run a complete MiCA compliance check for RLUSD. All 12 articles.

> Get the full MiCA evidence pack for EURC. Is it overall MiCA compliant?

**Market Overview**
> Give me a full MiCA market overview — who's significant, any peg alerts, interest violations?

**Reports**
> Generate a signed MiCA compliance report. I need it for a regulatory audit.

> Create a DORA risk report for our service provider assessment.

---

## 🏢 Enterprise Use Cases

**Due Diligence**
> We're onboarding EURCV as a settlement asset. Run full MiCA due diligence — all articles, reserve quality, custody, audit status, and peg history.

**Regulatory Monitoring**
> Set up a daily check: are any of our stablecoin positions (USDC, EURC, RLUSD) showing MiCA compliance changes or peg warnings?

**Comparison**
> Compare EURC, EURCV, EURe, AEUR and EURI on: MiCA authorization, reserve quality, audit freshness, and peg stability. Give me a structured comparison.

**Red Flags**
> Which stablecoins in the FeedOracle registry have compliance flags right now? Show violations and warnings across all MiCA articles.
