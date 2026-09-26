# -*- coding: utf-8 -*-
"""4. klase, 17. stunda: «Kāda ir darbību secība?»

Mikrotemata noslēgums. Izteiksmē līdz četrām darbībām secību nosaka divi
noteikumi: vispirms iekavas, tad reizināšana un dalīšana, tad saskaitīšana
un atņemšana - no kreisās uz labo. Tas ir 9. klases eksāmena pamats, tāpēc
secību numurē virs zīmēm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kāda ir darbību secība?"

MERKIS = ("Aprēķināsim izteiksmes vērtību ar līdz četrām darbībām un "
          "iekavām, ievērojot darbību secību.")

SATURS = [
    Sakums("Vai 2 + 3 · 4 ir 20 vai 14?",
           zimejums=restis([["kārtība", "darbības"],
                            ["1.", "( )"],
                            ["2.", "· un :"],
                            ["3.", "+ un −"]],
                           "darbību secība"),
           paraksts="Pareizi ir 14: vispirms 3 · 4.",
           fakti=["Visā pasaulē ir viena vienošanās par darbību secību.",
                  "Tāpēc kalkulators un tu iegūstat to pašu atbildi."]),

    Doma("Iekavas, reizināšana un dalīšana, tad saskaitīšana un atņemšana",
         "Vienas pakāpes darbības izpilda no kreisās uz labo.",
         soli=[
             "Atrodi iekavas un izrēķini tās pirmās.",
             "Tad reizināšanu un dalīšanu no kreisās uz labo.",
             "Tad saskaitīšanu un atņemšanu no kreisās uz labo.",
             "Virs zīmēm uzraksti darbības numuru - tā neapjuksi.",
         ],
         pieze="1000 − 200 − 100 = 700, nevis 900: atņem no kreisās uz "
               "labo."),

    Slidnis("Soli pa solim: 5000 − (1200 + 800) · 2",
            soli=[
                {"v": "5000 − (1200 + 800) · 2", "teksts": "Sākums."},
                {"v": "5000 − 2000 · 2", "teksts": "1. Iekavas: "
                 "1200 + 800 = 2000."},
                {"v": "5000 − 4000", "teksts": "2. Reizināšana: "
                 "2000 · 2 = 4000."},
                {"v": "1000", "teksts": "3. Atņemšana - gatavs!"},
            ],
            ievads="Katrā solī izpilda tikai vienu darbību."),

    Paraugs("300 + 600 : 3 − 50",
            uzd="Aprēķini 300 + 600 : 3 − 50.",
            soli=[
                ("600 : 3 = 200", "1. dalīšana."),
                ("300 + 200 = 500", "2. saskaitīšana (no kreisās)."),
                ("500 − 50 = 450", "3. atņemšana."),
            ],
            atbilde="450"),

    Ievadi("Izrēķini", [
        {"jaut": "2 + 3 · 4 = ?", "atb": ["14"], "padoms": "Vispirms 3 · 4."},
        {"jaut": "(2 + 3) · 4 = ?", "atb": ["20"],
         "padoms": "Vispirms iekavas."},
        {"jaut": "1000 − 200 − 100 = ?", "atb": ["700"],
         "padoms": "No kreisās uz labo."},
        {"jaut": "4000 − 800 : 4 = ?", "atb": ["3800"],
         "padoms": "Vispirms 800 : 4."},
        {"jaut": "(4000 − 800) : 4 = ?", "atb": ["800"],
         "padoms": "Vispirms iekavas: 3200."},
        {"jaut": "60 : 6 · 2 = ?", "atb": ["20"],
         "padoms": "No kreisās: 60 : 6 = 10."},
        {"jaut": "2500 + 500 · 3 − 1000 = ?", "atb": ["3000"],
         "padoms": "500 · 3 = 1500."},
        {"jaut": "(7 + 3) · (100 − 20) = ?", "atb": ["800"],
         "padoms": "10 · 80."},
    ], pamats=6),

    Varianti("Kura darbība pirmā?", [
        {"jaut": "450 − 50 · 3", "opcijas": ["50 · 3", "450 − 50"],
         "pareizi": 0, "padoms": "Reizināšana pirms atņemšanas."},
        {"jaut": "(450 − 50) · 3", "opcijas": ["450 − 50", "50 · 3"],
         "pareizi": 0, "padoms": "Iekavas vispirms."},
        {"jaut": "80 : 4 : 2", "opcijas": ["80 : 4", "4 : 2"],
         "pareizi": 0, "padoms": "No kreisās uz labo."},
        {"jaut": "Kur jāliek iekavas, lai 10 − 4 − 2 = 8?",
         "opcijas": ["10 − (4 − 2)", "(10 − 4) − 2", "iekavas nevajag"],
         "pareizi": 0, "padoms": "10 − 2 = 8."},
    ], pamats=4),

    Pasaule("Kinoteātra rēķins",
            Ievadi("", [
                {"jaut": "4 biļetes pa 8 € un popkorns 6 €. Izteiksme: "
                         "4 · 8 + 6. Cik kopā?",
                 "atb": ["38"], "padoms": "32 + 6."},
                {"jaut": "Ģimene maksāja ar 50 €. Izteiksme: "
                         "50 − (4 · 8 + 6). Cik atdod?",
                 "atb": ["12"], "padoms": "50 − 38."},
                {"jaut": "Draugi dala 60 € rēķinu uz 4, katrs vēl pērk "
                         "dzērienu 2 €. 60 : 4 + 2 = ?",
                 "atb": ["17"], "padoms": "15 + 2."},
                {"jaut": "Zāle: 12 rindas pa 25 vietām, 48 aizņemtas. "
                         "12 · 25 − 48 = ?",
                 "atb": ["252"], "padoms": "300 − 48."},
            ]),
            pavediens="veikals",
            konteksts="Kasē izteiksmi neraksta, bet kase to rēķina tieši "
                      "pareizajā secībā.",
            kapec="Pareiza secība ir starpība starp 38 € un 56 €."),

    Kopsavilkums([
        "Zinu darbību secību: iekavas, · un :, tad + un −.",
        "Vienas pakāpes darbības izpildu no kreisās uz labo.",
        "Numurēju darbības virs zīmēm.",
        "Izrēķinu izteiksmes ar līdz četrām darbībām.",
    ]),

    Majas([
        "Sastādi izteiksmi savam pusdienu rēķinam ar reizināšanu un "
        "saskaitīšanu.",
        "Pārbaudi kalkulatorā: vai tas rēķina 2 + 3 · 4 = 14?",
        "Izdomā izteiksmi, kurā iekavas maina atbildi.",
    ]),
]
