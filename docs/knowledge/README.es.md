# Knowledge base

[English](README.md) | **Español**

Hechos del dominio: qué es cada entidad, de dónde sale cada dato y qué reglas aplican. El código dice *cómo*; esto dice *qué es verdad* y *cómo lo sabemos*.

Por qué existe y cómo se busca: [concepts/knowledge-base](../concepts/knowledge-base.es.md).

## Estructura

```
docs/knowledge/
├── README.md                    formato y lista de colecciones (inglés)
├── README.es.md                 este archivo
└── <coleccion>/<entidad>.md     un archivo por entidad
```

El proyecto elige sus colecciones (`entities/`, `sources/`, `rules/`, ...). Los ejemplos de este repo usan `entities/` con un dominio ficticio de tienda. El cuerpo está en inglés y el título conserva el nombre en español entre paréntesis, para que las dos consultas encuentren el archivo.

## Formato de un archivo

```markdown
---
id: order
status: active
verified: 2026-11-19
---
# Order

## Qué es
## Fuente
## Reglas
## Observaciones
```

### Frontmatter

Plano (`clave: valor`), primero en el archivo. Sin listas ni anidamiento.

| Clave | Obligatoria | Valores |
|---|---|---|
| `id` | sí | Identificador estable, el mismo que usa el código |
| `status` | sí | `active`, `deprecated`, `draft` |
| `verified` | sí | Fecha `AAAA-MM-DD` de la última verificación contra la fuente, o `none` |

El proyecto agrega las claves que necesite (`source`, `owner`, `code`, ...). Un valor que no aplica es `none`.

### Cuerpo

- Una sección `## ` por tema. Cada sección es un fragmento de búsqueda: corta y con un título que diga lo que contiene.
- Todo hecho lleva su fuente: un enlace, una `path:line` o un comando. Lo que no se pudo verificar dice "a verificar".
- Si una entidad tiene dos nombres (en código y en negocio), pon los dos: la búsqueda no entiende sinónimos.

## Buscar

```bash
rg "id: order" docs/knowledge                                  # con id exacto
python3 -m scripts.knowledge_index search "lifecycle" # por relevancia
```

## Colecciones

| Colección | Contiene |
|---|---|
| [entities/](entities/) | Ejemplos: [order](entities/order.md), [customer](entities/customer.md) |
