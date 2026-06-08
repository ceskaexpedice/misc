# Rights Table

Tabulka `rights` uchovává mapování mezi rolemi, akcemi a kritérii.

## Struktura

| Sloupec | Typ | Popis |
|----------|-----|--------|
| id | bigint | Primární klíč |
| role | varchar | Název role |
| action | varchar | Identifikátor akce |
| criteria | json / relation | Seznam kritérií |

## Popis

Každý záznam reprezentuje oprávnění vzniklé kombinací:

- role z Keycloaku
- akce definované v Krameriovi
- přiřazená kritéria