# -*- coding: utf-8 -*-
"""4. klase, 144. stunda: «Kā lielāku vienību izteikt mazākā?»

Laukuma vienību kāpnes: 1 m² = 100 dm² = 10 000 cm², 1 cm² = 100 mm².
Katrs pakāpiens ir 100, nevis 10 - tāpēc laukuma pārvēršana atšķiras no
garuma pārvēršanas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā lielāku vienību izteikt mazākā?"

MERKIS = ("Izteiksim lielākas laukuma mērvienības mazākās un otrādi.")

SATURS = [
    Sakums("Kāpnes ar pakāpieniem pa 100",
           zimejums=restis([["mm²", "cm²", "dm²", "m²"],
                            ["· 100", "· 100", "· 100", ""]],
                           "laukuma vienības"),
           paraksts="1 m² = 100 dm² = 10 000 cm².",
           fakti=["Garumam pakāpiens 10, laukumam - 100.",
                  "Jo 10 · 10 = 100."]),

    Doma("Laukumā katrs pakāpiens ir 100",
         "Pārvēršot lielāku laukuma vienību blakus mazākajā, reizina ar 100; "
         "mazāku lielākajā - dala ar 100.",
         soli=[
             "m² → dm²: · 100.",
             "dm² → cm²: · 100.",
             "cm² → mm²: · 100.",
             "Uz augšu - dala ar 100.",
         ],
         pieze="3 m² = 300 dm² = 30 000 cm²."),

    Paraugs("5 m² dm²",
            uzd="Izsaki 5 m² kvadrātdecimetros.",
            soli=[
                ("1 m² = 100 dm²", None),
                ("5 · 100 = 500", None),
            ],
            atbilde="500 dm²"),

    Ievadi("Pārvērt", [
        {"jaut": "2 m² = ? dm²", "atb": ["200"], "padoms": "2 · 100."},
        {"jaut": "7 dm² = ? cm²", "atb": ["700"], "padoms": "7 · 100."},
        {"jaut": "4 cm² = ? mm²", "atb": ["400"], "padoms": "4 · 100."},
        {"jaut": "600 dm² = ? m²", "atb": ["6"], "padoms": "600 : 100."},
        {"jaut": "1 m² = ? cm²", "atb": ["10000", "10 000"],
         "padoms": "100 · 100."},
        {"jaut": "3 dm² 25 cm² = ? cm²", "atb": ["325"],
         "padoms": "300 + 25."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "Toms: 3 m² = 30 dm². Kļūda?",
         "opcijas": ["jāreizina ar 100: 300 dm²", "viss pareizi",
                     "jādala ar 10"], "pareizi": 0,
         "padoms": "Laukumam pakāpiens 100."},
        {"jaut": "Kas lielāks: 2 m² vai 150 dm²?",
         "opcijas": ["2 m²", "150 dm²", "vienādi"], "pareizi": 0,
         "padoms": "200 > 150."},
        {"jaut": "Kas lielāks: 5 dm² vai 480 cm²?",
         "opcijas": ["5 dm²", "480 cm²", "vienādi"], "pareizi": 0,
         "padoms": "500 > 480."},
    ]),

    Pasaule("Flīzes vannas istabā",
            Ievadi("", [
                {"jaut": "Siena 2 m². Cik dm²?", "atb": ["200"],
                 "padoms": "2 · 100."},
                {"jaut": "Viena flīze 1 dm × 1 dm = 1 dm². Cik flīžu vajag?",
                 "atb": ["200"], "padoms": "200 : 1."},
                {"jaut": "Lielāka flīze 4 dm². Cik tādu flīžu vajag?",
                 "atb": ["50"], "padoms": "200 : 4."},
                {"jaut": "Flīze maksā 3 €. Cik maksā 50 flīzes?",
                 "atb": ["150"], "padoms": "50 · 3."},
            ]),
            pavediens="maja",
            konteksts="Flīzētājs sienu mēra m², bet flīzes - dm²; bez "
                      "pārvēršanas nevar izrēķināt, cik pirkt.",
            kapec="Pareiza pārvēršana - pareizs flīžu skaits."),

    Kopsavilkums([
        "Pārvēršu laukuma vienības: m², dm², cm², mm².",
        "Zinu, ka pakāpiens ir 100.",
        "Salīdzinu laukumus dažādās vienībās.",
    ]),

    Majas([
        "Izmēri durvis un aprēķini laukumu dm² un m².",
        "Pārvērt: 4 m², 12 dm², 9 cm² mazākās vienībās.",
        "Paskaidro, kāpēc laukumam pakāpiens ir 100.",
    ]),
]
