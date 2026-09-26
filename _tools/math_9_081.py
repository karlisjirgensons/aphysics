# -*- coding: utf-8 -*-
"""9. klase, 81. stunda: «Kā atrisināt spriežot?»

Pirms sakņu formulas - ar galvu: (x − 3)^2 = 16 izvelk sakni, x^2 − 5x + 6
sadala reizinātājos (x − 2)(x − 3), jo 2 + 3 = 5 un 2 · 3 = 6. Tā
skolēns redz, ka saknes ir «apslēptas» koeficientos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis, saknes)

TEMA = "Kā atrisināt spriežot?"

MERKIS = ("Atrisināsim vienkāršu kvadrātvienādojumu, spriežot vai sadalot "
          "reizinātājos.")

_T = "text"

SATURS = [
    Sakums("Divi skaitļi: summa 5, reizinājums 6",
           zimejums=restis([["x₁", "x₂", "summa", "reizinājums"],
                            ["1", "6", "7", "6"], ["2", "3", "5", "6"]]),
           paraksts="2 un 3 - tās ir x² − 5x + 6 = 0 saknes.",
           fakti=["(x − 2)(x − 3) = x^2 − 5x + 6.",
                  "Ja a = 1: summa = −b, reizinājums = c.",
                  "Tā saknes var uzminēt, ja tās ir veseli skaitļi."]),

    Slidnis("Divi spriešanas ceļi", [
        {"v": "Kvadrāts", "teksts": "(x − 3)^2 = 16 ⇒ x − 3 = ±4 ⇒ x = 7 vai "
                                    "x = −1"},
        {"v": "Reizinātāji", "teksts": "x^2 − 5x + 6 = 0 ⇒ (x − 2)(x − 3) = 0 "
                                       "⇒ x = 2 vai x = 3"},
        {"v": "Pārbaude", "teksts": "2^2 − 5 · 2 + 6 = 0 ✔; 9 − 15 + 6 = 0 ✔"},
    ]),

    Doma("Spriešana",
         "Ja x^2 + bx + c = (x − m)(x − n), tad m + n = −b un m · n = c.",
         soli=[
             "Meklē divus skaitļus ar reizinājumu c.",
             "No tiem izvēlies pāri, kuru summa ir −b.",
             "Saknes ir šie skaitļi.",
             "Ja neizdodas - lietos sakņu formulu (86.-87. stunda).",
         ],
         pieze="Šī sakarība ir Vjeta teorēma - tā ir eksāmena formulu lapā: "
               "x_1 + x_2 = −p, x_1 · x_2 = q."),

    Paraugs("Ar negatīvām saknēm",
            uzd="Atrisini x^2 + 7x + 12 = 0.",
            soli=[
                ("Reizinājums 12, summa −7", "−b = −7."),
                ("−3 un −4: (−3) · (−4) = 12, −3 + (−4) = −7",
                 "Pāris atrasts."),
                ("(x + 3)(x + 4) = 0", "Pārbaude ar atvēršanu."),
            ],
            atbilde="x_1 = −4, x_2 = −3"),

    Ievadi("Atrisini spriežot", [
        {"jaut": "x^2 − 7x + 10 = 0", "atb": saknes("2", "5"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "2 · 5 = 10, 2 + 5 = 7."},
        {"jaut": "x^2 + x − 6 = 0", "atb": saknes("−3", "2"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "Reizinājums −6, summa −1."},
        {"jaut": "(x + 1)^2 = 9", "atb": saknes("−4", "2"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "x + 1 = ±3."},
        {"jaut": "x^2 − 2x − 8 = 0", "atb": saknes("−2", "4"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "−2 · 4 = −8."},
        {"jaut": "x^2 − 6x + 9 = 0", "atb": ["3"],
         "padoms": "(x − 3)^2 = 0."},
    ], pamats=3),

    Varianti("Kurš pāris der?", [
        {"jaut": "x^2 − 9x + 20 = 0",
         "opcijas": ["4 un 5", "2 un 10", "−4 un −5", "1 un 20"],
         "pareizi": 0, "padoms": "Summa 9."},
        {"jaut": "x^2 + 2x − 15 = 0",
         "opcijas": ["−5 un 3", "5 un −3", "−5 un −3", "15 un 1"],
         "pareizi": 0, "padoms": "Summa −2."},
    ]),

    Pasaule("Kinoteātra zāle",
            Ievadi("", [
                {"jaut": "Zālē rindu ir par 4 mazāk nekā vietu rindā; kopā "
                         "96 vietas. x(x − 4) = 96. Cik vietu rindā?",
                 "atb": ["12"], "padoms": "12 · 8 = 96."},
                {"jaut": "Cik rindu?", "atb": ["8"], "padoms": "12 − 4."},
            ]),
            pavediens="skola",
            konteksts="Skolas aktu zāles krēslus izvieto taisnstūrī; zina "
                      "kopskaitu un starpību.",
            kapec="Spriežot atrod pāri 12 un 8 bez formulas."),

    Kopsavilkums([
        "Atrisinu (x − m)^2 = k, izvelkot sakni.",
        "Sadalu x^2 + bx + c reizinātājos, meklējot pāri.",
        "Pārbaudu saknes, ievietojot tās.",
    ]),

    Majas([
        "Atrisini spriežot: x^2 − 11x + 30 = 0; x^2 + 3x − 10 = 0.",
        "Izdomā vienādojumu ar saknēm 6 un −1.",
        "Kāpēc x^2 + x + 1 = 0 nevar atrisināt spriežot? (Padoms: 86. stunda.)",
    ]),
]
