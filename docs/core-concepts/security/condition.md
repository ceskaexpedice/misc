[Index](../../index) / [Základní koncepty](../../core-concepts) / [Zabezpečení](../../core-concepts/security)

# Podmínky

Podmínky jsou dodatečné požadavky, které musí být splněny před tím, než je akce povolena.

Poskytují jemnozrnnou kontrolu nad rámec jednoduché autorizace založené na rolích.

## Příklady

Mezi typické podmínky patří:

- povolené rozsahy IP adres
- licenční omezení
- omezení přístupu na úrovni konkrétních sbírek

Významným typem podmínky je **licence** (viz [Licence](../../domain-concepts/license/index)).

## Model vyhodnocení

I když role přidělí akci, přístup může být stále zamítnut, pokud nejsou splněny požadované podmínky.

```text
Role
  ↓
Action
  ↓
Criteria
  ↓
Permit / Deny
```


## Proč podmínky existují

Mnoho případů v knihovních systémech vyžaduje pravidla přístupu, která nelze vyjádřit pouze pomocí rolí uživatelů.

Například:

- přístup může být povolen pouze z institucionálních sítí
- přístup může záviset na platné licenční smlouvě
- přístup může záviset na požadovaném obsahu

Podmínky umožňují tato pravidla konfigurovat bez nutnosti zavádět další role.

