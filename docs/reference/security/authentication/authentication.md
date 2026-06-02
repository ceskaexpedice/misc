# Autentizace v Kramerius

## Přehled

Kramerius používá **Keycloak jako centrální autentizační systém** pro všechny uživatelské aplikace. Každá instalace (typicky jedna knihovna nebo instituce) provozuje vlastní Keycloak instanci, případně rozšířenou o federaci externích identity providerů (např. SAML).

Autentizace je založená na **stateless OAuth2 / OpenID Connect Bearer tokenech**.

---

## Vazba na Keycloak

Kramerius používá Keycloak jako externí identity provider.

Konfigurační a provozní aspekty jsou popsány zde:

- `reference/deployment/keycloak.md`
- `reference/configuration/keycloak.md`

---

## Dotčené aplikace

- Reader UI
- Admin UI

---

## Login flow

1. Redirect do Keycloak
2. autentizace uživatele
3. návrat OIDC Bearer tokenu
4. použití tokenu v API requestech

---

## Token-based autentizace

- stateless model
- každý request obsahuje Bearer token
- backend validuje token

---

## Role a atributy

Token obsahuje:
- identity
- roles
- federované atributy

---

## Role enrichment

Kramerius může:
- doplnit role
- upravit role
- mapovat role interně

---

## Oddělení odpovědností

- authentication = identita
- authorization = oprávnění

---

## Shrnutí

Autentizace je založena na Keycloak a OIDC tokenech.