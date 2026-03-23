# Example: Responding to reviewers — clinical trial manuscript

**Field:** Clinical Research / Public Health
**Team:** `*team health`
**Pipeline used:** `*pipeline rebuttal`
**Journal:** Cadernos de Saúde Pública

---

## Scenario

Your manuscript on a community hypertension intervention in a Brazilian SUS setting received:
- Decision: **Major revision**
- Reviewer 1: 4 major concerns, 2 minor
- Reviewer 2: 2 major concerns, 3 minor
- Editor: 1 request (CONSORT checklist)

---

## Step-by-step session

### 1. Load context

```
*team health
*pipeline rebuttal
```

### 2. Paste reviewer comments

Paste the full reviewer text. Peer Reviewer + Scientific Writer classify each comment:

```
COMMENT CLASSIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

R1.1 — MAJOR — Valid
  "The sample size justification is insufficient. The authors report n=87
  but do not provide a power calculation."
  → Response strategy: full G*Power calculation + add to Methods

R1.2 — MAJOR — Valid
  "Loss to follow-up is 23%, above the 20% threshold. Authors must
  perform sensitivity analysis."
  → Response strategy: add per-protocol + ITT analysis comparison

R1.3 — MAJOR — Partially valid (misunderstanding)
  "The control group received 'usual care' which is not defined."
  → Response strategy: clarify definition already in §2.3, add explicit sentence

R1.4 — MAJOR — Unjustified
  "The authors should have used a factorial design."
  → Response strategy: politely decline — factorial design was not feasible
    in SUS context; cite CONSORT for pragmatic trials

R2.1 — MAJOR — Valid
  "No CONSORT flow diagram provided."
  → Response strategy: add Figure 1 (CONSORT flow)

R2.2 — MAJOR — Valid
  "Primary outcome not pre-registered."
  → Response strategy: register now in ReBEC + declare in response

Editor — MAJOR
  "Please provide completed CONSORT 2010 checklist."
  → Response strategy: complete and attach as supplementary
```

### 3. Generate rebuttal

```
*rebuttal
```

Scientific Writer drafts full letter. Example for R1.4 (unjustified request):

```
Comment R1.4:
"The authors should have used a factorial design to test the independent
and combined effects of the interventions."

Response:
We thank the reviewer for this suggestion. However, we respectfully maintain
our single-arm pragmatic design for the following reasons:

(1) Factorial designs require substantially larger sample sizes (typically 4×
for a 2×2 factorial), which was infeasible in the SUS community health setting
where recruitment was constrained to 87 participants over 18 months.

(2) Our objective was to evaluate the feasibility and effect size of the
combined intervention package as delivered in routine practice — a question
better suited to a pragmatic trial (Loudon et al., 2015 [REF NEEDED: PRECIS-2
paper, Trials journal]).

(3) CONSORT extensions for pragmatic trials (Zwarenstein et al., 2008) support
single-arm designs when the research question concerns real-world effectiveness.

Manuscript change: Added clarification in §2.1 (Study Design): "A pragmatic
single-arm design was chosen over factorial design because [reason above,
condensed to 2 sentences]."
```

### 4. Summary table

NEXUS generates:

```
SUMMARY OF CHANGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Comment  | Change                        | Location
---------|-------------------------------|------------------
R1.1     | G*Power calculation added     | Methods §2.4
R1.2     | Sensitivity analysis added    | Results §3.3 + Table 4
R1.3     | Control group definition      | Methods §2.3 (clarified)
R1.4     | No change (justified decline) | Response letter only
R2.1     | CONSORT flow diagram added    | Figure 1
R2.2     | ReBEC registration added      | Abstract + Methods §2.1
Editor   | CONSORT checklist attached    | Supplementary File S1
```

---

## Key outputs

- Complete rebuttal letter (ready to paste into journal system)
- Summary of changes table
- Notes on which changes require new analysis (R1.2 sensitivity analysis)
- RESEARCHER DECISIONS: ReBEC registration number (must obtain before submission)

---

## Lessons from this example

1. **Never paraphrase reviewer comments** — always quote exactly (credibility + clarity)
2. **"No change" is a valid response** — but requires explicit, referenced justification
3. **CONSORT/STROBE is non-negotiable** for health journals — `*team health` flags this automatically
4. **Pre-registration retroactively** (ReBEC, ClinicalTrials.gov) is acceptable if declared transparently
