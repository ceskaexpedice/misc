[Index](../index) / [Konfigurace](../../configuration)

# Process platform konfigurace

- ➡️ [Process Platform](https://github.com/ceskaexpedice/process-platform/wiki/RunningPlatform)
- ➡️ [Konfigurace Plugins](../reference/process-platform/plugins)
- ➡️ [Konfigurace Public Worker](../core/configuration-process-platform.md)


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


# Parametry mail.properties


| Parametr | Popis | Výchozí hodnota |
|-----------|--------|----------------|
| `mail.from.user` | E-mailová adresa odesílatele, která bude uvedena v poli **From** u odesílaných zpráv. | – |
| `mail.smtp.user` | Uživatelské jméno používané pro autentizaci vůči SMTP serveru. Obvykle se jedná o e-mailovou adresu. | – |
| `mail.smtp.host` | Název nebo IP adresa SMTP serveru používaného pro odesílání e-mailů. | – |
| `mail.smtp.startttls.enable` | Povolení protokolu STARTTLS pro zabezpečení komunikace se SMTP serverem. Hodnoty: `true` nebo `false`. | – |
| `mail.smtp.port` | Port SMTP serveru. Například `25`, `465` nebo `587`. | – |
| `mail.smtp.auth` | Určuje, zda je pro připojení k SMTP serveru vyžadována autentizace. Hodnoty: `true` nebo `false`. | – |
| `mail.smtp.socketFactory.port` | Port používaný SSL socket factory. Obvykle odpovídá hodnotě `mail.smtp.port`. | – |
| `mail.smtp.socketFactory.class` | Implementace socket factory používaná pro SSL/TLS spojení. | `javax.net.ssl.SSLSocketFactory` |