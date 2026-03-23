---
description: "Pipeline completo de manuscrito via NEXUS squad. Uso: /manuscrito [tema] --periodico [nome] --idioma [pt|en]"
argument-hint: "[tema] --periodico [nome] --idioma [pt|en]"
---

Use o agente `nexus` para executar o pipeline completo de manuscrito com base em: $ARGUMENTS

O NEXUS deve:
1. Apresentar o briefing da missão e confirmar o pipeline antes de executar
2. Acionar `pesquisador-literatura` + `especialista-dados` em paralelo
3. Acionar `analista-critico` para validar novidade
4. Acionar `redator-cientifico` para redigir o manuscrito IMRAD completo
5. Acionar `revisor-pares` para pré-revisão simulando o periódico alvo
6. Entregar versão final com cover letter

Se `--periodico` não for informado, perguntar antes de iniciar.
Se `--idioma` não for informado, usar inglês (EN) como padrão.
