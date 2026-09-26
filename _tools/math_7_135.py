# -*- coding: utf-8 -*-
"""7. klase, 135. stunda: «Kā pārveidot vienādojumu ekvivalenti?»

Svaru likums: ja abiem kausiem pieliek vai noņem vienu un to pašu, vai
abus sareizina ar vienu skaitli (ne 0), līdzsvars saglabājas. Tās ir
ekvivalentās pārveidošanas - un ar tām atrisina jebkuru lineāru vienādojumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kā pārveidot vienādojumu ekvivalenti?"

MERKIS = ("Lietosim vienādojuma abām pusēm vienādas darbības un pamatosim "
          "pārveidojumu.")

SATURS = [
    Sakums("Ko dari vienam kausam - dari arī otram",
           fakti=["Abām pusēm var pieskaitīt vai atņemt to pašu skaitli.",
                  "Abas puses var reizināt vai dalīt ar to pašu skaitli ≠ 0.",
                  "Līdzsvars (saknes) saglabājas."]),

    Doma("Divas ekvivalentās pārveidošanas",
         "1) Vienādojuma abām pusēm var pieskaitīt (vai atņemt) vienu un to "
         "pašu skaitli vai izteiksmi. 2) Abas puses var reizināt (vai dalīt) "
         "ar vienu un to pašu skaitli, kas nav nulle. Iegūst ekvivalentu "
         "vienādojumu.",
         soli=[
             "Mērķis: x vienā pusē, skaitlis - otrā.",
             "Atbrīvojies no saskaitāmajiem ar pretējo darbību abās pusēs.",
             "Atbrīvojies no koeficienta, dalot abas puses.",
             "Pieraksti katru soli un darbību.",
         ],
         pieze="Reizināt ar 0 nedrīkst: 0 = 0 ir patiess vienmēr - sakne "
               "pazustu."),

    Slidnis("Svari soli pa solim: 3x + 4 = 19", [
        {"v": "3x + 4 = 19", "teksts": "Sākums.", "josla": 100},
        {"v": "3x = 15", "teksts": "Abām pusēm − 4.", "josla": 80},
        {"v": "x = 5", "teksts": "Abas puses : 3.", "josla": 30},
    ]),

    Paraugs("Pieraksts ar darbībām",
            uzd="Atrisini 5x − 7 = 18.",
            soli=[
                ("5x − 7 + 7 = 18 + 7", "(abām pusēm + 7)"),
                ("5x = 25", "Vienkāršo."),
                ("x = 5", "(abas puses : 5)"),
                ("Pārbaude: 25 − 7 = 18", "Pareizi."),
            ],
            atbilde="x = 5"),

    Ievadi("Atrisini", [
        {"jaut": "x + 9 = 4",
         "atb": ["−5", "-5"], "padoms": "Abām pusēm − 9."},
        {"jaut": "6x = −42",
         "atb": ["−7", "-7"], "padoms": "Abas : 6."},
        {"jaut": "{x|5} = −3",
         "atb": ["−15", "-15"], "padoms": "Abas · 5."},
        {"jaut": "4x + 3 = 23",
         "atb": ["5"], "padoms": "4x = 20."},
        {"jaut": "−2x + 5 = 17",
         "atb": ["−6", "-6"], "padoms": "−2x = 12."},
        {"jaut": "0,5x − 1 = 3",
         "atb": ["8"], "padoms": "0,5x = 4."},
    ], pamats=4),

    Varianti("Pareizais solis", [
        {"jaut": "7x = 21. Kā iegūt x?",
         "opcijas": ["Abas puses dalīt ar 7", "Atņemt 7",
                     "Reizināt ar 7", "Pieskaitīt 7"],
         "pareizi": 0, "padoms": "Koeficients."},
        {"jaut": "Kura darbība nav ekvivalenta?",
         "opcijas": ["Abas puses reizināt ar 0",
                     "Abām pusēm pieskaitīt 5", "Abas puses dalīt ar −2",
                     "Abām pusēm atņemt x"],
         "pareizi": 0, "padoms": "0 = 0."},
    ]),

    Pasaule("Mobilā datu paka",
            Ievadi("", [
                {"jaut": "Paka: 5 € + 1,5 € par GB. Rēķins 17 €. Cik GB? "
                         "(5 + 1,5x = 17)",
                 "atb": ["8"], "padoms": "1,5x = 12."},
                {"jaut": "Rēķins 11 €. Cik GB?",
                 "atb": ["4"], "padoms": "1,5x = 6."},
                {"jaut": "Rēķins 5 €. Cik GB?",
                 "atb": ["0"], "padoms": "1,5x = 0."},
            ]),
            pavediens="dati",
            konteksts="Operatora rēķinā ir tikai summa - vienādojums pasaka "
                      "patērētos GB.",
            kapec="Ekvivalentas darbības noved līdz x."),

    Kopsavilkums([
        "Pieskaitu vai atņemu vienu un to pašu abām pusēm.",
        "Reizinu vai dalu abas puses ar skaitli ≠ 0.",
        "Pierakstu darbību pie katra soļa.",
        "Pārbaudu sakni.",
    ]),

    Majas([
        "Atrisini: 8x − 5 = 27; −3x + 2 = 20.",
        "Pieraksti katram solim darbību iekavās.",
        "Paskaidro, kāpēc nedrīkst reizināt ar 0.",
    ]),
]
