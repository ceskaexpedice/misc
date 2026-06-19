# Instalace a správa Solr

Tato stránka popisuje postup instalace a správy vyhledávacího enginu **Solr** pro Kramerius 7. Pro konfiguraci parametrů Solr viz stránka [Solr Configuration](Reference/Solr-configuration.md).

---

## Instalace Solr

1. Stáhněte si poslední verzi Solr z oficiálních stránek: [https://lucene.apache.org/solr/downloads.html](https://lucene.apache.org/solr/downloads.html)
2. Spusťte Solr příkazem: <solr_home>/bin/solr start

3. Nainstalujte potřebná jádra (Solr cores), viz níže.

---

## Jádro Search

- Slouží pro vyhledávání klientskými aplikacemi (veřejné a administrativní rozhraní digitální knihovny).
- Postup vytvoření jádra:
1. V administračním rozhraní Solr vytvořte nové jádro s názvem `search`.
2. Zkopírujte obsah instalačního adresáře:
  ```
  kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/search
  ```
do `<solr_home>/server/solr/search`.
3. Přidejte jádro `search` v administračním rozhraní.

---

## Jádro Processing

- Nahrazuje resource index Fedory. Každý nově importovaný objekt je zaznamenán spolu se svými vazbami.
- Postup vytvoření jádra:
1. V administračním rozhraní Solr vytvořte jádro s názvem `processing`.
2. Konfigurační soubory pro jádro jsou v instalačním adresáři:
  ```
  kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/processing
  ```

---

## Jádro Logs

- Slouží pro ukládání přístupů uživatelů a generování statistik a reportů.
- Postup vytvoření jádra:
1. V administračním rozhraní Solr vytvořte jádro `logs`.
2. Zkopírujte obsah:
  ```
  kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/logs
  ```
do `<solr_home>/server/solr/logs`.

---

## Aktualizace schématu (Search core)

Při přechodu na vyšší verzi K7 může být potřeba aktualizovat soubor **managed-schema**.

1. Stáhněte nové konfigurační soubory a slovníky z instalačního balíčku nebo přímo z [git repozitáře](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/search/conf).
2. Umístěte je do adresáře `<solr_home>/server/solr/search`.
3. Otevřete Solr admin: [http://localhost:8983/](http://localhost:8983/)
4. V záložce **Core Admin** vyberte jádro `search` a klikněte na **Reload**.

---

> **Tip:** Pro konfiguraci URL Solr jáder, přihlašovací jména a hesla se podívejte na stránku [Solr Configuration](Reference/Solr-configuration.md).

