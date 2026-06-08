# Actions

Actions represent permissions understood by Kramerius.

An action describes an operation that may be performed within the system.

Examples include:

- Viewing content
- Editing metadata
- Managing users
- Accessing administration functions

Actions are assigned to roles.

## Why Actions Exist

Actions provide a stable authorization model independent of the external Identity Provider.

Instead of embedding application-specific permissions into Keycloak, Kramerius evaluates actions internally.

## Relationship to Roles

```text
Role
  ↓
Action
```

A role grants one or more actions.

The complete list of available actions is documented in the reference documentation.

## Related Topics

- [Role](roles)
- [Kriteria](criteria)
- [Actions Reference](../../../reference/security/actions/)