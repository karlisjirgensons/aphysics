# -*- coding: utf-8 -*-
"""9. klase, 99. stunda: «Kā atrisināt sistēmu?»

Sistēma no lineāras un kvadrātnevienādības: katru atrisina atsevišķi, abas
atbildes iezīmē uz vienas skaitļu taisnes, atbilde ir kopīgā daļa
(šķēlums). Divi svītrojumi - dubultsvītrojums ir atbilde.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, taisne)

TEMA = "Kā atrisināt sistēmu?"

MERKIS = ("Atrisināsim sistēmu, kurā ir lineāra un kvadrātnevienādība.")

SATURS = [
    Sakums("Abām nevienādībām jāizpildās vienlaikus",
           zimejums=taisne(-4, 6, 1, atzimes=[(-2, "−2"), (1, "1"),
                                              (3, "3")],
                           intervali=[(-2, 3, False, False),
                                      (1, None, True, False)]),
           paraksts="x² − x − 6 < 0 un x ≥ 1: kopīgā daļa [1; 3).",
           fakti=["Pirmā: −2 < x < 3.",
                  "Otrā: x ≥ 1.",
                  "Sistēma: 1 ≤ x < 3 - tur, kur abi svītrojumi."]),

    Doma("Sistēmas atrisināšana",
         "Atrisini katru nevienādību, iezīmē abas uz vienas taisnes un ņem "
         "kopīgo daļu.",
         soli=[
             "Lineārā: pārnes un dali (ar negatīvu - zīme mainās!).",
             "Kvadrātnevienādība: nulles + skice.",
             "Abas atbildes uz vienas taisnes.",
             "Atbilde - kur abi svītrojumi pārklājas.",
             "Ja pārklājuma nav - sistēmai nav atrisinājuma.",
         ]),

    Slidnis("Pa soļiem", [
        {"v": "1", "teksts": "x^2 − x − 6 < 0 ⇒ −2 < x < 3",
         "zim": taisne(-4, 6, 1, atzimes=[(-2, "−2"), (3, "3")],
                       intervali=[(-2, 3, False, False)])},
        {"v": "2", "teksts": "2x − 2 ≥ 0 ⇒ x ≥ 1",
         "zim": taisne(-4, 6, 1, atzimes=[(1, "1")],
                       intervali=[(1, None, True, False)])},
        {"v": "3", "teksts": "Kopīgā daļa: x ∈ [1; 3)",
         "zim": taisne(-4, 6, 1, atzimes=[(1, "1"), (3, "3")],
                       intervali=[(1, 3, True, False)])},
    ]),

    Paraugs("Sistēma",
            uzd="Atrisini sistēmu: x^2 − 4 ≥ 0 un x < 5.",
            soli=[
                ("x ≤ −2 vai x ≥ 2", "Kvadrātnevienādība."),
                ("x < 5", "Lineārā."),
                ("x ≤ −2 vai 2 ≤ x < 5", "Kopīgā daļa."),
            ],
            atbilde="x ∈ (−∞; −2] ∪ [2; 5)"),

    Varianti("Kopīgā daļa", [
        {"jaut": "−1 < x < 4 un x > 2",
         "opcijas": ["2 < x < 4", "−1 < x < 2", "x > −1", "nav"],
         "pareizi": 0, "padoms": "Pārklājums."},
        {"jaut": "x < 0 un x > 3",
         "opcijas": ["nav atrisinājuma", "0 < x < 3", "visi x", "x = 0"],
         "pareizi": 0, "padoms": "Nepārklājas."},
        {"jaut": "x^2 ≤ 9 un x ≥ 0",
         "opcijas": ["[0; 3]", "[−3; 3]", "[0; +∞)", "[3; +∞)"],
         "pareizi": 0, "padoms": "−3 ≤ x ≤ 3 un x ≥ 0."},
    ]),

    Ievadi("Atrisini sistēmu (atbilde - galapunkts vai skaits)", [
        {"jaut": "x^2 − 5x < 0 un x ≥ 2: mazākais atrisinājums?",
         "atb": ["2"], "padoms": "0 < x < 5 un x ≥ 2."},
        {"jaut": "Tai pašai: cik veselu atrisinājumu?", "atb": ["3"],
         "padoms": "2, 3, 4."},
        {"jaut": "x^2 ≤ 16 un 3x − 6 > 0: lielākais atrisinājums?",
         "atb": ["4"], "padoms": "−4 ≤ x ≤ 4 un x > 2."},
    ]),

    Pasaule("Ātruma ierobežojums",
            Ievadi("", [
                {"jaut": "Bremzēšanas ceļš s = 0,01v^2 + 0,2v (m) nedrīkst "
                         "pārsniegt 48 m, un ātrums ≥ 30 km/h. Lielākais "
                         "atļautais ātrums (km/h)?", "atb": ["60"],
                 "padoms": "v^2 + 20v − 4800 ≤ 0; nulles −80 un 60."},
                {"jaut": "Cik m ir bremzēšanas ceļš pie 30 km/h?",
                 "atb": ["15"], "padoms": "9 + 6."},
            ]),
            pavediens="celojums",
            konteksts="Bremzēšanas ceļš aug kvadrātiski - tāpēc pilsētā ātrums "
                      "ir ierobežots.",
            kapec="Sistēma apvieno fizikas un likuma prasības."),

    Kopsavilkums([
        "Atrisinu katru sistēmas nevienādību.",
        "Atrodu kopīgo daļu uz skaitļu taisnes.",
        "Pierakstu atbildi ar intervāliem.",
    ]),

    Majas([
        "Atrisini: x^2 − 2x − 8 ≤ 0 un x > 0.",
        "Atrisini: x^2 > 1 un x < 3.",
        "Uzraksti sistēmu, kuras atbilde ir [0; 2].",
    ]),
]
