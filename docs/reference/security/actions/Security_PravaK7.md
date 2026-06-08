#Přístupová práva
[[_TOC_]]

# Úvod

Systém práv pro systém vychází ze [[systému práv v K5|PravaK5]]. Na straně K7 došlo k úpravám:

 - byla vytvořena role kramerius_admin která nahrazuje dřívější roli k4_admins (k4_admins zůstává pouze z důvodu zpětné kompatibility, v pozdějších verzích bude jádrem aktivně mazána)
 - došlo ke zrušení nepoužívaných akcí a přejmenování stávajících, případně byly některé akce sloučeny do jedné 


# Nové akce

Reprezentované akce v K7:  

- *a_read/Číst* - Akce čti definuje operaci číst data (obrázky). _Pokud má uživatel práva tuto akci provádět, objeví se mu  velký náhled, vygeneruje PDF nebo zobrazí deepZoom prohlížečka._
- *a_pdf_read/Pdf a tisk* - Definuje použití endpointu pro generování pdf dokumentů případně tisku
- *a_delete/Mazání* - Smazání objektu, resp. spuštění procesu mazání nad objektem. 
- *a_process_read/Ćtení procesů* - Možnost si číst procesy (v admin rozhraní zobrazit tabulku spuštěných procesů) 
- *a_process_edit/Správa procesů* - Možnost číst a spravovat procesy (v admin rozhraní zobrazit tabulku spuštěných procesů s 
možností spravovat proces = zastavit proces, smazat proces, vstoupit do detailu a prohlížet logy). Pokud má uživatel nadefinovanou tuto akci, nemusí mít již definovanou akci _a_process_read_
- *a_owner_process_edit/Správa vlastních procesů*  - Možnost číst a spravovat _svoje_ procesy, tedy procesy spuštěné konkrétním uživatelem.  
- *a_index/Indexace*  - Možnost spustit indexaci na konkrétním objektu.
- *a_rebuild_processing_index/Rebuild procssing indexu*  - Možnost spuštění procesu pro rebuild processing indexu. 
- *a_import/Import* - Možnost spuštění importního procesu. Pokrývá operace import FOXML a NDK-METS balíčku.    
- *a_set_accessibility/Přístupnost* - Možnost spuštění procesu nastavení nastavení přístupnosti objetů, 
pokrývá operace nastavení příznaku i nastavování a rušení licencí 
- *a_set_accessibility/Přístupnost* - Možnost spustit nastavení přístupnosti případně licence 
- *a_export_cdk/Export do ČDK* - Přístup pro ČDK
- *a_statistics/Statistiky* - Možnost číst statistky
- *a_statistics_edit/Editace statistik* - Možnost mazání statistik
- *a_export_replications/Export replikace* - Umožnění replikace titulu 
- *a_import_replications/Import replikace* - Umožnění spuštění procesu replikace
- *a_rights_edit/Editace práv* - Umožnění editace práv
- *a_criteria_read/Kritéria* - Umožnění čtení kritérií.
- *a_collections_read/Čtení sbírek* - Umožní číst/zobrazit seznam sbírek
- *a_collections_edit/Editace sbírek* - Umožní upravovat sbírky případně vybranou sbírku 
- *a_able_tobe_part_of_collections* - Právo umožní uživatelům přidávat vybrané díla do sbírek. 
V případě, že je právo nastaveno na úrovni repositáře, pak má uživatel právo přidávat všechny objekty. 
- *a_generate_nkplogs/Generování NKP logů* - Akce pro spuštění generování NKP logů 
- *a_roles_edit/Editace rolí* - Akce přidávání/mazaní/editace rolí 
- *a_roles_read/Čtení rolí* - Akce čtení rolí
- *a_admin_read/Admin čtení* - Přístup do administračního rozhraní

# Dědičnost objektů a sbírky

Dědičnost zůstala zachována, tedy pokud je má definované právo nadřazeý objekt, má právo i jeho potomek.  Blíže je to specifikované zde: [[systému práv v K5|PravaK5#Dedicnost]].

U sbírek je tento fakt důležitý: Pokud má uživatel práva na vrchní úroveň sbírky, pak má stejná práva i na podsbírky. Z toho důvodu vznikla akce  `a_able_tobe_part_of_collections`, která kontroluje objekty, které si můžete do sbírky přiřadit. (Aby se zabránilo situaci, kdy uživatel má právo pouze na svou vlastní sbírku a přidáním cizích sbírek/objektů získá právo s nimi manipulovat)  

