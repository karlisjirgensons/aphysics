# -*- coding: utf-8 -*-
"""5. klase, 150. stunda: «Kā izskatās 25 % riņķī?»

Jauns mikrotemats sākas ar aci, ne ar transportieri. Ceturtdaļu, pusi un trīs
ceturtdaļas riņķī var uzskicēt bez mērīšanas, un tieši šī prasme vēlāk ļauj
pamanīt, ka diagramma ir uzzīmēta greizi. Tāpēc stundā skicē ar roku un tikai
pēc tam pārbauda ar skaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         rinkis)

TEMA = "Kā izskatās 25 % riņķī?"

MERKIS = ("Mācīsimies uzskicēt riņķi ar sadalījumu 25 %, 50 % un 75 % un "
          "skaidrot savu spriedumu.")

SATURS = [
    Sakums("Ceturtdaļa riņķa",
           zimejums=rinkis(sektors=90, virsraksts="25 % no riņķa",
                           paraksts="taisns leņķis"),
           paraksts="25 % riņķī ir tieši taisns leņķis.",
           fakti=["Viss riņķis ir 100 %.",
                  "Puse riņķa ir 50 %.",
                  "Ceturtdaļa - 25 %, un tā ir taisns leņķis."]),

    Doma("Puse, ceturtdaļa, trīs ceturtdaļas",
         "Riņķi ērti sadalīt uz aci pusēs un ceturtdaļās: 50 % ir puse, 25 % "
         "ir ceturtdaļa, 75 % - trīs ceturtdaļas.",
         soli=[
             "Novelc vienu diametru - riņķis sadalīts uz pusēm.",
             "Novelc otru diametru krustiski - iznāk četras ceturtdaļas.",
             "Viena ceturtdaļa ir 25 %.",
             "Divas ceturtdaļas ir 50 %, trīs - 75 %.",
             "Pārējos procentus novērtē starp šīm atzīmēm.",
         ],
         pieze="40 % uz aci ir mazliet mazāk par pusi, bet vairāk par "
               "ceturtdaļu. Tieši tā arī skicē: vispirms atrod tuvāko "
               "ceturtdaļu, tad pielabo."),

    Slidnis("Cik liels ir sektors?",
            [{"v": "25 %", "teksts": "ceturtdaļa riņķa", "josla": 25,
              "zim": rinkis(sektors=90)},
             {"v": "50 %", "teksts": "puse riņķa", "josla": 50,
              "zim": rinkis(sektors=180)},
             {"v": "75 %", "teksts": "trīs ceturtdaļas", "josla": 75,
              "zim": rinkis(sektors=270)}],
            ievads="Spied soli pa solim: sektors aug pa ceturtdaļai."),

    Paraugs("Uzskicē 75 %",
            uzd="Kā uzzīmēt 75 % riņķī bez transportiera?",
            soli=[
                ("Sadali riņķi četrās ceturtdaļās",
                 "Divi krustiski diametri."),
                ("Katra ceturtdaļa ir 25 %",
                 "100 : 4."),
                ("Iekrāso trīs ceturtdaļas",
                 "3 · 25 = 75."),
                ("Neiekrāsota paliek viena",
                 "Tā ir 25 %."),
            ],
            atbilde="75 % ir trīs riņķa ceturtdaļas"),

    Ievadi("Procenti un riņķa daļas", [
        {"jaut": "Cik procentu ir viss riņķis?",
         "atb": ["100"], "padoms": "Viss veselais."},
        {"jaut": "Cik procentu ir puse riņķa?",
         "atb": ["50"], "padoms": "100 : 2."},
        {"jaut": "Cik procentu ir ceturtdaļa riņķa?",
         "atb": ["25"], "padoms": "100 : 4."},
        {"jaut": "Cik procentu ir trīs ceturtdaļas?",
         "atb": ["75"], "padoms": "25 · 3."},
        {"jaut": "Iekrāsoti 25 %. Cik procentu palika balti?",
         "atb": ["75"], "padoms": "100 - 25."},
        {"jaut": "Iekrāsoti 60 %. Cik procentu palika balti?",
         "atb": ["40"], "padoms": "100 - 60."},
        {"jaut": "Cik ceturtdaļu ir 50 %?",
         "atb": ["2"], "padoms": "50 : 25."},
        {"jaut": "Cik procentu ir viena astotdaļa riņķa?",
         "atb": ["12,5"], "padoms": "100 : 8."},
    ], pamats=4,
        ievads="Vispirms atrodi tuvāko ceturtdaļu, tad pielabo."),

    Zimejums("Puse riņķa",
             rinkis(sektors=180, virsraksts="50 % no riņķa",
                    paraksts="izstiepts leņķis"),
             paskaidro="Puse riņķa ir izstiepts leņķis - 180°. Tāpēc "
                       "50 % skicē var novilkt ar vienu taisnu līniju.",
             ievads="Otrā atzīme, ko var uzlikt bez mērīšanas."),

    Varianti("Cik liela ir daļa?", [
        {"jaut": "25 % riņķī ir...",
         "opcijas": ["Ceturtdaļa", "Puse", "Trīs ceturtdaļas", "Viss riņķis"],
         "pareizi": 0,
         "padoms": "100 : 4."},
        {"jaut": "50 % riņķī ir...",
         "opcijas": ["Puse", "Ceturtdaļa", "Trešdaļa", "Viss riņķis"],
         "pareizi": 0,
         "padoms": "Viens diametrs."},
        {"jaut": "Sektors izskatās mazliet mazāks par pusi. Cik procentu tas "
                 "varētu būt?",
         "opcijas": ["40 %", "70 %", "25 %", "90 %"],
         "pareizi": 0,
         "padoms": "Starp ceturtdaļu un pusi."},
        {"jaut": "Iekrāsoti 75 %. Cik ceturtdaļu tas ir?",
         "opcijas": ["Trīs", "Divas", "Viena", "Četras"],
         "pareizi": 0,
         "padoms": "75 : 25."},
        {"jaut": "Visu sektoru procentiem kopā jādod...",
         "opcijas": ["100 %", "50 %", "360 %", "1 %"],
         "pareizi": 0,
         "padoms": "Viss riņķis."},
        {"jaut": "Kā riņķi sadala četrās ceturtdaļās?",
         "opcijas": ["Ar diviem krustiskiem diametriem", "Ar vienu diametru",
                     "Ar rādiusu", "Ar cirkuli"],
         "pareizi": 0,
         "padoms": "Divas līnijas."},
    ], pamats=4),

    Pasaule("Kā izskatās klases aptauja?",
            Ievadi("", [
                {"jaut": "Klasē 25 % izvēlējās futbolu. Cik procentu "
                         "izvēlējās ko citu?",
                 "atb": ["75"], "padoms": "100 - 25."},
                {"jaut": "Puse klases brauc ar autobusu. Cik procentu tas "
                         "ir?",
                 "atb": ["50"], "padoms": "{1|2} = 50 %."},
                {"jaut": "Klasē 20 skolēni, 5 spēlē šahu. Cik procentu tas "
                         "ir?",
                 "atb": ["25"], "padoms": "{5|20} = {25|100}."},
                {"jaut": "Cik procentu no klases nespēlē šahu?",
                 "atb": ["75"], "padoms": "100 - 25."},
            ]),
            pavediens="skola",
            konteksts="Klases aptaujas rezultātus visvieglāk parādīt riņķī: "
                      "uzreiz redz, kura daļa ir lielāka.",
            kapec="Ceturtdaļas un puses var uzskicēt bez mērīšanas."),

    Kopsavilkums([
        "Uzskicēju riņķī 25 %, 50 % un 75 %.",
        "Zinu, ka viss riņķis ir 100 %.",
        "Novērtēju citus procentus starp ceturtdaļu atzīmēm.",
        "Pamatoju savu skici ar skaitļiem.",
    ]),

    Majas([
        "Uzzīmē trīs riņķus un iekrāso tajos 25 %, 50 % un 75 %.",
        "Uzskicē riņķi, kurā iekrāsoti apmēram 40 %.",
        "Pieraksti, cik procentu katrā riņķī palika balti.",
    ]),
]
