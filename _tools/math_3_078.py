# -*- coding: utf-8 -*-
"""3. klase, 78. stunda: «Kā daļu parāda pulkstenis?»

Pulkstenis ir daļu modelis, kuru bērns lieto katru dienu, pats to nezinot:
ciparnīca ir riņķis, sadalīts 12 daļās, un «pusstunda» ar «ceturtdaļstunda»
jau ir daļskaitļu vārdi. Šī stunda to sasaista ar laiku minūtēs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         rinkis)

TEMA = "Kā daļu parāda pulkstenis?"

MERKIS = ("Ar pulksteņa modeli parādīsim pusi un ceturtdaļu no stundas.")

SATURS = [
    Sakums("Kāpēc saka «pusstunda», nevis «trīsdesmit minūtes»?",
           zimejums=rinkis(sektors=180, virsraksts="pusstunda",
                           paraksts="30 minūtes no 60"),
           fakti=["Stundā ir 60 minūtes.",
                  "Puse stundas ir 30 minūtes, ceturtdaļa - 15."]),

    Doma("Ciparnīca ir riņķis, sadalīts daļās",
         "Puse stundas ir {1|2} no 60 minūtēm, ceturtdaļa - {1|4} no 60.",
         soli=[
             "Atceries: stundā ir 60 minūtes.",
             "Puse: 60 : 2 = 30 minūtes.",
             "Ceturtdaļa: 60 : 4 = 15 minūtes.",
             "Trešdaļa: 60 : 3 = 20 minūtes.",
         ],
         pieze="60 ir ērts skaitlis tieši tāpēc, ka tas dalās ar 2, 3, 4, 5, "
               "6 un 10 - gandrīz jebkuru daļu var izteikt veselās minūtēs."),

    Slidnis("Kā aug stunda",
            soli=[
                {"v": "{1|4} stundas", "teksts": "15 minūtes.", "josla": 25},
                {"v": "{1|2} stundas", "teksts": "30 minūtes.", "josla": 50},
                {"v": "{3|4} stundas", "teksts": "45 minūtes.", "josla": 75},
                {"v": "1 stunda", "teksts": "60 minūtes - viss vesels.",
                 "josla": 100},
            ],
            ievads="Katrs solis pieliek vienu ceturtdaļu stundas."),

    Paraugs("Cik minūšu ir trīs ceturtdaļstundas?",
            uzd="Cik minūšu ir {3|4} stundas?",
            soli=[
                ("60 : 4 = 15",
                 "Viena ceturtdaļa stundas."),
                ("3 · 15 = 45",
                 "Trīs ceturtdaļas."),
                ("45 minūtes",
                 "Pārbaude: 60 − 45 = 15, tas ir tieši viena ceturtdaļa."),
            ],
            atbilde="45 minūtes"),

    Ievadi("Daļa no stundas", [
        {"jaut": "Cik minūšu ir {1|2} stundas?", "atb": ["30"],
         "padoms": "60 : 2."},
        {"jaut": "Cik minūšu ir {1|4} stundas?", "atb": ["15"],
         "padoms": "60 : 4."},
        {"jaut": "Cik minūšu ir {1|3} stundas?", "atb": ["20"],
         "padoms": "60 : 3."},
        {"jaut": "Cik minūšu ir {3|4} stundas?", "atb": ["45"],
         "padoms": "3 · 15."},
        {"jaut": "Cik minūšu ir {1|6} stundas?", "atb": ["10"],
         "padoms": "60 : 6."},
        {"jaut": "Cik minūšu ir {2|3} stundas?", "atb": ["40"],
         "padoms": "2 · 20."},
    ], pamats=4),

    Zimejums("Ceturtdaļa ciparnīcā",
             rinkis(sektors=90, virsraksts="ceturtdaļstunda",
                    paraksts="15 minūtes"),
             paskaidro="Ceturtdaļa ir taisns leņķis ciparnīcā - no 12 līdz 3.",
             ievads="Tā izskatās 15 minūtes."),

    Varianti("Cik ilgi tas ir?", [
        {"jaut": "Cik minūšu ir pusstunda?",
         "opcijas": ["30", "15", "45", "60"],
         "pareizi": 0, "padoms": "60 : 2."},
        {"jaut": "Kāda daļa no stundas ir 20 minūtes?",
         "opcijas": ["{1|3}", "{1|2}", "{1|4}", "{2|3}"],
         "pareizi": 0, "padoms": "60 : 20 = 3."},
        {"jaut": "Kāda daļa no stundas ir 45 minūtes?",
         "opcijas": ["{3|4}", "{1|2}", "{2|3}", "{4|5}"],
         "pareizi": 0, "padoms": "Trīs ceturtdaļas pa 15 minūtēm."},
        {"jaut": "Cik ceturtdaļstundu ir vienā stundā?",
         "opcijas": ["4", "2", "6", "15"],
         "pareizi": 0, "padoms": "60 : 15."},
    ], pamats=4),

    Pasaule("Cik ilgi cepas kūka?",
            Ievadi("", [
                {"jaut": "Kūka cepas {3|4} stundas. Cik minūšu tas ir?",
                 "atb": ["45"], "padoms": "3 · 15."},
                {"jaut": "Mīkla jāatstāj {1|2} stundu. Cik minūšu?",
                 "atb": ["30"], "padoms": "60 : 2."},
                {"jaut": "Cik minūšu kopā aizņem abi soļi?",
                 "atb": ["75"], "padoms": "45 + 30."},
                {"jaut": "Cik tas ir stundās un minūtēs? Ieraksti minūtes "
                         "virs veselās stundas.",
                 "atb": ["15"], "padoms": "75 − 60."},
            ]),
            pavediens="virtuve",
            konteksts="Receptēs laiku raksta gan minūtēs, gan daļās no "
                      "stundas - abi jāprot pārvērst.",
            kapec="Ja daļu nesaprot, kūka paliek krāsnī par ilgu."),

    Kopsavilkums([
        "Zinu, ka stundā ir 60 minūtes.",
        "Aprēķinu pusi, trešdaļu un ceturtdaļu no stundas.",
        "Parādu daļu uz pulksteņa ciparnīcas.",
        "Nosaku, kāda daļa no stundas ir dotais minūšu skaits.",
    ]),

    Majas([
        "Paskaties pulkstenī un pasaki, cik minūšu palicis līdz pilnai "
        "stundai.",
        "Izrēķini, cik minūšu ir {2|3} stundas.",
        "Atrodi kādu darbu mājās, kas aizņem tieši ceturtdaļstundu.",
    ]),
]
