# Vyhodnocení kritérií

Kritéria představují dodatečné podmínky nad rámec rolí a akcí.

## Princip

Role určuje, co uživatel smí dělat.

Kritérium určuje, za jakých podmínek to smí dělat.

## Příklad

```text
ROLE_READER
      ↓
VIEW_DOCUMENT
      ↓
LICENSED_ACCESS
```

Uživatel může mít potřebnou roli, ale přístup bude zamítnut, pokud není splněna licence.

## Pořadí vyhodnocení

```text
Role Check
     ↓
Action Check
     ↓
Criteria Check
     ↓
Decision
```

## Typické příklady

### IP omezení

Přístup pouze z definovaných adres nebo sítí.

### Licenční omezení

Přístup pouze pro dokumenty pokryté platnou licencí.

### Objektová omezení

Přístup závislý na vlastnostech konkrétního objektu.

## Související kapitoly

- [Reference / Criteria](../../../reference/security/criteria/)