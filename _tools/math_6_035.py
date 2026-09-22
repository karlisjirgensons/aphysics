# -*- coding: utf-8 -*-
"""6. klase, 35. stunda: «Cik apmēram sanāks?»

Novērtēšana ir prasme, kuru eksāmenā prasa, bet stundā bieži izlaiž. Tā ir
vienīgā aizsardzība pret kļūdu, kas maina atbildi desmitkārt - un tā strādā
ātrāk nekā jebkura pārbaude.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Cik apmēram sanāks?"

MERKIS = ("Mācīsimies novērtēt daļu un jauktu skaitļu reizinājuma un "
          "dalījuma aptuveno vērtību.")

SATURS = [
    Sakums("Vispirms mini, tikai tad rēķini",
           zimejums=taisne(0, 12, 2, [(6, "novērtējums")]),
           paraksts="3{1|4} · 2{1|8} ir apmēram 3 · 2, tātad ap 6. Atbilde 7 "
                    "ir ticama, bet 70 nav.",
           fakti=["Novērtē, noapaļojot līdz tuvākajam veselajam skaitlim.",
                  "Ja īstā atbilde ir tālu no novērtējuma, kaut kur ir "
                  "kļūda."]),

    Doma("Noapaļo un rēķini galvā",
         "Aptuveno vērtību iegūst, jauktos skaitļus noapaļojot līdz "
         "veseliem, bet īstas daļas - līdz 0, {1|2} vai 1.",
         soli=[
             "Noapaļo katru skaitli līdz tuvākajam ērtajam skaitlim.",
             "Izrēķini noapaļoto darbību galvā.",
             "Pieraksti novērtējumu.",
             "Izrēķini precīzi.",
             "Salīdzini: ja atšķirība ir liela, meklē kļūdu.",
         ],
         pieze="Reizinot ar skaitli, kas mazāks par 1, novērtējums ir mazāks "
               "par sākotnējo; dalot ar tādu - lielāks. Tas vien jau pasaka, "
               "vai atbilde ir ticama."),

    Paraugs("Novērtē un tad izrēķini",
            uzd="Cik apmēram ir 4{7|8} · 2{1|10}?",
            soli=[
                ("4{7|8} ir gandrīz 5",
                 "{7|8} ir tuvu vienam."),
                ("2{1|10} ir gandrīz 2",
                 "{1|10} ir tuvu nullei."),
                ("5 · 2 = 10",
                 "Tāds ir novērtējums."),
                ("Precīzi: {39|8} · {21|10} = {819|80} ir apmēram 10,2",
                 "Novērtējums bija tuvu."),
            ],
            atbilde="apmēram 10"),

    Ievadi("Novērtē bez precīza rēķina", [
        {"jaut": "Cik apmēram ir 5{1|9} · 3{1|8}? Atbildi raksti kā vesels "
                 "skaitlis.",
         "atb": ["15"], "padoms": "5 · 3."},
        {"jaut": "Cik apmēram ir 7{8|9} : 1{9|10}? Atbildi raksti kā vesels "
                 "skaitlis.",
         "atb": ["4"], "padoms": "8 : 2."},
        {"jaut": "Cik apmēram ir 9{1|10} · {1|2}? Atbildi raksti kā vesels "
                 "skaitlis.",
         "atb": ["4", "5"], "padoms": "Puse no 9."},
        {"jaut": "20 · {9|10} būs lielāks vai mazāks par 20? Raksti "
                 "«lielāks» vai «mazāks».",
         "atb": ["mazāks"], "padoms": "{9|10} ir mazāks par 1."},
        {"jaut": "20 : {9|10} būs lielāks vai mazāks par 20? Raksti "
                 "«lielāks» vai «mazāks».",
         "atb": ["lielāks"], "padoms": "Dalot ar mazāku par 1."},
        {"jaut": "Cik apmēram ir 11{7|8} : 2{15|16}? Atbildi raksti kā "
                 "vesels skaitlis.",
         "atb": ["4"], "padoms": "12 : 3."},
    ], pamats=4,
        ievads="Novērtējums ir viena rinda galvā, nevis burtnīcā."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "3{1|4} · 4{1|5} skolēns ieguva 130. Vai tas ir ticami?",
         "opcijas": ["Nē, jābūt ap 13", "Jā, tas ir pareizi",
                     "Nevar spriest", "Jā, jo skaitļi ir lieli"],
         "pareizi": 0,
         "padoms": "3 · 4 = 12."},
        {"jaut": "{1|2} · 18 skolēns ieguva 36. Kur ir kļūda?",
         "opcijas": ["Viņš dalīja ar {1|2}, nevis reizināja",
                     "Viņš saskaitīja", "Nav kļūdas",
                     "Viņš aizmirsa saīsināt"],
         "pareizi": 0,
         "padoms": "Puse no 18 ir 9."},
        {"jaut": "Kurš novērtējums der uzdevumam 6{1|8} : {1|2}?",
         "opcijas": ["Apmēram 12", "Apmēram 3", "Apmēram 6", "Apmēram 1"],
         "pareizi": 0,
         "padoms": "Dalot ar pusi, skaitlis dubultojas."},
        {"jaut": "Kāpēc novērtējumu izdara *pirms* rēķina?",
         "opcijas": ["Lai zinātu, ko gaidīt no atbildes",
                     "Lai būtu ātrāk", "Lai nerēķinātu vispār",
                     "Tas nav svarīgi"],
         "pareizi": 0,
         "padoms": "Gaidīta atbilde pasargā no rupjas kļūdas."},
    ], pamats=4),

    Pasaule("Vai pietiks degvielas?",
            Ievadi("", [
                {"jaut": "Brauciens ir 2{9|10} h, stundā patērē 5{1|10} l. "
                         "Cik apmēram litru? Raksti veselu skaitli.",
                 "atb": ["15"], "padoms": "3 · 5."},
                {"jaut": "Tvertnē ir 20 l. Vai pietiks? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "15 ir mazāk par 20."},
                {"jaut": "Cik apmēram stundu var braukt ar 20 l? Raksti "
                         "veselu skaitli.",
                 "atb": ["4"], "padoms": "20 : 5."},
                {"jaut": "Ja patēriņš būtu {1|2} no pašreizējā, cik apmēram "
                         "litru prasītu brauciens?",
                 "atb": ["7", "8"], "padoms": "Puse no 15."},
            ]),
            pavediens="celojums",
            konteksts="Pie degvielas uzpildes nav laika rēķināt precīzi - ir "
                      "tikai jāzina, vai pietiks.",
            kapec="Novērtējums atbild ātrāk nekā precīzs rēķins."),

    Kopsavilkums([
        "Novērtēju reizinājuma un dalījuma aptuveno vērtību.",
        "Noapaļoju jauktus skaitļus līdz veseliem, daļas - līdz 0, {1|2} "
        "vai 1.",
        "Salīdzinu precīzo atbildi ar novērtējumu.",
        "Pamanu rupju kļūdu, pirms to izlabo skolotājs.",
    ]),

    Majas([
        "Novērtē un tad izrēķini 8{1|7} · 3{1|9}.",
        "Atrodi vecā darbā atbildi, kuru novērtējums būtu apšaubījis.",
        "Novērtē, cik maksās 3{1|2} kg augļu, ja kilograms ir 2{1|10} €.",
    ]),
]
