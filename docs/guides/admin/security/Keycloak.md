Autentizace v Krameriovi v7 je řešena pomocí tokenů standardu OAuth2.

Jako autentizační server slouží Keycloak. Kramerius defaultně předpokládá použití standardní distribuce Keycloaku - standalone server. Postup je popsaný na této stránce Getting started: https://www.keycloak.org/getting-started/getting-started-zip

V podstatě to jsou 4 kroky:
1. stáhnout a rozbalit distribuční zip  (https://github.com/keycloak/keycloak/releases/download/15.1.0/keycloak-15.1.0.zip)

2. v adresáři rozbaleného zipu spustit server příkazem:
`bin/standalone.sh -Djboss.socket.binding.port-offset=3 -Dkeycloak.profile.feature.upload_scripts=enabled`

(oproti jejich návodu jsou tam dvě properties navíc - ta první spustí keycloak na portu 8083 místo defaultního 8080, na kterém běží Kramerius. Druhá umožní v dalším kroku nahrát předkonfigurovaný realm pro Kramerius)

3. přihlásit se na http://localhost:8083 a vytvořit si administrátorský účet s libovolným jménem a heslem, třeba `keycloakAdmin` a s ním se pak přihlásit do admin konzole keycloaku

4. Podle administrátorské dokumentace Keycloaku založte realm `kramerius`,  klient `krameriusClient` (preferovany typ klienta je public , tedy volba client authentication off), v uživatelích `krameriusAdmin` a v rolích `common_users`, `public_users`, `kramerius_admin` a `k4_admins`. Můžete také přidat externí identity providery, například Shibboleth, Facebook, Twitter apod.

Pro zjednodušení komunikace mezi klientem a serverem je součástí API Krameria endpoint pro získání access tokenu, který slouží jako fasáda/proxy k volání autentizačního API keycloaku.
 
Endpoint je na URL search/api/auth/token, metoda POST.

V těle requestu je uvedeno jméno a heslo, např. takto: `username=krameriusAdmin&password=krameriusAdmin`

Kramerius request konvertuje na původní volání keycloaku na URL http://localhost:8083/auth/realms/kramerius/protocol/openid-connect/token a do body přidá zbývající parametry &client_id=krameriusClient&grant_type=password, případně client_secret

Parametry URL, client_id a client_secret se dají předefinovat pomocí configuration.properties, defaultní hodnoty odpovídají definici realmu kramerius-realm.json a vypadají takto:

```
keycloak.tokenurl=http://localhost:8083/auth/realms/kramerius/protocol/openid-connect/token
keycloak.clientId=krameriusClient
keycloak.secret=kyPtgyMN7rFfPiJzgaaE90cpBryAQ4nG  #pouziva se pouze pokud je aktivni client authentication
```

Komunikace mezi Krameriem a Keycloakem je konfigurována v souboru `keycloak.json`, který je umístěn v pracovním adresáři Krameria (~\.kramerius4). Jeho defaultní obsah odpovídá nastavení defaultního realmu kramerius-realm.json:

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