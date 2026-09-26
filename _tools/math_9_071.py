# -*- coding: utf-8 -*-
"""9. klase, 71. stunda: «Kā saīsināt algebrisku daļu?»

Daļu saīsina, dalot skaitītāju un saucēju ar kopīgu REIZINĀTĀJU, tāpēc
vispirms abus sadala reizinātājos. Jāpieraksta arī, pie kādām vērtībām
daļai ir jēga (saucējs ≠ 0).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā saīsināt algebrisku daļu?"

MERKIS = ("Saīsināsim algebrisku daļu, sadalot skaitītāju un saucēju "
          "reizinātājos.")

_T = "text"

SATURS = [
    Sakums("{x^2 − 9|x + 3} = ?",
           zimejums=restis([["x", "(x² − 9) : (x + 3)", "x − 3"],
                            ["5", "16 : 8 = 2", "2"],
                            ["10", "91 : 13 = 7", "7"]]),
           paraksts="Garā daļa vienmēr ir x − 3 (ja x ≠ −3).",
           fakti=["Skaitītājs: x^2 − 9 = (x − 3)(x + 3).",
                  "Kopīgo reizinātāju x + 3 saīsina.",
                  "Pie x = −3 daļai nav jēgas."]),

    Slidnis("Saīsināšana pa soļiem", [
        {"v": "1", "teksts": "{x^2 + 4x + 4|x^2 − 4} - sadala abus"},
        {"v": "2", "teksts": "{(x + 2)^2|(x − 2)(x + 2)} - kopīgs reizinātājs "
                             "x + 2"},
        {"v": "3", "teksts": "{x + 2|x − 2}, x ≠ ±2"},
    ]),

    Doma("Saīsināšanas kārtība",
         "Sadali skaitītāju un saucēju reizinātājos → nosaki, kur saucējs ir "
         "0 → saīsini kopīgos reizinātājus.",
         soli=[
             "Iznes kopīgo reizinātāju vai lieto formulu.",
             "Pieraksti aizliegtās vērtības (saucējs = 0).",
             "Saīsini tikai VISA skaitītāja un VISA saucēja reizinātājus.",
             "Pārbaudi ar skaitli.",
         ],
         pieze="{a − b|b − a} = −1, jo b − a = −(a − b)."),

    Paraugs("Ar iznešanu",
            uzd="Saīsini daļu {3x^2 − 6x|x^2 − 4}.",
            soli=[
                ("3x^2 − 6x = 3x(x − 2)", "Skaitītājs."),
                ("x^2 − 4 = (x − 2)(x + 2)", "Saucējs; x ≠ ±2."),
                ("{3x(x − 2)|(x − 2)(x + 2)} = {3x|x + 2}", "Saīsina x − 2."),
            ],
            atbilde="{3x|x + 2}"),

    Ievadi("Saīsini", [
        {"jaut": "{x^2 − 25|x − 5}", "atb": ["x + 5", "5 + x"],
         "tastatura": _T, "padoms": "(x − 5)(x + 5)."},
        {"jaut": "{a^2 + 6a + 9|a + 3}", "atb": ["a + 3", "3 + a"],
         "tastatura": _T, "padoms": "(a + 3)^2."},
        {"jaut": "{4x − 8|x^2 − 4x + 4} = {4|?}", "atb": ["x − 2"],
         "tastatura": _T, "padoms": "4(x − 2) : (x − 2)^2."},
        {"jaut": "{y − 7|7 − y}", "atb": ["−1", "-1"],
         "padoms": "Pretēji skaitļi."},
        {"jaut": "{x^2 − x|x} = ? (x ≠ 0)", "atb": ["x − 1"],
         "tastatura": _T, "padoms": "x(x − 1) : x."},
    ], pamats=3),

    Varianti("Pareizi saīsināts?", [
        {"jaut": "{x^2 + 9|x + 3} = x + 3",
         "opcijas": ["Nē - x^2 + 9 nesadalās", "Jā", "Jā, ja x > 0",
                     "Jābūt x − 3"],
         "pareizi": 0, "padoms": "Pārbaudi x = 1: 10 : 4 ≠ 4."},
        {"jaut": "{x + 2|x + 5} = {2|5}",
         "opcijas": ["Nē - x ir saskaitāmais, ne reizinātājs", "Jā",
                     "Jā, ja x ≠ 0", "Jābūt {x|x}"],
         "pareizi": 0, "padoms": "Saīsina tikai reizinātājus."},
        {"jaut": "Kurām x vērtībām daļai {x|x^2 − 1} nav jēgas?",
         "opcijas": ["x = 1 un x = −1", "x = 0", "x = 1", "Nav tādu"],
         "pareizi": 0, "padoms": "x^2 − 1 = 0."},
    ]),

    Pasaule("Vidējais ātrums",
            Ievadi("", [
                {"jaut": "Velosipēdists nobrauc x^2 − 16 km laikā x − 4 "
                         "stundas. Vidējais ātrums = {x^2 − 16|x − 4} = x + ? "
                         "km/h", "atb": ["4"], "padoms": "(x − 4)(x + 4)."},
                {"jaut": "x = 16. Ātrums (km/h)?", "atb": ["20"],
                 "padoms": "16 + 4."},
            ]),
            pavediens="celojums",
            konteksts="Ātrums ir ceļš : laiks; kad abi ir izteiksmes, daļa "
                      "bieži saīsinās.",
            kapec="Saīsinātā izteiksme ir vieglāk aprēķināma."),

    Kopsavilkums([
        "Sadalu skaitītāju un saucēju reizinātājos.",
        "Saīsinu tikai kopīgus reizinātājus.",
        "Pierakstu, kur daļai nav jēgas.",
    ]),

    Majas([
        "Saīsini: {x^2 − 1|x^2 + 2x + 1}; {5a − 10|a^2 − 4}.",
        "Paskaidro, kāpēc {x + 3|3} ≠ x.",
        "Pārbaudi katru rezultātu ar x = 3.",
    ]),
]
