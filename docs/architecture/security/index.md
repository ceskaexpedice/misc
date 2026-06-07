# 🔐 Architektura zabezpečení

Bezpečnostní model Krameria je rozdělen na dvě samostatné části:

- **Autentizace** – ověření identity uživatele.
- **Autorizace** – vyhodnocení oprávnění pro konkrétní operaci.

Kramerius deleguje autentizaci na externího poskytovatele identity (Identity Provider), typicky Keycloak. Po úspěšném přihlášení provádí vlastní autorizaci nad rolemi, akcemi a kritérii.

## Přehled architektury

```text
+--------+
| Browser|
+--------+
     |
     | Login
     v
+-----------+
| Keycloak  |
+-----------+
     |
     | Access Token (JWT)
     v
+-----------+
| Kramerius |
+-----------+
     |
     +--> Authentication Layer
     |
     +--> Authorization Layer
     |
     +--> Business Services
```

## Hlavní komponenty

### Identity Provider

Externí systém odpovědný za:

- autentizaci uživatelů,
- správu účtů,
- správu rolí,
- vydávání tokenů.

Kramerius nepřistupuje přímo k uživatelské databázi.

### Authentication Layer

Vrstva odpovědná za:

- validaci tokenu,
- získání identity uživatele,
- načtení rolí z tokenu.

Výstupem je autentizovaný uživatel dostupný během zpracování požadavku.

### Authorization Layer

Vrstva odpovědná za:

- vyhodnocení požadované akce,
- získání oprávnění z konfigurace Krameria,
- vyhodnocení kritérií,
- rozhodnutí Permit / Deny.

### Business Services

Vlastní aplikační logika Krameria.

Každá chráněná operace deklaruje požadovanou akci, kterou musí uživatel splňovat.

## Související kapitoly

- [Autentizace](authentication/)
- [Autorizace](authorization/)