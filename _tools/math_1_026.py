# -*- coding: utf-8 -*-
"""1. klase, 26. stunda: «Kā pierakstīt tā, lai pats saproti?»

Divu aiļu tabula: lapu pārloka uz pusēm, katrai ailei virsraksts. Tabulā
dati stāv kārtīgi, un tos var nolasīt arī pēc nedēļas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā pierakstīt tā, lai pats saproti?"

MERKIS = ("Šodien izveidosim divu aiļu tabulu un ierakstīsim tajā savus "
          "datus.")

_TABULA = restis([["V", "O"], [3, 2], [1, 4], [5, 0], [2, 3]])

SATURS = [
    Sakums("Kur pierakstīt ripiņu iznākumus, lai nesajuktu?",
           zimejums=_TABULA,
           paraksts="Aile V - violetās, aile O - oranžās.",
           fakti=["Pārloki lapu uz pusēm - ir divas ailes.",
                  "Katrai ailei - virsraksts.",
                  "Katrs iznākums - jaunā rindā."]),

    Doma("Tabula kārtīgam pierakstam",
         "Tabulā katram skaitlim ir sava vieta, tāpēc to var izlasīt arī "
         "vēlāk.",
         soli=[
             "Pārloki lapu uz pusēm.",
             "Augšā uzraksti aiļu virsrakstus.",
             "Katru iznākumu ieraksti jaunā rindā.",
         ]),

    Ievadi("Nolasi tabulu", [
        {"jaut": "Cik oranžu bija pirmajā rindā?", "zim": _TABULA,
         "atb": ["2"], "padoms": "Aile O, pirmā rinda."},
        {"jaut": "Cik violetu bija trešajā rindā?", "zim": _TABULA,
         "atb": ["5"], "padoms": "Aile V, trešā rinda."},
        {"jaut": "Cik reizes izbēra ripiņas?", "zim": _TABULA,
         "atb": ["4"], "padoms": "Saskaiti rindas bez virsraksta."},
        {"jaut": "Cik ripiņu kopā katrā rindā?", "zim": _TABULA,
         "atb": ["5"], "padoms": "3 + 2."},
    ]),

    Varianti("Kāpēc tabula?", [
        {"jaut": "Kas notiek, ja aiļu virsrakstus neuzraksta?",
         "opcijas": ["nevar saprast, kas kur", "nekas",
                     "tabula ir skaistāka"], "pareizi": 0,
         "padoms": "Kā zināt, kura aile ir kura?"},
        {"jaut": "Kur ierakstīt nākamo iznākumu?",
         "opcijas": ["jaunā rindā apakšā", "virs virsraksta",
                     "tai pašā rindā"], "pareizi": 0,
         "padoms": "Katram iznākumam sava rinda."},
    ]),

    Petijums("Mana tabula", [
        "Pārloki lapu uz pusēm un novelc līniju.",
        "Uzraksti virsrakstus: «zēni» un «meitenes».",
        "Saskaiti katrā galdā sēdošos un ieraksti rindā.",
        "Nolasi: kurā galdā visvairāk meiteņu?",
    ], vajag="lapa, zīmulis, lineāls"),

    Pasaule("Laikapstākļi nedēļā",
            Ievadi("", [
                {"jaut": "Cik saulainu dienu?",
                 "zim": restis([["saule", "lietus"], [4, 3]]),
                 "atb": ["4"], "padoms": "Aile «saule»."},
                {"jaut": "Cik dienu kopā?", "atb": ["7"],
                 "padoms": "4 + 3."},
            ]),
            pavediens="planeta",
            konteksts="Klase nedēļu pierakstīja, vai spīdēja saule vai "
                      "lija.",
            kapec="Tabula ļauj salīdzināt, pat ja atceries vairs neko."),

    Kopsavilkums([
        "Izveidoju divu aiļu tabulu ar virsrakstiem.",
        "Ierakstu datus rindās.",
        "Nolasu datus no tabulas.",
    ]),

    Majas([
        "Izveido tabulu «karotes / dakšas» un saskaiti mājās.",
        "Nedēļu pieraksti tabulā: saule vai mākoņi.",
        "Parādi tabulu mājiniekiem un izstāsti to.",
    ]),
]
