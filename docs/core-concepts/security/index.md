# 🔐 Security

Security in Kramerius is based on two independent concepts:

- **Authentication** – determining who the user is.
- **Authorization** – determining what the user is allowed to do.

Authentication is delegated to an external identity provider, typically Keycloak, using OAuth 2.0 and OpenID Connect.

Authorization is performed by Kramerius itself. Access decisions are based on a combination of roles, actions, and criteria.

## Security Model

```text
User
  ↓
Role
  ↓
Action
  ↓
Criteria
  ↓
Access Decision
```

A user authenticates through an identity provider and receives one or more roles.

Roles are mapped to actions within Kramerius. Actions represent permissions such as viewing content, modifying metadata, or administering the system.

Additional criteria may be evaluated before access is granted. Criteria can restrict access based on factors such as IP address ranges or licensing conditions.

## Concepts

- [Autentizace](authentication)
- [Autorizace](authorization)
- [Role](roles)
- [Akce](actions)
- [Kriteria](criteria)