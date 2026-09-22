# -*- coding: utf-8 -*-
"""5. klase, 75. stunda: «Cik bija sākumā?»

Apgrieztais uzdevums, un tieši tur skolēni kļūdās visbiežāk: zināms nevis
veselais, bet daļas vērtība. Paņēmiens ir tas pats, tikai darbības apmainītas
vietām - vispirms dala ar skaitītāju, tad reizina ar saucēju. Tāpēc stunda
māca vienu ieradumu: vispirms atrod vienu daļu, tikai tad meklē veselo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Cik bija sākumā?"

MERKIS = ("Iemācīsimies aprēķināt veselo, ja zināma tā daļas vērtība, "
          "spriežot no beigām.")

SATURS = [
    Sakums("Nobraukti 180 km - cik garš ir ceļš?",
           zimejums=dala(4, 3, "3/4 = 180 km"),
           paraksts="Ja trīs ceturtdaļas ir 180 km, viena ceturtdaļa ir "
                    "60 km.",
           fakti=["Šoreiz zināms nevis kopgarums, bet daļas vērtība.",
                  "Vispirms jāatrod, cik ir viena daļa.",
                  "Tikai tad var pateikt, cik ir viss ceļš."]),

    Doma("Vispirms viena daļa, tad veselais",
         "Ja zināma daļas vērtība, veselo atrod, dalot šo vērtību ar "
         "skaitītāju un reizinot ar saucēju.",
         soli=[
             "Pieraksti, kāda daļa ir zināma un kāda ir tās vērtība.",
             "Dali vērtību ar skaitītāju - iegūsi vienu daļu.",
             "Reizini vienu daļu ar saucēju - iegūsi veselo.",
             "Pārbaudi: vai no veselā tiešām iznāk dotā vērtība.",
         ],
         pieze="Salīdzini ar iepriekšējo stundu: tur veselo dalīja ar "
               "saucēju un reizināja ar skaitītāju; te - otrādi. Tāpēc "
               "vienmēr vispirms jānoskaidro, kurš skaitlis ir zināms."),

    Paraugs("{3|4} ceļa ir 180 km. Cik garš ir viss ceļš?",
            uzd="Aprēķini visa ceļa garumu.",
            soli=[
                ("Zināma daļa {3|4}, tās vērtība 180 km",
                 "Vispirms saprot, kas dots."),
                ("180 : 3 = 60 (km)",
                 "Viena ceturtdaļa ceļa."),
                ("60 · 4 = 240 (km)",
                 "Visas četras ceturtdaļas."),
                ("Pārbaude: 240 : 4 · 3 = 180",
                 "No veselā iznāk dotā vērtība."),
            ],
            atbilde="Viss ceļš ir 240 km"),

    Ievadi("Atrodi veselo", [
        {"jaut": "{1|2} ceļa ir 30 km. Cik kilometru ir viss ceļš?",
         "atb": ["60"], "padoms": "30 · 2."},
        {"jaut": "{1|3} ceļa ir 40 km. Cik kilometru ir viss ceļš?",
         "atb": ["120"], "padoms": "40 · 3."},
        {"jaut": "{3|4} ceļa ir 180 km. Cik kilometru ir viss ceļš?",
         "atb": ["240"], "padoms": "180 : 3 · 4."},
        {"jaut": "{2|5} ceļa ir 80 km. Cik kilometru ir viss ceļš?",
         "atb": ["200"], "padoms": "80 : 2 · 5."},
        {"jaut": "{3|5} bagāžas ir 12 kg. Cik kilogramu ir visa bagāža?",
         "atb": ["20"], "padoms": "12 : 3 · 5."},
        {"jaut": "{2|3} laika ir 40 minūtes. Cik minūšu ir viss laiks?",
         "atb": ["60"], "padoms": "40 : 2 · 3."},
        {"jaut": "{5|6} degvielas ir 50 l. Cik litru ir pilna tvertne?",
         "atb": ["60"], "padoms": "50 : 5 · 6."},
        {"jaut": "{4|7} summas ir 80 €. Cik eiro ir visa summa?",
         "atb": ["140"], "padoms": "80 : 4 · 7."},
    ], pamats=4,
        ievads="Dali ar skaitītāju, reizini ar saucēju - tieši otrādi nekā "
               "iepriekš."),

    Zimejums("Viena ceturtdaļa ir 60 km",
             dala(4, 1, "1/4 = 60 km"),
             paskaidro="Kad zināms viens gabals, viss pārējais ir "
                       "reizināšana: četri tādi gabali ir 240 km.",
             ievads="Ceļš no daļas uz veselo iet caur vienu daļu."),

    Varianti("Kurš rēķins te vajadzīgs?", [
        {"jaut": "Zināma daļas vērtība. Kā atrod veselo?",
         "opcijas": ["Dala ar skaitītāju, reizina ar saucēju",
                     "Dala ar saucēju, reizina ar skaitītāju",
                     "Reizina ar skaitītāju",
                     "Dala ar saucēju"],
         "pareizi": 0,
         "padoms": "Vispirms viena daļa."},
        {"jaut": "{2|3} no skaitļa ir 20. Cik ir viss skaitlis?",
         "opcijas": ["30", "40", "60", "10"],
         "pareizi": 0,
         "padoms": "20 : 2 · 3."},
        {"jaut": "{1|5} no skaitļa ir 7. Cik ir viss skaitlis?",
         "opcijas": ["35", "12", "7", "5"],
         "pareizi": 0,
         "padoms": "7 · 5."},
        {"jaut": "Kā pārbaudīt atbildi?",
         "opcijas": ["No atrastā veselā aprēķināt doto daļu",
                     "Saskaitīt abus skaitļus",
                     "Saīsināt daļu",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Jāiznāk dotajai vērtībai."},
        {"jaut": "Veselais vienmēr ir...",
         "opcijas": ["Lielāks par savas daļas vērtību",
                     "Mazāks par savas daļas vērtību",
                     "Vienāds ar to",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Daļa ir gabals no veselā."},
        {"jaut": "{3|8} no summas ir 60 €. Cik ir viena astotdaļa?",
         "opcijas": ["20 €", "60 €", "180 €", "8 €"],
         "pareizi": 0,
         "padoms": "60 : 3."},
    ], pamats=4),

    Pasaule("Cik garš bija maršruts?",
            Ievadi("", [
                {"jaut": "Nobraukta {2|5} maršruta, tas ir 60 km. Cik "
                         "kilometru ir viss maršruts?",
                 "atb": ["150"], "padoms": "60 : 2 · 5."},
                {"jaut": "Izlietota {3|4} degvielas, tas ir 45 l. Cik litru "
                         "bija pilnā tvertnē?",
                 "atb": ["60"], "padoms": "45 : 3 · 4."},
                {"jaut": "Pagājusi {5|6} brauciena laika, tas ir 100 minūtes. "
                         "Cik minūtes ilgst viss brauciens?",
                 "atb": ["120"], "padoms": "100 : 5 · 6."},
                {"jaut": "Iztērēta {2|7} naudas, tas ir 40 €. Cik eiro bija "
                         "sākumā?",
                 "atb": ["140"], "padoms": "40 : 2 · 7."},
            ]),
            pavediens="celojums",
            konteksts="Ceļā bieži zināms tikai nobrauktais gabals, bet "
                      "jāzina viss maršruts.",
            kapec="No daļas uz veselo var aiziet tikpat droši kā otrādi."),

    Kopsavilkums([
        "Atpazīstu uzdevumu, kurā dota daļas vērtība, nevis veselais.",
        "Atrodu vienas daļas vērtību, dalot ar skaitītāju.",
        "Aprēķinu veselo, reizinot vienu daļu ar saucēju.",
        "Pārbaudu atbildi, aprēķinot doto daļu no atrastā veselā.",
    ]),

    Majas([
        "{3|7} no skaitļa ir 21. Atrodi šo skaitli.",
        "Izdomā uzdevumu, kurā zināma daļas vērtība, un atrisini to.",
        "Pieraksti, ar ko šī stunda atšķiras no iepriekšējās.",
    ]),
]
