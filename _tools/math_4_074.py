# -*- coding: utf-8 -*-
"""4. klase, 74. stunda: «Cik apmēram sanāks?»

Mikrotemata noslēgums. Divciparu reizinātājus noapaļo līdz desmitiem un
sareizina galvā ar nuļļu triku: 48 · 32 ≈ 50 · 30 = 1500. Tā ir pārbaude,
bez kuras nevajadzētu sākt nevienu divciparu stabiņu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Cik apmēram sanāks?"

MERKIS = ("Noteiksim reizinājuma aptuveno vērtību, reizinot tuvākos pilnos "
          "desmitus.")

SATURS = [
    Sakums("Vai 48 kastēs pa 32 olām ir vairāk par 1000?",
           zimejums=kolonnas([("aptuveni", 1500), ("precīzi", 1536),
                              ("robeža", 1000)]),
           paraksts="48 ≈ 50, 32 ≈ 30, 50 · 30 = 1500.",
           fakti=["Aptuvenā atbilde galvā - dažās sekundēs.",
                  "Tā uzreiz pasaka: jā, vairāk par 1000."]),

    Doma("Abus reizinātājus noapaļo līdz desmitiem",
         "Divu divciparu skaitļu reizinājumu novērtē, reizinot tuvākos pilnos "
         "desmitus.",
         soli=[
             "Noapaļo katru reizinātāju: 48 ≈ 50, 32 ≈ 30.",
             "Sareizini: 5 · 3 = 15, pieliek 00 - 1500.",
             "Precīzā atbilde būs tuvu 1500.",
             "Ja precīzā ir 150 vai 15 000 - meklē kļūdu.",
         ],
         pieze="Ja vienu reizinātāju noapaļoji uz augšu, otru uz leju, "
               "novērtējums parasti ir ļoti tuvs."),

    Paraugs("Novērtē 67 · 23",
            uzd="Novērtē 67 · 23.",
            soli=[
                ("67 ≈ 70, 23 ≈ 20", None),
                ("70 · 20 = 1400", None),
                ("67 · 23 = 1541", "Precīzi - tuvu 1400."),
            ],
            atbilde="apmēram 1400"),

    Kustiba("Kur apstāsies?", [
        {"jaut": "Novērtē 48 · 32 ≈ 50 · 30. Aizved līdz novērtējumam.",
         "atb": 1500, "beigas": 5000, "iedala": 500,
         "merkis": "≈", "objekts": "Vilciens",
         "padoms": "15 un 00.",
         "stasts": "Vilciens brauc līdz aptuvenajai vērtībai."},
        {"jaut": "Novērtē 81 · 39 ≈ 80 · 40.",
         "atb": 3200, "beigas": 5000, "iedala": 500,
         "merkis": "≈", "objekts": "Vilciens", "padoms": "32 un 00."},
        {"jaut": "Novērtē 19 · 21 ≈ 20 · 20.",
         "atb": 400, "beigas": 5000, "iedala": 500,
         "merkis": "≈", "objekts": "Vilciens", "padoms": "4 un 00."},
        {"jaut": "Novērtē 58 · 71 ≈ 60 · 70.",
         "atb": 4200, "beigas": 5000, "iedala": 500,
         "merkis": "≈", "objekts": "Vilciens", "padoms": "42 un 00."},
    ], pamats=2),

    Ievadi("Novērtē", [
        {"jaut": "29 · 41 ≈ ?", "atb": ["1200"], "padoms": "30 · 40."},
        {"jaut": "52 · 18 ≈ ?", "atb": ["1000"], "padoms": "50 · 20."},
        {"jaut": "73 · 62 ≈ ?", "atb": ["4200"], "padoms": "70 · 60."},
        {"jaut": "88 · 11 ≈ ?", "atb": ["900"], "padoms": "90 · 10."},
    ]),

    Varianti("Ticams vai nē?", [
        {"jaut": "48 · 32 = 1536. Ticams?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "≈ 1500."},
        {"jaut": "39 · 41 = 1159. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "≈ 1600; pareizi 1599."},
        {"jaut": "91 · 19 = 17 290. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "≈ 1800; pareizi 1729."},
        {"jaut": "Cik ciparu būs 64 · 27?",
         "opcijas": ["4", "3", "5", "2"], "pareizi": 0,
         "padoms": "60 · 30 = 1800."},
    ], pamats=4),

    Pasaule("Skolas ēdnīca mēnesī",
            Ievadi("", [
                {"jaut": "Klasē 28 skolēni, mēnesī 21 skolas diena. "
                         "Novērtē pusdienu skaitu: 30 · 20 = ?",
                 "atb": ["600"], "padoms": "3 · 2 un 00."},
                {"jaut": "Precīzi: 28 · 21 = ?", "atb": ["588"],
                 "padoms": "28 · 20 + 28."},
                {"jaut": "Pusdienas maksā 3 €. Novērtē mēneša summu klasei: "
                         "600 · 3 = ?",
                 "atb": ["1800"], "padoms": "6 · 3 un 00."},
                {"jaut": "Precīzi: 588 · 3 = ?", "atb": ["1764"],
                 "padoms": "1500 + 240 + 24."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīcas vadītāja vispirms novērtē, cik produktu "
                      "vajag, un tikai tad rēķina precīzi.",
            kapec="Novērtējums pasaka, vai plāns ir saprātīgs."),

    Kopsavilkums([
        "Noapaļoju reizinātājus līdz desmitiem.",
        "Novērtēju reizinājumu galvā.",
        "Pārbaudu precīzo atbildi ar novērtējumu.",
    ]),

    Majas([
        "Novērtē, cik stundu tu pavadi skolā gadā (6 · 172 ≈ ?).",
        "Novērtē, cik lappušu izlasīsi, ja 31 dienu lasīsi pa 18 lappusēm.",
        "Pārbaudi novērtējumu ar kalkulatoru.",
    ]),
]
