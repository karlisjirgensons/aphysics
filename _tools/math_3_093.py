# -*- coding: utf-8 -*-
"""3. klase, 93. stunda: «Kad daļa ir vesels?»

Robežgadījums, kas noder visam turpmākajam: ja ņemtas visas daļas, sanāk
viens vesels. Skolēns to modelē un tad izmanto, lai pateiktu, cik daļu vēl
pietrūkst - tas ir 95. stundas priekšdarbs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         dala)

TEMA = "Kad daļa ir vesels?"

MERKIS = ("Modelēsim gadījumus, kad daļa veido veselo: četras ceturtdaļas "
          "ir viens.")

SATURS = [
    Sakums("Cik ceturtdaļu vajag, lai sanāktu vesela kūka?",
           zimejums=dala(4, 4, "4/4 = 1", "četras ceturtdaļas"),
           paraksts="Kad ņemtas visas daļas, sanāk viens vesels.",
           fakti=["{4|4} = 1, {8|8} = 1, {10|10} = 1.",
                  "Veselo var pierakstīt ar jebkuru saucēju."]),

    Doma("Visas daļas kopā ir viens vesels",
         "Ja skaitītājs ir vienāds ar saucēju, daļa ir tieši 1.",
         soli=[
             "Paskaties, cik daļās sadalīts veselais.",
             "Saskaiti, cik daļu ir ņemtas.",
             "Ja abi skaitļi sakrīt, daļa ir viens vesels.",
             "Pieraksti to: {n|n} = 1.",
         ],
         pieze="Tāpēc vienu un to pašu skaitli 1 var pierakstīt bezgalīgi "
               "daudzos veidos: {2|2}, {3|3}, {100|100}."),

    Slidnis("Ceļš līdz veselajam",
            soli=[
                {"v": "{1|4}", "teksts": "Viena ceturtdaļa.", "josla": 25},
                {"v": "{2|4}", "teksts": "Divas - tā ir puse.", "josla": 50},
                {"v": "{3|4}", "teksts": "Trīs ceturtdaļas.", "josla": 75},
                {"v": "{4|4} = 1", "teksts": "Četras - viens vesels.",
                 "josla": 100},
            ],
            ievads="Katrs solis pieliek vienu ceturtdaļu."),

    Paraugs("Cik piektdaļu ir vienā veselajā?",
            uzd="Cik piektdaļu vajag, lai sanāktu viens vesels?",
            soli=[
                ("Saucējs ir 5",
                 "Veselais sadalīts piecās daļās."),
                ("Vajag visas piecas",
                 "Tikai tad nekas nepaliek pāri."),
                ("{5|5} = 1",
                 "Piecas piektdaļas ir viens vesels."),
            ],
            atbilde="5 piektdaļas"),

    Ievadi("Cik daļu ir veselajā?", [
        {"jaut": "Cik ceturtdaļu ir vienā veselajā?", "atb": ["4"],
         "padoms": "Saucējs ir 4."},
        {"jaut": "Cik astotdaļu ir vienā veselajā?", "atb": ["8"],
         "padoms": "Saucējs ir 8."},
        {"jaut": "Cik desmitdaļu ir vienā veselajā?", "atb": ["10"],
         "padoms": "Saucējs ir 10."},
        {"jaut": "Cik ceturtdaļu ir divos veselos?", "atb": ["8"],
         "padoms": "2 · 4."},
        {"jaut": "Cik trešdaļu ir trijos veselos?", "atb": ["9"],
         "padoms": "3 · 3."},
        {"jaut": "Cik astotdaļu ir divos veselos?", "atb": ["16"],
         "padoms": "2 · 8."},
    ], pamats=4),

    Zimejums("Astoņas astotdaļas",
             dala(8, 8, "8/8 = 1", "visas daļas ņemtas"),
             paskaidro="Neatkarīgi no saucēja, visas daļas kopā vienmēr dod "
                       "vienu veselu.",
             ievads="Tas pats vesels, cits saucējs."),

    Varianti("Kura daļa ir viens vesels?", [
        {"jaut": "Kura daļa ir vienāda ar 1?",
         "opcijas": ["{7|7}", "{7|8}", "{8|7}", "{1|7}"],
         "pareizi": 0, "padoms": "Skaitītājs vienāds ar saucēju."},
        {"jaut": "Cik sestdaļu ir vienā veselajā?",
         "opcijas": ["6", "3", "12", "1"],
         "pareizi": 0, "padoms": "Saucējs ir 6."},
        {"jaut": "Cik ceturtdaļu ir trijos veselos?",
         "opcijas": ["12", "7", "3", "4"],
         "pareizi": 0, "padoms": "3 · 4."},
        {"jaut": "Kura daļa ir lielāka par 1?",
         "opcijas": ["{9|8}", "{8|8}", "{7|8}", "{1|8}"],
         "pareizi": 0, "padoms": "Skaitītājs lielāks par saucēju."},
    ], pamats=4),

    Pasaule("Cik gadalaiku ir gadā?",
            Ievadi("", [
                {"jaut": "Gadā ir 4 gadalaiki. Cik ceturtdaļu no gada ir "
                         "viens gadalaiks?",
                 "atb": ["1"], "padoms": "Viena ceturtdaļa."},
                {"jaut": "Cik mēnešu ir vienā gadalaikā, ja gadā ir 12 "
                         "mēneši?",
                 "atb": ["3"], "padoms": "12 : 4."},
                {"jaut": "Cik mēnešu ir {3|4} no gada?", "atb": ["9"],
                 "padoms": "3 · 3."},
                {"jaut": "Cik gadalaiku vajag, lai sanāktu vesels gads?",
                 "atb": ["4"], "padoms": "{4|4} = 1."},
            ]),
            pavediens="daba",
            konteksts="Gads dabā ir sadalīts četrās gandrīz vienādās daļās - "
                      "un tikai visas četras kopā ir vesels gads.",
            kapec="Tieši tāpēc {4|4} un 1 ir viens un tas pats."),

    Kopsavilkums([
        "Zinu, ka visas daļas kopā dod vienu veselu.",
        "Zinu, ka {n|n} = 1.",
        "Aprēķinu, cik daļu ir vairākos veselos.",
        "Modelēju veselo ar joslu vai riņķi.",
    ]),

    Majas([
        "Uzzīmē modeli, kurā {6|6} = 1.",
        "Izrēķini, cik ceturtdaļu ir piecos veselos.",
        "Uzraksti trīs dažādus veidus, kā pierakstīt skaitli 1 ar daļu.",
    ]),
]
