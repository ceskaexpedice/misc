[Index](../../index) / [Deployment](..) / [On Premise](../on-premise)  

# Popis instalace a nastavení K7

Popis instalace a konfigurace systému Kramerius 7 s integrovaným úložištěm Akubra. Instalace předchozí verze Kramerius 5 je popsána [[zde|Instalace verze K5]]

Před instalací aplikace Kramerius je třeba nainstalovat následující systémové komponenty:
---
* **Java: JDK 11**, je možno využít javu z balíčku OpenJDK případně Oracle JDK. 
    * Instalační balíčky naleznete zde [OpenJDK](https://openjdk.org/), [Oracle JDK](https://www.oracle.com/java/technologies/downloads/) 
* **Aplikační server: Tomcat 9.x**
    *  Stáhnout Apache Tomcat je možno [zde](https://tomcat.apache.org/download-90.cgi)
* Databáze: **Postgres 8.4 nebo novější**
    * Stáhnout databázi je možno [zde](https://www.postgresql.org/download/), případně je možno využít [docker image](https://hub.docker.com/_/postgres) nebo předpřipravené image z projektu [bitnami](https://bitnami.com/stack/postgresql/containers) 
* Vyhledávací engine **Solr verze  8.0 a vyšší**
    * Pro instalaci je možno využít samostatného balíku dostupného [zde](https://solr.apache.org/downloads.html). 
    * V případě provozování v Dockeru nebo Kubernetes doporučujeme využít již předpřipravené image z projektu [bintami](https://bitnami.com/stack/solr) nebo [solr operator](https://solr.apache.org/operator/).  
* Autentizační server **Keycloak**
    * Server je možno stáhnout [zde](https://www.keycloak.org/downloads). Verze může být jakákoliv z volně dostupných. 
    * **Důležitá poznámka: Pro rozchození Federace eduID je nutné řešit pomocí klonu keycloaku, popis instalace je přítomen zde [keyckloak-eduid](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Security_Keycloak-a-eduID)** 
* Webový server **Apache httpd** nebo **Nginx**
    * Verze může být jakákoliv z volně dostupných. 



---
U komponent u kterých není uvedené specifické jméno revize je rozumné používat jejich aktualizace. Popis instalace a administrace těchto systémových komponent není součástí této dokumentace, předpokládáme, že administrátor aplikace Kramerius 7 ovládá instalaci a administraci výše uvedených komponent.

Operační systém může být libovolný, na kterém je možno tyto komponenty provozovat, vlastní aplikace Kramerius 7 žádné speciální požadavky na systém nemá. Systém je vyvíjen a testován na běžných distribucích Linuxu. Hardware serveru musí být dimenzován na uvažované množství dat, doporučujeme minimálně dvojnásobnou velikost pevného disku, než je plánovaná velikost obrazových dat. Vzhledem k velké paměťové náročnosti práce s grafickými daty (náhledy stránek, zoomování) je třeba i při minimálním provozu aplikace alespoň 8GB RAM. 

K7 je vhodné nainstalovat pod samostatným uživatelským účtem, například kramerius.

V produkčním prostředí je před J2EE server (Tomcat) vhodné předřadit webserver přístupný na portu 80, například Apache s nakonfigurovanými moduly mod_proxy a mod_proxy_ajp.

Každou komponentu systému Kramerius (tedy vlastní aplikaci Kramerius (search.war), indexer SOLR, databázi PostgreSQL)  je možné nainstalovat na samostatný server.  

### Distribuční soubory

Distribuční soubory jádra aplikace Kramerius najdete v sekci [Releases](https://github.com/ceskaexpedice/kramerius/releases)  

Všechny soubory jsou zabaleny do jednoho archivního souboru kramerius-x.x.x.zip (znaky x.x.x jsou samozřejmě nahrazeny konkrétním číslem verze). 

Pokud v konkrétním release některý z uvedených souborů chybí, znamená to, že v něm oproti předchozí verzi nedošlo k žádné změně.

V následujících odstavcích jsou uvedeny požadavky aplikace Kramerius na specifickou konfiguraci systémových komponent, pokud možno i s odkazy na příklady konkrétních úprav příslušných konfiguračních souborů. Tyto příklady jsou uvedeny pouze pro ilustraci jedné z možných konfigurací a nenahrazují dokumentaci k jednotlivým systémovým komponentám. V případě distribuované instalace je třeba uvedené příklady konfiguračních URL (localhost) nahradit adresami příslušných serverů. 

(v uvedených příkladech konfigurace předpokládáme instalaci Tomcatu do domácího adresáře uživatele kramerius4)

# PostgreSQL

* Vytvořit uživatele `fedoraAdmin` a pro něj databázi `kramerius4` a [nastavit datasource](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#konfigurace-datasource). 


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

Parametry `.path` udávají cestu ke kořenovému adresáři příslušného úložiště (objectStore nebo datastreamStore). 

Parametry `.pattern` určují vnitřní strukturu úložiště, tedy počet úrovní stromu podadresářů a počet adresářů v jednotlivých úrovních. Názvy adresářů odpovídají počátečním znakům MD5 hashe názvu uloženého souboru, každému znaku # v patternu tedy odpovídá jeden hexadecimální znak (0 - f). Výchozí pattern ##/## tedy znamená, že úložiště bude mít dvě úrovně adresářů, v každé z nich je maximálně 256 adresářů (00-ff), celkem tedy přibližně 65000 adresářů. Při rovnoměrném rozložení souborů by tedy počet souborů v jednom adresáři neměl pro běžné instalace překročit 1000 souborů. Jen pro skutečně velké instituce se stovkami milionů dokumentů by bylo vhodné změnit pattern na 3 úrovně (##/##/##). Strukturu úložiště je možné měnit jen pokud nic neobsahuje, pro změnu struktury existujícího úložiště je potřeba použít **Konvertor formátu úložiště**.    

Pokud vaše instalace Fedory nepoužívá úložiště Akubra, ale starší formát Legacy-fs, můžete využít podporu tohoto fotmátu nastavením konfigurační property `legacyfs=true`. Podrobnosti ke konfiguraci Legacy-fs najdete níže na této stránce v sekci **Legacy low level storage**

Alternativní možnost je konvertovat úložiště z formátu Legacy-fs do formátu Akubra pomocí nástroje popsaného v sekci **Konvertor formátu úložiště** na konci této stránky. 

## Instalace indexu (SOLR)
1. Stáhněte si poslední verzi vyhledávacího enginu [SOLR](https://lucene.apache.org/solr/downloads.html) 
2. Spustěte příkazem  `<solr_home>/bin/solr start`
3. Nainstalujte potřebná jádra (Solr core), viz níže

### jádro Search
Jádro je určeno pro vyhledávání klientskými aplikacemi (veřejné, admininstrační rozhraní digitální knihovny). Popis instalace:

- V [administračním rozhraní](http://localhost:8983/) spuštěné instance vyhledávacího enginu solr vytvořte nové vyhledávací jádro. 
    - Standardní název je `search`. Pokud je potřeba zvolit jiný název nebo je nutno provozovat solr na jiném portu, je nutno  změnit defaultní [konfiguraci](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/res/configuration.properties#L11). 
- Postup pro vytvoření jádra je analogický k tomu, co je uvedeno [zde](https://github.com/ceskaexpedice/kramerius/wiki/P%C5%99echod-na-novou-verzi-SOLR). 
    - Nejdříve je nutno zkopírovat vše z instalačního adresáře [kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/search](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/search) do 
adresáře `<solr_home>/server/solr/search` a poté v administračním rozhraní přidat jádro se jménem `search` a instalačním adresářem `search`.

### jádro Processing
Vyhledávací jádro nahrazuje funkcionalitu resource indexu (dříve používaný repozitář Fedora). Jde o interní index repozitáře.
Každý nově importovaný objekt je nyní popsán v tomto indexu spolu se svými vazbami.  Postup instalace je následující: 
- V [administračním rozhraní](http://localhost:8983/) spuštěné instance vytvořte jádro `processing` obdobným způsobem, jako bylo vytvořeno jádro `search`.  
    - Změna portu nebo názvu jádra je opět možná pomocí  možná pomocí [konf. souboru](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/res/configuration.properties#L12).
- Konf soubory pro jádro processing jsou v instalačním adresáři [kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/processing](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/processing/). 

### jádro Logs
Jádro slouží pro ukládání informací o přístupu uživatelů. A následně jako zdroj dat pro generování statistika a reportů.
Popis instalace:

- V [administračním rozhraní](http://localhost:8983/) spuštěné instance vyhledávacího enginu solr vytvořte nové vyhledávací jádro s názvem logs.
- Postup pro vytvoření jádra je analogický k tomu, co je uvedeno [zde](https://github.com/ceskaexpedice/kramerius/wiki/P%C5%99echod-na-novou-verzi-SOLR).
    - Nejdříve je nutno zkopírovat vše z instalačního adresáře [kramerius-7.x.y.zip/installation-7.x.y/solr-7.x/logs](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/logs) do adresáře <solr_home>/server/solr/logs a poté v administračním rozhraní přidat jádro se jménem logs a instalačním adresářem logs.


#### Aktualizace schématu (jádro search)
Při přechodu na některou vyšší verzi K7 může nastat potřeba aktualizovat schéma (zejména soubor managed-schema) Postup je následující: 

- Stáhněte si konfigurační soubory a slovníky buď z instalačního balíčku nebo přímo z git [repozitáře](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/search/conf).
- Stáhnuté soubory umístěte do adresáře `<solr_home>/server/solr/search`. 
- Otevřte administrační prostředí solru `http://localhost:8983/`. 
- V záložce core-admin vyberte jádro `search` a zmáčkněte tlačítko `reload`.

# Instalace Tomcatu a jádra aplikace 

## Administrační aplikace 
Postup instalace je stejný jako u předchozí verze Kramerius 5. Zkopírujte soubor `search.war` do adresáře `<catalina_home>/webapps`.
Ve spouštěcím skriptu Tomcatu nastavte dodatečné spouštěcí parametry pro aplikační server : `-Djava.awt.headless=true  -XX:MaxPermSize=128m -Xms512m -Xmx1024m` 

## Autentizace  
Autentizace je řešena pomocí autentizačního serveru keycloak. Je nutno provést následující kroky. 

1. Přihlásit se do administračního prostředí keycloaku 
2. Vytvořit nový realm s názvem **kramerius**
3. Vytvořit roli s názvem **kramerius_admin**
4. V seznamu uživatelů vytvořit uživatele/administrátora a přiřadit výše zmíněnou roli 
5. V seznamu "clients" vytvořit nového klienta s názvem "krameriusClient", který má nastavené/povolené následující možnosti: 
   * Valid redirect URIs: ```*```
   * Web origins: ```*```
   * Web origins: ```*```
   * Client authentication: **ON**  
   * Authorization: **ON**  
   * Standard flow: **ON**  
   * Direct access grants: **ON**  
   * Implicit flow: **ON**  
   * OAuth 2.0 Device Authorization Grant: **ON**  
   * Front channel logout: **ON**
   * Backchannel logout session required: **ON**

Konfiguraci klienta je nutno exportovat ve formátu Keycloak OIDC JSON (kontextové menu Action -> Download adaptor configs) a uložit do konfiguračního adresáře: 
~/.kramerius4/keycloak.json
 

## Konfigurace datasource

Do souboru `$CATALINA_HOME/conf/context.xml` přidat definici datasource: 
```
<Resource name="jdbc/kramerius4" auth="Container" type="javax.sql.DataSource"
        initialSize="3"
        maxTotal="100" maxIdle="30" maxWaitMillis="10000"
        username="fedoraAdmin" password="fedoraAdmin" driverClassName="org.postgresql.Driver"
        url="jdbc:postgresql://localhost/kramerius4"/>

```

## Nastavení kódování URI

V aplikačním serveru nastavte kódování URI na UTF-8  ([[příklad pro Tomcat|PrikladKonfigurace#URIEncoding]])


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

Součástí distribuce Krameria 7 je samostatný nástroj pro konverzi formátu úložiště z legacy-fs do formátu Akubra, případně z existujícího formátu Akubra do formátu Akubra s jinou strukturou (s jinou úrovní vnořených adresářů). V obou variantách je konverze prováděna přesouváním (přejmenováváním) souborů mezi kořenovými adresáři původního a nového úložiště v rámci jednoho disku. Soubory tedy nejsou kopírovány a obsah původního úložiště je nevratně odstraněn. 

**Před použitím konvertoru je tedy vhodné původní úložiště zálohovat.**

Konverzní nástroj je součást distribuce Krameria 7 v souboru `migration-x.x.x.zip`. Jeho obsah rozbalte do libovolného adresáře na serveru Krameria, konvertor se spouští příkazem `migration` v podadresáři `bin`. Parametry a nastavení procesu jsou popsány v následujících odstavcích 

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


# Zachování existujících url odkazů při migraci

Pokud je při migraci dat problém, že v datech existují odkazy na starý IIP server a my chceme aby data odkazovala na nový a zároveň není možnost odkazy v datech přímo měnit, je možnost využít [rewrite komponetu aplikačního serveru Tomcat](https://tomcat.apache.org/tomcat-9.0-doc/rewrite.html). 

Komponenta používá přepisovací pravidla podobná httpd serveru Apache. Zde je modelový příklad, jak by přepis ULR mohl vypadat: 

```
RewriteCond %{QUERY_STRING} ^(.*)FIF=/mnt/kramerius/iipimages/(.*)\.jp2&HEI=128&CVT=jpeg$
RewriteRule ^/fcgi-bin/iipsrv.fcgi$ http://newimageserver.library.com/%2/thumb.jpg? [R,L]

RewriteCond %{QUERY_STRING} ^(.*)FIF=/mnt/kramerius/iipimages/(.*)\.jp2&HEI=700&CVT=jpeg$
RewriteRule ^/fcgi-bin/iipsrv.fcgi$ http://newimageserver.library.com/%2/preview.jpg? [R,L]

RewriteCond %{QUERY_STRING} ^(.*)FIF=/mnt/kramerius/iipimages/(.*)\.jp2&WID=999999&CVT=jpeg$
RewriteRule ^/fcgi-bin/iipsrv.fcgi$ http://newimageserver.library.com//%2/big.jpg? [R,L]

RewriteCond %{QUERY_STRING} ^(.*)FIF=/mnt/kramerius/iipimages/(.*)\.jp2&CVT=jpeg$
RewriteRule ^/fcgi-bin/iipsrv.fcgi$ http://newimageserver.library.com//%2/big.jpg? [R,L]

RewriteCond %{QUERY_STRING} ^(.*)Zoomify=/mnt/kramerius/iipimages/(.*)\.jp2/ImageProperties.xml$
RewriteRule ^/fcgi-bin/iipsrv.fcgi$ http://newimageserver.library.com/%2/ImageProperties.xml [R,L]

RewriteCond %{QUERY_STRING} ^(.*)Zoomify=/mnt/kramerius/iipimages/(.*)\.jp2(.*)$
RewriteRule ^/fcgi-bin/iipsrv.fcgi$ http://newimageserver.library.com/%2%3 [R,L] 
```



# Rebuild processing indexu

Kramerius 7 nahrazuje resource index fedory 3 novým jádrem indexu SOLR s identifikátorem `processing`. Pokud Kramerius 7 nasazujete na již existující úložiště ve formátu akubra nebo jste formát úložiště konvertovali utilitou `migration`, je potřeba processing index inicializovat pomocí administrátorského procesu `Rebuild processing indexu`, který můžete  spustit odpovídající položkou v administrátorském menu.  


# OAI4SOLR

Kramerius 7 podporuje protokal OAI pomocí implementace `oai4solr`, která pracuje přímo nad daty indexu SOLR. Instalační soubory a popis instalace a konfigurace je k dipozici v modulu installation/oai (https://github.com/ceskaexpedice/kramerius/tree/master/installation). Pro verzi SOLR6 použijte knihovnu `oai4solr6`, pro SOLR 7 a vyšší knihovnu `oai4solr7`



Po prvním spuštění aplikace se v databázi vytvoří databázové tabulky s předdefinovanými autorizačními pravidly a implicitnim administrátorským uživatelem.  Předdefinované jméno a heslo admin uživatele je: 

`krameriusAdmin` 

`krameriusAdmin`


# Konfigurace

Po prvním spuštění aplikačního serveru s nainstalovanou aplikací Kramerius (pod systémovým uživatelem kramerius4) je v domovském adresáři uživatele kramerius4 vytvořen adresář `.kramerius4` a v něm prázdné soubory `configuration.properties`, `search.properties`,`client.properties`, `indexer.properties` a `migration.properties`. Konfigurační soubory K5 využívají rozšířené syntaxe properties podporované použitou knihovnou Apache commons-configuration.  Soubory jsou uspořádány ve dvoustupňové hierarchii: Základní sdílené properties jsou v souboru configuration.properties, jednotlivé plugin moduly externích procesů je pak rozšiřují ve svých konfiguračních souborech (např. migration.properties, indexer.properties). Konfigurační properties specifické pro GUI K5 jsou v souboru search.properties.

Defaultní hodnoty properties (viz níže) jsou definovány uvnitř aplikačního archivu search.war. Hodnoty je možno předefinovat jejich uvedením ve stejně pojmenovaném souboru umístěném v adresáři $USER_HOME/.kramerius4. Tyto konfigurační soubory (prázdné) jsou vytvořeny automaticky při prvním spuštění K7, resp. příslušného externího procesu.

Obsah defaultních hodnot jednotlivých konfiguračních souborů najdete zde:

  [[configuration.properties|https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/res/configuration.properties]]

[[search.properties|https://github.com/ceskaexpedice/kramerius/blob/master/search/src/java/res/configuration.properties]]

[[indexer.properties|https://github.com/ceskaexpedice/kramerius/blob/master/processes/indexer/src/res/configuration.properties]]

[[migration.properties (konverze z K3)|https://github.com/ceskaexpedice/kramerius/blob/master/processes/import-cmdtool/src/main/resources/res/configuration.properties]]

[[migration.properties (konverze z METS-NDK)|https://github.com/ceskaexpedice/kramerius/blob/master/processes/import-mets/src/main/resources/res/configuration.properties]]

[[static_export.properties|https://github.com/ceskaexpedice/kramerius/blob/master/processes/static-export/src/main/java/res/configuration.properties]]


[[client.properties|https://github.com/ceskaexpedice/kramerius/blob/master/client/src/main/resources/res/configuration.properties]]

Texty jednotlivých součástí GUI Krameria jsou lokalizovány pomocí standardního mechanismu resource bundle jazyka Java (viz např. [[http://docs.oracle.com/javase/6/docs/api/java/util/ResourceBundle.html]]), výchozí obsah lokalizačního souboru `labels.properties` je k dispozici zde: [[labels_cs.properties pro K5|https://github.com/ceskaexpedice/kramerius/blob/master/search/src/java/labels_cs.properties]] 
[[labels_cs.properties pro editor uživatelů|https://github.com/ceskaexpedice/rightseditor/blob/master/src/main/resources/labels_cs.properties]]

Požadované změny je možno provádět přepsáním hodnoty příslušného klíče v souboru `~/.kramerius4/bundles/labels.properties`, resp. `~/.kramerius4/bundles/labels_cs.properties` .

V případě rozsáhlejších, víceřádkových textů, systém Kramerius disponuje mechanismem zápisu textu do samostatného souboru. Soubory mohou být předefinovány v adresáři `~/.kramerius4/texts`.

  * `texts/first_page_nolines_xml`  - obsahuje text o nedostupnosti, který se objeví v dialogu při generování PDF i v samotném dokumentu. Implicitně zobrazovaný text je [[first_page_nolines_xml|https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/texts/first_page_nolines_xml]]
  * `texts/help`  - Obsahuje text nápovědy.  Pokud není definovaný, zobrazí interní nápovědu Krameria.
  * `texts/rightMsg`  - Obsahuje text o nedostupnosti dokumentu.  Pokud není definovaný, zobrazí krátký text z `labels.properties` určený klíčem `rightMsg`
  * `texts/intro`  - Obsahuje popisný text o digitální knihovně.  Implicitně zobrazovaný text [[intro|https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/cz/incad/kramerius/service/impl/res/default_intro]].
  * `texts/k5info`  - Obsahuje popisný zobrazovaný v klientské aplikaci.  Implicitně zobrazovaný text [[intro|https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/cz/incad/kramerius/pdf/impl/res/k5info]].


# Podpora protokolů deepZoom, zoomify, IIIF

(volitelné nastavení)

Kromě standardního zobrazení obrázků v jejich nativním formátu má aplikace Kramerius 5 možnost prezentovat je pomocí integrované prohlížečky Seadragon (http://www.zoom.it). Prohlížečka Seadragon je aktivována pro konkrétní zobrazovaný digitální objekt (například stránku monografie), pokud jeho FOXML definice obsahuje v datastreamu RELS-EXT RDF literál `<kramerius4:tiles-url>`.  Je možno využít dvě alternativy: 

## Využít produkt IIP server (https://web.archive.org/web/20190226234031/https://help.oldmapsonline.org/jpeg2000)

Konfigurace imageserveru je popsána na wiki stránce [[Konfigurace imageserveru pro podporu IIIF|Konfigurace-imageserveru-pro-podporu-IIIF]]
Zde slouží Kramerius jako prostředník. Klientské dotazy na jednotlivé dlaždice přeposílá IIP serveru a sám se stará pouze o autorizaci požadavku. Hodnotou literálu `<kramerius4:tiles-url>` je přímo URL na zoomovaný obrázek v IIP serveru. 

Příklady definic v RELS-EXT:

```
<kramerius4:tiles-url>http://192.168.1.1/fcgi-bin/iipsrv.fcgi?DeepZoom=/mzk03/001/042/654/2619265924.jp2</kramerius4:tiles>

<kramerius4:tiles-url>http://imageserver.mzk.cz/mzk03/001/066/607/2619320306/1</kramerius4:tiles-url>

<kramerius4:tiles-url>http://iipserv.nkp.cz/fcgi-bin/iipsrv.fcgi?Zoomify=/home/k4/iip-data/2619265924.jp2</kramerius4:tiles-url>

```

# Aktualizace na novou verzi Krameria

Při aktualizaci existující instalace Krameria stačí na aplikační server nainstalovat nové verze souborů `*.war` (a případně sdílené knihovny `securtiy-core.jar` ) z distribučního balíčku `Core-x.x.x.tar.gz` a `security-core-x.x.x.tar.gz`. Konfiguraci systému a ostatních komponent z balíčku `installation-x.x.x.zip` a `Editors-x.x.x.zip` není obvykle třeba měnit (pokud u konkrétní verze není uvedeno jinak). 

Postup instalace je závislý na konkrétním aplikačním serveru. Pro server Tomcat je vhodné postupovat takto:
   
* vypněte Tomcat
* **Důležité:** smažte rozbalené adresáře `search` a `rightseditor` z adresáře `tomcat/webapps` a `tomcat/work/Catalina/localhost`
* do adresáře `tomcat/webapps` nakopírujte nové verze souborů `search.war` a `rightseditor.war`, do adresáře `tomcat/lib` soubor `security-core.jar`   
* restartujte Tomcat

Pokud se liší nasazené a nové schéma solr jádra `search` (soubor `managed-schema`), proveďte aktualizaci schématu na vyšší verzi, jako je to popsáno  [zde](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#aktualizace-sch%C3%A9matu-j%C3%A1dro-search) nebo [zde](https://github.com/ceskaexpedice/kramerius/wiki/Vyhled%C3%A1vac%C3%AD-index#nav%C3%BD%C5%A1en%C3%AD-verze-indexeru).

# Doporučení pro instalaci 

* Klientské systémy (klientská aplikace a administrační aplikace) by měly být provozovány za systémem apache a propojené pomocí `mod_ajp` případně `mod_jk`.
* Doporučujeme pro provozování systému Kramerius  použít protokol `https`. 


# Instalace klientské aplikace

Kramerius klient je samostatná aplikace napsaná ve frameworku angular. Její popis instalace a nastavení všech parametrů je možno najít 
[zde](https://github.com/ceskaexpedice/kramerius-web-client/wiki/Nasazen%C3%AD-klienta) 


# Instalace administrační aplikace

Administrace jádra je nyní možná ze samostatného klienta. Popis instalace je vidět [zde](https://github.com/ceskaexpedice/kramerius-admin-client/wiki/Instalace-a-konfigurace#instalace-a-konfigurace)

# Přechod z verze K5

Pro přechod ze starěí verze systému K5 je nutné provést následující kroky: 

Pokud jsou data uložena ve Fedoře ve formátu AKUBRA: 

1. Doinstalovat příslušené komponenty případně nainstalovat v novější verzi (Keycloak, Solr, Postgresql).
2. Vytvořit nové jádra v systému [solr (search, processing, logs)](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#instalace-indexu-solr)
3. Zprovoznit autentizaci přes [Keycloak](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#autentizace)
4. Nastavit konfigurační proměnnout tak, aby ukazovala na data uložené v adresáři pro akubru.
  Jedná se o proměnné: 
```
objectStore.path=<path_to_fedora>/data/objectStore
datastreamStore.path=<path_to_fedora>/data/datastreamStore
```
5. Spustit administrační rozhraní a v něm spustit: 
  *  Vybudovat processing index - Záložka **Repozitář**, tlačítko **Vybudovat processing index**
  *  Reindexovat data - Záložka **Indexace** podzáložka **Model** a tlačítko **Indexovat** 

Pokud jsou data uložena ve Fedoře ve formátu LegacyFS pak je nutno ještě data konvertovat do formátu Akubra pomocí utility MigrationUtils. 
Návod je [zde](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#konverze-legacy-fs---akubra).  
