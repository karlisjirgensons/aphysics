# -*- coding: utf-8 -*-
"""2. klase, 26. stunda: «Cik veikli rēķini 20 apjomā?»

Atkārtojums pēc vasaras: saskaitīšana un atņemšana 20 apjomā. Galvenais
paņēmiens ir «caur 10» - 8 + 5 = 8 + 2 + 3, un to redz divos desmitnieka
rāmjos: vispirms piepilda pirmo rāmi, tad liek otrā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, ramis)

TEMA = "Cik veikli rēķini 20 apjomā?"

MERKIS = ("Šodien atkārtosim saskaitīšanu un atņemšanu 20 apjomā un "
          "izskaidrosim, kā rēķinām caur 10.")

SATURS = [
    Sakums("Kā izrēķināt 8 + 5, neskaitot uz pirkstiem?",
           zimejums=ramis(13, ramji=2, otra=5),
           paraksts="Vispirms piepildi desmitu, tad pieliec atlikumu.",
           fakti=["8 + 2 = 10, vēl paliek 3.",
                  "10 + 3 = 13.",
                  "Caur 10 ir ātrāk nekā skaitīt pa vienam."]),

    Doma("Caur desmitu",
         "Saskaitot vispirms papildina līdz 10, atņemot - atņem līdz 10.",
         soli=[
             "8 + 5: cik pietrūkst līdz 10? - 2.",
             "5 sadali: 2 un 3.",
             "8 + 2 = 10, 10 + 3 = 13.",
             "Atņemot: 13 − 5 = 13 − 3 − 2 = 10 − 2 = 8.",
         ]),

    Slidnis("8 + 5 rāmjos", [
        {"v": "8", "teksts": "Pirmajā rāmī 8.", "zim": ramis(8, ramji=2)},
        {"v": "8 + 2 = 10", "teksts": "Pirmais rāmis pilns.",
         "zim": ramis(10, ramji=2, otra=2)},
        {"v": "10 + 3 = 13", "teksts": "Otrajā rāmī vēl 3.",
         "zim": ramis(13, ramji=2, otra=5)},
    ]),

    Paraugs("Cik ir 14 − 6?",
            uzd="Atņem caur 10.",
            soli=[("14 − 4 = 10", "Vispirms atņem līdz 10."),
                  ("10 − 2 = 8", "Atlikušie 2 no 6.")],
            atbilde="8"),

    Ievadi("Rēķini", [
        {"jaut": "9 + 4 = ?", "atb": ["13"], "padoms": "9 + 1 + 3."},
        {"jaut": "7 + 6 = ?", "atb": ["13"], "padoms": "7 + 3 + 3."},
        {"jaut": "15 − 7 = ?", "atb": ["8"], "padoms": "15 − 5 − 2."},
        {"jaut": "12 − 5 = ?", "atb": ["7"], "padoms": "12 − 2 − 3."},
        {"jaut": "8 + 8 = ?", "atb": ["16"], "padoms": "8 + 2 + 6."},
        {"jaut": "17 − 9 = ?", "atb": ["8"], "padoms": "17 − 7 − 2."},
        {"jaut": "6 + 9 = ?", "atb": ["15"], "padoms": "9 + 1 + 5."},
        {"jaut": "11 − 4 = ?", "atb": ["7"], "padoms": "11 − 1 − 3."},
    ], pamats=6),

    Pasaule("Cik uzlīmju albumā?",
            Ievadi("", [
                {"jaut": "Albumā bija 9 uzlīmes, draugs uzdāvināja 7. Cik "
                         "tagad?", "atb": ["16"], "padoms": "9 + 1 + 6."},
                {"jaut": "Lapā ir vieta 20 uzlīmēm. Cik vēl pietrūkst?",
                 "atb": ["4"], "padoms": "20 − 16."},
            ]),
            pavediens="speles",
            konteksts="Futbola uzlīmju albumā katrā lapā ir 20 vietu.",
            kapec="Rēķinot caur 10, atbildi atrod vienā mirklī."),

    Kopsavilkums([
        "Saskaitu 20 apjomā caur 10.",
        "Atņemu 20 apjomā caur 10.",
        "Izskaidroju savu paņēmienu.",
    ]),

    Majas([
        "Ar mājinieku spēlē: viens saka skaitli līdz 10, otrs saka, cik "
        "pietrūkst līdz 10.",
        "Izrēķini: 7 + 8, 6 + 7, 16 − 8, 13 − 6.",
        "Paskaidro, kā rēķināji.",
    ]),
]
