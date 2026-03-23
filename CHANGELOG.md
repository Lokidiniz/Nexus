# Changelog — NEXUS Academic Research Squad

All notable changes to this project are documented here.

---

## [2.0.0] — 2026-03-22

### Added
- **Multilingual support**: all agents auto-detect user language and respond in PT-BR, EN, or ES
- **English agent names**: `literature-researcher`, `methodologist`, `critical-analyst`, `scientific-writer`, `peer-reviewer`, `data-specialist` — broader community acceptance
- **New pipelines**:
  - Thesis / Dissertation (chapter by chapter + full defense prep)
  - Scientific Poster (conference-ready)
  - Systematic Review / Scoping Review (PRISMA)
  - Funding Proposal expanded (NSF, FAPESP, CONACYT, CONICET, NIH)
- **Quick Mode**: NEXUS responds directly to simple questions without full pipeline
- **Export formats**: Markdown, LaTeX, ABNT, Word-paste ready
- **Skills**:
  - `/nexus` — auto-detect language entry point
  - `/nexus-en` — English mode
  - `/nexus-es` — Spanish mode
- **GitHub repository**: README in 3 languages, automated installers (install.sh, install.ps1)
- **Banner v2.0**: updated with `PT-BR · EN · ES` and version tag

### Changed
- NEXUS banner updated from v1.0 to v2.0
- All agent descriptions now bilingual (EN primary, examples in all languages)
- Funding proposal pipeline expanded to include international agencies
- Quality control checklist improved with explicit reference tracking

### Fixed
- Old agent names (`pesquisador-literatura`, `analista-critico`, etc.) replaced with English names throughout NEXUS coordination
- Reference placeholder rules clarified for Scientific Writer

---

## [1.0.0] — 2026-02-01

### Initial Release
- NEXUS coordinator agent (Opus model)
- 6 specialized agents: pesquisador-literatura, metodologista, analista-critico, redator-cientifico, revisor-pares, especialista-dados
- Pipelines: literature review, full manuscript, data analysis, rebuttal, funding proposal (BR)
- Skills: `/pesquisa`, `/texto-cientifico`
- Languages: PT-BR only
- Context: UFMA electrochemistry lab (ZIFs/MOFs sensors)
