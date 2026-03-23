# Contribuindo com o NEXUS

Obrigado por contribuir com o NEXUS Academic Research Framework.

O NEXUS é um sistema open-source de orquestração de IA para pesquisa científica. Contribuições que aumentem o rigor, a cobertura ou a usabilidade são bem-vindas.

---

## Início rápido

```bash
git clone https://github.com/Lokidiniz/Nexus.git
cd Nexus
bash sync-ide.sh    # sincroniza agentes com sua instalação do Claude Code
```

---

## O que você pode contribuir

| Tipo de contribuição | Onde | Observações |
|---|---|---|
| Novo agente | `agents/` + `~/.claude/agents/` | Deve seguir a especificação de agente |
| Novo workflow | `workflows/` | YAML, deve seguir o schema |
| Nova task | `tasks/` | Markdown, deve incluir verificação RDS |
| Novo contexto de time | `teams/` | YAML, constantes específicas do campo |
| Correção de bug | Qualquer arquivo | Descreva o problema no PR |
| Tradução | `README.xx.md` | PT-BR, EN, ES suportados |
| Documentação | `docs/` | Arquitetura, guias, exemplos |
| Exemplo de uso | `examples/` | Walkthrough real por área de pesquisa |

---

## Adicionando um novo agente

1. Crie `agents/[nome].md` com este frontmatter:

```yaml
---
name: nome-do-agente
icon: "🔵"
archetype: "O [Papel]"
description: "Descrição em uma linha. Comandos: *cmd1, *cmd2."
model: sonnet          # haiku | sonnet | opus
color: blue            # blue | green | red | yellow | purple | orange
commands:
  - name: "*cmd1 [arg]"
    description: "O que cmd1 faz"
  - name: "*cmd2"
    description: "O que cmd2 faz"
---
```

2. O corpo deve incluir:
   - `Leia .nexus/activation-pipeline.md e .nexus/constitution.md antes de cada sessão.`
   - Saudação de ativação (veja agentes existentes para o formato)
   - Seção de comando para cada `*comando`
   - Verificação RDS antes de tarefas criativas
   - Autodetecção de idioma ao final

3. Adicione o agente em:
   - `agents/` no repositório
   - Tabela do squad em `.nexus/activation-pipeline.md`
   - Tabela do squad em `.claude/CLAUDE.md`
   - Tabela do squad em `.cursor/rules/nexus.mdc`
   - Tabela do squad em `.gemini/GEMINI.md`
   - Tabela do squad em `agents/nexus.md`

4. Teste: abra um projeto no Claude Code, mencione o agente pelo nome, verifique se ativa corretamente.

---

## Adicionando um novo workflow

Crie `workflows/[nome].yaml` seguindo este schema:

```yaml
name: nome-do-workflow
description: "O que este pipeline entrega"
version: "1.0"

inputs:
  - nome_input: "Descrição do input necessário"

phases:
  - id: 1
    name: nome_fase
    agent: nome-do-agente      # deve corresponder ao nome do arquivo sem .md
    task: nome-da-task         # deve corresponder ao arquivo em tasks/ sem .md
    description: "O que esta fase faz"
    inputs: [nome_input]
    prompt: |
      Instruções exatas para o agente nesta fase.
    output: variavel_saida

quality_gates:
  - "Verificação específica antes da entrega"

deliverables:
  - name: "arquivo_saida.md"
    description: "O que este arquivo contém"

limitations:
  - "O que este pipeline não consegue fazer"
```

---

## Sistema de Decisão de Pesquisa (RDS)

Toda tarefa criativa começa com uma avaliação RDS. Ao escrever tasks, inclua sempre:

```
RDS CHECK — *comando
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REUSE  (≥90%) → aplicar abordagem existente sem modificação
ADAPT  (60–89%) → modificar para o contexto específico
CREATE (<60%) → construir do zero com justificativa explícita
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Conformidade com a Constituição

Todas as contribuições devem respeitar a Constituição do NEXUS (`.nexus/constitution.md`):

- **Sem referências fabricadas** — exemplos usam `[REF NEEDED: descrição]`, nunca `[N]`
- **Sem dados inventados** — templates de task nunca incluem números fictícios como exemplos
- **Autonomia do pesquisador** — agentes propõem, pesquisador decide
- **Transparência** — toda saída declara suas limitações

PRs que violem a constituição não serão aceitos.

---

## Diretrizes de Pull Request

1. **Um assunto por PR** — não misture correções de bug com novos recursos
2. **Teste seu agente** — verifique se o frontmatter é parseado, o agente ativa, os comandos funcionam
3. **Atualize todas as tabelas** — ao adicionar agente/workflow, atualize os quatro arquivos de ativação
4. **Descreva o problema** — qual lacuna esta contribuição preenche?
5. **Rótulo de campo** — adicione: `electrochemistry`, `education`, `health`, `social-sciences`, `core`

---

## Código de Conduta

Este projeto serve à comunidade científica. As contribuições devem:
- Apoiar a integridade da pesquisa (sem atalhos que fabricam resultados)
- Ser inclusivas entre campos, idiomas e instituições
- Citar as fontes originais ao adaptar frameworks existentes

---

*NEXUS Academic Research Framework · Licença MIT · github.com/Lokidiniz/Nexus*
