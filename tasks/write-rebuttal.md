# Task: write-rebuttal
## Agent: Scientific Writer + Peer Reviewer | Command: `*rebuttal`

### Purpose
Draft a complete, professional response to reviewer comments. Conciliatory tone, direct answers, tracked manuscript changes.

---

## RDS Check

```
RDS CHECK — *rebuttal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Template: Standard academic rebuttal format (REUSE ≥90%)
Adaptations needed: [none / tone / field convention]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Execution Steps

### Mode: interactive

1. Receive reviewer comments (paste full text)
2. Classify each comment: Major / Minor / Misunderstanding / Unjustified
3. **Checkpoint**: share comment classification, await confirmation
4. Draft response for each comment
5. **Checkpoint**: show draft responses, await feedback
6. Finalize complete rebuttal letter

### Mode: yolo

1. Classify comments, draft all responses, deliver complete letter

---

## Rebuttal Letter Structure

```
Dear Editors and Reviewers,

Thank you for the thorough review of our manuscript "[Title]" (Manuscript ID: [XX]).
We appreciate the constructive comments that have strengthened the work. Below, we provide
a point-by-point response to all concerns. Changes in the revised manuscript are highlighted
in [blue / tracked changes / supplementary diff].

─────────────────────────────────────────────────────────

REVIEWER 1

Comment R1.1:
"[Exact quote from reviewer — never paraphrase]"

Response:
[Direct answer. Start with genuine acknowledgment if the point is valid.
If the concern is based on a misunderstanding, explain clearly without being defensive.]

Manuscript change:
[Section X, line Y: "old text" → "new text"]
OR: [No change required — because: (explicit justification)]

─────────────────────────────────────────────────────────

Comment R1.2:
"[Exact quote]"

Response:
[...]

Manuscript change:
[...]

─────────────────────────────────────────────────────────

REVIEWER 2

[Same structure]

─────────────────────────────────────────────────────────

EDITOR COMMENTS (if any)

[Same structure]

─────────────────────────────────────────────────────────

SUMMARY OF CHANGES

| Comment | Change | Location |
|---------|--------|----------|
| R1.1    | Added selectivity data | Table 2 + Methods §2.4 |
| R1.2    | Revised LOD calculation | Methods §2.5 |
| R2.1    | Added comparison table | Table 3 |

We believe the revised manuscript fully addresses all concerns raised.
We thank the reviewers and editors for their valuable contributions to improving this work.

Sincerely,
[Corresponding author name]
[Institution]
[Email]
```

---

## Comment Classification Guide

| Type | Response strategy |
|---|---|
| **Valid major** | Full agreement + concrete change + "The reviewer is correct that..." |
| **Valid minor** | Agreement + small fix + show the change |
| **Partially valid** | Agree on the concern, explain why your approach still holds, compromise where possible |
| **Misunderstanding** | Clarify without condescension, offer to improve manuscript clarity |
| **Unjustified/overreach** | Polite but firm: cite literature, explain methodology rationale, decline if scientifically unsound |

---

## Tone Rules

- Never: "As stated clearly in the manuscript..." (condescending)
- Never: "The reviewer misunderstood..." (defensive)
- Always: "We apologize for the lack of clarity..." (even when it's their fault)
- Always: "Following the reviewer's suggestion..." (credit the reviewer)
- For unjustified requests: "We respectfully disagree because [specific reason with citation]"

---

## Author Notes (for researcher)

After draft is ready, writer lists:
- Which changes require new experiments or data
- Which responses require researcher to verify facts
- Passages where researcher must make the final judgment call
