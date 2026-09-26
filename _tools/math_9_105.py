# -*- coding: utf-8 -*-
"""9. klase, 105. stunda: «Kā no vienādojuma iegūt funkciju?»

Izsakot y ar x, vienādojums 2x + y = 7 kļūst par lineāru funkciju
y = −2x + 7 - ar slīpumu un krustpunktu, ko pazīst no 8. klases. Tā ir
arī ievietošanas paņēmiena pirmā puse.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, plakne)

TEMA = "Kā no vienādojuma iegūt funkciju?"

MERKIS = ("Izteiksim vienu nezināmo ar otru un pierakstīsim atbilstošo "
          "funkciju.")

_T = "text"

SATURS = [
    Sakums("2x + y = 7 un y = −2x + 7 - viena taisne",
           zimejums=plakne(grafiki=[(-2, 7, "y = −2x + 7")],
                           punkti=[(0, 7, "(0; 7)"), (3, 1, "(3; 1)")],
                           no_x=-1, lidz_x=5, no_y=-2, lidz_y=8),
           paraksts="Funkcijas formā uzreiz redz slīpumu −2 un sākumu 7.",
           fakti=["Pārnes 2x: y = 7 − 2x.",
                  "k = −2 - slīpums, b = 7 - krustpunkts ar y asi.",
                  "Funkcijas formā vieglāk zīmēt un salīdzināt."]),

    Doma("Izsaki y",
         "No ax + by = c iegūst y = −{a|b}x + {c|b} (ja b ≠ 0).",
         soli=[
             "Atstāj y locekli vienā pusē, pārējo pārnes.",
             "Dali ar koeficientu pie y.",
             "Uzraksti formā y = kx + b.",
             "Pārbaudi ar vienu pāri.",
         ]),

    Paraugs("Ar dalīšanu",
            uzd="Izsaki y no 3x − 2y = 8.",
            soli=[
                ("−2y = −3x + 8", "Pārnes 3x."),
                ("y = 1,5x − 4", "Dala ar −2."),
                ("Pārbaude: x = 4 ⇒ y = 2; 12 − 4 = 8 ✔", "Pāris der."),
            ],
            atbilde="y = 1,5x − 4"),

    Ievadi("Izsaki y", [
        {"jaut": "x + y = 9 ⇒ y = ?", "atb": ["9 − x", "−x + 9"],
         "tastatura": _T, "padoms": "Pārnes x."},
        {"jaut": "4x + y = 3 ⇒ y = ?", "atb": ["3 − 4x", "−4x + 3"],
         "tastatura": _T, "padoms": "Pārnes 4x."},
        {"jaut": "2x + 2y = 10 ⇒ y = ?", "atb": ["5 − x", "−x + 5"],
         "tastatura": _T, "padoms": "Dala ar 2."},
        {"jaut": "x − y = 4 ⇒ y = ?", "atb": ["x − 4", "−4 + x"],
         "tastatura": _T, "padoms": "−y = 4 − x."},
        {"jaut": "6x + 3y = 12 ⇒ y = ?", "atb": ["4 − 2x", "−2x + 4"],
         "tastatura": _T, "padoms": "3y = 12 − 6x."},
    ], pamats=3),

    Varianti("Slīpums un krustpunkts", [
        {"jaut": "5x + y = 2. Slīpums k = ?",
         "opcijas": ["−5", "5", "2", "−2"],
         "pareizi": 0, "padoms": "y = −5x + 2."},
        {"jaut": "x + 4y = 8. Krustpunkts ar y asi?",
         "opcijas": ["(0; 2)", "(0; 8)", "(8; 0)", "(0; 4)"],
         "pareizi": 0, "padoms": "y = −0,25x + 2."},
        {"jaut": "Kuras divas taisnes ir paralēlas?",
         "opcijas": ["2x + y = 1 un 2x + y = 5", "x + y = 1 un x − y = 1",
                     "y = x un y = −x", "x = 2 un y = 2"],
         "pareizi": 0, "padoms": "Vienāds k = −2."},
    ]),

    Pasaule("Taksometra tarifs",
            Ievadi("", [
                {"jaut": "Brauciens maksā C € par x km: C − 0,8x = 2,5. Izsaki "
                         "C = ?", "atb": ["0,8x + 2,5", "2,5 + 0,8x"],
                 "tastatura": _T, "padoms": "Pārnes 0,8x."},
                {"jaut": "Cik € maksā 10 km?", "atb": ["10,5"],
                 "padoms": "8 + 2,5."},
                {"jaut": "Cik km var nobraukt par 18,5 €?", "atb": ["20"],
                 "padoms": "0,8x = 16."},
            ]),
            pavediens="celojums",
            konteksts="Taksometra cena = iekāpšanas maksa + cena par km.",
            kapec="Funkcijas forma uzreiz rāda maksu par km un sākuma cenu."),

    Kopsavilkums([
        "Izsaku y ar x no lineāra vienādojuma.",
        "Nolasu slīpumu un krustpunktu ar y asi.",
        "Salīdzinu taisnes pēc slīpuma.",
    ]),

    Majas([
        "Izsaki y: 5x − y = 3; 2x + 5y = 10.",
        "Izsaki x no x + 3y = 7.",
        "Atrodi savas pilsētas taksometra tarifu un uzraksti funkciju.",
    ]),
]
