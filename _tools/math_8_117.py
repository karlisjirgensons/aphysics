# -*- coding: utf-8 -*-
"""8. klase, 117. stunda: «Kā aprēķināt polinoma vērtību?»

Bloka noslēgums: vērtību iegūst, ievietojot skaitli; negatīvu skaitli
ievieto iekavās. Ar vērtību pārbauda pārveidojumu - ja vērtības atšķiras,
ir kļūda; ja sakrīt, pārveidojums visticamāk pareizs, bet tas vēl nav
pierādījums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā aprēķināt polinoma vērtību?"

MERKIS = ("Aprēķināsim polinoma vērtību dotai mainīgā vērtībai un "
          "pārbaudīsim pārveidojumu.")

SATURS = [
    Sakums("P(x) = x² − 3x + 2. Kad tas ir 0?",
           zimejums=restis([["x", "0", "1", "2", "3"],
                            ["P(x)", "2", "0", "0", "2"]]),
           paraksts="Vērtības tabula: x = 1 un x = 2 dod nulli.",
           fakti=["Vērtību aprēķina, ievietojot skaitli mainīgā vietā.",
                  "Negatīvu skaitli ievieto iekavās: (−2)^2 = 4.",
                  "Ar vērtību var pārbaudīt pārveidojumu."]),

    Doma("Ievieto un aprēķini",
         "Polinoma vērtība ir skaitlis.",
         soli=[
             "Ieraksti skaitli iekavās mainīgā vietā.",
             "Vispirms kāpini, tad reizini, beigās saskaiti.",
             "Pārbaudei aprēķini vērtību pirms un pēc pārveidojuma.",
             "Ja vērtības atšķiras - pārveidojumā ir kļūda.",
         ]),

    Paraugs("Ievieto negatīvu skaitli",
            uzd="Aprēķini 2x^2 − 3x + 1, ja x = −2.",
            soli=[
                ("2 · (−2)^2 − 3 · (−2) + 1", "Ievieto iekavās."),
                ("2 · 4 + 6 + 1", "Kāpina un reizina."),
                ("15", "Saskaita."),
            ],
            atbilde="15"),

    Ievadi("Aprēķini vērtību", [
        {"jaut": "3x − 5, x = 4", "atb": ["7"], "padoms": "12 − 5."},
        {"jaut": "x^2 − 3x + 2, x = 5", "atb": ["12"],
         "padoms": "25 − 15 + 2."},
        {"jaut": "a^2 + 2a, a = −3", "atb": ["3"], "padoms": "9 − 6."},
        {"jaut": "2x^3 − x, x = −1", "atb": ["−1", "-1"],
         "padoms": "−2 + 1."},
        {"jaut": "(a + 2) − (a − 3), a = 10", "atb": ["5"],
         "padoms": "12 − 7; tas der jebkuram a."},
        {"jaut": "x^2 − 4x + 4, x = 2", "atb": ["0"], "padoms": "4 − 8 + 4."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Kā ievieto x = −3 izteiksmē x^2?",
         "opcijas": ["(−3)^2 = 9", "−3^2 = −9", "−6", "6"],
         "pareizi": 0, "padoms": "Iekavās!"},
        {"jaut": "Pārbaude ar vienu skaitli sakrīt. Tas nozīmē...",
         "opcijas": ["kļūda maz ticama, bet nav pierādīts",
                     "pārveidojums pierādīts", "noteikti kļūda",
                     "jāpārbauda ar 0"],
         "pareizi": 0, "padoms": "Viens skaitlis var nejauši sakrist."},
        {"jaut": "Skolēns: 3x − (x − 2) = 2x − 2. Pārbaude ar x = 0 dod...",
         "opcijas": ["2 un −2 - ir kļūda", "0 un 0", "2 un 2",
                     "−2 un −2"],
         "pareizi": 0, "padoms": "3 · 0 − (0 − 2) = 2."},
    ]),

    Pasaule("Bumbas lidojums",
            Ievadi("", [
                {"jaut": "Bumbas augstums h = 20t − 5t^2 (m). t = 1 s. h?",
                 "atb": ["15"], "padoms": "20 − 5."},
                {"jaut": "t = 2 s. h?", "atb": ["20"], "padoms": "40 − 20."},
                {"jaut": "t = 4 s. h?", "atb": ["0"],
                 "padoms": "80 − 80 - bumba zemē."},
            ]),
            pavediens="sports",
            konteksts="Uz augšu mestas bumbas augstumu apraksta polinoms ar "
                      "laiku t.",
            kapec="Ievietojot laiku, uzzina augstumu jebkurā brīdī."),

    Kopsavilkums([
        "Aprēķinu polinoma vērtību, arī negatīvam skaitlim.",
        "Veidoju vērtību tabulu.",
        "Pārbaudu pārveidojumu ar skaitli.",
    ]),

    Majas([
        "Aizpildi tabulu polinomam x^2 − 2x no x = −2 līdz 3.",
        "Pārbaudi savus 116. stundas pārveidojumus ar x = 2.",
        "Aprēķini bumbas augstumu, ja t = 3 s.",
    ]),
]
