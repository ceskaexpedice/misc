[Index](../../../index) / [Návody](../../../guides/) / [Kurátor](../../curator/) / [Pracovní postupy](../../curator/workflows) 

# Zpracování nové dávky (Import + indexace)

Tento workflow popisuje kompletní zpracování nové digitální dávky od jejího importu až po indexaci v systému Kramerius.

Workflow se skládá ze dvou navazujících kroků:

1. Import dat
2. Indexace dat

Oba kroky jsou spouštěny v Admin klientu a běží asynchronně.

---

## Přehled procesu

```mermaid
flowchart LR
A[Výběr root dokumentu] --> B[Spuštění importu]
B --> C[Asynchronní import]
C --> D[Indexace]
D --> E[Dokument dostupný ve vyhledávání]
```

---

## 1. [Import](../tasks/start-import.md)

Import je vstupní krok, který načte data z importního adresáře definovaného v konfiguraci systému.

## 2. [Indexace](../tasks/start-indexing.md)

Po úspěšném importu následuje indexace dat do vyhledávacího systému.

---

## Jak poznám, že workflow proběhlo správně?

- importní proces skončí bez chyby
- indexace dokončena
- dokument je dostupný ve vyhledávání

---

## Co dělat při problému

- import selhal → viz Troubleshooting
- indexace neběží → viz Troubleshooting
- dokument se nezobrazuje → viz Troubleshooting

➡️ [Řešení problémů](../troubleshooting/index)

---

## Související dokumentace

- ➡️ TODO
- ➡️ 
