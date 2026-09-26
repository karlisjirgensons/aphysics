# -*- coding: utf-8 -*-
"""1. klase, 143. stunda: «Cik smags un cik daudz?»

Masu mēra kilogramos (kg), šķidruma tilpumu - litros (l). Veikalā:
cukurs 1 kg, piens 1 l, kartupeļi 5 kg. Saskaita un salīdzina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, kolonnas)

TEMA = "Cik smags un cik daudz?"

MERKIS = ("Šodien lietosim kilogramu un litru, nosakot preču masu un "
          "tilpumu veikalā.")

SATURS = [
    Sakums("Kas smagāks: 1 kg cukura vai 1 kg spalvu?",
           fakti=["Abi sver 1 kg - tikpat!",
                  "Masu mēra kilogramos (kg).",
                  "Šķidrumu mēra litros (l)."]),

    Doma("kg un l",
         "Kilograms saka, cik smags; litrs - cik šķidruma.",
         soli=[
             "Cukurs, milti, kartupeļi - kg.",
             "Piens, sula, ūdens - l.",
             "Saskaita tāpat kā skaitļus: 2 kg + 3 kg = 5 kg.",
         ]),

    Varianti("kg vai l?", [
        {"jaut": "Maiss kartupeļu", "opcijas": ["kg", "l"],
         "jaukt": False, "pareizi": 0, "padoms": "Ciets - sver."},
        {"jaut": "Pudele sulas", "opcijas": ["l", "kg"], "jaukt": False,
         "pareizi": 0, "padoms": "Šķidrums."},
        {"jaut": "Paka miltu", "opcijas": ["kg", "l"], "jaukt": False,
         "pareizi": 0, "padoms": "Sver."},
        {"jaut": "Spainis ūdens", "opcijas": ["l", "kg"], "jaukt": False,
         "pareizi": 0, "padoms": "Šķidrums."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "2 kg āboli + 3 kg bumbieri = ? kg", "atb": ["5"],
         "padoms": "2 + 3."},
        {"jaut": "Spainī 10 l, izlēja 4 l. Cik l palika?", "atb": ["6"],
         "padoms": "10 − 4."},
        {"jaut": "Kurš maiss smagākais? Cik kg?",
         "zim": kolonnas([("kartupeļi", 5), ("sīpoli", 2), ("burkāni", 3)],
                         " kg"),
         "atb": ["5"], "padoms": "Augstākais stabiņš."},
        {"jaut": "3 pudeles pa 1 l. Cik litru?", "atb": ["3"],
         "padoms": "1 + 1 + 1."},
    ]),

    Pasaule("Iepirkšanās",
            Ievadi("", [
                {"jaut": "Somā 2 kg kartupeļu un 1 kg miltu. Cik kg nes?",
                 "atb": ["3"], "padoms": "2 + 1."},
                {"jaut": "Plus 2 l piena (1 l ≈ 1 kg). Apmēram cik kg?",
                 "atb": ["5"], "padoms": "3 + 2."},
            ]),
            pavediens="veikals",
            konteksts="Tu palīdzi nest iepirkumus.",
            kapec="Kilogrami pasaka, cik smaga soma."),

    Kopsavilkums([
        "Zinu, ka masu mēra kg.",
        "Zinu, ka šķidrumu mēra l.",
        "Saskaitu un salīdzinu kg un l.",
    ]),

    Majas([
        "Atrodi virtuvē 3 produktus ar kg un 3 ar l.",
        "Kurš visvieglākais?",
        "Nosver sevi (ar pieaugušo) - cik kg?",
    ]),
]
