# -*- coding: utf-8 -*-
"""4. klase, 75. stunda: «Kā sadalīt reizinājumu pa daļām?»

Divu divciparu skaitļu reizināšanas pirmais ceļš: vienu reizinātāju
sadala desmitos un vienos. 23 · 14 = 23 · 10 + 23 · 4. Abi gabali jau ir
zināmi - reizināšana ar 10 un ar viencipara skaitli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā sadalīt reizinājumu pa daļām?"

MERKIS = ("Reizināsim divus divciparu skaitļus pakāpeniski, izsakot skaitli "
          "kā summu.")

SATURS = [
    Sakums("Cik stundu ir 14 diennaktīs?",
           zimejums=restis([["24 · 14", "=", "24 · 10", "+", "24 · 4"],
                            ["", "=", "240", "+", "96"],
                            ["", "=", "336", "", ""]],
                           "divas nedēļas stundās"),
           paraksts="Diennaktī 24 stundas, divās nedēļās 14 diennaktis.",
           fakti=["Grūtu reizinājumu sadala divos vieglos.",
                  "Tas pats likums, ko 27. stundā: (a + b) · c."]),

    Doma("Sadali vienu reizinātāju desmitos un vienos",
         "a · 14 = a · 10 + a · 4: reizini ar desmitiem, tad ar vieniem un "
         "saskaiti.",
         soli=[
             "Izvēlies reizinātāju, ko sadalīt: 14 = 10 + 4.",
             "Reizini ar desmitiem: 24 · 10 = 240.",
             "Reizini ar vieniem: 24 · 4 = 96.",
             "Saskaiti: 240 + 96 = 336.",
         ],
         pieze="Ja reizinātājs ir 38, sadala 30 + 8: a · 30 + a · 8."),

    Paraugs("35 · 26",
            uzd="Izrēķini 35 · 26 pa daļām.",
            soli=[
                ("26 = 20 + 6", None),
                ("35 · 20 = 700", "35 · 2 = 70, pieliek 0."),
                ("35 · 6 = 210", None),
                ("700 + 210 = 910", "Pārbaude: 910 ir starp 30 · 26 = 780 un "
                 "40 · 26 = 1040."),
            ],
            atbilde="910"),

    Slidnis("47 · 13 pa daļām",
            soli=[
                {"v": "47 · 13", "teksts": "13 = 10 + 3."},
                {"v": "47 · 10 = 470", "teksts": "Desmiti.", "josla": 77},
                {"v": "47 · 3 = 141", "teksts": "Vieni.", "josla": 23},
                {"v": "470 + 141 = 611", "teksts": "Kopā.", "josla": 100},
            ],
            ievads="Josla rāda, cik liela daļa nāk no katra gabala."),

    Ievadi("Pa daļām", [
        {"jaut": "24 · 14 = ?", "atb": ["336"], "padoms": "240 + 96."},
        {"jaut": "32 · 12 = ?", "atb": ["384"], "padoms": "320 + 64."},
        {"jaut": "45 · 21 = ?", "atb": ["945"], "padoms": "900 + 45."},
        {"jaut": "18 · 15 = ?", "atb": ["270"], "padoms": "180 + 90."},
        {"jaut": "56 · 23 = ?", "atb": ["1288"], "padoms": "1120 + 168."},
        {"jaut": "73 · 31 = ?", "atb": ["2263"], "padoms": "2190 + 73."},
    ], pamats=4),

    Varianti("Kurš sadalījums pareizs?", [
        {"jaut": "Kā sadalīt 27 · 16?",
         "opcijas": ["27 · 10 + 27 · 6", "27 · 10 + 6",
                     "27 + 16 · 10", "20 · 10 + 7 · 6"], "pareizi": 0,
         "padoms": "16 = 10 + 6, katrs reiz 27."},
        {"jaut": "Kas nav kārtībā: 43 · 12 = 430 + 2 = 432?",
         "opcijas": ["jāpieskaita 43 · 2 = 86", "viss pareizi",
                     "jāpieskaita 12"], "pareizi": 0,
         "padoms": "Pareizi 430 + 86 = 516."},
        {"jaut": "Cik ir 43 · 12?",
         "opcijas": ["516", "432", "473", "526"], "pareizi": 0,
         "padoms": "430 + 86."},
    ]),

    Pasaule("Bitenieka rēķini",
            Ievadi("", [
                {"jaut": "Dravā 24 stropi, katrā 15 kg medus sezonā. Cik kg?",
                 "atb": ["360"], "padoms": "24 · 10 + 24 · 5."},
                {"jaut": "Medu pilda 500 g burciņās - katrā kilogramā divas. "
                         "Cik burciņu sanāk no 360 kg?",
                 "atb": ["720"], "padoms": "Katrā kg divas burciņas."},
                {"jaut": "Burciņa maksā 12 €. Cik maksā 25 burciņas?",
                 "atb": ["300"], "padoms": "12 · 25 = 12 · 20 + 12 · 5."},
                {"jaut": "Vienā stropā 18 rāmīši. Cik rāmīšu 24 stropos?",
                 "atb": ["432"], "padoms": "18 · 20 + 18 · 4."},
            ]),
            pavediens="daba",
            konteksts="Latvijas biškopji no stropa sezonā iegūst vidēji "
                      "15-25 kg medus.",
            kapec="Pa daļām var sareizināt jebkurus divciparu skaitļus."),

    Kopsavilkums([
        "Sadalu divciparu reizinātāju desmitos un vienos.",
        "Reizinu pa daļām un saskaitu.",
        "Pārbaudu ar aptuveno vērtību.",
    ]),

    Majas([
        "Izrēķini, cik stundu ir 31 diennaktī.",
        "Izrēķini, cik mēnešu tu esi nodzīvojis (vecums · 12).",
        "Izdomā reizinājumu un sadali to divos veidos.",
    ]),
]
