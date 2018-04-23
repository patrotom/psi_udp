## Příklady komunikace ##

## Stažení fotografie z pohledu klienta ##

382 00000000 ** SEND ** seq=0 ack=0 flags=04 data(1): 01 
388 E6510001 ** RECV ** seq=0 ack=0 flags=04 data(1): 01 

*Klient obdržel SYN. Už ví číslo spojení (E6510001) a může začít přijímat data.*

558 E6510001 ** RECV ** seq=0 ack=0 flags=00 data(255): cc fa d9 74 7e fb 34 d6 … 18 50 0e 2f b5 73 f9 7b 
558 E6510001 ** SEND ** seq=0 ack=255 flags=00 data(0): –
558 E6510001 ** RECV ** seq=255 ack=0 flags=00 data(255): b6 6e 56 1e a8 f1 42 da … 2b a2 40 ab d8 1d 2f 28 
558 E6510001 ** SEND ** seq=0 ack=510 flags=00 data(0): –
558 E6510001 ** RECV ** seq=510 ack=0 flags=00 data(255): 72 bb 33 da 60 87 7b 84 … 0c d6 1d ac d6 78 a7 7e 
558 E6510001 ** SEND ** seq=0 ack=765 flags=00 data(0): –
559 E6510001 ** RECV ** seq=1530 ack=0 flags=00 data(255): f6 27 24 ee 47 e9 b9 7b … 09 73 0e 64 5e cd e2 bf 
559 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=1530
559 E6510001 ** SEND ** seq=0 ack=765 flags=00 data(0): –
559 E6510001 ** RECV ** seq=2040 ack=0 flags=00 data(255): 4c 75 4f b1 41 c3 22 99 … 68 84 76 a2 2e 78 be 0b 
559 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=2040
559 E6510001 ** SEND ** seq=0 ack=765 flags=00 data(0): –
658 E6510001 ** RECV ** seq=1020 ack=0 flags=00 data(255): 75 c2 c5 de f2 68 42 c5 … 4a 11 9b d1 f2 f4 7a 30 
658 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=1020
658 E6510001 ** SEND ** seq=0 ack=765 flags=00 data(0): –
660 E6510001 ** RECV ** seq=2295 ack=0 flags=00 data(255): 48 7d 49 82 de bc 88 e2 … ac cd 93 33 25 02 d1 10 
660 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=2295
660 E6510001 ** SEND ** seq=0 ack=765 flags=00 data(0): –
760 E6510001 ** RECV ** seq=765 ack=0 flags=00 data(255): 8c 8b 28 3f 6e d7 cb bd … cf 45 66 8e dc a1 43 26 
760 E6510001 ** SEND ** seq=0 ack=1275 flags=00 data(0): –
760 E6510001 ** RECV ** seq=1020 ack=0 flags=00 data(255): 75 c2 c5 de f2 68 42 c5 … 4a 11 9b d1 f2 f4 7a 30 
760 E6510001 ** SEND ** seq=0 ack=1275 flags=00 data(0): –
760 E6510001 ** RECV ** seq=1530 ack=0 flags=00 data(255): f6 27 24 ee 47 e9 b9 7b … 09 73 0e 64 5e cd e2 bf 
760 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=1530
760 E6510001 ** SEND ** seq=0 ack=1275 flags=00 data(0): –
761 E6510001 ** RECV ** seq=1785 ack=0 flags=00 data(255): a8 9f 78 66 73 d0 6e 7a … f7 31 43 d1 bc cf 5c 06 
761 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=1785
761 E6510001 ** SEND ** seq=0 ack=1275 flags=00 data(0): –
762 E6510001 ** RECV ** seq=2040 ack=0 flags=00 data(255): 4c 75 4f b1 41 c3 22 99 … 68 84 76 a2 2e 78 be 0b 
762 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=2040
762 E6510001 ** SEND ** seq=0 ack=1275 flags=00 data(0): –
762 E6510001 ** RECV ** seq=2550 ack=0 flags=00 data(255): 2f 01 73 20 9c ea 79 e5 … af f6 38 8d 05 5a a3 b1 
762 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=2550
762 E6510001 ** SEND ** seq=0 ack=1275 flags=00 data(0): –
762 E6510001 ** RECV ** seq=3060 ack=0 flags=00 data(255): 57 31 87 0c eb ce f7 40 … 95 ac 58 28 8c e3 cb 94 
762 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=3060
762 E6510001 ** SEND ** seq=0 ack=1275 flags=00 data(0): –
860 E6510001 ** RECV ** seq=1275 ack=0 flags=00 data(255): ae 32 69 87 75 b8 df 79 … cf 1d 33 4e 4c 81 cf 8d 
860 E6510001 ** SEND ** seq=0 ack=2805 flags=00 data(0): –
860 E6510001 ** RECV ** seq=1530 ack=0 flags=00 data(255): f6 27 24 ee 47 e9 b9 7b … 09 73 0e 64 5e cd e2 bf 
860 E6510001 ** SEND ** seq=0 ack=2805 flags=00 data(0): –
860 E6510001 ** RECV ** seq=3315 ack=0 flags=00 data(255): e3 f3 5e 78 7c 68 77 2d … 32 b9 f9 e9 46 66 5b fb 
860 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=3315
860 E6510001 ** SEND ** seq=0 ack=2805 flags=00 data(0): –
860 E6510001 ** RECV ** seq=3570 ack=0 flags=00 data(255): 5c 74 ad 1f 62 93 62 02 … 8d fb b7 4b 1f 9d d7 cb 
860 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=3570
860 E6510001 ** SEND ** seq=0 ack=2805 flags=00 data(0): –
861 E6510001 ** RECV ** seq=4590 ack=0 flags=00 data(255): c6 5b 0d a0 e7 14 e4 5d … 0e 6c bf 52 20 1a 45 8f 
861 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=4590
861 E6510001 ** SEND ** seq=0 ack=2805 flags=00 data(0): –
862 E6510001 ** RECV ** seq=2805 ack=0 flags=00 data(255): 2f 2c 48 3e ab 45 c0 5c … 8d f9 fa e9 22 1f 70 81 
862 E6510001 ** SEND ** seq=0 ack=3825 flags=00 data(0): –
961 E6510001 ** RECV ** seq=3315 ack=0 flags=00 data(255): e3 f3 5e 78 7c 68 77 2d … 32 b9 f9 e9 46 66 5b fb 
961 E6510001 ** SEND ** seq=0 ack=3825 flags=00 data(0): –
961 E6510001 ** RECV ** seq=3825 ack=0 flags=00 data(255): 4f 05 a1 04 2b d9 69 27 … 29 68 49 66 7d e2 b5 df 
961 E6510001 ** SEND ** seq=0 ack=4080 flags=00 data(0): –
961 E6510001 ** RECV ** seq=4335 ack=0 flags=00 data(255): 3f dc 60 01 8b 51 2b 26 … a5 32 0b d3 ed d8 81 0a 
962 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=4335
962 E6510001 ** SEND ** seq=0 ack=4080 flags=00 data(0): –
962 E6510001 ** RECV ** seq=4845 ack=0 flags=00 data(255): 28 bf 30 0e 9a 4a ed bd … 84 1d d1 d2 99 41 44 14 
962 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=4845
962 E6510001 ** SEND ** seq=0 ack=4080 flags=00 data(0): –
963 E6510001 ** RECV ** seq=5865 ack=0 flags=00 data(255): b3 bd 2c 7f 97 47 40 d8 … 43 0a e1 2d d1 76 1e 12 
963 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=5865
963 E6510001 ** SEND ** seq=0 ack=4080 flags=00 data(0): –
1063 E6510001 ** RECV ** seq=4080 ack=0 flags=00 data(255): 4c ff 17 48 1d 95 24 d2 … 68 aa b3 5a d8 c5 be 86 
1063 E6510001 ** SEND ** seq=0 ack=5100 flags=00 data(0): –
1063 E6510001 ** RECV ** seq=4335 ack=0 flags=00 data(255): 3f dc 60 01 8b 51 2b 26 … a5 32 0b d3 ed d8 81 0a 
1063 E6510001 ** SEND ** seq=0 ack=5100 flags=00 data(0): –
1063 E6510001 ** RECV ** seq=4845 ack=0 flags=00 data(255): 28 bf 30 0e 9a 4a ed bd … 84 1d d1 d2 99 41 44 14 
1063 E6510001 ** SEND ** seq=0 ack=5100 flags=00 data(0): –
1064 E6510001 ** RECV ** seq=5100 ack=0 flags=00 data(255): 91 6e e8 a7 20 af 94 63 … a3 8c bd 2c f6 5b ac 42 
1064 E6510001 ** SEND ** seq=0 ack=5355 flags=00 data(0): –
1064 E6510001 ** RECV ** seq=5355 ack=0 flags=00 data(255): 40 93 d6 15 b6 89 78 0a … 21 db 32 e0 7d 76 c9 2d 
1064 E6510001 ** SEND ** seq=0 ack=5610 flags=00 data(0): –
1064 E6510001 ** RECV ** seq=5610 ack=0 flags=00 data(255): 7a b5 fb b6 f3 7e ad 04 … 5a c6 20 ff 67 be 1c 88 
1064 E6510001 ** SEND ** seq=0 ack=6120 flags=00 data(0): –
1064 E6510001 ** RECV ** seq=5865 ack=0 flags=00 data(255): b3 bd 2c 7f 97 47 40 d8 … 43 0a e1 2d d1 76 1e 12 
1065 E6510001 ** SEND ** seq=0 ack=6120 flags=00 data(0): –
1067 E6510001 ** RECV ** seq=6630 ack=0 flags=00 data(255): 6f 76 67 26 71 00 85 df … 28 1d af 4e 9f 5e 6c 6a 
1067 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=6630
1067 E6510001 ** SEND ** seq=0 ack=6120 flags=00 data(0): –
1067 E6510001 ** RECV ** seq=7140 ack=0 flags=00 data(255): 04 d2 66 e7 bc 66 aa 08 … 85 f8 d7 9e 54 6b cf 08 
1067 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=7140
1067 E6510001 ** SEND ** seq=0 ack=6120 flags=00 data(0): –
1068 E6510001 ** RECV ** seq=7650 ack=0 flags=00 data(255): bc 77 ae c5 d4 e1 3b 25 … ee 03 72 be e0 1c 91 4a 
1068 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=7650
1068 E6510001 ** SEND ** seq=0 ack=6120 flags=00 data(0): –
1069 E6510001 ** RECV ** seq=7905 ack=0 flags=00 data(255): 2a d7 da 30 5d fd a9 20 … fb 47 53 7b 29 dd 4e 61 
1069 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=7905
1069 E6510001 ** SEND ** seq=0 ack=6120 flags=00 data(0): –
1167 E6510001 ** RECV ** seq=6120 ack=0 flags=00 data(255): 1f 02 2e 73 f9 f3 c3 e6 … 06 28 ca 8a a1 b5 a7 96 
1167 E6510001 ** SEND ** seq=0 ack=6375 flags=00 data(0): –
1167 E6510001 ** RECV ** seq=8160 ack=0 flags=00 data(255): 5b d7 ba ce b6 31 6e 62 … c8 6a 95 3d b7 15 1e 50 
1167 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=8160
1167 E6510001 ** SEND ** seq=0 ack=6375 flags=00 data(0): –
1169 E6510001 ** RECV ** seq=7905 ack=0 flags=00 data(255): 2a d7 da 30 5d fd a9 20 … fb 47 53 7b 29 dd 4e 61 
1169 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=7905
1169 E6510001 ** SEND ** seq=0 ack=6375 flags=00 data(0): –
1267 E6510001 ** RECV ** seq=6375 ack=0 flags=00 data(255): 3e f9 eb 64 c4 66 1b 47 … d6 44 5b ad 00 74 3a 70 
1267 E6510001 ** SEND ** seq=0 ack=6885 flags=00 data(0): –
1267 E6510001 ** RECV ** seq=6630 ack=0 flags=00 data(255): 6f 76 67 26 71 00 85 df … 28 1d af 4e 9f 5e 6c 6a 
1267 E6510001 ** SEND ** seq=0 ack=6885 flags=00 data(0): –
1267 E6510001 ** RECV ** seq=6885 ack=0 flags=00 data(255): 3c 42 6c dd 04 fd 2e c8 … 9f 3d 2e bc f7 c0 72 77 
1267 E6510001 ** SEND ** seq=0 ack=7395 flags=00 data(0): –
1268 E6510001 ** RECV ** seq=7140 ack=0 flags=00 data(255): 04 d2 66 e7 bc 66 aa 08 … 85 f8 d7 9e 54 6b cf 08 
1268 E6510001 ** SEND ** seq=0 ack=7395 flags=00 data(0): –
1268 E6510001 ** RECV ** seq=7395 ack=0 flags=00 data(255): a2 5f b3 83 d9 7e e0 53 … 0e 20 96 84 dd d2 cb e0 
1268 E6510001 ** SEND ** seq=0 ack=8415 flags=00 data(0): –
1268 E6510001 ** RECV ** seq=8670 ack=0 flags=00 data(255): 75 15 8a ac 98 6a 29 ec … 18 db 61 15 94 56 cf 98 
1268 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=8670
1268 E6510001 ** SEND ** seq=0 ack=8415 flags=00 data(0): –
1269 E6510001 ** RECV ** seq=9180 ack=0 flags=00 data(255): e4 c1 93 94 4f b1 26 d0 … b5 2a f1 63 f9 ef 57 89 
1269 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=9180
1269 E6510001 ** SEND ** seq=0 ack=8415 flags=00 data(0): –
1270 E6510001 ** RECV ** seq=9435 ack=0 flags=00 data(255): 40 97 b5 20 6e 50 8f 04 … 74 68 e1 2d ca e0 2b 52 
1270 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=9435
1270 E6510001 ** SEND ** seq=0 ack=8415 flags=00 data(0): –
1270 E6510001 ** RECV ** seq=9690 ack=0 flags=00 data(255): 25 30 37 3d af af 89 fd … ed c9 ce d0 56 08 51 e5 
1270 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=9690
1270 E6510001 ** SEND ** seq=0 ack=8415 flags=00 data(0): –
1270 E6510001 ** RECV ** seq=9945 ack=0 flags=00 data(255): 72 c5 23 84 a3 20 74 00 … b8 df e6 e0 ba 7a 2d ad 
1270 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=9945
1270 E6510001 ** SEND ** seq=0 ack=8415 flags=00 data(0): –
1270 E6510001 ** RECV ** seq=10200 ack=0 flags=00 data(255): 85 7c 0a ea ec 0f 75 f6 … a4 90 b4 16 90 1c c8 ec 
1270 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=10200
1270 E6510001 ** SEND ** seq=0 ack=8415 flags=00 data(0): –
1370 E6510001 ** RECV ** seq=8415 ack=0 flags=00 data(255): 7a 7c 99 0f e4 a9 7b 78 … ea cb dc 4a d8 f9 47 ed 
1370 E6510001 ** SEND ** seq=0 ack=8925 flags=00 data(0): –
1370 E6510001 ** RECV ** seq=9435 ack=0 flags=00 data(255): 40 97 b5 20 6e 50 8f 04 … 74 68 e1 2d ca e0 2b 52 
1370 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=9435
1370 E6510001 ** SEND ** seq=0 ack=8925 flags=00 data(0): –
1370 E6510001 ** RECV ** seq=9690 ack=0 flags=00 data(255): 25 30 37 3d af af 89 fd … ed c9 ce d0 56 08 51 e5 
1370 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=9690
1370 E6510001 ** SEND ** seq=0 ack=8925 flags=00 data(0): –
1371 E6510001 ** RECV ** seq=9945 ack=0 flags=00 data(255): 72 c5 23 84 a3 20 74 00 … b8 df e6 e0 ba 7a 2d ad 
1371 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=9945
1371 E6510001 ** SEND ** seq=0 ack=8925 flags=00 data(0): –
1371 E6510001 ** RECV ** seq=10200 ack=0 flags=00 data(255): 85 7c 0a ea ec 0f 75 f6 … a4 90 b4 16 90 1c c8 ec 
1371 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=10200
1371 E6510001 ** SEND ** seq=0 ack=8925 flags=00 data(0): –
1470 E6510001 ** RECV ** seq=10200 ack=0 flags=00 data(255): 85 7c 0a ea ec 0f 75 f6 … a4 90 b4 16 90 1c c8 ec 
1470 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=10200
1470 E6510001 ** SEND ** seq=0 ack=8925 flags=00 data(0): –
1471 E6510001 ** RECV ** seq=10455 ack=0 flags=00 data(255): 81 52 3e 0c 71 e4 98 f0 … 79 48 7d bc bf 29 de 74 
1471 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=10455
1471 E6510001 ** SEND ** seq=0 ack=8925 flags=00 data(0): –
1571 E6510001 ** RECV ** seq=8925 ack=0 flags=00 data(255): f1 bc 72 f7 3a 34 f3 a8 … ed a7 cb 29 6c 60 9e 5d 
1571 E6510001 ** SEND ** seq=0 ack=10710 flags=00 data(0): –
1571 E6510001 ** RECV ** seq=9180 ack=0 flags=00 data(255): e4 c1 93 94 4f b1 26 d0 … b5 2a f1 63 f9 ef 57 89 
1571 E6510001 ** SEND ** seq=0 ack=10710 flags=00 data(0): –
1571 E6510001 ** RECV ** seq=9690 ack=0 flags=00 data(255): 25 30 37 3d af af 89 fd … ed c9 ce d0 56 08 51 e5 
1572 E6510001 ** SEND ** seq=0 ack=10710 flags=00 data(0): –
1572 E6510001 ** RECV ** seq=10455 ack=0 flags=00 data(255): 81 52 3e 0c 71 e4 98 f0 … 79 48 7d bc bf 29 de 74 
1572 E6510001 ** SEND ** seq=0 ack=10710 flags=00 data(0): –
1572 E6510001 ** RECV ** seq=10965 ack=0 flags=00 data(255): a0 c7 13 fb b4 44 e7 fe … 81 a1 a5 b2 f9 b8 68 35 
1572 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=10965
1572 E6510001 ** SEND ** seq=0 ack=10710 flags=00 data(0): –
1573 E6510001 ** RECV ** seq=11985 ack=0 flags=00 data(255): 0e 09 57 37 36 d4 be 77 … dd 03 b5 c5 2e a9 85 95 
1573 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=11985
1573 E6510001 ** SEND ** seq=0 ack=10710 flags=00 data(0): –
1573 E6510001 ** RECV ** seq=12240 ack=0 flags=00 data(255): 72 58 8c c9 e1 e5 74 67 … 5f 09 1f c6 85 f0 4d 69 
1573 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=12240
1573 E6510001 ** SEND ** seq=0 ack=10710 flags=00 data(0): –
1573 E6510001 ** RECV ** seq=12495 ack=0 flags=00 data(255): 23 43 90 16 9d e7 31 d1 … 00 d7 ad a0 9f 13 0c 18 
1574 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=12495
1574 E6510001 ** SEND ** seq=0 ack=10710 flags=00 data(0): –
1672 E6510001 ** RECV ** seq=10710 ack=0 flags=00 data(255): f9 1a ef d1 f0 f1 c4 e5 … e0 e5 8e 02 39 6b e0 3a 
1672 E6510001 ** SEND ** seq=0 ack=11220 flags=00 data(0): –
1672 E6510001 ** RECV ** seq=11475 ack=0 flags=00 data(255): 46 5d c2 f9 06 41 f9 22 … 96 46 62 47 89 ae 22 aa 
1672 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=11475
1672 E6510001 ** SEND ** seq=0 ack=11220 flags=00 data(0): –
1672 E6510001 ** RECV ** seq=11730 ack=0 flags=00 data(255): 9e e8 d8 bf f3 49 55 8b … 50 b5 a2 0d b0 f9 8f 17 
1672 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=11730
1672 E6510001 ** SEND ** seq=0 ack=11220 flags=00 data(0): –
1773 E6510001 ** RECV ** seq=11220 ack=0 flags=00 data(255): 7e 04 26 f8 2f e0 5f dd … 97 cc 7a 24 34 f3 7c 63 
1773 E6510001 ** SEND ** seq=0 ack=12750 flags=00 data(0): –
1773 E6510001 ** RECV ** seq=11475 ack=0 flags=00 data(255): 46 5d c2 f9 06 41 f9 22 … 96 46 62 47 89 ae 22 aa 
1773 E6510001 ** SEND ** seq=0 ack=12750 flags=00 data(0): –
1773 E6510001 ** RECV ** seq=11730 ack=0 flags=00 data(255): 9e e8 d8 bf f3 49 55 8b … 50 b5 a2 0d b0 f9 8f 17 
1774 E6510001 ** SEND ** seq=0 ack=12750 flags=00 data(0): –
1774 E6510001 ** RECV ** seq=12240 ack=0 flags=00 data(255): 72 58 8c c9 e1 e5 74 67 … 5f 09 1f c6 85 f0 4d 69 
1774 E6510001 ** SEND ** seq=0 ack=12750 flags=00 data(0): –
1774 E6510001 ** RECV ** seq=12495 ack=0 flags=00 data(255): 23 43 90 16 9d e7 31 d1 … 00 d7 ad a0 9f 13 0c 18 
1774 E6510001 ** SEND ** seq=0 ack=12750 flags=00 data(0): –
1774 E6510001 ** RECV ** seq=13515 ack=0 flags=00 data(255): 33 a8 da 2f 9e cf fb 17 … b3 75 b7 bf c2 62 90 af 
1774 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=13515
1774 E6510001 ** SEND ** seq=0 ack=12750 flags=00 data(0): –
1775 E6510001 ** RECV ** seq=14280 ack=0 flags=00 data(255): 3c 85 a1 dc 2a 3d 5a c7 … 2f f8 47 2f 42 60 e5 d2 
1775 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=14280
1775 E6510001 ** SEND ** seq=0 ack=12750 flags=00 data(0): –
1875 E6510001 ** RECV ** seq=12750 ack=0 flags=00 data(255): d9 af bc 85 df 1f 1e e2 … c2 dd 52 76 bc 6c c8 b5 
1875 E6510001 ** SEND ** seq=0 ack=13005 flags=00 data(0): –
1875 E6510001 ** RECV ** seq=13260 ack=0 flags=00 data(255): 53 94 cf bf 00 1c 02 fd … 43 bb 26 d7 4d 1e 31 75 
1875 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=13260
1875 E6510001 ** SEND ** seq=0 ack=13005 flags=00 data(0): –
1876 E6510001 ** RECV ** seq=13770 ack=0 flags=00 data(255): bc 81 b2 4f 79 83 6f e8 … fd 93 19 df 07 44 34 18 
1876 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=13770
1876 E6510001 ** SEND ** seq=0 ack=13005 flags=00 data(0): –
1876 E6510001 ** RECV ** seq=14025 ack=0 flags=00 data(255): f7 61 f6 44 a2 80 da d2 … a0 71 5e 98 b1 91 0f 85 
1876 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=14025
1876 E6510001 ** SEND ** seq=0 ack=13005 flags=00 data(0): –
1877 E6510001 ** RECV ** seq=14790 ack=0 flags=00 data(255): e5 39 2d c1 36 8a f9 c8 … 1b c9 15 2a 4a b3 ce da 
1877 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=14790
1877 E6510001 ** SEND ** seq=0 ack=13005 flags=00 data(0): –
1975 E6510001 ** RECV ** seq=13515 ack=0 flags=00 data(255): 33 a8 da 2f 9e cf fb 17 … b3 75 b7 bf c2 62 90 af 
1975 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=13515
1975 E6510001 ** SEND ** seq=0 ack=13005 flags=00 data(0): –
1976 E6510001 ** RECV ** seq=14025 ack=0 flags=00 data(255): f7 61 f6 44 a2 80 da d2 … a0 71 5e 98 b1 91 0f 85 
1976 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=14025
1976 E6510001 ** SEND ** seq=0 ack=13005 flags=00 data(0): –
2076 E6510001 ** RECV ** seq=13005 ack=0 flags=00 data(255): ca 42 d8 5d 9f c6 0e 70 … 64 85 be 7f 16 2f aa eb 
2076 E6510001 ** SEND ** seq=0 ack=14535 flags=00 data(0): –
2076 E6510001 ** RECV ** seq=13260 ack=0 flags=00 data(255): 53 94 cf bf 00 1c 02 fd … 43 bb 26 d7 4d 1e 31 75 
2076 E6510001 ** SEND ** seq=0 ack=14535 flags=00 data(0): –
2076 E6510001 ** RECV ** seq=13515 ack=0 flags=00 data(255): 33 a8 da 2f 9e cf fb 17 … b3 75 b7 bf c2 62 90 af 
2077 E6510001 ** SEND ** seq=0 ack=14535 flags=00 data(0): –
2077 E6510001 ** RECV ** seq=14025 ack=0 flags=00 data(255): f7 61 f6 44 a2 80 da d2 … a0 71 5e 98 b1 91 0f 85 
2077 E6510001 ** SEND ** seq=0 ack=14535 flags=00 data(0): –
2077 E6510001 ** RECV ** seq=14790 ack=0 flags=00 data(255): e5 39 2d c1 36 8a f9 c8 … 1b c9 15 2a 4a b3 ce da 
2077 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=14790
2077 E6510001 ** SEND ** seq=0 ack=14535 flags=00 data(0): –
2078 E6510001 ** RECV ** seq=15810 ack=0 flags=00 data(255): e0 16 ed 95 88 30 34 41 … 49 fe b5 e9 8b 14 89 24 
2078 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=15810
2078 E6510001 ** SEND ** seq=0 ack=14535 flags=00 data(0): –
2078 E6510001 ** RECV ** seq=16065 ack=0 flags=00 data(255): 91 bd b5 e4 f5 9e 4b 49 … 2e b2 b6 7b 47 38 07 07 
2078 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=16065
2078 E6510001 ** SEND ** seq=0 ack=14535 flags=00 data(0): –
2078 E6510001 ** RECV ** seq=16320 ack=0 flags=00 data(255): c7 f8 b1 bb a8 81 5f d5 … d4 30 0d 2c 3c ed 27 ab 
2078 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=16320
2079 E6510001 ** SEND ** seq=0 ack=14535 flags=00 data(0): –
2178 E6510001 ** RECV ** seq=14535 ack=0 flags=00 data(255): dc 6a 90 9d 16 98 27 cf … 9c ae a5 45 97 f7 bc f1 
2178 E6510001 ** SEND ** seq=0 ack=15045 flags=00 data(0): –
2178 E6510001 ** RECV ** seq=15300 ack=0 flags=00 data(255): a7 6a a1 d0 da 2f af 42 … 23 7c 33 bb 57 69 10 b4 
2179 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=15300
2179 E6510001 ** SEND ** seq=0 ack=15045 flags=00 data(0): –
2179 E6510001 ** RECV ** seq=15555 ack=0 flags=00 data(255): d9 58 d5 da 92 51 cc db … 55 9b dd 7e ea 49 f6 8e 
2179 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=15555
2179 E6510001 ** SEND ** seq=0 ack=15045 flags=00 data(0): –
2179 E6510001 ** RECV ** seq=15810 ack=0 flags=00 data(255): e0 16 ed 95 88 30 34 41 … 49 fe b5 e9 8b 14 89 24 
2179 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=15810
2179 E6510001 ** SEND ** seq=0 ack=15045 flags=00 data(0): –
2179 E6510001 ** RECV ** seq=16065 ack=0 flags=00 data(255): 91 bd b5 e4 f5 9e 4b 49 … 2e b2 b6 7b 47 38 07 07 
2179 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=16065
2180 E6510001 ** SEND ** seq=0 ack=15045 flags=00 data(0): –
2180 E6510001 ** RECV ** seq=16575 ack=0 flags=00 data(255): 2a 29 d0 be c2 dc ab 83 … 77 1d 49 f7 e2 71 81 e1 
2181 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=16575
2181 E6510001 ** SEND ** seq=0 ack=15045 flags=00 data(0): –
2181 E6510001 ** RECV ** seq=16830 ack=0 flags=00 data(255): 93 7c 05 b6 2d 9b 41 8f … ac c7 13 49 f2 60 13 1d 
2181 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=16830
2181 E6510001 ** SEND ** seq=0 ack=15045 flags=00 data(0): –
2278 E6510001 ** RECV ** seq=15045 ack=0 flags=00 data(255): 9c d4 55 a4 27 da 67 9e … e4 15 76 9b 3a 45 93 db 
2278 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2278 E6510001 ** RECV ** seq=15555 ack=0 flags=00 data(255): d9 58 d5 da 92 51 cc db … 55 9b dd 7e ea 49 f6 8e 
2278 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2279 E6510001 ** RECV ** seq=16320 ack=0 flags=00 data(255): c7 f8 b1 bb a8 81 5f d5 … d4 30 0d 2c 3c ed 27 ab 
2279 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2279 E6510001 ** RECV ** seq=17595 ack=0 flags=00 data(255): ab b1 57 67 66 d4 8a d5 … 12 81 a1 ea a6 d5 17 f4 
2280 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=17595
2280 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2280 E6510001 ** RECV ** seq=17850 ack=0 flags=00 data(255): 11 6c a8 03 13 9a c5 05 … 5f 71 51 e8 0d 55 32 e1 
2280 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=17850
2280 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2280 E6510001 ** RECV ** seq=18105 ack=0 flags=00 data(255): 9d a3 a1 60 69 a7 52 88 … 5f b9 ac 96 cd 3d 69 d9 
2280 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=18105
2280 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2280 E6510001 ** RECV ** seq=18360 ack=0 flags=00 data(255): 02 f7 e3 6d 0d ae 5f 9e … 2b 0f c4 f3 13 c5 db 59 
2281 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=18360
2281 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2281 E6510001 ** RECV ** seq=18615 ack=0 flags=00 data(255): 3f 24 9d ad 1b 55 12 69 … 95 c7 f0 4e 67 45 db 11 
2281 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=18615
2281 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2281 E6510001 ** RECV ** seq=18870 ack=0 flags=00 data(255): c6 57 97 40 c9 9b f1 18 … 53 d2 29 6b b7 a2 b6 cc 
2281 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=18870
2281 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2381 E6510001 ** RECV ** seq=17340 ack=0 flags=00 data(255): 76 18 24 16 ab 21 f6 31 … 70 10 a9 6c 50 b7 bf fe 
2381 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=17340
2381 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2381 E6510001 ** RECV ** seq=18105 ack=0 flags=00 data(255): 9d a3 a1 60 69 a7 52 88 … 5f b9 ac 96 cd 3d 69 d9 
2382 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=18105
2382 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2481 E6510001 ** RECV ** seq=17340 ack=0 flags=00 data(255): 76 18 24 16 ab 21 f6 31 … 70 10 a9 6c 50 b7 bf fe 
2481 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=17340
2481 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2481 E6510001 ** RECV ** seq=18105 ack=0 flags=00 data(255): 9d a3 a1 60 69 a7 52 88 … 5f b9 ac 96 cd 3d 69 d9 
2481 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=18105
2481 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2481 E6510001 ** RECV ** seq=18870 ack=0 flags=00 data(255): c6 57 97 40 c9 9b f1 18 … 53 d2 29 6b b7 a2 b6 cc 
2481 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=18870
2481 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2582 E6510001 ** RECV ** seq=17595 ack=0 flags=00 data(255): ab b1 57 67 66 d4 8a d5 … 12 81 a1 ea a6 d5 17 f4 
2582 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=17595
2582 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2582 E6510001 ** RECV ** seq=18105 ack=0 flags=00 data(255): 9d a3 a1 60 69 a7 52 88 … 5f b9 ac 96 cd 3d 69 d9 
2583 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=18105
2583 E6510001 ** SEND ** seq=0 ack=17085 flags=00 data(0): –
2683 E6510001 ** RECV ** seq=17085 ack=0 flags=00 data(255): 1d 7c 6f b8 f8 cd 0d c4 … 77 60 0d 82 b5 c4 42 15 
2683 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2683 E6510001 ** RECV ** seq=17850 ack=0 flags=00 data(255): 11 6c a8 03 13 9a c5 05 … 5f 71 51 e8 0d 55 32 e1 
2683 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2684 E6510001 ** RECV ** seq=18360 ack=0 flags=00 data(255): 02 f7 e3 6d 0d ae 5f 9e … 2b 0f c4 f3 13 c5 db 59 
2684 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2684 E6510001 ** RECV ** seq=18870 ack=0 flags=00 data(255): c6 57 97 40 c9 9b f1 18 … 53 d2 29 6b b7 a2 b6 cc 
2684 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2684 E6510001 ** RECV ** seq=19635 ack=0 flags=00 data(255): 43 1e 8e 09 b6 a2 d0 be … 0d 44 fb 22 27 96 11 db 
2685 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=19635
2685 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2685 E6510001 ** RECV ** seq=20910 ack=0 flags=00 data(255): bd f2 1b 2b f6 69 4a ff … 08 41 12 16 bc 2a 97 ad 
2685 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=20910
2685 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2785 E6510001 ** RECV ** seq=19635 ack=0 flags=00 data(255): 43 1e 8e 09 b6 a2 d0 be … 0d 44 fb 22 27 96 11 db 
2785 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=19635
2785 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2786 E6510001 ** RECV ** seq=20145 ack=0 flags=00 data(255): 33 78 de ff f3 f6 5c 52 … c6 3f fe 33 90 bd 6b be 
2786 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=20145
2786 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2786 E6510001 ** RECV ** seq=20400 ack=0 flags=00 data(255): 4f 28 59 12 74 f4 8c 86 … 49 55 ff f8 1a cf 47 59 
2786 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=20400
2786 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2786 E6510001 ** RECV ** seq=20655 ack=0 flags=00 data(255): 16 62 f8 ba a9 28 c3 df … 05 86 7c e7 7c 9d 41 c6 
2786 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=20655
2786 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2886 E6510001 ** RECV ** seq=19380 ack=0 flags=00 data(255): d4 22 c5 7f 51 13 2d 17 … 53 8b ad 8d 7b eb 0d 0b 
2886 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=19380
2886 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2886 E6510001 ** RECV ** seq=19890 ack=0 flags=00 data(255): 27 78 b6 0c 35 ff 32 f4 … 0d 62 af 45 b5 c8 91 31 
2886 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=19890
2886 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2886 E6510001 ** RECV ** seq=20145 ack=0 flags=00 data(255): 33 78 de ff f3 f6 5c 52 … c6 3f fe 33 90 bd 6b be 
2886 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=20145
2886 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2886 E6510001 ** RECV ** seq=20400 ack=0 flags=00 data(255): 4f 28 59 12 74 f4 8c 86 … 49 55 ff f8 1a cf 47 59 
2886 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=20400
2886 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2886 E6510001 ** RECV ** seq=20655 ack=0 flags=00 data(255): 16 62 f8 ba a9 28 c3 df … 05 86 7c e7 7c 9d 41 c6 
2886 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=20655
2887 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2887 E6510001 ** RECV ** seq=20910 ack=0 flags=00 data(255): bd f2 1b 2b f6 69 4a ff … 08 41 12 16 bc 2a 97 ad 
2887 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=20910
2887 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2987 E6510001 ** RECV ** seq=19635 ack=0 flags=00 data(255): 43 1e 8e 09 b6 a2 d0 be … 0d 44 fb 22 27 96 11 db 
2987 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=19635
2987 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2987 E6510001 ** RECV ** seq=20145 ack=0 flags=00 data(255): 33 78 de ff f3 f6 5c 52 … c6 3f fe 33 90 bd 6b be 
2987 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=20145
2988 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –
2988 E6510001 ** RECV ** seq=20400 ack=0 flags=00 data(255): 4f 28 59 12 74 f4 8c 86 … 49 55 ff f8 1a cf 47 59 
2988 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=20400
2988 E6510001 ** SEND ** seq=0 ack=19125 flags=00 data(0): –

