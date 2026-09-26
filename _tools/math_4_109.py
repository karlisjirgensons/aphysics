# -*- coding: utf-8 -*-
"""4. klase, 109. stunda: «Kur risinājumā kļūda?»

Kļūdu analīze: skolēns saņem aplamus risinājumus un paskaidro, kas
nav kārtībā. Tipiskās kļūdas - saskaitīti saucēji, atņemts no saucēja,
aizmirsts, ka {n|n} = 1. Paskaidrot kļūdu ir grūtāk nekā to neizdarīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kur risinājumā kļūda?"

MERKIS = ("Analizēsim dotu daļu saskaitīšanas risinājumu, pamatosim tā "
          "aplamību un ieteiksim labojumu.")

SATURS = [
    Sakums("Skolotāja sarkanais pildspalvas brīdis",
           zimejums=restis([["risinājums", "vai pareizi?"],
                            ["2/7 + 3/7 = 5/14", "nē"],
                            ["2/7 + 3/7 = 5/7", "jā"],
                            ["6/7 − 2/7 = 4/0", "nē"]],
                           "atrodi kļūdas"),
           fakti=["Visbiežākā kļūda - saskaitīt arī saucējus.",
                  "Kļūdu var pamanīt ar pārbaudi - vai atbilde saprātīga?"]),

    Doma("Pārbaudi ar modeli",
         "Aplamu risinājumu atmasko, salīdzinot atbildi ar zīmējumu vai "
         "spriedumu par lielumu.",
         soli=[
             "Izlasi risinājumu soli pa solim.",
             "Pārbaudi, vai saucējs palicis tas pats.",
             "Pārbaudi, vai summa ir lielāka par katru saskaitāmo.",
             "Uzraksti pareizo risinājumu un paskaidro atšķirību.",
         ],
         pieze="{2|7} + {3|7} = {5|14}? {5|14} ir mazāk nekā {2|7} - summa "
               "nevar būt mazāka par saskaitāmo!"),

    Paraugs("Analizē kļūdu",
            uzd="Juris: {5|6} − {1|6} = {4|0}. Kas nav kārtībā?",
            soli=[
                ("6 − 6 = 0", "Atņēma arī saucējus."),
                ("saucējs nevar būt 0", "Tas liecina par kļūdu."),
                ("{5|6} − {1|6} = {4|6}", "Pareizais risinājums."),
            ],
            atbilde="saucējs jāpatur 6: {4|6}"),

    Varianti("Kāda kļūda?", [
        {"jaut": "{3|10} + {4|10} = {7|20}",
         "opcijas": ["saskaitīti saucēji", "viss pareizi",
                     "nepareizi skaitītāji"], "pareizi": 0,
         "padoms": "Pareizi {7|10}."},
        {"jaut": "{5|8} + {3|8} = {8|8} = 8",
         "opcijas": ["{8|8} = 1, nevis 8", "viss pareizi",
                     "saskaitīti saucēji"], "pareizi": 0,
         "padoms": "Visas daļas ir veselais."},
        {"jaut": "1 − {2|5} = {1|5}",
         "opcijas": ["1 jāraksta kā {5|5}", "viss pareizi",
                     "saucējs nepareizs"], "pareizi": 0,
         "padoms": "{5|5} − {2|5} = {3|5}."},
        {"jaut": "{4|9} + {2|9} = {6|9}",
         "opcijas": ["viss pareizi", "saskaitīti saucēji",
                     "jābūt {6|18}"], "pareizi": 0,
         "padoms": "4 + 2 = 6, saucējs 9."},
    ], pamats=4),

    Ievadi("Labo kļūdu", [
        {"jaut": "{3|10} + {4|10} = ? (pareizi)", "atb": ["7/10"],
         "vieta": "piem., 1/2", "padoms": "Saucējs paliek."},
        {"jaut": "1 − {2|5} = ? (pareizi)", "atb": ["3/5"],
         "vieta": "piem., 1/2", "padoms": "{5|5} − {2|5}."},
        {"jaut": "{5|8} + {3|8} = ? (vesels skaitlis)", "atb": ["1"],
         "padoms": "{8|8}."},
        {"jaut": "{7|12} − {7|12} = ?", "atb": ["0"],
         "padoms": "Nekas nepaliek."},
    ]),

    Pasaule("Kafejnīcas čeks",
            Varianti("", [
                {"jaut": "Viesmīlis: galdam A pica {3|8}, galdam B {2|8}. "
                         "«Kopā {5|16} picas.» Kļūda?",
                 "opcijas": ["jā, pareizi {5|8}", "nē, pareizi",
                             "pareizi {6|8}"], "pareizi": 0,
                 "padoms": "Saucējs paliek 8."},
                {"jaut": "«Kūka {4|6} apēsta, palika {2|0}.» Kļūda?",
                 "opcijas": ["jā, palika {2|6}", "nē", "palika {4|6}"],
                 "pareizi": 0, "padoms": "Saucējs nevar būt 0."},
                {"jaut": "«Pārdots {6|6} tortes - tas ir 6 tortes.» Kļūda?",
                 "opcijas": ["jā, tā ir 1 torte", "nē", "tās ir 0 tortes"],
                 "pareizi": 0, "padoms": "{6|6} = 1."},
            ]),
            pavediens="virtuve",
            konteksts="Kafejnīcā kļūdains aprēķins nozīmē nepareizu rēķinu "
                      "klientam.",
            kapec="Kas atrod kļūdu, tas saprot matemātiku dziļāk."),

    Kopsavilkums([
        "Atrodu tipiskās kļūdas daļu saskaitīšanā un atņemšanā.",
        "Paskaidroju, kāpēc risinājums aplams.",
        "Uzrakstu pareizo risinājumu.",
    ]),

    Majas([
        "Izdomā vienu aplamu risinājumu un palūdz kādam atrast kļūdu.",
        "Paskaidro, kāpēc summa nevar būt mazāka par saskaitāmo.",
        "Pārbaudi savus šīs nedēļas uzdevumus - vai atrodi kļūdu?",
    ]),
]
