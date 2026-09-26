# -*- coding: utf-8 -*-
"""2. klase, 138. stunda: «Kā skaitīt pa 3?»

Skaitīšana pa 3: 3, 6, 9, 12 ... 30. Uz skaitļu taisnes - vienādi lēcieni
pa 3. Katrs skaitlis virknē ir reizinājums ar 3, un lēcienu skaits pasaka,
ar ko reizināja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Pasaule,
                         Sakums, Varianti, simta_kvadrats, taisne)

TEMA = "Kā skaitīt pa 3?"

MERKIS = ("Šodien skaitīsim pa 3 uz priekšu, pierakstīsim virkni un "
          "izmantosim skaitļu taisni.")

SATURS = [
    Sakums("Kā ātri saskaitīt trīslapu āboliņus?",
           zimejums=taisne(0, 15, 3, bultas=[(0, 3, "+3"), (3, 6, "+3"),
                                              (6, 9, "+3"), (9, 12, "+3"),
                                              (12, 15, "+3")]),
           paraksts="5 lēcieni pa 3 - 15.",
           fakti=["Katram āboliņam 3 lapiņas.",
                  "Skaiti pa 3: 3, 6, 9, 12, 15.",
                  "Lēcienu skaits - āboliņu skaits."]),

    Doma("Pa 3",
         "Katrs nākamais ir par 3 lielāks; lēcienu skaits ir reizinātājs.",
         soli=[
             "Sāc no 0.",
             "Lec pa 3: 3, 6, 9 ...",
             "Skaiti lēcienus uz pirkstiem.",
             "4 lēcieni - 12, jo 4 · 3 = 12.",
         ]),

    Ievadi("Turpini virkni", [
        {"jaut": "3, 6, 9, 12, ...", "atb": ["15"], "padoms": "+3."},
        {"jaut": "15, 18, 21, ...", "atb": ["24"], "padoms": "+3."},
        {"jaut": "24, 27, ...", "atb": ["30"], "padoms": "+3."},
        {"jaut": "Atpakaļ: 30, 27, 24, ...", "atb": ["21"], "padoms": "−3."},
    ]),

    Kustiba("Varde lec pa 3", [
        {"jaut": "Varde lec 6 reizes pa 3 no nulles. Kur tā apstāsies?",
         "atb": 18, "beigas": 30, "iedala": 3, "objekts": "varde",
         "merkis": "6 · 3", "padoms": "3, 6, 9, 12, 15, 18."},
        {"jaut": "8 lēcieni pa 3. Kur?", "atb": 24, "beigas": 30,
         "iedala": 3, "objekts": "varde", "merkis": "8 · 3",
         "padoms": "8 · 3."},
    ]),

    Varianti("Vai virknē?", [
        {"jaut": "Vai 20 ir virknē pa 3?",
         "zim": simta_kvadrats(1, 30, izcelt=list(range(3, 31, 3))),
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "18, 21 - 20 izlaists."},
        {"jaut": "Vai 27 ir virknē pa 3?",
         "zim": simta_kvadrats(1, 30, izcelt=list(range(3, 31, 3))),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "9 · 3."},
    ]),

    Pasaule("Trijstūra galdi kafejnīcā",
            Ievadi("", [
                {"jaut": "Pie katra galda 3 krēsli. Cik krēslu pie 7 galdiem?",
                 "atb": ["21"], "padoms": "Skaiti pa 3 septiņas reizes."},
                {"jaut": "Ienāca 27 viesi. Cik galdu vajag?", "atb": ["9"],
                 "padoms": "Pa 3 līdz 27."},
            ]),
            pavediens="virtuve",
            konteksts="Kafejnīcā pie trijstūra galdiņiem sēž pa trim.",
            kapec="Skaitot pa 3, ātri saskaita vietas."),

    Kopsavilkums([
        "Skaitu pa 3 uz priekšu un atpakaļ.",
        "Izmantoju skaitļu taisni.",
        "Zinu, ka lēcienu skaits ir reizinātājs.",
    ]),

    Majas([
        "Skaiti pa 3 līdz 30, lecot uz vietas.",
        "Uzraksti virkni.",
        "Atrodi mājās lietas, kas ir pa 3.",
    ]),
]
