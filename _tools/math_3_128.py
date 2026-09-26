# -*- coding: utf-8 -*-
"""3. klase, 128. stunda: «Kā izlasīt un uzrakstīt lielu skaitli?»

Temats par rēķināšanu 1000 apjomā sākas ar pierakstu. 62. stundā skaitļus
lasīja no vietu tabulas; te pievienojas raksts vārdiem, kur kļūdas rodas
citur - «trīs simti piecpadsmit» un «trīs simti piecdesmit» izskatās līdzīgi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izlasīt un uzrakstīt lielu skaitli?"

MERKIS = ("Lasīsim un rakstīsim skaitļus līdz 1000 ar cipariem un vārdiem.")

SATURS = [
    Sakums("Cik dienu ilgst lidojums līdz Marsam?",
           zimejums=restis([["simti", "desmiti", "vieni"],
                            [2, 1, 0]],
                           "210 dienas"),
           paraksts="Divi simti desmit - desmitu vietā ir 1, vienu vietā 0.",
           fakti=["Līdz Marsam kuģis lido apmēram 210 dienas.",
                  "Trīsciparu skaitlī ir simti, desmiti un vieni."]),

    Doma("Lasi no lielākās vietas uz mazāko",
         "Vispirms nosauc simtus, tad desmitus, tad vienus - un nulles "
         "vietas izlaid.",
         soli=[
             "Pieraksti skaitli vietu tabulā.",
             "Nosauc simtu ciparu un vārdu «simti».",
             "Nosauc desmitus un vienus.",
             "Ja vietā ir 0, to nenosauc.",
         ],
         pieze="Uzmanīgi ar skaitļiem no 11 līdz 19: «trīs simti piecpadsmit» "
               "ir 315, bet «trīs simti piecdesmit» ir 350."),

    Paraugs("Kā uzrakstīt «seši simti septiņi»?",
            uzd="Pieraksti ar cipariem skaitli «seši simti septiņi».",
            soli=[
                ("Simtu vietā 6",
                 "Seši simti."),
                ("Desmitu vietā nav nekā",
                 "Tāpēc tur raksta 0."),
                ("607",
                 "Vienu vietā ir 7."),
            ],
            atbilde="607"),

    Ievadi("Raksti ar cipariem", [
        {"jaut": "Uzraksti ar cipariem: seši simti septiņi", "atb": ["607"],
         "padoms": "Desmitu vietā nulle."},
        {"jaut": "Uzraksti ar cipariem: trīs simti piecdesmit",
         "atb": ["350"], "padoms": "Vienu vietā nulle."},
        {"jaut": "Uzraksti ar cipariem: trīs simti piecpadsmit",
         "atb": ["315"], "padoms": "Piecpadsmit ir 15."},
        {"jaut": "Uzraksti ar cipariem: deviņi simti deviņdesmit deviņi",
         "atb": ["999"], "padoms": "Lielākais trīsciparu skaitlis."},
        {"jaut": "Uzraksti ar cipariem: divi simti",
         "atb": ["200"], "padoms": "Divas nulles."},
        {"jaut": "Uzraksti ar cipariem: četri simti divdesmit",
         "atb": ["420"], "padoms": "Vienu vietā nulle."},
    ], pamats=4),

    Zimejums("Divi līdzīgi skaitļi",
           restis([["S", "D", "V"],
                   [3, 1, 5],
                   [3, 5, 0]],
                  "315 un 350"),
             paskaidro="«Piecpadsmit» un «piecdesmit» skan līdzīgi, bet "
                       "cipari stāv dažādās vietās.",
             ievads="Uzmanīgi ar šiem vārdiem."),

    Varianti("Kurš skaitlis tas ir?", [
        {"jaut": "Kā pieraksta «astoņi simti divi»?",
         "opcijas": ["802", "820", "82", "8002"],
         "pareizi": 0, "padoms": "Desmitu vietā nulle."},
        {"jaut": "Kā pieraksta «pieci simti sešdesmit»?",
         "opcijas": ["560", "506", "56", "5060"],
         "pareizi": 0, "padoms": "Vienu vietā nulle."},
        {"jaut": "Kurš ir lielākais trīsciparu skaitlis?",
         "opcijas": ["999", "1000", "900", "990"],
         "pareizi": 0, "padoms": "Visās vietās deviņnieki."},
        {"jaut": "Kurš ir mazākais trīsciparu skaitlis?",
         "opcijas": ["100", "111", "10", "101"],
         "pareizi": 0, "padoms": "Simtu vietā mazākais derīgais cipars."},
    ], pamats=4),

    Pasaule("Cik dienu ilgst lidojums?",
            Ievadi("", [
                {"jaut": "Līdz Marsam 210 dienas. Cik simtu tajā ir?",
                 "atb": ["2"], "padoms": "Simtu cipars."},
                {"jaut": "Cik desmitu ir skaitlī 210?", "atb": ["1"],
                 "padoms": "Desmitu cipars."},
                {"jaut": "Atpakaļceļš arī 210 dienas. Cik dienu ir abos "
                         "virzienos?",
                 "atb": ["420"], "padoms": "2 · 210."},
                {"jaut": "Uz Marsa jāpavada 500 dienas. Cik dienu ilgst viss "
                         "ceļojums?",
                 "atb": ["920"], "padoms": "420 + 500."},
            ]),
            pavediens="kosmoss",
            konteksts="Kosmosa misijas ilgumu skaita dienās, un tas gandrīz "
                      "vienmēr ir trīsciparu skaitlis.",
            kapec="Viena cipara kļūda misijas plānā maina visu."),

    Kopsavilkums([
        "Lasu un rakstu skaitļus līdz 1000 ar cipariem.",
        "Rakstu skaitļus arī ar vārdiem.",
        "Zinu, ka nulle tur vietu.",
        "Atšķiru «piecpadsmit» no «piecdesmit».",
    ]),

    Majas([
        "Uzraksti ar vārdiem skaitļus 408, 780 un 913.",
        "Atrodi mājās vai ziņās trīs trīsciparu skaitļus.",
        "Izlasi tos skaļi kādam mājiniekam.",
    ]),
]
