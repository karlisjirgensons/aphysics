# -*- coding: utf-8 -*-
"""4. klase, 89. stunda: «Kāda ir darbību secība?»

Darbību secība ar lieliem skaitļiem - tas pats noteikums, ko 17. stundā,
tikai tagad reizināšana un dalīšana ir ar divciparu skaitļiem. Skolēns
numurē darbības, un tikai tad rēķina - tā neviena darbība nepazūd.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kāda ir darbību secība?"

MERKIS = ("Aprēķināsim izteiksmes vērtību ar divām vai trim darbībām un "
          "iekavām.")

SATURS = [
    Sakums("Vai 1000 − 24 · 25 ir 24 400 vai 400?",
           zimejums=restis([["1000 − 24 · 25", ""],
                            ["1. 24 · 25", "= 600"],
                            ["2. 1000 − 600", "= 400"]],
                           "vispirms reizināšana"),
           paraksts="Pareizi ir 400.",
           fakti=["Ja rēķina no kreisās, sanāk 976 · 25 = 24 400.",
                  "Bet reizināšana jāizpilda pirms atņemšanas."]),

    Doma("Iekavas, · un :, tad + un −",
         "Noteikums nemainās, lai cik lieli skaitļi: vispirms iekavas, tad "
         "reizināšana un dalīšana, tad saskaitīšana un atņemšana.",
         soli=[
             "Virs katras zīmes uzraksti darbības numuru.",
             "Izpildi darbības pēc numuriem, katru pierakstot.",
             "Vienas pakāpes darbības - no kreisās uz labo.",
             "Pārbaudi galarezultātu ar novērtējumu.",
         ],
         pieze="(1000 − 24) · 25 = 976 · 25 = 24 400 - iekavas maina visu."),

    Slidnis("5000 − 840 : 21 · 12",
            soli=[
                {"v": "5000 − 840 : 21 · 12", "teksts": "Sākums."},
                {"v": "5000 − 40 · 12", "teksts": "1. dalīšana."},
                {"v": "5000 − 480", "teksts": "2. reizināšana."},
                {"v": "4520", "teksts": "3. atņemšana."},
            ]),

    Paraugs("(35 + 13) · 21 − 999",
            uzd="Aprēķini (35 + 13) · 21 − 999.",
            soli=[
                ("35 + 13 = 48", "1. iekavas."),
                ("48 · 21 = 1008", "2. reizināšana."),
                ("1008 − 999 = 9", "3. atņemšana."),
            ],
            atbilde="9"),

    Ievadi("Izrēķini", [
        {"jaut": "1000 − 24 · 25 = ?", "atb": ["400"], "padoms": "600."},
        {"jaut": "(1000 − 24) · 25 = ?", "atb": ["24400", "24 400"],
         "padoms": "976 · 25."},
        {"jaut": "720 : 24 + 16 · 5 = ?", "atb": ["110"],
         "padoms": "30 + 80."},
        {"jaut": "720 : (24 + 16) · 5 = ?", "atb": ["90"],
         "padoms": "720 : 40 = 18; 18 · 5."},
        {"jaut": "5000 − 840 : 21 · 12 = ?", "atb": ["4520"],
         "padoms": "40 · 12 = 480."},
        {"jaut": "(35 + 13) · 21 − 999 = ?", "atb": ["9"],
         "padoms": "1008 − 999."},
    ], pamats=4),

    Varianti("Kura darbība pirmā?", [
        {"jaut": "300 + 45 · 12",
         "opcijas": ["45 · 12", "300 + 45"], "pareizi": 0,
         "padoms": "Reizināšana."},
        {"jaut": "960 : 32 : 3",
         "opcijas": ["960 : 32", "32 : 3"], "pareizi": 0,
         "padoms": "No kreisās."},
        {"jaut": "Kur likt iekavas, lai 48 − 16 · 2 = 64?",
         "opcijas": ["(48 − 16) · 2", "48 − (16 · 2)",
                     "iekavas nevajag"], "pareizi": 0,
         "padoms": "32 · 2 = 64."},
    ]),

    Pasaule("Sporta kluba rēķins",
            Ievadi("", [
                {"jaut": "Klubā 24 bērni, katram forma 35 € un soma 15 €. "
                         "24 · (35 + 15) = ?",
                 "atb": ["1200"], "padoms": "24 · 50."},
                {"jaut": "Sponsors sedz 480 €. 1200 − 480 = ?",
                 "atb": ["720"], "padoms": "Atlikusī summa."},
                {"jaut": "Atlikumu sadala uz 24 ģimenēm: 720 : 24 = ?",
                 "atb": ["30"], "padoms": "24 · 30 = 720."},
                {"jaut": "Visu vienā izteiksmē: (24 · 50 − 480) : 24 = ?",
                 "atb": ["30"], "padoms": "Tas pats rezultāts."},
            ]),
            pavediens="sports",
            konteksts="Kluba grāmatvedis raksta vienu izteiksmi visam "
                      "rēķinam - un secība izšķir, cik maksās katrs.",
            kapec="Viena izteiksme ir īsāka par trim atsevišķiem rēķiniem."),

    Kopsavilkums([
        "Ievēroju darbību secību ar lieliem skaitļiem.",
        "Numurēju darbības pirms rēķināšanas.",
        "Lietoju iekavas, lai mainītu secību.",
    ]),

    Majas([
        "Uzraksti vienu izteiksmi savas klases ekskursijas budžetam.",
        "Izdomā izteiksmi, kurā iekavas maina rezultātu vairāk nekā 10 "
        "reizes.",
        "Pārbaudi ar kalkulatoru, vai tas ievēro darbību secību.",
    ]),
]
