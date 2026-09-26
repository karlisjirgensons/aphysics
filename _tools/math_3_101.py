# -*- coding: utf-8 -*-
"""3. klase, 101. stunda: «Cik ir puse no divpadsmit?»

Daļa no skaita - tas ir tas pats, ko skolēns jau prot ar dalīšanu, tikai
pierakstīts ar daļu. Divi soļi: dala ar saucēju, reizina ar skaitītāju. No
šīs prasmes aug visi procentu uzdevumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         dala)

TEMA = "Cik ir puse no divpadsmit?"

MERKIS = ("Noteiksim daļu no skaita praktiskā situācijā un pierakstīsim "
          "spriedumu.")

SATURS = [
    Sakums("Cik konfekšu ir puse no divpadsmit?",
           zimejums=dala(12, 6, "1/2 no 12 = 6", "divpadsmit vienādas daļas"),
           paraksts="Puse ir seši - tikpat, cik 12 : 2.",
           fakti=["Daļu no skaita atrod ar dalīšanu.",
                  "«Puse no 12» nozīmē to pašu, ko 12 : 2."]),

    Doma("Vispirms dali, tad reizini",
         "{2|3} no 12 nozīmē: 12 : 3 = 4, tad 2 · 4 = 8.",
         soli=[
             "Izdali skaitli ar saucēju - tā ir viena daļa.",
             "Reizini iegūto ar skaitītāju.",
             "Pieraksti atbildi kopā ar vārdu.",
             "Pārbaudi: atbildei jābūt mazākai par veselo.",
         ],
         pieze="Ja skaitītājs ir 1, otrais solis nav vajadzīgs: {1|4} no 20 "
               "ir vienkārši 20 : 4 = 5."),

    Slidnis("Daļas no 12",
            soli=[
                {"v": "{1|4} no 12 = 3", "teksts": "12 : 4.", "josla": 25},
                {"v": "{1|3} no 12 = 4", "teksts": "12 : 3.", "josla": 33},
                {"v": "{1|2} no 12 = 6", "teksts": "12 : 2.", "josla": 50},
                {"v": "{3|4} no 12 = 9", "teksts": "3 · 3.", "josla": 75},
            ],
            ievads="Viens un tas pats skaitlis, dažādas daļas."),

    Paraugs("Cik ir {2|3} no 12?",
            uzd="Aprēķini {2|3} no 12.",
            soli=[
                ("12 : 3 = 4",
                 "Viena trešdaļa."),
                ("2 · 4 = 8",
                 "Divas trešdaļas."),
                ("{2|3} no 12 ir 8",
                 "Pārbaude: 8 ir mazāk par 12."),
            ],
            atbilde="8"),

    Ievadi("Daļa no skaita", [
        {"jaut": "Cik ir {1|2} no 12?", "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "Cik ir {1|3} no 12?", "atb": ["4"], "padoms": "12 : 3."},
        {"jaut": "Cik ir {2|3} no 12?", "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Cik ir {3|4} no 20?", "atb": ["15"],
         "padoms": "20 : 4 = 5; 3 · 5."},
        {"jaut": "Cik ir {2|5} no 30?", "atb": ["12"],
         "padoms": "30 : 5 = 6; 2 · 6."},
        {"jaut": "Cik ir {5|6} no 24?", "atb": ["20"],
         "padoms": "24 : 6 = 4; 5 · 4."},
    ], pamats=4),

    Zimejums("Divas trešdaļas",
             dala(3, 2, "2/3 no 12 = 8", "trīs daļas pa 4"),
             paskaidro="Katra trešdaļa ir 4, tāpēc divas trešdaļas ir 8.",
             ievads="Tā izskatās {2|3} no 12."),

    Varianti("Cik tas ir?", [
        {"jaut": "Cik ir {1|4} no 20?",
         "opcijas": ["5", "4", "16", "80"],
         "pareizi": 0, "padoms": "20 : 4."},
        {"jaut": "Cik ir {3|5} no 25?",
         "opcijas": ["15", "5", "20", "10"],
         "pareizi": 0, "padoms": "25 : 5 = 5; 3 · 5."},
        {"jaut": "Kurš solis ir pirmais?",
         "opcijas": ["Dalīt ar saucēju", "Reizināt ar skaitītāju",
                     "Saskaitīt", "Atņemt"],
         "pareizi": 0, "padoms": "Vispirms atrod vienu daļu."},
        {"jaut": "Cik ir {4|5} no 40?",
         "opcijas": ["32", "8", "20", "45"],
         "pareizi": 0, "padoms": "40 : 5 = 8; 4 · 8."},
    ], pamats=4),

    Pasaule("Cik preču ir ar atlaidi?",
            Ievadi("", [
                {"jaut": "Veikalā 60 preces, {1|3} ir ar atlaidi. Cik preču?",
                 "atb": ["20"], "padoms": "60 : 3."},
                {"jaut": "Cik preču ir bez atlaides?", "atb": ["40"],
                 "padoms": "60 − 20."},
                {"jaut": "Cita diena: 80 preces, {1|4} ar atlaidi. Cik "
                         "preču?",
                 "atb": ["20"], "padoms": "80 : 4."},
                {"jaut": "Cik preču ir {3|4} no 80?", "atb": ["60"],
                 "padoms": "3 · 20."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā akcijā parasti ir daļa no precēm - ceturtdaļa "
                      "vai trešdaļa no visa plaukta.",
            kapec="Daļa no skaita pasaka, cik preču tiešām ir lētākas."),

    Kopsavilkums([
        "Aprēķinu daļu no skaita divos soļos.",
        "Vispirms dalu ar saucēju, tad reizinu ar skaitītāju.",
        "Pierakstu spriedumu un atbildi ar vārdu.",
        "Pārbaudu, vai atbilde ir mazāka par veselo.",
    ]),

    Majas([
        "Izrēķini {1|2}, {1|4} un {3|4} no 40.",
        "Atrodi mājās 20 vienādas lietas un atdali no tām {1|5}.",
        "Izdomā uzdevumu, kurā jāatrod {2|3} no skaita.",
    ]),
]
