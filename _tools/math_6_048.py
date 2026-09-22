# -*- coding: utf-8 -*-
"""6. klase, 48. stunda: «Kā algoritmi saistīti savā starpā?»

Mikrotemata noslēgums. Četri algoritmi izrādās divi pāri, un abos pāros ir
viens un tas pats: komata solis pa labi vai pa kreisi. Kad skolēns to
pamana, no galvas vairs nav jāmācās nekas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā algoritmi saistīti savā starpā?"

MERKIS = ("Raksturosim saistību starp četriem algoritmiem un lietosim tos "
          "aprēķinos.")

SATURS = [
    Sakums("Četri likumi, divi virzieni",
           zimejums=restis([["· 10", "· 0,1"],
                            [": 0,1", ": 10"]],
                           "pa labi / pa kreisi"),
           paraksts="Kreisajā kolonnā komats iet pa labi, labajā - pa "
                    "kreisi. Katrā rindā ir viens un tas pats rezultāts.",
           fakti=["Reizināt ar 10 = dalīt ar 0,1.",
                  "Dalīt ar 10 = reizināt ar 0,1.",
                  "Tāpēc atceras nevis četrus likumus, bet vienu virzienu."]),

    Doma("Nosaki virzienu, tad soļu skaitu",
         "Visi četri algoritmi ir viens: vispirms nosaki, vai skaitlis augs "
         "vai sarūk, tad saskaiti, par cik vietām komats ceļo.",
         soli=[
             "Paskaties, vai darbības rezultāts būs lielāks vai mazāks.",
             "Lielāks - komats pa labi; mazāks - pa kreisi.",
             "Saskaiti nulles vai ciparus aiz komata - tas ir soļu skaits.",
             "Pārcel komatu un pieraksti trūkstošās nulles.",
             "Pārbaudi ar pretējo darbību.",
         ],
         pieze="Virziena noteikšana ir svarīgāka par soļu skaitīšanu: soli "
               "var pārskaitīt, bet nepareizs virziens padara atbildi "
               "simtkārt greizu."),

    Paraugs("Vienā izteiksmē visi četri",
            uzd="Cik ir 2,5 · 100 : 0,1 · 0,01?",
            soli=[
                ("2,5 · 100 = 250",
                 "Divas vietas pa labi."),
                ("250 : 0,1 = 2500",
                 "Viena vieta pa labi."),
                ("2500 · 0,01 = 25",
                 "Divas vietas pa kreisi."),
                ("Kopā: pa labi trīs, pa kreisi divas - viena vieta pa labi",
                 "No 2,5 uz 25."),
            ],
            atbilde="25"),

    Ievadi("Lieto visus četrus", [
        {"jaut": "Cik ir 3,2 · 10 : 0,1?",
         "atb": ["320"], "padoms": "Divas vietas pa labi."},
        {"jaut": "Cik ir 480 : 100 · 0,1?",
         "atb": ["0,48", "0.48"], "padoms": "Trīs vietas pa kreisi."},
        {"jaut": "Cik ir 0,05 : 0,01 · 10?",
         "atb": ["50"], "padoms": "Trīs vietas pa labi."},
        {"jaut": "Cik ir 7,5 · 0,1 : 0,001?",
         "atb": ["750"], "padoms": "Divas vietas pa labi."},
        {"jaut": "Cik ir 1200 · 0,001 · 100?",
         "atb": ["120"], "padoms": "Viena vieta pa kreisi."},
        {"jaut": "Ar ko jāreizina 0,04, lai iegūtu 40?",
         "atb": ["1000"], "padoms": "Trīs vietas pa labi."},
    ], pamats=4,
        ievads="Saskaiti soļus pa labi un pa kreisi - un atņem."),

    Varianti("Kurš pāris ir vienāds?", [
        {"jaut": "Reizināt ar 100 ir tas pats, kas...",
         "opcijas": ["dalīt ar 0,01", "dalīt ar 100",
                     "reizināt ar 0,01", "atņemt 100"],
         "pareizi": 0,
         "padoms": "Abas ceļ komatu divas vietas pa labi."},
        {"jaut": "Dalīt ar 1000 ir tas pats, kas...",
         "opcijas": ["reizināt ar 0,001", "reizināt ar 1000",
                     "dalīt ar 0,001", "atņemt 1000"],
         "pareizi": 0,
         "padoms": "Abas ceļ komatu trīs vietas pa kreisi."},
        {"jaut": "Izteiksmē 8 · 10 : 0,1 komats kopumā pārceļas...",
         "opcijas": ["divas vietas pa labi", "divas pa kreisi",
                     "nemaz", "vienu pa labi"],
         "pareizi": 0,
         "padoms": "Abas darbības palielina."},
        {"jaut": "Izteiksmē 8 · 10 · 0,1 rezultāts ir...",
         "opcijas": ["8", "80", "0,8", "800"],
         "pareizi": 0,
         "padoms": "Viens solis pa labi un viens pa kreisi."},
    ], pamats=4),

    Pasaule("Cik tas ir citās mērvienībās?",
            Ievadi("", [
                {"jaut": "Fails ir 2500 KB. Cik MB tas ir, ja 1 MB = "
                         "1000 KB?",
                 "atb": ["2,5", "2.5"], "padoms": "2500 : 1000."},
                {"jaut": "Cik KB ir 0,4 MB?",
                 "atb": ["400"], "padoms": "0,4 · 1000."},
                {"jaut": "Video ir 1,2 GB. Cik MB tas ir, ja 1 GB = "
                         "1000 MB?",
                 "atb": ["1200"], "padoms": "1,2 · 1000."},
                {"jaut": "Cik GB ir 250 MB?",
                 "atb": ["0,25", "0.25"], "padoms": "250 : 1000."},
            ]),
            pavediens="dati",
            konteksts="Failu izmēri ir viena un tā paša skaitļa dažādi "
                      "pieraksti - starp tiem ir tikai komata solis.",
            kapec="Viens virziens un viens soļu skaits izskaidro visus "
                  "pārveidojumus."),

    Kopsavilkums([
        "Zinu, ka četri algoritmi ir divi pāri ar vienādu rezultātu.",
        "Vispirms nosaku virzienu, tikai tad soļu skaitu.",
        "Rēķinu izteiksmes, kurās ir vairākas šādas darbības.",
        "Lietoju tos mērvienību un failu izmēru pārveidošanā.",
    ]),

    Majas([
        "Izrēķini 6,4 · 1000 : 0,01 un pieraksti soļu skaitu.",
        "Uzraksti divas dažādas darbības, kas dod vienu un to pašu "
        "rezultātu.",
        "Pārvērt trīs failu izmērus no KB uz MB.",
    ]),
]
