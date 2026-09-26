# -*- coding: utf-8 -*-
"""1. klase, 86. stunda: «Cik trūkst līdz 10?»

Saskaitot ar pāriešanu, vispirms papildina līdz 10: 8 + 5 = 8 + 2 + 3.
«Cik trūkst līdz 10» - tie paši desmita draugi, kas 23. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, taisne)

TEMA = "Cik trūkst līdz 10?"

MERKIS = ("Šodien noteiksim, cik trūkst līdz pilnam desmitam, un "
          "izmantosim to saskaitīšanā.")

SATURS = [
    Sakums("8 + 5: vispirms līdz 10, tad tālāk",
           zimejums=taisne(0, 20, 1, [(13, "13")],
                           bultas=[(8, 10, "+2"), (10, 13, "+3")]),
           paraksts="8 + 2 = 10, 10 + 3 = 13.",
           fakti=["Cik trūkst līdz 10? - desmita draugs.",
                  "Pēc tam pieskaita atlikumu.",
                  "8 + 5 = 8 + 2 + 3."]),

    Paraugs("Caur desmitu",
            uzd="Izrēķini 8 + 5.",
            soli=[
                ("8 + 2 = 10", "Līdz 10 trūkst 2."),
                ("5 = 2 + 3", "No 5 paņemam 2, paliek 3."),
                ("10 + 3 = 13", "Pieskaita atlikumu."),
            ],
            atbilde="13"),

    Doma("Lēciens caur 10",
         "Lec līdz 10, tad vēl tik, cik palika.",
         soli=[
             "Cik trūkst līdz 10?",
             "Paņem to no otrā skaitļa.",
             "Pieskaiti atlikumu desmitam.",
         ]),

    Ievadi("Līdz 10", [
        {"jaut": "Cik trūkst līdz 10 no 7?", "atb": ["3"],
         "padoms": "7 + 3 = 10."},
        {"jaut": "Cik trūkst līdz 10 no 9?", "atb": ["1"],
         "padoms": "9 + 1."},
        {"jaut": "7 + 5 = 7 + 3 + ?", "atb": ["2"],
         "padoms": "5 = 3 + 2."},
        {"jaut": "9 + 6 = 10 + ?", "atb": ["5"], "padoms": "6 − 1."},
        {"jaut": "6 + 8 = ?", "atb": ["14"], "padoms": "8 + 2 + 4."},
        {"jaut": "7 + 7 = ?", "atb": ["14"], "padoms": "7 + 3 + 4."},
    ], pamats=4),

    Pasaule("Konfekšu kārba",
            Ievadi("", [
                {"jaut": "Kārbā 10 vietu, ir 6 konfektes. Tu ieliec 7. Cik "
                         "pietrūka vietas? (cik paliek ārā)", "atb": ["3"],
                 "padoms": "4 ietilpst, 3 paliek."},
                {"jaut": "Cik konfekšu kopā?", "atb": ["13"],
                 "padoms": "6 + 7."},
            ]),
            pavediens="veikals",
            konteksts="Konfekšu kārbā ir tieši 10 vietu.",
            kapec="Līdz 10 - un tad tālāk."),

    Kopsavilkums([
        "Zinu, cik trūkst līdz 10.",
        "Saskaitu, papildinot līdz 10.",
        "Pierakstu: 8 + 5 = 8 + 2 + 3.",
    ]),

    Majas([
        "Izrēķini caur 10: 9 + 4, 8 + 6, 7 + 5.",
        "Parādi ar pirkstiem.",
        "Kurš bija vieglākais?",
    ]),
]
