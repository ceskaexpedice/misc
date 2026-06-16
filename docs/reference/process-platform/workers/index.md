# Workers

Kramerius poskytuje několik worker aplikací postavených na Process Platform.

Worker je samostatná webová aplikace běžící v Tomcatu. Obsahuje sadu pluginů, které zpřístupňují procesy určené uživatelům nebo správcům systému.

Tato sekce popisuje workery dodávané s Krameriem a pluginy, které obsahují.

## Curator Worker

Worker určený pro kurátory a správce digitální knihovny.

Obsahuje pluginy související zejména s importem dat, indexací, správou metadat a dalšími kurátorskými činnostmi.

Viz [Curator Worker](curator).

## CDK Worker

Worker určený pro provoz prostředí České digitální knihovny (CDK).

Obsahuje pluginy používané pro migraci dat, synchronizaci a zpracování obsahu sdíleného mezi jednotlivými institucemi.

Viz [CDK Worker](cdk).

## Public Worker

Worker určený pro služby dostupné koncovým uživatelům.

Obsahuje pluginy umožňující provádět asynchronní operace, například generování PDF dokumentů a další exportní úlohy.

Viz [Public Worker](public).

## Související dokumentace

* [Processes](../processes) – kompletní přehled dostupných procesů a jejich payloadů
