# REST API – Návody pro vývojáře a integrátory

## Pro koho je tato stránka
Tato stránka je určena pro **vývojáře a integrátory**, kteří chtějí napojit Kramerius na jiné systémy nebo vyvíjet moduly.  
Pokud hledáte pouze koncepty, vraťte se na [Getting Started – Vývojář](../getting-started/developer).

---

## 1. Přehled REST API
- Kramerius poskytuje REST API pro přístup k datům a procesům
- Endpoints jsou rozděleny podle modulů (Core, Akubra, Solr, Process Framework)
- Autentizace přes tokeny a role (viz [Security Model](Core_Concepts_Security.md))

---

## 2. Typické scénáře
- Vyhledávání dokumentů a knih
- Přístup k metadatům a souborům
- Spouštění procesů (import, export, hromadné operace)
- Správa uživatelů a rolí (omezeno na administrátory)

---

## 3. Testování a integrace
- Přístup k API přes Postman nebo CURL
- Ověření tokenů a oprávnění
- Sledování logů a chybových kódů

> Detailní parametry, endpointy a request/response payloady viz [Reference – REST API](../reference/API)

---

## 4. Doporučené postupy
- Používat minimální oprávnění pro tokeny
- Oddělit testovací a produkční prostředí
- Auditovat volání API a sledovat logy

---

## 5. Kde pokračovat dál
- [Reference – REST API](../reference/API) – kompletní seznam endpointů a parametrů
- [Getting Started – Vývojář](../getting-started/developer) – návrat na startovní stránku
