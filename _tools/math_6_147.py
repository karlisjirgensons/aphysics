# -*- coding: utf-8 -*-
"""6. klase, 147. stunda: «Kāpēc reizinājums sanāk negatīvs?»

Pēdējais gada temats. Reizināšana ar negatīvu skaitli te netiek pasludināta,
bet izsecināta: reizinājums ir vienādu saskaitāmo summa, un no tā uzreiz
izriet, kāpēc pluss reiz mīnuss dod mīnusu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāpēc reizinājums sanāk negatīvs?"

MERKIS = ("Skaidrosim, kāpēc pozitīva un negatīva skaitļa reizinājums ir "
          "negatīvs.")

SATURS = [
    Sakums("Reizinājums ir vienādu saskaitāmo summa",
           zimejums=restis([["3 · (−4)", "=", "−4 + (−4) + (−4)",
                             "=", "−12"]]),
           paraksts="Trīs vienādi negatīvi saskaitāmie dod negatīvu summu.",
           fakti=["Reizināt ar 3 nozīmē saskaitīt trīs vienādus skaitļus.",
                  "Trīs mīnusi kopā dod mīnusu.",
                  "Tāpēc pozitīva un negatīva skaitļa reizinājums ir "
                  "negatīvs."]),

    Doma("No saskaitīšanas uz reizināšanu",
         "Reizinājums ar veselu skaitli ir vienādu saskaitāmo summa, tāpēc "
         "negatīva skaitļa reizinājums ar pozitīvu ir negatīvs.",
         soli=[
             "Pārraksti reizinājumu kā vienādu saskaitāmo summu.",
             "Saskaiti tos pēc zīmju likuma.",
             "Pieraksti rezultātu ar zīmi.",
             "Pārbaudi uz skaitļu taisnes: vairāki soļi vienā virzienā.",
             "Formulē secinājumu par zīmi.",
         ],
         pieze="Reizinātājus drīkst mainīt vietām, tāpēc (−4) · 3 ir tas "
               "pats, kas 3 · (−4). Abos gadījumos rezultāts ir −12."),

    Paraugs("Pārraksti kā summu",
            uzd="Kāpēc 3 · (−4) = −12?",
            soli=[
                ("3 · (−4) = (−4) + (−4) + (−4)",
                 "Trīs vienādi saskaitāmie."),
                ("Visi trīs ir negatīvi",
                 "Zīmes vienādas - moduļus saskaita."),
                ("4 + 4 + 4 = 12, zīme mīnus",
                 "Rezultāts −12."),
                ("Uz taisnes: trīs soļi pa 4 vienībām pa kreisi",
                 "No nulles līdz −12."),
            ],
            atbilde="−12"),

    Ievadi("Izrēķini reizinājumu", [
        {"jaut": "Cik ir 3 · (−4)?",
         "atb": ["-12", "−12"], "padoms": "Trīs negatīvi saskaitāmie."},
        {"jaut": "Cik ir 5 · (−2)?",
         "atb": ["-10", "−10"], "padoms": "Pieci soļi pa 2 pa kreisi."},
        {"jaut": "Cik ir (−6) · 4?",
         "atb": ["-24", "−24"], "padoms": "Reizinātājus drīkst mainīt "
                                          "vietām."},
        {"jaut": "Cik ir 7 · (−3)?",
         "atb": ["-21", "−21"], "padoms": "7 · 3, zīme mīnus."},
        {"jaut": "Cik ir (−9) · 1?",
         "atb": ["-9", "−9"], "padoms": "Reizinot ar 1, nekas nemainās."},
        {"jaut": "Cik ir (−5) · 0?",
         "atb": ["0"], "padoms": "Neviena saskaitāmā."},
    ], pamats=4),

    Varianti("Kāda būs zīme?", [
        {"jaut": "Pozitīva un negatīva skaitļa reizinājums ir...",
         "opcijas": ["negatīvs", "pozitīvs", "nulle", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Vairāki negatīvi saskaitāmie."},
        {"jaut": "4 · (−5) ir tas pats, kas...",
         "opcijas": ["(−5) + (−5) + (−5) + (−5)", "−5 − 4",
                     "4 − 5", "(−4) · 5 nav tas pats"],
         "pareizi": 0,
         "padoms": "Četri vienādi saskaitāmie."},
        {"jaut": "Vai (−4) · 3 un 3 · (−4) ir vienādi?",
         "opcijas": ["Jā, reizinātājus drīkst mainīt vietām",
                     "Nē, secība maina zīmi",
                     "Jā, bet tikai veseliem skaitļiem", "Nē"],
         "pareizi": 0,
         "padoms": "Reizināšanas īpašība."},
        {"jaut": "Jebkura skaitļa reizinājums ar nulli ir...",
         "opcijas": ["nulle", "pats skaitlis", "negatīvs", "viens"],
         "pareizi": 0,
         "padoms": "Neviena saskaitāmā."},
    ], pamats=4),

    Pasaule("Cik daudz iztērēts?",
            Ievadi("", [
                {"jaut": "Katru dienu iztērē 4 € jeb −4 €. Cik eiro trīs "
                         "dienās?",
                 "atb": ["-12", "−12"], "padoms": "3 · (−4)."},
                {"jaut": "Cik eiro nedēļā, ja katru dienu −4 €?",
                 "atb": ["-28", "−28"], "padoms": "7 · (−4)."},
                {"jaut": "Temperatūra krīt par 3 grādiem stundā. Par cik "
                         "grādiem piecās stundās?",
                 "atb": ["-15", "−15"], "padoms": "5 · (−3)."},
                {"jaut": "Zonde nolaižas par 6 m minūtē. Kurā dziļumā tā ir "
                         "pēc 4 minūtēm?",
                 "atb": ["-24", "−24"], "padoms": "4 · (−6)."},
            ]),
            pavediens="celojums",
            konteksts="Vienāds ikdienas izdevums vairākās dienās ir tieši "
                      "reizināšana ar negatīvu skaitli.",
            kapec="Vairāki vienādi soļi pa kreisi ir reizinājums."),

    Zimejums("Trīs vienādi soļi",
             restis([["0", "−4", "−8", "−12"]],
                    "trīs soļi pa 4 vienībām"),
             paskaidro="Katrs solis ir −4. Pēc trim soļiem esam pie −12 - "
                       "tieši tas ir 3 · (−4).",
             ievads="Reizinājums uz skaitļu taisnes."),

    Kopsavilkums([
        "Pārrakstu reizinājumu kā vienādu saskaitāmo summu.",
        "Paskaidroju, kāpēc rezultāts ir negatīvs.",
        "Zinu, ka reizinātājus drīkst mainīt vietām.",
        "Aprēķinu pozitīva un negatīva skaitļa reizinājumu.",
    ]),

    Majas([
        "Pārraksti kā summu un izrēķini 4 · (−6).",
        "Izrēķini (−7) · 5 un pieraksti, kāpēc zīme ir mīnuss.",
        "Uzzīmē skaitļu taisni vienam no reizinājumiem.",
    ]),
]
