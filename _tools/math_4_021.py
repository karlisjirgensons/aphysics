# -*- coding: utf-8 -*-
"""4. klase, 21. stunda: «Kā izplānot ceļojumu?»

Visas temata prasmes vienā uzdevumā: lieli skaitļi, saskaitīšana un
atņemšana, darbību secība un aptuvenā vērtība. Izmaksas pieraksta ar vienu
izteiksmi (3-4 darbības), tad salīdzina divus variantus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas,
                         restis)

TEMA = "Kā izplānot ceļojumu?"

MERKIS = ("Ar 3-4 darbību izteiksmēm plānosim un salīdzināsim ceļojuma vai "
          "pasākuma izmaksas.")

SATURS = [
    Sakums("Vilciens vai autobuss uz Tallinu?",
           zimejums=restis([["", "vilciens", "autobuss"],
                            ["biļete 1 cilv.", "25 €", "18 €"],
                            ["ceļā", "5 h", "4 h 30 min"],
                            ["bagāža", "bez maksas", "5 €"]],
                           "Rīga-Tallina"),
           fakti=["Lētākais variants ne vienmēr ir tas, kas šķiet.",
                  "Visu izmaksu izteiksme parāda patiesību."]),

    Doma("Viena izteiksme visām izmaksām",
         "Pieraksti visas izmaksas vienā izteiksmē, izrēķini to un tikai tad "
         "salīdzini variantus.",
         soli=[
             "Uzskaiti visu, par ko jāmaksā.",
             "Ko maksā par katru cilvēku, reizini ar cilvēku skaitu.",
             "Saskaiti visas daļas vienā izteiksmē.",
             "Aptuveni pārbaudi un salīdzini variantus.",
         ],
         pieze="4 cilvēki ar autobusu: 4 · 18 + 4 · 5 = 72 + 20 = 92 €."),

    Paraugs("Ģimene brauc ar vilcienu",
            uzd="4 cilvēki, vilciens 25 € katram, bagāža bez maksas. Cik "
                "maksā ceļš turp un atpakaļ?",
            soli=[
                ("4 · 25 = 100", "Viens virziens."),
                ("100 · 2 = 200", "Turp un atpakaļ."),
                ("(4 · 25) · 2 = 200 €", "Viena izteiksme."),
            ],
            atbilde="200 €"),

    Ievadi("Izrēķini variantus", [
        {"jaut": "Autobuss: 4 · 18 + 4 · 5 = ? (viens virziens)",
         "atb": ["92"], "padoms": "72 + 20."},
        {"jaut": "Autobuss turp un atpakaļ: (4 · 18 + 4 · 5) · 2 = ?",
         "atb": ["184"], "padoms": "92 · 2."},
        {"jaut": "Par cik autobuss lētāks nekā vilciens (turp un atpakaļ, "
                 "200 €)?", "atb": ["16"], "padoms": "200 − 184."},
        {"jaut": "Viesnīca: 2 naktis pa 85 €, brokastis 4 · 2 · 10 €. "
                 "2 · 85 + 4 · 2 · 10 = ?", "atb": ["250"],
         "padoms": "170 + 80."},
    ]),

    Zimejums("Kopējās izmaksas",
             kolonnas([("vilciens", 450), ("autobuss", 434)], " €"),
             paskaidro="Ar viesnīcu (250 €) vilciens sanāk 450 €, autobuss - "
                       "434 €. Starpība tikai 16 €, bet vilcienā ceļā ir ērtāk.",
             ievads="Cena nav vienīgais, ko ņem vērā."),

    Varianti("Kura izteiksme pareiza?", [
        {"jaut": "3 draugi, biļete 12 € katram, viena pica 15 € visiem. "
                 "Kopā?",
         "opcijas": ["3 · 12 + 15", "3 · (12 + 15)", "3 + 12 + 15",
                     "(3 + 12) · 15"], "pareizi": 0,
         "padoms": "Picu pērk vienu, biļetes - trīs."},
        {"jaut": "Tas pats, bet pica katram. Kopā?",
         "opcijas": ["3 · (12 + 15)", "3 · 12 + 15", "12 + 15",
                     "3 + 12 · 15"], "pareizi": 0,
         "padoms": "Katrs maksā 12 + 15."},
        {"jaut": "Budžets 100 €, iztērē 3 · 12 + 15. Cik paliek?",
         "opcijas": ["100 − (3 · 12 + 15)", "100 − 3 · 12 + 15",
                     "100 − 3 + 12 + 15", "(100 − 3) · 12"], "pareizi": 0,
         "padoms": "Visu tēriņu atņem vienā reizē - iekavās."},
        {"jaut": "Cik ir 100 − (3 · 12 + 15)?",
         "opcijas": ["49", "79", "51", "85"], "pareizi": 0,
         "padoms": "36 + 15 = 51; 100 − 51."},
    ], pamats=4),

    Pasaule("Klases ekskursija uz Siguldu",
            Ievadi("", [
                {"jaut": "24 skolēni, autobuss 240 € visiem. Ieeja pilī 3 € "
                         "katram. 240 + 24 · 3 = ?",
                 "atb": ["312"], "padoms": "240 + 72."},
                {"jaut": "Plus trošu vagoniņš 5 € katram. Cik viss kopā?",
                 "atb": ["432"], "padoms": "312 + 24 · 5."},
                {"jaut": "Klases kasē 500 €. Cik paliks?",
                 "atb": ["68"], "padoms": "500 − 432."},
                {"jaut": "Ja brauc vēl 2 skolotāji (bez maksas autobusā, "
                         "bet maksā ieeju un vagoniņu), cik vairāk?",
                 "atb": ["16"], "padoms": "2 · (3 + 5)."},
            ]),
            pavediens="celojums",
            konteksts="Klase plāno ekskursiju: autobuss visiem kopā, ieeja "
                      "un izklaides - katram.",
            kapec="Izteiksme parāda, kur nauda aiziet un ko var "
                  "ietaupīt."),

    Kopsavilkums([
        "Pierakstu izmaksas ar vienu izteiksmi.",
        "Nošķiru izmaksas par katru un kopīgās izmaksas.",
        "Salīdzinu divus variantus.",
        "Pārbaudu, vai budžets pietiek.",
    ]),

    Majas([
        "Izplāno iedomātu dienas braucienu ģimenei: ceļš, ieeja, ēdiens.",
        "Uzraksti izmaksas ar vienu izteiksmi un izrēķini.",
        "Pajautā mājiniekiem, kas vēl būtu jāieskaita budžetā.",
    ]),
]
