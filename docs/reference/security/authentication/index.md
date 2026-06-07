# Authentication

Kramerius používá OAuth 2.0 Access Token ve formátu JWT.

## Supported Standards

- OAuth 2.0
- OpenID Connect
- JWT

## Token Sources

Kramerius očekává token v hlavičce:

```http
Authorization: Bearer <token>
```

## Required Claims

| Claim | Description |
|---------|---------|
| sub | User identifier |
| preferred_username | Username |
| realm_access.roles | Assigned roles |

## User Principal

Po úspěšné validaci tokenu vzniká interní reprezentace uživatele.

### Attributes

| Attribute | Source |
|------------|------------|
| id | sub |
| username | preferred_username |
| roles | realm_access.roles |

## Authentication Errors

| Error | Description |
|--------|--------|
| Invalid token | Token cannot be validated |
| Expired token | Token expired |
| Missing token | No token provided |