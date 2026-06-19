Popis instalace a konfigurace systému Kramerius 7 s integrovaným úložištěm Akubra.

## Konfigurace úložiště Akubra

Základní změnou Krameria 7 oproti předchozí verzi 5 je nahrazení dokumentového repozitáře Fedora Commons 3, resp. integrace jeho souborového úložiště Akubra přímo do jádra Krameria při zachování zpětné kompatibility datové struktury.
Umístění datových souborů je určeno následujícími parametry v souboru `configuration.properties`:
```
objectStore.path=${sys:user.home}/.kramerius4/data/objectStore
objectStore.pattern=##/##
datastreamStore.path=${sys:user.home}/.kramerius4/data/datastreamStore
datastreamStore.pattern=##/##
```

Při přechodu z existující instalace Krameria 5 je potřeba uvedené výchozí hodnoty změnit podle skutečného umístění původního datového úložiště Fedora. 

Pokud vaše instalace Fedory nepoužívá úložiště Akubra, ale starší formát Legacy-fs, můžete využít podporu tohoto fotmátu nastavením konfigurační property `legacyfs=true`. Podrobnosti ke konfiguraci Legacy-fs najdete níže na této stránce v sekci **Legacy low level storage**

Alternativní možnost je konvertovat úložiště z formátu Legacy-fs do formátu Akubra pomocí nástroje popsaného v sekci **Konvertor formátu úložiště** na konci této stránky. 

