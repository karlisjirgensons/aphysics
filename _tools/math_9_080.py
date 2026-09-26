# -*- coding: utf-8 -*-
"""9. klase, 80. stunda: «Kas ir kvadrātvienādojums?»

ax^2 + bx + c = 0, kur a ≠ 0. Stunda sākas ar strūklaku: ūdens strūkla ir
parabola, un jautājums «kur ūdens nokrīt?» ir kvadrātvienādojums. Skolēns
atpazīst vienādojumu un nosauc koeficientus a, b, c.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, parabola)

TEMA = "Kas ir kvadrātvienādojums?"

MERKIS = ("Noteiksim, vai vienādojums ir kvadrātvienādojums, un nosauksim "
          "tā koeficientus.")

SATURS = [
    Sakums("Kur strūklakas ūdens nokrīt zemē?",
           zimejums=parabola(-0.5, 2, 0, -1, 5, -1, 3,
                             punkti=[(0, 0, "0"), (4, 0, "4")]),
           paraksts="Strūkla: y = −0,5x² + 2x; zemē y = 0.",
           fakti=["−0,5x^2 + 2x = 0 - kvadrātvienādojums.",
                  "Ūdens izšaujas x = 0 un nokrīt x = 4 m.",
                  "Parabolas - strūklakas, tilti, basketbola metieni."]),

    Doma("Kvadrātvienādojums",
         "Vienādojumu ax^2 + bx + c = 0, kur a, b, c ir skaitļi un a ≠ 0, "
         "sauc par kvadrātvienādojumu.",
         soli=[
             "a - koeficients pie x^2 (nedrīkst būt 0).",
             "b - koeficients pie x; c - brīvais loceklis.",
             "Ja b = 0 vai c = 0 - nepilnais kvadrātvienādojums.",
             "Pirms nosauc a, b, c, pārveido uz «= 0» formu.",
         ],
         pieze="Ja a = 0, x^2 pazūd un vienādojums kļūst lineārs."),

    Varianti("Kvadrātvienādojums vai nē?", [
        {"jaut": "3x^2 − 5x + 2 = 0",
         "opcijas": ["Jā", "Nē, lineārs", "Nē, kubisks", "Nē, nav x"],
         "pareizi": 0, "padoms": "Augstākā pakāpe 2."},
        {"jaut": "5x − 7 = 0",
         "opcijas": ["Nē, lineārs", "Jā", "Jā, nepilns", "Nē, kubisks"],
         "pareizi": 0, "padoms": "Nav x^2."},
        {"jaut": "x^3 − x = 0",
         "opcijas": ["Nē - ir x^3", "Jā", "Jā, nepilns", "Nē, lineārs"],
         "pareizi": 0, "padoms": "Trešā pakāpe."},
        {"jaut": "x^2 = 7x",
         "opcijas": ["Jā, nepilns (c = 0)", "Nē", "Jā, pilns",
                     "Nē, lineārs"],
         "pareizi": 0, "padoms": "x^2 − 7x = 0."},
    ]),

    Ievadi("Nosauc koeficientus", [
        {"jaut": "2x^2 + 7x − 4 = 0 (eksāmens 2025). a = ?", "atb": ["2"],
         "padoms": "Pie x^2."},
        {"jaut": "Tajā pašā b = ?", "atb": ["7"], "padoms": "Pie x."},
        {"jaut": "Tajā pašā c = ?", "atb": ["−4", "-4"],
         "padoms": "Brīvais loceklis ar zīmi."},
        {"jaut": "x^2 − 9 = 0. b = ?", "atb": ["0"], "padoms": "Nav x."},
        {"jaut": "−x^2 + 3x = 0. a = ?", "atb": ["−1", "-1"],
         "padoms": "−x^2 = −1 · x^2."},
        {"jaut": "5 − x^2 + 2x = 0. c = ?", "atb": ["5"],
         "padoms": "Secība nav svarīga."},
    ], pamats=4),

    Pasaule("Strūklaka parkā",
            Ievadi("", [
                {"jaut": "Strūkla y = −0,5x^2 + 2x. a = ?", "atb": ["−0,5",
                                                                  "-0,5"],
                 "padoms": "Pie x^2."},
                {"jaut": "Cik augstu ūdens paceļas pie x = 2 (m)?",
                 "atb": ["2"], "padoms": "−0,5 · 4 + 4."},
                {"jaut": "Vai x = 4 ūdens ir zemē? Ieraksti y(4).",
                 "atb": ["0"], "padoms": "−0,5 · 16 + 8."},
            ]),
            pavediens="tehnika",
            konteksts="Strūklakas inženieris izvēlas a un b, lai ūdens krītu "
                      "tieši baseinā.",
            kapec="Kvadrātvienādojums atbild «kur?», funkcija - «cik augstu?»."),

    Kopsavilkums([
        "Atpazīstu kvadrātvienādojumu.",
        "Nosaucu koeficientus a, b, c ar zīmēm.",
        "Zinu, ka a ≠ 0.",
    ]),

    Majas([
        "Pārveido uz formu ax^2 + bx + c = 0: (x − 1)(x + 4) = 6.",
        "Nosauc a, b, c vienādojumā 3 − 2x^2 = x.",
        "Atrodi internetā strūklakas vai tilta foto ar parabolu.",
    ]),
]
