# ⚙️ Konfigurace systému Kramerius

Tato kapitola popisuje konfiguraci systému Kramerius a jeho integrovaných komponent.

Konfigurace je rozdělena do dvou hlavních úrovní:

- **Konfigurace Kramerius Core**
- **Konfigurace integrovaných služeb**

Toto rozdělení je důležité pro správné pochopení toho, co se kde nastavuje:
- část konfigurace přímo ovlivňuje chování aplikace Kramerius
- část konfigurace se týká externích systémů, které Kramerius využívá

---

## Jak číst tuto kapitolu

Pro správnou orientaci:

- Pokud nastavujete **chování celeho Krameria** → sekce *Konfigurace Kramerius Core*
- Pokud nastavujete **externí služby** → sekce *Konfigurace integrovaných služeb*
- Pokud hledáte detailní technické chování systému → kapitola *[Reference](../reference)*
- Pokud řešíte nasazení → kapitola *[Deployment](../deployment)*

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

## Konfigurace Kramerius Core

Jádro aplikace (Java/Tomcat) obsahuje množství konfiguračních parametrů. Tyto parametry mají definované výchozí hodnoty přímo v distribučním balíčku (`.war`).
Typicky jde o parametry, které přímo ovlivňují chování systému:

- URL adresy integrovaných služeb (SOLR, Akubra, Keycloak)
- databázová připojení
- cache, timeouty
- nastavení procesní platformy
- další runtime parametry

[Konfigurační soubory, výchozí hodnoty parametrů a jak je přepsat](files/configuration-files).

### Důležité konfigurační parametry:
* 📄 [Obecné](files/configuration-properties) – *Hlavní konfigurační soubor pro chování systému.*
* 📄 [Akubra](files/configuration-akubra) – *Nastavení repository.*
* 📄 [Search](files/configuration-solr) – *Nastavení vyhledávání.*

### Způsob přepisování (Override):
V produkčním prostředí (Docker) nepřepisujeme přímo `.properties` soubory uvnitř kontejneru. Místo toho využíváme mechanismus **předávání proměnných prostředí**, které Tomcat aplikace mapuje na Java vlastnosti, případně montujeme (volume mount) externí soubor:

* **Možnost A (Doporučeno):** Přepis pomocí ENV v `docker-compose.yml` (např. `JDBC_URL=...`).
* **Možnost B:** Namontování vlastního souboru do cesty `/usr/local/tomcat/conf/configuration.properties`.

---

## Konfigurace integrovaných služeb

Tato část popisuje konfiguraci externích systémů, které Kramerius využívá.

Tyto komponenty mají vlastní konfigurační mechanismy a často i vlastní dokumentaci.

### [Search (Solr)](search)
- definice indexů
- analyzéry
- schema
- boostování a relevance

### [Security (Keycloak)](security)
- realm konfigurace
- klienti
- role a oprávnění
- mapování uživatelů

### [Akubra](https://github.com/ceskaexpedice/akubra/wiki)
- storage backend
- ukládání digitálních objektů
- konfigurace persistence

### [Process Platform](https://github.com/ceskaexpedice/process-platform/wiki)
- asynchronni ulohy

### [Distribuovane zamky](https://github.com/ceskaexpedice/hazelcast-locks-server/wiki)
- synchronizace

### IIIF Image Server
- cachování obrazů
- limity generování
- zdroje obrazů

---

## Konfigurace v Docker nasazení (Deployment)

Při nasazení pomocí Docker Compose je veškerá konfigurace centralizovaná do jednoho místa – souboru `.env`, ze kterého čerpá `docker-compose.yml`.
Pro snadnější instalaci a manipulaci vznikl projekt [Kramerius docker compose](https://github.com/ceskaexpedice/kramerius-docker-compose), který obsahuje všechny komponenty kontejnerizované.

### Soubor `.env` (Příklad a šablona)

Zde udržujte seznam pouze těch proměnných, které **musí** administrátor před spuštěním změnit (tzv. "Základní setup").

---

## Navazujici dokumentace

- ➡️ [Architektura](../architecture)
- ➡️ [Reference](../reference)
- ➡️ [Deployment](../deployment)
- ➡️ [Navody](../guides)


