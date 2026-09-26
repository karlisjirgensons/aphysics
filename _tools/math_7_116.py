# -*- coding: utf-8 -*-
"""7. klase, 116. stunda: «Kā pierakstīt attiecību ar burtiem?»

Ja lielumi attiecas kā 2 : 3, tos pieraksta kā 2x un 3x - viena daļa ir x.
Tā pati ideja der trim lielumiem (2x, 3x, 5x). Stunda lieto to receptēs,
naudas dalīšanā un leņķos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā pierakstīt attiecību ar burtiem?"

MERKIS = ("Aprakstīsim ar izteiksmi lielumus, kas doti kā divu vai trīs "
          "skaitļu attiecība.")

SATURS = [
    Sakums("Betons: cements, smiltis, šķembas - 1 : 2 : 4",
           zimejums=dala(7, 1, "1 daļa cementa no 7"),
           paraksts="Kopā 7 daļas; viena daļa - x.",
           fakti=["Cements x, smiltis 2x, šķembas 4x.",
                  "Kopā x + 2x + 4x = 7x.",
                  "Ja visa maisījuma ir 350 kg, x = 50 kg."]),

    Doma("Viena daļa = x",
         "Ja lielumi attiecas kā a : b : c, tos pieraksta kā ax, bx un cx, "
         "kur x ir vienas daļas lielums. To summa ir (a + b + c)x.",
         soli=[
             "Apzīmē vienu daļu ar x.",
             "Katru lielumu izsaki kā daļu skaitu · x.",
             "Summa - visu daļu skaits · x.",
             "Zinot summu, atrodi x un katru lielumu.",
         ],
         pieze="Attiecība 2 : 3 nenozīmē, ka lielumi ir 2 un 3 - tie var būt "
               "20 un 30 vai 2x un 3x."),

    Paraugs("Naudas dalīšana",
            uzd="Trīs draugi dalās ar 90 € attiecībā 2 : 3 : 4. Cik katram?",
            soli=[
                ("2x, 3x, 4x", "Apzīmē."),
                ("2x + 3x + 4x = 9x = 90", "Summa."),
                ("x = 10", "Viena daļa."),
                ("20 €, 30 €, 40 €", "Katram."),
            ],
            atbilde="20 €, 30 € un 40 €"),

    Varianti("Pieraksti", [
        {"jaut": "Zēnu un meiteņu skaits attiecas kā 3 : 4. Kopā?",
         "opcijas": ["7x", "12x", "3x + 4", "34x"],
         "pareizi": 0, "padoms": "3x + 4x."},
        {"jaut": "Leņķi attiecas kā 1 : 2 : 6. Lielākais?",
         "opcijas": ["6x", "9x", "2x", "x + 6"],
         "pareizi": 0, "padoms": "6 daļas."},
        {"jaut": "Malas 5 : 7. Starpība?",
         "opcijas": ["2x", "12x", "35x", "7x − 5"],
         "pareizi": 0, "padoms": "7x − 5x."},
        {"jaut": "Sula un ūdens 1 : 4. Kāda daļa ir sula?",
         "opcijas": ["{1|5}", "{1|4}", "{4|5}", "{1|3}"],
         "pareizi": 0, "padoms": "1 no 5 daļām."},
    ], pamats=4),

    Ievadi("Aprēķini", [
        {"jaut": "Sula un ūdens 1 : 4, kopā 2 l. Cik l sulas?",
         "atb": ["0,4"], "padoms": "5x = 2."},
        {"jaut": "Betons 1 : 2 : 4, kopā 350 kg. Cik kg šķembu?",
         "atb": ["200"], "padoms": "x = 50, 4x."},
        {"jaut": "Malas 5 : 7, perimetrs taisnstūrim 48 cm. Garākā mala "
                 "(cm)?",
         "atb": ["14"], "padoms": "2(5x + 7x) = 48, x = 2."},
        {"jaut": "Zēni un meitenes 3 : 4, klasē 28. Cik zēnu?",
         "atb": ["12"], "padoms": "7x = 28."},
    ]),

    Pasaule("Pankūku recepte",
            Ievadi("", [
                {"jaut": "Milti, piens, olas pēc masas 5 : 8 : 2. Kopā 750 g. "
                         "Cik g miltu?",
                 "atb": ["250"], "padoms": "15x = 750, x = 50."},
                {"jaut": "Cik g piena?",
                 "atb": ["400"], "padoms": "8 · 50."},
                {"jaut": "Ja ņem 150 g miltu, cik g piena?",
                 "atb": ["240"], "padoms": "x = 30."},
            ]),
            pavediens="virtuve",
            konteksts="Pavāri receptes raksta attiecībās - tad tās var "
                      "pagatavot jebkuram viesu skaitam.",
            kapec="Attiecība ar x der jebkuram daudzumam."),

    Kopsavilkums([
        "Pierakstu attiecību a : b : c kā ax, bx, cx.",
        "Summu izsaku kā (a + b + c)x.",
        "Atrodu x un katru lielumu.",
        "Lietoju attiecības receptēs un dalīšanā.",
    ]),

    Majas([
        "Sadali 120 € attiecībā 1 : 2 : 3.",
        "Pārraksti mīļāko recepti attiecībās.",
        "Taisnstūra malas 2 : 3, laukums? Uzraksti ar x.",
    ]),
]
