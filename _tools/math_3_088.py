# -*- coding: utf-8 -*-
"""3. klase, 88. stunda: «Kāda daļa ir mazāka nekā viens?»

Mikrotemata noslēgums. Īsta daļa - tā, kurai skaitītājs ir mazāks par saucēju -
vienmēr atrodas starp 0 un 1. Šī stunda to nosaka un parāda arī abus robežu
gadījumus: {n|n} = 1 un daļas, kas ir lielākas par veselo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kāda daļa ir mazāka nekā viens?"

MERKIS = ("Skaidrosim, ka īsta daļa atrodas starp 0 un 1, un minēsim "
          "piemērus.")

SATURS = [
    Sakums("Kā pēc pieraksta pateikt, vai daļa ir mazāka par vienu?",
           zimejums=taisne(0, 1, 1, [(0.2, "1/5"), (0.6, "3/5"),
                                     (1.0, "5/5")]),
           paraksts="Kamēr skaitītājs ir mazāks par saucēju, daļa ir mazāka "
                    "par 1.",
           fakti=["Ja skaitītājs mazāks par saucēju, daļa ir īsta.",
                  "Īsta daļa vienmēr atrodas starp 0 un 1."]),

    Doma("Salīdzini skaitītāju ar saucēju",
         "Ja skaitītājs ir mazāks - daļa ir mazāka par 1; ja vienāds - daļa "
         "ir 1; ja lielāks - daļa ir lielāka par 1.",
         soli=[
             "Paskaties uz abiem skaitļiem daļā.",
             "Ja skaitītājs mazāks - daļa ir starp 0 un 1.",
             "Ja skaitītājs vienāds ar saucēju - daļa ir tieši 1.",
             "Ja skaitītājs lielāks - daļa pārsniedz veselo.",
         ],
         pieze="Daļa, kas lielāka par 1, arī ir pareiza: {9|8} nozīmē vienu "
               "veselu un vēl vienu astotdaļu. Tikai tā vairs nav *īsta* "
               "daļa."),

    Paraugs("Vai {7|8} ir mazāks par 1?",
            uzd="Pārbaudi, vai {7|8} ir mazāks par vienu.",
            soli=[
                ("Skaitītājs 7, saucējs 8",
                 "Salīdzina abus skaitļus."),
                ("7 < 8",
                 "Skaitītājs ir mazāks."),
                ("{7|8} < 1",
                 "Līdz veselajam pietrūkst vienas astotdaļas."),
            ],
            atbilde="jā, pietrūkst {1|8}"),

    Ievadi("Salīdzini ar vienu", [
        {"jaut": "Cik daļu pietrūkst līdz 1 daļai {7|8}?", "atb": ["1"],
         "padoms": "8 − 7."},
        {"jaut": "Cik daļu pietrūkst līdz 1 daļai {3|10}?", "atb": ["7"],
         "padoms": "10 − 3."},
        {"jaut": "Cik ir {6|6}?", "atb": ["1"],
         "padoms": "Visas daļas ņemtas."},
        {"jaut": "Cik daļu pietrūkst līdz 1 daļai {2|5}?", "atb": ["3"],
         "padoms": "5 − 2."},
        {"jaut": "Daļā {9|8} - cik astotdaļu ir virs veselā?",
         "atb": ["1"], "padoms": "9 − 8."},
        {"jaut": "Cik ceturtdaļu ir divos veselos?", "atb": ["8"],
         "padoms": "2 · 4."},
    ], pamats=4),

    Zimejums("Daļa, kas pārsniedz veselo",
             taisne(0, 2, 1, [(1.0, "1"), (1.25, "5/4")]),
             paskaidro="{5|4} ir viens vesels un vēl viena ceturtdaļa - tāpēc "
                       "tā atrodas aiz vieninieka.",
             ievads="Ne visas daļas ir mazākas par vienu."),

    Varianti("Vai daļa ir īsta?", [
        {"jaut": "Kura daļa ir mazāka par 1?",
         "opcijas": ["{5|6}", "{6|6}", "{7|6}", "{12|6}"],
         "pareizi": 0, "padoms": "Skaitītājs mazāks par saucēju."},
        {"jaut": "Kura daļa ir tieši 1?",
         "opcijas": ["{9|9}", "{9|10}", "{10|9}", "{1|9}"],
         "pareizi": 0, "padoms": "Skaitītājs vienāds ar saucēju."},
        {"jaut": "Kura daļa ir lielāka par 1?",
         "opcijas": ["{11|10}", "{9|10}", "{10|10}", "{1|10}"],
         "pareizi": 0, "padoms": "Skaitītājs lielāks par saucēju."},
        {"jaut": "Cik pietrūkst līdz 1 daļai {4|9}?",
         "opcijas": ["{5|9}", "{4|9}", "{9|4}", "{1|9}"],
         "pareizi": 0, "padoms": "9 − 4 = 5."},
    ], pamats=4),

    Pasaule("Cik spēles ir izspēlētas?",
            Ievadi("", [
                {"jaut": "Sezonā 20 spēles, izspēlētas 13. Cik spēļu vēl "
                         "atlicis?",
                 "atb": ["7"], "padoms": "20 − 13."},
                {"jaut": "Cik spēļu ir {1|2} no 20?", "atb": ["10"],
                 "padoms": "20 : 2."},
                {"jaut": "Cik spēļu ir {3|4} no 20?", "atb": ["15"],
                 "padoms": "20 : 4 = 5; 3 · 5."},
                {"jaut": "Vai 13 spēles ir vairāk par pusi? Raksti «jā» vai "
                         "«nē».",
                 "atb": ["jā", "ja"], "padoms": "13 > 10.",
                 "tastatura": "text"},
            ]),
            pavediens="sports",
            konteksts="Sezonas vidū vienmēr saka, kāda daļa jau aiz muguras - "
                      "un tā vienmēr ir mazāka par vienu.",
            kapec="Kad daļa kļūst par veselu, sezona ir beigusies."),

    Kopsavilkums([
        "Zinu, ka īsta daļa atrodas starp 0 un 1.",
        "Salīdzinu skaitītāju ar saucēju un nosaku daļas lielumu.",
        "Zinu, ka {n|n} = 1.",
        "Zinu, ka daļa var būt arī lielāka par vienu.",
    ]),

    Majas([
        "Uzraksti trīs daļas, kas mazākas par 1, un trīs, kas vienādas ar 1.",
        "Atrodi daļu, kas lielāka par 1, un paskaidro, ko tā nozīmē.",
        "Atzīmē uz skaitļu taisnes {3|5} un {5|5}.",
    ]),
]
