# NEXUS — Academic Research Squad v2.0

> AI agent system for high-impact scientific research, built on **Claude Code** (Anthropic). Works in **PT-BR · EN · ES**.

[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0-blue)]()

---

## What is NEXUS?

**NEXUS** is a system of 6 specialized AI agents that runs inside Claude Code to assist researchers at every stage of scientific production:

| Agent | Technical name | Specialty |
|-------|---------------|-----------|
| Literature Researcher | `literature-researcher` | Systematic search, state of the art |
| Methodologist | `methodologist` | Research design, sampling, ethics |
| Critical Analyst | `critical-analyst` | Methodological rigor, gaps, argumentation |
| Scientific Writer | `scientific-writer` | IMRAD writing, APA/Vancouver/IEEE, cover letter, rebuttal |
| Peer Reviewer | `peer-reviewer` | Pre-review simulating any journal |
| Data Specialist | `data-specialist` | Quanti/quali analysis, LOD/LOQ, figures |

**NEXUS** is the coordinator that orchestrates all of them.

---

## Why use it?

- **Free** — works with Claude Code (free plan)
- **Multi-field** — chemistry, health, education, social sciences, engineering, law
- **Multilingual** — responds in PT-BR, EN, or ES automatically
- **Global journals** — knows Nature, Science, JACS, Lancet, NEJM, IEEE, and 50+ profiles
- **Ready-made pipelines** — systematic review, full manuscript, thesis, poster, rebuttal, funding proposal

---

## Installation

### Prerequisite
[Claude Code](https://claude.ai/code) installed and configured.

### Automatic install (Linux/macOS/WSL)
```bash
curl -fsSL https://raw.githubusercontent.com/YOUR_USER/nexus-squad/main/install.sh | bash
```

### Automatic install (Windows PowerShell)
```powershell
irm https://raw.githubusercontent.com/YOUR_USER/nexus-squad/main/install.ps1 | iex
```

### Manual install
```bash
git clone https://github.com/YOUR_USER/nexus-squad.git
cd nexus-squad
cp agents/*.md ~/.claude/agents/
cp -r skills/* ~/.claude/skills/
```

---

## How to use

### Activate NEXUS
In Claude Code, use the `/nexus-en` skill:
```
/nexus-en I need a systematic literature review on MOF-based electrochemical sensors
```

```
/nexus-en Write the Introduction section for Biosensors & Bioelectronics
```

```
/nexus-en Review my manuscript as an ACS Nano reviewer
```

```
/nexus-en Build a funding proposal for NSF — electrochemical sensors for food safety
```

### Available Pipelines

| Task | Agents | Est. time |
|------|--------|-----------|
| Literature review | literature-researcher → critical-analyst → scientific-writer | ~5 min |
| Full manuscript | All 6 agents in sequence | ~15 min |
| Data analysis | data-specialist → critical-analyst | ~3 min |
| Pre-submission review | peer-reviewer + critical-analyst | ~5 min |
| Funding proposal | literature-researcher + methodologist → scientific-writer | ~10 min |
| Thesis chapter | literature-researcher → scientific-writer → critical-analyst | ~8 min |
| Scientific poster | data-specialist → scientific-writer | ~3 min |
| Rebuttal | peer-reviewer + critical-analyst → scientific-writer | ~5 min |

---

## Contributing

Pull requests are welcome! To contribute:
1. Fork the repository
2. Create a branch: `git checkout -b feature/new-pipeline`
3. Commit: `git commit -m 'Add: pipeline for law review articles'`
4. Push: `git push origin feature/new-pipeline`
5. Open a Pull Request

---

## License

MIT — use freely, including for commercial purposes. Give credit.

---

## Other languages

- [README em Português](README.md)
- [README en Español](README.es.md)

---

*Built with Claude Code + Anthropic API*
