# Akubra Storage

Tato kapitola poskytuje **referenční popis úložiště Akubra**, které Kramerius používá pro perzistenci digitálních objektů. Zaměřuje se na architekturu, odpovědnosti a konfigurační vazby tohoto storage backendu. Neobsahuje instalační ani migrační postupy.

---

## Účel Akubra storage

Akubra slouží jako **hlavní perzistentní úložiště digitálních objektů** v Krameriovi. Je navržena tak, aby:

- poskytovala stabilní a transakčně konzistentní úložiště,
- oddělovala logickou reprezentaci objektů od fyzického uložení dat,
- umožňovala různé implementace backendu bez změn aplikační logiky.

Kramerius pracuje s Akubrou jako s abstraktní vrstvou nad filesystemem.

---

## Architektonický model

Akubra storage je založena na následujících principech:

- **Objektový model**  
  Každý digitální objekt je reprezentován jako logická jednotka s vlastní identitou.

- **Oddělení logiky a fyzického uložení**  
  Aplikace nepracuje přímo s konkrétními cestami na disku.

- **Stabilní identifikátory**  
  Fyzická struktura úložiště není určena pro přímou manipulaci uživatelem.

Tento model umožňuje měnit interní strukturu úložiště bez dopadu na vyšší vrstvy aplikace.

---

## Typy uložených dat

Akubra storage typicky obsahuje:

- binární reprezentace digitálních objektů,
- technická metadata potřebná pro správu objektů,
- interní struktury nutné pro konzistenci a obnovu dat.

Obsah úložiště je považován za **aplikačně řízený**, nikoli uživatelsky editovatelný.

---

## Konfigurační vazby

Konfigurace Akubry je oddělena od ostatních částí aplikace, ale má přímé vazby na:

- indexační mechanismy,
- exportní a integrační procesy,
- distribuované zámky v clusterovém prostředí.

Změna konfigurace Akubry může ovlivnit:

- dostupnost dat,
- výkon operací nad objekty,
- chování paralelních instancí aplikace.

---

## Akubra a běh ve více instancích

V prostředí s více běžícími instancemi Krameria:

- Akubra storage je typicky **sdílená**,
- přístup k ní musí být synchronizován,
- konzistence je zajišťována ve spolupráci s distribuovanými zámky.

Z tohoto důvodu je Akubra úzce provázána s konfigurací **Hazelcast Locking**.

---

## Omezení a očekávání

Při práci s Akubra storage se předpokládá, že:

- úložiště je spolehlivé a perzistentní,
- nedochází k manuálním zásahům do jeho struktury,
- zálohování je řešeno na úrovni infrastruktury.

Porušení těchto předpokladů může vést k nekonzistenci nebo ztrátě dat.

---

## Vazba na další referenční kapitoly

Tato kapitola popisuje roli Akubry v architektuře Krameria. Konkrétní technické detaily jsou popsány v následujících kapitolách:

- **Akubra Storage Configuration** – konfigurační parametry a struktura
- **Legacy Storage** – alternativní model úložiště
- **Hazelcast Locking** – synchronizace přístupu v clusteru

---

Další stránka v referenci: **`Akubra-Storage-Configuration.md`**.  
Mám pokračovat?
