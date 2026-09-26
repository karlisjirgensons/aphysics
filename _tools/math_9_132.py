# -*- coding: utf-8 -*-
"""9. klase, 132. stunda: «Kā atrast diferenci un pirmo locekli?»

Ja zināmi divi locekļi, starp tiem ir (m − k) soļi: d = {a_m − a_k|m − k}.
Tad a_1 atrod, ejot atpakaļ. Tā ir arī sistēma ar diviem nezināmajiem
(a_1 un d) - saikne ar 9.6. tematu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, taisne)

TEMA = "Kā atrast diferenci un pirmo locekli?"

MERKIS = ("Aprēķināsim diferenci un pirmo locekli, ja zināmi divi locekļi.")

SATURS = [
    Sakums("a₃ = 11 un a₇ = 23. Kāds ir solis?",
           zimejums=taisne(0, 26, 2, atzimes=[(11, "a₃"), (23, "a₇")],
                           bultas=[(11, 23, "4d = 12")]),
           paraksts="No a₃ līdz a₇ - 4 soļi: d = 12 : 4 = 3.",
           fakti=["d = {a_7 − a_3|7 − 3} = 3.",
                  "a_1 = a_3 − 2d = 11 − 6 = 5.",
                  "Tas pats ar sistēmu: a_1 + 2d = 11, a_1 + 6d = 23."]),

    Doma("Divi locekļi → d un a_1",
         "d = {a_m − a_k|m − k}; tad a_1 = a_k − (k − 1)d.",
         soli=[
             "Starpība starp locekļiem.",
             "Dali ar soļu skaitu (numuru starpību).",
             "Ej atpakaļ līdz a_1.",
             "Pārbaudi ar otro doto locekli.",
         ]),

    Paraugs("Ar sistēmu",
            uzd="a_4 = 7, a_{10} = −11. Atrodi a_1 un d.",
            soli=[
                ("a_1 + 3d = 7 un a_1 + 9d = −11", "Formula divreiz."),
                ("6d = −18 ⇒ d = −3", "Atņem."),
                ("a_1 = 7 − 3 · (−3) = 16", "Ievieto."),
            ],
            atbilde="a_1 = 16, d = −3"),

    Ievadi("Aprēķini", [
        {"jaut": "a_2 = 8, a_5 = 20. d = ?", "atb": ["4"],
         "padoms": "12 : 3."},
        {"jaut": "Tai pašai a_1 = ?", "atb": ["4"], "padoms": "8 − 4."},
        {"jaut": "a_3 = 30, a_8 = 5. d = ?", "atb": ["−5", "-5"],
         "padoms": "−25 : 5."},
        {"jaut": "a_1 = 6, a_{11} = 36. d = ?", "atb": ["3"],
         "padoms": "30 : 10."},
        {"jaut": "a_5 = 17, d = 3. a_1 = ?", "atb": ["5"],
         "padoms": "17 − 12."},
    ], pamats=3),

    Varianti("Soļu skaits", [
        {"jaut": "Cik soļu no a_4 līdz a_{12}?",
         "opcijas": ["8", "12", "9", "4"],
         "pareizi": 0, "padoms": "12 − 4."},
        {"jaut": "a_2 = 5, a_6 = 5. d = ?",
         "opcijas": ["0", "5", "1", "nevar zināt"],
         "pareizi": 0, "padoms": "Nav pieauguma."},
    ]),

    Pasaule("Kalna ceļa temperatūra",
            Ievadi("", [
                {"jaut": "Kāpjot kalnā, temperatūra krīt vienmērīgi: 3. "
                         "pieturā 14 °C, 8. pieturā 4 °C. Par cik grādiem "
                         "mainās katrā pieturā?", "atb": ["−2", "-2"],
                 "padoms": "(4 − 14) : 5."},
                {"jaut": "Cik °C bija 1. pieturā?", "atb": ["18"],
                 "padoms": "14 + 4."},
            ]),
            pavediens="celojums",
            konteksts="Kalnos temperatūra krītas aptuveni vienmērīgi līdz ar "
                      "augstumu.",
            kapec="Divi mērījumi pietiek, lai atrastu visu virkni."),

    Kopsavilkums([
        "Atrodu d no diviem locekļiem.",
        "Atrodu a_1, ejot atpakaļ.",
        "Risinu to arī ar sistēmu.",
    ]),

    Majas([
        "a_6 = 25, a_{11} = 45. Atrodi a_1 un d.",
        "a_2 = −1, a_7 = 14. Atrodi a_{20}.",
        "Pārbaudi atbildes, izrakstot locekļus.",
    ]),
]
