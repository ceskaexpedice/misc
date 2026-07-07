[Index](../../index) / [Základní koncepty](../../core-concepts) / [Zabezpečení](../../core-concepts/security)

# Autorizace

Autorizace odpovídá na otázku:

> Je autentizovaný uživatel oprávněn provést konkrétní akci?

Autorizace je vyhodnocována systémem Kramerius.

Rozhodování o přístupu je založeno na:

- rolích
- akcích
- podmínkách

---

## Seznam akcí

- Kramerius má pevně definovaný seznam akcí, např.:
    - `READ`
    - `WRITE`
    - `EXPORT`
    - `ADMIN_ACTION`
- Každá akce může být chráněna více pravidly (rules).

---

## Pravidla přiřazení oprávnění

Ke každé akci lze přiřadit:

1. **Role** – uživatel musí mít danou roli, aby mohl akci provést.
2. **Licence** – kontrola, zda dokument nebo sbírka má přiřazenou licenci, která oprávnění umožňuje.
3. **Další kritéria** – např. `IPAddress`, které omezí přístup podle sítě uživatele.

> Při vyhodnocování více pravidel hraje roli **priorita pravidel a licencí**.

---

## Hierarchie licencí

- Licence jsou součástí FOXML dokumentů v Akubra repository.
- Každý objekt (stránka, kniha, periodikum) může mít 0–n licencí.
- Licence vyššího objektu (např. kniha nebo repo) se **implicitně uplatní na všechny nižší objekty** při vyhodnocování (ne fyzicky).
- Licence mohou být **globální** nebo **lokální**.

---

## Vyhodnocení oprávnění – příklad

Akce: READ
Role: krameriusAdmin

Kriterium = Licence = dnnto
Kritérium = IPAddress = 192.168.0.0/24
Výsledek: povolení, pokud uživatel má roli krameriusAdmin a dokument má licenci dnnto
a je přihlášen z IP v povoleném rozsahu


- K jedné akci lze přiřadit více pravidel – systém je vyhodnocuje postupně.
- Licence mohou mít **prioritu**, pokud se na akci vztahuje více licencí.

---

## Hierarchické vyhodnocování přístupů

Při vyhodnocování oprávnění Kramerius postupuje **hierarchicky** podle struktury objektů v repository:

- Každý digitální objekt (stránka, kniha, periodikum) může mít přiřazenu 0–n licencí.
- Pokud u konkrétního objektu není licence explicitně definována, systém **dědí licence z nadřazeného objektu**.
    - Například:
        - Licence je definována u **monografie**.
        - Stránka `page` uvnitř této monografie nemá žádnou vlastní licenci.
        - Při vyhodnocování přístupu pro stránku se použije licence definovaná u monografie.
- Toto dědění probíhá pouze při **runtime vyhodnocení přístupů**, licence se fyzicky nepřepisuje do nižších objektů.

> Poznámka: Tato hierarchie platí i pro skupiny dokumentů nebo celé repozitáře. Vyšší objekt určuje implicitní pravidla pro všechny podřízené objekty.


## Integrace s procesy a UI klientem

- **Admin Client** zobrazuje sekci Procesy, ale všechny procesy volají REST API **Manageru procesního frameworku**.
- Oprávnění pro spuštění procesů jsou vyhodnocována pomocí role + licence + kritéria.
- Kurátor nebo admin uvidí pouze procesy, ke kterým má právo přístupu.

