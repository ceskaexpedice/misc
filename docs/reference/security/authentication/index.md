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

### [Token lifecycle](token-lifecycle)

### [Token model](token-model)

## User Principal

Po úspěšné validaci tokenu vzniká interní reprezentace uživatele.

### Role v systému

Každý přihlášený uživatel má přiřazenou jednu nebo více rolí. Ve výchozím nastavení jsou v Krameriovi k dispozici tyto dvě role:


- **kramerius_admin**  
  Administrátorská role, která opravňuje k provádění všech administrátorských úkonů a správě uživatelských oprávnění.

- **common_users**  
  Role pro všechny běžné uživatele, která zajišťuje základní přístupová oprávnění.

- **dnnt_users**  
  Role určená pro uživatele, kteří mají přístup k dnnto dokumentům

## Authentication Errors

| Error | Description |
|--------|--------|
| Invalid token | Token cannot be validated |
| Expired token | Token expired |
| Missing token | No token provided |


