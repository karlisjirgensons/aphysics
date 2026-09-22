# -*- coding: utf-8 -*-
"""5. klase, 8. stunda: «Kā lasa romiešu ciparus?»

Romiešu pieraksts ir otrs piemērs tam, ka pieraksta sistēmu var būt vairākas.
Šajā stundā tikai lasa un raksta pamata zīmes; saskaitīšanas un atņemšanas
likums nāk nākamajā stundā, lai abas lietas nesajauktos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Kā lasa romiešu ciparus?"

MERKIS = ("Iemācīsimies romiešu ciparu zīmes un izlasīsim ar tām pierakstītus "
          "skaitļus.")

SATURS = [
    Sakums("Cik zīmju vajag skaitlim 38?",
           zimejums=kolonnas([("mūsu", 2), ("romiešu", 7), ("binārais", 6)]),
           paraksts="38, XXXVIII un 100110 - viens skaitlis, trīs garumi.",
           fakti=["Romiešu pierakstā nav nulles un nav vietas nozīmes.",
                  "Tos vēl redz uz pulksteņiem un gadsimtu apzīmējumos."]),

    Doma("Katrai zīmei sava vērtība",
         "Romiešu ciparus parasti saskaita no kreisās uz labo.",
         soli=[
             "I ir 1, V ir 5, X ir 10.",
             "L ir 50, C ir 100, D ir 500, M ir 1000.",
             "Zīmes raksta no lielākās uz mazāko un saskaita.",
             "Vienu zīmi pēc kārtas neraksta vairāk par trim reizēm.",
         ],
         pieze="Atceries pēc kārtas: I, V, X, L, C, D, M. Vērtības aug: "
               "1, 5, 10, 50, 100, 500, 1000."),

    Paraugs("Ko nozīmē XXVII?",
            uzd="Izlasi romiešu skaitli XXVII.",
            soli=[
                ("X = 10, X = 10, V = 5, I = 1, I = 1",
                 "Vispirms katrai zīmei pieraksta tās vērtību."),
                ("10 + 10 + 5 + 1 + 1",
                 "Zīmes iet no lielākās uz mazāko, tāpēc visas saskaita."),
                ("= 27", "Saskaita un pieraksta atbildi."),
            ],
            atbilde="XXVII ir 27"),

    Ievadi("Izlasi romiešu skaitli", [
        {"jaut": "VII", "atb": ["7"], "padoms": "5 + 1 + 1."},
        {"jaut": "XV", "atb": ["15"], "padoms": "10 + 5."},
        {"jaut": "XXXI", "atb": ["31"], "padoms": "10 + 10 + 10 + 1."},
        {"jaut": "LXII", "atb": ["62"], "padoms": "50 + 10 + 1 + 1."},
        {"jaut": "CLV", "atb": ["155"], "padoms": "100 + 50 + 5."},
        {"jaut": "MDC", "atb": ["1600"], "padoms": "1000 + 500 + 100."},
    ], pamats=4,
        ievads="Ieraksti, kāds skaitlis tas ir mūsu pierakstā."),

    Ievadi("Uzraksti ar romiešu cipariem", [
        {"jaut": "12", "atb": ["xii"], "padoms": "10 + 1 + 1.",
         "tastatura": "text", "vieta": "XII"},
        {"jaut": "26", "atb": ["xxvi"], "padoms": "10 + 10 + 5 + 1.",
         "tastatura": "text"},
        {"jaut": "70", "atb": ["lxx"], "padoms": "50 + 10 + 10.",
         "tastatura": "text"},
        {"jaut": "300", "atb": ["ccc"], "padoms": "100 + 100 + 100.",
         "tastatura": "text"},
    ], ievads="Lielos vai mazos burtus - vienalga."),

    Varianti("Kurš pieraksts ir pareizs?", [
        {"jaut": "Kā pareizi uzrakstīt 30?",
         "opcijas": ["XXX", "XXXX", "LX", "VVVVVV"],
         "pareizi": 0,
         "padoms": "Trīs desmiti."},
        {"jaut": "Kāpēc IIII nav pareizs pieraksts?",
         "opcijas": ["Vienu zīmi neraksta četras reizes pēc kārtas",
                     "Tāpēc, ka I ir par mazu",
                     "Tāpēc, ka trūkst V",
                     "Tāpēc, ka jāraksta no labās uz kreiso"],
         "pareizi": 0,
         "padoms": "Vairāk par trim vienādām zīmēm pēc kārtas neraksta."},
        {"jaut": "Kurš no šiem ir lielākais skaitlis?",
         "opcijas": ["CL", "LX", "XC", "XL"],
         "pareizi": 0,
         "padoms": "CL = 150."},
        {"jaut": "Kurā gadsimtā dzīvojam, ja rakstām XXI?",
         "opcijas": ["21.", "19.", "16.", "11."],
         "pareizi": 0,
         "padoms": "X + X + I."},
    ], pamats=4),

    Pasaule("Kurā gadā uzņemta filma?",
            Ievadi("", [
                {"jaut": "Filmas beigās raksta MCMXCIX. Kurš tas gads?",
                 "atb": ["1999"], "padoms": "M + CM + XC + IX."},
                {"jaut": "Grāmatas nodaļa XVII - kura tā pēc kārtas?",
                 "atb": ["17"], "padoms": "10 + 5 + 1 + 1."},
                {"jaut": "Uz ēkas rakstīts MCMLXXX. Kurš gads?",
                 "atb": ["1980"], "padoms": "1000 + 900 + 50 + 30."},
                {"jaut": "Kurā gadsimtā ir 1980. gads?",
                 "atb": ["20"], "padoms": "Gadi no 1901 līdz 2000."},
            ]),
            pavediens="dati",
            konteksts="Filmu beigās un uz ēkām gadu bieži raksta ar romiešu "
                      "cipariem.",
            kapec="Lai vecu uzrakstu izlasītu, pietiek zināt septiņas "
                  "zīmes."),

    Kopsavilkums([
        "Zinu romiešu ciparu zīmes I, V, X, L, C, D un M.",
        "Izlasu romiešu skaitli, kurā zīmes iet no lielākās uz mazāko.",
        "Uzrakstu skaitli ar romiešu cipariem, neatkārtojot zīmi vairāk par "
        "trim reizēm.",
    ]),

    Majas([
        "Atrodi mājās vai pilsētā kaut ko uzrakstītu ar romiešu cipariem.",
        "Uzraksti ar romiešu cipariem savu dzimšanas dienas datumu un mēnesi.",
        "Padomā, kāpēc ar romiešu cipariem būtu grūti sareizināt XXIV un "
        "XVI.",
    ]),
]
