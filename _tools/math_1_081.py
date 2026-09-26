# -*- coding: utf-8 -*-
"""1. klase, 81. stunda: «Vai summa mainās, mainot vietām?»

Arī 20 apjomā saskaitāmos var mainīt vietām: 3 + 14 = 14 + 3 = 17.
Lielāko liek pirmo - un tā pieskaitīt ir vieglāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, ramis)

TEMA = "Vai summa mainās, mainot vietām?"

MERKIS = ("Šodien no piemēriem secināsim, ka saskaitāmos var mainīt vietām, "
          "un lietosim to.")

SATURS = [
    Sakums("3 + 14 - kā ātrāk?",
           zimejums=ramis(17, 2, otra=3),
           paraksts="14 + 3: no 14 trīs uz priekšu - 17.",
           fakti=["3 + 14 = 14 + 3.",
                  "Sāc ar lielāko.",
                  "Summa nemainās."]),

    Doma("Lielāko pirmo",
         "Samaini saskaitāmos, ja otrais ir lielāks.",
         soli=[
             "Atrodi lielāko saskaitāmo.",
             "Uzraksti to pirmo.",
             "Pieskaiti mazāko.",
         ]),

    Ievadi("Samaini un saskaiti", [
        {"jaut": "2 + 15 = ?", "atb": ["17"], "padoms": "15 + 2."},
        {"jaut": "4 + 13 = ?", "atb": ["17"], "padoms": "13 + 4."},
        {"jaut": "1 + 18 = ?", "atb": ["19"], "padoms": "18 + 1."},
        {"jaut": "5 + 11 = ?", "atb": ["16"], "padoms": "11 + 5."},
        {"jaut": "3 + 16 = ?", "atb": ["19"], "padoms": "16 + 3."},
        {"jaut": "6 + 12 = ?", "atb": ["18"], "padoms": "12 + 6."},
    ], pamats=4),

    Varianti("Vienādi?", [
        {"jaut": "7 + 12 un 12 + 7", "opcijas": ["vienādi", "dažādi"],
         "jaukt": False, "pareizi": 0, "padoms": "Abi 19."},
        {"jaut": "15 − 3 un 3 − 15", "opcijas": ["vienādi", "dažādi"],
         "jaukt": False, "pareizi": 1, "padoms": "Atņemšanā nedrīkst."},
    ]),

    Pasaule("Kastaņi",
            Ievadi("", [
                {"jaut": "Ance atnesa 4 kastaņus, Jēkabs - 14. Cik kopā?",
                 "atb": ["18"], "padoms": "14 + 4."},
            ]),
            pavediens="daba",
            konteksts="Kastaņus saliek vienā kastē.",
            kapec="Nav svarīgi, kura kastaņi pirmie."),

    Kopsavilkums([
        "Zinu, ka saskaitāmos var mainīt vietām.",
        "Saskaitot sāku ar lielāko.",
        "Atņemšanā vietas nemainu.",
    ]),

    Majas([
        "Izrēķini 2 + 16 divos veidos.",
        "Kurš bija vieglāks?",
        "Izdomā piemēru, kur maiņa ļoti palīdz.",
    ]),
]
