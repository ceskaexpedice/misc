[Index](../index) / [Začínáme](../getting-started)

# Zaciname – Vývojář / Integrátor

Tato stránka slouží jako **vstupní rozcestník pro vývojáře a integrátory**, kteří pracují s platformou Kramerius z pohledu **integrace, rozšiřování a vývoje vlastních řešení**.

Nejde o detailní technický manuál, ale o **orientační přehled**:
- s jakými částmi systému vývojář pracuje
- jaká rozhraní Kramerius poskytuje
- kde v dokumentaci pokračovat dál

---

## Pro koho je tato stránka

Určeno pro **vývojáře a integrátory**, kteří:
- integrují Kramerius s externími systémy
- využívají nebo rozšiřují REST API
- vyvíjejí vlastní moduly, nástroje nebo procesy
- automatizují práci nad obsahem

Pokud řešíte instalaci, provoz nebo konfiguraci infrastruktury, pokračujte na  
**[Getting Started - Admin](admin)**.

---

## Role vývojáře v Kramerius

Vývojář v Krameriovi typicky řeší:

- práci s **REST API** Krameria
- integraci s externími systémy a službami
- vývoj doplňkových modulů a nástrojů
- napojení na **procesní framework**
- testování a ladění integračních scénářů

> Tato stránka slouží jako rozcestník a checklist, nikoli jako krokový návod.

---

## S jakými částmi systému vývojář pracuje

Z pohledu vývojáře se Kramerius skládá z následujících částí:

### Kramerius Core (REST API)
Hlavní integrační rozhraní systému:
- práce s digitálními objekty a metadaty
- správa procesů
- vyhledávání a přístup k obsahu

➡️ Viz **[REST API](../reference/api)**.

---

### UI klienti
- čtenářské UI
- Admin Client

Vývojář:
- typicky UI nerozvíjí přímo
- ale musí rozumět jeho chování a vazbě na API

➡️ Viz **[Admin klient](../reference/client-admin)**.

---

### Repository (Akubra / Fedora)
- fyzické uložení digitálních objektů
- struktura a vztahy mezi objekty

Vývojář s repozitářem obvykle pracuje **nepřímo prostřednictvím API**, ale měl by znát základní principy.

➡️ Viz **[Akubra](../reference/akubra/index)**.

---

### Search
- indexace a vyhledávání obsahu
- práce s dotazy, filtry a výsledky

➡️ Viz **[Search](../reference/search)**.

---

### Procesní framework
- spouštění a řízení procesů
- automatizace a dávkové operace
- možnost vývoje vlastních procesů

➡️ Viz **[Procesy](../reference/process-platform/index)**.

---

### Bezpečnost a autentizace
- práce s autentizací (tokeny, role)
- respektování autorizačního modelu systému
- zabezpečení API volání

➡️ Viz **[Bezpecnost](../reference/security/index)**.

---

## Jak pokračovat dál

Pro detailní informace pokračujte do těchto částí dokumentace:

1. **[Základní pojmy](../core-concepts/index)** – vytvoření správného mentálního modelu systému
2. **[Návody](../guides/developer/index)** – instalace, konfigurace a provoz
3. **[Scénáře](../scenarios/index)** – reálné situace (např. nasazení nové instance, integrace knihovny)
4. **[Reference](../reference/index)** – detailní technické informace a konfigurace

---

## Co tato stránka nepokrývá

Tato stránka:
- neřeší instalaci ani provoz systému
- nepopisuje interní implementaci jádra
- nenahrazuje referenční dokumentaci API

Slouží jako **vstupní bod do dokumentace pro roli vývojáře / integrátora**.
