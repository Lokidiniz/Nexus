# Task: design-study
## Agent: Methodologist | Command: `*design [question]`

### Purpose
Design a complete research study from a research question, including methodology, sampling strategy, data collection instruments, and analysis plan.

---

## RDS Check

Before designing, methodologist runs:

```
RDS CHECK — *design
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Question type: [causal / descriptive / explanatory / exploratory]
Population: [target population]

Candidate designs:
  [1] [Design name] — Match: [%] → [REUSE / ADAPT / REJECT + reason]
  [2] [Design name] — Match: [%] → [REUSE / ADAPT / REJECT + reason]

Recommended: [design] — Tier [1/2/3]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Execution Steps

### Mode: interactive

1. **Receive** research question
2. **Classify** question type (causal / descriptive / explanatory / exploratory)
3. **Apply RDS** — evaluate candidate designs, select tier
4. **Present design options** — wait for researcher confirmation before proceeding
5. **Deliver** selected design specification
6. **Present instrument draft** — wait for feedback
7. **Finalize** complete study protocol

### Mode: yolo

1. Classify question, apply RDS, select best design
2. Deliver complete study specification with all components
3. Log all design decisions at end

### Mode: pre-flight

1. Present full design plan with options and trade-offs
2. Await `ok / adjust / cancel`
3. Execute confirmed plan

---

## Output Format

```
📐 STUDY DESIGN — [Research Question]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RDS: [REUSE / ADAPT / CREATE] — [design name]

DESIGN SPECIFICATION
━━━━━━━━━━━━━━━━━━━━
Design:          [name and type]
Approach:        [quantitative / qualitative / mixed]
Paradigm:        [positivist / interpretivist / pragmatist]
Objective:       [what the study will determine]

POPULATION & SAMPLE
━━━━━━━━━━━━━━━━━━━
Target population:   [description]
Sampling strategy:   [probabilistic / purposive / convenience / snowball]
Inclusion criteria:  [list]
Exclusion criteria:  [list]
Sample size:         [n = X — method: G*Power / Cohen / saturation]
Justification:       [why this sample is sufficient]

DATA COLLECTION
━━━━━━━━━━━━━━━
Instrument:       [questionnaire / interview guide / observation protocol / lab protocol]
Variables:        [dependent: | independent: | confounders:]
Procedures:       [step-by-step collection protocol]
Timepoints:       [cross-sectional / longitudinal — T1, T2, ...]
Ethical notes:    [CONEP / IRB requirements, consent, anonymization]

ANALYSIS PLAN
━━━━━━━━━━━━━
Quantitative:   [tests planned — justify based on distribution + sample]
Qualitative:    [approach — thematic / content / discourse / phenomenological]
Software:       [R / SPSS / Python / NVivo / ATLAS.ti]

VALIDITY THREATS & MITIGATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Internal validity:   [threat → mitigation]
External validity:   [threat → mitigation]
Construct validity:  [threat → mitigation]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESEARCHER DECISIONS NEEDED
• [Decisions only the researcher can make]
```

---

## Design Quick-Reference

| Question Type | Recommended Design | Notes |
|---|---|---|
| X causes Y? | RCT (gold standard) | If randomization feasible |
| X causes Y, no randomization | Quasi-experimental | Use propensity score / DiD |
| How common is X? | Cross-sectional survey | Power calculation required |
| How does X unfold over time? | Longitudinal cohort | Costly; define follow-up |
| What is X like? | Qualitative (phenomenological / grounded theory) | Purposive sample, saturation |
| How do people understand X? | Interpretive / ethnographic | Fieldwork required |
| Does intervention X work here? | Action research | Participatory, iterative |
| Combination of above | Mixed methods | Justify integration point |

---

## Ethical Checklist

- [ ] Informed consent procedure defined
- [ ] Data anonymization/pseudonymization planned
- [ ] Vulnerable populations: additional protections specified
- [ ] Brazilian studies: CONEP/CEP platform required?
- [ ] International: IRB registration required?
- [ ] Data storage and retention plan defined
- [ ] Conflict of interest declared
