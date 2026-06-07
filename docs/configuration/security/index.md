# Security Administration

Tato část popisuje, jak je autorizační model Krameria spravován v systému.

Nejde o technickou konfiguraci aplikace (properties, docker apod.), ale o **datový model uložený v databázi a spravovaný přes administraci**.

---

## Přehled spravovaných částí

### Role (externí)
Spravované v Keycloak.

### Actions (interní)
Definované v kódu Krameria.

### Criteria (interní / rozšiřitelné)
Implementované v Krameriovi.

### Rights (databáze)
Mapování:

- Role → Action
- Action → Criteria

---

## Admin model

Administrátor definuje:

- které role mají jaké akce
- jaká kritéria se vztahují k akcím

Tato data se ukládají do databáze jako „rights“.

---

## Životní cyklus

1. Role vznikne v Keycloak
2. Role se objeví v Krameriu
3. Admin ji namapuje na akce
4. Přidá kritéria
5. Uloží se do DB
6. Runtime engine to vyhodnocuje