# Prerequisites (On-Premise Deployment)

Tato stránka popisuje **technické předpoklady prostředí**, které musí být splněny před samotnou instalací Krameria v režimu **on‑premise**.

Cílem této kapitoly je připravit běhové prostředí tak, aby bylo možné Kramerius bez problémů nainstalovat a spustit. Samotná instalace Krameria je popsána v samostatné kapitole.

---

## Přehled požadavků

Pro on‑premise provoz Krameria jsou vyžadovány následující komponenty:

* Operační systém
* Java (JDK)
* Aplikační server (Apache Tomcat)
* Databáze
* Vyhledávací server (SOLR)
* Dostatečné systémové prostředky

---

## Operační systém

Kramerius je primárně provozován na Linuxových serverech. Podporované a běžně používané jsou zejména:

* Debian / Ubuntu
* RHEL / AlmaLinux / Rocky Linux

Provoz na jiných Unix‑like systémech je možný, ale není oficiálně testován.

---

## Java

Kramerius je Java aplikace a vyžaduje nainstalované **JDK** (nikoli pouze JRE).

* Doporučená verze: **Java 21**
* JAVA_HOME musí být nastaveno v prostředí, kde běží aplikační server

Je nutné zajistit, aby Tomcat i všechny pomocné nástroje používaly stejnou Java verzi.

---

## Aplikační server (Apache Tomcat)

Kramerius je distribuován jako WAR aplikace a je určen k provozu v aplikačním serveru **Apache Tomcat**.

* Doporučená verze Tomcatu odpovídající použité Java verzi
* Tomcat musí být spuštěn pod samostatným systémovým uživatelem
* Musí být zajištěn zápis do pracovních a datových adresářů Krameria

Konkrétní postup nasazení Krameria do Tomcatu je popsán v kapitole **Installation**.

---

## Databáze

Kramerius využívá relační databázi pro ukládání aplikačních dat.

* Doporučená databáze: **PostgreSQL**
* Databáze musí být dostupná z aplikačního serveru
* Je nutné mít vytvořenou databázi a uživatele s odpovídajícími právy

Podrobnosti o databázovém schématu a konfiguračních parametrech jsou uvedeny v části **Reference**.

---

## Vyhledávací server (SOLR)

Vyhledávání v Krameriovi je realizováno pomocí **Apache SOLR**.

* SOLR musí běžet jako samostatná služba
* Musí být dostupný z aplikačního serveru přes HTTP
* Je nutné mít připravené jádro (core / collection) pro Kramerius

Volba mezi standardním SOLR a SOLR Cloud závisí na velikosti instance a objemu dat.

---

## Systémové prostředky

Minimální požadavky na server se liší podle velikosti instance a objemu dat. Obecně je nutné počítat s:

* Dostatečnou pamětí pro JVM (heap)
* Rychlým diskovým úložištěm
* Stabilním síťovým připojením mezi jednotlivými komponentami

Doporučení pro sizing je uvedeno v samostatných kapitolách dokumentace.

---

## Další kroky

Po splnění všech výše uvedených předpokladů můžete pokračovat kapitolou:

* **Guides → Deployment → On‑Premise → Installation**

Podrobné vysvětlení jednotlivých pojmů a konfiguračních parametrů je k dispozici v části **Reference**.
