# Core Concepts – Security

Tato stránka popisuje základní principy **aplikační bezpečnosti** v Krameriovi, se zaměřením na **uživatele, role a autentizaci**. Neřeší bezpečnost infrastruktury ani operačního systému.

---

## Uživatelská identita

- **Uživatel** je člověk, který se přihlašuje do systému Kramerius.
- Uživatelé mohou být **interní** (spravovaní přímo Keycloakem v dané knihovně) nebo **federovaní** přes SAML z jiné knihovny.
- Přihlášení probíhá přes **Keycloak** (IdP), který ověřuje identitu a vygeneruje autentizační token (např. JWT).

### Login flow – přehled
1. Uživatel si vybere knihovnu / instanci Krameria.
2. Zadá přihlašovací údaje (interní nebo přes SAML federaci).
3. Keycloak ověří identitu.
4. Vygeneruje token, který obsahuje seznam rolí uživatele.
5. Token se používá pro autorizaci volání Kramerius Core a dalších komponent.


> **Místo pro diagram login flow a federace mezi knihovnami**  
> *(vložit obrázek zde, např. `login_flow.png`)*
> 

---

## Role

- Role v Kramerius **neodpovídají rolím z dokumentace typu „kurátor / admin / vývojář“**, které slouží pro orientaci v Guides a Getting Started.
- Role jsou **technické Keycloak role**, např.:
   - `common-users` – anonymní / nepřihlášený uživatel
   - `krameriusAdmin` – administrátor platformy
   - další role definované v Keycloak
- Kramerius Core si **eviduje role z tokenu** a používá je k vyhodnocení oprávnění k obsahu, procesům a funkcím.

---

## Licence

👉 **[SEC_K7_Licence](../reference/security/authorization/license/index)**

---

##  Authentication model

Authentication model

Autentizace v Krameriovi je řešena pomocí standardů OAuth 2.0 a OpenID Connect. Kramerius sám uživatele neautentizuje, ale deleguje autentizaci na externí identity provider.

Nejčastěji používaným identity providerem je Keycloak.

Role Keycloaku a Krameria

Keycloak

ověřuje identitu uživatele

vydává access tokeny

spravuje uživatele, role a identity providery

Kramerius

přijímá access tokeny

ověřuje jejich platnost

vyhodnocuje oprávnění vůči interním pravidlům (role, licence, akce)

Tok autentizace

Klient (UI nebo jiný systém) získá access token od identity providera.

Token je přiložen ke každému volání Kramerius API.

Kramerius ověří token a vyhodnotí oprávnění.

Token proxy endpoint

Pro zjednodušení komunikace poskytuje Kramerius vlastní API endpoint, který funguje jako proxy k token endpointu identity providera.

Tento mechanismus zjednodušuje klientskou integraci, ale nenahrazuje standardní OAuth2 tok.---

## Vyhodnocení oprávnění (overview)

1. Klient posílá token při každém volání API nebo při použití Admin Clienta.
2. Core ověří platnost tokenu a načte seznam rolí.
3. Na základě rolí Core určí, ke kterým funkcím, datům a procesům má uživatel přístup.
4. Role jsou technický základ pro **RBAC** (role-based access control).

> Další detaily o tom, jak se role mapují na tabulky oprávnění a jak probíhá vyhodnocení, budou doplněny postupně.

---

## Další kroky

Pro pochopení **jak jsou oprávnění vyhodnocována** podle role, licence a dalších kritérií viz:

- [Práva a vyhodnocování akcí](Permissions)
- [Guides – Administrátor](Guides_Security)
