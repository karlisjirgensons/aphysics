# -*- coding: utf-8 -*-
"""4. klase, 125. stunda: «Ko darīt, ja modeli izveidot nevar?»

2400 € nevar sakraut monētās uz galda - jāspriež. {1|6} no 2400 € =
2400 : 6. Pieraksts atbilst domāšanai: «viena sestdaļa ir 2400 dalīts ar 6».
Skolēns pieraksta risinājumu, lai to varētu izlasīt arī cits.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Ko darīt, ja modeli izveidot nevar?"

MERKIS = ("Aprēķināsim daļu no lielas summas, spriežot un pierakstot "
          "risinājumu.")

SATURS = [
    Sakums("Kā sadalīt 2400 € sešiem?",
           zimejums=kolonnas([("viss", 2400), ("1/6", 400)], " €"),
           paraksts="{1|6} no 2400 € = 2400 : 6 = 400 €.",
           fakti=["Tik daudz monētu uz galda nesalikt.",
                  "Bet dalīt var galvā vai stūrītī."]),

    Doma("Pieraksti tā, kā domā",
         "Lielām summām modeli aizstāj pieraksts: «{1|n} no a ir a : n».",
         soli=[
             "Uzraksti: {1|6} no 2400 € = 2400 : 6.",
             "Izrēķini: 24 simti : 6 = 4 simti.",
             "Atbilde: 400 €.",
             "Pārbaude: 400 · 6 = 2400.",
         ],
         pieze="Atbildi raksti ar mērvienību - «400», bez €, neko nepasaka."),

    Paraugs("{1|8} no 5600 €",
            uzd="Ģimenes gada atvaļinājuma budžets 5600 €, {1|8} - "
                "ēdienam. Cik €?",
            soli=[
                ("{1|8} no 5600 € = 5600 : 8", None),
                ("56 simti : 8 = 7 simti", None),
                ("= 700 €", None),
            ],
            atbilde="700 €"),

    Ievadi("Lielas summas", [
        {"jaut": "{1|6} no 2400 € = ?", "atb": ["400"], "padoms": "24 : 6."},
        {"jaut": "{1|5} no 3500 € = ?", "atb": ["700"], "padoms": "35 : 5."},
        {"jaut": "{1|9} no 8100 € = ?", "atb": ["900"], "padoms": "81 : 9."},
        {"jaut": "{1|4} no 6000 € = ?", "atb": ["1500"],
         "padoms": "6000 : 4."},
        {"jaut": "{1|12} no 4800 € = ?", "atb": ["400"], "padoms": "48 : 12."},
        {"jaut": "{1|25} no 5000 € = ?", "atb": ["200"],
         "padoms": "5000 : 25."},
    ], pamats=4),

    Varianti("Kurš pieraksts pareizs?", [
        {"jaut": "{1|3} no 900 €",
         "opcijas": ["900 : 3 = 300 €", "900 · 3 = 2700 €",
                     "900 − 3 = 897 €"], "pareizi": 0,
         "padoms": "Dalīšana."},
        {"jaut": "Toms: {1|4} no 2000 € = 8000 €. Kļūda?",
         "opcijas": ["reizināja, nevis dalīja", "viss pareizi",
                     "atņēma"], "pareizi": 0,
         "padoms": "Daļa nevar būt lielāka par veselo."},
        {"jaut": "Vai daļa {1|n} var būt lielāka par veselo?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "Tā ir viena no n daļām."},
    ]),

    Pasaule("Skolas budžets",
            Ievadi("", [
                {"jaut": "Skolas bibliotēkai 4800 € gadā, {1|4} - "
                         "enciklopēdijām. Cik €?",
                 "atb": ["1200"], "padoms": "4800 : 4."},
                {"jaut": "Sporta zālei 3600 €, {1|9} - bumbām. Cik €?",
                 "atb": ["400"], "padoms": "3600 : 9."},
                {"jaut": "Ekskursijām 7200 €, {1|8} - 4. klasēm. Cik €?",
                 "atb": ["900"], "padoms": "7200 : 8."},
                {"jaut": "Datoriem 9000 €, {1|3} - planšetēm. Cik €?",
                 "atb": ["3000"], "padoms": "9000 : 3."},
            ]),
            pavediens="skola",
            konteksts="Skolas direktors sadala gada budžetu daļās "
                      "dažādām vajadzībām.",
            kapec="Lielas summas dala ar spriedumu, ne ar monētām."),

    Kopsavilkums([
        "Aprēķinu daļu no lielas summas bez modeļa.",
        "Pierakstu risinājumu: «{1|n} no a = a : n».",
        "Rakstu atbildi ar mērvienību.",
    ]),

    Majas([
        "Izdomā lielu summu un aprēķini tās {1|4}, {1|5} un {1|10}.",
        "Pajautā vecākiem, kāda daļa algas aiziet īrei (aptuveni).",
        "Pārbaudi ar kalkulatoru: {1|16} no 9600 €.",
    ]),
]
