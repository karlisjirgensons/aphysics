# -*- coding: utf-8 -*-
"""1. klase, 94. stunda: «Kā atņemt divciparu skaitli?»

18 − 13: abiem ir pa desmitam, tie atņemas; paliek vieni: 8 − 3 = 5.
Pierakstā: 18 − 13 = 18 − 10 − 3 = 8 − 3 = 5.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, desmiti)

TEMA = "Kā atņemt divciparu skaitli?"

MERKIS = ("Šodien atņemsim divciparu skaitli, izmantojot skaitļa "
          "sastāvu.")

SATURS = [
    Sakums("18 − 13 - kā ātri?",
           zimejums=desmiti(1, 8),
           paraksts="Atņem desmitu, tad 3 vienus: paliek 5.",
           fakti=["13 = 10 + 3.",
                  "Vispirms atņem desmitu: 18 − 10 = 8.",
                  "Tad vienus: 8 − 3 = 5."]),

    Paraugs("Pa daļām",
            uzd="Izrēķini 18 − 13.",
            soli=[
                ("13 = 10 + 3", "Sadala atņemamo."),
                ("18 − 10 = 8", "Atņem desmitu."),
                ("8 − 3 = 5", "Atņem vienus."),
            ],
            atbilde="5"),

    Doma("Desmits no desmita",
         "Atņem desmitu no desmita, vienus no vieniem.",
         soli=[
             "Sadali atņemamo desmitā un vienos.",
             "Atņem desmitu.",
             "Atņem vienus.",
         ]),

    Ievadi("Atņem", [
        {"jaut": "17 − 12 = ?", "atb": ["5"], "padoms": "7 − 2."},
        {"jaut": "19 − 14 = ?", "atb": ["5"], "padoms": "9 − 4."},
        {"jaut": "16 − 11 = ?", "atb": ["5"], "padoms": "6 − 1."},
        {"jaut": "15 − 15 = ?", "atb": ["0"], "padoms": "Viss aiziet."},
        {"jaut": "18 − 10 = ?", "atb": ["8"], "padoms": "Tikai desmits."},
        {"jaut": "20 − 13 = ?", "atb": ["7"], "padoms": "20 − 10 − 3."},
    ], pamats=4),

    Varianti("Kurš solis pareizs?", [
        {"jaut": "19 − 16 = ?",
         "opcijas": ["9 − 6 = 3", "19 − 6 = 13", "16 − 9 = 7"],
         "pareizi": 0, "padoms": "Desmiti atņemas."},
    ]),

    Pasaule("Lappuses grāmatā",
            Ievadi("", [
                {"jaut": "Grāmatā 18 lappušu. Izlasīju 12. Cik vēl?",
                 "atb": ["6"], "padoms": "8 − 2."},
                {"jaut": "Brālim 19 lappušu, izlasīja 13. Cik vēl?",
                 "atb": ["6"], "padoms": "9 − 3."},
            ]),
            pavediens="skola",
            konteksts="Lasīšanas stundā katrs lasa savu grāmatu.",
            kapec="Atņemšana pasaka, cik vēl palicis."),

    Kopsavilkums([
        "Atņemu divciparu skaitli pa daļām.",
        "Vispirms desmitu, tad vienus.",
        "Pierakstu soļus.",
    ]),

    Majas([
        "Izrēķini 17 − 15 un 19 − 11.",
        "Pieraksti soļus.",
        "Pārbaudi ar saskaitīšanu.",
    ]),
]
