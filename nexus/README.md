# NEXUS Squad — Plugin para Claude Code

Squad de pesquisa acadêmica com 7 agentes especializados, coordenados pelo **NEXUS**. Cobre todo o ciclo de vida de um manuscrito científico: busca de literatura → análise crítica → redação → revisão por pares.

## Instalação

```bash
claude plugin install /caminho/para/nexus-squad
```

Ou diretamente de um repositório Git:

```bash
claude plugin install https://github.com/seu-usuario/nexus-squad
```

## Agentes incluídos

| Agente | Função |
|--------|--------|
| `nexus` | Coordenador do squad — orquestra o pipeline completo |
| `pesquisador-literatura` | Busca sistemática com Consensus + PubMed + WebSearch |
| `analista-critico` | Avaliação de rigor metodológico e novidade científica |
| `redator-cientifico` | Redação IMRAD para qualquer periódico, PT-BR ou EN |
| `revisor-pares` | Pré-revisão simulando o periódico alvo |
| `especialista-dados` | Análise de dados, LOD/LOQ, figuras, estatística |
| `metodologista` | Design de pesquisa, amostragem, instrumentos |

## Skills incluídas

| Skill | Uso |
|-------|-----|
| `/pesquisa [tema]` | Busca artigos no Consensus e sintetiza evidências |
| `/texto-cientifico [seção]` | Redige seções de artigos, TCC, dissertação |

## Como usar

### Tarefa simples (1 skill)
```
/pesquisa ZIF-67 sensores eletroquímicos antibióticos
```

### Pipeline completo (via NEXUS)
```
Preciso da Introdução para um artigo sobre eletrodos FDM+ZIF-67
para detecção de tetraciclina no Sensors and Actuators B
```
O NEXUS acionará automaticamente: `pesquisador-literatura` → `analista-critico` → `redator-cientifico`

### Revisão de manuscrito
```
Revisa meu rascunho antes de submeter para o Electrochimica Acta
```
O NEXUS acionará: `revisor-pares` + `analista-critico` (paralelo) → `redator-cientifico`

## Exemplos de pipelines disponíveis

- **Revisão sistemática de literatura**
- **Manuscrito completo do zero**
- **Análise de dados (LOD, LOQ, DPV, CV)**
- **Resposta a revisores (Rebuttal)**
- **Proposta de fomento (CNPq, CAPES, FAPEMA)**
- **Design de novo projeto de pesquisa**

## Requisitos de MCP

Para uso completo, os seguintes MCP servers são recomendados:
- `Consensus` — busca de literatura científica
- `PubMed` — busca e metadados de artigos biomédicos/químicos

## Contexto de desenvolvimento

Desenvolvido para pesquisa em sensores eletroquímicos com MOFs/ZIFs e impressão 3D (FDM), laboratório de eletroquímica UFMA. Funciona para qualquer área científica.

## Versão

1.0.0
