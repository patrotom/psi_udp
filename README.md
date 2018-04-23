# Domácí úloha č. 2 - UDP Klient #

## Situace ##

Na oběžné dráze planety Mars létá sonda, která sbírá informace a fotografie od robotů pracujících na povrchu planety (viz úloha č.1). Získané informace se poté přenášejí ze sondy do řídícího centra na Zemi.

## Úkoly ##

Vaším úkolem je:

1. načíst ze sondy poslední známou fotografii okolí, aby mohli vědci zjistit, v jakém terénu se roboti nachází
2. provést upload nového firmwaru do sondy

## Obecné schema komunikace ##

Sonda komunikuje pomocí protokolu UDP a přijímá data na portu 4000. Proces běžící v sondě budeme nazývat serverem a proces, který se sondou komunikuje, klientem.

### Formát paketu ###

| identifikátor 'spojení' | sekvenční číslo | číslo potvrzení | příznak	data | data   |
| ----------------------- | --------------- | --------------- | ------------ | ------ |
| 4B                      | 2B              | 2B              | 1B           | 0-255B |
