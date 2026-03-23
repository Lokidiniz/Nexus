# Example: Electrochemical sensor ZIF-8 / dopamine detection

**Field:** Analytical Electrochemistry
**Team:** `*team electrochemistry`
**Pipeline used:** `*pipeline full-manuscript`
**Journal target:** Sensors and Actuators B: Chemical

---

## Scenario

You have:
- CV and DPV data for a ZIF-8 modified carbon paste electrode
- LOD = 0.12 µmol L⁻¹ (calculated from calibration curve)
- Selectivity data vs. uric acid, ascorbic acid, glucose
- Real sample: human serum (spiked, recovery 96–102%)
- No manuscript yet — starting from scratch

---

## Step-by-step session

### 1. Load team context

```
*team electrochemistry
```

Output: team context loaded — journal profiles, mandatory data list, LOD/LOQ protocol activated.

### 2. Assess data sufficiency before writing

```
*assess-data
```

Provide your data summary. Data Specialist checks:
- [x] CV curves (electrolyte + analyte)
- [x] DPV calibration curve (LOD/LOQ calculated)
- [x] Selectivity (3 interferents minimum)
- [x] Real sample recovery
- [ ] Stability (missing — agent flags this)
- [ ] Reproducibility (RSD%, n=5 — agent flags this)

Agent output:
```
📊 DATA ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sufficiency: 78% — CONDITIONAL for submission

MISSING (must add before submission):
  M1. Stability: test electrode over 7–14 days (signal retention %)
  M2. Reproducibility: RSD% for n=5 electrodes (inter-electrode)

PRESENT:
  ✓ LOD = 0.12 µmol L⁻¹ (3σ/S method)
  ✓ Selectivity: UA, AA, Glucose tested
  ✓ Real sample: serum, recovery 96–102%

Recommendation: collect stability + reproducibility data before full manuscript pipeline.
```

### 3. Run full manuscript pipeline

After collecting missing data:

```
*pipeline full-manuscript --journal "Sensors and Actuators B"
```

NEXUS Mission Briefing shows:
```
Phase 1a → literature-researcher: search dopamine sensors + ZIF-8 (2020–2024)
Phase 1b → critical-analyst: novelty check vs. retrieved literature
Phase 2  → methodologist: validate study design + ethics
Phase 3  → scientific-writer: Introduction + Methods
Phase 4  → data-specialist: Results figures plan + LOD verification
Phase 5  → scientific-writer: Results + Discussion + Conclusion
Phase 6  → peer-reviewer: pre-submission review (Sensors B profile)
Phase 7  → NEXUS: integration + final delivery
```

### 4. Literature search result (example)

```
*search "ZIF-8 electrochemical sensor dopamine" --years 2020-2024
```

Researcher receives:
- 12 relevant papers with DOI
- Comparison table: LOD range in literature (0.05–2.8 µmol L⁻¹)
- Gap identified: most use GCE; CPE with ZIF-8 underexplored
- 3 papers flagged as direct competitors

### 5. LOD verification

```
*calc-lod
```

Paste your calibration data. Data Specialist verifies:
- Method: 3σ/S (IUPAC, correct for DPV)
- R² check: must be ≥ 0.999 for linear range
- Output: LOD, LOQ, linear range, sensitivity

### 6. Pre-submission review

```
*review --journal "Sensors and Actuators B"
```

Peer Reviewer simulates Sens. Actuators B criteria:
- Novelty: moderate (ZIF-8 + CPE combination)
- LOD competitive: yes (0.12 vs. literature range)
- Flags: missing comparison table with recent literature (add Table 3)
- Score: 6.8/10 — Major revision predicted without the table

---

## Key outputs

After full pipeline:
- Complete manuscript (Introduction → Conclusion)
- Figure plan (5 figures specified)
- Reference list with confirmed DOIs
- Cover letter draft
- Predicted reviewer concerns + suggested responses

---

## Lessons from this example

1. **Always run `*assess-data` first** — saves time by identifying missing data before writing
2. **`*team electrochemistry` is mandatory** — loads LOD/LOQ protocol + journal profiles automatically
3. **Comparison table is non-negotiable** for analytical chemistry journals — peer reviewer will always flag its absence
4. **Real sample data** dramatically increases acceptance chances (recovery 96–102% is strong)
