# -*- coding: utf-8 -*-
"""4. klase, 120. stunda: «Kā apkopot daļas un to vērtības?»

Tabula «daļa - vērtība» vienam veselajam: {1|2}, {1|4}, {1|8}, {3|4} no
40. Tā parāda likumsakarības - puse no puses ir ceturtdaļa, trīs
ceturtdaļas ir trīs reizes viena. Datu apkopošana tabulā ir arī eksāmena
prasme.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā apkopot daļas un to vērtības?"

MERKIS = ("Veidosim tabulu, kurā attēlota daļa un tās skaitliskā vērtība.")

SATURS = [
    Sakums("Cik ir daļas no 40?",
           zimejums=restis([["daļa", "1/2", "1/4", "1/8", "3/4"],
                            ["no 40", 20, 10, 5, 30]],
                           "viens veselais - daudz daļu"),
           paraksts="Katra ceturtdaļa ir divas astotdaļas: 10 = 5 + 5.",
           fakti=["Tabula parāda visas daļas vienuviet.",
                  "Tajā redz sakarības, ko atsevišķi nepamana."]),

    Doma("Viens veselais - viena tabula",
         "Tabulā pirmajā rindā raksta daļas, otrajā - to vērtības no viena un "
         "tā paša veselā.",
         soli=[
             "Uzraksti veselo: 40.",
             "Aprēķini pamatdaļas: {1|2}, {1|4}, {1|8} no 40.",
             "Aprēķini citas daļas no pamatdaļām: {3|4} = 3 · 10.",
             "Meklē sakarības: {1|8} ir puse no {1|4}.",
         ],
         pieze="Pēdējā kolonnā vari ielikt {4|4} = 40 - pašu veselo."),

    Paraugs("Tabula no 60",
            uzd="Aizpildi tabulu daļām {1|2}, {1|3}, {2|3}, {1|6} no 60.",
            soli=[
                ("{1|2} no 60 = 30", None),
                ("{1|3} no 60 = 20", None),
                ("{2|3} no 60 = 40", "Divas trešdaļas."),
                ("{1|6} no 60 = 10", "Puse no trešdaļas."),
            ],
            atbilde="30, 20, 40, 10"),

    Zimejums("Tabula no 60",
             restis([["daļa", "1/2", "1/3", "2/3", "1/6"],
                     ["no 60", 30, 20, 40, 10]],
                    "sakarības"),
             paskaidro="{1|6} ir puse no {1|3}: 10 ir puse no 20.",
             ievads="Tā pati tabula - cits veselais."),

    Ievadi("Aizpildi tabulu (veselais 80)", [
        {"jaut": "{1|2} no 80 = ?", "atb": ["40"], "padoms": "80 : 2."},
        {"jaut": "{1|4} no 80 = ?", "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "{3|4} no 80 = ?", "atb": ["60"], "padoms": "3 · 20."},
        {"jaut": "{1|8} no 80 = ?", "atb": ["10"], "padoms": "80 : 8."},
        {"jaut": "{5|8} no 80 = ?", "atb": ["50"], "padoms": "5 · 10."},
        {"jaut": "{1|10} no 80 = ?", "atb": ["8"], "padoms": "80 : 10."},
    ], pamats=4),

    Varianti("Sakarības tabulā", [
        {"jaut": "Ja {1|4} no veselā ir 16, cik ir {1|8}?",
         "opcijas": ["8", "32", "16", "4"], "pareizi": 0,
         "padoms": "Astotdaļa ir puse no ceturtdaļas."},
        {"jaut": "Ja {1|3} ir 20, cik ir {2|3}?",
         "opcijas": ["40", "20", "10", "60"], "pareizi": 0,
         "padoms": "Divreiz vairāk."},
        {"jaut": "Ja {1|2} ir 25, cik ir veselais?",
         "opcijas": ["50", "25", "20", "100"], "pareizi": 0,
         "padoms": "Divas puses."},
    ]),

    Pasaule("Mana diennakts tabula",
            Ievadi("", [
                {"jaut": "Diennaktī 24 h. Miegs {3|8}. Cik stundu?",
                 "atb": ["9"], "padoms": "24 : 8 · 3."},
                {"jaut": "Skola {1|4}. Cik stundu?", "atb": ["6"],
                 "padoms": "24 : 4."},
                {"jaut": "Ēšana {1|12}. Cik stundu?", "atb": ["2"],
                 "padoms": "24 : 12."},
                {"jaut": "Cik stundu paliek citām lietām?", "atb": ["7"],
                 "padoms": "24 − 9 − 6 − 2."},
            ]),
            pavediens="skola",
            konteksts="Diennakts ir veselais - un tabula parāda, kur aiziet "
                      "tavs laiks.",
            kapec="Tabula ar daļām ir laika plānošanas rīks."),

    Kopsavilkums([
        "Veidoju tabulu «daļa - vērtība».",
        "Aprēķinu daļas no pamatdaļām.",
        "Atrodu sakarības tabulā.",
    ]),

    Majas([
        "Izveido tabulu savai diennaktij ar daļām un stundām.",
        "Aizpildi tabulu daļām {1|2}, {1|4}, {3|4} no 100.",
        "Atrodi tabulā sakarību un paskaidro to mājiniekiem.",
    ]),
]
