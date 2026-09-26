# -*- coding: utf-8 -*-
"""9. klase, 93. stunda: «Kas ir funkcijas nulles?»

Funkcijas nulles - argumenta vērtības, pie kurām y = 0 - ir tās pašas
vienādojuma saknes. Stundā arī krustpunkts ar y asi (0; c) un eksāmena
13.2. uzdevums: pamatot, ka punkts nepieder grafikam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, parabola, saknes)

TEMA = "Kas ir funkcijas nulles?"

MERKIS = ("Noteiksim funkcijas nulles un saistīsim tās ar vienādojuma "
          "saknēm.")

_T = "text"

SATURS = [
    Sakums("Kur grafiks satiek asis?",
           zimejums=parabola(1, -2, -8, -3, 5, -10, 6,
                             punkti=[(-2, 0, "−2"), (4, 0, "4"),
                                     (0, -8, "(0; −8)")]),
           paraksts="y = x² − 2x − 8: nulles −2 un 4; ar y asi (0; −8).",
           fakti=["Nulles: x, kuriem y = 0.",
                  "Tās ir vienādojuma x^2 − 2x − 8 = 0 saknes.",
                  "Ar y asi grafiks krustojas punktā (0; c)."]),

    Doma("Funkcijas nulles",
         "Funkcijas y = f(x) nulles ir x vērtības, pie kurām f(x) = 0; "
         "grafikā - krustpunkti ar x asi.",
         soli=[
             "Pielīdzini funkciju nullei: ax^2 + bx + c = 0.",
             "Atrisini (jebkura metode).",
             "Krustpunkti ar x asi: (x_1; 0) un (x_2; 0).",
             "Krustpunkts ar y asi: x = 0, y = c.",
         ]),

    Paraugs("Eksāmens 2025, 13.2. (2 punkti)",
            uzd="Pamato, ka punkts A(3; 1) nepieder funkcijas y = x^2 + 2x "
                "grafikam.",
            soli=[
                ("x = 3: y = 3^2 + 2 · 3 = 15", "Ievieto abscisu."),
                ("15 ≠ 1", "Ordināta nesakrīt."),
                ("Tātad A nepieder grafikam", "Secinājums vārdiem."),
            ],
            atbilde="y(3) = 15 ≠ 1"),

    Ievadi("Atrodi", [
        {"jaut": "y = x^2 − 9: nulles", "atb": saknes("−3", "3"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "x^2 = 9."},
        {"jaut": "y = x^2 + 4x: nulles", "atb": saknes("−4", "0"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "x(x + 4) = 0."},
        {"jaut": "y = 2x^2 − 3x + 7: krustpunkta ar y asi ordināta?",
         "atb": ["7"], "padoms": "y(0) = c."},
        {"jaut": "y = x^2 − 5x + 6: nulles", "atb": saknes("2", "3"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "D = 1."},
        {"jaut": "Vai punkts (2; 4) pieder y = x^2? (y(2) = ?)",
         "atb": ["4"], "padoms": "2^2 = 4 - pieder."},
    ], pamats=3),

    Varianti("Pieder vai nepieder?", [
        {"jaut": "(1; 0) un y = x^2 − 1",
         "opcijas": ["Pieder", "Nepieder"], "jaukt": False,
         "pareizi": 0, "padoms": "1 − 1 = 0."},
        {"jaut": "(−2; 5) un y = x^2 + x",
         "opcijas": ["Pieder", "Nepieder"], "jaukt": False,
         "pareizi": 1, "padoms": "4 − 2 = 2 ≠ 5."},
        {"jaut": "(0; −3) un y = 2x^2 − 3",
         "opcijas": ["Pieder", "Nepieder"], "jaukt": False,
         "pareizi": 0, "padoms": "c = −3."},
    ]),

    Pasaule("Tilta arka",
            Ievadi("", [
                {"jaut": "Arka y = −0,02x^2 + 2x (metros). Kur arka balstās uz "
                         "zemes? Nulles:", "atb": saknes("0", "100"),
                 "tastatura": _T, "vieta": "x₁; x₂",
                 "padoms": "x(−0,02x + 2) = 0."},
                {"jaut": "Arkas laidums (m)?", "atb": ["100"],
                 "padoms": "100 − 0."},
            ]),
            pavediens="tehnika",
            konteksts="Tērauda tilta arka ir parabola; tās nulles ir balstu "
                      "vietas.",
            kapec="Nulles dod laidumu starp balstiem."),

    Kopsavilkums([
        "Atrodu funkcijas nulles.",
        "Atrodu krustpunktu ar y asi.",
        "Pamatoju, vai punkts pieder grafikam.",
    ]),

    Majas([
        "Atrodi nulles un krustpunktu ar y asi: y = x^2 + x − 12.",
        "Pamato, ka B(−1; 4) nepieder grafikam y = 3x^2 − 2x.",
        "Uzzīmē skici ar atrastajiem punktiem.",
    ]),
]
