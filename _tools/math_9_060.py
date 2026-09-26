# -*- coding: utf-8 -*-
"""9. klase, 60. stunda: «Kā grupēt locekļus?»

Četriem locekļiem bez kopīga reizinātāja: sagrupē pa pāriem, katrā pārī
iznes reizinātāju, un parādās kopīga iekava. Laukuma modelis rāda, ka
(a + b)(x + y) ir četri taisnstūri.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija, restis)

TEMA = "Kā grupēt locekļus?"

MERKIS = "Sadalīsim polinomu reizinātājos ar grupēšanas paņēmienu."

_T = "text"

_LAUKUMS = geometrija([("_1", 0, 0), ("_2", 5, 0), ("_3", 7, 0),
                       ("_4", 7, 3), ("_5", 7, 5), ("_6", 5, 5),
                       ("_7", 0, 5), ("_8", 0, 3), ("_9", 5, 3)],
                      nogriezni=[("_1", "_3"), ("_3", "_5"), ("_5", "_7"),
                                 ("_7", "_1"), ("_2", "_6"), ("_8", "_4")],
                      iekrasot=[(("_1", "_2", "_9", "_8"), 0),
                                (("_9", "_4", "_5", "_6"), 0),
                                (("_2", "_3", "_4", "_9"), 1),
                                (("_8", "_9", "_6", "_7"), 1)],
                      malas=[(("_1", "_2"), "x"), (("_2", "_3"), "y"),
                             (("_7", "_8"), "b"), (("_8", "_1"), "a")],
                      uzraksti=[(2.5, 1.5, "ax"), (6, 1.5, "ay"),
                                (2.5, 4, "bx"), (6, 4, "by")])

SATURS = [
    Sakums("ax + ay + bx + by - kopīga reizinātāja nav",
           zimejums=_LAUKUMS,
           paraksts="Četri taisnstūri kopā: (a + b)(x + y).",
           fakti=["Grupē pa pāriem: (ax + ay) + (bx + by).",
                  "Katrā pārī iznes: a(x + y) + b(x + y).",
                  "Kopīgā iekava ārā: (x + y)(a + b)."]),

    Slidnis("Grupēšana pa soļiem", [
        {"v": "1", "teksts": "ax + ay + bx + by",
         "zim": restis([["ax", "ay", "bx", "by"]])},
        {"v": "2", "teksts": "(ax + ay) + (bx + by) - pāri",
         "zim": restis([["ax + ay", "bx + by"]])},
        {"v": "3", "teksts": "a(x + y) + b(x + y) - iznests katrā pārī",
         "zim": restis([["a(x + y)", "b(x + y)"]])},
        {"v": "4", "teksts": "(x + y)(a + b) - kopīgā iekava ārā",
         "zim": restis([["(x + y)", "·", "(a + b)"]])},
    ]),

    Doma("Grupēšanas paņēmiens",
         "Sagrupē locekļus tā, lai katrā grupā pēc iznešanas paliktu vienāda "
         "iekava.",
         soli=[
             "Sagrupē pa diviem (dažreiz jāmaina secība).",
             "Katrā grupā iznes kopīgo reizinātāju.",
             "Ja iekavas vienādas - iznes tās.",
             "Ja iekavas atšķiras tikai ar zīmi - iznes −1.",
         ]),

    Paraugs("Ar mīnusu",
            uzd="Sadali reizinātājos x^3 − 2x^2 − 3x + 6.",
            soli=[
                ("(x^3 − 2x^2) + (−3x + 6)", "Pāri."),
                ("x^2(x − 2) − 3(x − 2)", "Otrajā iznes −3!"),
                ("(x − 2)(x^2 − 3)", "Kopīgā iekava."),
            ],
            atbilde="(x − 2)(x^2 − 3)"),

    Ievadi("Sadali ar grupēšanu", [
        {"jaut": "ab + 3a + 2b + 6", "atb": ["(b + 3)(a + 2)",
                                             "(a + 2)(b + 3)"],
         "tastatura": _T, "padoms": "a(b + 3) + 2(b + 3)."},
        {"jaut": "xy − 5x + 4y − 20", "atb": ["(y − 5)(x + 4)",
                                              "(x + 4)(y − 5)"],
         "tastatura": _T, "padoms": "x(y − 5) + 4(y − 5)."},
        {"jaut": "a^2 + ab + 2a + 2b", "atb": ["(a + b)(a + 2)",
                                               "(a + 2)(a + b)"],
         "tastatura": _T, "padoms": "a(a + b) + 2(a + b)."},
        {"jaut": "mn − 2m − 3n + 6", "atb": ["(n − 2)(m − 3)",
                                             "(m − 3)(n − 2)"],
         "tastatura": _T, "padoms": "m(n − 2) − 3(n − 2)."},
    ]),

    Varianti("Pabeidz", [
        {"jaut": "3x(y − 4) + 5(y − 4) = ?",
         "opcijas": ["(y − 4)(3x + 5)", "(y − 4)(3x · 5)",
                     "15x(y − 4)", "(y − 4)^2(3x + 5)"],
         "pareizi": 0, "padoms": "Kopīgā iekava."},
        {"jaut": "a(x − 1) − b(1 − x) = ?",
         "opcijas": ["(x − 1)(a + b)", "(x − 1)(a − b)",
                     "(1 − x)(a − b)", "Nevar sadalīt"],
         "pareizi": 0, "padoms": "−b(1 − x) = +b(x − 1)."},
    ]),

    Pasaule("Divu preču komplekti",
            Ievadi("", [
                {"jaut": "Veikals pārdod a kastes ar x zīmuļiem un y "
                         "pildspalvām, un b tādas pašas kastes. Viss kopā: "
                         "(a + b)(x + y). a = 4, b = 6, x = 10, y = 5. Kopā "
                         "priekšmetu?", "atb": ["150"], "padoms": "10 · 15."},
                {"jaut": "Tas pats, skaitot pa daļām: ax + ay + bx + by = ?",
                 "atb": ["150"], "padoms": "40 + 20 + 60 + 30."},
            ]),
            pavediens="veikals",
            konteksts="Noliktavā vienādas kastes nāk divās piegādēs; katrā "
                      "kastē ir divu veidu preces.",
            kapec="Grupēšana apvieno četrus rēķinus vienā."),

    Kopsavilkums([
        "Sagrupēju locekļus pa pāriem.",
        "Iznesu reizinātāju katrā pārī un tad kopīgo iekavu.",
        "Uzmanos ar mīnusa zīmi.",
    ]),

    Majas([
        "Sadali: 2ax − 6a + bx − 3b; x^3 + x^2 + x + 1.",
        "Pārbaudi, atverot iekavas.",
        "Uzzīmē laukuma modeli izteiksmei (a + 3)(b + 2).",
    ]),
]
