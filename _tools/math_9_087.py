# -*- coding: utf-8 -*-
"""9. klase, 87. stunda: «Kā lietot sakņu formulu?»

x_{1;2} = {−b ± √D|2a} - universāla metode jebkuram kvadrātvienādojumam.
Stunda seko eksāmena 7.2. uzdevumam (2x^2 + 7x − 4 = 0, 3 punkti) un rāda,
kā noformēt risinājumu, lai dabūtu visus punktus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, parabola, saknes)

TEMA = "Kā lietot sakņu formulu?"

MERKIS = ("Atrisināsim kvadrātvienādojumu ar sakņu formulu un noformēsim "
          "risinājumu.")

_T = "text"

SATURS = [
    Sakums("Viena formula - jebkuram kvadrātvienādojumam",
           zimejums=parabola(2, 7, -4, -5, 2, -12, 4,
                             punkti=[(-4, 0, "−4"), (0.5, 0, "0,5")]),
           paraksts="2x² + 7x − 4 = 0: saknes −4 un 0,5 - bez minēšanas.",
           fakti=["x_{1;2} = {−b ± √D|2a} - eksāmena formulu lapā.",
                  "Ja D = 0, abas saknes sakrīt: x = {−b|2a}.",
                  "Formula iegūta ar pilnā kvadrāta atdalīšanu."]),

    Doma("Sakņu formula",
         "Ja D ≥ 0, kvadrātvienādojuma ax^2 + bx + c = 0 saknes ir "
         "x_{1;2} = {−b ± √D|2a}.",
         soli=[
             "Pieraksti a, b, c.",
             "Aprēķini D un pārbaudi zīmi.",
             "Ievieto formulā: vispirms ar +, tad ar −.",
             "Pieraksti atbildi: x_1 = ..., x_2 = ... .",
         ]),

    Paraugs("Eksāmens 2025, 7.2. uzdevums (3 punkti)",
            uzd="Atrisini vienādojumu 2x^2 + 7x − 4 = 0.",
            soli=[
                ("D = 7^2 − 4 · 2 · (−4) = 81", "1. punkts - diskriminants."),
                ("x_{1;2} = {−7 ± 9|4}", "2. punkts - formula ar vērtībām."),
                ("x_1 = {−7 + 9|4} = 0,5; x_2 = {−7 − 9|4} = −4",
                 "3. punkts - abas saknes."),
            ],
            atbilde="x_1 = 0,5; x_2 = −4"),

    Slidnis("Kur rodas kļūdas", [
        {"v": "−b", "teksts": "b = −6 ⇒ −b = 6 (nevis −6)"},
        {"v": "b²", "teksts": "(−6)^2 = 36 (nevis −36)"},
        {"v": "2a", "teksts": "Dala VISU skaitītāju: {−b ± √D|2a}, ne tikai √D"},
        {"v": "±", "teksts": "Divas saknes - neaizmirsti «−» variantu"},
    ]),

    Ievadi("Atrisini ar sakņu formulu", [
        {"jaut": "x^2 − 6x + 5 = 0", "atb": saknes("1", "5"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "D = 16."},
        {"jaut": "x^2 + 2x − 15 = 0", "atb": saknes("−5", "3"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "D = 64."},
        {"jaut": "2x^2 − 5x + 2 = 0", "atb": saknes("0,5", "2"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "D = 9; {5 ± 3|4}."},
        {"jaut": "3x^2 + 5x − 2 = 0", "atb": saknes("−2", "{1|3}") +
         saknes("−2", "1/3"), "tastatura": _T, "vieta": "x₁; x₂",
         "padoms": "D = 49; {−5 ± 7|6}."},
        {"jaut": "4x^2 − 4x + 1 = 0", "atb": ["0,5"],
         "padoms": "D = 0; x = {4|8}."},
    ], pamats=3),

    Varianti("Kura rinda pareiza?", [
        {"jaut": "x^2 − 4x − 12 = 0: x_{1;2} = ?",
         "opcijas": ["{4 ± 8|2}", "{−4 ± 8|2}", "{4 ± 64|2}", "{4 ± 8|1}"],
         "pareizi": 0, "padoms": "−b = 4, √D = 8."},
        {"jaut": "Saknes no {4 ± 8|2}:",
         "opcijas": ["6 un −2", "12 un −4", "4 un 8", "6 un 2"],
         "pareizi": 0, "padoms": "{12|2} un {−4|2}."},
    ]),

    Pasaule("Ietve ap baseinu",
            Ievadi("", [
                {"jaut": "Baseins 10 m × 6 m, ap to ietve x m platumā; kopā ar "
                         "ietvi laukums 96 m². (10 + 2x)(6 + 2x) = 96 ⇒ "
                         "x^2 + 8x − 9 = 0. Pozitīvā sakne?", "atb": ["1"],
                 "padoms": "D = 100; {−8 + 10|2}."},
                {"jaut": "Ietves laukums (m²)?", "atb": ["36"],
                 "padoms": "96 − 60."},
            ]),
            pavediens="maja",
            konteksts="Arhitekts plāno flīzēm noklātu joslu ap baseinu ar "
                      "zināmu kopējo laukumu.",
            kapec="Negatīvā sakne −9 platumam neder."),

    Kopsavilkums([
        "Lietoju sakņu formulu x_{1;2} = {−b ± √D|2a}.",
        "Noformēju risinājumu eksāmena stilā.",
        "Izvairos no zīmju kļūdām.",
    ]),

    Majas([
        "Atrisini: 3x^2 − 7x + 2 = 0; x^2 + 10x + 21 = 0.",
        "Pārbaudi saknes ar Vjetu.",
        "Pieraksti risinājumu tā, kā eksāmenā (3 soļi).",
    ]),
]
