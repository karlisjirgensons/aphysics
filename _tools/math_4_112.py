# -*- coding: utf-8 -*-
"""4. klase, 112. stunda: «Kā daļu izteikt ar pamatdaļām?»

{3|5} = {1|5} + {1|5} + {1|5}: katra daļa ir pamatdaļu summa. Tas ir
tilts uz reizināšanu - vienādu saskaitāmo summu īsāk pieraksta ar
reizinājumu, un tas notiks nākamajā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, dala)

TEMA = "Kā daļu izteikt ar pamatdaļām?"

MERKIS = ("Izteiksim daļu kā pamatdaļu summu un pierakstīsim to īsāk.")

SATURS = [
    Sakums("No kā sastāv {3|5}?",
           zimejums=dala(5, 3, "1/5 + 1/5 + 1/5"),
           paraksts="Trīs vienādi gabali pa {1|5}.",
           fakti=["Pamatdaļa - daļa ar skaitītāju 1.",
                  "Katra daļa ir tās pamatdaļu summa."]),

    Doma("Skaitītājs pasaka, cik pamatdaļu",
         "Daļa {a|n} ir a pamatdaļu {1|n} summa.",
         soli=[
             "Atrodi pamatdaļu: saucējs 5 → {1|5}.",
             "Skaitītājs 3 → trīs saskaitāmie.",
             "{3|5} = {1|5} + {1|5} + {1|5}.",
             "Īsāk: trīs reizes {1|5}.",
         ],
         pieze="Neīsta daļa arī: {7|4} = septiņas reizes {1|4}."),

    Paraugs("{4|9}",
            uzd="Izsaki {4|9} ar pamatdaļām.",
            soli=[
                ("pamatdaļa {1|9}", None),
                ("{1|9} + {1|9} + {1|9} + {1|9}", "Četras reizes."),
            ],
            atbilde="četras pamatdaļas {1|9}"),

    Ievadi("Cik pamatdaļu?", [
        {"jaut": "Cik pamatdaļu {1|7} ir {5|7}?", "atb": ["5"],
         "padoms": "Skaitītājs."},
        {"jaut": "Cik pamatdaļu {1|10} ir {9|10}?", "atb": ["9"],
         "padoms": "Skaitītājs."},
        {"jaut": "{1|6} + {1|6} + {1|6} + {1|6} = ?", "atb": ["4/6"],
         "vieta": "piem., 1/2", "padoms": "Četras sestdaļas."},
        {"jaut": "Cik pamatdaļu {1|3} ir 2 veselos?", "atb": ["6"],
         "padoms": "{6|3} = 2."},
    ]),

    Varianti("Pareizi?", [
        {"jaut": "{3|4} = {1|4} + {1|4} + {1|4}",
         "opcijas": ["pareizi", "aplami"], "pareizi": 0,
         "padoms": "Trīs ceturtdaļas."},
        {"jaut": "{2|5} = {1|5} + {1|5} + {1|5}",
         "opcijas": ["aplami", "pareizi"], "pareizi": 0,
         "padoms": "Tās ir {3|5}."},
        {"jaut": "{1|8} + {1|8} = {2|16}",
         "opcijas": ["aplami", "pareizi"], "pareizi": 0,
         "padoms": "Saucējs paliek: {2|8}."},
        {"jaut": "Kura ir pamatdaļa?",
         "opcijas": ["{1|12}", "{2|12}", "{12|1}", "{12|12}"], "pareizi": 0,
         "padoms": "Skaitītājs 1."},
    ], pamats=4),

    Pasaule("Laika pamatdaļas",
            Ievadi("", [
                {"jaut": "Minūte ir {1|60} stundas. Cik minūšu ir {15|60} "
                         "stundas?",
                 "atb": ["15"], "padoms": "15 pamatdaļas."},
                {"jaut": "Diena ir {1|7} nedēļas. Kāda daļa nedēļas ir 5 "
                         "darba dienas?",
                 "atb": ["5/7"], "vieta": "piem., 1/2", "padoms": "5 · {1|7}."},
                {"jaut": "Mēnesis ir {1|12} gada. Kāda daļa gada ir vasara "
                         "(3 mēneši)?",
                 "atb": ["3/12"], "vieta": "piem., 1/2", "padoms": "3 · {1|12}."},
                {"jaut": "Cik mēnešu ir {9|12} gada?", "atb": ["9"],
                 "padoms": "Skaitītājs."},
            ]),
            pavediens="skola",
            konteksts="Laiks ir sadalīts pamatdaļās: minūte ir stundas "
                      "sešdesmitā daļa, diena - nedēļas septītā.",
            kapec="Pamatdaļas ļauj izteikt jebkuru laiku kā daļu."),

    Kopsavilkums([
        "Izsaku daļu kā pamatdaļu summu.",
        "Zinu, ka skaitītājs pasaka pamatdaļu skaitu.",
        "Pamanu, ka vienādus saskaitāmos var pierakstīt īsāk.",
    ]),

    Majas([
        "Izsaki kā pamatdaļu summu: {5|8}, {3|10}, {6|4}.",
        "Aprēķini, kāda daļa dienas ir tavs miegs (pamatdaļa {1|24}).",
        "Padomā: kā summu {1|8} + {1|8} + {1|8} uzrakstīt īsāk?",
    ]),
]
