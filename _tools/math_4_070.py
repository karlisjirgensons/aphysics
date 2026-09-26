# -*- coding: utf-8 -*-
"""4. klase, 70. stunda: «Kas notiek, reizinot ar 10?»

4.4. temata sākums. Reizinot ar 10, katrs cipars pārceļas vienu šķiru pa
kreisi, un tukšajā vieninieku vietā nostājas 0. Tas nav «pieliek nulli»
triks, bet šķiru likums - to parāda šķiru tabula.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kas notiek, reizinot ar 10?"

MERKIS = ("Modelēsim un paskaidrosim reizinājumu ar 10, 100 un 1000, "
          "izmantojot šķiru modeļus.")

SATURS = [
    Sakums("Kāpēc ar 10 reizināt ir tik viegli?",
           zimejums=restis([["", "T", "S", "D", "V"],
                            ["37", "", "", 3, 7],
                            ["37 · 10", "", 3, 7, 0],
                            ["37 · 100", 3, 7, 0, 0]],
                           "cipari pārceļas pa kreisi"),
           paraksts="Katrs cipars kļūst 10 reizes vērtīgāks.",
           fakti=["3 desmiti kļūst par 3 simtiem, 7 vieni - par 7 desmitiem.",
                  "Tukšo vienu vietu aizpilda nulle."]),

    Doma("Reizinot ar 10, katrs cipars pāriet nākamajā šķirā",
         "Reizinot ar 10, 100 vai 1000, cipari pārvietojas par vienu, divām "
         "vai trim šķirām pa kreisi, un beigās rodas tikpat nuļļu.",
         soli=[
             "· 10: viena šķira pa kreisi, beigās viena 0.",
             "· 100: divas šķiras, divas 0.",
             "· 1000: trīs šķiras, trīs 0.",
             "Pārbaudi ar šķiru tabulu, ja šaubies.",
         ],
         pieze="Tāpēc 45 · 100 = 4500: 4 desmiti kļūst 4 tūkstoši, 5 vieni - "
               "5 simti."),

    Slidnis("37 aug",
            soli=[
                {"v": "37", "teksts": "3 D 7 V", "josla": 1},
                {"v": "37 · 10 = 370", "teksts": "3 S 7 D 0 V", "josla": 10},
                {"v": "37 · 100 = 3700", "teksts": "3 T 7 S 0 D 0 V",
                 "josla": 100},
            ],
            ievads="Josla parāda, cik reižu skaitlis izaudzis."),

    Paraugs("205 · 10",
            uzd="Izrēķini 205 · 10 un paskaidro ar šķirām.",
            soli=[
                ("2 S 0 D 5 V", "Sākotnējais skaitlis."),
                ("2 T 0 S 5 D 0 V", "Katrs cipars par šķiru pa kreisi."),
                ("205 · 10 = 2050", None),
            ],
            atbilde="2050"),

    Ievadi("Reizini ar 10, 100, 1000", [
        {"jaut": "48 · 10 = ?", "atb": ["480"], "padoms": "Viena 0."},
        {"jaut": "48 · 100 = ?", "atb": ["4800"], "padoms": "Divas 0."},
        {"jaut": "7 · 1000 = ?", "atb": ["7000"], "padoms": "Trīs 0."},
        {"jaut": "310 · 10 = ?", "atb": ["3100"],
         "padoms": "Esošā nulle paliek, pieliek vēl vienu."},
        {"jaut": "90 · 100 = ?", "atb": ["9000"], "padoms": "9 · 1000."},
        {"jaut": "? · 10 = 6400", "atb": ["640"],
         "padoms": "Kurš skaitlis, reizināts ar 10, dod 6400?"},
    ], pamats=4),

    Varianti("Kas notiek ar ciparu?", [
        {"jaut": "Skaitlī 56 cipars 5 ir desmiti. Kas tas ir 56 · 100?",
         "opcijas": ["tūkstoši", "simti", "desmiti", "vieni"], "pareizi": 0,
         "padoms": "Divas šķiras pa kreisi."},
        {"jaut": "Cik reižu 3400 ir lielāks nekā 34?",
         "opcijas": ["100", "10", "1000", "2"], "pareizi": 0,
         "padoms": "Divas nulles."},
        {"jaut": "Kurš pieraksts pareizs?",
         "opcijas": ["25 · 100 = 2500", "25 · 100 = 250",
                     "25 · 100 = 25 000", "25 · 100 = 125"], "pareizi": 0,
         "padoms": "Divas nulles."},
        {"jaut": "Kā izmainās 60, reizinot ar 10?",
         "opcijas": ["kļūst 600", "kļūst 70", "kļūst 6000", "kļūst 610"],
         "pareizi": 0, "padoms": "Viena šķira pa kreisi."},
    ], pamats=4),

    Pasaule("Mērvienību pārvēršana",
            Ievadi("", [
                {"jaut": "1 cm = 10 mm. Cik mm ir 34 cm?", "atb": ["340"],
                 "padoms": "34 · 10."},
                {"jaut": "1 m = 100 cm. Cik cm ir 27 m?", "atb": ["2700"],
                 "padoms": "27 · 100."},
                {"jaut": "1 km = 1000 m. Cik m ir 8 km?", "atb": ["8000"],
                 "padoms": "8 · 1000."},
                {"jaut": "1 € = 100 ct. Cik centu ir 45 €?", "atb": ["4500"],
                 "padoms": "45 · 100."},
            ]),
            pavediens="celojums",
            konteksts="Mērvienības ir veidotas ar 10, 100 un 1000 - tāpēc "
                      "pārvēršana ir reizināšana ar šiem skaitļiem.",
            kapec="Viens likums - visas mērvienības."),

    Kopsavilkums([
        "Reizinu ar 10, 100 un 1000.",
        "Paskaidroju to ar šķiru pārvietošanos.",
        "Lietoju to mērvienību pārvēršanai.",
    ]),

    Majas([
        "Pārvērt savu augumu centimetros un milimetros.",
        "Izrēķini, cik centu ir 25 €, 50 € un 99 €.",
        "Paskaidro mājiniekiem, kāpēc reizinot ar 10 «rodas nulle».",
    ]),
]
