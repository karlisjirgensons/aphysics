# -*- coding: utf-8 -*-
"""2. klase, 82. stunda: «Kura izteiksme ir lielāka?»

Izteiksmes var salīdzināt, tās nerēķinot: 45 + 28 un 45 + 32 - pirmie
saskaitāmie vienādi, otrs lielāks otrajā, tātad arī summa. Spriešana ir
ātrāka un māca pamanīt struktūru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Kura izteiksme ir lielāka?"

MERKIS = ("Šodien salīdzināsim divu izteiksmju vērtības, spriežot un "
          "neveicot precīzus aprēķinus.")

_ZIMES = ["<", ">", "="]

SATURS = [
    Sakums("Kura summa lielāka - 45 + 28 vai 45 + 32? Nerēķini!",
           fakti=["Abās ir 45.",
                  "32 ir vairāk nekā 28.",
                  "Tātad 45 + 32 ir lielāka."]),

    Doma("Salīdzini, nerēķinot",
         "Atrodi, kas ir vienāds, un salīdzini to, kas atšķiras.",
         soli=[
             "Summā: ja viens saskaitāmais vienāds - lielāka tā, kur "
             "otrs lielāks.",
             "Starpībā: ja atņem no vienāda skaitļa - lielāka tā, kur "
             "atņem mazāk.",
             "Starpībā: ja atņem vienādu - lielāka tā, kur mazināmais "
             "lielāks.",
             "Ja nevar izspriest - novērtē ar apaļiem skaitļiem.",
         ]),

    Varianti("Liec zīmi", [
        {"jaut": "37 + 25 ☐ 37 + 19", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 1, "padoms": "25 > 19."},
        {"jaut": "80 − 26 ☐ 80 − 31", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 1, "padoms": "Atņem mazāk - paliek vairāk."},
        {"jaut": "54 + 18 ☐ 18 + 54", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 2, "padoms": "Saskaitāmos samaina."},
        {"jaut": "62 − 20 ☐ 72 − 20", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 0, "padoms": "62 < 72."},
        {"jaut": "49 + 30 ☐ 50 + 30", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 0, "padoms": "49 < 50."},
        {"jaut": "90 − 45 ☐ 90 − 44", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 0, "padoms": "Atņem vairāk - paliek mazāk."},
    ], pamats=4),

    Ievadi("Par cik?", [
        {"jaut": "Par cik 45 + 32 lielāks nekā 45 + 28?", "atb": ["4"],
         "padoms": "32 − 28."},
        {"jaut": "Par cik 80 − 26 lielāks nekā 80 − 31?", "atb": ["5"],
         "padoms": "31 − 26."},
    ]),

    Pasaule("Kurš veikals lētāks?",
            Varianti("", [
                {"jaut": "Veikalā A: velosipēds 89 € + ķivere 25 €. Veikalā "
                         "B: tas pats velosipēds 89 € + ķivere 21 €. Kur "
                         "lētāk?", "opcijas": ["B", "A", "vienādi"],
                 "pareizi": 0, "padoms": "Velosipēds vienāds, ķivere "
                                         "lētāka B."},
                {"jaut": "Par cik lētāk?", "opcijas": ["4 €", "21 €",
                                                       "10 €"],
                 "pareizi": 0, "padoms": "25 − 21."},
            ]),
            pavediens="veikals",
            konteksts="Cenas var salīdzināt, pat neskaitot kopsummu.",
            kapec="Spriest ir ātrāk nekā rēķināt."),

    Kopsavilkums([
        "Salīdzinu izteiksmes, nerēķinot precīzi.",
        "Atrodu, kas vienāds un kas atšķiras.",
        "Lieku zīmes <, > un =.",
    ]),

    Majas([
        "Izdomā divas summas ar vienu vienādu saskaitāmo.",
        "Lai mājinieks pasaka, kura lielāka, nerēķinot.",
        "Pārbaudi, izrēķinot.",
    ]),
]
