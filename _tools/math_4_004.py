# -*- coding: utf-8 -*-
"""4. klase, 4. stunda: «Kā rēķinu galvā un kā rakstos?»

Divi ceļi uz vienu atbildi. Galvā rēķina pa šķirām no lielākās, rakstos -
stabiņā no mazākās. Skolēns izmēģina abus un stāsta, kā rīkojās: 4.1.
tematā tie paši ceļi vedīs līdz 10 000.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā rēķinu galvā un kā rakstos?"

MERKIS = ("Saskaitīsim un atņemsim līdz 1000 gan galvā, gan rakstos un "
          "pastāstīsim, kā rīkojāmies.")

SATURS = [
    Sakums("Kurš ātrāk - galva vai zīmulis?",
           zimejums=restis([["", "galvā", "rakstos"],
                            ["300 + 400", "uzreiz", "lēni"],
                            ["387 + 459", "grūti", "droši"]],
                           "katram rēķinam savs ceļš"),
           paraksts="Vienkāršu rēķinu dari galvā, sarežģītu - stabiņā.",
           fakti=["Galvā rēķina pa šķirām: simti, desmiti, vieni.",
                  "Stabiņā sāk no vieniem un pārnes desmitus."]),

    Doma("Galvā - no lielākās šķiras, rakstos - no mazākās",
         "Abi ceļi saskaita tās pašas šķiras, tikai citā secībā.",
         soli=[
             "Galvā: 346 + 230 = 346 + 200 + 30 = 546 + 30 = 576.",
             "Rakstos: vienus zem vieniem, desmitus zem desmitiem.",
             "Stabiņā sāc ar vieniem; ja sanāk 10 vai vairāk, desmitu "
             "pārnes.",
             "Pastāsti skaļi, ko dari katrā solī.",
         ],
         pieze="Ja vienos sanāk 9 + 7 = 16, raksti 6, bet 1 desmitu pārnes uz "
               "desmitu stabiņu."),

    Paraugs("387 + 459 stabiņā",
            uzd="Saskaiti 387 + 459 rakstos.",
            soli=[
                ("7 + 9 = 16",
                 "Vienos raksta 6, 1 desmitu pārnes."),
                ("8 + 5 + 1 = 14",
                 "Desmitos raksta 4, 1 simtu pārnes."),
                ("3 + 4 + 1 = 8",
                 "Simtos raksta 8."),
                ("387 + 459 = 846", None),
            ],
            atbilde="846"),

    Slidnis("Galvā pa šķirām: 528 + 347",
            soli=[
                {"v": "528", "teksts": "Sākam ar pirmo skaitli.",
                 "josla": 60},
                {"v": "528 + 300 = 828", "teksts": "Pieskaita simtus.",
                 "josla": 94},
                {"v": "828 + 40 = 868", "teksts": "Pieskaita desmitus.",
                 "josla": 98},
                {"v": "868 + 7 = 875", "teksts": "Pieskaita vienus - gatavs.",
                 "josla": 100},
            ],
            ievads="Otro skaitli sadala šķirās un pieskaita pa vienai."),

    Ievadi("Rēķini, kā tev ērtāk", [
        {"jaut": "450 + 300 = ?", "atb": ["750"],
         "padoms": "Pieskaiti 3 simtus."},
        {"jaut": "623 + 254 = ?", "atb": ["877"],
         "padoms": "Šķiras nepārsniedz 9 - pārnest nevajag."},
        {"jaut": "478 + 365 = ?", "atb": ["843"],
         "padoms": "Vienos 13, desmitos 7 + 6 + 1 = 14."},
        {"jaut": "900 − 350 = ?", "atb": ["550"],
         "padoms": "900 − 300 = 600, 600 − 50."},
        {"jaut": "732 − 418 = ?", "atb": ["314"],
         "padoms": "No 2 nevar atņemt 8 - aizņemies desmitu."},
        {"jaut": "605 − 287 = ?", "atb": ["318"],
         "padoms": "Desmitu nav - sadali simtu."},
    ], pamats=4),

    Varianti("Kā tu to rēķinātu?", [
        {"jaut": "500 + 400 - galvā vai rakstos?",
         "opcijas": ["galvā", "rakstos"], "pareizi": 0,
         "padoms": "5 simti + 4 simti."},
        {"jaut": "Kur ir kļūda: 356 + 278 = 524?",
         "opcijas": ["aizmirsa pārnest desmitu",
                     "sajauca šķiras", "nav kļūdas"],
         "pareizi": 0,
         "padoms": "6 + 8 = 14 - vienu desmitu jāpārnes; pareizi 634."},
        {"jaut": "Ar ko sāk saskaitīšanu stabiņā?",
         "opcijas": ["ar vieniem", "ar simtiem", "ar desmitiem"],
         "pareizi": 0, "padoms": "No labās puses."},
        {"jaut": "Kā pārbaudīt 812 − 395 = 417?",
         "opcijas": ["417 + 395 = 812", "812 + 395", "417 − 395",
                     "812 − 417 − 395"],
         "pareizi": 0, "padoms": "Starpība plus atņēmējs dod mazināmo."},
    ], pamats=4),

    Pasaule("Cik soļu šodien?",
            Ievadi("", [
                {"jaut": "Līdz skolai ir 468 soļi. Cik soļu turp un atpakaļ?",
                 "atb": ["936"], "padoms": "468 + 468."},
                {"jaut": "Līdz veikalam - 285 soļi. Cik soļu ceļā uz skolu "
                         "un veikalu kopā?",
                 "atb": ["753"], "padoms": "468 + 285."},
                {"jaut": "Mērķis ir 1000 soļu. Cik trūkst pēc 753 soļiem?",
                 "atb": ["247"], "padoms": "1000 − 753."},
                {"jaut": "Par cik ceļš uz skolu ir garāks nekā uz veikalu?",
                 "atb": ["183"], "padoms": "468 − 285."},
            ]),
            pavediens="sports",
            konteksts="Soļu skaitītājs telefonā vai pulkstenī saskaita katru "
                      "soli - bet kopsummu izrēķini tu.",
            kapec="Stabiņš der tad, kad skaitļi ir neērti galvai."),

    Kopsavilkums([
        "Saskaitu un atņemu līdz 1000 galvā pa šķirām.",
        "Saskaitu un atņemu stabiņā ar pārnešanu.",
        "Izvēlos, kad rēķināt galvā un kad rakstos.",
        "Pārbaudu atņemšanu ar saskaitīšanu.",
    ]),

    Majas([
        "Saskaiti divu grāmatu lappušu skaitu vispirms galvā, tad stabiņā.",
        "Pastāsti mājiniekam, kā atņēmi 605 − 287.",
        "Izdomā vienu rēķinu, ko ērtāk darīt galvā, un vienu - rakstos.",
    ]),
]
