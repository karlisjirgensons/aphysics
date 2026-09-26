# -*- coding: utf-8 -*-
"""4. klase, 84. stunda: «Kā dala rakstos?»

Stūrītis ar divciparu dalītāju: grūtākais ir uzminēt dalījuma ciparu (cik
reižu 32 ietilpst 147?). Palīdz noapaļošana - 32 ≈ 30, 147 ≈ 150, 150 : 30 =
5, un pārbaude ar reizinājumu - 32 · 5 = 160, par daudz, tātad 4.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā dala rakstos?"

MERKIS = ("Dalīsim rakstos (stūrītī) ar divciparu skaitli un komentēsim "
          "katru soli.")

SATURS = [
    Sakums("Cik ciparu būs dalījumā?",
           zimejums=restis([["1", "4", "7", "2", "|", "32"],
                            ["1", "2", "8", "", "|", "46"],
                            ["", "1", "9", "2", "", ""],
                            ["", "1", "9", "2", "", ""],
                            ["", "", "", "0", "", ""]],
                           "1472 : 32 = 46"),
           paraksts="Pirmais nepilnais dalāmais - 147.",
           fakti=["1 un 14 ir mazāki par 32 - tāpēc sāk ar 147.",
                  "Dalījumā būs divi cipari: desmiti un vieni."]),

    Doma("Uzmini ciparu, pārbaudi, labo",
         "Dalījuma ciparu atrod ar noapaļošanu, tad pārbauda ar reizināšanu "
         "un vajadzības gadījumā samazina vai palielina.",
         soli=[
             "Atrodi pirmo nepilno dalāmo: 147.",
             "Uzmini: 32 ≈ 30, 147 ≈ 150, 150 : 30 = 5.",
             "Pārbaudi: 32 · 5 = 160 > 147 - par daudz, ņem 4.",
             "32 · 4 = 128, 147 − 128 = 19; nolaid 2 → 192; 192 : 32 = 6.",
         ],
         pieze="Atlikums katrā solī jābūt mazākam par dalītāju - citādi "
               "cipars bija par mazu."),

    Paraugs("1472 : 32",
            uzd="Izdali stūrītī 1472 : 32.",
            soli=[
                ("147 : 32 = 4 (atl. 19)", "32 · 4 = 128."),
                ("192 : 32 = 6", "Nolaiž 2."),
                ("1472 : 32 = 46", "Pārbaude: 46 · 32 = 1472."),
            ],
            atbilde="46"),

    Slidnis("Uzminēt ciparu: 245 : 35",
            soli=[
                {"v": "35 ≈ 40, 245 ≈ 240", "teksts": "Noapaļo."},
                {"v": "240 : 40 = 6", "teksts": "Minējums: 6."},
                {"v": "35 · 6 = 210", "teksts": "245 − 210 = 35 - nav "
                 "mazāks par 35! Cipars par mazu."},
                {"v": "35 · 7 = 245", "teksts": "Tieši. Cipars 7."},
            ]),

    Ievadi("Stūrītī", [
        {"jaut": "1472 : 32 = ?", "atb": ["46"], "padoms": "147, 192."},
        {"jaut": "245 : 35 = ?", "atb": ["7"], "padoms": "35 · 7."},
        {"jaut": "1702 : 23 = ?", "atb": ["74"], "padoms": "170, 92."},
        {"jaut": "2944 : 64 = ?", "atb": ["46"], "padoms": "294, 384."},
        {"jaut": "5320 : 56 = ?", "atb": ["95"], "padoms": "532, 280."},
        {"jaut": "3276 : 42 = ?", "atb": ["78"], "padoms": "327, 336."},
    ], pamats=4),

    Varianti("Minējums un pārbaude", [
        {"jaut": "Cik reižu 23 ietilpst 170?",
         "opcijas": ["7", "8", "6", "17"], "pareizi": 0,
         "padoms": "23 · 7 = 161, 23 · 8 = 184."},
        {"jaut": "Minēji 5, bet atlikums sanāca 40, dalot ar 32. Ko darīt?",
         "opcijas": ["palielināt ciparu uz 6", "samazināt uz 4",
                     "viss kārtībā"], "pareizi": 0,
         "padoms": "40 > 32 - vēl viens 32 ietilpst."},
        {"jaut": "Ar kuru skaitli sāk 3276 : 42?",
         "opcijas": ["327", "32", "3", "3276"], "pareizi": 0,
         "padoms": "32 < 42, tāpēc ņem trīs ciparus."},
    ]),

    Pasaule("Grāmatu tirgus",
            Ievadi("", [
                {"jaut": "Izdevniecība iespieda 1472 grāmatas, kastē 32. Cik "
                         "kastu?",
                 "atb": ["46"], "padoms": "1472 : 32."},
                {"jaut": "Tirgū pārdeva grāmatas par 1702 €, katra 23 €. Cik "
                         "grāmatu?",
                 "atb": ["74"], "padoms": "1702 : 23."},
                {"jaut": "Tipogrāfija 64 minūtēs izdrukā 2944 lapas. Cik "
                         "minūtē?",
                 "atb": ["46"], "padoms": "2944 : 64."},
                {"jaut": "Grāmatā 3276 rindiņas, lappusē 42. Cik lappušu?",
                 "atb": ["78"], "padoms": "3276 : 42."},
            ]),
            pavediens="skola",
            konteksts="Grāmatu izdošanā skaitļi ir tūkstošos - lapas, "
                      "rindiņas un kastes.",
            kapec="Stūrītis dala jebkuru skaitli - soli pa solim."),

    Kopsavilkums([
        "Dalu stūrītī ar divciparu skaitli.",
        "Minu dalījuma ciparu ar noapaļošanu.",
        "Pārbaudu un labo ciparu, ja vajag.",
    ]),

    Majas([
        "Izdali stūrītī 2048 : 32.",
        "Izrēķini, cik lappušu grāmatā, ja 3150 rindiņas pa 35 rindiņām.",
        "Paskaidro mājiniekiem, kā uzminēt dalījuma ciparu.",
    ]),
]
