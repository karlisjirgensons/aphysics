# -*- coding: utf-8 -*-
"""3. klase, 142. stunda: «Kā atņemt pilnus simtus?»

Atņemšana 1000 apjomā sākas tāpat kā saskaitīšana - ar vieglāko gadījumu.
Pilnus simtus atņem tāpat kā vienus, un skolēns pats formulē paņēmienu,
kuru lietos visā atlikušajā mikrotematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā atņemt pilnus simtus?"

MERKIS = ("Atņemsim pilnus simtus un desmitus un skaidrosim savu paņēmienu.")

SATURS = [
    Sakums("Ja 8 − 5 = 3, tad cik ir 800 − 500?",
           zimejums=restis([[8, "−", 5, "=", 3],
                            [80, "−", 50, "=", 30],
                            [800, "−", 500, "=", 300]],
                           "viens rēķins, trīs vietas"),
           paraksts="Simtus atņem tāpat kā vienus.",
           fakti=["8 simti mīnus 5 simti ir 3 simti.",
                  "Atņemt var tikai vienādas vienības."]),

    Doma("Atņem vienādas vienības",
         "800 − 500 ir 8 simti mīnus 5 simti - tas pats, kas 8 − 5, tikai "
         "simtos.",
         soli=[
             "Nosauc, cik vienību ir katrā skaitlī.",
             "Atņem tās kā parastus skaitļus.",
             "Pieraksti rezultātu tajā pašā vienībā.",
             "Pārbaudi ar saskaitīšanu.",
         ],
         pieze="Ja skaitļi nav apaļi, tos sadala: 750 − 300 ir 700 − 300 un "
               "vēl 50, tātad 450."),

    Slidnis("Kā sarūk skaitlis",
            soli=[
                {"v": "800", "teksts": "Sākums.", "josla": 100},
                {"v": "− 200 = 600", "teksts": "Atņem divus simtus.",
                 "josla": 75},
                {"v": "− 200 = 400", "teksts": "Vēl divus.", "josla": 50},
                {"v": "− 400 = 0", "teksts": "Un atlikušos četrus.",
                 "josla": 0},
            ],
            ievads="Katrs solis atņem pilnus simtus."),

    Paraugs("Cik ir 750 − 300?",
            uzd="Izrēķini 750 − 300.",
            soli=[
                ("700 − 300 = 400",
                 "Atņem simtus."),
                ("Paliek vēl 50",
                 "Desmiti nemainās."),
                ("400 + 50 = 450",
                 "Atbilde ir 450."),
            ],
            atbilde="450"),

    Ievadi("Atņem simtus un desmitus", [
        {"jaut": "800 − 500 = ?", "atb": ["300"], "padoms": "8 − 5 simti."},
        {"jaut": "750 − 300 = ?", "atb": ["450"], "padoms": "700 − 300 + 50."},
        {"jaut": "90 − 40 = ?", "atb": ["50"], "padoms": "9 − 4 desmiti."},
        {"jaut": "600 − 250 = ?", "atb": ["350"], "padoms": "600 − 200 − 50."},
        {"jaut": "1000 − 400 = ?", "atb": ["600"], "padoms": "10 − 4 simti."},
        {"jaut": "480 − 80 = ?", "atb": ["400"], "padoms": "Desmiti izzūd."},
    ], pamats=4),

    Zimejums("Kad jāaizņemas simts",
             restis([[600, "−", 250, "=", 350]],
                    "600 − 200 = 400, tad 400 − 50 = 350"),
             paskaidro="Atņemot pa daļām, grūtākais solis kļūst vienkāršs.",
             ievads="Divi soļi vienā rēķinā."),

    Varianti("Cik sanāk?", [
        {"jaut": "Cik ir 900 − 400?",
         "opcijas": ["500", "50", "5", "1300"],
         "pareizi": 0, "padoms": "9 − 4 simti."},
        {"jaut": "Cik ir 70 − 30?",
         "opcijas": ["40", "4", "400", "100"],
         "pareizi": 0, "padoms": "7 − 3 desmiti."},
        {"jaut": "Cik ir 850 − 200?",
         "opcijas": ["650", "630", "600", "550"],
         "pareizi": 0, "padoms": "800 − 200 + 50."},
        {"jaut": "Cik ir 1000 − 750?",
         "opcijas": ["250", "350", "150", "200"],
         "pareizi": 0, "padoms": "1000 − 700 − 50."},
    ], pamats=4),

    Pasaule("Cik metru atlicis līdz finišam?",
            Ievadi("", [
                {"jaut": "Distance 800 m, noskrieti 500 m. Cik atlicis?",
                 "atb": ["300"], "padoms": "8 − 5 simti."},
                {"jaut": "Distance 1000 m, noskrieti 750 m. Cik atlicis?",
                 "atb": ["250"], "padoms": "1000 − 750."},
                {"jaut": "Distance 600 m, noskrieti 250 m. Cik atlicis?",
                 "atb": ["350"], "padoms": "600 − 250."},
                {"jaut": "Cik metru kopā noskrieti visās trīs distancēs?",
                 "atb": ["1500"], "padoms": "500 + 750 + 250."},
            ]),
            pavediens="sports",
            konteksts="Sacensībās vienmēr saka, cik metru atlicis - un tas ir "
                      "atņemšanas rēķins.",
            kapec="Ar apaļiem simtiem atlikumu var pateikt uzreiz."),

    Kopsavilkums([
        "Atņemu pilnus simtus un desmitus.",
        "Saskatu analoģiju ar vienu atņemšanu.",
        "Atņemu pa daļām, ja skaitļi nav apaļi.",
        "Pārbaudu rezultātu ar saskaitīšanu.",
    ]),

    Majas([
        "Izrēķini 700 − 300, 950 − 400 un 1000 − 650.",
        "Pārbaudi katru ar saskaitīšanu.",
        "Atrodi divus apaļus simtus, kuru starpība ir 400.",
    ]),
]
