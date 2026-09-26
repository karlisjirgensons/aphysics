# -*- coding: utf-8 -*-
"""4. klase, 72. stunda: «Kā reizināt skaitļus ar nullēm galā?»

Vispārinājums: 300 · 40 = 3 · 4 · 100 · 10 = 12 · 1000. Sareizina skaitļus
bez nullēm un pieliek visas nulles kopā. Uzmanīgi, ja reizinājums pats
beidzas ar nulli: 50 · 20 = 1000 (nevis 100).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā reizināt skaitļus ar nullēm galā?"

MERKIS = ("Secināsim, kā sareizināt skaitļus, kas beidzas ar vienu vai "
          "vairākām nullēm.")

SATURS = [
    Sakums("Cik sēdvietu 20 lidmašīnās pa 300 vietām?",
           zimejums=restis([["300 · 20", "3 · 2", "000 klāt"],
                            ["", "6", "6000"]],
                           "nulles noliek malā, pēc tam pieliek"),
           paraksts="3 · 2 = 6, un vēl trīs nulles - 6000.",
           fakti=["Lielā lidmašīnā var būt ap 300 sēdvietām.",
                  "Nulles var noskaitīt atsevišķi."]),

    Doma("Sareizini bez nullēm, pieliec visas nulles",
         "Skaitļu nulles galā «noliek malā», sareizina pārējo un pieliek "
         "nulles tik, cik bija abos reizinātājos kopā.",
         soli=[
             "Saskaiti nulles abos skaitļos: 300 un 20 - trīs nulles.",
             "Sareizini bez nullēm: 3 · 2 = 6.",
             "Pieliec nulles: 6000.",
             "Ja reizinājumā pašā ir nulle (5 · 2 = 10), tā paliek!",
         ],
         pieze="50 · 20: 5 · 2 = 10, plus divas nulles - 1000."),

    Paraugs("400 · 50",
            uzd="Izrēķini 400 · 50.",
            soli=[
                ("nulles: 2 + 1 = 3", None),
                ("4 · 5 = 20", "Reizinājumā jau ir sava nulle."),
                ("20 un vēl 000 → 20 000", None),
            ],
            atbilde="20 000"),

    Ievadi("Nulles galā", [
        {"jaut": "300 · 20 = ?", "atb": ["6000"], "padoms": "6 un 000."},
        {"jaut": "40 · 50 = ?", "atb": ["2000"], "padoms": "20 un 00."},
        {"jaut": "120 · 30 = ?", "atb": ["3600"], "padoms": "36 un 00."},
        {"jaut": "250 · 40 = ?", "atb": ["10000", "10 000"],
         "padoms": "25 · 4 = 100 un 00."},
        {"jaut": "70 · 80 = ?", "atb": ["5600"], "padoms": "56 un 00."},
        {"jaut": "600 · 15 = ?", "atb": ["9000"], "padoms": "90 un 00."},
    ], pamats=4),

    Varianti("Cik nuļļu?", [
        {"jaut": "Cik nuļļu būs 30 · 200 rezultātā?",
         "opcijas": ["3", "2", "1", "4"], "pareizi": 0,
         "padoms": "6 un 000."},
        {"jaut": "Cik nuļļu būs 50 · 40 rezultātā?",
         "opcijas": ["3", "2", "1", "4"], "pareizi": 0,
         "padoms": "5 · 4 = 20 - vēl viena nulle."},
        {"jaut": "Kura atbilde pareiza: 25 · 400?",
         "opcijas": ["10 000", "1000", "100 000", "10 400"], "pareizi": 0,
         "padoms": "25 · 4 = 100, pieliek 00."},
        {"jaut": "Toms: 60 · 50 = 300. Kas nav kārtībā?",
         "opcijas": ["pazaudēja vienu nulli", "viss pareizi",
                     "sajauca ciparus"], "pareizi": 0,
         "padoms": "6 · 5 = 30, pieliek 00 - 3000."},
    ], pamats=4),

    Pasaule("Aviokompānijas diena",
            Ievadi("", [
                {"jaut": "Lidmašīnā 180 vietu. Cik vietu 20 reisos?",
                 "atb": ["3600"], "padoms": "18 · 2 = 36, pieliek 00."},
                {"jaut": "Biļete 50 €. Ieņēmumi no 180 pasažieriem?",
                 "atb": ["9000"], "padoms": "18 · 5 = 90, pieliek 00."},
                {"jaut": "Lidmašīna stundā nolido 800 km. Cik km 9 stundās?",
                 "atb": ["7200"], "padoms": "8 · 9 = 72, pieliek 00."},
                {"jaut": "Lidmašīna minūtē patērē 30 l degvielas. Cik litru 10 "
                         "minūtēs?",
                 "atb": ["300"], "padoms": "30 · 10."},
            ]),
            pavediens="celojums",
            konteksts="Aviācijā skaitļi ir lieli, bet bieži apaļi - un nulles "
                      "var noskaitīt atsevišķi.",
            kapec="Nulles triks ļauj rēķināt ar tūkstošiem galvā."),

    Kopsavilkums([
        "Reizinu skaitļus ar nullēm galā.",
        "Saskaitu nulles abos reizinātājos.",
        "Pamanu, ja reizinājums pats beidzas ar nulli.",
    ]),

    Majas([
        "Izrēķini, cik sekunžu ir 60 minūtēs (60 · 60).",
        "Izdomā 3 piemērus, kuros reizinājums pats beidzas ar 0.",
        "Pārbaudi ar kalkulatoru: 50 · 200 = ?",
    ]),
]
