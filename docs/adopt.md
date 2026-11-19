# Adoptar el harness en un proyecto

Tiempo estimado: una hora para la base, y después crece con los context gaps.

## 1. Copiar los invariantes

```
.cursor/agents/           los 5 agentes, sin cambios
.cursor/hooks.json
.cursor/hooks/gates.py
scripts/init.sh
scripts/knowledge_index.py
scripts/__init__.py
docs/work/0000-template.md
docs/decisions/0000-template.md
docs/knowledge/README.md
```

Si el proyecto ya tiene `scripts/`, ajusta las rutas en `init.sh` y en `AGENTS.md`. El buscador lee `docs/knowledge/` relativo a la raíz del repo.

Copia también `tests/test_gates.py` y `tests/test_knowledge_index.py` si quieres que la suite del proyecto proteja el harness. Ajusta `test_repo_examples_are_findable` a tu propia knowledge.

## 2. Llenar los bloques editables

| Archivo | Bloque | Qué poner |
|---|---|---|
| `AGENTS.md` | `PROJECT` (4 bloques) | Descripción, comandos exactos, gates humanos, reglas de código |
| `scripts/init.sh` | `PROJECT CONFIG` | `TOOLS`, `TEST_CMD`, `PROJECT_FILES` |
| `.cursor/hooks/gates.py` | `GATES` | Los gates de shell de tu `AGENTS.md` |

Regla: los comandos de `AGENTS.md` y `TEST_CMD` de `init.sh` deben coincidir.

## 3. Crear la primera skill

Una sola, para el área de código que más se toca. Usa `.cursor/skills/example/SKILL.md` como plantilla y bórrala después. Ver [skills](concepts/skills.md).

## 4. Sembrar la knowledge

No documentes todo el dominio de golpe. Empieza con las tres o cuatro entidades que aparecen en casi todas las tareas. El resto llega por context gaps. Ver [knowledge/README](knowledge/README.md).

## 5. Verificar

```bash
./scripts/init.sh
echo '{"command":"git push"}' | python3 .cursor/hooks/gates.py   # debe responder ask
echo 'basura' | python3 .cursor/hooks/gates.py                 # debe responder deny
python3 -m scripts.knowledge_index search "<una entidad tuya>"
```

## 6. Primera tarea

Elige una tarea pequeña de carril normal y recórrela entera. Al cerrar, aplica los context gaps. Las primeras tres tareas son las que más mejoran el harness.

## Qué no hacer

- No editar los agentes para meter reglas del proyecto. Eso es un context gap: va a una capa.
- No crecer `AGENTS.md` con todo. Si una regla aplica a un área, va a su skill.
- No abrir el workspace en una carpeta padre si quieres que el hook funcione: Cursor carga el `hooks.json` del workspace abierto.
