# -*- coding: utf-8 -*-
"""9. klase, 95. stunda: «Kāda ir funkcijas lielākā vērtība?»

Virsotne ir vai nu zemākais (a > 0), vai augstākais (a < 0) punkts: y_v ir
funkcijas mazākā vai lielākā vērtība, un vērtību apgabals ir [y_v; +∞) vai
(−∞; y_v]. Pieraksts ar intervāliem - kā eksāmena 8. uzdevumā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, parabola)

TEMA = "Kāda ir funkcijas lielākā vērtība?"

MERKIS = ("Noteiksim funkcijas lielāko vai mazāko vērtību un vērtību "
          "apgabalu.")

SATURS = [
    Sakums("Cik augstu var uzmest bumbu?",
           zimejums=parabola(-1, 4, 1, -1, 5, -2, 6,
                             punkti=[(2, 5, "max 5")]),
           paraksts="y = −x² + 4x + 1: augstāk par 5 grafiks neceļas.",
           fakti=["a < 0: virsotne ir augstākais punkts.",
                  "Lielākā vērtība y_v = 5; mazākās nav.",
                  "Vērtību apgabals: (−∞; 5]."]),

    Slidnis("Zari nosaka, kas ir virsotne", [
        {"v": "a > 0", "teksts": "y = x^2 − 4x + 1: mazākā vērtība −3, "
                                 "E(f) = [−3; +∞)",
         "zim": parabola(1, -4, 1, -1, 5, -4, 6, punkti=[(2, -3, "min")])},
        {"v": "a < 0", "teksts": "y = −x^2 + 4x + 1: lielākā vērtība 5, "
                                 "E(f) = (−∞; 5]",
         "zim": parabola(-1, 4, 1, -1, 5, -4, 6, punkti=[(2, 5, "max")])},
    ]),

    Doma("Lielākā un mazākā vērtība",
         "Ja a > 0, y_v ir mazākā vērtība; ja a < 0, y_v ir lielākā vērtība.",
         soli=[
             "Aprēķini x_v un y_v.",
             "Pēc a zīmes nosaki: min vai max.",
             "Vērtību apgabals: [y_v; +∞) vai (−∞; y_v].",
             "Kvadrātiekava - vērtība pieder, apaļā - nepieder.",
         ]),

    Paraugs("Mazākā vērtība",
            uzd="Atrodi funkcijas y = 2x^2 − 8x + 3 mazāko vērtību un "
                "vērtību apgabalu.",
            soli=[
                ("x_v = −{−8|4} = 2", "Virsotnes abscisa."),
                ("y_v = 8 − 16 + 3 = −5", "Ordināta."),
                ("a = 2 > 0 ⇒ min = −5", "Zari augšup."),
            ],
            atbilde="min y = −5; E(f) = [−5; +∞)"),

    Ievadi("Aprēķini", [
        {"jaut": "y = x^2 − 6x + 10. Mazākā vērtība?", "atb": ["1"],
         "padoms": "x_v = 3; 9 − 18 + 10."},
        {"jaut": "y = −x^2 + 2x + 8. Lielākā vērtība?", "atb": ["9"],
         "padoms": "x_v = 1; −1 + 2 + 8."},
        {"jaut": "y = (x + 4)^2 − 7. Mazākā vērtība?", "atb": ["−7", "-7"],
         "padoms": "Kvadrāts ≥ 0."},
        {"jaut": "y = −3x^2 + 12. Lielākā vērtība?", "atb": ["12"],
         "padoms": "x_v = 0."},
    ]),

    Varianti("Vērtību apgabals", [
        {"jaut": "y = x^2 + 2",
         "opcijas": ["[2; +∞)", "(−∞; 2]", "(2; +∞)", "visi skaitļi"],
         "pareizi": 0, "padoms": "Min 2, pieder."},
        {"jaut": "y = −(x − 1)^2 + 6",
         "opcijas": ["(−∞; 6]", "[6; +∞)", "(−∞; 1]", "[1; 6]"],
         "pareizi": 0, "padoms": "Max 6."},
        {"jaut": "Vai y = x^2 − 4x var būt −5?",
         "opcijas": ["Nē - mazākā vērtība −4", "Jā", "Tikai x < 0",
                     "Jā, pie x = 5"],
         "pareizi": 0, "padoms": "y_v = −4."},
    ]),

    Pasaule("Mazākais degvielas patēriņš",
            Ievadi("", [
                {"jaut": "Auto patēriņš P = 0,002v^2 − 0,28v + 15 (l/100 km). "
                         "Pie kāda ātruma (km/h) patēriņš mazākais?",
                 "atb": ["70"], "padoms": "−{−0,28|0,004}."},
                {"jaut": "Mazākais patēriņš (l/100 km)?", "atb": ["5,2"],
                 "padoms": "9,8 − 19,6 + 15."},
            ]),
            pavediens="celojums",
            konteksts="Pārāk lēni vai pārāk ātri - auto tērē vairāk; kaut kur "
                      "pa vidu ir labākais ātrums.",
            kapec="Parabolas virsotne ir ekonomiskākais ātrums."),

    Kopsavilkums([
        "Nosaku lielāko vai mazāko vērtību pēc virsotnes.",
        "Pierakstu vērtību apgabalu ar intervālu.",
        "Lietoju to praktiskos optimizācijas uzdevumos.",
    ]),

    Majas([
        "Atrodi lielāko vērtību: y = −2x^2 + 4x + 1.",
        "Atrodi vērtību apgabalu: y = x^2 + 6x.",
        "Atrodi internetā sava auto (vai ģimenes auto) ekonomiskāko ātrumu.",
    ]),
]
