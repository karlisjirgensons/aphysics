# -*- coding: utf-8 -*-
"""9. klase, 66. stunda: «Kas ir kvadrātu starpība?»

a^2 − b^2 = (a − b)(a + b). Laukuma modelis: no kvadrāta a^2 izgriež b^2,
un atlikušo L veida figūru pārliek taisnstūrī (a + b) × (a − b).
Galvā: 48 · 52 = 50^2 − 2^2 = 2496.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kas ir kvadrātu starpība?"

MERKIS = "Formulēsim un lietosim kvadrātu starpības formulu."

_T = "text"

# a = 5, b = 2.
_L_FIGURA = geometrija([("_1", 0, 0), ("_2", 5, 0), ("_3", 5, 3),
                        ("_4", 3, 3), ("_5", 3, 5), ("_6", 0, 5),
                        ("_7", 3, 0)],
                       nogriezni=[("_1", "_2"), ("_2", "_3"), ("_3", "_4"),
                                  ("_4", "_5"), ("_5", "_6"), ("_6", "_1"),
                                  ("_7", "_4")],
                       iekrasot=[(("_1", "_7", "_4", "_5", "_6"), 0),
                                 (("_7", "_2", "_3", "_4"), 1)],
                       malas=[(("_1", "_2"), "a"), (("_6", "_1"), "a"),
                              (("_2", "_3"), "a − b")])

_TAISNSTURIS = geometrija([("_1", 0, 0), ("_2", 7, 0), ("_3", 7, 3),
                           ("_4", 0, 3), ("_5", 5, 0), ("_6", 5, 3)],
                          nogriezni=[("_1", "_2"), ("_2", "_3"),
                                     ("_3", "_4"), ("_4", "_1"),
                                     ("_5", "_6")],
                          iekrasot=[(("_1", "_5", "_6", "_4"), 0),
                                    (("_5", "_2", "_3", "_6"), 1)],
                          malas=[(("_1", "_2"), "a + b"),
                                 (("_4", "_1"), "a − b")])

SATURS = [
    Sakums("48 · 52 galvā?",
           zimejums=_TAISNSTURIS,
           paraksts="(50 − 2)(50 + 2) = 50² − 2² = 2500 − 4 = 2496.",
           fakti=["a^2 − b^2 = (a − b)(a + b).",
                  "Vidējo locekļu nav - tie saīsinās.",
                  "Der gan atvēršanai, gan sadalīšanai."]),

    Slidnis("No kvadrāta uz taisnstūri", [
        {"v": "a² − b²", "teksts": "No kvadrāta a × a izgriež kvadrātu b × b",
         "zim": _L_FIGURA},
        {"v": "Pārliek", "teksts": "Taisnstūri a − b pārliek blakus",
         "zim": _TAISNSTURIS},
        {"v": "Laukums", "teksts": "(a + b)(a − b) - tas pats laukums",
         "zim": _TAISNSTURIS},
    ]),

    Doma("Kvadrātu starpība",
         "a^2 − b^2 = (a − b)(a + b).",
         soli=[
             "Atverot: (a − b)(a + b) = a^2 + ab − ab − b^2.",
             "Sadalot: atpazīsti divus kvadrātus ar mīnusu starp tiem.",
             "Katru kvadrātu «izvelc no saknes»: 9x^2 = (3x)^2.",
             "Summa a^2 + b^2 reizinātājos NEsadalās.",
         ]),

    Paraugs("Sadali reizinātājos",
            uzd="Sadali reizinātājos 25x^2 − 16.",
            soli=[
                ("25x^2 = (5x)^2; 16 = 4^2", "Divi kvadrāti."),
                ("(5x)^2 − 4^2 = (5x − 4)(5x + 4)", "Formula."),
            ],
            atbilde="(5x − 4)(5x + 4)"),

    Ievadi("Atver vai sadali", [
        {"jaut": "(x − 3)(x + 3)", "atb": ["x^2 − 9"], "tastatura": _T,
         "padoms": "x^2 − 3^2."},
        {"jaut": "(2a + 5)(2a − 5)", "atb": ["4a^2 − 25"], "tastatura": _T,
         "padoms": "(2a)^2 − 25."},
        {"jaut": "x^2 − 49", "atb": ["(x − 7)(x + 7)", "(x + 7)(x − 7)"],
         "tastatura": _T, "padoms": "49 = 7^2."},
        {"jaut": "9y^2 − 1", "atb": ["(3y − 1)(3y + 1)", "(3y + 1)(3y − 1)"],
         "tastatura": _T, "padoms": "(3y)^2 − 1^2."},
        {"jaut": "Galvā: 31 · 29 = ?", "atb": ["899"],
         "padoms": "30^2 − 1."},
        {"jaut": "Galvā: 105 · 95 = ?", "atb": ["9975", "9 975"],
         "padoms": "100^2 − 25."},
    ], pamats=4),

    Varianti("Sadalās vai nē?", [
        {"jaut": "x^2 + 16",
         "opcijas": ["Nesadalās (summa)", "(x + 4)(x − 4)", "(x + 4)^2",
                     "(x + 4)(x + 4)"],
         "pareizi": 0, "padoms": "Formula ir starpībai."},
        {"jaut": "a^2 − 10",
         "opcijas": ["(a − √10)(a + √10)", "Nesadalās nekādi",
                     "(a − 5)(a + 5)", "(a − 10)^2"],
         "pareizi": 0, "padoms": "10 = (√10)^2."},
        {"jaut": "4 − x^2",
         "opcijas": ["(2 − x)(2 + x)", "(x − 2)(x + 2)", "(4 − x)^2",
                     "Nesadalās"],
         "pareizi": 0, "padoms": "2^2 − x^2."},
    ]),

    Pasaule("Kvadrātveida plāksne ar caurumu",
            Ievadi("", [
                {"jaut": "Plāksne 12 cm × 12 cm, vidū izgriež kvadrātu 4 cm × "
                         "4 cm. Palikušais laukums (cm²)?", "atb": ["128"],
                 "padoms": "(12 − 4)(12 + 4)."},
                {"jaut": "Plāksne 25 × 25, caurums 15 × 15. Laukums?",
                 "atb": ["400"], "padoms": "10 · 40."},
            ]),
            pavediens="tehnika",
            konteksts="Metāla starplikas izgriež kā kvadrātu ar kvadrātveida "
                      "caurumu.",
            kapec="Viena reizināšana, nevis divi kvadrāti."),

    Kopsavilkums([
        "Lietoju a^2 − b^2 = (a − b)(a + b).",
        "Atpazīstu kvadrātus: 9x^2 = (3x)^2.",
        "Zinu, ka summa a^2 + b^2 nesadalās.",
    ]),

    Majas([
        "Sadali: 64 − a^2; 49x^2 − 36y^2.",
        "Galvā: 67 · 73; 998 · 1002.",
        "Izgriez no papīra L figūru un pārliec to taisnstūrī.",
    ]),
]
