# -*- coding: utf-8 -*-
"""1. klase, 115. stunda: «Kur uzdevumā slēpjas nezināmais?»

Situāciju pieraksta ar vienādību, nezināmā vietā liek «?»: «Bija 8, dažus
atnesa, tagad 13» - 8 + ? = 13. Nezināmais var būt sākumā, vidū vai
beigās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Kur uzdevumā slēpjas nezināmais?"

MERKIS = ("Šodien pierakstīsim situāciju ar vienādību, nezināmā vietā liekot "
          "«?».")

SATURS = [
    Sakums("Bija 8 baloni, dažus atnesa, tagad 13. Kā pierakstīt?",
           fakti=["8 + ? = 13.",
                  "«?» - to, ko nezinām.",
                  "Nezināmais var būt jebkurā vietā."]),

    Doma("Uzraksti ar «?»",
         "Raksti stāstu tādā kārtībā, kā tas notika, un nezināmā vietā - «?».",
         soli=[
             "Cik bija sākumā? (vai «?»)",
             "Kas notika: + vai −, cik? (vai «?»)",
             "Cik beigās? (vai «?»)",
         ]),

    Varianti("Kurš pieraksts der?", [
        {"jaut": "Bija 8 baloni, dažus atnesa, tagad 13.",
         "opcijas": ["8 + ? = 13", "8 + 13 = ?", "? − 8 = 13"],
         "pareizi": 0, "padoms": "Nezinām, cik atnesa."},
        {"jaut": "Bija dažas konfektes, 5 apēda, palika 9.",
         "opcijas": ["? − 5 = 9", "9 − 5 = ?", "5 + 9 = ?"],
         "pareizi": 0, "padoms": "Nezinām sākumu."},
        {"jaut": "Bija 15 zīmuļi, 6 aizdeva. Cik palika?",
         "opcijas": ["15 − 6 = ?", "15 + 6 = ?", "? − 6 = 15"],
         "pareizi": 0, "padoms": "Nezinām beigas."},
    ]),

    Ievadi("Atrodi «?»", [
        {"jaut": "8 + ? = 13", "atb": ["5"], "padoms": "13 − 8."},
        {"jaut": "? − 5 = 9", "atb": ["14"], "padoms": "9 + 5."},
        {"jaut": "15 − 6 = ?", "atb": ["9"], "padoms": "15 − 5 − 1."},
        {"jaut": "? + 7 = 16", "atb": ["9"], "padoms": "16 − 7."},
    ]),

    Pasaule("Vilciens",
            Ievadi("", [
                {"jaut": "Vilcienā bija 12 pasažieru. Stacijā kāpa iekšā "
                         "dažiem, tagad 18. Cik iekāpa?", "atb": ["6"],
                 "padoms": "12 + ? = 18."},
            ]),
            pavediens="celojums",
            konteksts="Vilcienā stacijās cilvēki kāpj iekšā un ārā.",
            kapec="«?» parāda, ko meklējam."),

    Kopsavilkums([
        "Pierakstu situāciju ar vienādību.",
        "Lieku «?» nezināmā vietā.",
        "Atrodu nezināmo.",
    ]),

    Majas([
        "Izdomā stāstu, kur nezināms ir sākums.",
        "Pieraksti to ar «?».",
        "Atrisini un pārbaudi.",
    ]),
]
