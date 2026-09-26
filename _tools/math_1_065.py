# -*- coding: utf-8 -*-
"""1. klase, 65. stunda: «Kuri skaitļi ir starp?»

Skaitļi starp 36 un 42 ir 37, 38, 39, 40, 41 - paši galapunkti neskaitās.
Simta kvadrātā tos redz pēc kārtas, arī pāri rindas malai.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, simta_kvadrats)

TEMA = "Kuri skaitļi ir starp?"

MERKIS = ("Šodien nosauksim skaitļus starp diviem dotiem, izmantojot simta "
          "kvadrātu.")

SATURS = [
    Sakums("Kuri skaitļi ir starp 36 un 42?",
           zimejums=simta_kvadrats(31, 50, izcelt=[37, 38, 39, 40, 41]),
           paraksts="37, 38, 39, 40, 41 - pieci skaitļi.",
           fakti=["«Starp» - bez pašiem galiem.",
                  "Simta kvadrātā tie stāv pēc kārtas.",
                  "Pēc 40 turpina nākamajā rindā."]),

    Doma("Starp diviem skaitļiem",
         "Sāc ar skaitli pēc pirmā un beidz pirms otrā.",
         soli=[
             "Pirmais: par 1 lielāks nekā mazākais.",
             "Skaiti uz priekšu.",
             "Apstājies pirms lielākā.",
         ]),

    Ievadi("Starp", [
        {"jaut": "Kurš skaitlis ir starp 59 un 61?", "atb": ["60"],
         "padoms": "Tikai viens."},
        {"jaut": "Cik skaitļu ir starp 36 un 42?", "atb": ["5"],
         "padoms": "37, 38, 39, 40, 41."},
        {"jaut": "Cik skaitļu ir starp 10 un 20?", "atb": ["9"],
         "padoms": "11 līdz 19."},
        {"jaut": "Mazākais skaitlis starp 78 un 85?", "atb": ["79"],
         "padoms": "Pēc 78."},
        {"jaut": "Lielākais skaitlis starp 78 un 85?", "atb": ["84"],
         "padoms": "Pirms 85."},
        {"jaut": "Kurš ir starp 49 un 51?", "atb": ["50"],
         "padoms": "Pusceļā."},
    ], pamats=4),

    Varianti("Vai ir starp?", [
        {"jaut": "Vai 42 ir starp 36 un 42?", "opcijas": ["Nē", "Jā"],
         "jaukt": False, "pareizi": 0, "padoms": "Galapunkts neskaitās."},
        {"jaut": "Vai 55 ir starp 50 un 60?", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "Vidū."},
    ]),

    Pasaule("Mājas uz ielas",
            Ievadi("", [
                {"jaut": "Tu dzīvo mājā nr. 23, draugs - nr. 27. Cik māju ir "
                         "starp jums (numuri pēc kārtas)?", "atb": ["3"],
                 "padoms": "24, 25, 26."},
            ]),
            pavediens="celojums",
            konteksts="Mājas uz ielas numurētas pēc kārtas.",
            kapec="«Starp» palīdz saskaitīt, cik jāpaiet garām."),

    Kopsavilkums([
        "Nosaucu skaitļus starp diviem dotiem.",
        "Zinu, ka galapunkti neskaitās.",
        "Saskaitu, cik to ir.",
    ]),

    Majas([
        "Kuri datumi ir starp tavu un mammas dzimšanas dienu šajā mēnesī?",
        "Nosauc skaitļus starp 88 un 95.",
        "Izdomā divus skaitļus ar 3 skaitļiem starp tiem.",
    ]),
]
