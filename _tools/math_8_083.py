# -*- coding: utf-8 -*-
"""8. klase, 83. stunda: «Cik daudz ietilpst traukā?»

Temata noslēgums pirms PD4: praktiski tilpuma uzdevumi ar mērvienību
pārveidojumiem. Galvenā saite 1 l = 1 dm³ = 1000 cm³, tāpēc izmērus ērti
pārvērst decimetros. 1 mm lietus uz 1 m² ir 1 litrs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, kermenis)

TEMA = "Cik daudz ietilpst traukā?"

MERKIS = ("Risināsim praktisku uzdevumu par tilpumu ar mērvienību "
          "pārveidojumiem.")

SATURS = [
    Sakums("Cik litru ietilpst akvārijā?",
           zimejums=kermenis("kvadrs"),
           paraksts="1 l = 1 dm³ = 1000 cm³",
           fakti=["1 l = 1 dm³ = 1000 cm³; 1 ml = 1 cm³.",
                  "1 m³ = 1000 l.",
                  "Pirms rēķina visus izmērus pārvērš vienās vienībās."]),

    Doma("No izmēriem līdz litriem",
         "Ja izmērus pārvērš decimetros, tilpums uzreiz ir litros.",
         soli=[
             "Pārvērš visus izmērus vienās vienībās (ērti - dm).",
             "Aprēķini tilpumu V = S · h.",
             "dm³ ir litri; m³ reizina ar 1000.",
             "Novērtē: vai atbilde ir saprātīga?",
         ]),

    Paraugs("Akvārijs",
            uzd="Akvārijs 60 cm × 30 cm × 40 cm piepildīts līdz 35 cm "
                "augstumam. Cik litru ūdens tajā ir?",
            soli=[
                ("6 dm × 3 dm × 3,5 dm", "Pārvērš dm."),
                ("V = 6 · 3 · 3,5 = 63 dm³", "Tilpums."),
                ("63 dm³ = 63 l", "Litri."),
            ],
            atbilde="63 l"),

    Ievadi("Aprēķini", [
        {"jaut": "Kaste 2 dm × 3 dm × 5 dm. Cik litru?", "atb": ["30"],
         "padoms": "2 · 3 · 5 dm³."},
        {"jaut": "Katls - cilindrs r = 1 dm, h = 2 dm (π ≈ 3,14). Cik "
                 "litru?", "atb": ["6,28"], "padoms": "3,14 · 1 · 2."},
        {"jaut": "Baseins 10 m × 5 m × 1,5 m. Cik m³?", "atb": ["75"],
         "padoms": "10 · 5 · 1,5."},
        {"jaut": "Cik litru ir 75 m³?", "atb": ["75000", "75 000"],
         "padoms": "· 1000."},
        {"jaut": "Glāze - cilindrs r = 3 cm, h = 10 cm (π ≈ 3,14). Cik ml?",
         "atb": ["282,6"], "padoms": "3,14 · 9 · 10."},
        {"jaut": "Cik pilnas glāzes var ieliet no 2 l pudeles?",
         "atb": ["7"], "padoms": "2000 : 282,6 ≈ 7,1."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "1 m³ = ?",
         "opcijas": ["1000 l", "100 l", "10 l", "1 000 000 l"],
         "pareizi": 0, "padoms": "10 dm · 10 dm · 10 dm."},
        {"jaut": "250 cm³ = ?",
         "opcijas": ["0,25 l", "2,5 l", "25 l", "0,025 l"],
         "pareizi": 0, "padoms": "1 l = 1000 cm³."},
        {"jaut": "Ja visus trauka izmērus divkāršo, tilpums...",
         "opcijas": ["palielinās 8 reizes", "divkāršojas", "četrkāršojas",
                     "nemainās"],
         "pareizi": 0, "padoms": "2 · 2 · 2."},
    ]),

    Pasaule("Lietus muca",
            Ievadi("", [
                {"jaut": "Muca - cilindrs d = 6 dm, h = 9 dm (π ≈ 3,14). Cik "
                         "litru (veselos)?",
                 "atb": ["254"], "padoms": "3,14 · 9 · 9 = 254,34."},
                {"jaut": "Nolija 20 mm lietus uz 50 m² jumta. Cik litru "
                         "notek?",
                 "atb": ["1000"], "padoms": "50 m² · 0,02 m = 1 m³."},
                {"jaut": "Cik mucu var piepildīt pilnas?", "atb": ["3"],
                 "padoms": "1000 : 254,34 ≈ 3,9."},
            ]),
            pavediens="planeta",
            konteksts="Lietus ūdeni krāj mucās dārza laistīšanai; 1 mm lietus "
                      "uz 1 m² ir 1 litrs.",
            kapec="Tilpumu m³ pārvērš litros, lai salīdzinātu ar mucu."),

    Kopsavilkums([
        "Pārvēršu izmērus vienās vienībās.",
        "Aprēķinu trauka tilpumu litros.",
        "Novērtēju, vai atbilde ir saprātīga.",
    ]),

    Majas([
        "Izmēri spaini vai katlu un aprēķini, cik litru tajā ietilpst.",
        "Pārbaudi ar litra burku.",
        "Aprēķini, cik litru ūdens ir tavā vannā vai dušas traukā.",
    ]),
]