:

10482 E6510001 ** SEND ** seq=0 ack=65280 flags=00 data(0): –
10482 E6510001 ** RECV ** seq=65280 ack=0 flags=00 data(255): 0b 8d f7 85 9f 06 ce e3 … 30 ca c7 a3 2b ab 8e c2 
10482 E6510001 ** SEND ** seq=0 ack=764 flags=00 data(0): –

*Všimněte si, že sekvenční číslo v přijímaném proudu dat přeteklo - na komunikaci to nemá vliv.*

10482 E6510001 ** RECV ** seq=65535 ack=0 flags=00 data(255): ad 47 51 3b d5 c4 33 75 … 63 6a 3f 9b ea 2b 7f a4 
10482 E6510001 ** SEND ** seq=0 ack=764 flags=00 data(0): –
10482 E6510001 ** RECV ** seq=254 ack=0 flags=00 data(255): ea 3e 1f 37 68 85 07 51 … 72 58 4e cf df 43 0a f8 
10482 E6510001 ** SEND ** seq=0 ack=764 flags=00 data(0): –
10483 E6510001 ** RECV ** seq=764 ack=0 flags=00 data(255): 4d f8 af da 10 a9 d5 02 … 1f 93 af 98 86 7a 63 43 
10483 E6510001 ** SEND ** seq=0 ack=1019 flags=00 data(0): –
10483 E6510001 ** RECV ** seq=1274 ack=0 flags=00 data(255): 6e ed 76 c5 02 a3 46 4b … e5 f5 d7 61 32 78 46 27 
10483 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=1274
10483 E6510001 ** SEND ** seq=0 ack=1019 flags=00 data(0): –
10483 E6510001 ** RECV ** seq=1529 ack=0 flags=00 data(255): b8 df eb ff f2 37 17 82 … 4a a3 fd 1d 60 1e 7f 27 
10483 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=1529
10483 E6510001 ** SEND ** seq=0 ack=1019 flags=00 data(0): –
10484 E6510001 ** RECV ** seq=2039 ack=0 flags=00 data(255): 94 f5 d9 19 4b ab 18 4b … 26 ac a2 2a db 9d 37 d6 
10484 E6510001 Tento paket se mi nehodi do rady, ale budu si ho pamatovat: seq=2039
10484 E6510001 ** SEND ** seq=0 ack=1019 flags=00 data(0): –

