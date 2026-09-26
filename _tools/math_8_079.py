# -*- coding: utf-8 -*-
"""8. klase, 79. stunda: «Kā izskatās izklājums?»

Bloka noslēgums: kvadra, trijstūra prizmas un cilindra izklājums pēc
dotiem izmēriem. Cilindra sānu virsma ir taisnstūris 2πr × h - tieši
pamata riņķa līnijas garumā. Sagatavo virsmas laukumu (80.-81. stunda).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, cilindra_izklajums,
                         izklajums, prizmas_izklajums)

TEMA = "Kā izskatās izklājums?"

MERKIS = ("Zīmēsim prizmas un cilindra virsmas izklājumu pēc dotiem "
          "izmēriem.")

SATURS = [
    Sakums("Kā atritināt cilindru?",
           zimejums=cilindra_izklajums(),
           paraksts="Sānu virsma ir taisnstūris, tā garums - pamata riņķa "
                    "līnija.",
           fakti=["Cilindra izklājums: taisnstūris un divi riņķi.",
                  "Taisnstūra izmēri ir 2πr × h.",
                  "Prizmas izklājums: sānu taisnstūri rindā un divi pamati."]),

    Doma("Izklājums pēc izmēriem",
         "Izklājumā ir visas virsmas daļas īstajā izmērā.",
         soli=[
             "Kvadram: 6 taisnstūri, pretējie - vienādi.",
             "Trijstūra prizmai: taisnstūri a × h, b × h, c × h un divi "
             "trijstūri.",
             "Cilindram: taisnstūris 2πr × h un divi riņķi ar rādiusu r.",
             "Pārbaudi: malām, kas salokot saskaras, jābūt vienāda garuma.",
         ]),

    Slidnis("Trīs izklājumi", [
        {"v": "Kvadrs", "teksts": "Seši taisnstūri, pa pāriem vienādi",
         "zim": izklajums(4, 3, 2)},
        {"v": "Trijstūra prizma", "teksts": "Trīs taisnstūri un divi "
                                            "trijstūri",
         "zim": prizmas_izklajums(3, 4, 5, 6)},
        {"v": "Cilindrs", "teksts": "Taisnstūris 2πr × h un divi riņķi",
         "zim": cilindra_izklajums()},
    ]),

    Paraugs("Cilindra izklājums",
            uzd="Cilindram r = 5 cm, h = 12 cm. Kādi ir izklājuma izmēri "
                "(π ≈ 3,14)?",
            soli=[
                ("2πr = 2 · 3,14 · 5 = 31,4 cm", "Taisnstūra garums."),
                ("h = 12 cm", "Taisnstūra platums."),
                ("Divi riņķi ar r = 5 cm", "Pamati."),
            ],
            atbilde="Taisnstūris 31,4 cm × 12 cm un divi riņķi ar r = 5 cm"),

    Ievadi("Aprēķini izmērus", [
        {"jaut": "Cilindrs r = 2 cm, h = 10 cm. Taisnstūra garums (cm, π ≈ "
                 "3,14)?", "atb": ["12,56"], "padoms": "2 · 3,14 · 2."},
        {"jaut": "Šī taisnstūra platums (cm)?", "atb": ["10"],
         "padoms": "h."},
        {"jaut": "Taisnstūris 31,4 cm × 8 cm. Pamata rādiuss (cm, π ≈ 3,14)?",
         "atb": ["5"], "padoms": "2 · 3,14 · r = 31,4."},
        {"jaut": "Prizma ar pamata malām 3, 4, 5 cm. Sānu taisnstūru "
                 "kopējais garums (cm)?", "atb": ["12"],
         "padoms": "3 + 4 + 5."},
        {"jaut": "Kvadrā 4 × 3 × 2 - cik taisnstūru 4 × 3?", "atb": ["2"],
         "padoms": "Pretējās skaldnes."},
        {"jaut": "Cik kvadrātu ir kuba izklājumā?", "atb": ["6"],
         "padoms": "Sešas skaldnes."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Vai no taisnstūra 20 × 10 un diviem riņķiem ar r = 5 var "
                 "salocīt cilindru?",
         "opcijas": ["Nē - vajag 31,4 garu taisnstūri", "Jā",
                     "Tikai ja h = 5", "Tikai ja r = 10"],
         "pareizi": 0, "padoms": "2π · 5 ≈ 31,4."},
        {"jaut": "Cik trijstūru ir četrstūra prizmas izklājumā?",
         "opcijas": ["0", "2", "4", "6"],
         "pareizi": 0, "padoms": "Pamati ir četrstūri."},
        {"jaut": "Sešstūra prizmas izklājumā ir...",
         "opcijas": ["6 taisnstūri un 2 sešstūri", "6 trijstūri",
                     "2 taisnstūri un 6 sešstūri", "8 taisnstūri"],
         "pareizi": 0, "padoms": "n sāni un 2 pamati."},
    ]),

    Pasaule("Dāvanu kastīte",
            Ievadi("", [
                {"jaut": "Kastīte - prizma ar taisnleņķa trijstūra pamatu "
                         "(6, 8, 10 cm) un garumu 15 cm. Sānu taisnstūru "
                         "laukums kopā (cm²)?",
                 "atb": ["360"], "padoms": "(6 + 8 + 10) · 15."},
                {"jaut": "Abu pamatu laukums kopā (cm²)?", "atb": ["48"],
                 "padoms": "2 · {6 · 8|2}."},
                {"jaut": "Cik cm² kartona vajag visam izklājumam?",
                 "atb": ["408"], "padoms": "360 + 48."},
            ]),
            pavediens="veikals",
            konteksts="Iepakojumu izgriež no kartona izklājuma formā un "
                      "saloka.",
            kapec="Izklājuma laukums ir kastītes virsmas laukums."),

    Kopsavilkums([
        "Zīmēju kvadra, prizmas un cilindra izklājumu.",
        "Aprēķinu cilindra izklājuma taisnstūra izmērus.",
        "Pārbaudu, vai izklājumu var salocīt.",
    ]),

    Majas([
        "Izgriez cilindra izklājumu ar r = 3 cm un h = 8 cm un saloki to.",
        "Izjauc kādu kartona iepakojumu un uzzīmē tā izklājumu.",
        "Aprēķini, cik kartona aizņem tavs izklājums.",
    ]),
]
