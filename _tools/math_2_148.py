# -*- coding: utf-8 -*-
"""2. klase, 148. stunda: «Kā apvienot visas tabulas?»

Reizinājumi ar 2, 3, 4 un 5 vienā pārskatāmā tabulā: rinda - reizinātājs,
kolonna - otrs reizinātājs, krustpunktā - reizinājums. Tabulā redz arī
sakarības: 4 kolonna ir divreiz 2 kolonna.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kā apvienot visas tabulas?"

MERKIS = ("Šodien sakārtosim reizinājumus ar 2, 3, 4 un 5 vienā pārskatāmā "
          "tabulā.")

_KOPA = restis([["·", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [2, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                [3, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
                [4, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
                [5, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]])

SATURS = [
    Sakums("Kā vienā lapā ielikt 40 reizinājumus?",
           zimejums=_KOPA,
           paraksts="Rinda un kolonna - krustpunktā reizinājums.",
           fakti=["Kreisajā kolonnā: 2, 3, 4, 5.",
                  "Augšējā rindā: 1 līdz 10.",
                  "Krustpunktā: to reizinājums."]),

    Doma("Kā lasīt tabulu",
         "Atrodi rindu vienam reizinātājam un kolonnu otram.",
         soli=[
             "4 · 7: atrodi rindu «4».",
             "Ej pa labi līdz kolonnai «7».",
             "Krustpunktā ir 28.",
             "Dalīšanai: rindā «4» atrodi 28 - augšā ir 7.",
         ]),

    Ievadi("Lasi tabulu", [
        {"jaut": "3 · 8 = ?", "zim": _KOPA, "atb": ["24"],
         "padoms": "Rinda 3, kolonna 8."},
        {"jaut": "5 · 6 = ?", "zim": _KOPA, "atb": ["30"],
         "padoms": "Rinda 5, kolonna 6."},
        {"jaut": "4 · 9 = ?", "zim": _KOPA, "atb": ["36"],
         "padoms": "Rinda 4, kolonna 9."},
        {"jaut": "Rindā «4» atrodi 32. Kāds skaitlis augšā?", "zim": _KOPA,
         "atb": ["8"], "padoms": "32 : 4 = 8."},
    ]),

    Varianti("Sakarības", [
        {"jaut": "Salīdzini rindas «2» un «4». Kas redzams?", "zim": _KOPA,
         "opcijas": ["rindā 4 viss divreiz lielāks",
                     "rindā 4 viss par 2 lielāks", "tās vienādas"],
         "pareizi": 0, "padoms": "4 = 2 + 2."},
        {"jaut": "Kurš skaitlis tabulā ir 3 reizes?", "zim": _KOPA,
         "opcijas": ["12", "14", "25"], "pareizi": 0,
         "padoms": "2 · 6, 3 · 4, 4 · 3."},
        {"jaut": "Kurā rindā visi skaitļi beidzas ar 0 vai 5?", "zim": _KOPA,
         "opcijas": ["5", "4", "3"], "pareizi": 0, "padoms": "Pa 5."},
    ]),

    Pasaule("Veikala cenu tabula",
            Ievadi("", [
                {"jaut": "Kafejnīcā kēksiņš maksā 3 €, pīrāgs 4 €. Cik "
                         "maksā 6 kēksiņi?", "zim": _KOPA, "atb": ["18"],
                 "mers": "€", "padoms": "3 · 6."},
                {"jaut": "Cik maksā 6 pīrāgi?", "zim": _KOPA, "atb": ["24"],
                 "mers": "€", "padoms": "4 · 6."},
            ]),
            pavediens="veikals",
            konteksts="Pārdevēji lieto cenu tabulas, lai rēķinātu ātri.",
            kapec="Viena tabula - daudz atbilžu."),

    Kopsavilkums([
        "Sakārtoju reizinājumus ar 2, 3, 4, 5 vienā tabulā.",
        "Atrodu reizinājumu rindas un kolonnas krustpunktā.",
        "Redzu sakarības starp rindām.",
    ]),

    Majas([
        "Pārraksti apvienoto tabulu uz lielas lapas.",
        "Iekrāso vienādos skaitļus ar vienu krāsu.",
        "Kurus skaitļus atradi vairākās vietās?",
    ]),
]
