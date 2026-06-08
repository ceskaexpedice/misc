# Database Schema Initialization

Kramerius obsahuje SQL schéma, které je součástí distribuovaného WAR balíčku.

## Chování při startu

Při startu aplikace:

1. zkontroluje existenci tabulek
2. pokud neexistují, provede inicializační skripty
3. vytvoří potřebnou strukturu databáze

## Umístění schématu

SQL skripty jsou uloženy uvnitř aplikace:

```
WEB-INF/classes/db/schema.sql
```

nebo obdobně v resources.

## Poznámka

Tento mechanismus je určen pouze pro inicializaci.
V produkčním prostředí se očekává spravovaná databáze.