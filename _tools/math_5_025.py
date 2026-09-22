# -*- coding: utf-8 -*-
"""5. klase, 25. stunda: «Vai vienādība ir patiesa?»

Divi pieraksti, kas izskatās gandrīz vienādi - 36 : 4 · 9 un 36 : (4 · 9) -,
bet dod dažādas atbildes. Stunda ir par to, ka iekavas nav rotājums, un par
vispārinājumu, ko no šī piemēra var izdarīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Vai vienādība ir patiesa?"

MERKIS = ("Mācīsimies noteikt, vai vienādība ir patiesa, un formulēt "
          "vispārinājumu par iekavām reizināšanā un dalīšanā.")

SATURS = [
    Sakums("Divi pieraksti, viena atšķirība",
           fakti=["36 : 4 · 9 - vai tas ir 81?",
                  "36 : (4 · 9) - vai tas ir 1?",
                  "Atšķiras tikai iekavas. Atbildes atšķiras daudzkārt."]),

    Doma("Vienādas pakāpes darbības pilda pēc kārtas",
         "Reizināšanu un dalīšanu izpilda no kreisās uz labo - ja vien "
         "iekavas nepasaka citādi.",
         soli=[
             "Atrodi iekavas - to saturu rēķina vispirms.",
             "Ja iekavu nav, ej no kreisās uz labo.",
             "Izrēķini abas vienādības puses atsevišķi.",
             "Salīdzini: ja puses sakrīt, vienādība ir patiesa.",
         ],
         pieze="Tāpēc 36 : 4 · 9 = 81, bet 36 : (4 · 9) = 1. Reizinājumam "
               "iekavas neko nemaina - 2 · 3 · 4 vienmēr ir 24 -, bet "
               "dalīšanā tās maina visu."),

    Paraugs("Pārbaudi abas puses",
            uzd="Vai vienādība 36 : 4 · 9 = 36 : (4 · 9) ir patiesa?",
            soli=[
                ("Kreisā puse: 36 : 4 = 9",
                 "Iekavu nav, tāpēc no kreisās uz labo."),
                ("9 · 9 = 81",
                 "Kreisā puse ir 81."),
                ("Labā puse: 4 · 9 = 36",
                 "Vispirms iekavas."),
                ("36 : 36 = 1",
                 "Labā puse ir 1."),
                ("81 ≠ 1, tāpēc vienādība nav patiesa",
                 "Atšķirību radīja iekavas."),
            ],
            atbilde="nav patiesa: 81 ≠ 1"),

    Ievadi("Izrēķini un salīdzini", [
        {"jaut": "Cik ir 36 : 4 · 9?", "atb": ["81"],
         "padoms": "No kreisās uz labo."},
        {"jaut": "Cik ir 36 : (4 · 9)?", "atb": ["1"],
         "padoms": "Vispirms iekavas."},
        {"jaut": "Cik ir 100 : 5 · 2?", "atb": ["40"],
         "padoms": "100 : 5 = 20."},
        {"jaut": "Cik ir 100 : (5 · 2)?", "atb": ["10"],
         "padoms": "5 · 2 = 10."},
        {"jaut": "Cik ir 48 : 6 : 2?", "atb": ["4"],
         "padoms": "48 : 6 = 8, tad 8 : 2."},
        {"jaut": "Cik ir 48 : (6 : 2)?", "atb": ["16"],
         "padoms": "6 : 2 = 3."},
        {"jaut": "Cik ir 2 · 3 · 4?", "atb": ["24"],
         "padoms": "Secība te neko nemaina."},
        {"jaut": "Cik ir 2 · (3 · 4)?", "atb": ["24"],
         "padoms": "Tas pats - reizinājumam iekavas nekaitē."},
    ], pamats=4,
        ievads="Vispirms iekavas, pēc tam no kreisās uz labo."),

    Varianti("Formulē vispārinājumu", [
        {"jaut": "Kad iekavas reizinājumā maina rezultātu?",
         "opcijas": ["Nekad", "Vienmēr", "Ja skaitļi ir lieli",
                     "Ja reizinātāju ir trīs"],
         "pareizi": 0,
         "padoms": "Pārbaudi 2 · 3 · 4 un 2 · (3 · 4)."},
        {"jaut": "Kad iekavas dalījumā maina rezultātu?",
         "opcijas": ["Gandrīz vienmēr", "Nekad",
                     "Tikai ar nepāra skaitļiem",
                     "Tikai tad, ja atbilde ir apaļa"],
         "pareizi": 0,
         "padoms": "36 : 4 · 9 un 36 : (4 · 9)."},
        {"jaut": "Kura vienādība ir patiesa?",
         "opcijas": ["24 : 6 : 2 = 2", "24 : 6 : 2 = 8",
                     "24 : (6 : 2) = 2", "24 : 6 · 2 = 2"],
         "pareizi": 0,
         "padoms": "24 : 6 = 4, tad 4 : 2."},
        {"jaut": "Ko nozīmē zīme ≠?",
         "opcijas": ["Puses nav vienādas", "Puses ir vienādas",
                     "Jārēķina tālāk", "Atbilde ir aptuvena"],
         "pareizi": 0,
         "padoms": "Tā ir pārsvītrota vienādības zīme."},
    ], pamats=4),

    Pasaule("Vai čekā viss ir pareizi?",
            Ievadi("", [
                {"jaut": "60 eiro dala 3 cilvēki, katrs pieliek 2 eiro "
                         "dzeramnaudas: 60 : 3 + 2. Cik maksā viens?",
                 "atb": ["22"], "padoms": "60 : 3 = 20, tad + 2."},
                {"jaut": "Ja dzeramnauda 6 eiro ir kopīga: (60 + 6) : 3. Cik "
                         "maksā viens?",
                 "atb": ["22"], "padoms": "66 : 3."},
                {"jaut": "120 eiro dala ar 4 un tad ar 2: 120 : 4 : 2. Cik "
                         "sanāk?",
                 "atb": ["15"], "padoms": "120 : 4 = 30."},
                {"jaut": "Un cik sanāk 120 : (4 : 2)?",
                 "atb": ["60"], "padoms": "4 : 2 = 2."},
            ]),
            pavediens="veikals",
            konteksts="Kopīgu čeku dalot, viena iekava izšķir, vai maksā "
                      "katrs par sevi vai visi kopā.",
            kapec="Iekava pasaka, kas notiek vispirms - un tas maina summu."),

    Kopsavilkums([
        "Nosaku, vai vienādība ir patiesa, izrēķinot abas puses.",
        "Zinu, ka reizināšanu un dalīšanu pilda no kreisās uz labo.",
        "Zinu, ka iekavas reizinājumā neko nemaina, bet dalījumā maina visu.",
        "Lietoju zīmi ≠, ja puses nav vienādas.",
    ]),

    Majas([
        "Uzraksti divas izteiksmes ar tiem pašiem skaitļiem, kuras atšķiras "
        "tikai ar iekavām.",
        "Izrēķini abas un paskaties, cik liela ir atšķirība.",
        "Atrodi izteiksmi, kurai iekavas neko nemaina, un paskaidro kāpēc.",
    ]),
]
