# -*- coding: utf-8 -*-
"""1. klase, 60. stunda: «Kur dzīvē redzam simtu?»

Simts ir 10 desmiti jeb 100 vieni. Dzīvē: 100 centu ir 1 eiro, grāmatā
ap 100 lappušu, 100 soļi. Simtu raksta ar trim cipariem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, desmiti)

TEMA = "Kur dzīvē redzam simtu?"

MERKIS = ("Šodien uzzināsim, ka simts ir 10 desmiti, un atradīsim simtu "
          "dzīvē.")

SATURS = [
    Sakums("Cik desmitu ir simtā?",
           zimejums=desmiti(10, 0),
           paraksts="10 stieņi pa 10 - 100.",
           fakti=["Simts = 10 desmiti = 100 vieni.",
                  "100 centi = 1 eiro.",
                  "Simtu raksta ar trim cipariem: 100."]),

    Doma("Simts",
         "Kad desmitu ir 10, tos saliek vienā simtā - tāpat kā 10 vienus "
         "vienā desmitā.",
         soli=[
             "Skaiti desmitus: 10, 20, 30 ... 90, 100.",
             "Pēc 99 nāk 100.",
             "100 raksta: 1, 0, 0.",
         ]),

    Ievadi("Simts", [
        {"jaut": "Cik desmitu ir 100?", "atb": ["10"],
         "padoms": "10, 20 ... 100."},
        {"jaut": "Cik pietrūkst līdz 100, ja ir 9 desmiti?", "zim":
         desmiti(9, 0), "atb": ["10"], "padoms": "Vēl viens desmits."},
        {"jaut": "Kurš skaitlis ir pēc 99?", "atb": ["100"],
         "padoms": "Nākamais."},
        {"jaut": "Cik centu ir 1 eiro?", "atb": ["100"],
         "padoms": "Simts centu."},
    ]),

    Varianti("Kur ir apmēram simts?", [
        {"jaut": "Kas var būt apmēram 100?",
         "opcijas": ["lappuses grāmatā", "pirksti rokā",
                     "kājas galdam"], "pareizi": 0,
         "padoms": "Grāmatas ir biezas."},
        {"jaut": "Kas ir vairāk nekā 100?",
         "opcijas": ["matu uz galvas", "bērnu ģimenē", "dienu nedēļā"],
         "pareizi": 0, "padoms": "Matu ir ļoti daudz."},
    ]),

    Pasaule("Simts soļi",
            Ievadi("", [
                {"jaut": "Līdz veikalam 100 soļu. Tu nogāji 60. Cik vēl?",
                 "atb": ["40"], "padoms": "No 60 līdz 100 - 4 desmiti."},
                {"jaut": "Tu nogāji 90. Cik vēl?", "atb": ["10"],
                 "padoms": "Viens desmits."},
            ]),
            pavediens="celojums",
            konteksts="Līdz veikalam no mājām ir tieši 100 soļu.",
            kapec="Simts ir mērs, ko var sajust ar kājām."),

    Kopsavilkums([
        "Zinu, ka simts ir 10 desmiti.",
        "Zinu, ka 100 centu ir 1 eiro.",
        "Atrodu simtu dzīvē.",
    ]),

    Majas([
        "Noej 100 soļu un paskaties, cik tālu tas ir.",
        "Atrodi grāmatu ar vairāk nekā 100 lappusēm.",
        "Saskaiti līdz 100 pa 10.",
    ]),
]
