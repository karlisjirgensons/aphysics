# -*- coding: utf-8 -*-
"""1. klase, 56. stunda: «Kā sauc skaitļus otrajā desmitā?»

Skaitļi no 11 līdz 19: viens desmits un vēl daži vieni. Nosaukumi -
vienpadsmit, divpadsmit ... deviņpadsmit («-padsmit» nozīmē «un desmit»).
Līdz 20 pietrūkst tik, cik līdz pilnam otrajam rāmim.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, ramis)

TEMA = "Kā sauc skaitļus otrajā desmitā?"

MERKIS = ("Šodien lasīsim un rakstīsim skaitļus no 11 līdz 19 un "
          "noteiksim, cik pietrūkst līdz 20.")

SATURS = [
    Sakums("Kāpēc 14 sauc par četrpadsmit?",
           zimejums=ramis(14, 2),
           paraksts="Pilns desmits un vēl 4 - četrpadsmit.",
           fakti=["«-padsmit» - vēl desmit.",
                  "14 = 10 + 4.",
                  "Otrais rāmis rāda, cik trūkst līdz 20."]),

    Doma("Viens desmits un vieni",
         "Skaitļos no 11 līdz 19 ir viens desmits un vēl vieni.",
         soli=[
             "Pirmais cipars 1 - viens desmits.",
             "Otrais cipars - cik vēl vienu.",
             "Nosaukums: vieni + «padsmit».",
         ]),

    Ievadi("Cik ir?", [
        {"jaut": "Cik ripiņu?", "zim": ramis(13, 2), "atb": ["13"],
         "padoms": "10 un 3."},
        {"jaut": "Cik ripiņu?", "zim": ramis(18, 2), "atb": ["18"],
         "padoms": "10 un 8."},
        {"jaut": "Cik pietrūkst līdz 20?", "zim": ramis(16, 2), "atb": ["4"],
         "padoms": "Tukšās rūtiņas."},
        {"jaut": "Cik pietrūkst līdz 20?", "zim": ramis(11, 2), "atb": ["9"],
         "padoms": "Tukšās rūtiņas."},
        {"jaut": "Uzraksti ar cipariem: septiņpadsmit", "atb": ["17"],
         "padoms": "Desmits un 7."},
        {"jaut": "Uzraksti ar cipariem: divpadsmit", "atb": ["12"],
         "padoms": "Desmits un 2."},
    ], pamats=4),

    Varianti("Kā sauc?", [
        {"jaut": "15", "opcijas": ["piecpadsmit", "piecdesmit",
                                   "pieci"], "pareizi": 0,
         "padoms": "Desmits un 5."},
        {"jaut": "19", "opcijas": ["deviņpadsmit", "deviņdesmit",
                                   "deviņi"], "pareizi": 0,
         "padoms": "Desmits un 9."},
        {"jaut": "Kurš skaitlis ir starp 13 un 15?",
         "opcijas": ["14", "12", "16"], "pareizi": 0,
         "padoms": "13, ?, 15."},
    ]),

    Pasaule("Dzimšanas diena",
            Ievadi("", [
                {"jaut": "Māsai šodien 13 gadi. Cik gadu būs pēc 2 gadiem?",
                 "atb": ["15"], "padoms": "13, 14, 15."},
                {"jaut": "Cik gadu vēl līdz 20?", "atb": ["7"],
                 "padoms": "No 13 līdz 20."},
            ]),
            pavediens="maja",
            konteksts="Vecākā māsa svin dzimšanas dienu.",
            kapec="Otrā desmita skaitļi - pusaudžu gadi."),

    Kopsavilkums([
        "Lasu un rakstu skaitļus no 11 līdz 19.",
        "Zinu, ka tajos ir viens desmits un vieni.",
        "Nosaku, cik pietrūkst līdz 20.",
    ]),

    Majas([
        "Nosauc skaļi skaitļus no 11 līdz 20 un atpakaļ.",
        "Atrodi mājās skaitļus no 11 līdz 19.",
        "Cik gadu būs tev, kad beigsi 9. klasi?",
    ]),
]
