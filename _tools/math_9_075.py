# -*- coding: utf-8 -*-
"""9. klase, 75. stunda: «Kā atrisināt vienādojumu ar iznestu reizinātāju?»

Nepilnais kvadrātvienādojums ax^2 + bx = 0: iznes x, iegūst x(ax + b) = 0,
saknes 0 un −{b|a}. Biežākā kļūda - dalīt ar x un pazaudēt sakni 0.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, likne, plakne, saknes)

TEMA = "Kā atrisināt vienādojumu ar iznestu reizinātāju?"

MERKIS = ("Atrisināsim nepilno kvadrātvienādojumu, sadalot izteiksmi "
          "reizinātājos.")

_T = "text"

SATURS = [
    Sakums("x² = 5x - cik sakņu?",
           zimejums=plakne(grafiki=[(likne(lambda x: x * x - 5 * x, -1, 6,
                                           -8, 6), "y = x² − 5x")],
                           punkti=[(0, 0, "0"), (5, 0, "5")],
                           no_x=-1, lidz_x=6, no_y=-8, lidz_y=6, solis_y=2),
           paraksts="Parabola krusto x asi divos punktos: 0 un 5.",
           fakti=["x^2 − 5x = 0 ⇒ x(x − 5) = 0.",
                  "Saknes: 0 un 5.",
                  "Dalot ar x, sakne 0 pazūd!"]),

    Doma("ax^2 + bx = 0",
         "Iznes x: x(ax + b) = 0, tātad x = 0 vai ax + b = 0.",
         soli=[
             "Pārnes visu uz vienu pusi, otrā - 0.",
             "Iznes x (un kopīgo skaitli).",
             "Pielīdzini katru reizinātāju nullei.",
             "Vienmēr viena sakne ir 0.",
         ]),

    Slidnis("Kāpēc nedrīkst dalīt ar x", [
        {"v": "✘", "teksts": "x^2 = 5x | : x ⇒ x = 5 (sakne 0 pazaudēta)"},
        {"v": "✔", "teksts": "x^2 − 5x = 0 ⇒ x(x − 5) = 0 ⇒ x = 0 vai x = 5"},
        {"v": "Pārbaude", "teksts": "0^2 = 5 · 0 ✔ un 5^2 = 5 · 5 ✔"},
    ]),

    Paraugs("Ar koeficientiem",
            uzd="Atrisini 3x^2 + 12x = 0.",
            soli=[
                ("3x(x + 4) = 0", "Iznes 3x."),
                ("x = 0 vai x + 4 = 0", "Reizinājums ir nulle."),
                ("x_1 = −4, x_2 = 0", "Saknes."),
            ],
            atbilde="−4; 0"),

    Ievadi("Atrisini", [
        {"jaut": "x^2 − 7x = 0", "atb": saknes("0", "7"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "x(x − 7) = 0."},
        {"jaut": "2x^2 + 8x = 0", "atb": saknes("−4", "0"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "2x(x + 4) = 0."},
        {"jaut": "5x^2 = 15x", "atb": saknes("0", "3"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "5x(x − 3) = 0."},
        {"jaut": "4x^2 − 6x = 0", "atb": saknes("0", "1,5"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "2x(2x − 3) = 0."},
        {"jaut": "x^2 = −x", "atb": saknes("−1", "0"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "x(x + 1) = 0."},
    ], pamats=3),

    Varianti("Kur kļūda?", [
        {"jaut": "3x^2 = 9x ⇒ 3x = 9 ⇒ x = 3",
         "opcijas": ["Pazaudēta sakne 0", "Pareizi", "Jābūt x = 27",
                     "Jābūt x = −3"],
         "pareizi": 0, "padoms": "Dalīja ar x."},
        {"jaut": "x^2 + 4x = 0 ⇒ x(x + 4) = 0 ⇒ x = 0; x = 4",
         "opcijas": ["Otrā sakne −4", "Pareizi", "Otrā sakne 2",
                     "Viena sakne"],
         "pareizi": 0, "padoms": "x + 4 = 0."},
    ]),

    Pasaule("Kvadrāts ar tādu pašu laukumu kā perimetru",
            Ievadi("", [
                {"jaut": "Kvadrāta mala x. Laukums = perimetrs: x^2 = 4x. "
                         "Kurš x der kvadrātam (x > 0)?", "atb": ["4"],
                 "padoms": "x(x − 4) = 0; x = 0 neder."},
                {"jaut": "Taisnstūris x × 6: laukums = perimetrs, "
                         "6x = 2(x + 6). x = ?", "atb": ["3"],
                 "padoms": "6x = 2x + 12."},
            ]),
            pavediens="maja",
            konteksts="Kvadrāts 4 × 4: laukums 16 un perimetrs 16 - skaitļi "
                      "sakrīt.",
            kapec="Vienādojuma sakne 0 matemātiski der, bet kvadrātam - ne."),

    Kopsavilkums([
        "Atrisinu ax^2 + bx = 0, iznesot x.",
        "Nekad nedalu ar x - saknes nepazaudēju.",
        "Izvērtēju, kura sakne der situācijai.",
    ]),

    Majas([
        "Atrisini: 6x^2 − 3x = 0; x^2 = 11x.",
        "Izdomā vienādojumu ax^2 + bx = 0 ar saknēm 0 un 2,5.",
        "Uzzīmē y = x^2 − 3x skici un atzīmē saknes.",
    ]),
]
