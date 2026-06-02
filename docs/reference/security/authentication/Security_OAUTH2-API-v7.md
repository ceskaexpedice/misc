## Bezpečnost, autentizace a autorizace

Autorizace a autenizace je realizována pomocí protokolu Oauth2. Klient/browser, který se chce autentizovat nejdříve pošle request na jádro krameria na endpoint `~/search/api/client/v7.0/user/login`. Ten ho přesměruje na aktuální keycloak, kde se uživatel autentizuje jedním s podporovaných typů přihlášení (formulář, shibboleth federace,  facebook, google, atd..), následně je přesměrován na konfigurovanou adresu s parametrem `code`. Pomocí parametru je klient/browser schopen získat `access token`.  Poté `access token` používá ve všech voláních na jádro. 

Diagram získání JWT tokenu:

```mermaid
sequenceDiagram
    participant Uživatel
    participant Klient
    participant Jádro
    participant Keycloak

    Uživatel->>Klient: Požadavek na přihlášení
    Klient->>Jádro: Požadavek na autentizaci
    Jádro-->>Klient: Přesměrování na Keycloak
    Klient->>Keycloak: Dotaz na Keycloak
    Keycloak-->>Klient: Odpověď z Keycloaku - formulář s možnostmi přihlášení
    Uživatel->>Keycloak: Zadání přihlašovacích údajů
    Keycloak-->>Klient: Přesměrování zpět na Klient s code parametrem
    Klient->>Jádro: Požadavek na token s code parametrem
    Jádro->>Keycloak: Požadavek na token s code parametrem
    Keycloak-->>Jádro: Odpověď s tokenem
    Jádro-->>Klient: Odpověď s tokenem
```

<!--
* Okdkaz na práva - práva v K7
* Sekvence diagram přístupu k tokenu
* Keycloak - nastavení a přístupy
* EDuid federace 
* DNNT 
-->