# -*- coding: utf-8 -*-
"""8. klase, 28. stunda: «Kā skaitli pierakstīt kā pakāpi?»

Otrādi nekā līdz šim: dots skaitlis, jāatrod bāze un kāpinātājs. Rīks ir
sadalīšana pirmreizinātājos. Viens skaitlis var būt vairākas pakāpes
(64 = 2^6 = 4^3 = 8^2), un to izmanto, lai pakāpes ar dažādām bāzēm
pārvērstu par pakāpēm ar vienu bāzi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kā skaitli pierakstīt kā pakāpi?"

MERKIS = ("Pierakstīsim skaitli vai reizinājumu kā pakāpi, ja tas iespējams.")

SATURS = [
    Sakums("64 - trīs dažādas pakāpes",
           zimejums=restis([["2⁶", "4³", "8²"],
                            ["64", "64", "64"]]),
           paraksts="Viens skaitlis - trīs pieraksti.",
           fakti=["4³ = (2²)³ = 2⁶.",
                  "8² = (2³)² = 2⁶.",
                  "Pakāpi atrod, sadalot skaitli pirmreizinātājos."]),

    Doma("No skaitļa uz pakāpi",
         "Lai skaitli pierakstītu kā pakāpi, to sadala pirmreizinātājos un "
         "saskaita vienādos.",
         soli=[
             "Dali ar mazāko pirmskaitli, kamēr dalās.",
             "Saskaiti, cik reižu parādās katrs pirmskaitlis.",
             "Ja ir tikai viens pirmskaitlis - tā ir pakāpe: 243 = 3^5.",
             "Ja vairāki - reizinājums: 72 = 2^3 · 3^2.",
             "Daļa ar 1 skaitītājā - negatīvs kāpinātājs: {1|8} = 2^−3.",
         ],
         pieze="Decimāldaļas ar 1 un nullēm ir 10 pakāpes: 0,0001 = 10^−4."),

    Paraugs("Sadali pirmreizinātājos",
            uzd="Pieraksti 243, 72 un 0,008 ar pakāpēm.",
            soli=[
                ("243 = 3 · 81 = 3 · 3^4 = 3^5", "Tikai trijnieki."),
                ("72 = 8 · 9 = 2^3 · 3^2", "Divi pirmskaitļi."),
                ("0,008 = {8|1000} = {2^3|10^3} = ({1|5})^3 = 5^−3",
                 "0,008 = 0,2^3."),
            ],
            atbilde="3^5; 2^3 · 3^2; 5^−3"),

    Zimejums("Dalīšanas kāpnes",
             restis([["72", "2"], ["36", "2"], ["18", "2"], ["9", "3"],
                     ["3", "3"], ["1", ""]]),
             paskaidro="Labajā kolonnā - trīs divnieki un divi trijnieki: "
                       "72 = 2³ · 3²."),

    Ievadi("Pieraksti kā pakāpi", [
        {"jaut": "128 = 2^?", "atb": ["7"], "padoms": "2^7 = 128."},
        {"jaut": "81 = 3^?", "atb": ["4"], "padoms": "9 · 9."},
        {"jaut": "{1|25} = 5^?", "atb": ["−2", "-2"], "padoms": "{1|5^2}."},
        {"jaut": "0,001 = 10^?", "atb": ["−3", "-3"], "padoms": "{1|1000}."},
        {"jaut": "27^2 = 3^?", "atb": ["6"], "padoms": "(3^3)^2."},
        {"jaut": "8 · 32 = 2^?", "atb": ["8"], "padoms": "2^3 · 2^5."},
    ], pamats=4),

    Varianti("Viena bāze", [
        {"jaut": "4^5 ar bāzi 2 ir...",
         "opcijas": ["2^{10}", "2^7", "2^5", "2^{20}"],
         "pareizi": 0, "padoms": "(2^2)^5."},
        {"jaut": "{1|9} ar bāzi 3 ir...",
         "opcijas": ["3^−2", "3^2", "−3^2", "3^−3"],
         "pareizi": 0, "padoms": "{1|3^2}."},
        {"jaut": "Kuru skaitli nevar pierakstīt kā pakāpi ar naturālu bāzi "
                 "un kāpinātāju > 1?",
         "opcijas": ["12", "16", "27", "25"],
         "pareizi": 0, "padoms": "12 = 2^2 · 3."},
    ]),

    Pasaule("Šifri un atslēgas",
            Ievadi("", [
                {"jaut": "Kodu slēdzenei ir 3 riteņi ar cipariem 0-9: 10^3 "
                         "kombināciju. Cik?",
                 "atb": ["1000"], "padoms": "10 · 10 · 10."},
                {"jaut": "Parole no 4 simboliem, katram 32 iespējas. Cik "
                         "kombināciju ir 32^4? Pieraksti kā 2^?",
                 "atb": ["2^20", "2^{20}", "1048576"],
                 "padoms": "(2^5)^4.", "tastatura": "text"},
                {"jaut": "Cik tas ir skaitlī?",
                 "atb": ["1048576", "1 048 576"],
                 "padoms": "2^{10} · 2^{10} = 1024 · 1024."},
            ]),
            pavediens="kodi",
            konteksts="Paroles drošību mēra bitos: 32 iespējas ir 5 biti, "
                      "tāpēc 4 simboli dod 2^{20} kombināciju.",
            kapec="Pakāpe ar bāzi 2 parāda paroles stiprumu bitos."),

    Kopsavilkums([
        "Sadalu skaitli pirmreizinātājos un pierakstu ar pakāpēm.",
        "Pierakstu daļu ar negatīvu kāpinātāju.",
        "Pārveidoju pakāpi uz citu bāzi: 4^5 = 2^{10}.",
    ]),

    Majas([
        "Pieraksti kā pakāpi: 625, 1024, {1|49}, 0,00001.",
        "Sadali pirmreizinātājos 360 un pieraksti ar pakāpēm.",
        "Atrodi visus veidus, kā pierakstīt 729 kā pakāpi.",
    ]),
]
