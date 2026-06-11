# 📖 Reference

Tato kapitola obsahuje technickou referenci jednotlivých částí systému. Každá podkapitola popisuje konkrétní modul, jeho rozhraní, konfiguraci a způsob použití.
# Reference

Reference obsahuje technický popis systému Kramerius z hlediska jeho chování a provozu.

Slouží dvěma hlavním skupinám uživatelů:

- **vývojáři**, kteří potřebují znát technické chování API a interních komponent
- **administrátoři a provozovatelé**, kteří potřebují informace pro provoz systému

---

## Struktura Reference

Reference je rozdělena do dvou oblastí:

### System Reference
Popisuje technické chování systému a jeho komponent.

Například:
- REST API Kramerius Core
- chování vyhledávání (Search)
- bezpečnostní model (Security)
- integrace s Akubra a dalšími systémy

### Operations Reference
Popisuje provozní aspekty systému.

Například:
- logging
- monitoring
- backup a restore
- troubleshooting
- provozní DevOps nástroje
---

## System

### [Core](core/index)
TODO.

### [Akubra](akubra/index)
Modul pro práci s digitálním obsahem a správu repozitářů. Obsahuje pravidla pro ukládání, verzování a manipulaci s daty.

### [API](api/index)
Dokumentace veřejného i interního API. Popisuje dostupné endpointy, formáty požadavků a odpovědí a autentizační mechanismy.

### [CDK](cdk/index)
Infrastructure-as-code vrstva pro definici a správu cloudových zdrojů. Zahrnuje deploymenty a konfigurace prostředí.

### [Client](client/index)
Referenční popis klientské aplikace pro koncové uživatele. Obsahuje architekturu, integrace a základní chování UI.

### [Client Admin](client-admin/index)
Administrátorské rozhraní klientské aplikace. Slouží ke správě uživatelů, oprávnění a systémových nastavení.

### [Distributed Locks](distributed-locks/index)
Mechanismy pro distribuované zamykání v rámci clusteru. Popis implementace a použití pro synchronizaci procesů.

### [Image Server](image-server/index)
Služba pro ukládání, zpracování a poskytování obrázků. Obsahuje API pro transformace a optimalizaci.

### [Process Platform](process-platform/index)
Jádro systému pro správu a vykonávání procesů. Popis workflow, plánování a komunikace mezi komponentami.

### [Search](search/index)
Vyhledávací modul. Indexace dat, dotazovací API a konfigurace fulltextového vyhledávání.

### [Security](security/index)
Bezpečnostní model systému. Autentizace, autorizace, správa tokenů a bezpečnostní politiky.

### [Statistics](statistics/index)
Modul pro sběr a vyhodnocování statistik. Reporty, agregace dat a analytické výstupy.

## Operations

### [Monitoring](monitoring/index)
Systém pro sledování stavu aplikací a infrastruktury. Metriky, logy, alerty a dashboardy.

### [DevOps](devops/index)
Procesy a nástroje pro CI/CD, nasazování, monitoring buildů a správu provozního prostředí.

### [Zalohovani](backup/index)
TODO


