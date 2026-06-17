[Index](../index) / [Začínáme](../getting-started)

# 🛠 Zaciname – Administrátor

Tato stránka je určena jako **vstupní rozcestník pro systémové administrátory a IT pracovníky**, kteří zajišťují instalaci, konfiguraci a provoz platformy Kramerius.

Nejde o detailní návody krok za krokem.  
Cílem je pomoci vám:
- pochopit roli administrátora v ekosystému Kramerius
- zorientovat se v hlavních komponentách systému
- najít správné části dokumentace, kde pokračovat dál

---

## Pro koho je tato stránka

Určeno pro **administrátory Krameria**, kteří:
- instalují a nasazují systém
- konfigurují jednotlivé komponenty
- zajišťují provoz, monitoring a aktualizace
- odpovídají za bezpečnost a technické integrace

Pokud pracujete primárně s obsahem (sbírky, metadata, procesy), použijte  
👉 **[Zaciname – Kurátor](curator)**

---

## Role administrátora v Kramerius

Administrátor v Krameriovi typicky řeší:

- technickou instalaci a nasazení systému
- konfiguraci Core a navazujících komponent
- provozní dohled, monitoring a logování
- aktualizace, zálohování a obnovu dat
- nastavení bezpečnosti a integrací s externími systémy

> Tato stránka slouží jako **mentální checklist**, nikoli jako provozní manuál.

---

## Přehled systému z pohledu administrátora

Administrátor by měl mít základní přehled o těchto částech systému:

- **Kramerius Core**  
  Centrální Java aplikace běžící v Tomcatu, poskytující REST API.

- **UI klienti**  
  Čtenářský klient a Admin Client napojené na Core.

- **Repository (Akubra / Fedora)**  
  Fyzické uložení digitálních objektů, struktura dat a zálohování.

- **Solr**  
  Indexace a vyhledávání nad digitálním obsahem.

- **Procesní framework**  
  Technický běh importních a dávkových procesů.

- **Autentizace a autorizace**  
  Integrace s IdP (např. Keycloak) a řízení rolí a oprávnění.

Detailní vysvětlení těchto pojmů najdete v části  
👉 **[Základní pojmy](../core-concepts/index)**

---

## Způsoby nasazení

Kramerius lze provozovat v různých typech prostředí:

- **Docker Compose**  
  Doporučený start pro testování a menší instalace.

- **Kubernetes**  
  Produkční provoz s důrazem na škálování a dostupnost.

- **On-premise instalace**  
  Tradiční instalace bez kontejnerizace (legacy scénáře).

Popis najdete v části  
👉 **[Deployment](../deployment/index)**

---

## Bezpečnost

Bezpečnost je průřezové téma, které se týká více částí systému.

Administrátor by měl rozumět:
- základním bezpečnostním principům Krameria
- vazbě mezi uživateli, rolemi a obsahem
- integraci s externím poskytovatelem identity

Detailní technické informace patří do  
👉 **[Bezpečnost](../reference/security/index)**

---

## Jak pokračovat dál

Po přečtení této stránky doporučujeme následující cestu:

1. **[Základní pojmy](../core-concepts/index)** – vytvoření správného mentálního modelu systému
2. **[Návody](../guides/admin/index)** – instalace, konfigurace a provoz
3. **[Scénáře](../scenarios/index)** – reálné situace (např. nasazení nové instance, integrace knihovny)
4. **[Reference](../reference/index)** – detailní technické informace a konfigurace

---

## Co tato stránka nepokrývá

Tato stránka:
- neobsahuje detailní instalační postupy
- neřeší správu obsahu a sbírek
- nenahrazuje detailní dokumentaci jednotlivých komponent

Slouží jako **stabilní vstupní bod do dokumentace pro roli administrátora**.
