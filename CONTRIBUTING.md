# Contributing to NEXUS

Thank you for contributing to the NEXUS Academic Research Framework.

NEXUS is an open-source AI orchestration system for scientific research. Contributions that increase rigor, coverage, or usability are welcome.

---

## Quick Start

```bash
git clone https://github.com/Lokidiniz/Nexus.git
cd Nexus
bash sync-ide.sh    # sync agents to your Claude Code installation
```

---

## What You Can Contribute

| Contribution type | Where | Notes |
|---|---|---|
| New agent | `agents/` + `~/.claude/agents/` | Must follow agent spec |
| New workflow | `workflows/` | YAML, must match schema |
| New task | `tasks/` | Markdown, must include RDS check |
| New team context | `teams/` | YAML, field-specific constants |
| Bug fix | Any file | Describe the problem in the PR |
| Translation | `README.xx.md` | PT-BR, EN, ES supported |
| Docs | `docs/` | Architecture, guides, examples |

---

## Adding a New Agent

1. Create `agents/[name].md` with this frontmatter:

```yaml
---
name: agent-name
icon: "🔵"
archetype: "The [Role]"
description: "One-line description for agent selector. Commands: *cmd1, *cmd2."
model: sonnet          # haiku | sonnet | opus
color: blue            # blue | green | red | yellow | purple | orange
commands:
  - name: "*cmd1 [arg]"
    description: "What cmd1 does"
  - name: "*cmd2"
    description: "What cmd2 does"
---
```

2. Body must include:
   - `Read .nexus/activation-pipeline.md and .nexus/constitution.md before every session.`
   - Activation greeting (see existing agents for format)
   - Command section for each `*command`
   - RDS check before creative tasks
   - Language auto-detection at the end

3. Add the agent to:
   - `agents/` in the repository
   - The squad table in `.nexus/activation-pipeline.md`
   - The squad table in `.claude/CLAUDE.md`
   - The squad table in `.cursor/rules/nexus.mdc`
   - The squad table in `.gemini/GEMINI.md`
   - The squad table in `agents/nexus.md`

4. Test: open a project in Claude Code, mention the agent by name, verify it activates correctly.

---

## Adding a New Workflow

Create `workflows/[name].yaml` following this schema:

```yaml
name: workflow-name
description: "What this pipeline delivers"
version: "1.0"

inputs:
  - input_name: "Description of required input"

phases:
  - id: 1
    name: phase_name
    agent: agent-name          # must match agent filename without .md
    task: task-name            # must match tasks/ filename without .md
    description: "What this phase does"
    inputs: [input_name]
    prompt: |
      Exact instructions for the agent in this phase.
    output: output_variable

  - id: 2
    name: parallel_phase_a
    parallel_group: A          # phases with same group letter run simultaneously
    depends_on: [1]
    agent: another-agent
    ...

quality_gates:
  - "Specific thing to verify before delivery"

deliverables:
  - name: "output_filename.md"
    description: "What this file contains"

limitations:
  - "What this pipeline cannot do"
```

Add the workflow name to:
- `CLAUDE.md` (workflows section)
- `.cursor/rules/nexus.mdc`
- `.gemini/GEMINI.md`
- `agents/nexus.md` (available workflows list)

---

## Adding a New Task

Create `tasks/[name].md` with:

1. **Header**: task name, agent, command
2. **RDS Check**: example RDS evaluation for this task type
3. **Execution Steps**: for each mode (yolo / interactive / pre-flight)
4. **Output Format**: exact template the agent should use
5. **Reference material**: quick-reference tables, checklists, examples

Task files are loaded by agents as context. Keep them concise and structured.

---

## Adding a New Team

Create `teams/team-[field].yaml`:

```yaml
name: "team-field"
display_name: "Field Name"
description: "When to use this team context"

context:
  field: "field name"
  dominant_paradigm: "..."
  key_methods: [method1, method2]
  common_journals: [journal1, journal2]
  citation_style: "APA / Vancouver / ABNT / IEEE"
  language_default: "pt-br / en"

constants:
  key_name: "value used across agents in this team"

journal_profiles:
  - name: "Journal Name"
    impact: "IF or Qualis"
    focus: "scope description"
    key_requirements: [requirement1, requirement2]

constitution_notes:
  - "Field-specific note about data integrity or reporting standards"
```

---

## Constitution Compliance

All contributions must comply with the NEXUS Constitution (`.nexus/constitution.md`):

- **No fabricated references** — examples use `[REF NEEDED: description]`, never `[N]`
- **No invented data** — task templates never include made-up numbers as examples
- **Researcher autonomy** — agents propose, researcher decides
- **Transparency** — every output declares its limitations

PRs that violate the constitution will not be merged.

---

## Pull Request Guidelines

1. **One concern per PR** — don't mix bug fixes with new features
2. **Test your agent** — verify the frontmatter parses, the agent activates, commands work
3. **Update all tables** — if adding an agent/workflow, update all four activation files
4. **Describe the problem** — what gap does this contribution fill?
5. **Field label** — add a label: `electrochemistry`, `education`, `health`, `social-sciences`, `core`

---

## Code of Conduct

This project serves the scientific community. Contributions must:
- Support research integrity (no shortcuts that fabricate results)
- Be inclusive across research fields, languages, and institutions
- Cite original sources when adapting existing frameworks

---

*NEXUS Academic Research Framework · MIT License · github.com/Lokidiniz/Nexus*
