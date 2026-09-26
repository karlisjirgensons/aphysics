# -*- coding: utf-8 -*-
"""1. klase, 73. stunda: «Cik centimetru ir decimetrā?»

Decimetrs (dm) ir 10 centimetru - tāpat kā desmits ir 10 vieni. Metrs (m)
ir 10 decimetru. 3 dm = 30 cm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, lineals)

TEMA = "Cik centimetru ir decimetrā?"

MERKIS = ("Šodien iepazīsim decimetru un metru un pāriesim no decimetriem uz "
          "centimetriem.")

SATURS = [
    Sakums("Kas ir decimetrs?",
           zimejums=lineals(20, [(0, 10, "1 dm = 10 cm")]),
           paraksts="No 0 līdz 10 - viens decimetrs.",
           fakti=["1 dm = 10 cm.",
                  "1 m = 10 dm = 100 cm.",
                  "Pieraksta: cm, dm, m."]),

    Doma("Desmiti garumā",
         "Decimetrs ir centimetru desmits.",
         soli=[
             "10 cm saliek vienā decimetrā.",
             "3 dm = 10 cm + 10 cm + 10 cm = 30 cm.",
             "10 dm saliek vienā metrā.",
         ]),

    Ievadi("Pārveido", [
        {"jaut": "1 dm = ? cm", "atb": ["10"], "padoms": "Desmits."},
        {"jaut": "3 dm = ? cm", "atb": ["30"], "padoms": "10, 20, 30."},
        {"jaut": "50 cm = ? dm", "atb": ["5"], "padoms": "5 desmiti."},
        {"jaut": "1 m = ? dm", "atb": ["10"], "padoms": "10 decimetru."},
        {"jaut": "1 m = ? cm", "atb": ["100"], "padoms": "10 dm pa 10 cm."},
        {"jaut": "7 dm = ? cm", "atb": ["70"], "padoms": "7 desmiti."},
    ], pamats=4),

    Varianti("Kura mērvienība?", [
        {"jaut": "Grāmatas garums 2 ...",
         "opcijas": ["dm", "m", "cm"], "pareizi": 0,
         "padoms": "20 cm."},
        {"jaut": "Klases garums 8 ...", "opcijas": ["m", "cm", "dm"],
         "pareizi": 0, "padoms": "Ļoti garš."},
        {"jaut": "Dzēšgumijas garums 3 ...", "opcijas": ["cm", "dm", "m"],
         "pareizi": 0, "padoms": "Mazs."},
    ]),

    Pasaule("Lente dāvanai",
            Ievadi("", [
                {"jaut": "Dāvanai vajag 4 dm lentes. Cik cm?", "atb": ["40"],
                 "padoms": "4 · 10."},
                {"jaut": "Lente ir 1 m. Cik dm paliks pēc 4 dm?", "atb": ["6"],
                 "padoms": "10 − 4."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā lenti mēra un griež.",
            kapec="Mērvienības var mainīt - garums paliek tas pats."),

    Kopsavilkums([
        "Zinu, ka 1 dm = 10 cm.",
        "Zinu, ka 1 m = 10 dm = 100 cm.",
        "Pārveidoju decimetrus centimetros.",
    ]),

    Majas([
        "Izgriez papīra sloksni 1 dm garu.",
        "Izmēri ar to galdu: cik dm?",
        "Atrodi mājās kaut ko apmēram 1 dm garu.",
    ]),
]
