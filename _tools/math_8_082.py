# -*- coding: utf-8 -*-
"""8. klase, 82. stunda: «Kā aprēķina tilpumu?»

Prizmai un cilindram viena formula: V = pamata laukums · h. Slīdnis krauj
pamatu slāni pa slānim - katrs 1 cm biezs slānis ir pamata laukums cm³.
Cilindram V = πr^2h.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, kermenis)

TEMA = "Kā aprēķina tilpumu?"

MERKIS = ("Aprēķināsim prizmas un cilindra tilpumu, lietojot pamata laukumu "
          "un augstumu.")

SATURS = [
    Sakums("Cik liels ir cilindra tilpums?",
           zimejums=kermenis("cilindrs"),
           paraksts="Pamata laukums πr^2, reizināts ar augstumu h.",
           fakti=["Tilpums = pamata laukums · augstums.",
                  "Prizmai un cilindram formula ir viena.",
                  "Cilindram V = πr^2h."]),

    Slidnis("Slānis pa slānim", [
        {"v": "1 slānis", "teksts": "Pamats S = 12 cm², biezums 1 cm: "
                                    "12 cm³", "josla": 25},
        {"v": "2 slāņi", "teksts": "24 cm³", "josla": 50},
        {"v": "3 slāņi", "teksts": "36 cm³", "josla": 75},
        {"v": "4 slāņi", "teksts": "h = 4 cm: V = 12 · 4 = 48 cm³",
         "josla": 100},
    ]),

    Doma("Tilpuma formula",
         "V = S · h - pamata laukums, reizināts ar augstumu.",
         soli=[
             "Aprēķini pamata laukumu S.",
             "Reizini ar augstumu h.",
             "Cilindram pamats ir riņķis: V = πr^2h.",
             "Tilpuma vienības ir kubā: cm³, m³; 1 l = 1 dm³.",
         ]),

    Paraugs("Prizma un cilindrs",
            uzd="Prizmas pamats - taisnleņķa trijstūris ar katetēm 3 un 4 cm, "
                "h = 10 cm. Cilindram r = 3 cm, h = 5 cm. Aprēķini tilpumus.",
            soli=[
                ("S = {3 · 4|2} = 6 cm²", "Prizmas pamats."),
                ("V = 6 · 10 = 60 cm³", "Prizma."),
                ("V = π · 9 · 5 = 45π", "Cilindrs."),
                ("45 · 3,14 ≈ 141,3 cm³", "Aptuveni."),
            ],
            atbilde="60 cm³ un 45π ≈ 141,3 cm³"),

    Ievadi("Aprēķini tilpumu", [
        {"jaut": "Kvadrs 5 × 4 × 3 cm. V (cm³)?", "atb": ["60"],
         "padoms": "20 · 3."},
        {"jaut": "Prizma: pamata laukums 12 cm², h = 7 cm. V (cm³)?",
         "atb": ["84"], "padoms": "12 · 7."},
        {"jaut": "Cilindrs r = 2, h = 10. V = ?π", "atb": ["40"],
         "padoms": "4 · 10."},
        {"jaut": "Cilindrs d = 6, h = 4. V = ?π", "atb": ["36"],
         "padoms": "r = 3; 9 · 4."},
        {"jaut": "Trijstūra prizma: pamata mala 6, tās augstums 4, "
                 "prizmas h = 10. V?", "atb": ["120"],
         "padoms": "S = 12; 12 · 10."},
        {"jaut": "Cilindrs: V = 90π, r = 3. h = ?", "atb": ["10"],
         "padoms": "9h = 90."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Divkāršojot cilindra rādiusu, tilpums...",
         "opcijas": ["četrkāršojas", "divkāršojas", "astoņkāršojas",
                     "nemainās"],
         "pareizi": 0, "padoms": "r ir kvadrātā."},
        {"jaut": "Divkāršojot cilindra augstumu, tilpums...",
         "opcijas": ["divkāršojas", "četrkāršojas", "nemainās",
                     "astoņkāršojas"],
         "pareizi": 0, "padoms": "h pirmajā pakāpē."},
        {"jaut": "Formulā V = πr^2h - kas ir πr^2?",
         "opcijas": ["Pamata laukums", "Sānu virsma", "Riņķa līnija",
                     "Diametrs"],
         "pareizi": 0, "padoms": "Riņķa laukums."},
    ]),

    Pasaule("Siera ritulis",
            Ievadi("", [
                {"jaut": "Siera ritulis - cilindrs ar d = 20 cm un h = 8 cm. "
                         "V = ?π cm³",
                 "atb": ["800"], "padoms": "100 · 8."},
                {"jaut": "Aptuveni (π ≈ 3,14), cm³?", "atb": ["2512"],
                 "padoms": "800 · 3,14."},
                {"jaut": "1 cm³ siera sver 1,1 g. Masa kg (līdz "
                         "desmitdaļām)?",
                 "atb": ["2,8"], "padoms": "2512 · 1,1 = 2763,2 g."},
            ]),
            pavediens="virtuve",
            konteksts="Sieru pārdod pēc svara, bet svars ir atkarīgs no "
                      "tilpuma.",
            kapec="Cilindra tilpums ir pamata laukums reiz augstums - tāpat "
                  "kā kastei."),

    Kopsavilkums([
        "Aprēķinu prizmas tilpumu ar pamata laukumu un augstumu.",
        "Aprēķinu cilindra tilpumu V = πr^2h.",
        "Spriežu, kā tilpums mainās, mainot r vai h.",
    ]),

    Majas([
        "Izmēri krūzi un aprēķini, cik cm³ tajā ietilpst.",
        "Pārbaudi ar mērglāzi.",
        "Aprēķini sava istabas gaisa tilpumu m³.",
    ]),
]
