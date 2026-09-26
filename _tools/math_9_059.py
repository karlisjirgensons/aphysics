# -*- coding: utf-8 -*-
"""9. klase, 59. stunda: «Kā iznest kopīgo reizinātāju?»

Sadalīšanas likums no otras puses: ab + ac = a(b + c). Kopīgais reizinātājs
ir lielākais skaitlis un katrs burts mazākajā pakāpē, kas ir visos
locekļos. Iekavās paliek tas, ko iegūst, dalot katru locekli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā iznest kopīgo reizinātāju?"

MERKIS = ("Sadalīsim polinomu reizinātājos, iznesot kopīgo reizinātāju, un "
          "skaidrosim darbību.")

_T = "text"

SATURS = [
    Sakums("6x + 9 = ?(? + ?)",
           zimejums=geometrija([("A", 0, 0), ("E", 4, 0), ("B", 7, 0),
                                ("C", 7, 3), ("F", 4, 3), ("D", 0, 3)],
                               nogriezni=["AB", "BC", "CD", "DA", "EF"],
                               iekrasot=[("AEFD", 0), ("EBCF", 1)],
                               malas=[("AE", "2x"), ("EB", "3"),
                                      ("DA", "3")],
                               uzraksti=[(2, 1.5, "6x"), (5.5, 1.5, "9")]),
           paraksts="Abiem gabaliem kopīga mala 3: 6x + 9 = 3(2x + 3).",
           fakti=["Kopīgais reizinātājs - tas, ar ko dalās visi locekļi.",
                  "Iekavās - katrs loceklis, dalīts ar to.",
                  "Pārbaude: atver iekavas."]),

    Doma("Iznešana pa soļiem",
         "ab + ac = a(b + c): kopīgo reizinātāju raksta pirms iekavām.",
         soli=[
             "Skaitļiem - lielākais kopīgais dalītājs (LKD).",
             "Burtiem - burts, kas ir visos locekļos, mazākajā pakāpē.",
             "Iekavās - katrs loceklis, dalīts ar kopīgo reizinātāju.",
             "Atver iekavas un pārbaudi.",
         ],
         pieze="Ja viss loceklis ir iznests, iekavās paliek 1: "
               "4x + x = x(4 + 1)."),

    Paraugs("Ar burtiem un pakāpēm",
            uzd="Sadali reizinātājos 12a^3b − 18a^2b^2.",
            soli=[
                ("LKD(12; 18) = 6", "Skaitļi."),
                ("a: mazākā pakāpe a^2; b: mazākā pakāpe b", "Burti."),
                ("6a^2b(2a − 3b)", "Iekavās: 12a^3b : 6a^2b = 2a; "
                                   "18a^2b^2 : 6a^2b = 3b."),
            ],
            atbilde="6a^2b(2a − 3b)"),

    Ievadi("Iznes kopīgo reizinātāju", [
        {"jaut": "5x + 10", "atb": ["5(x + 2)", "5(2 + x)"], "tastatura": _T,
         "padoms": "LKD(5; 10) = 5."},
        {"jaut": "7a − 7b", "atb": ["7(a − b)"], "tastatura": _T,
         "padoms": "Abos ir 7."},
        {"jaut": "x^2 + 3x", "atb": ["x(x + 3)", "x(3 + x)"],
         "tastatura": _T, "padoms": "Abos ir x."},
        {"jaut": "12y − 8y^2", "atb": ["4y(3 − 2y)"], "tastatura": _T,
         "padoms": "LKD 4, burts y."},
        {"jaut": "a^3 + a^2", "atb": ["a^2(a + 1)", "a^2(1 + a)"],
         "tastatura": _T, "padoms": "Mazākā pakāpe a^2."},
        {"jaut": "15m^2n + 10mn", "atb": ["5mn(3m + 2)", "5mn(2 + 3m)"],
         "tastatura": _T, "padoms": "5, m, n."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "8x + 4 = 4(2x)",
         "opcijas": ["Iekavās trūkst 1: 4(2x + 1)", "Pareizi",
                     "Jābūt 8(x + 4)", "Jābūt 2(4x + 2)"],
         "pareizi": 0, "padoms": "4 : 4 = 1."},
        {"jaut": "6a − 9ab = 3(2a − 3ab)",
         "opcijas": ["Nav iznests viss: 3a(2 − 3b)", "Pareizi un pilnīgi",
                     "Jābūt 3a(2 − 9b)", "Jābūt 6(a − 9b)"],
         "pareizi": 0, "padoms": "a arī ir kopīgs."},
        {"jaut": "−x^2 − 5x = −x(x + 5)",
         "opcijas": ["Pareizi", "Jābūt −x(x − 5)", "Jābūt x(x + 5)",
                     "Jābūt −x(−x + 5)"],
         "pareizi": 0, "padoms": "−x · 5 = −5x."},
    ]),

    Pasaule("Galva rēķina",
            Ievadi("", [
                {"jaut": "Kafejnīcā 17 € reiz 23 viesi plus 17 € reiz 77 viesi. "
                         "17 · 23 + 17 · 77 = 17 · ? ",
                 "atb": ["100"], "padoms": "23 + 77."},
                {"jaut": "Kopā (€)?", "atb": ["1700"], "padoms": "17 · 100."},
                {"jaut": "4,5 · 38 + 4,5 · 62 = ?", "atb": ["450"],
                 "padoms": "4,5 · 100."},
            ]),
            pavediens="veikals",
            konteksts="Pārdevējs ar iznešanu sarēķina kopsummu galvā: kopīgā "
                      "cena ārā, daudzumi iekavās.",
            kapec="Iznešana pārvērš garu rēķinu vienā reizināšanā."),

    Kopsavilkums([
        "Atrodu kopīgo reizinātāju: LKD un burti mazākajā pakāpē.",
        "Iznesu to pirms iekavām.",
        "Pārbaudu, atverot iekavas.",
    ]),

    Majas([
        "Sadali: 14x^2 − 21x; 9a^2b + 6ab^2; 5x − 5.",
        "Galvā: 36 · 57 + 36 · 43.",
        "Izdomā izteiksmi, kurā kopīgais reizinātājs ir 4xy.",
    ]),
]
