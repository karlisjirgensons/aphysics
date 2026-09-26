# -*- coding: utf-8 -*-
"""9. klase, 76. stunda: «Kā atrisināt vienādojumu ar kvadrātu starpību?»

ax^2 − c = 0: kvadrātu starpība dod divas pretējas saknes ±√({c|a}).
x^2 = 9 ir x = ±3, nevis tikai 3 - to rāda gan formula, gan parabolas
krustpunkti ar taisni y = 9.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, likne, plakne, saknes)

TEMA = "Kā atrisināt vienādojumu ar kvadrātu starpību?"

MERKIS = ("Atrisināsim vienādojumu, lietojot kvadrātu starpības formulu.")

_T = "text"

SATURS = [
    Sakums("x² = 9 - tikai 3?",
           zimejums=plakne(grafiki=[(likne(lambda x: x * x, -4, 4, -2, 10),
                                     "y = x²"), (0, 9, "y = 9")],
                           punkti=[(-3, 9, "−3"), (3, 9, "3")],
                           no_x=-4, lidz_x=4, no_y=-2, lidz_y=10, solis_y=2),
           paraksts="Parabola un taisne krustojas divos punktos.",
           fakti=["(−3)^2 = 9 tāpat kā 3^2 = 9.",
                  "x^2 − 9 = (x − 3)(x + 3) = 0.",
                  "Saknes: x = ±3."]),

    Doma("x^2 = c",
         "Ja c > 0, vienādojumam x^2 = c ir divas saknes: x = ±√c.",
         soli=[
             "Pārveido: ax^2 = c ⇒ x^2 = {c|a}.",
             "Vai ar formulu: x^2 − c = (x − √c)(x + √c) = 0.",
             "Neaizmirsti ± - saknes ir pretēji skaitļi.",
             "Ja c nav pilns kvadrāts - atbilde ar sakni: ±√7.",
         ]),

    Paraugs("Ar koeficientu",
            uzd="Atrisini 4x^2 − 25 = 0.",
            soli=[
                ("(2x − 5)(2x + 5) = 0", "Kvadrātu starpība."),
                ("2x = 5 vai 2x = −5", "Katrs reizinātājs."),
                ("x = ±2,5", "Saknes."),
            ],
            atbilde="−2,5; 2,5"),

    Ievadi("Atrisini", [
        {"jaut": "x^2 − 16 = 0", "atb": saknes("−4", "4"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "(x − 4)(x + 4) = 0."},
        {"jaut": "x^2 = 49", "atb": saknes("−7", "7"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "±7."},
        {"jaut": "9x^2 − 1 = 0", "atb": saknes("−{1|3}", "{1|3}") +
         saknes("−1/3", "1/3"), "tastatura": _T, "vieta": "x₁; x₂",
         "padoms": "(3x − 1)(3x + 1) = 0."},
        {"jaut": "2x^2 = 50", "atb": saknes("−5", "5"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "x^2 = 25."},
        {"jaut": "x^2 − 0,36 = 0", "atb": saknes("−0,6", "0,6"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "0,6^2 = 0,36."},
    ], pamats=3),

    Varianti("Izvēlies atbildi", [
        {"jaut": "x^2 = 7",
         "opcijas": ["x = ±√7", "x = √7", "x = 3,5", "Nav sakņu"],
         "pareizi": 0, "padoms": "Divas saknes."},
        {"jaut": "(x − 1)^2 = 4",
         "opcijas": ["x = 3 vai x = −1", "x = 3", "x = ±2", "x = 5"],
         "pareizi": 0, "padoms": "x − 1 = ±2."},
        {"jaut": "x^2 + 4 = 0",
         "opcijas": ["Nav reālu sakņu", "x = ±2", "x = −2", "x = 2"],
         "pareizi": 0, "padoms": "x^2 = −4 - neiespējami."},
    ]),

    Pasaule("Kvadrātveida flīze",
            Ievadi("", [
                {"jaut": "Kvadrātveida flīzes laukums 900 cm². Mala (cm)?",
                 "atb": ["30"], "padoms": "x^2 = 900, x > 0."},
                {"jaut": "Grīda 36 000 cm², vajag 400 vienādas kvadrātveida "
                         "flīzes. Vienas flīzes mala (cm, līdz desmitdaļām)?",
                 "atb": ["9,5"], "padoms": "x^2 = 90, x ≈ 9,49."},
            ]),
            pavediens="maja",
            konteksts="Flīzes malu aprēķina no laukuma; negatīvā sakne "
                      "garumam neder.",
            kapec="Vienādojumam divas saknes, situācijai - viena."),

    Kopsavilkums([
        "Atrisinu ax^2 − c = 0 ar kvadrātu starpību.",
        "Pierakstu abas saknes ±.",
        "Zinu, kad sakņu nav.",
    ]),

    Majas([
        "Atrisini: 16x^2 = 9; x^2 − 12 = 0.",
        "Atrisini (x + 2)^2 = 25.",
        "Paskaidro, kāpēc x^2 = −9 nav sakņu.",
    ]),
]
