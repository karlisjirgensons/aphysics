# -*- coding: utf-8 -*-
"""2. klase, 1. stunda: «Kas šim priekšmetam ir īpašs?»

Otrā gada pirmā stunda sāk ar novērošanu: priekšmetam ir daudz īpašību, bet
tikai dažas ir būtiskas - bez tām priekšmets vairs nav tas pats. Šī
atšķirība ir pamatā visai grupēšanai, ko mācās 2.1. tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kas šim priekšmetam ir īpašs?"

MERKIS = ("Šodien nosauksim priekšmeta īpašības un atšķirsim būtiskās no "
          "nebūtiskajām.")

_BUTISKA = ["būtiska", "nav būtiska"]

SATURS = [
    Sakums("Kā atrast savu somu starp 25 līdzīgām somām?",
           zimejums=bildes([[("soma", 5)]]),
           paraksts="Somas ir līdzīgas, bet katrai ir kas savs.",
           fakti=["Krāsa, izmērs, forma un materiāls ir īpašības.",
                  "Pēc īpašībām priekšmetu var atrast un aprakstīt.",
                  "Matemātika sākas ar vērīgu skatīšanos."]),

    Doma("Īpašība - tas, ko var pateikt par priekšmetu",
         "Būtiska ir tā īpašība, bez kuras priekšmets vairs nav tas pats.",
         soli=[
             "Apskati formu, krāsu, izmēru un materiālu.",
             "Padomā, kam priekšmetu lieto.",
             "Pajautā: ja šī īpašība mainās, vai tas vēl ir tas pats?",
             "Ja jā - īpašība nav būtiska.",
         ],
         pieze="Ābols var būt sarkans vai zaļš - krāsa nav būtiska. Bet ābols "
               "vienmēr ir auglis, kas aug kokā."),

    Varianti("Būtiska vai nav būtiska?", [
        {"jaut": "Krēslam ir sēdeklis.", "opcijas": _BUTISKA,
         "jaukt": False, "pareizi": 0,
         "padoms": "Bez sēdekļa uz krēsla nevar apsēsties."},
        {"jaut": "Krēsls ir zils.", "opcijas": _BUTISKA, "jaukt": False,
         "pareizi": 1, "padoms": "Arī sarkans krēsls ir krēsls."},
        {"jaut": "Trijstūrim ir 3 stūri.", "opcijas": _BUTISKA,
         "jaukt": False, "pareizi": 0,
         "padoms": "Ar 4 stūriem tas vairs nav trijstūris."},
        {"jaut": "Bumba ir liela.", "opcijas": _BUTISKA, "jaukt": False,
         "pareizi": 1, "padoms": "Ir arī mazas bumbas."},
        {"jaut": "Zīmulis atstāj pēdas uz papīra.", "opcijas": _BUTISKA,
         "jaukt": False, "pareizi": 0,
         "padoms": "Kam zīmulis, ja tas neraksta?"},
        {"jaut": "Grāmata ir 30 cm gara.", "opcijas": _BUTISKA,
         "jaukt": False, "pareizi": 1,
         "padoms": "Grāmatas ir dažādos izmēros."},
    ], pamats=4),

    Ievadi("Saskaiti pēc īpašības", [
        {"jaut": "Cik figūrām ir tieši 3 stūri?",
         "zim": bildes([["trijsturis", "kvadrats", "aplis", "trijsturis",
                         "kvadrats", "trijsturis"]]),
         "atb": ["3"], "padoms": "Meklē trijstūrus."},
        {"jaut": "Cik figūrām nav neviena stūra?",
         "zim": bildes([["aplis", "kvadrats", "aplis", "trijsturis",
                         "aplis", "aplis", "kvadrats"]]),
         "atb": ["4"], "padoms": "Aplim stūru nav."},
        {"jaut": "Cik priekšmetus var ēst?",
         "zim": bildes([["abols", "bumba", "abols", "zimulis", "zivs",
                         "karote"]]),
         "atb": ["3"], "padoms": "Divi āboli un zivs."},
        {"jaut": "Cik priekšmetiem ir riteņi?",
         "zim": bildes([["masina", "kresls", "masina", "soma", "masina"]]),
         "atb": ["3"], "padoms": "Riteņi ir mašīnām."},
    ]),

    Pasaule("Kura ir Toma soma?",
            Varianti("", [
                {"jaut": "Toma soma ir zila un maza. Kura soma ir viņa?",
                 "opcijas": ["C", "A", "B"],
                 "pareizi": 0, "padoms": "Jāder abām īpašībām."},
                {"jaut": "Annas soma ir liela un ar atstarotāju. Kura?",
                 "opcijas": ["B", "A", "C"],
                 "pareizi": 0, "padoms": "Liela ir tikai viena."},
            ]),
            pavediens="skola",
            konteksts="Garderobē palikušas trīs somas: A - sarkana, maza; "
                      "B - zila, liela, ar atstarotāju; C - zila, maza.",
            kapec="Bieži ar vienu īpašību nepietiek - vajag divas kopā."),

    Kopsavilkums([
        "Nosaucu priekšmeta formu, krāsu, izmēru un materiālu.",
        "Atšķiru būtisku īpašību no nebūtiskas.",
        "Atrodu priekšmetu pēc divām īpašībām.",
    ]),

    Majas([
        "Izvēlies vienu priekšmetu virtuvē un nosauc 5 tā īpašības.",
        "Kura no tām ir būtiska? Pastāsti mājiniekam, kāpēc.",
        "Apraksti savu kurpi tā, lai to var atrast starp citām.",
    ]),
]
