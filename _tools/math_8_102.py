# -*- coding: utf-8 -*-
"""8. klase, 102. stunda: «Kā aprēķina romba laukumu?»

Divas formulas: S = {d_1 · d_2|2} (rombs ir puse no taisnstūra d_1 × d_2)
un S = a · h (kā paralelogramam). No abām kopā atrod augstumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā aprēķina romba laukumu?"

MERKIS = ("Lietosim romba laukuma formulu ar diagonālēm un ar malu un "
          "augstumu.")

SATURS = [
    Sakums("Kāpēc rombs ir puse no taisnstūra?",
           zimejums=geometrija([("A", 0, 2), ("B", 3, 0, 270), ("C", 6, 2),
                                ("D", 3, 4, 90), ("_1", 0, 0), ("_2", 6, 0),
                                ("_3", 6, 4), ("_4", 0, 4)],
                               nogriezni=[("_1", "_2"), ("_2", "_3"),
                                          ("_3", "_4"), ("_4", "_1"),
                                          "AB", "BC", "CD", "DA", "AC",
                                          "BD"],
                               iekrasot=[("ABCD", 0)]),
           paraksts="Rombs aizņem tieši pusi no taisnstūra d_1 × d_2.",
           fakti=["S = {d_1 · d_2|2}.",
                  "Kā paralelogramam: S = a · h.",
                  "Abas formulas dod vienu laukumu."]),

    Doma("Divas formulas",
         "Ar diagonālēm - puse no reizinājuma; ar malu - mala reiz "
         "augstums.",
         soli=[
             "Diagonāles sadala rombu četros vienādos trijstūros.",
             "Taisnstūrī ap rombu ir vēl četri tādi paši trijstūri.",
             "Tātad S = {d_1 · d_2|2}.",
             "Ja zināma mala un augstums: S = a · h.",
         ]),

    Paraugs("Augstums no diagonālēm",
            uzd="Romba diagonāles ir 10 cm un 24 cm, mala - 13 cm. Atrodi "
                "laukumu un augstumu.",
            soli=[
                ("S = {10 · 24|2} = 120 cm²", "Diagonāles."),
                ("13 · h = 120", "S = a · h."),
                ("h = {120|13} ≈ 9,2 cm", "Atrisina."),
            ],
            atbilde="120 cm², h ≈ 9,2 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Diagonāles 6 un 8. S?", "atb": ["24"],
         "padoms": "{48|2}."},
        {"jaut": "Diagonāles 10 un 4. S?", "atb": ["20"],
         "padoms": "{40|2}."},
        {"jaut": "S = 30, viena diagonāle 12. Otra?", "atb": ["5"],
         "padoms": "d_1 · d_2 = 60."},
        {"jaut": "Mala 5, augstums 4. S?", "atb": ["20"], "padoms": "5 · 4."},
        {"jaut": "S = 40, mala 8. Augstums?", "atb": ["5"],
         "padoms": "40 : 8."},
        {"jaut": "Kvadrāta diagonāle 6. S?", "atb": ["18"],
         "padoms": "Kvadrāts ir rombs: {36|2}."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Cik vienādos trijstūros diagonāles sadala rombu?",
         "opcijas": ["4", "2", "3", "8"],
         "pareizi": 0, "padoms": "Taisnleņķa trijstūri pie O."},
        {"jaut": "Divkāršojot abas diagonāles, laukums...",
         "opcijas": ["četrkāršojas", "divkāršojas", "nemainās",
                     "astoņkāršojas"],
         "pareizi": 0, "padoms": "2 · 2."},
        {"jaut": "Vai formula {d_1 · d_2|2} der paralelogramam?",
         "opcijas": ["Nē - tikai rombam (un kvadrātam)", "Jā, vienmēr",
                     "Tikai taisnstūrim", "Tikai trapecei"],
         "pareizi": 0, "padoms": "Vajag perpendikulāras diagonāles."},
    ]),

    Pasaule("Rombveida pūķis",
            Ievadi("", [
                {"jaut": "Pūķa šķērskoki (diagonāles) ir 80 cm un 50 cm. "
                         "Auduma laukums (cm²)?",
                 "atb": ["2000"], "padoms": "{80 · 50|2}."},
                {"jaut": "Cik dm² tas ir?", "atb": ["20"],
                 "padoms": "1 dm² = 100 cm²."},
                {"jaut": "Abus šķērskokus pagarina par 10 %. Cik reizes "
                         "palielinās laukums?",
                 "atb": ["1,21"], "padoms": "1,1 · 1,1."},
            ]),
            pavediens="sports",
            konteksts="Pūķa šķērskoki ir romba diagonāles - pēc tiem rēķina "
                      "audumu.",
            kapec="Romba laukums ir puse no diagonāļu reizinājuma."),

    Kopsavilkums([
        "Aprēķinu romba laukumu ar diagonālēm.",
        "Aprēķinu romba laukumu ar malu un augstumu.",
        "No laukuma atrodu diagonāli vai augstumu.",
    ]),

    Majas([
        "Izgriez rombu no taisnstūra 10 × 6 cm un pārbaudi, ka tas ir puse.",
        "Izmēri romba formas priekšmeta diagonāles un aprēķini laukumu.",
        "Aprēķini tā paša romba laukumu ar malu un augstumu.",
    ]),
]
