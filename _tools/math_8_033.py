# -*- coding: utf-8 -*-
"""8. klase, 33. stunda: «Kas ir skaitļa normālforma?»

Normālforma a · 10^n (1 ≤ a < 10) ir tas, kā zinātne pieraksta ļoti lielus
un ļoti mazus skaitļus. Slīdnis bīda komatu un skaita soļus - kāpinātājs
ir tikai soļu skaits ar zīmi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kas ir skaitļa normālforma?"

MERKIS = ("Pierakstīsim skaitli normālformā un mācīsimies to lasīt.")

SATURS = [
    Sakums("Līdz Mēnesim - 384 000 km",
           zimejums=restis([["384 000", "=", "3,84 · 10⁵"],
                            ["0,00052", "=", "5,2 · 10⁻⁴"]]),
           paraksts="Pirmais reizinātājs ir no 1 līdz 10, otrais - 10 pakāpe.",
           fakti=["Nulles vairs nav jāskaita.",
                  "Kāpinātājs uzreiz pasaka skaitļa lielumu.",
                  "Tā raksta kalkulatori un zinātnes grāmatas."]),

    Doma("Normālforma",
         "Pozitīva skaitļa normālforma ir a · 10^n, kur 1 ≤ a < 10 un n ir "
         "vesels skaitlis. Skaitli n sauc par skaitļa kārtu.",
         soli=[
             "Pārvieto komatu tā, lai pirms tā paliktu viens cipars (ne 0).",
             "Saskaiti, par cik vietām komats pārvietojās.",
             "Skaitlis bija lielāks par 10 - kāpinātājs pozitīvs.",
             "Skaitlis bija mazāks par 1 - kāpinātājs negatīvs.",
             "Pārbaude: 1 ≤ a < 10.",
         ],
         pieze="12 · 10^3 nav normālforma (12 > 10), arī 0,5 · 10^2 nav "
               "(0,5 < 1)."),

    Slidnis("Bīdi komatu", [
        {"v": "384 000", "teksts": "Komats beigās: 384 000,"},
        {"v": "3,84 · 10^5", "teksts": "5 vietas pa kreisi - kāpinātājs 5"},
        {"v": "0,00052", "teksts": "Mazs skaitlis"},
        {"v": "5,2 · 10^−4", "teksts": "4 vietas pa labi - kāpinātājs −4"},
    ]),

    Paraugs("Pieraksti normālformā",
            uzd="Pieraksti normālformā 7 200 000, 0,0301 un 45 · 10^3.",
            soli=[
                ("7 200 000 = 7,2 · 10^6", "6 vietas."),
                ("0,0301 = 3,01 · 10^−2", "2 vietas pa labi."),
                ("45 · 10^3 = 4,5 · 10 · 10^3 = 4,5 · 10^4",
                 "45 vēl nav normālformā."),
            ],
            atbilde="7,2 · 10^6; 3,01 · 10^−2; 4,5 · 10^4"),

    Ievadi("Atrodi kāpinātāju", [
        {"jaut": "52 000 = 5,2 · 10^?", "atb": ["4"], "padoms": "4 vietas."},
        {"jaut": "0,007 = 7 · 10^?", "atb": ["−3", "-3"],
         "padoms": "3 vietas pa labi."},
        {"jaut": "1 500 000 000 = 1,5 · 10^?", "atb": ["9"],
         "padoms": "Miljards = 10^9."},
        {"jaut": "0,000 064 = 6,4 · 10^?", "atb": ["−5", "-5"],
         "padoms": "5 vietas."},
        {"jaut": "830 · 10^2 = 8,3 · 10^?", "atb": ["4"],
         "padoms": "830 = 8,3 · 10^2."},
        {"jaut": "0,25 · 10^−3 = 2,5 · 10^?", "atb": ["−4", "-4"],
         "padoms": "0,25 = 2,5 · 10^−1."},
    ], pamats=4),

    Varianti("Vai tā ir normālforma?", [
        {"jaut": "Kurš pieraksts ir normālforma?",
         "opcijas": ["6,02 · 10^{23}", "60,2 · 10^{22}", "0,602 · 10^{24}",
                     "602 · 10^{21}"],
         "pareizi": 0, "padoms": "1 ≤ a < 10."},
        {"jaut": "Kura skaitļa kārta ir lielāka: 9,9 · 10^3 vai "
                 "1,1 · 10^4?",
         "opcijas": ["1,1 · 10^4", "9,9 · 10^3", "Vienāda",
                     "Nevar noteikt"],
         "pareizi": 0, "padoms": "Salīdzina kāpinātājus."},
    ]),

    Pasaule("Kosmosa attālumi",
            Ievadi("", [
                {"jaut": "Līdz Saulei 150 000 000 km = 1,5 · 10^? km",
                 "atb": ["8"], "padoms": "8 vietas."},
                {"jaut": "Gaismas gads ≈ 9 460 000 000 000 km = 9,46 · 10^? km",
                 "atb": ["12"], "padoms": "12 vietas."},
                {"jaut": "Ūdeņraža atoma diametrs ≈ 0,000 000 000 1 m = "
                         "1 · 10^? m",
                 "atb": ["−10", "-10"], "padoms": "10 vietas pa labi."},
            ]),
            pavediens="kosmoss",
            konteksts="No atoma līdz galaktikai - viens pieraksts. "
                      "Kāpinātājs rāda, cik reižu desmit lielāks vai mazāks.",
            kapec="Starp atomu un gaismas gadu ir 26 kārtas (metros)."),

    Kopsavilkums([
        "Pierakstu skaitli normālformā a · 10^n.",
        "Nosaku, vai pieraksts ir normālformā.",
        "Nosaku kāpinātāju pēc komata pārvietošanas.",
    ]),

    Majas([
        "Pieraksti normālformā: Latvijas iedzīvotāju skaitu, Zemes masu, "
        "sarkanā asinsķermenīša izmēru (atrodi internetā).",
        "Pārveido 250 · 10^4 un 0,03 · 10^−2 normālformā.",
        "Sakārto trīs skaitļus pēc lieluma, skatoties tikai uz kāpinātāju.",
    ]),
]
