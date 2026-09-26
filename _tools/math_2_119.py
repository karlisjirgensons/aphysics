# -*- coding: utf-8 -*-
"""2. klase, 119. stunda: «Kur dabā ir pāri?»

Pāri ir visur: acis, rokas, putna spārni, kurpes. Ja zina pāru skaitu,
kopējo skaitu atrod, skaitot pa 2 - tas ir tas pats, kas reizināt ar 2.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes, taisne)

TEMA = "Kur dabā ir pāri?"

MERKIS = ("Šodien atradīsim objektus, ko veido pāri, un pierakstīsim "
          "kopējo skaitu.")

SATURS = [
    Sakums("Cik spārnu ir 6 putniem?",
           zimejums=bildes([[("putns", 6)]]),
           paraksts="Katram putnam 2 spārni.",
           fakti=["Skaiti pa 2: 2, 4, 6, 8, 10, 12.",
                  "6 putniem - 12 spārni.",
                  "Pāri ir visur dabā."]),

    Doma("Skaitīšana pa pāriem",
         "Ja katrā ir pa 2, skaita pa 2.",
         soli=[
             "Saskaiti, cik ir priekšmetu (pāru).",
             "Katram - 2.",
             "Skaiti: 2, 4, 6 ... tik reizes, cik pāru.",
             "Pēdējais skaitlis - kopējais skaits.",
         ]),

    Ievadi("Cik kopā?", [
        {"jaut": "Cik acu ir 5 kaķiem?", "atb": ["10"],
         "padoms": "2, 4, 6, 8, 10."},
        {"jaut": "Cik kurpju ir 7 pāros?", "atb": ["14"],
         "padoms": "Skaiti pa 2 septiņas reizes."},
        {"jaut": "Cik roku ir 9 bērniem?", "atb": ["18"],
         "padoms": "9 + 9."},
        {"jaut": "Cik ausu ir 4 zaķiem?", "atb": ["8"], "padoms": "4 + 4."},
        {"jaut": "Cik riteņu ir 8 velosipēdiem?", "atb": ["16"],
         "padoms": "8 + 8."},
        {"jaut": "Cik kāju ir 10 vistām?",
         "atb": ["20"], "padoms": "10 + 10."},
    ], pamats=4),

    Varianti("Pāri vai nē?", [
        {"jaut": "Kam nav pāra?", "opcijas": ["deguns", "acs", "auss"],
         "pareizi": 0, "padoms": "Deguns ir viens."},
        {"jaut": "Kas nāk pa pāriem?", "opcijas": ["cimdi", "cepure",
                                                    "šalle"],
         "pareizi": 0, "padoms": "Katrai rokai."},
        {"jaut": "Skaitot pa 2 no 2, kurš skaitlis nebūs?",
         "zim": taisne(0, 20, 2), "opcijas": ["15", "14", "16"],
         "pareizi": 0, "padoms": "Pa 2 - tikai dubulti."},
    ]),

    Pasaule("Ligzdas pavasarī",
            Ievadi("", [
                {"jaut": "Katrā ligzdā ir putnu pāris. Ir 8 ligzdas. Cik "
                         "putnu?", "atb": ["16"], "padoms": "8 + 8."},
                {"jaut": "Parkā saskaitīja 20 gulbju - visi pāros. Cik "
                         "pāru?", "atb": ["10"], "padoms": "10 + 10."},
            ]),
            pavediens="daba",
            konteksts="Gulbji un stārķi dzīvo pāros visu mūžu.",
            kapec="Dabas pētnieki skaita putnus pa pāriem."),

    Kopsavilkums([
        "Atrodu dabā un mājās pārus.",
        "Skaitu pa 2.",
        "Aprēķinu kopējo skaitu no pāru skaita.",
    ]),

    Majas([
        "Atrodi mājās 5 lietas, kas nāk pa pāriem.",
        "Saskaiti pa 2, cik to ir kopā.",
        "Uzraksti, cik pāru un cik kopā.",
    ]),
]
