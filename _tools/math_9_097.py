# -*- coding: utf-8 -*-
"""9. klase, 97. stunda: «Kā atrisināt kvadrātnevienādību?»

Metode ar grafika skici: atrod nulles, uzskicē parabolu (tikai zaru
virziens un nulles), nolasa, kur grafiks ir virs (> 0) vai zem (< 0) x
ass. Tabula un zīmju metode nav vajadzīga.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, parabola, taisne)

TEMA = "Kā atrisināt kvadrātnevienādību?"

MERKIS = ("Atrisināsim kvadrātnevienādību, izmantojot funkcijas grafika "
          "skici.")

SATURS = [
    Sakums("Kur x² − x − 6 ir pozitīvs?",
           zimejums=parabola(1, -1, -6, -4, 5, -7, 7,
                             punkti=[(-2, 0, "−2"), (3, 0, "3")]),
           paraksts="Virs x ass: pa kreisi no −2 un pa labi no 3.",
           fakti=["x^2 − x − 6 > 0 ⇔ grafiks virs x ass.",
                  "Atbilde: x < −2 vai x > 3.",
                  "Starp nullēm grafiks ir zem ass (< 0)."]),

    Doma("Grafika metode",
         "Atrodi nulles, uzskicē parabolu un nolasi, kur tā ir virs vai zem "
         "x ass.",
         soli=[
             "Pārveido tā, lai labajā pusē būtu 0.",
             "Atrisini ax^2 + bx + c = 0 - nulles.",
             "Skice: zaru virziens (a) un nulles uz ass.",
             "> 0 - kur grafiks virs ass; < 0 - kur zem.",
             "≥ vai ≤ - nulles pieder atbildei.",
         ]),

    Slidnis("Trīs nevienādības, vienas nulles", [
        {"v": "> 0", "teksts": "x < −2 vai x > 3",
         "zim": taisne(-5, 6, 1, atzimes=[(-2, "−2"), (3, "3")],
                       intervali=[(None, -2, False, False),
                                  (3, None, False, False)])},
        {"v": "< 0", "teksts": "−2 < x < 3",
         "zim": taisne(-5, 6, 1, atzimes=[(-2, "−2"), (3, "3")],
                       intervali=[(-2, 3, False, False)])},
        {"v": "≥ 0", "teksts": "x ≤ −2 vai x ≥ 3 (nulles pieder)",
         "zim": taisne(-5, 6, 1, atzimes=[(-2, "−2"), (3, "3")],
                       intervali=[(None, -2, False, True),
                                  (3, None, True, False)])},
    ]),

    Paraugs("Zari lejup",
            uzd="Atrisini −x^2 + 4x > 0.",
            soli=[
                ("−x^2 + 4x = 0 ⇒ x = 0 vai x = 4", "Nulles."),
                ("a = −1 < 0 - zari lejup", "Skice: kalniņš."),
                ("Virs ass - starp nullēm", "Nolasa."),
            ],
            atbilde="0 < x < 4"),

    Varianti("Nolasi atbildi", [
        {"jaut": "x^2 − 9 < 0",
         "opcijas": ["−3 < x < 3", "x < −3 vai x > 3", "x < 3", "x > −3"],
         "pareizi": 0, "padoms": "Zari augšup, zem ass - vidū."},
        {"jaut": "x^2 − 4x ≥ 0",
         "opcijas": ["x ≤ 0 vai x ≥ 4", "0 ≤ x ≤ 4", "x ≥ 4",
                     "x < 0 vai x > 4"],
         "pareizi": 0, "padoms": "Nulles 0 un 4 pieder."},
        {"jaut": "x^2 + 1 > 0",
         "opcijas": ["jebkurš x", "nav atrisinājuma", "x > −1", "x > 1"],
         "pareizi": 0, "padoms": "Visa parabola virs ass."},
        {"jaut": "x^2 + 1 < 0",
         "opcijas": ["nav atrisinājuma", "jebkurš x", "x < −1", "−1 < x < 1"],
         "pareizi": 0, "padoms": "Grafiks nekad zem ass."},
    ]),

    Ievadi("Atrodi galapunktus", [
        {"jaut": "x^2 − 5x + 4 < 0: a < x < b. a = ?", "atb": ["1"],
         "padoms": "Nulles 1 un 4."},
        {"jaut": "Tai pašai b = ?", "atb": ["4"], "padoms": "Lielākā nulle."},
        {"jaut": "x^2 − 16 ≤ 0: lielākais atrisinājums?", "atb": ["4"],
         "padoms": "−4 ≤ x ≤ 4."},
        {"jaut": "−x^2 + 2x + 3 ≥ 0: mazākais atrisinājums?",
         "atb": ["−1", "-1"], "padoms": "Nulles −1 un 3, kalniņš."},
    ]),

    Pasaule("Kad bumba ir augstāk par 15 m?",
            Ievadi("", [
                {"jaut": "h = −5t^2 + 20t > 15 ⇒ t^2 − 4t + 3 < 0. No cik s?",
                 "atb": ["1"], "padoms": "Nulles 1 un 3."},
                {"jaut": "Līdz cik s?", "atb": ["3"], "padoms": "1 < t < 3."},
            ]),
            pavediens="sports",
            konteksts="Iepriekšējās stundas bumba: nevienādība atbild, CIK "
                      "ILGI tā ir augstāk par 15 m.",
            kapec="Vienādojums dod brīžus, nevienādība - laika intervālu."),

    Kopsavilkums([
        "Atrisinu kvadrātnevienādību ar grafika skici.",
        "Nolasu, kur grafiks virs vai zem ass.",
        "Ievēroju, vai nulles pieder atbildei.",
    ]),

    Majas([
        "Atrisini: x^2 − 3x − 10 > 0; 2x^2 − 8 ≤ 0.",
        "Uzzīmē atbildes uz skaitļu taisnes.",
        "Kāpēc x^2 ≥ 0 der jebkuram x?",
    ]),
]
