# Role

Role představují skupiny uživatelů se stejnými odpovědnostmi nebo oprávněními.

Role jsou spravovány poskytovatelem identity a jsou dostupné v Krameriu po úspěšné autentizaci.

Příklady:

- Administrátor
- Knihovník
- Registrovaný uživatel
- Anonymní uživatel

Role přímo neudělují oprávnění.

Místo toho jsou role mapovány na akce v systému Kramerius.

## Mapování rolí

```text
Role
  ↓
Action
```

Jedna role může udělovat více akcí.

Více rolí může udělovat stejnou akci.

