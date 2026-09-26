# -*- coding: utf-8 -*-
"""1. klase, 142. stunda: «Kas ir puse no metra?»

Pārlokot metru uz pusēm, iegūst 50 cm = 5 dm. Puse no decimetra - 5 cm.
To praktiski nosaka ar mērlenti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, dala, lineals)

TEMA = "Kas ir puse no metra?"

MERKIS = ("Šodien, pārlokot mērlenti, noteiksim pusi no metra un pusi no "
          "decimetra.")

SATURS = [
    Sakums("Pārloki metru uz pusēm - cik cm?",
           zimejums=dala(2, 1, "puse no 1 m = 50 cm"),
           paraksts="Puse no 100 cm ir 50 cm.",
           fakti=["Puse - viena no divām vienādām daļām.",
                  "Puse no metra - 50 cm = 5 dm.",
                  "Puse no decimetra - 5 cm."]),

    Petijums("Loki mērlenti", [
        "Paņem 1 m garu auklu vai papīra sloksni.",
        "Pārloki uz pusēm.",
        "Izmēri pusi ar lineālu.",
        "Pārloki vēlreiz - cik cm tagad?",
    ], vajag="1 m aukla vai sloksne, lineāls"),

    Doma("Puse",
         "Puse ir tik, lai divas vienādas daļas kopā dotu visu.",
         soli=[
             "Puse no 100 cm: 50 + 50 = 100.",
             "Puse no 10 cm: 5 + 5 = 10.",
             "Pārbaudi: divas puses kopā - viss.",
         ]),

    Ievadi("Puse", [
        {"jaut": "Puse no 1 m - cik cm?", "atb": ["50"],
         "padoms": "50 + 50 = 100."},
        {"jaut": "Puse no 1 dm - cik cm?", "zim": lineals(10, [(0, 5, "")]),
         "atb": ["5"], "padoms": "5 + 5 = 10."},
        {"jaut": "Puse no 1 m - cik dm?", "atb": ["5"], "padoms": "5 + 5."},
        {"jaut": "Puse no 20 cm?", "atb": ["10"], "padoms": "10 + 10."},
    ]),

    Varianti("Puse vai ne?", [
        {"jaut": "Vai 40 cm ir puse no metra?",
         "opcijas": ["Nē - 50 cm", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "40 + 40 = 80."},
        {"jaut": "Vai 5 dm ir puse no metra?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "5 dm = 50 cm."},
    ]),

    Pasaule("Lente divām māsām",
            Ievadi("", [
                {"jaut": "Mamma nopirka 1 m lentes un sadalīja uz pusēm. Cik "
                         "cm katrai?", "atb": ["50"], "padoms": "Puse."},
            ]),
            pavediens="maja",
            konteksts="Divām māsām matiem vajag vienādas lentes.",
            kapec="Uz pusēm - godīgi abām."),

    Kopsavilkums([
        "Zinu, ka puse no metra ir 50 cm.",
        "Zinu, ka puse no decimetra ir 5 cm.",
        "Nosaku pusi, pārlokot.",
    ]),

    Majas([
        "Pārloki šalli vai dvieli uz pusēm - izmēri pusi.",
        "Atrodi mājās kaut ko apmēram pusmetru garu.",
        "Izmēri un pārbaudi.",
    ]),
]
