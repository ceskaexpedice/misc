[Index](../../../index) / [Reference](../../../reference) / [Search](../../search) 

# Vyhledávání (Search)

Vyhledávání je subsystém systému Kramerius, který poskytuje fulltextové a strukturované vyhledávání nad indexovanými digitálními objekty (Fedora repository model).

Vyhledávání pracuje nad indexem v Apache Solr, který je generován a udržován jako samostatná část systému.

---

## Přehled

Popis aktuální podoby schématu: [Google spreadsheet](https://docs.google.com/spreadsheets/d/1DoDnSIGPqPnYbb0U2RSNLKm9eAY2FQNimJyTPeQsC2A/edit#gid=0)

Search subsystém je zodpovědný za:

- fulltextové vyhledávání nad indexovanými objekty
- strukturované filtrování podle metadat
- fasetovou navigaci
- poskytování výsledků pro API a UI

Search pracuje nad předem připraveným indexem, který vzniká z repozitářových dat.

---

## Co Search NENÍ

Pro vyjasnění odpovědnosti:

Search **nezahrnuje**:

- ❌ proces indexace a transformace dat z repozitáře
- ❌ RELS-EXT logiku a Akubra processing
- ❌ auditní logování
- ❌ Solr deployment a škálování
- ❌ build-time generování Solr schémat

---

## Search model

Search index reprezentuje digitální objekty z repozitáře:

- monografie
- periodika
- ročníky / čísla
- stránky
- sbírky

Každý objekt je převeden do Solr dokumentu obsahujícího:

- metadata
- fulltext (pokud existuje)
- strukturu a hierarchii
- vazby na rodiče a potomky

---

## Hierarchie objektů

Index respektuje hierarchii repozitáře:

- Sbírka
    - Periodikum
        - Ročník
            - Číslo
                - Stránka

- Monografie
    - Stránka

Hierarchie je reflektována v indexu pro účely navigace a filtrování.

---

## Indexové schéma (Solr)

Search je postaven nad Solr schématem, které definuje indexovaná pole.

### Příklady polí

| Pole | Typ | Význam |
|------|-----|--------|
| `id` | string | unikátní identifikátor objektu |
| `title` | text | název objektu |
| `author` | string | autor nebo tvůrce |
| `fulltext` | text | plný text obsahu |
| `type` | string | typ objektu |
| `parent_id` | string | nadřazený objekt |
| `path` | string | hierarchická cesta |
| `created_at` | date | čas vytvoření |
| `license` | string | licence objektu |

### Poznámky

- Solr schema je součástí systémového kontraktu
- změny schema vyžadují reindexaci
- schema je generováno build procesem (viz Build System)

---

## Model dotazování

Search podporuje:

### Fulltext
- vyhledávání v `title` a `fulltext`

### Strukturované filtry
- typ objektu
- metadata
- hierarchie

### Fasety
- typy objektů
- autoři
- sbírky
- roky

---

## API rozhraní

Search je zpřístupněn přes REST API.

Viz:
→ Reference / API / Search

Tato sekce popisuje pouze vyhledávací model, nikoliv konkrétní endpointy.

---

## Konfigurace

Search je řízen systémovou konfigurací.

Typické parametry:

- `solr.url` – adresa Solr instance nebo clusteru
- `solr.core` – název indexu
- `search.timeout` – timeout dotazů
- `search.facet.limit` – limit faset

Viz:
→ Reference / Configuration / Search

---

## Solr a deployment

Search využívá Apache Solr jako indexační backend.

Detaily provozu Solr (cluster, škálování, replikace) nejsou součástí Search modelu.

Viz:
→ Reference / Deployment / Solr

---

## Indexační pipeline (externí subsystém)

Indexace dat **není součástí Search**, ale je zajištěna samostatným subsystémem:

- Processing (Akubra / RELS-EXT logika)
- indexační pipeline
- synchronizace změn z repozitáře

Search pouze pracuje s výsledným indexem.

---

## Build systému indexu (externí)

Solr schema a index struktura jsou generovány při build procesu.

Tato oblast zahrnuje:

- generování `managed-schema`
- transformaci schema pro různé Solr environmenty
- kopírování Solr core konfigurací

Viz:
→ Reference / Build System / Solr Schema

---

## Konzistence

Search není silně konzistentní s repozitářem.

- index je aktualizován asynchronně
- mohou nastat dočasné nekonzistence
- plná reindexace obnovuje konzistentní stav

---

## Shrnutí

Search je subsystém Krameria zodpovědný za:

- vyhledávání nad indexovanými daty
- práci nad Solr indexem
- poskytování query a filtrů

Search **neřeší**:
- indexaci dat
- RELS-EXT / Processing logiku
- audit / logy
- deployment Solr
- build indexu

