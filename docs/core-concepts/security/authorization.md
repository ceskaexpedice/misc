# Authorization

Authorization answers the question:

> Is the authenticated user allowed to perform a specific action?

Authorization is evaluated by Kramerius.

Access decisions are based on:

- Roles
- Actions
- Criteria

## Authorization Model

```text
Authenticated User
        ↓
       Roles
        ↓
      Actions
        ↓
      Criteria
        ↓
 Access Decision
```

A role alone does not grant access.

Instead, roles are associated with actions, and actions may be subject to additional criteria.

## Examples

A user may have a role that allows viewing digital objects.

However, access may still be denied if:

- the request originates from an unauthorized IP address,
- a required license is not available,
- another access criterion is not satisfied.

## Related Topics

- [Roles](../roles/)
- [Actions](../actions/)
- [Criteria](../criteria/)
- [Authorization Reference](../../../reference/security/authorization/)