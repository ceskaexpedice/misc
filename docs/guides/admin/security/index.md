[Index](../../../index) / [Navody](../../../guides) / [Administrator](..)

# Bezpečnost – Návody pro administrátora

## 1. Přihlášení a správa uživatelů
- Konfigurace připojení k centrálnímu IdP (např. Keycloak)
- Vytváření a správa uživatelských účtů
- Přiřazování rolí uživatelům
- Testování přihlášení do UI klientů

---

## 1. Keycloak set up, service account
- ➡️ [TODO Keycloak](Keycloak)
- ➡️ [TODO Keycloak eduid](Keycloak-a-eduID)
- ➡️ [TODO Keycloak Service Account](KeycloakServiceAccount)


Tento návod popisuje základní vývojové nastavení Keycloaku pro použití s Krameriem.

Předpoklady
běžící instance Krameria, Java runtime, lokální vývojové prostředí

1. Stažení a spuštění Keycloaku
Stáhněte distribuční balíček Keycloaku a rozbalte jej.
Spusťte server s port offsetem, aby nedošlo ke kolizi s Krameriem:
Keycloak poběží na portu 8083
je povolena možnost nahrání skriptů do realmu

2. Inicializace administrátorského účtu
Po prvním spuštění:
otevřete administrační rozhraní Keycloaku
vytvořte administrátorský účet
přihlaste se do admin konzole

3. Konfigurace realmu a klienta
V administrační konzoli:
vytvořte realm kramerius
vytvořte klient krameriusClient
doporučený typ: public (client authentication disabled)

4. Uživatelé a role
Vytvořte následující role:
common_users
public_users
kramerius_admin
k4_admins
Vytvořte uživatele (např. krameriusAdmin) a přiřaďte jim odpovídající role.
Volitelně lze nakonfigurovat externí identity providery (Shibboleth, Facebook, …).

5. Použití token proxy endpointu
Kramerius poskytuje endpoint pro získání access tokenu:
URL: search/api/auth/token
metoda: POST

V těle požadavku jsou předány přihlašovací údaje uživatele.

---


## 2. Role a oprávnění
- Přehled základních rolí: čtenář, kurátor, admin, projektový manažer, vývojář
- Jak přiřadit práva k modulům a procesům
- Nastavení minimálních oprávnění (princip least privilege)

> Diagram rolí a přístupů naleznete v [Core Concepts – Security Model](core-concepts/Security)

---

## 3. Bezpečnostní scénáře
- **Nový uživatel**: registrace, role, první přihlášení
- **Audit přístupu**: kontrola logů a událostí
- **Revokace práv**: jak odebrat oprávnění uživateli nebo roli
- **Provozní kontrola**: kontrola správného nastavení API a UI klientů

> Každý scénář má odkaz na detailní návody v Reference.

---

## 4. Doporučené postupy
- Používejte centrální IdP pro všechny role
- Pravidelně kontrolujte přístupové logy
- Oddělujte administrativní a uživatelské role
- Minimální oprávnění pro každou roli

---

## 5. Kde pokračovat dál
- [Reference – Security](../reference/Security) – kompletní seznam proměnných, tokenů a oprávnění
- [Core Concepts – Security Model](core-concepts/Security) – koncepty a principy
- [Getting Started – Administrátor](../getting-started/admin) – návrat na startovní stránku role  

