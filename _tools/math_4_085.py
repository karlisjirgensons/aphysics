# -*- coding: utf-8 -*-
"""4. klase, 85. stunda: «Cik apmēram būs dalījums?»

Dalījumu novērtē, noapaļojot dalītāju līdz desmitiem un dalāmo līdz ērtam
skaitlim (1472 : 32 ≈ 1500 : 30 = 50). Tad pārbauda ar kalkulatoru - un
novērtējums pasaka, vai kalkulatorā nav nospiests kas lieks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Cik apmēram būs dalījums?"

MERKIS = ("Noteiksim dalījuma aptuveno vērtību un pārbaudīsim to ar "
          "kalkulatoru.")

SATURS = [
    Sakums("Cik dienu ceļā, ja jānobrauc 2940 km pa 490 km dienā?",
           zimejums=kolonnas([("aptuveni", 6), ("precīzi", 6)],
                             " d."),
           paraksts="2940 : 490 ≈ 3000 : 500 = 6.",
           fakti=["Novērtējums dažreiz sakrīt ar precīzo.",
                  "Pat ja nesakrīt, tas pasaka, cik ciparu būs."]),

    Doma("Noapaļo dalītāju, pielāgo dalāmo",
         "Dalītāju noapaļo līdz desmitiem, dalāmo - līdz skaitlim, kas ar to "
         "ērti dalās.",
         soli=[
             "Noapaļo dalītāju: 32 ≈ 30.",
             "Atrodi ērtu dalāmo tuvumā: 1472 ≈ 1500.",
             "Dali galvā: 1500 : 30 = 50.",
             "Precīzajam jābūt tuvu 50 (tas ir 46).",
         ],
         pieze="Ja kalkulatorā sanāk 4,6 vai 460, novērtējums uzreiz "
               "parāda kļūdu."),

    Paraugs("Novērtē 2784 : 48",
            uzd="Novērtē un pārbaudi ar kalkulatoru 2784 : 48.",
            soli=[
                ("48 ≈ 50, 2784 ≈ 2800 vai 3000", None),
                ("3000 : 50 = 60", "Novērtējums."),
                ("2784 : 48 = 58", "Kalkulatorā - tuvu 60."),
            ],
            atbilde="58"),

    Kustiba("Kur būs dalījums?", [
        {"jaut": "Novērtē 1472 : 32 ≈ 1500 : 30.",
         "atb": 50, "beigas": 100, "iedala": 10,
         "merkis": "≈", "objekts": "Laiva",
         "padoms": "150 : 3.",
         "stasts": "Laiva peld līdz novērtējumam."},
        {"jaut": "Novērtē 2784 : 48 ≈ 3000 : 50.",
         "atb": 60, "beigas": 100, "iedala": 10,
         "merkis": "≈", "objekts": "Laiva", "padoms": "300 : 5."},
        {"jaut": "Novērtē 1239 : 59 ≈ 1200 : 60.",
         "atb": 20, "beigas": 100, "iedala": 10,
         "merkis": "≈", "objekts": "Laiva", "padoms": "120 : 6."},
        {"jaut": "Novērtē 7120 : 89 ≈ 7200 : 90.",
         "atb": 80, "beigas": 100, "iedala": 10,
         "merkis": "≈", "objekts": "Laiva", "padoms": "720 : 9."},
    ], pamats=2),

    Varianti("Vai kalkulators neiet greizi?", [
        {"jaut": "Kalkulators: 3276 : 42 = 780. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "3200 : 40 = 80; pareizi 78."},
        {"jaut": "Kalkulators: 1702 : 23 = 74. Ticams?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "1600 : 20 = 80 - tuvu."},
        {"jaut": "Kalkulators: 5320 : 56 = 9,5. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "5400 : 60 = 90; pareizi 95."},
        {"jaut": "Cik ciparu būs 8526 : 42?",
         "opcijas": ["3", "2", "4", "1"], "pareizi": 0,
         "padoms": "8000 : 40 = 200."},
    ], pamats=4),

    Ievadi("Novērtē", [
        {"jaut": "4830 : 69 ≈ 4900 : 70 = ?", "atb": ["70"],
         "padoms": "490 : 7."},
        {"jaut": "2760 : 46 ≈ 3000 : 50 = ?", "atb": ["60"],
         "padoms": "300 : 5."},
        {"jaut": "1586 : 21 ≈ 1600 : 20 = ?", "atb": ["80"],
         "padoms": "160 : 2."},
        {"jaut": "Precīzi 2760 : 46 = ?", "atb": ["60"],
         "padoms": "46 · 60 = 2760."},
    ]),

    Pasaule("Ceļojums ar auto",
            Ievadi("", [
                {"jaut": "Rīga-Barselona ir ap 2940 km. Dienā 490 km. Novērtē "
                         "dienas: 3000 : 500 = ?",
                 "atb": ["6"], "padoms": "30 : 5."},
                {"jaut": "Precīzi: 2940 : 490 = ?", "atb": ["6"],
                 "padoms": "294 : 49."},
                {"jaut": "Degviela 2940 km ceļam - 210 l. Cik km ar 1 l? "
                         "(2940 : 210)",
                 "atb": ["14"], "padoms": "294 : 21."},
                {"jaut": "Ceļa izmaksas 1488 € uz 4 cilvēkiem. Cik katram?",
                 "atb": ["372"], "padoms": "1488 : 4."},
            ]),
            pavediens="celojums",
            konteksts="Plānojot tālu braucienu, vispirms novērtē dienas un "
                      "izmaksas galvā, tad precizē.",
            kapec="Novērtējums pasargā no plāniem, kas nav iespējami."),

    Kopsavilkums([
        "Novērtēju dalījumu ar divciparu dalītāju.",
        "Pārbaudu kalkulatora rezultātu ar novērtējumu.",
        "Nosaku, cik ciparu būs dalījumā.",
    ]),

    Majas([
        "Novērtē, cik dienu vajag, lai nobrauktu 1200 km pa 300 km dienā.",
        "Ar kalkulatoru izdali 3 skaitļus un pārbaudi ar novērtējumu.",
        "Izdomā «kalkulatora kļūdu» un atmasko to.",
    ]),
]
