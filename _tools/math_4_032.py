# -*- coding: utf-8 -*-
"""4. klase, 32. stunda: «Kā dalīt, ja jāsadala desmits?»

85 : 5 - astoņi desmiti nedalās ar 5 bez atlikuma. Vienu desmitu vai
vairākus pārvērš vienos: 85 = 50 + 35. Galvenais paņēmiens - izteikt
dalāmo kā summu, kurā katrs saskaitāmais dalās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā dalīt, ja jāsadala desmits?"

MERKIS = ("Dalīsim ar pāreju citā šķirā, piemēram, 85 : 5, un "
          "paskaidrosim savu paņēmienu.")

SATURS = [
    Sakums("5 draugi un 85 €: 8 desmitnieki - kā dalīt?",
           zimejums=restis([["85", "=", "50", "+", "35"],
                            [": 5", "", "10", "+", "7"]],
                           "sadala tā, lai katra daļa dalās"),
           paraksts="85 : 5 = 10 + 7 = 17.",
           fakti=["8 desmitniekus uz 5 nevar sadalīt vienādi.",
                  "3 desmitniekus samaina vienniekos - un var."]),

    Doma("Izsaki dalāmo kā summu, kurā katrs gabals dalās",
         "Paņem lielāko pilno desmitu skaitu, kas dalās ar dalītāju; atlikušo "
         "daļu dali atsevišķi.",
         soli=[
             "Cik pilnu desmitu var sadalīt? 85 : 5 → 50 (5 desmiti).",
             "Atlikušais: 85 − 50 = 35.",
             "Dali abus: 50 : 5 = 10, 35 : 5 = 7.",
             "Saskaiti: 10 + 7 = 17. Pārbaude: 17 · 5 = 85.",
         ],
         pieze="Var arī citādi: 85 = 80 + 5 neder (80 : 5 nav tabulā), bet "
               "85 = 40 + 45 der: 8 + 9 = 17."),

    Paraugs("72 : 4",
            uzd="Izrēķini 72 : 4.",
            soli=[
                ("72 = 40 + 32", "40 un 32 abi dalās ar 4."),
                ("40 : 4 = 10", None),
                ("32 : 4 = 8", None),
                ("10 + 8 = 18", "Pārbaude: 18 · 4 = 72."),
            ],
            atbilde="18"),

    Slidnis("Kā sadalīt 96 : 6",
            soli=[
                {"v": "96 : 6", "teksts": "9 desmiti nedalās ar 6 bez "
                 "atlikuma."},
                {"v": "96 = 60 + 36", "teksts": "Paņem 6 desmitus, atliek 36."},
                {"v": "60 : 6 + 36 : 6", "teksts": "Abi dalās."},
                {"v": "10 + 6 = 16", "teksts": "Gatavs. 16 · 6 = 96."},
            ]),

    Ievadi("Ar pāreju", [
        {"jaut": "85 : 5 = ?", "atb": ["17"], "padoms": "50 + 35."},
        {"jaut": "72 : 3 = ?", "atb": ["24"], "padoms": "60 + 12."},
        {"jaut": "56 : 4 = ?", "atb": ["14"], "padoms": "40 + 16."},
        {"jaut": "91 : 7 = ?", "atb": ["13"], "padoms": "70 + 21."},
        {"jaut": "78 : 6 = ?", "atb": ["13"], "padoms": "60 + 18."},
        {"jaut": "98 : 7 = ?", "atb": ["14"], "padoms": "70 + 28."},
        {"jaut": "54 : 3 = ?", "atb": ["18"], "padoms": "30 + 24."},
        {"jaut": "76 : 2 = ?", "atb": ["38"], "padoms": "60 + 16."},
    ], pamats=6),

    Varianti("Kura summa der?", [
        {"jaut": "Kā sadalīt 64, lai dalītu ar 4?",
         "opcijas": ["40 + 24", "60 + 4", "50 + 14", "30 + 34"],
         "pareizi": 0, "padoms": "Abi saskaitāmie dalās ar 4."},
        {"jaut": "Kā sadalīt 84, lai dalītu ar 7?",
         "opcijas": ["70 + 14", "80 + 4", "60 + 24", "40 + 44"],
         "pareizi": 0, "padoms": "70 : 7 = 10, 14 : 7 = 2."},
        {"jaut": "Cik ir 84 : 7?",
         "opcijas": ["12", "14", "11", "13"], "pareizi": 0,
         "padoms": "10 + 2."},
    ]),

    Pasaule("Sporta komandu izloze",
            Ievadi("", [
                {"jaut": "Turnīrā 96 spēlētāji sadalās 8 komandās. Cik "
                         "spēlētāju komandā?",
                 "atb": ["12"], "padoms": "80 + 16."},
                {"jaut": "75 bumbas sadala 5 laukumos vienādi. Cik bumbu "
                         "katrā laukumā?",
                 "atb": ["15"], "padoms": "50 + 25."},
                {"jaut": "Stafetes 72 dalībnieki - komandās pa 4. Cik "
                         "komandu?",
                 "atb": ["18"], "padoms": "72 : 4."},
                {"jaut": "Ūdens 84 pudeles - 6 komandām vienādi. Cik katrai?",
                 "atb": ["14"], "padoms": "60 + 24."},
            ]),
            pavediens="sports",
            konteksts="Sporta dienā visi jāsadala godīgi - komandas, bumbas "
                      "un ūdens.",
            kapec="Kas prot sadalīt desmitu, tas sadala jebkuru skaitli."),

    Kopsavilkums([
        "Dalu ar pāreju citā šķirā.",
        "Izsaku dalāmo kā ērtu summu.",
        "Paskaidroju savu paņēmienu un pārbaudu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini 90 : 6 divos dažādos veidos.",
        "Izdomā uzdevumu, kurā jāsadala 78 konfektes 6 bērniem.",
        "Paskaidro mājiniekiem, kā dalīji 85 : 5.",
    ]),
]
