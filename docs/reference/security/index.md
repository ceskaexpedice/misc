# Bezpečnost – Reference pro administrátora

## Pro koho je tato stránka
Tato stránka je určena pro **administrátory a vývojáře**, kteří potřebují znát **konkrétní technické detaily bezpečnosti Krameria**.  
Pokud hledáte pouze principy a scénáře, vraťte se na:
- [Core Concepts – Security Model](Core_Concepts_Security.md)
- [Guides – Security](Guides_Security)

---

## 1. Proměnné prostředí (Environment Variables)
Pro správné nasazení Krameria s bezpečností je nutné nastavit tyto proměnné:

| Proměnná | Popis | Příklad |
|----------|------|--------|
| `KRAMERIUS_IDP_URL` | URL centrálního IdP | `https://keycloak.example.com` |
| `KRAMERIUS_IDP_REALM` | Realm / doména v IdP | `kramerius-realm` |
| `KRAMERIUS_IDP_CLIENT` | Klientské ID aplikace | `kramerius-admin` |
| `KRAMERIUS_IDP_SECRET` | Tajný klíč klienta | `********` |
| `KRAMERIUS_ROLE_MAPPING` | Mapování rolí Krameria na IdP | JSON soubor nebo proměnná |

> Další proměnné závisí na deploymentu (Docker Compose, Kubernetes).

---

## 2. TODO Config Keycloak
Token endpoint
Klíč	Popis	Výchozí hodnota
keycloak.tokenurl	URL token endpointu identity providera	odpovídá defaultnímu realmu
OAuth klient
Klíč	Popis	Poznámka
keycloak.clientId	Identifikátor OAuth klienta	musí odpovídat konfiguraci realmu
keycloak.secret	Client secret	používá se pouze při zapnuté client authentication
Konfigurační soubor keycloak.json

Soubor keycloak.json definuje propojení Krameria s identity providerem a je uložen v pracovním adresáři Krameria.

```
{
  "realm": "kramerius",
  "auth-server-url": "http://localhost:8083/auth/",
  "ssl-required": "external",
  "resource": "krameriusClient",
  "verify-token-audience": false,
  "confidential-port": 0,
  "policy-enforcer": {}
}
```

V produkčním prostředí je tedy třeba příslušně upravit hodnoty `secret`  a  `auth-server-url`

Obsahuje zejména:

název realmu

URL autentizačního serveru

identifikaci klienta

V produkčním prostředí je nutné upravit zejména:

auth-server-url

secret pokud je použit

---

## 2. Tokeny a autentizace
- **Access token** – JWT, platný pro přístup k API a UI klientům
- **Refresh token** – obnovuje platnost access tokenu
- **Scope a claimy** – definují oprávnění uživatele
- Tokeny se ověřují při každém volání REST API a v UI klientu

---

## 3. Role a oprávnění
| Role | Popis | Oprávnění |
|------|------|-----------|
| Čtenář | Prohlížení dokumentů | Přístup k UI a vyhledávání |
| Kurátor | Správa sbírek | CRUD na sbírky, metadata |
| Administrátor | Provoz systému | Instalace, konfigurace, správa uživatelů |
| Projektový manažer | Monitoring a plánování | Přehled procesů, audit |
| Vývojář / Integrátor | Moduly a API | REST API, napojení procesů |

> Role jsou přiřazeny uživatelům přes IdP.  
> Detaily mapování rolí naleznete v `KRAMERIUS_ROLE_MAPPING`.

---

## 4. Přístup k API
- Každý REST endpoint kontroluje **token a role**
- Některé endpointy jsou **omezené na administrátory**
- Všechny požadavky musí být přes HTTPS

> Konkrétní seznam endpointů a potřebných rolí viz [Reference – REST API](API)

---

## 5. Best practices
- Nikdy nesdílejte tajné klíče (`IDP_SECRET`) mimo bezpečné úložiště
- Používejte **minimální oprávnění** pro všechny role
- Auditujte změny rolí a oprávnění
- Oddělujte administrativní a uživatelské účty

---

## 6. Kde pokračovat dál
- [Guides – Security](Guides_Security) – praktické scénáře
- [Core Concepts – Security Model](core-concepts/Security) – principy a koncepty
- [Getting Started – Administrátor](../getting-started/admin) – návrat na startovní stránku role  

