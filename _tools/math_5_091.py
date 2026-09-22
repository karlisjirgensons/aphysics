# -*- coding: utf-8 -*-
"""5. klase, 91. stunda: «Kas ir jaukts skaitlis?»

Jauna temata pirmā stunda. Jaukts skaitlis skolēnam jau ir pazīstams no
sarunas - «pusotra glāze» -, bet nav pazīstams kā pieraksts. Tāpēc stunda
sākas nevis ar pārveidošanu, bet ar lasīšanu: 1{1|2} ir summa, kurā plusa
zīme vienkārši nav uzrakstīta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, taisne)

TEMA = "Kas ir jaukts skaitlis?"

MERKIS = ("Iemācīsimies izskaidrot jauktu skaitli kā vesela skaitļa un "
          "īstas daļas summu.")

SATURS = [
    Sakums("Pusotra glāze piena",
           zimejums=taisne(0, 2, 1, [(1.5, "1 1/2")],
                           virsraksts="Starp 1 un 2"),
           paraksts="1{1|2} ir viens vesels un vēl puse.",
           fakti=["Receptē raksta «pusotra glāze».",
                  "Matemātikā to pašu raksta 1{1|2}.",
                  "Tas ir viens skaitlis, nevis divi."]),

    Doma("Vesels un daļa vienā skaitlī",
         "Jaukts skaitlis sastāv no vesela skaitļa un īstas daļas; tas "
         "nozīmē to pašu, ko abu summa.",
         soli=[
             "Nolasi veselo daļu - lielo skaitli pa kreisi.",
             "Nolasi daļu - tai jābūt īstai, mazākai par 1.",
             "Izlasi visu: «viens vesels un viena puse».",
             "Pieraksti to pašu kā summu: 1 + {1|2}.",
             "Pārbaudi, vai daļa tiešām ir īsta.",
         ],
         pieze="Jauktā skaitļa daļai vienmēr jābūt īstai. Pieraksts 1{3|2} "
               "nav pareizs: {3|2} pati jau ir lielāka par vienu, tāpēc "
               "veselais tajā vēl nav atdalīts."),

    Paraugs("Izlasi 2{3|4}",
            uzd="Paskaidro, ko nozīmē jauktais skaitlis 2{3|4}.",
            soli=[
                ("Veselā daļa ir 2",
                 "Divi veseli."),
                ("Daļa ir {3|4}",
                 "Trīs ceturtdaļas - īsta daļa."),
                ("2{3|4} = 2 + {3|4}",
                 "Tā pati summa, tikai bez plusa."),
                ("Tas ir starp 2 un 3",
                 "Bet tuvāk trijniekam."),
            ],
            atbilde="2{3|4} ir divi veseli un trīs ceturtdaļas"),

    Ievadi("Nosaki veselo un daļu", [
        {"jaut": "Kāda ir jauktā skaitļa 2{3|4} veselā daļa?",
         "atb": ["2"], "padoms": "Lielais skaitlis pa kreisi."},
        {"jaut": "Kāda ir jauktā skaitļa 5{1|3} veselā daļa?",
         "atb": ["5"], "padoms": "Lielais skaitlis pa kreisi."},
        {"jaut": "Kāds ir jauktā skaitļa 3{2|5} daļas saucējs?",
         "atb": ["5"], "padoms": "Zem svītras."},
        {"jaut": "Kāds ir jauktā skaitļa 3{2|5} daļas skaitītājs?",
         "atb": ["2"], "padoms": "Virs svītras."},
        {"jaut": "Starp kuriem veseliem skaitļiem atrodas 4{1|6}? Ieraksti "
                 "mazāko.",
         "atb": ["4"], "padoms": "Veselā daļa."},
        {"jaut": "Starp kuriem veseliem skaitļiem atrodas 4{1|6}? Ieraksti "
                 "lielāko.",
         "atb": ["5"], "padoms": "Nākamais vesels skaitlis."},
        {"jaut": "Cik ir 1 + {1|2}? Atbildi raksti kā a b/c, piemēram 1 1/2.",
         "atb": ["1 1/2", "3/2"], "padoms": "Jaukts skaitlis."},
        {"jaut": "Cik ir 2 + {3|4}? Atbildi raksti kā a b/c.",
         "atb": ["2 3/4", "11/4"], "padoms": "Jaukts skaitlis."},
    ], pamats=4,
        ievads="Jauktā skaitlī ir divas daļas: vesels skaitlis un īsta daļa."),

    Zimejums("Viens vesels un vēl puse",
             dala(2, 1, "1/2 no otrā vesela"),
             paskaidro="Pirmā josla ir viens vesels, šī otrā ir tikai līdz "
                       "pusei. Kopā tas ir 1{1|2}.",
             ievads="Jauktu skaitli zīmē kā veselu un vēl gabalu."),

    Varianti("Kurš pieraksts ir pareizs?", [
        {"jaut": "Ko nozīmē 3{1|4}?",
         "opcijas": ["3 + {1|4}", "3 · {1|4}", "3 - {1|4}", "{3|4}"],
         "pareizi": 0,
         "padoms": "Vesels un daļa kopā."},
        {"jaut": "Kurš pieraksts *nav* pareizs jaukts skaitlis?",
         "opcijas": ["1{3|2}", "1{1|2}", "2{3|4}", "5{1|6}"],
         "pareizi": 0,
         "padoms": "Daļai jābūt īstai."},
        {"jaut": "Kāda jābūt jauktā skaitļa daļai?",
         "opcijas": ["Īstai, mazākai par 1", "Neīstai", "Nesaīsināmai",
                     "Ar saucēju 2"],
         "pareizi": 0,
         "padoms": "Citādi veselais nav atdalīts."},
        {"jaut": "Starp kuriem skaitļiem atrodas 7{2|3}?",
         "opcijas": ["7 un 8", "6 un 7", "2 un 3", "7 un 7"],
         "pareizi": 0,
         "padoms": "Veselā daļa ir 7."},
        {"jaut": "Kā sarunā sauc skaitli 1{1|2}?",
         "opcijas": ["Pusotrs", "Divarpus", "Pusē", "Viens un divi"],
         "pareizi": 0,
         "padoms": "Pusotra glāze."},
        {"jaut": "Vai 2{1|2} ir lielāks par 2?",
         "opcijas": ["Jā, par pusi", "Nē", "Tikpat", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Veselais plus daļa."},
    ], pamats=4),

    Pasaule("Receptē ir pusotra glāze",
            Ievadi("", [
                {"jaut": "Receptē 1{1|2} glāzes miltu. Cik veselu glāžu tas "
                         "ir vismaz?",
                 "atb": ["1"], "padoms": "Veselā daļa."},
                {"jaut": "Cik vēl jāpieliek klāt? Atbildi raksti kā a/b.",
                 "atb": ["1/2"], "padoms": "Daļa."},
                {"jaut": "Receptē 2{3|4} glāzes ūdens. Cik veselu glāžu tas "
                         "ir vismaz?",
                 "atb": ["2"], "padoms": "Veselā daļa."},
                {"jaut": "Receptē 3{1|3} glāzes piena. Kāds ir daļas "
                         "saucējs?",
                 "atb": ["3"], "padoms": "Zem svītras."},
            ]),
            pavediens="virtuve",
            konteksts="Receptēs jaukti skaitļi ir visur: pusotra glāze, "
                      "divarpus karotes.",
            kapec="Lai pēc receptes varētu rēķināt, jāsaprot abas skaitļa "
                  "daļas."),

    Kopsavilkums([
        "Izlasu jauktu skaitli un nosaucu tā veselo daļu un daļu.",
        "Skaidroju jauktu skaitli kā vesela skaitļa un īstas daļas summu.",
        "Zinu, ka jauktā skaitļa daļai jābūt īstai.",
        "Nosaku, starp kuriem veseliem skaitļiem atrodas jaukts skaitlis.",
    ]),

    Majas([
        "Uzraksti piecus jauktus skaitļus un izlasi tos skaļi.",
        "Atrodi receptē jauktu skaitli un pieraksti to kā summu.",
        "Paskaidro, kāpēc 2{5|4} nav pareizs pieraksts.",
    ]),
]
