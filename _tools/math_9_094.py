# -*- coding: utf-8 -*-
"""9. klase, 94. stunda: «Kā uzzīmēt grafiku?»

Grafika zīmēšanas algoritms: zaru virziens → virsotne → nulles → krustpunkts
ar y asi → simetriskais punkts → gluda līnija. Slīdnis zīmē pa vienam
punktam, kā burtnīcā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, parabola, plakne, restis)

TEMA = "Kā uzzīmēt grafiku?"

MERKIS = ("Zīmēsim kvadrātfunkcijas grafiku, izmantojot virsotni, nulles un "
          "simetriju.")

_PLAKNE = dict(no_x=-2, lidz_x=6, no_y=-6, lidz_y=6, solis_y=2)
_VIRSOTNE = (2, -4, "V(2; −4)")
_NULLES = [(0, 0, "0"), (4, 0, "4")]
_SIMETRISKIE = [(-1, 5, "(−1; 5)"), (5, 5, "(5; 5)")]

SATURS = [
    Sakums("y = x² − 4x - bez gariem aprēķiniem",
           zimejums=parabola(1, -4, 0, punkti=[_VIRSOTNE] + _NULLES,
                             **_PLAKNE),
           paraksts="Pieci raksturīgi punkti - un grafiks gatavs.",
           fakti=["a > 0 - zari uz augšu.",
                  "Virsotne (2; −4), nulles 0 un 4.",
                  "Simetrija dod punktus bez rēķināšanas."]),

    Slidnis("Zīmējam pa soļiem", [
        {"v": "Virsotne", "teksts": "x_v = 2, y_v = −4",
         "zim": plakne(punkti=[_VIRSOTNE], **_PLAKNE)},
        {"v": "Nulles", "teksts": "x(x − 4) = 0 ⇒ 0 un 4",
         "zim": plakne(punkti=[_VIRSOTNE] + _NULLES, **_PLAKNE)},
        {"v": "Vēl punkti", "teksts": "y(−1) = 5; simetriski y(5) = 5",
         "zim": plakne(punkti=[_VIRSOTNE] + _NULLES + _SIMETRISKIE,
                       **_PLAKNE)},
        {"v": "Līkne", "teksts": "Savieno ar gludu līniju (ne lauztu!)",
         "zim": parabola(1, -4, 0, punkti=[_VIRSOTNE] + _NULLES +
                         _SIMETRISKIE, **_PLAKNE)},
    ]),

    Doma("Algoritms",
         "Zaru virziens (a) → virsotne → nulles → krustpunkts ar y asi → "
         "simetriskie punkti → gluda līnija.",
         soli=[
             "a > 0 - zari augšup, a < 0 - lejup.",
             "Virsotne: x_v = −{b|2a}, y_v - ievietojot.",
             "Nulles: ax^2 + bx + c = 0 (ja ir).",
             "Punkts (0; c) un tā simetriskais pret x = x_v.",
             "Ja vajag - tabula ar vēl 2 punktiem.",
         ]),

    Ievadi("Sagatavo zīmējumu y = −x^2 + 2x + 3", [
        {"jaut": "a = ? (tas nosaka zaru virzienu)", "atb": ["−1", "-1"],
         "padoms": "a = −1."},
        {"jaut": "x_v = ?", "atb": ["1"], "padoms": "−{2|−2}."},
        {"jaut": "y_v = ?", "atb": ["4"], "padoms": "−1 + 2 + 3."},
        {"jaut": "Krustpunkts ar y asi: y = ?", "atb": ["3"],
         "padoms": "c."},
        {"jaut": "Simetriskais punktam (0; 3) ir (?; 3)", "atb": ["2"],
         "padoms": "Ass x = 1."},
    ], pamats=5),

    Varianti("Kurš grafiks?", [
        {"jaut": "y = −x^2 + 4",
         "opcijas": ["Zari lejup, virsotne (0; 4)",
                     "Zari augšup, virsotne (0; 4)",
                     "Zari lejup, virsotne (4; 0)",
                     "Taisne"],
         "pareizi": 0, "padoms": "a = −1."},
        {"jaut": "Eksāmens: kurā zīmējumā ir y = x^2 skice?",
         "opcijas": ["Zari augšup, virsotne (0; 0)",
                     "Zari lejup, virsotne (0; 0)",
                     "Zari augšup, virsotne (0; 1)",
                     "Taisne caur (0; 0)"],
         "pareizi": 0, "padoms": "a = 1, b = c = 0."},
    ]),

    Pasaule("Lēciens tālumā",
            Ievadi("", [
                {"jaut": "Sportista masas centra augstums h = −0,5x^2 + 2x + 1 "
                         "(m), x - attālums. Cik m augsts ir lēciena augstākais "
                         "punkts?", "atb": ["3"], "padoms": "x_v = 2; "
                                                         "−2 + 4 + 1."},
                {"jaut": "Kur tas ir (x_v, m)?", "atb": ["2"],
                 "padoms": "−{2|−1}."},
            ]),
            pavediens="sports",
            konteksts="Treneris video pārvērš lēcienu grafikā un meklē "
                      "augstāko punktu.",
            kapec="Grafiks parāda visu lēcienu vienā skatā.",
            zimejums=restis([["x", "0", "1", "2", "3", "4"],
                             ["h", "1", "2,5", "3", "2,5", "1"]])),

    Kopsavilkums([
        "Zīmēju parabolu pēc algoritma.",
        "Izmantoju simetriju punktu atrašanai.",
        "Savienoju punktus ar gludu līkni.",
    ]),

    Majas([
        "Uzzīmē y = x^2 − 2x − 3 burtnīcā pēc algoritma.",
        "Uzzīmē y = −x^2 + 4x.",
        "Pārbaudi zīmējumu ar tiešsaistes grafiku rīku.",
    ]),
]
