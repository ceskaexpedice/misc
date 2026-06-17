[Index](../index) / [Konfigurace](../../configuration)

# Keycloak configuration

## Realm

Každá instalace má vlastní realm.

---

## Clients

- krameriusClient (UI)
- account

---

## Role model

- realm roles
- client roles

---

## Identity federation

- SAML
- LDAP (volitelně)

---

## Protocol mappers

- roles
- attributes (eduPerson*)

---

## Config Keycloak
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

## Shrnutí

Konfigurace Keycloak definuje identitu a role uživatelů.