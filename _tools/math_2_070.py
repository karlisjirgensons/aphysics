# -*- coding: utf-8 -*-
"""2. klase, 70. stunda: «Ko aprēķināt vispirms?»

Situācija no vairākiem teikumiem prasa vairākas darbības, un to secība
nav nejauša: vispirms jāuzzina tas, ko nākamais solis izmanto. Šodien soļus
vēl raksta atsevišķi; vienā izteiksmē tos saliks nākamajā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, sloksnes)

TEMA = "Ko aprēķināt vispirms?"

MERKIS = ("Šodien situāciju ar vairākiem teikumiem raksturosim ar atsevišķām "
          "darbībām un paskaidrosim to secību.")

SATURS = [
    Sakums("Lai uzzinātu, cik ābolu palika, kas jāzina vispirms?",
           zimejums=sloksnes([("savāca", 10, "40"), ("apēda", 3, "12"),
                              ("iedeva", 2, "8")], starpiba=False),
           fakti=["Savāca 40, apēda 12, iedeva kaimiņiem 8.",
                  "Vispirms - cik palika pēc ēšanas: 40 − 12 = 28.",
                  "Tad - pēc dāvināšanas: 28 − 8 = 20."]),

    Doma("Secība ir svarīga",
         "Vispirms aprēķina to, bez kā nākamo soli nevar izdarīt.",
         soli=[
             "Izlasi visu situāciju.",
             "Atrodi, kas notika pirmais.",
             "Pieraksti 1. darbību un tās rezultātu.",
             "Ar šo rezultātu veic 2. darbību.",
         ]),

    Paraugs("Cik bērnu autobusā?",
            uzd="Autobusā bija 25 bērni. Pieturā iekāpa 8, nākamajā izkāpa 6.",
            soli=[("1) 25 + 8 = 33", "Pēc pirmās pieturas."),
                  ("2) 33 − 6 = 27", "Pēc otrās pieturas.")],
            atbilde="27 bērni"),

    Ievadi("Pa soļiem", [
        {"jaut": "Makā 50 €. Nopirka grāmatu par 18 €, tad saņēma 10 €. "
                 "Cik tagad?", "atb": ["42"], "mers": "€",
         "padoms": "50 − 18 = 32, 32 + 10."},
        {"jaut": "Plauktā 34 grāmatas. Ielika 12, paņēma 20. Cik tagad?",
         "atb": ["26"], "padoms": "34 + 12 = 46, 46 − 20."},
        {"jaut": "Dārzā 60 puķes. Nogrieza 15, iestādīja 7. Cik tagad?",
         "atb": ["52"], "padoms": "60 − 15 = 45, 45 + 7."},
        {"jaut": "Kastē 45 klucīši. Izbēra 20, atpakaļ ielika 9. Cik "
                 "kastē?", "atb": ["34"], "padoms": "45 − 20 = 25, 25 + 9."},
        {"jaut": "Vilcienā 70 pasažieri. Izkāpa 32, iekāpa 18. Cik tagad?",
         "atb": ["56"], "padoms": "70 − 32 = 38, 38 + 18."},
        {"jaut": "Bija 28 uzlīmes. Dabūja 15, pazaudēja 5. Cik tagad?",
         "atb": ["38"], "padoms": "28 + 15 = 43, 43 − 5."},
    ], pamats=4),

    Varianti("Kura ir 1. darbība?", [
        {"jaut": "Klasē 26 bērni. 4 aizgāja pie ārsta, pēc tam 2 atgriezās. "
                 "Kura ir pirmā darbība?",
         "opcijas": ["26 − 4", "26 + 2", "4 − 2"], "pareizi": 0,
         "padoms": "Kas notika pirmais?"},
        {"jaut": "Anna iekrāja 30 €, vecmāmiņa iedeva 20 €, Anna nopirka "
                 "spēli par 35 €. Kura ir otrā darbība?",
         "opcijas": ["50 − 35", "30 − 35", "30 + 20"], "pareizi": 0,
         "padoms": "Pēc 30 + 20 = 50."},
    ]),

    Pasaule("Rudens ražas novākšana",
            Ievadi("", [
                {"jaut": "Savāca 40 ābolus, apēda 12, kaimiņiem iedeva 8. "
                         "Cik palika?", "atb": ["20"],
                 "padoms": "40 − 12 = 28, 28 − 8."},
                {"jaut": "Nākamajā dienā savāca vēl 25. Cik tagad?",
                 "atb": ["45"], "padoms": "20 + 25."},
            ]),
            pavediens="daba",
            konteksts="Ģimene vāc ābolus vecvecāku dārzā.",
            kapec="Pareizā secībā rēķinot, atbilde sakrīt ar īstenību."),

    Kopsavilkums([
        "Sadalu situāciju atsevišķās darbībās.",
        "Nosaku, kura darbība jāveic vispirms.",
        "Izmantoju iepriekšējā soļa rezultātu.",
    ]),

    Majas([
        "Izdomā stāstu ar trīs notikumiem, kur kaut kā kļūst vairāk vai "
        "mazāk.",
        "Pieraksti darbības pa soļiem.",
        "Lai mājinieks pārbauda.",
    ]),
]
