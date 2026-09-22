# -*- coding: utf-8 -*-
"""5. klase, 45. stunda: «Kur kāpināšana stāv darbību secībā?»

Darbību secība skolēnam jau zināma, bet tagad tajā ienāk ceturtais līmenis.
Kāpināšana notiek pirms reizināšanas - un tieši tur rodas tipiskā kļūda
3 · 2², ko šī stunda arī medī.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kur kāpināšana stāv darbību secībā?"

MERKIS = ("Iemācīsimies noteikt darbību secību izteiksmē, kurā ir kāpināšana "
          "un iekavas.")

SATURS = [
    Sakums("Cik ir 3 · 2²?",
           fakti=["Viens saka 36: vispirms 3 · 2 = 6, tad 6² = 36.",
                  "Otrs saka 12: vispirms 2² = 4, tad 3 · 4 = 12.",
                  "Pareizs ir otrais - kāpināšana notiek pirmā."]),

    Doma("Vispirms iekavas, tad pakāpes, tad reizināšana",
         "Darbību secība ir četros līmeņos: iekavas, kāpināšana, "
         "reizināšana un dalīšana, saskaitīšana un atņemšana.",
         soli=[
             "Izrēķini visu, kas ir iekavās.",
             "Izrēķini visas pakāpes.",
             "Izrēķini reizināšanu un dalīšanu no kreisās uz labo.",
             "Izrēķini saskaitīšanu un atņemšanu no kreisās uz labo.",
         ],
         pieze="Iekavas ir stiprākas par visu: (3 · 2)² = 6² = 36, bet "
               "3 · 2² = 3 · 4 = 12. Tieši tāpēc iekavas raksta - lai "
               "mainītu secību."),

    Paraugs("Izrēķini pa līmeņiem",
            uzd="Aprēķini 5 + 3 · 2².",
            soli=[
                ("Iekavu nav",
                 "Pirmais līmenis izlaists."),
                ("2² = 4",
                 "Kāpināšana ir otrā."),
                ("3 · 4 = 12",
                 "Reizināšana ir trešā."),
                ("5 + 12 = 17",
                 "Saskaitīšana ir pēdējā."),
            ],
            atbilde="5 + 3 · 2² = 17"),

    Ievadi("Ievēro secību", [
        {"jaut": "Cik ir 3 · 2²?", "atb": ["12"],
         "padoms": "Vispirms 2² = 4."},
        {"jaut": "Cik ir (3 · 2)²?", "atb": ["36"], "padoms": "Vispirms "
                                                              "iekavas."},
        {"jaut": "Cik ir 5 + 3 · 2²?", "atb": ["17"], "padoms": "4, tad 12, "
                                                                "tad 17."},
        {"jaut": "Cik ir (5 + 3) · 2²?", "atb": ["32"],
         "padoms": "8 · 4."},
        {"jaut": "Cik ir 2³ + 3²?", "atb": ["17"], "padoms": "8 + 9."},
        {"jaut": "Cik ir 100 − 4²?", "atb": ["84"], "padoms": "100 − 16."},
        {"jaut": "Cik ir 2 · 5² − 10?", "atb": ["40"],
         "padoms": "25, tad 50, tad 40."},
        {"jaut": "Cik ir (2 · 5)² − 10?", "atb": ["90"],
         "padoms": "100 − 10."},
    ], pamats=4,
        ievads="Iekavas, pakāpes, reizināšana, saskaitīšana."),

    Varianti("Kura darbība ir pirmā?", [
        {"jaut": "Izteiksmē 5 + 3 · 2² kura darbība ir pirmā?",
         "opcijas": ["Kāpināšana", "Saskaitīšana", "Reizināšana",
                     "Vienalga kura"],
         "pareizi": 0,
         "padoms": "Pakāpes rēķina pirms reizināšanas."},
        {"jaut": "Kāpēc 3 · 2² nav 36?",
         "opcijas": ["Kāpina tikai 2, ne 3 · 2",
                     "Jo 3 · 2 = 6",
                     "Jo pakāpe ir pēdējā",
                     "Tas ir 36"],
         "pareizi": 0,
         "padoms": "Kāpinātājs attiecas tikai uz skaitli, kuram tas "
                   "uzrakstīts."},
        {"jaut": "Kā panākt, lai kāpinātu tieši 3 · 2?",
         "opcijas": ["Uzrakstīt (3 · 2)²", "Uzrakstīt 3 · 2²",
                     "Uzrakstīt 3² · 2", "Tā nevar"],
         "pareizi": 0,
         "padoms": "Iekavas ir stiprākas par visu."},
        {"jaut": "Kurš darbību līmenis ir pats pēdējais?",
         "opcijas": ["Saskaitīšana un atņemšana", "Kāpināšana",
                     "Reizināšana", "Iekavas"],
         "pareizi": 0,
         "padoms": "Pa vienam līmenim uz leju."},
    ], pamats=4),

    Pasaule("Cik vietas aizņem attēli?",
            Ievadi("", [
                {"jaut": "Ir 3 attēli, katrs 2² megabaiti. Cik megabaitu "
                         "kopā?",
                 "atb": ["12"], "padoms": "3 · 4."},
                {"jaut": "Mapē 5 megabaiti un vēl 3 attēli pa 2² megabaitiem. "
                         "Cik kopā?",
                 "atb": ["17"], "padoms": "5 + 12."},
                {"jaut": "Ekrāns ir 10² punktu plats un tikpat augsts. Cik "
                         "punktu tajā ir?",
                 "atb": ["10000"], "padoms": "100 · 100."},
                {"jaut": "Bija 100 megabaiti, dzēsa 4² megabaitus. Cik "
                         "palika?",
                 "atb": ["84"], "padoms": "100 − 16."},
            ]),
            pavediens="dati",
            konteksts="Failu izmēri gandrīz vienmēr ir pakāpes, un tos "
                      "saskaita kopā ar parastiem skaitļiem.",
            kapec="Vispirms izrēķina pakāpi, tikai tad saskaita."),

    Kopsavilkums([
        "Nosaku darbību secību izteiksmē ar kāpināšanu.",
        "Zinu, ka pakāpes rēķina pirms reizināšanas.",
        "Zinu, ka iekavas ir stiprākas par visu.",
        "Pamanu atšķirību starp 3 · 2² un (3 · 2)².",
    ]),

    Majas([
        "Izrēķini 2 + 3² · 2 un (2 + 3)² · 2.",
        "Uzraksti izteiksmi, kurā iekavas maina atbildi vismaz par 20.",
        "Pārbaudi savas atbildes ar kalkulatoru.",
    ]),
]
