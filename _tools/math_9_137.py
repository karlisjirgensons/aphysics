# -*- coding: utf-8 -*-
"""9. klase, 137. stunda: «Cik ir visu skaitļu summa no 1 līdz 100?»

Leģenda par mazo Gausu: skolotājs uzdeva saskaitīt 1 + 2 + ... + 100,
Gauss atbildēja uzreiz - 50 pāri pa 101. Tā pati ideja kā summas formulai,
izstāstīta kā stāsts un pārbaudīta ar citām summām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Cik ir visu skaitļu summa no 1 līdz 100?"

MERKIS = ("Aprēķināsim summu, izmantojot progresijas īpašības, un "
          "skaidrosim paņēmienu.")

SATURS = [
    Sakums("Mazā Gausa triks",
           zimejums=restis([["1 + 100", "2 + 99", "3 + 98", "…", "50 + 51"],
                            ["101", "101", "101", "…", "101"]]),
           paraksts="50 pāri pa 101: summa 5050.",
           fakti=["Stāsta, ka Gauss to atrisināja kā skolēns.",
                  "Pirmais + pēdējais = otrais + priekšpēdējais = ...",
                  "Tā ir summas formula: {(1 + 100) · 100|2}."]),

    Doma("Pāru metode",
         "Aritmētiskajā progresijā simetrisku locekļu summas ir vienādas: "
         "a_1 + a_n = a_2 + a_{n−1} = ...",
         soli=[
             "Saliec pāros pirmo ar pēdējo, otro ar priekšpēdējo...",
             "Katrs pāris dod a_1 + a_n.",
             "Pāru skaits: {n|2}.",
             "Nepāra n gadījumā vidējais loceklis paliek viens - formula "
             "der arī tad.",
         ]),

    Slidnis("Gausa triks dažādām summām", [
        {"v": "1..10", "teksts": "5 pāri pa 11: 55"},
        {"v": "1..100", "teksts": "50 pāri pa 101: 5050"},
        {"v": "1..1000", "teksts": "500 pāri pa 1001: 500 500"},
        {"v": "51..100", "teksts": "25 pāri pa 151: 3775"},
    ]),

    Ievadi("Aprēķini ar Gausa triku", [
        {"jaut": "1 + 2 + ... + 20 = ?", "atb": ["210"], "padoms": "10 · 21."},
        {"jaut": "1 + 2 + ... + 50 = ?", "atb": ["1275", "1 275"],
         "padoms": "25 · 51."},
        {"jaut": "11 + 12 + ... + 30 = ?", "atb": ["410"],
         "padoms": "20 locekļi: 10 · 41."},
        {"jaut": "1 + 2 + ... + n = 78. n = ?", "atb": ["12"],
         "padoms": "{n(n + 1)|2} = 78."},
    ]),

    Varianti("Izvēlies", [
        {"jaut": "1 + 2 + ... + n = ?",
         "opcijas": ["{n(n + 1)|2}", "{n^2|2}", "n(n + 1)", "{n + 1|2}"],
         "pareizi": 0, "padoms": "a_1 = 1, a_n = n."},
        {"jaut": "Cik locekļu ir summā 15 + 16 + ... + 40?",
         "opcijas": ["26", "25", "40", "55"],
         "pareizi": 0, "padoms": "40 − 15 + 1."},
    ]),

    Pasaule("Svētku galda sveces",
            Ievadi("", [
                {"jaut": "Katrā dzimšanas dienā uz torta tik sveču, cik gadu. "
                         "Cik sveču kopā izdegušas, kad svin 15. dzimšanas "
                         "dienu (1. līdz 15.)?", "atb": ["120"],
                 "padoms": "{15 · 16|2}."},
                {"jaut": "Un līdz 18. dzimšanas dienai?", "atb": ["171"],
                 "padoms": "{18 · 19|2}."},
            ]),
            pavediens="virtuve",
            konteksts="Katru gadu tortē ir par vienu sveci vairāk - pēc kārtas "
                      "1, 2, 3, ...",
            kapec="Gausa summa saskaita visus gadus uzreiz."),

    Kopsavilkums([
        "Saskaitu 1 + 2 + ... + n ar pāru metodi.",
        "Lietoju formulu {n(n + 1)|2}.",
        "Nosaku locekļu skaitu summā.",
    ]),

    Majas([
        "Aprēķini 1 + 2 + ... + 200.",
        "Aprēķini 101 + 102 + ... + 200.",
        "Izstāsti Gausa triku kādam mājās.",
    ]),
]
