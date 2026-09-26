# -*- coding: utf-8 -*-
"""9. klase, 74. stunda: «Ko nozīmē, ka reizinājums ir nulle?»

Galvenā vienādojumu risināšanas ideja līdz pat gada beigām: a · b = 0 tikai
tad, ja a = 0 vai b = 0. Tāpēc vienādojumu ar «= 0» sadala reizinātājos un
katru reizinātāju pielīdzina nullei.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis, saknes)

TEMA = "Ko nozīmē, ka reizinājums ir nulle?"

MERKIS = ("Secināsim, ka reizinājums ir nulle tikai tad, ja kāds "
          "reizinātājs ir nulle.")

SATURS = [
    Sakums("Divi skaitļi, reizinājums 0. Ko var teikt?",
           zimejums=restis([["a", "b", "a · b"], ["0", "7", "0"],
                            ["−3", "0", "0"], ["2", "5", "10"]]),
           paraksts="Nulle rodas tikai tad, ja kāds reizinātājs ir 0.",
           fakti=["a · b = 0 ⇔ a = 0 vai b = 0.",
                  "Vārds «vai»: var būt arī abi.",
                  "Ar summu tā nestrādā: a + b = 0 neko nepasaka."]),

    Doma("Reizinājums nulle",
         "Reizinājums ir nulle tad un tikai tad, ja vismaz viens reizinātājs "
         "ir nulle.",
         soli=[
             "Vienādojuma labajā pusē jābūt 0.",
             "Kreisā puse - reizinājums.",
             "Katru reizinātāju pielīdzina 0 un atrisina.",
             "Atbildē - visas saknes.",
         ],
         pieze="(x − 2)(x + 5) = 3 šādi risināt NEDRĪKST: 3 nav 0."),

    Paraugs("Divas saknes",
            uzd="Atrisini (x − 2)(x + 5) = 0.",
            soli=[
                ("x − 2 = 0 vai x + 5 = 0", "Reizinājums ir 0."),
                ("x = 2 vai x = −5", "Katrs vienādojums."),
                ("Pārbaude: 0 · 7 = 0; (−7) · 0 = 0", "Abas der."),
            ],
            atbilde="x_1 = −5, x_2 = 2"),

    Ievadi("Atrisini (atbildē saknes ar «;»)", [
        {"jaut": "(x − 4)(x − 1) = 0", "atb": saknes("1", "4"),
         "tastatura": "text", "vieta": "x₁; x₂", "padoms": "x − 4 = 0 vai "
                                                             "x − 1 = 0."},
        {"jaut": "x(x + 6) = 0", "atb": saknes("−6", "0"),
         "tastatura": "text", "vieta": "x₁; x₂", "padoms": "x = 0 vai "
                                                             "x + 6 = 0."},
        {"jaut": "(2x − 6)(x + 1) = 0", "atb": saknes("−1", "3"),
         "tastatura": "text", "vieta": "x₁; x₂", "padoms": "2x = 6."},
        {"jaut": "(x + 3)^2 = 0", "atb": ["−3", "-3"],
         "padoms": "Viena sakne."},
        {"jaut": "5(x − 7) = 0", "atb": ["7"], "padoms": "5 ≠ 0."},
    ], pamats=3),

    Varianti("Drīkst vai nedrīkst?", [
        {"jaut": "(x − 1)(x − 2) = 6 ⇒ x − 1 = 6 vai x − 2 = 6",
         "opcijas": ["Nedrīkst - labajā pusē nav 0", "Drīkst",
                     "Drīkst, ja x > 0", "Drīkst ar 6 = 2 · 3"],
         "pareizi": 0, "padoms": "Tikai ar nulli."},
        {"jaut": "x(x − 3) = 0. Skolēns: «x = 3». Kas trūkst?",
         "opcijas": ["Sakne x = 0", "Nekas", "Sakne x = −3",
                     "Sakne x = 1"],
         "pareizi": 0, "padoms": "Arī x = 0."},
    ]),

    Pasaule("Lēciens ar bumbu",
            Ievadi("", [
                {"jaut": "Bumbas augstums h = t(20 − 5t) m pēc t sekundēm. "
                         "Kad h = 0? (atbildē abi laiki)",
                 "atb": saknes("0", "4"), "tastatura": "text",
                 "vieta": "t₁; t₂", "padoms": "t = 0 vai 20 − 5t = 0."},
                {"jaut": "Cik sekundes bumba ir gaisā?", "atb": ["4"],
                 "padoms": "No 0 līdz 4."},
            ]),
            pavediens="sports",
            konteksts="Uzmesta bumba ir zemē divreiz: kad to met un kad tā "
                      "nokrīt.",
            kapec="Katrs reizinātājs = 0 dod vienu no šiem brīžiem."),

    Kopsavilkums([
        "Zinu: a · b = 0 ⇔ a = 0 vai b = 0.",
        "Atrisinu vienādojumu, kas ir reizinājums = 0.",
        "Nepazaudēju sakni x = 0.",
    ]),

    Majas([
        "Atrisini: (x + 8)(3x − 12) = 0; x(2x + 5) = 0.",
        "Paskaidro, kāpēc (x − 1)(x − 2) = 2 nedod x = 3.",
        "Izdomā vienādojumu ar saknēm −2 un 7.",
    ]),
]
