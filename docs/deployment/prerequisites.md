# Prerequisites

Před instalací aplikace Kramerius je třeba zajistit následující systémové komponenty:

## Java
- JDK 11 (OpenJDK nebo Oracle JDK)
- Instalační balíčky:
    - [OpenJDK](https://openjdk.java.net/)
    - [Oracle JDK](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)

## Aplikační server
- Tomcat 9.x
- Stáhnout: [Apache Tomcat](https://tomcat.apache.org/)

## Databáze
- PostgreSQL 8.4 nebo novější
- Možnosti instalace:
    - Nativní instalace podle dokumentace PostgreSQL
    - Docker image nebo předpřipravené image z projektu Bitnami

## Vyhledávací engine
- Solr 8.0 a vyšší
- Instalace:
    - Samostatný balík: [Apache Solr](https://solr.apache.org/)
    - Pro Docker/Kubernetes doporučujeme předpřipravené image z Bitnami nebo Solr Operator

## Autentizační server
- Keycloak (libovolná volně dostupná verze)
- Stáhnout: [Keycloak](https://www.keycloak.org/)
- Poznámka: Pro rozchození Federace eduID je nutné řešit pomocí klonu Keycloak (více info [keycloak-eduid](https://www.keycloak.org/eduid))

## Webový server
- Apache httpd nebo Nginx (libovolná volně dostupná verze)
- Doporučení pro produkční prostředí: před J2EE server (Tomcat) předřadit webserver přístupný na portu 80, např. Apache s moduly `mod_proxy` a `mod_proxy_ajp`.

## Operační systém
- Libovolný systém, na kterém lze provozovat výše uvedené komponenty
- Testováno na běžných distribucích Linuxu

## Hardware
- Velikost pevného disku: doporučeno minimálně dvojnásobek plánované velikosti dat
- RAM: alespoň 8 GB pro minimální provoz (kvůli náročnosti práce s grafickými daty)

## Uživatelský účet
- Doporučeno instalovat K7 pod samostatným uživatelským účtem, např. `kramerius`

## Poznámka k instalaci komponent
- Každou komponentu systému Kramerius (aplikace Kramerius – `search.war`, indexer Solr, databáze PostgreSQL) lze instalovat na samostatný server
- Administrace jednotlivých systémových komponent není součástí této dokumentace; předpokládáme, že administrátor zná jejich instalaci a správu

## Distribuční soubory

Distribuční soubory jádra aplikace Kramerius najdete v sekci [Releases](https://github.com/ceskaexpedice/kramerius/releases)
Všechny soubory jsou zabaleny do jednoho archivního souboru kramerius-x.x.x.zip (znaky x.x.x jsou samozřejmě nahrazeny konkrétním číslem verze).
Pokud v konkrétním release některý z uvedených souborů chybí, znamená to, že v něm oproti předchozí verzi nedošlo k žádné změně.
V následujících odstavcích jsou uvedeny požadavky aplikace Kramerius na specifickou konfiguraci systémových komponent, pokud možno i s odkazy na příklady konkrétních úprav příslušných konfiguračních souborů. Tyto příklady jsou uvedeny pouze pro ilustraci jedné z možných konfigurací a nenahrazují dokumentaci k jednotlivým systémovým komponentám. V případě distribuované instalace je třeba uvedené příklady konfiguračních URL (localhost) nahradit adresami příslušných serverů.
(v uvedených příkladech konfigurace předpokládáme instalaci Tomcatu do domácího adresáře uživatele kramerius4)

## PostgreSQL

* Vytvořit uživatele `fedoraAdmin` a pro něj databázi `kramerius4` a [nastavit datasource](https://github.com/ceskaexpedice/kramerius/wiki/Guides_Instalace#konfigurace-datasource). 

