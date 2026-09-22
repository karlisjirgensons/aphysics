# -*- coding: utf-8 -*-
"""5. klase, 16. stunda: «Kuri skaitļi noapaļojas līdz šim?»

Mikrotemata pēdējā stunda - noapaļošana apgrieztā virzienā. No viena skaitļa
tagad sanāk vesela skaitļu kopa (3. un 4. stunda), un atbilde nav skaitlis,
bet robežas. Šis pats spriedums vēlāk atgriežas, runājot par mērījumu
precizitāti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kuri skaitļi noapaļojas līdz šim?"

MERKIS = ("Mācīsimies nosaukt visus skaitļus, kurus noapaļojot iegūst doto "
          "skaitli, un norādīt, līdz kurai šķirai noapaļots.")

SATURS = [
    Sakums("Uz ceļazīmes rakstīts «500 m». Cik tur īsti ir?",
           zimejums=taisne(400, 600, 100, [(450, "450"), (549, "549")]),
           paraksts="Līdz simtiem uz 500 noapaļojas viss, kas atrodas starp "
                    "abiem punktiem.",
           fakti=["Noapaļots skaitlis nestāsta, kāds bija īstais.",
                  "Toties tas pasaka, starp kurām robežām īstais atrodas."]),

    Doma("No apaļa skaitļa atpakaļ sanāk nevis viens skaitlis, bet robežas",
         "Meklē mazāko un lielāko skaitli, kas vēl noapaļojas līdz dotajam.",
         soli=[
             "Noskaidro, līdz kurai šķirai skaitlis noapaļots.",
             "Atņem pusi no šķiras - tas ir mazākais skaitlis.",
             "Pieskaiti pusi no šķiras - tur sākas jau nākamais apaļais.",
             "Lielākais ir par 1 mazāks nekā šī augšējā robeža.",
         ],
         pieze="Līdz simtiem noapaļojot 500, mazākais ir 450, bet lielākais - "
               "549, nevis 550: pats 550 jau noapaļojas uz 600."),

    Zimejums("Kur beidzas viens simts un sākas otrs",
             taisne(440, 560, 20, [(450, "450"), (549, "549")]),
             paskaidro="Pa kreisi no 450 skaitļi noapaļojas uz 400, no 550 - "
                       "uz 600. Pa vidu paliek tieši 100 skaitļu.",
             ievads="Tas pats gabals tuvāk."),

    Paraugs("Kuri skaitļi dod 3 000?",
            uzd="Kurus skaitļus noapaļojot līdz tūkstošiem, sanāk 3 000?",
            soli=[
                ("Šķira ir tūkstoši, puse no tās ir 500",
                 "Tieši par tik skaitlis drīkst atšķirties."),
                ("3 000 − 500 = 2 500",
                 "Mazākais skaitlis: 2 500 noapaļojas uz augšu."),
                ("3 000 + 500 = 3 500",
                 "Te jau sākas 4 000, tāpēc 3 500 neder."),
                ("Lielākais ir 3 500 − 1 = 3 499",
                 "Kopā sanāk skaitļi no 2 500 līdz 3 499."),
            ],
            atbilde="visi skaitļi no 2 500 līdz 3 499"),

    Ievadi("Nosauc robežas", [
        {"jaut": "Līdz simtiem noapaļojot, sanāk 800. Kāds ir mazākais "
                 "skaitlis?",
         "atb": ["750"], "padoms": "800 − 50."},
        {"jaut": "Un kāds ir lielākais?", "atb": ["849"],
         "padoms": "850 jau noapaļotos uz 900."},
        {"jaut": "Līdz desmitiem noapaļojot, sanāk 60. Kāds ir mazākais "
                 "skaitlis?",
         "atb": ["55"], "padoms": "Puse no desmita ir 5."},
        {"jaut": "Un kāds ir lielākais?", "atb": ["64"],
         "padoms": "65 jau noapaļotos uz 70."},
        {"jaut": "Līdz tūkstošiem noapaļojot, sanāk 7 000. Kāds ir mazākais "
                 "skaitlis?",
         "atb": ["6500"], "padoms": "7 000 − 500."},
        {"jaut": "Un kāds ir lielākais?", "atb": ["7499"],
         "padoms": "7 500 jau noapaļotos uz 8 000."},
        {"jaut": "Cik dažādu veselu skaitļu noapaļojas līdz 800 (līdz "
                 "simtiem)?",
         "atb": ["100"], "padoms": "No 750 līdz 849."},
        {"jaut": "Cik dažādu veselu skaitļu noapaļojas līdz 60 (līdz "
                 "desmitiem)?",
         "atb": ["10"], "padoms": "No 55 līdz 64."},
    ], pamats=4,
        ievads="Uzraksti tikai skaitli."),

    Varianti("Ko pasaka apaļš skaitlis?", [
        {"jaut": "Ceļazīme rāda «500 m» (noapaļots līdz simtiem). Vai līdz "
                 "mērķim var būt 462 m?",
         "opcijas": ["Jā, 462 noapaļojas uz 500",
                     "Nē, tur jābūt tieši 500",
                     "Nē, 462 noapaļojas uz 400",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Vai 462 ir starp 450 un 549?"},
        {"jaut": "Skaitlis noapaļots līdz desmitiem un sanāca 40. Kurš "
                 "skaitlis noteikti neder?",
         "opcijas": ["45", "36", "44", "40"],
         "pareizi": 0,
         "padoms": "Pārbaudi, uz ko noapaļojas katrs."},
        {"jaut": "Kāpēc lielākais skaitlis ir 549, nevis 550?",
         "opcijas": ["550 jau noapaļojas uz 600",
                     "550 nav vesels skaitlis",
                     "550 ir par lielu pēc skaitīšanas",
                     "Tā ir kļūda grāmatā"],
         "pareizi": 0,
         "padoms": "Atceries kārtulu par 5."},
        {"jaut": "Cik plata ir kopa, kas noapaļojas līdz vienam un tam pašam "
                 "simtam?",
         "opcijas": ["100 skaitļi", "50 skaitļi", "99 skaitļi",
                     "Katru reizi citādi"],
         "pareizi": 0,
         "padoms": "Saskaiti no 750 līdz 849."},
    ], pamats=4),

    Pasaule("Cik gara ir upe?",
            Ievadi("", [
                {"jaut": "Grāmatā rakstīts, ka upe ir 500 km gara (noapaļots "
                         "līdz simtiem). Kāds ir mazākais iespējamais garums?",
                 "atb": ["450"], "padoms": "500 − 50."},
                {"jaut": "Kāds ir lielākais iespējamais garums?",
                 "atb": ["549"], "padoms": "550 jau būtu 600."},
                {"jaut": "Ezera platība norādīta 200 ha (līdz simtiem). Kāda "
                         "ir mazākā iespējamā platība?",
                 "atb": ["150"], "padoms": "200 − 50."},
                {"jaut": "Meža platība norādīta 4 000 ha (līdz tūkstošiem). "
                         "Kāda ir lielākā iespējamā platība?",
                 "atb": ["4499"], "padoms": "4 500 jau būtu 5 000."},
            ]),
            pavediens="daba",
            konteksts="Dabas datos gandrīz viss ir noapaļots, tāpēc pētnieks "
                      "vienmēr zina tikai robežas.",
            kapec="Apaļš skaitlis pasaka, cik tālu īstais drīkst būt."),

    Kopsavilkums([
        "Nosaucu mazāko un lielāko skaitli, kas noapaļojas līdz dotajam.",
        "Norādu, līdz kurai šķirai skaitlis ir noapaļots.",
        "Zinu, ka augšējā robeža pieder jau nākamajam apaļajam skaitlim.",
        "Saprotu, ka noapaļots skaitlis pasaka robežas, ne precīzo vērtību.",
    ]),

    Majas([
        "Atrodi mājās vai uz ielas apaļu skaitli un uzraksti, starp kurām "
        "robežām varētu būt īstais.",
        "Izdomā skaitli, pasaki draugam tikai tā noapaļojumu līdz simtiem un "
        "palūdz uzminēt robežas.",
        "Padomā, kāpēc «ap 3 000» un «3 000» sarunā nozīmē vienu un to pašu.",
    ]),
]
