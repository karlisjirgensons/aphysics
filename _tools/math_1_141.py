# -*- coding: utf-8 -*-
"""1. klase, 141. stunda: «Metros, decimetros vai centimetros?»

Vienu garumu var pierakstīt dažādi: 1 m = 10 dm = 100 cm; 50 cm = 5 dm.
Izvēlas ērtāko mērvienību un salīdzina pierakstus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Metros, decimetros vai centimetros?"

MERKIS = ("Šodien izteiksim viena priekšmeta garumu vairākās mērvienībās un "
          "salīdzināsim pierakstus.")

_TABULA = restis([["m", "dm", "cm"], [1, 10, 100], ["puse", 5, 50]])

SATURS = [
    Sakums("1 m, 10 dm un 100 cm - vai tas pats?",
           zimejums=_TABULA,
           paraksts="Viena rinda - viens garums trijos pierakstos.",
           fakti=["1 m = 10 dm = 100 cm.",
                  "1 dm = 10 cm.",
                  "Lieliem garumiem - m, maziem - cm."]),

    Doma("Pārveido",
         "Uz mazāku mērvienību - skaitlis lielāks; uz lielāku - mazāks.",
         soli=[
             "dm → cm: pa 10 (3 dm = 30 cm).",
             "cm → dm: cik desmitu (40 cm = 4 dm).",
             "m → dm: 1 m = 10 dm.",
         ]),

    Ievadi("Pārveido", [
        {"jaut": "5 dm = ? cm", "atb": ["50"], "padoms": "5 desmiti."},
        {"jaut": "80 cm = ? dm", "atb": ["8"], "padoms": "8 desmiti."},
        {"jaut": "1 m = ? cm", "atb": ["100"], "padoms": "10 dm pa 10 cm."},
        {"jaut": "2 m = ? dm", "atb": ["20"], "padoms": "10 + 10."},
        {"jaut": "60 cm = ? dm", "atb": ["6"], "padoms": "6 desmiti."},
        {"jaut": "1 m = ? dm", "atb": ["10"], "padoms": "Metrā 10 dm."},
    ], pamats=4),

    Varianti("Vienādi?", [
        {"jaut": "40 cm un 4 dm", "opcijas": ["vienādi", "dažādi"],
         "jaukt": False, "pareizi": 0, "padoms": "4 dm = 40 cm."},
        {"jaut": "1 m un 90 cm", "opcijas": ["dažādi", "vienādi"],
         "jaukt": False, "pareizi": 0, "padoms": "1 m = 100 cm."},
        {"jaut": "Kura mērvienība ērtāka mājas augstumam?",
         "opcijas": ["m", "cm"], "jaukt": False, "pareizi": 0,
         "padoms": "Liels garums."},
    ]),

    Pasaule("Aukla pūķim",
            Ievadi("", [
                {"jaut": "Pūķim vajag 1 m auklas. Tev ir 7 dm. Cik dm "
                         "pietrūkst?", "atb": ["3"], "padoms": "10 − 7."},
                {"jaut": "Cik tas ir cm?", "atb": ["30"],
                 "padoms": "3 dm."},
            ]),
            pavediens="sports",
            konteksts="Rudenī laiž pūķus.",
            kapec="Pārveidojot mērvienības, var salīdzināt."),

    Kopsavilkums([
        "Izsaku garumu m, dm un cm.",
        "Pārveidoju mērvienības.",
        "Izvēlos ērtāko.",
    ]),

    Majas([
        "Izmēri galdu un pieraksti trijos veidos.",
        "Kura mērvienība ērtākā?",
        "Paskaidro mājiniekam.",
    ]),
]
