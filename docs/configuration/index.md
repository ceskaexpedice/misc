# Konfigurace systému Kramerius

Tato kapitola popisuje konfigurační principy systému Kramerius, architekturu nastavení jednotlivých komponent a způsob, jakým se konfigurace aplikuje v různých prostředích (zejména Docker).

---

## 1. Konfigurační strategie a hierarchie

Systém Kramerius využívá vrstvenou konfiguraci. Obecné pravidlo pro správu konfigurace je:

1. **Výchozí hodnoty (Defaults):** Jsou zabaleny přímo v aplikaci (`.war` soubory) nebo definovány v Docker images.
2. **Globální/Instalační konfigurace:** Společná nastavení pro celé nasazení (např. URL adresy, přístupy do databází) jsou řízena na úrovni **Docker Compose** pomocí proměnných prostředí (Environment Variables).
3. **Specifická/Detailní konfigurace:** Detailní chování aplikací (např. vnitřní ladění Kramerius jádra) se konfiguruje pomocí externích konfiguračních souborů namontovaných do kontejnerů.

---

## 2. Přehled konfiguračních úrovní

Pro rychlou orientaci slouží následující tabulka, která ukazuje, kde se co konfiguruje:

| Komponenta            | Typ konfigurace | Primární umístění / Mechanismus                           | Odkaz na detail                                                |
|:----------------------| :--- |:----------------------------------------------------------|:---------------------------------------------------------------|
| **Kramerius jádro**   | Aplikace (Java/Tomcat) | `configuration.properties` properties files               | [Konfiguracni soubory](files/configuration-files)        |
| **Docker Compose**    | Infrastruktura / Prostředí | Soubor `.env` a `docker-compose.yml`                      | [Docker Compose](../deployment/docker/index)                    |
| **Keycloak**          | Bezpečnost (Cizí komponenta) | Administrační rozhraní + exportovaná sféra (Realm JSON)   | [Dokumentace Keycloak](https://www.keycloak.org/documentation) |
| **IIIF Image Server** | Obrazový server | Konfigurační soubor serveru (např. Cantaloupe.properties) | [Reference serveru](#)                                         |

---

## 3. Detailní konfigurace komponent

### 3.1. Kramerius jádro

Jádro aplikace (Java/Tomcat) obsahuje množství konfiguračních parametrů. Tyto parametry mají definované výchozí hodnoty přímo v distribučním balíčku (`.war`).

[Konfigurační soubory, výchozí hodnoty parametrů a jak je přepsat](files/configuration-files).  

#### Důležité konfigurační parametry:
* 📄 [Obecné](files/configuration-properties) – *Hlavní konfigurační soubor pro chování systému.*
* 📄 [Akubra](files/configuration-akubra) – *Nastavení repository.*
* 📄 [Search](files/configuration-solr) – *Nastavení vyhledávání.*

#### Způsob přepisování (Override):
V produkčním prostředí (Docker) nepřepisujeme přímo `.properties` soubory uvnitř kontejneru. Místo toho využíváme mechanismus **předávání proměnných prostředí**, které Tomcat aplikace mapuje na Java vlastnosti, případně montujeme (volume mount) externí soubor:

* **Možnost A (Doporučeno):** Přepis pomocí ENV v `docker-compose.yml` (např. `JDBC_URL=...`).
* **Možnost B:** Namontování vlastního souboru do cesty `/usr/local/tomcat/conf/configuration.properties`.

---

### 3.2. Akubra Repository

Konfigurace nízkoúrovňového úložiště digitálních dokumentů.

* 📄 [Akubra (GitHub)](https://github.com/ceskaexpedice/akubra)

---

### 3.3. Process Platform

Konfigurace framework pro asynchronní spouštění úloh.

* 📄 [Process Platform)](https://github.com/ceskaexpedice/process-platform/wiki/RunningPlatform)

---

### 3.3. Převzaté komponenty (Keycloak, IIIF, atd.)

U komponent, které nejsou vyvíjeny v rámci projektu Kramerius, se dokumentace omezuje **pouze na integrační vazby**. Detailní konfiguraci naleznete v oficiální dokumentaci daných projektů.

* **Keycloak:** Konfiguruje se primárně přes UI. Pro automatické nasazení se používá inicializační soubor `realm-export.json`, který je součástí našeho Docker deploymentu.
* **IIIF Image Server:** Konfigurace cachování a limitů pro generování obrazů.

---

## 4. Konfigurace v Docker nasazení (Deployment)

Při nasazení pomocí Docker Compose je veškerá konfigurace centralizovaná do jednoho místa – souboru `.env`, ze kterého čerpá `docker-compose.yml`.
Pro snadnější instalaci a manipulaci vznikl projekt [Kramerius docker compose](https://github.com/ceskaexpedice/kramerius-docker-compose), který obsahuje všechny komponenty kontejnerizované.

### Soubor `.env` (Příklad a šablona)

Zde udržujte seznam pouze těch proměnných, které **musí** administrátor před spuštěním změnit (tzv. "Základní setup").

```env
# --- NASTAVENÍ PROSTŘEDÍ ---
COMPOSE_PROJECT_NAME=kramerius-produkce
KRAMERIUS_VERSION=7.x.x

# --- SÍŤ A DOMÉNY ---
KRAMERIUS_DOMAIN=kramerius.knihovna.cz
EXTERNAL_PORT=80

# --- DATABÁZE ---
DB_USER=kramerius
DB_PASSWORD=ZmenMojeHeslo123!
DB_NAME=kramerius_db

# --- INTEGRACE ---
KEYCLOAK_URL=[https://auth.knihovna.cz](https://auth.knihovna.cz)