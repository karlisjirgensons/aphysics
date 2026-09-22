# -*- coding: utf-8 -*-
"""6. klase, 83. stunda: «Kuras vienādības jāzina no galvas?»

Stunda par ātrumu. Pieci procenti, kurus zina no galvas, atrisina lielāko
daļu sadzīves uzdevumu bez pildspalvas - un tieši tie visbiežāk parādās
veikalā, ziņās un eksāmenā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kuras vienādības jāzina no galvas?"

MERKIS = ("Lietosim vienādības 50 % = puse, 25 % = ceturtdaļa, 20 % = "
          "piektdaļa aprēķinos.")

SATURS = [
    Sakums("Pieci procenti, kurus neaizmirst",
           zimejums=restis([["50 %", "25 %", "20 %", "10 %", "1 %"],
                            ["1/2", "1/4", "1/5", "1/10", "1/100"]]),
           paraksts="Ja šīs piecas vienādības zina no galvas, lielāko daļu "
                    "uzdevumu var izrēķināt bez pildspalvas.",
           fakti=["50 % ir puse: dala ar 2.",
                  "25 % ir ceturtdaļa: dala ar 4.",
                  "10 % ir desmitdaļa: pārceļ komatu."]),

    Doma("Dali, nevis reizini",
         "Zināmos procentus rēķina ar dalīšanu: 50 % ir dalīt ar 2, 25 % - "
         "ar 4, 20 % - ar 5, 10 % - ar 10.",
         soli=[
             "Paskaties, vai procents ir viens no zināmajiem.",
             "Ja ir - dali kopumu ar attiecīgo skaitli.",
             "Ja nav - sadali to zināmo summā vai starpībā.",
             "Pieraksti atbildi.",
             "Pārbaudi ar novērtējumu.",
         ],
         pieze="Arī nezināmus procentus var salikt no zināmiem: 30 % ir "
               "25 % + 5 %, bet 15 % ir 10 % + 5 %. Piecus procentus iegūst, "
               "uz pusēm daloties desmit procentus."),

    Paraugs("Trīs procenti galvā",
            uzd="Cik ir 50 %, 25 % un 10 % no 80?",
            soli=[
                ("50 % no 80: 80 : 2 = 40",
                 "Puse."),
                ("25 % no 80: 80 : 4 = 20",
                 "Ceturtdaļa."),
                ("10 % no 80: 80 : 10 = 8",
                 "Desmitdaļa."),
                ("Pārbaude: 40 + 20 + 8 = 68, tas ir 85 % no 80",
                 "Procentu summa atbilst daļu summai."),
            ],
            atbilde="40, 20 un 8"),

    Ievadi("Rēķini galvā", [
        {"jaut": "Cik ir 50 % no 80?",
         "atb": ["40"], "padoms": "80 : 2."},
        {"jaut": "Cik ir 25 % no 80?",
         "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "Cik ir 20 % no 80?",
         "atb": ["16"], "padoms": "80 : 5."},
        {"jaut": "Cik ir 10 % no 45?",
         "atb": ["4,5", "4.5"], "padoms": "Komats pa kreisi."},
        {"jaut": "Cik ir 1 % no 600?",
         "atb": ["6"], "padoms": "600 : 100."},
        {"jaut": "Cik ir 30 % no 60?",
         "atb": ["18"], "padoms": "25 % ir 15, 5 % ir 3."},
    ], pamats=4,
        ievads="Katram uzdevumam padomā, ar ko dalīt."),

    Pasaule("Cik maksās ar atlaidi?",
            Kustiba("", [
                {"jaut": "Prece maksā 60 €, atlaide 50 %. Cik eiro ir "
                         "atlaide?",
                 "atb": 30, "beigas": 60, "iedala": 10, "mers": "eiro",
                 "merkis": "atlaide", "objekts": "Cena",
                 "padoms": "60 : 2."},
                {"jaut": "Prece maksā 60 €, atlaide 25 %. Cik eiro ir "
                         "atlaide?",
                 "atb": 15, "beigas": 60, "iedala": 10, "mers": "eiro",
                 "merkis": "atlaide", "objekts": "Cena",
                 "padoms": "60 : 4."},
                {"jaut": "Prece maksā 60 €, atlaide 20 %. Cik eiro ir "
                         "atlaide?",
                 "atb": 12, "beigas": 60, "iedala": 10, "mers": "eiro",
                 "merkis": "atlaide", "objekts": "Cena",
                 "padoms": "60 : 5."},
                {"jaut": "Prece maksā 60 €, atlaide 10 %. Cik eiro ir "
                         "atlaide?",
                 "atb": 6, "beigas": 60, "iedala": 10, "mers": "eiro",
                 "merkis": "atlaide", "objekts": "Cena",
                 "padoms": "60 : 10."},
            ]),
            pavediens="veikals",
            konteksts="Pie plaukta atlaidi rēķina galvā - kalkulatoru "
                      "neviens neizņem.",
            kapec="Piecas zināmas vienādības aizstāj lielāko daļu rēķinu."),

    Varianti("Ar ko dalīt?", [
        {"jaut": "Lai atrastu 25 %, kopumu dala ar...",
         "opcijas": ["4", "25", "2", "5"],
         "pareizi": 0,
         "padoms": "Ceturtdaļa."},
        {"jaut": "Lai atrastu 20 %, kopumu dala ar...",
         "opcijas": ["5", "20", "4", "2"],
         "pareizi": 0,
         "padoms": "Piektdaļa."},
        {"jaut": "Kā ātrāk atrast 75 %?",
         "opcijas": ["Atņemt 25 % no kopuma", "Dalīt ar 75",
                     "Reizināt ar 75", "Dalīt ar 3"],
         "pareizi": 0,
         "padoms": "100 % − 25 %."},
        {"jaut": "Kā atrast 5 %?",
         "opcijas": ["Puse no 10 %", "Dalīt ar 5",
                     "Reizināt ar 5", "Puse no 20 %"],
         "pareizi": 0,
         "padoms": "10 % : 2."},
    ], pamats=4),

    Kopsavilkums([
        "Zinu no galvas 50 %, 25 %, 20 %, 10 % un 1 % kā daļas.",
        "Rēķinu tos ar dalīšanu, nevis ar reizināšanu.",
        "Saliek nezināmus procentus no zināmiem.",
        "Pārbaudu rezultātu ar novērtējumu.",
    ]),

    Majas([
        "Izrēķini galvā 50 %, 25 % un 10 % no 120.",
        "Atrodi veikalā trīs cenas un izrēķini 20 % atlaidi katrai.",
        "Pieraksti, kā no zināmiem procentiem salikt 35 %.",
    ]),
]
