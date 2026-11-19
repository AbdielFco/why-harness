# AGENTS.md

[English](AGENTS.md) | **Español**

Punto de entrada de cada sesión. Mantenlo corto: enlaza, no copies.
Los títulos se quedan en inglés: los agentes los buscan así. El archivo que ejecutan es `AGENTS.md`.

<!-- PROJECT: un párrafo. Qué hace el proyecto y dónde vive su estado. -->
`why-harness` es una plantilla genérica de harness de IA. Su código son dos scripts de la stdlib y sus tests.
<!-- /PROJECT -->

## Start here

1. Corre `./scripts/init.sh`. Un `[FAIL]` detiene la sesión.
2. Con ticket, lee `docs/work/<TICKET>.md`. Si no existe, créalo desde `docs/work/0000-template.md`. Sin ticket, usa un slug en kebab-case.
3. Índice de docs: `docs/README.md`.
4. Busca un hecho por `id:` bajo `docs/knowledge/`. Sin nombre exacto: `python3 -m scripts.knowledge_index search "<query>"`. Lee solo el fragmento en el `path:line` que devuelve.

## Commands

<!-- PROJECT: los comandos exactos. Los agentes los leen de aquí y no los adivinan. -->
| Purpose | Command |
|---|---|
| Session check | `./scripts/init.sh` |
| Full test suite | `python3 -m unittest discover tests` |
| Single test | `python3 -m unittest tests.<module>` |
| Lint | none |
| Knowledge search | `python3 -m scripts.knowledge_index search "<query>"` |
<!-- /PROJECT -->

## Lanes

- **Fast lane**: docs, typos, comentarios, config sin lógica. La sesión principal edita y después corre el `reviewer`. Sin plan y sin test.
- **Normal lane**: cualquier cambio de lógica, comportamiento o interfaz. Pipeline completo.

Ante la duda, carril normal.

## Pipeline (normal lane)

`planner` -> aprobación humana -> `test-writer` -> `implementer` -> `validator` -> `reviewer`.

Los agentes viven en `.cursor/agents/`. Cada uno devuelve `PASS` o `FAIL` con: qué está mal, qué está incompleto, sugerencias y el context gap (`AGENTS.md`, una skill o `docs/knowledge/`).

Un `FAIL` vuelve a la etapa que falló. Un `FAIL` de `validator` o `reviewer` vuelve a `implementer`. Commit solo con una orden explícita, y solo después de que el reviewer devuelva `PASS`.

## Human gates

<!-- PROJECT: acciones que necesitan un sí explícito. Refleja las de shell en .cursor/hooks/gates.py. -->
Necesitan un sí explícito: commit, push, borrar archivos o datos, agregar o quitar una dependencia, cualquier deploy, editar secretos o permisos, editar `.cursor/hooks/`.
<!-- /PROJECT -->

`.cursor/hooks/gates.py` aplica la parte de shell. No ve una edición de archivo ni una escritura dentro de un proceso en ejecución. Esas siguen esperando un sí.

## Code rules

<!-- PROJECT: de tres a seis reglas, o un puntero a la skill que las tiene. -->
- Solo stdlib. Ninguna dependencia nueva.
- Sin `except` desnudo. Los errores van a stderr con un prefijo; stdout es el resultado del comando.
- Cada cambio de script tiene un test en `tests/`.
<!-- /PROJECT -->

No leas `.env` ni archivos de credenciales. Los nombres de variables viven en `.env.example`.

## Memory

| Type | Lives in | Lasts |
|---|---|---|
| Task | `docs/work/<TICKET>.md` | hasta cerrar la tarea |
| Decision (why) | `docs/decisions/` | permanente |
| Fact (what) | `docs/knowledge/` | permanente |

La sesión principal es la única que escribe `docs/work/<TICKET>.md`. Los subagentes devuelven reportes y no lo escriben.

Cambia de sesión al terminar cada fase (Plan, Implement, Verify), o antes si la sesión repite una pregunta ya respondida en el work file, contradice un hecho registrado, recibe dos correcciones o lee más de 10 archivos sin escribir. La sesión nueva lee `AGENTS.md`, el work file y sigue desde "Remaining".

## Closing a task

1. Aplica cada entrada de "Context gaps" del work file a su capa (`AGENTS.md`, skill o knowledge).
2. Agrega un archivo de decisión cuando la tarea tomó una decisión que el código no muestra.
3. Pon el resumen en el PR y borra `docs/work/<TICKET>.md`.
