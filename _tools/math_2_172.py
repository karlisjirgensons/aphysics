# -*- coding: utf-8 -*-
"""2. klase, 172. stunda: «Ko gribu iemācīties 3. klasē?»

Gada pēdējā stunda: atskats uz 2. klasē apgūto (8 temati) un ieskats 3.
klasē - reizināšana ar 6-10, daļas, trīsciparu skaitļi, plāns un modeļi.
Stunda beidzas ar skolēna paša mērķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Ko gribu iemācīties 3. klasē?"

MERKIS = ("Šodien apkoposim gadā apgūto un iepazīsimies ar 3. klases "
          "tematiem.")

_GADS = restis([["2. klasē iemācījos", "piemērs"],
                ["grupēt", "Venna diagramma"],
                ["mērīt", "6 cm 5 mm"],
                ["rēķināt līdz 100", "47 + 36 = 83"],
                ["laiks", "8:23"],
                ["izteiksmes", "50 − (12 + 8)"],
                ["figūras", "perimetrs, laukums"],
                ["reizināt un dalīt", "4 · 5 = 20"]])

SATURS = [
    Sakums("Ko tu proti tagad, bet neprati septembrī?",
           zimejums=_GADS,
           paraksts="8 temati - viens gads.",
           fakti=["Septembrī - grupēšana un mērīšana.",
                  "Maijā - reizināšana un dalīšana.",
                  "Nākamgad - vēl lielāki skaitļi!"]),

    Doma("Ko nesīs 3. klase",
         "3. klasē mācīsies to, kam 2. klasē uzbūvēts pamats.",
         soli=[
             "Reizināšana ar 6, 7, 8, 9 un 10.",
             "Daļas: puse, trešdaļa - ar daļskaitļa pierakstu.",
             "Trīsciparu skaitļi līdz 1000.",
             "Vietas plāns un telpiski modeļi.",
         ]),

    Ievadi("Gada viktorīna", [
        {"jaut": "Cik mm ir 1 cm?", "atb": ["10"], "padoms": "2.2. temats."},
        {"jaut": "56 + 27 = ?", "atb": ["83"], "padoms": "70 + 13."},
        {"jaut": "Cik minūšu stundā?", "atb": ["60"], "padoms": "2.4. temats."},
        {"jaut": "40 − (15 + 5) = ?", "atb": ["20"], "padoms": "Iekavas."},
        {"jaut": "Kvadrāta mala 6 cm. P = ?", "atb": ["24"], "mers": "cm",
         "padoms": "4 · 6."},
        {"jaut": "35 : 5 = ?", "atb": ["7"], "padoms": "5 · 7."},
    ], pamats=4),

    Varianti("Kas nāks 3. klasē?", [
        {"jaut": "Kuru reizinājumu mācīsies 3. klasē?",
         "opcijas": ["7 · 8", "4 · 5", "2 · 3"], "pareizi": 0,
         "padoms": "Reizināšana ar 6-10."},
        {"jaut": "Līdz kuram skaitlim rēķinās 3. klasē?",
         "opcijas": ["1000", "100", "20"], "pareizi": 0,
         "padoms": "Trīsciparu skaitļi."},
    ]),

    Petijums("Mans mērķis", [
        "Izvēlies, kurš 2. klases temats tev patika visvairāk.",
        "Pastāsti klasei vienu lietu, ko iemācījies.",
        "Uzraksti vienu lietu, ko gribi iemācīties 3. klasē.",
        "Ieliec lapiņu aploksnē - atvērsiet septembrī!",
    ], vajag="lapiņa, aploksne"),

    Pasaule("Vasaras matemātika",
            Ievadi("", [
                {"jaut": "Vasarā ir 13 nedēļas. Ja katru nedēļu izlasi 2 "
                         "grāmatas, cik grāmatu izlasīsi? (13 · 2)",
                 "atb": ["26"], "padoms": "13 + 13."},
            ]),
            pavediens="skola",
            konteksts="Vasarā matemātika neaiziet atvaļinājumā.",
            kapec="Kas vasarā rēķina, septembrī sāk vieglāk."),

    Kopsavilkums([
        "Apkopoju, ko iemācījos 2. klasē.",
        "Zinu, ko mācīsies 3. klasē.",
        "Izvirzīju savu mērķi.",
    ]),

    Majas([
        "Vasarā vienreiz nedēļā izdomā matemātikas uzdevumu.",
        "Skaiti naudu veikalā un laiku ceļā.",
        "Uz tikšanos 3. klasē!",
    ]),
]
