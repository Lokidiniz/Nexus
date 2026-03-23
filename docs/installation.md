# Instalação

## Pré-requisito

[Claude Code](https://claude.ai/code) instalado e configurado. O NEXUS funciona como uma extensão do Claude Code — não substitui, amplifica.

---

## Opção 1 — npm (recomendada)

```bash
npx nexus-research init
```

O instalador:

- Baixa todos os arquivos do repositório oficial
- Instala agentes em `~/.claude/agents/` automaticamente
- Copia `CLAUDE.md` para ativação global
- Não requer dependências — Node.js puro

**Flags disponíveis:**

```bash
npx nexus-research init --force    # sobrescreve arquivos existentes
npx nexus-research init --yes      # pula confirmação
npx nexus-research init --global   # instala apenas globalmente
npx nexus-research init --no-hooks # sem hooks Python
```

---

## Opção 2 — Script automático

=== "Linux / macOS / WSL"
    ```bash
    curl -fsSL https://raw.githubusercontent.com/Lokidiniz/Nexus/main/install.sh | bash
    ```

=== "Windows PowerShell"
    ```powershell
    irm https://raw.githubusercontent.com/Lokidiniz/Nexus/main/install.ps1 | iex
    ```

---

## Opção 3 — Manual (git clone)

```bash
git clone https://github.com/Lokidiniz/Nexus.git nexus-squad
cd nexus-squad

# Agentes (globais — disponíveis em qualquer projeto)
cp agents/*.md ~/.claude/agents/

# Skills
cp -r skills/* ~/.claude/skills/

# Ativação global
cp .claude/CLAUDE.md ~/.claude/CLAUDE.md
```

---

## Verificando a instalação

Abra qualquer projeto no Claude Code e digite:

```
*help
```

Se o NEXUS estiver ativo, você verá o menu de comandos completo.

---

## Ativar em um projeto específico

Copie o arquivo de ativação para a raiz do seu projeto:

```bash
cp /caminho/para/nexus-squad/CLAUDE.md meu-projeto/.claude/CLAUDE.md
```

Isso ativa o NEXUS especificamente nesse projeto, com contexto de project preenchível:

```yaml
project:
  title: "Meu projeto"
  field: "chemistry"
  target_journal: "Electrochimica Acta"
  stage: "draft"
  language: "pt-br"
```

---

## Suporte multi-IDE

| IDE | O que instalar | Comando |
|-----|---------------|---------|
| **Claude Code** | `~/.claude/agents/*.md` | Automático |
| **Cursor** | `.cursor/rules/nexus.mdc` | Incluído no clone |
| **Gemini CLI** | `.gemini/GEMINI.md` | Incluído no clone |

Para sincronizar manualmente após atualizações:

```bash
bash sync-ide.sh
bash sync-ide.sh --force   # sobrescreve
```
