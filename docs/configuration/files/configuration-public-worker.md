[Index](../index) / [Konfigurace](../../configuration)  / [Soubory](../../configuration/files)

# Public worker konfigurace

Tato stránka poskytuje **referenční přehled konfiguračních parametrů Akubra storage** v Kramerius 7. Obsahuje defaultní hodnoty, účel a doporučené nastavení.

Konfigurace se načítá z:

- **Default**: uvnitř JAR souboru knihovny `configuration.properties`
- **Uživatelské přetížení**: soubor `$USER_HOME/.kramerius4/configuration.properties`

Uživatel může ve svém souboru předefinovat libovolnou hodnotu z defaultního souboru.

---

## Parametry Public Worker

| Parametr | Popis | Výchozí hodnota |
|-----------|--------|----------------|
| `dochub.storage.user` | Cesta, kde jsou uloženy vygenerované PDF, e-knihy a texty pro konkrétního uživatele. | `~/.kramerius4/docs/user-out` |
| `dochub.storage.permanent` | Cesta, kde jsou uloženy obecné části PDF a e-knih, které nejsou závislé na konkrétním uživateli. | `~/.kramerius4/docs/permanent` |
| `dochub.user.max.size.gb` | Maximální povolená velikost uživatelského úložiště v GB. Po překročení limitu jsou všechny soubory odstraněny. | – |
| `dochub.permanent.max.size.gb` | Maximální povolená velikost permanentního úložiště v GB. Po překročení limitu jsou všechny soubory odstraněny. | – |
| `dochub.permanent.expiration.hours` | Odstraní všechny dokumenty v permanentním úložišti starší než zadaný počet hodin. | `3000` |
| `dochub.user.expiration.hours` | Odstraní všechny dokumenty v uživatelském úložišti starší než zadaný počet hodin. | `100` |