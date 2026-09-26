# -*- coding: utf-8 -*-
"""2. klase, 79. stunda: «Kā pierakstīt starprezultātus?»

Divi pieraksta veidi: atsevišķi (1) 25 + 17 = 42; 2) 60 − 42 = 18) un
saistītajā pierakstā vienā rindā: 60 − (25 + 17) = 60 − 42 = 18. Saistītais
pieraksts ir īsāks, bet katrai vienādības zīmei jābūt patiesai.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pierakstīt starprezultātus?"

MERKIS = ("Šodien pierakstīsim starprezultātus atsevišķi un saistītajā "
          "pierakstā.")

SATURS = [
    Sakums("Kā pierakstīt aprēķinu vienā rindā bez kļūdām?",
           fakti=["60 − (25 + 17) = 60 − 42 = 18.",
                  "Katra «=» zīme savieno vienādas lietas.",
                  "Tā ir saistītais pieraksts."]),

    Doma("Saistītais pieraksts",
         "Katrā solī izteiksmi pārraksta, aizstājot izrēķināto ar skaitli.",
         soli=[
             "Uzraksti izteiksmi.",
             "«=» un to pašu, tikai 1. darbības vietā - tās rezultāts.",
             "«=» un vērtība.",
             "Pārbaudi: vai katrs gabals starp «=» ir vienāds?",
         ],
         pieze="Nepareizi: 25 + 17 = 42 − 60 = 18. Te 42 nav vienāds ar 18!"),

    Paraugs("Divi pieraksti",
            uzd="Aprēķini 75 − 30 + 12.",
            soli=[("Atsevišķi: 1) 75 − 30 = 45; 2) 45 + 12 = 57",
                   "Katra darbība savā rindā."),
                  ("Saistīti: 75 − 30 + 12 = 45 + 12 = 57",
                   "Viss vienā rindā.")],
            atbilde="57"),

    Ievadi("Aizpildi pierakstu", [
        {"jaut": "80 − (26 + 14) = 80 − ? = 40", "atb": ["40"],
         "padoms": "26 + 14."},
        {"jaut": "33 + 27 − 15 = ? − 15 = 45", "atb": ["60"],
         "padoms": "33 + 27."},
        {"jaut": "90 − 45 − 25 = 45 − 25 = ?", "atb": ["20"],
         "padoms": "45 − 25."},
        {"jaut": "56 − (30 − 4) = 56 − ? = 30", "atb": ["26"],
         "padoms": "30 − 4."},
    ]),

    Varianti("Vai pieraksts ir pareizs?", [
        {"jaut": "40 + 20 = 60 − 15 = 45",
         "opcijas": ["Nē - 60 nav 45", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Starp «=» jābūt vienādam."},
        {"jaut": "40 + 20 − 15 = 60 − 15 = 45",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Visi gabali ir 45."},
    ]),

    Pasaule("Pārgājiena kilometri",
            Ievadi("", [
                {"jaut": "Maršruts 50 km. Pirmajā dienā 18 km, otrajā 17 km. "
                         "Cik atlicis? 50 − (18 + 17) = 50 − 35 = ?",
                 "atb": ["15"], "mers": "km", "padoms": "50 − 35."},
            ]),
            pavediens="celojums",
            konteksts="Pārgājienā kilometrus skaita katru vakaru.",
            kapec="Saistītais pieraksts ir īss un skaidrs."),

    Kopsavilkums([
        "Pierakstu starprezultātus atsevišķi.",
        "Pierakstu tos saistītajā pierakstā.",
        "Pārbaudu, vai katra «=» zīme ir patiesa.",
    ]),

    Majas([
        "Aprēķini divos pierakstos: 70 − (22 + 18).",
        "Atrodi kļūdu: 30 + 5 = 35 − 10 = 25.",
        "Uzraksti to pareizi.",
    ]),
]
