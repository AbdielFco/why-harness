# Harness

[English](harness.md) | **Español**

## Qué es

El **harness** es todo lo que rodea al modelo y que no es el modelo: qué lee al empezar, qué reglas sigue, qué herramientas tiene, qué no puede hacer sin permiso, cómo se verifica su trabajo y dónde guarda lo que aprende.

El término viene de *test harness*: el andamiaje que ejecuta código bajo condiciones controladas y comprueba el resultado. Aquí el código bajo prueba es el comportamiento del agente.

```
agente = modelo + harness
```

Dos agentes con el mismo modelo y distinto harness rinden distinto. El modelo pone la capacidad; el harness decide cuánto de esa capacidad llega al resultado.

## Por qué existe

Sin harness, un agente de código:

- **Lee de más.** Abre archivos enteros "por si acaso" y llena la ventana de contexto con ruido.
- **Olvida.** Lo que decidió hace 40 mensajes se diluye o se compacta mal.
- **Edita antes de entender.** Puede hacerlo, así que lo hace.
- **Se autoaprueba.** Escribe el código y el test, y el test confirma lo que el código hace, no lo que debía hacer.
- **Cruza límites.** Un `rm`, un `push` o un deploy son un comando más.

Cada pieza de este repo ataca una de esas fallas.

## Cómo se relaciona con otros términos

| Término | Pregunta que responde | Alcance |
|---|---|---|
| Prompt engineering | ¿Cómo redacto esta instrucción? | Un mensaje |
| Context engineering | ¿Qué información entra a la ventana y cuándo? | Una sesión |
| Harness engineering | ¿Qué estructura hace que cualquier sesión salga bien? | El proyecto, todas las sesiones |

El harness contiene a los otros dos: `AGENTS.md` y los agentes son prompts bien redactados; la búsqueda por fragmentos y las skills son context engineering. Lo que añade el harness es lo que **no** depende del modelo: hooks deterministas, `init.sh`, el contrato de reportes y la memoria en disco.

## Cómo funciona aquí

| Falla | Pieza | Doc |
|---|---|---|
| Lee de más | Búsqueda `path:line`, skills a demanda | [knowledge-base](knowledge-base.es.md), [skills](skills.es.md) |
| Olvida | Work file, decisiones, knowledge | [memory-and-sessions](memory-and-sessions.es.md) |
| Edita antes de entender | planner readonly + aprobación humana | [agents-and-subagents](agents-and-subagents.es.md) |
| Se autoaprueba | test-writer separado, reviewer con contexto limpio | [agents-and-subagents](agents-and-subagents.es.md) |
| Cruza límites | Hook `gates.py` | [hooks](hooks.es.md) |
| Repite los mismos errores | Context gap | [feedback-loop](feedback-loop.es.md) |

## Coste en contexto

El harness también consume tokens: `AGENTS.md` y las `description` de las skills están siempre cargados. Por eso `AGENTS.md` se mantiene corto y enlaza en vez de copiar. La regla es que una línea siempre cargada tiene que evitar más tokens de los que cuesta.

## Límites

- El harness no hace más inteligente al modelo. Reduce las formas de fallar.
- Las reglas en markdown son sugerencias para el modelo. Solo el hook y `init.sh` son obligatorios.
- Un harness demasiado grande es su propio problema: cada línea siempre cargada compite con el trabajo real.

## Cómo adaptarlo

No se edita este concepto, se llenan las tres capas del proyecto. Ver [adopt](../adopt.es.md).
