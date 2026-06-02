# Token model v Kramerius

## Přehled

Kramerius používá OpenID Connect (OIDC) Bearer tokeny vydávané systémem Keycloak jako vstupní identitu uživatele.

Token představuje externí bezpečnostní identitu získanou z Keycloak a případně z federovaných identity providerů.

Kramerius tento token:

- validuje
- interpretuje
- transformuje do interního bezpečnostního modelu

Tento dokument popisuje strukturu tokenu a význam jednotlivých částí z pohledu Krameria.

---

## Vztah ke Keycloak

Token je vydáván Keycloak realm serverem.

Typické vlastnosti tokenu:

- JWT formát
- OIDC kompatibilní
- Bearer token
- časově omezená platnost

Konfigurace Keycloak není součástí tohoto dokumentu.

Viz:

- `reference/configuration/keycloak.md`
- `reference/deployment/keycloak.md`

---

## Standardní OIDC část tokenu

Token obsahuje standardní OIDC metadata:

| Pole | Význam |
|---|---|
| exp | čas expirace tokenu |
| iat | čas vydání tokenu |
| auth_time | čas autentizace uživatele |
| jti | unikátní identifikátor tokenu |
| iss | issuer (Keycloak realm URL) |
| aud | audience |
| sub | unikátní identifikátor uživatele |
| typ | typ tokenu |
| azp | autorizovaný klient |
| session_state | identifikátor session |
| sid | session identifier |
| acr | authentication context |

---

## Realm role

Pole `realm_access.roles` obsahuje realm role definované v Keycloak.

Typické role:

- `dnnt_users`
- `special-needs`
- `default-roles-kramerius`
- `offline_access`
- `uma_authorization`

Tyto role reprezentují:

- skupiny uživatelů
- globální oprávnění
- technické Keycloak role
- vstup pro autorizaci v Krameriu

---

## Client role

Pole `resource_access` obsahuje role navázané na konkrétní Keycloak klienty.

Typický příklad:

- `manage-account`
- `manage-account-2fa`
- `view-profile`

Tyto role:

- jsou specifické pro Keycloak klienta
- většinou nejsou používány pro business autorizaci v Krameriu
- slouží především interním funkcím Keycloaku

---

## Identity atributy

Token může obsahovat další atributy identity.

Typické atributy:

| Atribut | Význam |
|---|---|
| preferred_username | uživatelské jméno |
| displayName | zobrazované jméno |
| email | email uživatele |
| email_verified | informace o ověření emailu |

---

## Federované atributy

Při použití federace identity mohou být do tokenu přidány federované atributy.

Typické atributy:

| Atribut | Význam |
|---|---|
| eduPersonPrincipalName | federovaný login |
| eduPersonUniqueId | unikátní federovaný identifikátor |
| eduPersonEntitlement | federovaná oprávnění |
| eduPersonScopedAffiliation | afiliace uživatele |
| affiliation | další afiliace |

Tyto atributy pocházejí typicky z:

- SAML identity providerů
- LDAP
- externích federací
- Keycloak mapperů

---

## Nestandardní atributy

Federované atributy nejsou standardní součástí OIDC.

Jejich:

- názvy
- význam
- dostupnost

se mohou lišit mezi jednotlivými instalacemi.

---

## Role a atributy

Token obsahuje dva odlišné typy bezpečnostních informací.

### Role

Role představují:

- skupiny
- oprávnění
- autorizační vstupy

Zdroj:

- realm_access.roles
- případně mappery

---

### Atributy

Atributy představují:

- identitu uživatele
- federované informace
- metadata identity

Zdroj:

- identity provider
- LDAP
- SAML
- mappery

---

## Vztah ke Kramerius Security Contextu

Kramerius nepoužívá token přímo jako interní bezpečnostní model.

Místo toho:

1. validuje token
2. extrahuje identity a role
3. interpretuje atributy
4. aplikuje role enrichment
5. vytváří interní Security Context

---

## Role enrichment

Kramerius může nad rámec tokenu:

- doplnit další role
- mapovat externí role
- odvodit oprávnění z atributů
- přidat doménová oprávnění

Výsledná autorizace tedy nemusí odpovídat pouze původnímu tokenu.

---

## Oddělení odpovědností

| Vrstva | Odpovědnost |
|---|---|
| Keycloak | autentizace a vydání tokenu |
| Token | přenos identity |
| Kramerius Security Context | interní reprezentace identity |
| Authorization layer | rozhodování o přístupu |

---

## Bezpečnostní poznámky

Kramerius:

- důvěřuje validovanému tokenu
- neudržuje server-side session
- autentizuje každý request samostatně
- používá token pouze po dobu jeho platnosti

---

## Shrnutí

OIDC token představuje vstupní identitu uživatele získanou z Keycloak.

Kramerius z tokenu vytváří vlastní interní bezpečnostní model, který kombinuje:

- identity atributy
- role
- federované informace
- interní role enrichment
- doménová oprávnění