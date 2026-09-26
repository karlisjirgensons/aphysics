# -*- coding: utf-8 -*-
"""8. klase, 61. stunda: «Kā reizina izteiksmes ar saknēm?»

Reizina kā ar burtiem: skaitlis ar skaitli, sakne ar sakni, iekavas - katru
ar katru. (√a)^2 = a, tāpēc (2 + √3)(2 − √3) kļūst par veselu skaitli.
Saīsinātās reizināšanas formulas nāks 8.6. tematā - te iekavas atver soli
pa solim.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā reizina izteiksmes ar saknēm?"

MERKIS = ("Reizināsim izteiksmes, kas satur kvadrātsaknes, un vienkāršosim "
          "rezultātu.")

SATURS = [
    Sakums("Cik ir (√5)^2?",
           zimejums=geometrija([("A", 0, 0), ("B", 2, 0), ("C", 2, 2),
                                ("D", 0, 2)],
                               nogriezni=["AB", "BC", "CD", "DA"],
                               malas=[("AB", "√5"), ("BC", "√5")],
                               iekrasot=[("ABCD", 0)],
                               uzraksti=[(1, 1, "S = 5")]),
           paraksts="Kvadrāta ar malu √5 laukums ir 5.",
           fakti=["(√a)^2 = a, ja a ≥ 0.",
                  "Skaitļus reizina ar skaitļiem, saknes - ar saknēm.",
                  "Iekavas atver kā parasti: katru ar katru."]),

    Doma("Reizināšana ar saknēm",
         "Reizina kā ar burtiem: skaitlis ar skaitli, sakne ar sakni.",
         soli=[
             "2√3 · 5√2 = 10√6.",
             "√2(√8 + 3) = √16 + 3√2 = 4 + 3√2.",
             "(1 + √2)(3 − √2) = 3 − √2 + 3√2 − 2 = 1 + 2√2.",
         ],
         pieze="Rezultātā iznes reizinātājus un savelk līdzīgās saknes."),

    Paraugs("Iekavas ar saknēm",
            uzd="Vienkāršo (2 + √3)(2 − √3) un (√5 + 1)^2.",
            soli=[
                ("(2 + √3)(2 − √3) = 4 − 2√3 + 2√3 − 3", "Katru ar katru."),
                ("= 1", "Saknes saīsinās."),
                ("(√5 + 1)^2 = (√5 + 1)(√5 + 1)", "Kvadrāts - reizinājums "
                                                  "ar sevi."),
                ("= 5 + √5 + √5 + 1 = 6 + 2√5", "Savelk līdzīgos."),
            ],
            atbilde="1 un 6 + 2√5"),

    Ievadi("Aprēķini", [
        {"jaut": "(√7)^2 = ?", "atb": ["7"], "padoms": "√7 · √7."},
        {"jaut": "3√2 · 4√2 = ?", "atb": ["24"], "padoms": "12 · 2."},
        {"jaut": "2√3 · √12 = ?", "atb": ["12"], "padoms": "2 · √36."},
        {"jaut": "(√6 − 1)(√6 + 1) = ?", "atb": ["5"],
         "padoms": "6 + √6 − √6 − 1."},
        {"jaut": "√3(√27 − √3) = ?", "atb": ["6"], "padoms": "9 − 3."},
        {"jaut": "(3√5)^2 = ?", "atb": ["45"], "padoms": "9 · 5."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "(2√3)^2 = ?",
         "opcijas": ["12", "6", "36", "2√9"],
         "pareizi": 0, "padoms": "4 · 3."},
        {"jaut": "√2(√2 + 1) = ?",
         "opcijas": ["2 + √2", "√5", "3", "2√2 + 1"],
         "pareizi": 0, "padoms": "√2 · √2 + √2 · 1."},
        {"jaut": "(√3 + 1)^2 = ?",
         "opcijas": ["4 + 2√3", "4", "4 + √3", "2 + 2√3"],
         "pareizi": 0, "padoms": "3 + √3 + √3 + 1."},
    ]),

    Pasaule("Precīzs laukums",
            Ievadi("", [
                {"jaut": "Taisnstūra malas ir 3√2 m un 5√2 m. Laukums (m²)?",
                 "atb": ["30"], "padoms": "15 · 2."},
                {"jaut": "Kvadrāta mala ir (2 + √2) m. Laukums ir "
                         "(a + b√2) m². a = ?",
                 "atb": ["6"], "padoms": "4 + 2√2 + 2√2 + 2."},
                {"jaut": "Tajā pašā laukumā b = ?",
                 "atb": ["4"], "padoms": "2√2 + 2√2."},
            ]),
            pavediens="maja",
            konteksts="Precīzi izmēri ar saknēm rodas, piemēram, no "
                      "diagonālēm. Laukumu tad rēķina, reizinot tās.",
            kapec="Precīzajā atbildē nav noapaļošanas kļūdas."),

    Kopsavilkums([
        "Reizinu saknes un skaitļus pirms tām.",
        "Atveru iekavas ar saknēm.",
        "Zinu, ka (√a)^2 = a.",
    ]),

    Majas([
        "Aprēķini: 5√2 · 2√8; (√10)^2; √5(√20 + √5).",
        "Vienkāršo (3 − √2)(3 + √2).",
        "Izdomā taisnstūri ar malām ar saknēm, kura laukums ir vesels skaitlis.",
    ]),
]
