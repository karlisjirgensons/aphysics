# -*- coding: utf-8 -*-
"""3. klase, 9. stunda: «Kā reizināšana ar 8 saistās ar reizināšanu ar 4?»

Astotnieku rindu neiegaumē atsevišķi - to iegūst, dubultojot četrinieku
rindu. Tas ir tas pats paņēmiens, kas jau strādāja ar 6, tikai tagad solis
nav saskaitīšana, bet dubultošana; vēlāk no tās aug reizināšana ar 16 un 32.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā reizināšana ar 8 saistās ar reizināšanu ar 4?"

MERKIS = ("Iegūsim reizinājumus ar 8, dubultojot reizinājumus ar 4, un "
          "pierakstīsim visu astotnieku rindu.")

SATURS = [
    Sakums("Kā dators skaita ar 8?",
           zimejums=restis([[4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
                            [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]],
                           "augšā 4 ·, apakšā 8 ·"),
           paraksts="Katrs apakšējais skaitlis ir tieši divreiz lielāks.",
           fakti=["Datoros gandrīz viss skaitās pa 8: baits ir 8 biti.",
                  "8 ir divi reiz 4, tāpēc astotnieku rinda ir dubultota "
                  "četrinieku rinda."]),

    Doma("Astoņas grupas ir četras grupas, ņemtas divreiz",
         "8 · a = 2 · (4 · a) - tāpēc astotnieku rindu iegūst, dubultojot "
         "četrinieku rindu.",
         soli=[
             "Izrēķini 4 · a - četrinieku rindu tu zini.",
             "Dubulto rezultātu, tas ir, pieskaiti to pašu vēlreiz.",
             "Sanākusī atbilde ir 8 · a.",
             "Pārbaudi: astotnieku rindas skaitļi vienmēr ir pāra skaitļi.",
         ],
         pieze="Dubultot var arī divreiz pēc kārtas: 8 · a ir 2 · 2 · 2 · a. "
               "Tāpēc 8 · 7 = 7 → 14 → 28 → 56."),

    Slidnis("No 7 līdz 56 trijos dubultojumos",
            soli=[
                {"v": "7", "teksts": "Sākam ar pašu skaitli.", "josla": 12},
                {"v": "2 · 7 = 14", "teksts": "Pirmais dubultojums.",
                 "josla": 25},
                {"v": "4 · 7 = 28", "teksts": "Otrais dubultojums.",
                 "josla": 50},
                {"v": "8 · 7 = 56", "teksts": "Trešais dubultojums - gatavs!",
                 "josla": 100},
            ],
            ievads="Trīs reizes pa divi ir astoņi. Spied soļus."),

    Paraugs("Cik ir 8 · 9?",
            uzd="Izrēķini 8 · 9, izmantojot četrinieku rindu.",
            soli=[
                ("4 · 9 = 36",
                 "Četrinieku rindu proti no otrās klases."),
                ("36 + 36 = 72",
                 "Dubulto - tās ir astoņas grupas."),
                ("8 · 9 = 72",
                 "Pārbaude: 72 : 8 = 9 - sakrīt."),
            ],
            atbilde="72"),

    Ievadi("Dubulto četrinieku rindu", [
        {"jaut": "4 · 6 = 24. Cik ir 8 · 6?", "atb": ["48"],
         "padoms": "24 + 24."},
        {"jaut": "4 · 7 = 28. Cik ir 8 · 7?", "atb": ["56"],
         "padoms": "28 + 28."},
        {"jaut": "4 · 8 = 32. Cik ir 8 · 8?", "atb": ["64"],
         "padoms": "32 + 32."},
        {"jaut": "4 · 5 = 20. Cik ir 8 · 5?", "atb": ["40"],
         "padoms": "20 + 20."},
        {"jaut": "4 · 10 = 40. Cik ir 8 · 10?", "atb": ["80"],
         "padoms": "40 + 40."},
        {"jaut": "4 · 3 = 12. Cik ir 8 · 3?", "atb": ["24"],
         "padoms": "12 + 12."},
    ], pamats=4),

    Zimejums("Astotnieku rinda",
             restis([[8, 16, 24, 32, 40],
                     [48, 56, 64, 72, 80]],
                    "no 8 līdz 80"),
             paskaidro="Visi šie skaitļi ir pāra skaitļi, un katrs ir par 8 "
                       "lielāks nekā iepriekšējais.",
             ievads="Šī ir rinda, kas tev jāzina līdz temata beigām."),

    Varianti("Vai dubultojums ir pareizs?", [
        {"jaut": "Kā no 4 · 6 iegūt 8 · 6?",
         "opcijas": ["Rezultātu dubulto", "Rezultātam pieskaita 6",
                     "Rezultātam pieskaita 4", "Rezultātu reizina ar 4"],
         "pareizi": 0, "padoms": "8 ir divreiz vairāk nekā 4."},
        {"jaut": "Kurš skaitlis *nav* astotnieku rindā?",
         "opcijas": ["44", "48", "56", "64"],
         "pareizi": 0, "padoms": "44 : 8 nav vesels skaitlis."},
        {"jaut": "Cik ir 8 · 8?",
         "opcijas": ["64", "56", "72", "16"],
         "pareizi": 0, "padoms": "32 + 32."},
        {"jaut": "Cik astotnieku grupu ir 40?",
         "opcijas": ["5", "4", "8", "6"],
         "pareizi": 0, "padoms": "40 : 8."},
    ], pamats=4),

    Pasaule("Cik riteņu ir robotu rūpnīcā?",
            Ievadi("", [
                {"jaut": "Vienam noliktavas robotam ir 8 riteņi. Cik riteņu "
                         "ir 6 robotiem?",
                 "atb": ["48"], "padoms": "6 · 8."},
                {"jaut": "Cik riteņu ir 9 robotiem?",
                 "atb": ["72"], "padoms": "9 · 8."},
                {"jaut": "Noliktavā saskaitīja 64 riteņus. Cik robotu tur "
                         "strādā?",
                 "atb": ["8"], "padoms": "64 : 8."},
                {"jaut": "Katrs robots paceļ 8 kastes reizē. Cik kastu "
                         "pacels 7 roboti?",
                 "atb": ["56"], "padoms": "7 · 8."},
            ]),
            pavediens="tehnika",
            konteksts="Noliktavu roboti brauc pa taisnām rindām un ceļ "
                      "vienādas kastes - viss tur ir vienādās grupās.",
            kapec="Ja grupas ir vienādas, rūpnīcas darbu var izrēķināt "
                  "iepriekš."),

    Kopsavilkums([
        "Iegūstu reizinājumus ar 8, dubultojot reizinājumus ar 4.",
        "Zinu visu astotnieku rindu no 8 līdz 80.",
        "Zinu, ka 8 · a var iegūt, trīs reizes dubultojot a.",
        "Pārbaudu atbildi ar dalīšanu.",
    ]),

    Majas([
        "Uzraksti četrinieku rindu un blakus - dubultoto astotnieku rindu.",
        "Dubulto trīs reizes skaitli 6 un pārbaudi, vai sanāk 8 · 6.",
        "Saskaiti, cik riteņu ir visiem transportlīdzekļiem jūsu pagalmā.",
    ]),
]
