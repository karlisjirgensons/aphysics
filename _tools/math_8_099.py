# -*- coding: utf-8 -*-
"""8. klase, 99. stunda: «Kā aprēķināt paralelograma lielumus?»

Aprēķini ar īpašībām: P = 2(a + b), blakus leņķi 180°. Klasisks gadījums
- leņķa bisektrise nogriež vienādsānu trijstūri: AD = 5, AB = 8, A
bisektrise krusto DC punktā K, DK = 5, KC = 3 (koordinātes to ievēro).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā aprēķināt paralelograma lielumus?"

MERKIS = "Aprēķināsim paralelograma malas, leņķus un perimetru."

SATURS = [
    Sakums("Kur bisektrise krusto malu?",
           zimejums=geometrija([("A", 0, 0), ("B", 8, 0), ("C", 11, 4),
                                ("D", 3, 4), ("K", 8, 4, 90)],
                               nogriezni=["AB", "BC", "CD", "DA", "AK"],
                               lenki=[("BAK", "", 1), ("KAD", "", 1)],
                               malas=[("AB", "8"), ("DA", "5")],
                               iekrasot=[("ADK", 1)]),
           paraksts="AK - bisektrise: DK = AD = 5, tāpēc KC = 3.",
           fakti=["Perimetrs P = 2(a + b).",
                  "Blakus leņķu summa ir 180°, pretējie leņķi vienādi.",
                  "Bisektrise nogriež vienādsānu trijstūri."]),

    Doma("Rīki aprēķiniem",
         "Katru nezināmo atrod ar kādu īpašību.",
         soli=[
             "Ieraksti zīmējumā visus zināmos lielumus.",
             "Pretējās malas un leņķi vienādi, blakus leņķi dod 180°.",
             "Bisektrise + šķērsleņķi ⇒ vienādsānu trijstūris.",
             "Pārbaudi ar perimetru vai leņķu summu 360°.",
         ]),

    Paraugs("Bisektrise",
            uzd="Paralelogramā ABCD AD = 5, AB = 8; ∠A bisektrise krusto DC "
                "punktā K. Atrodi KC un perimetru.",
            soli=[
                ("∠DKA = ∠KAB", "Šķērsleņķi, AB ∥ DC."),
                ("∠KAB = ∠DAK", "AK - bisektrise."),
                ("∠DKA = ∠DAK ⇒ DK = AD = 5", "△ADK vienādsānu."),
                ("KC = 8 − 5 = 3; P = 2 · (8 + 5) = 26", "DC = AB = 8."),
            ],
            atbilde="KC = 3, P = 26"),

    Ievadi("Aprēķini", [
        {"jaut": "P = 36, AB = 11. BC?", "atb": ["7"], "padoms": "18 − 11."},
        {"jaut": "AB − BC = 4, P = 28. AB?", "atb": ["9"],
         "padoms": "AB + BC = 14."},
        {"jaut": "∠A ir par 40° mazāks nekā ∠B. ∠A?", "atb": ["70"],
         "padoms": "∠A + ∠B = 180°."},
        {"jaut": "Bisektrise no A: DK = 6, KC = 4. P?", "atb": ["32"],
         "padoms": "AD = 6, DC = 10."},
        {"jaut": "∠A = 3∠B. ∠B?", "atb": ["45"], "padoms": "4∠B = 180°."},
    ]),

    Varianti("Izvēlies", [
        {"jaut": "Malas 5 un 7. Perimetrs?",
         "opcijas": ["24", "35", "12", "17"],
         "pareizi": 0, "padoms": "2 · 12."},
        {"jaut": "Viens leņķis 50°. Pārējie?",
         "opcijas": ["50°, 130°, 130°", "50°, 50°, 50°",
                     "130°, 130°, 130°", "40°, 140°, 130°"],
         "pareizi": 0, "padoms": "Pretējais vienāds, blakus 180°."},
        {"jaut": "Bisektrise no A krusto DC punktā K. Kurš trijstūris ir "
                 "vienādsānu?",
         "opcijas": ["ADK", "ABK", "KBC", "ABC"],
         "pareizi": 0, "padoms": "DK = AD."},
    ]),

    Pasaule("Eglītes parkets",
            Ievadi("", [
                {"jaut": "Parketa dēlītis - paralelograms ar malām 30 cm un "
                         "7 cm, šaurais leņķis 45°. Platais leņķis?",
                 "atb": ["135"], "padoms": "180 − 45."},
                {"jaut": "Dēlīša perimetrs (cm)?", "atb": ["74"],
                 "padoms": "2 · 37."},
                {"jaut": "Cik cm malu kopā ir 10 dēlīšiem?", "atb": ["740"],
                 "padoms": "10 · 74."},
            ]),
            pavediens="maja",
            konteksts="Eglītes parketu liek no paralelograma formas "
                      "dēlīšiem.",
            kapec="Zinot vienu leņķi, zina visus četrus."),

    Kopsavilkums([
        "Aprēķinu paralelograma malas un perimetru.",
        "Aprēķinu leņķus ar īpašībām.",
        "Lietoju bisektrises nogriezto vienādsānu trijstūri.",
    ]),

    Majas([
        "Izmēri paralelograma formas priekšmetu un aprēķini perimetru.",
        "Uzzīmē paralelogramu ar malām 6 cm un 4 cm un novelc bisektrisi.",
        "Pārbaudi, vai DK = AD.",
    ]),
]
