# NEXUS — Squad de Pesquisa Acadêmica v2.0

> Plugin que transforma o **Claude Code** em um assistente científico completo, com 7 agentes especializados coordenados pelo NEXUS para cobrir todo o ciclo de vida de uma publicação científica. Funciona em **PT-BR · EN · ES**.

[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0-blue)]()

---

## O que é o NEXUS?

O **NEXUS** é um sistema de 6 agentes especializados que opera dentro do Claude Code para auxiliar pesquisadores em todas as etapas da produção científica:

| Agente | Nome técnico | Especialidade |
|--------|-------------|---------------|
| Literature Researcher | `literature-researcher` | Busca sistemática, estado da arte |
| Methodologist | `methodologist` | Design de pesquisa, amostragem, ética |
| Critical Analyst | `critical-analyst` | Rigor metodológico, lacunas, argumentação |
| Scientific Writer | `scientific-writer` | Redação IMRAD, ABNT, cover letter, rebuttal |
| Peer Reviewer | `peer-reviewer` | Pré-revisão simulando qualquer periódico |
| Data Specialist | `data-specialist` | Análise quanti/quali, LOD/LOQ, figuras |

O **NEXUS** é o coordenador que orquestra todos eles.

---

## Por que usar?

- **Gratuito** — funciona com Claude Code (plano gratuito)
- **Multi-área** — química, saúde, educação, ciências sociais, engenharia, direito
- **Multilíngue** — responde em PT-BR, EN ou ES automaticamente
- **Periódicos brasileiros** — conhece o sistema Qualis, CAPES, CNPq, SciELO
- **Pipelines prontos** — revisão sistemática, manuscrito completo, tese, pôster, rebuttal, proposta de fomento

---

## Instalação

### Pré-requisito
[Claude Code](https://claude.ai/code) instalado e configurado.

### Instalação automática (Linux/macOS/WSL)
```bash
curl -fsSL https://raw.githubusercontent.com/Lokidiniz/Nexus/main/install.sh | bash
```

### Instalação automática (Windows PowerShell)
```powershell
irm https://raw.githubusercontent.com/Lokidiniz/Nexus/main/install.ps1 | iex
```

### Instalação manual
```bash
# 1. Clone o repositório
git clone https://github.com/Lokidiniz/Nexus.git
cd Nexus

# 2. Copie os agentes
cp agents/*.md ~/.claude/agents/

# 3. Copie as skills
cp -r skills/* ~/.claude/skills/
```

---

## Como usar

### Ativar o NEXUS no Claude Code

```bash
# Auto-detecta idioma (PT-BR/EN/ES)
/nexus Preciso de uma revisão de literatura sobre sensores eletroquímicos com ZIF-8

# Modo inglês
/nexus-en Write the Introduction for Biosensors & Bioelectronics

# Modo espanhol
/nexus-es Necesito una propuesta para CONACYT
```

### Comandos diretos

| Comando | O que faz |
|---------|-----------|
| `/nexus [tarefa]` | Ativa NEXUS (auto-idioma) |
| `/nexus-en [task]` | NEXUS em inglês |
| `/nexus-es [tarea]` | NEXUS em espanhol |
| `/pesquisa [tema]` | Busca rápida no Consensus |
| `/texto-cientifico [seção]` | Redação de seção isolada |

### Exemplos de uso

```
/nexus revisão sistemática sobre aprendizagem ativa no ensino médio
/nexus escrever manuscrito completo para Electrochimica Acta
/nexus revisar rascunho como revisor do ACS Sensors
/nexus proposta CNPq sobre sensores descartáveis para segurança alimentar
/nexus capítulo de revisão de literatura da minha dissertação
/nexus calcular LOD/LOQ dos meus dados de DPV
/nexus pôster científico para congresso de eletroquímica
```

---

## Pipelines Disponíveis

| Tarefa | Agentes | Tempo est. |
|--------|---------|-----------|
| Revisão de literatura | literature-researcher → critical-analyst → scientific-writer | ~5 min |
| Manuscrito completo | 6 agentes em sequência | ~15 min |
| Análise de dados | data-specialist → critical-analyst | ~3 min |
| Pré-revisão | peer-reviewer + critical-analyst | ~5 min |
| Proposta de fomento | literature-researcher + methodologist → scientific-writer | ~10 min |
| Capítulo de tese | literature-researcher → scientific-writer → critical-analyst | ~8 min |
| Pôster científico | data-specialist → scientific-writer | ~3 min |
| Rebuttal | peer-reviewer + critical-analyst → scientific-writer | ~5 min |

### Pipelines automáticos (diagrama)

```
Revisão de Literatura
  literature-researcher → critical-analyst → scientific-writer

Manuscrito Completo
  literature-researcher ┐
                         ├→ critical-analyst → scientific-writer → peer-reviewer
  data-specialist       ┘

Revisão de Manuscrito
  peer-reviewer  ┐
                  ├→ scientific-writer
  critical-analyst┘

Proposta de Fomento
  literature-researcher ┐
                          ├→ critical-analyst → scientific-writer
  methodologist          ┘
```

---

## Requisitos de MCP

Para uso completo das ferramentas de busca, configure no Claude Code:

- **Consensus** — síntese de literatura científica (disponível em claude.ai)
- **PubMed** (opcional) — base de dados biomédica/química

---

## Estrutura do Repositório

```
Nexus/
├── agents/                    # Agentes do squad
│   ├── nexus.md               # Coordenador principal (Opus)
│   ├── literature-researcher.md
│   ├── methodologist.md
│   ├── critical-analyst.md
│   ├── scientific-writer.md
│   ├── peer-reviewer.md
│   └── data-specialist.md
├── skills/                    # Skills de ativação
│   ├── nexus/                 # /nexus (auto-detecta idioma)
│   ├── nexus-en/              # /nexus-en (English)
│   └── nexus-es/              # /nexus-es (Español)
├── install.sh                 # Instalador Linux/macOS/WSL
├── install.ps1                # Instalador Windows
├── CHANGELOG.md               # Histórico de versões
└── README.md                  # Este arquivo
```

---

## Contribuição

Pull requests são bem-vindos!
1. Fork o repositório
2. Crie uma branch: `git checkout -b feature/novo-pipeline`
3. Commit: `git commit -m 'Add: pipeline para revisão em direito'`
4. Push e abra um Pull Request

---

## Contexto de desenvolvimento

Desenvolvido para pesquisa em **sensores eletroquímicos** com MOFs/ZIFs e impressão 3D (FDM/DIW), laboratório de eletroquímica UFMA. Funciona para qualquer área: química, saúde, educação, engenharia, ciências sociais.

---

## Licença

MIT — livre para usar, adaptar e distribuir. Dê os créditos.

---

## Outros idiomas

- [English README](README.en.md)
- [README en Español](README.es.md)

---

*Desenvolvido com Claude Code + Anthropic API*
