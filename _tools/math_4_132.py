# -*- coding: utf-8 -*-
"""4. klase, 132. stunda: «Kā pieraksta spriedumu?»

Ja zināma nevis pamatdaļa, bet daļa ({3|4} ir 18), veselo atrod divos
soļos: vispirms viena daļa (18 : 3 = 6), tad veselais (6 · 4 = 24).
Pieraksts atkārto domu gaitu - katrā rindā viens spriedums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā pieraksta spriedumu?"

MERKIS = ("Veidosim pierakstu, kas atbilst domāšanas gaitai, nosakot veselo "
          "un daļu.")

SATURS = [
    Sakums("Trīs ceturtdaļas ir 18. Cik ir viss?",
           zimejums=restis([["?", "?", "?", "?"],
                            ["18", "", "", ""]],
                           "trīs gabali kopā - 18"),
           paraksts="Viens gabals 18 : 3 = 6, viss 6 · 4 = 24.",
           fakti=["Vispirms atrod vienu gabalu.",
                  "Tad visus gabalus."]),

    Doma("Katrā rindā viens spriedums",
         "Ja {a|n} no veselā ir b, tad {1|n} ir b : a, bet veselais - "
         "(b : a) · n.",
         soli=[
             "1. rinda: ko zinām - {3|4} veselā ir 18.",
             "2. rinda: {1|4} veselā ir 18 : 3 = 6.",
             "3. rinda: veselais ir 6 · 4 = 24.",
             "4. rinda: pārbaude - {3|4} no 24 = 18.",
         ],
         pieze="Labs pieraksts ir tāds, ko var izlasīt kā stāstu."),

    Paraugs("{2|5} klases ir 10",
            uzd="{2|5} klases skolēnu brauc ar velosipēdu - tie ir 10. Cik "
                "skolēnu klasē?",
            soli=[
                ("{2|5} klases ir 10 skolēni", "Ko zinām."),
                ("{1|5} klases ir 10 : 2 = 5", "Viena daļa."),
                ("klasē ir 5 · 5 = 25", "Veselais."),
                ("{2|5} no 25 = 10", "Pārbaude."),
            ],
            atbilde="25 skolēni"),

    Ievadi("Divos soļos", [
        {"jaut": "{3|4} ir 18. Veselais = ?", "atb": ["24"],
         "padoms": "18 : 3 · 4."},
        {"jaut": "{2|5} ir 10. Veselais = ?", "atb": ["25"],
         "padoms": "10 : 2 · 5."},
        {"jaut": "{5|6} ir 40. Veselais = ?", "atb": ["48"],
         "padoms": "40 : 5 · 6."},
        {"jaut": "{3|8} ir 15. Veselais = ?", "atb": ["40"],
         "padoms": "15 : 3 · 8."},
        {"jaut": "{4|7} ir 28. Veselais = ?", "atb": ["49"],
         "padoms": "28 : 4 · 7."},
        {"jaut": "{2|3} ir 50 €. Veselais = ? €", "atb": ["75"],
         "padoms": "50 : 2 · 3."},
    ], pamats=4),

    Varianti("Kura rinda nepareiza?", [
        {"jaut": "Juris: «{3|4} ir 12. {1|4} ir 12 : 4 = 3. Veselais 3 · 4 = "
                 "12.» Kur kļūda?",
         "opcijas": ["jādala ar 3, nevis 4", "veselais 12 pareizs",
                     "jāreizina ar 3"], "pareizi": 0,
         "padoms": "{1|4} ir 12 : 3 = 4; veselais 16."},
        {"jaut": "Cik ir pareizais veselais, ja {3|4} ir 12?",
         "opcijas": ["16", "12", "9", "48"], "pareizi": 0,
         "padoms": "4 · 4."},
        {"jaut": "Kā pārbaudīt, ka veselais ir 16?",
         "opcijas": ["{3|4} no 16 = 12", "16 · 3 = 48", "16 − 12 = 4"],
         "pareizi": 0, "padoms": "Jāsanāk dotajai daļai."},
    ]),

    Pasaule("Kalna virsotne",
            Ievadi("", [
                {"jaut": "Alpīnisti uzkāpuši {3|5} kalna augstuma - 1200 m. "
                         "Cik m ir {1|5}?",
                 "atb": ["400"], "padoms": "1200 : 3."},
                {"jaut": "Cik augsts ir kalns?", "atb": ["2000"],
                 "padoms": "400 · 5."},
                {"jaut": "Cik metru vēl jākāpj?", "atb": ["800"],
                 "padoms": "2000 − 1200."},
                {"jaut": "Laivotāji nobrauca {5|8} upes - 50 km. Cik gara "
                         "visa upe?",
                 "atb": ["80"], "padoms": "50 : 5 · 8."},
            ]),
            pavediens="celojums",
            konteksts="Ceļotāji bieži zina, cik jau paveikts un kāda tā ir "
                      "daļa - un no tā izrēķina visu ceļu.",
            kapec="Pieraksts pa soļiem ļauj nepazust garā uzdevumā."),

    Kopsavilkums([
        "Atrodu veselo, ja zināma daļa (ne tikai pamatdaļa).",
        "Pierakstu risinājumu - katrā rindā viens spriedums.",
        "Pārbaudu, aprēķinot daļu no atrastā veselā.",
    ]),

    Majas([
        "Atrisini un pieraksti: {3|5} ir 21. Cik ir viss?",
        "Izdomā uzdevumu par ceļojumu, kurā zināma daļa ceļa.",
        "Palūdz kādam izlasīt tavu pierakstu kā stāstu.",
    ]),
]
