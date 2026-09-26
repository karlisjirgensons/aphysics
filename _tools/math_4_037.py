# -*- coding: utf-8 -*-
"""4. klase, 37. stunda: «Kā reizināt katru šķiru atsevišķi?»

No divciparu uz trīsciparu: 243 · 3 = 200 · 3 + 40 · 3 + 3 · 3. Taisnstūris
tagad sadalās trīs daļās. Tā ir tā pati sadalīšanas īpašība - tikai ar
vienu saskaitāmo vairāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā reizināt katru šķiru atsevišķi?"

MERKIS = ("Reizināsim trīsciparu skaitli ar viencipara skaitli, lietojot "
          "decimālo sastāvu.")

SATURS = [
    Sakums("Cik sēdvietu ir 4 vilciena vagonos?",
           zimejums=restis([["", "simti", "desmiti", "vieni"],
                            ["124", "100", "20", "4"],
                            ["· 4", "400", "80", "16"]],
                           "124 · 4 = 400 + 80 + 16"),
           paraksts="Pavisam 496 vietas.",
           fakti=["Vilciena vagonā var būt ap 124 sēdvietām.",
                  "Katra šķira tiek reizināta atsevišķi."]),

    Doma("Trīs šķiras - trīs reizinājumi",
         "Sadali trīsciparu skaitli simtos, desmitos un vienos, reizini katru "
         "un saskaiti.",
         soli=[
             "243 = 200 + 40 + 3.",
             "200 · 3 = 600, 40 · 3 = 120, 3 · 3 = 9.",
             "600 + 120 + 9 = 729.",
             "Aptuvena pārbaude: 243 ≈ 250, 250 · 3 = 750 - tuvu.",
         ],
         pieze="Nulle šķirā dod nulli reizinājumā: 305 · 2 = 600 + 0 + 10."),

    Paraugs("318 · 5",
            uzd="Izrēķini 318 · 5.",
            soli=[
                ("300 · 5 = 1500", None),
                ("10 · 5 = 50", None),
                ("8 · 5 = 40", None),
                ("1500 + 50 + 40 = 1590", None),
            ],
            atbilde="1590"),

    Slidnis("Kā aug 234 · 4",
            soli=[
                {"v": "200 · 4 = 800", "teksts": "Simti.", "josla": 85},
                {"v": "800 + 30 · 4 = 920", "teksts": "Pieskaita desmitus.",
                 "josla": 98},
                {"v": "920 + 4 · 4 = 936", "teksts": "Pieskaita vienus.",
                 "josla": 100},
            ],
            ievads="Lielāko daļu dod simti - vieni ir tikai aste."),

    Ievadi("Pa šķirām", [
        {"jaut": "213 · 3 = ?", "atb": ["639"], "padoms": "600 + 30 + 9."},
        {"jaut": "124 · 4 = ?", "atb": ["496"], "padoms": "400 + 80 + 16."},
        {"jaut": "305 · 2 = ?", "atb": ["610"], "padoms": "600 + 10."},
        {"jaut": "152 · 6 = ?", "atb": ["912"], "padoms": "600 + 300 + 12."},
        {"jaut": "421 · 7 = ?", "atb": ["2947"],
         "padoms": "2800 + 140 + 7."},
        {"jaut": "246 · 3 = ?", "atb": ["738"], "padoms": "600 + 120 + 18."},
    ], pamats=4),

    Varianti("Kurš sadalījums pareizs?", [
        {"jaut": "Kā sadalīt 427 · 3?",
         "opcijas": ["400 · 3 + 20 · 3 + 7 · 3", "400 + 20 + 7 · 3",
                     "4 · 3 + 2 · 3 + 7 · 3", "427 + 3"], "pareizi": 0,
         "padoms": "Katru daļu reizina ar 3."},
        {"jaut": "Cik ir 400 · 3?",
         "opcijas": ["1200", "120", "12 000", "403"], "pareizi": 0,
         "padoms": "4 simti · 3 = 12 simti."},
        {"jaut": "Cik ir 427 · 3?",
         "opcijas": ["1281", "1261", "1201", "1227"], "pareizi": 0,
         "padoms": "1200 + 60 + 21."},
    ]),

    Pasaule("Vilciens uz Daugavpili",
            Ievadi("", [
                {"jaut": "Vilcienā 4 vagoni pa 124 vietām. Cik vietu pavisam?",
                 "atb": ["496"], "padoms": "124 · 4."},
                {"jaut": "Brīvdienās piekabina vēl 2 vagonus. Cik vietu 6 "
                         "vagonos?",
                 "atb": ["744"], "padoms": "124 · 6."},
                {"jaut": "Vilciens dienā brauc 3 reizes turp. Cik vietu "
                         "dienā (4 vagoni)?",
                 "atb": ["1488"], "padoms": "496 · 3."},
                {"jaut": "Rīga-Daugavpils ir 218 km. Cik km nobrauc 4 "
                         "braucienos?",
                 "atb": ["872"], "padoms": "800 + 40 + 32."},
            ]),
            pavediens="celojums",
            konteksts="Dzelzceļa plānotāji rēķina vietas vagonos un "
                      "braucienos - viss ir reizināšana.",
            kapec="Pa šķirām var sareizināt jebkuru trīsciparu skaitli."),

    Kopsavilkums([
        "Sadalu trīsciparu skaitli šķirās.",
        "Reizinu katru šķiru atsevišķi un saskaitu.",
        "Pārbaudu ar aptuveno vērtību.",
    ]),

    Majas([
        "Izrēķini, cik lappušu ir 3 vienādās grāmatās mājās.",
        "Izrēķini 111 · 5 un 222 · 4. Ko pamani?",
        "Pastāsti mājiniekam, kā reizināji 318 · 5.",
    ]),
]
