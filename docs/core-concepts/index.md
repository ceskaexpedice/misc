# Core Concepts

## Přehled

Kramerius je platforma pro správu, dlouhodobé uchovávání a zpřístupňování digitalizovaných dokumentů.

Systém umožňuje:

- ukládání digitálních objektů a jejich metadat
- správu digitalizovaného obsahu
- indexaci a vyhledávání
- řízení přístupových práv
- zpřístupnění obsahu prostřednictvím REST API
- automatizované zpracování pomocí asynchronních procesů

Tato část dokumentace vysvětluje základní koncepty a pojmy používané napříč celým systémem.

---

## Jak číst dokumentaci

Dokumentace Krameria je rozdělena do několika částí:

| Sekce | Zaměření |
|---------|---------|
| Core Concepts | základní pojmy a doménový model |
| Architecture | vztahy mezi komponentami a datové toky |
| Reference | technická reference jednotlivých subsystémů |
| Configuration | konfigurace systému |
| Deployment | nasazení a provoz |
| Guides | návody a pracovní postupy |

Core Concepts představují společný slovník používaný ve všech ostatních částech dokumentace.

---

## Digitální objekt

Základní jednotkou systému je digitální objekt.

Digitální objekt může představovat například:

- knihu
- periodikum
- číslo periodika
- stránku
- obrázek
- zvukový dokument
- jiný digitalizovaný materiál

Objekty jsou organizovány do hierarchických struktur a tvoří logický model dokumentu.

---

## PID

Každý digitální objekt má jednoznačný identifikátor označovaný jako PID (Persistent Identifier).

PID slouží jako:

- primární identifikátor objektu
- identifikátor používaný v REST API
- identifikátor používaný při indexaci
- identifikátor používaný v procesních úlohách

PID představuje základní identitu objektu v celém systému.

---

## Metadata

Každý objekt obsahuje metadata popisující jeho obsah.

Metadata mohou obsahovat například:

- název
- autora
- datum vydání
- jazyk
- typ dokumentu
- licenční informace

Metadata jsou ukládána v repository a současně indexována pro účely vyhledávání.

---

## Datastreamy

Kromě metadat obsahují objekty také datastreamy.

Datastream představuje konkrétní uložená data připojená k objektu.

Typickými příklady jsou:

- bibliografická metadata
- technická metadata
- OCR text
- obrazová data
- zvukové soubory

---

## Repository

Digitální objekty jsou ukládány v repository vrstvě.

Repository zajišťuje:

- ukládání objektů
- správu datastreamů
- verzování dat
- přístup k digitálnímu obsahu

Implementace repository je založena na Fedora repository a modulu Akubra.

---

## Vyhledávání

Pro vyhledávání dokumentů používá Kramerius indexační vrstvu založenou na Apache Solr.

Vyhledávání je založeno na:

- indexovaných metadatech
- OCR textech
- facetech
- filtrování výsledků

Reader klient využívá search index jako hlavní zdroj pro vyhledávání dokumentů.

---

## Přístupová práva

Kramerius rozlišuje autentizaci a autorizaci.

Autentizace ověřuje identitu uživatele.

Autorizace rozhoduje:

- které objekty může uživatel zobrazit
- jaké operace může provádět
- jaká omezení vyplývají z licencí a rolí

---

## Procesy

Některé operace v systému probíhají asynchronně.

Typicky:

- importy dokumentů
- exporty
- indexace
- dávkové operace
- administrativní úlohy

Tyto operace jsou vykonávány prostřednictvím Process Frameworku.

---

## Process Framework

Process Framework je samostatná komponenta zajišťující plánování a vykonávání procesů.

Procesy jsou:

- vytvářeny administrátory
- spravovány Process Managerem
- vykonávány worker službami

Administrace procesů probíhá prostřednictvím Admin klienta.

---

## REST API

Hlavní způsob komunikace s Krameriem představuje REST API.

API poskytuje přístup k:

- digitálním objektům
- metadatům
- stránkám dokumentů
- vyhledávání
- správě procesů
- administrativním operacím

REST API je využíváno klientskými aplikacemi i integračními systémy.

---

## Klientské aplikace

Kramerius typicky využívá dva hlavní klienty.

### Reader

Aplikace určená pro koncové uživatele.

Poskytuje:

- prohlížení dokumentů
- vyhledávání
- práci s digitálními sbírkami

### Admin

Administrativní aplikace určená správcům systému.

Poskytuje:

- správu dokumentů
- správu procesů
- správu konfigurace
- kurátorské operace

---

## Další kapitoly

Doporučené pokračování:

- Digital Objects
- PID
- Metadata
- Datastreams
- Collections
- Licenses
- Search Index
- Process Framework

Tyto kapitoly rozvíjejí jednotlivé koncepty podrobněji.