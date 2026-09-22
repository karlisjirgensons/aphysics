# -*- coding: utf-8 -*-
"""5. klase, 151. stunda: «Cik grādu ir sektoram?»

Šeit satiekas 112. stunda un procenti: pilns leņķis ir 360°, un procenti ir
simtdaļas, tāpēc viens procents ir 3,6°. No šī viena skaitļa izriet visa
sektoru diagrammas zīmēšana, un tieši tāpēc stunda ir par rēķinu, ne par
zīmuli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis, rinkis)

TEMA = "Cik grādu ir sektoram?"

MERKIS = ("Iemācīsimies aprēķināt sektoru leņķu lielumus, izmantojot "
          "zināšanas par leņķiem.")

SATURS = [
    Sakums("Viens procents ir 3,6 grādi",
           zimejums=rinkis(sektors=90, virsraksts="25 % ir 90°"),
           paraksts="360 : 100 = 3,6, tāpēc 25 % ir 25 · 3,6 = 90°.",
           fakti=["Pilns leņķis ir 360°.",
                  "Viss riņķis ir arī 100 %.",
                  "Tātad 1 % ir 3,6°."]),

    Doma("No procentiem uz grādiem",
         "Sektora leņķi aprēķina, procentu skaitu reizinot ar 3,6, jo viens "
         "procents no pilna leņķa ir 3,6°.",
         soli=[
             "Pieraksti sektora procentu skaitu.",
             "Reizini to ar 3,6.",
             "Pieraksti rezultātu ar grādu zīmi.",
             "Biežākos procentus atceries: 25 % ir 90°, 50 % ir 180°.",
             "Pārbaudi: visu sektoru leņķiem kopā jādod 360°.",
         ],
         pieze="Ērtāk ir rēķināt caur daļām: 25 % ir ceturtdaļa, tātad "
               "360 : 4 = 90°. Ar 10 % vēl ātrāk - 360 : 10 = 36°, un tad "
               "vajadzīgo reizina."),

    Paraugs("Cik grādu ir 25 % sektoram?",
            uzd="Aprēķini sektora leņķi.",
            soli=[
                ("Viss riņķis ir 360°",
                 "Pilns leņķis."),
                ("25 % = {1|4}",
                 "Ceturtdaļa."),
                ("360 : 4 = 90",
                 "Sektora leņķis."),
                ("Vai arī: 25 · 3,6 = 90",
                 "Tas pats caur vienu procentu."),
            ],
            atbilde="25 % sektoram ir 90°"),

    Ievadi("Aprēķini sektora leņķi", [
        {"jaut": "Cik grādu ir 25 % sektoram?",
         "atb": ["90"], "padoms": "360 : 4."},
        {"jaut": "Cik grādu ir 50 % sektoram?",
         "atb": ["180"], "padoms": "360 : 2."},
        {"jaut": "Cik grādu ir 10 % sektoram?",
         "atb": ["36"], "padoms": "360 : 10."},
        {"jaut": "Cik grādu ir 20 % sektoram?",
         "atb": ["72"], "padoms": "36 · 2."},
        {"jaut": "Cik grādu ir 75 % sektoram?",
         "atb": ["270"], "padoms": "90 · 3."},
        {"jaut": "Cik grādu ir 1 % sektoram? Ieraksti skaitli.",
         "atb": ["3,6"], "padoms": "360 : 100."},
        {"jaut": "Cik grādu ir 5 % sektoram?",
         "atb": ["18"], "padoms": "3,6 · 5."},
        {"jaut": "Cik procentu ir 180° sektoram?",
         "atb": ["50"], "padoms": "Puse riņķa."},
    ], pamats=4,
        ievads="Procentus reizini ar 3,6 vai rēķini caur daļu."),

    Zimejums("Biežākie sektori",
             restis([["10 %", "25 %", "50 %"],
                     ["36°", "90°", "180°"]],
                    virsraksts="Procenti un to leņķi"),
             paskaidro="Trīs pāri, kurus ir vērts zināt no galvas: no tiem "
                       "var salikt gandrīz jebkuru diagrammu.",
             ievads="Šos leņķus nav vērts rēķināt katru reizi."),

    Varianti("Cik grādu tas ir?", [
        {"jaut": "Cik grādu ir viens procents no pilna leņķa?",
         "opcijas": ["3,6°", "1°", "36°", "10°"],
         "pareizi": 0,
         "padoms": "360 : 100."},
        {"jaut": "25 % sektoram ir...",
         "opcijas": ["90°", "25°", "180°", "36°"],
         "pareizi": 0,
         "padoms": "Ceturtdaļa riņķa."},
        {"jaut": "10 % sektoram ir...",
         "opcijas": ["36°", "10°", "3,6°", "60°"],
         "pareizi": 0,
         "padoms": "360 : 10."},
        {"jaut": "Visu sektoru leņķiem kopā jādod...",
         "opcijas": ["360°", "180°", "100°", "90°"],
         "pareizi": 0,
         "padoms": "Pilns leņķis."},
        {"jaut": "50 % sektoram ir...",
         "opcijas": ["180°", "90°", "50°", "360°"],
         "pareizi": 0,
         "padoms": "Puse riņķa."},
        {"jaut": "Kā pārbauda visus aprēķinātos leņķus?",
         "opcijas": ["Saskaita tos - jāsanāk 360°",
                     "Salīdzina ar 100",
                     "Dala ar 3,6",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Pilns leņķis."},
    ], pamats=4),

    Pasaule("Aptaujas rezultāti grādos",
            Ievadi("", [
                {"jaut": "50 % izvēlējās futbolu. Cik grādu ir šis sektors?",
                 "atb": ["180"], "padoms": "360 : 2."},
                {"jaut": "25 % izvēlējās basketbolu. Cik grādu ir šis "
                         "sektors?",
                 "atb": ["90"], "padoms": "360 : 4."},
                {"jaut": "Pārējie 25 % izvēlējās volejbolu. Cik grādu?",
                 "atb": ["90"], "padoms": "360 : 4."},
                {"jaut": "Cik grādu ir visi trīs sektori kopā?",
                 "atb": ["360"], "padoms": "180 + 90 + 90."},
            ]),
            pavediens="skola",
            konteksts="Pirms diagrammu zīmē, katram aptaujas rezultātam "
                      "aprēķina savu leņķi.",
            kapec="Bez leņķiem transportieris nav ko likt uz papīra."),

    Kopsavilkums([
        "Zinu, ka viens procents no pilna leņķa ir 3,6°.",
        "Aprēķinu sektora leņķi no procentiem.",
        "Atceros biežākos pārus: 25 % ir 90°, 50 % ir 180°.",
        "Pārbaudu, vai visu sektoru leņķi kopā dod 360°.",
    ]),

    Majas([
        "Aprēķini leņķus sektoriem 40 %, 30 % un 30 %.",
        "Pārbaudi, vai to summa ir 360°.",
        "Atrodi diagrammu grāmatā un novērtē viena sektora leņķi.",
    ]),
]
