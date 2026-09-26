# -*- coding: utf-8 -*-
"""1. klase, 146. stunda: «Kā pieskaitīt desmitus divciparu skaitlim?»

34 + 20: vieni paliek, desmitiem pieskaita: 3 + 2 = 5 desmiti - 54.
Simta kvadrātā - divi soļi uz leju. «Par 10 lielāks» - viens solis uz
leju.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, simta_kvadrats)

TEMA = "Kā pieskaitīt desmitus divciparu skaitlim?"

MERKIS = ("Šodien divciparu skaitlim pieskaitīsim un atņemsim pilnus "
          "desmitus un nosauksim par 10 lielāku vai mazāku skaitli.")

SATURS = [
    Sakums("34 + 20 - kur simta kvadrātā?",
           zimejums=simta_kvadrats(31, 60, izcelt=[34, 44, 54]),
           paraksts="No 34 divi soļi uz leju: 44, 54.",
           fakti=["Vieni paliek tie paši.",
                  "Mainās tikai desmiti.",
                  "+10 - solis uz leju, −10 - uz augšu."]),

    Doma("Vieni paliek",
         "Pieskaitot desmitus, mainās tikai desmitu cipars.",
         soli=[
             "34 + 20: desmiti 3 + 2 = 5.",
             "Vieni paliek 4.",
             "Atbilde: 54.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "34 + 20 = ?", "atb": ["54"], "padoms": "3 + 2 desmiti."},
        {"jaut": "57 + 30 = ?", "atb": ["87"], "padoms": "5 + 3 desmiti."},
        {"jaut": "68 − 40 = ?", "atb": ["28"], "padoms": "6 − 4 desmiti."},
        {"jaut": "Par 10 lielāks nekā 45?", "atb": ["55"],
         "padoms": "Solis uz leju."},
        {"jaut": "Par 10 mazāks nekā 72?", "atb": ["62"],
         "padoms": "Solis uz augšu."},
        {"jaut": "91 − 60 = ?", "atb": ["31"], "padoms": "9 − 6 desmiti."},
    ], pamats=4),

    Varianti("Kas mainās?", [
        {"jaut": "Kas mainās, ja 23 pieskaita 40?",
         "opcijas": ["desmitu cipars", "vienu cipars", "abi"],
         "pareizi": 0, "padoms": "Vieni paliek 3."},
    ]),

    Pasaule("Lappuses",
            Ievadi("", [
                {"jaut": "Tu esi 26. lappusē, izlasīsi vēl 30. Kurā lappusē "
                         "būsi?", "atb": ["56"], "padoms": "26 + 30."},
            ]),
            pavediens="skola",
            konteksts="Lasīšanas grāmatā ir daudz lappušu.",
            kapec="Desmiti ātri pieskaitāmi."),

    Kopsavilkums([
        "Pieskaitu desmitus divciparu skaitlim.",
        "Atņemu desmitus.",
        "Nosaucu par 10 lielāku un mazāku skaitli.",
    ]),

    Majas([
        "Nosauc par 10 lielāku skaitli nekā tavs mājas numurs.",
        "Izrēķini 45 + 30 un 76 − 50.",
        "Pārbaudi simta kvadrātā.",
    ]),
]
