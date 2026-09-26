# -*- coding: utf-8 -*-
"""3. klase, 134. stunda: «Cik ir desmit simtu?»

Mikrotemata noslēgums un robežas pāreja: desmit simti veido tūkstoti, un
skaitļu rinda turpinās tālāk. Modelis ir tas pats, kas visai decimālajai
sistēmai - desmit vienādas vienības veido nākamo, lielāko.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Cik ir desmit simtu?"

MERKIS = ("Skaidrosim, ka desmit simti veido tūkstoti, un modelēsim to.")

SATURS = [
    Sakums("Kas notiek pēc 999?",
           zimejums=restis([["10 vieni", "=", "1 desmits"],
                            ["10 desmiti", "=", "1 simts"],
                            ["10 simti", "=", "1 tūkstotis"]],
                           "katra vienība no desmit mazākām"),
           paraksts="Katra nākamā vienība sastāv no desmit iepriekšējām.",
           fakti=["Desmit simti ir viens tūkstotis.",
                  "1000 ir pirmais četrciparu skaitlis."]),

    Doma("Desmit vienādas vienības veido nākamo",
         "Desmit vieni ir desmits, desmit desmiti ir simts, desmit simti ir "
         "tūkstotis.",
         soli=[
             "Saskaiti simtus: 100, 200, ... 900.",
             "Pieskaiti vēl vienu simtu.",
             "Sanāk 1000 - jauna vienība.",
             "Skaitlim parādās ceturtā vieta - tūkstoši.",
         ],
         pieze="Tieši tāpēc 999 + 1 = 1000: vieni pārplūst desmitos, desmiti "
               "simtos, simti tūkstošos - visas trīs vietas reizē."),

    Slidnis("No simta līdz tūkstotim",
            soli=[
                {"v": "100", "teksts": "Viens simts.", "josla": 10},
                {"v": "500", "teksts": "Pieci simti.", "josla": 50},
                {"v": "900", "teksts": "Deviņi simti.", "josla": 90},
                {"v": "1000", "teksts": "Desmit simti - viens tūkstotis.",
                 "josla": 100},
            ],
            ievads="Katrs solis pieliek simtus."),

    Paraugs("Cik ir 999 + 1?",
            uzd="Izrēķini 999 + 1 un paskaidro, kas notiek ar cipariem.",
            soli=[
                ("9 vieni + 1 = 10 vieni",
                 "Vieni pārplūst: paliek 0, desmitos aiziet 1."),
                ("9 desmiti + 1 = 10 desmitu",
                 "Desmiti pārplūst: paliek 0, simtos aiziet 1."),
                ("9 simti + 1 = 10 simtu = 1 tūkstotis",
                 "Sanāk 1000."),
            ],
            atbilde="1000"),

    Ievadi("Simti un tūkstoši", [
        {"jaut": "Cik simtu ir vienā tūkstotī?", "atb": ["10"],
         "padoms": "Desmit simti."},
        {"jaut": "Cik desmitu ir vienā simtā?", "atb": ["10"],
         "padoms": "Desmit desmiti."},
        {"jaut": "Cik desmitu ir vienā tūkstotī?", "atb": ["100"],
         "padoms": "10 · 10."},
        {"jaut": "Cik ir 999 + 1?", "atb": ["1000"],
         "padoms": "Visas vietas pārplūst."},
        {"jaut": "Cik ir 1000 − 1?", "atb": ["999"],
         "padoms": "Pretējā darbība."},
        {"jaut": "Cik simtu ir 2000?", "atb": ["20"],
         "padoms": "2 · 10."},
    ], pamats=4),

    Zimejums("Kā aug vietas",
             restis([["vieni", "desmiti", "simti", "tūkstoši"],
                     [1, 10, 100, 1000]],
                    "katra nākamā 10 reizes lielāka"),
             paskaidro="Katra vieta ir tieši 10 reizes lielāka par "
                       "iepriekšējo - tāpēc reizināšana ar 10 pievieno nulli.",
             ievads="Četras vietas, viens noteikums."),

    Varianti("Cik tur ir?", [
        {"jaut": "Cik simtu ir vienā tūkstotī?",
         "opcijas": ["10", "100", "1000", "5"],
         "pareizi": 0, "padoms": "Desmit simti."},
        {"jaut": "Cik ir 999 + 1?",
         "opcijas": ["1000", "9910", "100", "9991"],
         "pareizi": 0, "padoms": "Visas vietas pārplūst."},
        {"jaut": "Cik simtu ir 1500?",
         "opcijas": ["15", "5", "150", "1,5"],
         "pareizi": 0, "padoms": "Aizsedz divus pēdējos ciparus."},
        {"jaut": "Cik reižu 1000 ir lielāks par 100?",
         "opcijas": ["10", "100", "900", "2"],
         "pareizi": 0, "padoms": "1000 : 100."},
    ], pamats=4),

    Pasaule("Cik tālu ir orbīta?",
            Ievadi("", [
                {"jaut": "Satelīts riņķo 400 km augstumā. Cik simtu "
                         "kilometru tas ir?",
                 "atb": ["4"], "padoms": "400 : 100."},
                {"jaut": "Cits satelīts ir 1000 km augstumā. Cik simtu "
                         "kilometru?",
                 "atb": ["10"], "padoms": "1000 : 100."},
                {"jaut": "Par cik kilometriem otrs ir augstāk?",
                 "atb": ["600"], "padoms": "1000 − 400."},
                {"jaut": "Trešais ir 2000 km augstumā. Cik reižu augstāk par "
                         "pirmo?",
                 "atb": ["5"], "padoms": "2000 : 400."},
            ]),
            pavediens="kosmoss",
            konteksts="Orbītas augstumu mēra simtos un tūkstošos kilometru - "
                      "un šīs vienības aug tieši pa desmit.",
            kapec="Desmitu sistēma ļauj lielus skaitļus lasīt bez "
                  "kalkulatora."),

    Kopsavilkums([
        "Zinu, ka desmit simti veido tūkstoti.",
        "Modelēju pāreju no 999 uz 1000.",
        "Zinu, cik desmitu ir simtā un tūkstotī.",
        "Pārrēķinu skaitļus simtos.",
    ]),

    Majas([
        "Saskaiti pa simtiem no 100 līdz 1000.",
        "Izrēķini, cik simtu ir 700, 1200 un 2500.",
        "Uzraksti, kas notiek ar cipariem, pieskaitot 1 skaitlim 999.",
    ]),
]
