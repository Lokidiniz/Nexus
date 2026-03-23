---
id: calculate-lod
agent: data-specialist
command: "*calc-lod"
description: "Calculate LOD, LOQ, sensitivity, linearity, and full analytical validation parameters"
modes: [yolo, interactive, pre-flight]
version: 2.0.0
---

# Task: Calculate LOD/LOQ

**Agent**: 📊 Data Specialist
**Trigger**: `*calc-lod [--method 3sigma|blank|calibration] [--technique dpv|swv|cv|other]`

---

## Activation

```
📊 Data Specialist — precision data analysis for publishable science
Mode: [current mode]
Ready for: *calc-lod *stats *figures *assess-data *interpret

Task: *calc-lod
Technique: [detected or ask]
Method: [3σ/S | ask researcher]
```

---

## Data Requirements (ask if not provided)

```
REQUIRED:
□ Blank/background signal (minimum 10 measurements) → calculates σ
□ Calibration curve data (concentration vs. signal) → calculates S (slope)
□ Analytical technique (DPV / SWV / CV / spectroscopy / other)

OPTIONAL:
□ Number of replicates per concentration
□ Matrix type (standard / real sample)
□ Target analyte and expected concentration range
```

---

## Calculation Protocol

### LOD (Limit of Detection)

**Method 1 — Blank (preferred for electrochemical)**
```
σ = standard deviation of blank signal (n ≥ 10)
S = slope of linear calibration curve
LOD = 3σ / S
```

**Method 2 — Calibration curve residuals**
```
σ = standard deviation of residuals from linear fit
S = slope
LOD = 3σ / S
```

**Method 3 — Signal-to-noise (for chromatography/spectroscopy)**
```
LOD = 3 × (noise) / S
```

### LOQ (Limit of Quantification)
```
LOQ = 10σ / S
```

### Analytical Sensitivity
```
Sensitivity = S = slope of calibration curve [signal/concentration unit]
```

### Linearity Assessment
```
R² ≥ 0.998 required for publication
Report: R², linear range, equation (y = mx + b ± SE)
```

### Recovery (real matrix)
```
Recovery (%) = (found / added) × 100
Acceptable: 95–105% (analytical) | 80–120% (biological matrices)
```

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 ANALYTICAL PARAMETERS: [Analyte / Technique]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CALIBRATION
  Equation:     y = [m]x + [b]  (± SE)
  R²:           [value]
  Linear range: [min] – [max] [unit]

DETECTION LIMITS
  σ (blank SD): [value] [unit]
  S (slope):    [value] [unit/concentration]
  LOD:          [value] [concentration unit]
  LOQ:          [value] [concentration unit]
  Sensitivity:  [value] [signal/concentration]

COMPARISON WITH LITERATURE
  [Table: this work vs. 3-5 published methods]
  [REF NEEDED: search "LOD [analyte] [technique]" for comparison]

CONSTITUTION CHECK
  ☑ Values calculated from provided data (not estimated)
  ☑ Method explicitly stated
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUTHOR NOTES
• Provide: [list any missing data needed]
• Verify: R² ≥ 0.998 for target journal requirements
• Selectivity study still needed (interference test)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Next: *figures (plan LOD curve figure) | *stats (selectivity test) | NEXUS continues
```
