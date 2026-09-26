# -*- coding: utf-8 -*-
"""8. klase, 119. stunda: «Kā reizina divus polinomus?»

Katru pirmā polinoma locekli reizina ar katru otrā: (a + b)(c + d) =
ac + ad + bc + bd. Reizinājumu skaits = locekļu skaitu reizinājums;
beigās savelk līdzīgos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā reizina divus polinomus?"

MERKIS = "Reizināsim divus polinomus un paskaidrosim darbības kārtību."

_T = "text"

SATURS = [
    Sakums("(x + 3)(x − 5) = ?",
           zimejums=restis([["·", "x", "−5"],
                            ["x", "x²", "−5x"],
                            ["+3", "3x", "−15"]]),
           paraksts="Tabulā katrs ar katru: x^2 − 5x + 3x − 15 = x^2 − 2x − 15.",
           fakti=["Katru locekli reizina ar katru.",
                  "2 locekļi × 2 locekļi = 4 reizinājumi.",
                  "Beigās savelk līdzīgos locekļus."]),

    Doma("Katrs ar katru",
         "(a + b)(c + d) = ac + ad + bc + bd.",
         soli=[
             "Pirmā polinoma pirmo locekli reizini ar visiem otrā.",
             "Tad otro locekli - ar visiem otrā.",
             "Pārbaudi, vai reizinājumu skaits ir pareizs (2 · 3 = 6).",
             "Savelc līdzīgos un sakārto.",
         ]),

    Paraugs("Binoms un trinoms",
            uzd="Aprēķini (2a − 1)(a^2 + a − 3).",
            soli=[
                ("2a^3 + 2a^2 − 6a", "2a · katru."),
                ("− a^2 − a + 3", "−1 · katru."),
                ("2a^3 + a^2 − 7a + 3", "Savelk."),
            ],
            atbilde="2a^3 + a^2 − 7a + 3"),

    Ievadi("Sareizini (normālformā)", [
        {"jaut": "(x + 2)(x + 3)", "atb": ["x^2 + 5x + 6"], "tastatura": _T,
         "padoms": "x^2 + 3x + 2x + 6."},
        {"jaut": "(a − 1)(a + 4)", "atb": ["a^2 + 3a − 4"], "tastatura": _T,
         "padoms": "a^2 + 4a − a − 4."},
        {"jaut": "(2x + 1)(x − 3)", "atb": ["2x^2 − 5x − 3"],
         "tastatura": _T, "padoms": "2x^2 − 6x + x − 3."},
        {"jaut": "(x − 2)(x + 2)", "atb": ["x^2 − 4"], "tastatura": _T,
         "padoms": "Vidējie saīsinās."},
        {"jaut": "(x + 1)(x^2 − x + 1)", "atb": ["x^3 + 1"],
         "tastatura": _T, "padoms": "Seši reizinājumi, četri saīsinās."},
        {"jaut": "(a + b)(a + b)", "atb": ["a^2 + 2ab + b^2"],
         "tastatura": _T, "padoms": "ab + ba = 2ab."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "Cik reizinājumu, reizinot binomu ar trinomu?",
         "opcijas": ["6", "5", "3", "2"],
         "pareizi": 0, "padoms": "2 · 3."},
        {"jaut": "(x + 1)(x + 1) = ?",
         "opcijas": ["x^2 + 2x + 1", "x^2 + 1", "x^2 + x + 1", "2x + 2"],
         "pareizi": 0, "padoms": "x + x = 2x."},
        {"jaut": "(x − 3)(x + 3) = ?",
         "opcijas": ["x^2 − 9", "x^2 + 9", "x^2 − 6x − 9", "x^2 − 3"],
         "pareizi": 0, "padoms": "−3x + 3x = 0."},
    ]),

    Pasaule("Foto rāmī",
            Ievadi("", [
                {"jaut": "Foto x × (x + 2) cm; rāmis katrā pusē pieliek 3 cm: "
                         "(x + 6)(x + 8). Koeficients pie x?",
                 "atb": ["14"], "padoms": "8x + 6x."},
                {"jaut": "Brīvais loceklis?", "atb": ["48"],
                 "padoms": "6 · 8."},
                {"jaut": "x = 10. Ārējais laukums (cm²)?", "atb": ["288"],
                 "padoms": "16 · 18 = 100 + 140 + 48."},
            ]),
            pavediens="maja",
            konteksts="Rāmis palielina abus izmērus, tāpēc reizina divus "
                      "binomus.",
            kapec="Katrs ar katru - neviens loceklis nepaliek aizmirsts."),

    Kopsavilkums([
        "Reizinu divus polinomus - katru locekli ar katru.",
        "Pārbaudu reizinājumu skaitu.",
        "Savelku līdzīgos locekļus.",
    ]),

    Majas([
        "Sareizini: (x + 4)(x − 1); (2a + 3)(a + 2).",
        "Pārbaudi ar x = 2 un a = 1.",
        "Aprēķini (x + 1)(x + 2)(x + 3) pa soļiem.",
    ]),
]
