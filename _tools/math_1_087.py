# -*- coding: utf-8 -*-
"""1. klase, 87. stunda: «Kā sadalīt otro saskaitāmo?»

Otro saskaitāmo sadala divās daļās - viena papildina līdz 10, otra ir
atlikums. Soļus pieraksta: 9 + 6 = 9 + 1 + 5 = 10 + 5 = 15. Te noder
skaitļa mājiņa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, majina)

TEMA = "Kā sadalīt otro saskaitāmo?"

MERKIS = ("Šodien saskaitīsim ar desmita pāriešanu, sadalot otro "
          "saskaitāmo, un pierakstīsim soļus.")

SATURS = [
    Sakums("9 + 6: kā sadalīt 6?",
           zimejums=majina(6, [(1, 5)]),
           paraksts="6 = 1 + 5: 1 līdz desmitam, 5 atlikumā.",
           fakti=["Pirmā daļa - līdz 10.",
                  "Otrā daļa - atlikums.",
                  "9 + 6 = 9 + 1 + 5 = 15."]),

    Slidnis("Soļi", [
        {"v": "9 + 6", "teksts": "Cik trūkst līdz 10? - 1",
         "zim": majina(6, [(1, None)])},
        {"v": "9 + 1 + 5", "teksts": "6 = 1 + 5",
         "zim": majina(6, [(1, 5)])},
        {"v": "10 + 5 = 15", "teksts": "Desmits un atlikums",
         "zim": majina(15, [(10, 5)])},
    ]),

    Doma("Sadali un saskaiti",
         "Mājiņa palīdz sadalīt otro skaitli pareizi.",
         soli=[
             "Cik pirmajam trūkst līdz 10?",
             "Sadali otro skaitli: tik + atlikums.",
             "Pieraksti: 9 + 6 = 9 + 1 + 5 = 10 + 5 = 15.",
         ]),

    Ievadi("Sadali", [
        {"jaut": "8 + 4 = 8 + 2 + ?", "atb": ["2"], "padoms": "4 = 2 + 2."},
        {"jaut": "7 + 6 = 7 + 3 + ?", "atb": ["3"], "padoms": "6 = 3 + 3."},
        {"jaut": "9 + 8 = 9 + 1 + ?", "atb": ["7"], "padoms": "8 = 1 + 7."},
        {"jaut": "6 + 5 = 6 + ? + 1", "atb": ["4"], "padoms": "6 + 4 = 10."},
        {"jaut": "8 + 9 = ?", "atb": ["17"], "padoms": "8 + 2 + 7."},
        {"jaut": "5 + 7 = ?", "atb": ["12"], "padoms": "5 + 5 + 2."},
    ], pamats=4),

    Varianti("Kurš sadalījums der?", [
        {"jaut": "7 + 5 = 7 + ? + ?",
         "opcijas": ["3 + 2", "1 + 4", "5 + 0"], "pareizi": 0,
         "padoms": "7 + 3 = 10."},
        {"jaut": "9 + 7 = 9 + ? + ?",
         "opcijas": ["1 + 6", "2 + 5", "3 + 4"], "pareizi": 0,
         "padoms": "9 + 1 = 10."},
    ]),

    Pasaule("Pogas rāmjos",
            Ievadi("", [
                {"jaut": "Šujot 8 pogām pievieno 5. Cik pogu? (caur 10)",
                 "atb": ["13"], "padoms": "8 + 2 + 3."},
            ]),
            pavediens="maja",
            konteksts="Pogas glabā kastītēs pa 10.",
            kapec="Sadalot otro skaitli, rēķins kļūst viegls."),

    Kopsavilkums([
        "Sadalu otro saskaitāmo divās daļās.",
        "Papildinu līdz 10.",
        "Pierakstu visus soļus.",
    ]),

    Majas([
        "Pieraksti ar soļiem 9 + 5, 8 + 6, 7 + 8.",
        "Parādi ar mājiņu, kā sadalīji.",
        "Paskaidro mājiniekam.",
    ]),
]
