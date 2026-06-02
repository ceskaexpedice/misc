# On‑Premise Deployment

Tento návod popisuje instalaci a nasazení systému **Kramerius** v prostředí **on‑premise** (bez Dockeru a Kubernetes).

> Tento dokument je **praktický návod (Guide)**. Základní pojmy a technické detaily jsou popsány v sekcích **Core Concepts** a **Reference**.

---

## Kdy zvolit on‑premise variantu

On‑premise nasazení je vhodné pokud:

* provozujete Kramerius na vlastním serveru nebo VM
* nemůžete nebo nechcete používat Docker
* potřebujete plnou kontrolu nad filesystemem a JVM

---

## Přehled komponent

On‑premise instalace typicky obsahuje tyto části:

* Java (JDK)
* Apache Tomcat
* Kramerius jádro (`kramerius.war`)
* Solr (`search.war`)
* Storage (Akubra / filesystem)
* Databáze (PostgreSQL)

> Význam jednotlivých komponent je popsán v **Core Concepts**.

---

## 1. Příprava prostředí

### Java

* Doporučená verze: **Java 21**
* Java musí být dostupná pro Tomcat

> Konkrétní požadavky na Javu viz **Reference → Runtime Requirements**.

### Apache Tomcat

* Doporučená verze: Tomcat 9 nebo 10 (dle verze Krameria)
* Tomcat musí běžet pod uživatelem, který má přístup ke storage

---

## 2. Databáze

* Podporovaná databáze: PostgreSQL
* Databáze musí být dostupná z Tomcatu

> Schéma databáze a konfigurační parametry jsou popsány v **Reference → Database**.

---

## 3. Storage

Kramerius ukládá digitální objekty do storage vrstvy.

### Volba storage backendu

* Akubra filesystem backend (doporučeno)
* Legacy filesystem (jen pro starší instalace)

> Princip fungování storage je popsán v **Core Concepts → Storage**.

### Umístění dat

* Storage adresář musí být:

    * perzistentní
    * zapisovatelný pro Tomcat
    * zálohovatelný

Příklad:

* `/var/lib/kramerius/data`

> Konkrétní konfigurační klíče viz **Reference → Storage**.

---

## 4. Nasazení aplikací

### Kramerius jádro

* Nasazení souboru `kramerius.war` do Tomcatu
* Konfigurace pomocí properties souborů

### Solr (search)

* Nasazení `search.war`
* Inicializace Solr core

> Parametry indexace a schéma Solr jsou popsány v **Reference → Indexer**.

---

## 5. Ověření instalace

Po spuštění:

* ověřte dostupnost webového rozhraní
* ověřte přístup k databázi
* ověřte zápis do storage

---

## Související dokumentace

* **Core Concepts → Storage**
* **Reference → Storage**
* **Reference → Configuration**
* **Guides → Deployment → Docker Compose** (alternativní nasazení)
