# -*- coding: utf-8 -*-
"""9. klase, 90. stunda: «Kā atrisināt vienādojumu ar nezināmo saucējā?»

Daļveida vienādojums: vispirms aizliegtās vērtības (saucējs ≠ 0), tad
reizināšana ar kopsaucēju, tad kvadrātvienādojums, un beigās - lieko sakņu
izmešana. Klasiskais slazds: sakne, kas padara saucēju par nulli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, saknes)

TEMA = "Kā atrisināt vienādojumu ar nezināmo saucējā?"

MERKIS = ("Atrisināsim vienādojumu ar nezināmo saucējā un pārbaudīsim "
          "atrisinājuma pieļaujamību.")

_T = "text"

SATURS = [
    Sakums("{x^2|x − 3} = {9|x − 3} - saknes ±3?",
           fakti=["x^2 = 9 ⇒ x = 3 vai x = −3.",
                  "Bet x = 3 dod saucēju 0 - dalīt ar nulli nedrīkst!",
                  "Vienīgā sakne: x = −3."]),

    Doma("Nezināmais saucējā",
         "Vispirms pieraksti, kuras x vērtības nav pieļaujamas; pēc "
         "atrisināšanas tās izmet.",
         soli=[
             "Saucējs ≠ 0: atrodi aizliegtās vērtības.",
             "Reizini ar kopsaucēju.",
             "Atrisini iegūto vienādojumu.",
             "Salīdzini saknes ar aizliegtajām; liekās izmet.",
         ]),

    Slidnis("Piemērs", [
        {"v": "Dots", "teksts": "{x|x − 2} = {8|x^2 − 4}"},
        {"v": "1", "teksts": "x ≠ 2 un x ≠ −2"},
        {"v": "2", "teksts": "· (x − 2)(x + 2): x(x + 2) = 8"},
        {"v": "3", "teksts": "x^2 + 2x − 8 = 0 ⇒ x = 2 vai x = −4"},
        {"v": "4", "teksts": "x = 2 ir aizliegta! Atbilde: x = −4"},
    ]),

    Paraugs("Divas daļas",
            uzd="Atrisini {6|x} + {6|x + 1} = 5.",
            soli=[
                ("x ≠ 0, x ≠ −1", "Aizliegtās vērtības."),
                ("6(x + 1) + 6x = 5x(x + 1)", "· x(x + 1)."),
                ("5x^2 − 7x − 6 = 0; D = 49 + 120 = 169", "Standartforma."),
                ("x = {7 ± 13|10}: x_1 = 2, x_2 = −0,6", "Abas pieļaujamas."),
            ],
            atbilde="−0,6; 2"),

    Ievadi("Atrisini", [
        {"jaut": "{x^2|x + 1} = {1|x + 1}", "atb": ["1"],
         "padoms": "x^2 = 1, bet x ≠ −1."},
        {"jaut": "{x + 4|x} = x", "atb": saknes("−1,56", "2,56"),
         "tastatura": _T, "vieta": "x₁; x₂",
         "padoms": "x^2 − x − 4 = 0; {1 ± √17|2}, līdz simtdaļām."},
        {"jaut": "{12|x} = x + 1", "atb": saknes("−4", "3"), "tastatura": _T,
         "vieta": "x₁; x₂", "padoms": "x^2 + x − 12 = 0."},
        {"jaut": "{x|x − 5} = {25|x^2 − 5x}", "atb": ["−5", "-5"],
         "padoms": "x^2 = 25; x ≠ 5, x ≠ 0."},
    ]),

    Varianti("Pieļaujama vai nē?", [
        {"jaut": "{3|x − 4} = ...: sakne x = 4",
         "opcijas": ["Nepieļaujama", "Pieļaujama"], "jaukt": False,
         "pareizi": 0, "padoms": "Saucējs 0."},
        {"jaut": "{1|x^2 + 1} = ...: sakne x = −1",
         "opcijas": ["Nepieļaujama", "Pieļaujama"], "jaukt": False,
         "pareizi": 1, "padoms": "x^2 + 1 = 2 ≠ 0."},
        {"jaut": "{x|x(x − 2)} = ...: sakne x = 0",
         "opcijas": ["Nepieļaujama", "Pieļaujama"], "jaukt": False,
         "pareizi": 0, "padoms": "x = 0 saucējā."},
    ]),

    Pasaule("Upes laiva",
            Ievadi("", [
                {"jaut": "Laiva 12 km pa straumi un 12 km pret straumi (2 km/h) "
                         "nobrauc 5 h. {12|v + 2} + {12|v − 2} = 5 ⇒ "
                         "5v^2 − 24v − 20 = 0. Pozitīvā sakne v = ? km/h",
                 "atb": ["5,52"], "padoms": "{24 + √976|10} ≈ 5,52."},
                {"jaut": "Kāpēc negatīvā sakne neder? Ieraksti tās "
                         "tuvinājumu (līdz simtdaļām).", "atb": ["−0,72",
                                                                "-0,72"],
                 "padoms": "{24 − 31,24|10}."},
            ]),
            pavediens="celojums",
            konteksts="Kustībā pa upi ātrums pa straumi ir v + 2, pret - v − 2; "
                      "laiks = ceļš : ātrums.",
            kapec="Ātrums v − 2 > 0, tāpēc v > 2 - tikai viena sakne der."),

    Kopsavilkums([
        "Pierakstu aizliegtās vērtības.",
        "Reizinu ar kopsaucēju un atrisinu.",
        "Izmetu saknes, kas padara saucēju par nulli.",
    ]),

    Majas([
        "Atrisini: {2|x − 1} + {1|x} = 1.",
        "Atrisini: {x^2 − 9|x + 3} = 0.",
        "Paskaidro, kāpēc sakne var «pazust» pēc pārbaudes.",
    ]),
]
