# Security databáze v Kramerius

## Přehled

Kramerius používá vlastní PostgreSQL databázi pro ukládání autorizačních dat.

Tato databáze doplňuje externí autentizační systém (Keycloak) o interní bezpečnostní model Krameria.

Databáze obsahuje zejména:

- interní reprezentaci uživatelů
- role
- oprávnění
- access rules
- autorizační kritéria
- vazby mezi rolemi a akcemi

---

## Oddělení autentizace a autorizace

Bezpečnostní model Krameria je rozdělen na dvě části:

| Vrstva | Odpovědnost |
|---|---|
| Keycloak | autentizace uživatele |
| Security databáze | autorizace a access rules |

Keycloak tedy neobsahuje kompletní bezpečnostní model systému.

---

## Základní princip

Po autentizaci uživatele:

1. Kramerius validuje token
2. vytvoří Security Context
3. načte interní autorizační pravidla z PostgreSQL
4. vyhodnotí přístupová oprávnění

---

## Tabulka user_entity

Tabulka `user_entity` obsahuje interní reprezentaci uživatelů.

Nejde o primární identity provider.

Tabulka slouží zejména pro:

- evidenci uživatelů, kteří se alespoň jednou přihlásili
- interní vazby na role a oprávnění
- práci autorizační vrstvy

Uživatel vzniká typicky při prvním úspěšném přihlášení.

---

## Tabulka right_entity

Tabulka `right_entity` představuje centrální část autorizačního modelu.

Obsahuje definice:

- akcí
- oprávnění
- vazeb na role
- vazeb na autorizační kritéria

Typické příklady akcí:

- čtení dokumentu
- administrativní operace
- export
- správa objektů

---

## Autorizační kritéria

Oprávnění mohou být podmíněna kritérii.

Kritérium může reprezentovat například:

- licenci dokumentu
- typ dokumentu
- dostupnost obsahu
- příslušnost uživatele
- institucionální omezení

---

## Role a access rules

Autorizace v Krameriu není založena pouze na jednoduchém RBAC modelu.

Výsledné rozhodnutí může kombinovat:

- role uživatele
- licence
- atributy identity
- autorizační kritéria
- vlastnosti dokumentu

---

## Runtime vyhodnocení

Při vyhodnocení přístupu Kramerius kombinuje:

- informace z tokenu
- interní role
- data ze security databáze
- metadata objektu
- autorizační kritéria

Výsledkem je access decision pro konkrétní operaci.

---

## Logický model

Zjednodušený model:

User
↓
Roles
↓
Rights
↓
Criteria
↓
Access decision

---

## Důležitá poznámka

Skutečný databázový model obsahuje více tabulek a vazeb.

Tento dokument popisuje pouze základní architektonický model bezpečnostní vrstvy.

Detailní databázová struktura může být popsána samostatně.

---

## Vztah k dalším dokumentům

- `authentication/overview.md`
- `authentication/token-model.md`
- `authorization/role-model.md`
- `authorization/access-rules.md`

---

## Shrnutí

Kramerius používá vlastní PostgreSQL autorizační model nad rámec Keycloak autentizace.

Výsledná autorizace kombinuje:

- identity z tokenu
- interní role
- access rules
- autorizační kritéria
- metadata dokumentů