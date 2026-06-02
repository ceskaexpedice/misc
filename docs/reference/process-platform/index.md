# Zpracování (Processing)

Subsystém Processing je zodpovědný za asynchronní vykonávání systémových operací, jako je indexace, import a údržbové úlohy.

Je postaven nad externí platformou Process Platform (PCP), která poskytuje infrastrukturní část (manager, worker nody, lifecycle, plánování).

Kramerius nad touto platformou definuje vlastní procesy a workery.

Viz:
→ dokumentace Process Platform (externí projekt)

---

## Přehled

Processing zajišťuje:

- propagaci změn z repozitáře do odvozených dat (např. vyhledávací index)
- asynchronní vykonávání dlouhotrvajících operací
- řízené a spolehlivé spouštění systémových úloh

Processing je klíčová část systému a přímo ovlivňuje:

- Vyhledávání (Search)
- konzistenci dat
- výkon systému

---

## Architektura

Processing v Krameriu se skládá z:

- Process Platform (externí framework)
- Kramerius workerů (běhové jednotky)
- Kramerius procesů (doménové operace)

---

## Process Platform (PCP)

Vykonávání procesů zajišťuje Process Platform.

Ta zahrnuje:

- manager node (plánování a koordinace procesů)
- worker nody (vykonávací jednotky)
- stavový model procesů
- REST API pro správu procesů

Kramerius tuto funkcionalitu neimplementuje, ale používá ji jako běhovou závislost.

Viz:
→ dokumentace Process Platform

---

## Kramerius workery

Kramerius definuje vlastní worker aplikace nad PCP.

Worker je typicky distribuován jako kontejnerový image a obsahuje:

- PCP runtime (např. Tomcat + REST API)
- sadu pluginů definujících konkrétní procesy Krameria

Příklad:
- CuratorWorker

Worker je zodpovědný za vykonávání konkrétních typů procesů.

V systému může běžet více worker instancí paralelně.

---

## Kramerius procesy

Procesy reprezentují konkrétní doménové operace.

Typické procesy:

- Import
- Index
- Reindex
- údržbové operace nad daty

Každý proces:

- je vykonáván asynchronně
- běží ve workeru
- ovlivňuje repozitář a/nebo odvozená data (např. index)

---

## Vztah k vyhledávání

Processing zajišťuje aktualizaci vyhledávacího indexu.

- Search (Vyhledávání) data čte
- Processing data zapisuje / aktualizuje

Aktualizace indexu probíhá prostřednictvím asynchronních procesů.

Viz:
→ Reference / Search

---

## Model vykonávání

Procesy jsou:

- plánovány přes Process Platform
- vykonávány asynchronně
- zpracovávány workery

To znamená:

- eventual consistency mezi repozitářem a indexem
- zpožděné projevení změn v systému

---

## Reindexace

Reindexace je speciální typ procesu, který slouží k:

- znovuvytvoření vyhledávacího indexu
- obnovení konzistence dat
- aplikaci změn ve schématu nebo datovém modelu

Reindexace může probíhat nad:

- jednotlivým objektem
- podstromem objektů
- celým repozitářem

---

## Build a deployment

Kramerius definuje workery a procesní pluginy při buildu.

- worker image obsahuje konkrétní procesy
- každý worker poskytuje určitou funkcionalitu

Nasazení workerů je popsáno v:

→ Reference / Deployment / Processing

---

## Shrnutí

Subsystém Processing:

- vykonává asynchronní operace systému
- je postaven nad Process Platform
- definuje konkrétní procesy a workery Krameria
- zajišťuje aktualizaci odvozených dat (např. vyhledávací index)

Představuje „write“ část systému vůči subsystémům jako je Search.