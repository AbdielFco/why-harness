# Memoria y sesiones

[English](memory-and-sessions.md) | **Español**

## Qué es

La **memoria** es lo que sobrevive a una sesión. Aquí vive en disco, en tres tipos según cuánto dura:

| Tipo | Responde | Dónde | Dura |
|---|---|---|---|
| Tarea | ¿Dónde quedamos? | `docs/work/<TICKET>.md` | Hasta cerrar la tarea |
| Decisión | ¿Por qué es así? | `docs/decisions/NNNN-*.md` | Permanente |
| Hecho | ¿Qué es verdad? | `docs/knowledge/` | Permanente, se actualiza |

## Por qué existe

- **La conversación no es memoria.** Se compacta, se resume, y al abrir otra sesión desaparece.
- **Una sesión larga se degrada.** Acumula intentos fallidos, lecturas irrelevantes y correcciones. A partir de cierto punto es más barato empezar limpio que seguir.
- **Empezar limpio solo funciona si el estado está escrito.** El work file es lo que hace barato cambiar de sesión.

## Cómo funciona aquí

### El work file

Plantilla en [work/0000-template.md](../work/0000-template.es.md): Phase, Goal, Plan, Remaining, Verification, Context gaps, Log.

- Lo crea el orquestador al empezar una tarea.
- **Un solo escritor:** solo el orquestador lo edita. Los subagentes devuelven reportes y el orquestador copia lo relevante. Dos agentes escribiendo el mismo archivo producen estados contradictorios.
- Se borra al cerrar la tarea. Lo que valga la pena conservar pasa a una decisión, a la knowledge o al PR.

### Cuándo cambiar de sesión

Al terminar cada fase (Plan, Implement, Verify), o antes si la sesión:

- repite una pregunta ya respondida en el work file,
- contradice un hecho registrado,
- recibe dos correcciones del humano, o
- lee más de 10 archivos sin escribir nada.

Cada señal indica que el contexto está contaminado o perdido. La sesión nueva lee `AGENTS.md`, el work file y continúa desde "Remaining".

### Por qué no hay carpeta de investigaciones

Una investigación que vale la pena guardar termina siendo un hecho (knowledge) o una decisión (decisions). Una tercera carpeta compite con las otras dos y nadie sabe dónde buscar.

## Coste en contexto

El work file se lee al empezar cada sesión: debe caber en una pantalla. Si crece, lo que no es "Remaining" se resume o se mueve.

## Límites

- El orquestador puede olvidar actualizar el work file. El reviewer lo verifica en su gate.
- Cambiar de sesión lo decide el humano o el agente; el harness solo da las señales.

## Cómo adaptarlo

Usa el id de ticket de tu gestor como nombre del work file. Ajusta las señales de cambio de sesión si tu flujo lo pide.
