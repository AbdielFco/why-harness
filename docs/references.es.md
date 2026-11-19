# Fuentes de referencia

[English](references.md) | **Español**

Fuentes detrás de las decisiones en [decisions/](decisions/). Cada una es una influencia: este repo no afirma implementar esos sistemas. Fechas y URLs revisadas el 2026-11-19.

## Agentes, flujos y el harness

| Fuente | Qué aporta aquí |
|---|---|
| Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 19 dic 2024 | Un flujo con camino fijo rinde mejor que un agente libre para una tarea conocida. Los patrones orchestrator-workers y evaluator-optimizer son el pipeline: planner, implementer, validator y reviewer, con un punto de aprobación humana. |
| Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents), 26 nov 2025 | Una sesión nueva no tiene memoria, así que el estado vive en disco. Su inicializador escribe un `init.sh` y un archivo de progreso; la sesión siguiente los lee y hace un solo incremento. Eso es `scripts/init.sh`, `docs/work/` y la regla de cambiar de sesión. |
| Anthropic, [Harness design for long-running apps](https://www.anthropic.com/research/harness-design-long-running-apps), 24 mar 2026 | Separa planificar, generar y evaluar para que un error de especificación no se propague en silencio. La misma razón por la que planner y reviewer son de solo lectura, y el validator es una etapa distinta del reviewer. |

## El contexto como presupuesto

| Fuente | Qué aporta aquí |
|---|---|
| Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), 2025 | El conjunto más pequeño de tokens con señal. Recuperación justo a tiempo por identificador, en vez de cargar el corpus. Notas fuera de la ventana para lo que tiene que sobrevivir a la compactación. Eso es `AGENTS.md`, la búsqueda `path:line`, las skills y el work file. |
| Nelson F. Liu et al., [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172), TACL 2024 (arXiv:2307.03172, 2023) | La precisión baja cuando el dato relevante queda en el medio de una entrada larga. Razón para devolver una sección y no un archivo, y para mantener corto lo que siempre va cargado. |

## Recuperación

| Fuente | Qué aporta aquí |
|---|---|
| Stephen Robertson y Hugo Zaragoza, [The Probabilistic Relevance Framework: BM25 and Beyond](https://doi.org/10.1561/1500000019), Foundations and Trends in Information Retrieval 3(4), 333–389, 2009 | El ranking de `scripts/knowledge_index.py`: frecuencia del término, frecuencia inversa en el corpus y normalización por longitud. En memoria y sin dependencias a propósito; el tradeoff está en el [ADR 0004](decisions/0004-in-memory-bm25-over-embeddings.es.md). |

## Convenciones y cumplimiento

| Fuente | Qué aporta aquí |
|---|---|
| [AGENTS.md](https://agents.md/), a cargo de la Agentic AI Foundation bajo la Linux Foundation | El archivo abierto y neutral para las instrucciones del proyecto. Es el punto de entrada para que las mismas reglas sirvan en Cursor, Claude Code y opencode. Ver [portability](concepts/portability.es.md). |
| Cursor, [Hooks](https://cursor.com/docs/hooks) | `beforeShellExecution` recibe el comando por stdin y responde `allow`, `ask` o `deny`. `failClosed: true` bloquea el comando si el script falla. Eso es `.cursor/hooks.json` y `gates.py`. |
| Jerome H. Saltzer y Michael D. Schroeder, [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939), Proceedings of the IEEE 63(9), 1975 | Defaults a prueba de fallos: una decisión que no se puede tomar se niega. El hook niega un payload que no puede leer. Ver [ADR 0003](decisions/0003-fail-closed-shell-hook.es.md). |
