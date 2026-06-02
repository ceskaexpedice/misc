# Popis instalace a nastavení K7

Popis instalace a konfigurace systému Kramerius 7 s integrovaným úložištěm Akubra. Instalace předchozí verze Kramerius 5 je popsána [[zde|Instalace verze K5]]

Před instalací aplikace Kramerius je třeba nainstalovat následující systémové komponenty:
---
TODO viz prerequisites

## Distribuční soubory

Distribuční soubory jádra aplikace Kramerius najdete v sekci [Releases](https://github.com/ceskaexpedice/kramerius/releases)  

Všechny soubory jsou zabaleny do jednoho archivního souboru kramerius-x.x.x.zip (znaky x.x.x jsou samozřejmě nahrazeny konkrétním číslem verze). 

Pokud v konkrétním release některý z uvedených souborů chybí, znamená to, že v něm oproti předchozí verzi nedošlo k žádné změně.

V následujících odstavcích jsou uvedeny požadavky aplikace Kramerius na specifickou konfiguraci systémových komponent, pokud možno i s odkazy na příklady konkrétních úprav příslušných konfiguračních souborů. Tyto příklady jsou uvedeny pouze pro ilustraci jedné z možných konfigurací a nenahrazují dokumentaci k jednotlivým systémovým komponentám. V případě distribuované instalace je třeba uvedené příklady konfiguračních URL (localhost) nahradit adresami příslušných serverů. 

(v uvedených příkladech konfigurace předpokládáme instalaci Tomcatu do domácího adresáře uživatele kramerius4)

## PostgreSQL

* Vytvořit uživatele `fedoraAdmin` a pro něj databázi `kramerius4` a [nastavit datasource](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#konfigurace-datasource). 


## Konfigurace úložiště Akubra
TODO odkaz na reference
### Synchronizace paralelních zápisů

TODO odkaz na reference

Synchronizace paralelních zápisů do jednoho úložiště z více souběžných procesů a případně více instancí Krameria je zajištěna sdílenou tabulkou zámků v distribuované paměťové databázi Hazelcast. Synchronizace probíhá automaticky a defaultní nastavení není obvykle třeba měnit. K nastavení jména instance a uživatele lze případně použít následující property:

```
hazelcast.instance=akubrasync
hazelcast.user=dev
``` 

## Instalace indexu (SOLR)
1. Stáhněte si poslední verzi vyhledávacího enginu [SOLR](https://lucene.apache.org/solr/downloads.html) 
2. Spustěte příkazem  `<solr_home>/bin/solr start`
3. Nainstalujte potřebná jádra (Solr core), viz níže

TODO odkaz na Reference


#### Aktualizace schématu (jádro search)
Při přechodu na některou vyšší verzi K7 může nastat potřeba aktualizovat schéma (zejména soubor managed-schema) Postup je následující: 

- Stáhněte si konfigurační soubory a slovníky buď z instalačního balíčku nebo přímo z git [repozitáře](https://github.com/ceskaexpedice/kramerius/tree/master/installation/solr-7.x/search/conf).
- Stáhnuté soubory umístěte do adresáře `<solr_home>/server/solr/search`. 
- Otevřte administrační prostředí solru `http://localhost:8983/`. 
- V záložce core-admin vyberte jádro `search` a zmáčkněte tlačítko `reload`.

## Instalace Tomcatu a jádra aplikace 

### Administrační aplikace 
Postup instalace je stejný jako u předchozí verze Kramerius 5. Zkopírujte soubor `search.war` do adresáře `<catalina_home>/webapps`.
Ve spouštěcím skriptu Tomcatu nastavte dodatečné spouštěcí parametry pro aplikační server : `-Djava.awt.headless=true  -XX:MaxPermSize=128m -Xms512m -Xmx1024m` 

### Autentizace  
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
```~/.kramerius4/keycloak.json````
 

### Konfigurace datasource

TODO odkaz na Reference

Do souboru `$CATALINA_HOME/conf/context.xml` přidat definici datasource: 
```
<Resource name="jdbc/kramerius4" auth="Container" type="javax.sql.DataSource"
        initialSize="3"
        maxTotal="100" maxIdle="30" maxWaitMillis="10000"
        username="fedoraAdmin" password="fedoraAdmin" driverClassName="org.postgresql.Driver"
        url="jdbc:postgresql://localhost/kramerius4"/>

```

### Nastavení kódování URI

V aplikačním serveru nastavte kódování URI na UTF-8  ([[příklad pro Tomcat|PrikladKonfigurace#URIEncoding]])


# Import a  migrace dat

Pro import dat lze využít standardních importních procesů. 
* Import standardních foxml dat 
* Import NDK  balíčků 
* Replikace K4.

# Rebuild processing indexu

Kramerius 7 nahrazuje resource index fedory 3 novým jádrem indexu SOLR s identifikátorem `processing`. Pokud Kramerius 7 nasazujete na již existující úložiště ve formátu akubra nebo jste formát úložiště konvertovali utilitou `migration`, je potřeba processing index inicializovat pomocí administrátorského procesu `Rebuild processing indexu`, který můžete  spustit odpovídající položkou v administrátorském menu.  


# OAI4SOLR

Kramerius 7 podporuje protokal OAI pomocí implementace `oai4solr`, která pracuje přímo nad daty indexu SOLR. Instalační soubory a popis instalace a konfigurace je k dipozici v modulu installation/oai (https://github.com/ceskaexpedice/kramerius/tree/master/installation). Pro verzi SOLR6 použijte knihovnu `oai4solr6`, pro SOLR 7 a vyšší knihovnu `oai4solr7`



Po prvním spuštění aplikace se v databázi vytvoří databázové tabulky s předdefinovanými autorizačními pravidly a implicitnim administrátorským uživatelem.  Předdefinované jméno a heslo admin uživatele je: 

`krameriusAdmin` 

`krameriusAdmin`


# Konfigurace

TODO odkaz na reference

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

