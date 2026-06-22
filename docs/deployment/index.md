[Index](../index)

# 🚢 Deployment

Tato kapitola popisuje **způsoby nasazení (deploymentu) systému Kramerius 7**.  
Slouží jako **rozcestník**, který pomůže zvolit vhodný způsob provozu a odkáže na odpovídající instalační a provozní návody.

Kramerius je modulární systém a lze jej provozovat v různých prostředích podle velikosti instance, provozních požadavků a zkušeností provozovatele.

---

## Přehled podporovaných způsobů nasazení

Kramerius lze provozovat těmito základními způsoby:

| Způsob nasazení | Typické použití | Doporučeno pro |
|-----------------|------------------|---------------|
| **On-premise** | Ruční instalace jednotlivých komponent | Menší instance, integrace do existující infrastruktury |
| **Docker Compose** | Kontejnerizované komponenty řízené pomocí Docker Compose | Vývoj, testování, jednodušší produkční provoz |
| **Kubernetes** | Kontejnerizovaný provoz v orchestraci | Velké instance, vysoká dostupnost, škálování |

Každý způsob nasazení má své výhody a omezení. Podrobné návody jsou uvedeny v příslušných **Guides**.

---

## On-premise (klasická instalace)

On-premise deployment znamená provoz Krameria jako sady samostatných služeb instalovaných přímo na server (nebo servery).

Typicky zahrnuje:
- Java (JDK)
- Apache Tomcat
- Kramerius jádro (search.war)
- SOLR
- Další podpůrné služby (Keycloak, databáze apod.)

Tento způsob poskytuje **maximální kontrolu nad prostředím**, ale vyžaduje více manuální konfigurace a správy.

➡️ [Instalace On Premise](on-premise/installation)

---

## Docker Compose

Pro zjednodušení instalace a provozu je k dispozici projekt **Kramerius Docker Compose**, který obsahuje všechny potřebné komponenty již kontejnerizované.

Charakteristiky:
- rychlé spuštění
- jednotné prostředí
- vhodné pro vývoj i produkční provoz menších a středních instancí
- nižší nároky na znalost infrastruktury

Typicky postačuje:
- nainstalovaný Docker
- nainstalovaný Docker Compose
- spuštění celé instance jedním příkazem

➡️ [Deployment Docker Compose](../guides/admin/installation)

---

## Kubernetes

Pro velké nebo kritické instalace lze Kramerius provozovat v prostředí **Kubernetes**.

Tento způsob umožňuje:
- vysokou dostupnost
- horizontální škálování
- oddělení jednotlivých komponent
- integraci s existující cloudovou infrastrukturou

Je určen především pro:
- národní nebo centrální digitální knihovny
- instance s velmi velkým objemem dat
- provozní týmy se zkušeností s Kubernetes

➡️ [Deployment Kubernetes](../guides/admin/installation)

---

## Jak zvolit správný způsob nasazení

Obecné doporučení:

- **Vývoj / testování** → Docker Compose
- **Menší produkční instance** → Docker Compose nebo On-premise
- **Velké produkční instance** → Kubernetes

Detailní požadavky (velikost indexu, dostupnost, bezpečnost, zálohování) jsou popsány v jednotlivých guidech.

---

## Vztah k ostatním částem dokumentace

- **Getting Started**  
  Stručný úvod do systému a odkazy na tuto kapitolu.

- **Guides**  
  Konkrétní instalační a provozní návody pro jednotlivé typy nasazení.

- **Core Concepts**  
  Popis architektury a principů Krameria, nezávislý na způsobu deploymentu.

- **References**  
  Technické reference (konfigurační parametry, API, schémata), použitelné napříč všemi způsoby nasazení.

---

## Shrnutí

Tato kapitola slouží jako **rozcestník deploymentu**:
- neobsahuje detailní návody
- pomáhá s výběrem vhodného řešení
- odkazuje na odpovídající **Guides**
