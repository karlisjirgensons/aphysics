# -*- coding: utf-8 -*-
"""5. klase, 172. stunda: «Ko gribu iemācīties 6. klasē?»

Mācību gada pēdējā stunda. Te nav jauna rēķina un nav pārbaudes: ir viens
skatiens atpakaļ un viens uz priekšu. Gads sākās ar naturāliem skaitļiem un
beidzās ar grafikiem, un 6. klasē tas pats ceļš turpinās - tikai ar
negatīviem skaitļiem, attiecībām un ķermeņu tilpumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis, taisne)

TEMA = "Ko gribu iemācīties 6. klasē?"

MERKIS = ("Apkoposim gadā apgūto un iepazīsimies ar 6. klases tematiem.")

SATURS = [
    Sakums("Gads astoņos tematos",
           zimejums=restis([["1/4", "2 1/3", "0,25", "25 %"]],
                           virsraksts="Viens skaitlis, četras valodas"),
           paraksts="Gada laikā iemācījāmies pārtulkot starp visām četrām.",
           fakti=["Gads sākās ar naturāliem skaitļiem līdz miljardam.",
                  "Pa vidu bija daļas, leņķi un laukumi.",
                  "Beidzās ar procentiem un grafikiem."]),

    Doma("Katrs temats turpinās nākamajā gadā",
         "6. klasē turpinās tas pats: daļas kļūs par attiecībām, "
         "decimāldaļas - par reizināšanu un dalīšanu, figūras - par "
         "telpiskiem ķermeņiem.",
         soli=[
             "Daļas 6. klasē reizinās un dalīs.",
             "Parādīsies negatīvi skaitļi - zem nulles.",
             "Attiecība kļūs par atsevišķu tematu.",
             "Figūrām rēķinās virsmas laukumu un tilpumu.",
             "Grafiki paliks, bet kļūs sarežģītāki.",
         ],
         pieze="Viss, kas šogad iemācīts, nākamgad ir pamats. Tāpēc "
               "kopsavilkumi, kas rakstīti katras stundas beigās, ir vērtīgi "
               "arī vasarā - tie ir īsākais atkārtojums."),

    Paraugs("Viens skaitlis četrās valodās",
            uzd="Pieraksti ceturtdaļu visos veidos, kas mācīti šogad.",
            soli=[
                ("{1|4}",
                 "Parastā daļa."),
                ("0,25",
                 "Decimāldaļa."),
                ("25 %",
                 "Procenti."),
                ("90° riņķī",
                 "Sektors diagrammā."),
            ],
            atbilde="{1|4} = 0,25 = 25 % = 90° sektors"),

    Ievadi("Gada kopsavilkums", [
        {"jaut": "{1|4} kā decimāldaļa. Ieraksti skaitli.",
         "atb": ["0,25"], "padoms": "{25|100}."},
        {"jaut": "{1|4} procentos. Ieraksti skaitli.",
         "atb": ["25"], "padoms": "{25|100}."},
        {"jaut": "Cik grādu ir 25 % sektoram?",
         "atb": ["90"], "padoms": "360 : 4."},
        {"jaut": "Cik ir {1|2} + {1|3}? Atbildi raksti kā a/b.",
         "atb": ["5/6"], "padoms": "Kopsaucējs 6."},
        {"jaut": "Cik ir 25 % no 80?",
         "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "Cik grādu ir izstieptam leņķim?",
         "atb": ["180"], "padoms": "Puse apgrieziena."},
        {"jaut": "Taisnstūris 6 m x 4 m. Cik kvadrātmetru ir laukums?",
         "atb": ["24"], "padoms": "6 · 4."},
        {"jaut": "Cik ir 3,45 + 1,2?",
         "atb": ["4,65"], "padoms": "1,2 = 1,20."},
    ], pamats=4,
        ievads="Pa vienam uzdevumam no katra gada temata."),

    Zimejums("Kas gaida 6. klasē",
             taisne(1, 8, 1, [(8, "un tālāk")],
                    virsraksts="Astoņi šī gada temati"),
             paskaidro="Katrs no tiem turpina kaut ko no šī gada: attiecības "
                       "nāk no daļām, tilpums - no laukuma.",
             ievads="Nākamais gads sāksies tur, kur šis beidzās."),

    Varianti("Ko atceries no gada?", [
        {"jaut": "Kas ir procents?",
         "opcijas": ["Viena simtdaļa", "Viena desmitdaļa", "Viens vesels",
                     "Mērvienība"],
         "pareizi": 0,
         "padoms": "Saucējs 100."},
        {"jaut": "Cik grādu ir pilnam leņķim?",
         "opcijas": ["360°", "180°", "90°", "100°"],
         "pareizi": 0,
         "padoms": "Viss apgrieziens."},
        {"jaut": "Ar ko sākas daļu saskaitīšana ar dažādiem saucējiem?",
         "opcijas": ["Ar kopsaucēju", "Ar saīsināšanu", "Ar novērtējumu",
                     "Ar atbildi"],
         "pareizi": 0,
         "padoms": "Vienādi gabali vispirms."},
        {"jaut": "Kurš skaitlis ir lielāks - 0,45 vai 0,5?",
         "opcijas": ["0,5", "0,45", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "0,50 pret 0,45."},
        {"jaut": "Ko rāda sektoru diagramma?",
         "opcijas": ["Daļas no viena veselā", "Izmaiņu laikā",
                     "Cilvēku skaitu", "Leņķus"],
         "pareizi": 0,
         "padoms": "Procentus."},
        {"jaut": "Kas turpināsies 6. klasē?",
         "opcijas": ["Viss, kas mācīts šogad", "Tikai daļas",
                     "Tikai ģeometrija", "Nekas"],
         "pareizi": 0,
         "padoms": "Katrs temats ir pamats nākamajam."},
    ], pamats=4),

    Pasaule("Ko šogad iemācījos par savu dienu?",
            Ievadi("", [
                {"jaut": "Skolā pagāja {1|3} dienas, mājasdarbos {1|6}. Cik "
                         "daļa kopā? Atbildi raksti kā a/b.",
                 "atb": ["1/2", "3/6"], "padoms": "{2|6} + {1|6}."},
                {"jaut": "Cik procentu no dienas tas ir?",
                 "atb": ["50"], "padoms": "{1|2} = 50 %."},
                {"jaut": "Cik stundu tas ir no 24 stundām?",
                 "atb": ["12"], "padoms": "24 : 2."},
                {"jaut": "Cik grādu būtu šis sektors diagrammā?",
                 "atb": ["180"], "padoms": "360 : 2."},
            ]),
            pavediens="skola",
            konteksts="Viens jautājums par savu dienu izmanto daļas, "
                      "procentus, leņķus un diagrammu - visu gadu vienā "
                      "uzdevumā.",
            kapec="Tieši tā matemātika arī strādā: temati nav atsevišķi."),

    Kopsavilkums([
        "Apkopoju, ko esmu iemācījies šajā gadā.",
        "Pārtulkoju vienu skaitli daļā, decimāldaļā un procentos.",
        "Zinu, kuri temati turpināsies 6. klasē.",
        "Atzīmēju, ko vēl gribu apgūt labāk.",
    ]),

    Majas([
        "Uzraksti trīs lietas, ko šogad iemācījies vislabāk.",
        "Uzraksti vienu, ko gribētu atkārtot vasarā.",
        "Uzraksti, ko gaidi no 6. klases.",
    ]),
]
