# -*- coding: utf-8 -*-
"""9. klase, 77. stunda: «Cik sakņu ir vienādojumam?»

Nepilnajiem kvadrātvienādojumiem sakņu skaitu var pateikt pirms
risināšanas: ax^2 + bx = 0 - vienmēr divas, ax^2 = 0 - viena, ax^2 + c = 0
- divas vai neviena atkarībā no zīmēm. Slīdnis to rāda ar parabolu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, likne, plakne, restis)


def _parabola(c, virsraksts):
    """y = x^2 + c un tās krustpunkti ar x asi."""
    return plakne(grafiki=[(likne(lambda x: x * x + c, -4, 4, -5, 6),
                            virsraksts)],
                  no_x=-4, lidz_x=4, no_y=-5, lidz_y=6)


TEMA = "Cik sakņu ir vienādojumam?"

MERKIS = ("Noteiksim nepilnā kvadrātvienādojuma sakņu skaitu un pamatosim "
          "to.")

SATURS = [
    Sakums("0, 1 vai 2 saknes?",
           zimejums=restis([["vienādojums", "saknes"],
                            ["x² − 4 = 0", "2"], ["x² = 0", "1"],
                            ["x² + 4 = 0", "0"]]),
           paraksts="Trīs līdzīgi vienādojumi - dažāds sakņu skaits.",
           fakti=["x^2 nekad nav negatīvs.",
                  "x^2 = pozitīvs → 2 saknes; x^2 = 0 → 1; x^2 = negatīvs → 0.",
                  "ax^2 + bx = 0 vienmēr ir 2 saknes (b ≠ 0)."]),

    Slidnis("Bīdi parabolu uz augšu", [
        {"v": "c = −4", "teksts": "x^2 − 4 = 0: krusto x asi divreiz → 2 "
                                  "saknes", "zim": _parabola(-4, "y = x² − 4")},
        {"v": "c = 0", "teksts": "x^2 = 0: pieskaras x asij → 1 sakne",
         "zim": _parabola(0, "y = x²")},
        {"v": "c = 2", "teksts": "x^2 + 2 = 0: nesasniedz x asi → 0 sakņu",
         "zim": _parabola(2, "y = x² + 2")},
    ]),

    Doma("Sakņu skaits",
         "ax^2 + c = 0 ⇒ x^2 = −{c|a}: ja −{c|a} > 0 - divas saknes, = 0 - "
         "viena, < 0 - neviena.",
         soli=[
             "Izsaki x^2 = skaitlis.",
             "Skaitlis pozitīvs → ±√skaitlis.",
             "Skaitlis 0 → x = 0.",
             "Skaitlis negatīvs → reālu sakņu nav.",
         ]),

    Varianti("Cik sakņu?", [
        {"jaut": "3x^2 − 12 = 0", "opcijas": ["2", "1", "0", "3"],
         "pareizi": 0, "padoms": "x^2 = 4."},
        {"jaut": "5x^2 + 20 = 0", "opcijas": ["0", "1", "2", "4"],
         "pareizi": 0, "padoms": "x^2 = −4."},
        {"jaut": "7x^2 = 0", "opcijas": ["1", "0", "2", "7"],
         "pareizi": 0, "padoms": "Tikai x = 0."},
        {"jaut": "x^2 + 9x = 0", "opcijas": ["2", "1", "0", "9"],
         "pareizi": 0, "padoms": "x(x + 9) = 0."},
        {"jaut": "−x^2 + 1 = 0", "opcijas": ["2", "0", "1", "Nevar zināt"],
         "pareizi": 0, "padoms": "x^2 = 1."},
    ], pamats=3),

    Ievadi("Atrodi c", [
        {"jaut": "x^2 + c = 0 ir tieši viena sakne. c = ?", "atb": ["0"],
         "padoms": "x^2 = 0."},
        {"jaut": "x^2 − c = 0 saknes ir ±6. c = ?", "atb": ["36"],
         "padoms": "6^2."},
        {"jaut": "2x^2 + c = 0 saknes ±3. c = ?", "atb": ["−18", "-18"],
         "padoms": "2 · 9 + c = 0."},
    ]),

    Pasaule("Kritiens no tilta",
            Ievadi("", [
                {"jaut": "Akmens krīt no 45 m: augstums h = 45 − 5t^2. Kad "
                         "h = 0? t = ? s (t > 0)", "atb": ["3"],
                 "padoms": "5t^2 = 45, t^2 = 9."},
                {"jaut": "Vienādojumam 45 − 5t^2 = 0 ir 2 saknes. Kura no tām "
                         "šeit neder? Ieraksti to.",
                 "atb": ["−3", "-3"], "padoms": "Laiks nav negatīvs."},
            ]),
            pavediens="tehnika",
            konteksts="Brīvā kritienā ceļš aug kā t^2 - tāpēc rodas "
                      "kvadrātvienādojums.",
            kapec="Matemātika dod 2 saknes, fizika izvēlas vienu."),

    Kopsavilkums([
        "Nosaku sakņu skaitu pirms risināšanas.",
        "Saistu sakņu skaitu ar parabolas krustpunktiem.",
        "Izvērtēju, kura sakne der situācijai.",
    ]),

    Majas([
        "Bez risināšanas nosaki sakņu skaitu: 4x^2 − 1 = 0; x^2 + 0,01 = 0.",
        "Izdomā vienādojumu ax^2 + c = 0 bez saknēm.",
        "Izmēri, cik ilgi krīt bumba no galda, un pārbaudi ar h = 5t^2.",
    ]),
]
