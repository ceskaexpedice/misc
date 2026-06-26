[Index](../../../index) / [Konfigurace](../../)  / [Core](../)

# Token endpoint

Tato stránka poskytuje **referenční přehled konfiguračních parametrů Akubra storage**. Obsahuje defaultní hodnoty, účel a doporučené nastavení.

Konfigurace se načítá z:

- **Default**: uvnitř JAR souboru knihovny `configuration.properties`
- **Uživatelské přetížení**: soubor `$USER_HOME/.kramerius4/configuration.properties`

Uživatel může ve svém souboru předefinovat libovolnou hodnotu z defaultního souboru.


# Token endpoint

| Klíč                | Popis                                  | Výchozí hodnota             |
| ------------------- | -------------------------------------- | --------------------------- |
| `keycloak.tokenurl` | URL token endpointu identity providera | Odpovídá defaultnímu realmu |

## OAuth klient

| Klíč                | Popis                       | Poznámka                                           |
| ------------------- | --------------------------- | -------------------------------------------------- |
| `keycloak.clientId` | Identifikátor OAuth klienta | Musí odpovídat konfiguraci realmu                  |
| `keycloak.secret`   | Client secret               | Používá se pouze při zapnuté client authentication |

| Property | Description |
|---|---|
| keycloak.realm | Keycloak realm |
| keycloak.clientId | OAuth client ID |
| securedstreams | Protected datastreams |

