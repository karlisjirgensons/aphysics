# -*- coding: utf-8 -*-
"""4. klase, 79. stunda: «Kā reizināt trīsciparu skaitli?»

Trīsciparu skaitlis reiz divciparu - tas pats stabiņš ar divām rindām,
tikai rindas garākas. Rezultāti var pārsniegt 10 000 - tāpēc novērtējums
pirms rēķina ir obligāts. Reizināšanu ar trīsciparu skaitli 4. klasē
neapskata.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā reizināt trīsciparu skaitli?"

MERKIS = ("Reizināsim trīsciparu skaitli ar divciparu skaitli rakstos un "
          "komentēsim, kas mainās.")

SATURS = [
    Sakums("Cik km nobrauc autobuss 24 dienās?",
           zimejums=restis([["", "", "3", "1", "5"],
                            ["·", "", "", "2", "4"],
                            ["", "1", "2", "6", "0"],
                            ["", "6", "3", "0", ""],
                            ["", "7", "5", "6", "0"]],
                           "315 · 24 = 7560"),
           paraksts="Dienā 315 km - 24 dienās 7560 km.",
           fakti=["Rindas garākas, bet soļi tie paši.",
                  "Novērtējums: 300 · 25 = 7500 - sākam."]),

    Doma("Tie paši soļi, garākas rindas",
         "Trīsciparu skaitli reizina ar vieniem un ar desmitiem, otro rindu "
         "nobīda, rindas saskaita.",
         soli=[
             "Novērtē: noapaļo trīsciparu līdz simtiem, divciparu - līdz "
             "desmitiem.",
             "1. rinda: 315 · 4 = 1260.",
             "2. rinda: 315 · 2 = 630, nobīdīta - 6300.",
             "1260 + 6300 = 7560.",
         ],
         pieze="Kas mainās? Rindās ir vairāk ciparu un vairāk pārnesumu - "
               "tāpēc jāraksta rūpīgi."),

    Paraugs("243 · 32",
            uzd="Sareizini 243 · 32.",
            soli=[
                ("250 · 30 = 7500", "Novērtējums."),
                ("243 · 2 = 486", "1. rinda."),
                ("243 · 3 = 729 → 7290", "2. rinda."),
                ("486 + 7290 = 7776", "Tuvu 7500 - der."),
            ],
            atbilde="7776"),

    Ievadi("Rēķini", [
        {"jaut": "315 · 24 = ?", "atb": ["7560"], "padoms": "1260 + 6300."},
        {"jaut": "243 · 32 = ?", "atb": ["7776"], "padoms": "486 + 7290."},
        {"jaut": "125 · 16 = ?", "atb": ["2000"], "padoms": "750 + 1250."},
        {"jaut": "208 · 45 = ?", "atb": ["9360"], "padoms": "1040 + 8320."},
        {"jaut": "164 · 25 = ?", "atb": ["4100"], "padoms": "820 + 3280."},
        {"jaut": "412 · 23 = ?", "atb": ["9476"], "padoms": "1236 + 8240."},
    ], pamats=4),

    Varianti("Novērtē pirms rēķina", [
        {"jaut": "Aptuveni 389 · 21 ≈ ?",
         "opcijas": ["8000", "800", "80 000", "4000"], "pareizi": 0,
         "padoms": "400 · 20."},
        {"jaut": "Cik ciparu būs 412 · 21?",
         "opcijas": ["4", "3", "5", "6"], "pareizi": 0,
         "padoms": "400 · 20 = 8000 - četri cipari."},
        {"jaut": "Anna: 208 · 45 = 1872. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "200 · 50 = 10 000; aizmirsa nobīdīt rindu."},
    ]),

    Pasaule("Kosmosa kuģa kravas",
            Ievadi("", [
                {"jaut": "Kravas kapsulā 125 pakas pa 24 kg. Cik kg?",
                 "atb": ["3000"], "padoms": "125 · 24."},
                {"jaut": "Stacija aplido Zemi 16 reizes diennaktī. Cik reizes "
                         "365 dienās? (365 · 16)",
                 "atb": ["5840"], "padoms": "2190 + 3650."},
                {"jaut": "Satelīts ik minūti nosūta 128 attēlus. Cik 45 "
                         "minūtēs?",
                 "atb": ["5760"], "padoms": "640 + 5120."},
                {"jaut": "Raķetes dzinējs sekundē sadedzina 250 kg. Cik 36 "
                         "sekundēs?",
                 "atb": ["9000"], "padoms": "250 · 4 · 9."},
            ]),
            pavediens="kosmoss",
            konteksts="Kosmosā visu skaita lielos daudzumos - un katra "
                      "kļūda maksā dārgi.",
            kapec="Novērtējums un stabiņš kopā dod drošu rezultātu."),

    Kopsavilkums([
        "Reizinu trīsciparu skaitli ar divciparu stabiņā.",
        "Novērtēju rezultātu pirms rēķina.",
        "Paskaidroju, kas mainās salīdzinājumā ar divciparu skaitļiem.",
    ]),

    Majas([
        "Izrēķini, cik dienu tu esi nodzīvojis (365 · vecums).",
        "Izrēķini, cik lappušu 12 grāmatās pa 256 lappusēm.",
        "Pārbaudi abus rezultātus ar kalkulatoru.",
    ]),
]
