# Agentes y subagentes

## Qué es

- **Agente principal (orquestador):** la sesión con la que habla el humano. No tiene un archivo propio; su contrato es `AGENTS.md`.
- **Subagente:** una instancia del modelo con su propia ventana de contexto, un rol y un permiso concretos, definida en `.cursor/agents/<nombre>.md`. Recibe una entrada, trabaja aislado y devuelve un reporte.

## Por qué existe

Un solo agente que planifica, escribe tests, implementa y revisa tiene dos problemas:

1. **Contexto.** Al revisar, carga toda la historia de la implementación: los intentos fallidos, las lecturas, los errores. Su ventana está llena y sesgada.
2. **Sesgo de autor.** Quien escribió el código lo revisa con la intención en la cabeza, no con lo que el diff dice.

Separar en subagentes resuelve las dos cosas: cada uno empieza limpio y tiene un solo trabajo.

## El sentido de cada agente

Cada agente existe porque separa una responsabilidad que, mezclada con otra, produce un sesgo concreto.

| Agente | Permiso | Hace | Separa | Sesgo que evita |
|---|---|---|---|---|
| **planner** | readonly | Localiza, lee, propone archivos, test, reuso, gates, riesgos | Entender de hacer | Editar antes de entender |
| **test-writer** | solo tests | Escribe un test que falla por la razón del plan | Especificar de implementar | Un test que confirma la implementación en vez de la intención |
| **implementer** | archivos del plan | Cambio mínimo que pone el test en verde | Implementar de ampliar alcance | El "ya que estoy" |
| **validator** | ejecuta, no edita | Suite completa y chequeo de aceptación | Evidencia dinámica de opinión | "Debería funcionar" |
| **reviewer** | readonly | Contrasta el diff con el plan | Juzgar de haber escrito | Revisar la intención y no el diff |
| **orquestador** | todo, con gates | Junta reportes, escribe la memoria, aplica context gaps | Coordinar de ejecutar | Estados contradictorios entre subagentes |

### Por qué validator y reviewer no se fusionan

El validator ejecuta comandos y produce artefactos (reportes de tests, coverage). El reviewer solo lee el diff. Si se fusionan, el revisor arrastra la salida de los tests y pierde el contexto limpio, que es justo lo que lo hace útil.

### Por qué test-writer e implementer no se fusionan

Si el mismo agente escribe el test y el código, el test tiende a describir lo que el código hace. Separados, el test describe lo que el plan pide, y el implementer no puede tocarlo: si el test está mal, devuelve `FAIL` y lo dice.

### Por qué planner y reviewer son readonly

Un agente que no puede editar no tiene la tentación de "arreglarlo rápido". El planner tiene que entender; el reviewer tiene que juzgar. Ninguno de los dos trabajos mejora con permiso de escritura.

## Cómo funciona aquí: el contrato del reporte

Los cinco devuelven la misma estructura:

```markdown
## Verdict: PASS | FAIL
## Gate              checklist propio de cada agente
## What is wrong
## What is incomplete
## Suggestions
## Context gap       AGENTS.md | skill | knowledge
```

- **Verdict** binario: no hay "PASS con observaciones". O cumple el gate o no.
- **Gate:** un checklist verificable. Evita que el agente se califique por impresión.
- **Context gap:** qué le faltó para cumplir y en qué capa debería estar. Ver [feedback-loop](feedback-loop.md).

El contrato va inline en cada agente y no en un archivo compartido: un subagente no hereda archivos, y un include costaría una lectura extra en cada invocación.

### Los agentes son invariantes

Ningún agente nombra un lenguaje, un framework ni un dominio. Leen los comandos de `AGENTS.md`, el cómo de la skill que coincida y los hechos de `docs/knowledge/`. Al instalar el harness en otro proyecto, los agentes se copian sin cambios.

## Coste en contexto

Invocar un subagente cuesta su prompt (~40 líneas) más la entrada. A cambio, todo lo que lee queda fuera de la sesión principal, que solo recibe el reporte. En una tarea normal, el planner puede leer 10 archivos y devolver 30 líneas.

## Límites

- `readonly` depende de que la herramienta lo respete. Cursor lo aplica; otras herramientas pueden no hacerlo.
- Cinco etapas para un typo es desperdicio. Por eso existe el carril rápido ([pipeline-and-lanes](pipeline-and-lanes.md)).
- Los subagentes no comparten memoria entre sí. Todo lo que uno necesita del otro pasa por el orquestador.

## Cómo adaptarlo

No edites los agentes. Si un agente falla por algo propio del proyecto, eso es un context gap: va a `AGENTS.md`, a una skill o a la knowledge.
