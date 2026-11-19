---
id: customer
status: active
verified: none
---
# Customer (cliente)

Fictional example. Replace it with a real entity from your domain.

## What it is

Whoever buys. A customer has zero or more [orders](order.md).

## Identity

Identified by email, unique and lowercase. Changing the email does not create a new customer.

Source: unverified (in a real project, the `path:line` of the unique index).

## Notes

A customer with no orders is not deleted automatically.
