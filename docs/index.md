# NEXUS Academic Research Framework

> **"We return control to those with the courage to build."**

NEXUS é um framework open-source de orquestração de IA que transforma o [Claude Code](https://claude.ai/code) em um assistente científico completo, com **7 agentes especializados** coordenados para cobrir todo o ciclo de vida de uma publicação científica.

Funciona em **PT-BR · EN · ES** — Claude Code · Cursor · Gemini CLI.

---

## Instalação em 1 comando

```bash
npx nexus-research init
```

Ou via script:

=== "Linux / macOS / WSL"
    ```bash
    curl -fsSL https://raw.githubusercontent.com/Lokidiniz/Nexus/main/install.sh | bash
    ```

=== "Windows PowerShell"
    ```powershell
    irm https://raw.githubusercontent.com/Lokidiniz/Nexus/main/install.ps1 | iex
    ```

---

## O Squad

| Agente | Especialidade | Comandos principais |
|--------|--------------|-------------------|
| 🧠 **NEXUS** | Orquestração e pipelines | `*pipeline`, `*quick`, `*mode` |
| 🔬 **Literature Researcher** | Busca sistemática, estado da arte | `*search`, `*map`, `*find-gap` |
| 📐 **Methodologist** | Design de pesquisa, amostragem, ética | `*design`, `*sample`, `*instrument` |
| ⚡ **Critical Analyst** | Rigor metodológico, gaps, argumentação | `*analyze`, `*check-novelty` |
| ✍️ **Scientific Writer** | IMRAD, ABNT, APA, cover letter | `*write`, `*rewrite`, `*abstract` |
| 🎯 **Peer Reviewer** | Simulação de revisão por pares | `*review`, `*rebuttal`, `*score` |
| 📊 **Data Specialist** | LOD/LOQ, estatística, figuras | `*calc-lod`, `*stats`, `*figures` |

---

## Início rápido

Após instalar, abra seu projeto no Claude Code e digite:

```
*pipeline literature-review
```

```
*pipeline full-manuscript --journal "Electrochimica Acta"
```

```
*quick Qual o melhor método para calcular LOD em DPV?
```

---

## Pipelines disponíveis

| Pipeline | O que entrega |
|----------|--------------|
| `*pipeline literature-review` | Revisão sistemática completa |
| `*pipeline full-manuscript` | Artigo completo do zero |
| `*pipeline pre-submission` | Revisão antes de submeter |
| `*pipeline data-analysis` | Análise estatística + figuras |
| `*pipeline funding-proposal` | Proposta CNPq / CAPES / NSF |
| `*pipeline thesis` | Capítulo de tese/dissertação |
| `*pipeline rebuttal` | Resposta a revisores |
| `*pipeline poster` | Pôster científico |

---

## Constituição (não-negociável)

Todos os agentes são governados por 6 artigos:

1. **Integridade dos dados** — nenhuma referência fabricada, nenhum dado inventado
2. **Autonomia do pesquisador** — conclusões e metodologia são sempre suas decisões
3. **Reprodutibilidade** — métodos descritos com detalhe suficiente para replicação
4. **Atribuição** — fontes citadas, contribuições dos agentes transparentes
5. **Adequação ao contexto** — métodos adequados ao campo e à pergunta
6. **Ciência aberta** — incentivo a acesso aberto, compartilhamento de dados, preprints

---

## Comunidade

- [GitHub](https://github.com/Lokidiniz/Nexus) — issues, PRs, discussões
- [Contribuindo](contributing.md) — como adicionar agentes, workflows, exemplos
- [Arquitetura](architecture.md) — como o framework funciona internamente
