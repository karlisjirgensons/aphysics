# -*- coding: utf-8 -*-
"""9. klase, 127. stunda: «Kāpēc virkne ir funkcija?»

Virkne ir funkcija, kuras argumenti ir naturāli skaitļi: n → a_n. Tāpēc
a_n = 2n + 1 un y = 2x + 1 ir «radinieki» - tikai virknei grafiks ir
atsevišķi punkti, nevis nepārtraukta līnija.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, plakne)

TEMA = "Kāpēc virkne ir funkcija?"

MERKIS = "Skaidrosim virkni kā funkciju ar naturāliem argumentiem."

_PUNKTI = [(n, 2 * n + 1, "") for n in range(1, 6)]

SATURS = [
    Sakums("a_n = 2n + 1 un y = 2x + 1 - kas kopīgs?",
           zimejums=plakne(grafiki=[(2, 1, "y = 2x + 1")], punkti=_PUNKTI,
                           no_x=0, lidz_x=6, no_y=0, lidz_y=12, solis_y=2),
           paraksts="Virknes punkti guļ uz funkcijas taisnes.",
           fakti=["Virkne - funkcija ar argumentu n ∈ ℕ.",
                  "Katram n - tieši viens a_n.",
                  "Grafiks - atsevišķi punkti, ne līnija."]),

    Doma("Virkne kā funkcija",
         "Skaitļu virkne ir funkcija, kuras definīcijas apgabals ir naturālie "
         "skaitļi: katram n atbilst loceklis a_n.",
         soli=[
             "Arguments - numurs n (1, 2, 3, ...).",
             "Vērtība - loceklis a_n.",
             "Starp n = 2 un n = 3 nekā nav - nav «a_{2,5}».",
             "Funkcijas īpašības (augoša, dilstoša) der arī virknei.",
         ]),

    Slidnis("Augoša, dilstoša, svārstīga", [
        {"v": "Augoša", "teksts": "a_n = 2n + 1: katrs nākamais lielāks",
         "zim": plakne(punkti=_PUNKTI, no_x=0, lidz_x=6, no_y=0, lidz_y=12,
                       solis_y=2)},
        {"v": "Dilstoša", "teksts": "a_n = 10 − 2n: katrs nākamais mazāks",
         "zim": plakne(punkti=[(n, 10 - 2 * n, "") for n in range(1, 6)],
                       no_x=0, lidz_x=6, no_y=-2, lidz_y=10, solis_y=2)},
        {"v": "Svārstīga", "teksts": "a_n = (−1)^n: −1, 1, −1, 1, ...",
         "zim": plakne(punkti=[(n, (-1) ** n, "") for n in range(1, 7)],
                       no_x=0, lidz_x=7, no_y=-2, lidz_y=2)},
    ]),

    Varianti("Augoša vai dilstoša?", [
        {"jaut": "a_n = 5n − 3",
         "opcijas": ["Augoša", "Dilstoša", "Svārstīga", "Konstanta"],
         "pareizi": 0, "padoms": "+5 katrā solī."},
        {"jaut": "a_n = 20 − n",
         "opcijas": ["Dilstoša", "Augoša", "Svārstīga", "Konstanta"],
         "pareizi": 0, "padoms": "−1 katrā solī."},
        {"jaut": "a_n = 7",
         "opcijas": ["Konstanta", "Augoša", "Dilstoša", "Nav virkne"],
         "pareizi": 0, "padoms": "Visi 7."},
        {"jaut": "Vai a_n = 3n var būt 10?",
         "opcijas": ["Nē - n būtu {10|3}, nav naturāls", "Jā",
                     "Jā, n = 3", "Jā, n = 4"],
         "pareizi": 0, "padoms": "n ∈ ℕ."},
    ]),

    Ievadi("Funkcija un virkne", [
        {"jaut": "f(x) = x^2 − 1. Virknei a_n = f(n): a_3 = ?", "atb": ["8"],
         "padoms": "9 − 1."},
        {"jaut": "Tai pašai: a_1 = ?", "atb": ["0"], "padoms": "1 − 1."},
        {"jaut": "a_n = 10 − 2n. Kurš loceklis pirmais negatīvs? n = ?",
         "atb": ["6"], "padoms": "10 − 12 = −2."},
    ]),

    Pasaule("Taksometra tarifs pa kilometriem",
            Ievadi("", [
                {"jaut": "Taksometrs skaita veselus km: cena par n km "
                         "a_n = 2 + 0,9n €. a_5 = ?", "atb": ["6,5"],
                 "padoms": "2 + 4,5."},
                {"jaut": "Par 4,3 km skaitītājs rēķina 5 km. Cik €?",
                 "atb": ["6,5"], "padoms": "Nav «a_{4,3}» - noapaļo uz augšu."},
            ]),
            pavediens="celojums",
            konteksts="Daži skaitītāji rēķina pa veseliem kilometriem - tā ir "
                      "virkne, nevis nepārtraukta funkcija.",
            kapec="Virknes arguments ir tikai vesels skaitlis."),

    Kopsavilkums([
        "Skaidroju virkni kā funkciju ar n ∈ ℕ.",
        "Attēloju virkni ar punktiem.",
        "Nosaku, vai virkne augoša vai dilstoša.",
    ]),

    Majas([
        "Uzzīmē virknes a_n = n^2 pirmos 5 punktus.",
        "Salīdzini ar y = x^2 grafiku.",
        "Atrodi dzīvē lielumu, kas mainās tikai «pa soļiem».",
    ]),
]
