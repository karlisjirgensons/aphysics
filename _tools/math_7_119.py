# -*- coding: utf-8 -*-
"""7. klase, 119. stunda: «Kā savilkt līdzīgos saskaitāmos?»

Līdzīgi saskaitāmie atšķiras tikai ar koeficientu: 3x un 5x, 2ab un −ab.
Tos savelk, saskaitot koeficientus - tā ir reizināšanas sadalāmības
īpašība: 3x + 5x = (3 + 5)x = 8x. Nelīdzīgos (3x un 5) savilkt nevar.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā savilkt līdzīgos saskaitāmos?"

MERKIS = ("Savilksim līdzīgos saskaitāmos un raksturosim izmantoto "
          "darbību īpašību.")

SATURS = [
    Sakums("3 āboli + 5 āboli = 8 āboli. Bet 3 āboli + 5 bumbieri?",
           zimejums=restis([["3x + 5x", "= 8x", "līdzīgi"],
                            ["3x + 5y", "nevar", "nelīdzīgi"],
                            ["3x + 5", "nevar", "nelīdzīgi"]]),
           fakti=["Saskaita tikai «vienādas lietas».",
                  "x ar x, y ar y, skaitļus ar skaitļiem."]),

    Doma("Saskaiti koeficientus",
         "Saskaitāmos, kuriem ir vienāda burtu daļa, sauc par līdzīgiem. Tos "
         "savelk, saskaitot koeficientus un burtu daļu pārrakstot: "
         "ax + bx = (a + b)x.",
         soli=[
             "Atrodi līdzīgos saskaitāmos (vienāda burtu daļa).",
             "Pasvītro tos vienādi.",
             "Saskaiti to koeficientus ar zīmēm.",
             "Pieraksti rezultātu; nelīdzīgos pārraksti.",
         ],
         pieze="x = 1x, −x = −1x. Ja koeficientu summa ir 0, saskaitāmais "
               "pazūd: 4a − 4a = 0."),

    Paraugs("Savelc",
            uzd="Vienkāršo: 5a + 3 − 2a + 7 − a.",
            soli=[
                ("a saskaitāmie: 5a − 2a − a", "Pasvītro."),
                ("(5 − 2 − 1)a = 2a", "Koeficienti."),
                ("Skaitļi: 3 + 7 = 10", "Otrā grupa."),
                ("2a + 10", "Rezultāts."),
            ],
            atbilde="2a + 10"),

    Ievadi("Savelc līdzīgos", [
        {"jaut": "7x + 4x = ?",
         "atb": ["11x"], "padoms": "7 + 4.", "tastatura": "text"},
        {"jaut": "9y − 12y = ?",
         "atb": ["−3y", "-3y"], "padoms": "9 − 12.", "tastatura": "text"},
        {"jaut": "a + a + 3a = ?",
         "atb": ["5a"], "padoms": "1 + 1 + 3.", "tastatura": "text"},
        {"jaut": "4m + 5 − m − 8 = ?",
         "atb": ["3m − 3", "3m-3", "-3+3m"], "padoms": "3m un −3.",
         "tastatura": "text"},
        {"jaut": "2ab + 3ba = ?",
         "atb": ["5ab", "5ba"], "padoms": "ab = ba.", "tastatura": "text"},
        {"jaut": "0,5x − 1,5x = ?",
         "atb": ["−x", "-x", "-1x"], "padoms": "−1x = −x.",
         "tastatura": "text"},
    ], pamats=4),

    Varianti("Līdzīgi vai nē?", [
        {"jaut": "3x un −7x",
         "opcijas": ["Līdzīgi", "Nelīdzīgi"], "pareizi": 0, "jaukt": False,
         "padoms": "Tas pats x."},
        {"jaut": "2x un 2x²",
         "opcijas": ["Līdzīgi", "Nelīdzīgi"], "pareizi": 1, "jaukt": False,
         "padoms": "x un x² - dažādi."},
        {"jaut": "5ab un −ba",
         "opcijas": ["Līdzīgi", "Nelīdzīgi"], "pareizi": 0, "jaukt": False,
         "padoms": "ab = ba."},
        {"jaut": "Kura atbilde ir 3x + 2x + 4?",
         "opcijas": ["5x + 4", "9x", "5x + 4x", "9"],
         "pareizi": 0, "padoms": "4 paliek atsevišķi."},
    ], pamats=4),

    Pasaule("Iepirkumu saraksts",
            Ievadi("", [
                {"jaut": "Ķekars banānu b €, piens p €. Pirmdien: 2b + p; "
                         "trešdien: 3b + 2p; piektdien: b + p. Nedēļā - "
                         "cik b?",
                 "atb": ["6b"], "padoms": "2 + 3 + 1.",
                 "tastatura": "text"},
                {"jaut": "Un cik p?",
                 "atb": ["4p"], "padoms": "1 + 2 + 1.",
                 "tastatura": "text"},
                {"jaut": "Cik € nedēļā, ja b = 1,5, p = 1,2?",
                 "atb": ["13,8"], "padoms": "9 + 4,8."},
            ]),
            pavediens="veikals",
            konteksts="Kase saskaita vienādās preces kopā - tas ir līdzīgo "
                      "saskaitāmo savilkšana.",
            kapec="Viena izteiksme - visai nedēļai."),

    Kopsavilkums([
        "Atrodu līdzīgos saskaitāmos.",
        "Savelku, saskaitot koeficientus.",
        "Zinu, ka tā ir reizināšanas sadalāmības īpašība.",
        "Nelīdzīgos atstāju atsevišķi.",
    ]),

    Majas([
        "Vienkāršo: 8a − 3b + 2a + 5b − a.",
        "Uzraksti savas nedēļas iepirkumus ar burtiem un savelc.",
        "Paskaidro, kāpēc 3x + 2 ≠ 5x.",
    ]),
]
