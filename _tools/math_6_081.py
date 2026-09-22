# -*- coding: utf-8 -*-
"""6. klase, 81. stunda: «Kā procentus saistīt ar daļu?»

Jauns temats, bet ne jauns jēdziens: procents ir simtdaļa, un viss, ko
skolēni jau prot ar daļām, te strādā tālāk. Tāpēc stunda sākas nevis ar
definīciju, bet ar pārrakstīšanu - viens skaitlis, trīs pieraksti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Kā procentus saistīt ar daļu?"

MERKIS = ("Skaidrosim, ka «a kā b procenti» nozīmē to pašu, ko «a kā b "
          "daļa».")

SATURS = [
    Sakums("Procents ir simtdaļa un nekas cits",
           zimejums=dala(10, 3, "30 %"),
           paraksts="30 % ir {30|100}, tas ir {3|10}, tas ir 0,3 - viens "
                    "skaitlis trijos pierakstos.",
           fakti=["Vārds «procents» nozīmē «no simta».",
                  "1 % = {1|100} = 0,01.",
                  "Tāpēc viss, ko proti ar daļām, strādā arī ar procentiem."]),

    Doma("Trīs pieraksti, viens skaitlis",
         "Procents ir daļa ar saucēju 100, tāpēc katru procentu var "
         "pierakstīt kā parasto daļu un kā decimāldaļu.",
         soli=[
             "Pieraksti procentu kā daļu ar saucēju 100.",
             "Saīsini to, ja var.",
             "Pārraksti to pašu kā decimāldaļu.",
             "Pārbaudi, vai visi trīs pieraksti attēlo vienu skaitli.",
             "Izvēlies to pierakstu, kurā rēķināt ērtāk.",
         ],
         pieze="Pretējā virzienā tāpat: {1|4} = {25|100} = 25 %. Daļu "
               "paplašina līdz saucējam 100 - tieši to mācījāmies "
               "iepriekšējā tematā."),

    Slidnis("Viens un tas pats skaitlis",
            [{"v": "10 %", "teksts": "{1|10} = 0,1", "josla": 10,
              "zim": dala(10, 1)},
             {"v": "25 %", "teksts": "{1|4} = 0,25", "josla": 25,
              "zim": dala(4, 1)},
             {"v": "50 %", "teksts": "{1|2} = 0,5", "josla": 50,
              "zim": dala(2, 1)},
             {"v": "75 %", "teksts": "{3|4} = 0,75", "josla": 75,
              "zim": dala(4, 3)}],
            ievads="Spied soli pa solim: procenti, daļa un decimāldaļa mainās "
                   "kopā, jo tas ir viens skaitlis."),

    Paraugs("Pārraksti trijos veidos",
            uzd="Pieraksti 40 % kā parasto daļu un kā decimāldaļu.",
            soli=[
                ("40 % = {40|100}",
                 "Procents ir simtdaļa."),
                ("{40|100} = {2|5}",
                 "Saīsina ar 20."),
                ("{40|100} = 0,4",
                 "Simtdaļas decimālpierakstā."),
                ("Pārbaude: 0,4 · 100 = 40",
                 "Atgriežas procenti."),
            ],
            atbilde="{2|5} un 0,4"),

    Ievadi("Pārraksti citā veidā", [
        {"jaut": "Cik ir 50 % decimāldaļā?",
         "atb": ["0,5", "0.5"], "padoms": "{50|100}."},
        {"jaut": "Cik ir 25 % parastajā daļā? Atbildi raksti kā a/b.",
         "atb": ["1/4", "25/100"], "padoms": "{25|100} saīsināts."},
        {"jaut": "Cik procentu ir {1|5}?",
         "atb": ["20"], "padoms": "{20|100}."},
        {"jaut": "Cik procentu ir 0,75?",
         "atb": ["75"], "padoms": "75 simtdaļas."},
        {"jaut": "Cik ir 8 % decimāldaļā?",
         "atb": ["0,08", "0.08"], "padoms": "{8|100}."},
        {"jaut": "Cik procentu ir {3|4}?",
         "atb": ["75"], "padoms": "{75|100}."},
    ], pamats=4),

    Varianti("Kurš pieraksts ir tas pats?", [
        {"jaut": "1 % ir tas pats, kas...",
         "opcijas": ["{1|100}", "{1|10}", "0,1", "1"],
         "pareizi": 0,
         "padoms": "Viena simtdaļa."},
        {"jaut": "{1|2} ir tas pats, kas...",
         "opcijas": ["50 %", "2 %", "12 %", "0,02"],
         "pareizi": 0,
         "padoms": "{50|100}."},
        {"jaut": "0,05 ir tas pats, kas...",
         "opcijas": ["5 %", "50 %", "0,5 %", "500 %"],
         "pareizi": 0,
         "padoms": "Piecas simtdaļas."},
        {"jaut": "100 % ir tas pats, kas...",
         "opcijas": ["viss kopums", "puse", "simts", "{1|100}"],
         "pareizi": 0,
         "padoms": "{100|100} = 1."},
    ], pamats=4),

    Pasaule("Ko raksta uz iepakojuma?",
            Ievadi("", [
                {"jaut": "Sulā ir 50 % augļu. Cik tas ir daļā? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/2", "50/100"], "padoms": "{50|100}."},
                {"jaut": "Jogurtā ir 2,5 % tauku. Cik tas ir decimāldaļā?",
                 "atb": ["0,025", "0.025"], "padoms": "{2,5|100}."},
                {"jaut": "Maizē ir {1|4} rudzu miltu. Cik procentu tas ir?",
                 "atb": ["25"], "padoms": "{25|100}."},
                {"jaut": "Sokolādē ir 0,7 kakao. Cik procentu tas ir?",
                 "atb": ["70"], "padoms": "70 simtdaļas."},
            ]),
            pavediens="veikals",
            konteksts="Uz iepakojumiem sastāvu raksta procentos, receptēs - "
                      "daļās; tie ir viens un tas pats.",
            kapec="Pāreja starp pierakstiem ļauj salīdzināt produktus."),

    Kopsavilkums([
        "Zinu, ka procents ir simtdaļa.",
        "Pārrakstu procentus kā parasto daļu un kā decimāldaļu.",
        "Pārrakstu daļu un decimāldaļu kā procentus.",
        "Izvēlos ērtāko pierakstu rēķinam.",
    ]),

    Majas([
        "Pieraksti 10 %, 60 % un 5 % visos trijos veidos.",
        "Atrodi mājās iepakojumu ar procentiem un pārraksti tos kā daļu.",
        "Paskaidro kādam, kāpēc 50 % ir puse.",
    ]),
]
