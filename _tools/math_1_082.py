# -*- coding: utf-8 -*-
"""1. klase, 82. stunda: «Kā pierakstīt savu rēķinu?»

Rēķina pierakstā redz katru soli: 13 + 5 = 10 + 3 + 5 = 10 + 8 = 18.
Katrā solī «=» nozīmē «tikpat», tāpēc katra rinda jāvar izskaidrot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pierakstīt savu rēķinu?"

MERKIS = ("Šodien pierakstīsim rēķinu pa soļiem un izskaidrosim katru "
          "soli.")

SATURS = [
    Sakums("Kā parādīt, kā tu izrēķināji 13 + 5?",
           fakti=["13 + 5 = 10 + 3 + 5.",
                  "= 10 + 8 = 18.",
                  "Katrs solis ir patiess."]),

    Paraugs("Pieraksts pa soļiem",
            uzd="Izrēķini 13 + 5 un parādi soļus.",
            soli=[
                ("13 + 5 = 10 + 3 + 5", "13 sadala desmitā un vienos."),
                ("= 10 + 8", "Saskaita vienus: 3 + 5 = 8."),
                ("= 18", "Desmits un 8."),
            ],
            atbilde="18"),

    Doma("Labs pieraksts",
         "Katrs solis ir īss un patiess - un to var izskaidrot.",
         soli=[
             "Sadali skaitli: 13 = 10 + 3.",
             "Saskaiti vienus.",
             "Pieliec desmitu.",
             "Pārbaudi, vai katrs «=» ir patiess.",
         ]),

    Ievadi("Aizpildi soli", [
        {"jaut": "14 + 3 = 10 + 4 + 3 = 10 + ?", "atb": ["7"],
         "padoms": "4 + 3."},
        {"jaut": "12 + 6 = 10 + ? + 6", "atb": ["2"], "padoms": "12 = 10 + 2."},
        {"jaut": "15 + 4 = 10 + 9 = ?", "atb": ["19"], "padoms": "10 + 9."},
        {"jaut": "11 + 7 = 10 + 1 + 7 = ?", "atb": ["18"],
         "padoms": "10 + 8."},
    ]),

    Varianti("Kurš solis nav patiess?", [
        {"jaut": "16 + 2 = 10 + 6 + 2 = 10 + 9 = 19",
         "opcijas": ["10 + 6 + 2 = 10 + 9", "16 + 2 = 10 + 6 + 2",
                     "10 + 9 = 19"], "pareizi": 0,
         "padoms": "6 + 2 = 8, nevis 9."},
    ]),

    Pasaule("Zīmuļi divās kārbās",
            Ievadi("", [
                {"jaut": "Kārbā 12 zīmuļu, otrā 5. Pieraksti: 12 + 5 = 10 + "
                         "2 + 5 = 10 + ? ", "atb": ["7"], "padoms": "2 + 5."},
                {"jaut": "Cik zīmuļu kopā?", "atb": ["17"],
                 "padoms": "10 + 7."},
            ]),
            pavediens="skola",
            konteksts="Skolotāja lūdz parādīt, kā tu skaitīji.",
            kapec="Pieraksts ļauj citam pārbaudīt tavu domu."),

    Kopsavilkums([
        "Pierakstu rēķinu pa soļiem.",
        "Izskaidroju katru soli.",
        "Pārbaudu, vai katrs «=» patiess.",
    ]),

    Majas([
        "Pieraksti pa soļiem 14 + 5.",
        "Paskaidro mājiniekam katru soli.",
        "Atrodi kļūdu: 13 + 4 = 10 + 3 + 4 = 10 + 6.",
    ]),
]
