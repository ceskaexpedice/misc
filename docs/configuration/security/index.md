[Index](../index) / [Konfigurace](../../configuration)

# Zabezpečení konfigurace

Tato část popisuje, jak se bezpečnostní model Krameria nastavuje a spravuje v běžícím systému.

Na rozdíl od technické konfigurace (properties, deployment) jde o **datový model uložený v databázi a externím identity provideru**.

---

## Co je spravováno externě

- uživatelé
- role
- autentizace (login, tokeny)

Kramerius tato data pouze využívá.

➡️ [Keycloak](keycloak)

---

## Co je spravováno v Krameriu 

Kramerius obsahuje administrační model pro:

- mapování rolí na akce
- přiřazení kritérií k akcím
- definici oprávnění (rights)

Tato data jsou uložena v databázi.

➡️ [Admin aplikace](https://github.com/ceskaexpedice/kramerius-admin-client/wiki)

### Config Keycloak
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
- název realmu
- URL autentizačního serveru
- identifikaci klienta
V produkčním prostředí je nutné upravit zejména:
- auth-server-url
- secret pokud je použit

---


---

## Navazujici dokumentace

- ➡️ [Základní pojmy](../core-concepts/security)
- ➡️ [Architektura](../architecture/security)
- ➡️ [Reference](../reference/security)
- ➡️ [Navody](../guides/admin)
