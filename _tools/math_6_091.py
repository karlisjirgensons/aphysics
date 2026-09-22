# -*- coding: utf-8 -*-
"""6. klase, 91. stunda: «Cik liela ir vielas masas daļa?»

Mikrotemata noslēgums ar dabaszinātņu saturu. Šķīduma koncentrācija ir tas
pats procentu rēķins, tikai citā vārdā - un tieši tādā veidā tas parādīsies
ķīmijā un fizikā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Cik liela ir vielas masas daļa?"

MERKIS = ("Lietosim procentus uzdevumā ar dabaszinātņu saturu.")

SATURS = [
    Sakums("Jūras ūdenī ir 3,5 % sāls",
           fakti=["Masas daļa ir vielas masa pret visa šķīduma masu.",
                  "1 kg jūras ūdens satur apmēram 35 g sāls.",
                  "Tā pati formula strādā visos šķīdumos."]),

    Doma("Viela pret visu šķīdumu",
         "Vielas masas daļa procentos ir vielas masa, dalīta ar visa "
         "šķīduma masu un reizināta ar 100.",
         soli=[
             "Pieraksti vielas masu un šķīduma kopējo masu.",
             "Pārbaudi, vai šķīduma masā ir ieskaitīta arī pati viela.",
             "Pieraksti daļu: viela pret šķīdumu.",
             "Reizini ar 100.",
             "Pārbaudi, vai rezultāts ir mazāks par 100 %.",
         ],
         pieze="Biežākā kļūda: dalīt ar ūdens masu, nevis ar visa šķīduma "
               "masu. Ja 20 g sāls izšķīdina 180 g ūdens, šķīduma masa ir "
               "200 g, nevis 180 g."),

    Paraugs("Aprēķini koncentrāciju",
            uzd="20 g sāls izšķīdina 180 g ūdens. Cik liela ir sāls masas "
                "daļa procentos?",
            soli=[
                ("Šķīduma masa: 20 + 180 = 200 g",
                 "Sāls un ūdens kopā."),
                ("{20|200} = {1|10}",
                 "Viela pret šķīdumu."),
                ("{1|10} = 0,1",
                 "Decimālpierakstā."),
                ("0,1 · 100 = 10 %",
                 "Masas daļa."),
            ],
            atbilde="10 %"),

    Ievadi("Aprēķini masas daļu", [
        {"jaut": "20 g sāls un 180 g ūdens. Cik gramu ir šķīdums?",
         "atb": ["200"], "padoms": "20 + 180."},
        {"jaut": "Cik procenti ir sāls masas daļa?",
         "atb": ["10"], "padoms": "{20|200}."},
        {"jaut": "5 g cukura un 95 g ūdens. Cik procenti ir cukura masas "
                 "daļa?",
         "atb": ["5"], "padoms": "Šķīdums 100 g."},
        {"jaut": "1 kg jūras ūdens satur 3,5 % sāls. Cik gramu tas ir?",
         "atb": ["35"], "padoms": "1000 · 0,035."},
        {"jaut": "Šķīdumā 400 g, sāls 8 %. Cik gramu sāls?",
         "atb": ["32"], "padoms": "8 · 4."},
        {"jaut": "Šķīdumā 400 g, sāls 8 %. Cik gramu ūdens?",
         "atb": ["368"], "padoms": "400 − 32."},
    ], pamats=4,
        ievads="Šķīduma masā ietilpst arī pati viela."),

    Pasaule("Cik sāls ir traukā?",
            Kustiba("", [
                {"jaut": "500 g šķīduma, sāls 4 %. Cik gramu sāls?",
                 "atb": 20, "beigas": 100, "iedala": 20, "mers": "grami",
                 "merkis": "sāls masa", "objekts": "Svari",
                 "padoms": "1 % ir 5 g."},
                {"jaut": "1000 g šķīduma, sāls 3,5 %. Cik gramu sāls?",
                 "atb": 35, "beigas": 100, "iedala": 20, "mers": "grami",
                 "merkis": "sāls masa", "objekts": "Svari",
                 "padoms": "1 % ir 10 g."},
                {"jaut": "250 g šķīduma, sāls 20 %. Cik gramu sāls?",
                 "atb": 50, "beigas": 100, "iedala": 20, "mers": "grami",
                 "merkis": "sāls masa", "objekts": "Svari",
                 "padoms": "Piektdaļa."},
                {"jaut": "800 g šķīduma, sāls 10 %. Cik gramu sāls?",
                 "atb": 80, "beigas": 100, "iedala": 20, "mers": "grami",
                 "merkis": "sāls masa", "objekts": "Svari",
                 "padoms": "Desmitdaļa."},
            ]),
            pavediens="planeta",
            konteksts="Okeāna ūdens sāļumu mēra tieši tā - gramos uz "
                      "kilogramu ūdens.",
            kapec="Masas daļa ir procenti, tikai ar citu nosaukumu."),

    Petijums("Pagatavo 10 % šķīdumu",
             vajag="svari vai karote, ūdens, sāls, glāze",
             soli=[
                 "Nosver 10 g sāls.",
                 "Aprēķini, cik gramu ūdens vajag 10 % šķīdumam.",
                 "Ielej ūdeni un izšķīdini sāli.",
                 "Pieraksti abas masas un pārbaudi savu aprēķinu.",
             ],
             secinajums="Ja sāls ir 10 g un šķīdumam jābūt 100 g, ūdens "
                        "vajag 90 g - nevis 100 g."),

    Varianti("Ar ko dalīt?", [
        {"jaut": "Masas daļu rēķina, dalot vielas masu ar...",
         "opcijas": ["visa šķīduma masu", "ūdens masu",
                     "100", "vielas masu"],
         "pareizi": 0,
         "padoms": "Kopums ir viss šķīdums."},
        {"jaut": "20 g sāls un 180 g ūdens. Kāda ir šķīduma masa?",
         "opcijas": ["200 g", "180 g", "160 g", "20 g"],
         "pareizi": 0,
         "padoms": "Abas masas kopā."},
        {"jaut": "Lai pagatavotu 200 g 5 % šķīduma, sāls vajag...",
         "opcijas": ["10 g", "5 g", "20 g", "40 g"],
         "pareizi": 0,
         "padoms": "1 % ir 2 g."},
        {"jaut": "Cik gramu ūdens vajag tam pašam šķīdumam?",
         "opcijas": ["190 g", "200 g", "195 g", "180 g"],
         "pareizi": 0,
         "padoms": "200 − 10."},
    ], pamats=4),

    Kopsavilkums([
        "Aprēķinu vielas masas daļu procentos.",
        "Zinu, ka šķīduma masā ietilpst arī pati viela.",
        "Aprēķinu vielas masu no procentiem un šķīduma masas.",
        "Pagatavoju šķīdumu ar doto koncentrāciju.",
    ]),

    Majas([
        "Aprēķini, cik sāls vajag 300 g 5 % šķīdumam.",
        "Atrodi, cik procentu sāls ir tavā mājās lietotajā ūdenī vai "
        "produktā.",
        "Pieraksti, kāpēc nedrīkst dalīt ar ūdens masu.",
    ]),
]
