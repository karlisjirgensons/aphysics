# -*- coding: utf-8 -*-
"""9. klase, 65. stunda: «Kāda ir starpības kvadrāta formula?»

(a − b)^2 = a^2 − 2ab + b^2: tikai vidējā locekļa zīme mainās. Iegūst to
divos veidos - sareizinot vai ievietojot −b summas formulā. Mīnuss b^2
priekšā NEPARĀDĀS - (−b)^2 = b^2.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kāda ir starpības kvadrāta formula?"

MERKIS = "Formulēsim un lietosim starpības kvadrāta formulu."

_T = "text"

SATURS = [
    Sakums("(10 − 1)² = 100 − 1?",
           zimejums=restis([["(10 − 1)²", "100 − 20 + 1"], ["9² = 81", "81"]]),
           paraksts="Vidējais loceklis −20; pēdējais +1.",
           fakti=["(a − b)^2 = a^2 − 2ab + b^2.",
                  "Mīnuss ir tikai pie 2ab.",
                  "b^2 vienmēr ar plusu: (−b)^2 = b^2."]),

    Doma("Starpības kvadrāts",
         "(a − b)^2 = a^2 − 2ab + b^2.",
         soli=[
             "Pirmā kvadrāts.",
             "MĪNUS divkāršots reizinājums.",
             "PLUS otrā kvadrāts.",
             "Ievērībai: (b − a)^2 = (a − b)^2.",
         ],
         pieze="Summas un starpības formulas kopā: (a ± b)^2 = a^2 ± 2ab + "
               "b^2 - tā tās raksta eksāmena formulu lapā."),

    Paraugs("Eksāmena stilā",
            uzd="Atver iekavas: (2c − 3)^2.",
            soli=[
                ("(2c)^2 = 4c^2", "Pirmā kvadrāts."),
                ("2 · 2c · 3 = 12c", "Divkāršots reizinājums - ar mīnusu."),
                ("3^2 = 9", "Otrā kvadrāts - ar plusu."),
            ],
            atbilde="4c^2 − 12c + 9"),

    Ievadi("Atver iekavas", [
        {"jaut": "(x − 5)^2", "atb": ["x^2 − 10x + 25"], "tastatura": _T,
         "padoms": "2 · 5x = 10x."},
        {"jaut": "(a − 1)^2", "atb": ["a^2 − 2a + 1"], "tastatura": _T,
         "padoms": "Formula."},
        {"jaut": "(3y − 2)^2", "atb": ["9y^2 − 12y + 4"], "tastatura": _T,
         "padoms": "2 · 3y · 2."},
        {"jaut": "(4 − x)^2", "atb": ["16 − 8x + x^2", "x^2 − 8x + 16"],
         "tastatura": _T, "padoms": "Tas pats kā (x − 4)^2."},
        {"jaut": "(2a − 5b)^2", "atb": ["4a^2 − 20ab + 25b^2"],
         "tastatura": _T, "padoms": "2 · 2a · 5b."},
        {"jaut": "(x − {1|2})^2 = x^2 − x + ? (decimāldaļa)",
         "atb": ["0,25"], "padoms": "({1|2})^2."},
    ], pamats=4),

    Varianti("Atrodi kļūdu", [
        {"jaut": "(x − 3)^2 = x^2 − 9",
         "opcijas": ["Trūkst −6x un zīme pie 9: x^2 − 6x + 9", "Pareizi",
                     "Jābūt x^2 + 9", "Jābūt x^2 − 3x + 9"],
         "pareizi": 0, "padoms": "Formula ar trim locekļiem."},
        {"jaut": "(a − 2)^2 = a^2 − 4a − 4",
         "opcijas": ["Pēdējais +4", "Pareizi", "Vidējais −2a",
                     "Jābūt a^2 + 4"],
         "pareizi": 0, "padoms": "(−2)^2 = +4."},
        {"jaut": "(5 − x)^2 un (x − 5)^2 ...",
         "opcijas": ["ir vienādi", "atšķiras ar zīmi",
                     "atšķiras ar 10x", "nav salīdzināmi"],
         "pareizi": 0, "padoms": "(−t)^2 = t^2."},
    ]),

    Pasaule("Rāmja iekšpuse",
            Ievadi("", [
                {"jaut": "Kvadrātveida rāmis ar ārējo malu 30 cm, platums 2 cm "
                         "no katras puses. Iekšējā mala (cm)?", "atb": ["26"],
                 "padoms": "30 − 2 · 2."},
                {"jaut": "Stikla laukums (30 − 4)^2 = 900 − ? + 16",
                 "atb": ["240"], "padoms": "2 · 30 · 4."},
                {"jaut": "Stikla laukums (cm²)?", "atb": ["676"],
                 "padoms": "26^2."},
            ]),
            pavediens="maja",
            konteksts="Bildes rāmis «apēd» joslu no katras malas - stikls ir "
                      "mazāks kvadrāts.",
            kapec="Starpības kvadrāts dod stikla laukumu."),

    Kopsavilkums([
        "Lietoju starpības kvadrāta formulu.",
        "Liku pareizas zīmes: − pie 2ab, + pie b^2.",
        "Zinu, ka (b − a)^2 = (a − b)^2.",
    ]),

    Majas([
        "Atver: (x − 9)^2; (2m − 7)^2; (0,5 − a)^2.",
        "Aprēķini galvā 49^2 = (50 − 1)^2.",
        "Uzzīmē laukuma modeli (a − b)^2.",
    ]),
]
