# -*- coding: utf-8 -*-
"""8. klase, 115. stunda: «Kā saskaita polinomus?»

Saskaitot atver iekavas un savelk līdzīgos; atņemot maina visas atņemamā
polinoma zīmes. Līdzīgos ērti rakstīt vienu zem otra kā skaitļus stabiņā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā saskaita polinomus?"

MERKIS = ("Saskaitīsim un atņemsim polinomus, savelkot līdzīgos "
          "locekļus.")

_T = "text"

SATURS = [
    Sakums("Saskaiti stabiņā",
           zimejums=restis([["3x²", "+ 2x", "− 1"],
                            ["x²", "− 5x", "+ 4"],
                            ["4x²", "− 3x", "+ 3"]]),
           paraksts="Līdzīgie locekļi stāv viens zem otra.",
           fakti=["Saskaitot atver iekavas un savelk līdzīgos.",
                  "Atņemot maina visas atņemamā polinoma zīmes.",
                  "Ērti rakstīt līdzīgos locekļus vienu zem otra."]),

    Doma("Summa un starpība",
         "Polinomus saskaita, saskaitot līdzīgo locekļu koeficientus.",
         soli=[
             "Summa: (A) + (B) - iekavas vienkārši atver.",
             "Starpība: (A) − (B) - otrās iekavas atver, mainot katru "
             "zīmi.",
             "Savelc līdzīgos locekļus.",
             "Pieraksti normālformā.",
         ]),

    Paraugs("Atņem",
            uzd="Aprēķini (3x^2 + 2x − 1) − (x^2 − 5x + 4).",
            soli=[
                ("3x^2 + 2x − 1 − x^2 + 5x − 4", "Zīmes otrajā iekavā "
                                                 "mainās."),
                ("2x^2 + 7x − 5", "Savelk."),
            ],
            atbilde="2x^2 + 7x − 5"),

    Ievadi("Aprēķini (normālformā)", [
        {"jaut": "(2a + 3) + (5a − 1)", "atb": ["7a + 2"], "tastatura": _T,
         "padoms": "2a + 5a; 3 − 1."},
        {"jaut": "(x^2 + x) + (2x^2 − 3x)", "atb": ["3x^2 − 2x"],
         "tastatura": _T, "padoms": "Kvadrāti un x atsevišķi."},
        {"jaut": "(4b − 2) − (b + 5)", "atb": ["3b − 7"], "tastatura": _T,
         "padoms": "4b − 2 − b − 5."},
        {"jaut": "(a^2 − 1) − (a^2 − 3a)", "atb": ["3a − 1"],
         "tastatura": _T, "padoms": "a^2 saīsinās, −(−3a) = +3a."},
        {"jaut": "(5x^2 + 2x) − (2x^2 − x + 4)",
         "atb": ["3x^2 + 3x − 4"], "tastatura": _T,
         "padoms": "−(−x) = +x."},
        {"jaut": "(y + 1) + (y − 1) − (2y)", "atb": ["0"],
         "padoms": "Viss saīsinās."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "(a + b) − (a − b) = ?",
         "opcijas": ["2b", "0", "2a", "−2b"],
         "pareizi": 0, "padoms": "a + b − a + b."},
        {"jaut": "(x^2 − x) + (x − x^2) = ?",
         "opcijas": ["0", "2x^2", "2x", "x^2 − x"],
         "pareizi": 0, "padoms": "Pretēji polinomi."},
        {"jaut": "Kādu polinomu jāpieskaita x + 3, lai iegūtu 5x?",
         "opcijas": ["4x − 3", "4x + 3", "5x − 3", "6x"],
         "pareizi": 0, "padoms": "5x − (x + 3)."},
    ]),

    Pasaule("Divi veikali",
            Ievadi("", [
                {"jaut": "Veikalā A pirkums maksā (3x + 2) €, veikalā B - "
                         "(2x + 5) €. A − B = ?x − 3",
                 "atb": ["1"], "padoms": "3x + 2 − 2x − 5 = x − 3."},
                {"jaut": "Pie kāda x abos maksā vienādi?", "atb": ["3"],
                 "padoms": "x − 3 = 0."},
                {"jaut": "Abos kopā: 5x + ?", "atb": ["7"],
                 "padoms": "2 + 5."},
            ]),
            pavediens="veikals",
            konteksts="x - preču skaits; polinomu starpība parāda, kurā "
                      "veikalā lētāk.",
            kapec="Atņemot polinomu, maina visas tā zīmes."),

    Kopsavilkums([
        "Saskaitu polinomus.",
        "Atņemu polinomus, mainot zīmes.",
        "Savelku līdzīgos locekļus.",
    ]),

    Majas([
        "Aprēķini: (4x^2 − x + 2) + (x^2 + 3x − 5) un to starpību.",
        "Pārbaudi ar x = 1.",
        "Izdomā divus polinomus, kuru summa ir 10x.",
    ]),
]
