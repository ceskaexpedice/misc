[Index](../index) / [Konfigurace](../../configuration)  / [Soubory](../../configuration/core)

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

