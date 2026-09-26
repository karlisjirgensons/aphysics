# -*- coding: utf-8 -*-
"""3. klase, 130. stunda: «Kurš skaitlis ir lielāks?»

Salīdzināšanas noteikums ir īss: vispirms ciparu skaits, tad cipari no
kreisās puses. Svarīgākais te nav pats noteikums, bet tā *secība* - 98 ir
mazāks par 100, kaut sākas ar deviņnieku.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kurš skaitlis ir lielāks?"

MERKIS = ("Salīdzināsim divus trīsciparu skaitļus un pierakstīsim "
          "salīdzinājumu ar «>» vai «<».")

SATURS = [
    Sakums("Kurš ir lielāks - 98 vai 100?",
           zimejums=restis([[98, "<", 100],
                            [463, ">", 458]],
                           "divi salīdzinājumi"),
           paraksts="Vispirms skatās ciparu skaitu, tad ciparus no kreisās.",
           fakti=["Skaitlis ar vairāk cipariem vienmēr ir lielāks.",
                  "Ja ciparu skaits vienāds, salīdzina no kreisās puses."]),

    Doma("Vispirms ciparu skaits, tad cipari no kreisās",
         "Ja abiem ciparu skaits vienāds, salīdzina pirmo ciparu; ja tie "
         "sakrīt - nākamo.",
         soli=[
             "Saskaiti ciparus abos skaitļos.",
             "Ja skaits atšķiras, lielāks ir tas, kuram ciparu vairāk.",
             "Ja skaits vienāds, salīdzini simtu ciparus.",
             "Ja tie sakrīt, ej uz desmitiem, tad uz vieniem.",
         ],
         pieze="Tāpēc 463 > 458: simti abiem ir 4, bet desmiti 6 un 5 - "
               "tālāk skatīties nav vajadzības."),

    Paraugs("Kurš skaitlis ir lielāks?",
            uzd="Salīdzini 463 un 458.",
            soli=[
                ("Abiem trīs cipari",
                 "Ciparu skaits vienāds."),
                ("Simti: 4 un 4",
                 "Vienādi, ejam tālāk."),
                ("Desmiti: 6 > 5",
                 "Tātad 463 > 458."),
            ],
            atbilde="463 > 458"),

    Ievadi("Salīdzini skaitļus", [
        {"jaut": "Kurš skaitlis ir lielāks: 463 vai 458? Ieraksti lielāko.",
         "atb": ["463"], "padoms": "Desmiti: 6 > 5."},
        {"jaut": "Kurš ir lielāks: 98 vai 100? Ieraksti lielāko.",
         "atb": ["100"], "padoms": "Trīs cipari pret diviem."},
        {"jaut": "Kurš ir lielāks: 507 vai 570? Ieraksti lielāko.",
         "atb": ["570"], "padoms": "Desmiti: 7 > 0."},
        {"jaut": "Kurš ir mazāks: 319 vai 391? Ieraksti mazāko.",
         "atb": ["319"], "padoms": "Desmiti: 1 < 9."},
        {"jaut": "Par cik 463 ir lielāks par 458?", "atb": ["5"],
         "padoms": "463 − 458."},
        {"jaut": "Kurš ir lielāks: 900 vai 899? Ieraksti lielāko.",
         "atb": ["900"], "padoms": "Simti: 9 = 8? Nē, 9 > 8."},
    ], pamats=4),

    Zimejums("Salīdzināšana pa vietām",
             restis([["", "S", "D", "V"],
                     ["463", 4, 6, 3],
                     ["458", 4, 5, 8]],
                    "salīdzina no kreisās"),
             paskaidro="Simti sakrīt, tāpēc izšķir desmiti - un vienus pat "
                       "nav jāskatās.",
             ievads="Abi skaitļi vietu tabulā."),

    Varianti("Kurš ir lielāks?", [
        {"jaut": "Kurš skaitlis ir lielākais?",
         "opcijas": ["901", "899", "890", "109"],
         "pareizi": 0, "padoms": "Simti: 9, 8, 8, 1."},
        {"jaut": "Kurš skaitlis ir mazākais?",
         "opcijas": ["207", "270", "702", "720"],
         "pareizi": 0, "padoms": "Simti un desmiti."},
        {"jaut": "Ko salīdzina vispirms?",
         "opcijas": ["Ciparu skaitu", "Pēdējo ciparu",
                     "Ciparu summu", "Vidējo ciparu"],
         "pareizi": 0, "padoms": "Vairāk ciparu - lielāks skaitlis."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["99 < 100", "99 > 100", "99 = 100", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Divi cipari pret trim."},
    ], pamats=4),

    Pasaule("Kura planēta ir tālāk?",
            Ievadi("", [
                {"jaut": "Mēness ir 384 tūkstošus km tālu, Venera tuvākajā "
                         "vietā 41 miljonu km. Kurš skaitlis ir lielāks - "
                         "384 vai 41? Ieraksti lielāko.",
                 "atb": ["384"], "padoms": "Trīs cipari pret diviem."},
                {"jaut": "Kosmosa kuģis nolidoja 463 km, otrs 458 km. Par "
                         "cik kilometriem pirmais nolidoja vairāk?",
                 "atb": ["5"], "padoms": "463 − 458."},
                {"jaut": "Cik kilometru abi nolidoja kopā?", "atb": ["921"],
                 "padoms": "463 + 458."},
                {"jaut": "Trešais nolidoja 500 km. Cik kilometru visi trīs?",
                 "atb": ["1421"], "padoms": "921 + 500."},
            ]),
            pavediens="kosmoss",
            konteksts="Kosmosā attālumus vienmēr salīdzina - tikai tā var "
                      "izvēlēties, kurp lidot vispirms.",
            kapec="Salīdzinot skaitļus, jāskatās arī mērvienība: 384 tūkstoši "
                  "un 41 miljons nav salīdzināmi tieši."),

    Kopsavilkums([
        "Salīdzinu divus trīsciparu skaitļus.",
        "Vispirms salīdzinu ciparu skaitu.",
        "Tad salīdzinu ciparus no kreisās puses.",
        "Pierakstu salīdzinājumu ar «>» vai «<».",
    ]),

    Majas([
        "Salīdzini 604 un 640, 199 un 201, 888 un 880.",
        "Pieraksti katram salīdzinājuma zīmi.",
        "Atrodi divus skaitļus, kuri atšķiras tikai ar pēdējo ciparu.",
    ]),
]
