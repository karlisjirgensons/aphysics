# -*- coding: utf-8 -*-
"""9. klase, 43. stunda: «Kas ir kosinuss un tangenss?»

Pārējās divas attiecības: cos α = {b|c} un tg α = {a|b}. Latvijā tangensu
raksta «tg», kalkulatorā - «tan». Tangenss ir slīpums, ko ceļa zīme
«kāpums 10 %» jau rāda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis, taisnlenka)

TEMA = "Kas ir kosinuss un tangenss?"

MERKIS = ("Definēsim kosinusu un tangensu un noteiksim tos konkrētā "
          "trijstūrī.")

SATURS = [
    Sakums("Ceļa zīme «kāpums 10 %» - kas tas ir?",
           zimejums=taisnlenka(10, 3, ("1 m", "10 m", None), "α"),
           paraksts="10 m uz priekšu - 1 m uz augšu: tg α = 0,1 "
                    "(nav mērogā).",
           fakti=["tg α = pretkatete : piekatete - tas ir slīpums.",
                  "cos α = piekatete : hipotenūza.",
                  "Latvijā raksta tg α; kalkulatorā poga «tan»."]),

    Doma("Trīs trigonometriskās sakarības",
         "sin α = {a|c}, cos α = {b|c}, tg α = {a|b}, kur a - pretkatete, "
         "b - piekatete, c - hipotenūza.",
         soli=[
             "Sinuss: pretkatete : hipotenūza.",
             "Kosinuss: piekatete : hipotenūza.",
             "Tangenss: pretkatete : piekatete.",
             "Pārbaude: tg α = {sin α|cos α}.",
         ],
         pieze="Leņķa B kosinuss ir leņķa A sinuss: cos B = sin A."),

    Paraugs("Visas trīs",
            uzd="△ABC, ∠C = 90°, AC = 8, BC = 6. Atrodi sin A, cos A, tg A.",
            soli=[
                ("AB = √(64 + 36) = 10", "Hipotenūza."),
                ("sin A = {6|10} = 0,6; cos A = {8|10} = 0,8",
                 "Pretkatete BC, piekatete AC."),
                ("tg A = {6|8} = 0,75", "Pretkatete : piekatete."),
            ],
            atbilde="0,6; 0,8; 0,75"),

    Ievadi("Aprēķini (katetes 5 un 12, hipotenūza 13; α pretī 5)", [
        {"jaut": "cos α = ? (daļa)", "atb": ["{12|13}", "12/13"],
         "tastatura": "text", "padoms": "Piekatete 12."},
        {"jaut": "tg α = ? (daļa)", "atb": ["{5|12}", "5/12"],
         "tastatura": "text", "padoms": "5 : 12."},
        {"jaut": "Otra leņķa β tangenss? (daļa)", "atb": ["{12|5}", "12/5",
                                                         "2,4"],
         "tastatura": "text", "padoms": "Pretī β ir 12."},
        {"jaut": "cos α = 0,6, hipotenūza 20. Piekatete?", "atb": ["12"],
         "padoms": "20 · 0,6."},
        {"jaut": "tg α = 1,5, piekatete 4. Pretkatete?", "atb": ["6"],
         "padoms": "4 · 1,5."},
        {"jaut": "tg α = 0,5, pretkatete 7. Piekatete?", "atb": ["14"],
         "padoms": "7 : 0,5."},
    ], pamats=4),

    Varianti("Kura sakarība?", [
        {"jaut": "{AC|AB} (∠C = 90°) ir...",
         "opcijas": ["cos A", "sin A", "tg A", "tg B"],
         "pareizi": 0, "padoms": "AC - piekatete leņķim A."},
        {"jaut": "{BC|AC} ir...",
         "opcijas": ["tg A", "cos A", "sin B", "tg B"],
         "pareizi": 0, "padoms": "Pretī A : pie A."},
        {"jaut": "Kura var būt lielāka par 1?",
         "opcijas": ["tg α", "sin α", "cos α", "neviena"],
         "pareizi": 0, "padoms": "Katete var būt garāka par otru kateti."},
        {"jaut": "cos 60° = sin ?",
         "opcijas": ["30°", "60°", "90°", "120°"],
         "pareizi": 0, "padoms": "cos α = sin(90° − α)."},
    ]),

    Pasaule("Ceļa zīmes kalnos",
            Ievadi("", [
                {"jaut": "Zīme «kāpums 8 %». Cik m ceļš paceļas uz 500 m "
                         "horizontāli?", "atb": ["40"], "padoms": "500 · 0,08."},
                {"jaut": "Ceļš paceļas 60 m uz 400 m. Kāpums procentos?",
                 "atb": ["15", "15 %", "15%"], "padoms": "tg α = 0,15."},
                {"jaut": "Kurš ceļš stāvāks: 12 % vai tg α = 0,1?",
                 "atb": ["12", "12 %", "12%"], "padoms": "0,12 > 0,1."},
            ]),
            pavediens="celojums",
            konteksts="Kāpuma zīme rāda tangensu procentos: pacēlums uz 100 m "
                      "horizontāli.",
            kapec="Autovadītājs lasa tangensu, pat to nezinot.",
            zimejums=restis([["zīme", "tg α"], ["8 %", "0,08"],
                             ["15 %", "0,15"]])),

    Kopsavilkums([
        "Definēju kosinusu un tangensu.",
        "Nosaku sin, cos, tg konkrētā trijstūrī.",
        "Saprotu kāpumu procentos kā tangensu.",
    ]),

    Majas([
        "Trijstūrī 7, 24, 25 aprēķini sin, cos, tg abiem šaurajiem leņķiem.",
        "Pārbaudi: vai tg α = sin α : cos α?",
        "Atrodi internetā stāvāko ielu pasaulē un tās kāpumu procentos.",
    ]),
]
