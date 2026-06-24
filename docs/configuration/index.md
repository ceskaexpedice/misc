[Index](../index)

# ⚙️ Konfigurace systému Kramerius

Tato kapitola popisuje konfiguraci systému Kramerius a jeho integrovaných komponent.

Konfigurace je rozdělena do dvou hlavních úrovní:

- **Konfigurace Kramerius Core**
- **Konfigurace integrovaných služeb**

Toto rozdělení je důležité pro správné pochopení toho, co se kde nastavuje:
- část konfigurace přímo ovlivňuje chování aplikace Kramerius
- část konfigurace se týká externích systémů, které Kramerius využívá

---


## Kramerius Core

Jádro aplikace (Java/Tomcat) obsahuje množství konfiguračních parametrů. Tyto parametry mají definované výchozí hodnoty přímo v distribučním balíčku (`.war`).
Typicky jde o parametry, které přímo ovlivňují chování systému:

- URL adresy integrovaných služeb (SOLR, Akubra, Keycloak)
- databázová připojení
- cache, timeouty
- nastavení procesní platformy
- další runtime parametry

➡️ [Konfigurační soubory, výchozí hodnoty parametrů a jak je přepsat](files/index)

### Logování
TODO

### Monitoring
TODO

---

## Konfigurace integrovaných služeb

Tato část popisuje konfiguraci externích systémů, které Kramerius využívá.

Tyto komponenty mají vlastní konfigurační mechanismy a často i vlastní dokumentaci.

### [Akubra](https://github.com/ceskaexpedice/akubra/wiki)
- storage backend
- ukládání digitálních objektů
- konfigurace persistence

Hlavní konfigurace se děje skrze Kramerius Core:
➡️ [Akubra konfigurace](files/configuration-akubra)

### [Vyhledávání](search)
- definice indexů
- analyzéry
- schema
- boostování a relevance

Konfigurace přístupu k SOLR se děje skrze Kramerius Core:
➡️ [Vyhledávání](files/configuration-solr)

### [Zabezpečení](security)
- realm konfigurace
- klienti
- role a oprávnění
- mapování uživatelů


### [Process Platform](https://github.com/ceskaexpedice/process-platform/wiki)
- asynchronni ulohy

➡️ [Konfigurace Plugins](../reference/process-platform/plugins)


### [Distribuované zámky](https://github.com/ceskaexpedice/hazelcast-locks-server/wiki)
- synchronizace

Hlavní konfigurace se děje skrze Kramerius Core:
➡️ [Hazelcast konfigurace](files/configuration-akubra)

### [IIIF Image Server](iiif)
- cachování obrazů
- limity generování
- zdroje obrazů

### ČDK
TODO

### [Web klient](https://github.com/ceskaexpedice/kramerius-web-client-v3/wiki)
- hlavní konfigurace
- úvodní stránka
- licence

---

## Konfigurace v Docker nasazení (Deployment)

Při nasazení pomocí Docker Compose je veškerá konfigurace centralizovaná do jednoho místa – souboru `.env`, ze kterého čerpá `docker-compose.yml`.
Pro snadnější instalaci a manipulaci vznikl projekt [Kramerius docker compose](https://github.com/ceskaexpedice/kramerius-docker-compose), který obsahuje všechny komponenty kontejnerizované.

### Soubor `.env` (Příklad a šablona)

Zde udržujte seznam pouze těch proměnných, které **musí** administrátor před spuštěním změnit (tzv. "Základní setup").

---

## Konfigurační strategie a hierarchie

Systém Kramerius využívá vrstvenou konfiguraci. Obecné pravidlo pro správu konfigurace je:

1. **Výchozí hodnoty (Defaults)**  
   Jsou zabaleny přímo v aplikaci (`.war` soubory) nebo definovány v Docker image.

2. **Globální / instalační konfigurace**  
   Společná nastavení pro celé nasazení (např. URL adresy, databáze, připojení ke službám) jsou řízena na úrovni **Docker Compose** pomocí proměnných prostředí.

3. **Detailní konfigurace komponent**  
   Specifické chování jednotlivých modulů nebo integrovaných služeb (např. Solr schema, Keycloak role) se konfiguruje v jejich vlastních konfiguračních souborech.

---

## Přehled konfiguračních oblastí

| Komponenta              | Kategorie                 | Popis |
|:------------------------|:--------------------------|:------|
| **Kramerius Core**      | Aplikace Kramerius        | Hlavní konfigurační parametry systému (`configuration.properties`, ENV proměnné) |
| **Process Platform**    | Integrovaná služba        | Konfigurace asynchronního zpracování úloh |
| **Web Client**          | Aplikace Kramerius        | Konfigurace frontend klienta |
| **Docker Compose**      | Infrastruktura            | `.env` a `docker-compose.yml` |
| **Search (SOLR)**       | Integrovaná služba (cizi) | Schémata, analyzéry, indexační konfigurace |
| **Security (Keycloak)** | Integrovaná služba        | Realm, klienti, role a mapování oprávnění |
| **Akubra**              | Integrovaná služba        | Repository a úložiště digitálních objektů |
| **IIIF Image Server**   | Integrovaná služba (cizi) | Konfigurace generování a cachování obrazů |

---

## Navazujici dokumentace

- ➡️ [Architektura](../architecture)
- ➡️ [Reference](../reference)
- ➡️ [Deployment](../deployment)
- ➡️ [Navody](../guides)


