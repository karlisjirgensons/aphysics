# -*- coding: utf-8 -*-
"""8. klase, 59. stunda: «Kā iznest reizinātāju pirms saknes?»

√(a^2 · b) = a√b, ja a ≥ 0. Zemsaknes skaitli sadala lielākajā pilnajā
kvadrātā un pārējā daļā. Ienešana ir apgrieztā darbība - to jau lietoja
saknes salīdzinot (56. stunda).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā iznest reizinātāju pirms saknes?"

MERKIS = "Iznesīsim reizinātāju pirms saknes un ienesīsim to zem saknes."

SATURS = [
    Sakums("Vai √50 = 5√2?",
           zimejums=restis([["√50", "25 · 2", "5√2"],
                            ["√12", "4 · 3", "2√3"],
                            ["√72", "36 · 2", "6√2"]]),
           paraksts="Zem saknes atrod pilnu kvadrātu un to iznes.",
           fakti=["√(a^2 · b) = a√b, ja a ≥ 0.",
                  "Meklē lielāko pilno kvadrātu zem saknes.",
                  "Ienesot reizinātāju, to kāpina kvadrātā: 3√2 = √18."]),

    Doma("Iznešana un ienešana",
         "Pilna kvadrāta reizinātājs iziet no saknes kā tā sakne.",
         soli=[
             "Sadali zemsaknes skaitli: pilns kvadrāts · pārējais: 75 = 25 · 3.",
             "Pilnā kvadrāta sakni iznes: √75 = 5√3.",
             "Pārbaudi, vai pārējā daļā vēl ir kvadrāts: √72 = 2√18 nav "
             "galā - 72 = 36 · 2, tāpēc √72 = 6√2.",
             "Ienesot: 4√5 = √(16 · 5) = √80.",
         ],
         pieze="Ar mainīgo: √(9x^2) = 3x, ja x ≥ 0."),

    Paraugs("Iznes reizinātāju",
            uzd="Vienkāršo √200, √(0,18) un √(48a^2), ja a ≥ 0.",
            soli=[
                ("√200 = √(100 · 2) = 10√2", "100 - lielākais pilnais "
                                             "kvadrāts."),
                ("√(0,18) = √(0,09 · 2) = 0,3√2", "0,09 = 0,3^2."),
                ("√(48a^2) = √(16 · 3 · a^2) = 4a√3", "a ≥ 0, tāpēc "
                                                     "√(a^2) = a."),
            ],
            atbilde="10√2; 0,3√2; 4a√3"),

    Ievadi("Ieraksti trūkstošo skaitli", [
        {"jaut": "√45 = ?√5", "atb": ["3"], "padoms": "45 = 9 · 5."},
        {"jaut": "√98 = ?√2", "atb": ["7"], "padoms": "98 = 49 · 2."},
        {"jaut": "√300 = ?√3", "atb": ["10"], "padoms": "300 = 100 · 3."},
        {"jaut": "3√7 = √?", "atb": ["63"], "padoms": "9 · 7."},
        {"jaut": "√(0,08) = ?√2", "atb": ["0,2"],
         "padoms": "0,08 = 0,04 · 2."},
        {"jaut": "√180 = ?√5", "atb": ["6"], "padoms": "180 = 36 · 5."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "Vienkāršākais √32 pieraksts:",
         "opcijas": ["4√2", "2√8", "16√2", "8√2"],
         "pareizi": 0, "padoms": "32 = 16 · 2; 2√8 vēl var vienkāršot."},
        {"jaut": "2√5 ienests zem saknes:",
         "opcijas": ["√20", "√10", "√25", "√45"],
         "pareizi": 0, "padoms": "4 · 5."},
        {"jaut": "Kuru sakni NEVAR vienkāršot?",
         "opcijas": ["√30", "√28", "√54", "√63"],
         "pareizi": 0, "padoms": "30 = 2 · 3 · 5 - pilna kvadrāta nav."},
    ]),

    Pasaule("Kvadrātveida flīze",
            Ievadi("", [
                {"jaut": "Kvadrātveida flīzes laukums ir 18 dm². Mala = ?√2 dm",
                 "atb": ["3"], "padoms": "18 = 9 · 2."},
                {"jaut": "Cik dm tas ir aptuveni (līdz desmitdaļām)?",
                 "atb": ["4,2"], "padoms": "3 · 1,414."},
                {"jaut": "Kvadrāta diagonāle = mala · √2. Cik dm ir šīs "
                         "flīzes diagonāle?",
                 "atb": ["6"], "padoms": "3√2 · √2 = 3 · 2."},
            ]),
            pavediens="maja",
            konteksts="Precīzos aprēķinos saknes pieraksta vienkāršoti - tā "
                      "vieglāk rēķināt tālāk.",
            kapec="Vienkāršotā sakne ļauj izrēķināt diagonāli bez "
                  "tuvinājumiem."),

    Kopsavilkums([
        "Iznesu reizinātāju pirms saknes.",
        "Ienesu reizinātāju zem saknes.",
        "Pārbaudu, vai sakne ir pilnīgi vienkāršota.",
    ]),

    Majas([
        "Vienkāršo: √27, √80, √162, √(0,12).",
        "Ienes zem saknes: 5√3, 7√2.",
        "Atrodi kvadrātveida flīzi un izrēķini tās diagonāli.",
    ]),
]
