[Index](../../index) / [Konfigurace](../../configuration)

# Process platform konfigurace

- ➡️ [Konfigurace skrze Core](../core/configuration-properties/configuration-process-platform.md)
- ➡️ [Process Platform modul](https://github.com/ceskaexpedice/process-platform/wiki/RunningPlatform)
- ➡️ [Konfigurace Plugins](../../reference/process-platform/plugins)


## Public worker sablony 

Úvodní stránka PDF
Generování první stránky je možno ovlivnit vlastní šablonou. Stránka se může lišit dle licence a jazykové mutace. Šablony jsou uložené na následující cestě:

```text
<home>/
└─ .kramerius4/
   └─ process-pdfs-settings/
      └─ public/
         ├─ firstpage.xml
         ├─ cs/
         │  └─ firstpage.xml
         └─ special-needs/
            ├─ firstpage.xml
            └─ cs/
               └─ firstpage.xml
```

Kde adresář process-pdfs-settings odpovídá hlavnímu konfiguračnímu adresáři, pod ním jsou podadresáře odpovídající licencím, nyní buď public nebo special-needs a každý adresář může obsahovat defaultní šablonu firstpage.xml nebo podadresáře se šablonami odpovídající jazkovým mutacím cs, en, atd..

Příklad šablon naleznete zde.

## Navazujici dokumentace

- ➡️ [Reference](../../reference/process-platform/)

