# Kramerius Core – Reference

## Přehled

Tato kapitola popisuje technické rozhraní a chování aplikačního jádra systému Kramerius (Kramerius Core).

Kramerius Core je Java WAR aplikace poskytující REST API a zajišťující business logiku systému včetně autentizace, autorizace a integrace s externími i interními komponentami.

---

## REST API

Kramerius Core poskytuje REST API, které je hlavním vstupním bodem pro všechny klientské aplikace.

API je stateless a komunikace probíhá přes HTTP protokol.

### Hlavní oblasti API:

- digitální objekty (Akubra)
- vyhledávání (Search / SOLR)
- uživatelé a oprávnění (Security / Keycloak)
- procesní zpracování (Process Platform)

Detailní specifikace jednotlivých endpointů je popsána v příslušných podkapitolách Reference.

---

## Bezpečnost (Security)

Kramerius Core implementuje bezpečnostní vrstvu založenou na integraci s Keycloak.

### Chování systému:

- autentizace probíhá pomocí JWT tokenů vydaných Keycloakem
- autorizace je řízena pomocí rolí a oprávnění
- přístup k REST endpointům je řízen security vrstvou Kramerius Core

### Integrace:

- validace tokenů vůči Keycloak serveru
- mapování rolí z Keycloak do interního modelu oprávnění

---

## Integrace s komponentami

Kramerius Core komunikuje s následujícími systémy:

### Interní komponenty

- **Akubra**
    - ukládání a čtení digitálních objektů

- **Process Platform**
    - spouštění a řízení asynchronních úloh

### Externí komponenty

- **SOLR**
    - vyhledávání a indexace dat
    - dotazování nad indexem

- **Keycloak**
    - autentizace uživatelů
    - správa rolí a klientů

---

## Chování systému

Kramerius Core funguje jako orchestrátor požadavků:

1. Přijme HTTP request přes REST API
2. Provede autentizaci a autorizaci
3. Deleguje operace na příslušné komponenty
    - Akubra pro práci s digitálními objekty
    - SOLR pro vyhledávání
    - Process Platform pro asynchronní úlohy
4. Sestaví a vrátí odpověď klientovi

---

## Chybové stavy

API vrací standardizované HTTP status kódy:

- `200 OK` – úspěšné zpracování
- `400 Bad Request` – neplatný požadavek
- `401 Unauthorized` – chybí autentizace
- `403 Forbidden` – nedostatečná oprávnění
- `500 Internal Server Error` – chyba na straně serveru

---

## Konfigurace (odkaz)

Detailní konfigurace Kramerius Core je popsána v kapitole:

👉 [Configuration → Kramerius Core](../../configuration/kramerius-core/)