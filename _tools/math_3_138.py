# -*- coding: utf-8 -*-
"""3. klase, 138. stunda: «Kad rodas jauns simts?»

Pāreja jeb pārnesums - tas, kas atšķir vieglo saskaitīšanu no īstās. Modelis
ir skaidrs: desmit vieni kļūst par vienu desmitu un pārceļas nākamajā
kolonnā. Tā ir tā pati doma, kas 134. stundā bija ar 999 + 1.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kad rodas jauns simts?"

MERKIS = ("Saskaitīsim ar pāreju jaunā desmitā un simtā un modelēsim to.")

SATURS = [
    Sakums("Kas notiek, ja vienu sanāk vairāk par desmit?",
           zimejums=restis([["", 1, 1, ""],
                            ["", 2, 6, 8],
                            ["+", 1, 5, 4],
                            ["", 4, 2, 2]],
                           "268 + 154"),
           paraksts="Mazie vieninieki virs kolonnām ir pārnesumi.",
           fakti=["Desmit vieni kļūst par vienu desmitu.",
                  "Desmit desmiti kļūst par vienu simtu."]),

    Doma("Desmit mazākās vienības kļūst par vienu lielāko",
         "Ja kolonnā sanāk 10 vai vairāk, desmitnieku pārnes nākamajā "
         "kolonnā pa kreisi.",
         soli=[
             "Saskaiti vienus: ja sanāk 10 vai vairāk, atdali desmitu.",
             "Vienu vietā pieraksti to, kas paliek pāri.",
             "Desmitu pārnes virs desmitu kolonnas.",
             "Saskaitot desmitus, neaizmirsti pārnesumu.",
         ],
         pieze="Pārnesums vienmēr ir tikai 1: pat 9 + 9 = 18 dod tikai vienu "
               "desmitu, jo divi cipari kopā nekad nedod 20."),

    Slidnis("Kā notiek pāreja",
            soli=[
                {"v": "8 + 4 = 12",
                 "teksts": "Vieni: raksta 2, pārnes 1.", "josla": 33},
                {"v": "6 + 5 + 1 = 12",
                 "teksts": "Desmiti: raksta 2, pārnes 1.", "josla": 66},
                {"v": "2 + 1 + 1 = 4",
                 "teksts": "Simti: atbilde ir 422.", "josla": 100},
            ],
            ievads="268 + 154 pa kolonnām."),

    Paraugs("Cik ir 268 + 154?",
            uzd="Saskaiti stabiņā 268 + 154.",
            soli=[
                ("8 + 4 = 12",
                 "Vienu vietā raksta 2, desmitu pārnes."),
                ("6 + 5 + 1 = 12",
                 "Desmitu vietā raksta 2, simtu pārnes."),
                ("2 + 1 + 1 = 4",
                 "Simtu vietā raksta 4; atbilde ir 422."),
            ],
            atbilde="422"),

    Ievadi("Saskaiti ar pāreju", [
        {"jaut": "268 + 154 = ?", "atb": ["422"], "padoms": "Divas pārejas."},
        {"jaut": "175 + 236 = ?", "atb": ["411"], "padoms": "5 + 6 = 11."},
        {"jaut": "347 + 285 = ?", "atb": ["632"], "padoms": "7 + 5 = 12."},
        {"jaut": "456 + 178 = ?", "atb": ["634"], "padoms": "6 + 8 = 14."},
        {"jaut": "129 + 91 = ?", "atb": ["220"], "padoms": "9 + 1 = 10."},
        {"jaut": "555 + 445 = ?", "atb": ["1000"], "padoms": "Visas vietas "
                                                             "pārplūst."},
    ], pamats=4),

    Zimejums("Kad pārnesuma nav",
             restis([["", 3, 4, 2],
                     ["+", 2, 1, 5],
                     ["", 5, 5, 7]],
                    "342 + 215 - bez pārejas"),
             paskaidro="Te neviena kolonna nepārsniedz 9, tāpēc pārnesumu "
                       "nav.",
             ievads="Salīdzini ar stundas sākuma zīmējumu."),

    Varianti("Kad rodas pārnesums?", [
        {"jaut": "Kad kolonnā rodas pārnesums?",
         "opcijas": ["Kad summa ir 10 vai vairāk", "Vienmēr",
                     "Kad summa ir mazāka par 10", "Nekad"],
         "pareizi": 0, "padoms": "Desmit mazākās kļūst par vienu lielāko."},
        {"jaut": "Cik liels var būt pārnesums?",
         "opcijas": ["1", "2", "10", "9"],
         "pareizi": 0, "padoms": "9 + 9 + 1 = 19."},
        {"jaut": "Cik ir 199 + 1?",
         "opcijas": ["200", "1910", "110", "290"],
         "pareizi": 0, "padoms": "Divas vietas pārplūst."},
        {"jaut": "Cik ir 268 + 132?",
         "opcijas": ["400", "390", "410", "300"],
         "pareizi": 0, "padoms": "8 + 2 = 10; 6 + 3 + 1 = 10."},
    ], pamats=4),

    Pasaule("Cik kilometru ir kopā?",
            Ievadi("", [
                {"jaut": "Posmi 268 km un 154 km. Cik kopā?", "atb": ["422"],
                 "padoms": "Ar divām pārejām."},
                {"jaut": "Vēl posms 178 km. Cik kopā?", "atb": ["600"],
                 "padoms": "422 + 178."},
                {"jaut": "Viss ceļš 750 km. Cik atlicis?", "atb": ["150"],
                 "padoms": "750 − 600."},
                {"jaut": "Cik kilometru ir turp un atpakaļ, ja ceļš ir "
                         "750 km?",
                 "atb": ["1500"], "padoms": "2 · 750."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojuma kilometri reti ir apaļi - tāpēc gandrīz "
                      "katrā saskaitīšanā ir pāreja.",
            kapec="Bez pārnesuma summa iznāk par mazu, un ceļš liekas "
                  "īsāks, nekā ir."),

    Kopsavilkums([
        "Saskaitu ar pāreju jaunā desmitā un simtā.",
        "Zinu, ka desmit vieni kļūst par vienu desmitu.",
        "Pierakstu pārnesumu virs nākamās kolonnas.",
        "Zinu, ka pārnesums vienmēr ir 1.",
    ]),

    Majas([
        "Izrēķini stabiņā 287 + 165 un 398 + 247.",
        "Atzīmē katrā piemērā, kur radās pārnesums.",
        "Atrodi divus trīsciparu skaitļus, kuru summa ir tieši 1000.",
    ]),
]
