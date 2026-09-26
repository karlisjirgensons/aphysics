# -*- coding: utf-8 -*-
"""8. klase, 25. stunda: «Kā pāriet uz pozitīvu kāpinātāju?»

Negatīvs kāpinātājs «pārceļ» reizinātāju pāri daļas svītrai: x^−2 no
skaitītāja kļūst par x^2 saucējā un otrādi. Daļai ar negatīvu kāpinātāju
pietiek to apgriezt. Rezultātu pieraksta bez negatīviem kāpinātājiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā pāriet uz pozitīvu kāpinātāju?"

MERKIS = ("Pārveidosim pakāpi ar negatīvu kāpinātāju par pakāpi ar pozitīvu "
          "kāpinātāju.")

SATURS = [
    Sakums("Pāri svītrai - zīme mainās",
           zimejums=restis([["x⁻²", "=", "1/x²"],
                            ["1/x⁻³", "=", "x³"]]),
           paraksts="Reizinātājs pāriet uz otru daļas pusi, kāpinātājs "
                    "maina zīmi.",
           fakti=["No skaitītāja uz saucēju - kāpinātājs maina zīmi.",
                  "No saucēja uz skaitītāju - arī.",
                  "Pārējie reizinātāji paliek savās vietās."]),

    Doma("Trīs likumi",
         "Visi trīs izriet no a^−n = {1|a^n}.",
         soli=[
             "a^−n = {1|a^n}.",
             "{1|a^−n} = a^n.",
             "({a|b})^−n = ({b|a})^n - daļu apgriež.",
             "Pārceļ tikai to reizinātāju, kuram ir negatīvs kāpinātājs.",
         ],
         pieze="Eksāmenā atbildi pieraksta bez negatīviem kāpinātājiem, ja "
               "vien uzdevumā nav prasīts citādi."),

    Slidnis("Daļa ar negatīvu kāpinātāju", [
        {"v": "({2|3})^−2", "teksts": "Sākums"},
        {"v": "1 : ({2|3})^2", "teksts": "a^−n = {1|a^n}"},
        {"v": "1 : {4|9}", "teksts": "Kāpina daļu"},
        {"v": "{9|4}", "teksts": "Dalīt ar daļu - reizināt ar apgriezto"},
        {"v": "({3|2})^2 = {9|4}", "teksts": "Īsāk: apgriež un kāpina"},
    ]),

    Paraugs("Pieraksti bez negatīviem kāpinātājiem",
            uzd="Pārveido 3x^−4y^2 un {a^−2|b^−5}.",
            soli=[
                ("3x^−4y^2 = {3y^2|x^4}", "Tikai x pāriet uz saucēju."),
                ("{a^−2|b^−5} = {b^5|a^2}", "Abi pārceļas un maina zīmi."),
            ],
            atbilde="{3y^2|x^4}; {b^5|a^2}"),

    Ievadi("Pārveido", [
        {"jaut": "({1|2})^−3 - aprēķini", "atb": ["8"],
         "padoms": "2^3."},
        {"jaut": "({2|5})^−1 - decimāldaļā", "atb": ["2,5", "2.5"],
         "padoms": "{5|2}."},
        {"jaut": "{1|10^−3} - aprēķini", "atb": ["1000"],
         "padoms": "10^3."},
        {"jaut": "({3|4})^−2 - atbildi raksti kā a/b",
         "atb": ["{16|9}", "16/9"], "padoms": "({4|3})^2."},
        {"jaut": "(0,5)^−2 - aprēķini", "atb": ["4"],
         "padoms": "0,5 = {1|2}."},
        {"jaut": "{6|2^−2} - aprēķini", "atb": ["24"],
         "padoms": "6 · 2^2."},
    ], pamats=4),

    Varianti("Kurš pieraksts ir vienāds?", [
        {"jaut": "5a^−3 =",
         "opcijas": ["{5|a^3}", "{1|5a^3}", "−5a^3", "{a^3|5}"],
         "pareizi": 0, "padoms": "Pārceļ tikai a^−3."},
        {"jaut": "{x^2|y^−4} =",
         "opcijas": ["x^2y^4", "{x^2|y^4}", "{1|x^2y^4}", "x^−2y^4"],
         "pareizi": 0, "padoms": "y^−4 pāriet augšā."},
        {"jaut": "(2a)^−2 =",
         "opcijas": ["{1|4a^2}", "{2|a^2}", "−4a^2", "{4|a^2}"],
         "pareizi": 0, "padoms": "Visu iekavu uz saucēju."},
    ]),

    Pasaule("Ātrums un laiks",
            Ievadi("", [
                {"jaut": "Ātrumu raksta m · s^−1 - tas pats, kas m/s. Cik m/s "
                         "ir 36 km · h^−1? (1 km/h = {1|3,6} m/s)",
                 "atb": ["10"], "padoms": "36 : 3,6."},
                {"jaut": "Frekvence 50 s^−1 nozīmē 50 reizes sekundē. Cik "
                         "sekunžu ilgst viena svārstība? (decimāldaļā)",
                 "atb": ["0,02", "0.02"], "padoms": "{1|50}."},
                {"jaut": "Motors griežas 3000 min^−1. Cik apgriezienu "
                         "sekundē?",
                 "atb": ["50"], "padoms": "3000 : 60."},
            ]),
            pavediens="tehnika",
            konteksts="Fizikā un tehnikā «dalīts ar» raksta ar negatīvu "
                      "kāpinātāju: km · h^−1, s^−1, min^−1.",
            kapec="Rozetes strāva Latvijā mainās 50 reizes sekundē - 50 Hz."),

    Kopsavilkums([
        "Pārceļu reizinātāju ar negatīvu kāpinātāju pāri daļas svītrai.",
        "Apgriežu daļu ar negatīvu kāpinātāju.",
        "Pierakstu rezultātu tikai ar pozitīviem kāpinātājiem.",
    ]),

    Majas([
        "Pārveido: 7x^−2, {1|y^−6}, ({5|2})^−2, {a^−3b|c^−1}.",
        "Aprēķini (0,2)^−2 un (0,1)^−3.",
        "Atrodi uz sadzīves tehnikas uzlīmes mērvienību ar ^−1.",
    ]),
]
