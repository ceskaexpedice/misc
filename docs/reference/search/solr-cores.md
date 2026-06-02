# Solr Cores Reference

Tato stránka poskytuje přehled hlavních Solr jader používaných v systému **Kramerius 7** a jejich účel.

Informace zde jsou určeny pro referenci při konfiguraci a práci se systémem. Pro postup instalace a správy Solr jader viz [Guides: Instalace a správa Solr](../Guides/Instalace-Solr.md).

---

## Solr Cores

Kramerius využívá vyhledávací engin **Solr** a definuje tři hlavní jádra (cores), každé s odlišným účelem:

| Jádro | Popis | Konfigurace |
|-------|-------|-------------|
| `search` | Určeno pro vyhledávání klientskými aplikacemi (veřejné rozhraní i administrace). | `solrSearchHost=http://localhost:8983/solr/search` <br> `solrSearchLogin=__` <br> `solrSearchPassword=__` |
| `processing` | Interní index repozitáře, nahrazuje dřívější resource index. Každý nově importovaný objekt je indexován spolu se svými vazbami. | `solrProcessingHost=http://localhost:8983/solr/processing` |
| `logs` | Slouží pro ukládání informací o přístupu uživatelů, slouží jako zdroj dat pro statistiky a reporty. | - |

> ⚠️ Seznam jáder a jejich účel patří do **Reference**, protože jde o vysvětlení konfigurace Solr v rámci Krameriaus. Samotná instalace Solru a jáder patří do **Guides → Installation**.



## Search Core

- **Účel:** Hlavní vyhledávací jádro pro klientské aplikace (veřejné i administrační rozhraní).
- **Konfigurační parametr:** `solrSearchHost`
- **Popis:**  
  Obsahuje index objektů digitální knihovny, který je použit pro vyhledávání a zobrazování výsledků uživatelům.
- **Příklad hodnoty:** `http://localhost:8983/solr/search`

---

## Processing Core

- **Účel:** Interní index repozitáře, nahrazuje dříve používaný Resource Index Fedory.
- **Konfigurační parametr:** `solrProcessingHost`
- **Popis:**  
  Každý importovaný objekt je indexován v tomto jádře spolu se všemi vazbami. Slouží interně pro správu dat a zpracování.
- **Příklad hodnoty:** `http://localhost:8983/solr/processing`

---

## Logs Core

- **Účel:** Ukládání informací o přístupu uživatelů a zdroj pro statistiky a reporty.
- **Konfigurační parametr:** nemá přímý parametr v `configuration.properties`; přístup přes Solr admin UI.
- **Popis:**  
  Jádro slouží pro sledování aktivit a generování reportů o využívání systému.
- **Instalace:** viz [Guides: Instalace a správa Solr](../Guides/Instalace-Solr.md)

---

> ⚠️ Poznámka: Pro každý upgrade Kramerius nebo Solr může být nutné aktualizovat schéma jádra **search** (soubor `managed-schema`). Pro postup viz [Guides: Aktualizace schématu Search Core](../Guides/Instalace-Solr.md#aktualizace-sch%C3%A9matu-j%C3%A1dro-search).

