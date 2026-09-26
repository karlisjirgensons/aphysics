# -*- coding: utf-8 -*-
"""9. klase, 120. stunda: «Kā risināt uzdevumu par maisījumiem?»

Maisījumi un sastāvs: sāls šķīdums, sakausējums, kafijas maisījums. Viens
vienādojums - masas (daudzuma) summa, otrs - vielas daudzuma summa
(masa · daļa). Procenti kļūst par decimāldaļām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā risināt uzdevumu par maisījumiem?"

MERKIS = ("Risināsim uzdevumu par sastāvu vai izmaksām, veidojot sistēmu.")

SATURS = [
    Sakums("Kā iegūt 10 % sāls šķīdumu no 5 % un 20 %?",
           zimejums=restis([["šķīdums", "masa", "sāls daļa", "sāls"],
                            ["5 %", "x", "0,05", "0,05x"],
                            ["20 %", "y", "0,2", "0,2y"],
                            ["10 %", "300 g", "0,1", "30 g"]]),
           paraksts="x + y = 300 un 0,05x + 0,2y = 30.",
           fakti=["Masas saskaitās.",
                  "Sāls daudzumi saskaitās.",
                  "Procenti nesaskaitās - tos pārvērš gramos."]),

    Doma("Maisījuma sistēma",
         "Pirmais vienādojums - daudzumu summa, otrais - «vielas» summa "
         "(daudzums · daļa vai daudzums · cena).",
         soli=[
             "Nezināmie - sastāvdaļu daudzumi.",
             "Tabula: daudzums, daļa (cena), vielas daudzums (summa).",
             "Rindu «kopā» pieraksti divos vienādojumos.",
             "Procentus raksti kā decimāldaļas: 5 % = 0,05.",
         ]),

    Paraugs("Šķīdums",
            uzd="Atrisini x + y = 300, 0,05x + 0,2y = 30.",
            soli=[
                ("· 20: x + 4y = 600", "Otro vienkāršo."),
                ("Atņem pirmo: 3y = 300 ⇒ y = 100", "20 % šķīdums."),
                ("x = 200", "5 % šķīdums."),
            ],
            atbilde="200 g 5 % un 100 g 20 % šķīduma"),

    Ievadi("Aprēķini", [
        {"jaut": "Kafija 8 €/kg un 14 €/kg, maisījums 6 kg par 10 €/kg. "
                 "Cik kg lētākās?", "atb": ["4"],
         "padoms": "x + y = 6, 8x + 14y = 60."},
        {"jaut": "Cik kg dārgākās?", "atb": ["2"], "padoms": "6 − 4."},
        {"jaut": "Cik g sāls ir 250 g 8 % šķīduma?", "atb": ["20"],
         "padoms": "0,08 · 250."},
        {"jaut": "Sakausējums: 40 % un 70 % vara, iegūst 30 kg ar 60 % vara. "
                 "Cik kg 70 %?", "atb": ["20"],
         "padoms": "x + y = 30, 0,4x + 0,7y = 18."},
    ], pamats=2),

    Varianti("Kurš vienādojums?", [
        {"jaut": "5 % un 20 % šķīdumi dod 300 g 10 %. Otrais vienādojums:",
         "opcijas": ["0,05x + 0,2y = 30", "5x + 20y = 10",
                     "0,05x + 0,2y = 0,1", "x + y = 10"],
         "pareizi": 0, "padoms": "Sāls grami."},
        {"jaut": "Vai 10 % un 20 % šķīdumus sajaucot var iegūt 25 %?",
         "opcijas": ["Nē - maisījums ir starp 10 % un 20 %", "Jā",
                     "Jā, ja daudz 20 %", "Tikai uzsildot"],
         "pareizi": 0, "padoms": "Vidējais ir starp."},
    ]),

    Pasaule("Stallis (eksāmens 2025)",
            Ievadi("", [
                {"jaut": "Stallī 88 nodalījumi, aizņemti 75 %. Cik dzīvnieku?",
                 "atb": ["66"], "padoms": "0,75 · 88."},
                {"jaut": "Ponijs 180 €, zirgs 270 € mēnesī; kopā 16 650 €. "
                         "x + y = 66, 180x + 270y = 16 650. Zirgu (y)?",
                 "atb": ["53"], "padoms": "180 · 66 = 11 880; 90y = 4770."},
                {"jaut": "Poniju?", "atb": ["13"], "padoms": "66 − 53."},
            ]),
            pavediens="daba",
            konteksts="2025. gada eksāmena 2. daļas 3. uzdevums (5 punkti) - "
                      "tieši šāda «maisījuma» sistēma.",
            kapec="Tabula ar skaitu, cenu un summu atrisina arī eksāmenu."),

    Kopsavilkums([
        "Sastādu tabulu maisījuma uzdevumam.",
        "Pierakstu daudzumu un vielas vienādojumus.",
        "Pārvēršu procentus decimāldaļās.",
    ]),

    Majas([
        "Cik 30 % un 10 % šķīduma jāņem, lai iegūtu 400 g 15 %?",
        "Sajauc 3 kg riekstu pa 12 €/kg ar rozīnēm pa 6 €/kg, lai "
        "1 kg maksātu 8 €. Cik kg rozīņu?",
        "Atrodi uz pārtikas iepakojuma procentus un izrēķini gramus.",
    ]),
]
