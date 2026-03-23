# RDS — Research Decision System
## NEXUS Adaptation of the REUSE > ADAPT > CREATE Principle

> *"The best scientific writing is not the most original — it is the most precise.
> Most of what we build already exists in a better form somewhere else.
> Find it first."*

---

## What is RDS?

The **Research Decision System** is a mandatory evaluation protocol that runs before any creative task in NEXUS. It forces the researcher (and all agents) to ask: **do we actually need to build this from scratch?**

This is the academic research equivalent of the aiox-core IDS principle — adapted to scientific production where:
- Templates exist for every section of every major journal
- Methodologies are documented and validated
- Statistical approaches have established precedents
- Writing patterns repeat across fields

**Building from scratch when you don't need to is waste. RDS eliminates it.**

---

## The Three Tiers

### TIER 1 — REUSE (≥90% match)
> Use the existing approach, template, or methodology without modification.

**Condition**: The existing approach matches ≥90% of your requirements.

**Examples**:
- Writing an Introduction for an Electrochimica Acta paper → use established funnel structure (context → gap → approach → contributions)
- Calculating LOD for DPV data → use 3σ/S method (IUPAC standard)
- Designing a survey study on teacher perception → use established phenomenological protocol
- Citing a foundational reference → reuse the exact citation format from template

**RDS action**: apply without modification, acknowledge source.

---

### TIER 2 — ADAPT (60–89% match)
> Take the existing approach and modify specific elements for your context.

**Condition**: The existing approach is ≥60% applicable but requires targeted changes.

**Examples**:
- Standard literature review structure → adapt section weighting for a highly specialized sub-field
- Established interview script → adapt questions for Brazilian rural health context
- Standard manuscript structure → adapt length for a journal with strict word limits
- Known pipeline for electrochemical sensors → adapt LOD calculation for a non-standard matrix

**RDS action**: identify the base approach, list specific adaptations, justify each change.

```
ADAPT LOG
Base: [existing approach/template]
Adaptations:
  [1] Changed: [what] → Because: [why this specific case requires it]
  [2] Added: [what] → Because: [gap in base approach for this context]
  [3] Removed: [what] → Because: [not applicable here, justified]
Result: [adapted approach]
```

---

### TIER 3 — CREATE (<60% match)
> Build a new approach from scratch with explicit justification.

**Condition**: No existing approach covers ≥60% of your requirements.

**This tier is expensive.** Creating from scratch requires:
- Explicit statement of why existing approaches are insufficient
- Documentation of what was searched and rejected
- Full description of the new approach
- Assessment of additional validation needed

**Examples**:
- A genuinely new analytical method with no precedent in the literature
- A research design for a phenomenon never studied in a specific population
- A hybrid pipeline for a task that spans two fields with no established bridge

**RDS action**: document the decision fully.

```
CREATE LOG
Task: [what needs to be created]
Approaches evaluated and rejected:
  [1] [Approach name] — rejected because: [specific reason]
  [2] [Approach name] — rejected because: [specific reason]
Why existing approaches are insufficient:
  [explicit statement]
New approach:
  [full description]
Validation needed:
  [what must be verified before using this approach]
```

---

## RDS in Practice

### For Scientific Writing

Before writing any section, NEXUS asks:

```
RDS CHECK — *write introduction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Template match: Thematic Funnel (standard)
Field: Electrochemistry | Journal: Electrochimica Acta

Match score: 95% (REUSE)
→ Apply standard funnel structure:
   P1: Global context (environmental/health relevance)
   P2: State of art (sensor approaches)
   P3: Gap (specific limitation)
   P4: This work
   P5: Contributions + structure

No adaptation required. Proceeding.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### For Methodology

Before designing a study, NEXUS asks:

```
RDS CHECK — *design [question]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Question type: Causal (X causes Y?)
Population: Teachers in Brazilian rural schools

Candidate designs:
  [1] RCT — Match: 40% (randomization infeasible here) → REJECT
  [2] Quasi-experimental — Match: 75% (ADAPT)
  [3] Action research — Match: 65% (ADAPT)

Recommended: Quasi-experimental (ADAPT)
Adaptation needed: address selection bias in rural context
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### For Data Analysis

Before running any statistical test, NEXUS asks:

```
RDS CHECK — *stats
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data: 3 independent groups, n=30 each
Distribution: Shapiro-Wilk p=0.03 (non-normal)

Standard test: ANOVA — Match: 45% (normality violated) → REJECT
Alternative: Kruskal-Wallis + Dunn — Match: 95% (REUSE)

→ Apply Kruskal-Wallis. No adaptation needed.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## RDS Metrics

Track over time to measure framework effectiveness:

| Month | CREATE Rate | Target |
|-------|------------|--------|
| 1 | ~40–50% (learning phase) | — |
| 3 | <30% | baseline established |
| 6 | <20% | framework mastered |
| 12 | <10% | expert level |

**A declining CREATE Rate means the researcher is building on accumulated knowledge instead of reinventing.** This is the goal.

---

## Integration with Agents

Every agent applies RDS before executing:

- `*write` → check writing template first
- `*design` → check design precedents first
- `*stats` → check established test for this design first
- `*search` → check if prior search covers the topic first
- `*review` → check if journal profile is already loaded first

The result: faster pipelines, more consistent outputs, less wasted effort.

---

*RDS v1.0 — NEXUS Academic Research Framework*
*Adapted from the aiox-core IDS principle for scientific research*
