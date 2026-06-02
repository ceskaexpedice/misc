# Zapojení knihovny do DNNT

## Cíl scénáře
Cílem je připravit instanci Krameria tak, aby mohla být
zapojena do DNNT v souladu s bezpečnostními a provozními požadavky.

## Pro koho je scénář
- Administrátor
- Kurátor (částečně)

## Předpoklady
- Funkční instance Krameria
- Přístup k IdP (Keycloak)
- Znalost základních pojmů

---

## Přehled kroků
1. Vytvoření servisního účtu
2. Nastavení rolí a oprávnění
3. Konfigurace logování
4. Bezpečnostní omezení API
5. Ověření funkčnosti

---

## 1. Servisní účet
(Stručně, s odkazem na detailní guide)

➡️ viz [Guides – Security – Service Accounts](...)

---

## 2. Bezpečnostní nastavení
(tady shrneš, *které* security scénáře se použijí a *proč*)

➡️ odkazy:
- Security Scenario A
- Role mapping

---

## 3. Logování a audit
(co musí být zapnuto, na jaké úrovni, proč)

➡️ viz [Guides – Logging](...)

---

## 4. Validace a kontrola
Checklist:
- [ ] token funguje
- [ ] role správně omezené
- [ ] logy obsahují auditní záznamy
