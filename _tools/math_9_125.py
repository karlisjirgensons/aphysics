# -*- coding: utf-8 -*-
"""9. klase, 125. stunda: «Kā virkni pieraksta ar formulu?»

Vispārīgā locekļa formula a_n = 3n + 1 ļauj uzreiz atrast jebkuru
locekli - arī simto - bez visu iepriekšējo rēķināšanas. Sērkociņu
kvadrātu virkne no iepriekšējās stundas iegūst formulu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā virkni pieraksta ar formulu?"

MERKIS = ("Aprēķināsim virknes locekļus, ja dota vispārīgā locekļa formula.")

SATURS = [
    Sakums("Cik sērkociņu vajag 100 kvadrātiem?",
           zimejums=restis([["n", "1", "2", "3", "…", "100"],
                            ["aₙ", "4", "7", "10", "…", None]]),
           paraksts="Formula a_n = 3n + 1 atbild uzreiz: 301.",
           fakti=["Pirmajam kvadrātam 4, katram nākamajam +3.",
                  "a_n = 3n + 1: pārbaude a_1 = 4 ✔.",
                  "a_{100} = 301 - bez 99 soļiem."]),

    Doma("Vispārīgā locekļa formula",
         "Formula a_n = f(n) pasaka, kā no numura n aprēķināt locekli.",
         soli=[
             "Ievieto n vietā vajadzīgo numuru.",
             "Aprēķini - tas ir loceklis a_n.",
             "Pārbaudi formulu ar pirmajiem locekļiem.",
         ]),

    Paraugs("Aprēķini locekļus",
            uzd="a_n = n^2 − 2n. Atrodi a_1, a_5 un a_{10}.",
            soli=[
                ("a_1 = 1 − 2 = −1", "n = 1."),
                ("a_5 = 25 − 10 = 15", "n = 5."),
                ("a_{10} = 100 − 20 = 80", "n = 10."),
            ],
            atbilde="−1; 15; 80"),

    Slidnis("Formula → virkne", [
        {"v": "a_n = 2n", "teksts": "2, 4, 6, 8, ... - pāra skaitļi"},
        {"v": "a_n = 2n − 1", "teksts": "1, 3, 5, 7, ... - nepāra skaitļi"},
        {"v": "a_n = n^2", "teksts": "1, 4, 9, 16, ... - kvadrāti"},
        {"v": "a_n = 5 · 2^n", "teksts": "10, 20, 40, 80, ... - dubultojas"},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "a_n = 4n − 3. a_1 = ?", "atb": ["1"], "padoms": "4 − 3."},
        {"jaut": "a_n = 4n − 3. a_{20} = ?", "atb": ["77"], "padoms": "80 − 3."},
        {"jaut": "a_n = {n + 1|n}. a_4 = ? (decimāldaļa)", "atb": ["1,25"],
         "padoms": "{5|4}."},
        {"jaut": "a_n = (−1)^n · n. a_3 = ?", "atb": ["−3", "-3"],
         "padoms": "(−1)^3 = −1."},
        {"jaut": "a_n = 3n + 1. Kurš loceklis ir 61? n = ?", "atb": ["20"],
         "padoms": "3n + 1 = 61."},
    ], pamats=3),

    Varianti("Kura formula?", [
        {"jaut": "5, 10, 15, 20, ...",
         "opcijas": ["a_n = 5n", "a_n = n + 5", "a_n = 5 + n^2",
                     "a_n = 10n"],
         "pareizi": 0, "padoms": "Reizinājums ar 5."},
        {"jaut": "3, 5, 7, 9, ...",
         "opcijas": ["a_n = 2n + 1", "a_n = 3n", "a_n = n + 2",
                     "a_n = 2n − 1"],
         "pareizi": 0, "padoms": "a_1 = 3."},
    ]),

    Pasaule("Kāpņu pakāpieni no kubiem",
            Ievadi("", [
                {"jaut": "Kāpnes no kubiem: 1., 2., 3. pakāpiens - 1, 3, 6 "
                         "kubi; a_n = {n(n + 1)|2}. Cik kubu 10 pakāpienos?",
                 "atb": ["55"], "padoms": "{10 · 11|2}."},
                {"jaut": "Cik kubu 20 pakāpienos?", "atb": ["210"],
                 "padoms": "{20 · 21|2}."},
            ]),
            pavediens="maja",
            konteksts="Bērnu kāpnes no LEGO: katrs pakāpiens ir kolonna, "
                      "augstāka par iepriekšējo.",
            kapec="Formula saskaita bez skaitīšanas."),

    Kopsavilkums([
        "Aprēķinu locekļus pēc formulas.",
        "Atrodu locekļa numuru pēc vērtības.",
        "Saistu formulu ar virknes likumsakarību.",
    ]),

    Majas([
        "a_n = 7 − 2n: atrodi a_1, a_5, a_{10}.",
        "Kurš virknes a_n = 5n − 2 loceklis ir 98?",
        "Uzraksti formulu virknei 6, 11, 16, 21, ...",
    ]),
]
