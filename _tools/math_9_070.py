# -*- coding: utf-8 -*-
"""9. klase, 70. stunda: «Kā vienkāršot garāku izteiksmi?»

Eksāmena 1. daļas tipiskais uzdevums: (2c − 3)(5 + c) − 3c vai
(x + 2)^2 − (x − 2)^2. Plāns - katru daļu atver ar piemērotāko paņēmienu,
iekavas ar mīnusu priekšā atver uzmanīgi, tad savelk līdzīgos locekļus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā vienkāršot garāku izteiksmi?"

MERKIS = ("Vienkāršosim izteiksmi, lietojot vairākas formulas un "
          "pārveidojumus.")

_T = "text"

SATURS = [
    Sakums("(x + 2)² − (x − 2)² - cik tas ir?",
           zimejums=restis([["x", "(x + 2)² − (x − 2)²", "8x"],
                            ["1", "9 − 1 = 8", "8"],
                            ["5", "49 − 9 = 40", "40"]]),
           paraksts="Garā izteiksme vienmēr ir tikai 8x.",
           fakti=["Katras iekavas atver ar formulu.",
                  "Mīnuss pirms iekavām maina VISAS zīmes.",
                  "Līdzīgie locekļi saīsinās."]),

    Doma("Vienkāršošanas plāns",
         "Atver katru daļu atsevišķi (iekavās!), tad noņem iekavas ar zīmēm "
         "un savelc līdzīgos locekļus.",
         soli=[
             "Nosaki katrai daļai paņēmienu: formula vai reizināšana.",
             "Rezultātu raksti iekavās, ja priekšā ir mīnuss.",
             "Atver iekavas, mainot zīmes aiz mīnusa.",
             "Savelc līdzīgos locekļus, sakārto pēc pakāpēm.",
         ]),

    Paraugs("Eksāmens 2025, 3.4. uzdevums",
            uzd="Izpildi darbības: (2c − 3)(5 + c) − 3c.",
            soli=[
                ("(2c − 3)(5 + c) = 10c + 2c^2 − 15 − 3c",
                 "Katrs ar katru."),
                ("= 2c^2 + 7c − 15", "Savelk."),
                ("2c^2 + 7c − 15 − 3c = 2c^2 + 4c − 15", "Atņem 3c."),
            ],
            atbilde="2c^2 + 4c − 15"),

    Paraugs("Divas formulas",
            uzd="Vienkāršo: (a + 3)(a − 3) − (a − 1)^2.",
            soli=[
                ("(a + 3)(a − 3) = a^2 − 9", "Kvadrātu starpība."),
                ("(a − 1)^2 = a^2 − 2a + 1", "Starpības kvadrāts."),
                ("a^2 − 9 − (a^2 − 2a + 1) = a^2 − 9 − a^2 + 2a − 1",
                 "Mīnuss maina zīmes."),
                ("= 2a − 10", "Savelk."),
            ],
            atbilde="2a − 10"),

    Ievadi("Vienkāršo", [
        {"jaut": "(x + 1)^2 − x^2", "atb": ["2x + 1", "1 + 2x"],
         "tastatura": _T, "padoms": "x^2 + 2x + 1 − x^2."},
        {"jaut": "(a − 4)(a + 4) + 16", "atb": ["a^2"], "tastatura": _T,
         "padoms": "a^2 − 16 + 16."},
        {"jaut": "(x + 3)^2 − (x − 3)^2", "atb": ["12x"], "tastatura": _T,
         "padoms": "6x − (−6x)."},
        {"jaut": "2(x − 1)^2 − 2x^2", "atb": ["−4x + 2", "2 − 4x"],
         "tastatura": _T, "padoms": "2x^2 − 4x + 2 − 2x^2."},
        {"jaut": "(y + 5)(y − 2) − y^2", "atb": ["3y − 10", "−10 + 3y"],
         "tastatura": _T, "padoms": "y^2 + 3y − 10 − y^2."},
    ], pamats=3),

    Varianti("Kur kļūda?", [
        {"jaut": "x^2 − (x − 2)^2 = x^2 − x^2 − 4x + 4",
         "opcijas": ["Zīmes: jābūt + 4x − 4", "Pareizi",
                     "Jābūt x^2 − x^2 − 4", "Trūkst 2x"],
         "pareizi": 0, "padoms": "−(x^2 − 4x + 4) = −x^2 + 4x − 4."},
        {"jaut": "(a + b)^2 − (a − b)^2 = ?",
         "opcijas": ["4ab", "2b^2", "0", "2a^2 + 2b^2"],
         "pareizi": 0, "padoms": "2ab − (−2ab)."},
    ]),

    Pasaule("Burvju triks",
            Ievadi("", [
                {"jaut": "«Izdomā skaitli n, aprēķini (n + 1)^2 − (n − 1)^2 "
                         "un izdali ar n.» Kas vienmēr sanāk?",
                 "atb": ["4"], "padoms": "(n + 1)^2 − (n − 1)^2 = 4n."},
                {"jaut": "Pārbaudi ar n = 7: (64 − 36) : 7 = ?",
                 "atb": ["4"], "padoms": "28 : 7."},
            ]),
            pavediens="speles",
            konteksts="Burvis «uzmin» rezultātu, jo izteiksme vienkāršojas "
                      "līdz konstantei.",
            kapec="Vienkāršošana atklāj trika noslēpumu."),

    Kopsavilkums([
        "Vienkāršoju izteiksmes ar vairākām formulām.",
        "Pareizi atveru iekavas ar mīnusu priekšā.",
        "Pārbaudu rezultātu, ievietojot skaitli.",
    ]),

    Majas([
        "Vienkāršo: (2x − 1)^2 − 4x(x − 1).",
        "Vienkāršo: (m + n)(m − n) + (n − m)^2.",
        "Izdomā savu «burvju triku» ar formulām.",
    ]),
]
