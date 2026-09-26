# -*- coding: utf-8 -*-
"""4. klase, 13. stunda: «Kā saskaitīt rakstos?»

Stabiņš līdz 10 000 ir tas pats stabiņš, kas līdz 1000, tikai ar vēl vienu
šķiru. Galvenais - komentēt katru soli skaļi: «septiņi plus pieci ir
divpadsmit, divi rakstu, vienu paturu prātā».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā saskaitīt rakstos?"

MERKIS = ("Saskaitīsim un atņemsim četrciparu skaitļus rakstos un "
          "komentēsim katru darbības soli.")

SATURS = [
    Sakums("Cik km nobrauca autobuss?",
           zimejums=restis([["", "T", "S", "D", "V"],
                            ["", 2, 4, 5, 7],
                            ["+", 3, 8, 6, 5],
                            ["=", 6, 3, 2, 2]],
                           "2457 km + 3865 km"),
           paraksts="Stabiņā katra šķira stāv savā kolonnā.",
           fakti=["Pirmdien autobuss nobrauca 2457 km, otrdien 3865 km.",
                  "Galvā to ir grūti - rakstos droši."]),

    Doma("Vieni zem vieniem, un sāc no labās",
         "Stabiņā saskaita katru šķiru atsevišķi; ja sanāk 10 vai vairāk, "
         "vienu pārnes uz nākamo šķiru.",
         soli=[
             "Raksti skaitļus tā, lai šķiras stāv cita zem citas.",
             "Saskaiti vienus; ja ≥ 10, raksti vienus, desmitu pārnes.",
             "Tāpat desmitus, simtus un tūkstošus, pieskaitot pārnesto.",
             "Pārbaudi ar aptuvenu rēķinu: 2500 + 3900 ≈ 6400.",
         ],
         pieze="Komentē skaļi - tā pamanīsi aizmirstu pārnesumu."),

    Paraugs("2457 + 3865",
            uzd="Saskaiti rakstos 2457 + 3865.",
            soli=[
                ("7 + 5 = 12", "Raksta 2, 1 pārnes uz desmitiem."),
                ("5 + 6 + 1 = 12", "Raksta 2, 1 pārnes uz simtiem."),
                ("4 + 8 + 1 = 13", "Raksta 3, 1 pārnes uz tūkstošiem."),
                ("2 + 3 + 1 = 6", "Raksta 6."),
                ("2457 + 3865 = 6322", None),
            ],
            atbilde="6322 km"),

    Paraugs("6204 − 1578",
            uzd="Atņem rakstos 6204 − 1578.",
            soli=[
                ("14 − 8 = 6", "No 4 nevar atņemt 8 - aizņemas desmitu, bet "
                 "desmitu nav, tāpēc sadala simtu."),
                ("9 − 7 = 2", "No simta palika 9 desmiti."),
                ("11 − 5 = 6", "Simtos palika 1 - aizņemas tūkstoti."),
                ("5 − 1 = 4", "Tūkstošos palika 5."),
                ("6204 − 1578 = 4626", None),
            ],
            atbilde="4626"),

    Ievadi("Stabiņā", [
        {"jaut": "3426 + 2351 = ?", "atb": ["5777"],
         "padoms": "Pārnest nevajag."},
        {"jaut": "4589 + 2736 = ?", "atb": ["7325"],
         "padoms": "Pārnes trijās šķirās."},
        {"jaut": "8765 − 3421 = ?", "atb": ["5344"],
         "padoms": "Aizņemties nevajag."},
        {"jaut": "7032 − 2856 = ?", "atb": ["4176"],
         "padoms": "Desmitu nav daudz - aizņemies no simtiem."},
        {"jaut": "1999 + 2999 = ?", "atb": ["4998"],
         "padoms": "Vai: 2000 + 3000 − 2."},
        {"jaut": "5000 − 2468 = ?", "atb": ["2532"],
         "padoms": "Sadali tūkstoti: 4 T, 9 S, 9 D, 10 V."},
    ], pamats=4),

    Varianti("Atrodi kļūdu", [
        {"jaut": "Ieva: 3568 + 2745 = 5213. Kas nav kārtībā?",
         "opcijas": ["aizmirsa pārnesumus", "sajauca šķiras",
                     "viss pareizi"], "pareizi": 0,
         "padoms": "Pareizi ir 6313."},
        {"jaut": "Toms: 4000 − 1234 = 3234. Kas nav kārtībā?",
         "opcijas": ["no mazā cipara atņēma nulli", "viss pareizi",
                     "sajauca + un −"], "pareizi": 0,
         "padoms": "Pareizi ir 2766 - tūkstotis jāsadala."},
        {"jaut": "Kā pārbaudīt 6322 − 3865 = 2457?",
         "opcijas": ["2457 + 3865", "6322 + 3865", "2457 − 3865",
                     "6322 + 2457"], "pareizi": 0,
         "padoms": "Starpība + atņēmējs = mazināmais."},
        {"jaut": "Ja vienos 8 + 7, ko raksta vienu vietā?",
         "opcijas": ["5", "15", "1", "8"], "pareizi": 0,
         "padoms": "15 - raksta 5, desmitu pārnes."},
    ], pamats=4),

    Pasaule("Autobusa maršruts",
            Ievadi("", [
                {"jaut": "Maršruts Rīga-Parīze ir 1850 km, Parīze-Madride "
                         "1270 km. Cik km kopā?",
                 "atb": ["3120"], "padoms": "1850 + 1270."},
                {"jaut": "Atpakaļceļš ir tikpat garš. Cik km viss "
                         "brauciens?",
                 "atb": ["6240"], "padoms": "3120 + 3120."},
                {"jaut": "Autobusa odometrs pirms brauciena rādīja 3765 km. "
                         "Ko tas rādīs pēc 6240 km?",
                 "atb": ["10005", "10 005"], "padoms": "3765 + 6240."},
                {"jaut": "Cik km vēl atlikuši līdz Madridei, ja nobraukti "
                         "2486 km no 3120?",
                 "atb": ["634"], "padoms": "3120 − 2486."},
            ]),
            pavediens="celojums",
            konteksts="Autobusu kompānijas skaita tūkstošiem kilometru - "
                      "katrs brauciens ir stabiņa rēķins.",
            kapec="Rakstos var saskaitīt jebkurus skaitļus bez kļūdām."),

    Kopsavilkums([
        "Saskaitu četrciparu skaitļus stabiņā ar pārnešanu.",
        "Atņemu stabiņā, aizņemoties no nākamās šķiras.",
        "Komentēju katru soli.",
        "Pārbaudu atņemšanu ar saskaitīšanu.",
    ]),

    Majas([
        "Atrodi divu pilsētu attālumus līdz Rīgai un saskaiti tos stabiņā.",
        "Izdomā vienu stabiņu ar trim pārnesumiem un atrisini.",
        "Paskaidro mājiniekam, kā atņemt 5000 − 2468.",
    ]),
]
