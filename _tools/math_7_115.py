# -*- coding: utf-8 -*-
"""7. klase, 115. stunda: «Kā aprēķināt izteiksmes vērtību?»

Izteiksmes vērtību aprēķina, ievietojot mainīgā vietā skaitli un ievērojot
darbību secību. Negatīvus skaitļus ievieto iekavās - tā izvairās no
biežākās kļūdas ar zīmēm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā aprēķināt izteiksmes vērtību?"

MERKIS = ("Aprēķināsim algebriskas izteiksmes vērtību dotai mainīgā "
          "vērtībai.")

SATURS = [
    Sakums("Formula Excel tabulā",
           zimejums=restis([["x", "−2", "0", "3"],
                            ["2x² − 3x", "14", "0", "9"]]),
           paraksts="Tabula ievieto katru x un aprēķina.",
           fakti=["Datora izklājlapa aprēķina izteiksmi tūkstošiem reižu.",
                  "Tā ievēro darbību secību.",
                  "Negatīvu skaitli ievieto iekavās."]),

    Doma("Ievieto iekavās un rēķini pēc kārtas",
         "Lai aprēķinātu izteiksmes vērtību, mainīgā vietā ieraksta doto "
         "skaitli (negatīvu - iekavās) un izpilda darbības pareizā secībā: "
         "kāpināšana, tad reizināšana un dalīšana, tad saskaitīšana un "
         "atņemšana.",
         soli=[
             "Pārraksti izteiksmi, burta vietā ieliekot (skaitli).",
             "Vispirms kāpinājumi.",
             "Tad reizināšana un dalīšana.",
             "Beigās saskaitīšana un atņemšana.",
         ],
         pieze="(−3)² = 9, bet −3² = −9. Iekavas nosaka, vai kāpina arī "
               "mīnusu."),

    Paraugs("Ar negatīvu skaitli",
            uzd="Aprēķini 2x² − 3x, ja x = −2.",
            soli=[
                ("2 · (−2)² − 3 · (−2)", "Ievieto iekavās."),
                ("2 · 4 − 3 · (−2)", "(−2)² = 4."),
                ("8 + 6", "Reizināšana."),
                ("14", "Saskaitīšana."),
            ],
            atbilde="14"),

    Ievadi("Aprēķini", [
        {"jaut": "5a − 7, ja a = −3",
         "atb": ["−22", "-22"], "padoms": "−15 − 7."},
        {"jaut": "x² + 2x, ja x = −4",
         "atb": ["8"], "padoms": "16 − 8."},
        {"jaut": "3(m − 2), ja m = 0,5",
         "atb": ["−4,5", "-4,5"], "padoms": "3 · (−1,5)."},
        {"jaut": "{a + b|2}, ja a = 7, b = −3",
         "atb": ["2"], "padoms": "4 : 2."},
        {"jaut": "−x², ja x = 5",
         "atb": ["−25", "-25"], "padoms": "Kāpina tikai x."},
        {"jaut": "(−x)², ja x = 5",
         "atb": ["25"], "padoms": "(−5)²."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "Toms: x = −3, x² = −9. Kur kļūda?",
         "opcijas": ["(−3)² = 9 - aizmirsa iekavas",
                     "Kļūdas nav", "x² = 6", "x² = −6"],
         "pareizi": 0, "padoms": "Mīnuss reiz mīnuss."},
        {"jaut": "2 + 3a, ja a = 4. Līga: 5 · 4 = 20. Kur kļūda?",
         "opcijas": ["Reizināšana pirms saskaitīšanas: 2 + 12 = 14",
                     "Kļūdas nav", "Jābūt 24", "Jābūt 9"],
         "pareizi": 0, "padoms": "Darbību secība."},
    ]),

    Pasaule("Fizikas formula",
            Ievadi("", [
                {"jaut": "Bremzēšanas ceļš s = {v²|100} (m), v - km/h. Cik "
                         "m pie 50 km/h?",
                 "atb": ["25"], "padoms": "2500 : 100."},
                {"jaut": "Cik m pie 100 km/h?",
                 "atb": ["100"], "padoms": "10 000 : 100."},
                {"jaut": "Ātrums divkāršojās - cik reizes pieauga "
                         "bremzēšanas ceļš?",
                 "atb": ["4"], "padoms": "100 : 25."},
            ]),
            pavediens="celojums",
            konteksts="Autovadītāja apmācībā bremzēšanas ceļu aprēķina ar "
                      "aptuvenu formulu - un ātrums tajā ir kvadrātā.",
            kapec="Divreiz ātrāk - četrreiz garāks bremzēšanas ceļš."),

    Zimejums("Bremzēšanas ceļš",
             restis([["v, km/h", "30", "50", "70", "100"],
                     ["s, m", "9", "25", "49", "100"]]),
             paskaidro="Ātrums aug vienmērīgi, ceļš - daudz straujāk."),

    Kopsavilkums([
        "Ievietoju skaitli mainīgā vietā.",
        "Negatīvu skaitli lieku iekavās.",
        "Ievēroju darbību secību.",
        "Atšķiru (−x)² no −x².",
    ]),

    Majas([
        "Aprēķini 3x² − x + 1, ja x = −1; 0; 2.",
        "Izveido tabulu bremzēšanas ceļam 20-120 km/h.",
        "Atrodi formulu sadzīvē un aprēķini vienu vērtību.",
    ]),
]
