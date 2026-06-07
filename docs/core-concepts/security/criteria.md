# Criteria

Criteria are additional conditions that must be satisfied before an action is granted.

They provide fine-grained control beyond simple role-based authorization.

## Examples

Typical criteria include:

- Allowed IP ranges
- Licensing conditions
- Collection-specific access restrictions

## Evaluation Model

```text
Role
  ↓
Action
  ↓
Criteria
  ↓
Permit / Deny
```

Even if a role grants an action, access may still be denied if the required criteria are not satisfied.

## Why Criteria Exist

Many library use cases require access rules that cannot be expressed solely through user roles.

For example:

- Access may be allowed only from institutional networks.
- Access may depend on a valid license agreement.
- Access may depend on the requested content.

Criteria make such rules configurable without introducing additional roles.

## Related Topics

- [Authorization](../authorization/)
- [Criteria Reference](../../../reference/security/criteria/)