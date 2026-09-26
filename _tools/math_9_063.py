# -*- coding: utf-8 -*-
"""9. klase, 63. stunda: «Kas notiek, kāpinot binomu?»

(a + b)^2 NAV a^2 + b^2 - tā ir biežākā algebras kļūda. Sareizinot binomu
ar sevi, parādās vidējais loceklis 2ab. Stunda sākas ar pārbaudi skaitļos:
(3 + 4)^2 = 49, bet 3^2 + 4^2 = 25.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kas notiek, kāpinot binomu?"

MERKIS = ("Iegūsim binoma kvadrāta formulu, sareizinot binomu ar sevi.")

_T = "text"

SATURS = [
    Sakums("(3 + 4)² = 3² + 4²?",
           zimejums=restis([["(3 + 4)²", "3² + 4²"], ["7² = 49", "9 + 16 = 25"]]),
           paraksts="49 ≠ 25 - kur pazuda 24?",
           fakti=["Trūkstošie 24 = 2 · 3 · 4.",
                  "(a + b)^2 = a^2 + 2ab + b^2.",
                  "2ab - «dubultotais reizinājums»."]),

    Slidnis("Sareizinām binomu ar sevi", [
        {"v": "1", "teksts": "(a + b)^2 = (a + b)(a + b)"},
        {"v": "2", "teksts": "= a · a + a · b + b · a + b · b"},
        {"v": "3", "teksts": "= a^2 + ab + ab + b^2"},
        {"v": "4", "teksts": "= a^2 + 2ab + b^2"},
    ], ievads="Katru locekli reizina ar katru."),

    Doma("Summas kvadrāts",
         "(a + b)^2 = a^2 + 2ab + b^2.",
         soli=[
             "Pirmā kvadrāts: a^2.",
             "Divkāršots reizinājums: 2ab.",
             "Otrā kvadrāts: b^2.",
             "Nekad neaizmirsti vidējo locekli!",
         ]),

    Paraugs("Ar koeficientiem",
            uzd="Atver iekavas: (3x + 2)^2.",
            soli=[
                ("(3x)^2 = 9x^2", "Pirmā kvadrāts - arī koeficients kvadrātā."),
                ("2 · 3x · 2 = 12x", "Divkāršots reizinājums."),
                ("2^2 = 4", "Otrā kvadrāts."),
            ],
            atbilde="9x^2 + 12x + 4"),

    Ievadi("Atver iekavas", [
        {"jaut": "(x + 3)^2", "atb": ["x^2 + 6x + 9"], "tastatura": _T,
         "padoms": "x^2 + 2 · 3x + 9."},
        {"jaut": "(a + 5)^2", "atb": ["a^2 + 10a + 25"], "tastatura": _T,
         "padoms": "2 · 5a = 10a."},
        {"jaut": "(2x + 1)^2", "atb": ["4x^2 + 4x + 1"], "tastatura": _T,
         "padoms": "(2x)^2 = 4x^2."},
        {"jaut": "(4 + b)^2 (eksāmens 2025)", "atb": ["16 + 8b + b^2",
                                                    "b^2 + 8b + 16"],
         "tastatura": _T, "padoms": "16 + 2 · 4b + b^2."},
        {"jaut": "(x + y)^2", "atb": ["x^2 + 2xy + y^2"], "tastatura": _T,
         "padoms": "Formula."},
        {"jaut": "(5a + 2b)^2", "atb": ["25a^2 + 20ab + 4b^2"],
         "tastatura": _T, "padoms": "2 · 5a · 2b = 20ab."},
    ], pamats=4),

    Varianti("Kļūdas slazds", [
        {"jaut": "(x + 4)^2 = ?",
         "opcijas": ["x^2 + 8x + 16", "x^2 + 16", "x^2 + 4x + 16",
                     "x^2 + 8x + 8"],
         "pareizi": 0, "padoms": "2 · 4x = 8x."},
        {"jaut": "Kurš vidējais loceklis ir izteiksmē (2a + 3)^2?",
         "opcijas": ["12a", "6a", "5a", "9a"],
         "pareizi": 0, "padoms": "2 · 2a · 3."},
    ]),

    Pasaule("Lielāks ekrāns",
            Ievadi("", [
                {"jaut": "Kvadrātveida ekrāna mala x cm; jaunajam modelim par "
                         "10 cm lielāka. Laukums (x + 10)^2 = x^2 + ?x + 100",
                 "atb": ["20"], "padoms": "2 · 10."},
                {"jaut": "x = 30. Cik cm² laukums pieauga?", "atb": ["700"],
                 "padoms": "20 · 30 + 100."},
            ]),
            pavediens="tehnika",
            konteksts="Ražotāji reklāmā saka «par 10 cm lielāks», bet laukums "
                      "aug daudz vairāk, nekā šķiet.",
            kapec="Vidējais loceklis 2ab ir tā «slēptā» daļa."),

    Kopsavilkums([
        "Iegūstu summas kvadrāta formulu.",
        "Atveru iekavas (a + b)^2 bez kļūdas.",
        "Pārbaudu ar skaitļiem.",
    ]),

    Majas([
        "Pārbaudi formulu ar a = 5, b = 2.",
        "Atver: (x + 7)^2; (3a + 1)^2; (2m + 5n)^2.",
        "Paskaidro draugam, kāpēc (a + b)^2 ≠ a^2 + b^2.",
    ]),
]
