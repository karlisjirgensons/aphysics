# -*- coding: utf-8 -*-
"""6. klase, 84. stunda: «Kā zīmējums palīdz?»

Procentu josla ir tas pats modelis, ar kuru 6.1. tematā dalīja kopumu
attiecībā - tikai tagad daļu vienmēr ir simts. Zīmējums neaizstāj rēķinu,
bet pasaka, kura darbība vajadzīga, un tieši tur skolēni kļūdās visbiežāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Kā zīmējums palīdz?"

MERKIS = ("Veidosim shematisku zīmējumu, lai attēlotu vienu skaitli kā otra "
          "procentus.")

SATURS = [
    Sakums("Josla, kurā vienmēr ir 100 daļu",
           zimejums=dala(10, 6, "60 %"),
           paraksts="Visa josla ir kopums jeb 100 %. Iekrāsotā daļa ir tas, "
                    "par ko uzdevums runā.",
           fakti=["Zīmējumā vienmēr atzīmē abus galus: 0 % un 100 %.",
                  "Zem joslas raksta skaitļus, virs tās - procentus.",
                  "Tad uzreiz redz, kurš skaitlis ir nezināmais."]),

    Doma("Uzzīmē joslu un atzīmē abus stāvus",
         "Procentu uzdevumu attēlo ar joslu: virs tās raksta procentus, zem "
         "tās - skaitļus, un nezināmo atzīmē ar jautājuma zīmi.",
         soli=[
             "Uzzīmē joslu un pieraksti 0 % un 100 % galos.",
             "Atzīmē doto procentu vietu uz joslas.",
             "Zem joslas pieraksti zināmos skaitļus.",
             "Nezināmo atzīmē ar jautājuma zīmi.",
             "Paskaties, vai trūkst daļas vai kopuma - tas pasaka darbību.",
         ],
         pieze="Ja jautājuma zīme ir zem procenta, jārēķina daļa no kopuma; "
               "ja zem 100 %, jāmeklē kopums. Zīmējums atbild uz jautājumu "
               "«reizināt vai dalīt»."),

    Slidnis("Josla un skaitļi kopā",
            [{"v": "20 % no 200", "teksts": "= 40", "josla": 20,
              "zim": dala(10, 2)},
             {"v": "40 % no 200", "teksts": "= 80", "josla": 40,
              "zim": dala(10, 4)},
             {"v": "60 % no 200", "teksts": "= 120", "josla": 60,
              "zim": dala(10, 6)},
             {"v": "80 % no 200", "teksts": "= 160", "josla": 80,
              "zim": dala(10, 8)}],
            ievads="Spied soli pa solim: kopums paliek 200, bet iekrāsotā "
                   "daļa un skaitlis mainās kopā."),

    Paraugs("Uzzīmē un izrēķini",
            uzd="Klasē ir 25 skolēni, 60 % no viņiem apmeklē pulciņu. Cik "
                "skolēnu tas ir?",
            soli=[
                ("Josla: 0 % kreisajā galā, 100 % labajā",
                 "Zem 100 % raksta 25."),
                ("Atzīmē 60 % un zem tā liec jautājuma zīmi",
                 "Nezināmais ir daļa, ne kopums."),
                ("1 % ir 25 : 100 = 0,25",
                 "Viena simtdaļa."),
                ("60 · 0,25 = 15",
                 "Sešdesmit simtdaļas."),
            ],
            atbilde="15 skolēni"),

    Ievadi("Nolasi no joslas", [
        {"jaut": "Kopums 25, meklē 60 %. Cik ir 1 %?",
         "atb": ["0,25", "0.25"], "padoms": "25 : 100."},
        {"jaut": "Cik ir 60 % no 25?",
         "atb": ["15"], "padoms": "60 · 0,25."},
        {"jaut": "Kopums 200, meklē 35 %. Cik ir 1 %?",
         "atb": ["2"], "padoms": "200 : 100."},
        {"jaut": "Cik ir 35 % no 200?",
         "atb": ["70"], "padoms": "35 · 2."},
        {"jaut": "Kopums 400. Cik ir 15 %?",
         "atb": ["60"], "padoms": "1 % ir 4."},
        {"jaut": "Kopums 50. Cik ir 12 %?",
         "atb": ["6"], "padoms": "1 % ir 0,5."},
    ], pamats=4,
        ievads="Viens procents ir kopums, dalīts ar simtu."),

    Varianti("Ko pasaka zīmējums?", [
        {"jaut": "Jautājuma zīme ir zem 100 %. Ko meklē?",
         "opcijas": ["Kopumu", "Daļu", "Procentus", "Starpību"],
         "pareizi": 0,
         "padoms": "100 % ir viss kopums."},
        {"jaut": "Jautājuma zīme ir zem 30 %. Ko meklē?",
         "opcijas": ["Daļu no kopuma", "Kopumu",
                     "Procentu skaitu", "Atlikumu"],
         "pareizi": 0,
         "padoms": "Procents ir zināms, daļa - nav."},
        {"jaut": "Ko raksta zem joslas?",
         "opcijas": ["Skaitļus", "Procentus", "Daļas", "Neko"],
         "pareizi": 0,
         "padoms": "Virs joslas ir procenti."},
        {"jaut": "Kopums 60, iekrāsotas 3 daļas no 10. Cik procentu tas ir?",
         "opcijas": ["30", "3", "10", "60"],
         "pareizi": 0,
         "padoms": "{3|10} = {30|100}."},
    ], pamats=4),

    Pasaule("Cik liela daļa no budžeta?",
            Ievadi("", [
                {"jaut": "Klases budžets ir 200 €. Cik eiro ir 1 %?",
                 "atb": ["2"], "padoms": "200 : 100."},
                {"jaut": "Ēdieniem atvēl 45 %. Cik eiro tas ir?",
                 "atb": ["90"], "padoms": "45 · 2."},
                {"jaut": "Dekorācijām atvēl 15 %. Cik eiro tas ir?",
                 "atb": ["30"], "padoms": "15 · 2."},
                {"jaut": "Cik procentu paliek pārējam?",
                 "atb": ["40"], "padoms": "100 − 45 − 15."},
            ]),
            pavediens="skola",
            konteksts="Klases pasākuma budžetu vispirms sadala procentos un "
                      "tikai tad pārvērš eiro.",
            kapec="Josla parāda visu sadalījumu vienā attēlā."),

    Zimejums("Viss budžets vienā joslā",
             dala(20, 9, "45 % ēdieniem"),
             paskaidro="Josla ir 100 %. Deviņas daļas no divdesmit ir 45 % - "
                       "tieši tik, cik atvēlēts ēdieniem.",
             ievads="Vienā joslā redz gan daļu, gan atlikumu."),

    Kopsavilkums([
        "Veidoju procentu joslu ar 0 % un 100 % galos.",
        "Rakstu procentus virs joslas, skaitļus - zem tās.",
        "Atrodu viena procenta vērtību un no tās pārējo.",
        "No zīmējuma nosaku, vai meklē daļu vai kopumu.",
    ]),

    Majas([
        "Uzzīmē joslu uzdevumam «30 % no 80» un izrēķini to.",
        "Uzzīmē joslu savam nedēļas laikam: mācības, miegs, brīvais laiks.",
        "Pieraksti, cik procentu no diennakts tu guli.",
    ]),
]
