# -*- coding: utf-8 -*-
"""7. klase, 121. stunda: «Kas notiek ar zīmēm pirms iekavām?»

Mīnuss pirms iekavām ir reizinājums ar −1: −(a − b) = −a + b. Tāpēc,
atverot iekavas ar mīnusu priekšā, visi saskaitāmie maina zīmi. Pluss pirms
iekavām zīmes nemaina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas notiek ar zīmēm pirms iekavām?"

MERKIS = ("Atvērsim iekavas, pirms kurām ir mīnusa zīme, un pamatosim "
          "zīmju maiņu.")

SATURS = [
    Sakums("Atņem visu grozu",
           zimejums=restis([["pirms", "pēc"],
                            ["+(a − b)", "a − b"],
                            ["−(a − b)", "−a + b"],
                            ["−(a + b)", "−a − b"]]),
           paraksts="Mīnuss maina katra saskaitāmā zīmi.",
           fakti=["Atņemot «10 € mīnus 3 € atlaide», atņem 10 un pieskaita 3.",
                  "−(10 − 3) = −10 + 3 = −7.",
                  "Mīnuss pirms iekavām ir reizinājums ar −1."]),

    Doma("Mīnuss = reizinājums ar −1",
         "Ja pirms iekavām ir mīnuss, iekavas atverot, visu saskaitāmo zīmes "
         "maina uz pretējām: −(a + b − c) = −a − b + c. Ja pirms iekavām ir "
         "pluss - zīmes nemainās.",
         soli=[
             "Paskaties uz zīmi pirms iekavām.",
             "Pluss - pārraksti bez iekavām.",
             "Mīnuss - katram saskaitāmajam maini zīmi.",
             "Ja pirms iekavām ir −3, reizini ar −3 katru.",
         ],
         pieze="Pirmais saskaitāmais iekavās bez zīmes ir ar plusu: −(x − 2) = "
               "−x + 2."),

    Paraugs("Divas iekavas",
            uzd="Vienkāršo: (5x − 3) − (2x − 7).",
            soli=[
                ("5x − 3 − 2x + 7", "Otrās iekavas - zīmes maina."),
                ("5x − 2x = 3x", "Līdzīgie."),
                ("−3 + 7 = 4", "Skaitļi."),
                ("3x + 4", "Rezultāts."),
            ],
            atbilde="3x + 4"),

    Ievadi("Atver iekavas", [
        {"jaut": "−(x + 5) = ?",
         "atb": ["−x − 5", "-x-5"], "padoms": "Abas zīmes mainās.",
         "tastatura": "text"},
        {"jaut": "−(3a − 4) = ?",
         "atb": ["−3a + 4", "-3a+4", "4-3a"], "padoms": "−3a un +4.",
         "tastatura": "text"},
        {"jaut": "−2(y − 6) = ?",
         "atb": ["−2y + 12", "-2y+12", "12-2y"], "padoms": "−2 · (−6) = 12.",
         "tastatura": "text"},
        {"jaut": "10 − (x − 3) = ?",
         "atb": ["13 − x", "13-x", "-x+13"], "padoms": "10 − x + 3.",
         "tastatura": "text"},
        {"jaut": "(4m + 1) − (m + 1) = ?",
         "atb": ["3m"], "padoms": "4m + 1 − m − 1.",
         "tastatura": "text"},
        {"jaut": "−3(2 − x) + 6 = ?",
         "atb": ["3x"], "padoms": "−6 + 3x + 6.",
         "tastatura": "text"},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "7 − (x + 2) = 7 − x + 2",
         "opcijas": ["Jābūt 7 − x − 2", "Pareizi", "Jābūt 7 + x − 2",
                     "Jābūt 5x"],
         "pareizi": 0, "padoms": "Arī +2 maina zīmi."},
        {"jaut": "−(a − b) = −a − b",
         "opcijas": ["Jābūt −a + b", "Pareizi", "Jābūt a − b",
                     "Jābūt a + b"],
         "pareizi": 0, "padoms": "−(−b) = +b."},
    ]),

    Pasaule("Budžets ar atlaidi",
            Ievadi("", [
                {"jaut": "Kontā K €. Nopirka lietu par c € ar 5 € atlaidi: "
                         "K − (c − 5). Cik € palika, ja K = 100, c = 30?",
                 "atb": ["75"], "padoms": "100 − 25."},
                {"jaut": "Pārraksti bez iekavām: K − c + ? Kāds skaitlis?",
                 "atb": ["5"], "padoms": "−(−5) = +5."},
                {"jaut": "Pērk 2 lietas pa c € ar 5 € atlaidi katrai: "
                         "K − 2(c − 5). Cik € paliek?",
                 "atb": ["50"], "padoms": "100 − 50."},
            ]),
            pavediens="veikals",
            konteksts="Atlaide ir «mīnuss mīnusā» - tā naudu kontā "
                      "palielina.",
            kapec="Zīmju maiņa ir reāla nauda."),

    Kopsavilkums([
        "Zinu, ka mīnuss pirms iekavām maina visas zīmes.",
        "Zinu, ka pluss pirms iekavām zīmes nemaina.",
        "Reizinu ar negatīvu skaitli katru saskaitāmo.",
        "Atrodu kļūdas zīmju maiņā.",
    ]),

    Majas([
        "Vienkāršo: (8a − 5) − (3a − 2) + (a + 1).",
        "Izdomā budžeta situāciju ar −(c − atlaide).",
        "Paskaidro, kāpēc −(−b) = b.",
    ]),
]
