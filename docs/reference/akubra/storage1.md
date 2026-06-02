# Storage Reference

Tato stránka slouží jako **referenční dokumentace** k úložným komponentám systému Kramerius. Obsahuje **úplný a přesný popis pojmů, konfiguračních parametrů a technických detailů**, které se vztahují ke storage vrstvě.

> ⚠️ Tato stránka **neobsahuje instalační ani provozní návody**. Postupy typu „jak to nastavit“ patří do sekce **Guides / Deployment**.

---

## Přehled komponent

| Komponenta            | Popis                                 |
| --------------------- | ------------------------------------- |
| **Akubra repository** | Primární úložiště digitálních objektů |
| **LegacyFS**          | Historické filesystemové úložiště     |
| **Solr index**        | Vyhledávací a indexační databáze      |

Podrobnější konceptuální vysvětlení vztahů mezi těmito komponentami je uvedeno v **Core Concepts → Storage**.

---

## Akubra Repository

### Základní pojmy

| Pojem            | Význam                                                        |
| ---------------- | ------------------------------------------------------------- |
| **Object**       | Logická jednotka uložená v Akubře (např. monografie, stránka) |
| **Datastream**   | Konkrétní datový proud objektu (např. OCR, IMAGE)             |
| **Storage path** | Fyzické umístění dat na disku                                 |

### Konfigurační parametry

| Parametr                 | Význam                   | Příklad                  |
| ------------------------ | ------------------------ | ------------------------ |
| `akubra.repository.type` | Typ úložiště             | `filesystem`             |
| `akubra.repository.root` | Kořenový adresář dat     | `/data/kramerius/akubra` |
| `akubra.repository.id`   | Identifikátor repository | `kramerius-akubra`       |

> Význam a použití těchto parametrů v konkrétních scénářích je popsán v **Guides → Storage Setup**.

---

## LegacyFS

LegacyFS představuje historický způsob ukládání digitálních objektů do filesystemu.

### Vlastnosti

* strukturované adresáře dle PID
* přímý přístup k souborům
* používáno ve starších verzích Krameria

### Konfigurační parametry

| Parametr           | Význam                                |
| ------------------ | ------------------------------------- |
| `legacyfs.root`    | Kořenový adresář legacy dat           |
| `legacyfs.enabled` | Povolení legacy režimu (`true/false`) |

---

## Solr Index (Storage pohled)

Tato kapitola popisuje **storage-related aspekty Solr indexu**, nikoliv dotazování.

### Jádra / kolekce

| Název       | Účel                     |
| ----------- | ------------------------ |
| `kramerius` | Hlavní vyhledávací index |

### Konfigurační parametry

| Parametr                    | Význam                           |
| --------------------------- | -------------------------------- |
| `solrHost`                  | URL Solr endpointu               |
| `solrSearch.useCompositeId` | Použití složeného identifikátoru |

> Detailní popis indexovaných polí je uveden v **References → Search Index Fields**.

---

## Vazby na další části dokumentace

* **Core Concepts → Storage** – vysvětlení architektury a role storage
* **Guides → Deployment / Storage** – praktické návody (On‑prem, Docker, Kubernetes)
* **References → Search** – dotazování a práce s indexem

---

## Zásady této referenční stránky

* kompletnost (všechny relevantní parametry a pojmy)
* technická přesnost
* žádné postupy ani scénáře
* odkazy na Guides místo návodů
