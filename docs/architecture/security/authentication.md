# Autentizace

Autentizace v Krameriovi je založena na standardech OAuth 2.0 a OpenID Connect.

Ověření identity probíhá mimo Kramerius v externím Identity Provideru.

## Tok autentizace

```text
User
  |
  | Login
  v
Keycloak
  |
  | JWT Token
  v
Kramerius
```

Po úspěšném přihlášení získá klient přístupový token.

Token je následně přikládán ke každému požadavku na API.

## Zpracování tokenu

Při příjmu požadavku Kramerius:

1. získá token z HTTP požadavku,
2. ověří jeho platnost,
3. ověří podpis,
4. načte identitu uživatele,
5. načte role.

## Výsledek autentizace

Po úspěšné autentizaci jsou dostupné:

- identifikátor uživatele,
- uživatelské jméno,
- role,
- další atributy předané poskytovatelem identity.

Tyto informace jsou následně použity při autorizaci.

## Související kapitoly

- [Reference / Authentication](../../../reference/security/authentication/)