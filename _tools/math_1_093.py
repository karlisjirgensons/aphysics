# -*- coding: utf-8 -*-
"""1. klase, 93. stunda: «Kas kopīgs 8 − 3 un 18 − 3?»

18 − 3: desmits paliek, no vieniem atņem tāpat kā 8 − 3. Tātad
18 − 3 = 10 + 5 = 15. Analoģija ar pirmo desmitu, kā 78. stundā
saskaitīšanai.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, ramis)

TEMA = "Kas kopīgs 8 − 3 un 18 − 3?"

MERKIS = ("Šodien no divciparu skaitļa atņemsim viencipara skaitli, "
          "izmantojot pirmo desmitu.")

SATURS = [
    Sakums("8 − 3 = 5. Cik ir 18 − 3?",
           zimejums=ramis(15, 2),
           paraksts="Desmits paliek, 8 − 3 = 5: 15.",
           fakti=["18 = 10 + 8.",
                  "Atņem tikai no vieniem.",
                  "18 − 3 = 10 + 5 = 15."]),

    Slidnis("Tas pats otrajā desmitā", [
        {"v": "8 − 3 = 5", "teksts": "Pirmajā desmitā", "zim": ramis(5)},
        {"v": "18 − 3 = 15", "teksts": "Pilns desmits paliek",
         "zim": ramis(15, 2)},
    ]),

    Doma("Desmits paliek",
         "Ja vienu pietiek, atņem tikai no vieniem - desmits nemainās.",
         soli=[
             "Sadali: 18 = 10 + 8.",
             "Atņem no vieniem: 8 − 3 = 5.",
             "Pieliec desmitu: 15.",
         ]),

    Ievadi("Pāri", [
        {"jaut": "7 − 2 = 5. Cik ir 17 − 2?", "atb": ["15"],
         "padoms": "Desmits un 5."},
        {"jaut": "9 − 4 = 5. Cik ir 19 − 4?", "atb": ["15"],
         "padoms": "Desmits un 5."},
        {"jaut": "16 − 5 = ?", "atb": ["11"], "padoms": "6 − 5 = 1."},
        {"jaut": "14 − 4 = ?", "atb": ["10"], "padoms": "4 − 4 = 0."},
        {"jaut": "19 − 7 = ?", "atb": ["12"], "padoms": "9 − 7 = 2."},
        {"jaut": "15 − 3 = ?", "atb": ["12"], "padoms": "5 − 3 = 2."},
    ], pamats=4),

    Varianti("Kurš palīdz?", [
        {"jaut": "Kurš piemērs palīdz izrēķināt 17 − 5?",
         "opcijas": ["7 − 5", "17 − 7", "1 − 5"], "pareizi": 0,
         "padoms": "Vieni: 7 un 5."},
    ]),

    Pasaule("Zīmuļi penālī",
            Ievadi("", [
                {"jaut": "Penālī 18 zīmuļu, 4 aizdeva. Cik palika?",
                 "atb": ["14"], "padoms": "8 − 4 = 4."},
            ]),
            pavediens="skola",
            konteksts="Klasesbiedri aizņemas zīmuļus.",
            kapec="Zinot 8 − 4, zini arī 18 − 4."),

    Kopsavilkums([
        "Atņemu viencipara skaitli no divciparu.",
        "Izmantoju pirmā desmita piemērus.",
        "Zinu, ka desmits paliek.",
    ]),

    Majas([
        "Uzraksti 3 pārus kā 9 − 6 un 19 − 6.",
        "Izrēķini tos.",
        "Paskaidro mājiniekam, kas tiem kopīgs.",
    ]),
]
