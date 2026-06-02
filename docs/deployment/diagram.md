# Diagram

Kramerius jadro je dodáván jako **WAR soubor**, který běží v aplikačním serveru **Tomcat**. Aplikace využívá několik externích a interních modulů pro správu dat, vyhledávání, autentizaci a orchestrace procesů.

```mermaid
flowchart TB
  subgraph Tomcat
    KrameriusWAR["Kramerius WAR (Tomcat)"]
  end

  KrameriusWAR -->|využívá| PostgreSQL["PostgreSQL\n(metadata + access rights)"]
  KrameriusWAR -->|vyhledávání| Solr["Solr (search, processing, logs)"]
  KrameriusWAR -->|spouští procesy| ProcFramework["Procesní framework"]
  ProcFramework -->|používá| Akubra["Akubra Storage\n(object & datastream)"]
  KrameriusWAR -->|používá| Akubra
  Akubra -->|využívá| Hazelcast["Hazelcast Server\n(distributed locking)"]
  KrameriusWAR --> IIIF["IIIF Image Server"]
  KrameriusWAR --> Keycloak["Keycloak\n(authentication)"]
```

