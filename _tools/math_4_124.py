# -*- coding: utf-8 -*-
"""4. klase, 124. stunda: «Kā aprēķināt daļu no naudas?»

Pamatdaļa no naudas daudzuma - vispirms ar monētu modeli: 20 € sadala 4
vienādās kaudzītēs, katrā 5 €. Modelis parāda, ka «{1|4} no» ir tas pats,
kas «dalīt ar 4». Pēc tam - bez monētām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā aprēķināt daļu no naudas?"

MERKIS = ("Noteiksim pamatdaļu no naudas daudzuma, vispirms ar monētu "
          "modeļiem.")

SATURS = [
    Sakums("Kā godīgi sadalīt 20 € četriem?",
           zimejums=restis([["1. kaudze", "2 €", "2 €", "1 €"],
                            ["2. kaudze", "2 €", "2 €", "1 €"],
                            ["3. kaudze", "2 €", "2 €", "1 €"],
                            ["4. kaudze", "2 €", "2 €", "1 €"]],
                           "katrā 5 €"),
           paraksts="{1|4} no 20 € ir 5 €.",
           fakti=["Pamatdaļa no naudas - sadalīt vienādās kaudzītēs.",
                  "«{1|4} no» nozīmē «dalīt ar 4»."]),

    Doma("{1|n} no skaitļa = skaitlis : n",
         "Lai atrastu pamatdaļu no naudas daudzuma, to sadala saucēja skaitā "
         "vienādu daļu.",
         soli=[
             "Nosaki veselo: 20 €.",
             "Nosaki saucēju: {1|4} → 4.",
             "Dali: 20 : 4 = 5.",
             "Pārbaudi: 4 kaudzes pa 5 € = 20 €.",
         ],
         pieze="Ja centi, pārvērt tos: {1|2} no 3 € = 300 ct : 2 = 150 ct."),

    Paraugs("{1|5} no 35 €",
            uzd="Cik ir {1|5} no 35 €?",
            soli=[
                ("35 : 5 = 7", None),
                ("5 · 7 = 35", "Pārbaude."),
            ],
            atbilde="7 €"),

    Ievadi("Pamatdaļa no naudas", [
        {"jaut": "{1|2} no 18 € = ? €", "atb": ["9"], "padoms": "18 : 2."},
        {"jaut": "{1|3} no 24 € = ? €", "atb": ["8"], "padoms": "24 : 3."},
        {"jaut": "{1|4} no 40 € = ? €", "atb": ["10"], "padoms": "40 : 4."},
        {"jaut": "{1|10} no 50 € = ? €", "atb": ["5"], "padoms": "50 : 10."},
        {"jaut": "{1|2} no 3 € = ? ct", "atb": ["150"],
         "padoms": "300 ct : 2."},
        {"jaut": "{1|4} no 1 € = ? ct", "atb": ["25"],
         "padoms": "100 ct : 4."},
    ], pamats=4),

    Varianti("Kā izrēķināt?", [
        {"jaut": "{1|6} no 42 €",
         "opcijas": ["42 : 6", "42 · 6", "42 − 6", "6 : 42"], "pareizi": 0,
         "padoms": "Dala ar saucēju."},
        {"jaut": "Cik ir {1|6} no 42 €?",
         "opcijas": ["7 €", "36 €", "252 €", "6 €"], "pareizi": 0,
         "padoms": "42 : 6."},
        {"jaut": "Kas ir vairāk: {1|2} no 10 € vai {1|3} no 12 €?",
         "opcijas": ["{1|2} no 10 €", "{1|3} no 12 €", "vienādi"],
         "pareizi": 0, "padoms": "5 € un 4 €."},
    ]),

    Pasaule("Kabatasnaudas plāns",
            Ievadi("", [
                {"jaut": "Mēnesī 20 € kabatasnauda. {1|4} krāj. Cik € krāj?",
                 "atb": ["5"], "padoms": "20 : 4."},
                {"jaut": "{1|5} no 20 € tērē grāmatām. Cik €?", "atb": ["4"],
                 "padoms": "20 : 5."},
                {"jaut": "{1|10} no 20 € ziedo dzīvnieku patversmei. Cik €?",
                 "atb": ["2"], "padoms": "20 : 10."},
                {"jaut": "Cik € paliek citām lietām?", "atb": ["9"],
                 "padoms": "20 − 5 − 4 − 2."},
            ]),
            pavediens="veikals",
            konteksts="Daudzi bērni kabatasnaudu sadala daļās: krājumiem, "
                      "tēriņiem un dāvinājumiem.",
            kapec="Daļas palīdz plānot naudu, pirms tā iztērēta."),

    Kopsavilkums([
        "Aprēķinu pamatdaļu no naudas, dalot ar saucēju.",
        "Modelēju ar monētu kaudzītēm.",
        "Pārvēršu eiro centos, ja vajag.",
    ]),

    Majas([
        "Ar spēļu naudu sadali 12 € trim vienādās daļās.",
        "Izplāno savu kabatasnaudu ar trim daļām.",
        "Izrēķini {1|4} no 2 € centos.",
    ]),
]
