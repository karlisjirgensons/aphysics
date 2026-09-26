# -*- coding: utf-8 -*-
"""9. klase, 126. stunda: «Kā pieraksta rekurenti?»

Rekurents pieraksts: pirmais loceklis un likums, kā no iepriekšējā iegūt
nākamo (a_{n+1} = a_n + 3). Tā strādā izklājlapa un datorprogramma - katra
šūna izmanto iepriekšējo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā pieraksta rekurenti?"

MERKIS = ("Aprēķināsim locekļus, ja dots pirmais loceklis un veids, kā "
          "iegūt nākamo.")

SATURS = [
    Sakums("Izklājlapā: A2 = A1 + 3",
           zimejums=restis([["šūna", "A1", "A2", "A3", "A4", "A5"],
                            ["vērtība", "4", "7", "10", "13", "16"]]),
           paraksts="Katra šūna - iepriekšējā plus 3.",
           fakti=["a_1 = 4, a_{n+1} = a_n + 3.",
                  "Lai atrastu a_5, jāzina a_4.",
                  "Tā rēķina izklājlapas un programmas."]),

    Doma("Rekurents pieraksts",
         "Virkni uzdod ar pirmo locekli un formulu, kas izsaka a_{n+1} ar "
         "a_n (dažreiz arī ar a_{n−1}).",
         soli=[
             "Sāc ar doto a_1.",
             "Ievieto formulā, iegūsti a_2.",
             "Atkārto, līdz vajadzīgajam loceklim.",
             "Vispārīgā formula ļauj «pārlēkt»; rekurentā - soli pa solim.",
         ]),

    Slidnis("Rekurenti likumi", [
        {"v": "+3", "teksts": "a_1 = 2, a_{n+1} = a_n + 3: 2, 5, 8, 11, ..."},
        {"v": "· 2", "teksts": "a_1 = 3, a_{n+1} = 2a_n: 3, 6, 12, 24, ..."},
        {"v": "Fibonači", "teksts": "a_1 = a_2 = 1, a_{n+2} = a_{n+1} + a_n: "
                                    "1, 1, 2, 3, 5, 8, ..."},
    ]),

    Paraugs("Aprēķini pa soļiem",
            uzd="a_1 = 5, a_{n+1} = 2a_n − 3. Atrodi a_4.",
            soli=[
                ("a_2 = 2 · 5 − 3 = 7", "n = 1."),
                ("a_3 = 2 · 7 − 3 = 11", "n = 2."),
                ("a_4 = 2 · 11 − 3 = 19", "n = 3."),
            ],
            atbilde="a_4 = 19"),

    Ievadi("Aprēķini", [
        {"jaut": "a_1 = 10, a_{n+1} = a_n − 4. a_4 = ?", "atb": ["−2", "-2"],
         "padoms": "10, 6, 2, −2."},
        {"jaut": "a_1 = 1, a_{n+1} = 3a_n. a_5 = ?", "atb": ["81"],
         "padoms": "1, 3, 9, 27, 81."},
        {"jaut": "a_1 = 2, a_{n+1} = a_n^2 − 1. a_3 = ?", "atb": ["8"],
         "padoms": "2, 3, 8."},
        {"jaut": "a_1 = 64, a_{n+1} = {a_n|2}. a_6 = ?", "atb": ["2"],
         "padoms": "64, 32, 16, 8, 4, 2."},
    ]),

    Varianti("Kurš rekurentais likums?", [
        {"jaut": "7, 12, 17, 22, ...",
         "opcijas": ["a_1 = 7, a_{n+1} = a_n + 5",
                     "a_1 = 7, a_{n+1} = 5a_n",
                     "a_1 = 5, a_{n+1} = a_n + 7",
                     "a_{n+1} = a_n − 5"],
         "pareizi": 0, "padoms": "+5."},
        {"jaut": "Kāpēc a_{100} ar rekurento formulu atrast ir grūti?",
         "opcijas": ["Jāaprēķina visi 99 iepriekšējie",
                     "Formula nav pareiza", "a_{100} neeksistē",
                     "Tas nav grūti"],
         "pareizi": 0, "padoms": "Soli pa solim."},
    ]),

    Pasaule("Baktēriju kolonija",
            Ievadi("", [
                {"jaut": "Sākumā 500 baktērijas; ik stundu to skaits "
                         "dubultojas: a_{n+1} = 2a_n. Cik pēc 3 stundām?",
                 "atb": ["4000", "4 000"], "padoms": "500, 1000, 2000, 4000."},
                {"jaut": "Pēc cik stundām pārsniegs 30 000?", "atb": ["6"],
                 "padoms": "8000, 16 000, 32 000."},
            ]),
            pavediens="daba",
            konteksts="Laboratorijā baktērijas vairojas: katra stundas beigās "
                      "dalās divās.",
            kapec="Rekurents likums apraksta augšanu soli pa solim."),

    Kopsavilkums([
        "Aprēķinu locekļus pēc rekurentā likuma.",
        "Atšķiru rekurento un vispārīgo pierakstu.",
        "Pierakstu rekurento likumu dotai virknei.",
    ]),

    Majas([
        "Izklājlapā izveido virkni a_1 = 3, a_{n+1} = a_n + 4 līdz a_{20}.",
        "Atrodi a_5: a_1 = 1, a_{n+1} = 2a_n + 1.",
        "Uzraksti rekurento likumu virknei 100, 90, 80, ...",
    ]),
]
