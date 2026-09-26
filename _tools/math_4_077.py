# -*- coding: utf-8 -*-
"""4. klase, 77. stunda: «Kā reizina rakstos?»

Stabiņš ar divciparu reizinātāju: divas daļreizinājuma rindas - viena ar
vieniem, otra ar desmitiem (nobīdīta par vienu vietu pa kreisi) - un to
summa. Nobīde ir tā pati nulle no 70. stundas, tikai neuzrakstīta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā reizina rakstos?"

MERKIS = ("Reizināsim divus divciparu skaitļus rakstos un paskaidrosim katru "
          "soli.")

SATURS = [
    Sakums("Kā stabiņā sareizina 47 · 36?",
           zimejums=restis([["", "", "4", "7"],
                            ["·", "", "3", "6"],
                            ["", "2", "8", "2"],
                            ["1", "4", "1", ""],
                            ["1", "6", "9", "2"]],
                           "47 · 36 = 1692"),
           paraksts="Rinda 282 = 47 · 6; rinda 141_ = 47 · 30.",
           fakti=["Otrā rinda sākas vienu vietu pa kreisi.",
                  "Tā tukšā vieta ir nulle - reizinām ar desmitiem."]),

    Doma("Divas rindas un to summa",
         "Vispirms reizini ar vieniem, tad ar desmitiem (rakstot par vienu "
         "vietu pa kreisi), tad saskaiti rindas.",
         soli=[
             "1. rinda: 47 · 6 = 282.",
             "2. rinda: 47 · 3 = 141, raksta zem desmitiem (tas ir 1410).",
             "Saskaiti: 282 + 1410 = 1692.",
             "Aptuveni: 50 · 40 = 2000 - atbilde ticama.",
         ],
         pieze="Ja otro rindu neaizbīda pa kreisi, sanāk 282 + 141 - "
               "aplamība."),

    Slidnis("Stabiņš 58 · 24",
            soli=[
                {"v": "58 · 4 = 232", "teksts": "1. rinda - vieni."},
                {"v": "58 · 2 = 116 → 1160", "teksts": "2. rinda - desmiti, "
                 "nobīdīta."},
                {"v": "232 + 1160 = 1392", "teksts": "Saskaita rindas."},
            ]),

    Paraugs("63 · 45",
            uzd="Sareizini 63 · 45 stabiņā.",
            soli=[
                ("63 · 5 = 315", "1. rinda."),
                ("63 · 4 = 252 → 2520", "2. rinda, nobīdīta."),
                ("315 + 2520 = 2835", None),
            ],
            atbilde="2835"),

    Ievadi("Stabiņā", [
        {"jaut": "47 · 36 = ?", "atb": ["1692"], "padoms": "282 + 1410."},
        {"jaut": "58 · 24 = ?", "atb": ["1392"], "padoms": "232 + 1160."},
        {"jaut": "63 · 45 = ?", "atb": ["2835"], "padoms": "315 + 2520."},
        {"jaut": "29 · 17 = ?", "atb": ["493"], "padoms": "203 + 290."},
        {"jaut": "84 · 56 = ?", "atb": ["4704"], "padoms": "504 + 4200."},
        {"jaut": "76 · 98 = ?", "atb": ["7448"], "padoms": "608 + 6840."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "Juris: 34 · 25 = 170 + 68 = 238. Kas nav kārtībā?",
         "opcijas": ["otrā rinda nav nobīdīta (jābūt 680)",
                     "viss pareizi", "reizināja ar 2 un 5 nepareizi"],
         "pareizi": 0, "padoms": "Pareizi 170 + 680 = 850."},
        {"jaut": "Cik ir 34 · 25?",
         "opcijas": ["850", "238", "750", "950"], "pareizi": 0,
         "padoms": "170 + 680."},
        {"jaut": "Ar ko reizina, veidojot otro rindu 52 · 37?",
         "opcijas": ["ar 3 desmitiem", "ar 7", "ar 37", "ar 52"],
         "pareizi": 0, "padoms": "Desmitu cipars."},
    ]),

    Pasaule("Kinoteātra ieņēmumi",
            Ievadi("", [
                {"jaut": "Zālē 18 rindas pa 24 sēdvietām. Cik vietu?",
                 "atb": ["432"], "padoms": "18 · 24."},
                {"jaut": "Biļete 12 €. Ieņēmumi pilnai zālei? (432 · 12)",
                 "atb": ["5184"], "padoms": "864 + 4320."},
                {"jaut": "Vienā seansā pārdotas 37 biļetes pa 12 €. Cik €?",
                 "atb": ["444"], "padoms": "37 · 12."},
                {"jaut": "Popkorns 7 € - pārdoti 65. Cik €?",
                 "atb": ["455"], "padoms": "65 · 7."},
            ]),
            pavediens="veikals",
            konteksts="Kinoteātris katru dienu rēķina vietas un ieņēmumus - "
                      "divciparu reizinājumi ir ikdiena.",
            kapec="Stabiņš ļauj sareizināt jebkurus skaitļus bez "
                  "kalkulatora."),

    Kopsavilkums([
        "Reizinu divus divciparu skaitļus stabiņā.",
        "Nobīdu otro rindu par vienu vietu pa kreisi.",
        "Saskaitu rindas un pārbaudu ar novērtējumu.",
    ]),

    Majas([
        "Sareizini stabiņā savu vecumu ar 52 (cik nedēļu nodzīvots).",
        "Izdomā vienu stabiņu ar pārnesumiem abās rindās.",
        "Paskaidro mājiniekiem, kāpēc otrā rinda nobīdīta.",
    ]),
]
