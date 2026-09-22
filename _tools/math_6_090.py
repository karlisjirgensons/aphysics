# -*- coding: utf-8 -*-
"""6. klase, 90. stunda: «Ko rāda skolas sporta dati?»

Datu stunda. Skolēni paši ir datu avots, un tieši tāpēc secinājumi te ir
īsti. Procenti kļūst par valodu, kurā par klasi var pateikt vairāk nekā ar
skaitļiem - jo klases ir dažāda lieluma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Ko rāda skolas sporta dati?"

MERKIS = ("Apkoposim datus, apstrādāsim tos un formulēsim secinājumus, "
          "lietojot procentus un daļas.")

SATURS = [
    Sakums("Skaitļi maldina, procenti - ne",
           zimejums=kolonnas([("6.a", 12), ("6.b", 15), ("6.c", 9)]),
           paraksts="Trīs klases, dažāds sportotāju skaits - bet arī klases "
                    "ir dažāda lieluma.",
           fakti=["Lielākā klase var izskatīties aktīvāka tikai tāpēc, ka "
                  "tā ir lielāka.",
                  "Procenti padara klases salīdzināmas.",
                  "Secinājumu vienmēr pamato ar skaitli."]),

    Doma("Vispirms apkopo, tad pārrēķini, tad secini",
         "Datus apstrādā trijos soļos: apkopo tabulā, pārrēķina procentos un "
         "tikai tad formulē secinājumu.",
         soli=[
             "Izveido tabulu: grupa, daļa, kopums.",
             "Katrai grupai aprēķini procentus.",
             "Sakārto procentus augošā vai dilstošā secībā.",
             "Formulē secinājumu vienā teikumā.",
             "Pamato to ar konkrētu skaitli.",
         ],
         pieze="Secinājums bez skaitļa nav secinājums. «6.c ir aktīvākā» ir "
               "viedoklis; «6.c sporto 45 %, pārējās mazāk par 40 %» ir "
               "secinājums."),

    Paraugs("Salīdzini trīs klases",
            uzd="6.a: 12 no 24; 6.b: 15 no 30; 6.c: 9 no 20. Kura klase "
                "sporto visaktīvāk?",
            soli=[
                ("6.a: {12|24} = 50 %",
                 "Puse."),
                ("6.b: {15|30} = 50 %",
                 "Arī puse."),
                ("6.c: {9|20} = 45 %",
                 "Mazāk nekā puse."),
                ("6.a un 6.b ir vienlīdz aktīvas",
                 "Lielākais skaitlis nenozīmē lielāko daļu."),
            ],
            atbilde="6.a un 6.b - abām 50 %"),

    Ievadi("Pārrēķini procentos", [
        {"jaut": "12 no 24. Cik procenti?",
         "atb": ["50"], "padoms": "Puse."},
        {"jaut": "15 no 30. Cik procenti?",
         "atb": ["50"], "padoms": "Arī puse."},
        {"jaut": "9 no 20. Cik procenti?",
         "atb": ["45"], "padoms": "{9|20} = {45|100}."},
        {"jaut": "7 no 28. Cik procenti?",
         "atb": ["25"], "padoms": "{1|4}."},
        {"jaut": "18 no 24. Cik procenti?",
         "atb": ["75"], "padoms": "{3|4}."},
        {"jaut": "Klasē 25 skolēni, sporto 40 %. Cik skolēnu tas ir?",
         "atb": ["10"], "padoms": "40 · 0,25."},
    ], pamats=4),

    Petijums("Apkopo savas klases datus",
             vajag="klases saraksts un burtnīca",
             soli=[
                 "Izvēlieties jautājumu: cik daudzi apmeklē pulciņu, brauc "
                 "ar velosipēdu vai sporto.",
                 "Savāciet datus un pierakstiet tos tabulā.",
                 "Aprēķiniet procentus.",
                 "Uzzīmējiet stabiņu attēlu.",
                 "Formulējiet vienu secinājumu ar skaitli.",
             ],
             secinajums="Ja klasē ir 25 skolēni, viens skolēns ir 4 % - "
                        "tāpēc mazā klasē katrs skaitlis ir «smagāks»."),

    Varianti("Kurš secinājums ir pamatots?", [
        {"jaut": "6.a: 12 no 24; 6.c: 9 no 20. Kurš apgalvojums ir "
                 "pareizs?",
         "opcijas": ["6.a sporto lielāka daļa", "6.c sporto lielāka daļa",
                     "Abās vienādi", "Nevar salīdzināt"],
         "pareizi": 0,
         "padoms": "50 % pret 45 %."},
        {"jaut": "Kāpēc nevar salīdzināt tikai skaitļus?",
         "opcijas": ["Jo klases ir dažāda lieluma",
                     "Jo skaitļi ir lieli",
                     "Jo procenti ir precīzāki", "Var salīdzināt"],
         "pareizi": 0,
         "padoms": "12 no 24 un 12 no 40 nav viens un tas pats."},
        {"jaut": "Klasē 25 skolēni. Cik procentu ir viens skolēns?",
         "opcijas": ["4", "1", "25", "2,5"],
         "pareizi": 0,
         "padoms": "100 : 25."},
        {"jaut": "Kas secinājumā ir obligāts?",
         "opcijas": ["Skaitlis, kas to pamato", "Stabiņu attēls",
                     "Tabula", "Procentu zīme"],
         "pareizi": 0,
         "padoms": "Bez skaitļa tas ir viedoklis."},
    ], pamats=4),

    Pasaule("Ko rāda skolas dati?",
            Ievadi("", [
                {"jaut": "Skolā 400 skolēnu, sporto 160. Cik procenti?",
                 "atb": ["40"], "padoms": "{160|400} = {2|5}."},
                {"jaut": "Pērn sportoja 140. Cik procenti tas bija?",
                 "atb": ["35"], "padoms": "{140|400}."},
                {"jaut": "Par cik procentu punktiem tas pieauga?",
                 "atb": ["5"], "padoms": "40 − 35."},
                {"jaut": "Par cik cilvēkiem tas pieauga?",
                 "atb": ["20"], "padoms": "160 − 140."},
            ]),
            pavediens="sports",
            konteksts="Skolas gada pārskatā datus rāda procentos, lai tos "
                      "varētu salīdzināt ar iepriekšējo gadu.",
            kapec="Procenti ļauj salīdzināt arī tad, ja kopums ir mainījies."),

    Zimejums("Trīs klases procentos",
             kolonnas([("6.a", 50), ("6.b", 50), ("6.c", 45)], " %"),
             paskaidro="Tie paši dati procentos: tagad stabiņi ir "
                       "salīdzināmi, jo visu klašu kopums ir 100 %.",
             ievads="Salīdzini šo attēlu ar stundas sākuma attēlu."),

    Kopsavilkums([
        "Apkopoju datus tabulā un pārrēķinu tos procentos.",
        "Salīdzinu dažāda lieluma grupas.",
        "Attēloju datus stabiņu attēlā.",
        "Formulēju secinājumu un pamatoju to ar skaitli.",
    ]),

    Majas([
        "Savāc datus par savu ģimeni vai draugiem un pārrēķini tos "
        "procentos.",
        "Uzzīmē stabiņu attēlu saviem datiem.",
        "Pieraksti vienu secinājumu ar skaitli.",
    ]),
]
