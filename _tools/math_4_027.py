# -*- coding: utf-8 -*-
"""4. klase, 27. stunda: «Kāpēc drīkst reizināt pa daļām?»

Trīs stundas skolēns reizināja pa daļām; tagad to nosauc: (a + b) · c =
a · c + b · c. Rūtiņu taisnstūris to pierāda - viens taisnstūris ir divu
taisnstūru summa. Tas ir sadalīšanas likums, uz kā stāv viss reizināšanas
stabiņš un vēlāk algebra.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kāpēc drīkst reizināt pa daļām?"

MERKIS = ("Lietosim un paskaidrosim īpašību (a + b) · c = a · c + b · c.")

SATURS = [
    Sakums("Kā ātri izrēķināt dārza laukumu?",
           zimejums=figura([(0, 0), (13, 0), (13, 4), (10, 4), (10, 0),
                            (10, 4), (0, 4)],
                           uzraksti=[(5, 2, "10 · 4"), (11.5, 2, "3 · 4")],
                           platums=14, augstums=5),
           paraksts="13 · 4 = 10 · 4 + 3 · 4.",
           fakti=["Dobi 13 × 4 var sadalīt divās: 10 × 4 un 3 × 4.",
                  "Rūtiņu skaits nemainās, ja taisnstūri sagriež."]),

    Doma("(a + b) · c = a · c + b · c",
         "Summu var reizināt, reizinot katru saskaitāmo atsevišķi un "
         "rezultātus saskaitot.",
         soli=[
             "Uzraksti vienu reizinātāju kā summu: 13 = 10 + 3.",
             "Reizini katru saskaitāmo: 10 · 4 un 3 · 4.",
             "Saskaiti: 40 + 12 = 52.",
             "Pārbaude: taisnstūrī 13 × 4 ir 52 rūtiņas.",
         ],
         pieze="Tā pati īpašība der atņemšanai: (a − b) · c = a · c − b · c. "
               "19 · 3 = 20 · 3 − 1 · 3 = 57."),

    Paraugs("(30 + 7) · 5",
            uzd="Izrēķini (30 + 7) · 5 divos veidos.",
            soli=[
                ("37 · 5 = 185", "1. veids: vispirms iekavas, 30 + 7 = 37."),
                ("30 · 5 + 7 · 5 = 150 + 35", "2. veids: pa daļām."),
                ("150 + 35 = 185", "Abi veidi dod vienu atbildi."),
            ],
            atbilde="185"),

    Zimejums("Viens taisnstūris - divi taisnstūri",
             figura([(0, 0), (8, 0), (8, 5), (5, 5), (5, 0), (5, 5),
                     (0, 5)],
                    uzraksti=[(2.5, 2.5, "5 · 5"), (6.5, 2.5, "3 · 5")],
                    platums=9, augstums=6, aizpildi=False),
             paskaidro="(5 + 3) · 5 = 5 · 5 + 3 · 5 = 25 + 15 = 40.",
             ievads="Svītra sadala taisnstūri; laukums paliek tas pats."),

    Ievadi("Pa daļām", [
        {"jaut": "(20 + 6) · 3 = ?", "atb": ["78"], "padoms": "60 + 18."},
        {"jaut": "(40 + 5) · 2 = ?", "atb": ["90"], "padoms": "80 + 10."},
        {"jaut": "(100 + 4) · 6 = ?", "atb": ["624"], "padoms": "600 + 24."},
        {"jaut": "(50 − 1) · 4 = ?", "atb": ["196"], "padoms": "200 − 4."},
        {"jaut": "29 · 3 = 30 · 3 − ? Ieraksti trūkstošo.", "atb": ["3"],
         "padoms": "1 · 3."},
        {"jaut": "7 · 12 = 7 · 10 + 7 · ?", "atb": ["2"],
         "padoms": "12 = 10 + 2."},
    ], pamats=4),

    Varianti("Vai vienādība patiesa?", [
        {"jaut": "(10 + 4) · 3 = 10 · 3 + 4 · 3",
         "opcijas": ["patiesa", "aplama"], "pareizi": 0,
         "padoms": "Reizina abus saskaitāmos."},
        {"jaut": "(10 + 4) · 3 = 10 · 3 + 4",
         "opcijas": ["aplama", "patiesa"], "pareizi": 0,
         "padoms": "Aizmirsa sareizināt 4 ar 3."},
        {"jaut": "8 · 25 = 8 · 20 + 8 · 5",
         "opcijas": ["patiesa", "aplama"], "pareizi": 0,
         "padoms": "25 = 20 + 5."},
        {"jaut": "(6 + 2) · 5 = 6 + 2 · 5",
         "opcijas": ["aplama", "patiesa"], "pareizi": 0,
         "padoms": "Pa kreisi 40, pa labi 16."},
    ], pamats=4),

    Pasaule("Stadiona sēdvietas",
            Ievadi("", [
                {"jaut": "Tribīnē 8 rindas, katrā 25 vietas: 20 un vēl 5. "
                         "8 · 20 + 8 · 5 = ?",
                 "atb": ["200"], "padoms": "160 + 40."},
                {"jaut": "Otrā tribīnē 6 rindas pa 34 vietām. Cik vietu?",
                 "atb": ["204"], "padoms": "6 · 30 + 6 · 4."},
                {"jaut": "Trešā tribīnē 9 rindas pa 19 vietām. Cik vietu?",
                 "atb": ["171"], "padoms": "9 · 20 − 9."},
                {"jaut": "Cik vietu visās trijās tribīnēs?",
                 "atb": ["575"], "padoms": "200 + 204 + 171."},
            ]),
            pavediens="sports",
            konteksts="Tribīne ir taisnstūris no sēdvietām - rindas reiz "
                      "vietas rindā.",
            kapec="Pa daļām rēķināt ir ātrāk nekā skaitīt katru vietu."),

    Kopsavilkums([
        "Zinu īpašību (a + b) · c = a · c + b · c.",
        "Paskaidroju to ar rūtiņu taisnstūri.",
        "Izmantoju to arī ar atņemšanu: 19 · 3 = 60 − 3.",
    ]),

    Majas([
        "Uzzīmē rūtiņās taisnstūri 12 × 5 un parādi, kā to sadalīt.",
        "Izrēķini 98 · 4 ar (100 − 2) · 4.",
        "Paskaidro mājiniekiem, kāpēc drīkst reizināt pa daļām.",
    ]),
]
