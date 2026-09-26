# -*- coding: utf-8 -*-
"""9. klase, 88. stunda: «Kad saknes ir iracionālas?»

Ja D nav pilns kvadrāts, saknes ir iracionālas: x^2 − 4x + 1 = 0 dod
2 ± √3. Precīza atbilde ar sakni, tuvināta - ar kalkulatoru. Eksāmenā
jāseko norādei, ko prasa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, parabola, saknes)

TEMA = "Kad saknes ir iracionālas?"

MERKIS = ("Pierakstīsim saknes ar kvadrātsakni un noteiksim to aptuveno "
          "vērtību.")

_T = "text"

SATURS = [
    Sakums("x² − 4x + 1 = 0: saknes nav veseli skaitļi",
           zimejums=parabola(1, -4, 1, -1, 5, -4, 6,
                             punkti=[(0.268, 0, "≈ 0,27"),
                                     (3.732, 0, "≈ 3,73")]),
           paraksts="Krustpunkti starp iedaļām - iracionāli skaitļi.",
           fakti=["D = 16 − 4 = 12 - nav pilns kvadrāts.",
                  "x_{1;2} = {4 ± √12|2} = 2 ± √3.",
                  "2 + √3 ≈ 3,73; 2 − √3 ≈ 0,27."]),

    Doma("Iracionālas saknes",
         "Ja D > 0 nav pilns kvadrāts, saknes pieraksta ar √ un vienkāršo.",
         soli=[
             "Iznes reizinātāju no saknes: √12 = √(4 · 3) = 2√3.",
             "Saīsini daļu: {4 ± 2√3|2} = 2 ± √3.",
             "Precīza atbilde: 2 ± √3.",
             "Tuvinātā: kalkulators, noapaļo kā prasīts.",
         ]),

    Paraugs("Vienkāršošana",
            uzd="Atrisini x^2 + 6x + 4 = 0.",
            soli=[
                ("D = 36 − 16 = 20", "Diskriminants."),
                ("√20 = 2√5", "Iznes 4."),
                ("x_{1;2} = {−6 ± 2√5|2} = −3 ± √5", "Saīsina ar 2."),
                ("x_1 ≈ −0,76; x_2 ≈ −5,24", "√5 ≈ 2,236."),
            ],
            atbilde="−3 ± √5"),

    Ievadi("Tuvinātas saknes (līdz simtdaļām)", [
        {"jaut": "x^2 − 2 = 0", "atb": saknes("−1,41", "1,41"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "±√2."},
        {"jaut": "x^2 − 2x − 1 = 0", "atb": saknes("−0,41", "2,41"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "1 ± √2."},
        {"jaut": "x^2 + 4x + 1 = 0", "atb": saknes("−3,73", "−0,27"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "−2 ± √3."},
    ]),

    Varianti("Precīzā atbilde", [
        {"jaut": "x^2 − 6x + 7 = 0",
         "opcijas": ["3 ± √2", "6 ± √8", "3 ± √8", "−3 ± √2"],
         "pareizi": 0, "padoms": "D = 8; {6 ± 2√2|2}."},
        {"jaut": "{10 ± √20|2} = ?",
         "opcijas": ["5 ± √5", "5 ± √10", "5 ± 10", "10 ± √5"],
         "pareizi": 0, "padoms": "√20 = 2√5."},
        {"jaut": "Kura D vērtība dod racionālas saknes?",
         "opcijas": ["D = 49", "D = 20", "D = 2", "D = 50"],
         "pareizi": 0, "padoms": "Pilns kvadrāts."},
    ]),

    Pasaule("Zelta taisnstūris",
            Ievadi("", [
                {"jaut": "Zelta proporcija φ ir x^2 − x − 1 = 0 pozitīvā sakne "
                         "{1 + √5|2}. φ ≈ ? (līdz tūkstošdaļām)",
                 "atb": ["1,618"], "padoms": "(1 + 2,236) : 2."},
                {"jaut": "Kartiņa 10 cm plata. Cik cm garai jābūt, lai "
                         "attiecība būtu φ? (līdz desmitdaļām)",
                 "atb": ["16,2"], "padoms": "10 · 1,618."},
            ]),
            pavediens="dati",
            konteksts="Daudzu logo un ekrānu proporcijās dizaineri lieto zelta "
                      "griezumu.",
            kapec="Iracionāla sakne - un tomēr ļoti praktiska."),

    Kopsavilkums([
        "Pierakstu iracionālas saknes ar √.",
        "Vienkāršoju: iznesu no saknes un saīsinu.",
        "Aprēķinu tuvinātas vērtības.",
    ]),

    Majas([
        "Atrisini precīzi: x^2 − 10x + 18 = 0.",
        "Aprēķini tuvināti līdz desmitdaļām.",
        "Izmēri bankas karti: vai tās malas ir tuvu zelta attiecībai?",
    ]),
]
