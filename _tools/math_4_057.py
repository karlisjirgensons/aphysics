# -*- coding: utf-8 -*-
"""4. klase, 57. stunda: «Cik grādu ir taisnam leņķim?»

Grāds kā leņķa mērvienība. Taisns leņķis ir 90°, izstiepts - 180°, pilns
apgrieziens - 360°. Šaurs leņķis ir mazāks par taisnu, plats - lielāks par
taisnu, bet mazāks par izstieptu. Spriest par leņķa veidu var bez
transportiera - salīdzinot ar taisnu leņķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis, restis)

TEMA = "Cik grādu ir taisnam leņķim?"

MERKIS = ("Zināsim, ka taisns leņķis ir 90°, un spriedīsim par šaura un "
          "plata leņķa lielumu.")

SATURS = [
    Sakums("Kāpēc skeitbordists saka «trīssešdesmit»?",
           zimejums=restis([["apgrieziens", "grādi"],
                            ["ceturtdaļa", "90°"],
                            ["puse", "180°"],
                            ["pilns", "360°"]],
                           "grādi un apgriezieni"),
           paraksts="«360» nozīmē pilnu apgriezienu gaisā.",
           fakti=["Pilns apgrieziens ir 360 grādi.",
                  "Taisns leņķis - ceturtdaļa apgrieziena - ir 90°."]),

    Doma("Taisns leņķis ir 90°",
         "Leņķi mēra grādos (°): taisns - 90°, izstiepts - 180°; šaurs ir "
         "mazāks par 90°, plats - starp 90° un 180°.",
         soli=[
             "Šaurs leņķis: mazāks par 90°.",
             "Taisns leņķis: tieši 90°.",
             "Plats leņķis: lielāks par 90°, mazāks par 180°.",
             "Izstiepts leņķis: 180° - malas veido taisni.",
         ],
         pieze="Salīdzini ar burtnīcas stūri: ja leņķis ietilpst stūrī, tas "
               "ir šaurs."),

    Zimejums("Četri leņķu veidi",
             lenkis([(0, ""), (45, "šaurs"), (90, "taisns"), (135, "plats"),
                     (180, "")],
                    loki=[(0, 45, "45°"), (0, 90, ""), (0, 135, "")]),
             paskaidro="Visi leņķi mērīti no labās malas. 180° - izstiepts.",
             ievads="Viena nekustīgā mala - dažādi leņķi."),

    Paraugs("Kāds ir 120° leņķis?",
            uzd="Nosaki, kāds leņķis ir 120°.",
            soli=[
                ("120° > 90°", "Lielāks par taisnu."),
                ("120° < 180°", "Mazāks par izstieptu."),
            ],
            atbilde="plats leņķis"),

    Varianti("Kāds leņķis?", [
        {"jaut": "35°", "opcijas": ["šaurs", "taisns", "plats",
                                    "izstiepts"], "pareizi": 0,
         "padoms": "35 < 90."},
        {"jaut": "90°", "opcijas": ["taisns", "šaurs", "plats",
                                    "izstiepts"], "pareizi": 0,
         "padoms": "Tieši 90."},
        {"jaut": "150°", "opcijas": ["plats", "šaurs", "taisns",
                                     "izstiepts"], "pareizi": 0,
         "padoms": "Starp 90 un 180."},
        {"jaut": "180°", "opcijas": ["izstiepts", "plats", "taisns",
                                     "šaurs"], "pareizi": 0,
         "padoms": "Malas vienā taisnē."},
        {"jaut": "89°", "opcijas": ["šaurs", "taisns", "plats",
                                    "izstiepts"], "pareizi": 0,
         "padoms": "Mazāks par 90, kaut ļoti tuvu."},
        {"jaut": "91°", "opcijas": ["plats", "taisns", "šaurs",
                                    "izstiepts"], "pareizi": 0,
         "padoms": "Mazliet lielāks par 90."},
    ], pamats=4),

    Ievadi("Grādi", [
        {"jaut": "Cik grādu ir divos taisnos leņķos kopā?", "atb": ["180"],
         "padoms": "90 + 90."},
        {"jaut": "Cik grādu ir pilnā apgriezienā?", "atb": ["360"],
         "padoms": "4 · 90."},
        {"jaut": "Par cik grādiem 90° lielāks nekā 35°?", "atb": ["55"],
         "padoms": "90 − 35."},
        {"jaut": "Cik grādu trūkst 130° leņķim līdz izstieptam?",
         "atb": ["50"], "padoms": "180 − 130."},
    ]),

    Pasaule("Skeitparka triki",
            Ievadi("", [
                {"jaut": "Triks «180» - puse apgrieziena. Cik grādu pagriežas "
                         "divos «180» pēc kārtas?",
                 "atb": ["360"], "padoms": "180 + 180."},
                {"jaut": "Triks «540» ir pilns apgrieziens un vēl cik "
                         "grādu?",
                 "atb": ["180"], "padoms": "540 − 360."},
                {"jaut": "Cik pilnu apgriezienu ir «900» trikā?",
                 "atb": ["2"], "padoms": "360 · 2 = 720, paliek 180."},
                {"jaut": "Rampa ir 40° leņķī pret zemi. Kāds leņķa veids? "
                         "Raksti «šaurs», «taisns» vai «plats».",
                 "atb": ["šaurs", "saurs"], "tastatura": "text",
                 "padoms": "40 < 90."},
            ]),
            pavediens="sports",
            konteksts="Skeitbordā un snovbordā trikus sauc grādos: 180, 360, "
                      "540, 720 un pat 1080.",
            kapec="Grādi ir leņķa valoda arī sportā."),

    Kopsavilkums([
        "Zinu, ka taisns leņķis ir 90°, izstiepts - 180°.",
        "Atšķiru šauru, taisnu, platu un izstieptu leņķi.",
        "Spriežu par leņķi, salīdzinot ar taisnu.",
    ]),

    Majas([
        "Atrodi mājās 3 šaurus un 3 platus leņķus.",
        "Paskaidro, kāpēc «360» skeitbordā nozīmē pilnu apgriezienu.",
        "Pārbaudi ar burtnīcas stūri, vai durvju leņķis ir taisns.",
    ]),
]
