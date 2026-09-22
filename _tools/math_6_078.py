# -*- coding: utf-8 -*-
"""6. klase, 78. stunda: «Kā mainās tilpums, mainot vienu izmēru?»

Turpinājums iepriekšējai stundai, bet grūtāks: ja mainās tikai viens izmērs,
tilpums mainās tikpat reižu, nevis kubā. Salīdzinājums ar iepriekšējo stundu
te ir svarīgāks par pašu atbildi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kā mainās tilpums, mainot vienu izmēru?"

MERKIS = ("Spriedīsim par tilpuma izmaiņām, mainot vienu vai vairākus "
          "izmērus.")

SATURS = [
    Sakums("Viens izmērs - viens reizinātājs",
           fakti=["Ja augstumu palielina 2 reizes, tilpums aug 2 reizes.",
                  "Ja divus izmērus - tilpums aug 4 reizes.",
                  "Ja visus trīs - 8 reizes; tā bija iepriekšējā stundā."]),

    Doma("Saskaiti, cik izmēru mainījās",
         "Tilpums mainās tik reižu, cik ir visu mainīto izmēru reizinātāju "
         "reizinājums; nemainītie izmēri tilpumu neietekmē.",
         soli=[
             "Pieraksti, kuri izmēri mainās un cik reižu.",
             "Sareizini visus šos reizinātājus.",
             "Reizini sākotnējo tilpumu ar iegūto skaitli.",
             "Pārbaudi ar tiešu aprēķinu.",
             "Salīdzini ar gadījumu, kad mainās visi trīs izmēri.",
         ],
         pieze="Ja vienu izmēru palielina 2 reizes, bet otru samazina "
               "2 reizes, tilpums nemainās: 2 · {1|2} = 1. Tāpēc kaste var "
               "mainīt formu, saglabājot ietilpību."),

    Slidnis("Mainās tikai augstums",
            [{"v": "augstums 2 cm", "teksts": "tilpums 40 cm³", "josla": 25},
             {"v": "augstums 4 cm", "teksts": "tilpums 80 cm³", "josla": 50},
             {"v": "augstums 6 cm", "teksts": "tilpums 120 cm³",
              "josla": 75},
             {"v": "augstums 8 cm", "teksts": "tilpums 160 cm³",
              "josla": 100}],
            ievads="Pamats paliek 5 x 4 cm, mainās tikai augstums. Tilpums "
                   "aug tieši tikpat reižu - vienmērīgi."),

    Paraugs("Divi izmēri mainās",
            uzd="Kastes tilpums ir 60 cm³. Garumu palielina 2 reizes, "
                "augstumu - 3 reizes. Kāds būs jaunais tilpums?",
            soli=[
                ("Mainās divi izmēri: 2 reizes un 3 reizes",
                 "Platums paliek tas pats."),
                ("2 · 3 = 6",
                 "Kopējais reizinātājs."),
                ("60 · 6 = 360 cm³",
                 "Jaunais tilpums."),
                ("Pārbaude: ja visi trīs augtu 2 reizes, būtu 60 · 8 = 480",
                 "Divi izmēri dod mazāku pieaugumu nekā trīs."),
            ],
            atbilde="360 cm³"),

    Ievadi("Cik reižu mainās tilpums?", [
        {"jaut": "Augstumu palielina 2 reizes. Cik reižu aug tilpums?",
         "atb": ["2"], "padoms": "Viens izmērs - viens reizinātājs."},
        {"jaut": "Garumu un platumu palielina 2 reizes. Cik reižu aug "
                 "tilpums?",
         "atb": ["4"], "padoms": "2 · 2."},
        {"jaut": "Tilpums bija 30 cm³, augstumu palielina 3 reizes. Cik cm³ "
                 "tagad?",
         "atb": ["90"], "padoms": "30 · 3."},
        {"jaut": "Tilpums bija 48 cm³, garumu samazina 2 reizes. Cik cm³ "
                 "tagad?",
         "atb": ["24"], "padoms": "48 : 2."},
        {"jaut": "Garumu palielina 2 reizes, augstumu samazina 2 reizes. Cik "
                 "reižu mainās tilpums?",
         "atb": ["1"], "padoms": "Tilpums nemainās."},
        {"jaut": "Tilpums bija 20 cm³; garumu palielina 3 reizes, platumu "
                 "2 reizes. Cik cm³ tagad?",
         "atb": ["120"], "padoms": "20 · 6."},
    ], pamats=4),

    Varianti("Kas notiks ar tilpumu?", [
        {"jaut": "Mainās tikai viens izmērs, 2 reizes. Tilpums...",
         "opcijas": ["aug 2 reizes", "aug 4 reizes",
                     "aug 8 reizes", "nemainās"],
         "pareizi": 0,
         "padoms": "Viens reizinātājs."},
        {"jaut": "Divus izmērus palielina 3 reizes. Tilpums aug...",
         "opcijas": ["9 reizes", "3 reizes", "27 reizes", "6 reizes"],
         "pareizi": 0,
         "padoms": "3 · 3."},
        {"jaut": "Vienu izmēru palielina 4 reizes, citu samazina 4 reizes. "
                 "Tilpums...",
         "opcijas": ["nemainās", "aug 16 reizes",
                     "samazinās 16 reizes", "aug 4 reizes"],
         "pareizi": 0,
         "padoms": "4 · {1|4} = 1."},
        {"jaut": "Kurš izmērs tilpumu neietekmē?",
         "opcijas": ["Neviens - visi trīs ietekmē",
                     "Augstums", "Platums", "Garums"],
         "pareizi": 0,
         "padoms": "Tilpums ir visu trīs reizinājums."},
    ], pamats=4),

    Pasaule("Kā pārveidot iepakojumu?",
            Ievadi("", [
                {"jaut": "Kaste 20 x 10 x 5 cm. Cik cm³ ir tilpums?",
                 "atb": ["1000", "1 000"], "padoms": "200 · 5."},
                {"jaut": "Augstumu palielina līdz 10 cm. Cik cm³ tagad?",
                 "atb": ["2000", "2 000"], "padoms": "Divas reizes vairāk."},
                {"jaut": "Garumu samazina līdz 10 cm, augstums paliek 10 cm. "
                         "Cik cm³ tagad?",
                 "atb": ["1000", "1 000"], "padoms": "10 · 10 · 10."},
                {"jaut": "Cik reižu mainījās tilpums salīdzinājumā ar "
                         "sākumu?",
                 "atb": ["1"], "padoms": "Tas ir tas pats tilpums."},
            ]),
            pavediens="veikals",
            konteksts="Ražotājs mēdz mainīt iepakojuma formu, saglabājot "
                      "saturu - viens izmērs aug, otrs sarūk.",
            kapec="Tilpums nemainās, ja reizinātāju reizinājums ir viens."),

    Kopsavilkums([
        "Spriežu par tilpuma izmaiņām, mainot vienu vai vairākus izmērus.",
        "Sareizinu visu mainīto izmēru reizinātājus.",
        "Zinu, kad tilpums nemainās, lai gan izmēri mainās.",
        "Salīdzinu ar gadījumu, kad mainās visi trīs izmēri.",
    ]),

    Majas([
        "Aprēķini, cik reižu mainīsies tilpums, ja divus izmērus palielinās "
        "2 reizes.",
        "Atrodi divus izmēru pārveidojumus, kas tilpumu atstāj nemainīgu.",
        "Pieraksti, kāpēc viens izmērs nemaina tilpumu kubā.",
    ]),
]
