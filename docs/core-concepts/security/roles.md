# Roles

Roles represent groups of users with similar responsibilities or permissions.

Roles are managed by the Identity Provider and become available to Kramerius after authentication.

Examples:

- Administrator
- Librarian
- Registered User
- Anonymous User

Roles do not directly grant permissions.

Instead, roles are mapped to actions within Kramerius.

## Role Mapping

```text
Role
  ↓
Action
```

A single role may grant multiple actions.

Multiple roles may grant the same action.

## Related Topics

- [Actions](../actions/)
- [Authorization](../authorization/)