# Contribuyendo con NEXUS

Gracias por contribuir con el NEXUS Academic Research Framework.

NEXUS es un sistema open-source de orquestación de IA para investigación científica. Se aceptan contribuciones que aumenten el rigor, la cobertura o la usabilidad.

---

## Inicio rápido

```bash
git clone https://github.com/Lokidiniz/Nexus.git
cd Nexus
bash sync-ide.sh    # sincroniza agentes con tu instalación de Claude Code
```

---

## Qué puedes contribuir

| Tipo de contribución | Dónde | Notas |
|---|---|---|
| Nuevo agente | `agents/` + `~/.claude/agents/` | Debe seguir la especificación |
| Nuevo workflow | `workflows/` | YAML, debe seguir el schema |
| Nueva task | `tasks/` | Markdown, debe incluir verificación RDS |
| Nuevo contexto de equipo | `teams/` | YAML, constantes específicas del área |
| Corrección de bug | Cualquier archivo | Describe el problema en el PR |
| Traducción | `README.xx.md` | PT-BR, EN, ES soportados |
| Documentación | `docs/` | Arquitectura, guías, ejemplos |
| Ejemplo de uso | `examples/` | Walkthrough real por área de investigación |

---

## Agregando un nuevo agente

1. Crea `agents/[nombre].md` con este frontmatter:

```yaml
---
name: nombre-agente
icon: "🔵"
archetype: "El [Rol]"
description: "Descripción en una línea. Comandos: *cmd1, *cmd2."
model: sonnet          # haiku | sonnet | opus
color: blue
commands:
  - name: "*cmd1 [arg]"
    description: "Qué hace cmd1"
---
```

2. El cuerpo debe incluir:
   - `Lee .nexus/activation-pipeline.md y .nexus/constitution.md antes de cada sesión.`
   - Saludo de activación
   - Sección de comandos
   - Verificación RDS antes de tareas creativas
   - Autodetección de idioma al final

3. Agrega el agente en los cuatro archivos de activación:
   - `.nexus/activation-pipeline.md`
   - `.claude/CLAUDE.md`
   - `.cursor/rules/nexus.mdc`
   - `.gemini/GEMINI.md`
   - `agents/nexus.md`

---

## Sistema de Decisión de Investigación (RDS)

Cada tarea creativa comienza con una evaluación RDS:

```
REUSE  (≥90%) → aplicar enfoque existente sin modificación
ADAPT  (60–89%) → modificar para el contexto específico
CREATE (<60%) → construir desde cero con justificación explícita
```

---

## Cumplimiento de la Constitución

Todas las contribuciones deben cumplir la Constitución de NEXUS (`.nexus/constitution.md`):

- **Sin referencias fabricadas** — usar `[REF NEEDED: descripción]`, nunca `[N]`
- **Sin datos inventados** — las plantillas nunca incluyen números ficticios como ejemplos
- **Autonomía del investigador** — los agentes proponen, el investigador decide
- **Transparencia** — toda salida declara sus limitaciones

---

## Directrices para Pull Request

1. **Un tema por PR** — no mezcles correcciones de bug con nuevas funcionalidades
2. **Prueba tu agente** — verifica que el frontmatter se parsea y los comandos funcionan
3. **Actualiza todas las tablas** — si agregas agente/workflow, actualiza los cuatro archivos de activación
4. **Describe el problema** — ¿qué brecha llena esta contribución?
5. **Etiqueta de área** — agrega: `electrochemistry`, `education`, `health`, `social-sciences`, `core`

---

## Código de Conducta

Este proyecto sirve a la comunidad científica. Las contribuciones deben:
- Apoyar la integridad de la investigación
- Ser inclusivas entre disciplinas, idiomas e instituciones
- Citar las fuentes originales al adaptar frameworks existentes

---

*NEXUS Academic Research Framework · Licencia MIT · github.com/Lokidiniz/Nexus*
