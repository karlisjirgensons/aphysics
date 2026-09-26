# -*- coding: utf-8 -*-
"""8. klase, 81. stunda: «Kā aprēķina cilindra virsmas laukumu?»

S = 2πr^2 + 2πrh: divi pamati un sānu taisnstūris 2πr × h (79. stundas
izklājums). Katrs saskaitāmais ir sava daļa - caurulei paliek tikai sānu
virsma, bundžai bez vāka - viens pamats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, cilindra_izklajums)

TEMA = "Kā aprēķina cilindra virsmas laukumu?"

MERKIS = ("Aprēķināsim cilindra virsmas laukumu un paskaidrosim katru "
          "saskaitāmo.")

SATURS = [
    Sakums("No kā sastāv cilindra virsma?",
           zimejums=cilindra_izklajums(),
           paraksts="Divi riņķi un taisnstūris 2πr × h.",
           fakti=["Sānu virsma = 2πr · h.",
                  "Abi pamati kopā = 2πr^2.",
                  "S = 2πr^2 + 2πrh."]),

    Doma("Katrs saskaitāmais",
         "Virsma ir divu pamatu un sānu virsmas summa.",
         soli=[
             "Viena pamata laukums ir πr^2; diviem - 2πr^2.",
             "Sānu virsma ir taisnstūris: garums 2πr, platums h.",
             "Saskaiti; atbildi atstāj ar π vai noapaļo.",
             "Caurulei pamatu nav - tikai sānu virsma.",
         ],
         pieze="Iznesot kopīgo reizinātāju: S = 2πr(r + h)."),

    Paraugs("Aprēķini virsmu",
            uzd="Cilindram r = 3 cm, h = 10 cm. Aprēķini virsmas laukumu.",
            soli=[
                ("2 · π · 9 = 18π", "Pamati."),
                ("2 · π · 3 · 10 = 60π", "Sānu virsma."),
                ("18π + 60π = 78π", "Kopā."),
                ("78 · 3,14 ≈ 244,9 cm²", "Aptuveni."),
            ],
            atbilde="78π ≈ 244,9 cm²"),

    Ievadi("Aprēķini", [
        {"jaut": "r = 2, h = 5. Sānu virsma = ?π", "atb": ["20"],
         "padoms": "2 · 2 · 5."},
        {"jaut": "Tam pašam cilindram abi pamati = ?π", "atb": ["8"],
         "padoms": "2 · 4."},
        {"jaut": "Visa virsma = ?π", "atb": ["28"], "padoms": "20 + 8."},
        {"jaut": "r = 5, h = 5. S = ?π", "atb": ["100"],
         "padoms": "50 + 50."},
        {"jaut": "Caurule: r = 1 m, garums 10 m. Sānu virsma = ?π m²",
         "atb": ["20"], "padoms": "2 · 1 · 10."},
        {"jaut": "r = 10, h = 20, π ≈ 3,14. S?", "atb": ["1884"],
         "padoms": "200π + 400π = 600π."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Ko nozīmē 2πr formulā 2πrh?",
         "opcijas": ["Taisnstūra garumu", "Pamata laukumu", "Augstumu",
                     "Diametru"],
         "pareizi": 0, "padoms": "Riņķa līnijas garums."},
        {"jaut": "Bundžai bez vāka virsma ir...",
         "opcijas": ["πr^2 + 2πrh", "2πr^2 + 2πrh", "2πrh", "πr^2h"],
         "pareizi": 0, "padoms": "Tikai viens pamats."},
        {"jaut": "r = 1, h = 1. S = ?",
         "opcijas": ["4π", "2π", "3π", "π"],
         "pareizi": 0, "padoms": "2π + 2π."},
    ]),

    Pasaule("Skārda bundža",
            Ievadi("", [
                {"jaut": "Bundža d = 10 cm, h = 12 cm. Etiķetes laukums = ?π "
                         "cm²",
                 "atb": ["120"], "padoms": "2 · 5 · 12."},
                {"jaut": "Skārds visai bundžai = ?π cm²", "atb": ["170"],
                 "padoms": "120 + 2 · 25."},
                {"jaut": "Aptuveni (π ≈ 3,14), veselos cm²?", "atb": ["534"],
                 "padoms": "170 · 3,14 = 533,8."},
            ]),
            pavediens="virtuve",
            konteksts="Ražotājs rēķina, cik skārda un papīra vajag katrai "
                      "bundžai - miljoniem reižu.",
            kapec="Etiķete ir tikai sānu virsma, skārds - visa virsma."),

    Kopsavilkums([
        "Aprēķinu cilindra pamatu un sānu virsmu.",
        "Paskaidroju katru formulas saskaitāmo.",
        "Pielāgoju formulu caurulei un bundžai bez vāka.",
    ]),

    Majas([
        "Izmēri bundžu un aprēķini etiķetes un visa skārda laukumu.",
        "Aprēķini tualetes papīra ruļļa kartona čaulas laukumu.",
        "Salīdzini: kurai bundžai vajag mazāk skārda - zemai un platai vai "
        "augstai un šaurai?",
    ]),
]
