# -*- coding: utf-8 -*-
"""1. klase, 90. stunda: «Kādā secībā saskaitīt trīs skaitļus?»

Trīs skaitļus var saskaitīt jebkurā secībā. Izdevīgi vispirms saskaitīt
desmita draugus: 7 + 5 + 3 = 7 + 3 + 5 = 10 + 5 = 15.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kādā secībā saskaitīt trīs skaitļus?"

MERKIS = ("Šodien izvēlēsimies izdevīgāko secību, saskaitot trīs skaitļus "
          "20 apjomā.")

SATURS = [
    Sakums("7 + 5 + 3 - ar ko sākt?",
           fakti=["Atrodi desmita draugus: 7 un 3.",
                  "Saskaiti tos vispirms: 10.",
                  "Tad pieliec pārējo: 10 + 5 = 15."]),

    Paraugs("Izdevīga secība",
            uzd="Izrēķini 7 + 5 + 3.",
            soli=[
                ("7 + 3 = 10", "Desmita draugi vispirms."),
                ("10 + 5 = 15", "Pieliek trešo skaitli."),
            ],
            atbilde="15"),

    Doma("Meklē desmitu",
         "Trīs skaitļus var saskaitīt jebkurā secībā - izvēlies to, kas dod "
         "10.",
         soli=[
             "Paskaties uz visiem trim.",
             "Atrodi divus, kas kopā ir 10.",
             "Saskaiti tos, tad pieliec trešo.",
         ]),

    Ievadi("Saskaiti gudri", [
        {"jaut": "6 + 8 + 4", "atb": ["18"], "padoms": "6 + 4 = 10."},
        {"jaut": "2 + 9 + 8", "atb": ["19"], "padoms": "2 + 8 = 10."},
        {"jaut": "5 + 7 + 5", "atb": ["17"], "padoms": "5 + 5 = 10."},
        {"jaut": "1 + 6 + 9", "atb": ["16"], "padoms": "1 + 9 = 10."},
        {"jaut": "3 + 4 + 7", "atb": ["14"], "padoms": "3 + 7 = 10."},
        {"jaut": "8 + 3 + 2", "atb": ["13"], "padoms": "8 + 2 = 10."},
    ], pamats=4),

    Varianti("Ar ko sākt?", [
        {"jaut": "4 + 9 + 6", "opcijas": ["4 + 6", "4 + 9", "9 + 6"],
         "pareizi": 0, "padoms": "Desmita draugi."},
        {"jaut": "3 + 5 + 5", "opcijas": ["5 + 5", "3 + 5"],
         "jaukt": False, "pareizi": 0, "padoms": "5 + 5 = 10."},
    ]),

    Pasaule("Āboli trīs grozos",
            Ievadi("", [
                {"jaut": "Grozos 8, 4 un 2 āboli. Cik kopā?", "atb": ["14"],
                 "padoms": "8 + 2 = 10, un 4."},
                {"jaut": "Grozos 3, 6 un 7 āboli. Cik kopā?", "atb": ["16"],
                 "padoms": "3 + 7 = 10, un 6."},
            ]),
            pavediens="daba",
            konteksts="Dārzā salasīja ābolus trīs grozos.",
            kapec="Gudra secība - ātrāk un bez kļūdām."),

    Kopsavilkums([
        "Saskaitu trīs skaitļus jebkurā secībā.",
        "Vispirms meklēju desmita draugus.",
        "Izvēlos izdevīgāko secību.",
    ]),

    Majas([
        "Izrēķini 9 + 5 + 1 un 4 + 8 + 6.",
        "Pastāsti, ar ko sāki.",
        "Izdomā savu piemēru ar desmita draugiem.",
    ]),
]
