# -*- coding: utf-8 -*-
"""4. klase, 43. stunda: «Kā dala rakstos?»

Dalīšana stūrītī ir pakāpeniskā dalīšana, tikai sakārtota: pirmais
nepilnais dalāmais, dalījuma cipars, reizinājums, atlikums, nākamais
cipars. Katru soli skolēns izrunā - tā viņš pats pamana, ja dalījumā
pietrūkst nulles (824 : 4 = 206, nevis 26).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā dala rakstos?"

MERKIS = ("Dalīsim rakstos (stūrītī) un paskaidrosim, kā veido pierakstu.")

SATURS = [
    Sakums("Kā dala lielu skaitli, ja galvā grūti?",
           zimejums=restis([["7", "3", "5", "|", "5"],
                            ["5", "", "", "|", "147"],
                            ["2", "3", "", "", ""],
                            ["2", "0", "", "", ""],
                            ["", "3", "5", "", ""],
                            ["", "3", "5", "", ""],
                            ["", "", "0", "", ""]],
                           "735 : 5 stūrītī"),
           paraksts="Soli pa solim - no kreisās uz labo.",
           fakti=["Stūrītī dalīšana sākas no lielākās šķiras.",
                  "Katrā solī: dali, reizini, atņem, nolaid nākamo ciparu."]),

    Doma("Dali - reizini - atņem - nolaid",
         "Stūrītī atkārto četrus soļus, līdz visi dalāmā cipari ir izmantoti.",
         soli=[
             "Atrodi pirmo nepilno dalāmo: 7 (simti) dalās ar 5.",
             "Dali: 7 : 5 = 1, raksti 1 dalījumā.",
             "Reizini: 1 · 5 = 5; atņem: 7 − 5 = 2.",
             "Nolaid nākamo ciparu: 23; atkārto - 23 : 5 = 4 (atl. 3), "
             "tad 35 : 5 = 7.",
         ],
         pieze="Ja nolaistais skaitlis ir mazāks par dalītāju, dalījumā "
               "raksta 0: 824 : 4 = 206."),

    Paraugs("824 : 4",
            uzd="Izdali stūrītī 824 : 4.",
            soli=[
                ("8 : 4 = 2", "Simti. 2 · 4 = 8, atlikums 0."),
                ("2 : 4 = 0 (atl. 2)", "Nolaiž 2 - tas ir mazāks par 4: dalījumā 0."),
                ("24 : 4 = 6", "Nolaiž 4, sanāk 24."),
                ("824 : 4 = 206", "Pārbaude: 206 · 4 = 824."),
            ],
            atbilde="206"),

    Slidnis("Stūrītis: 672 : 3",
            soli=[
                {"v": "6 : 3 = 2", "teksts": "Simti: raksta 2."},
                {"v": "7 : 3 = 2 (atl. 1)", "teksts": "Desmiti: raksta 2, "
                 "atlikums 1."},
                {"v": "12 : 3 = 4", "teksts": "Atlikumam piekabina 2 - sanāk "
                 "12. Raksta 4."},
                {"v": "672 : 3 = 224", "teksts": "Pārbaude: 224 · 3 = 672."},
            ]),

    Ievadi("Stūrītī", [
        {"jaut": "735 : 5 = ?", "atb": ["147"], "padoms": "7, 23, 35."},
        {"jaut": "672 : 3 = ?", "atb": ["224"], "padoms": "6, 7, 12."},
        {"jaut": "824 : 4 = ?", "atb": ["206"], "padoms": "Neaizmirsti 0."},
        {"jaut": "936 : 6 = ?", "atb": ["156"], "padoms": "9, 33, 36."},
        {"jaut": "912 : 8 = ?", "atb": ["114"], "padoms": "9, 11, 32."},
        {"jaut": "618 : 6 = ?", "atb": ["103"], "padoms": "6, 1, 18."},
    ], pamats=4),

    Varianti("Kas ir pirmais nepilnais dalāmais?", [
        {"jaut": "384 : 6 - ar ko sāk?",
         "opcijas": ["38", "3", "384", "84"], "pareizi": 0,
         "padoms": "3 ir mazāks par 6 - ņem divus ciparus."},
        {"jaut": "Cik ciparu būs dalījumā 384 : 6?",
         "opcijas": ["2", "3", "1", "4"], "pareizi": 0,
         "padoms": "Sāk ar 38 - desmitiem."},
        {"jaut": "Kārlis: 624 : 3 = 28. Kas nav kārtībā?",
         "opcijas": ["pazaudēja nulli: pareizi 208",
                     "viss pareizi", "sajauca ciparus"], "pareizi": 0,
         "padoms": "2 : 3 = 0 - jāraksta 0."},
        {"jaut": "Cik ir 384 : 6?",
         "opcijas": ["64", "604", "46", "84"], "pareizi": 0,
         "padoms": "38 : 6 = 6 (atl. 2), 24 : 6 = 4."},
    ], pamats=4),

    Pasaule("Grāmatu lasīšanas plāns",
            Ievadi("", [
                {"jaut": "Grāmatā 672 lappuses. Ja lasa 3 mēnešus vienādi, "
                         "cik lappušu mēnesī?",
                 "atb": ["224"], "padoms": "672 : 3."},
                {"jaut": "Mēnesī ir 4 nedēļas. Cik lappušu nedēļā (224 : 4)?",
                 "atb": ["56"], "padoms": "224 : 4."},
                {"jaut": "Nedēļā 7 dienas. Cik lappušu dienā (56 : 7)?",
                 "atb": ["8"], "padoms": "56 : 7."},
                {"jaut": "Citu grāmatu - 324 lappuses - izlasa 6 dienās "
                         "vienādi. Cik lappušu dienā?",
                 "atb": ["54"], "padoms": "324 : 6."},
            ]),
            pavediens="skola",
            konteksts="Resnu grāmatu vieglāk izlasīt, ja sadala to vienādās "
                      "dienas porcijās.",
            kapec="Dalīšana pārvērš lielu mērķi mazos dienas darbiņos."),

    Kopsavilkums([
        "Dalu stūrītī: dali, reizini, atņem, nolaid.",
        "Atrodu pirmo nepilno dalāmo.",
        "Neaizmirstu nulli dalījumā.",
        "Pārbaudu ar reizināšanu.",
    ]),

    Majas([
        "Izdali stūrītī savas mīļākās grāmatas lappušu skaitu ar 7.",
        "Izdomā dalījumu, kurā dalījumā ir nulle.",
        "Paskaidro mājiniekiem četrus stūrīša soļus.",
    ]),
]
