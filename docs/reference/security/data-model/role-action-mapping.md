# Role → Action Mapping

Mapování rolí na akce je základem autorizačního modelu.

## Princip

Role sama o sobě neuděluje oprávnění.

Oprávnění vzniká až mapováním na akce.

## Struktura dat

Mapování je uloženo v tabulkách:

- rights
- role_action (pokud existuje normalizace)