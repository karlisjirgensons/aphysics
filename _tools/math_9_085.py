# -*- coding: utf-8 -*-
"""9. klase, 85. stunda: «Kā pārbaudīt sakni?»

Sakni pārbauda SĀKOTNĒJĀ vienādojumā - ne pārveidotajā, jo kļūda var būt
tieši pārveidojumā. Stundā arī ātrā pārbaude ar Vjeta teorēmu (formulu
lapā): x_1 + x_2 = −p, x_1 · x_2 = q.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā pārbaudīt sakni?"

MERKIS = "Pārbaudīsim saknes, ievietojot tās sākotnējā vienādojumā."

SATURS = [
    Sakums("Vai x = 4 ir vienādojuma x² − 3x = 4 sakne?",
           zimejums=restis([["x", "x² − 3x", "= 4?"], ["4", "16 − 12 = 4", "✔"],
                            ["−1", "1 + 3 = 4", "✔"], ["2", "4 − 6 = −2", "✘"]]),
           paraksts="Ievieto un salīdzini abas puses.",
           fakti=["Sakne padara vienādojumu par patiesu vienādību.",
                  "Pārbauda sākotnējā vienādojumā.",
                  "Kvadrātvienādojumam var būt 2 saknes - pārbauda abas."]),

    Doma("Pārbaude",
         "Ievieto skaitli sākotnējā vienādojumā un aprēķini abas puses "
         "atsevišķi; ja tās vienādas - skaitlis ir sakne.",
         soli=[
             "Negatīvu skaitli ievieto iekavās: (−3)^2 = 9.",
             "Aprēķini kreiso pusi, tad labo.",
             "Salīdzini.",
             "Ātrā pārbaude (a = 1): x_1 + x_2 = −b, x_1 · x_2 = c.",
         ]),

    Paraugs("Pārbaude ar negatīvu sakni",
            uzd="Pārbaudi, vai x = −3 ir vienādojuma 2x^2 + 5x = 3 sakne.",
            soli=[
                ("2 · (−3)^2 + 5 · (−3) = 18 − 15 = 3", "Kreisā puse."),
                ("3 = 3", "Labā puse sakrīt."),
            ],
            atbilde="jā, x = −3 ir sakne"),

    Varianti("Sakne vai nē?", [
        {"jaut": "x = 2 vienādojumam x^2 + x − 6 = 0",
         "opcijas": ["Sakne", "Nav sakne"], "jaukt": False,
         "pareizi": 0, "padoms": "4 + 2 − 6 = 0."},
        {"jaut": "x = −2 vienādojumam x^2 + x − 6 = 0",
         "opcijas": ["Sakne", "Nav sakne"], "jaukt": False,
         "pareizi": 1, "padoms": "4 − 2 − 6 = −4."},
        {"jaut": "x = 0,5 vienādojumam 2x^2 + 7x − 4 = 0",
         "opcijas": ["Sakne", "Nav sakne"], "jaukt": False,
         "pareizi": 0, "padoms": "0,5 + 3,5 − 4 = 0."},
        {"jaut": "x = −4 vienādojumam 2x^2 + 7x − 4 = 0",
         "opcijas": ["Sakne", "Nav sakne"], "jaukt": False,
         "pareizi": 0, "padoms": "32 − 28 − 4 = 0."},
    ]),

    Ievadi("Ātrā pārbaude ar Vjetu (a = 1)", [
        {"jaut": "x^2 − 9x + 14 = 0. Sakņu summa = ?", "atb": ["9"],
         "padoms": "−b."},
        {"jaut": "Tās pašas sakņu reizinājums = ?", "atb": ["14"],
         "padoms": "c."},
        {"jaut": "Viena sakne 2. Otra?", "atb": ["7"], "padoms": "9 − 2."},
        {"jaut": "x^2 + 4x − 21 = 0, viena sakne 3. Otra?",
         "atb": ["−7", "-7"], "padoms": "Summa −4."},
    ]),

    Pasaule("Mājasdarba pārbaude",
            Varianti("", [
                {"jaut": "Draugs atrisināja x^2 − 5x − 6 = 0 un ieguva 2 un 3. "
                         "Ātrā pārbaude: 2 · 3 = 6, bet c = −6. Secinājums?",
                 "opcijas": ["Kļūda: pareizi −1 un 6", "Viss pareizi",
                             "Kļūda: pareizi 1 un −6", "Nevar pārbaudīt"],
                 "pareizi": 0, "padoms": "−1 · 6 = −6; −1 + 6 = 5."},
                {"jaut": "Kurš pārbaudes veids ir drošākais?",
                 "opcijas": ["Ievietot sākotnējā vienādojumā",
                             "Paskatīties atbildēs", "Pajautāt draugam",
                             "Ievietot pārveidotajā vienādojumā"],
                 "pareizi": 0, "padoms": "Kļūda var būt pārveidojumā."},
            ]),
            pavediens="skola",
            konteksts="Eksāmenā atbildes nav - pārbaudīt vari tikai pats.",
            kapec="Pusminūtes pārbaude izglābj punktus."),

    Kopsavilkums([
        "Pārbaudu sakni sākotnējā vienādojumā.",
        "Negatīvu skaitli ievietoju iekavās.",
        "Ātri pārbaudu ar sakņu summu un reizinājumu.",
    ]),

    Majas([
        "Pārbaudi, vai 1,5 ir vienādojuma 2x^2 − x = 3 sakne.",
        "Atrisini x^2 − 8x + 15 = 0 un pārbaudi ar Vjetu.",
        "Izdomā vienādojumu, kura saknes ir −2 un 5.",
    ]),
]
