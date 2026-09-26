# -*- coding: utf-8 -*-
"""8. klase, 55. stunda: «Kā atrisināt vienādojumu ar kvadrātu?»

x^2 = 49 ir divas saknes: 7 un −7. Aritmētiskā sakne dod tikai vienu, tāpēc
atbildē raksta ±√a. Sakņu skaits atkarīgs no labās puses zīmes: divas,
viena vai neviena. Parabola to parāda - grafiku izmantos vēlāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, plakne)

TEMA = "Kā atrisināt vienādojumu ar kvadrātu?"

MERKIS = ("Atrisināsim vienādojumu, kurā nezināmais ir kvadrātā, un "
          "pamatosim abas saknes.")

_PARABOLA = [(x / 4.0, x * x / 16.0) for x in range(-12, 13)]


def _y(c, uzr):
    return plakne(grafiki=[(_PARABOLA, "y = x²"), (0, c, uzr)],
                  no_x=-4, lidz_x=4, no_y=-2, lidz_y=9, solis=1)


SATURS = [
    Sakums("x² = 49 - cik atrisinājumu?",
           zimejums=_y(4, "y = 4"),
           paraksts="Taisne y = 4 krusto parabolu divos punktos: x = −2 un "
                    "x = 2.",
           fakti=["7² = 49 un arī (−7)² = 49.",
                  "Tātad x = 7 vai x = −7.",
                  "Pieraksta: x = ±7."]),

    Doma("Vienādojums x^2 = a",
         "Sakņu skaits atkarīgs no a zīmes.",
         soli=[
             "a > 0: divas saknes x = √a un x = −√a (x = ±√a).",
             "a = 0: viena sakne x = 0.",
             "a < 0: sakņu nav.",
             "Vispirms pārveido līdz x^2 = a: 3x^2 − 12 = 0 ⇒ x^2 = 4.",
         ],
         pieze="Iracionālas saknes atstāj ar √: x = ±√5. Tuvinājumu raksta "
               "tikai tad, ja to prasa."),

    Slidnis("Pārbīdi taisni y = a", [
        {"v": "a = 4", "teksts": "Divi krustpunkti: x = ±2",
         "zim": _y(4, "y = 4")},
        {"v": "a = 1", "teksts": "Divi krustpunkti: x = ±1",
         "zim": _y(1, "y = 1")},
        {"v": "a = 0", "teksts": "Viens: x = 0", "zim": _y(0, "")},
        {"v": "a = −1", "teksts": "Neviena - taisne zem parabolas",
         "zim": _y(-1, "y = −1")},
    ]),

    Paraugs("Pārveido un atrisini",
            uzd="Atrisini 2x^2 − 50 = 0 un (x − 1)^2 = 9.",
            soli=[
                ("2x^2 = 50 ⇒ x^2 = 25", "Pārnes un dala."),
                ("x = ±5", "Divas saknes."),
                ("x − 1 = 3 vai x − 1 = −3", "Iekava kvadrātā - arī ±."),
                ("x = 4 vai x = −2", "Pārbaude: 3^2 = 9, (−3)^2 = 9."),
            ],
            atbilde="±5; 4 un −2"),

    Ievadi("Atrisini (ieraksti pozitīvo sakni vai sakņu skaitu)", [
        {"jaut": "x^2 = 81. Pozitīvā sakne?", "atb": ["9"],
         "padoms": "x = ±9."},
        {"jaut": "x^2 = 0,36. Negatīvā sakne?", "atb": ["−0,6", "-0,6",
                                                        "-0.6"],
         "padoms": "±0,6."},
        {"jaut": "x^2 + 16 = 0. Cik sakņu?", "atb": ["0"],
         "padoms": "x^2 = −16."},
        {"jaut": "5x^2 = 45. Pozitīvā sakne?", "atb": ["3"],
         "padoms": "x^2 = 9."},
        {"jaut": "(x + 2)^2 = 16. Lielākā sakne?", "atb": ["2"],
         "padoms": "x + 2 = ±4."},
        {"jaut": "x^2 = 7. Pozitīvā sakne līdz simtdaļām?",
         "atb": ["2,65", "2.65"], "padoms": "√7 ≈ 2,646."},
    ], pamats=4),

    Varianti("Kurš atrisinājums pareizs?", [
        {"jaut": "x^2 = 64",
         "opcijas": ["x = ±8", "x = 8", "x = 32", "x = ±32"],
         "pareizi": 0, "padoms": "Arī (−8)^2 = 64."},
        {"jaut": "x^2 = −25",
         "opcijas": ["Sakņu nav", "x = ±5", "x = −5", "x = 5"],
         "pareizi": 0, "padoms": "Kvadrāts nav negatīvs."},
        {"jaut": "x^2 = 3",
         "opcijas": ["x = ±√3", "x = √3", "x = ±1,5", "x = ±9"],
         "pareizi": 0, "padoms": "Precīzi ar sakni."},
    ]),

    Pasaule("Krītošs akmens",
            Ievadi("", [
                {"jaut": "Akmens krīt s = 5t^2 metrus t sekundēs. No kāda "
                         "augstuma tas krīt 3 s? (m)",
                 "atb": ["45"], "padoms": "5 · 9."},
                {"jaut": "No 80 m tilta - cik sekundes krīt? (5t^2 = 80)",
                 "atb": ["4"], "padoms": "t^2 = 16; t > 0."},
                {"jaut": "Kāpēc atmet t = −4?",
                 "atb": ["laiks", "laiks nav negatīvs", "laiks nevar būt "
                         "negatīvs"],
                 "padoms": "Ieraksti vārdu «laiks».", "tastatura": "text"},
            ]),
            pavediens="daba",
            konteksts="Brīvā kritienā ceļš aug ar laika kvadrātu (g ≈ 10 m/s², "
                      "tāpēc 5t^2).",
            kapec="Vienādojumam ir divas saknes, bet situācijai der viena."),

    Kopsavilkums([
        "Atrisinu x^2 = a un nosaku sakņu skaitu.",
        "Pierakstu atbildi ar ±.",
        "Pārveidoju vienādojumu līdz x^2 = a.",
        "Izvēlos sakni, kas der situācijai.",
    ]),

    Majas([
        "Atrisini: x^2 = 121, 4x^2 = 1, x^2 + 9 = 0, (x − 3)^2 = 25.",
        "Aprēķini, cik ilgi krīt akmens no 20 m.",
        "Paskaidro, kāpēc x^2 = 0 ir tikai viena sakne.",
    ]),
]
