# -*- coding: utf-8 -*-
"""4. klase, 12. stunda: «Kā saskaitīt galvā?»

Galvas rēķins četrciparu skaitļiem strādā tikai vienkāršos gadījumos - kad
mainās viena vai divas šķiras. Tieši tos stunda trenē: 3400 + 2500,
6000 − 1200, 4990 + 10. Pārējo rēķinās rakstos nākamajā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, kolonnas)

TEMA = "Kā saskaitīt galvā?"

MERKIS = ("Saskaitīsim un atņemsim četrciparu skaitļus galvā vienkāršos "
          "gadījumos, izmantojot decimālo sastāvu.")

SATURS = [
    Sakums("Cik maksā ceļojums uz Itāliju?",
           zimejums=kolonnas([("lidmašīna", 1200), ("viesnīca", 2300)],
                             " €"),
           paraksts="1200 + 2300 = 3500 - bez zīmuļa.",
           fakti=["Pilnus simtus var saskaitīt kā mazus skaitļus: 12 + 23.",
                  "Tikai beigās pieliek divas nulles."]),

    Doma("Saskaiti vienādas šķiras kopā",
         "Galvā rēķina pa šķirām: tūkstošus ar tūkstošiem, simtus ar "
         "simtiem.",
         soli=[
             "Sadali otru skaitli šķirās: 2300 = 2000 + 300.",
             "Pieskaiti tūkstošus: 1200 + 2000 = 3200.",
             "Pieskaiti simtus: 3200 + 300 = 3500.",
             "Ja skaitlis ir tuvu apaļam, izmanto to: 4990 + 10 = 5000.",
         ],
         pieze="Atņemot tāpat: 6500 − 1200 = 5500 − 200 = 5300."),

    Paraugs("5800 + 700",
            uzd="Izrēķini galvā 5800 + 700.",
            soli=[
                ("5800 + 200 = 6000",
                 "Vispirms līdz apaļam tūkstotim."),
                ("700 − 200 = 500",
                 "Tik vēl jāpieskaita."),
                ("6000 + 500 = 6500", None),
            ],
            atbilde="6500"),

    Slidnis("Pa šķirām: 7400 − 2600",
            soli=[
                {"v": "7400", "teksts": "Sākam.", "josla": 74},
                {"v": "7400 − 2000 = 5400", "teksts": "Atņem tūkstošus.",
                 "josla": 54},
                {"v": "5400 − 400 = 5000", "teksts": "Atņem simtus līdz "
                 "apaļam.", "josla": 50},
                {"v": "5000 − 200 = 4800", "teksts": "Atlikušos 200 - gatavs.",
                 "josla": 48},
            ],
            ievads="600 sadala 400 + 200, lai iet caur apaļu skaitli."),

    Ievadi("Galvā!", [
        {"jaut": "3000 + 4000 = ?", "atb": ["7000"], "padoms": "3 + 4 "
         "tūkstoši."},
        {"jaut": "2500 + 3400 = ?", "atb": ["5900"],
         "padoms": "25 + 34 simti."},
        {"jaut": "6000 − 1500 = ?", "atb": ["4500"],
         "padoms": "60 − 15 simti."},
        {"jaut": "4990 + 10 = ?", "atb": ["5000"],
         "padoms": "Līdz apaļam tūkstotim."},
        {"jaut": "8300 − 900 = ?", "atb": ["7400"],
         "padoms": "8300 − 300 − 600."},
        {"jaut": "1750 + 250 = ?", "atb": ["2000"],
         "padoms": "50 + 50 = 100, 700 + 200 + 100 = 1000."},
        {"jaut": "9000 − 1 = ?", "atb": ["8999"],
         "padoms": "Viens mazāk par apaļu."},
        {"jaut": "5600 + 3400 = ?", "atb": ["9000"],
         "padoms": "56 + 34 simti."},
    ], pamats=6),

    Varianti("Kurš ceļš vieglāks?", [
        {"jaut": "Kā ērtāk izrēķināt 3998 + 2500?",
         "opcijas": ["4000 + 2500 − 2", "3998 + 2000 + 5",
                     "3000 + 2000 + 998", "stabiņā"], "pareizi": 0,
         "padoms": "3998 ir 4000 bez diviem."},
        {"jaut": "Cik ir 7200 − 200?",
         "opcijas": ["7000", "5200", "7000 − 2", "6800"], "pareizi": 0,
         "padoms": "Atņem divus simtus."},
        {"jaut": "Kurš rēķins ir tas pats, kas 4500 + 3500?",
         "opcijas": ["45 + 35 simti", "45 + 35", "4 + 3 tūkstoši",
                     "450 + 350"], "pareizi": 0,
         "padoms": "Abi ir pilni simti."},
        {"jaut": "Kurā gadījumā galvā ir grūti?",
         "opcijas": ["3847 + 2586", "3000 + 2000", "4500 + 500",
                     "6000 − 1000"], "pareizi": 0,
         "padoms": "Visās šķirās neapaļi cipari - labāk stabiņā."},
    ], pamats=4),

    Pasaule("Budžets ģimenes ceļojumam",
            Ievadi("", [
                {"jaut": "Lidojums 1200 €, viesnīca 2300 €. Cik kopā?",
                 "atb": ["3500"], "padoms": "12 + 23 simti."},
                {"jaut": "Ēdienam atliek 800 €. Cik viss ceļojums?",
                 "atb": ["4300"], "padoms": "3500 + 800."},
                {"jaut": "Krājumā ir 5000 €. Cik paliks pēc ceļojuma?",
                 "atb": ["700"], "padoms": "5000 − 4300."},
                {"jaut": "Ja viesnīca maksātu par 500 € mazāk, cik būtu "
                         "viss?",
                 "atb": ["3800"], "padoms": "4300 − 500."},
            ]),
            pavediens="celojums",
            konteksts="Ģimene plāno braucienu - lielās summas ir apaļas, "
                      "tāpēc tās var saskaitīt galvā.",
            kapec="Galvas rēķins palīdz uzreiz saprast, vai nauda "
                  "pietiek."),

    Kopsavilkums([
        "Saskaitu un atņemu pilnus simtus un tūkstošus galvā.",
        "Izmantoju apaļus skaitļus kā pieturas punktus.",
        "Zinu, kad galvā ir par grūtu un labāk rakstīt.",
    ]),

    Majas([
        "Sastādi iedomāta ceļojuma budžetu no trim apaļām summām un "
        "saskaiti galvā.",
        "Izrēķini galvā, cik gadu pagājis kopš 1990. gada.",
        "Pajautā mājiniekiem 3 galvas rēķinus un pārbaudi viņu atbildes.",
    ]),
]
