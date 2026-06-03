# Kramerius jádro – Dokumentace

Vítejte v dokumentaci systému **Kramerius jádro** – modulární platformy pro správu a zpřístupnění digitálních knihovních sbírek.

---

## Začínáme (Getting Started)

Nevíte, kde začít?  
Zvolte si svou roli a projděte základní orientaci v systému:

👉 **[Getting Started](getting-started/index.md)**  
*(Kurátor / Administrátor / Vývojář)*

---

## Jak je dokumentace strukturována

Dokumentace je rozdělena do hlavních částí. Každá odpovídá na jiný typ otázek:

### 🧠 Základní pojmy
Co znamenají pojmy v doméně

👉 **[Základní pojmy](core-concepts/index)**

---

### 🧠 Architektura
Jak jsou části systému organizované a jak spolu spolupracují

👉 **[Architektura](architecture/index)**

---

### 📚 Reference
Jak přesně fungují komponenty

👉 **[Reference](reference/index)**

---

### 🛠 Konfigurace
Jak se systém nastavuje

👉 **[Konfigurace](configuration/index)**

---

### 🛠 Deployment
jak systém běží v infrastruktuře

👉 **[Deployment](deployment/index)**

---

### 🛠 Návody
Jak udělat konkrétní úkol

👉 **[Návody](guides/index)**

---

### 🔀 Scénáře
Ucelené průřezové návody pro reálné situace
ace

👉 **[Scénáře](scenarios/index)**

---


## Jak dokumentaci používat

- **Noví uživatelé** → Getting Started
- **Porozumění systému** → Core Concepts
- **Konkrétní úkol** → Guides
- **Reálný problém** → Scenarios
- **Technické detaily** → Reference

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

## Přispívání a vývoj dokumentace

Dokumentace se vyvíjí spolu se systémem Kramerius.  
Jednotlivé části se mohou zpřesňovat, ale základní struktura zůstává stabilní.
