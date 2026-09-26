# -*- coding: utf-8 -*-
"""1. klase, 71. stunda: «Kurš skaitlis pazuda?»

Virknē trūkst skaitļa vidū. Vispirms atrod likumu no blakus skaitļiem, tad
ieliek trūkstošo un pārbauda: vai likums der visur?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kurš skaitlis pazuda?"

MERKIS = ("Šodien ierakstīsim virknē trūkstošos skaitļus un paskaidrosim "
          "savu izvēli.")

SATURS = [
    Sakums("10; 20; ?; 40; 50 - kurš pazuda?",
           zimejums=restis([[10, 20, None, 40, 50]]),
           paraksts="Likums +10 - pazuda 30.",
           fakti=["Atrodi likumu no blakus skaitļiem.",
                  "Ieliec trūkstošo pēc likuma.",
                  "Pārbaudi visu virkni."]),

    Doma("Atrodi un pārbaudi",
         "Trūkstošo skaitli atrod ar likumu - un pārbauda ar abiem "
         "kaimiņiem.",
         soli=[
             "Atrodi divus blakus skaitļus un likumu.",
             "Pieskaiti likumu skaitlim pirms «?».",
             "Pārbaudi: vai no «?» līdz nākamajam arī der?",
         ]),

    Ievadi("Kurš pazuda?", [
        {"jaut": "Kurš pazuda?", "zim": restis([[10, 20, None, 40, 50]]),
         "atb": ["30"], "padoms": "+10."},
        {"jaut": "Kurš pazuda?", "zim": restis([[5, 10, 15, None, 25]]),
         "atb": ["20"], "padoms": "+5."},
        {"jaut": "Kurš pazuda?", "zim": restis([[2, None, 6, 8, 10]]),
         "atb": ["4"], "padoms": "+2."},
        {"jaut": "Kurš pazuda?", "zim": restis([[35, 33, 31, None, 27]]),
         "atb": ["29"], "padoms": "−2."},
        {"jaut": "Kurš pazuda?", "zim": restis([[None, 17, 27, 37, 47]]),
         "atb": ["7"], "padoms": "−10 no 17."},
        {"jaut": "Kurš pazuda?", "zim": restis([[60, 50, None, 30, 20]]),
         "atb": ["40"], "padoms": "−10."},
    ], pamats=4),

    Varianti("Kāpēc?", [
        {"jaut": "Virknē 3; 6; ?; 12 Laura ielika 9. Kāpēc tas der?",
         "opcijas": ["likums +3: 6 + 3 = 9 un 9 + 3 = 12",
                     "9 ir mans mīļākais skaitlis", "9 ir lielāks nekā 6"],
         "pareizi": 0, "padoms": "Pārbaudi abus kaimiņus."},
    ]),

    Pasaule("Lappuses grāmatā",
            Ievadi("", [
                {"jaut": "No grāmatas izkrita lapa. Palika lappuses 22 un 25. "
                         "Kuras lappuses pazuda? Uzraksti mazāko.",
                 "atb": ["23"], "padoms": "Pēc 22."},
                {"jaut": "Un lielāko?", "atb": ["24"],
                 "padoms": "Pirms 25."},
            ]),
            pavediens="skola",
            konteksts="Lappušu numuri ir virkne ar likumu +1.",
            kapec="Pēc likuma var atrast, kas pazudis."),

    Kopsavilkums([
        "Atrodu virknes likumu.",
        "Ierakstu trūkstošo skaitli.",
        "Pārbaudu ar abiem kaimiņiem.",
    ]),

    Majas([
        "Uzraksti virkni ar 2 trūkstošiem skaitļiem mājiniekam.",
        "Atrodi kalendārā trūkstošu datumu virkni.",
        "Kurš skaitlis pazuda: 45; 50; ?; 60?",
    ]),
]
