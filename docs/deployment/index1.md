# Runtime topologie Kramerius

## Přehled

Kramerius je distribuovaný systém složený z více samostatných služeb.

Systém zahrnuje:

- aplikační backend
- vyhledávací vrstvu
- image server
- autentizační infrastrukturu
- process platform
- worker služby
- PostgreSQL databáze
- distribuované locking služby

---

## Hlavní komponenty

| Komponenta | Účel |
|---|---|
| Kramerius | hlavní aplikační backend |
| Solr | fulltextové vyhledávání a index |
| Keycloak | autentizace a identity management |
| PostgreSQL | persistence aplikačních dat |
| Image Server | poskytování obrazových dat |
| Process Manager | orchestrace procesů |
| Worker služby | background processing |
| Hazelcast Lock Server | distribuované locky |
| Memcached | cache vrstva |

---

## Hlavní backend

Služba `kramerius` představuje hlavní backend systému.

Zodpovídá za:

- REST API
- autorizaci
- práci s repository
- vyhledávání
- komunikaci s image serverem
- business logiku

Backend běží v Tomcat kontejneru.

---

## Vyhledávací vrstva

Kramerius používá Apache Solr jako vyhledávací a indexační vrstvu.

Solr obsahuje:

- fulltextový index
- metadata dokumentů
- facety
- search konfiguraci

Backend komunikuje se Solr serverem přes HTTP API.

---

## Image server

Image infrastruktura je rozdělena na dvě části:

| Služba | Účel |
|---|---|
| iipimage | image processing backend |
| imageserver | nginx proxy pro image data |

Image server poskytuje:

- tiled rendering
- zoom
- IIIF endpointy
- transformace obrazových dat

---

## Audio server

Služba `audioserver` poskytuje audio obsah přes nginx.

Obsah je publikován přímo ze storage vrstvy.

---

## Security infrastruktura

Autentizace je zajištěna pomocí:

- Keycloak
- PostgreSQL databáze Keycloak

Keycloak poskytuje:

- OIDC autentizaci
- Bearer tokeny
- federaci identity
- role management

---

## PostgreSQL databáze

Systém používá více samostatných PostgreSQL databází.

| Databáze | Účel |
|---|---|
| krameriusPostgres | aplikační data |
| keycloakPostgres_eduid | identity management |
| processPostgres | process platform |

---

## Backup služby

PostgreSQL databáze mají samostatné backup kontejnery.

Backup služby:

- pravidelně vytvářejí dump databází
- uchovávají historické zálohy
- používají plánované cron-like schedulery

---

## Distribuované locky

Služba `lock_server` poskytuje distribuované lockování pomocí Hazelcast.

Použití:

- synchronizace workerů
- koordinace procesů
- prevence paralelního zpracování

---

## Process Platform

Background processing je odděleno od hlavního backendu.

Process platform se skládá z:

| Komponenta | Účel |
|---|---|
| processManager | orchestrace procesů |
| curatorWorker | kurátorské procesy |
| publicWorker | veřejné procesy |

---

## Worker model

Worker služby:

- periodicky pollují Process Manager
- získávají tasky
- vykonávají background processing
- pracují nezávisle na hlavním backendu

---

## Sdílené storage

Více služeb sdílí společné mounted volumes.

Typicky:

- importní data
- image data
- audio data
- logy
- temporary files

---

## Persistence vrstvy

Persistentní storage zahrnuje:

- PostgreSQL data
- Solr indexy
- image data
- audio data
- konfigurace
- logy

---

## Networking model

Služby komunikují přes Docker interní síť.

Některé služby publikují porty externě:

| Služba | Port |
|---|---|
| Kramerius | 8088 |
| Solr | 8983 |
| Keycloak | 8990 |
| Process Manager | 8082 |
| Workers | 8084 / 8086 |
| Image server | 8888 |

---

## Health checks

Vybrané služby používají health checks:

- Solr
- PostgreSQL
- Keycloak

Tyto kontroly slouží pro:

- startup orchestration
- restart management
- dependency readiness

---

## Startup závislosti

Služby používají `depends_on` pro řízení pořadí startu.

Například:

Kramerius backend závisí na:

- Solr
- Keycloak
- PostgreSQL
- image serverech
- cache vrstvě

---

## Horizontální oddělení systému

Architektura odděluje:

| Vrstva | Komponenty |
|---|---|
| Presentation | UI aplikace |
| API | Kramerius backend |
| Search | Solr |
| Security | Keycloak |
| Processing | Process Platform |
| Media | Image server |
| Persistence | PostgreSQL |

---

## Architektonický model

Zjednodušený model:

UI
↓
Kramerius API
↓
Search / Security / Repository / Image services
↓
Storage + PostgreSQL

---

## Shrnutí

Kramerius používá modulární distribuovanou architekturu založenou na samostatných službách.

Jednotlivé komponenty jsou odděleny podle odpovědností:

- autentizace
- vyhledávání
- processing
- persistence
- image serving
- orchestrace procesů