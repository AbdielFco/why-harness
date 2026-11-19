---
id: order
status: active
verified: none
---
# Order (orden, pedido)

Ejemplo ficticio. Reemplázalo por una entidad real de tu dominio.

## Qué es

Una compra de un [customer](customer.md): uno o más productos, un total y un estado.

## Ciclo de vida

Una orden pasa por `created` -> `paid` -> `shipped` -> `delivered`. Puede pasar a `cancelled` desde `created` o `paid`, nunca después de `shipped`.

Fuente: a verificar (en un proyecto real, `path:line` del enum de estados).

## Reglas

- El total es la suma de las líneas menos descuentos, más impuestos. Los impuestos se calculan sobre el subtotal con descuento.
- Una orden `paid` no cambia sus líneas.

Fuente: a verificar.

## Observaciones

En el código se llama `Order`; en soporte se le dice "pedido". Los dos términos están en el título para que la búsqueda los encuentre.
