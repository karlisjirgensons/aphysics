# -*- coding: utf-8 -*-
"""8. klase, 109. stunda: «Kas ir monoma normālforma?»

Normālformā koeficients stāv priekšā, katrs burts parādās vienreiz,
burti - alfabēta secībā. Monoma pakāpe ir visu burtu kāpinātāju summa;
skaitlim (ne nullei) tā ir 0.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kas ir monoma normālforma?"

MERKIS = "Pārveidosim monomu normālformā un noteiksim tā pakāpi."

SATURS = [
    Sakums("3a · 2b · a - kā to uzrakstīt īsāk?",
           zimejums=restis([["3a · 2b · a", "→", "6a²b"]]),
           paraksts="Skaitļus sareizina, vienādus burtus - apvieno pakāpē.",
           fakti=["Normālformā koeficients priekšā, katrs burts vienreiz.",
                  "Burtus raksta alfabēta secībā.",
                  "Monoma pakāpe - visu kāpinātāju summa."]),

    Doma("Normālforma",
         "Normālformā monomu var salīdzināt ar citiem vienā skatienā.",
         soli=[
             "Sareizini visus skaitļus - tas ir koeficients.",
             "Vienādus burtus apvieno: a · a^2 = a^3.",
             "Burtus sakārto alfabēta secībā.",
             "Pakāpe: saskaiti kāpinātājus (x ir x^1).",
         ],
         pieze="Skaitļa 7 pakāpe ir 0, jo 7 = 7x^0."),

    Paraugs("Pārveido",
            uzd="Pārveido normālformā −2x^2y · 5xy^3 un nosaki pakāpi.",
            soli=[
                ("−2 · 5 = −10", "Koeficients."),
                ("x^2 · x = x^3; y · y^3 = y^4", "Vienādi burti."),
                ("−10x^3y^4", "Normālforma."),
                ("3 + 4 = 7", "Pakāpe."),
            ],
            atbilde="−10x^3y^4, pakāpe 7"),

    Ievadi("Normālforma", [
        {"jaut": "4a · 3a^2: koeficients?", "atb": ["12"],
         "padoms": "4 · 3."},
        {"jaut": "4a · 3a^2: pakāpe?", "atb": ["3"], "padoms": "a^3."},
        {"jaut": "x^2y · xy^3: pakāpe?", "atb": ["7"],
         "padoms": "x^3y^4."},
        {"jaut": "Skaitļa 5 pakāpe?", "atb": ["0"],
         "padoms": "Nav neviena burta."},
        {"jaut": "−3ab^2c: pakāpe?", "atb": ["4"], "padoms": "1 + 2 + 1."},
        {"jaut": "2x · (−x) · 3y: koeficients?", "atb": ["−6", "-6"],
         "padoms": "2 · (−1) · 3."},
    ], pamats=4),

    Varianti("Kura ir normālforma?", [
        {"jaut": "Izvēlies monomu normālformā.",
         "opcijas": ["3a^2b", "a · 3ab", "ba · 3a", "3 · a · a · b"],
         "pareizi": 0, "padoms": "Koeficients priekšā, katrs burts "
                                 "vienreiz."},
        {"jaut": "Monoma 5x^2y^3 pakāpe ir...",
         "opcijas": ["5", "6", "3", "2"],
         "pareizi": 0, "padoms": "2 + 3; koeficientu neskaita."},
        {"jaut": "Kuri monomi ir līdzīgi (atšķiras tikai ar koeficientu)?",
         "opcijas": ["3a^2b un −a^2b", "3a^2b un 3ab^2", "a^2 un a^3",
                     "ab un a"],
         "pareizi": 0, "padoms": "Tā pati burtu daļa."},
    ]),

    Pasaule("Kastes tilpums",
            Ievadi("", [
                {"jaut": "Kaste: garums 2a, platums a, augstums 3a. Tilpums "
                         "normālformā = ?a^3",
                 "atb": ["6"], "padoms": "2 · 1 · 3."},
                {"jaut": "Tilpuma monoma pakāpe?", "atb": ["3"],
                 "padoms": "a^3."},
                {"jaut": "a = 10 cm. Tilpums (cm³)?", "atb": ["6000"],
                 "padoms": "6 · 1000."},
            ]),
            pavediens="maja",
            konteksts="Tilpums ir trīs garumu reizinājums, tāpēc tā monoma "
                      "pakāpe ir 3.",
            kapec="Pakāpe parāda mērvienību: m, m², m³."),

    Kopsavilkums([
        "Pārveidoju monomu normālformā.",
        "Nosaku monoma pakāpi.",
        "Atpazīstu līdzīgus monomus.",
    ]),

    Majas([
        "Pārveido normālformā: 2a · 5b · a^2; −x · 4y · x.",
        "Nosaki katra monoma pakāpi.",
        "Izdomā divus līdzīgus monomus ar dažādiem koeficientiem.",
    ]),
]
