# -*- coding: utf-8 -*-
"""2. klase, 77. stunda: «Kā pieraksta aprēķinu?»

Izteiksmes vērtības aprēķināšanas pieraksts: virs darbībām uzraksta to
secību (1, 2), zem izteiksmes - starprezultātus, un beigās vērtību.
Skolēns vēro, kā to dara, un skaidro pierakstu vārdos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pieraksta aprēķinu?"

MERKIS = ("Šodien vērosim un skaidrosim, kā pieraksta izteiksmes vērtības "
          "aprēķinu.")

SATURS = [
    Sakums("Kā pierakstīt aprēķinu tā, lai skolotājs redz katru soli?",
           fakti=["Virs darbībām uzraksta secību: 1, 2.",
                  "Pēc tam katru darbību izrēķina.",
                  "Beigās - izteiksmes vērtība."]),

    Doma("Aprēķina pieraksts",
         "Pieraksts parāda secību un katru starprezultātu.",
         soli=[
             "Uzraksti izteiksmi.",
             "Virs katras darbības uzraksti tās numuru.",
             "Izrēķini 1. darbību un pieraksti rezultātu.",
             "Izrēķini 2. darbību - tā ir vērtība.",
         ]),

    Paraugs("Aprēķini 64 − (19 + 21)",
            uzd="Pieraksti aprēķinu ar darbību secību.",
            soli=[("1: 19 + 21 = 40", "Pirmā darbība - iekavās."),
                  ("2: 64 − 40 = 24", "Otrā darbība."),
                  ("64 − (19 + 21) = 24", "Vērtība.")],
            atbilde="24"),

    Paraugs("Aprēķini 38 + 17 − 25",
            uzd="Bez iekavām - no kreisās uz labo.",
            soli=[("1: 38 + 17 = 55", "Pirmā no kreisās."),
                  ("2: 55 − 25 = 30", "Otrā."),
                  ("38 + 17 − 25 = 30", "Vērtība.")],
            atbilde="30"),

    Ievadi("Starprezultāti", [
        {"jaut": "52 − (16 + 14): 1. darbības rezultāts?", "atb": ["30"],
         "padoms": "16 + 14."},
        {"jaut": "52 − (16 + 14) = ?", "atb": ["22"], "padoms": "52 − 30."},
        {"jaut": "27 + 33 − 18: 1. darbības rezultāts?", "atb": ["60"],
         "padoms": "27 + 33."},
        {"jaut": "27 + 33 − 18 = ?", "atb": ["42"], "padoms": "60 − 18."},
        {"jaut": "91 − 45 + 24: 1. darbības rezultāts?", "atb": ["46"],
         "padoms": "91 − 45."},
        {"jaut": "91 − 45 + 24 = ?", "atb": ["70"], "padoms": "46 + 24."},
    ], pamats=4),

    Varianti("Kura ir 1. darbība?", [
        {"jaut": "75 − (20 + 35)", "opcijas": ["20 + 35", "75 − 20",
                                               "75 − 35"],
         "pareizi": 0, "padoms": "Iekavas vispirms."},
        {"jaut": "48 − 20 + 12", "opcijas": ["48 − 20", "20 + 12",
                                             "48 + 12"],
         "pareizi": 0, "padoms": "No kreisās."},
    ]),

    Pasaule("Sporta punkti",
            Ievadi("", [
                {"jaut": "Komanda: 36 punkti, bonuss 14, sods 20. Aprēķini "
                         "36 + 14 − 20.", "atb": ["30"],
                 "padoms": "1: 50, 2: 30."},
                {"jaut": "Otra komanda: 60 − (12 + 8). Cik punktu?",
                 "atb": ["40"], "padoms": "1: 20, 2: 40."},
            ]),
            pavediens="sports",
            konteksts="Stafetē punktus pieskaita un atņem.",
            kapec="Pieraksts ļauj tiesnesim pārbaudīt katru soli."),

    Kopsavilkums([
        "Atzīmēju darbību secību virs izteiksmes.",
        "Pierakstu katru starprezultātu.",
        "Paskaidroju savu aprēķinu.",
    ]),

    Majas([
        "Aprēķini ar pierakstu: 80 − (35 + 15), 29 + 31 − 40.",
        "Atzīmē darbību secību.",
        "Paskaidro mājiniekam katru soli.",
    ]),
]
