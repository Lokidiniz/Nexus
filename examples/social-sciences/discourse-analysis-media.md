# Example: Discourse analysis of media coverage

**Field:** Social Sciences / Communication Studies
**Team:** `*team social-sciences`
**Pipeline used:** `*pipeline full-manuscript`
**Journal target:** Dados — Revista de Ciências Sociais (Qualis A1, PT-BR)

---

## Scenario

Research question:
> "How did Brazilian mainstream media frame the quilombola land rights debate between 2020 and 2023?"

Starting point: corpus of 180 news articles collected from 4 major newspapers. No theoretical framework chosen yet.

---

## Step-by-step session

### 1. Load context

```
*team social-sciences
*mode interactive
```

Team loads: qualitative paradigm defaults, Qualis-aware journal profiles, Latin American context flags, ABNT citation style.

### 2. Find the theoretical gap

```
*find-gap "media framing quilombola land rights Brazil"
```

Literature Researcher output:
- 22 relevant studies (2015–2023), Sociologia & Política + DADOS + Lua Nova
- Dominant frameworks: Framing theory (Entman 1993), Critical Discourse Analysis (Fairclough), Agenda-setting
- Gap: studies focus on electoral coverage or environmental framings; quilombola territorial rights post-Marco Temporal (2023 STF ruling) not yet studied
- Brazilian context: Decreto 4887/2003, ADPF 742 — key legal references loaded

### 3. Validate novelty and framework

```
*check-novelty
```

```
*analyze "use Critical Discourse Analysis vs Framing Theory for media analysis"
```

Critical Analyst output:
```
FRAMEWORK COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Framing Theory (Entman):
  Fit: 75% — good for identifying problem definition, causal attribution
  Limitation: less equipped for ideological/power analysis

Critical Discourse Analysis (Fairclough):
  Fit: 88% — better for power relations, hegemony, social reproduction
  Limitation: more demanding corpus size (your 180 articles: sufficient)

Recommendation: CDA (Fairclough) — ADAPT
Adaptation: integrate Entman's frame taxonomy as analytical categories
within CDA's three-dimensional model (text / discursive practice / social practice)

RDS: ADAPT (85% match)
```

### 4. Design the study

```
*design "analyze media framing of quilombola land rights through CDA"
```

Methodologist output:
- Design: qualitative documentary analysis (CDA — Fairclough 3D model)
- Corpus: 180 articles (purposive — Folha, O Globo, O Estado, Correio Braziliense)
- Sampling strategy: maximum variation (geography, political affiliation of outlets)
- Analysis unit: lexical choices + rhetorical devices + intertextuality
- Software: NVivo or Atlas.ti (manual coding acceptable for 180 articles)
- Ethics: public domain documents — CEP not required; researcher positionality mandatory

### 5. Write the manuscript

```
*write introduction --journal "Dados" --lang pt-br
```

```
*write methods --journal "Dados" --lang pt-br
```

Scientific Writer produces Introduction in PT-BR with:
- Funnel: global context (land rights debates) → Brazilian context (quilombola legislation) → Marco Temporal STF ruling → gap → objective
- Theoretical framework section: CDA + Framing integrated approach (with `[REF NEEDED: Fairclough 1992 Language and Power]`)
- ABNT citations throughout

### 6. Critical analysis before submission

```
*validate-methods
```

Critical Analyst flags:
- M1. Researcher positionality: must be declared (CDA standard) — add §2.1
- M2. Inter-rater reliability: if coding with co-author, calculate Cohen's kappa or Krippendorff's alpha
- m1. Theoretical saturation: not applicable to documentary analysis — clarify in methods

### 7. Peer review simulation

```
*review --journal "Dados"
```

Predicted concerns for DADOS profile:
- Theoretical contribution to Brazilian sociology must be explicit (not just applied CDA)
- Latin American theoretical production: at least 3 Brazilian/Latin American theorists cited
- Methodological transparency: full codebook must be available (supplementary or OSF)

Score prediction: 7.2/10 — minor revision if positionality + Latin American theory addressed.

---

## Key outputs

- Complete manuscript (PT-BR, ABNT, ~8.000 palavras)
- Analytical framework: CDA + Entman integrated codebook
- Figure plan: 2 tables (frame frequency × outlet × year)
- Cover letter for DADOS editorial board

---

## Lessons from this example

1. **Framework choice matters** — CDA vs. Framing is not arbitrary; *analyze justifies each choice against your specific object
2. **Latin American theory is non-negotiable** for Brazilian social science journals — `*team social-sciences` flags this automatically
3. **Researcher positionality** for CDA is equivalent to reflexivity in qualitative health research — required, not optional
4. **180 articles is sufficient for CDA** — but codebook transparency (OSF or supplementary) dramatically increases acceptance
