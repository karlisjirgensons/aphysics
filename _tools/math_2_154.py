# -*- coding: utf-8 -*-
"""2. klase, 154. stunda: «Kā reizinājums palīdz dalīt?»

Dalījumu atrod, domājot par reizināšanu: 16 : 2 = ? jo 2 · 8 = 16;
35 : 5 = ? jo 5 · 7 = 35. Reizināšanas tabula ir arī dalīšanas tabula,
ja to lasa otrādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kā reizinājums palīdz dalīt?"

MERKIS = ("Šodien noteiksim dalījumu, domājot, ar cik jāreizina dalītājs "
          "(16 : 2 = ?, jo 2 · 8 = 16).")

_KOPA = restis([["·", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [2, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                [3, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
                [4, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
                [5, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]])

SATURS = [
    Sakums("Kā atrast 28 : 4, ja dalīšanas tabulas nav?",
           zimejums=_KOPA,
           paraksts="Rindā «4» atrodi 28 - augšā ir 7.",
           fakti=["Dalīšana ir reizināšana otrādi.",
                  "28 : 4 = ?, jo 4 · ? = 28.",
                  "4 · 7 = 28, tātad 28 : 4 = 7."]),

    Doma("Dalīšana caur reizināšanu",
         "Dalot pajautā: ar cik jāreizina dalītājs, lai iegūtu dalāmo?",
         soli=[
             "35 : 5 = ?",
             "Pajautā: 5 · ? = 35.",
             "Atrodi tabulā vai atceries: 5 · 7 = 35.",
             "Atbilde: 35 : 5 = 7.",
         ]),

    Ievadi("Dali", [
        {"jaut": "35 : 5 = ?", "zim": _KOPA, "atb": ["7"],
         "padoms": "5 · 7 = 35."},
        {"jaut": "24 : 3 = ?", "zim": _KOPA, "atb": ["8"],
         "padoms": "3 · 8 = 24."},
        {"jaut": "36 : 4 = ?", "atb": ["9"], "padoms": "4 · 9 = 36."},
        {"jaut": "45 : 5 = ?", "atb": ["9"], "padoms": "5 · 9 = 45."},
        {"jaut": "27 : 3 = ?", "atb": ["9"], "padoms": "3 · 9 = 27."},
        {"jaut": "32 : 4 = ?", "atb": ["8"], "padoms": "4 · 8 = 32."},
        {"jaut": "30 : 5 = ?", "atb": ["6"], "padoms": "5 · 6 = 30."},
        {"jaut": "18 : 3 = ?", "atb": ["6"], "padoms": "3 · 6 = 18."},
    ], pamats=6),

    Varianti("Kurš reizinājums palīdz?", [
        {"jaut": "40 : 5 = ?", "opcijas": ["5 · 8 = 40", "5 · 5 = 25",
                                           "4 · 10 = 40"],
         "pareizi": 0, "padoms": "Dalītājs 5."},
        {"jaut": "21 : 3 = ?", "opcijas": ["3 · 7 = 21", "3 · 3 = 9",
                                           "2 · 10 = 20"],
         "pareizi": 0, "padoms": "Dalītājs 3."},
    ]),

    Pasaule("Grāmatu plaukti",
            Ievadi("", [
                {"jaut": "Bibliotēkā 40 jaunas grāmatas liek pa 5 katrā "
                         "plauktā. Cik plauktu?", "atb": ["8"],
                 "padoms": "5 · 8 = 40."},
                {"jaut": "Ja liek pa 4, cik plauktu?", "atb": ["10"],
                 "padoms": "4 · 10 = 40."},
            ]),
            pavediens="skola",
            konteksts="Skolas bibliotēka saņēma jaunas grāmatas.",
            kapec="Reizināšanas tabula palīdz arī dalīt."),

    Kopsavilkums([
        "Atrodu dalījumu ar reizināšanu.",
        "Lasu reizināšanas tabulu otrādi.",
        "Dalu ar 2, 3, 4 un 5.",
    ]),

    Majas([
        "Izveido dalīšanas kartītes ar 3, 4, 5.",
        "Aizmugurē uzraksti palīgreizinājumu.",
        "Trenējies ar mājinieku.",
    ]),
]
