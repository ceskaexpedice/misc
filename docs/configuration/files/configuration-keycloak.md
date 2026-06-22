[Index](../index) / [Konfigurace](../../configuration)  / [Soubory](../../configuration/files)

# Token endpoint

| Klíč                | Popis                                  | Výchozí hodnota             |
| ------------------- | -------------------------------------- | --------------------------- |
| `keycloak.tokenurl` | URL token endpointu identity providera | Odpovídá defaultnímu realmu |

## OAuth klient

| Klíč                | Popis                       | Poznámka                                           |
| ------------------- | --------------------------- | -------------------------------------------------- |
| `keycloak.clientId` | Identifikátor OAuth klienta | Musí odpovídat konfiguraci realmu                  |
| `keycloak.secret`   | Client secret               | Používá se pouze při zapnuté client authentication |
