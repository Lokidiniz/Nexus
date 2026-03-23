# Example: Teacher perception of inclusive education

**Field:** Education / Qualitative Research
**Team:** `*team education`
**Pipeline used:** `*pipeline literature-review` → `*pipeline full-manuscript`
**Journal target:** Cadernos de Pesquisa (Qualis A2, PT-BR)

---

## Scenario

Researcher wants to study:
> "How do teachers in Brazilian public schools perceive barriers to inclusive education for students with ASD?"

Starting point: research question defined, no data collected yet.

---

## Step-by-step session

### 1. Load team context + set language

```
*team education
```

```
*mode interactive
```

### 2. Map the literature

```
*map "inclusive education ASD Brazil teachers"
```

Literature Researcher delivers:
- State of the art: 18 papers (2018–2024), ERIC + SciELO + Periódicos CAPES
- Dominant approaches: survey (64%), qualitative interview (28%), mixed (8%)
- Gap: most studies focus on student outcomes, not teacher perception
- Brazilian context: BNCC implementation (2017) + Lei Brasileira de Inclusão (2015)

### 3. Design the study

```
*design "How do teachers perceive barriers to inclusive education for ASD students in Brazilian public schools?"
```

RDS CHECK output:
```
RDS CHECK — *design
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Question type: Descriptive/Explanatory (perceptions — subjective)
Population: Teachers, Brazilian public schools, ASD context

Candidate designs:
  [1] Survey (Likert) — Match: 55% → insufficient for depth of perception
  [2] Phenomenological qualitative — Match: 90% → REUSE
  [3] Mixed methods — Match: 70% → ADAPT (only if resources allow)

Recommended: Phenomenological qualitative (TIER 1 REUSE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Methodologist delivers:
- Design: phenomenological qualitative (Giorgi approach)
- Sample: 12–15 teachers (purposive, theoretical saturation)
- Instrument: semi-structured interview guide (12 questions)
- Analysis: thematic-phenomenological analysis (NVivo or manual)
- Ethics: CEP/CONEP required, consent form template provided

### 4. Validate novelty

```
*check-novelty
```

Critical Analyst output:
```
Novelty assessment:
  Theoretical gap: YES — teacher perception framed through phenomenological lens is underrepresented
  Methodological gap: YES — most Brazilian studies use quantitative surveys
  Context gap: YES — post-BNCC implementation perspective (2019–2024) not studied

Contribution type: INCREMENTAL + CONTEXTUAL (appropriate for Cadernos de Pesquisa)
Risk: Low — well-defined gap, appropriate method
```

### 5. Write the manuscript

After data collection and analysis:

```
*write introduction --journal "Cadernos de Pesquisa" --lang pt-br
```

```
*write methods --journal "Cadernos de Pesquisa" --lang pt-br
```

Scientific Writer applies:
- Funnel structure: global context (inclusion legislation) → Brazilian context (BNCC) → gap → objective
- Methods: ABNT format, CEP approval declared, positionality statement included
- Citation rules: no `[N]` — uses `[REF NEEDED: BNCC 2017 official document]` where uncertain

### 6. Peer review simulation

```
*review --journal "Cadernos de Pesquisa"
```

Predicted concerns:
- M1. Researcher positionality: must be explicitly declared (qualitative standard)
- M2. Saturation: justify how saturation was determined
- m1. Translation of quotes: if interviews in PT-BR, explain translation procedure for English abstract

---

## Key outputs

- Complete methodology section with CEP protocol outline
- Interview guide (12 questions, validated against research objective)
- Thematic analysis framework
- Manuscript draft (PT-BR, Cadernos de Pesquisa format)
- Reviewer report with strengthening strategy

---

## Lessons from this example

1. **Phenomenological design for perception questions** — when the goal is "how do people experience X", qualitative is almost always TIER 1 REUSE
2. **Brazilian context requires BNCC + LBI references** — `*team education` loads these automatically
3. **Positionality is non-negotiable** in qualitative research for Brazilian journals — add a paragraph in Methods
4. **Saturation, not sample size** — methodologist will specify range (12–15) not a fixed n
