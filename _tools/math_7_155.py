# -*- coding: utf-8 -*-
"""7. klase, 155. stunda: «Kas notiek, reizinot ar negatīvu skaitli?»

2 < 5, bet −2 > −5. Reizinot (vai dalot) nevienādību ar negatīvu skaitli,
zīme mainās uz pretējo. Uz skaitļu taisnes reizinājums ar −1 ir spoguļattēls
pret nulli - un secība apgriežas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kas notiek, reizinot ar negatīvu skaitli?"

MERKIS = ("Pamatosim, kāpēc, reizinot nevienādību ar negatīvu skaitli, "
          "zīme mainās.")

SATURS = [
    Sakums("Spogulis pie nulles",
           zimejums=taisne(-6, 6, 1, [(2, "2"), (5, "5"), (-2, "−2"),
                                      (-5, "−5")]),
           paraksts="2 < 5, bet −2 > −5.",
           fakti=["Reizinot ar −1, punkti atspoguļojas pret 0.",
                  "Kas bija labāk, tagad ir kreisāk.",
                  "Tāpēc zīme < kļūst par >."]),

    Doma("Negatīvs reizinātājs apgriež zīmi",
         "Ja a < b un c < 0, tad ac > bc. Reizinot vai dalot abas "
         "nevienādības puses ar negatīvu skaitli, nevienādības zīme mainās uz "
         "pretējo.",
         soli=[
             "Pirms reizināšanas vai dalīšanas - skaties reizinātāja zīmi.",
             "Pozitīvs - zīme paliek.",
             "Negatīvs - < kļūst >, ≤ kļūst ≥ un otrādi.",
             "Pārbaudi ar skaitli.",
         ],
         pieze="Pieskaitot negatīvu skaitli zīme NEmainās - tikai reizinot "
               "un dalot."),

    Paraugs("Dali ar negatīvu",
            uzd="Atrisini −3x < 12.",
            soli=[
                ("x > 12 : (−3)", "(abas puses : (−3), zīme mainās)"),
                ("x > −4", "Rezultāts."),
                ("Pārbaude x = 0: 0 < 12 ✓", "0 > −4 - der."),
                ("Pārbaude x = −5: 15 < 12 ✗", "−5 < −4 - neder."),
            ],
            atbilde="x > −4"),

    Varianti("Zīme mainās?", [
        {"jaut": "x < 6, reizina ar −2.",
         "opcijas": ["−2x > −12", "−2x < −12", "−2x > 12", "−2x < 12"],
         "pareizi": 0, "padoms": "Mainās."},
        {"jaut": "−x ≥ 4. Kāds x?",
         "opcijas": ["x ≤ −4", "x ≥ −4", "x ≥ 4", "x ≤ 4"],
         "pareizi": 0, "padoms": "· (−1)."},
        {"jaut": "x > 3, pieskaita −5.",
         "opcijas": ["x − 5 > −2", "x − 5 < −2", "x − 5 > 8",
                     "x − 5 < 8"],
         "pareizi": 0, "padoms": "Pieskaitot nemainās."},
        {"jaut": "{x|−2} > 1. Kāds x?",
         "opcijas": ["x < −2", "x > −2", "x < 2", "x > 2"],
         "pareizi": 0, "padoms": "· (−2), mainās."},
    ], pamats=4),

    Ievadi("Atrisini (robeža)", [
        {"jaut": "−5x ≤ 20. x ≥ ?",
         "atb": ["−4", "-4"], "padoms": ": (−5), mainās."},
        {"jaut": "−x > 7. x < ?",
         "atb": ["−7", "-7"], "padoms": "· (−1)."},
        {"jaut": "−2x < −10. x > ?",
         "atb": ["5"], "padoms": ": (−2)."},
    ]),

    Pasaule("Temperatūra zem nulles",
            Varianti("", [
                {"jaut": "Rīgā −3 °C, Tartu −8 °C. Kur aukstāk?",
                 "opcijas": ["Tartu", "Rīgā", "Vienādi"],
                 "pareizi": 0, "jaukt": False,
                 "padoms": "−8 < −3."},
                {"jaut": "Moduļi: 3 un 8. «Salnas stiprums» lielāks...",
                 "opcijas": ["Tartu - 8 > 3", "Rīgā", "Vienādi"],
                 "pareizi": 0, "jaukt": False,
                 "padoms": "Reizinot ar −1, secība apgriežas."},
            ]),
            pavediens="planeta",
            konteksts="Ziemā «lielāks sals» nozīmē mazāku temperatūru - tā "
                      "ir zīmes maiņa reizinot ar −1.",
            kapec="Negatīvi skaitļi apgriež secību."),

    Kopsavilkums([
        "Zinu, ka reizinot ar negatīvu, zīme mainās.",
        "Pamatoju ar spoguļattēlu pret 0.",
        "Pieskaitot negatīvu, zīmi nemainu.",
        "Pārbaudu ar skaitli.",
    ]),

    Majas([
        "Atrisini: −4x ≥ 8; −{x|3} < 2.",
        "Uzzīmē uz taisnes 1 < 4 un −1 > −4.",
        "Paskaidro draugam, kāpēc zīme mainās.",
    ]),
]
