# -*- coding: utf-8 -*-
"""3. klase, 39. stunda: «Kura darbība ir pirmā?»

Darbību secība ir vienošanās, bez kuras viena izteiksme nozīmētu dažādas
lietas dažādiem cilvēkiem. Tieši tā to te arī pasniedz: nevis kā likumu, ko
iekalt, bet kā noteikumu, par kuru pasaule ir vienojusies - arī kalkulatori.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kura darbība ir pirmā?"

MERKIS = ("Noteiksim darbību secību: vispirms iekavas, tad reizināšana un "
          "dalīšana, tad saskaitīšana un atņemšana.")

SATURS = [
    Sakums("Cik ir 2 + 3 · 4?",
           zimejums=restis([["2 + 3 · 4"],
                            ["= 2 + 12 = 14"],
                            ["= 5 · 4 = 20"]],
                           "divas atbildes vienai izteiksmei"),
           paraksts="Pareiza ir tikai viena - tā, kas ievēro darbību secību.",
           fakti=["Bez vienošanās viena izteiksme nozīmētu divas lietas.",
                  "Visā pasaulē reizina pirms saskaitīšanas.",
                  "Arī kalkulators ievēro šo pašu secību."]),

    Doma("Vispirms iekavas, tad reizināšana, tad saskaitīšana",
         "Darbību secība ir trīs pakāpieni: ( ), tad · un :, tad + un −.",
         soli=[
             "Vispirms izpildi visu, kas ir iekavās.",
             "Tad reizināšanu un dalīšanu - pēc kārtas no kreisās puses.",
             "Tad saskaitīšanu un atņemšanu - arī no kreisās puses.",
             "Katrā solī pārraksti izteiksmi no jauna.",
         ],
         pieze="Reizināšana un dalīšana ir vienā pakāpienā: 12 : 3 · 2 rēķina "
               "no kreisās - vispirms 12 : 3 = 4, tad 4 · 2 = 8."),

    Slidnis("Kā rēķina 2 + 3 · 4",
            soli=[
                {"v": "2 + 3 · 4", "teksts": "Izteiksme, kā tā uzrakstīta.",
                 "josla": 20},
                {"v": "3 · 4 = 12", "teksts": "Vispirms reizināšana.",
                 "josla": 60},
                {"v": "2 + 12 = 14", "teksts": "Tikai tad saskaitīšana.",
                 "josla": 100},
            ],
            ievads="Spied soļus un skaties, kura darbība notiek pirmā."),

    Paraugs("Cik ir 20 − 2 · 6?",
            uzd="Aprēķini izteiksmes 20 − 2 · 6 vērtību.",
            soli=[
                ("2 · 6 = 12",
                 "Reizināšana ir augstākā pakāpiena darbība."),
                ("20 − 12 = 8",
                 "Tikai tad atņemšana."),
                ("20 − 2 · 6 = 8",
                 "Pieraksta pilnu atbildi."),
            ],
            atbilde="8"),

    Ievadi("Ievēro secību", [
        {"jaut": "5 + 2 · 3 = ?", "atb": ["11"], "padoms": "Vispirms 2 · 3."},
        {"jaut": "20 − 3 · 4 = ?", "atb": ["8"], "padoms": "Vispirms 3 · 4."},
        {"jaut": "12 : 4 + 7 = ?", "atb": ["10"],
         "padoms": "Vispirms 12 : 4."},
        {"jaut": "6 · 3 − 8 = ?", "atb": ["10"], "padoms": "Vispirms 6 · 3."},
        {"jaut": "24 : 6 · 2 = ?", "atb": ["8"],
         "padoms": "No kreisās: vispirms 24 : 6."},
        {"jaut": "9 + 4 · 5 = ?", "atb": ["29"], "padoms": "Vispirms 4 · 5."},
    ], pamats=4),

    Zimejums("Trīs pakāpieni",
             restis([["1.", "iekavas ( )"],
                     ["2.", "reizināšana · un dalīšana :"],
                     ["3.", "saskaitīšana + un atņemšana −"]],
                    "darbību secība"),
             paskaidro="Vienā pakāpienā esošās darbības izpilda pēc kārtas no "
                       "kreisās puses.",
             ievads="Šo tabulu vērts uzrakstīt burtnīcas pirmajā lappusē."),

    Varianti("Kura darbība pirmā?", [
        {"jaut": "Kura darbība ir pirmā izteiksmē 7 + 5 · 2?",
         "opcijas": ["Reizināšana", "Saskaitīšana", "Abas reizē",
                     "Vienalga"],
         "pareizi": 0, "padoms": "Reizināšana ir augstākā pakāpienā."},
        {"jaut": "Cik ir 10 − 6 : 2?",
         "opcijas": ["7", "2", "8", "5"],
         "pareizi": 0, "padoms": "Vispirms 6 : 2 = 3."},
        {"jaut": "Kura darbība ir pirmā izteiksmē 18 : 3 · 2?",
         "opcijas": ["Dalīšana", "Reizināšana", "Abas reizē", "Vienalga"],
         "pareizi": 0, "padoms": "Vienā pakāpienā - no kreisās puses."},
        {"jaut": "Cik ir 4 · 5 − 12 : 4?",
         "opcijas": ["17", "2", "8", "20"],
         "pareizi": 0, "padoms": "20 − 3."},
    ], pamats=4),

    Pasaule("Cik vietas aizņem faili?",
            Ievadi("", [
                {"jaut": "Telefonā ir 5 video pa 8 MB un vēl 12 MB mūzikas. "
                         "Cik MB kopā? (5 · 8 + 12)",
                 "atb": ["52"], "padoms": "Vispirms 5 · 8."},
                {"jaut": "Atmiņā ir 100 MB. Cik MB brīvi? (100 − 5 · 8)",
                 "atb": ["60"], "padoms": "Vispirms 5 · 8 = 40."},
                {"jaut": "6 attēlus pa 3 MB izdzēsa no 40 MB mapes. Cik "
                         "palika? (40 − 6 · 3)",
                 "atb": ["22"], "padoms": "Vispirms 6 · 3 = 18."},
                {"jaut": "24 MB sadalīja 4 mapēs un pievienoja vēl 5 MB. "
                         "(24 : 4 + 5)",
                 "atb": ["11"], "padoms": "Vispirms 24 : 4 = 6."},
            ]),
            pavediens="dati",
            konteksts="Telefona atmiņu rēķina tieši tā: vispirms reizina "
                      "failu skaitu ar izmēru, tad saskaita.",
            kapec="Ja secību sajauc, atbilde par brīvo vietu ir pilnīgi "
                  "cita."),

    Kopsavilkums([
        "Zinu darbību secību: iekavas, reizināšana un dalīšana, "
        "saskaitīšana un atņemšana.",
        "Aprēķinu izteiksmi pa soļiem, katru reizi pārrakstot.",
        "Zinu, ka vienā pakāpienā darbības izpilda no kreisās puses.",
        "Saprotu, kāpēc šāda vienošanās ir vajadzīga.",
    ]),

    Majas([
        "Aprēķini 3 + 4 · 5, 30 − 12 : 3 un 2 · 6 + 3 · 4.",
        "Pārbaudi savas atbildes ar kalkulatoru.",
        "Uzraksti darbību secības tabulu burtnīcas pirmajā lappusē.",
    ]),
]
