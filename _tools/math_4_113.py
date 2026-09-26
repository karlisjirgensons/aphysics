# -*- coding: utf-8 -*-
"""4. klase, 113. stunda: «Kā daļu uzrakstīt kā reizinājumu?»

{3|5} = 3 · {1|5}: vienādu pamatdaļu summa kļūst par reizinājumu, tāpat kā
4 + 4 + 4 = 3 · 4 no 3. klases. Šis pieraksts sagatavo vesela skaitļa un
daļas reizinājumu nākamajā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā daļu uzrakstīt kā reizinājumu?"

MERKIS = ("Pierakstīsim daļu kā skaitītāja un pamatdaļas reizinājumu.")

SATURS = [
    Sakums("4 + 4 + 4 = 3 · 4. Un {1|5} + {1|5} + {1|5}?",
           zimejums=restis([["veseli", "4 + 4 + 4", "3 · 4"],
                            ["daļas", "1/5 + 1/5 + 1/5", "3 · 1/5"]],
                           "tas pats likums"),
           paraksts="{3|5} = 3 · {1|5}.",
           fakti=["Reizināšana ir vienādu saskaitāmo summa.",
                  "Tas der arī daļām."]),

    Doma("{a|n} = a · {1|n}",
         "Daļu var uzrakstīt kā skaitītāja un pamatdaļas reizinājumu.",
         soli=[
             "Atrodi pamatdaļu: {1|n}.",
             "Skaitītājs - cik reižu to ņem.",
             "Pieraksti: {a|n} = a · {1|n}.",
             "Otrādi: a · {1|n} = {a|n}.",
         ],
         pieze="7 · {1|4} = {7|4} - arī neīsta daļa."),

    Slidnis("No summas uz reizinājumu",
            soli=[
                {"v": "{1|8} + {1|8} + {1|8} + {1|8} + {1|8}",
                 "teksts": "Garš pieraksts."},
                {"v": "5 · {1|8}", "teksts": "Īsāk - reizinājums."},
                {"v": "{5|8}", "teksts": "Vēl īsāk - daļa."},
            ]),

    Paraugs("6 · {1|7}",
            uzd="Izrēķini 6 · {1|7}.",
            soli=[
                ("6 · {1|7} = {1|7} + ... + {1|7}", "Sešas reizes."),
                ("= {6|7}", None),
            ],
            atbilde="{6|7}"),

    Ievadi("Reizinājums un daļa", [
        {"jaut": "4 · {1|9} = ?", "atb": ["4/9"], "vieta": "piem., 1/2",
         "padoms": "Četras devītdaļas."},
        {"jaut": "{7|10} = ? · {1|10}", "atb": ["7"],
         "padoms": "Skaitītājs."},
        {"jaut": "{5|3} = 5 · {1|?}", "atb": ["3"], "padoms": "Saucējs."},
        {"jaut": "9 · {1|4} = ?", "atb": ["9/4"], "vieta": "piem., 1/2",
         "padoms": "Neīsta daļa."},
    ]),

    Varianti("Kurš pieraksts?", [
        {"jaut": "{3|8} = ?",
         "opcijas": ["3 · {1|8}", "8 · {1|3}", "3 · 8", "{1|3} · {1|8}"],
         "pareizi": 0, "padoms": "Skaitītājs · pamatdaļa."},
        {"jaut": "2 · {1|5} = ?",
         "opcijas": ["{2|5}", "{2|10}", "{1|10}", "{5|2}"], "pareizi": 0,
         "padoms": "Divas piektdaļas."},
        {"jaut": "Vai 5 · {1|5} = 1?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "{5|5} = 1."},
    ]),

    Pasaule("Picērijas pasūtījumi",
            Ievadi("", [
                {"jaut": "Katra pica sagriezta 8 gabalos. Viens gabals - "
                         "{1|8} picas. 3 · {1|8} = ?",
                 "atb": ["3/8"], "vieta": "piem., 1/2",
                 "padoms": "Trīs gabali."},
                {"jaut": "Ģimene paņēma 10 gabalus: 10 · {1|8} = ?",
                 "atb": ["10/8"], "vieta": "piem., 1/2",
                 "padoms": "Neīsta daļa."},
                {"jaut": "Cik veselu picu ir 16 · {1|8}?", "atb": ["2"],
                 "padoms": "{16|8} = 2."},
                {"jaut": "Cik gabalu vajag 3 veselām picām?", "atb": ["24"],
                 "padoms": "3 · 8."},
            ]),
            pavediens="virtuve",
            konteksts="Picērijā pārdod gabalos - katrs ir pamatdaļa, un "
                      "pasūtījums ir to reizinājums.",
            kapec="Reizinājums ar pamatdaļu ir ātrākais daļas pieraksts."),

    Kopsavilkums([
        "Pierakstu daļu kā reizinājumu: {a|n} = a · {1|n}.",
        "Pārvēršu reizinājumu atpakaļ par daļu.",
        "Zinu, ka tas der arī neīstām daļām.",
    ]),

    Majas([
        "Uzraksti kā reizinājumu: {4|7}, {9|10}, {5|2}.",
        "Izrēķini: 8 · {1|12}, 3 · {1|3}.",
        "Paskaidro, kāpēc 4 · {1|4} = 1.",
    ]),
]
