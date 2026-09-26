# -*- coding: utf-8 -*-
"""3. klase, 38. stunda: «Kā pārbaudīt savu darbu?»

Divas pārbaudes, kas strādā vienmēr: pretējā darbība un aptuvenā vērtība.
Pirmā atklāj sīkas kļūdas, otrā - rupjas. Stunda tās liek lietot kopā, jo
katra atsevišķi kādu kļūdas veidu palaiž garām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pārbaudīt savu darbu?"

MERKIS = ("Pārbaudīsim rezultātus ar pretējo darbību un ar aptuveno vērtību.")

SATURS = [
    Sakums("Kā pašam atrast savu kļūdu?",
           zimejums=restis([["rēķins", "pretējā darbība", "aptuveni"],
                            ["47 + 28 = 75", "75 − 28 = 47", "50 + 30 = 80"]],
                           "divas pārbaudes vienam rēķinam"),
           paraksts="Pirmā pārbauda precīzi, otrā - vai atbilde vispār ir "
                    "ticama.",
           fakti=["Pretējā darbība atklāj sīkas kļūdas.",
                  "Aptuvenā vērtība atklāj rupjas kļūdas."]),

    Doma("Divas pārbaudes, divi kļūdu veidi",
         "Pretējā darbība saka «par vienu par daudz», aptuvenā vērtība saka "
         "«desmit reižu par daudz».",
         soli=[
             "Izrēķini uzdevumu.",
             "Pārbaudi ar pretējo darbību: summu atņem, reizinājumu izdali.",
             "Novērtē atbildi aptuveni un salīdzini ar iegūto.",
             "Ja kāda pārbaude nesakrīt, rēķini vēlreiz.",
         ],
         pieze="Pretējā darbība saskaitīšanai ir atņemšana, reizināšanai - "
               "dalīšana, un otrādi. Tās vienmēr iet pa pāriem."),

    Paraugs("Vai 63 − 27 = 36?",
            uzd="Pārbaudi rezultātu 63 − 27 = 36 abos veidos.",
            soli=[
                ("36 + 27 = 63",
                 "Pretējā darbība: starpībai pieskaita atņēmēju."),
                ("60 − 30 = 30",
                 "Aptuvenā vērtība; atbilde 36 ir tuvu 30."),
                ("Abas pārbaudes sakrīt",
                 "Rezultāts ir pareizs."),
            ],
            atbilde="36 ir pareizi"),

    Ievadi("Izrēķini un pārbaudi", [
        {"jaut": "Ar ko pārbaudīt 45 + 38 = 83? Ieraksti pārbaudes rezultātu: "
                 "83 − 38 = ?",
         "atb": ["45"], "padoms": "Summai atņem otru saskaitāmo."},
        {"jaut": "Ar ko pārbaudīt 7 · 8 = 56? Ieraksti: 56 : 8 = ?",
         "atb": ["7"], "padoms": "Reizinājumu dala ar reizinātāju."},
        {"jaut": "72 − 35 = ?", "atb": ["37"], "padoms": "72 − 40 + 5."},
        {"jaut": "Pārbaudi: 37 + 35 = ?", "atb": ["72"],
         "padoms": "Ja sanāk 72, atbilde bija pareiza."},
        {"jaut": "84 : 6 = ?", "atb": ["14"], "padoms": "60 : 6 un 24 : 6."},
        {"jaut": "Pārbaudi: 14 · 6 = ?", "atb": ["84"],
         "padoms": "60 + 24."},
    ], pamats=4),

    Zimejums("Kas ar ko pārbauda",
             restis([["darbība", "pārbaude"],
                     ["saskaitīšana", "atņemšana"],
                     ["atņemšana", "saskaitīšana"],
                     ["reizināšana", "dalīšana"],
                     ["dalīšana", "reizināšana"]],
                    "darbības iet pa pāriem"),
             paskaidro="Katrai darbībai ir sava pretējā - tāpēc pārbaudīt "
                       "var vienmēr.",
             ievads="Šī tabula der visam gadam."),

    Varianti("Kura pārbaude der?", [
        {"jaut": "Ar ko pārbauda 96 : 8 = 12?",
         "opcijas": ["12 · 8", "96 · 8", "96 − 8", "12 : 8"],
         "pareizi": 0, "padoms": "Dalīšanu pārbauda ar reizināšanu."},
        {"jaut": "Skolēns uzrakstīja 38 + 47 = 715. Kura pārbaude to atklāj "
                 "visātrāk?",
         "opcijas": ["Aptuvenā vērtība 40 + 50 = 90",
                     "Pretējā darbība", "Pārrakstīšana", "Nekura"],
         "pareizi": 0, "padoms": "Kļūda ir rupja - to redz uzreiz."},
        {"jaut": "Ar ko pārbauda 85 − 39 = 46?",
         "opcijas": ["46 + 39", "85 + 39", "46 − 39", "85 : 39"],
         "pareizi": 0, "padoms": "Atņemšanu pārbauda ar saskaitīšanu."},
        {"jaut": "Kāpēc vajag abas pārbaudes?",
         "opcijas": ["Tās atklāj dažādus kļūdu veidus",
                     "Tā prasa skolotājs", "Lai darbs būtu garāks",
                     "Lai nevajadzētu rēķināt"],
         "pareizi": 0, "padoms": "Viena ķer sīkas, otra - rupjas kļūdas."},
    ], pamats=4),

    Pasaule("Vai rezultātu tabula ir pareiza?",
            Ievadi("", [
                {"jaut": "Komanda guva 48 un 37 punktus. Cik kopā?",
                 "atb": ["85"], "padoms": "48 + 40 − 3."},
                {"jaut": "Pārbaudi: 85 − 37 = ?", "atb": ["48"],
                 "padoms": "Ja sanāk 48, summa bija pareiza."},
                {"jaut": "Pretinieki guva 6 reizes pa 9 punktiem. Cik kopā?",
                 "atb": ["54"], "padoms": "6 · 9."},
                {"jaut": "Pārbaudi: 54 : 9 = ?", "atb": ["6"],
                 "padoms": "Reizinājumu dala ar reizinātāju."},
            ]),
            pavediens="sports",
            konteksts="Sacensību tabulā kļūda maina uzvarētāju - tāpēc katru "
                      "summu pārbauda divi cilvēki.",
            kapec="Pārbaude aizņem mirkli un pasargā no strīda."),

    Kopsavilkums([
        "Pārbaudu rezultātu ar pretējo darbību.",
        "Pārbaudu rezultātu ar aptuveno vērtību.",
        "Zinu, kura darbība ir kuras pretējā.",
        "Lietoju abas pārbaudes kopā.",
    ]),

    Majas([
        "Izrēķini piecus piemērus un pārbaudi katru abos veidos.",
        "Atrodi kļūdu rēķinā 74 − 28 = 54 un izlabo to.",
        "Pastāsti mājiniekiem, kāpēc aptuvenā vērtība ir noderīga.",
    ]),
]
