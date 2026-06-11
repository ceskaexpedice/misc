# Zakladni pojmy

## Přehled

Kramerius je platforma pro správu, dlouhodobé uchovávání a zpřístupňování digitalizovaných dokumentů.

Systém umožňuje:

- ukládání digitálních objektů a jejich metadat
- správu digitalizovaného obsahu
- indexaci a vyhledávání
- řízení přístupových práv
- zpřístupnění obsahu prostřednictvím REST API
- automatizované zpracování pomocí asynchronních procesů

Tato část dokumentace vysvětluje základní koncepty a pojmy používané napříč celým systémem.

---

## Jak číst dokumentaci

Dokumentace Krameria je rozdělena do několika částí:

| Sekce          | Zaměření |
|----------------|---------|
| Zakladni pojmy | základní pojmy a doménový model |
| Architektura   | vztahy mezi komponentami a datové toky |
| Reference      | technická reference jednotlivých subsystémů |
| Konfigurace    | konfigurace systému |
| Deployment     | nasazení a provoz |
| Navody         | návody a pracovní postupy |

Zakladni pojmy představují společný slovník používaný ve všech ostatních částech dokumentace.

---

## Obsah

### [Kramerius Core](core/index)
Kramerius Core je centrální aplikační vrstva systému Kramerius, která poskytuje REST API, implementuje business logiku a bezpečnost, a zároveň orchestruje spolupráci interních i externích komponent, na kterých je celý systém postaven.

### [Uloziste dokumentu Akubra](akubra/index)
Digitalni dokumenty, metadata, sbirky

### [Vyhledavani](search/index)
Indexace dat, dotazovací API, fulltextového vyhledávání.

### [Zabezpeceni](security/index)
Aplikacni zabezpeceni, autentizace, autorizace

### [Asynchronni procesy](process-platform/index)
Asynchronni procesy, framework na sousteni a provadeni procesu

### [REST API](api/index)
Veřejné i interní REST API

### [CDK](cdk/index)
Česká digitální knihovna (CDK) je centrální agregační a přístupová vrstva nad více nezávislými instancemi systému Kramerius. 

---

## Navazujici dokumentace

- ➡️ [Zaciname](../getting-started)
- ➡️ [Architektura](../architecture)
- ➡️ [Reference](../reference)
- ➡️ [Konfigurace](../configuration)
- ➡️ [Deployment](../deployment)
- ➡️ [Navody](../guides)
