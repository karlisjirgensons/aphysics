# -*- coding: utf-8 -*-
"""7. klase, 141. stunda: «Kā aprēķināt nezināmo locekli?»

No pamatīpašības ad = bc izriet: nezināmais ārējais loceklis = vidējo
reizinājums : zināmais ārējais; nezināmais vidējais = ārējo reizinājums :
zināmais vidējais. Tas ir vienādojums, ko risina vienā solī.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā aprēķināt nezināmo locekli?"

MERKIS = ("Aprēķināsim proporcijas nezināmo locekli un pārbaudīsim "
          "rezultātu.")

SATURS = [
    Sakums("{x|6} = {10|15}: viens krustiskais reizinājums",
           fakti=["15x = 60.",
                  "x = 4.",
                  "Pārbaude: 4 · 15 = 6 · 10 = 60."]),

    Doma("Krustiskais reizinājums → vienādojums",
         "Lai atrastu nezināmo proporcijas locekli, izmanto ad = bc: iegūst "
         "vienādojumu un to atrisina.",
         soli=[
             "Pieraksti ārējo reizinājumu = vidējo reizinājumu.",
             "Atrisini iegūto vienādojumu.",
             "Pārbaudi, ievietojot atpakaļ.",
         ],
         pieze="Ja proporcijā ir izteiksme (x + 2), to liek iekavās: "
               "{x + 2|3} = {4|6} ⇒ 6(x + 2) = 12."),

    Paraugs("Ar izteiksmi",
            uzd="Atrisini {x + 2|5} = {6|10}.",
            soli=[
                ("10(x + 2) = 5 · 6", "(ad = bc)"),
                ("10x + 20 = 30", "Atver iekavas."),
                ("10x = 10, x = 1", "Atrisina."),
                ("Pārbaude: {3|5} = {6|10}", "Pareizi."),
            ],
            atbilde="x = 1"),

    Ievadi("Atrodi x", [
        {"jaut": "x : 4 = 9 : 12",
         "atb": ["3"], "padoms": "12x = 36."},
        {"jaut": "{5|x} = {15|21}",
         "atb": ["7"], "padoms": "15x = 105."},
        {"jaut": "2,5 : x = 5 : 8",
         "atb": ["4"], "padoms": "5x = 20."},
        {"jaut": "{x − 1|3} = {8|6}",
         "atb": ["5"], "padoms": "6(x − 1) = 24."},
        {"jaut": "{3|x} = {x|12} (x > 0)",
         "atb": ["6"], "padoms": "x² = 36."},
        {"jaut": "{2x|5} = {4|10}",
         "atb": ["1"], "padoms": "20x = 20."},
    ], pamats=4),

    Varianti("Kurš vienādojums?", [
        {"jaut": "{x|7} = {3|21}",
         "opcijas": ["21x = 21", "7x = 63", "3x = 147", "x = 21 · 3"],
         "pareizi": 0, "padoms": "x · 21 = 7 · 3."},
        {"jaut": "8 : x = 2 : 5",
         "opcijas": ["2x = 40", "8x = 10", "5x = 16", "x = 8 · 2"],
         "pareizi": 0, "padoms": "Ārējie 8 · 5, vidējie x · 2."},
    ]),

    Pasaule("Valūtas maiņa",
            Ievadi("", [
                {"jaut": "1 € = 1,08 $. Cik $ par 250 €? (1 : 1,08 = 250 : x)",
                 "atb": ["270"], "padoms": "x = 1,08 · 250."},
                {"jaut": "Cik € par 54 $?",
                 "atb": ["50"], "padoms": "54 : 1,08."},
                {"jaut": "1 € = 11,5 zviedru kronas. Cik € ir 230 kronas?",
                 "atb": ["20"], "padoms": "230 : 11,5."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojot ārzemēs, cenu pārrēķina ar proporciju pēc "
                      "valūtas kursa.",
            kapec="Kurss ir attiecība - proporcija dod cenu."),

    Kopsavilkums([
        "Pierakstu ad = bc kā vienādojumu.",
        "Aprēķinu nezināmo ārējo vai vidējo locekli.",
        "Lieku iekavas ap izteiksmēm.",
        "Pārbaudu, ievietojot atpakaļ.",
    ]),

    Majas([
        "Atrisini: 7 : x = 21 : 9; {x + 3|4} = {5|2}.",
        "Pārrēķini ceļojuma budžetu citā valūtā.",
        "Izdomā proporcijas uzdevumu draugam.",
    ]),
]
