# -*- coding: utf-8 -*-
"""2. klase, 33. stunda: «Desmiti ar desmitiem, vieni ar vieniem?»

Divciparu skaitļus saskaita pa daļām: stieņus ar stieņiem, kubiņus ar
kubiņiem. 34 + 25 = (30 + 20) + (4 + 5) = 50 + 9 = 59. Šodien vieni vēl
nepārsniedz 9, tāpēc jauns desmits nerodas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, desmiti)

TEMA = "Desmiti ar desmitiem, vieni ar vieniem?"

MERKIS = ("Šodien modelēsim divciparu skaitļu saskaitīšanu ar desmitu "
          "stieņiem un secināsim, kādā kārtībā to darīt.")

SATURS = [
    Sakums("Kā ātri saskaitīt 34 + 25 kubiņus?",
           zimejums=desmiti(5, 9),
           paraksts="5 stieņi un 9 kubiņi - 59.",
           fakti=["Stieņus skaita ar stieņiem: 3 + 2 = 5 desmiti.",
                  "Kubiņus ar kubiņiem: 4 + 5 = 9 vieni.",
                  "Kopā 59."]),

    Doma("Katrs ar savu",
         "Desmitus saskaita ar desmitiem, vienus - ar vieniem.",
         soli=[
             "Sadali: 34 = 30 + 4, 25 = 20 + 5.",
             "Desmiti: 30 + 20 = 50.",
             "Vieni: 4 + 5 = 9.",
             "Saliec kopā: 50 + 9 = 59.",
         ]),

    Slidnis("34 + 25 ar kubiņiem", [
        {"v": "34", "teksts": "3 stieņi, 4 kubiņi.", "zim": desmiti(3, 4)},
        {"v": "+ 20", "teksts": "Pieliek 2 stieņus - 54.",
         "zim": desmiti(5, 4)},
        {"v": "+ 5", "teksts": "Pieliek 5 kubiņus - 59.",
         "zim": desmiti(5, 9)},
    ]),

    Paraugs("Cik ir 42 + 36?",
            uzd="Saskaiti pa daļām.",
            soli=[("40 + 30 = 70", "Desmiti ar desmitiem."),
                  ("2 + 6 = 8", "Vieni ar vieniem."),
                  ("70 + 8 = 78", "Saliek kopā.")],
            atbilde="78"),

    Ievadi("Saskaiti", [
        {"jaut": "23 + 14 = ?", "atb": ["37"], "padoms": "30 + 7."},
        {"jaut": "51 + 27 = ?", "atb": ["78"], "padoms": "70 + 8."},
        {"jaut": "36 + 42 = ?", "atb": ["78"], "padoms": "70 + 8."},
        {"jaut": "15 + 61 = ?", "atb": ["76"], "padoms": "70 + 6."},
        {"jaut": "44 + 44 = ?", "atb": ["88"], "padoms": "80 + 8."},
        {"jaut": "62 + 35 = ?", "atb": ["97"], "padoms": "90 + 7."},
    ], pamats=4),

    Varianti("Kas notika?", [
        {"jaut": "Toms: 34 + 25 = 84. Ko viņš sajauca?",
         "opcijas": ["Saskaitīja 3 desmitus ar 5 vieniem",
                     "Nekas - pareizi", "Atņēma"], "pareizi": 0,
         "padoms": "Desmiti ar desmitiem!"},
        {"jaut": "Kura summa ir 69?",
         "opcijas": ["45 + 24", "45 + 42", "54 + 24"], "pareizi": 0,
         "padoms": "60 + 9."},
    ]),

    Pasaule("Cik skolēnu ekskursijā?",
            Ievadi("", [
                {"jaut": "2.a klasē 23 skolēni, 2.b - 25. Cik kopā?",
                 "atb": ["48"], "padoms": "40 + 8."},
                {"jaut": "Autobusā ir 50 vietu. Vai visiem pietiks? "
                         "Cik vietu paliks brīvas?", "atb": ["2"],
                 "padoms": "50 − 48."},
            ]),
            pavediens="celojums",
            konteksts="Divas klases kopā brauc uz Rīgas zoodārzu.",
            kapec="Autobusu pasūta pēc kopējā skaita."),

    Kopsavilkums([
        "Sadalu skaitli desmitos un vienos.",
        "Saskaitu desmitus ar desmitiem un vienus ar vieniem.",
        "Saliku rezultātu kopā.",
    ]),

    Majas([
        "No zīmuļiem saliec «desmitus» ar gumijām un parādi 32 + 24.",
        "Izrēķini: 41 + 37, 25 + 53.",
        "Paskaidro mājiniekam, kā rēķināji.",
    ]),
]
