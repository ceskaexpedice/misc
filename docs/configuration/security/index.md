[Index](../index) / [Konfigurace](../../configuration)

# Konfigurace zabezpečení

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

Tato data jsou uložena v databázi. Potřebné informace viz navazující dokumentace na konci stránky.

Konfigurace přístupu ke keycloak se děje skrze Kramerius Core:
➡️ [Keycloak](../files/configuration-keycloak)

### Konfigurační soubor `keycloak.json`

Konfigurace OAuth klienta může být alternativně načítána ze souboru `keycloak.json`.

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
- ➡️ [Navody](../guides/admin/security)
