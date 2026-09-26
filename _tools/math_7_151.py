# -*- coding: utf-8 -*-
"""7. klase, 151. stunda: «Kā salīdzināt izteiksmes ar mainīgo?»

Izteiksmes ar mainīgo ne vienmēr var salīdzināt vienā vārdā: x + 3 vienmēr
ir lielāks par x, bet 2x un 3x - atkarīgs no x zīmes. Stunda iemāca spriest
un pamatot, arī ar pretpiemēru.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kā salīdzināt izteiksmes ar mainīgo?"

MERKIS = ("Salīdzināsim izteiksmes (x un x + 3; 2x un 3x), spriežot un "
          "pamatojot spriedumu.")

SATURS = [
    Sakums("Kurš lielāks - 2x vai 3x?",
           zimejums=restis([["x", "2x", "3x", "lielāks"],
                            ["5", "10", "15", "3x"],
                            ["0", "0", "0", "vienādi"],
                            ["−5", "−10", "−15", "2x"]]),
           fakti=["Atbilde atkarīga no x!",
                  "Pozitīvam x - 3x lielāks.",
                  "Negatīvam x - 2x lielāks."]),

    Doma("Salīdzini ar starpību",
         "Divas izteiksmes salīdzina, aprēķinot to starpību: ja starpība "
         "vienmēr pozitīva - pirmā vienmēr lielāka. Ja starpības zīme "
         "atkarīga no x, atbilde ir «atkarībā no x».",
         soli=[
             "Aprēķini A − B un vienkāršo.",
             "(x + 3) − x = 3 > 0 - vienmēr lielāks x + 3.",
             "3x − 2x = x - zīme kā x.",
             "Pamato ar pretpiemēru, ja apgalvojums nav vienmēr patiess.",
         ]),

    Paraugs("Salīdzini",
            uzd="Salīdzini x² un x.",
            soli=[
                ("x = 2: 4 > 2", "x² lielāks."),
                ("x = {1|2}: {1|4} < {1|2}", "x lielāks."),
                ("x = 1: vienādi", "Arī x = 0."),
                ("Atkarīgs no x", "Nav viennozīmīgas atbildes."),
            ],
            atbilde="Ja x > 1 vai x < 0 - x² lielāks; ja 0 < x < 1 - x lielāks."),

    Varianti("Kurš lielāks?", [
        {"jaut": "a + 5 un a",
         "opcijas": ["a + 5 vienmēr", "a vienmēr", "Atkarīgs no a"],
         "pareizi": 0, "jaukt": False, "padoms": "Starpība 5."},
        {"jaut": "b − 2 un b + 1",
         "opcijas": ["b − 2 vienmēr", "b + 1 vienmēr", "Atkarīgs no b"],
         "pareizi": 1, "jaukt": False, "padoms": "Starpība 3."},
        {"jaut": "5y un 4y",
         "opcijas": ["5y vienmēr", "4y vienmēr", "Atkarīgs no y"],
         "pareizi": 2, "jaukt": False, "padoms": "Starpība y."},
        {"jaut": "−x un x",
         "opcijas": ["−x vienmēr", "x vienmēr", "Atkarīgs no x"],
         "pareizi": 2, "jaukt": False, "padoms": "x = −1 un x = 1."},
        {"jaut": "x² + 1 un 0",
         "opcijas": ["x² + 1 vienmēr", "0 vienmēr", "Atkarīgs no x"],
         "pareizi": 0, "jaukt": False, "padoms": "x² ≥ 0."},
        {"jaut": "2(x + 1) un 2x + 1",
         "opcijas": ["2(x + 1) vienmēr", "2x + 1 vienmēr", "Atkarīgs no x"],
         "pareizi": 0, "jaukt": False, "padoms": "2x + 2 − 2x − 1 = 1."},
    ], pamats=4),

    Pasaule("Divi mobilie tarifi",
            Varianti("", [
                {"jaut": "A: 0,05 € par minūti. B: 0,04 € par minūti + 3 €. "
                         "Kurš vienmēr lētāks?",
                 "opcijas": ["Atkarīgs no minūšu skaita", "A vienmēr",
                             "B vienmēr", "Vienādi"],
                 "pareizi": 0, "padoms": "Starpība 0,01m − 3."},
                {"jaut": "Pie cik minūtēm vienādi?",
                 "opcijas": ["300", "30", "3", "3000"],
                 "pareizi": 0, "padoms": "0,01m = 3."},
            ]),
            pavediens="dati",
            konteksts="Salīdzinot tarifus, atbilde parasti ir «atkarīgs no "
                      "lietošanas» - un nevienādība pasaka robežu.",
            kapec="Starpības zīme izšķir."),

    Kopsavilkums([
        "Salīdzinu izteiksmes ar starpību.",
        "Atšķiru «vienmēr» un «atkarīgs no x».",
        "Pamatoju ar pretpiemēru.",
        "Salīdzinu 2x un 3x negatīviem un pozitīviem x.",
    ]),

    Majas([
        "Salīdzini x un {1|x}, kad x > 0.",
        "Salīdzini 4 − x un 4 + x.",
        "Salīdzini divus reālus tarifus.",
    ]),
]
