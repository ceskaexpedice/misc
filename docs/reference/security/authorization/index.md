# Authorization

Autorizační rozhodnutí vzniká vyhodnocením:

1. rolí uživatele,
2. přiřazených akcí,
3. kritérií.

## Decision Model

```text
Role
 ↓
Action
 ↓
Criteria
 ↓
Permit / Deny
```

## Evaluation Rules

### Missing Action

Pokud uživatel nemá požadovanou akci:

```text
DENY
```

### Failed Criterion

Pokud není splněno kritérium:

```text
DENY
```

### Successful Evaluation

Pokud jsou splněny všechny podmínky:

```text
PERMIT
```