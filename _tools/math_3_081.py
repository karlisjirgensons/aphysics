# -*- coding: utf-8 -*-
"""3. klase, 81. stunda: «Kā pieraksta daļu?»

Pirmais daļskaitļa pieraksts. Līdz šim daļu sauca vārdiem; tagad parādās
daļsvītra, skaitītājs un saucējs. Latviešu standartā daļu raksta vertikāli -
skaitītājs virs svītras, saucējs zem tās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā pieraksta daļu?"

MERKIS = ("Lasīsim un pierakstīsim parasto daļu; nosauksim skaitītāju un "
          "saucēju.")

SATURS = [
    Sakums("Kā pierakstīt «trīs no astoņām» ar cipariem?",
           zimejums=dala(8, 3, "3/8", "trīs astotdaļas"),
           paraksts="Virs svītras - cik ņemtas; zem svītras - cik ir pavisam.",
           fakti=["Daļu raksta ar daļsvītru: skaitītājs virs, saucējs zem.",
                  "{3|8} lasa «trīs astotdaļas»."]),

    Doma("Skaitītājs virs svītras, saucējs zem tās",
         "{3|8} nozīmē: veselais sadalīts 8 daļās, no tām ņemtas 3.",
         soli=[
             "Saskaiti, cik vienādu daļu ir pavisam - tas ir saucējs.",
             "Uzraksti to zem daļsvītras.",
             "Saskaiti, cik daļu ir ņemtas - tas ir skaitītājs.",
             "Uzraksti to virs daļsvītras.",
         ],
         pieze="Saucējs nosaka daļas *vārdu*: ar saucēju 4 daļu sauc par "
               "ceturtdaļu, ar saucēju 8 - par astotdaļu."),

    Paraugs("Kā pierakstīt iekrāsoto daļu?",
            uzd="Figūra sadalīta 5 vienādās daļās, 2 no tām iekrāsotas. "
                "Pieraksti iekrāsoto daļu.",
            soli=[
                ("Saucējs ir 5",
                 "Tik vienādu daļu ir pavisam."),
                ("Skaitītājs ir 2",
                 "Tik daļu ir iekrāsotas."),
                ("{2|5}",
                 "Lasa: «divas piektdaļas»."),
            ],
            atbilde="{2|5}"),

    Ievadi("Pieraksti daļu", [
        {"jaut": "Figūrā 4 daļas, iekrāsota 1. Kāds ir saucējs?",
         "atb": ["4"], "padoms": "Cik daļu ir pavisam."},
        {"jaut": "Tajā pašā figūrā - kāds ir skaitītājs?",
         "atb": ["1"], "padoms": "Cik daļu ir iekrāsotas."},
        {"jaut": "Figūrā 10 daļas, iekrāsotas 7. Kāds ir saucējs?",
         "atb": ["10"], "padoms": "Visas daļas."},
        {"jaut": "Tajā pašā figūrā - kāds ir skaitītājs?",
         "atb": ["7"], "padoms": "Iekrāsotās daļas."},
        {"jaut": "Daļā {5|6} - kāds ir saucējs?", "atb": ["6"],
         "padoms": "Skaitlis zem svītras."},
        {"jaut": "Daļā {5|6} - kāds ir skaitītājs?", "atb": ["5"],
         "padoms": "Skaitlis virs svītras."},
    ], pamats=4),

    Zimejums("Viena sestdaļa",
             dala(6, 1, "1/6", "sešas vienādas daļas"),
             paskaidro="Saucējs 6 pasaka daļas vārdu - sestdaļa; skaitītājs 1 "
                       "pasaka, ka ņemta viena.",
             ievads="Tā izskatās {1|6}."),

    Varianti("Kā lasa un raksta daļu?", [
        {"jaut": "Kā lasa {3|4}?",
         "opcijas": ["trīs ceturtdaļas", "četras trešdaļas",
                     "trīs un četri", "trīs dala ar četriem daļām"],
         "pareizi": 0, "padoms": "Vispirms skaitītājs, tad daļas vārds."},
        {"jaut": "Kurš skaitlis daļā ir saucējs?",
         "opcijas": ["Skaitlis zem svītras", "Skaitlis virs svītras",
                     "Lielākais skaitlis", "Mazākais skaitlis"],
         "pareizi": 0, "padoms": "Saucējs sauc daļu vārdā."},
        {"jaut": "Kā pieraksta «piecas astotdaļas»?",
         "opcijas": ["{5|8}", "{8|5}", "5 + 8", "58"],
         "pareizi": 0, "padoms": "Skaitītājs virs svītras."},
        {"jaut": "Figūrā 9 daļas, iekrāsotas 4. Kāda daļa ir iekrāsota?",
         "opcijas": ["{4|9}", "{9|4}", "{5|9}", "{4|5}"],
         "pareizi": 0, "padoms": "4 no 9."},
    ], pamats=4),

    Pasaule("Cik spēļu uzvarēja komanda?",
            Ievadi("", [
                {"jaut": "Komanda spēlēja 10 spēles, uzvarēja 7. Kāds ir "
                         "saucējs daļā?",
                 "atb": ["10"], "padoms": "Visas spēles."},
                {"jaut": "Kāds ir skaitītājs?", "atb": ["7"],
                 "padoms": "Uzvarētās spēles."},
                {"jaut": "Cik spēles komanda zaudēja?", "atb": ["3"],
                 "padoms": "10 − 7."},
                {"jaut": "Otra komanda spēlēja 8 spēles un uzvarēja 5. Cik "
                         "spēles tā zaudēja?",
                 "atb": ["3"], "padoms": "8 − 5."},
            ]),
            pavediens="sports",
            konteksts="Sporta tabulā uzvaras raksta kā daļu no visām "
                      "spēlēm - 7 no 10 jeb {7|10}.",
            kapec="Tikai daļa pasaka, cik labi komanda spēlēja: 7 uzvaras no "
                  "10 un no 30 nav viens un tas pats."),

    Kopsavilkums([
        "Pierakstu parasto daļu ar daļsvītru.",
        "Nosaucu skaitītāju un saucēju.",
        "Lasu daļu pareizi: «trīs ceturtdaļas».",
        "Pierakstu daļu pēc zīmējuma.",
    ]),

    Majas([
        "Uzzīmē figūru un pieraksti, kāda daļa tajā ir iekrāsota.",
        "Uzraksti trīs daļas ar saucēju 8.",
        "Atrodi mājās kaut ko, ko var pierakstīt kā daļu.",
    ]),
]
