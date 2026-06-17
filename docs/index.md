# Kramerius – Dokumentace

Vítejte v dokumentaci systému **Kramerius** – modulární platformy pro správu a zpřístupnění digitálních knihovních sbírek.

## 🚀 Začínáme

Nevíte, kde začít?  
Zvolte si svou roli a projděte základní orientaci v systému

👉 **[Začínáme](getting-started/index.md)**  
*(Kurátor / Administrátor / Vývojář)*

---

## 📚 Základní pohled

Co znamenají pojmy v Krameriu z pohledu uživatele i systému.

👉 🧠 **[Doménové pojmy](domain-concepts/index)**  
Vysvětlení pojmů tak, jak se používají při práci se systémem (např. dokument, sbírka, import, metadata).

👉 ⚙️ **[Hlavní části Krameria](core-concepts/index)**  
Akubra, procesy, indexace, API, FOXML, ...

---

## 🛠️ Návody
Jak udělat konkrétní úkol

👉 **[Návody](guides/index)**

---

## 🎯 Scénáře
Use cases pro reálné situace


👉 **[Scénáře](scenarios/index)**

---

## 🏗️ Architektura
Jak jsou části systému organizované a jak spolupracují

👉 **[Architektura](architecture/index)**

---

## 📖 Reference
Jak přesně fungují komponenty

👉 **[Reference](reference/index)**

---

## ⚙️ Konfigurace
Jak se systém nastavuje

👉 **[Konfigurace](configuration/index)**

---

## 🚢 Deployment
jak systém běží v infrastruktuře

👉 **[Deployment](deployment/index)**

---


## Jak dokumentaci používat

- **Noví uživatelé** → Začínáme
- **Porozumění systému** → Základní pojmy, Architektura
- **Konkrétní úkol** → Návody
- **Reálný problém** → Scénáře
- **Technické detaily** → Reference 
- **Nasazení, konfigurace** → Deployment, Konfigurace

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
