# -*- coding: utf-8 -*-
"""2. klase, 125. stunda: «Kā uzbūvēt reizināšanas ar 2 tabulu?»

Reizinājumu ar 2 tabulu būvē pats: katrs nākamais ir par 2 lielāks nekā
iepriekšējais. Tabulā redz rakstu - rezultāti ir dubulti un beidzas ar
0, 2, 4, 6, 8.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kā uzbūvēt reizināšanas ar 2 tabulu?"

MERKIS = ("Šodien izveidosim reizinājumu ar 2 tabulu un izmantosim to "
          "aprēķinos.")

_TABULA = restis([["1 · 2", "2 · 2", "3 · 2", "4 · 2", "5 · 2"],
                  [2, 4, 6, 8, 10],
                  ["6 · 2", "7 · 2", "8 · 2", "9 · 2", "10 · 2"],
                  [12, 14, 16, 18, 20]])

SATURS = [
    Sakums("Kā uzbūvēt tabulu, lai nekas nav jāatceras?",
           zimejums=_TABULA,
           paraksts="Katrs nākamais - par 2 vairāk.",
           fakti=["1 · 2 = 2, tad pieskaiti 2.",
                  "Rezultāti beidzas ar 0, 2, 4, 6, 8.",
                  "Tie ir visi dubulti līdz 20."]),

    Doma("Tabulas būvēšana",
         "Katrs nākamais reizinājums ir par 2 lielāks nekā iepriekšējais.",
         soli=[
             "Sāc: 1 · 2 = 2.",
             "Nākamais: 2 · 2 = 2 + 2 = 4.",
             "Tad 3 · 2 = 4 + 2 = 6 ... līdz 10 · 2 = 20.",
             "Pārbaudi: 5 · 2 = 10 - puse ceļa.",
         ]),

    Slidnis("Tabula aug", [
        {"v": "1 · 2 = 2", "teksts": "Sākums.",
         "zim": restis([["1 · 2"], [2]])},
        {"v": "2 · 2 = 4", "teksts": "2 + 2.",
         "zim": restis([["1 · 2", "2 · 2"], [2, 4]])},
        {"v": "3 · 2 = 6", "teksts": "4 + 2.",
         "zim": restis([["1 · 2", "2 · 2", "3 · 2"], [2, 4, 6]])},
        {"v": "10 · 2 = 20", "teksts": "Visa tabula.", "zim": _TABULA},
    ]),

    Ievadi("Izmanto tabulu", [
        {"jaut": "7 · 2 = ?", "zim": _TABULA, "atb": ["14"],
         "padoms": "Atrodi tabulā."},
        {"jaut": "9 · 2 = ?", "atb": ["18"], "padoms": "10 · 2 − 2."},
        {"jaut": "6 · 2 = ?", "atb": ["12"], "padoms": "5 · 2 + 2."},
        {"jaut": "? · 2 = 16", "atb": ["8"], "padoms": "Tabulā 16."},
        {"jaut": "? · 2 = 10", "atb": ["5"], "padoms": "Tabulā 10."},
        {"jaut": "3 · 2 + 4 · 2 = ?", "atb": ["14"], "padoms": "6 + 8."},
    ], pamats=4),

    Varianti("Vai tabulā?", [
        {"jaut": "Vai 13 ir reizināšanas ar 2 tabulā?",
         "opcijas": ["Nē - beidzas ar 3", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "Tikai 0, 2, 4, 6, 8 beigās."},
        {"jaut": "Kurš skaitlis ir tabulā?", "opcijas": ["18", "17", "19"],
         "pareizi": 0, "padoms": "9 · 2."},
    ]),

    Pasaule("Biļetes zoodārzā",
            Ievadi("", [
                {"jaut": "Bērna biļete 2 €. Cik maksā 8 biļetes? 8 · 2 = ?",
                 "atb": ["16"], "mers": "€", "padoms": "Tabulā."},
                {"jaut": "Klasei ir 20 €. Cik bērnu biļešu var nopirkt?",
                 "atb": ["10"], "padoms": "? · 2 = 20."},
            ]),
            pavediens="celojums",
            konteksts="Klase brauc uz zoodārzu.",
            kapec="Tabula ļauj rēķināt biļetes galvā."),

    Kopsavilkums([
        "Uzbūvēju reizināšanas ar 2 tabulu.",
        "Zinu, ka katrs nākamais ir par 2 lielāks.",
        "Izmantoju tabulu aprēķinos.",
    ]),

    Majas([
        "Uzraksti tabulu no galvas uz lapiņas.",
        "Pārbaudi ar kalkulatoru vai mājinieku.",
        "Izkārt to pie sava galda.",
    ]),
]
