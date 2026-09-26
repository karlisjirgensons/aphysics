# -*- coding: utf-8 -*-
"""3. klase, 11. stunda: «Kas notiek, reizinot ar 10?»

Reizināšana ar 10 ir pirmā likumsakarība, kas runā par ciparu *vietām*, nevis
par grupām: katrs cipars pārceļas vienu vietu pa kreisi, un tukšo vietu
aizpilda nulle. No šī noteikuma vēlāk aug gan reizināšana ar 100, gan mērogs
un metru pārrēķini 3.3. tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kas notiek, reizinot ar 10?"

MERKIS = ("Formulēsim likumsakarību par reizināšanu ar 10 un lietosim to "
          "aprēķinos.")

SATURS = [
    Sakums("Kāpēc 10 reizes vairāk ir tik viegli pierakstīt?",
           zimejums=restis([[3, 7, 12, 25],
                            [30, 70, 120, 250]],
                           "augšā skaitlis, apakšā tas pats reiz 10"),
           paraksts="Cipari paliek tie paši - klāt nāk tikai nulle.",
           fakti=["Mūsu skaitļu sistēmā katra nākamā vieta ir 10 reizes "
                  "lielāka.",
                  "Tāpēc reizināšana ar 10 ir vienkārši viena solis pa "
                  "kreisi."]),

    Doma("Reizinot ar 10, katrs cipars pārceļas vienu vietu pa kreisi",
         "Vieni kļūst par desmitiem, desmiti par simtiem - un brīvo vietu "
         "aizņem nulle.",
         soli=[
             "Paskaties, kurā vietā stāv katrs cipars.",
             "Pārcel katru ciparu vienu vietu pa kreisi.",
             "Vienu vietā ieraksti 0.",
             "Pārbaudi: atbildei jābūt tieši 10 reizes lielākai.",
         ],
         pieze="Nulle te nav «pierakstīta tāpat» - tā *tur vietu*, lai "
               "pārējie cipari paliktu tur, kur vajag."),

    Slidnis("Kā 4 kļūst par 4000",
            soli=[
                {"v": "4", "teksts": "Četri vieni.", "josla": 10},
                {"v": "4 · 10 = 40", "teksts": "Četri desmiti.", "josla": 35},
                {"v": "40 · 10 = 400", "teksts": "Četri simti.", "josla": 65},
                {"v": "400 · 10 = 4000", "teksts": "Četri tūkstoši.",
                 "josla": 100},
            ],
            ievads="Katrs solis reizina ar 10 - un pieliek vienu nulli."),

    Paraugs("Cik centimetru ir 7 decimetros?",
            uzd="Vienā decimetrā ir 10 cm. Cik centimetru ir 7 dm?",
            soli=[
                ("1 dm = 10 cm",
                 "Vispirms pieraksta to, ko zina par mērvienībām."),
                ("7 · 10 = 70",
                 "Septiņas desmitnieku grupas; ciparam 7 pieliek nulli."),
                ("7 dm = 70 cm",
                 "Atbildi raksta kopā ar mērvienību."),
            ],
            atbilde="70 cm"),

    Ievadi("Reizini ar 10", [
        {"jaut": "6 · 10 = ?", "atb": ["60"], "padoms": "Pieliec nulli."},
        {"jaut": "12 · 10 = ?", "atb": ["120"], "padoms": "Pieliec nulli."},
        {"jaut": "10 · 9 = ?", "atb": ["90"], "padoms": "Vienalga, kurā "
                                                        "pusē stāv 10."},
        {"jaut": "35 · 10 = ?", "atb": ["350"], "padoms": "Pieliec nulli."},
        {"jaut": "70 : 10 = ?", "atb": ["7"], "padoms": "Noņem nulli."},
        {"jaut": "240 : 10 = ?", "atb": ["24"], "padoms": "Noņem nulli."},
    ], pamats=4),

    Zimejums("Vietas nosaukumi",
             restis([["simti", "desmiti", "vieni"],
                     ["", "5", "0"],
                     ["5", "0", "0"]],
                    "50 un 500"),
             paskaidro="Reizinot ar 10, piecinieks pārcēlās no desmitu "
                       "vietas uz simtu vietu.",
             ievads="Skaties, kur atrodas cipars 5."),

    Varianti("Kur likumsakarība der?", [
        {"jaut": "Cik ir 10 · 10?",
         "opcijas": ["100", "20", "110", "1000"],
         "pareizi": 0, "padoms": "Desmit desmiti."},
        {"jaut": "Kurš apgalvojums ir pareizs?",
         "opcijas": ["Reizinot ar 10, cipari nemainās",
                     "Reizinot ar 10, katrs cipars kļūst lielāks par 10",
                     "Reizinot ar 10, atbilde ir par 10 lielāka",
                     "Reizinot ar 10, pēdējais cipars nozūd"],
         "pareizi": 0, "padoms": "Mainās tikai ciparu vietas."},
        {"jaut": "Cik metru ir 8 dekametros, ja 1 dam = 10 m?",
         "opcijas": ["80 m", "18 m", "800 m", "8 m"],
         "pareizi": 0, "padoms": "8 · 10."},
        {"jaut": "Skaitlis reizināts ar 10 dod 450. Kāds bija skaitlis?",
         "opcijas": ["45", "4500", "440", "55"],
         "pareizi": 0, "padoms": "Noņem vienu nulli."},
    ], pamats=4),

    Pasaule("Cik tālu tiek drons?",
            Ievadi("", [
                {"jaut": "Drons lido 10 m sekundē. Cik metru tas nolidos "
                         "7 sekundēs?",
                 "atb": ["70"], "padoms": "7 · 10."},
                {"jaut": "Cik metru tas nolidos 25 sekundēs?",
                 "atb": ["250"], "padoms": "25 · 10."},
                {"jaut": "Drons nolidoja 90 m. Cik sekundes tas lidoja?",
                 "atb": ["9"], "padoms": "90 : 10."},
                {"jaut": "Otrs drons lido 10 reizes ātrāk par gājēju, kas "
                         "iet 6 m sekundē. Cik metru sekundē lido drons?",
                 "atb": ["60"], "padoms": "6 · 10."},
            ]),
            pavediens="tehnika",
            konteksts="Dronu ātrumu mēra metros sekundē, un apaļi desmiti "
                      "padara aprēķinu gandrīz mutisku.",
            kapec="Ar desmitnieku likumsakarību attālumu var pateikt uzreiz, "
                  "bez papīra."),

    Kopsavilkums([
        "Zinu, kas notiek ar cipariem, reizinot ar 10.",
        "Reizinu un dalu ar 10 bez pieraksta stabiņā.",
        "Zinu, ka nulle tur vietu, nevis stāv tāpat.",
        "Lietoju šo likumsakarību mērvienību pārrēķinos.",
    ]),

    Majas([
        "Izrēķini, cik centimetru ir tavā augumā, ja to pasaki decimetros.",
        "Uzraksti piecus skaitļus un blakus tos pašus, reizinātus ar 10.",
        "Atrodi mājās iepakojumu, uz kura rakstīts skaitlis ar nulli galā.",
    ]),
]
