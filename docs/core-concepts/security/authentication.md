# Authentication

Authentication answers the question:

> Who is the current user?

Kramerius does not manage user identities directly. Instead, it relies on an external Identity Provider (IdP), typically Keycloak.

After successful login, the Identity Provider issues a security token containing information about the authenticated user.

## Authentication Result

The result of authentication is an authenticated identity represented by:

- User identifier
- Username
- Assigned roles
- Additional identity attributes

The authenticated identity is attached to every request and becomes the input for authorization.

## Related Topics

- [Authorization](../authorization/)
- [Security Architecture](../../../architecture/security/)
- [Authentication Reference](../../../reference/security/authentication/)