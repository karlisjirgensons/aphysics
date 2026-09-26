# -*- coding: utf-8 -*-
"""7. klase, 57. stunda: «Kā no algoritma iegūt formulu?»

Funkciju bieži apraksta ar soļiem: «paņem skaitli, reizini ar 3, pieskaiti
2». Katru soli pārtulkojot, iegūst formulu y = 3x + 2. Stunda to dara abos
virzienos un ar programmēšanas piemēru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā no algoritma iegūt formulu?"

MERKIS = ("Pierakstīsim ar formulu funkciju, kas aprakstīta algoritma "
          "veidā.")

SATURS = [
    Sakums("«Iedomājies skaitli...» triks",
           zimejums=restis([["solis", "ar 5", "ar x"],
                            ["iedomājies", "5", "x"],
                            ["reizini ar 2", "10", "2x"],
                            ["pieskaiti 6", "16", "2x + 6"]]),
           paraksts="Katrs solis kļūst par formulas daļu.",
           fakti=["Burvji un programmētāji lieto algoritmus.",
                  "Formula ir algoritms vienā rindā."]),

    Doma("Katrs solis - viena darbība formulā",
         "Lai no algoritma iegūtu formulu, argumentu apzīmē ar x un katru "
         "soli pieraksta kā darbību ar iepriekšējo rezultātu.",
         soli=[
             "Sāc ar x.",
             "Katru soli pieraksti, darbību izpildot ar visu iepriekšējo "
             "izteiksmi - ja vajag, ieliec to iekavās.",
             "Beigās: y = iegūtā izteiksme.",
             "Pārbaudi ar vienu skaitli: algoritms un formula dod vienu "
             "rezultātu.",
         ],
         pieze="«Pieskaiti 3, tad reizini ar 2» ir y = 2(x + 3), nevis "
               "2x + 3. Iekavas saglabā secību."),

    Paraugs("Algoritms ar iekavām",
            uzd="Algoritms: paņem skaitli, pieskaiti 4, reizini ar 3, atņem "
                "5. Uzraksti formulu.",
            soli=[
                ("x + 4", "Pirmais solis."),
                ("3(x + 4)", "Reizina visu iepriekšējo."),
                ("y = 3(x + 4) − 5", "Atņem."),
                ("x = 1: 3 · 5 − 5 = 10", "Pārbaude."),
            ],
            atbilde="y = 3(x + 4) − 5"),

    Varianti("Kura formula atbilst?", [
        {"jaut": "Reizini ar 5, tad atņem 1.",
         "opcijas": ["y = 5x − 1", "y = 5(x − 1)", "y = x − 5", "y = 5 − x"],
         "pareizi": 0,
         "padoms": "Vispirms reizina."},
        {"jaut": "Atņem 1, tad reizini ar 5.",
         "opcijas": ["y = 5(x − 1)", "y = 5x − 1", "y = x − 5",
                     "y = 5 − x"],
         "pareizi": 0,
         "padoms": "Iekavas - atņemšana notiek pirmā."},
        {"jaut": "Izdali ar 2, pieskaiti 7.",
         "opcijas": ["y = {x|2} + 7", "y = {x + 7|2}", "y = 2x + 7",
                     "y = 7x + 2"],
         "pareizi": 0,
         "padoms": "Dala tikai x."},
        {"jaut": "Formula y = 4x + 3. Kurš algoritms?",
         "opcijas": ["Reizini ar 4, pieskaiti 3",
                     "Pieskaiti 3, reizini ar 4",
                     "Pieskaiti 4, reizini ar 3",
                     "Reizini ar 3, pieskaiti 4"],
         "pareizi": 0,
         "padoms": "Darbību secība."},
    ], pamats=4),

    Ievadi("Aprēķini pēc algoritma", [
        {"jaut": "Pieskaiti 4, reizini ar 3, atņem 5. Rezultāts, ja x = 6?",
         "atb": ["25"], "padoms": "3 · 10 − 5."},
        {"jaut": "y = 5x − 1. Cik ir y, ja x = −2?",
         "atb": ["−11", "-11"], "padoms": "−10 − 1."},
        {"jaut": "y = 5(x − 1). Cik ir y, ja x = −2?",
         "atb": ["−15", "-15"], "padoms": "5 · (−3)."},
        {"jaut": "Algoritms: reizini ar 2, pieskaiti 6. Rezultāts 20. "
                 "Kāds bija skaitlis?",
         "atb": ["7"], "padoms": "Ej atpakaļ: 20 − 6 = 14; 14 : 2."},
    ]),

    Pasaule("Programma skaitļotājā",
            Ievadi("", [
                {"jaut": "Programma: a = x; a = a · 2; a = a + 10; "
                         "izvada a. Ko tā izvada, ja x = 15?",
                 "atb": ["40"], "padoms": "30 + 10."},
                {"jaut": "Programma izvadīja 26. Kāds bija x?",
                 "atb": ["8"], "padoms": "(26 − 10) : 2."},
                {"jaut": "Temperatūras pārvēršana: F = 1,8C + 32. Cik °F ir "
                         "20 °C?",
                 "atb": ["68"], "padoms": "36 + 32."},
            ]),
            pavediens="dati",
            konteksts="Katra programma, kas rēķina, ir algoritms - un to var "
                      "pierakstīt kā formulu.",
            kapec="Formula un programma - viens un tas pats."),

    Kopsavilkums([
        "Pārtulkoju algoritma soļus formulā.",
        "Lieku iekavas, ja darbība attiecas uz visu iepriekšējo.",
        "Pārbaudu formulu ar vienu skaitli.",
        "Eju algoritmu atpakaļ, lai atrastu sākuma skaitli.",
    ]),

    Majas([
        "Izdomā «iedomājies skaitli» triku un uzraksti formulu.",
        "Pārbaudi to uz ģimenes locekļiem.",
        "Uzraksti algoritmu formulai y = 2(x + 5) − 3.",
    ]),
]
