# Configuration Overview

Tato kapitola poskytuje **referenční přehled konfiguračního modelu Krameria**. Popisuje základní principy konfigurace, typy konfiguračních zdrojů a jejich vzájemné vztahy. Neslouží jako instalační návod – cílem je vysvětlit *co* se konfiguruje a *proč*.

---

## Základní principy konfigurace

Konfigurace Krameria je rozdělena do několika vrstev, které se navzájem doplňují:

- **Aplikační konfigurace**  
  Řídí chování samotné aplikace (repozitáře, indexace, protokoly, cache, integrace).

- **Provozní konfigurace**  
  Závisí na prostředí, ve kterém je Kramerius spuštěn (on-premise, Docker, cluster).

- **Konfigurace úložišť a sdílených služeb**  
  Řeší práci s perzistentními daty a synchronizaci mezi instancemi.

Jednotlivé konfigurační prvky nejsou izolované – změna v jedné části (např. úložiště) má přímý dopad na další subsystémy (indexace, IIIF, exporty).

---

## Konfigurační zdroje

Kramerius využívá kombinaci několika typů konfiguračních zdrojů.

### Konfigurační soubory

Základ konfigurace je definován v souborech uložených na filesystemu aplikace. Tyto soubory:

- popisují strukturovaná nastavení (např. storage, indexy, služby),
- jsou čitelné a verzovatelné,
- tvoří hlavní referenční bod konfigurace.

Konkrétní přehled souborů a jejich význam je popsán v kapitole **Configuration Files**.

---

### Systémové proměnné

Některé hodnoty mohou být dodány nebo přepsány pomocí systémových proměnných:

- typicky pro rozdíly mezi prostředími,
- bez nutnosti měnit samotné konfigurační soubory,
- často využívané v kontejnerových instalacích.

---

### Externí služby

Část konfigurace se netýká pouze aplikace samotné, ale definuje vazby na externí komponenty:

- úložiště (Akubra, legacy filesystem),
- distribuované zámky (Hazelcast),
- indexační a exportní mechanismy,
- integrační protokoly (IIIF, OAI-PMH).

Tyto oblasti jsou popsány v samostatných referenčních kapitolách.

---

## Hierarchie a precedence

Konfigurace má jasnou hierarchii, která určuje, odkud je výsledná hodnota převzata:

1. **Explicitní konfigurace v souborech**
2. **Přepsání pomocí systémových proměnných**
3. **Implicitní výchozí hodnoty aplikace**

Tento model umožňuje:

- mít stabilní základní konfiguraci,
- zároveň snadno přizpůsobit chování konkrétnímu prostředí.

---

## Konfigurace a běhové prostředí

Konfigurační model Krameria počítá s tím, že aplikace může běžet:

- jako jedna instance,
- nebo jako více instancí sdílejících společná data.

V takovém případě se konfigurace musí zabývat:

- konzistencí zápisů,
- sdíleným přístupem k úložišti,
- synchronizací operací mezi uzly.

Tyto aspekty jsou detailně rozebrány v kapitolách **Akubra Storage** a **Hazelcast Locking**.

---

## Vazba na další referenční kapitoly

Tato stránka slouží jako vstupní bod do referenční dokumentace konfigurace. Podrobnosti jsou rozděleny do následujících kapitol:

- **Configuration Files** – konkrétní soubory a jejich role
- **Akubra Storage** – perzistentní úložiště digitálních objektů
- **Legacy Storage** – původní model práce s filesystemem
- **Hazelcast Locking** – distribuované zámky a synchronizace
- **Protocols (IIIF, OAI-PMH)** – konfigurační dopady integračních rozhraní  
