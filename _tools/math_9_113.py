# -*- coding: utf-8 -*-
"""9. klase, 113. stunda: «Kā risināt ar ievietošanas paņēmienu?»

Ievietošana: no viena vienādojuma izsaka nezināmo un ievieto otrā - rodas
vienādojums ar vienu nezināmo. Labāk izsakot to nezināmo, kura koeficients
ir 1 vai −1.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, paris)

TEMA = "Kā risināt ar ievietošanas paņēmienu?"

MERKIS = ("Atrisināsim sistēmu, izsakot vienu nezināmo un ievietojot to "
          "otrā vienādojumā.")

_T = "text"

SATURS = [
    Sakums("y = 2x un x + y = 12",
           fakti=["Pirmais jau pasaka, kas ir y: 2x.",
                  "Ievieto otrajā: x + 2x = 12 ⇒ x = 4.",
                  "Tad y = 2 · 4 = 8; atbilde (4; 8)."]),

    Slidnis("Ievietošana pa soļiem", [
        {"v": "Dots", "teksts": "x + 2y = 7 un 3x − y = 7"},
        {"v": "1", "teksts": "No pirmā: x = 7 − 2y"},
        {"v": "2", "teksts": "Ievieto otrajā: 3(7 − 2y) − y = 7"},
        {"v": "3", "teksts": "21 − 6y − y = 7 ⇒ −7y = −14 ⇒ y = 2"},
        {"v": "4", "teksts": "x = 7 − 2 · 2 = 3; atbilde (3; 2)"},
    ]),

    Doma("Ievietošanas paņēmiens",
         "Izsaki vienu nezināmo no viena vienādojuma un ievieto otrajā; "
         "atrisini, tad atrodi otro nezināmo.",
         soli=[
             "Izvēlies nezināmo ar koeficientu 1 vai −1.",
             "Izsaki to: x = ... vai y = ... .",
             "Ievieto izteiksmi (iekavās!) otrajā vienādojumā.",
             "Atrisini un atrodi otro nezināmo.",
             "Pārbaudi abos vienādojumos.",
         ]),

    Paraugs("Ar negatīvu koeficientu",
            uzd="Atrisini: 2x − y = 5 un 3x + 2y = 11.",
            soli=[
                ("y = 2x − 5", "No pirmā."),
                ("3x + 2(2x − 5) = 11 ⇒ 7x = 21 ⇒ x = 3", "Ievieto."),
                ("y = 6 − 5 = 1", "Otrs nezināmais."),
                ("2 · 3 − 1 = 5 ✔; 9 + 2 = 11 ✔", "Pārbaude."),
            ],
            atbilde="(3; 1)"),

    Ievadi("Atrisini ar ievietošanu", [
        {"jaut": "y = x + 1 un 2x + y = 10", "atb": paris(3, 4),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "3x + 1 = 10."},
        {"jaut": "x = 2y un x + y = 9", "atb": paris(6, 3),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "3y = 9."},
        {"jaut": "x − y = 2 un 3x + y = 14", "atb": paris(4, 2),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "x = y + 2."},
        {"jaut": "y = 3x − 4 un y = x + 2", "atb": paris(3, 5),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "3x − 4 = x + 2."},
        {"jaut": "x + 3y = 1 un 2x − y = 9", "atb": paris(4, "−1") +
         paris(4, "-1"), "tastatura": _T, "vieta": "(x; y)",
         "padoms": "x = 1 − 3y."},
    ], pamats=3),

    Varianti("Ko izteikt?", [
        {"jaut": "4x + y = 11 un 3x − 5y = 6. Ērtāk izteikt...",
         "opcijas": ["y no pirmā", "x no pirmā", "x no otrā", "y no otrā"],
         "pareizi": 0, "padoms": "Koeficients 1."},
        {"jaut": "Kur kļūda: 3x − 2(4 − x)... ⇒ 3x − 8 − 2x?",
         "opcijas": ["−2 · (−x) = +2x", "Nav kļūdas", "Jābūt −8 + 2",
                     "Jābūt 3x + 8"],
         "pareizi": 0, "padoms": "Mīnuss reiz mīnuss."},
    ]),

    Pasaule("Ēdnīcas pusdienas",
            Ievadi("", [
                {"jaut": "Zupa ir par 1,5 € lētāka nekā pamatēdiens; kopā "
                         "5,50 €. y = x − 1,5 un x + y = 5,5. Pamatēdiens (€)?",
                 "atb": ["3,5"], "padoms": "2x − 1,5 = 5,5."},
                {"jaut": "Zupa (€)?", "atb": ["2"], "padoms": "3,5 − 1,5."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīcā cenas nav izliktas, bet zināma starpība un "
                      "kopsumma.",
            kapec="Viens vienādojums jau pasaka y - ievietošana ir dabiska."),

    Kopsavilkums([
        "Izsaku vienu nezināmo no viena vienādojuma.",
        "Ievietoju to otrā vienādojumā iekavās.",
        "Atrisinu un pārbaudu pāri.",
    ]),

    Majas([
        "Atrisini: x + y = 11, x − y = 3; y = 4x, 3x + y = 21.",
        "Atrisini: 5x − y = 7, 2x + 3y = 13.",
        "Pārbaudi atbildes abos vienādojumos.",
    ]),
]
