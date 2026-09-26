# -*- coding: utf-8 -*-
"""4. klase, 15. stunda: «Cik apmēram sanāks?»

Aptuvenā vērtība ir drošības josta: pirms rēķina to izrēķina galvā, pēc
rēķina salīdzina. Ja precīzā atbilde ir tālu no aptuvenās, kaut kur ir
kļūda. Te noder 11. stundas noapaļošana un 12. stundas galvas rēķins.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Cik apmēram sanāks?"

MERKIS = ("Noteiksim summas un starpības aptuveno vērtību un lietosim to "
          "precīzā rezultāta pārbaudei.")

SATURS = [
    Sakums("Vai kalkulators var kļūdīties?",
           zimejums=kolonnas([("aptuveni", 7000), ("kalkulatorā", 4213)]),
           paraksts="3876 + 3137 ≈ 4000 + 3000 = 7000. Bet ekrānā 4213?",
           fakti=["Kalkulators rēķina pareizi, bet cilvēks var nospiest "
                  "garām.",
                  "Aptuvenā vērtība uzreiz parāda, ka kaut kas nav kārtībā."]),

    Doma("Vispirms noapaļo, tad rēķini galvā",
         "Aptuvenā vērtība ir tuvu precīzajai; ja tās atšķiras daudz, "
         "precīzajā ir kļūda.",
         soli=[
             "Noapaļo katru skaitli līdz tūkstošiem vai simtiem.",
             "Saskaiti vai atņem noapaļotos skaitļus galvā.",
             "Izrēķini precīzi rakstos.",
             "Salīdzini: vai precīzā atbilde ir tuvu aptuvenajai?",
         ],
         pieze="Līdz simtiem noapaļo, ja vajag precīzāku pārbaudi: "
               "3876 + 3137 ≈ 3900 + 3100 = 7000."),

    Paraugs("Pārbaudi Annas atbildi",
            uzd="Anna izrēķināja 6128 − 2947 = 4181. Vai tas ticams?",
            soli=[
                ("6128 ≈ 6000, 2947 ≈ 3000", "Noapaļo līdz tūkstošiem."),
                ("6000 − 3000 = 3000", "Aptuvenā starpība."),
                ("4181 ir tālu no 3000", "Te ir kļūda."),
                ("6128 − 2947 = 3181", "Precīzi pārrēķinot."),
            ],
            atbilde="nē, pareizi ir 3181"),

    Ievadi("Aptuveni līdz tūkstošiem", [
        {"jaut": "4128 + 2915 ≈ ?", "atb": ["7000"],
         "padoms": "4000 + 3000."},
        {"jaut": "8740 − 3160 ≈ ?", "atb": ["6000"],
         "padoms": "9000 − 3000."},
        {"jaut": "1890 + 5230 ≈ ?", "atb": ["7000"],
         "padoms": "2000 + 5000."},
        {"jaut": "9520 − 4480 ≈ ?", "atb": ["6000"],
         "padoms": "10 000 − 4000."},
        {"jaut": "Līdz simtiem: 2380 + 1640 ≈ ?", "atb": ["4000"],
         "padoms": "2400 + 1600."},
        {"jaut": "Līdz simtiem: 5530 − 2270 ≈ ?", "atb": ["3200"],
         "padoms": "5500 − 2300."},
    ], pamats=4),

    Varianti("Vai atbilde ticama?", [
        {"jaut": "3021 + 4987 = 8008. Ticams?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "3000 + 5000 = 8000."},
        {"jaut": "7215 − 2980 = 5235. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "7000 − 3000 = 4000; pareizi 4235."},
        {"jaut": "2654 + 3218 = 872. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "Aptuveni 6000 - trūkst šķiras."},
        {"jaut": "9002 − 999 = 8003. Ticams?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "9000 − 1000 = 8000."},
    ], pamats=4),

    Zimejums("Aptuvenā un precīzā - kaimiņi",
             kolonnas([("4128 + 2915", 7043), ("4000 + 3000", 7000)]),
             paskaidro="Stabiņi gandrīz vienādi - tāpēc aptuvenā vērtība ir "
                       "laba pārbaude.",
             ievads="Kad viss pareizi, stabiņi ir gandrīz vienā augstumā."),

    Pasaule("Vai nauda pietiks?",
            Ievadi("", [
                {"jaut": "Televizors 1890 €, skaļruņi 1180 €. Aptuveni cik "
                         "kopā (līdz tūkstošiem)?",
                 "atb": ["3000"], "padoms": "2000 + 1000."},
                {"jaut": "Precīzi cik kopā?", "atb": ["3070"],
                 "padoms": "1890 + 1180."},
                {"jaut": "Ir 3500 €. Cik paliks precīzi?",
                 "atb": ["430"], "padoms": "3500 − 3070."},
                {"jaut": "Planšete 2950 € - vai ar 3000 € pietiek? Atbildi "
                         "«jā» vai «nē».",
                 "atb": ["jā", "ja"], "tastatura": "text",
                 "padoms": "2950 < 3000."},
            ]),
            pavediens="veikals",
            konteksts="Pirms kases vērts aptuveni saskaitīt - tad nav "
                      "pārsteigumu.",
            kapec="Aptuvenais rēķins galvā aizņem sekundes, bet pasargā no "
                  "lielas kļūdas."),

    Kopsavilkums([
        "Nosaku summas un starpības aptuveno vērtību.",
        "Salīdzinu precīzo atbildi ar aptuveno.",
        "Pamanu kļūdu, ja atbildes ļoti atšķiras.",
    ]),

    Majas([
        "Veikalā aptuveni saskaiti pirkumu un pēc tam salīdzini ar čeku.",
        "Izrēķini kalkulatorā 2 summas un pārbaudi tās ar aptuveno vērtību.",
        "Izdomā «aplamu» atbildi un palūdz mājiniekam to atmaskot.",
    ]),
]
