# -*- coding: utf-8 -*-
"""3. klase, 28. stunda: «Cik apmēram sanāks?»

Aptuvenā vērtība nav slinkuma paveids, bet pārbaudes rīks: ja 23 · 4 sanāca
gandrīz 500, kļūda ir redzama, pat neizrēķinot precīzi. Te to māca kā pirmo
soli pirms rēķina, ne pēc tā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Cik apmēram sanāks?"

MERKIS = ("Prognozēsim reizinājuma vai dalījuma aptuveno vērtību un "
          "izmantosim to rezultāta pārbaudei.")

SATURS = [
    Sakums("Kā pamanīt kļūdu, vēl nesākot rēķināt?",
           zimejums=kolonnas([("apmēram", 80), ("precīzi", 92)]),
           paraksts="23 · 4 ir apmēram 20 · 4 = 80; precīzā atbilde ir 92.",
           fakti=["Aptuveno vērtību iegūst, skaitli noapaļojot.",
                  "Ja precīzā atbilde ir tālu no aptuvenās, kaut kas nav "
                  "kārtībā."]),

    Doma("Vispirms novērtē, tad rēķini",
         "Noapaļo skaitli līdz tuvākajam desmitam, izrēķini galvā un salīdzini "
         "ar precīzo atbildi.",
         soli=[
             "Noapaļo divciparu skaitli līdz tuvākajam desmitam.",
             "Izrēķini reizinājumu ar apaļo skaitli galvā.",
             "Izrēķini precīzo atbildi.",
             "Salīdzini: abām jābūt tuvu viena otrai.",
         ],
         pieze="Ja noapaļoja *uz augšu*, precīzā atbilde būs mazāka; ja uz "
               "leju - lielāka. Tas pasaka, kurā pusē gaidīt rezultātu."),

    Paraugs("Cik apmēram ir 38 · 3?",
            uzd="Novērtē 38 · 3 un pēc tam izrēķini precīzi.",
            soli=[
                ("38 ≈ 40",
                 "Noapaļo līdz tuvākajam desmitam - uz augšu."),
                ("40 · 3 = 120",
                 "Aptuvenā vērtība; precīzā būs mazliet mazāka."),
                ("38 · 3 = 90 + 24 = 114",
                 "Precīzais rēķins pa daļām."),
                ("114 ir tuvu 120",
                 "Atbilde iztur pārbaudi."),
            ],
            atbilde="apmēram 120, precīzi 114"),

    Ievadi("Novērtē aptuveni", [
        {"jaut": "Cik apmēram ir 19 · 5? (Noapaļo 19 līdz 20.)",
         "atb": ["100"], "padoms": "20 · 5."},
        {"jaut": "Cik precīzi ir 19 · 5?", "atb": ["95"],
         "padoms": "100 − 5."},
        {"jaut": "Cik apmēram ir 41 · 3? (Noapaļo 41 līdz 40.)",
         "atb": ["120"], "padoms": "40 · 3."},
        {"jaut": "Cik precīzi ir 41 · 3?", "atb": ["123"],
         "padoms": "120 + 3."},
        {"jaut": "Cik apmēram ir 62 : 3? (Noapaļo 62 līdz 60.)",
         "atb": ["20"], "padoms": "60 : 3."},
        {"jaut": "Cik apmēram ir 28 · 4? (Noapaļo 28 līdz 30.)",
         "atb": ["120"], "padoms": "30 · 4."},
    ], pamats=4),

    Zimejums("Aptuvenā un precīzā vērtība",
             kolonnas([("40 · 3", 120), ("38 · 3", 114), ("30 · 3", 90)]),
             paskaidro="Precīzā atbilde vienmēr ir starp abām apaļajām "
                       "vērtībām - tā arī notiek pārbaude.",
             ievads="38 ir starp 30 un 40."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "Skolēns uzrakstīja 23 · 4 = 812. Kā to pamanīt?",
         "opcijas": ["20 · 4 ir tikai 80", "23 · 4 ir vairāk par 1000",
                     "Atbilde ir par mazu", "Kļūdas nav"],
         "pareizi": 0, "padoms": "Aptuvenā vērtība ir tuvu 80, ne 800."},
        {"jaut": "Starp kuriem skaitļiem ir 27 · 3?",
         "opcijas": ["Starp 60 un 90", "Starp 30 un 60",
                     "Starp 90 un 120", "Starp 200 un 300"],
         "pareizi": 0, "padoms": "20 · 3 = 60 un 30 · 3 = 90."},
        {"jaut": "Cik apmēram ir 89 : 9?",
         "opcijas": ["10", "8", "20", "9"],
         "pareizi": 0, "padoms": "90 : 9 = 10."},
        {"jaut": "Kad precīzā atbilde ir *mazāka* par aptuveno?",
         "opcijas": ["Kad noapaļoja uz augšu", "Kad noapaļoja uz leju",
                     "Vienmēr", "Nekad"],
         "pareizi": 0, "padoms": "Uz augšu noapaļots skaitlis ir lielāks "
                                 "par īsto."},
    ], pamats=4),

    Pasaule("Vai pietiks naudas?",
            Ievadi("", [
                {"jaut": "Prece maksā 29 ct, vajag 4 gabalus. Cik apmēram "
                         "tas maksās? (Noapaļo līdz 30.)",
                 "atb": ["120"], "padoms": "30 · 4."},
                {"jaut": "Cik tas maksās precīzi?",
                 "atb": ["116"], "padoms": "120 − 4."},
                {"jaut": "Kabatā ir 150 ct. Vai pietiks? Raksti «jā» vai "
                         "«nē».",
                 "atb": ["jā", "ja"], "padoms": "116 < 150.",
                 "tastatura": "text"},
                {"jaut": "Cik centu paliks pāri?",
                 "atb": ["34"], "padoms": "150 − 116."},
            ]),
            pavediens="veikals",
            konteksts="Pie plaukta parasti nav laika rēķināt precīzi - "
                      "pietiek zināt, vai summa ir tuvu kabatai.",
            kapec="Aptuvenā vērtība atbild uz svarīgāko jautājumu: vai "
                  "pietiks."),

    Kopsavilkums([
        "Noapaļoju divciparu skaitli līdz tuvākajam desmitam.",
        "Prognozēju reizinājuma vai dalījuma aptuveno vērtību.",
        "Salīdzinu precīzo atbildi ar aptuveno un pamanu rupjas kļūdas.",
        "Zinu, kurā pusē gaidīt precīzo atbildi.",
    ]),

    Majas([
        "Novērtē un tad izrēķini 32 · 4, 48 · 2 un 71 · 3.",
        "Veikalā novērtē trīs preču summu, pirms paskaties čekā.",
        "Atrodi rēķinu, kurā aptuvenā un precīzā atbilde atšķiras vismazāk.",
    ]),
]
