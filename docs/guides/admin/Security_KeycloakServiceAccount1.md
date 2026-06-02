Servisní účet je možno vytvořit v keycloaku následujícím způsobem: 

## Vytvoření účtu

V realmu kramerius vytvořte nový objekt typu **Client**: 


<details>
<summary><strong>Keycloak 18 a starší</strong></summary>

![image](https://github.com/user-attachments/assets/63d5dbe3-8f68-477a-b0b8-d062573cd7e4)


![image](https://github.com/user-attachments/assets/8c50b39f-027e-475b-adfa-9fda9fa237b3)




Poté v nastavení klienta zvolit následující: 


![image](https://github.com/user-attachments/assets/26046896-919e-4add-a7a6-63dd812733e0)

![image](https://github.com/user-attachments/assets/ab5e654b-42a6-4ae3-985a-083865ae8747)

![image](https://github.com/user-attachments/assets/a72e93cd-44ea-4d9e-b002-5b8b6643469a)

a v sekci Advanced settings:

![image](https://github.com/user-attachments/assets/2f7a4883-4717-4e20-8991-58d675104b10)


Poté objekt uložit.   

</details>

<details>
<summary><strong>Keycloak 22 a mladší</strong></summary>

![image](https://github.com/user-attachments/assets/2b9bd33d-91d9-4511-8ec1-394da5cab64f)


![image](https://github.com/user-attachments/assets/35dbdbfe-2813-4d2d-ae53-d76a43ef5b74)

V nastavení zvolte volbu **Client authentication** a **Service roles** 

![image](https://github.com/user-attachments/assets/49b34001-2352-498e-b6c0-b1a321fe050b)

Na další straně vyplnít **Valid redirect URIs**
![image](https://github.com/user-attachments/assets/819d6fdc-2fa3-4f04-a1f4-a31eb90e9ea1)

Pak objekt typu klient uložit.  Měl by se objevit v tabulce všech klientů

![image](https://github.com/user-attachments/assets/8ebc1f78-c866-4215-ac29-5170fcdd2ffb)

Poté je možno ještě změnit expiraci vydávaného tokenu pro klienta.  Viz následujíc nastavení.  

Clients > service_account_a > Advanced > Advanced settings 
![image](https://github.com/user-attachments/assets/b54970ec-3a47-491b-817a-35593875a224)

![image](https://github.com/user-attachments/assets/6aed00dd-e045-4f07-8815-c10c3fd00b76)




</details>




## Nastavení role pro servisní účet

<details>
<summary><strong>Keycloak 18 a starší</strong></summary>

V objektu client otevřít záložku s rolema pro servisní účet a servisnímu účtu přiřadit odpovídající roli.  Viz následující screenshot: 

![image](https://github.com/user-attachments/assets/5d67670c-c59a-4794-9dc4-263f1326262d)
</details>

<details>
<summary><strong>Keycloak 22 a mladší</strong></summary>
V objektu client otevřít záložku s rolema pro servisní účet a servisnímu účtu přiřadit odpovídající roli. Viz následující screenshotz:

![image](https://github.com/user-attachments/assets/f065f2fc-e595-4248-a25a-524c9d64e878)

</details>


## Získání tokenu

Pro komunikaci přes API je důležité zná **clientId** a **secret**.   ClientId jsme vytvářeli spolu s objektem a v našem případě to je `service_account_a`, secret lze získat z následovně:

<details>
<summary><strong>Keycloak 18 a starší</strong></summary>

![image](https://github.com/user-attachments/assets/c90df2c9-569b-491c-a12f-73ee6803f921)

</details>


<details>
<summary><strong>Keycloak 22 a mladší</strong></summary>

![image](https://github.com/user-attachments/assets/2a0acdd3-02c2-464e-be54-eeafbc891a39)

![image](https://github.com/user-attachments/assets/3397c195-10d9-4d86-9f44-9823b49617f8)

</details>


## Test tokenu

Token je možno vyzkoušet přes OpenAPI následujícím endpointem: 

`https://<k7_instance>/search/openapi/exts/v7.0/index.html#/Z%C3%ADsk%C3%A1n%C3%AD%20servisn%C3%ADho%20tokenu/get_tokens__clientid_`


![image](https://github.com/user-attachments/assets/f5a3ada8-d4bf-4e39-907a-803772c18214)


a pak ve výsledku je vidět token: 

![image](https://github.com/user-attachments/assets/a183ad4c-be03-482d-92e5-5e8d2069c630)









 



