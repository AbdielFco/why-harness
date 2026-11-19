# Portabilidad entre herramientas

## Qué es

Las piezas del harness son conceptos. Cada herramienta de agentes las ubica en una ruta distinta.

## Por qué existe

El equipo puede usar más de una herramienta, y el harness no debería atarse a una.

## Cómo funciona

| Pieza | Cursor | Claude Code | opencode |
|---|---|---|---|
| Entrada | `AGENTS.md` | `CLAUDE.md` (puede importar `AGENTS.md`) | `AGENTS.md` |
| Subagentes | `.cursor/agents/*.md` | `.claude/agents/*.md` | `.opencode/agent/*.md` |
| Skills | `.cursor/skills/*/SKILL.md` | `.claude/skills/*/SKILL.md` | `.opencode/skills/*/SKILL.md` |
| Hooks | `.cursor/hooks.json` | `.claude/settings.json` (`hooks`) | plugins |
| Fuera del índice | `.cursorignore` | `permissions.deny` | `permission.read` |

`AGENTS.md` es el formato común: varias herramientas lo leen sin configuración. Por eso es la entrada, y no un archivo propio de una herramienta.

La knowledge, la memoria, `init.sh` y `knowledge_index.py` son markdown y scripts: funcionan igual en cualquier herramienta.

## Coste en contexto

Ninguno extra. Solo cambian las rutas.

## Límites

- El protocolo de stdin/stdout de los hooks cambia entre herramientas. `gates.py` sigue el de Cursor; para otra herramienta, `decide()` se reusa y cambia el envoltorio de `main()`.
- `readonly` en subagentes no existe igual en todas. Donde no existe, se reemplaza por restringir sus herramientas.
- Las rutas de esta tabla cambian con las versiones de cada herramienta. Verifícalas en su documentación.

## Cómo adaptarlo

Mantén una sola fuente (los archivos en `.cursor/` o los de la herramienta principal) y enlaza o copia hacia las demás. Dos fuentes editadas a mano se desincronizan.