:

29732 E6510001 ** RECV ** seq=7392 ack=0 flags=00 data(255): 38 bd b6 a7 cf d5 df ce … 19 9f 56 20 b2 d3 9f 1f 
29732 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=7392
29732 E6510001 ** SEND ** seq=0 ack=6627 flags=00 data(0): –
29732 E6510001 ** RECV ** seq=7902 ack=0 flags=00 data(255): 61 8a d3 df 34 84 a1 8e … ce 7c ec 4a 4e 3a 65 f1 
29732 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=7902
29732 E6510001 ** SEND ** seq=0 ack=6627 flags=00 data(0): –
29732 E6510001 ** RECV ** seq=8157 ack=0 flags=00 data(35): c2 2d 01 56 3e ea b3 35 … f2 42 b0 f7 84 2c c3 69 
29732 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=8157
29732 E6510001 ** SEND ** seq=0 ack=6627 flags=00 data(0): –
29832 E6510001 ** RECV ** seq=6882 ack=0 flags=00 data(255): d3 e7 a0 f1 40 e8 ce 63 … 44 7a 41 ec 35 74 37 80 
29832 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=6882
29832 E6510001 ** SEND ** seq=0 ack=6627 flags=00 data(0): –
29832 E6510001 ** RECV ** seq=7137 ack=0 flags=00 data(255): 37 c4 d6 8a 9b d4 13 66 … 7b 52 95 78 26 7f cb 68 
29832 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=7137
29832 E6510001 ** SEND ** seq=0 ack=6627 flags=00 data(0): –
29832 E6510001 ** RECV ** seq=7392 ack=0 flags=00 data(255): 38 bd b6 a7 cf d5 df ce … 19 9f 56 20 b2 d3 9f 1f 
29832 E6510001 Tento paket se mi nehodi do rady, navic jsem ho jiz jednou prijal: seq=7392
29832 E6510001 ** SEND ** seq=0 ack=6627 flags=00 data(0): –
29933 E6510001 ** RECV ** seq=6627 ack=0 flags=00 data(255): 08 77 76 7d ed be 75 6d … 5d d4 3d c2 19 0a eb 11 
29933 E6510001 ** SEND ** seq=0 ack=8192 flags=00 data(0): –
29933 E6510001 ** RECV ** seq=6882 ack=0 flags=00 data(255): d3 e7 a0 f1 40 e8 ce 63 … 44 7a 41 ec 35 74 37 80 
29933 E6510001 ** SEND ** seq=0 ack=8192 flags=00 data(0): –
29934 E6510001 ** RECV ** seq=7137 ack=0 flags=00 data(255): 37 c4 d6 8a 9b d4 13 66 … 7b 52 95 78 26 7f cb 68 
29934 E6510001 ** SEND ** seq=0 ack=8192 flags=00 data(0): –
29934 E6510001 ** RECV ** seq=7392 ack=0 flags=00 data(255): 38 bd b6 a7 cf d5 df ce … 19 9f 56 20 b2 d3 9f 1f 
29934 E6510001 ** SEND ** seq=0 ack=8192 flags=00 data(0): –
29934 E6510001 ** RECV ** seq=7902 ack=0 flags=00 data(255): 61 8a d3 df 34 84 a1 8e … ce 7c ec 4a 4e 3a 65 f1 
29934 E6510001 ** SEND ** seq=0 ack=8192 flags=00 data(0): –
29934 E6510001 ** RECV ** seq=8192 ack=0 flags=02 data(0): –
29934 E6510001 ** SEND ** seq=0 ack=8192 flags=02 data(0): –
29938 E6510001 Spojeni bylo uzavreno. Bylo preneseno celkem 204800 bytu.