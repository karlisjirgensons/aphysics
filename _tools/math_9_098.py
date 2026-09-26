# -*- coding: utf-8 -*-
"""9. klase, 98. stunda: «Kā pierakstīt atrisinājumu kopu?»

Trīs pieraksti vienai atbildei: nevienādība (x < −2 vai x > 3), intervāli
(x ∈ (−∞; −2) ∪ (3; +∞)) un svītrojums uz skaitļu taisnes. Eksāmena 8. un
10. uzdevums prasa tieši šos pierakstus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis, taisne)

TEMA = "Kā pierakstīt atrisinājumu kopu?"

MERKIS = ("Pierakstīsim atrisinājumu kopu ar nevienādību un attēlosim to uz "
          "skaitļu taisnes.")

SATURS = [
    Sakums("Viena atbilde - trīs pieraksti",
           zimejums=taisne(-5, 6, 1, atzimes=[(-2, "−2"), (3, "3")],
                           intervali=[(None, -2, False, False),
                                      (3, None, False, False)]),
           paraksts="x < −2 vai x > 3  ⇔  x ∈ (−∞; −2) ∪ (3; +∞)",
           fakti=["Apaļā iekava - galapunkts nepieder («izdurts» punkts).",
                  "Kvadrātiekava - pieder (pilns punkts).",
                  "∪ - apvienojums: «vai»."]),

    Doma("Intervālu pieraksts",
         "Intervālā raksta mazāko galu, semikolu, lielāko galu; ±∞ vienmēr ar "
         "apaļo iekavu.",
         soli=[
             "a < x < b ⇔ x ∈ (a; b).",
             "a ≤ x ≤ b ⇔ x ∈ [a; b].",
             "x ≥ a ⇔ x ∈ [a; +∞); x < b ⇔ x ∈ (−∞; b).",
             "Divas daļas savieno ar ∪.",
         ]),

    Slidnis("No taisnes uz pierakstu", [
        {"v": "(−1; 4)", "teksts": "−1 < x < 4",
         "zim": taisne(-3, 6, 1, atzimes=[(-1, "−1"), (4, "4")],
                       intervali=[(-1, 4, False, False)])},
        {"v": "[−1; 4]", "teksts": "−1 ≤ x ≤ 4",
         "zim": taisne(-3, 6, 1, atzimes=[(-1, "−1"), (4, "4")],
                       intervali=[(-1, 4, True, True)])},
        {"v": "[2; +∞)", "teksts": "x ≥ 2",
         "zim": taisne(-3, 6, 1, atzimes=[(2, "2")],
                       intervali=[(2, None, True, False)])},
    ]),

    Paraugs("Eksāmens 2025, 10. uzdevums",
            uzd="Iezīmē uz skaitļu taisnes nevienādības 3x^2 + 16x − 12 ≥ 0 "
                "atrisinājumu.",
            soli=[
                ("D = 256 + 144 = 400; x = {−16 ± 20|6}", "Nulles."),
                ("x_1 = −6, x_2 = {2|3}", "Nulles pieder (≥)."),
                ("Zari augšup: x ≤ −6 vai x ≥ {2|3}", "Virs ass - malās."),
            ],
            atbilde="x ∈ (−∞; −6] ∪ [{2|3}; +∞)"),

    Varianti("Kurš pieraksts?", [
        {"jaut": "−3 ≤ x < 5",
         "opcijas": ["[−3; 5)", "(−3; 5]", "[−3; 5]", "(−3; 5)"],
         "pareizi": 0, "padoms": "−3 pieder, 5 ne."},
        {"jaut": "x > 7",
         "opcijas": ["(7; +∞)", "[7; +∞)", "(−∞; 7)", "(7; +∞]"],
         "pareizi": 0, "padoms": "7 nepieder, ∞ - apaļā."},
        {"jaut": "x ≤ 0 vai x ≥ 2",
         "opcijas": ["(−∞; 0] ∪ [2; +∞)", "[0; 2]", "(0; 2)",
                     "(−∞; 0) ∪ (2; +∞)"],
         "pareizi": 0, "padoms": "Abas malas, galapunkti pieder."},
        {"jaut": "Eksāmens: sistēmas atrisinājums 1 < x < 3 intervālā",
         "opcijas": ["(1; 3)", "[1; 3]", "(1; 3]", "(3; 1)"],
         "pareizi": 0, "padoms": "Stingras nevienādības."},
    ]),

    Ievadi("Veselie skaitļi kopā", [
        {"jaut": "Cik veselu skaitļu ir intervālā [−2; 3]?", "atb": ["6"],
         "padoms": "−2, −1, 0, 1, 2, 3."},
        {"jaut": "Cik veselu skaitļu ir (−2; 3)?", "atb": ["4"],
         "padoms": "Bez galiem."},
        {"jaut": "Mazākais veselais skaitlis kopā [2,5; +∞)?", "atb": ["3"],
         "padoms": "2,5 < 3."},
    ]),

    Pasaule("Temperatūras norma",
            Ievadi("", [
                {"jaut": "Ledusskapī jābūt 2 °C ≤ T ≤ 6 °C. Intervāls [2; ?]",
                 "atb": ["6"], "padoms": "Lielākais gals."},
                {"jaut": "Termometrs rāda 6,5 °C. Par cik grādiem tas "
                         "pārsniedz normu?", "atb": ["0,5"],
                 "padoms": "6,5 − 6."},
            ]),
            pavediens="virtuve",
            konteksts="Produktu glabāšanas normas raksta tieši kā intervālus.",
            kapec="Iekava pasaka, vai robeža vēl ir atļauta.",
            zimejums=restis([["produkts", "T, °C"], ["piens", "[2; 6]"],
                             ["saldējums", "(−∞; −18]"]])),

    Kopsavilkums([
        "Pierakstu atbildi ar nevienādību un intervāliem.",
        "Attēloju to uz skaitļu taisnes.",
        "Pareizi lietoju apaļās un kvadrātiekavas.",
    ]),

    Majas([
        "Pieraksti intervālos: x ≤ −1; 0 < x ≤ 5; x < 2 vai x > 8.",
        "Atrisini x^2 − 7x + 10 ≤ 0 un iezīmē uz taisnes.",
        "Atrodi produktu uz iepakojuma ar glabāšanas temperatūru.",
    ]),
]
