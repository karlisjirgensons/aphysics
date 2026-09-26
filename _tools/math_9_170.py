# -*- coding: utf-8 -*-
"""9. klase, 170. stunda: «Kā risinu vienādojumus un funkcijas?»

Eksāmena 1. daļas algebras otrā puse (2025. gada 7.-13. uzdevuma formāts):
lineārs un kvadrātvienādojums, sistēma, nevienādību sistēma kā intervāls,
lineāras funkcijas un parabolas īpašības, kustības grafiks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, paris, parabola, plakne, saknes)

TEMA = "Kā risinu vienādojumus un funkcijas?"

MERKIS = ("Risināsim eksāmena formāta uzdevumus par vienādojumiem, sistēmām "
          "un funkciju grafikiem.")

_LAIVA = [(0, 0), (2, 30), (4, 30), (5, 0)]

SATURS = [
    Sakums("Parabola, taisne, vienādojums - viens uzdevums trīs veidos",
           zimejums=parabola(1, 2, 0, -4, 2, -2, 4),
           paraksts="y = x^2 + 2x: saknes −2 un 0, virsotne x_v = −1.",
           fakti=["Saknes - kur grafiks krusto x asi.",
                  "x_v = −{b|2a}.",
                  "Punkts pieder grafikam, ja koordinātas der formulai."]),

    Paraugs("Kvadrātvienādojums (3 punkti)",
            uzd="Atrisini vienādojumu 2x^2 + 7x − 4 = 0.",
            soli=[
                ("D = b^2 − 4ac = 49 + 32 = 81", "Diskriminants."),
                ("x_{1;2} = {−7 ± 9|4}", "Sakņu formula."),
                ("x_1 = −4; x_2 = 0,5", "Aprēķins."),
            ],
            atbilde="x_1 = −4; x_2 = 0,5"),

    Ievadi("Vienādojumi", [
        {"jaut": "x − 4 = 11", "atb": ["15"], "padoms": "11 + 4."},
        {"jaut": "x^2 − 16 = 0 (saknes)", "atb": saknes("−4", "4"),
         "tastatura": "text", "vieta": "piem. 1; 4",
         "padoms": "x^2 = 16."},
        {"jaut": "3x^2 + 16x − 12 = 0 (saknes)",
         "atb": saknes("−6", "2/3"), "tastatura": "text",
         "vieta": "piem. 1; 4", "padoms": "D = 256 + 144 = 400."},
        {"jaut": "x + y = 7; x − y = 1", "atb": paris(4, 3),
         "tastatura": "text", "vieta": "(x; y)",
         "padoms": "Saskaiti: 2x = 8."},
    ]),

    Varianti("Funkcijas", [
        {"jaut": "Nevienādību sistēmas 1 < x un x < 3 atrisinājums...",
         "opcijas": ["(1; 3)", "[1; 3]", "(−∞; 3)", "(1; +∞)"],
         "pareizi": 0, "padoms": "Stingras nevienādības - apaļas iekavas."},
        {"jaut": "Vai A(3; 1) pieder y = x^2 + 2x grafikam?",
         "opcijas": ["Nē, jo 3^2 + 2 · 3 = 15 ≠ 1", "Jā",
                     "Nē, jo x ≠ y", "Nevar noteikt"],
         "pareizi": 0, "padoms": "Ievieto x = 3."},
        {"jaut": "y = −3x + 5 grafiks...",
         "opcijas": ["dilst, krusto y asi (0; 5)",
                     "aug, krusto y asi (0; 5)",
                     "dilst, krusto y asi (0; −3)",
                     "aug, krusto y asi (5; 0)"],
         "pareizi": 0, "padoms": "k < 0 - dilst."},
    ]),

    Ievadi("Funkcijas vērtības", [
        {"jaut": "y = −3x + 5, x = 2. y = ?", "atb": ["−1"],
         "padoms": "−6 + 5."},
        {"jaut": "y = x^2 + 2x virsotnes ordināta y_v?", "atb": ["−1"],
         "padoms": "(−1)^2 + 2 · (−1)."},
        {"jaut": "y = x^2 − 6x + 5 virsotnes abscisa?", "atb": ["3"],
         "padoms": "{6|2}."},
    ]),

    Pasaule("Brauciens ar motorlaivu",
            Ievadi("", [
                {"jaut": "Cik km ir no piestātnes līdz pludmalei?",
                 "atb": ["30"], "padoms": "Augstākais punkts."},
                {"jaut": "Ātrums līdz pludmalei (km/h)?", "atb": ["15"],
                 "padoms": "30 km : 2 h."},
                {"jaut": "Cik stundas tūrists atpūtās?", "atb": ["2"],
                 "padoms": "Horizontālais posms."},
                {"jaut": "Ātrums atpakaļceļā (km/h)?", "atb": ["30"],
                 "padoms": "30 km : 1 h."},
            ]),
            pavediens="celojums",
            konteksts="Grafikā - tūrista attālums no piestātnes atkarībā no "
                      "laika.",
            kapec="Kustības grafiks ir funkcijas grafiks: slīpums ir "
                  "ātrums.",
            zimejums=plakne(lauzta=_LAIVA, punkti=_LAIVA, no_x=0, lidz_x=6,
                            no_y=0, lidz_y=40, solis=1, solis_y=10,
                            x_nos="h", y_nos="km")),

    Kopsavilkums([
        "Risinu lineāru un kvadrātvienādojumu un sistēmu.",
        "Nosaku parabolas virsotni un pārbaudu punktu uz grafika.",
        "Nolasu ātrumu no kustības grafika.",
    ]),

    Majas([
        "Atrisini 3 kvadrātvienādojumus un pārbaudi ar Vjeta teorēmu.",
        "Uzzīmē y = −3x + 5 grafiku pēc divām vērtību tabulas rindām.",
        "Uzzīmē sava ceļa uz skolu grafiku (laiks - attālums).",
    ]),
]
