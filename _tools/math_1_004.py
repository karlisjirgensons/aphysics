# -*- coding: utf-8 -*-
"""1. klase, 4. stunda: «Kur satiec skaitli 7?»

Skaitlis dzīvē: 7 nedēļas dienas, 7 varavīksnes krāsas. Skaitīšana uz
priekšu un atpakaļ, sākot no jebkura skaitļa - skaitļu taisnē tas ir solis
pa labi vai pa kreisi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, Zimejums, restis, taisne)

TEMA = "Kur satiec skaitli 7?"

MERKIS = ("Šodien meklēsim skaitļus ap sevi un skaitīsim uz priekšu un "
          "atpakaļ no jebkura skaitļa.")

_DIENAS = restis([["P", "O", "T", "C", "Pk", "S", "Sv"]])

SATURS = [
    Sakums("Cik dienu ir nedēļā?",
           zimejums=_DIENAS,
           paraksts="Pirmdiena, otrdiena ... svētdiena - 7 dienas.",
           fakti=["Nedēļā ir 7 dienas.",
                  "Varavīksnē ir 7 krāsas.",
                  "Skaitļus redzam uz durvīm, autobusiem un pulksteņa."]),

    Doma("Uz priekšu un atpakaļ",
         "Skaitot uz priekšu, katrs nākamais ir par vienu lielāks; "
         "atpakaļ - par vienu mazāks.",
         soli=[
             "Nosauc skaitli, no kura sāc.",
             "Uz priekšu: 4, 5, 6, 7.",
             "Atpakaļ: 7, 6, 5, 4.",
         ],
         pieze="Skaitļu taisnē uz priekšu ir solis pa labi, atpakaļ - pa "
               "kreisi."),

    Zimejums("Skaitļu taisne",
             taisne(0, 10, 1, [(7, "7")],
                    bultas=[(4, 5, ""), (5, 6, ""), (6, 7, "")]),
             paskaidro="No 4 uz priekšu: 5, 6, 7."),

    Ievadi("Kurš nāk tālāk?", [
        {"jaut": "Kurš skaitlis ir pēc 7?", "atb": ["8"],
         "padoms": "Par vienu vairāk."},
        {"jaut": "Kurš skaitlis ir pirms 7?", "atb": ["6"],
         "padoms": "Par vienu mazāk."},
        {"jaut": "Skaiti atpakaļ: 10, 9, 8, ...", "atb": ["7"],
         "padoms": "Par vienu mazāk nekā 8."},
        {"jaut": "Skaiti uz priekšu: 3, 4, 5, ...", "atb": ["6"],
         "padoms": "Pēc 5."},
        {"jaut": "Kurš skaitlis ir starp 8 un 10?", "atb": ["9"],
         "padoms": "8, ?, 10."},
        {"jaut": "Skaiti atpakaļ: 5, 4, 3, ...", "atb": ["2"],
         "padoms": "Pirms 3."},
    ], pamats=4),

    Varianti("Kur dzīvē ir 7?", [
        {"jaut": "Cik dienu ir nedēļā?",
         "opcijas": ["7", "5", "10", "12"], "pareizi": 0,
         "padoms": "No pirmdienas līdz svētdienai."},
        {"jaut": "Cik pirkstu ir vienai rokai?",
         "opcijas": ["5", "7", "10", "4"], "pareizi": 0,
         "padoms": "Saskaiti savus pirkstus."},
        {"jaut": "Cik riteņu ir velosipēdam?",
         "opcijas": ["2", "3", "4", "7"], "pareizi": 0,
         "padoms": "Priekšā un aizmugurē."},
    ]),

    Pasaule("Raķetes starts",
            Ievadi("", [
                {"jaut": "Skaita atpakaļ: 10, 9, 8, 7, 6, ... Kurš nāk "
                         "tālāk?", "atb": ["5"], "padoms": "Pirms 6."},
                {"jaut": "Kurš skaitlis ir pirms 1?", "atb": ["0"],
                 "padoms": "Starts!"},
            ]),
            pavediens="kosmoss",
            konteksts="Pirms raķetes starta skaita atpakaļ no 10 līdz 0.",
            kapec="Skaitīšana atpakaļ pasaka, cik vēl palicis."),

    Kopsavilkums([
        "Zinu, ka nedēļā ir 7 dienas.",
        "Skaitu uz priekšu un atpakaļ no jebkura skaitļa.",
        "Nosaucu skaitli pirms un pēc dotā.",
    ]),

    Majas([
        "Atrodi mājās 3 vietas, kur redzams skaitlis 7.",
        "Skaiti atpakaļ no 10 līdz 0, kamēr kāds uzvelk zeķes.",
        "Pastāsti, kuras 7 dienas ir nedēļā.",
    ]),
]
