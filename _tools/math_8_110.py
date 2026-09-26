# -*- coding: utf-8 -*-
"""8. klase, 110. stunda: «Kā reizina monomus?»

Koeficientus sareizina, pakāpes ar vienādu bāzi - saskaita kāpinātājus
(a^m · a^n = a^{m + n}, 8.2. temats). Rezultātu raksta normālformā.
Atbildes ieraksta ar ^ vai augšrakstu - lapa tās uzskata par vienādām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā reizina monomus?"

MERKIS = "Reizināsim monomus, lietojot pakāpju īpašības."

_T = "text"

SATURS = [
    Sakums("3a²b · (−4ab³) = ?",
           zimejums=restis([["3 · (−4)", "a² · a", "b · b³"],
                            ["−12", "a³", "b⁴"]]),
           paraksts="Rezultāts: −12a^3b^4.",
           fakti=["Koeficientus sareizina.",
                  "Vienādiem burtiem kāpinātājus saskaita.",
                  "Rezultātu raksta normālformā."]),

    Doma("Monomu reizināšana",
         "Reizina atsevišķi skaitļus un katru burtu.",
         soli=[
             "Sareizini koeficientus (ievēro zīmes).",
             "Katram burtam saskaiti kāpinātājus: a^m · a^n = a^{m + n}.",
             "Burts, kas ir tikai vienā reizinātājā, pāriet nemainīts.",
             "Pieraksti normālformā.",
         ]),

    Paraugs("Reizini",
            uzd="Aprēķini (3a^2b) · (−4ab^3) un 0,5x^3 · 6xy.",
            soli=[
                ("3 · (−4) = −12; a^2 · a = a^3; b · b^3 = b^4",
                 "Pa daļām."),
                ("−12a^3b^4", "Pirmais rezultāts."),
                ("0,5 · 6 = 3; x^3 · x = x^4; y", "Otrais."),
                ("3x^4y", "Normālforma."),
            ],
            atbilde="−12a^3b^4 un 3x^4y"),

    Ievadi("Sareizini (raksti normālformā)", [
        {"jaut": "a^2 · a^5", "atb": ["a^7"], "tastatura": _T,
         "padoms": "2 + 5."},
        {"jaut": "2x · 5x^3", "atb": ["10x^4"], "tastatura": _T,
         "padoms": "2 · 5 un 1 + 3."},
        {"jaut": "3ab · 2a", "atb": ["6a^2b"], "tastatura": _T,
         "padoms": "a · a = a^2."},
        {"jaut": "(−2x) · (−3x^2)", "atb": ["6x^3"], "tastatura": _T,
         "padoms": "Mīnuss reiz mīnuss."},
        {"jaut": "4a^3 · 0,5a", "atb": ["2a^4"], "tastatura": _T,
         "padoms": "4 · 0,5 = 2."},
        {"jaut": "−xy · x^2y^2", "atb": ["−x^3y^3", "-x^3y^3"],
         "tastatura": _T, "padoms": "Koeficients −1."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "a^3 · a^4 = ?",
         "opcijas": ["a^7", "a^12", "2a^7", "a^1"],
         "pareizi": 0, "padoms": "Kāpinātājus saskaita."},
        {"jaut": "5x · 5x = ?",
         "opcijas": ["25x^2", "10x", "25x", "10x^2"],
         "pareizi": 0, "padoms": "5 · 5 un x · x."},
        {"jaut": "2a · 3b = ?",
         "opcijas": ["6ab", "5ab", "6a + b", "23ab"],
         "pareizi": 0, "padoms": "Dažādi burti paliek blakus."},
    ]),

    Pasaule("Kastes tilpums",
            Ievadi("", [
                {"jaut": "Kaste 2a × 3a × 5a. Tilpums = ?a^3",
                 "atb": ["30"], "padoms": "2 · 3 · 5."},
                {"jaut": "a = 10 cm. Tilpums (cm³)?", "atb": ["30000"],
                 "padoms": "30 · 1000."},
                {"jaut": "Cik litru tas ir?", "atb": ["30"],
                 "padoms": "1 l = 1000 cm³."},
            ]),
            pavediens="maja",
            konteksts="Izmērus ar a var mainīt; monoms tūlīt parāda tilpumu "
                      "jebkuram a.",
            kapec="Reizinot monomus, reizina koeficientus un saskaita "
                  "kāpinātājus."),

    Kopsavilkums([
        "Sareizinu monomus.",
        "Lietoju a^m · a^n = a^{m + n}.",
        "Rakstu rezultātu normālformā.",
    ]),

    Majas([
        "Sareizini: 3x^2 · 4x^3; −2ab · 5a^2b.",
        "Aprēķini kastes a × 2a × 4a tilpumu, ja a = 5 cm.",
        "Izdomā divus monomus, kuru reizinājums ir 12x^5.",
    ]),
]
