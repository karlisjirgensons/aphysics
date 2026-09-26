# -*- coding: utf-8 -*-
"""3. klase, 136. stunda: «Kā saskaitīt trīsciparu skaitļus galvā?»

Galvas rēķins ar decimālo sastāvu: simti pie simtiem, desmiti pie desmitiem,
vieni pie vieniem. Tas ir tas pats paņēmiens, kas 25. stundā strādāja ar
reizināšanu - skaitli sadala pa vietām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā saskaitīt trīsciparu skaitļus galvā?"

MERKIS = ("Saskaitīsim trīsciparu skaitļus galvā, izmantojot decimālo "
          "sastāvu.")

SATURS = [
    Sakums("Kā saskaitīt 342 un 215 bez papīra?",
           zimejums=restis([["", "S", "D", "V"],
                            [342, 300, 40, 2],
                            [215, 200, 10, 5]],
                           "abi skaitļi pa vietām"),
           paraksts="Simti pie simtiem, desmiti pie desmitiem.",
           fakti=["Galvā saskaita pa vietām, sākot ar simtiem.",
                  "Katru vietu saskaita atsevišķi un rezultātus apvieno."]),

    Doma("Saskaiti pa vietām, sākot ar lielākajām",
         "342 + 215 ir 300 + 200, tad 40 + 10, tad 2 + 5 - un rezultātus "
         "saliek kopā.",
         soli=[
             "Saskaiti simtus: 300 + 200 = 500.",
             "Saskaiti desmitus: 40 + 10 = 50.",
             "Saskaiti vienus: 2 + 5 = 7.",
             "Saliec kopā: 500 + 50 + 7 = 557.",
         ],
         pieze="Galvā ērtāk sākt ar simtiem: tad jau pēc pirmā soļa zini, "
               "cik apmēram sanāks, un kļūdu pamanīsi uzreiz."),

    Slidnis("Kā aug summa",
            soli=[
                {"v": "300 + 200 = 500", "teksts": "Simti.", "josla": 40},
                {"v": "+ 50 = 550", "teksts": "Desmiti.", "josla": 70},
                {"v": "+ 7 = 557", "teksts": "Vieni.", "josla": 100},
            ],
            ievads="Trīs soļi, un summa ir gatava."),

    Paraugs("Cik ir 342 + 215?",
            uzd="Izrēķini galvā 342 + 215.",
            soli=[
                ("300 + 200 = 500",
                 "Vispirms simti."),
                ("40 + 10 = 50",
                 "Tad desmiti."),
                ("2 + 5 = 7",
                 "Tad vieni."),
                ("500 + 50 + 7 = 557",
                 "Saliek kopā."),
            ],
            atbilde="557"),

    Ievadi("Saskaiti galvā", [
        {"jaut": "342 + 215 = ?", "atb": ["557"], "padoms": "500 + 50 + 7."},
        {"jaut": "251 + 324 = ?", "atb": ["575"], "padoms": "500 + 70 + 5."},
        {"jaut": "406 + 123 = ?", "atb": ["529"], "padoms": "500 + 20 + 9."},
        {"jaut": "530 + 240 = ?", "atb": ["770"], "padoms": "700 + 70."},
        {"jaut": "125 + 362 = ?", "atb": ["487"], "padoms": "400 + 80 + 7."},
        {"jaut": "604 + 205 = ?", "atb": ["809"], "padoms": "800 + 9."},
    ], pamats=4,
        ievads="Rēķini pa vietām un ieraksti tikai galīgo atbildi."),

    Zimejums("Saskaitīšana pa vietām",
             restis([["", "S", "D", "V"],
                     [342, 3, 4, 2],
                     [215, 2, 1, 5],
                     [557, 5, 5, 7]],
                    "katra vieta atsevišķi"),
             paskaidro="Katrā ailē cipari saskaitās atsevišķi - šeit neviena "
                       "vieta nepārplūst.",
             ievads="Tā izskatās saskaitīšana pa vietām."),

    Varianti("Cik sanāk?", [
        {"jaut": "Cik ir 231 + 145?",
         "opcijas": ["376", "386", "366", "276"],
         "pareizi": 0, "padoms": "300 + 70 + 6."},
        {"jaut": "Ar ko sākt, saskaitot galvā?",
         "opcijas": ["Ar simtiem", "Ar vieniem", "Ar desmitiem",
                     "Vienalga"],
         "pareizi": 0, "padoms": "Tad uzreiz zini aptuveno atbildi."},
        {"jaut": "Cik ir 450 + 320?",
         "opcijas": ["770", "750", "780", "670"],
         "pareizi": 0, "padoms": "700 + 70."},
        {"jaut": "Cik ir 502 + 306?",
         "opcijas": ["808", "818", "708", "888"],
         "pareizi": 0, "padoms": "800 + 8."},
    ], pamats=4),

    Pasaule("Cik kilometru divās dienās?",
            Ievadi("", [
                {"jaut": "Pirmajā dienā 342 km, otrajā 215 km. Cik kopā?",
                 "atb": ["557"], "padoms": "500 + 50 + 7."},
                {"jaut": "Trešajā dienā 231 km. Cik kopā trīs dienās?",
                 "atb": ["788"], "padoms": "557 + 231."},
                {"jaut": "Viss ceļš 900 km. Cik atlicis?", "atb": ["112"],
                 "padoms": "900 − 788."},
                {"jaut": "Vai atlikušo var nobraukt vienā dienā, ja vidēji "
                         "brauc 260 km? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "112 < 260.",
                 "tastatura": "text"},
            ]),
            pavediens="celojums",
            konteksts="Ceļojuma laikā attālumus saskaita galvā - navigators "
                      "rāda tikai atlikušo ceļu.",
            kapec="Pa vietām saskaitot, summu var pateikt dažās sekundēs."),

    Kopsavilkums([
        "Saskaitu trīsciparu skaitļus galvā.",
        "Sadalu skaitļus simtos, desmitos un vienos.",
        "Sāku ar simtiem un salieku rezultātus kopā.",
        "Pamanu kļūdu jau pēc pirmā soļa.",
    ]),

    Majas([
        "Izrēķini galvā 321 + 254, 430 + 260 un 505 + 304.",
        "Pārbaudi atbildes ar kalkulatoru.",
        "Saskaiti divas cenas no mājas čeka galvā.",
    ]),
]
