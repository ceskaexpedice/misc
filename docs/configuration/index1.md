# Konfigurace systému Kramerius

Tato kapitola popisuje konfigurační principy systému Kramerius, architekturu nastavení jednotlivých komponent a způsob, jakým se konfigurace aplikuje v různých prostředích (zejména Docker).

---

## 1. Konfigurační strategie a hierarchie

Systém Kramerius využívá vrstvenou konfiguraci. Obecné pravidlo pro správu konfigurace je:

1. **Výchozí hodnoty (Defaults):** Jsou zabaleny přímo v aplikaci (`.war` soubory) nebo definovány v Docker obrazech.
2. **Globální/Instalační konfigurace:** Společná nastavení pro celé nasazení (např. URL adresy, přístupy do databází) jsou řízena na úrovni **Docker Compose** pomocí proměnných prostředí (Environment Variables).
3. **Specifická/Detailní konfigurace:** Detailní chování aplikací (např. vnitřní ladění Kramerius jádra) se konfiguruje pomocí externích konfiguračních souborů namontovaných do kontejnerů.

---

## 2. Přehled konfiguračních úrovní

Pro rychlou orientaci slouží následující tabulka, která ukazuje, kde se co konfiguruje:

| Komponenta | Typ konfigurace | Primární umístění / Mechanismus | Odkaz na detail |
| :--- | :--- | :--- | :--- |
| **Kramerius Jádro** | Aplikace (Java/Tomcat) | `kramerius.properties`, `solr.properties` přes environment variables | [Detail viz níže](#31-kramerius-jadro) |
| **Docker Compose** | Infrastruktura / Prostředí | Soubor `.env` a `docker-compose.yml` | [Detail viz níže](#4-konfigurace-v-docker-nasazeni) |
| **Keycloak** | Bezpečnost (Cizí komponenta) | Administrační rozhraní + exportovaná sféra (Realm JSON) | [Dokumentace Keycloak](https://www.keycloak.org/documentation) |
| **IIIF Image Server** | Obrazový server | Konfigurační soubor serveru (např. Cantaloupe.properties) | [Reference serveru](#) |

---

## 3. Detailní konfigurace komponent

### 3.1. Kramerius Jádro

Jádro aplikace (Java/Tomcat) obsahuje velké množství konfiguračních parametrů. Tyto parametry mají definované výchozí hodnoty přímo v distribučním balíčku (`.war`).

> ⚠️ **Pravidlo pro dokumentaci:** Konfigurační vlastnosti (properties) **nejsou** v této Wiki duplikovány textově, aby nedocházelo k chybám při aktualizacích. Aktuální seznam a výchozí hodnoty naleznete vždy přímo v repozitáři.

#### Odkazy na zdrojové konfigurační soubory (Master Copy):
* 📄 [Kramerius Core Configuration (GitHub)](https://github.com/ceskaexpedice/akubra/blob/main/.../kramerius.properties) – *Hlavní konfigurační soubor pro chování systému, napojení na repozitář Akubra atd.*
* 📄 [Solr Index Configuration (GitHub)](https://github.com/ceskaexpedice/akubra/blob/main/.../solr.properties) – *Nastavení vyhledávacího jádra.*

#### Způsob přepisování (Override):
V produkčním prostředí (Docker) nepřepisujeme přímo `.properties` soubory uvnitř kontejneru. Místo toho využíváme mechanismus **předávání proměnných prostředí**, které Tomcat aplikace mapuje na Java vlastnosti, případně montujeme (volume mount) externí soubor:

* **Možnost A (Doporučeno):** Přepis pomocí ENV v `docker-compose.yml` (např. `KRAMERIUS_DATABASE_URL=...`).
* **Možnost B:** Namontování vlastního souboru do cesty `/usr/local/tomcat/conf/kramerius.properties`.

---

### 3.2. Akubra Repository

Konfigurace nízkoúrovňového úložiště digitálních dokumentů. Obsahuje specifická nastavení pro FS (File System) nebo vazbu na databázi.

* 📄 [Akubra Configuration Reference (GitHub)](https://github.com/ceskaexpedice/akubra)
* **Klíčové parametry k úpravě:**
    * `akubra.storage.dir` – Cesta k hlavnímu datovému adresáři.

---

### 3.3. Převzaté komponenty (Keycloak, IIIF, atd.)

U komponent, které nejsou vyvíjeny v rámci projektu Kramerius, se dokumentace omezuje **pouze na integrační vazby**. Detailní konfiguraci naleznete v oficiální dokumentaci daných projektů.

* **Keycloak:** Konfiguruje se primárně přes UI. Pro automatické nasazení se používá inicializační soubor `realm-export.json`, který je součástí našeho Docker deploymentu.
* **IIIF Image Server:** Konfigurace cachování a limitů pro generování obrazů.

---

## 4. Konfigurace v Docker nasazení (Deployment)

Při nasazení pomocí Docker Compose je veškerá konfigurace centralizovaná do jednoho místa – souboru `.env`, ze kterého čerpá `docker-compose.yml`.

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