# -*- coding: utf-8 -*-
"""3. klase, 137. stunda: «Kāpēc izdevīgi rakstīt vienu zem otra?»

Pieraksts stabiņā nav jauns rēķins - tas ir tas pats saskaitīšana pa vietām,
tikai pierakstīta tā, ka vietas sakrīt pašas. Tieši tāpēc svarīgākais
noteikums ir pareiza cipara zem cipara novietošana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāpēc izdevīgi rakstīt vienu zem otra?"

MERKIS = ("Veidosim saskaitīšanas pierakstu stabiņā un skaidrosim katru "
          "soli.")

SATURS = [
    Sakums("Kāpēc skaitļus raksta vienu zem otra?",
           zimejums=restis([["", 3, 4, 2],
                            ["+", 2, 1, 5],
                            ["", 5, 5, 7]],
                           "342 + 215"),
           paraksts="Vieni zem vieniem, desmiti zem desmitiem.",
           fakti=["Stabiņā vietas sakrīt pašas.",
                  "Saskaitīšanu sāk no vieniem, nevis no simtiem."]),

    Doma("Cipars zem cipara, saskaitīšana no labās",
         "Stabiņā katra vieta stāv savā kolonnā, tāpēc saskaitīt var pa "
         "vienai kolonnai.",
         soli=[
             "Uzraksti otru skaitli zem pirmā tā, lai vieni būtu zem vieniem.",
             "Velc svītru un sāc saskaitīt no labās puses.",
             "Saskaiti vienus, tad desmitus, tad simtus.",
             "Katras kolonnas rezultātu raksti zem svītras.",
         ],
         pieze="Galvā rēķina no simtiem, bet stabiņā - no vieniem: tikai tā "
               "zina, vai kolonnā rodas pārnesums."),

    Paraugs("Kā saskaitīt stabiņā?",
            uzd="Saskaiti stabiņā 342 + 215.",
            soli=[
                ("Vieni: 2 + 5 = 7",
                 "Sāk no labās kolonnas."),
                ("Desmiti: 4 + 1 = 5",
                 "Otrā kolonna."),
                ("Simti: 3 + 2 = 5",
                 "Trešā kolonna; atbilde ir 557."),
            ],
            atbilde="557"),

    Ievadi("Saskaiti stabiņā", [
        {"jaut": "342 + 215 = ?", "atb": ["557"], "padoms": "Pa kolonnām."},
        {"jaut": "531 + 246 = ?", "atb": ["777"], "padoms": "Pa kolonnām."},
        {"jaut": "204 + 693 = ?", "atb": ["897"], "padoms": "Pa kolonnām."},
        {"jaut": "415 + 362 = ?", "atb": ["777"], "padoms": "Pa kolonnām."},
        {"jaut": "126 + 351 = ?", "atb": ["477"], "padoms": "Pa kolonnām."},
        {"jaut": "703 + 205 = ?", "atb": ["908"], "padoms": "Pa kolonnām."},
    ], pamats=4,
        ievads="Uzraksti katru piemēru burtnīcā stabiņā un ieraksti atbildi."),

    Zimejums("Kur cipari stāv nepareizi",
             restis([["nepareizi", "pareizi"],
                     ["342", "342"],
                     ["+ 21", "+ 021"]],
                    "vietām jāsakrīt"),
             paskaidro="Ja cipari nav savās kolonnās, saskaitās nepareizās "
                       "vietas - desmiti pie vieniem.",
             ievads="Biežākā kļūda pierakstā stabiņā."),

    Varianti("Kā pareizi rakstīt?", [
        {"jaut": "No kuras puses sāk saskaitīt stabiņā?",
         "opcijas": ["No labās", "No kreisās", "No vidus", "Vienalga"],
         "pareizi": 0, "padoms": "Vispirms vieni."},
        {"jaut": "Kas jāsakrīt, rakstot vienu zem otra?",
         "opcijas": ["Vietas", "Ciparu skaits", "Pirmie cipari",
                     "Nekas"],
         "pareizi": 0, "padoms": "Vieni zem vieniem."},
        {"jaut": "Cik ir 250 + 316?",
         "opcijas": ["566", "556", "666", "576"],
         "pareizi": 0, "padoms": "Pa kolonnām."},
        {"jaut": "Kāpēc stabiņš ir ērts?",
         "opcijas": ["Vietas sakrīt pašas", "Tas ir skaistāks",
                     "Tas ir ātrāks par galvu", "Tas nav ērts"],
         "pareizi": 0, "padoms": "Nav jādomā par vietu nosaukumiem."},
    ], pamats=4),

    Pasaule("Cik kilometru ir maršrutā?",
            Ievadi("", [
                {"jaut": "Posmi 342 km un 215 km. Cik kopā?", "atb": ["557"],
                 "padoms": "Stabiņā."},
                {"jaut": "Vēl viens posms 231 km. Cik kopā?", "atb": ["788"],
                 "padoms": "557 + 231."},
                {"jaut": "Atpakaļceļš ir tāds pats. Cik kilometru turp un "
                         "atpakaļ?",
                 "atb": ["1576"], "padoms": "2 · 788."},
                {"jaut": "Par cik kilometriem garākais posms ir garāks par īsāko?",
                 "atb": ["127"], "padoms": "342 − 215."},
            ]),
            pavediens="celojums",
            konteksts="Maršruta posmus saskaita pa vienam - un garā sarakstā "
                      "stabiņš ir drošāks par galvu.",
            kapec="Stabiņā katrs solis paliek redzams, tāpēc kļūdu var "
                  "atrast."),

    Kopsavilkums([
        "Veidoju saskaitīšanas pierakstu stabiņā.",
        "Rakstu ciparus savās kolonnās.",
        "Saskaitu no labās puses.",
        "Skaidroju katru soli.",
    ]),

    Majas([
        "Uzraksti stabiņā un izrēķini 423 + 265 un 507 + 391.",
        "Pārbaudi abas atbildes ar galvas rēķinu.",
        "Atrodi kļūdu pierakstā, kurā cipari nav savās kolonnās.",
    ]),
]
