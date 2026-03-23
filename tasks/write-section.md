---
id: write-section
agent: scientific-writer
command: "*write"
description: "Write any scientific text section with journal-specific style and real citations"
modes: [yolo, interactive, pre-flight]
version: 2.0.0
---

# Task: Write Section

**Agent**: ✍️ Scientific Writer
**Trigger**: `*write [section] [--journal name] [--lang pt-br|en|es] [--format abnt|apa|vancouver|ieee]`

**Sections**: `introduction` `methods` `results` `discussion` `conclusion` `abstract` `literature-review` `full-manuscript` `cover-letter` `rebuttal` `proposal`

---

## Activation

```
✍️ Scientific Writer — precision text for high-impact science
Mode: [current mode]
Ready for: *write *rewrite *abstract *cover-letter *translate *rebuttal

Task: *write [section]
Target: [journal or format]
Language: [detected or specified]
```

---

## Pre-Write Checklist (run before writing)

- [ ] Real citations available from Literature Researcher? (if no → use `[REF NEEDED: description]`)
- [ ] Data summary available from Data Specialist? (for Results/Discussion)
- [ ] Critical analysis available from Critical Analyst? (for revisions)
- [ ] Journal/format confirmed? (determines style, length, voice)
- [ ] Language confirmed? (PT-BR / EN / ES)

---

## Section Templates

### Introduction — Thematic Funnel
```
P1: Broad context (why this topic matters globally)
P2: State of the art (what has been done — cite Literature Researcher output)
P3: Critical gap (what is missing or broken)
P4: This work's approach (how we address the gap)
P5: Contribution summary + paper structure
```

### Methods
- For experimental: reagents → equipment → procedure → statistical analysis
- For qualitative: paradigm → participants → instruments → analysis procedure → ethics
- For clinical: CONSORT/STROBE compliance → design → ethics approval → outcomes

### Results
- One central finding per paragraph
- Data first, interpretation after (interpretation belongs in Discussion)
- Connect every figure/table with analysis (never "see Figure X" alone)

### Discussion
- Contextualize each result with literature
- Compare with prior work (convergence AND divergence)
- Explain mechanisms / interpretations
- State limitations honestly
- Close the loop to Introduction gap

### Abstract (IMRaD compressed)
```
Background (1-2 sent) | Objective (1 sent) | Methods (1-2 sent) |
Results (2-3 sent with numbers) | Conclusion (1 sent)
```

---

## Citation Rules (Constitution Article I.1)

| Situation | Treatment |
|-----------|-----------|
| Real citation with DOI from Literature Researcher | Use (Author, Year) + include DOI in notes |
| No citation found for a claim | `[REF NEEDED: what to search for]` |
| Well-established fact | `[verify ref]` at end of sentence |
| **Never** | Generic `[1]` or `[N]` without context |

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✍️ SECTION: [Section Name]
Journal: [name] | Format: [standard] | Language: [lang]
Word count: ~[N] words
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[SECTION TEXT — publication ready]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUTHOR NOTES
• [Where to insert specific data]
• [References marked [REF NEEDED: description]]
• [Decisions only the researcher can make]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Next: *rewrite (revision) | peer-reviewer (*review) | NEXUS pipeline continues
```
