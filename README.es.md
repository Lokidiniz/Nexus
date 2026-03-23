# NEXUS — Squad de Investigación Académica v2.0

> Sistema de agentes de IA para investigación científica de alto impacto, construido sobre **Claude Code** (Anthropic). Funciona en **PT-BR · EN · ES**.

[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0-blue)]()

---

## ¿Qué es NEXUS?

**NEXUS** es un sistema de 6 agentes de IA especializados que corre dentro de Claude Code para asistir investigadores en todas las etapas de la producción científica:

| Agente | Nombre técnico | Especialidad |
|--------|---------------|-------------|
| Investigador de Literatura | `literature-researcher` | Búsqueda sistemática, estado del arte |
| Metodólogo | `methodologist` | Diseño de investigación, muestreo, ética |
| Analista Crítico | `critical-analyst` | Rigor metodológico, brechas, argumentación |
| Redactor Científico | `scientific-writer` | Redacción IMRAD, APA/Vancouver, cover letter, rebuttal |
| Revisor de Pares | `peer-reviewer` | Pre-revisión simulando cualquier revista |
| Especialista en Datos | `data-specialist` | Análisis cuanti/cuali, LOD/LOQ, figuras |

**NEXUS** es el coordinador que orquesta a todos ellos.

---

## ¿Por qué usarlo?

- **Gratuito** — funciona con Claude Code (plan gratuito)
- **Multi-área** — química, salud, educación, ciencias sociales, ingeniería, derecho
- **Multilingüe** — responde en PT-BR, EN o ES automáticamente
- **Revistas latinoamericanas** — conoce CONACYT, CONICET, SciELO, REDALYC
- **Pipelines listos** — revisión sistemática, manuscrito completo, tesis, póster, rebuttal, propuesta de financiamiento

---

## Instalación

### Prerrequisito
[Claude Code](https://claude.ai/code) instalado y configurado.

### Instalación automática (Linux/macOS/WSL)
```bash
curl -fsSL https://raw.githubusercontent.com/TU_USUARIO/nexus-squad/main/install.sh | bash
```

### Instalación automática (Windows PowerShell)
```powershell
irm https://raw.githubusercontent.com/TU_USUARIO/nexus-squad/main/install.ps1 | iex
```

### Instalación manual
```bash
git clone https://github.com/TU_USUARIO/nexus-squad.git
cd nexus-squad
cp agents/*.md ~/.claude/agents/
cp -r skills/* ~/.claude/skills/
```

---

## Cómo usar

### Activar NEXUS en español
En Claude Code, usa el skill `/nexus-es`:
```
/nexus-es Necesito una revisión sistemática sobre sensores electroquímicos con MOFs
```

```
/nexus-es Redactar la sección de Introducción para Sensors & Actuators B
```

```
/nexus-es Revisar mi manuscrito como revisor de la Revista Mexicana de Física
```

```
/nexus-es Propuesta de investigación para CONACYT — sensores para seguridad alimentaria
```

### Pipelines disponibles

| Tarea | Agentes | Tiempo est. |
|-------|---------|-------------|
| Revisión de literatura | literature-researcher → critical-analyst → scientific-writer | ~5 min |
| Manuscrito completo | 6 agentes en secuencia | ~15 min |
| Análisis de datos | data-specialist → critical-analyst | ~3 min |
| Pre-revisión | peer-reviewer + critical-analyst | ~5 min |
| Propuesta de financiamiento | literature-researcher + methodologist → scientific-writer | ~10 min |
| Capítulo de tesis | literature-researcher → scientific-writer → critical-analyst | ~8 min |
| Póster científico | data-specialist → scientific-writer | ~3 min |
| Rebuttal | peer-reviewer + critical-analyst → scientific-writer | ~5 min |

---

## Contribución

¡Los pull requests son bienvenidos! Para contribuir:
1. Fork del repositorio
2. Crea una rama: `git checkout -b feature/nuevo-pipeline`
3. Commit: `git commit -m 'Add: pipeline para artículos de derecho'`
4. Push: `git push origin feature/nuevo-pipeline`
5. Abre un Pull Request

---

## Licencia

MIT — uso libre, incluso comercial. Da crédito.

---

## Otros idiomas

- [README em Português](README.md)
- [English README](README.en.md)

---

*Desarrollado con Claude Code + Anthropic API*
