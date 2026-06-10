# Autentizace

Autentizace odpovídá na otázku:

> Kdo je aktuální uživatel?

Kramerius přímo nespravuje uživatelské identity. Místo toho spoléhá na externí poskytovatele identity (Identity Provider, IdP), typicky Keycloak.

Po úspěšném přihlášení poskytovatel identity vydá bezpečnostní token obsahující informace o autentizovaném uživateli.

## Výsledek autentizace

Výsledkem autentizace je autentizovaná identita reprezentovaná:

- identifikátorem uživatele
- uživatelským jménem
- přiřazenými rolemi
- dalšími atributy identity

Autentizovaná identita je připojena ke každému požadavku a stává se vstupem pro autorizaci.

## Související témata

- [Autorizace](authorization/)
- [Architektura zabezpečení](../../../architecture/security/)
- [Referenční přehled autentizace](../../../reference/security/authentication/)