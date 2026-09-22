# -*- coding: utf-8 -*-
"""6. klase, 103. stunda: «Kā skaitīt no negatīva skaitļa?»

Skaitīšana ar soli ir pirmais solis uz saskaitīšanu un atņemšanu. Te vēl nav
darbību, ir tikai kustība pa taisni - bet tieši tā vēlāk izskatīsies
«pieskaitīt» un «atņemt».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā skaitīt no negatīva skaitļa?"

MERKIS = ("Skaitīsim uz priekšu un atpakaļ no negatīva skaitļa ar soli 1, 2, "
          "5 un 10.")

SATURS = [
    Sakums("Skaitīšana ir kustība pa taisni",
           zimejums=taisne(-12, 4, 4, [(-10, "sākums"), (-4, "3 soļi")]),
           paraksts="No −10 ar soli 2 uz priekšu: −8, −6, −4. Katrs solis ir "
                    "viens lēciens pa labi.",
           fakti=["Uz priekšu nozīmē pa labi, atpakaļ - pa kreisi.",
                  "Solis var būt 1, 2, 5 vai 10 - likums nemainās.",
                  "Šķērsojot nulli, skaitīšana neapstājas."]),

    Doma("Solis pa labi - pieskaitīt, pa kreisi - atņemt",
         "Skaitot no negatīva skaitļa, katrs solis pa labi palielina skaitli "
         "par soļa lielumu, katrs solis pa kreisi - samazina.",
         soli=[
             "Atzīmē sākuma skaitli uz taisnes.",
             "Nosaki soļa lielumu un virzienu.",
             "Veic soļus pa vienam, pierakstot katru skaitli.",
             "Šķērsojot nulli, turpini kā parasti.",
             "Pārbaudi pēdējo skaitli: sākums plus soļu summa.",
         ],
         pieze="No −10 ar soli 5 uz priekšu: −10, −5, 0, 5, 10. Nulle nav "
               "šķērslis - tā ir tikai viena no pieturām."),

    Paraugs("Skaiti ar soli 5",
            uzd="Sāc no −12 un skaiti uz priekšu ar soli 5. Pieraksti "
                "piecus skaitļus.",
            soli=[
                ("Sākums: −12",
                 "Pirmais skaitlis."),
                ("−12 + 5 = −7",
                 "Solis pa labi."),
                ("−7 + 5 = −2",
                 "Vēl viens solis."),
                ("−2 + 5 = 3",
                 "Šķērsojam nulli."),
                ("3 + 5 = 8",
                 "Piektais skaitlis."),
            ],
            atbilde="−12; −7; −2; 3; 8"),

    Ievadi("Turpini skaitīšanu", [
        {"jaut": "Sāc no −10, solis 2 uz priekšu. Kāds ir otrais skaitlis?",
         "atb": ["-8", "−8"], "padoms": "−10 + 2."},
        {"jaut": "Sāc no −10, solis 5 uz priekšu. Kāds ir trešais skaitlis?",
         "atb": ["0"], "padoms": "−10, −5, 0."},
        {"jaut": "Sāc no −3, solis 1 atpakaļ. Kāds ir trešais skaitlis?",
         "atb": ["-5", "−5"], "padoms": "−3, −4, −5."},
        {"jaut": "Sāc no 5, solis 10 atpakaļ. Kāds ir otrais skaitlis?",
         "atb": ["-5", "−5"], "padoms": "5 − 10."},
        {"jaut": "Sāc no −20, solis 10 uz priekšu. Kāds ir ceturtais "
                 "skaitlis?",
         "atb": ["10"], "padoms": "−20, −10, 0, 10."},
        {"jaut": "Sāc no −1, solis 2 atpakaļ. Kāds ir ceturtais skaitlis?",
         "atb": ["-7", "−7"], "padoms": "−1, −3, −5, −7."},
    ], pamats=4),

    Pasaule("Cik dziļi nolaižas lifts?",
            Kustiba("", [
                {"jaut": "Lifts ir −5 stāvā un paceļas par 3 stāviem. Kurā "
                         "stāvā tas ir?",
                 "atb": -2, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "stāvs", "merkis": "mērķa stāvs", "objekts": "Lifts",
                 "padoms": "−5 + 3."},
                {"jaut": "No −2 tas nolaižas par 6 stāviem. Kurā stāvā tas "
                         "ir?",
                 "atb": -8, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "stāvs", "merkis": "mērķa stāvs", "objekts": "Lifts",
                 "padoms": "−2 − 6."},
                {"jaut": "No −8 tas paceļas par 10 stāviem. Kurā stāvā tas "
                         "ir?",
                 "atb": 2, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "stāvs", "merkis": "mērķa stāvs", "objekts": "Lifts",
                 "padoms": "−8 + 10."},
                {"jaut": "No 2 tas nolaižas par 5 stāviem. Kurā stāvā tas "
                         "ir?",
                 "atb": -3, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "stāvs", "merkis": "mērķa stāvs", "objekts": "Lifts",
                 "padoms": "2 − 5."},
            ]),
            pavediens="maja",
            konteksts="Lifts kustas pa skaitļu taisni: pagrabstāvi ir zem "
                      "nulles, dzīvokļi - virs tās.",
            kapec="Katrs stāvs ir viens solis, arī šķērsojot nulli."),

    Varianti("Kurā virzienā?", [
        {"jaut": "Solis uz priekšu uz skaitļu taisnes nozīmē...",
         "opcijas": ["pa labi", "pa kreisi", "uz augšu", "uz leju"],
         "pareizi": 0,
         "padoms": "Skaitļi aug pa labi."},
        {"jaut": "No −6 ar soli 2 uz priekšu trešais skaitlis ir...",
         "opcijas": ["−2", "−4", "0", "2"],
         "pareizi": 0,
         "padoms": "−6, −4, −2."},
        {"jaut": "Kas notiek, šķērsojot nulli?",
         "opcijas": ["Nekas - skaitīšana turpinās",
                     "Skaitīšana apstājas",
                     "Solis mainās", "Zīme pazūd"],
         "pareizi": 0,
         "padoms": "Nulle ir tikai viena pietura."},
        {"jaut": "No 3 ar soli 10 atpakaļ otrais skaitlis ir...",
         "opcijas": ["−7", "−13", "13", "−17"],
         "pareizi": 0,
         "padoms": "3 − 10."},
    ], pamats=4),

    Zimejums("Soļi pa taisni",
             taisne(-10, 10, 5, [(-10, "sākums"), (-5, "1."), (0, "2."),
                                 (5, "3.")]),
             paskaidro="No −10 ar soli 5: trīs soļi noved pie 5. Nulle ir "
                       "viena no pieturām.",
             ievads="Katrs solis ir vienāds lēciens."),

    Kopsavilkums([
        "Skaitu uz priekšu un atpakaļ no negatīva skaitļa.",
        "Lietoju soli 1, 2, 5 un 10.",
        "Turpinu skaitīšanu, šķērsojot nulli.",
        "Saistu soļus pa labi ar pieskaitīšanu, pa kreisi - ar atņemšanu.",
    ]),

    Majas([
        "Sāc no −15 un skaiti ar soli 5 uz priekšu līdz 15.",
        "Sāc no 4 un skaiti ar soli 3 atpakaļ, pierakstot piecus skaitļus.",
        "Pieraksti, cik soļu vajag no −12 līdz 0 ar soli 4.",
    ]),
]
