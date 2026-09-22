# -*- coding: utf-8 -*-
"""6. klase, 82. stunda: «Kā aprēķināt, cik procenti?»

Pirmais īstais procentu rēķins un uzreiz tas, kas eksāmenā sagādā visvairāk
grūtību: nevis «cik ir 20 % no 50», bet «cik procenti no 50 ir 10». Ceļš ir
viens - vispirms daļa, tad simtdaļas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā aprēķināt, cik procenti?"

MERKIS = ("Iemācīsimies aprēķināt vienu skaitli kā otra skaitļa procentus un "
          "pierakstīt rezultātu.")

SATURS = [
    Sakums("Vispirms daļa, tad procenti",
           zimejums=dala(20, 5, "5 no 20"),
           paraksts="{5|20} = {1|4} = {25|100} = 25 %. Trīs soļi, viens "
                    "skaitlis.",
           fakti=["«Cik procenti» vienmēr nozīmē «kāda daļa no kopuma».",
                  "Vispirms pieraksta daļu: daļa pret kopumu.",
                  "Tad daļu pārvērš simtdaļās."]),

    Doma("Daļa pret kopumu, tad reiz 100",
         "Lai uzzinātu, cik procentu viens skaitlis ir no otra, to izdala ar "
         "kopumu un reizina ar 100.",
         soli=[
             "Nosaki, kurš skaitlis ir kopums - tas ir 100 %.",
             "Pieraksti daļu: dotais skaitlis pret kopumu.",
             "Saīsini daļu vai izdali skaitītāju ar saucēju.",
             "Reizini ar 100 - iegūsi procentus.",
             "Pārbaudi: vai rezultāts ir ticams?",
         ],
         pieze="Kopums ne vienmēr ir lielākais skaitlis tekstā. «No 20 "
               "skolēniem 5 kavēja» - kopums ir 20, nevis 5; tieši tāpēc "
               "vispirms jāatrod, kas ir 100 %."),

    Paraugs("Cik procenti no 20 ir 5?",
            uzd="Klasē ir 20 skolēni, no tiem 5 brauc ar autobusu. Cik "
                "procenti tas ir?",
            soli=[
                ("Kopums ir 20 skolēni",
                 "Tie ir 100 %."),
                ("{5|20}",
                 "Daļa pret kopumu."),
                ("{5|20} = {1|4} = 0,25",
                 "Saīsina vai izdala."),
                ("0,25 · 100 = 25 %",
                 "Simtdaļās."),
            ],
            atbilde="25 %"),

    Ievadi("Cik procentu tas ir?", [
        {"jaut": "Cik procenti no 20 ir 5?",
         "atb": ["25"], "padoms": "{5|20} = {1|4}."},
        {"jaut": "Cik procenti no 50 ir 10?",
         "atb": ["20"], "padoms": "{10|50} = {1|5}."},
        {"jaut": "Cik procenti no 40 ir 30?",
         "atb": ["75"], "padoms": "{30|40} = {3|4}."},
        {"jaut": "Cik procenti no 200 ir 50?",
         "atb": ["25"], "padoms": "{50|200} = {1|4}."},
        {"jaut": "Cik procenti no 25 ir 25?",
         "atb": ["100"], "padoms": "Viss kopums."},
        {"jaut": "Cik procenti no 80 ir 8?",
         "atb": ["10"], "padoms": "{8|80} = {1|10}."},
    ], pamats=4,
        ievads="Vispirms atrodi, kurš skaitlis ir kopums."),

    Varianti("Kurš skaitlis ir 100 %?", [
        {"jaut": "«No 30 uzdevumiem 6 bija grūti.» Kurš skaitlis ir 100 %?",
         "opcijas": ["30", "6", "24", "100"],
         "pareizi": 0,
         "padoms": "Kopums ir visi uzdevumi."},
        {"jaut": "Cik procenti no 30 ir 6?",
         "opcijas": ["20", "6", "24", "30"],
         "pareizi": 0,
         "padoms": "{6|30} = {1|5}."},
        {"jaut": "Skolēns rēķina {20|5} · 100 = 400 %. Kas nav labi?",
         "opcijas": ["Daļa pierakstīta otrādi", "Nepareizi saīsināts",
                     "Aizmirsts reizināt", "Viss pareizi"],
         "pareizi": 0,
         "padoms": "Daļa pret kopumu, ne otrādi."},
        {"jaut": "Ja rezultāts sanāk vairāk nekā 100 %, tas nozīmē...",
         "opcijas": ["daļa ir lielāka par kopumu",
                     "vienmēr kļūdu", "daļa ir maza",
                     "kopums ir nulle"],
         "pareizi": 0,
         "padoms": "Tā mēdz būt, piemēram, pieaugumā."},
    ], pamats=4),

    Pasaule("Cik procenti no klases?",
            Ievadi("", [
                {"jaut": "Klasē 25 skolēni, 5 spēlē basketbolu. Cik "
                         "procenti?",
                 "atb": ["20"], "padoms": "{5|25} = {1|5}."},
                {"jaut": "10 skolēni brauc ar velosipēdu. Cik procenti?",
                 "atb": ["40"], "padoms": "{10|25} = {2|5}."},
                {"jaut": "Cik procenti *nebrauc* ar velosipēdu?",
                 "atb": ["60"], "padoms": "100 − 40."},
                {"jaut": "Skolā 500 skolēnu, klasē 25. Cik procenti no "
                         "skolas ir šī klase?",
                 "atb": ["5"], "padoms": "{25|500} = {1|20}."},
            ]),
            pavediens="skola",
            konteksts="Klases datus salīdzina ar skolas datiem tikai "
                      "procentos - skaitļi paši par sevi neko nepasaka.",
            kapec="Procenti padara dažāda lieluma grupas salīdzināmas."),

    Zimejums("Divas grupas, viens mērs",
             dala(10, 4, "40 %"),
             paskaidro="Josla vienmēr ir 100 %, un iekrāsotā daļa ir tas, ko "
                       "meklējam - vienalga, vai kopumā ir 25 vai 500.",
             ievads="Procenti ļauj salīdzināt nevienāda lieluma grupas."),

    Kopsavilkums([
        "Atrodu, kurš skaitlis ir kopums jeb 100 %.",
        "Pierakstu daļu: dotais skaitlis pret kopumu.",
        "Pārvēršu daļu procentos.",
        "Pārbaudu, vai rezultāts ir ticams.",
    ]),

    Majas([
        "Izrēķini, cik procenti no tavas klases ir zēni.",
        "Atrodi, cik procenti no nedēļas ir divas dienas.",
        "Pieraksti uzdevumu, kurā kopums nav lielākais skaitlis tekstā.",
    ]),
]
