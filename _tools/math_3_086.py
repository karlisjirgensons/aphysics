# -*- coding: utf-8 -*-
"""3. klase, 86. stunda: «Kā saskaitīt daļas ar vienādu saucēju?»

Pirmā darbība ar daļām. Ar modeli tā ir acīmredzama: divas astotdaļas un vēl
trīs astotdaļas ir piecas astotdaļas. Grūtākais ir noteikums, ka saucējs
nemainās - to skolēni jauc visbiežāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         dala)

TEMA = "Kā saskaitīt daļas ar vienādu saucēju?"

MERKIS = ("Ar modeli saskaitīsim un atņemsim parastās daļas ar vienādiem "
          "saucējiem.")

SATURS = [
    Sakums("Cik būs divas astotdaļas un vēl trīs astotdaļas?",
           zimejums=dala(8, 5, "2/8 + 3/8 = 5/8",
                         "astoņas vienādas daļas"),
           paraksts="Daļas ir vienādas, tāpēc tās var vienkārši saskaitīt.",
           fakti=["Saskaitot daļas ar vienādu saucēju, saucējs nemainās.",
                  "Saskaita tikai skaitītājus."]),

    Doma("Saskaita skaitītājus, saucējs paliek tas pats",
         "{2|8} + {3|8} = {5|8} - daļu lielums nemainās, mainās tikai to "
         "skaits.",
         soli=[
             "Pārbaudi, vai abām daļām saucējs ir viens un tas pats.",
             "Saskaiti skaitītājus.",
             "Saucēju pārraksti bez izmaiņām.",
             "Pārbaudi, vai atbilde nav lielāka par veselo.",
         ],
         pieze="Saucēju nesaskaita tāpēc, ka tas nav daudzums - tas ir daļas "
               "*vārds*. Divi āboli un trīs āboli ir pieci āboli, nevis pieci "
               "ābolāboli."),

    Slidnis("Kā aug summa",
            soli=[
                {"v": "{2|8}", "teksts": "Divas astotdaļas.", "josla": 25},
                {"v": "{2|8} + {1|8} = {3|8}",
                 "teksts": "Pieliek vēl vienu.", "josla": 37},
                {"v": "{3|8} + {2|8} = {5|8}",
                 "teksts": "Pieliek vēl divas.", "josla": 62},
                {"v": "{5|8} + {3|8} = {8|8} = 1",
                 "teksts": "Sanāca viens vesels.", "josla": 100},
            ],
            ievads="Saucējs visu laiku paliek 8."),

    Paraugs("Cik ir {2|8} + {3|8}?",
            uzd="Saskaiti {2|8} + {3|8}.",
            soli=[
                ("Saucēji ir vienādi - 8",
                 "Abas daļas ir astotdaļas."),
                ("2 + 3 = 5",
                 "Saskaita skaitītājus."),
                ("{2|8} + {3|8} = {5|8}",
                 "Saucējs paliek 8."),
            ],
            atbilde="{5|8}"),

    Ievadi("Saskaiti un atņem daļas", [
        {"jaut": "{2|8} + {3|8} = ? Ieraksti skaitītāju.", "atb": ["5"],
         "padoms": "2 + 3."},
        {"jaut": "{4|9} + {2|9} = ? Ieraksti skaitītāju.", "atb": ["6"],
         "padoms": "4 + 2."},
        {"jaut": "{5|6} − {2|6} = ? Ieraksti skaitītāju.", "atb": ["3"],
         "padoms": "5 − 2."},
        {"jaut": "{7|10} − {4|10} = ? Ieraksti skaitītāju.", "atb": ["3"],
         "padoms": "7 − 4."},
        {"jaut": "{3|5} + {2|5} = ? Cik tas ir veselo?", "atb": ["1"],
         "padoms": "{5|5} = 1."},
        {"jaut": "{1|4} + {2|4} = ? Ieraksti skaitītāju.", "atb": ["3"],
         "padoms": "1 + 2."},
    ], pamats=4,
        ievads="Saucējs nemainās, tāpēc pietiek ierakstīt skaitītāju."),

    Zimejums("Atņemšana",
             dala(6, 3, "5/6 − 2/6 = 3/6", "sešas vienādas daļas"),
             paskaidro="Atņemot arī saucējs paliek tas pats - noņem tikai "
                       "daļu skaitu.",
             ievads="No piecām sestdaļām noņem divas."),

    Varianti("Vai rēķins ir pareizs?", [
        {"jaut": "Cik ir {3|7} + {2|7}?",
         "opcijas": ["{5|7}", "{5|14}", "{6|7}", "{5|9}"],
         "pareizi": 0, "padoms": "Saucējs nemainās."},
        {"jaut": "Kāpēc saucēju nesaskaita?",
         "opcijas": ["Tas ir daļas vārds, ne daudzums",
                     "Tas ir par lielu", "Tā ir tradīcija",
                     "Saucēju saskaita"],
         "pareizi": 0, "padoms": "Astotdaļas paliek astotdaļas."},
        {"jaut": "Cik ir {9|10} − {5|10}?",
         "opcijas": ["{4|10}", "{4|0}", "{14|10}", "{4|5}"],
         "pareizi": 0, "padoms": "9 − 5."},
        {"jaut": "Cik ir {2|3} + {1|3}?",
         "opcijas": ["1", "{3|6}", "{2|6}", "{3|3} nav vesels"],
         "pareizi": 0, "padoms": "{3|3} = 1."},
    ], pamats=4),

    Pasaule("Cik distances ir noskriets?",
            Ievadi("", [
                {"jaut": "Skrējējs noskrēja {3|8} un vēl {2|8} distances. "
                         "Cik daļu kopā? Ieraksti skaitītāju.",
                 "atb": ["5"], "padoms": "3 + 2."},
                {"jaut": "Cik astotdaļu vēl atlicis?", "atb": ["3"],
                 "padoms": "8 − 5."},
                {"jaut": "Distance ir 800 m. Cik metru ir viena astotdaļa?",
                 "atb": ["100"], "padoms": "800 : 8."},
                {"jaut": "Cik metru viņš jau noskrējis?", "atb": ["500"],
                 "padoms": "5 · 100."},
            ]),
            pavediens="sports",
            konteksts="Garā skrējienā posmus saskaita pa vienam - un tie "
                      "visi ir vienāda garuma daļas.",
            kapec="Daļu saskaitīšana ir tā pati posmu saskaitīšana."),

    Kopsavilkums([
        "Saskaitu un atņemu daļas ar vienādiem saucējiem.",
        "Zinu, ka saucējs nemainās.",
        "Modelēju darbību ar joslu vai figūru.",
        "Zinu, ka {n|n} = 1.",
    ]),

    Majas([
        "Izrēķini {3|10} + {4|10} un {9|10} − {2|10}.",
        "Uzzīmē modeli vienam no šiem rēķiniem.",
        "Izdomā savu uzdevumu ar daļu saskaitīšanu.",
    ]),
]
