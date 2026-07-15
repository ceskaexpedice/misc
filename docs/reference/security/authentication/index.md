[Index](../../../index) / [Reference](../..)  / [Zabezpečení](..)

# Autentizace

Kramerius používá OAuth 2.0 Access Token ve formátu JWT.

## Podporovane standardy

- OAuth 2.0
- OpenID Connect
- JWT

## Token

Kramerius očekává token v hlavičce:

```http
Authorization: Bearer <token>
```

### CDK hlavicka
TODO

### [Token model](token-model)

### [Token lifecycle](token-lifecycle)


## User Principal

Po úspěšné validaci tokenu vzniká interní reprezentace uživatele.

### [Role](../roles)

## Authentication Errors

| Error | Description |
|--------|--------|
| Invalid token | Token cannot be validated |
| Expired token | Token expired |
| Missing token | No token provided |


