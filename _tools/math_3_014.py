# -*- coding: utf-8 -*-
"""3. klase, 14. stunda: «Kā skaitli uzrakstīt kā reizinājumu?»

Reizināšanas tabulu te lasa otrādi: nevis «cik ir 4 · 6», bet «no kā sastāv
24». Tas ir pirmais solis uz dalītājiem un vēlāk uz daļu saīsināšanu, un tas
pats uzdevums ģeometrijā nozīmē - cik dažādu taisnstūru var salikt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā skaitli uzrakstīt kā reizinājumu?"

MERKIS = ("Uzrakstīsim doto skaitli kā divu skaitļu reizinājumu vairākos "
          "veidos un pārliecināsimies, ka atradām visus.")

SATURS = [
    Sakums("Cik dažādus taisnstūrus var salikt no 12 rūtiņām?",
           zimejums=restis([["1 · 12", "2 · 6", "3 · 4"],
                            ["12 · 1", "6 · 2", "4 · 3"]],
                           "visi 12 sadalījumi"),
           paraksts="Katram reizinājumam atbilst viens taisnstūris.",
           fakti=["12 var uzrakstīt kā reizinājumu sešos veidos.",
                  "Bet dažādi taisnstūri ir tikai trīs - pārējie ir "
                  "pagriezti."]),

    Doma("Skaitli var sadalīt reizinātājos",
         "Uzrakstīt skaitli kā reizinājumu nozīmē atrast divus skaitļus, "
         "kuru reizinājums ir tieši šis skaitlis.",
         soli=[
             "Sāc ar 1: 1 reiz pats skaitlis vienmēr der.",
             "Pārbaudi 2: vai skaitlis ir pāra skaitlis?",
             "Tad 3, 4, 5 un tā tālāk - līdz reizinātāji satiekas.",
             "Kad otrais reizinātājs kļūst mazāks par pirmo, visi ir atrasti.",
         ],
         pieze="Skaitļus, kurus var uzrakstīt tikai kā 1 reiz pašu sevi, "
               "sauc par *pirmskaitļiem*: tādi ir 2, 3, 5, 7, 11, 13."),

    Paraugs("Kā uzrakstīt 18 kā reizinājumu?",
            uzd="Uzraksti 18 kā divu skaitļu reizinājumu visos veidos.",
            soli=[
                ("1 · 18",
                 "Pirmais vienmēr der."),
                ("2 · 9",
                 "18 ir pāra skaitlis, tātad dalās ar 2."),
                ("3 · 6",
                 "18 : 3 = 6 - arī der."),
                ("4 neder, 5 neder, 6 · 3 jau bija",
                 "Reizinātāji satikās, tātad visi ir atrasti."),
            ],
            atbilde="1 · 18, 2 · 9 un 3 · 6"),

    Ievadi("Atrodi otro reizinātāju", [
        {"jaut": "24 = 4 · ?", "atb": ["6"], "padoms": "24 : 4."},
        {"jaut": "42 = 6 · ?", "atb": ["7"], "padoms": "42 : 6."},
        {"jaut": "56 = 8 · ?", "atb": ["7"], "padoms": "56 : 8."},
        {"jaut": "45 = 9 · ?", "atb": ["5"], "padoms": "45 : 9."},
        {"jaut": "36 = 6 · ?", "atb": ["6"], "padoms": "Kvadrāts."},
        {"jaut": "63 = 7 · ?", "atb": ["9"], "padoms": "63 : 7."},
    ], pamats=4),

    Petijums("Saliec taisnstūrus no 24 rūtiņām",
             vajag="rūtiņu lapa un zīmulis",
             soli=[
                 "Uzzīmē visus taisnstūrus, kuros ir tieši 24 rūtiņas.",
                 "Pieraksti pie katra tā malu garumus kā reizinājumu.",
                 "Sakārto reizinājumus augošā secībā pēc pirmā skaitļa.",
                 "Pārliecinies, ka neviens nav aizmirsts.",
             ],
             secinajums="24 = 1 · 24 = 2 · 12 = 3 · 8 = 4 · 6 - četri "
                        "dažādi taisnstūri."),

    Zimejums("Kā aug un sarūk reizinātāji",
             restis([[1, 2, 3, 4, 6, 8, 12, 24],
                     [24, 12, 8, 6, 4, 3, 2, 1]],
                    "24 dalītāji pa pāriem"),
             paskaidro="Katram skaitlim augšējā rindā ir savs pāris apakšējā "
                       "rindā - un to reizinājums vienmēr ir 24.",
             ievads="Kad rindas satiekas vidū, visi pāri ir atrasti."),

    Varianti("Kurš sadalījums ir pareizs?", [
        {"jaut": "Kurš reizinājums dod 36?",
         "opcijas": ["4 · 9", "6 · 7", "5 · 7", "8 · 5"],
         "pareizi": 0, "padoms": "Pārbaudi katru ar tabulu."},
        {"jaut": "Kuru skaitli *nevar* uzrakstīt kā divu skaitļu "
                 "reizinājumu, kas abi lielāki par 1?",
         "opcijas": ["7", "8", "9", "10"],
         "pareizi": 0, "padoms": "7 ir pirmskaitlis."},
        {"jaut": "Cik dažādu taisnstūru var salikt no 16 rūtiņām?",
         "opcijas": ["3", "2", "4", "5"],
         "pareizi": 0, "padoms": "1 · 16, 2 · 8 un 4 · 4."},
        {"jaut": "Kurš skaitlis dalās gan ar 6, gan ar 9?",
         "opcijas": ["54", "45", "48", "63"],
         "pareizi": 0, "padoms": "54 : 6 = 9 un 54 : 9 = 6."},
    ], pamats=4),

    Pasaule("Kā salikt kastes noliktavā?",
            Ievadi("", [
                {"jaut": "48 kastes jāsaliek vienādās rindās pa 8. Cik "
                         "rindu sanāks?",
                 "atb": ["6"], "padoms": "48 : 8."},
                {"jaut": "Tās pašas 48 kastes saliek pa 6. Cik rindu?",
                 "atb": ["8"], "padoms": "48 : 6."},
                {"jaut": "Plauktā ietilpst 4 rindas. Cik kastu būs vienā "
                         "rindā, ja to ir 48?",
                 "atb": ["12"], "padoms": "48 : 4."},
                {"jaut": "Vai 48 kastes var salikt vienādās rindās pa 5? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "48 nedalās ar 5.",
                 "tastatura": "text"},
            ]),
            pavediens="tehnika",
            konteksts="Noliktavā kravu vienmēr saliek vienādās rindās - "
                      "citādi kastes neietilpst plauktā.",
            kapec="Reizinātāju meklēšana pasaka, kādi plaukti vispār der."),

    Kopsavilkums([
        "Uzrakstu skaitli kā divu skaitļu reizinājumu vairākos veidos.",
        "Pārbaudu pēc kārtas 1, 2, 3, 4, ... un zinu, kad apstāties.",
        "Saprotu, ka katram reizinājumam atbilst viens taisnstūris.",
        "Zinu, ka daži skaitļi dalās tikai ar 1 un sevi pašu.",
    ]),

    Majas([
        "Uzraksti visos veidos kā reizinājumu skaitļus 20, 30 un 32.",
        "Atrodi skaitli, ko var uzrakstīt vairāk nekā četros veidos.",
        "Uzzīmē visus taisnstūrus, kuros ir 18 rūtiņas.",
    ]),
]
