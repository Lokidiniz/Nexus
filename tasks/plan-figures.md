# Task: plan-figures
## Agent: Data Specialist | Command: `*figures`

### Purpose
Plan all publication figures: type, content, composition, software, and journal requirements. Does not generate files — delivers specs for researcher to execute.

---

## RDS Check

```
RDS CHECK — *figures
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Journal figure guidelines: [load if provided]
Field conventions: [electrochemistry / education / health / social sciences]
Template match: [standard figure set for field / ADAPT for specific data]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Execution Steps

1. Receive: data description (or data files), journal target, number of allowed figures
2. Classify data types: spectroscopic / electrochemical / statistical / qualitative / schematic
3. Map each data type → optimal figure type
4. Plan figure set: primary (essential) + secondary (supporting) + supplementary
5. Deliver complete figure specification

---

## Output Format

```
📊 FIGURE PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Journal: [name] | Limit: [n figures] | Format: [TIFF/EPS/PDF | dpi]

FIGURE SET
━━━━━━━━━━
Fig 1 — [Title]
  Type:     [composite panel / single plot / schematic]
  Content:  [what data is shown]
  Panels:   [1A: ... | 1B: ... | 1C: ...]
  Priority: ESSENTIAL
  Software: [Origin / Python matplotlib / R ggplot2 / GraphPad / Inkscape]
  Notes:    [scale bar needed? / color accessibility? / inset zoom?]

Fig 2 — [Title]
  Type:     [...]
  Content:  [...]
  Priority: ESSENTIAL / SUPPORTING
  Software: [...]

Supplementary Fig S1 — [Title]
  Type:     [...]
  Content:  [...]
  Priority: SUPPLEMENTARY

PRODUCTION CHECKLIST
━━━━━━━━━━━━━━━━━━━━
[ ] Resolution ≥ 300 dpi (bitmap) or vector format (PDF/EPS/SVG)
[ ] Font size ≥ 8pt at final print size
[ ] Color mode: RGB for online, CMYK for print (check journal)
[ ] Color-blind safe palette (avoid red+green without symbol redundancy)
[ ] All axes labeled with units
[ ] Error bars defined (SD / SEM / CI 95% — state which)
[ ] Statistical significance markers explained in caption
[ ] Scale bars on microscopy/SEM images
[ ] Line width ≥ 1pt for visibility at reduced size

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESEARCHER DECISIONS NEEDED
• [Data selections, color choices, which replicates to show]
```

---

## Figure Type Quick-Reference

| Data | Recommended figure type |
|---|---|
| CV / DPV curves | Overlaid line plot with offset if needed |
| Calibration curve | Scatter + regression line + equation + R² |
| LOD/LOQ | Calibration curve with 3σ/S annotation |
| Selectivity | Bar chart or spider chart |
| Stability over time | Line plot with error bars (SD, n=3) |
| XRD pattern | Stacked line plots with peak annotations |
| SEM morphology | Grayscale image + scale bar |
| Comparison with literature | Table preferred over figure |
| Qualitative themes | Frequency table or word cloud (field-dependent) |
| Statistical groups | Box plot (n>10) or bar + scatter overlay (n<10) |
| Mechanism/workflow | Schematic (Inkscape / BioRender / ChemDraw) |

---

## Color Palettes (accessible + print-safe)

**For line plots (electrochemistry):**
- Blue `#2166AC`, Red `#D6604D`, Green `#4DAC26`, Black `#000000`, Orange `#F46D43`

**For bar/group plots:**
- ColorBrewer `Set2` (8 colors, colorblind-safe)
- Viridis (sequential, perceptually uniform)

**Avoid**: pure red + green combinations (colorblind conflict)
