# -*- coding: utf-8 -*-
"""3. klase, 63. stunda: «Kā skaitli pierakstīt kā summu?»

Izvērstā forma ir vietu tabula, pierakstīta ar zīmēm: 605 = 600 + 5 =
6 · 100 + 5. No šī pieraksta vēlāk aug gan saskaitīšana stabiņā, gan
reizināšana pa daļām - tāpēc te to raksta abos veidos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā skaitli pierakstīt kā summu?"

MERKIS = ("Pierakstīsim skaitli izvērstā formā: 605 = 600 + 5 = "
          "6 · 100 + 5.")

SATURS = [
    Sakums("Kā skaitli izjaukt pa gabaliem?",
           zimejums=restis([[605, "=", 600, "+", 5],
                            ["", "=", "6 · 100", "+", 5]],
                           "izvērstā forma"),
           paraksts="Katrs cipars kļūst par savu gabalu.",
           fakti=["Izvērstā forma parāda, cik ir katras vietas vienību.",
                  "Ja vietā ir nulle, tās gabalu neraksta."]),

    Doma("Skaitlis ir savu vietu summa",
         "1740 = 1000 + 700 + 40 = 1 · 1000 + 7 · 100 + 4 · 10.",
         soli=[
             "Pieraksti skaitli vietu tabulā.",
             "Katram ciparam pieraksti tā vērtību.",
             "Saskaiti visas vērtības ar «+».",
             "Pārraksti to pašu kā reizinājumu summu.",
         ],
         pieze="Nulles vietu izlaiž: 2008 = 2000 + 8, nevis "
               "2000 + 0 + 0 + 8. Nulle summai neko nepieliek."),

    Paraugs("Kā izvērst 1740?",
            uzd="Pieraksti skaitli 1740 izvērstā formā abos veidos.",
            soli=[
                ("1740 = 1000 + 700 + 40",
                 "Katras vietas vērtība atsevišķi; vienu vietā ir nulle."),
                ("1740 = 1 · 1000 + 7 · 100 + 4 · 10",
                 "Tas pats, pierakstīts ar reizinājumiem."),
                ("Pārbaude: 1000 + 700 + 40 = 1740",
                 "Saskaitot atpakaļ, sanāk sākotnējais skaitlis."),
            ],
            atbilde="1000 + 700 + 40"),

    Ievadi("Saskaiti atpakaļ", [
        {"jaut": "600 + 5 = ?", "atb": ["605"], "padoms": "Desmitu nav."},
        {"jaut": "2000 + 300 + 40 + 7 = ?", "atb": ["2347"],
         "padoms": "Katram gabalam sava vieta."},
        {"jaut": "1000 + 50 = ?", "atb": ["1050"],
         "padoms": "Simtu vietā ir nulle."},
        {"jaut": "4 · 100 + 9 = ?", "atb": ["409"],
         "padoms": "400 + 9."},
        {"jaut": "3 · 1000 + 2 · 10 = ?", "atb": ["3020"],
         "padoms": "3000 + 20."},
        {"jaut": "5 · 1000 + 5 · 100 + 5 = ?", "atb": ["5505"],
         "padoms": "5000 + 500 + 5."},
    ], pamats=4),

    Zimejums("Divi pieraksti vienam skaitlim",
             restis([["2347", "=", "2000 + 300 + 40 + 7"],
                     ["", "=", "2 · 1000 + 3 · 100 + 4 · 10 + 7"]],
                    "izvērstā forma"),
             paskaidro="Otrais pieraksts uzreiz parāda, cik ir tūkstošu, "
                       "simtu un desmitu.",
             ievads="Abi pieraksti stāsta vienu un to pašu."),

    Varianti("Kurš pieraksts ir pareizs?", [
        {"jaut": "Kā izvērst 308?",
         "opcijas": ["300 + 8", "30 + 8", "300 + 0 + 8 + 0", "3 + 0 + 8"],
         "pareizi": 0, "padoms": "Desmitu vietā ir nulle."},
        {"jaut": "Kurš skaitlis ir 4 · 1000 + 6 · 10?",
         "opcijas": ["4060", "4600", "460", "40060"],
         "pareizi": 0, "padoms": "4000 + 60."},
        {"jaut": "Kā izvērst 5000?",
         "opcijas": ["5 · 1000", "5 + 1000", "50 · 100", "500 + 0"],
         "pareizi": 0, "padoms": "Pieci tūkstoši."},
        {"jaut": "Kurš pieraksts *nav* pareizs skaitlim 720?",
         "opcijas": ["7 + 2 + 0", "700 + 20", "7 · 100 + 2 · 10",
                     "700 + 20 + 0"],
         "pareizi": 0, "padoms": "Cipari paši nav to vērtības."},
    ], pamats=4),

    Pasaule("Cik kilometru ir katrā posmā?",
            Ievadi("", [
                {"jaut": "Ceļš ir 1200 + 300 + 50 km. Cik kilometru kopā?",
                 "atb": ["1550"], "padoms": "1200 + 350."},
                {"jaut": "Pirmais posms 800 km, otrais 400 km. Cik kopā?",
                 "atb": ["1200"], "padoms": "800 + 400."},
                {"jaut": "Izvērs skaitli 2050: cik tūkstošu tajā ir?",
                 "atb": ["2"], "padoms": "2 · 1000."},
                {"jaut": "Cik desmitu ir skaitlī 2050?",
                 "atb": ["5"], "padoms": "5 · 10 = 50."},
            ]),
            pavediens="celojums",
            konteksts="Garu ceļu sadala posmos, un katrs posms ir savs "
                      "skaitlis - gluži kā izvērstajā formā.",
            kapec="Kad ceļš ir sadalīts, viegli pateikt, cik vēl atlicis."),

    Kopsavilkums([
        "Pierakstu skaitli izvērstā formā ar summu.",
        "Pierakstu to pašu ar reizinājumiem.",
        "Zinu, ka nulles vietu summā neraksta.",
        "Saskaitu izvērsto formu atpakaļ un pārbaudu skaitli.",
    ]),

    Majas([
        "Izvērs trīs skaitļus: 407, 1260 un 3009.",
        "Saskaiti tos atpakaļ un pārbaudi.",
        "Uzraksti izvērstā formā savu mājas numuru vai pasta indeksu.",
    ]),
]
