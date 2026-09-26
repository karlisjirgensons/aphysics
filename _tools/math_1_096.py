# -*- coding: utf-8 -*-
"""1. klase, 96. stunda: «Ko nozīmē atņemt?»

Atņemšana ir arī nezināmā saskaitāmā meklēšana: 9 − 6 - kas kopā ar 6
dod 9? Skaitīšana uz priekšu no 6 līdz 9 dod 3. Tas bieži ir ātrāk nekā
skaitīt atpakaļ.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, majina, taisne)

TEMA = "Ko nozīmē atņemt?"

MERKIS = ("Šodien skaidrosim atņemšanu kā meklēšanu: kas kopā ar atņemamo "
          "dod doto skaitli.")

SATURS = [
    Sakums("9 − 6: kas kopā ar 6 dod 9?",
           zimejums=taisne(0, 10, 1, [(9, "9")],
                           bultas=[(6, 7, ""), (7, 8, ""), (8, 9, "")]),
           paraksts="No 6 līdz 9 - 3 lēcieni: 9 − 6 = 3.",
           fakti=["Atņemt - atrast, cik vēl līdz.",
                  "6 + ? = 9.",
                  "Skaiti uz priekšu no mazākā."]),

    Doma("Atņemšana kā «cik vēl?»",
         "9 − 6 un 6 + ? = 9 ir viens un tas pats jautājums.",
         soli=[
             "Izlasi: 15 − 12.",
             "Pajautā: 12 + ? = 15.",
             "Skaiti no 12 līdz 15: 3.",
         ],
         pieze="Ja skaitļi ir tuvu viens otram, skaitīt uz priekšu ir "
               "ātrāk."),

    Ievadi("Cik vēl līdz?", [
        {"jaut": "6 + ? = 9", "zim": majina(9, [(6, None)]), "atb": ["3"],
         "padoms": "7, 8, 9."},
        {"jaut": "15 − 12 = ?", "atb": ["3"], "padoms": "12 + ? = 15."},
        {"jaut": "20 − 17 = ?", "atb": ["3"], "padoms": "17 + ? = 20."},
        {"jaut": "14 − 11 = ?", "atb": ["3"], "padoms": "11 + ? = 14."},
        {"jaut": "13 − 9 = ?", "atb": ["4"], "padoms": "9 + ? = 13."},
        {"jaut": "18 − 15 = ?", "atb": ["3"], "padoms": "15 + ? = 18."},
    ], pamats=4),

    Varianti("Kurš jautājums ir tas pats?", [
        {"jaut": "12 − 8 = ?",
         "opcijas": ["8 + ? = 12", "12 + 8 = ?", "8 − 12 = ?"],
         "pareizi": 0, "padoms": "Cik vēl līdz 12?"},
    ]),

    Pasaule("Cik vēl jāgaida?",
            Ievadi("", [
                {"jaut": "Tev ir 7 gadi. Cik gadu vēl līdz 16?", "atb": ["9"],
                 "padoms": "7 + ? = 16."},
                {"jaut": "Grāmatā 20 lappušu, esi 17. lappusē. Cik vēl?",
                 "atb": ["3"], "padoms": "17 + ? = 20."},
            ]),
            pavediens="maja",
            konteksts="«Cik vēl?» ir atņemšana.",
            kapec="Skaitot uz priekšu, atbildi atrodi ātri."),

    Kopsavilkums([
        "Skaidroju atņemšanu kā «cik vēl līdz».",
        "Skaitu uz priekšu no atņemamā.",
        "Izvēlos ātrāko veidu.",
    ]),

    Majas([
        "Cik dienu vēl līdz brīvdienām? Skaiti uz priekšu.",
        "Izrēķini 16 − 13 ar skaitīšanu uz priekšu.",
        "Pastāsti, kāpēc tas ir ātri.",
    ]),
]
