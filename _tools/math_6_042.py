# -*- coding: utf-8 -*-
"""6. klase, 42. stunda: «Kā reizina rakstos?»

Algoritma stunda. Rakstu reizināšana decimāldaļām neatšķiras no veselajiem
skaitļiem - vienīgā atšķirība ir pēdējais solis. Tāpēc stunda beidzas ar to,
ka algoritmu formulē paši skolēni, vienā teikumā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā reizina rakstos?"

MERKIS = ("Mācīsimies reizināt decimāldaļas rakstos un formulēt algoritmu.")

SATURS = [
    Sakums("Komatu neliek rindās - to liek beigās",
           zimejums=restis([["", "1", "2", "5"],
                            ["·", "", "", "4"],
                            ["", "5", "0", "0"]]),
           paraksts="1,25 · 0,4: vispirms 125 · 4 = 500, tikai tad komats "
                    "trīs vietās - 0,500.",
           fakti=["Rakstos skaitļus līdzina pa labi, nevis pēc komata.",
                  "Komatu ieliek pašās beigās, saskaitot ciparus."]),

    Doma("Reizini kā veselus, tad ieliec komatu",
         "Decimāldaļas rakstos reizina tāpat kā veselus skaitļus, un komatu "
         "rezultātā ieliek, atskaitot tik ciparu, cik to ir abos "
         "reizinātājos kopā.",
         soli=[
             "Pieraksti skaitļus vienu zem otra, līdzinot pa labi.",
             "Neievēro komatus un reizini kā veselus skaitļus.",
             "Saskaiti ciparus aiz komata abos reizinātājos.",
             "Atskaiti tik ciparu rezultātā no labās puses un liec komatu.",
             "Ja ciparu nepietiek, priekšā pieraksti nulles.",
         ],
         pieze="0,02 · 0,3: 2 · 3 = 6, bet aiz komata jābūt trim cipariem. "
               "Tāpēc raksta 0,006 - divas nulles ir jāpieliek."),

    Paraugs("Reizini rakstos",
            uzd="Cik ir 3,6 · 0,25?",
            soli=[
                ("36 · 25 = 900",
                 "Reizina kā veselus skaitļus."),
                ("3,6 - viens cipars; 0,25 - divi",
                 "Kopā trīs cipari aiz komata."),
                ("0,900",
                 "Atskaita trīs ciparus no labās puses."),
                ("= 0,9",
                 "Nulles beigās nemaina vērtību."),
            ],
            atbilde="0,9"),

    Ievadi("Reizini rakstos", [
        {"jaut": "Cik ir 2,4 · 1,5?",
         "atb": ["3,6", "3.6"], "padoms": "24 · 15 = 360; divi cipari."},
        {"jaut": "Cik ir 0,8 · 0,35?",
         "atb": ["0,28", "0.28"], "padoms": "8 · 35 = 280; trīs cipari."},
        {"jaut": "Cik ir 12,5 · 0,4?",
         "atb": ["5"], "padoms": "125 · 4 = 500; divi cipari."},
        {"jaut": "Cik ir 0,02 · 0,3?",
         "atb": ["0,006", "0.006"], "padoms": "2 · 3 = 6; trīs cipari."},
        {"jaut": "Cik ir 4,05 · 0,2?",
         "atb": ["0,81", "0.81"], "padoms": "405 · 2 = 810; trīs cipari."},
        {"jaut": "Cik ir 1,08 · 2,5?",
         "atb": ["2,7", "2.7"], "padoms": "108 · 25 = 2700; trīs cipari."},
    ], pamats=4,
        ievads="Pirms rēķina pasaki, cik ciparu būs aiz komata."),

    Varianti("Kā pareizi pierakstīt?", [
        {"jaut": "Kā līdzina skaitļus, reizinot rakstos?",
         "opcijas": ["Pa labi, neievērojot komatu",
                     "Pēc komata", "Pa kreisi", "Pēc pirmā cipara"],
         "pareizi": 0,
         "padoms": "Komats šeit netiek ņemts vērā."},
        {"jaut": "0,05 · 0,02 rezultātā ir cik ciparu aiz komata?",
         "opcijas": ["4", "2", "3", "1"],
         "pareizi": 0,
         "padoms": "2 + 2."},
        {"jaut": "Cik ir 0,05 · 0,02?",
         "opcijas": ["0,001", "0,01", "0,0001", "0,1"],
         "pareizi": 0,
         "padoms": "5 · 2 = 10; četri cipari dod 0,0010."},
        {"jaut": "Ko darīt, ja ciparu rezultātā nepietiek?",
         "opcijas": ["Pierakstīt nulles priekšā",
                     "Pierakstīt nulles beigās",
                     "Noapaļot", "Atmest komatu"],
         "pareizi": 0,
         "padoms": "0,006 - nulles ir priekšā."},
    ], pamats=4),

    Zimejums("Kur atskaita ciparus",
             restis([["0", ",", "9", "0", "0"]],
                    "trīs cipari no labās puses"),
             paskaidro="3,6 · 0,25 = 0,900. Atskaita trīs ciparus un liek "
                       "komatu - pārējais ir jau izrēķināts.",
             ievads="Pēdējais solis vienmēr ir viens un tas pats."),

    Pasaule("Cik maksā materiāls?",
            Ievadi("", [
                {"jaut": "Auduma metrs maksā 4,8 €. Cik eiro maksā 2,5 m?",
                 "atb": ["12"], "padoms": "48 · 25 = 1200; divi cipari."},
                {"jaut": "Krāsas litrs maksā 12,4 €. Cik eiro maksā 0,75 l?",
                 "atb": ["9,3", "9.3"], "padoms": "124 · 75 = 9300."},
                {"jaut": "Flīzes kvadrātmetrs maksā 15,5 €. Cik eiro maksā "
                         "3,2 m²?",
                 "atb": ["49,6", "49.6"], "padoms": "155 · 32 = 4960."},
                {"jaut": "Līstes metrs maksā 2,35 €. Cik eiro maksā 4 m?",
                 "atb": ["9,4", "9.4"], "padoms": "235 · 4 = 940."},
            ]),
            pavediens="maja",
            konteksts="Būvmateriālu veikalā cenu reizina ar daudzumu, un abi "
                      "skaitļi parasti ir ar komatu.",
            kapec="Viena komata kļūda maina rēķinu desmit reižu."),

    Kopsavilkums([
        "Reizinu decimāldaļas rakstos kā veselus skaitļus.",
        "Nosaku komata vietu, saskaitot ciparus aiz komata.",
        "Pierakstu nulles priekšā, ja ciparu nepietiek.",
        "Formulēju algoritmu vienā teikumā.",
    ]),

    Majas([
        "Izrēķini rakstos 6,25 · 0,8 un 0,04 · 1,5.",
        "Pieraksti algoritmu saviem vārdiem trijos soļos.",
        "Atrodi mājās divas cenas un sareizini tās rakstos.",
    ]),
]
