# NEXUS — Squad de Pesquisa Acadêmica v2.0

> Sistema de agentes de IA para pesquisa científica de alto impacto, construído sobre **Claude Code** (Anthropic). Funciona em **PT-BR · EN · ES**.

[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0-blue)]()

---

## O que é o NEXUS?

O **NEXUS** é um sistema de 6 agentes especializados que opera dentro do Claude Code para auxiliar pesquisadores em todas as etapas da produção científica:

| Agente | Inglês (nome técnico) | Especialidade |
|--------|----------------------|---------------|
| Pesquisador de Literatura | `literature-researcher` | Busca sistemática, estado da arte |
| Metodologista | `methodologist` | Design de pesquisa, amostragem, ética |
| Analista Crítico | `critical-analyst` | Rigor metodológico, lacunas, argumentação |
| Redator Científico | `scientific-writer` | Redação IMRAD, ABNT, cover letter, rebuttal |
| Revisor de Pares | `peer-reviewer` | Pré-revisão simulando qualquer periódico |
| Especialista em Dados | `data-specialist` | Análise quanti/quali, LOD/LOQ, figuras |

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
curl -fsSL https://raw.githubusercontent.com/SEU_USUARIO/nexus-squad/main/install.sh | bash
```

### Instalação automática (Windows PowerShell)
```powershell
irm https://raw.githubusercontent.com/SEU_USUARIO/nexus-squad/main/install.ps1 | iex
```

### Instalação manual
```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/nexus-squad.git
cd nexus-squad

# 2. Copie os agentes
cp agents/*.md ~/.claude/agents/

# 3. Copie as skills
cp -r skills/* ~/.claude/skills/
```

---

## Como usar

### Ativar o NEXUS
No Claude Code, use o skill `/nexus`:
```
/nexus Preciso de uma revisão de literatura sobre sensores eletroquímicos com ZIF-8
```

Ou em inglês:
```
/nexus-en I need to write a manuscript for Biosensors & Bioelectronics
```

Ou em espanhol:
```
/nexus-es Necesito una propuesta de investigación para CONACYT
```

### Exemplos de uso

```bash
# Revisão sistemática de literatura
/nexus revisão sistemática sobre aprendizagem ativa no ensino médio

# Escrever seção de manuscrito
/nexus escrever introdução para Electrochimica Acta --journal "Electrochimica Acta"

# Pré-revisão antes de submissão
/nexus revisar manuscrito como revisor do ACS Sensors

# Proposta CNPq
/nexus proposta de pesquisa CNPq --stage ideia

# Capítulo de dissertação
/nexus capítulo de revisão de literatura da minha dissertação em química

# Análise de dados
/nexus calcular LOD/LOQ dos meus dados de DPV

# Pôster científico
/nexus pôster para congresso de eletroquímica
```

---

## Pipelines Disponíveis

| Tarefa | Agentes | Tempo estimado |
|--------|---------|----------------|
| Revisão de literatura | literature-researcher → critical-analyst → scientific-writer | ~5 min |
| Manuscrito completo | 6 agentes em sequência | ~15 min |
| Análise de dados | data-specialist → critical-analyst | ~3 min |
| Pré-revisão | peer-reviewer + critical-analyst | ~5 min |
| Proposta de fomento | literature-researcher + methodologist → scientific-writer | ~10 min |
| Capítulo de tese | literature-researcher → scientific-writer → critical-analyst | ~8 min |
| Pôster científico | data-specialist → scientific-writer | ~3 min |
| Rebuttal | peer-reviewer + critical-analyst → scientific-writer | ~5 min |

---

## Estrutura do Repositório

```
nexus-squad/
├── agents/                    # Agentes NEXUS
│   ├── nexus.md               # Coordenador principal
│   ├── literature-researcher.md
│   ├── methodologist.md
│   ├── critical-analyst.md
│   ├── scientific-writer.md
│   ├── peer-reviewer.md
│   └── data-specialist.md
├── skills/                    # Skills de ativação
│   ├── nexus/                 # /nexus (auto-detecta idioma)
│   ├── nexus-en/              # /nexus-en (English)
│   ├── nexus-es/              # /nexus-es (Español)
│   ├── pesquisa/              # /pesquisa (busca rápida Consensus)
│   └── texto-cientifico/      # /texto-cientifico (redação rápida)
├── install.sh                 # Instalador Linux/macOS/WSL
├── install.ps1                # Instalador Windows
├── CHANGELOG.md               # Histórico de versões
└── README.md                  # Este arquivo
```

---

## Contribuição

Pull requests são bem-vindos! Para contribuir:
1. Fork o repositório
2. Crie uma branch: `git checkout -b feature/novo-pipeline`
3. Commit suas mudanças: `git commit -m 'Add: pipeline para revisão de artigo em direito'`
4. Push: `git push origin feature/novo-pipeline`
5. Abra um Pull Request

---

## Licença

MIT — use livremente, inclusive para fins comerciais. Dê os créditos.

---

## Outros idiomas

- [English README](README.en.md)
- [README en Español](README.es.md)

---

*Desenvolvido com Claude Code + Anthropic API*
