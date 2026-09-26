# -*- coding: utf-8 -*-
"""8. klase, 35. stunda: «Kā rēķināt ar normālformu?»

Reizinot un dalot normālformas, skaitļus a apstrādā atsevišķi un 10 pakāpes
atsevišķi - tās pašas pakāpju īpašības. Beigās rezultāts bieži vairs nav
normālformā (20 · 10^5), tāpēc pēdējais solis ir «salabot» a.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kā rēķināt ar normālformu?"

MERKIS = ("Reizināsim un dalīsim normālformā pierakstītus skaitļus.")

SATURS = [
    Sakums("Cik ūdens pilienu ir baseinā?",
           zimejums=restis([["baseins", "2,5 · 10⁶ l"],
                            ["pilienu litrā", "2 · 10⁴"],
                            ["kopā", "5 · 10¹⁰"]]),
           paraksts="2,5 · 2 = 5; 10⁶ · 10⁴ = 10¹⁰.",
           fakti=["Skaitļus reizina atsevišķi.",
                  "10 pakāpes - pēc pakāpju īpašībām.",
                  "Rezultātu pārbauda: vai tas ir normālformā?"]),

    Doma("Reizināšana un dalīšana",
         "(a · 10^m) · (b · 10^n) = (a · b) · 10^{m + n}; "
         "(a · 10^m) : (b · 10^n) = (a : b) · 10^{m − n}.",
         soli=[
             "Sareizini vai izdali skaitļus a un b.",
             "Saskaiti vai atņem kāpinātājus.",
             "Ja a · b ≥ 10 - komats pa kreisi, kāpinātājs + 1.",
             "Ja a : b < 1 - komats pa labi, kāpinātājs − 1.",
         ]),

    Slidnis("Salabo rezultātu", [
        {"v": "(5 · 10^3) · (4 · 10^2)", "teksts": "Sākums"},
        {"v": "20 · 10^5", "teksts": "5 · 4 un 3 + 2"},
        {"v": "2 · 10^1 · 10^5", "teksts": "20 nav normālformā: 20 = 2 · 10"},
        {"v": "2 · 10^6", "teksts": "Gatavs"},
    ]),

    Ievadi("Aprēķini un pieraksti normālformā", [
        {"jaut": "(3 · 10^4) · (2 · 10^5) = 6 · 10^?", "atb": ["9"],
         "padoms": "4 + 5."},
        {"jaut": "(8 · 10^6) : (4 · 10^2) = 2 · 10^?", "atb": ["4"],
         "padoms": "6 − 2."},
        {"jaut": "(6 · 10^3) · (5 · 10^−1) = 3 · 10^?", "atb": ["3"],
         "padoms": "30 · 10^2 = 3 · 10^3."},
        {"jaut": "(1,2 · 10^5) : (4 · 10^−3) = 3 · 10^?", "atb": ["7"],
         "padoms": "0,3 · 10^8."},
        {"jaut": "(2 · 10^3)^3 = 8 · 10^?", "atb": ["9"],
         "padoms": "2^3 · 10^9."},
        {"jaut": "(9 · 10^8) : (3 · 10^8) - aprēķini", "atb": ["3"],
         "padoms": "10^0 = 1."},
    ], pamats=4),

    Varianti("Kurš rezultāts ir normālformā?", [
        {"jaut": "(4 · 10^2) · (3 · 10^5) =",
         "opcijas": ["1,2 · 10^8", "12 · 10^7", "1,2 · 10^7", "12 · 10^{10}"],
         "pareizi": 0, "padoms": "12 · 10^7 = 1,2 · 10^8."},
        {"jaut": "(2 · 10^6) : (5 · 10^2) =",
         "opcijas": ["4 · 10^3", "0,4 · 10^4", "4 · 10^4", "2,5 · 10^3"],
         "pareizi": 0, "padoms": "0,4 · 10^4 = 4 · 10^3."},
    ]),

    Pasaule("Cik ilgi gaisma iet?",
            Ievadi("", [
                {"jaut": "Gaismas ātrums 3 · 10^5 km/s. Līdz Mēnesim "
                         "3,84 · 10^5 km. Cik sekunžu? (decimāldaļā)",
                 "atb": ["1,28", "1.28"], "padoms": "3,84 : 3."},
                {"jaut": "Līdz Marsam (tuvākajā punktā) ap 5,4 · 10^7 km. "
                         "Cik sekunžu? (a · 10^2 - ieraksti skaitli)",
                 "atb": ["180"], "padoms": "1,8 · 10^2."},
                {"jaut": "Cik minūšu tas ir?",
                 "atb": ["3"], "padoms": "180 : 60."},
            ]),
            pavediens="kosmoss",
            konteksts="Marsa roveri nevar vadīt ar pulti - signāls iet "
                      "vairākas minūtes, tāpēc tie brauc paši.",
            kapec="Dalot normālformas, laiku iegūst vienā rindā."),

    Kopsavilkums([
        "Reizinu un dalu skaitļus normālformā.",
        "Lietoju pakāpju īpašības ar 10 pakāpēm.",
        "Salaboju rezultātu, lai 1 ≤ a < 10.",
    ]),

    Majas([
        "Aprēķini: (7 · 10^4)(3 · 10^−6), (9 · 10^5) : (1,5 · 10^2).",
        "Cik sekunžu gaisma iet no Saules (1,5 · 10^8 km)?",
        "Aprēķini, cik sekunžu ir 100 gados, normālformā.",
    ]),
]
