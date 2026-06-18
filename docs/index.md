# 📚 Kramerius – Dokumentace

Vítejte v dokumentaci systému **Kramerius**.

Kramerius je modulární platforma pro správu, ukládání a zpřístupnění digitálních knihovních dokumentů.

---

## 🔍 Hledání v dokumentaci

Najděte odpověď okamžitě pomocí vyhledávání nebo AI asistenta.

```text
🔎 Hledat v dokumentaci...
```

> Tip: Můžete hledat „jak importovat dokument“, „co je metadata“, „problém s indexací“ apod.

---

## 🎯 Co chcete dělat?

Vyberte si oblast podle svého cíle.

---

## 👤 Kurátor / práce s dokumenty

Práce s digitálními dokumenty, sbírkami a jejich zpracováním.

👉 🛠️ **[Návody pro kurátory](guides/curator/index)**
- import dokumentů
- indexace
- práce se sbírkami
- sledování procesů

👉 🧠 **[Doménové pojmy](domain-concepts/index)**
- dokument
- metadata
- sbírka
- licence
- import

👉 🎯 **[Scénáře](scenarios/index)**
- zapojeni do DNNT

---

## ⚙️ Administrátor / provoz systému

Správa systému, procesů a konfigurace.

👉 🛠️ **[Návody pro administrátora](guides/admin/index)**
- monitoring procesů
- správa běžících úloh
- konfigurace systému

👉 ⚙️ **[Konfigurace](configuration/index)**
- nastavení Krameria
- indexace
- storage a úložiště

👉 🚢 **[Deployment](deployment/index)**
- nasazení systému
- runtime prostředí
- Tomcat / služby

---

## 👨‍💻 Vývojář / integrace

Integrace, API a interní fungování systému.

👉 📖 **[Reference](reference/index)**
- REST API
- datové modely
- formáty (FOXML, METS)

👉 ⚙️ **[Technické koncepty](core-concepts/index)**
- Akubra
- procesní platforma
- indexace
- security model

👉 🧩 **[Architektura](architecture/index)**
- komponenty systému
- vazby mezi moduly

---

## 🧭 Rychlé vstupy

Pokud víte, co hledáte:

- 📚 [Doménové pojmy](domain-concepts/index)
- ⚙️ [Technické koncepty](core-concepts/index)
- 🛠️ [Návody](guides/index)
- 📖 [Reference](reference/index)

---

## 🧩 Co je Kramerius

Kramerius je open-source systém pro správu a zpřístupnění digitálních knihovních sbírek.

Používá se pro:

- digitalizované knihy a periodika
- mapy, hudebniny a archivní materiály
- born-digital dokumenty

Klíčové vlastnosti:

- dlouhodobé úložiště digitálních objektů (Akubra)
- indexace a vyhledávání (Solr)
- řízení importních a dávkových procesů
- správa přístupových práv
- REST API
- klientské aplikace (administrace + čtení)

Jádro systému běží jako Java aplikace v Tomcatu a tvoří integrační vrstvu nad jednotlivými komponentami.

---

## 🔧 Přispívání

Dokumentace se vyvíjí spolu se systémem Kramerius.

Struktura je navržena tak, aby:

- byla stabilní v čase
- podporovala různé role uživatelů
- umožňovala rozšiřování systému bez redesignu dokumentace  