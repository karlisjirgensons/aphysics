# -*- coding: utf-8 -*-
"""4. klase, 126. stunda: «Kā aprēķināt daļu no skaita?»

Divi soļi: vispirms pamatdaļa (dala ar saucēju), tad daļa (reizina ar
skaitītāju). {3|4} no 24 = 24 : 4 · 3 = 18. Šis «dali, tad reizini» ir
galvenais 4.6. temata algoritms.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Slidnis, Varianti, dala)

TEMA = "Kā aprēķināt daļu no skaita?"

MERKIS = ("Noteiksim pamatdaļu no elementu skaita un pēc tam - atlikušās "
          "daļas vērtību.")

SATURS = [
    Sakums("Cik ir {3|4} no 24 konfektēm?",
           zimejums=dala(4, 3, "katrā daļā 6, iekrāsotas 3 daļas = 18"),
           paraksts="24 : 4 = 6, tad 6 · 3 = 18.",
           fakti=["Vispirms atrod vienu daļu.",
                  "Tad paņem tik daļu, cik saka skaitītājs."]),

    Doma("Dali ar saucēju, reizini ar skaitītāju",
         "{a|n} no skaitļa b = b : n · a.",
         soli=[
             "Dali veselo ar saucēju: 24 : 4 = 6 (viena ceturtdaļa).",
             "Reizini ar skaitītāju: 6 · 3 = 18.",
             "Atlikusī daļa: 24 − 18 = 6 jeb {1|4}.",
             "Pārbaude: 18 + 6 = 24.",
         ],
         pieze="Ja skaitītājs 1, otrais solis nav vajadzīgs."),

    Slidnis("Divi soļi: {2|5} no 35",
            soli=[
                {"v": "35", "teksts": "Veselais.", "josla": 100},
                {"v": "35 : 5 = 7", "teksts": "Viena piektdaļa.",
                 "josla": 20},
                {"v": "7 · 2 = 14", "teksts": "Divas piektdaļas.",
                 "josla": 40},
            ]),

    Paraugs("{5|6} no 30",
            uzd="Klasē 30 skolēnu, {5|6} ir sporta pulciņā. Cik?",
            soli=[
                ("30 : 6 = 5", "Viena sestdaļa."),
                ("5 · 5 = 25", "Piecas sestdaļas."),
                ("30 − 25 = 5 nav pulciņā", None),
            ],
            atbilde="25 skolēni"),

    Kustiba("Aizbrauc līdz daļai", [
        {"jaut": "Ceļš 40 km. Aizbrauc {3|4} ceļa. Cik km?",
         "atb": 30, "beigas": 40, "iedala": 5, "mers": "km",
         "merkis": "3/4", "objekts": "Velosipēds",
         "padoms": "40 : 4 · 3.",
         "stasts": "Velosipēdists brauc pa 40 km trasi."},
        {"jaut": "Aizbrauc {2|5} ceļa. Cik km?",
         "atb": 16, "beigas": 40, "iedala": 5, "mers": "km",
         "merkis": "2/5", "objekts": "Velosipēds", "padoms": "40 : 5 · 2."},
        {"jaut": "Aizbrauc {7|8} ceļa. Cik km?",
         "atb": 35, "beigas": 40, "iedala": 5, "mers": "km",
         "merkis": "7/8", "objekts": "Velosipēds", "padoms": "40 : 8 · 7."},
        {"jaut": "Aizbrauc {3|10} ceļa. Cik km?",
         "atb": 12, "beigas": 40, "iedala": 5, "mers": "km",
         "merkis": "3/10", "objekts": "Velosipēds",
         "padoms": "40 : 10 · 3."},
    ], pamats=2),

    Ievadi("Daļa no skaita", [
        {"jaut": "{3|4} no 24 = ?", "atb": ["18"], "padoms": "6 · 3."},
        {"jaut": "{2|3} no 36 = ?", "atb": ["24"], "padoms": "12 · 2."},
        {"jaut": "{4|5} no 45 = ?", "atb": ["36"], "padoms": "9 · 4."},
        {"jaut": "{5|8} no 64 = ?", "atb": ["40"], "padoms": "8 · 5."},
    ]),

    Varianti("Kā rēķina?", [
        {"jaut": "{3|7} no 56",
         "opcijas": ["56 : 7 · 3", "56 : 3 · 7", "56 · 3 · 7", "56 − 3"],
         "pareizi": 0, "padoms": "Dali ar saucēju."},
        {"jaut": "Cik ir {3|7} no 56?",
         "opcijas": ["24", "8", "21", "168"], "pareizi": 0,
         "padoms": "8 · 3."},
        {"jaut": "Kas lielāks: {3|4} no 40 vai {2|3} no 45?",
         "opcijas": ["abi vienādi (30)", "pirmais", "otrais"], "pareizi": 0,
         "padoms": "30 un 30."},
    ]),

    Pasaule("Putnu vērošana",
            Ievadi("", [
                {"jaut": "Ezerā 48 putni, {3|8} ir pīles. Cik pīļu?",
                 "atb": ["18"], "padoms": "48 : 8 · 3."},
                {"jaut": "{1|4} ir gulbji. Cik gulbju?", "atb": ["12"],
                 "padoms": "48 : 4."},
                {"jaut": "Pārējie ir kaijas. Cik kaiju?", "atb": ["18"],
                 "padoms": "48 − 18 − 12."},
                {"jaut": "Kāda daļa ir kaijas? Raksti ar saucēju 8.",
                 "atb": ["3/8"], "vieta": "piem., 1/2",
                 "padoms": "{8|8} − {3|8} − {2|8}."},
            ]),
            pavediens="daba",
            konteksts="Ornitologi putnus skaita un apraksta daļās - kāda daļa "
                      "no visiem ir katra suga.",
            kapec="Dali un reizini - un zini, cik ir katras sugas."),

    Kopsavilkums([
        "Aprēķinu daļu no skaita divos soļos.",
        "Aprēķinu atlikušās daļas vērtību.",
        "Pārbaudu, saskaitot abas daļas.",
    ]),

    Majas([
        "Saskaiti grāmatas plauktā un izrēķini {2|3} no tām.",
        "Aprēķini, cik minūšu ir {5|6} stundas un {3|4} stundas.",
        "Izdomā «putnu» uzdevumu par savu pagalmu.",
    ]),
]
