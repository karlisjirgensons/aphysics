# -*- coding: utf-8 -*-
"""3. klase, 100. stunda: «Kā saskaitīt centus?»

Decimāldaļu saskaitīšana pirmo reizi - un naudā tā ir gandrīz acīmredzama:
saskaita centus, un, kad to sanāk vairāk par 100, rodas vēl viens eiro.
Tieši tā pati pāreja, kas veselos skaitļos notiek pie desmita.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā saskaitīt centus?"

MERKIS = ("Ar naudas modeļiem saskaitīsim vienkāršas decimāldaļas un "
          "skaidrosim līdzību ar veselo skaitļu saskaitīšanu.")

SATURS = [
    Sakums("Kas notiek, kad centu sanāk vairāk par simtu?",
           zimejums=restis([["0,75", "+", "0,50", "=", "1,25"],
                            ["75 ct", "+", "50 ct", "=", "125 ct"]],
                           "abos pierakstos tas pats"),
           paraksts="125 centi ir viens eiro un vēl 25 centi.",
           fakti=["Centus saskaita tāpat kā veselus skaitļus.",
                  "Kad sanāk vairāk par 100, rodas vēl viens eiro."]),

    Doma("Saskaiti centus, tad pārvērt eiro",
         "0,75 + 0,50 ir 75 + 50 = 125 centi, tas ir, 1,25 eiro.",
         soli=[
             "Pārvērt abas summas centos.",
             "Saskaiti centus kā parastus skaitļus.",
             "Ja iznāk vairāk par 100, atdali veselos eiro.",
             "Pieraksti atbildi ar komatu.",
         ],
         pieze="Rakstot vienu zem otra, komats jāliek zem komata - tad "
               "centi sakrīt ar centiem, bet eiro ar eiro."),

    Slidnis("Kā aug summa",
            soli=[
                {"v": "0,75", "teksts": "75 centi.", "josla": 38},
                {"v": "+ 0,25 = 1,00",
                 "teksts": "Sanāca tieši viens eiro.", "josla": 50},
                {"v": "+ 0,50 = 1,50",
                 "teksts": "Pusotrs eiro.", "josla": 75},
                {"v": "+ 0,50 = 2,00",
                 "teksts": "Divi eiro.", "josla": 100},
            ],
            ievads="Katrs solis pieliek vēl centus."),

    Paraugs("Cik ir 0,75 + 0,50?",
            uzd="Saskaiti 0,75 eiro un 0,50 eiro.",
            soli=[
                ("75 ct + 50 ct",
                 "Abas summas pārvērš centos."),
                ("75 + 50 = 125",
                 "Saskaita kā veselus skaitļus."),
                ("125 ct = 1,25 eiro",
                 "100 centi ir viens eiro, paliek 25."),
            ],
            atbilde="1,25 eiro"),

    Ievadi("Saskaiti naudu", [
        {"jaut": "0,75 + 0,50 = ? Raksti eiro ar komatu.",
         "atb": ["1,25", "1.25"], "padoms": "75 + 50 = 125 ct."},
        {"jaut": "0,30 + 0,40 = ? Raksti eiro ar komatu.",
         "atb": ["0,7", "0,70", "0.7", "0.70"], "padoms": "30 + 40 = 70 ct."},
        {"jaut": "1,20 + 0,80 = ? Raksti eiro ar komatu.",
         "atb": ["2", "2,0", "2,00", "2.0"], "padoms": "120 + 80 = 200 ct."},
        {"jaut": "Cik centu ir 0,45 + 0,35?", "atb": ["80"],
         "padoms": "45 + 35."},
        {"jaut": "Cik centu ir 1,50 − 0,75?", "atb": ["75"],
         "padoms": "150 − 75."},
        {"jaut": "0,60 + 0,60 = ? Raksti eiro ar komatu.",
         "atb": ["1,2", "1,20", "1.2", "1.20"], "padoms": "120 ct."},
    ], pamats=4),

    Zimejums("Komats zem komata",
             restis([["0,", "7", "5"],
                     ["0,", "5", "0"],
                     ["1,", "2", "5"]],
                    "saskaitīšana stabiņā"),
             paskaidro="Komats vienmēr stāv zem komata - tad desmitdaļas "
                       "sakrīt ar desmitdaļām.",
             ievads="Tā izskatās pieraksts stabiņā."),

    Varianti("Cik sanāk?", [
        {"jaut": "Cik ir 0,25 + 0,25?",
         "opcijas": ["0,50", "0,25", "0,05", "2,50"],
         "pareizi": 0, "padoms": "25 + 25 = 50 ct."},
        {"jaut": "Cik ir 0,90 + 0,20?",
         "opcijas": ["1,10", "0,110", "1,01", "0,92"],
         "pareizi": 0, "padoms": "90 + 20 = 110 ct."},
        {"jaut": "Kur liek komatu, rakstot stabiņā?",
         "opcijas": ["Zem komata", "Pa labi", "Pa kreisi", "Nekur"],
         "pareizi": 0, "padoms": "Vietas jāsakrīt."},
        {"jaut": "Cik ir 2,00 − 0,45?",
         "opcijas": ["1,55", "1,45", "2,45", "1,65"],
         "pareizi": 0, "padoms": "200 − 45 = 155 ct."},
    ], pamats=4),

    Pasaule("Cik maksā viss grozs?",
            Ievadi("", [
                {"jaut": "Maize 0,85 eiro, piens 0,95 eiro. Cik centu kopā?",
                 "atb": ["180"], "padoms": "85 + 95."},
                {"jaut": "Cik eiro tas ir? Raksti ar komatu.",
                 "atb": ["1,8", "1,80", "1.8", "1.80"], "padoms": "180 ct."},
                {"jaut": "Iedeva 2 eiro. Cik centu jāatdod atpakaļ?",
                 "atb": ["20"], "padoms": "200 − 180."},
                {"jaut": "Cik centu maksās divas maizes pa 0,85 eiro?",
                 "atb": ["170"], "padoms": "2 · 85."},
            ]),
            pavediens="veikals",
            konteksts="Kasē summu saskaita centos, un tikai beigās to parāda "
                      "eiro ar komatu.",
            kapec="Centos rēķināt ir vieglāk - tur nav komata, ko sajaukt."),

    Kopsavilkums([
        "Saskaitu un atņemu naudas summas.",
        "Pārvēršu eiro centos un saskaitu kā veselus skaitļus.",
        "Pierakstu atbildi ar komatu.",
        "Zinu, ka stabiņā komats stāv zem komata.",
    ]),

    Majas([
        "Saskaiti trīs cenas no mājas čeka un pārbaudi ar kopsummu.",
        "Izrēķini 0,65 + 0,45 divējādi: centos un eiro.",
        "Uzraksti divas summas, kuru kopsumma ir tieši 1 eiro.",
    ]),
]
