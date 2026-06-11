# 🎯 Scenarios

Tato stránka popisuje **ucelené průřezové scénáře pro reálné situace**, se kterými se při práci se systémem **Kramerius** typicky setkávají vývojáři, integrátoři a provozní týmy.

Na rozdíl od **Guides**, které se soustředí na *jednu konkrétní oblast* (např. security, procesy, deployment), jsou **Scenarios** zaměřeny na:

* řešení konkrétního cíle nebo situace,
* kombinaci více oblastí systému,
* praktický postup „od začátku do konce“.

Scénáře odpovídají otázce:

> **„Co všechno musím udělat, když chci vyřešit tuto reálnou situaci?“**

---

## Kdy použít Scenarios

Použijte tuto sekci dokumentace, pokud řešíte například:

* zapojení knihovny nebo služby Kramerius do externího systému (např. **DNNT**),
* nasazení nové instance Krameria v konkrétním prostředí,
* migraci dat mezi instancemi nebo verzemi systému,
* kombinaci **bezpečnosti, procesů a konfigurace** v jednom řešení,
* změny, které zasahují více modulů najednou.

Pokud hledáte izolovaný návod k jedné technologii nebo komponentě, pravděpodobně patří spíše do **Guides**.

---

## Vztah ke Guides

* **Guides**

    * zaměřené na jednu oblast (Security, Deployment, Processes, …)
    * vysvětlují *jak funguje* a *jak se používá* konkrétní část systému

* **Scenarios**

    * řeší konkrétní cílovou situaci
    * odkazují na více Guides
    * popisují rozhodnutí, návaznosti a praktické kroky

Scénář tedy často:

* kombinuje několik Guides,
* doplňuje je o kontext a doporučený postup,
* upozorňuje na typické chyby nebo alternativy.

---

## Přehled scénářů

Následující scénáře budou postupně rozpracovány:

### Zapojení Krameria do DNNT

* architektonické varianty integrace
* bezpečnostní model a práce s identitou
* konfigurace přístupů a oprávnění
* typické provozní scénáře

👉 **[DNNT zapojeni](DNNT_Integration)**

---

### Nasazení nové instance Krameria

* volba architektury a komponent
* základní konfigurace systému
* napojení na externí služby
* první ověření funkčnosti

---

### Migrace dat mezi instancemi

* příprava zdrojové a cílové instance
* práce s repozitářem a metadaty
* konzistence dat a validace
* řešení chybových stavů

---

### Kombinace bezpečnosti, procesů a konfigurace

* nastavení autentizace a autorizace
* spouštění procesů s různými rolemi
* řízení přístupů k datům
* typické enterprise scénáře

---

## Struktura scénáře

Každý scénář by měl mít jednotnou strukturu:

1. **Cíl scénáře**
2. **Výchozí předpoklady**
3. **Architektonický kontext**
4. **Postup krok za krokem**
5. **Vazby na Guides**
6. **Rizika a časté chyby**
7. **Ověření a provozní poznámky**

---

## Další rozšiřování

Sekce Scenarios je živá dokumentace a bude se rozšiřovat podle:

* reálných projektových zkušeností,
* opakujících se dotazů integrátorů a provozu,
* nových způsobů nasazení Krameria.

Doporučeno číst po seznámení se základní architekturou systému.
