# -*- coding: utf-8 -*-
"""3. klase, 98. stunda: «Kā ar komatu pieraksta centus?»

Nauda ir vieta, kur decimāldaļu lieto katru dienu. Eiro ir veselais, cents -
tā simtdaļa, un pieraksts 1,25 nozīmē vienu eiro un divdesmit piecus centus.
Tas ir arī pirmais gadījums ar divām zīmēm aiz komata.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā ar komatu pieraksta centus?"

MERKIS = ("Izteiksim naudas summu centos kā eiro un otrādi; skaidrosim "
          "pierakstu 0,01.")

SATURS = [
    Sakums("Ko nozīmē 1,25 uz cenu zīmes?",
           zimejums=restis([["eiro", "centi"],
                            ["1", "25"],
                            ["1,25", ""]],
                           "viens eiro un divdesmit pieci centi"),
           paraksts="Pirms komata - eiro, aiz komata - centi.",
           fakti=["Vienā eiro ir 100 centi.",
                  "Viens cents ir {1|100} eiro jeb 0,01 eiro.",
                  "Aiz komata vienmēr raksta divus ciparus."]),

    Doma("Cents ir eiro simtdaļa",
         "1 cents = {1|100} eiro = 0,01 eiro, tāpēc aiz komata ir divas "
         "vietas.",
         soli=[
             "Pirms komata raksti veselos eiro.",
             "Aiz komata raksti centus - vienmēr divus ciparus.",
             "Ja centu ir mazāk par 10, priekšā raksti nulli: 0,05.",
             "Lai pārvērstu eiro centos, reizini ar 100.",
         ],
         pieze="Tieši tāpēc 0,5 eiro un 0,05 eiro ir pavisam dažādas summas: "
               "50 centi un 5 centi."),

    Paraugs("Cik centu ir 2,35 eiro?",
            uzd="Izsaki 2,35 eiro centos.",
            soli=[
                ("2 eiro = 200 centi",
                 "Katrā eiro ir 100 centu."),
                ("35 centi",
                 "Cipari aiz komata."),
                ("200 + 35 = 235",
                 "Kopā 235 centi."),
            ],
            atbilde="235 centi"),

    Ievadi("Eiro un centi", [
        {"jaut": "Cik centu ir 1 eiro?", "atb": ["100"],
         "padoms": "Simts centu."},
        {"jaut": "Cik centu ir 2,35 eiro?", "atb": ["235"],
         "padoms": "200 + 35."},
        {"jaut": "Cik centu ir 0,05 eiro?", "atb": ["5"],
         "padoms": "Pieci centi."},
        {"jaut": "Cik centu ir 0,5 eiro?", "atb": ["50"],
         "padoms": "Piecdesmit centu."},
        {"jaut": "Izsaki 150 centus eiro. Raksti ar komatu.",
         "atb": ["1,5", "1,50", "1.5", "1.50"],
         "padoms": "100 + 50."},
        {"jaut": "Izsaki 407 centus eiro. Raksti ar komatu.",
         "atb": ["4,07", "4.07"], "padoms": "400 + 7."},
    ], pamats=4),

    Zimejums("Divas dažādas summas",
             restis([["0,5 eiro", "50 centi"],
                     ["0,05 eiro", "5 centi"]],
                    "viena nulle maina visu"),
             paskaidro="Pirmais cipars aiz komata ir desmitdaļas, otrais - "
                       "simtdaļas.",
             ievads="Salīdzini abas rindas."),

    Varianti("Cik tas ir centos?", [
        {"jaut": "Cik centu ir 3,20 eiro?",
         "opcijas": ["320", "32", "3200", "23"],
         "pareizi": 0, "padoms": "300 + 20."},
        {"jaut": "Kura summa ir lielāka?",
         "opcijas": ["0,5 eiro", "0,05 eiro", "Abas vienādas",
                     "To nevar pateikt"],
         "pareizi": 0, "padoms": "50 centi un 5 centi."},
        {"jaut": "Kā pieraksta 8 centus eiro?",
         "opcijas": ["0,08", "0,8", "8,00", "80,0"],
         "pareizi": 0, "padoms": "Aiz komata divi cipari."},
        {"jaut": "Kāda daļa no eiro ir viens cents?",
         "opcijas": ["{1|100}", "{1|10}", "{1|1000}", "{1|50}"],
         "pareizi": 0, "padoms": "Eiro sadalīts simts daļās."},
    ], pamats=4),

    Pasaule("Cik maksā pirkums?",
            Ievadi("", [
                {"jaut": "Prece maksā 1,25 eiro. Cik centu tas ir?",
                 "atb": ["125"], "padoms": "100 + 25."},
                {"jaut": "Otra prece maksā 0,75 eiro. Cik centu?",
                 "atb": ["75"], "padoms": "75 centi."},
                {"jaut": "Cik centu maksā abas preces kopā?",
                 "atb": ["200"], "padoms": "125 + 75."},
                {"jaut": "Cik eiro tas ir?", "atb": ["2"],
                 "padoms": "200 : 100."},
            ]),
            pavediens="veikals",
            konteksts="Kasē summu saskaita centos, bet čekā izdrukā eiro ar "
                      "komatu - abi pieraksti ir viens un tas pats.",
            kapec="Kad proti pārvērst, cenas var salīdzināt galvā."),

    Kopsavilkums([
        "Zinu, ka vienā eiro ir 100 centu.",
        "Izsaku eiro centos un centus eiro.",
        "Zinu, ka cents ir {1|100} eiro jeb 0,01 eiro.",
        "Zinu, ka 0,5 un 0,05 ir dažādas summas.",
    ]),

    Majas([
        "Paskaties mājas čekā un izsaki trīs cenas centos.",
        "Pieraksti ar komatu 7 centus, 70 centus un 700 centus.",
        "Saskaiti, cik centu ir tavā krājkasītē, un pieraksti to eiro.",
    ]),
]
