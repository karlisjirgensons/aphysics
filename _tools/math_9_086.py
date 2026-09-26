# -*- coding: utf-8 -*-
"""9. klase, 86. stunda: «Kas ir diskriminants?»

D = b^2 − 4ac «izšķir» (lat. discriminare) sakņu skaitu: D > 0 - divas,
D = 0 - viena, D < 0 - nav. Tas ir tas pats, ko 82. stundā redzēja
grafikā, tikai tagad bez zīmēšanas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, parabola, restis)

TEMA = "Kas ir diskriminants?"

MERKIS = ("Aprēķināsim diskriminantu un noteiksim sakņu skaitu pēc tā "
          "vērtības.")

SATURS = [
    Sakums("Cik sakņu - bez zīmēšanas?",
           zimejums=restis([["D", "saknes", "parabola"],
                            ["D > 0", "2", "krusto x asi"],
                            ["D = 0", "1", "pieskaras"],
                            ["D < 0", "0", "nesasniedz"]]),
           paraksts="D = b² − 4ac - viens skaitlis pasaka visu.",
           fakti=["Diskriminants - no latīņu «izšķirt».",
                  "Tas ir eksāmena formulu lapā.",
                  "Vispirms D - tad saknes."]),

    Doma("Diskriminants",
         "Kvadrātvienādojuma ax^2 + bx + c = 0 diskriminants ir "
         "D = b^2 − 4ac.",
         soli=[
             "Nosaki a, b, c (ar zīmēm!).",
             "b^2 vienmēr ≥ 0: (−5)^2 = 25.",
             "−4ac: uzmanies ar zīmēm.",
             "D > 0 - 2 saknes; D = 0 - 1; D < 0 - nav reālu sakņu.",
         ]),

    Slidnis("Trīs vienādojumi", [
        {"v": "D = 16", "teksts": "x^2 − 2x − 3 = 0: D = 4 + 12 = 16 > 0",
         "zim": parabola(1, -2, -3, -3, 5, -5, 6)},
        {"v": "D = 0", "teksts": "x^2 − 2x + 1 = 0: D = 4 − 4 = 0",
         "zim": parabola(1, -2, 1, -3, 5, -5, 6)},
        {"v": "D = −8", "teksts": "x^2 − 2x + 3 = 0: D = 4 − 12 = −8 < 0",
         "zim": parabola(1, -2, 3, -3, 5, -5, 6)},
    ]),

    Paraugs("Eksāmens 2025: 2x^2 + 7x − 4 = 0",
            uzd="Aprēķini diskriminantu un nosaki sakņu skaitu.",
            soli=[
                ("a = 2, b = 7, c = −4", "Koeficienti."),
                ("D = 7^2 − 4 · 2 · (−4) = 49 + 32 = 81", "−4 · 2 · (−4) = +32."),
                ("D > 0", "Divas saknes."),
            ],
            atbilde="D = 81, divas saknes"),

    Ievadi("Aprēķini D", [
        {"jaut": "x^2 − 5x + 6 = 0. D = ?", "atb": ["1"],
         "padoms": "25 − 24."},
        {"jaut": "x^2 + 4x + 4 = 0. D = ?", "atb": ["0"],
         "padoms": "16 − 16."},
        {"jaut": "3x^2 − x + 2 = 0. D = ?", "atb": ["−23", "-23"],
         "padoms": "1 − 24."},
        {"jaut": "2x^2 + 3x − 5 = 0. D = ?", "atb": ["49"],
         "padoms": "9 + 40."},
        {"jaut": "−x^2 + 6x − 9 = 0. D = ?", "atb": ["0"],
         "padoms": "36 − 4 · (−1) · (−9)."},
        {"jaut": "x^2 − 7 = 0. D = ?", "atb": ["28"],
         "padoms": "0 − 4 · 1 · (−7)."},
    ], pamats=4),

    Varianti("Cik sakņu?", [
        {"jaut": "D = 25", "opcijas": ["2", "1", "0", "25"],
         "pareizi": 0, "padoms": "D > 0."},
        {"jaut": "x^2 + x + 1 = 0",
         "opcijas": ["0 (D = −3)", "2", "1", "3"],
         "pareizi": 0, "padoms": "1 − 4."},
        {"jaut": "Ja a un c ir pretējām zīmēm, tad...",
         "opcijas": ["vienmēr 2 saknes", "vienmēr 0", "vienmēr 1",
                     "nevar zināt"],
         "pareizi": 0, "padoms": "−4ac > 0, tātad D > 0."},
    ]),

    Pasaule("Vai bumba sasniegs grozu?",
            Ievadi("", [
                {"jaut": "Bumbas augstums h = −5t^2 + 10t + 2 m. Vai tā "
                         "sasniedz 3,05 m? Vienādojums −5t^2 + 10t − 1,05 = 0. "
                         "D = ?", "atb": ["79"],
                 "padoms": "100 − 4 · (−5) · (−1,05) = 100 − 21."},
                {"jaut": "Vai 7 m augstumu? −5t^2 + 10t − 5 = 0. D = ?",
                 "atb": ["0"], "padoms": "100 − 100."},
                {"jaut": "Vai 8 m? −5t^2 + 10t − 6 = 0. D = ?",
                 "atb": ["−20", "-20"], "padoms": "100 − 120 < 0 - nesasniedz."},
            ]),
            pavediens="sports",
            konteksts="Basketbola grozs ir 3,05 m augstumā. Diskriminants "
                      "pasaka, vai bumba vispār tur nokļūst.",
            kapec="D < 0 nozīmē: tādā augstumā bumba nekad nebūs."),

    Kopsavilkums([
        "Aprēķinu D = b^2 − 4ac ar pareizām zīmēm.",
        "Nosaku sakņu skaitu pēc D.",
        "Saistu D ar parabolas un x ass krustpunktiem.",
    ]),

    Majas([
        "Aprēķini D: 4x^2 − 4x + 1 = 0; x^2 + 3x − 10 = 0.",
        "Pie kāda c vienādojumam x^2 + 6x + c = 0 ir viena sakne?",
        "Paskaidro, kāpēc ar a · c < 0 vienmēr ir divas saknes.",
    ]),
]
