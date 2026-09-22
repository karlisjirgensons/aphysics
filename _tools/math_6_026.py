# -*- coding: utf-8 -*-
"""6. klase, 26. stunda: «Kāpēc reizinot var iegūt mazāku skaitli?»

Stunda par priekšstatu, ne par darbību. «Reizinot kļūst vairāk» ir
pieņēmums no pirmajām klasēm, un tieši tas vēlāk traucē saprast procentus un
mērogu. Te to apzināti salauž - ar zīmējumu un ar skaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, dala)

TEMA = "Kāpēc reizinot var iegūt mazāku skaitli?"

MERKIS = ("Skaidrosim, kāpēc reizinājums ar īstu daļu ir mazāks nekā "
          "sākotnējais skaitlis.")

SATURS = [
    Sakums("Reizināšana ne vienmēr palielina",
           zimejums=dala(4, 3, "3/4"),
           paraksts="{3|4} no 12 ir 9. Reizinājums ir *mazāks* par 12, jo "
                    "{3|4} ir mazāks par 1.",
           fakti=["Reizinot ar skaitli, kas mazāks par 1, rezultāts sarūk.",
                  "Reizinot ar 1, skaitlis nemainās.",
                  "Tikai reizinot ar vairāk nekā 1, tas aug."]),

    Doma("Viss atkarīgs no tā, vai reizinātājs ir lielāks par 1",
         "Reizinot ar īstu daļu, ņem tikai daļu no skaitļa - tāpēc "
         "rezultāts ir mazāks par sākotnējo.",
         soli=[
             "Paskaties, vai reizinātājs ir lielāks vai mazāks par 1.",
             "Ja mazāks - gaidi mazāku rezultātu.",
             "Ja lielāks - gaidi lielāku.",
             "Ja tieši 1 - rezultāts būs tas pats skaitlis.",
             "Izrēķini un pārbaudi, vai minējums piepildījās.",
         ],
         pieze="Tas pats noteikums der abiem virzieniem: dalot ar īstu daļu, "
               "rezultāts *aug*. Tieši tāpēc «reizināt - vairāk, dalīt - "
               "mazāk» ir maldīgs noteikums."),

    Slidnis("Maini reizinātāju",
            [{"v": "20 · {1|4}", "teksts": "= 5 - krietni mazāk",
              "josla": 12},
             {"v": "20 · {1|2}", "teksts": "= 10 - uz pusi mazāk",
              "josla": 25},
             {"v": "20 · 1", "teksts": "= 20 - nekas nemainās",
              "josla": 50},
             {"v": "20 · {3|2}", "teksts": "= 30 - lielāks par 20",
              "josla": 75},
             {"v": "20 · 2", "teksts": "= 40 - divreiz vairāk",
              "josla": 100}],
            ievads="Spied soli pa solim: skaitlis 20 paliek, mainās tikai "
                   "reizinātājs. Robeža ir tieši pie vieninieka."),

    Paraugs("Kurš rezultāts būs lielāks?",
            uzd="Nerēķinot salīdzini: 36 · {5|6} un 36 · {7|6}.",
            soli=[
                ("{5|6} ir mazāks par 1",
                 "Skaitītājs mazāks par saucēju."),
                ("Tāpēc 36 · {5|6} būs mazāks par 36",
                 "Ņem tikai daļu no 36."),
                ("{7|6} ir lielāks par 1",
                 "Skaitītājs lielāks par saucēju."),
                ("Tāpēc 36 · {7|6} būs lielāks par 36",
                 "Ņem visu un vēl mazliet."),
                ("Pārbaude: 30 un 42",
                 "Minējums apstiprinās."),
            ],
            atbilde="lielāks ir 36 · {7|6}"),

    Ievadi("Vairāk vai mazāk?", [
        {"jaut": "Cik ir 12 · {3|4}?",
         "atb": ["9"], "padoms": "{36|4} = 9."},
        {"jaut": "Cik ir 20 · {2|5}?",
         "atb": ["8"], "padoms": "{40|5} = 8."},
        {"jaut": "Cik ir 18 · {7|6}?",
         "atb": ["21"], "padoms": "{126|6} = 21."},
        {"jaut": "Cik ir 15 · 1?",
         "atb": ["15"], "padoms": "Reizinot ar 1, nekas nemainās."},
        {"jaut": "Cik ir 30 · {5|6}?",
         "atb": ["25"], "padoms": "{150|6} = 25."},
        {"jaut": "Cik ir 24 · {5|4}?",
         "atb": ["30"], "padoms": "{120|4} = 30."},
    ], pamats=4,
        ievads="Pirms rēķini, pasaki, vai atbilde būs lielāka vai mazāka."),

    Pasaule("Cik tālu tiks ar šādu ātrumu?",
            Kustiba("", [
                {"jaut": "Parastā dienā droni veic 60 km. Vējā tas veic "
                         "{2|3} no parastā. Cik km?",
                 "atb": 40, "beigas": 90, "iedala": 15, "mers": "kilometri",
                 "merkis": "vējā", "objekts": "Drons",
                 "padoms": "{2|3} · 60 = 40 - mazāk par 60."},
                {"jaut": "Ar vēju mugurā tas veic {5|4} no parastā. Cik km?",
                 "atb": 75, "beigas": 90, "iedala": 15, "mers": "kilometri",
                 "merkis": "ar vēju", "objekts": "Drons",
                 "padoms": "{5|4} · 60 = 75 - vairāk par 60."},
                {"jaut": "Ar pusi uzlādes tas veic {1|2} no parastā. Cik km?",
                 "atb": 30, "beigas": 90, "iedala": 15, "mers": "kilometri",
                 "merkis": "puse uzlādes", "objekts": "Drons",
                 "padoms": "Puse no 60."},
                {"jaut": "Jaunais modelis veic {3|2} no parastā. Cik km?",
                 "atb": 90, "beigas": 90, "iedala": 15, "mers": "kilometri",
                 "merkis": "jaunais modelis", "objekts": "Drons",
                 "padoms": "{3|2} · 60 = 90."},
            ]),
            pavediens="tehnika",
            konteksts="Drona nobrauktais attālums ir viens un tas pats "
                      "skaitlis, reizināts ar dažādām daļām.",
            kapec="Pēc reizinātāja jau iepriekš var pateikt, uz kuru pusi "
                  "no parastā mērķis apstāsies."),

    Varianti("Bez rēķināšanas", [
        {"jaut": "Kurš skaitlis ir lielāks: 50 · {4|5} vai 50?",
         "opcijas": ["50", "50 · {4|5}", "Abi vienādi", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "{4|5} ir mazāks par 1."},
        {"jaut": "Kurš skaitlis ir lielāks: 40 · {9|8} vai 40?",
         "opcijas": ["40 · {9|8}", "40", "Abi vienādi", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "{9|8} ir lielāks par 1."},
        {"jaut": "Kad reizinājums ir tieši tāds pats kā sākotnējais skaitlis?",
         "opcijas": ["Kad reizinātājs ir 1", "Kad reizinātājs ir 0",
                     "Nekad", "Kad skaitlis ir pāra"],
         "pareizi": 0,
         "padoms": "{5|5} arī ir 1."},
        {"jaut": "Kas notiek, dalot skaitli ar {1|2}?",
         "opcijas": ["Tas kļūst divreiz lielāks",
                     "Tas kļūst divreiz mazāks",
                     "Tas nemainās", "Tas kļūst par nulli"],
         "pareizi": 0,
         "padoms": "Cik pusīšu ietilpst?"},
    ], pamats=4),

    Kopsavilkums([
        "Paskaidroju, kāpēc reizinājums ar īstu daļu ir mazāks.",
        "Pirms rēķināšanas pasaku, vai rezultāts augs vai sarūks.",
        "Zinu robežu: reizinātājs mazāks, vienāds vai lielāks par 1.",
        "Saprotu, ka dalot ar īstu daļu rezultāts aug.",
    ]),

    Majas([
        "Izdomā trīs reizinājumus, kuru rezultāts ir mazāks par pirmo "
        "skaitli.",
        "Pieraksti reizinājumu, kura rezultāts ir tieši tāds pats kā "
        "sākotnējais skaitlis.",
        "Paskaidro kādam mājās, kāpēc «reizinot vienmēr kļūst vairāk» nav "
        "taisnība.",
    ]),
]
