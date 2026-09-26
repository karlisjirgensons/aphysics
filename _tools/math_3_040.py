# -*- coding: utf-8 -*-
"""3. klase, 40. stunda: «Kā pieraksta risinājumu ar izteiksmi?»

31. stundā divu darbību uzdevumu risināja pa soļiem; te to pašu risinājumu
saliek vienā izteiksmē. Grūtākais ir iekavas: ja pirmā darbība ir zemākā
pakāpienā, bez iekavām izteiksme nozīmē ko citu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pieraksta risinājumu ar izteiksmi?"

MERKIS = ("Dotam tekstam veidosim risinājumu gan pa darbībām, gan kā vienu "
          "izteiksmi.")

SATURS = [
    Sakums("Kā divus rēķinus salikt vienā rindā?",
           zimejums=restis([["1. 4 · 15 = 60", "2. 90 − 60 = 30"],
                            ["90 − 4 · 15 = 30", ""]],
                           "pa darbībām un ar izteiksmi"),
           paraksts="Abi pieraksti stāsta vienu un to pašu.",
           fakti=["Izteiksme parāda visu risinājumu vienā rindā.",
                  "Ja pirmā darbība ir saskaitīšana, vajag iekavas."]),

    Doma("Izteiksmē darbības saliek to izpildes secībā",
         "Ja pirmā darbība ir zemākā pakāpienā nekā otrā, to ieliek iekavās.",
         soli=[
             "Pieraksti risinājumu pa darbībām.",
             "Ieliec pirmās darbības vietā tās izteiksmi.",
             "Pārbaudi, vai darbību secība to izpildīs pirmo.",
             "Ja nē - ieliec iekavas.",
         ],
         pieze="(20 + 4) · 3 un 20 + 4 · 3 ir divas dažādas izteiksmes: "
               "pirmā dod 72, otrā - 32. Iekavas maina visu."),

    Paraugs("Kā pierakstīt vienā izteiksmē?",
            uzd="Klasē bija 20 zēni un 4 meitenes. Katrs atnesa 3 grāmatas. "
                "Cik grāmatu kopā?",
            soli=[
                ("20 + 4 = 24",
                 "Pirmā darbība: cik bērnu ir kopā."),
                ("24 · 3 = 72",
                 "Otrā darbība: cik grāmatu atnesa visi."),
                ("(20 + 4) · 3 = 72",
                 "Izteiksmē pirmā darbība jāieliek iekavās, jo saskaitīšana "
                 "ir zemākā pakāpienā."),
            ],
            atbilde="72 grāmatas"),

    Ievadi("Aprēķini izteiksmi", [
        {"jaut": "(20 + 4) · 3 = ?", "atb": ["72"],
         "padoms": "Vispirms iekavas."},
        {"jaut": "20 + 4 · 3 = ?", "atb": ["32"],
         "padoms": "Bez iekavām vispirms reizina."},
        {"jaut": "(50 − 20) : 6 = ?", "atb": ["5"],
         "padoms": "Vispirms 50 − 20."},
        {"jaut": "50 − 20 : 5 = ?", "atb": ["46"],
         "padoms": "Vispirms 20 : 5."},
        {"jaut": "(12 + 8) · 4 = ?", "atb": ["80"],
         "padoms": "Vispirms 12 + 8."},
        {"jaut": "(30 − 6) : 4 = ?", "atb": ["6"],
         "padoms": "Vispirms 30 − 6."},
    ], pamats=4),

    Zimejums("Iekavas maina atbildi",
             restis([["(20 + 4) · 3", "= 72"],
                     ["20 + 4 · 3", "= 32"]],
                    "tie paši skaitļi, cita atbilde"),
             paskaidro="Skaitļi un zīmes ir vienādas - atšķiras tikai "
                       "iekavas.",
             ievads="Salīdzini abas rindas."),

    Varianti("Kura izteiksme atbilst uzdevumam?", [
        {"jaut": "«Bija 30 ābolu, apēda 6, pārējos sadalīja 4 bērniem.»",
         "opcijas": ["(30 − 6) : 4", "30 − 6 : 4", "30 : 4 − 6",
                     "30 − (6 : 4)"],
         "pareizi": 0, "padoms": "Vispirms atņem apēstos."},
        {"jaut": "«5 kastes pa 8 olām, 3 olas saplīsa.»",
         "opcijas": ["5 · 8 − 3", "(5 · 8) − (3 · 8)", "5 · (8 − 3)",
                     "5 + 8 − 3"],
         "pareizi": 0, "padoms": "Vispirms izrēķina visas olas."},
        {"jaut": "«Katrā no 5 kastēm bija 8 olas, no katras izņēma 3.»",
         "opcijas": ["5 · (8 − 3)", "5 · 8 − 3", "5 − 8 · 3", "(5 − 3) · 8"],
         "pareizi": 0, "padoms": "Vispirms izrēķina, cik palika vienā kastē."},
        {"jaut": "Kad iekavas nav vajadzīgas?",
         "opcijas": ["Kad pirmā darbība jau ir reizināšana",
                     "Nekad", "Vienmēr", "Kad skaitļi ir mazi"],
         "pareizi": 0, "padoms": "Reizināšanu izpilda pirmo arī bez iekavām."},
    ], pamats=4),

    Pasaule("Cik vietas paliek telefonā?",
            Ievadi("", [
                {"jaut": "Bija 60 MB brīvi, lejupielādēja 4 failus pa 9 MB. "
                         "Cik palika? (60 − 4 · 9)",
                 "atb": ["24"], "padoms": "Vispirms 4 · 9 = 36."},
                {"jaut": "Mapē bija 15 MB un 25 MB, to sadalīja 8 daļās. "
                         "((15 + 25) : 8)",
                 "atb": ["5"], "padoms": "Vispirms iekavas."},
                {"jaut": "7 attēli pa 4 MB un vēl 12 MB video. (7 · 4 + 12)",
                 "atb": ["40"], "padoms": "Vispirms 7 · 4."},
                {"jaut": "No 5 mapēm pa 12 MB izdzēsa pa 2 MB. (5 · (12 − 2))",
                 "atb": ["50"], "padoms": "Vispirms iekavas."},
            ]),
            pavediens="dati",
            konteksts="Telefona atmiņas rēķinā iekavas pasaka, vai dzēš no "
                      "katras mapes vai tikai vienu reizi.",
            kapec="Viena iekava maina atbildi par desmitiem megabaitu."),

    Kopsavilkums([
        "Pierakstu divu darbību risinājumu kā vienu izteiksmi.",
        "Zinu, kad vajadzīgas iekavas un kad ne.",
        "Aprēķinu izteiksmi, ievērojot darbību secību.",
        "Salīdzinu izteiksmes ar iekavām un bez tām.",
    ]),

    Majas([
        "Pieraksti kā izteiksmi: «bija 50 ct, nopirka 3 preces pa 12 ct».",
        "Aprēķini (14 + 6) · 3 un 14 + 6 · 3 un salīdzini atbildes.",
        "Izdomā uzdevumu, kuram vajadzīgas iekavas.",
    ]),
]
