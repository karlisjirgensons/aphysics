# -*- coding: utf-8 -*-
"""1. klase, 95. stunda: «Kā «izjaukt» desmitu?»

13 − 5: vienu nepietiek (3 < 5). Vispirms atņem 3 - līdz 10, tad vēl 2 no
desmita: 13 − 5 = 13 − 3 − 2 = 10 − 2 = 8. Desmits tiek «izjaukts».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, ramis, taisne)

TEMA = "Kā «izjaukt» desmitu?"

MERKIS = ("Šodien atņemsim ar desmita sadalīšanu un izskaidrosim katru "
          "soli.")

SATURS = [
    Sakums("13 − 5: vienu ir tikai 3 - ko darīt?",
           zimejums=taisne(0, 20, 1, [(8, "8")],
                           bultas=[(13, 10, "−3"), (10, 8, "−2")]),
           paraksts="Vispirms līdz 10, tad no desmita.",
           fakti=["5 = 3 + 2.",
                  "13 − 3 = 10.",
                  "10 − 2 = 8."]),

    Slidnis("13 − 5 rāmī", [
        {"v": "13", "teksts": "Pilns rāmis un 3", "zim": ramis(13, 2)},
        {"v": "13 − 3", "teksts": "Paliek pilns desmits",
         "zim": ramis(10, 2)},
        {"v": "10 − 2", "teksts": "Izjaucam desmitu: 8", "zim": ramis(8, 2)},
    ]),

    Paraugs("Caur desmitu atpakaļ",
            uzd="Izrēķini 14 − 6.",
            soli=[
                ("6 = 4 + 2", "Vispirms atņem tik, cik vienu."),
                ("14 − 4 = 10", "Līdz desmitam."),
                ("10 − 2 = 8", "Atlikumu no desmita."),
            ],
            atbilde="8"),

    Doma("Izjauc desmitu",
         "Ja vienu nepietiek, atņem līdz 10 un pārējo - no desmita.",
         soli=[
             "Cik vienu? Tik atņem vispirms.",
             "Tagad ir tieši 10.",
             "Atlikumu atņem no 10.",
         ]),

    Ievadi("Atņem caur 10", [
        {"jaut": "12 − 5 = 12 − 2 − ?", "atb": ["3"], "padoms": "5 = 2 + 3."},
        {"jaut": "15 − 7 = 10 − ?", "atb": ["2"], "padoms": "7 = 5 + 2."},
        {"jaut": "11 − 4 = ?", "atb": ["7"], "padoms": "11 − 1 − 3."},
        {"jaut": "16 − 9 = ?", "atb": ["7"], "padoms": "16 − 6 − 3."},
        {"jaut": "13 − 8 = ?", "atb": ["5"], "padoms": "13 − 3 − 5."},
        {"jaut": "17 − 9 = ?", "atb": ["8"], "padoms": "17 − 7 − 2."},
    ], pamats=4),

    Pasaule("Kūkas gabaliņi",
            Ievadi("", [
                {"jaut": "Uz šķīvja 12 cepumu. Viesi apēda 5. Cik palika?",
                 "atb": ["7"], "padoms": "12 − 2 − 3."},
            ]),
            pavediens="virtuve",
            konteksts="Svētkos viesi cienājas ar cepumiem.",
            kapec="Atņemot caur 10, rēķins ir vieglāks."),

    Kopsavilkums([
        "Atņemu ar desmita sadalīšanu.",
        "Vispirms līdz 10, tad no desmita.",
        "Izskaidroju katru soli.",
    ]),

    Majas([
        "Izrēķini caur 10: 14 − 7, 12 − 8, 15 − 9.",
        "Parādi ar pogām un olu kasti.",
        "Pieraksti soļus.",
    ]),
]
