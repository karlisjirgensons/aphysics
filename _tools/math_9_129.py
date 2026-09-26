# -*- coding: utf-8 -*-
"""9. klase, 129. stunda: «Kāda ir virknes likumsakarība?»

Mikrotemata noslēgums: no pirmajiem locekļiem atrast formulu. Pieeja -
salīdzināt ar zināmām virknēm (n, 2n, n^2, 2^n) un paskatīties uz
starpībām. Figūru virknes kā IQ testā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kāda ir virknes likumsakarība?"

MERKIS = ("Saskatīsim likumsakarību dotā virknē un pierakstīsim to ar "
          "formulu.")

_T = "text"

SATURS = [
    Sakums("IQ tests: 2, 6, 12, 20, 30, ?",
           zimejums=restis([["n", "1", "2", "3", "4", "5", "6"],
                            ["aₙ", "2", "6", "12", "20", "30", None],
                            ["starpība", "", "4", "6", "8", "10", None]]),
           paraksts="Starpības aug par 2 - nākamā ir 12, atbilde 42.",
           fakti=["Formula: a_n = n(n + 1).",
                  "Pārbaude: 5 · 6 = 30 ✔.",
                  "Starpības atklāj likumsakarību."]),

    Doma("Kā atrast formulu",
         "Salīdzini ar zināmām virknēm un aplūko starpības starp blakus "
         "locekļiem.",
         soli=[
             "Starpības vienādas → a_n = dn + b (lineāra).",
             "Starpības aug vienmērīgi → formula ar n^2.",
             "Katrs reizināts ar vienu skaitli → formula ar q^n.",
             "Pārbaudi formulu ar vismaz 3 locekļiem.",
         ]),

    Slidnis("Zināmās virknes", [
        {"v": "n", "teksts": "1, 2, 3, 4, ... - naturālie skaitļi"},
        {"v": "2n", "teksts": "2, 4, 6, 8, ... - pāra skaitļi"},
        {"v": "n²", "teksts": "1, 4, 9, 16, ... - kvadrāti"},
        {"v": "2ⁿ", "teksts": "2, 4, 8, 16, ... - divnieka pakāpes"},
        {"v": "n(n + 1)", "teksts": "2, 6, 12, 20, ... - «taisnstūra» skaitļi"},
    ]),

    Ievadi("Atrodi formulu vai locekli", [
        {"jaut": "4, 7, 10, 13, ... a_n = ?", "atb": ["3n + 1", "1 + 3n"],
         "tastatura": _T, "padoms": "Starpība 3, a_1 = 4."},
        {"jaut": "2, 5, 10, 17, 26, ... a_6 = ?", "atb": ["37"],
         "padoms": "n^2 + 1."},
        {"jaut": "3, 6, 12, 24, ... a_6 = ?", "atb": ["96"],
         "padoms": "· 2."},
        {"jaut": "1, 8, 27, 64, ... a_5 = ?", "atb": ["125"],
         "padoms": "n^3."},
        {"jaut": "0, 3, 8, 15, 24, ... a_n = ?", "atb": ["n^2 − 1"],
         "tastatura": _T, "padoms": "Kvadrāti mīnus 1."},
    ], pamats=3),

    Varianti("Figūru virkne", [
        {"jaut": "Trīsstūri no punktiem: 1, 3, 6, 10, ... Nākamais?",
         "opcijas": ["15", "14", "16", "20"],
         "pareizi": 0, "padoms": "+2, +3, +4, +5."},
        {"jaut": "Kvadrātu rāmji no flīzēm: 8, 12, 16, 20 (4n + 4). 10. "
                 "rāmis?",
         "opcijas": ["44", "40", "48", "36"],
         "pareizi": 0, "padoms": "4 · 10 + 4."},
    ]),

    Pasaule("Stadiona sēdvietas",
            Ievadi("", [
                {"jaut": "Tribīnē 1. rindā 20 vietu, katrā nākamajā par 2 "
                         "vairāk. Formula a_n = 2n + ?", "atb": ["18"],
                 "padoms": "a_1 = 20 = 2 + 18."},
                {"jaut": "Cik vietu 15. rindā?", "atb": ["48"],
                 "padoms": "30 + 18."},
            ]),
            pavediens="sports",
            konteksts="Stadiona tribīnes paplašinās uz augšu - katrā rindā "
                      "dažas vietas vairāk.",
            kapec="Formula atbild, cik krēslu pasūtīt katrai rindai."),

    Kopsavilkums([
        "Saskatu likumsakarību pēc starpībām.",
        "Salīdzinu ar zināmām virknēm.",
        "Pierakstu formulu un pārbaudu.",
    ]),

    Majas([
        "Atrodi formulu: 5, 9, 13, 17, ...; 1, 3, 9, 27, ...",
        "Izdomā savu «IQ testa» virkni draugam.",
        "Uzzīmē trīsstūra skaitļu figūras 1, 3, 6, 10.",
    ]),
]
