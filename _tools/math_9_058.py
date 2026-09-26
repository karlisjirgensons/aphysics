# -*- coding: utf-8 -*-
"""9. klase, 58. stunda: «Kad izteiksme ir reizinājums?»

Izteiksme ir sadalīta reizinātājos, ja PĒDĒJĀ darbība ir reizināšana.
3(x + 2) ir reizinājums, 3x + 6 - summa, lai gan vērtība tā pati. Šis
skatījums vajadzīgs visā temata tālākajā gaitā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, restis)

TEMA = "Kad izteiksme ir reizinājums?"

MERKIS = ("Noteiksim, vai izteiksme ir sadalīta reizinātājos, pēc pēdējās "
          "darbības.")

# Taisnstūris 3 × (x + 2): viens laukums - divi pieraksti.
_LAUKUMS = geometrija([("A", 0, 0), ("E", 5, 0), ("B", 7, 0), ("C", 7, 3),
                       ("F", 5, 3), ("D", 0, 3)],
                      nogriezni=["AB", "BC", "CD", "DA", "EF"],
                      iekrasot=[("AEFD", 0), ("EBCF", 1)],
                      malas=[("AE", "x"), ("EB", "2"), ("DA", "3")],
                      uzraksti=[(2.5, 1.5, "3x"), (6, 1.5, "6")])

SATURS = [
    Sakums("3(x + 2) un 3x + 6 - kas atšķiras?",
           zimejums=_LAUKUMS,
           paraksts="Viens laukums: kā reizinājums 3(x + 2) vai summa 3x + 6.",
           fakti=["Vērtība abām izteiksmēm vienāda.",
                  "Bet 3(x + 2) ir reizinājums - pēdējā darbība ir «·».",
                  "3x + 6 ir summa - pēdējā darbība ir «+»."]),

    Doma("Pēdējā darbība",
         "Izteiksme ir sadalīta reizinātājos, ja to aprēķinot pēdējā darbība "
         "ir reizināšana.",
         soli=[
             "Iedomājies, ka aprēķini izteiksmi ar skaitli.",
             "Kura darbība būtu pēdējā?",
             "«·» - reizinājums; «+» vai «−» - summa vai starpība.",
             "Sadalīt reizinātājos = pārveidot summu reizinājumā.",
         ]),

    Slidnis("Kura darbība pēdējā?", [
        {"v": "3(x + 2)", "teksts": "Vispirms x + 2, tad · 3 → reizinājums",
         "zim": restis([["x = 4", "4 + 2 = 6", "3 · 6 = 18"]])},
        {"v": "3x + 6", "teksts": "Vispirms 3 · x, tad + 6 → summa",
         "zim": restis([["x = 4", "3 · 4 = 12", "12 + 6 = 18"]])},
        {"v": "(x + 1)(x − 1)", "teksts": "Divas iekavas, tad · → reizinājums",
         "zim": restis([["x = 4", "5 un 3", "5 · 3 = 15"]])},
        {"v": "x(x + 1) + 2", "teksts": "Pēdējā ir + → NAV reizinājums",
         "zim": restis([["x = 4", "4 · 5 = 20", "20 + 2 = 22"]])},
    ]),

    Varianti("Reizinājums vai nē?", [
        {"jaut": "5a(b − 2)",
         "opcijas": ["Reizinājums", "Summa", "Starpība", "Dalījums"],
         "pareizi": 0, "padoms": "Pēdējā: 5a · (b − 2)."},
        {"jaut": "ab − 2a",
         "opcijas": ["Starpība", "Reizinājums", "Summa", "Kvadrāts"],
         "pareizi": 0, "padoms": "Pēdējā: −."},
        {"jaut": "(x − 3)^2",
         "opcijas": ["Reizinājums (x − 3)(x − 3)", "Starpība", "Summa",
                     "Neviens"],
         "pareizi": 0, "padoms": "Kvadrāts ir reizinājums."},
        {"jaut": "x(x + 2) − 3(x + 2)",
         "opcijas": ["Starpība", "Reizinājums", "Summa", "Kvadrāts"],
         "pareizi": 0, "padoms": "Pēdējā: − starp diviem reizinājumiem."},
        {"jaut": "(a + b)(a − b)",
         "opcijas": ["Reizinājums", "Starpība", "Summa", "Kvadrāts"],
         "pareizi": 0, "padoms": "Iekavas reizinātas."},
    ], pamats=3),

    Ievadi("Aprēķini abos veidos (x = 5)", [
        {"jaut": "3(x + 2) = ?", "atb": ["21"], "padoms": "3 · 7."},
        {"jaut": "3x + 6 = ?", "atb": ["21"], "padoms": "15 + 6."},
        {"jaut": "(x − 1)(x + 1) = ?", "atb": ["24"], "padoms": "4 · 6."},
        {"jaut": "x^2 − 1 = ?", "atb": ["24"], "padoms": "25 − 1."},
    ]),

    Pasaule("Iepirkumu čeks",
            Ievadi("", [
                {"jaut": "3 klasesbiedri pērk katrs sviestmaizi par 2,40 € un "
                         "sulu par 1,60 €. Kopā 3(2,40 + 1,60) = ? €",
                 "atb": ["12"], "padoms": "3 · 4."},
                {"jaut": "Tas pats kā summa 3 · 2,40 + 3 · 1,60 = ? €",
                 "atb": ["12"], "padoms": "7,20 + 4,80."},
            ]),
            pavediens="veikals",
            konteksts="Kasiere var skaitīt katru preci atsevišķi (summa) vai "
                      "vienu komplektu reiz 3 (reizinājums).",
            kapec="Reizinājuma forma bieži ir īsāka un ātrāka."),

    Kopsavilkums([
        "Nosaku izteiksmes pēdējo darbību.",
        "Atšķiru reizinājumu no summas.",
        "Zinu, ka vērtība nemainās, mainās tikai forma.",
    ]),

    Majas([
        "Uzraksti 3 izteiksmes, kas ir reizinājumi, un 3, kas nav.",
        "Aprēķini 7 · 13 + 7 · 87 divos veidos. Kurš ātrāks?",
        "Uzzīmē taisnstūri, kas parāda 2(a + 5).",
    ]),
]
