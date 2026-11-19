# Skills

## Qué es

Una **skill** es un archivo `SKILL.md` en `.cursor/skills/<nombre>/` con dos partes:

- **frontmatter** con `name` y `description`. La `description` está **siempre** en contexto: es el disparador.
- **cuerpo** con el conocimiento operativo: patrones, layout, errores típicos. Se lee **solo** cuando la `description` coincide con la tarea.

Esto es **divulgación progresiva**: el agente sabe que algo existe por una línea, y paga el resto solo cuando lo necesita.

## Por qué existe

La alternativa es poner todo en `AGENTS.md`. Con diez áreas de código, cada una con sus reglas, `AGENTS.md` crece a cientos de líneas que se pagan en cada turno aunque la tarea toque una sola área.

| | Todo en AGENTS.md | Skills |
|---|---|---|
| Coste por turno | Todas las reglas | Una `description` por skill |
| Coste cuando se usa | Igual | Más el cuerpo de una skill |
| Escala con | Número de áreas, lineal y siempre | Número de áreas tocadas |

## Cómo funciona aquí

`.cursor/skills/example/SKILL.md` es la plantilla. Los agentes la usan así:

1. El planner lee la skill cuya `description` coincide con el cambio y la nombra en el plan.
2. El test-writer y el implementer leen la skill que el plan nombra.
3. Si una skill confundió o le faltó una sección, el reporte lo dice en "Context gap: skill".

## Qué va en una skill y qué no

| Va en la skill | Va en otro lado |
|---|---|
| Cómo se estructura un módulo aquí | Qué significa un dato del dominio -> knowledge |
| Patrón de errores y logging | Comandos de test y build -> `AGENTS.md` |
| Errores típicos y cómo evitarlos | Por qué se decidió algo -> decisions |

## Escribir una buena description

- Empieza con "Use when" y nombra un disparador concreto: una ruta, un tipo de archivo, una acción.
- Di en una frase qué cubre el cuerpo, para que el agente decida sin abrirlo.
- Una skill por área. Una skill que se dispara con todo cuesta tokens en todo.

Mala: `description: Coding guidelines.`
Buena: `description: Use when adding or changing an HTTP endpoint under api/. Covers routing, input validation, error responses and where the test goes.`

## Coste en contexto

Una `description` cuesta entre 30 y 60 tokens por turno. El cuerpo, solo cuando se usa.

## Límites

- La coincidencia la decide el modelo. Una `description` ambigua puede dispararse de más o de menos.
- Una skill no es obligatoria. Si una regla no puede fallar, va al hook o a un test.

## Cómo adaptarlo

Borra `example/` y crea una skill por área de código de tu proyecto. Empieza con una sola: la del área que más se toca.
