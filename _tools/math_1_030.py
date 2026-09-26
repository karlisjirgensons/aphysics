# -*- coding: utf-8 -*-
"""1. klase, 30. stunda: «Vai svarīgi, kurš skaitlis ir pirmais?»

Saskaitot saskaitāmos var mainīt vietām: 2 + 5 = 5 + 2. To redz, pagriežot
ripiņu rindu otrādi. Tāpēc ērtāk sākt ar lielāko un pieskaitīt mazāko.
Atņemšanā tā nedrīkst.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, bildes)

TEMA = "Vai svarīgi, kurš skaitlis ir pirmais?"

MERKIS = ("Šodien pārliecināsimies, ka saskaitāmos var mainīt vietām, un "
          "izmantosim to.")


def _rinda(a, b, otradi=False):
    r = ["ripina"] * a + ["ripina*"] * b
    return bildes([r[::-1] if otradi else r])


SATURS = [
    Sakums("2 + 5 un 5 + 2 - vai tas pats?",
           zimejums=_rinda(2, 5),
           paraksts="Paskaties uz rindu no otras puses: 5 + 2.",
           fakti=["Ripiņu skaits nemainās, ja rindu pagriež.",
                  "2 + 5 = 5 + 2 = 7.",
                  "Ērtāk sākt ar lielāko skaitli."]),

    Slidnis("Pagriez rindu", [
        {"v": "2 + 5", "teksts": "No kreisās: 2 violetas un 5 oranžas",
         "zim": _rinda(2, 5)},
        {"v": "5 + 2", "teksts": "No labās: 5 oranžas un 2 violetas",
         "zim": _rinda(2, 5, True)},
    ]),

    Doma("Maiņa vietām",
         "Saskaitāmos var mainīt vietām - summa nemainās.",
         soli=[
             "Atrodi lielāko skaitli.",
             "Sāc ar to.",
             "Pieskaiti mazāko, skaitot uz priekšu.",
         ],
         pieze="Atņemšanā tā nevar: 5 − 2 nav tas pats, kas 2 − 5."),

    Ievadi("Sāc ar lielāko", [
        {"jaut": "1 + 8 = ?", "atb": ["9"], "padoms": "8 + 1."},
        {"jaut": "2 + 7 = ?", "atb": ["9"], "padoms": "7 un vēl 2."},
        {"jaut": "3 + 6 = ?", "atb": ["9"], "padoms": "6 un vēl 3."},
        {"jaut": "1 + 6 = ?", "atb": ["7"], "padoms": "6 un vēl 1."},
        {"jaut": "2 + 8 = ?", "atb": ["10"], "padoms": "8 un vēl 2."},
        {"jaut": "3 + 5 = ?", "atb": ["8"], "padoms": "5 un vēl 3."},
    ], pamats=4),

    Varianti("Vai vienāds?", [
        {"jaut": "4 + 3 un 3 + 4", "opcijas": ["vienādi", "dažādi"],
         "jaukt": False, "pareizi": 0, "padoms": "Abi ir 7."},
        {"jaut": "6 − 2 un 2 − 6", "opcijas": ["vienādi", "dažādi"],
         "jaukt": False, "pareizi": 1,
         "padoms": "No 2 nevar atņemt 6."},
        {"jaut": "1 + 9 un 9 + 1", "opcijas": ["vienādi", "dažādi"],
         "jaukt": False, "pareizi": 0, "padoms": "Abi ir 10."},
    ]),

    Pasaule("Ogas divos traukos",
            Ievadi("", [
                {"jaut": "Anna salasīja 2 zemenes, Jānis - 7. Cik kopā?",
                 "atb": ["9"], "padoms": "7 + 2."},
                {"jaut": "Vai būtu cits skaitlis, ja sāktu ar Annas ogām?",
                 "atb": ["9"], "padoms": "2 + 7 arī ir 9."},
            ]),
            pavediens="daba",
            konteksts="Bērni salasīja zemenes un sabēra kopā.",
            kapec="Kopā ir tikpat, lai kuru trauku sabērtu pirmo."),

    Kopsavilkums([
        "Zinu, ka 2 + 5 = 5 + 2.",
        "Saskaitot sāku ar lielāko skaitli.",
        "Zinu, ka atņemšanā vietas mainīt nedrīkst.",
    ]),

    Majas([
        "Noliec rindā 3 karotes un 6 dakšas. Saskaiti no abām pusēm.",
        "Izrēķini 1 + 7 un 7 + 1.",
        "Kurš ir vieglāk? Kāpēc?",
    ]),
]
