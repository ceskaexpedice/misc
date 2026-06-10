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

![Diagram](../assets/fedora-obj-tree.png)
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
  
![Diagram](../assets/fedora-obj-tree-streams.png)

---

## Sbirky

Digitální objekty mohou byt seskupovany do sbirek.

![Diagram](../assets/collections-path.png)

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

## Next Steps

- 📚 [Akubra Reference](../../reference/akubra/)