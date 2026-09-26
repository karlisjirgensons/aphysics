# -*- coding: utf-8 -*-
"""8. klase, 80. stunda: «Kā aprēķina prizmas virsmas laukumu?»

Virsmas laukums ir izklājuma laukums: divi pamati un sānu virsma. Sānu
taisnstūri rindā veido vienu taisnstūri P × h, tāpēc sānu virsma = pamata
perimetrs · h. Izklājums 3, 4, 5, 6 ir tas pats, kas 76. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, prizmas_izklajums)

TEMA = "Kā aprēķina prizmas virsmas laukumu?"

MERKIS = ("Aprēķināsim taisnas prizmas virsmas laukumu, izmantojot "
          "izklājumu.")

SATURS = [
    Sakums("Cik kartona vajag prizmai?",
           zimejums=prizmas_izklajums(3, 4, 5, 6),
           paraksts="Sānu virsma (3 + 4 + 5) · 6 = 72, pamati 2 · 6 = 12, "
                    "kopā 84.",
           fakti=["Virsmas laukums ir visu skaldņu laukumu summa.",
                  "Sānu virsma = pamata perimetrs · h.",
                  "Virsma = 2 · pamata laukums + sānu virsma."]),

    Doma("Prizmas virsma",
         "Sānu taisnstūri rindā veido vienu garu taisnstūri P × h.",
         soli=[
             "Aprēķini pamata laukumu un reizini ar 2.",
             "Aprēķini pamata perimetru P.",
             "Sānu virsma = P · h.",
             "Saskaiti abus rezultātus.",
         ],
         pieze="Kvadram: S = 2(ab + bc + ac) - tā ir tā pati formula."),

    Paraugs("Kvadrs",
            uzd="Aprēķini kvadra 5 cm × 4 cm × 3 cm virsmas laukumu "
                "(pamats 5 × 4, h = 3).",
            soli=[
                ("2 · 5 · 4 = 40 cm²", "Divi pamati."),
                ("P = 2 · (5 + 4) = 18 cm", "Pamata perimetrs."),
                ("18 · 3 = 54 cm²", "Sānu virsma."),
                ("40 + 54 = 94 cm²", "Pārbaude: 2(20 + 15 + 12) = 94."),
            ],
            atbilde="94 cm²"),

    Ievadi("Aprēķini virsmas laukumu", [
        {"jaut": "Kubs ar šķautni 3 cm. S (cm²)?", "atb": ["54"],
         "padoms": "6 · 9."},
        {"jaut": "Kvadrs 2 × 3 × 4 cm. S (cm²)?", "atb": ["52"],
         "padoms": "2(6 + 12 + 8)."},
        {"jaut": "Prizma: pamats - trijstūris 6, 8, 10 cm ar laukumu 24 cm², "
                 "h = 5 cm. S (cm²)?", "atb": ["168"],
         "padoms": "24 · 5 + 2 · 24."},
        {"jaut": "Sešstūra prizmas pamata perimetrs 12 cm, h = 10 cm. Sānu "
                 "virsma (cm²)?", "atb": ["120"], "padoms": "12 · 10."},
        {"jaut": "Kuba virsma ir 150 cm². Šķautne (cm)?", "atb": ["5"],
         "padoms": "Viena skaldne 25 cm²."},
        {"jaut": "Kvadrs 10 × 10 × 1 cm. S (cm²)?", "atb": ["240"],
         "padoms": "2(100 + 10 + 10)."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Sānu virsmu aprēķina kā...",
         "opcijas": ["pamata perimetrs · h", "pamata laukums · h",
                     "2 · pamata laukums", "perimetrs · 2"],
         "pareizi": 0, "padoms": "Taisnstūris P × h."},
        {"jaut": "Kubam ar šķautni 2 virsma ir...",
         "opcijas": ["24", "8", "12", "16"],
         "pareizi": 0, "padoms": "6 · 4."},
        {"jaut": "Kā mainās kuba virsma, ja šķautni divkāršo?",
         "opcijas": ["Četrkāršojas", "Divkāršojas", "Astoņkāršojas",
                     "Nemainās"],
         "pareizi": 0, "padoms": "Katra skaldne 4 reizes lielāka."},
    ]),

    Pasaule("Krāsojam kasti",
            Ievadi("", [
                {"jaut": "Koka kaste bez vāka: 60 cm × 40 cm, augstums 30 cm. "
                         "Cik dm² jānokrāso ārpusē?",
                 "atb": ["84"], "padoms": "24 + 2 · 18 + 2 · 12."},
                {"jaut": "Cik m² tas ir?", "atb": ["0,84"],
                 "padoms": "1 m² = 100 dm²."},
                {"jaut": "1 l krāsas sedz 10 m². Cik litru vajag divām kārtām "
                         "(līdz simtdaļām)?",
                 "atb": ["0,17"], "padoms": "1,68 : 10."},
            ]),
            pavediens="maja",
            konteksts="Krāsu, flīzes un kartonu pērk pēc virsmas laukuma.",
            kapec="Kastei bez vāka ir tikai piecas skaldnes."),

    Kopsavilkums([
        "Aprēķinu prizmas sānu virsmu ar pamata perimetru.",
        "Aprēķinu visu virsmas laukumu.",
        "Ievēroju, vai visas skaldnes tiešām ir jāskaita.",
    ]),

    Majas([
        "Izmēri kurpju kasti un aprēķini tās virsmas laukumu.",
        "Aprēķini, cik papīra vajag, lai ietītu dāvanu 30 × 20 × 10 cm.",
        "Paskaidro, kāpēc sānu virsma = P · h.",
    ]),
]
