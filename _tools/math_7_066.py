# -*- coding: utf-8 -*-
"""7. klase, 66. stunda: «Kā uzzīmēt grafiku pēc nosacījumiem?»

Ja zināmi divi nosacījumi - piemēram, divi grafika punkti vai slīpums un
viens punkts -, lineāro funkciju var atrast pilnībā. Stunda iemāca no
nosacījumiem atrast k un b un uzzīmēt grafiku.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā uzzīmēt grafiku pēc nosacījumiem?"

MERKIS = ("Zīmēsim grafiku lineārai funkcijai, kas atbilst diviem "
          "nosacījumiem.")

SATURS = [
    Sakums("Divi punkti - viena taisne",
           zimejums=plakne(grafiki=[(2, -1, "")],
                           punkti=[(1, 1, "A"), (3, 5, "B")],
                           no_x=-1, lidz_x=5, no_y=-2, lidz_y=7, solis=1),
           paraksts="Caur A(1; 1) un B(3; 5) iet tikai viena taisne.",
           fakti=["No A uz B: 2 pa labi, 4 uz augšu.",
                  "Uz 1 pa labi - 2 uz augšu: k = 2.",
                  "Ejot atpakaļ līdz x = 0: b = −1."]),

    Doma("Divi nosacījumi nosaka k un b",
         "Lineāro funkciju y = kx + b pilnībā nosaka divi nosacījumi. Ja "
         "doti divi punkti, k ir vērtības izmaiņa, dalīta ar argumenta "
         "izmaiņu, un b atrod, ievietojot vienu punktu.",
         soli=[
             "Aprēķini k: (y_2 − y_1) : (x_2 − x_1).",
             "Ievieto vienu punktu y = kx + b un atrodi b.",
             "Uzraksti formulu.",
             "Pārbaudi ar otru punktu.",
         ],
         pieze="Citi nosacījumi: «paralēla taisnei y = 3x» dod k = 3; «krusto "
               "y asi punktā 4» dod b = 4."),

    Paraugs("Caur diviem punktiem",
            uzd="Atrodi lineāro funkciju, kuras grafiks iet caur A(1; 1) un "
                "B(3; 5).",
            soli=[
                ("k = (5 − 1) : (3 − 1) = 2", "Izmaiņu dalījums."),
                ("1 = 2 · 1 + b", "Ievieto A."),
                ("b = −1", "Atrisina."),
                ("y = 2x − 1; pārbaude B: 2 · 3 − 1 = 5", "Der."),
            ],
            atbilde="y = 2x − 1"),

    Varianti("Kura funkcija atbilst?", [
        {"jaut": "Paralēla y = −x un iet caur (0; 3).",
         "opcijas": ["y = −x + 3", "y = x + 3", "y = −x − 3", "y = 3x"],
         "pareizi": 0,
         "padoms": "k = −1, b = 3."},
        {"jaut": "Iet caur (0; 0) un (2; 6).",
         "opcijas": ["y = 3x", "y = 2x + 6", "y = 6x", "y = x + 4"],
         "pareizi": 0,
         "padoms": "b = 0, k = 6 : 2."},
        {"jaut": "Krusto asis punktos (0; 4) un (2; 0).",
         "opcijas": ["y = −2x + 4", "y = 2x + 4", "y = −4x + 2",
                     "y = 2x − 4"],
         "pareizi": 0,
         "padoms": "b = 4; k = (0 − 4) : 2."},
        {"jaut": "Augoša, un iet caur (0; −2).",
         "opcijas": ["y = 3x − 2", "y = −3x − 2", "y = 3x + 2",
                     "y = −2"],
         "pareizi": 0,
         "padoms": "k > 0, b = −2."},
    ], pamats=4),

    Ievadi("Atrodi k un b", [
        {"jaut": "Taisne caur (0; 3) un (4; 11). k = ?",
         "atb": ["2"], "padoms": "8 : 4."},
        {"jaut": "Taisne caur (2; 7) un (5; 1). k = ?",
         "atb": ["−2", "-2"], "padoms": "(1 − 7) : (5 − 2)."},
        {"jaut": "Tai pašai taisnei b = ?",
         "atb": ["11"], "padoms": "7 = −4 + b."},
        {"jaut": "Paralēla y = 3x + 1 un iet caur (1; 10). b = ?",
         "atb": ["7"], "padoms": "10 = 3 + b."},
    ]),

    Zimejums("y = −2x + 11",
             plakne(grafiki=[(-2, 11, "y = −2x + 11")],
                    punkti=[(2, 7), (5, 1)],
                    no_x=0, lidz_x=6, no_y=0, lidz_y=12, solis=1, solis_y=2),
             paskaidro="Caur (2; 7) un (5; 1)."),

    Pasaule("Taksometra tarifs no čekiem",
            Ievadi("", [
                {"jaut": "Brauciens 4 km maksāja 6 €, brauciens 10 km - "
                         "10,80 €. Cik € maksā 1 km?",
                 "atb": ["0,8"], "padoms": "4,8 : 6."},
                {"jaut": "Cik € ir iekāpšanas maksa?",
                 "atb": ["2,8"], "padoms": "6 − 4 · 0,8."},
                {"jaut": "Cik € maksās 15 km?",
                 "atb": ["14,8"], "padoms": "2,8 + 12."},
            ]),
            pavediens="celojums",
            konteksts="No diviem čekiem var atjaunot visu tarifu - divi "
                      "punkti nosaka taisni.",
            kapec="Divi nosacījumi - k un b."),

    Kopsavilkums([
        "Atrodu k no diviem punktiem.",
        "Atrodu b, ievietojot punktu.",
        "Lietoju nosacījumus «paralēla» un «krusto asi».",
        "Pārbaudu funkciju ar otru punktu.",
    ]),

    Majas([
        "Atrodi funkciju caur (1; 5) un (4; 14).",
        "Atjauno sava telefona tarifu no diviem rēķiniem.",
        "Uzraksti divus nosacījumus un palūdz draugam atrast funkciju.",
    ]),
]
