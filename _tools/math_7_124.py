# -*- coding: utf-8 -*-
"""7. klase, 124. stunda: «Kā iznest kopīgo reizinātāju?»

Iznešana pirms iekavām ir iekavu atvēršana otrādi: 6x + 9 = 3(2x + 3).
Kopīgais reizinātājs ir visu saskaitāmo lielākais kopīgais dalītājs -
tas pats LKD, ko lietojām daļām, tikai tagad arī ar burtiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā iznest kopīgo reizinātāju?"

MERKIS = ("Sadalīsim izteiksmi reizinātājos, iznesot kopīgo reizinātāju "
          "pirms iekavām.")

SATURS = [
    Sakums("Iekavas otrādi",
           zimejums=restis([["atvērt →", "3(2x + 3) = 6x + 9"],
                            ["← iznest", "6x + 9 = 3(2x + 3)"]]),
           fakti=["Atverot iekavas, reizina.",
                  "Iznesot - dala katru saskaitāmo ar kopīgo reizinātāju.",
                  "Pārbaude: atver iekavas atpakaļ."]),

    Doma("Atrodi kopīgo, izdali katru",
         "Lai iznestu kopīgo reizinātāju, atrod skaitli (un burtu), ar ko "
         "dalās visi saskaitāmie, uzraksta to pirms iekavām un iekavās "
         "ieraksta katra saskaitāmā dalījumu.",
         soli=[
             "Atrodi koeficientu LKD.",
             "Pārbaudi, vai kāds burts ir visos saskaitāmajos.",
             "Uzraksti kopīgo reizinātāju pirms iekavām.",
             "Iekavās - katrs saskaitāmais, izdalīts ar to.",
             "Pārbaudi, atverot iekavas.",
         ],
         pieze="Ja saskaitāmais ir tieši kopīgais reizinātājs, iekavās paliek "
               "1: 5a + 5 = 5(a + 1), nevis 5(a + 0)."),

    Paraugs("Iznes kopīgo",
            uzd="Sadali reizinātājos: 12ab − 18a.",
            soli=[
                ("LKD(12; 18) = 6", "Skaitļi."),
                ("a ir abos", "Burts."),
                ("6a(2b − 3)", "12ab : 6a = 2b; 18a : 6a = 3."),
                ("Pārbaude: 6a · 2b − 6a · 3 = 12ab − 18a", "Sakrīt."),
            ],
            atbilde="6a(2b − 3)"),

    Ievadi("Iznes kopīgo reizinātāju", [
        {"jaut": "4x + 8 = 4(x + ?)",
         "atb": ["2"], "padoms": "8 : 4."},
        {"jaut": "15a − 10 = 5(? − 2) - ko raksta jautājuma vietā?",
         "atb": ["3a"], "padoms": "15a : 5.", "tastatura": "text"},
        {"jaut": "7m + 7 = ?",
         "atb": ["7(m + 1)", "7(m+1)", "7(1+m)"], "padoms": "7 : 7 = 1.",
         "tastatura": "text"},
        {"jaut": "x² + 3x = ?",
         "atb": ["x(x + 3)", "x(x+3)"], "padoms": "x abos.",
         "tastatura": "text"},
        {"jaut": "20y − 30 = 10(? ) - raksti izteiksmi iekavās",
         "atb": ["2y − 3", "2y-3"], "padoms": "20y : 10 un 30 : 10.",
         "tastatura": "text"},
        {"jaut": "Aprēķini ērti: 37 · 13 + 37 · 87 = ?",
         "atb": ["3700"], "padoms": "37(13 + 87)."},
    ], pamats=4),

    Varianti("Pareizi iznests?", [
        {"jaut": "6x + 3 = 3(2x)",
         "opcijas": ["Nē - jābūt 3(2x + 1)", "Jā", "Nē - 6(x + 3)",
                     "Nē - 3(x + 1)"],
         "pareizi": 0, "padoms": "3 : 3 = 1."},
        {"jaut": "8a − 12 = 4(2a − 3)",
         "opcijas": ["Jā", "Nē - 2(4a − 6) ir labāk", "Nē - 4(2a − 12)",
                     "Nē - 8(a − 12)"],
         "pareizi": 0, "padoms": "Iznests LKD 4."},
        {"jaut": "8a − 12 = 2(4a − 6). Vai tas ir pilnīgi?",
         "opcijas": ["Nē - var iznest vēl 2", "Jā",
                     "Nav pareizi vispār", "Jāatver"],
         "pareizi": 0, "padoms": "4a − 6 dalās ar 2."},
    ]),

    Pasaule("Ātrā rēķināšana veikalā",
            Ievadi("", [
                {"jaut": "3 preces pa 4,99 € un 7 preces pa 4,99 €. Cik €? "
                         "(4,99 · 10)",
                 "atb": ["49,9"], "padoms": "4,99(3 + 7)."},
                {"jaut": "Grupā 25 cilvēki, biļete 12 €, gids 3 € katram: "
                         "25 · 12 + 25 · 3 = ?",
                 "atb": ["375"], "padoms": "25(12 + 3) = 25 · 15."},
                {"jaut": "Cik € katrs maksā kopā?",
                 "atb": ["15"], "padoms": "12 + 3."},
            ]),
            pavediens="veikals",
            konteksts="Kasieri un pārdevēji iznes kopīgo reizinātāju galvā - "
                      "tā ir ātrāk nekā reizināt katru.",
            kapec="a · b + a · c = a(b + c) - ātrāks rēķins."),

    Kopsavilkums([
        "Atrodu kopīgo reizinātāju (LKD un kopīgos burtus).",
        "Iznesu to pirms iekavām.",
        "Iekavās rakstu katra saskaitāmā dalījumu.",
        "Pārbaudu, atverot iekavas.",
    ]),

    Majas([
        "Sadali reizinātājos: 14x − 21, 9a² + 3a, 10mn − 5n.",
        "Aprēķini ērti: 58 · 17 + 42 · 17.",
        "Pārbaudi katru, atverot iekavas.",
    ]),
]
