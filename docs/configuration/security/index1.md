# Security Model

Security v Krameriu je tvořena kombinací:

- externí identity správy (Keycloak)
- interního autorizačního modelu
- aplikačního vyhodnocovacího enginu

Nejde o klasickou konfiguraci, ale o **runtime model řízení přístupu**.

---

## Přehled vrstev

```text
Keycloak (Identity Provider)
        ↓
Roles (external identity layer)
        ↓
Kramerius Authorization Model (DB)
        ↓
Actions + Criteria
        ↓
Access Decision Engine
```

---

## Co je součást modelu

### 1. Role (externí)
- spravované v Keycloak
- reprezentují uživatele a skupiny

### 2. Actions (interní, pevné)
- definované v kódu
- reprezentují oprávnění

### 3. Criteria (interní + rozšiřitelné)
- IP restrikce
- licence
- objektová pravidla

### 4. Rights (persistované mapování)
- Role → Action
- Action → Criteria

uložené v databázi

---

## Jak se model používá

1. uživatel se přihlásí (Keycloak)
2. získá role
3. Kramerius načte rights z DB
4. role se mapují na actions
5. actions se vyhodnocují proti criteria
6. vznikne rozhodnutí (permit/deny)

---

## Důležitý princip

Security model je **data-driven**, nikoliv statický config.

To znamená:

- změny role → Keycloak
- změny oprávnění → DB (admin UI)
- změny pravidel → criteria implementace