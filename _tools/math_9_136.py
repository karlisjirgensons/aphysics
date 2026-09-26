# -*- coding: utf-8 -*-
"""9. klase, 136. stunda: «Kā saskaitīt pirmos locekļus?»

S_n = {(a_1 + a_n)n|2} (formulu lapā). Iegūst, uzrakstot summu divreiz -
uz priekšu un atpakaļ: katrs pāris dod a_1 + a_n, pāru ir n. Tāpat kā
kāpnes no kubiem, saliktas ar apgrieztu kopiju, veido taisnstūri.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā saskaitīt pirmos locekļus?"

MERKIS = ("Iegūsim un lietosim pirmo n locekļu summas formulu.")

SATURS = [
    Sakums("3 + 5 + 7 + 9 + 11 - divreiz",
           zimejums=restis([["S", "3", "5", "7", "9", "11"],
                            ["S", "11", "9", "7", "5", "3"],
                            ["2S", "14", "14", "14", "14", "14"]]),
           paraksts="2S = 5 · 14 ⇒ S = 35.",
           fakti=["Katrā kolonnā summa ir a_1 + a_n = 14.",
                  "Kolonnu ir n = 5.",
                  "S_n = {(a_1 + a_n)n|2}."]),

    Doma("Summas formula",
         "S_n = {(a_1 + a_n) · n|2}; ja a_n nav zināms, vispirms "
         "a_n = a_1 + (n − 1)d.",
         soli=[
             "Nosaki a_1, a_n un n.",
             "Saskaiti pirmo un pēdējo.",
             "Reizini ar locekļu skaitu.",
             "Dali ar 2.",
         ]),

    Slidnis("Kāpēc formula strādā", [
        {"v": "1", "teksts": "S = a_1 + a_2 + ... + a_n"},
        {"v": "2", "teksts": "S = a_n + a_{n−1} + ... + a_1 (atpakaļ)"},
        {"v": "3", "teksts": "Katrs pāris: a_1 + a_n (d pieskaitās un "
                             "atņemas)"},
        {"v": "4", "teksts": "2S = n(a_1 + a_n) ⇒ S = {(a_1 + a_n)n|2}"},
    ]),

    Paraugs("Ar diferenci",
            uzd="Atrodi progresijas 4, 7, 10, ... pirmo 20 locekļu summu.",
            soli=[
                ("a_{20} = 4 + 19 · 3 = 61", "Pēdējais loceklis."),
                ("S_{20} = {(4 + 61) · 20|2}", "Formula."),
                ("= 65 · 10 = 650", "Aprēķins."),
            ],
            atbilde="650"),

    Ievadi("Aprēķini summu", [
        {"jaut": "a_1 = 2, a_{10} = 20. S_{10} = ?", "atb": ["110"],
         "padoms": "{22 · 10|2}."},
        {"jaut": "1 + 3 + 5 + ... + 19 (10 locekļi) = ?", "atb": ["100"],
         "padoms": "{20 · 10|2}."},
        {"jaut": "a_1 = 5, d = 5. S_8 = ?", "atb": ["180"],
         "padoms": "a_8 = 40; {45 · 8|2}."},
        {"jaut": "a_1 = 30, d = −4. S_6 = ?", "atb": ["120"],
         "padoms": "a_6 = 10; {40 · 6|2}."},
        {"jaut": "Pirmo 50 pāra skaitļu summa (2 + 4 + ... + 100)?",
         "atb": ["2550", "2 550"], "padoms": "{102 · 50|2}."},
    ], pamats=3),

    Varianti("Pārbaudi", [
        {"jaut": "Nepāra skaitļu summa 1 + 3 + ... (n locekļi) ir...",
         "opcijas": ["n^2", "2n", "n(n + 1)", "{n|2}"],
         "pareizi": 0, "padoms": "{(1 + 2n − 1)n|2}."},
        {"jaut": "S_5 = 35 un a_1 = 3. a_5 = ?",
         "opcijas": ["11", "7", "32", "14"],
         "pareizi": 0, "padoms": "{(3 + a_5) · 5|2} = 35."},
    ]),

    Pasaule("Amfiteātra sēdvietas",
            Ievadi("", [
                {"jaut": "1. rindā 30 vietu, katrā nākamajā par 2 vairāk, rindu "
                         "ir 15. Vietu pēdējā rindā?", "atb": ["58"],
                 "padoms": "30 + 14 · 2."},
                {"jaut": "Cik vietu kopā?", "atb": ["660"],
                 "padoms": "{(30 + 58) · 15|2}."},
            ]),
            pavediens="skola",
            konteksts="Skolas aktu zāle ar pakāpienveida rindām - katrā "
                      "nākamajā rindā divas vietas vairāk.",
            kapec="Summas formula saskaita visu zāli vienā rindiņā."),

    Kopsavilkums([
        "Zinu, kā iegūst summas formulu.",
        "Aprēķinu S_n ar a_1, a_n un n.",
        "Vajadzības gadījumā vispirms atrodu a_n.",
    ]),

    Majas([
        "Atrodi 5 + 9 + 13 + ... (15 locekļi).",
        "Cik ir visu divciparu skaitļu summa?",
        "Pārbaudi: vai pirmo n nepāra skaitļu summa ir n^2 (n = 1, 2, 3, 4)?",
    ]),
]
