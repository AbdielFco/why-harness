---
id: order
status: active
verified: none
---
# Order (orden, pedido)

Fictional example. Replace it with a real entity from your domain.

## What it is

A purchase by a [customer](customer.md): one or more products, a total, and a state.

## Lifecycle

An order moves through `created`, then `paid`, then `shipped`, then `delivered`. It can move to `cancelled` from `created` or `paid`, and never after `shipped`.

Source: unverified (in a real project, the `path:line` of the state enum).

## Rules

- The total is the sum of the lines, minus discounts, plus tax. Tax is computed on the discounted subtotal.
- A `paid` order does not change its lines.

Source: unverified.

## Notes

The code calls it `Order`. Support calls it "pedido". Both words are in the title so search finds either one.
