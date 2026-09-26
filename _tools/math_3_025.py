# -*- coding: utf-8 -*-
"""3. klase, 25. stunda: «Kā reizināt 23 ar 2?»

Pirmais solis ārpus tabulas. Divciparu skaitli sadala desmitos un vienos,
katru daļu reizina atsevišķi un rezultātus saskaita. Tas ir tas pats
paņēmiens, kas vēlāk kļūs par reizināšanu stabiņā, tikai vēl pierakstīts
atklāti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā reizināt 23 ar 2?"

MERKIS = ("Iemācīsimies reizināt divciparu skaitli ar viencipara skaitli, "
          "atsevišķi reizinot desmitus un vienus.")

SATURS = [
    Sakums("Kā izrēķināt to, kā tabulā nav?",
           zimejums=restis([[23, "=", 20, "+", 3],
                            ["· 2", "", 40, "+", 6]],
                           "23 · 2 = 46"),
           paraksts="Skaitli sadala pa daļām, katru reizina atsevišķi.",
           fakti=["Reizināšanas tabulā ir tikai viencipara skaitļi.",
                  "Divciparu skaitli sadala desmitos un vienos."]),

    Doma("Sadali skaitli un reizini pa daļām",
         "23 · 2 = 20 · 2 + 3 · 2 - desmitus un vienus reizina atsevišķi un "
         "rezultātus saskaita.",
         soli=[
             "Sadali divciparu skaitli: 23 ir 20 un 3.",
             "Reizini desmitus: 20 · 2 = 40.",
             "Reizini vienus: 3 · 2 = 6.",
             "Saskaiti abus rezultātus: 40 + 6 = 46.",
         ],
         pieze="Desmitus reizināt ir viegli: 20 · 2 ir tas pats, kas 2 · 2 "
               "desmiti, tātad 4 desmiti jeb 40."),

    Slidnis("Kā sanāk 34 · 3",
            soli=[
                {"v": "34 = 30 + 4", "teksts": "Vispirms sadala skaitli.",
                 "josla": 25},
                {"v": "30 · 3 = 90", "teksts": "Reizina desmitus.",
                 "josla": 50},
                {"v": "4 · 3 = 12", "teksts": "Reizina vienus.",
                 "josla": 75},
                {"v": "90 + 12 = 102", "teksts": "Saskaita abas daļas.",
                 "josla": 100},
            ],
            ievads="Spied soļus un seko, kā skaitlis tiek salikts atpakaļ."),

    Paraugs("Cik ir 26 · 3?",
            uzd="Izrēķini 26 · 3, sadalot skaitli desmitos un vienos.",
            soli=[
                ("26 = 20 + 6",
                 "Divciparu skaitli sadala pa daļām."),
                ("20 · 3 = 60",
                 "Divi desmiti reiz trīs ir seši desmiti."),
                ("6 · 3 = 18",
                 "Vienus reizina pēc tabulas."),
                ("60 + 18 = 78",
                 "Abas daļas saskaita."),
            ],
            atbilde="78"),

    Ievadi("Reizini pa daļām", [
        {"jaut": "12 · 4 = ?", "atb": ["48"], "padoms": "40 + 8."},
        {"jaut": "23 · 3 = ?", "atb": ["69"], "padoms": "60 + 9."},
        {"jaut": "31 · 3 = ?", "atb": ["93"], "padoms": "90 + 3."},
        {"jaut": "24 · 4 = ?", "atb": ["96"], "padoms": "80 + 16."},
        {"jaut": "15 · 6 = ?", "atb": ["90"], "padoms": "60 + 30."},
        {"jaut": "18 · 5 = ?", "atb": ["90"], "padoms": "50 + 40."},
    ], pamats=4,
        ievads="Vispirms reizini desmitus, tad vienus, tad saskaiti."),

    Zimejums("Divas daļas vienā taisnstūrī",
             restis([["20 · 2 = 40", "3 · 2 = 6"],
                     ["desmiti", "vieni"]],
                    "23 · 2"),
             paskaidro="Taisnstūris ir sadalīts divās daļās; kopā tajās ir "
                       "46 rūtiņas.",
             ievads="Tā izskatās reizināšana pa daļām."),

    Varianti("Kurš sadalījums der?", [
        {"jaut": "Kā sadalīt 47 reizināšanai?",
         "opcijas": ["40 + 7", "4 + 7", "47 + 0", "40 · 7"],
         "pareizi": 0, "padoms": "Desmiti un vieni."},
        {"jaut": "Cik ir 20 · 4?",
         "opcijas": ["80", "24", "8", "60"],
         "pareizi": 0, "padoms": "Divi desmiti reiz četri."},
        {"jaut": "Cik ir 32 · 3?",
         "opcijas": ["96", "35", "66", "93"],
         "pareizi": 0, "padoms": "90 + 6."},
        {"jaut": "Kurš rēķins ir tas pats, kas 25 · 4?",
         "opcijas": ["20 · 4 + 5 · 4", "25 + 4", "20 · 4 + 5",
                     "2 · 4 + 5 · 4"],
         "pareizi": 0, "padoms": "Abas daļas reizina ar to pašu skaitli."},
    ], pamats=4),

    Pasaule("Cik maksā vairākas vienādas preces?",
            Ievadi("", [
                {"jaut": "Burtnīca maksā 23 ct. Cik maksā 3 burtnīcas?",
                 "atb": ["69"], "padoms": "60 + 9."},
                {"jaut": "Zīmuļu kaste maksā 14 ct. Cik maksā 5 kastes?",
                 "atb": ["70"], "padoms": "50 + 20."},
                {"jaut": "Cik maksā 4 burtnīcas pa 23 ct?",
                 "atb": ["92"], "padoms": "80 + 12."},
                {"jaut": "Cik centu pietrūks, ja kabatā ir 60 ct, bet vajag "
                         "3 burtnīcas?",
                 "atb": ["9"], "padoms": "69 − 60."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā cenas gandrīz nekad nav viencipara skaitļi - "
                      "tāpēc reizināšana pa daļām noder katru reizi.",
            kapec="Pirkuma summu var izrēķināt galvā, vēl stāvot pie "
                  "plaukta."),

    Kopsavilkums([
        "Reizinu divciparu skaitli ar viencipara skaitli.",
        "Sadalu skaitli desmitos un vienos un reizinu katru atsevišķi.",
        "Saskaitu abas daļas un pierakstu rezultātu.",
        "Reizinu apaļus desmitus bez pieraksta.",
    ]),

    Majas([
        "Izrēķini 16 · 4, 27 · 3 un 35 · 2, katru sadalot pa daļām.",
        "Atrodi veikalā cenu ar diviem cipariem un izrēķini, cik maksā "
        "trīs tādas preces.",
        "Pastāsti mājiniekiem, kāpēc 20 · 3 ir tikpat viegli kā 2 · 3.",
    ]),
]
