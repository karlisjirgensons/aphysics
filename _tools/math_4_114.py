# -*- coding: utf-8 -*-
"""4. klase, 114. stunda: «Kas sanāk, reizinot veselu skaitli ar daļu?»

3 · {2|5} = {2|5} + {2|5} + {2|5} = {6|5}: uz skaitļu taisnes trīs lēcieni
pa {2|5}. Secinājums: skaitītāju reizina, saucējs paliek. Tas ir vesela
skaitļa un daļas reizinājums - daļu reizināšana ar daļu ir 5. klases tēma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, taisne)

TEMA = "Kas sanāk, reizinot veselu skaitli ar daļu?"

MERKIS = ("Modelēsim uz skaitļu taisnes vesela skaitļa un daļas "
          "reizinājumu un secināsim rezultātu.")

SATURS = [
    Sakums("Trīs lēcieni pa {2|5}",
           zimejums=taisne(0, 2, 1, [(1.2, "6/5")], sikas=5,
                           bultas=[(0, 0.4, "2/5"), (0.4, 0.8, "2/5"),
                                   (0.8, 1.2, "2/5")]),
           paraksts="3 · {2|5} = {6|5}.",
           fakti=["Reizinājums - vienādi lēcieni pa taisni.",
                  "Trīs lēcieni pa divām piektdaļām - sešas piektdaļas."]),

    Doma("Reizina skaitītāju, saucējs paliek",
         "Veselu skaitli reizinot ar daļu, reizina skaitli ar skaitītāju, "
         "bet saucēju pārraksta: k · {a|n} = {k · a|n}.",
         soli=[
             "3 · {2|5} = {2|5} + {2|5} + {2|5}.",
             "Skaitītāju summa: 2 + 2 + 2 = 3 · 2 = 6.",
             "Saucējs paliek 5.",
             "3 · {2|5} = {6|5}.",
         ],
         pieze="Saucēju nereizina - tas pasaka gabalu izmēru, un tas "
               "nemainās."),

    Paraugs("4 · {3|8}",
            uzd="Izrēķini 4 · {3|8}.",
            soli=[
                ("4 · {3|8} = {4 · 3|8}", None),
                ("= {12|8}", None),
                ("{12|8} = 1 + {4|8}", "Neīsta daļa ar veselo."),
            ],
            atbilde="{12|8}"),

    Ievadi("Reizini", [
        {"jaut": "3 · {2|5} = ?", "atb": ["6/5"], "vieta": "piem., 1/2",
         "padoms": "3 · 2 = 6."},
        {"jaut": "2 · {3|7} = ?", "atb": ["6/7"], "vieta": "piem., 1/2",
         "padoms": "2 · 3."},
        {"jaut": "5 · {1|4} = ?", "atb": ["5/4"], "vieta": "piem., 1/2",
         "padoms": "5 · 1."},
        {"jaut": "4 · {3|8} = ?", "atb": ["12/8"], "vieta": "piem., 1/2",
         "padoms": "4 · 3."},
        {"jaut": "6 · {2|3} = ? (vesels skaitlis)", "atb": ["4"],
         "padoms": "{12|3} = 4."},
        {"jaut": "10 · {1|10} = ?", "atb": ["1"], "padoms": "{10|10}."},
    ], pamats=4),

    Varianti("Pareizi vai aplami?", [
        {"jaut": "2 · {3|5} = {6|10}",
         "opcijas": ["aplami", "pareizi"], "pareizi": 0,
         "padoms": "Saucēju nereizina: {6|5}."},
        {"jaut": "3 · {1|3} = 1",
         "opcijas": ["pareizi", "aplami"], "pareizi": 0,
         "padoms": "{3|3} = 1."},
        {"jaut": "4 · {2|9} = {8|9}",
         "opcijas": ["pareizi", "aplami"], "pareizi": 0,
         "padoms": "4 · 2 = 8."},
        {"jaut": "Kurš reizinājums ir lielāks par 1?",
         "opcijas": ["3 · {2|5}", "2 · {2|5}", "1 · {2|5}", "2 · {1|5}"],
         "pareizi": 0, "padoms": "{6|5} > 1."},
    ], pamats=4),

    Pasaule("Vitamīni un ūdens",
            Ievadi("", [
                {"jaut": "Dienā izdzer {3|4} l ūdens skolā. Cik litru 5 skolas "
                         "dienās? Raksti daļu.",
                 "atb": ["15/4"], "vieta": "piem., 1/2",
                 "padoms": "5 · 3."},
                {"jaut": "Cik veselu litru ir {15|4} l?", "atb": ["3"],
                 "padoms": "15 : 4 = 3 (atl. 3)."},
                {"jaut": "Tablete ir {1|2} no devas, dzer 3 reizes. Cik "
                         "devu? Raksti daļu.",
                 "atb": ["3/2"], "vieta": "piem., 1/2", "padoms": "3 · 1."},
                {"jaut": "Suns dienā apēd {2|3} bundžas. Cik bundžu 6 "
                         "dienās?",
                 "atb": ["4"], "padoms": "{12|3} = 4."},
            ]),
            pavediens="daba",
            konteksts="Daudz ikdienas daudzumu ir daļas, kas atkārtojas "
                      "katru dienu.",
            kapec="Reizinājums parāda, cik sanāk nedēļā vai mēnesī."),

    Kopsavilkums([
        "Reizinu veselu skaitli ar daļu.",
        "Reizinu skaitītāju, saucēju pārrakstu.",
        "Modelēju reizinājumu ar lēcieniem pa taisni.",
    ]),

    Majas([
        "Izrēķini, cik litru piena ģimene izdzer nedēļā, ja dienā {3|4} l.",
        "Uzzīmē taisni un parādi 4 · {1|3}.",
        "Paskaidro kādam, kāpēc saucēju nereizina.",
    ]),
]
