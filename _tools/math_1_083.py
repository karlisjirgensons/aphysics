# -*- coding: utf-8 -*-
"""1. klase, 83. stunda: «Cik kopā maksā divas preces?»

Divu preču cenas saskaita: 12 € + 5 € = 17 €. Mērvienība (€) paliek. Tad
salīdzina ar naudu makā - vai pietiek?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, monetas)

TEMA = "Cik kopā maksā divas preces?"

MERKIS = ("Šodien saskaitīsim divu preču cenas 20 apjomā un noteiksim, vai "
          "pietiek naudas.")

SATURS = [
    Sakums("Bumba 12 €, pumpis 5 €. Cik kopā?",
           zimejums=monetas(["10 €", "2 €", "5 €"]),
           paraksts="12 € + 5 € = 17 €.",
           fakti=["Cenas saskaita.",
                  "€ raksta pie rezultāta.",
                  "Tad salīdzina ar naudu makā."]),

    Paraugs("Divas preces",
            uzd="Grāmata maksā 13 €, pildspalva 4 €. Cik maksā abas?",
            soli=[
                ("13 € + 4 €", "Kopā - saskaita."),
                ("= 17 €", "3 + 4 = 7, un desmits."),
            ],
            atbilde="abas preces maksā 17 €."),

    Doma("Pirkuma summa",
         "Kopējā cena ir visu cenu summa.",
         soli=[
             "Nolasi katras preces cenu.",
             "Saskaiti cenas.",
             "Uzraksti rezultātu ar €.",
         ]),

    Ievadi("Cik kopā?", [
        {"jaut": "Sula 2 €, maize 1 €. Kopā (€)?", "atb": ["3"],
         "padoms": "2 + 1."},
        {"jaut": "Lelle 14 €, kleitiņa 3 €. Kopā (€)?", "atb": ["17"],
         "padoms": "14 + 3."},
        {"jaut": "Mašīnīte 11 €, baterijas 6 €. Kopā (€)?", "atb": ["17"],
         "padoms": "11 + 6."},
        {"jaut": "Grāmata 15 €, grāmatzīme 4 €. Kopā (€)?", "atb": ["19"],
         "padoms": "15 + 4."},
    ]),

    Varianti("Vai pietiek?", [
        {"jaut": "Makā 20 €. Pirkums 17 €.",
         "opcijas": ["pietiek", "nepietiek"], "jaukt": False, "pareizi": 0,
         "padoms": "17 < 20."},
        {"jaut": "Makā 15 €. Pirkums 12 € + 5 €.",
         "opcijas": ["pietiek", "nepietiek"], "jaukt": False, "pareizi": 1,
         "padoms": "17 > 15."},
    ]),

    Pasaule("Dāvana draugam",
            Ievadi("", [
                {"jaut": "Tev 20 €. Puzle 13 €, kartīte 2 €. Cik maksā abas?",
                 "atb": ["15"], "padoms": "13 + 2."},
                {"jaut": "Vai vēl pietiks kastītei par 4 €? Cik būs kopā?",
                 "atb": ["19"], "padoms": "15 + 4 - pietiek."},
            ]),
            pavediens="veikals",
            konteksts="Tu pērc dāvanu dzimšanas dienai.",
            kapec="Saskaiti, pirms ej uz kasi."),

    Kopsavilkums([
        "Saskaitu divu preču cenas.",
        "Rakstu rezultātu ar €.",
        "Salīdzinu ar naudu makā.",
    ]),

    Majas([
        "Atrodi reklāmā 2 preces un saskaiti cenas.",
        "Vai pietiktu ar 20 €?",
        "Izspēlē veikalu ar mājiniekiem.",
    ]),
]
