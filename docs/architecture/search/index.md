[Index](../../index) / [Architektura](../../architecture)

# Indexing subsystémy

```text
Repository
│
Indexer
│
Solr Index
│
Search API
│
Web Client
```


Kramerius používá několik nezávislých indexačních subsystémů, které pokrývají různé části systému:

- Search index (fulltext nad Fedora objekty)
- Processing model (RELS-EXT / Akubra interní stav)
- Logs index (audit a systémové události)
- Monitor index TODO
- sdnnt-sync index TODO

Všechny tyto subsystémy sdílejí společné principy:

- asynchronní aktualizace
- eventual consistency
- transformace dat z repozitáře
- závislost na indexačních pipeline

---

## Společné vlastnosti

### Eventual consistency
Všechny indexy mohou být dočasně nekonzistentní vůči repozitáři.

---

### Asynchronní zpracování
Změny v repozitáři jsou zpracovány přes queue/pipeline.

---

### Transformace dat
Data z repozitáře nejsou ukládána přímo, ale transformována do specializovaných modelů.

---

### Build-time struktura indexů

Indexy jsou částečně definovány build procesem:

- generování Solr schema
- příprava indexových struktur
- kopírování Solr core konfigurací

Viz:
→ Reference / Build System / Solr Schema

---

## Solr jako společná infrastruktura

Více indexů může sdílet:

- jednu Solr instanci
- nebo SolrCloud cluster
- různé cores / collections

Konkrétní konfigurace je popsána v:
→ Reference / Deployment / Solr

---

## Přehled indexů

### Search index
Fulltextové vyhledávání nad Fedora objekty.

→ Reference / Search / Search

---

### Processing model
Interní model RELS-EXT a Akubra vztahů.

→ Reference / Search / Processing

---

### Logs index
Audit a systémové události.

→ Reference / Search / Logs

# Vyhledavani


---

## Navazujici dokumentace

- ➡️ [Reference](../../reference/search)
