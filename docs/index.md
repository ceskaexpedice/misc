# Kramerius jádro – Dokumentace

Vítejte v dokumentaci systému **Kramerius jádro** – modulární platformy pro správu a zpřístupnění digitálních knihovních sbírek.

Tato dokumentace popisuje **celý ekosystém Kramerius jádro**: jeho základní principy, provoz, integrace i typické reálné scénáře nasazení v knihovnách.

---

## Co je Kramerius

Kramerius je systém pro:
- správu digitálních dokumentů a metadat
- dlouhodobé ukládání digitálních objektů (Akubra / Fedora)
- indexaci a vyhledávání (Solr)
- řízení importních a hromadných procesů
- správu přístupových práv a bezpečnosti

Jádro systému běží jako **Java aplikace v Tomcatu** a poskytuje **REST API**.  
Nad jádrem existují samostatné klientské aplikace (Čtenářský a Admin klient) a navazující moduly.

Kramerius je open source sw řešení pro zpřístupnění digitálních dokumentů. Primárně je určen pro digitalizované knihovní sbírky, monografie a periodika.
Využit může být ke zpřístupnění dalších typů dokumentů např. map, hudebnin a starých tisků, kronik, případně částí dokumentů jako jsou články a kapitoly.
Systém je vhodný také pro digital born dokumenty, tedy dokumenty, které vznikly v elektronické podobě. Kramerius je průběžně upravován tak, aby struktura metadat odpovídala standardům vyhlašovaným Národní knihovnou České republiky.
Systém poskytuje rozhraní pro přístup koncových uživatelů, zajišťující vyhledávání v metadatech a v plných textech, generování vícestránkových PDF dokumentů z vybraných stran,
vytváření virtuálních sbírek a další operace nad uloženou sbírkou digitálních dokumentů.
Využívá úložiště Akubra a nové schéma indexu vyhledávacího systému SOLR. Klientské prostředí zahrnuje uživatelského klienta a administrátorského určeného na správu systému.

---

## Začínáme (Getting Started)

Nevíte, kde začít?  
Zvolte si svou roli a projděte základní orientaci v systému:

👉 **[Getting Started](getting-started/index.md)**  
*(Kurátor / Administrátor / Vývojář)*

Getting Started vám pomůže:
- pochopit, jakou část dokumentace potřebujete
- vybrat správnou cestu podle vaší role
- neztratit se v technických detailech

---

## Jak je dokumentace strukturována

Dokumentace je rozdělena do hlavních částí. Každá odpovídá na jiný typ otázek:

### 🧠 Základní pojmy
Pokud jste v Krameriu noví, doporučujeme začít se základními koncepty systému:

- digitální objekty a jejich modely
- PID identifikátory
- datastreamy a repository
- kolekce a virtuální kolekce
- licence a přístupová práva
- indexace a vyhledávání

👉 **[Základní pojmy](core-concepts/index)**

---

### 🧠 Architektura
Jak jsou části systému organizované a jak spolu spolupracují

Architektura odpovídá na otázky:

- jaké komponenty systém má
- jak spolu komunikují
- jak tečou data
- kde se rozhoduje
- co je oddělená služba
- co je synchronní vs asynchronní
- co je runtime dependency
- co je persistentní
- co je externí infrastruktura

👉 **[Architektura](architecture/index)**

---

### 🛠 Deployment
Praktické návody „jak nasadit“.

👉 **[Deployment](deployment/index)**

---

### 🛠 Konfigurace
Jak nastavit.

👉 **[Konfigurace](configuration/index)**

---

### 🛠 Návody
Praktické návody „jak něco udělat“.

Použijte, pokud:
- instalujete nebo provozujete Kramerius
- pracujete s Admin klientem
- vyvíjíte nebo integrujete moduly

👉 **[Návody](guides/index)**

---

### 🔀 Scénáře
Ucelené průřezové návody pro reálné situace.

Použijte, pokud řešíte např.:
- zapojení knihovny do DNNT
- nasazení nové instance do ČDK
- migraci dat
- kombinaci bezpečnosti, procesů a konfigurace

👉 **[Scénáře](scenarios/index)**

---

### 📚 Reference
Detailní technická dokumentace.

Použijte, pokud hledáte:
- REST API
- konfigurační parametry
- formáty dat
- bezpečnostní detaily

👉 **[Reference](reference/index)**

---

## Jak dokumentaci používat

- **Noví uživatelé** → Getting Started
- **Porozumění systému** → Core Concepts
- **Konkrétní úkol** → Guides
- **Reálný problém** → Scenarios
- **Technické detaily** → Reference

---

## Přispívání a vývoj dokumentace

Dokumentace se vyvíjí spolu se systémem Kramerius.  
Jednotlivé části se mohou zpřesňovat, ale základní struktura zůstává stabilní.
