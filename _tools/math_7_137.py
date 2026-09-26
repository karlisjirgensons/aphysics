# -*- coding: utf-8 -*-
"""7. klase, 137. stunda: «Kā rīkoties ar iekavām un daļām?»

Vienādojumu ar iekavām vispirms vienkāršo (atver iekavas), vienādojumu ar
daļām - reizina ar kopsaucēju, lai daļas pazūd. Tad risina kā parasti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā rīkoties ar iekavām un daļām?"

MERKIS = ("Atrisināsim vienādojumu, kurā ir iekavas vai daļskaitļi.")

SATURS = [
    Sakums("Daļas pazūd ar vienu reizinājumu",
           fakti=["{x|2} + {x|3} = 10: kopsaucējs 6.",
                  "Reizinot abas puses ar 6: 3x + 2x = 60.",
                  "5x = 60, x = 12."]),

    Doma("Vispirms vienkāršo",
         "Ja vienādojumā ir iekavas - atver tās. Ja ir daļas - abas puses "
         "reizina ar visu saucēju mazāko kopīgo dalāmo, lai daļas pazustu. "
         "Tad pārnes un savelk.",
         soli=[
             "Atver iekavas (ievēro zīmes pirms tām).",
             "Daļām: atrodi kopsaucēju un reizini ar to katru saskaitāmo.",
             "Pārnes saskaitāmos, savelc.",
             "Dali ar koeficientu; pārbaudi.",
         ],
         pieze="Reizini ar kopsaucēju KATRU saskaitāmo - arī tos, kuri nav "
               "daļas."),

    Paraugs("Ar daļām",
            uzd="Atrisini {x|2} + {x − 1|3} = 6.",
            soli=[
                ("Kopsaucējs 6: 3x + 2(x − 1) = 36", "(· 6)"),
                ("3x + 2x − 2 = 36", "Atver iekavas."),
                ("5x = 38, x = 7,6", "Savelk un dala."),
                ("Pārbaude: 3,8 + 2,2 = 6", "Pareizi."),
            ],
            atbilde="x = 7,6"),

    Ievadi("Atrisini", [
        {"jaut": "3(x − 2) = 2x + 1",
         "atb": ["7"], "padoms": "3x − 6 = 2x + 1."},
        {"jaut": "2(x + 5) − (x − 3) = 20",
         "atb": ["7"], "padoms": "x + 13 = 20."},
        {"jaut": "{x|4} = {x|6} + 1",
         "atb": ["12"], "padoms": "· 12: 3x = 2x + 12."},
        {"jaut": "{2x − 1|3} = 5",
         "atb": ["8"], "padoms": "2x − 1 = 15."},
        {"jaut": "5 − 2(x − 1) = x + 1",
         "atb": ["2"], "padoms": "7 − 2x = x + 1."},
        {"jaut": "{x|3} − {x|5} = 2",
         "atb": ["15"], "padoms": "· 15: 5x − 3x = 30."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "{x|2} + 3 = 7 → reizina ar 2: x + 3 = 14",
         "opcijas": ["Jāreizina arī 3: x + 6 = 14", "Pareizi",
                     "Jādala ar 2", "x + 3 = 7"],
         "pareizi": 0, "padoms": "Katrs saskaitāmais."},
        {"jaut": "4 − (x + 2) = 1 → 4 − x + 2 = 1",
         "opcijas": ["Jābūt 4 − x − 2 = 1", "Pareizi",
                     "Jābūt 4 + x + 2 = 1", "Jābūt 4 − x = 1"],
         "pareizi": 0, "padoms": "Mīnuss pirms iekavām."},
    ]),

    Pasaule("Ceļojuma posmi",
            Ievadi("", [
                {"jaut": "Ceļojumā ar vilcienu nobrauca {1|2} ceļa, ar autobusu "
                         "{1|3} ceļa, kājām 12 km. Cik km viss ceļš? "
                         "({x|2} + {x|3} + 12 = x)",
                 "atb": ["72"], "padoms": "· 6: 3x + 2x + 72 = 6x."},
                {"jaut": "Cik km ar vilcienu?",
                 "atb": ["36"], "padoms": "72 : 2."},
                {"jaut": "Cik km ar autobusu?",
                 "atb": ["24"], "padoms": "72 : 3."},
            ]),
            pavediens="celojums",
            konteksts="Uzdevumi ar ceļa daļām ir klasiski eksāmenā - tos "
                      "risina ar vienādojumu un kopsaucēju.",
            kapec="Daļas pazūd, reizinot ar kopsaucēju."),

    Kopsavilkums([
        "Atveru iekavas vienādojumā.",
        "Reizinu abas puses ar kopsaucēju.",
        "Reizinu katru saskaitāmo.",
        "Pārbaudu sakni.",
    ]),

    Majas([
        "Atrisini: 4(x + 1) − 3(x − 2) = 15; {x|3} + {x|4} = 14.",
        "Izdomā ceļojuma uzdevumu ar daļām.",
        "Pārbaudi savas saknes.",
    ]),
]
