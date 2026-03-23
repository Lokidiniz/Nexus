# NEXUS Architecture

## Overview

NEXUS is an AI agent orchestration framework built on Claude Code's native agent system. It coordinates a squad of 7 specialized research agents through a shared behavioral contract, typed commands, and pre-built workflow pipelines.

```
User → *command or *pipeline → NEXUS Coordinator
                                     ↓
                    ┌────────────────────────────────┐
                    │         Agent Squad            │
                    │  🔬 Literature Researcher      │
                    │  📐 Methodologist              │
                    │  ⚡ Critical Analyst           │
                    │  ✍️  Scientific Writer         │
                    │  🎯 Peer Reviewer              │
                    │  📊 Data Specialist            │
                    └────────────────────────────────┘
                                     ↓
                              Integrated Output
```

---

## Core Components

### 1. Agents (`agents/`)

Each agent is a Markdown file with YAML frontmatter consumed by Claude Code:

```
agents/
├── nexus.md                 # Coordinator (model: opus)
├── literature-researcher.md # 🔬 (model: sonnet)
├── methodologist.md         # 📐 (model: sonnet)
├── critical-analyst.md      # ⚡ (model: sonnet)
├── scientific-writer.md     # ✍️  (model: sonnet)
├── peer-reviewer.md         # 🎯 (model: sonnet)
└── data-specialist.md       # 📊 (model: sonnet)
```

**Frontmatter schema:**
```yaml
name: agent-name
icon: "🔬"
archetype: "The Navigator"
description: "Used by Claude Code agent selector"
model: sonnet | haiku | opus
color: blue | green | red | yellow | purple | orange
commands:
  - name: "*command [args]"
    description: "What it does"
```

### 2. Shared Behavioral Contract (`.nexus/`)

All agents read these files at session start:

```
.nexus/
├── activation-pipeline.md   # Squad table, modes, command protocol, handoffs
├── constitution.md           # 6 non-negotiable articles
└── rds.md                    # Research Decision System (REUSE/ADAPT/CREATE)
```

### 3. Workflows (`workflows/`)

YAML-defined multi-agent pipelines. NEXUS reads these when `*pipeline [name]` is called:

```
workflows/
├── literature-review.yaml
├── full-manuscript.yaml
├── pre-submission.yaml
├── funding-proposal.yaml
├── thesis.yaml
├── data-analysis.yaml
├── rebuttal.yaml
└── poster.yaml
```

**Pipeline execution model:**
- Phases run sequentially by default
- Phases with `parallel_group: A` (or B, C...) run simultaneously
- Each phase: agent receives task prompt + inputs from prior phases
- NEXUS integrates all outputs at the end

### 4. Tasks (`tasks/`)

Detailed operation specifications loaded by agents as context:

```
tasks/
├── search-literature.md
├── write-section.md
├── calculate-lod.md
├── design-study.md
├── review-manuscript.md
├── write-rebuttal.md
├── write-abstract.md
├── plan-figures.md
└── write-cover-letter.md
```

Each task includes: RDS check template, mode-specific steps (yolo/interactive/pre-flight), output format.

### 5. Teams (`teams/`)

Field-specific context bundles loaded with `*team [name]`:

```
teams/
├── team-electrochemistry.yaml
├── team-education.yaml
├── team-health.yaml
└── team-social-sciences.yaml
```

Teams inject: journal profiles, mandatory data requirements, field conventions, citation style defaults.

### 6. Hooks (`.nexus/hooks/`)

Python scripts that run via Claude Code hooks:

```
.nexus/hooks/
├── reference-guard.py        # Detects fake/incomplete citations (PostToolUse)
└── constitution-enforcer.py  # Detects overpromising language (PreToolUse)
```

Both are non-blocking (exit 2 = warning). They enforce Constitution Articles I.1 and III.

### 7. IDE Support

```
.claude/CLAUDE.md            # Claude Code auto-activation
.cursor/rules/nexus.mdc      # Cursor IDE (alwaysApply: true)
.gemini/GEMINI.md            # Gemini CLI auto-activation
```

### 8. npm Package (`bin/nexus-init.js`)

One-command installation via `npx nexus-research init`. Downloads all framework files from GitHub, installs agents to `~/.claude/agents/`, no dependencies required.

---

## Operating Modes

| Mode | Behavior | Activation |
|---|---|---|
| `interactive` | Checkpoint after each major step, awaits `ok / adjust / cancel` | DEFAULT |
| `yolo` | Fully autonomous, decisions logged at end | `*mode yolo` |
| `pre-flight` | Full plan delivered first, awaits approval, then executes | `*mode pre-flight` |

Modes persist for the session until changed with `*mode [name]`.

---

## Research Decision System (RDS)

Every creative task starts with an RDS evaluation:

```
REUSE  (≥90% match) → apply existing approach unchanged
ADAPT  (60–89%)     → modify existing for your specific context
CREATE (<60%)       → build from scratch with explicit justification
```

See `.nexus/rds.md` for full documentation and examples.

---

## Constitution (non-negotiable)

Six articles govern all agent behavior:

| Article | Principle |
|---|---|
| I — Data Integrity | No fabricated references or invented data |
| II — Researcher Autonomy | Agents propose; researchers decide |
| III — Reproducibility | Methods described in sufficient detail to replicate |
| IV — Attribution | Sources cited, agent contributions transparent |
| V — Context Appropriateness | Methods suited to field and question |
| VI — Open Science | Encourage open access, data sharing, preprints |

---

## Agent Call Protocol (NEXUS internal)

When NEXUS delegates to a specialist:

```
[ 🧠 NEXUS → 🔬 literature-researcher ]
Task: [specific task with all parameters]
Mode: [current mode]
```

When specialist returns:

```
[ 🔬 literature-researcher → 🧠 NEXUS ]
Done: [1-line summary] | Flags: [issues if any]
→ Proceeding to [next step]...
```

---

## Language Support

Auto-detection at conversation start:
- PT-BR → Portuguese response
- EN → English response
- ES → Spanish response

Agent communication and outputs follow detected language. Technical identifiers (commands, file names, code) remain in their original form.

---

## Directory Reference

```
nexus-squad/
├── agents/                  # Agent definitions (→ ~/.claude/agents/ on install)
├── workflows/               # Pipeline YAML definitions
├── tasks/                   # Task operation specifications
├── teams/                   # Team context bundles
├── skills/                  # Claude Code skill definitions
├── bin/
│   └── nexus-init.js        # npx nexus-research init
├── docs/
│   └── architecture.md      # This file
├── .nexus/
│   ├── constitution.md
│   ├── activation-pipeline.md
│   ├── rds.md
│   └── hooks/
│       ├── reference-guard.py
│       └── constitution-enforcer.py
├── .claude/
│   ├── CLAUDE.md            # Auto-activation (project-level)
│   └── settings.json        # Hook configuration
├── .cursor/
│   └── rules/nexus.mdc      # Cursor IDE rules
├── .gemini/
│   └── GEMINI.md            # Gemini CLI activation
├── CLAUDE.md                # Root-level activation copy
├── CONTRIBUTING.md
├── package.json
├── sync-ide.sh
├── install.sh
└── install.ps1
```
