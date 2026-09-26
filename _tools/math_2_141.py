# -*- coding: utf-8 -*-
"""2. klase, 141. stunda: «Kā izveidot reizināšanas ar 3 tabulu?»

Tabulu būvē tāpat kā ar 2: katrs nākamais par 3 lielāks. Pārbauda ar
modeli (rindas pa 3). Tabulā ir raksts: ciparu summa reizinājumiem ar 3
vienmēr ir 3, 6 vai 9.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis, rutinas)

TEMA = "Kā izveidot reizināšanas ar 3 tabulu?"

MERKIS = ("Šodien izveidosim reizināšanas ar 3 tabulu un pārbaudīsim to ar "
          "modeli.")

_TABULA = restis([["1 · 3", "2 · 3", "3 · 3", "4 · 3", "5 · 3"],
                  [3, 6, 9, 12, 15],
                  ["6 · 3", "7 · 3", "8 · 3", "9 · 3", "10 · 3"],
                  [18, 21, 24, 27, 30]])

SATURS = [
    Sakums("Kā uzbūvēt tabulu, ja zini tikai 1 · 3 = 3?",
           zimejums=_TABULA,
           paraksts="Katrs nākamais - par 3 vairāk.",
           fakti=["3, 6, 9, 12 ... 30.",
                  "Tabulu pārbauda ar rūtiņām.",
                  "Noslēpums: 12 → 1 + 2 = 3, 27 → 2 + 7 = 9."]),

    Doma("Tabulas būvēšana",
         "Katrs nākamais reizinājums ar 3 ir par 3 lielāks.",
         soli=[
             "1 · 3 = 3.",
             "2 · 3 = 3 + 3 = 6.",
             "3 · 3 = 6 + 3 = 9 ... līdz 10 · 3 = 30.",
             "Pārbaudi ar modeli: rindas pa 3.",
         ]),

    Ievadi("Tabula", [
        {"jaut": "4 · 3 = ?", "zim": rutinas(3, 4), "atb": ["12"],
         "padoms": "4 rindas pa 3."},
        {"jaut": "7 · 3 = ?", "atb": ["21"], "padoms": "6 · 3 + 3."},
        {"jaut": "? · 3 = 24", "atb": ["8"], "padoms": "Tabulā 24."},
        {"jaut": "? · 3 = 15", "atb": ["5"], "padoms": "Tabulā 15."},
        {"jaut": "9 · 3 = ?", "atb": ["27"], "padoms": "10 · 3 − 3."},
        {"jaut": "6 · 3 = ?", "atb": ["18"], "padoms": "5 · 3 + 3."},
    ], pamats=4),

    Varianti("Pārbaudi tabulu", [
        {"jaut": "Kurš skaitlis nav reizināšanas ar 3 tabulā?",
         "zim": _TABULA, "opcijas": ["16", "18", "21"], "pareizi": 0,
         "padoms": "15, 18 - 16 izlaists."},
        {"jaut": "Anna uzrakstīja 8 · 3 = 21. Kur kļūda?",
         "opcijas": ["jābūt 24", "jābūt 18", "nav kļūdas"], "pareizi": 0,
         "padoms": "7 · 3 = 21, 8 · 3 = 24."},
    ]),

    Pasaule("Kioska cenas",
            Ievadi("", [
                {"jaut": "Saldējums maksā 3 €. Cik maksā 5 saldējumi?",
                 "atb": ["15"], "mers": "€", "padoms": "5 · 3."},
                {"jaut": "Tev ir 30 €. Cik saldējumu var nopirkt?",
                 "atb": ["10"], "padoms": "? · 3 = 30."},
            ]),
            pavediens="veikals",
            konteksts="Kioskā vasarā pārdod saldējumu pa 3 €.",
            kapec="Tabula ļauj rēķināt galvā."),

    Kopsavilkums([
        "Izveidoju reizināšanas ar 3 tabulu.",
        "Pārbaudu to ar modeli.",
        "Atrodu tabulā reizinājumus un reizinātājus.",
    ]),

    Majas([
        "Uzraksti tabulu no galvas.",
        "Pārbaudi ar ciparu summu (jābūt 3, 6 vai 9).",
        "Izkārt to blakus tabulai ar 2.",
    ]),
]
