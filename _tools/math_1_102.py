# -*- coding: utf-8 -*-
"""1. klase, 102. stunda: «Kā pastāstīt savu domu gaitu?»

Risinājumu stāsta pa soļiem - «vispirms, tad, beigās» - un pamato, kā
zina, ka rezultāts pareizs (pārbaude ar pretējo darbību).
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti)

TEMA = "Kā pastāstīt savu domu gaitu?"

MERKIS = ("Šodien izskaidrosim risinājumu pa soļiem un pamatosim, kāpēc "
          "rezultāts ir pareizs.")

SATURS = [
    Sakums("Kā pastāstīt, kā izrēķināji 14 − 6?",
           fakti=["Vispirms: 14 − 4 = 10.",
                  "Tad: 10 − 2 = 8.",
                  "Pārbaude: 8 + 6 = 14 - pareizi."]),

    Paraugs("Stāsts par risinājumu",
            uzd="Izrēķini 14 − 6 un izstāsti, kā.",
            soli=[
                ("Vispirms 14 − 4 = 10", "Atņēmu vienus līdz desmitam."),
                ("Tad 10 − 2 = 8", "Atlikušos 2 no desmita."),
                ("Pārbaude: 8 + 6 = 14", "Saskaitot sanāk sākums."),
            ],
            atbilde="8"),

    Doma("Stāsts pa soļiem",
         "Labs stāsts pasaka, ko darīji, un kā zini, ka tas ir pareizi.",
         soli=[
             "«Vispirms es...»",
             "«Tad es...»",
             "«Es zinu, ka pareizi, jo...»",
         ]),

    Varianti("Kurš stāsts labāks?", [
        {"jaut": "Kā izskaidrot 7 + 8 = 15?",
         "opcijas": ["7 + 3 = 10, vēl 5 - 15",
                     "Es vienkārši zinu", "Tā teica mamma"],
         "pareizi": 0, "padoms": "Kurš parāda soļus?"},
        {"jaut": "Kā pamatot, ka 12 − 5 = 7 ir pareizi?",
         "opcijas": ["7 + 5 = 12", "7 ir mazāks nekā 12", "tā izskatās"],
         "pareizi": 0, "padoms": "Pretējā darbība."},
        {"jaut": "Kurš vārds palīdz stāstīt pēc kārtas?",
         "opcijas": ["tad", "varbūt", "nezinu"], "pareizi": 0,
         "padoms": "Vispirms, tad, beigās."},
    ]),

    Petijums("Skolotājs pārī", [
        "Izrēķini 13 − 7.",
        "Pastāsti pārim soļus: vispirms, tad, pārbaude.",
        "Pāris saka, kas bija saprotams un kas ne.",
        "Mainieties lomām ar 9 + 4.",
    ], vajag="lapiņa, zīmulis"),

    Pasaule("Palīdzi mazajam brālim",
            Varianti("", [
                {"jaut": "Brālis nesaprot 6 + 5. Ko teikt vispirms?",
                 "opcijas": ["6 + 4 ir 10", "atbilde ir 11",
                             "skaiti pats"], "pareizi": 0,
                 "padoms": "Sāc ar pirmo soli."},
            ]),
            pavediens="maja",
            konteksts="Kas prot izskaidrot, tas saprot pats.",
            kapec="Stāstot tu pārbaudi arī savu domu."),

    Kopsavilkums([
        "Stāstu risinājumu pa soļiem.",
        "Pamatoju ar pārbaudi.",
        "Klausos un saprotu drauga stāstu.",
    ]),

    Majas([
        "Izskaidro mājiniekam, kā rēķināt 8 + 6.",
        "Palūdz, lai viņš pastāsta atpakaļ.",
        "Vai viņš saprata?",
    ]),
]
