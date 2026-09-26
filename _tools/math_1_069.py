# -*- coding: utf-8 -*-
"""1. klase, 69. stunda: «Kā skaitīt pa 2, 5 un 10?»

Skaitīšana lēcieniem: pa 2 (2, 4, 6...), pa 5 (5, 10, 15...), pa 10
(10, 20, 30...). Simta kvadrātā pa 10 ir viena kolonna, pa 5 - divas.
Tā skaita ātrāk nekā pa vienam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, simta_kvadrats)

TEMA = "Kā skaitīt pa 2, 5 un 10?"

MERKIS = ("Šodien skaitīsim uz priekšu un atpakaļ pa 2, pa 5 un pa 10.")

SATURS = [
    Sakums("Kā ātri saskaitīt zeķes? Pa pāriem!",
           zimejums=simta_kvadrats(1, 30, izcelt=list(range(2, 31, 2))),
           paraksts="Pa 2: 2, 4, 6, 8...",
           fakti=["Pa 2 - katrs otrais skaitlis.",
                  "Pa 5 - skaitļi, kas beidzas ar 5 vai 0.",
                  "Pa 10 - skaitļi, kas beidzas ar 0."]),

    Slidnis("Raksti simta kvadrātā", [
        {"v": "pa 2", "teksts": "2, 4, 6 ... - katrs otrais",
         "zim": simta_kvadrats(1, 50, izcelt=list(range(2, 51, 2)))},
        {"v": "pa 5", "teksts": "5, 10, 15 ... - divas kolonnas",
         "zim": simta_kvadrats(1, 50, izcelt=list(range(5, 51, 5)))},
        {"v": "pa 10", "teksts": "10, 20, 30 ... - viena kolonna",
         "zim": simta_kvadrats(izcelt=list(range(10, 101, 10)))},
    ]),

    Doma("Lēcieni",
         "Katrs lēciens ir vienāds: +2, +5 vai +10.",
         soli=[
             "Sāc no dotā skaitļa.",
             "Pieskaiti lēcienu atkal un atkal.",
             "Atpakaļ - atņem to pašu lēcienu.",
         ]),

    Ievadi("Turpini", [
        {"jaut": "2, 4, 6, 8, ...", "atb": ["10"], "padoms": "+2."},
        {"jaut": "5, 10, 15, 20, ...", "atb": ["25"], "padoms": "+5."},
        {"jaut": "10, 20, 30, 40, ...", "atb": ["50"], "padoms": "+10."},
        {"jaut": "Atpakaļ pa 10: 90, 80, 70, ...", "atb": ["60"],
         "padoms": "−10."},
        {"jaut": "Atpakaļ pa 5: 50, 45, 40, ...", "atb": ["35"],
         "padoms": "−5."},
        {"jaut": "Pa 2 no 11: 11, 13, 15, ...", "atb": ["17"],
         "padoms": "+2."},
    ], pamats=4),

    Pasaule("Monētas pa 5 centiem",
            Ievadi("", [
                {"jaut": "Tev ir 6 monētas pa 5 c. Cik centu? (Skaiti pa 5)",
                 "atb": ["30"], "padoms": "5, 10, 15, 20, 25, 30."},
                {"jaut": "Cik zeķu ir 7 pāros?", "atb": ["14"],
                 "padoms": "Pa 2."},
            ]),
            pavediens="veikals",
            konteksts="Daudz vienādu monētu ātrāk saskaita lēcieniem.",
            kapec="Lēcieni ir ātrāki nekā skaitīt pa vienam."),

    Kopsavilkums([
        "Skaitu pa 2, pa 5 un pa 10.",
        "Skaitu arī atpakaļ.",
        "Redzu rakstus simta kvadrātā.",
    ]),

    Majas([
        "Saskaiti apavus mājās pa pāriem.",
        "Saskaiti pirkstus ģimenē pa 5.",
        "Skaiti skaļi pa 10 līdz 100, lecot vienu lēcienu katram.",
    ]),
]
