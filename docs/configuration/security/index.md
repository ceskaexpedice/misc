[Index](../index) / [Konfigurace](../../configuration)

# Zabezpečení konfigurace

Tato část popisuje, jak se bezpečnostní model Krameria nastavuje a spravuje v běžícím systému.

Na rozdíl od technické konfigurace (properties, deployment) jde o **datový model uložený v databázi a externím identity provideru**.

---

## Co je spravováno externě

- uživatelé
- role
- autentizace (login, tokeny)

Kramerius tato data pouze využívá.

➡️ [Keycloak](keycloak)

---

## Co je spravováno v Krameriu 

Kramerius obsahuje administrační model pro:

- mapování rolí na akce
- přiřazení kritérií k akcím
- definici oprávnění (rights)

Tato data jsou uložena v databázi.

➡️ [Admin aplikace](https://github.com/ceskaexpedice/kramerius-admin-client/wiki)

---

## Navazujici dokumentace

- ➡️ [Základní pojmy](../core-concepts/security)
- ➡️ [Architektura](../architecture/security)
- ➡️ [Reference](../reference/security)
- ➡️ [Navody](../guides/admin)
