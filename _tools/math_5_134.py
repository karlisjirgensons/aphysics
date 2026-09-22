# -*- coding: utf-8 -*-
"""5. klase, 134. stunda: «Kā parasto daļu pārvērst decimāldaļā?»

Līdz šim ar komatu rakstīja tikai daļas, kurām saucējs jau bija 10, 100 vai
1000. Te parādās otrs solis: vispirms daļu paplašina līdz tādam saucējam,
un tikai tad raksta komatu. Tāpēc šī stunda ir 55. stundas turpinājums -
paplašināšana ar konkrētu mērķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā parasto daļu pārvērst decimāldaļā?"

MERKIS = ("Iemācīsimies lietot daļas pamatīpašību, lai daļu ar saucēju 2, 4, "
          "5, 20, 25 vai 50 pierakstītu kā decimāldaļu.")

SATURS = [
    Sakums("Vispirms saucējs 10 vai 100",
           zimejums=restis([["1/2", "5/10", "0,5"],
                            ["3/4", "75/100", "0,75"]],
                           virsraksts="Divi soļi līdz komatam"),
           paraksts="Daļu paplašina, tikai tad raksta ar komatu.",
           fakti=["Ar komatu raksta tikai saucējus 10, 100 un 1000.",
                  "Saucējus 2, 4, 5, 20, 25 un 50 var paplašināt.",
                  "Pēc paplašināšanas viss ir kā iepriekšējā stundā."]),

    Doma("Paplašini līdz 10, 100 vai 1000",
         "Parasto daļu pārvērš decimāldaļā, paplašinot to līdz saucējam 10, "
         "100 vai 1000 un tad pierakstot ar komatu.",
         soli=[
             "Paskaties, ar ko saucējs jāreizina, lai iznāktu 10, 100 vai "
             "1000.",
             "Reizini ar to pašu skaitli arī skaitītāju.",
             "Pieraksti iegūto daļu ar komatu.",
             "Pārbaudi ciparu skaitu aiz komata.",
             "Ja saucēju nevar paplašināt, decimāldaļa nesanāk īsa.",
         ],
         pieze="Der saucēji 2, 4, 5, 8, 10, 20, 25 un 50, jo tos var "
               "paplašināt līdz 10, 100 vai 1000. Saucēju 3 vai 7 tā "
               "pārveidot nevar - to mācīsies vēlāk."),

    Paraugs("Pārvērt {3|4} decimāldaļā",
            uzd="Pieraksti daļu {3|4} ar komatu.",
            soli=[
                ("4 · 25 = 100",
                 "Saucēju var paplašināt līdz 100."),
                ("3 · 25 = 75",
                 "Ar to pašu skaitli reizina skaitītāju."),
                ("{3|4} = {75|100}",
                 "Paplašinātā daļa."),
                ("{75|100} = 0,75",
                 "Divi cipari aiz komata."),
            ],
            atbilde="{3|4} = 0,75"),

    Ievadi("Pieraksti ar komatu", [
        {"jaut": "{1|2} kā decimāldaļa. Ieraksti skaitli.",
         "atb": ["0,5", "0,50"], "padoms": "{5|10}."},
        {"jaut": "{1|4} kā decimāldaļa.",
         "atb": ["0,25"], "padoms": "{25|100}."},
        {"jaut": "{3|4} kā decimāldaļa.",
         "atb": ["0,75"], "padoms": "{75|100}."},
        {"jaut": "{1|5} kā decimāldaļa.",
         "atb": ["0,2", "0,20"], "padoms": "{2|10}."},
        {"jaut": "{3|5} kā decimāldaļa.",
         "atb": ["0,6", "0,60"], "padoms": "{6|10}."},
        {"jaut": "{1|20} kā decimāldaļa.",
         "atb": ["0,05"], "padoms": "{5|100}."},
        {"jaut": "{1|25} kā decimāldaļa.",
         "atb": ["0,04"], "padoms": "{4|100}."},
        {"jaut": "{7|50} kā decimāldaļa.",
         "atb": ["0,14"], "padoms": "{14|100}."},
    ], pamats=4,
        ievads="Vispirms paplašini līdz 10 vai 100, tikai tad liec komatu."),

    Zimejums("Biežāk lietotās daļas",
             restis([["1/2", "1/4", "3/4", "1/5"],
                     ["0,5", "0,25", "0,75", "0,2"]],
                    virsraksts="Šos pārus ir vērts zināt no galvas"),
             paskaidro="Šīs četras daļas sastopamas tik bieži, ka to "
                       "decimālo pierakstu atceras uzreiz, nerēķinot.",
             ievads="Dažus pārus nav vērts katru reizi rēķināt."),

    Varianti("Ar ko paplašināt?", [
        {"jaut": "Ar ko jāreizina saucējs 4, lai iznāktu 100?",
         "opcijas": ["25", "4", "10", "20"],
         "pareizi": 0,
         "padoms": "4 · 25 = 100."},
        {"jaut": "Ar ko jāreizina saucējs 5, lai iznāktu 10?",
         "opcijas": ["2", "5", "10", "20"],
         "pareizi": 0,
         "padoms": "5 · 2 = 10."},
        {"jaut": "{1|4} kā decimāldaļa ir...",
         "opcijas": ["0,25", "0,14", "0,4", "1,4"],
         "pareizi": 0,
         "padoms": "{25|100}."},
        {"jaut": "{1|20} kā decimāldaļa ir...",
         "opcijas": ["0,05", "0,2", "0,5", "0,02"],
         "pareizi": 0,
         "padoms": "20 · 5 = 100."},
        {"jaut": "Kuru saucēju nevar paplašināt līdz 10, 100 vai 1000?",
         "opcijas": ["3", "4", "20", "50"],
         "pareizi": 0,
         "padoms": "10, 100 un 1000 ar 3 nedalās."},
        {"jaut": "{3|5} kā decimāldaļa ir...",
         "opcijas": ["0,6", "0,35", "0,53", "3,5"],
         "pareizi": 0,
         "padoms": "{6|10}."},
    ], pamats=4),

    Pasaule("Atlaide daļās un ar komatu",
            Ievadi("", [
                {"jaut": "Atlaide ir {1|4} no cenas. Kā to raksta ar komatu?",
                 "atb": ["0,25"], "padoms": "{25|100}."},
                {"jaut": "Atlaide ir {1|2} no cenas. Kā to raksta ar komatu?",
                 "atb": ["0,5", "0,50"], "padoms": "{5|10}."},
                {"jaut": "Atlaide ir {1|5} no cenas. Kā to raksta ar komatu?",
                 "atb": ["0,2", "0,20"], "padoms": "{2|10}."},
                {"jaut": "Atlaide ir {3|20} no cenas. Kā to raksta ar "
                         "komatu?",
                 "atb": ["0,15"], "padoms": "{15|100}."},
            ]),
            pavediens="veikals",
            konteksts="Reklāmā atlaidi raksta daļās, bet kasē tā pārvēršas "
                      "skaitlī ar komatu.",
            kapec="Abi pieraksti apzīmē vienu un to pašu atlaidi."),

    Kopsavilkums([
        "Paplašinu daļu līdz saucējam 10, 100 vai 1000.",
        "Pierakstu iegūto daļu ar komatu.",
        "Zinu no galvas {1|2}, {1|4}, {3|4} un {1|5} decimālo pierakstu.",
        "Atpazīstu saucējus, kurus tā paplašināt nevar.",
    ]),

    Majas([
        "Pieraksti ar komatu {2|5}, {7|20} un {9|25}.",
        "Uzraksti trīs daļas, kuras nevar pārvērst īsā decimāldaļā.",
        "Iemācies no galvas četrus biežāk lietotos pārus.",
    ]),
]
