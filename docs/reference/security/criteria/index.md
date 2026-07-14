# Criteria

Kritéria představují dodatečné podmínky autorizace.
Všechny informace o právech, licencích, dodatečných podmínkách jsou ukládány v servisní databázi Postgres SQL a situaci nejlépe vystihuje následující diagram:

![Architecture](../assets/criteria-evaluation.png)

Právo reprezentováno vazbou mezi rolí a akcí, kterou se uživatel snaží vykonat. V tomto jednoduchém případě vždy platí, že uživatel má právo vykonat danou akci.  
Vazba může být rozšířena o dodatečnou podmínky, ta pak dál specifikuje podmínky za kterých uživatel může danou akci vykonat.


## Available Criteria

### IP Address Criterion

Ověřuje IP adresu klienta.

#### Parameters

| Parameter | Description |
|------------|------------|
| allowedRanges | Povolené rozsahy IP adres |

---

### License Criterion

Ověřuje licenční podmínky.

#### Parameters

| Parameter | Description |
|------------|------------|
| licenseId | Identifikátor licence |

---

### Custom Criteria

Kramerius umožňuje implementovat vlastní kritéria.