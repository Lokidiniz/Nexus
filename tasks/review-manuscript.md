# Task: review-manuscript
## Agent: Peer Reviewer | Command: `*review [--journal name]`

### Purpose
Simulate expert peer review for any journal or field. Returns structured reviewer report with scores, major/minor revisions, and strengthening strategy.

---

## RDS Check

```
RDS CHECK — *review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Journal profile: [load if known, else use field-generic criteria]
Review type:     [standard single-blind / double-blind / open]
Match:           [≥90% REUSE standard template | <90% ADAPT for journal]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Execution Steps

### Mode: interactive

1. Receive manuscript + journal target (if provided)
2. Load journal profile from `.nexus/` or use field-generic criteria
3. First pass: read abstract + conclusions → initial novelty assessment
4. **Checkpoint**: share initial novelty score, await confirmation to proceed
5. Full review: all sections
6. Deliver structured report
7. **Checkpoint**: ask if researcher wants strengthening strategy

### Mode: yolo

1. Load journal profile, run full review
2. Deliver complete report + strengthening strategy in one output

### Mode: pre-flight

1. Present review plan (criteria to evaluate, journal profile loaded)
2. Await `ok / adjust / cancel`
3. Execute full review

---

## Output Format

```
🎯 PEER REVIEW REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Journal target: [name or "field-generic"]
Review profile: [simulated reviewer expertise]

DECISION RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━
[ ] Accept as is
[ ] Minor revision
[x] Major revision      ← mark with x
[ ] Reject

Overall score: [1–10] / 10

SECTION SCORES
━━━━━━━━━━━━━━
Title/Abstract:   [score] — [1-line comment]
Introduction:     [score] — [gap statement quality, funnel structure]
Methods:          [score] — [reproducibility, controls, statistics]
Results:          [score] — [data presentation, figure quality]
Discussion:       [score] — [contextualization, limitations, overreach]
Conclusion:       [score] — [supported by evidence, future directions]
References:       [score] — [currency, completeness, self-citation ratio]

MAJOR CONCERNS (must address)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
M1. [Concern] — [Section] — [Why this blocks acceptance]
M2. [Concern] — [Section] — [Why this blocks acceptance]
M3. [Concern] — [Section] — [Why this blocks acceptance]

MINOR CONCERNS (should address)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
m1. [Concern] — [Section]
m2. [Concern] — [Section]

POSITIVE ASPECTS
━━━━━━━━━━━━━━━
+ [What the manuscript does well — be specific]
+ [What reviewers are likely to praise]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRENGTHENING STRATEGY (before resubmission)
Priority order:
  [1] [Highest-impact fix]
  [2] [Second fix]
  [3] [Third fix]
Estimated effort: [minor polish / 1–2 weeks revision / major rework]
```

---

## Journal Scoring Criteria

### Electrochemistry / Analytical Chemistry
- Novelty (new material, new analyte, new approach): weight 30%
- Analytical performance (LOD, selectivity, matrix validation): weight 30%
- Mechanistic understanding (not just "it works"): weight 20%
- Comparison with literature (fair, complete): weight 20%

### Education / Social Sciences
- Theoretical framework (coherent, relevant): weight 25%
- Methodological rigor (appropriate, well-justified): weight 30%
- Contribution to field (local + international relevance): weight 25%
- Discussion quality (limitations declared): weight 20%

### Health / Clinical
- CONSORT/STROBE/PRISMA compliance: weight 30%
- Internal validity (bias control): weight 30%
- Clinical significance (not just statistical): weight 20%
- Reproducibility (sufficient protocol detail): weight 20%

---

## Common Rejection Reasons (by field)

**Electrochemistry**: missing real sample validation, selectivity not tested, no comparison with existing methods, LOD calculated incorrectly.

**Education**: theoretical framework inconsistent with methodology, saturation not demonstrated, researcher positionality not declared.

**Health**: sample size underpowered, confounders uncontrolled, outcomes clinically irrelevant despite statistical significance.
