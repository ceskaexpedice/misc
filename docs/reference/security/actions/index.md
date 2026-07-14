# Actions

Akce představují oprávnění používaná autorizačním systémem.

Seznam je k dispozici [zde](https://github.com/ceskaexpedice/kramerius/blob/master/shared/common/src/main/java/cz/incad/kramerius/security/SecuredActions.java)

## Chráněné akce

* **A_READ**  
  Má právo číst konkrétní objekt. Jedná se o klíčovou akci v systému, která rozhoduje, zda má uživatel povolení číst daný dokument nebo jeho jednotlivé stránky.

* **A_PDF_READ**  
  Akce uděluje uživateli právo přistupovat k PDF zdrojům. Pokud není povolena, přístup k PDF endpointům je zcela zakázán. I když je akce povolena, nemusí to znamenat, že uživatel získá přístup ke skutečným skenům dokumentu. Pokud nemá právo číst daný dokument, místo skenů se v PDF zobrazí hláška o nedostupnosti. Tato akce je standardně povolena pro všechny uživatele.

* **A_DELETE**  
  Akce reprezentuje možnost mazat konkrétní objekt/pid.

* **A_PROCESS_EDIT**  
  Akce reprezentuje možnost spravovovat všechny procesy. Mazat, prohlížet logy, atd..

* **A_PROCESS_READ**  
  Akce reprezentuje možnost read operace nad procesy. Možnost prohlížet logy, prohlížet seznamy procesů, atd..

* **A_OWNER_PROCESS_EDIT**  
  Akce umožňuje spravovat pouze vlastní procesy, tedy ty, u kterých je uživatel uveden jako vlastník. Toto je obzvláště důležité v případech, kdy jsou v systému Kramerius rozlišeni administrátoři a subadministrátoři. Subadministrátoři mohou spravovat pouze vlastní procesy a díla, zatímco plná správa ostatních procesů zůstává na administrátorech.

* **A_INDEX**  
  Akce umožňuje spustit indexační a reindexační procesy

* **A_REBUILD_PROCESSING_INDEX**  
  Akce umožňuje spouštet proces pro vybudování `processing indexu`

* **A_IMPORT**  
  Akce umožňuje spouštět FOXML a NDK Mets importy

* **A_SET_ACCESSIBILITY**  
  Právo nastavovat příznak viditelnosti a licence.

* **A_EXPORT_CDK**  
  Export pro CDK.

* **A_STATISTICS**  
  Zobrazení statistik.

* **A_STATISTICS_EDIT**  
  Možnost mazat statistiky.

* **A_EXPORT_STATISTICS**  
  Exportování statistik třetím stranám.

* **A_EXPORT_REPLICATIONS**  
  Replikace - export.

* **A_IMPORT_REPLICATIONS**  
  Replikace - import.

* **A_RIGHTS_EDIT**  
  Editace práv pro všechny objekty kromě sbírek.

* **A_CRITERIA_READ**  
  Právo číst kritéria.

* **A_COLLECTIONS_READ**  
  Právo číst informace o kolekcích z administrátorského pohledu.

* **A_COLLECTIONS_EDIT**  
  Editace kolekcí, přidávání do kolekcí.

* **A_ABLE_TOBE_PART_OF_COLLECTION**  
  Právo být zařazen do kolekce.

* **A_GENERATE_NKPLOGS**  
  Spuštění NKP logů.

* **A_ROLES_EDIT**  
  Editace rolí.

* **A_ROLES_READ**  
  Čtení rolí.

* **A_ADMIN_READ**  
  Právo na čtení administrátorského rozhraní.

* **A_SDNNT_SYNC**  
  Synchronizace SDNNT.

* **A_OBJECT_EDIT**  
  Editace objektů.

* **A_ADMIN_API_SPECIFICATION_READ**  
  Čtení specifikace OpenAPI pro administraci.
