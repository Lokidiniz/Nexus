# Task: write-abstract
## Agent: Scientific Writer | Command: `*abstract [--words limit]`

### Purpose
Write a publication-ready abstract (structured or unstructured) with keywords, from a manuscript draft or data summary.

---

## RDS Check

```
RDS CHECK — *abstract
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Format: [structured (journal requires) / unstructured (standard IMRaD)]
Word limit: [journal-specific or default 250]
Template match: IMRaD compressed (REUSE ≥90%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Unstructured Abstract (default — most journals)

**Structure: Background → Objective → Methods → Results → Conclusion**

```
[1-2 sentences: global context and problem relevance]
[1 sentence: specific gap this work addresses]
[1 sentence: objective of this study]
[1-2 sentences: methods — key approach, materials, analytical technique]
[2-3 sentences: main results WITH NUMBERS — LOD, %, n, p-value, effect size]
[1 sentence: conclusion — what this result means + main contribution]
```

**Target word count**: 150–250 words (adapt to journal limit)
**Numbers rule**: every result sentence must include at least one quantitative value.

---

## Structured Abstract (some journals require)

```
Background:   [1-2 sentences]
Objective:    [1 sentence]
Methods:      [2-3 sentences]
Results:      [2-3 sentences WITH numbers]
Conclusions:  [1-2 sentences]
```

---

## Keywords

```
3–6 keywords (journal default: 5)
Rules:
- Not in the title (they already index those)
- Most specific first, most general last
- Include: main technique | main analyte or field | key innovation
- Bilingual if manuscript is PT-BR for national journal: Portuguese + English terms
```

---

## Output Format

```
✍️ ABSTRACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Word count: XX / limit: XX]

[Abstract text]

Keywords: [keyword 1]; [keyword 2]; [keyword 3]; [keyword 4]; [keyword 5]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUTHOR NOTES
• Numbers marked [?] require researcher confirmation
• [REF NEEDED] items require citation from literature researcher
```

---

## Common Abstract Errors (checklist before delivery)

- [ ] Contains no result numbers → add at least 2 specific values
- [ ] Missing gap statement → reviewer cannot tell why this work was needed
- [ ] Conclusion overstates evidence → "proves" / "definitively shows" → soften
- [ ] Too long (>limit) → cut from background first, then methods
- [ ] Keywords overlap with title → replace with complementary terms
- [ ] Graphical abstract mentioned but not described → add alt-text or figure plan
