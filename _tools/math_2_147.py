# -*- coding: utf-8 -*-
"""2. klase, 147. stunda: «Kāpēc reizinājumi ar 5 ir viegli?»

Likumsakarība: reizinājums ar 5 beidzas ar 0 (pāra reizinātājam) vai ar 5
(nepāra). Un 5 · n ir puse no 10 · n - 8 · 5 = 80 : 2 = 40. Skolēns
formulē likumu pats, pēc tabulas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kāpēc reizinājumi ar 5 ir viegli?"

MERKIS = ("Šodien formulēsim likumsakarību par reizinājumu ar 5 pēdējo "
          "ciparu.")

_TABULA = restis([["1 · 5", "2 · 5", "3 · 5", "4 · 5", "5 · 5"],
                  [5, 10, 15, 20, 25],
                  ["6 · 5", "7 · 5", "8 · 5", "9 · 5", "10 · 5"],
                  [30, 35, 40, 45, 50]])

SATURS = [
    Sakums("Kāds ir katra reizinājuma ar 5 pēdējais cipars?",
           zimejums=_TABULA,
           paraksts="Tikai 5 vai 0!",
           fakti=["Nepāra · 5 - beidzas ar 5.",
                  "Pāra · 5 - beidzas ar 0.",
                  "Un 5 · n ir puse no 10 · n."]),

    Doma("Likumsakarība",
         "Reizinājums ar 5 ir puse no reizinājuma ar 10.",
         soli=[
             "8 · 10 = 80.",
             "8 · 5 ir puse: 80 : 2 = 40.",
             "Pāra skaitlis · 5 beidzas ar 0.",
             "Nepāra skaitlis · 5 beidzas ar 5.",
         ]),

    Varianti("Ar ko beigsies?", [
        {"jaut": "7 · 5", "opcijas": ["5", "0"], "jaukt": False,
         "pareizi": 0, "padoms": "7 - nepāra."},
        {"jaut": "6 · 5", "opcijas": ["5", "0"], "jaukt": False,
         "pareizi": 1, "padoms": "6 - pāra."},
        {"jaut": "9 · 5", "opcijas": ["5", "0"], "jaukt": False,
         "pareizi": 0, "padoms": "9 - nepāra."},
        {"jaut": "10 · 5", "opcijas": ["5", "0"], "jaukt": False,
         "pareizi": 1, "padoms": "10 - pāra."},
    ]),

    Ievadi("Puse no desmitkārša", [
        {"jaut": "6 · 10 = 60, tātad 6 · 5 = ?", "atb": ["30"],
         "padoms": "Puse no 60."},
        {"jaut": "8 · 5 = ?", "atb": ["40"], "padoms": "Puse no 80."},
        {"jaut": "4 · 5 = ?", "atb": ["20"], "padoms": "Puse no 40."},
        {"jaut": "7 · 5 = ?", "atb": ["35"], "padoms": "Puse no 70."},
        {"jaut": "9 · 5 = ?", "atb": ["45"], "padoms": "Puse no 90."},
        {"jaut": "? · 5 = 25", "atb": ["5"], "padoms": "Tabulā."},
    ], pamats=4),

    Pasaule("Monētas pa 5 centiem",
            Ievadi("", [
                {"jaut": "Krājkasītē 8 monētas pa 5 c. Cik centu?",
                 "atb": ["40"], "mers": "c", "padoms": "8 · 5."},
                {"jaut": "Vēl ielika 3 tādas. Cik tagad?", "atb": ["55"],
                 "mers": "c", "padoms": "11 · 5 = 40 + 15."},
            ]),
            pavediens="veikals",
            konteksts="Sīknaudu krāj krājkasītē.",
            kapec="Pa 5 c saskaita ātri."),

    Kopsavilkums([
        "Zinu, ka reizinājums ar 5 beidzas ar 0 vai 5.",
        "Aprēķinu 5 · n kā pusi no 10 · n.",
        "Paskaidroju likumsakarību.",
    ]),

    Majas([
        "Pārbaudi likumu ar 5 piemēriem.",
        "Izskaidro to mājiniekam.",
        "Aprēķini 5 · 12 ar triku (puse no 120).",
    ]),
]
