# NEXUS — Squad de Pesquisa Acadêmica para Claude Code

> Plugin que transforma o Claude Code em um assistente científico completo, com 7 agentes especializados coordenados pelo NEXUS para cobrir todo o ciclo de vida de uma publicação científica.

---

## Instalação

```bash
# 1. Registrar o marketplace
claude plugin marketplace add https://github.com/Lokidiniz/Nexus

# 2. Instalar o plugin
claude plugin install nexus
```

Pronto. Reinicie o Claude Code e os comandos estarão disponíveis.

---

## Comandos disponíveis

| Comando | O que faz |
|---------|-----------|
| `/literatura [tema]` | Revisão sistemática de literatura com busca real (Consensus + PubMed) |
| `/manuscrito [tema] --periodico [nome]` | Pipeline completo de manuscrito do zero até revisão por pares |
| `/revisar --periodico [nome]` | Revisão de rascunho existente com pré-revisão simulando o periódico |
| `/rebuttal` | Resposta a revisores — pacote completo de resubmissão |
| `/proposta [agencia]` | Proposta de fomento (CNPq, CAPES, FAPEMA, FINEP) |
| `/pesquisa [tema]` | Busca rápida no Consensus com síntese de evidências |
| `/texto-cientifico [seção]` | Redação de seções isoladas (introdução, métodos, resultados...) |

---

## Exemplos de uso

```
/literatura ZIF-67 sensores eletroquímicos antibióticos
```
```
/manuscrito eletrodos FDM + ZIF-67 para tetraciclina --periodico "Sensors and Actuators B"
```
```
/revisar --periodico "Electrochimica Acta"
[cole seu rascunho aqui]
```
```
/rebuttal
[cole os comentários dos revisores aqui]
```
```
/proposta cnpq --tema "sensores descartáveis para segurança alimentar" --edital "Universal 2025"
```

---

## O Squad

| Agente | Função |
|--------|--------|
| **nexus** | Coordenador — orquestra o pipeline completo |
| **pesquisador-literatura** | Busca sistemática com Consensus + PubMed + WebSearch |
| **analista-critico** | Avaliação de rigor metodológico, novidade e gaps |
| **redator-cientifico** | Redação IMRAD para qualquer periódico, PT-BR ou EN |
| **revisor-pares** | Pré-revisão simulando editor e revisores do periódico alvo |
| **especialista-dados** | LOD/LOQ, estatística, figuras, suficiência amostral |
| **metodologista** | Design de pesquisa, amostragem, instrumentos, ética |

---

## Pipelines automáticos

O NEXUS seleciona e orquestra os agentes automaticamente conforme a tarefa:

```
Revisão de Literatura
  pesquisador-literatura → analista-critico → redator-cientifico

Manuscrito Completo
  pesquisador-literatura ┐
                         ├→ analista-critico → redator-cientifico → revisor-pares
  especialista-dados    ┘

Revisão de Manuscrito
  revisor-pares ┐
                ├→ redator-cientifico
  analista-critico ┘

Resposta a Revisores
  revisor-pares ┐
                ├→ redator-cientifico
  analista-critico ┘

Proposta de Fomento
  pesquisador-literatura ┐
                          ├→ analista-critico → redator-cientifico
  metodologista          ┘
```

---

## Requisitos de MCP

Para uso completo das ferramentas de busca, configure os seguintes MCP servers no Claude Code:

- **Consensus** — síntese de literatura científica
- **PubMed** — base de dados biomédica/química

---

## Gerenciar o plugin

```bash
claude plugin list                  # ver status
claude plugin disable nexus         # desativar temporariamente
claude plugin enable nexus          # reativar
claude plugin uninstall nexus       # remover
claude plugin marketplace update nexus-marketplace  # atualizar
```

---

## Atualizar para nova versão

```bash
claude plugin marketplace update nexus-marketplace
claude plugin update nexus
```

---

## Contexto de desenvolvimento

Desenvolvido para pesquisa em **sensores eletroquímicos** com MOFs/ZIFs e impressão 3D (FDM/DIW), laboratório de eletroquímica UFMA. Funciona para qualquer área científica: química, saúde, educação, engenharia, ciências sociais.

---

## Licença

MIT — livre para usar, adaptar e distribuir.
