---
id: customer
status: active
verified: none
---
# Customer (cliente)

Ejemplo ficticio. Reemplázalo por una entidad real de tu dominio.

## Qué es

Quien compra. Tiene cero o más [orders](order.md).

## Identidad

Se identifica por email, único y en minúsculas. Un cambio de email no crea un customer nuevo.

Fuente: a verificar (en un proyecto real, `path:line` del índice único).

## Observaciones

Un customer sin órdenes no se borra automáticamente.
