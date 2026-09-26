# -*- coding: utf-8 -*-
"""7. klase, 117. stunda: «Kā pierakstīt procentu izmaiņas?»

Palielinājums par p % nozīmē reizināt ar (1 + {p|100}): par 20 % vairāk ir
1,2x. Samazinājums - ar (1 − {p|100}): par 20 % mazāk ir 0,8x. Stunda to
lieto atlaidēm, algām un cenu kāpumam - arī divos soļos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Kā pierakstīt procentu izmaiņas?"

MERKIS = ("Pierakstīsim ar izteiksmi lieluma palielinājumu vai "
          "samazinājumu procentos.")

SATURS = [
    Sakums("Atlaide 20 % - maksā 0,8x",
           zimejums=dala(10, 8, "maksā 80 % = 0,8x"),
           paraksts="Cena x, atlaide 20 %.",
           fakti=["Atlaide 20 %: paliek 80 % cenas.",
                  "80 % = 0,8 - tātad jāmaksā 0,8x.",
                  "Viens reizinājums, nevis divi soļi."]),

    Doma("Izmaiņa ir reizinājums",
         "Ja lielumu x palielina par p %, iegūst x(1 + {p|100}). Ja "
         "samazina par p %, iegūst x(1 − {p|100}).",
         soli=[
             "Pārvērt procentus decimāldaļā: 15 % = 0,15.",
             "Palielinājums: 1 + 0,15 = 1,15 → 1,15x.",
             "Samazinājums: 1 − 0,15 = 0,85 → 0,85x.",
             "Divas izmaiņas pēc kārtas - reizinātāji sareizinās.",
         ],
         pieze="+10 %, tad −10 % nav atpakaļ sākumā: 1,1 · 0,9 = 0,99 - "
               "paliek 99 %."),

    Slidnis("Cena pa soļiem (x = 100 €)", [
        {"v": "x", "teksts": "100 €", "josla": 50},
        {"v": "1,2x", "teksts": "+20 %: 120 €", "josla": 60},
        {"v": "1,2 · 0,8x = 0,96x", "teksts": "−20 %: 96 €", "josla": 48},
    ], ievads="Vispirms cena pieaug par 20 %, tad samazinās par 20 %."),

    Paraugs("Divas izmaiņas",
            uzd="Cena x vispirms pieauga par 10 %, tad samazinājās par 25 %. "
                "Pieraksti jauno cenu.",
            soli=[
                ("Pēc pieauguma: 1,1x", "1 + 0,1."),
                ("Pēc samazinājuma: 0,75 · 1,1x", "1 − 0,25."),
                ("0,825x", "Sareizina."),
                ("Kopumā −17,5 %", "1 − 0,825 = 0,175."),
            ],
            atbilde="0,825x"),

    Varianti("Kura izteiksme?", [
        {"jaut": "Alga x pieauga par 5 %.",
         "opcijas": ["1,05x", "x + 5", "0,05x", "5x"],
         "pareizi": 0, "padoms": "1 + 0,05."},
        {"jaut": "Cena x samazināta par 30 %.",
         "opcijas": ["0,7x", "0,3x", "x − 30", "1,3x"],
         "pareizi": 0, "padoms": "1 − 0,3."},
        {"jaut": "Iedzīvotāju skaits x pieauga 2 reizes.",
         "opcijas": ["2x (+100 %)", "1,02x", "1,2x", "x + 2"],
         "pareizi": 0, "padoms": "Divreiz = +100 %."},
        {"jaut": "PVN 21 % pieskaita cenai x.",
         "opcijas": ["1,21x", "0,21x", "x + 21", "0,79x"],
         "pareizi": 0, "padoms": "1 + 0,21."},
    ], pamats=4),

    Ievadi("Aprēķini", [
        {"jaut": "0,8x, ja x = 45 €",
         "atb": ["36"], "padoms": "0,8 · 45."},
        {"jaut": "Cena 200 €, +15 %. Jaunā cena (€)?",
         "atb": ["230"], "padoms": "1,15 · 200."},
        {"jaut": "Cena ar PVN (1,21x) ir 121 €. Cena bez PVN (€)?",
         "atb": ["100"], "padoms": "121 : 1,21."},
        {"jaut": "+10 %, tad −10 %. Cik % no sākuma cenas?",
         "atb": ["99"], "padoms": "1,1 · 0,9 = 0,99."},
    ]),

    Pasaule("Melnā piektdiena",
            Ievadi("", [
                {"jaut": "Austiņas 80 €. Pirms akcijas cenu pacēla par "
                         "25 %, tad deva 20 % atlaidi. Galīgā cena (€)?",
                 "atb": ["80"], "padoms": "1,25 · 0,8 = 1."},
                {"jaut": "Cik € bija «pirms atlaides» cena?",
                 "atb": ["100"], "padoms": "1,25 · 80."},
                {"jaut": "Cik % bija īstā atlaide no sākotnējās cenas?",
                 "atb": ["0"], "padoms": "Cena nemainījās."},
            ]),
            pavediens="veikals",
            konteksts="Patērētāju tiesību centrs brīdina: dažas «atlaides» "
                      "ir pēc iepriekšējas cenu paaugstināšanas.",
            kapec="Izteiksme 1,25 · 0,8x = x atmasko triku."),

    Kopsavilkums([
        "Pierakstu palielinājumu: x(1 + {p|100}).",
        "Pierakstu samazinājumu: x(1 − {p|100}).",
        "Reizinu reizinātājus divām izmaiņām pēc kārtas.",
        "Zinu, ka +p % un −p % neatceļ viens otru.",
    ]),

    Majas([
        "Atrodi veikalā atlaidi un pieraksti cenu kā izteiksmi.",
        "Aprēķini: +20 %, tad −20 %. Cik % no sākuma?",
        "Izdomā «viltīgu atlaidi» un atmasko to ar izteiksmi.",
    ]),
]
