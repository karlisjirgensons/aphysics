# -*- coding: utf-8 -*-
"""3. klase, 97. stunda: «Kā desmitdaļu pieraksta ar komatu?»

Pirmā decimāldaļa. Tā nav jauna doma, bet jauns *pieraksts* tam pašam, ko
skolēns jau prot: {3|10} un 0,3 ir viens un tas pats skaitlis. Latviešu
standartā decimāldaļu atdala komats, nevis punkts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         dala)

TEMA = "Kā desmitdaļu pieraksta ar komatu?"

MERKIS = ("Pierakstīsim daļu ar saucēju 10 kā decimāldaļu un lasīsim to "
          "divējādi.")

SATURS = [
    Sakums("Kāpēc uz cenu zīmes nav daļsvītras?",
           zimejums=dala(10, 3, "3/10 = 0,3", "desmit vienādas daļas"),
           paraksts="Viena un tā pati daļa, divi pieraksti.",
           fakti=["Daļu ar saucēju 10 var pierakstīt ar komatu.",
                  "{3|10} un 0,3 ir viens un tas pats skaitlis.",
                  "Latviski decimāldaļu atdala komats, ne punkts."]),

    Doma("Aiz komata raksta desmitdaļas",
         "0,3 nozīmē nulle veselo un trīs desmitdaļas - tas ir tas pats, kas "
         "{3|10}.",
         soli=[
             "Paskaties, vai saucējs ir 10.",
             "Pirms komata raksti veselo daļu - šeit 0.",
             "Aiz komata raksti skaitītāju.",
             "Izlasi to divējādi: «nulle komats trīs» vai «trīs desmitdaļas».",
         ],
         pieze="Ja veselo ir vairāk, tos raksta pirms komata: {13|10} ir "
               "1,3 - viens vesels un trīs desmitdaļas."),

    Slidnis("Kā aug desmitdaļas",
            soli=[
                {"v": "0,1", "teksts": "Viena desmitdaļa.", "josla": 10},
                {"v": "0,3", "teksts": "Trīs desmitdaļas.", "josla": 30},
                {"v": "0,5", "teksts": "Piecas - tā ir puse.", "josla": 50},
                {"v": "1,0", "teksts": "Desmit desmitdaļas - viens vesels.",
                 "josla": 100},
            ],
            ievads="Katrs solis pieliek desmitdaļas."),

    Paraugs("Kā pierakstīt {7|10} ar komatu?",
            uzd="Pieraksti daļu {7|10} kā decimāldaļu.",
            soli=[
                ("Saucējs ir 10",
                 "Tātad daļu var rakstīt ar komatu."),
                ("Veselo nav, tāpēc pirms komata 0",
                 "Daļa ir mazāka par vienu."),
                ("0,7",
                 "Lasa: «nulle komats septiņi» jeb «septiņas desmitdaļas»."),
            ],
            atbilde="0,7"),

    Ievadi("Pieraksti ar komatu", [
        {"jaut": "Pieraksti {3|10} ar komatu.", "atb": ["0,3", "0.3"],
         "padoms": "Nulle, komats, skaitītājs."},
        {"jaut": "Pieraksti {7|10} ar komatu.", "atb": ["0,7", "0.7"],
         "padoms": "Nulle komats septiņi."},
        {"jaut": "Pieraksti {5|10} ar komatu.", "atb": ["0,5", "0.5"],
         "padoms": "Tā ir puse."},
        {"jaut": "Cik desmitdaļu ir 0,9? Ieraksti skaitli.", "atb": ["9"],
         "padoms": "Cipars aiz komata."},
        {"jaut": "Pieraksti {12|10} ar komatu.", "atb": ["1,2", "1.2"],
         "padoms": "Viens vesels un divas desmitdaļas."},
        {"jaut": "Cik ir 0,5 no 20?", "atb": ["10"],
         "padoms": "Puse no 20."},
    ], pamats=4),

    Zimejums("Puse ar komatu",
             dala(10, 5, "5/10 = 0,5", "piecas desmitdaļas"),
             paskaidro="Viena un tā pati puse trijos pierakstos: {1|2}, "
                       "{5|10} un 0,5.",
             ievads="Tā izskatās 0,5."),

    Varianti("Kurš pieraksts der?", [
        {"jaut": "Kā pieraksta {4|10} ar komatu?",
         "opcijas": ["0,4", "4,0", "0,04", "4,10"],
         "pareizi": 0, "padoms": "Nulle veselo, četras desmitdaļas."},
        {"jaut": "Cik ir 0,5?",
         "opcijas": ["{5|10}", "{5|100}", "{1|5}", "{10|5}"],
         "pareizi": 0, "padoms": "Piecas desmitdaļas."},
        {"jaut": "Kurš skaitlis ir lielākais?",
         "opcijas": ["0,9", "0,5", "0,3", "0,1"],
         "pareizi": 0, "padoms": "Vairāk desmitdaļu."},
        {"jaut": "Ar ko latviski atdala decimāldaļu?",
         "opcijas": ["Ar komatu", "Ar punktu", "Ar atstarpi",
                     "Ar daļsvītru"],
         "pareizi": 0, "padoms": "Latviešu standarts."},
    ], pamats=4),

    Pasaule("Cik maksā prece?",
            Ievadi("", [
                {"jaut": "Cena ir 0,5 eiro. Cik centu tas ir?",
                 "atb": ["50"], "padoms": "Puse no 100."},
                {"jaut": "Cena ir 0,3 eiro. Cik centu tas ir?",
                 "atb": ["30"], "padoms": "Trīs desmitdaļas no 100."},
                {"jaut": "Cik maksā 2 preces pa 0,5 eiro? Raksti eiro ar "
                         "komatu.",
                 "atb": ["1", "1,0", "1.0"], "padoms": "Divas puses."},
                {"jaut": "Cik centu maksā 3 preces pa 0,3 eiro?",
                 "atb": ["90"], "padoms": "3 · 30."},
            ]),
            pavediens="veikals",
            konteksts="Cenu zīmē eiro un centus atdala komats - tieši tāpat "
                      "kā veselos un desmitdaļas.",
            kapec="Tāpēc, lasot cenu, tu jau lasi decimāldaļu."),

    Kopsavilkums([
        "Pierakstu daļu ar saucēju 10 kā decimāldaļu.",
        "Lasu decimāldaļu divējādi.",
        "Zinu, ka latviski decimāldaļu atdala komats.",
        "Zinu, ka {5|10} = 0,5 = {1|2}.",
    ]),

    Majas([
        "Pieraksti ar komatu {1|10}, {6|10} un {9|10}.",
        "Atrodi veikalā trīs cenas ar komatu un izlasi tās skaļi.",
        "Uzzīmē modeli skaitlim 0,4.",
    ]),
]
