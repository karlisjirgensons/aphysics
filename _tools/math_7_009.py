# -*- coding: utf-8 -*-
"""7. klase, 9. stunda: «Ar ko izlase atšķiras no apakškopas?»

Apakškopā secība nav svarīga: {a; b} = {b; a}. Izlasē (sakārtotā
izvēlē) secība ir svarīga: pirmā vieta un otrā vieta nav viens un tas pats.
Tāpēc izlašu vienmēr ir vairāk nekā apakškopu ar tikpat elementiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Ar ko izlase atšķiras no apakškopas?"

MERKIS = ("Noskaidrosim, kad izvēlē svarīga ir secība, un salīdzināsim "
          "izlases ar apakškopām.")

SATURS = [
    Sakums("Kapteinis un vietnieks vai divi dežuranti?",
           fakti=["Anna - kapteine, Pēteris - vietnieks: tas nav tas pats, "
                  "kas otrādi.",
                  "Anna un Pēteris - dežuranti: secība nav svarīga.",
                  "Pirmajā gadījumā ir izlase, otrajā - apakškopa."]),

    Doma("Izlasē secība ir svarīga",
         "Apakškopā elementu secība nav svarīga: {A; P} = {P; A}. Izlasē "
         "secība ir svarīga: (A; P) un (P; A) ir divas dažādas izlases.",
         soli=[
             "Jautā: ja divus izvēlētos samaina vietām, vai kaut kas "
             "mainās?",
             "Mainās (lomas, vietas, cipari skaitlī) - izlase.",
             "Nemainās (grupa, komanda, dāvanu komplekts) - apakškopa.",
             "Izlasi raksta apaļajās iekavās, apakškopu - figūriekavās.",
         ],
         pieze="Katrai apakškopai ar 2 elementiem atbilst 2 izlases - "
               "abās secībās. Tāpēc izlašu ir divreiz vairāk."),

    Paraugs("Viena grupa - divi jautājumi",
            uzd="No Annas, Bena un Cīrules izvēlas divus. a) Cik dažādu "
                "dežurantu pāru? b) Cik dažādu pāru «kapteinis un vietnieks»?",
            soli=[
                ("a) {A; B}, {A; C}, {B; C}",
                 "Secība nav svarīga - 3 apakškopas."),
                ("b) (A; B), (B; A), (A; C), (C; A), (B; C), (C; B)",
                 "Katram pārim divas secības."),
                ("3 · 2 = 6", "Kapteini izvēlas 3 veidos, vietnieku - 2."),
            ],
            atbilde="a) 3 pāri; b) 6 izlases"),

    Zimejums("Apakškopas pret izlasēm",
             restis([["apakškopa", "izlases"],
                     ["{A; B}", "(A; B), (B; A)"],
                     ["{A; C}", "(A; C), (C; A)"],
                     ["{B; C}", "(B; C), (C; B)"]]),
             paskaidro="Katrai apakškopai - divas izlases."),

    Varianti("Izlase vai apakškopa?", [
        {"jaut": "No 10 skrējējiem nosaka 1., 2. un 3. vietu.",
         "opcijas": ["Izlase - secība svarīga",
                     "Apakškopa - secība nav svarīga"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Zelts un bronza nav viens un tas pats."},
        {"jaut": "No 10 skolēniem izvēlas 3 uz ekskursiju.",
         "opcijas": ["Izlase - secība svarīga",
                     "Apakškopa - secība nav svarīga"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Visi trīs brauc vienādi."},
        {"jaut": "No cipariem 1-9 veido divciparu skaitli.",
         "opcijas": ["Izlase - secība svarīga",
                     "Apakškopa - secība nav svarīga"],
         "pareizi": 0, "jaukt": False,
         "padoms": "47 nav 74."},
        {"jaut": "No 6 augļiem izvēlas 2 smūtijam.",
         "opcijas": ["Izlase - secība svarīga",
                     "Apakškopa - secība nav svarīga"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Blenderis sajauc visu vienādi."},
    ], pamats=4),

    Ievadi("Saskaiti", [
        {"jaut": "No 4 skolēniem izvēlas kapteini un vietnieku. Cik "
                 "veidos?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "No 4 skolēniem izvēlas 2 dežurantus. Cik veidos?",
         "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "No 5 grāmatām noliek 2 plauktā vienu blakus otrai. "
                 "Cik veidos?",
         "atb": ["20"], "padoms": "5 · 4 - secība plauktā ir svarīga."},
        {"jaut": "No 5 grāmatām paņem 2 līdzi atvaļinājumā. Cik veidos?",
         "atb": ["10"], "padoms": "20 : 2."},
    ]),

    Pasaule("Konkursa uzvarētāji",
            Ievadi("", [
                {"jaut": "Robotikas sacensībās ir 6 komandas. Cik dažādos "
                         "veidos var sadalīt zelta un sudraba medaļu?",
                 "atb": ["30"], "padoms": "6 · 5."},
                {"jaut": "Divas labākās komandas brauc uz finālu Tallinā "
                         "(bez vietām). Cik dažādu pāru?",
                 "atb": ["15"], "padoms": "30 : 2."},
                {"jaut": "Cik veidos var sadalīt zeltu, sudrabu un bronzu?",
                 "atb": ["120"], "padoms": "6 · 5 · 4."},
            ]),
            pavediens="tehnika",
            konteksts="Sacensībās medaļas ir izlase, bet fināla komandas - "
                      "apakškopa.",
            kapec="Viens jautājums «vai secība svarīga?» maina atbildi divas "
                  "reizes."),

    Kopsavilkums([
        "Atšķiru izlasi (secība svarīga) no apakškopas.",
        "Izlasi rakstu apaļajās iekavās: (A; B).",
        "Zinu, ka divu elementu izlašu ir divreiz vairāk nekā apakškopu.",
        "Jautāju: vai samainot kaut kas mainās?",
    ]),

    Majas([
        "Izdomā divas situācijas: vienu ar izlasi, otru ar apakškopu.",
        "No 5 draugiem izvēlies 2: cik veidos, ja secība ir/nav svarīga?",
        "Kāpēc tālruņa numurs ir izlase, nevis apakškopa?",
    ]),
]
