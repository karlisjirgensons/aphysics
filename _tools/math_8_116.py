# -*- coding: utf-8 -*-
"""8. klase, 116. stunda: «Kā atver iekavas ar mīnusu?»

−(a − b + c) = −a + b − c: mīnuss pirms iekavām ir reizināšana ar −1,
tāpēc mainās KATRA locekļa zīme. Biežākā kļūda - mainīt tikai pirmo
zīmi: 8 − (x − 3) ≠ 8 − x − 3.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā atver iekavas ar mīnusu?"

MERKIS = ("Atvērsim iekavas, pirms kurām ir mīnusa zīme, un pamatosim zīmju "
          "maiņu.")

_T = "text"

SATURS = [
    Sakums("8 − (x − 3) = ?",
           zimejums=restis([["8 − (x − 3)", "=", "8 − x + 3"],
                            ["", "=", "11 − x"]]),
           paraksts="Mīnuss pirms iekavām maina katru zīmi iekavās.",
           fakti=["−(…) nozīmē (−1) · (…).",
                  "Mainās katra locekļa zīme, ne tikai pirmā.",
                  "Plus pirms iekavām zīmes nemaina."]),

    Doma("Zīmju maiņa",
         "−(a − b + c) = −a + b − c.",
         soli=[
             "Mīnuss pirms iekavām ir reizināšana ar −1.",
             "Reizinot ar −1, katrs loceklis maina zīmi.",
             "Pēc iekavu atvēršanas savelc līdzīgos.",
             "Ligzdotas iekavas atver no iekšpuses.",
         ],
         pieze="Pārbaude ar skaitli: x = 1 - 8 − (1 − 3) = 10, 11 − 1 = 10."),

    Paraugs("Vairākas iekavas",
            uzd="Vienkāršo 5x − (2x − 3) + (x − 4).",
            soli=[
                ("5x − 2x + 3 + x − 4", "Otrā iekava - zīmes mainās, trešā - "
                                        "ne."),
                ("4x − 1", "Savelk."),
            ],
            atbilde="4x − 1"),

    Ievadi("Atver iekavas un vienkāršo", [
        {"jaut": "−(x − 5)", "atb": ["−x + 5", "5 − x"], "tastatura": _T,
         "padoms": "Abi locekļi maina zīmi."},
        {"jaut": "7 − (a + 7)", "atb": ["−a"], "tastatura": _T,
         "padoms": "7 − a − 7."},
        {"jaut": "3a − (a − 2b)", "atb": ["2a + 2b"], "tastatura": _T,
         "padoms": "3a − a + 2b."},
        {"jaut": "10 − (4 − x)", "atb": ["x + 6", "6 + x"], "tastatura": _T,
         "padoms": "10 − 4 + x."},
        {"jaut": "2x − (3x − (x − 1))", "atb": ["−1"], "tastatura": _T,
         "padoms": "Iekšā: 3x − x + 1 = 2x + 1."},
        {"jaut": "−(−a − b)", "atb": ["a + b"], "tastatura": _T,
         "padoms": "Mīnuss reiz mīnuss."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "−(a − b) = ?",
         "opcijas": ["−a + b", "−a − b", "a − b", "a + b"],
         "pareizi": 0, "padoms": "Abas zīmes mainās."},
        {"jaut": "Skolēns: 8 − (x − 3) = 8 − x − 3. Kļūda?",
         "opcijas": ["Jābūt + 3", "Jābūt + x", "Kļūdas nav",
                     "Jābūt − 8"],
         "pareizi": 0, "padoms": "−(−3) = +3."},
        {"jaut": "Kāpēc zīmes mainās?",
         "opcijas": ["−(…) ir reizināšana ar −1", "Tā vienojās",
                     "Iekavas to prasa", "Tikai pirmā mainās"],
         "pareizi": 0, "padoms": "(−1) · (−3) = 3."},
    ]),

    Pasaule("Maka atlikums",
            Ievadi("", [
                {"jaut": "Makā 50 €. Iztērēja (x + 12) €. Atlikums = ? − x",
                 "atb": ["38"], "padoms": "50 − x − 12."},
                {"jaut": "x = 20. Atlikums (€)?", "atb": ["18"],
                 "padoms": "38 − 20."},
                {"jaut": "Ar atlaidi iztērēja (x − 5) €. Atlikums = ? − x",
                 "atb": ["55"], "padoms": "50 − x + 5."},
            ]),
            pavediens="veikals",
            konteksts="Atņemot izdevumus iekavās, atlaide (mīnuss iekavās) "
                      "atlikumu palielina.",
            kapec="Mīnuss pirms iekavām maina katru zīmi."),

    Kopsavilkums([
        "Atveru iekavas ar mīnusu, mainot katru zīmi.",
        "Pamatoju zīmju maiņu ar reizināšanu ar −1.",
        "Pārbaudu pārveidojumu ar skaitli.",
    ]),

    Majas([
        "Vienkāršo: 12 − (5 − a) − (a + 2).",
        "Atrodi kļūdu draugam izdomātā piemērā.",
        "Pārbaudi katru rezultātu ar a = 1.",
    ]),
]
