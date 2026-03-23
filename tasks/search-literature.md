---
id: search-literature
agent: literature-researcher
command: "*search"
description: "Systematic literature search with real citations from Consensus and WebSearch"
modes: [yolo, interactive, pre-flight]
version: 2.0.0
---

# Task: Search Literature

**Agent**: 🔬 Literature Researcher
**Trigger**: `*search [topic] [--field area] [--period years] [--depth quick|standard|comprehensive]`

---

## Activation

```
🔬 Literature Researcher — systematic search & state of the art
Mode: [current mode]
Ready for: *search *map *find-gap *cite

Task: *search
Topic: [detected topic]
Initiating systematic search protocol...
```

---

## Execution Steps

### Mode: YOLO
1. Auto-select top 3 query variants
2. Run Consensus search (3 queries)
3. Run WebSearch for recent preprints
4. Synthesize results
5. Deliver with decisions log

### Mode: INTERACTIVE (DEFAULT)
1. Confirm topic interpretation with researcher
2. Propose 3 query variants — researcher selects or modifies
3. Run searches (announce each)
4. Show intermediate results — researcher can redirect
5. Synthesize and deliver

### Mode: PRE-FLIGHT
1. Map the intellectual landscape in abstract (no searches yet)
2. Propose full search plan: databases, queries, filters, expected volume
3. Await researcher approval
4. Execute approved plan
5. Deliver complete synthesis

---

## Search Protocol

```
Query 1: [topic] — direct, most specific
Query 2: [topic] [mechanism/application/method] — applied angle
Query 3: [topic] review OR systematic review — synthesis angle
```

For Brazilian context, add:
```
Query 4: [topic] Brazil OR "contexto brasileiro" — local relevance
Query 5: [topic] site:scielo.br — Brazilian journals
```

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔬 SEARCH RESULTS: [Topic]
Databases: [list] | Queries: [n] | Articles found: [n]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SYNTHESIS
[Thematic synthesis of main findings — 3-5 paragraphs]

KEY ARTICLES (confirmed with DOI)
1. Author et al. (Year). Title. Journal. DOI: 10.XXXX/XXXXX
   → Key contribution: [1 line]

IDENTIFIED GAPS
• [Gap 1]
• [Gap 2]

CONSTITUTION CHECK
☑ All citations confirmed by tool execution
☑ No fabricated references
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Next: *find-gap | *map | NEXUS pipeline continues
```

---

## Handoff to NEXUS

```
[ @literature → NEXUS ]
Task: search-literature
Output: [N] articles found | [N] key gaps identified
Flags: [any zero-result queries, uncertain topics]
Next: critical-analyst (*analyze gaps) or scientific-writer (*write literature-review)
```