## Instalace indexu (SOLR)
1. Stáhněte si poslední verzi vyhledávacího enginu [SOLR](https://lucene.apache.org/solr/downloads.html) 
2. Spustěte příkazem  `<solr_home>/bin/solr start`

### Kramerius - core
Jádro je určeno pro vyhledávání v aplikaci search a v klientech. Popis instalace:

1. V [administračním rozhraní](http://localhost:8983/) spuštěné instance vyhledávacího enginu solr vytvořte nové vyhledávací jádro pro vyhledávání v aplikacích. 
    - Standardní název je `kramerius`. Pokud je potřeba zvolit jiný název nebo je nutno provozovat solr na jiném portu, je nutno  změnit defaultní [konfiguraci](https://github.com/ceskaexpedice/kramerius/blob/akubra/shared/common/src/main/java/res/configuration.properties#L9). 
2. Postup pro vytvoření jádra je analogický k tomu, co je uvedeno [zde](https://github.com/ceskaexpedice/kramerius/wiki/P%C5%99echod-na-novou-verzi-SOLR). 
    - Nejdříve je nutno zkopírovat vše z instalačního adresáře [kramerius-7.0.0-beta1.zip/installation-7.0.0-beta1/solr-7.x/kramerius](https://github.com/ceskaexpedice/kramerius/tree/akubra/installation/solr-7.x/kramerius) do 
adresáře `<solr_home>/server/solr/kramerius` a poté v administračním rozhraní přidat jádro se jménem `kramerius` a instalačním adresářem `kramerius`.

### Processing - core
Vyhledávací jádro nahrazuje funkcionalitu resource indexu. Každý nově importovaný objekt je nyní popsán v tomto indexu spolu se svými vazbami.  Postup instalace je následující: 
1. V [administračním rozhraní](http://localhost:8983/) spuštěné instance vytvořte jádro `processing` obdobným způsobem, jako bylo vytvořeno jádro `kramerius`.  
    - Změna portu nebo názvu jádra je opět možná pomocí  možná pomocí [konf. souboru](https://github.com/ceskaexpedice/kramerius/blob/akubra/shared/common/src/main/java/res/configuration.properties#L12).
2. Konf soubory pro jádro processing jsou v instalačním adresáři [kramerius-7.0.0-bet1.zip/installation-7.0.0-beta1/solr-7.x/processing](https://github.com/ceskaexpedice/kramerius/tree/akubra/installation/solr-7.x/processing/). 


# Instalace tomcatu a aplikací 

## Administrační aplikace 
Postup instalace je stejný jako u předchozí verze Kramerius 5. Zkopírujte soubor `search.war` do adresáře `<catalina_home>/webapps`.

## Instalace sdílených knihoven 
Do adresáře `<catalina_home>/libs` zkopírujte soubor `kramerius-7.0.0-beta1.zip/security-core.jar` a `kramerius-7.0.0-beta1.zip/postgresql-42.1.4.jar`

## Instalace autentizace. 
Autentizace aplikace je realizována pomocí [JAAS] (http://docs.oracle.com/javase/7/docs/technotes/guides/security/jaas/JAASRefGuide.html).  Vytvořte soubor `jaas.conf`s tímto obsahem
```
search {
 cz.incad.kramerius.security.jaas.K4LoginModule required debug=true;
};
```
Před spouštěním tomcatu je nutno nastavit systémovou proměnnou, která ukazuje na na tento soubor:

Linux:
```
export JAVA_OPTS="-Djava.security.auth.login.config=<path_to_jaas>/jaas.conf"
```

Windows:
```
set JAVA_OPTS="-Djava.security.auth.login.config=<path_to_jaas>\jaas.conf"
```

_Poznámka: V Tomcatu verze 9 se tato property nastavuje v souboru setenv.sh do systémové proměnné CATALINA_OPTS._

## Nastavení single sign-on 
Postupujte podle návodu [zde](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#autentizace-a-single-sign-on)

## Instalace editoru uživatelů 
Soubor `kramerius-7.0.0-beta1.zip/rightseditor.war` zkopírujte do adresáře `<catalina_home>/webapps`.

# Instalace databáze postgres
Instalace databáze je stejná jako u standardní verze. Z vytvářených databází je nutné vytvouřit pouze databázi `kramerius4`. Pro ni je nutno vytvořit uživatele (standardně `fedoraAdmin`) a [nastavit datasource](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#konfigurace-datasource). 


# Import a  migrace dat

Pro import dat lze využít standardních importních procesů. 
* Import standardních foxml dat 
* Import NDK  balíčků 
* Replikace K4.

# Legacy low level storage

Knihovna low level storage použitá v Krameriu 7 podporuje i starší formát úložiště (legacy file store). Zapíná se nastavením property legacyfs=true, další potřebné parametry s výchozími hodnotami jsou uvedené níže:   

```
legacyfs=false

#The java class used to determine the path algorithm;
path_algorithm=org.fcrepo.server.storage.lowlevel.TimestampPathAlgorithm

#The root directory for the internal storage of Fedora
#objects. This value should be adjusted based on your installation
#environment. This value should not point to the same location as
#datastream_store_base.
object_store_base=/export/home/fedora/data/objects

#Whether the escape character (i.e. (the token beginning an
#escape sequence) for the backing database (which includes
#registry tables) is the backslash character. This is needed to
#correctly store and retrieve filepaths from the registry
#tables, if running under Windows/DOS. (Set to true for MySQL and
#Postgresql, false for Derby and Oracle)
backslash_is_escape=false

#The root directory for the internal storage of Managed
#Content datastreams. This value should be adjusted based on your
#installation environment. This value should not point to the same
#location as object_store_base.
datastream_store_base=/filestore/part1

#The java class used to determine the path registry
path_registry=org.fcrepo.server.storage.lowlevel.DBPathRegistry

#The java class that determines the filesystem  implementation class;
file_system=org.fcrepo.server.storage.lowlevel.GenericFileSystem


legacyfs.minIdle=0
legacyfs.validationQuery=select 1
legacyfs.maxWait=-1
legacyfs.whenExhaustedAction=1
legacyfs.numTestsPerEvictionRun=3
legacyfs.dbUsername=fedoraAdmin
legacyfs.maxIdle=10
legacyfs.testOnBorrow=true
legacyfs.testWhileIdle=true
legacyfs.minEvictableIdleTimeMillis=1800000
legacyfs.timeBetweenEvictionRunsMillis=-1
legacyfs.testOnReturn=true
legacyfs.jdbcURL=jdbc:postgresql:fedora3
legacyfs.ddlConverter=org.fcrepo.server.utilities.PostgresDDLConverter
legacyfs.jdbcDriverClass=org.postgresql.Driver
legacyfs.dbPassword=fedoraAdmin
legacyfs.maxActive=100
```

Využití podpory legacy-fs je předpokládáno pouze u existujících instalací fedory s tímto formátem, Kramerius 7 nepodporuje zakládání nové prázdné databáze `fedora3`. Pro nové instalace Krameria použijte formát úložiště Akubra.
 
# Synchronizace paralelních zápisů

Synchronizace paralelních zápisů do jednoho úložiště z více souběžných procesů a případně více instancí Krameria je zajištěna sdílenou tabulkou zámků v distribuované paměťové databázi Hazelcast. Synchronizace probíhá automaticky a defaultní nastavení není obvykle třeba měnit. K nastavení jména instance a uživatele lze případně použít následující property:  

```
hazelcast.instance=akubrasync
hazelcast.user=dev
``` 

Pokud nestačí defaultní konfigurace clusteru Hazelcast, je možné jak server, tak klienty Hazelcast konfigurovat pomocí XML souborů. K tomu slouží property `hazelcast.config` a `hazelcast.clientconfig`, kterými je možné definovat cestu ke konfiguračnímu souboru pro hazelcast server, resp. klient. Soubory mohou být určeny buď absolutní cestou nebo relativně ke konfiguračnímu adresáři `.kramerius4`. Popis obsahu konfiguračních XML souborů najdete v dokumentaci [Hazelcast](https://docs.hazelcast.org/docs/latest/manual/html-single/#understanding-configuration)

# Konvertor formátu úložiště

Součástí distribuce Krameria 7 je samostatný nástroj pro konverzi formátu úložiště z legacy-fs do formátu Akubra, případně z existujícího formátu Akubra do formátu AKubra s jinou strukturou (s jinou úrovní vnořených adresářů). V obou variantách je konverze prováděna přesouváním (přejmenováváním) souborů mezi kořenovými adresáři původního a nového úložiště v rámci jednoho disku. Soubory tedy nejsou kopírovány a obsah původního úložiště je nevratně odstraněn. 

**Před použitím konvertoru je tedy vhodné původní úložiště zálohovat.**

Konverzní nástroj je součást distribuce Krameria 7 v souboru `migration-7.0.0-beta1.zip`. Jeho obsah rozbalte do libovolného adresáře na serveru Krameria, konvertor se spouští příkazem `migration` v podadresáři `bin`. Parametry a nastavení procesu jsou popsány v následujících odstavcích 

## Konverze legacy-fs -> akubra

Příkaz:
```
bin/migration LEGACY 0 0 false
```
1. číselný parametr: počáteční tokendbid z tabulky datastreampaths
2. číselný parametr: počáteční tokendbid z tabulky objectpaths
boolean parametr: jestli má být v rámci konverze automaticky proveden i rebuild processing indexu

Standardně je proces spuštěn s parametry 0 0 false - tedy od první položky v databázi. Jiné počáteční hodnoty tokendbid by se použily při případném restartu konverze po jejím předchozím neúspěšném ukončení - poslední úspěšně zpracovaná hodnota tokendbid je v tom případě vypsaná v logu procesu.

Pro větší úložiště je výhodnější spustit rebuild processing indexu samostatně až po skončení konverze (tedy ponechat hodnotu booleovského parametru false).

Nutné konfigurační proměnné:

```
legacyfs.jdbcURL - spojení do databáze fedora3
legacyfs.dbUsername - db uživatel
legacyfs.dbPassword - db password

datastreamStore.path - adresář cílového akubra_fs pro datastreamy
objectStore.path - adresář cílového akubra_fs pro objekty
datastreamStore.pattern -  struktura cílového adresáře akubra_fs pro datastreamy;
objectStore.pattern - struktura cílového adresáře akubra_fs pro objekty
```

Frekvence logování průbhu konverze je řízena property `akubra.migration.logfrequency`, výchozí hodnota je 10000

## Konverze akubra -> akubra

```
bin/migration AKUBRA false
```

Nutné konfigurační proměnné:

```
datastreamStore.migrationsource - adresář zdrojového akubra_fs pro datastreamy
objectStore.migrationsource - adresář zdrojového akubra_fs pro objekty

datastreamStore.path - adresář cílového akubra_fs pro datastreamy
objectStore.path - adresář cílového akubra_fs pro objekty
datastreamStore.pattern -  struktura cílového adresáře akubra_fs pro datastreamy;
objectStore.pattern - struktura cílového adresáře akubra_fs pro objekty
```


# Rebuild processing indexu

Kramerius 7 nahrazuje resource index fedory 3 novým jádrem indexu SOLR s identifikátorem `processing`. Pokud Kramerius 7 nasazujete na již existující úložiště ve formátu akubra nebo jste formát úložiště konvertovali utilitou `migration`, je potřeba processing index inicializovat pomocí administrátorského procesu `Rebuild processing indexu`, který můžete  spustit odpovídající položkou v administrátorském menu.  

# Migrace vyhledávacího indexu

Pokud na Kramerius 7 přecházíte z verze starší než 5.3.5, která ještě používá integrovaný index SOLR verze 4, je nutno přejít na samostatný SOLR verze 6 nebo vyšší. Popis instalace a migrace indexu je uveden na stránce [Přechod na novou verzi SOLR](Přechod-na-novou-verzi-SOLR)

# OAI4SOLR

Kramerius 7 podporuje protokal OAI pomocí implementace `oai4solr`, která pracuje přímo nad daty indexu SOLR. Instalační soubory a popis instalace a konfigurace je k dipozici v modulu installation/oai (https://github.com/ceskaexpedice/kramerius/tree/master/installation/oai). Pro verzi SOLR6 použijte knihovnu `oai4solr6`, pro SOLR 7 a vyšší knihovnu `oai4solr7`
