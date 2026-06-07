# Security Administration Model

Tato část popisuje, jak se bezpečnostní model Krameria nastavuje a spravuje v běžícím systému.

Na rozdíl od technické konfigurace (properties, deployment) jde o **datový model uložený v databázi a externím identity provideru**.

---

## Co je spravováno externě (Keycloak)

- uživatelé
- role
- autentizace (login, tokeny)

Kramerius tato data pouze využívá.

---

## Co je spravováno v Krameriu

Kramerius obsahuje administrační model pro:

- mapování rolí na akce
- přiřazení kritérií k akcím
- definici oprávnění (rights)

Tato data jsou uložena v databázi.

---

## Základní entity

### Role (externí)
Role pochází z Keycloaku a nejsou v Krameriu definovány.

### Actions (interní)
Akce jsou pevně definované v kódu Krameria.

### Criteria (interní + konfigurovatelné)
Kritéria mohou být:
- pevně implementovaná
- nebo konfigurovatelná (např. rozsahy IP, licence)

### Rights (DB model)
Rights definují vztah:

```text
Role + Action + Criteria
```

---

## Admin model

V administrátorském klientovi se nastavuje:

- které role mají přístup k jakým akcím
- jaká kritéria se k akci vztahují

Výsledkem je záznam v databázi.

---

## Životní cyklus konfigurace

1. Role vznikne v Keycloaku
2. Role se objeví v Krameriu
3. Administrátor ji namapuje na akce
4. Přidají se kritéria
5. Uloží se do DB
6. Runtime engine je používá při rozhodování