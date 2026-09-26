# -*- coding: utf-8 -*-
"""1. klase, 58. stunda: «Kā uzrakstīt to, ko dzirdi?»

Diktātā skaitli dzird kā vārdus - «trīsdesmit septiņi» - un pieraksta ar
cipariem: 37. «-desmit» nosauc desmitus, beigu vārds - vienus. Ja vienu
nav («piecdesmit»), otrajā vietā raksta 0.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, desmiti)

TEMA = "Kā uzrakstīt to, ko dzirdi?"

MERKIS = ("Šodien pierakstīsim nosauktus skaitļus līdz 100 ar cipariem un "
          "izlasīsim uzrakstītus.")

SATURS = [
    Sakums("«Trīsdesmit septiņi» - kā to uzrakstīt?",
           zimejums=desmiti(3, 7),
           paraksts="Trīsdesmit - 3 desmiti, septiņi - 7 vieni: 37.",
           fakti=["Vārds ar «-desmit» - desmiti.",
                  "Beigu vārds - vieni.",
                  "Ja vienu nav, raksti 0: piecdesmit - 50."]),

    Doma("No vārda uz cipariem",
         "Klausies pa daļām: vispirms desmiti, tad vieni.",
         soli=[
             "Dzirdi «...desmit» - uzraksti desmitu ciparu.",
             "Dzirdi beigu vārdu - uzraksti vienu ciparu.",
             "Beigu vārda nav? Raksti 0.",
         ],
         pieze="Skaitļi no 11 līdz 19 ir ar «-padsmit»: četrpadsmit - 14."),

    Ievadi("Uzraksti ar cipariem", [
        {"jaut": "trīsdesmit septiņi", "atb": ["37"],
         "padoms": "3 desmiti, 7 vieni."},
        {"jaut": "piecdesmit", "atb": ["50"], "padoms": "Vienu nav - 0."},
        {"jaut": "astoņdesmit divi", "atb": ["82"],
         "padoms": "8 desmiti, 2 vieni."},
        {"jaut": "deviņpadsmit", "atb": ["19"], "padoms": "Desmits un 9."},
        {"jaut": "sešdesmit četri", "atb": ["64"],
         "padoms": "6 desmiti, 4 vieni."},
        {"jaut": "divdesmit viens", "atb": ["21"],
         "padoms": "2 desmiti, 1 viens."},
    ], pamats=4),

    Varianti("Izlasi", [
        {"jaut": "48", "opcijas": ["četrdesmit astoņi",
                                   "astoņdesmit četri", "četrpadsmit"],
         "pareizi": 0, "padoms": "4 desmiti, 8 vieni."},
        {"jaut": "90", "opcijas": ["deviņdesmit", "deviņi",
                                   "deviņpadsmit"], "pareizi": 0,
         "padoms": "9 desmiti."},
        {"jaut": "15", "opcijas": ["piecpadsmit", "piecdesmit",
                                   "piecdesmit viens"], "pareizi": 0,
         "padoms": "Desmits un 5."},
    ]),

    Pasaule("Autobusa numurs",
            Ievadi("", [
                {"jaut": "Pieturā saka: «Pienāk autobuss numur trīsdesmit "
                         "trīs.» Kāds numurs?", "atb": ["33"],
                 "padoms": "3 desmiti, 3 vieni."},
                {"jaut": "«Tramvajs numur septiņi.»", "atb": ["7"],
                 "padoms": "Tikai vieni."},
            ]),
            pavediens="celojums",
            konteksts="Pieturā numurus bieži paziņo balsī.",
            kapec="Dzirdētu numuru jāpazīst uz autobusa."),

    Kopsavilkums([
        "Pierakstu dzirdētus skaitļus ar cipariem.",
        "Lasu divciparu skaitļus.",
        "Zinu, kad rakstīt 0.",
    ]),

    Majas([
        "Lai kāds nosauc 5 skaitļus, tu uzraksti.",
        "Nosauc skaļi dzīvokļu vai māju numurus uz ielas.",
        "Uzraksti savu tālruņa numura ciparus un izlasi pa pāriem.",
    ]),
]
