# -*- coding: utf-8 -*-
"""4. klase, 106. stunda: «Kā pieraksta summu un starpību?»

Pieraksta forma: {a|n} + {b|n} = {a + b|n} un {a|n} − {b|n} = {a − b|n}.
Pieraksts uz vienas līnijas ar vidējo soli (skaitītāju summa virs
svītras) parāda, ko dara. Atņemšana - tie paši gabali, tikai paņemti prom.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, dala)

TEMA = "Kā pieraksta summu un starpību?"

MERKIS = ("Saskaitīsim un atņemsim daļas ar vienādiem saucējiem, veidojot "
          "pareizu pierakstu.")

SATURS = [
    Sakums("Cik šokolādes palika?",
           zimejums=dala(10, 7, "7/10 - 4/10 = 3/10"),
           paraksts="Bija 7 gabali no 10, apēda 4.",
           fakti=["Atņemot daļas, arī saucējs paliek tas pats.",
                  "No skaitītāja atņem skaitītāju."]),

    Doma("{a|n} ± {b|n} = {a ± b|n}",
         "Daļām ar vienādiem saucējiem saskaita vai atņem skaitītājus, "
         "saucēju pārraksta.",
         soli=[
             "Pieraksti izteiksmi.",
             "Vidējā solī virs svītras - skaitītāju darbība, zem - saucējs.",
             "Izrēķini skaitītāju.",
             "Ja iznāk {n|n}, pieraksti arī = 1.",
         ],
         pieze="{7|10} − {4|10} = {7 − 4|10} = {3|10}."),

    Paraugs("{11|12} − {5|12}",
            uzd="Izrēķini {11|12} − {5|12} ar pilnu pierakstu.",
            soli=[
                ("{11|12} − {5|12} = {11 − 5|12}", "Vidējais solis."),
                ("= {6|12}", None),
            ],
            atbilde="{6|12}"),

    Ievadi("Saskaiti un atņem", [
        {"jaut": "{7|10} − {4|10} = ?", "atb": ["3/10"],
         "vieta": "piem., 1/2", "padoms": "7 − 4."},
        {"jaut": "{5|6} − {1|6} = ?", "atb": ["4/6"], "vieta": "piem., 1/2",
         "padoms": "5 − 1."},
        {"jaut": "{2|9} + {6|9} = ?", "atb": ["8/9"], "vieta": "piem., 1/2",
         "padoms": "2 + 6."},
        {"jaut": "1 − {3|8} = ? (1 = {8|8})", "atb": ["5/8"],
         "vieta": "piem., 1/2", "padoms": "8 − 3."},
        {"jaut": "{9|5} − {3|5} = ?", "atb": ["6/5"], "vieta": "piem., 1/2",
         "padoms": "9 − 3."},
        {"jaut": "{3|7} + {2|7} − {4|7} = ?", "atb": ["1/7"],
         "vieta": "piem., 1/2", "padoms": "3 + 2 − 4."},
    ], pamats=4),

    Varianti("Kurš pieraksts pareizs?", [
        {"jaut": "{5|9} − {2|9} = ?",
         "opcijas": ["{5 − 2|9} = {3|9}", "{5 − 2|9 − 9} = {3|0}",
                     "{5|9 − 2}"], "pareizi": 0,
         "padoms": "Saucēju neatņem."},
        {"jaut": "{4|11} + {4|11} = ?",
         "opcijas": ["{8|11}", "{8|22}", "{16|11}", "{4|22}"], "pareizi": 0,
         "padoms": "4 + 4."},
        {"jaut": "{6|6} − {6|6} = ?",
         "opcijas": ["0", "1", "{0|0}", "{12|6}"], "pareizi": 0,
         "padoms": "1 − 1."},
        {"jaut": "Kura summa ir 1?",
         "opcijas": ["{3|7} + {4|7}", "{3|7} + {3|7}", "{1|2} + {1|3}",
                     "{4|7} + {4|7}"], "pareizi": 0,
         "padoms": "{7|7}."},
    ], pamats=4),

    Pasaule("Telefona uzlāde",
            Ievadi("", [
                {"jaut": "No rīta uzlāde {9|10}. Līdz pusdienām iztērēja "
                         "{4|10}. Cik palika?",
                 "atb": ["5/10"], "vieta": "piem., 1/2", "padoms": "9 − 4."},
                {"jaut": "Uzlādēja vēl {3|10}. Cik tagad?",
                 "atb": ["8/10"], "vieta": "piem., 1/2", "padoms": "5 + 3."},
                {"jaut": "Vakarā iztērēja {6|10}. Cik palika?",
                 "atb": ["2/10"], "vieta": "piem., 1/2", "padoms": "8 − 6."},
                {"jaut": "Cik desmitdaļu jāuzlādē līdz pilnai (1)?",
                 "atb": ["8"], "padoms": "10 − 2."},
            ]),
            pavediens="dati",
            konteksts="Telefona akumulators ir daļa no pilna - to "
                      "tērē un uzlādē pa daļām.",
            kapec="Daļu saskaitīšana un atņemšana ir akumulatora "
                  "grāmatvedība."),

    Kopsavilkums([
        "Pierakstu daļu summu un starpību ar vidējo soli.",
        "Atņemu daļas ar vienādiem saucējiem.",
        "Rēķinu 1 − daļa, pārvēršot 1 par {n|n}.",
    ]),

    Majas([
        "Pieraksti dienas telefona uzlādes izmaiņas daļās.",
        "Izrēķini 1 − {5|12} un 1 − {3|4}.",
        "Izdomā vienu saskaitīšanas un vienu atņemšanas piemēru.",
    ]),
]
