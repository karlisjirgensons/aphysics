# -*- coding: utf-8 -*-
"""2. klase, 143. stunda: «Cik veikli zini reizinājumus ar 3?»

Mikrotemata noslēgums: treniņš ar kartītēm un pašnovērtējums - kurus
reizinājumus zinu no galvas, kurus vēl jātrenē. Jaukti ar 2 un 3, lai
skolēns nesajauc tabulas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Cik veikli zini reizinājumus ar 3?"

MERKIS = ("Šodien trenēsimies ar kartītēm un atzīmēsim, kurus reizinājumus "
          "ar 3 jau zinām no galvas.")

SATURS = [
    Sakums("Vai vari atbildēt ātrāk, nekā draugs paskaita līdz 3?",
           zimejums=restis([["7 · 3", "→", "?"], ["8 · 3", "→", "?"]]),
           fakti=["Kas zina no galvas, atbild uzreiz.",
                  "Kas nezina - skaita pa 3.",
                  "Šodien noskaidrosim, kuri tev jau ir galvā."]),

    Doma("Pašnovērtējums",
         "Atzīmē, ko zini uzreiz, un trenē pārējo.",
         soli=[
             "Atbildi uz kartīti.",
             "Ja atbildēji uzreiz - «zinu».",
             "Ja skaitīji - «trenēt».",
             "Trenē tikai «trenēt» kaudzi.",
         ]),

    Ievadi("Ātrā kārta", [
        {"jaut": "7 · 3 = ?", "atb": ["21"], "padoms": "6 · 3 + 3."},
        {"jaut": "4 · 3 = ?", "atb": ["12"], "padoms": "3 + 3 + 3 + 3."},
        {"jaut": "9 · 3 = ?", "atb": ["27"], "padoms": "30 − 3."},
        {"jaut": "6 · 2 = ?", "atb": ["12"], "padoms": "Tabula ar 2!"},
        {"jaut": "8 · 3 = ?", "atb": ["24"], "padoms": "7 · 3 + 3."},
        {"jaut": "5 · 3 = ?", "atb": ["15"], "padoms": "Puse no 30."},
        {"jaut": "8 · 2 = ?", "atb": ["16"], "padoms": "Dubulti."},
        {"jaut": "6 · 3 = ?", "atb": ["18"], "padoms": "5 · 3 + 3."},
    ], pamats=6),

    Varianti("Nesajauc!", [
        {"jaut": "7 · 2 vai 7 · 3 - kurš ir 21?",
         "opcijas": ["7 · 3", "7 · 2"], "jaukt": False, "pareizi": 0,
         "padoms": "7 · 2 = 14."},
        {"jaut": "Kurš reizinājums ir lielāks: 9 · 2 vai 5 · 3?",
         "opcijas": ["9 · 2 = 18", "5 · 3 = 15"], "jaukt": False,
         "pareizi": 0, "padoms": "18 > 15."},
    ]),

    Pasaule("Kauliņu spēle",
            Ievadi("", [
                {"jaut": "Spēlē katrs punkts dod 3 soļus. Uzmeti 6. Cik "
                         "soļu?", "atb": ["18"], "padoms": "6 · 3."},
                {"jaut": "Draugs uzmeta 4. Par cik soļiem tu tiec tālāk?",
                 "atb": ["6"], "padoms": "18 − 12."},
            ]),
            pavediens="speles",
            konteksts="Galda spēlē kauliņa punktus reizina ar 3.",
            kapec="Kas zina reizinājumus, spēlē ātrāk."),

    Kopsavilkums([
        "Trenēju reizinājumus ar 3.",
        "Zinu, kurus jau zinu no galvas.",
        "Nesajaucu reizinājumus ar 2 un 3.",
    ]),

    Majas([
        "Trenējies ar kartītēm 5 minūtes.",
        "Pieraksti, kuri reizinājumi vēl grūti.",
        "Rīt trenē tikai tos.",
    ]),
]
