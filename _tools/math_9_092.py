# -*- coding: utf-8 -*-
"""9. klase, 92. stunda: «Kur atrodas parabolas virsotne?»

x_v = −{b|2a} (formulu lapā) - un kāpēc: parabola ir simetriska, virsotne
ir pa vidu starp saknēm, x_v = {x_1 + x_2|2}. Pēc tam y_v iegūst,
ievietojot x_v funkcijā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, parabola)

TEMA = "Kur atrodas parabolas virsotne?"

MERKIS = "Aprēķināsim virsotnes koordinātas un pamatosim formulu."

SATURS = [
    Sakums("Augstākais strūklakas punkts",
           zimejums=parabola(-1, 4, 0, -1, 5, -2, 5,
                             punkti=[(0, 0, "0"), (4, 0, "4"),
                                     (2, 4, "(2; 4)")]),
           paraksts="y = −x² + 4x: saknes 0 un 4, virsotne pa vidu.",
           fakti=["Parabola ir simetriska pret taisni x = x_v.",
                  "x_v = −{b|2a} = −{4|−2} = 2.",
                  "y_v = −4 + 8 = 4."]),

    Doma("Virsotne",
         "Parabolas y = ax^2 + bx + c virsotnes abscisa x_v = −{b|2a}; "
         "ordinātu y_v iegūst, ievietojot x_v.",
         soli=[
             "Aprēķini x_v = −{b|2a}.",
             "Ievieto: y_v = a · x_v^2 + b · x_v + c.",
             "Pārbaude: ja ir saknes, x_v = {x_1 + x_2|2}.",
             "Simetrijas ass: taisne x = x_v.",
         ],
         pieze="Formula izriet no pilnā kvadrāta: a(x + {b|2a})^2 + ... - "
               "kvadrāts ir 0 pie x = −{b|2a}."),

    Slidnis("Simetrija", [
        {"v": "x = 1", "teksts": "y(1) = 3; simetriskais punkts x = 3, "
                                 "y(3) = 3",
         "zim": parabola(-1, 4, 0, -1, 5, -2, 5,
                         punkti=[(1, 3, "1"), (3, 3, "3")])},
        {"v": "x = 0", "teksts": "y(0) = 0; simetriskais x = 4, y(4) = 0",
         "zim": parabola(-1, 4, 0, -1, 5, -2, 5,
                         punkti=[(0, 0, "0"), (4, 0, "4")])},
        {"v": "x = 2", "teksts": "Virsotne: tā pati ass abiem pāriem",
         "zim": parabola(-1, 4, 0, -1, 5, -2, 5,
                         punkti=[(2, 4, "(2; 4)")])},
    ]),

    Paraugs("Eksāmens 2025, 13.1.",
            uzd="Dota funkcija y = x^2 + 2x. Aprēķini parabolas virsotnes "
                "abscisu x_v.",
            soli=[
                ("a = 1, b = 2", "Koeficienti."),
                ("x_v = −{2|2 · 1} = −1", "Formula."),
                ("y_v = 1 − 2 = −1", "Ja vajag arī ordinātu."),
            ],
            atbilde="x_v = −1"),

    Ievadi("Aprēķini virsotni", [
        {"jaut": "y = x^2 − 6x + 5. x_v = ?", "atb": ["3"],
         "padoms": "−{−6|2}."},
        {"jaut": "Tai pašai y_v = ?", "atb": ["−4", "-4"],
         "padoms": "9 − 18 + 5."},
        {"jaut": "y = −2x^2 + 8x − 3. x_v = ?", "atb": ["2"],
         "padoms": "−{8|−4}."},
        {"jaut": "Tai pašai y_v = ?", "atb": ["5"],
         "padoms": "−8 + 16 − 3."},
        {"jaut": "y = x^2 + 5. Virsotne x_v = ?", "atb": ["0"],
         "padoms": "b = 0."},
        {"jaut": "Saknes 1 un 7. x_v = ?", "atb": ["4"],
         "padoms": "Vidū."},
    ], pamats=4),

    Varianti("Izvēlies virsotni", [
        {"jaut": "y = (x − 3)^2 + 2",
         "opcijas": ["(3; 2)", "(−3; 2)", "(3; −2)", "(2; 3)"],
         "pareizi": 0, "padoms": "Pilnā kvadrāta forma."},
        {"jaut": "y = x^2 − 4",
         "opcijas": ["(0; −4)", "(4; 0)", "(2; 0)", "(0; 4)"],
         "pareizi": 0, "padoms": "b = 0."},
    ]),

    Pasaule("Strūklakas augstums",
            Ievadi("", [
                {"jaut": "Strūkla y = −0,5x^2 + 3x. Cik m no sprauslas ir "
                         "augstākais punkts (x_v)?", "atb": ["3"],
                 "padoms": "−{3|−1}."},
                {"jaut": "Cik m augstu ūdens paceļas (y_v)?", "atb": ["4,5"],
                 "padoms": "−4,5 + 9."},
            ]),
            pavediens="tehnika",
            konteksts="Strūklakas projektā norāda, cik augstu un cik tālu "
                      "sniedzas strūkla.",
            kapec="Virsotne ir augstākais punkts."),

    Kopsavilkums([
        "Aprēķinu x_v = −{b|2a} un y_v.",
        "Izmantoju parabolas simetriju.",
        "Pārbaudu: x_v ir pa vidu starp saknēm.",
    ]),

    Majas([
        "Atrodi virsotni: y = 2x^2 − 12x + 7; y = −x^2 − 2x.",
        "Uzraksti parabolu ar virsotni (1; −3).",
        "Pamato formulu x_v = −{b|2a} ar simetriju.",
    ]),
]
