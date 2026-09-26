# -*- coding: utf-8 -*-
"""1. klase, 29. stunda: «Ko nozīmē «+» un «−»?»

«+» - pienāca klāt, saliek kopā; «−» - aizgāja prom, atdeva, apēda.
Situāciju vispirms izspēlē ar lietām, tad pieraksta ar darbību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Ko nozīmē «+» un «−»?"

MERKIS = ("Šodien pierakstīsim ar «+» un «−», kas notiek stāstā.")

SATURS = [
    Sakums("Uz zara sēž 4 putni, atlido vēl 2. Kā to pierakstīt?",
           zimejums=bildes([[("putns", 4), ("putns*", 2)]]),
           paraksts="4 + 2 = 6",
           fakti=["«+» - pienāca klāt, saliek kopā.",
                  "«−» - aizgāja prom, atdeva, apēda.",
                  "Aiz «=» raksta, cik sanāca."]),

    Doma("Klāt vai prom?",
         "Ja kļūst vairāk - «+», ja kļūst mazāk - «−».",
         soli=[
             "Cik bija sākumā?",
             "Vai nāca klāt (+) vai gāja prom (−)?",
             "Cik nāca vai gāja?",
             "Uzraksti: sākums, zīme, skaitlis, =, rezultāts.",
         ]),

    Varianti("Plus vai mīnus?", [
        {"jaut": "Grozā 5 āboli, Ieva apēda 1.",
         "opcijas": ["5 − 1", "5 + 1"], "jaukt": False, "pareizi": 0,
         "padoms": "Apēda - kļuva mazāk."},
        {"jaut": "Plauktā 3 grāmatas, noliek vēl 4.",
         "opcijas": ["3 + 4", "3 − 4"], "jaukt": False, "pareizi": 0,
         "padoms": "Noliek - kļūst vairāk."},
        {"jaut": "Dīķī 7 zivis, 2 aizpeldēja.",
         "opcijas": ["7 − 2", "7 + 2"], "jaukt": False, "pareizi": 0,
         "padoms": "Aizpeldēja - mazāk."},
        {"jaut": "Stāvvietā 6 mašīnas, atbrauca 3.",
         "opcijas": ["6 + 3", "6 − 3"], "jaukt": False, "pareizi": 0,
         "padoms": "Atbrauca - vairāk."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "4 + 2 = ?", "zim": bildes([[("putns", 4), ("putns*", 2)]]),
         "atb": ["6"], "padoms": "Saskaiti visus putnus."},
        {"jaut": "5 − 1 = ?", "zim": bildes([[("abols", 4), ""]]),
         "atb": ["4"], "padoms": "Viens apēsts."},
        {"jaut": "7 − 2 = ?", "atb": ["5"], "padoms": "Skaiti atpakaļ 2."},
        {"jaut": "3 + 4 = ?", "atb": ["7"], "padoms": "No 3 uz priekšu 4."},
    ]),

    Pasaule("Autobusa pietura",
            Ievadi("", [
                {"jaut": "Autobusā 8 cilvēki. Pieturā izkāpj 3. Cik "
                         "palika?", "atb": ["5"], "padoms": "8 − 3."},
                {"jaut": "Tad iekāpj 2. Cik tagad?", "atb": ["7"],
                 "padoms": "5 + 2."},
            ]),
            pavediens="celojums",
            konteksts="Autobusā cilvēki iekāpj un izkāpj.",
            kapec="Iekāpj - plus, izkāpj - mīnus."),

    Kopsavilkums([
        "Zinu, ka «+» nozīmē klāt, «−» - prom.",
        "Pierakstu stāstu ar darbību.",
        "Aprēķinu, cik sanāca.",
    ]),

    Majas([
        "Izdomā stāstu par «+» ar rotaļlietām.",
        "Izdomā stāstu par «−» ar konfektēm.",
        "Pieraksti abus ar cipariem un zīmēm.",
    ]),
]
