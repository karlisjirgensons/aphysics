# -*- coding: utf-8 -*-
"""5. klase, 46. stunda: «Kā aprēķināt garu izteiksmi?»

Četras darbības vienā izteiksmē. Jaunas vielas te nav - ir tikai disciplīna:
pierakstīt katru soli un pēc tam pārbaudīt ar kalkulatoru. Pārbaude ar
kalkulatoru te ir atsevišķa prasme, jo kalkulators nezina, ko skolēns domāja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā aprēķināt garu izteiksmi?"

MERKIS = ("Mācīsimies aprēķināt izteiksmes vērtību ar līdz četrām darbībām "
          "un pārbaudīt to ar kalkulatoru.")

SATURS = [
    Sakums("Četras darbības vienā rindā",
           fakti=["(12 + 8) : 4 + 3² · 2 - ar ko sākt?",
                  "Ar iekavām, tad pakāpi, tad dalīšanu un reizināšanu.",
                  "Katru soli pieraksta - citādi pazūd, kur radās kļūda."]),

    Doma("Viens solis - viena rinda",
         "Garu izteiksmi rēķina pa soļiem, katru reizi pārrakstot visu "
         "izteiksmi no jauna.",
         soli=[
             "Pārraksti izteiksmi un pasvītro to, ko rēķināsi pirmo.",
             "Izrēķini vienu darbību un pārraksti izteiksmi ar rezultātu.",
             "Atkārto, kamēr palicis viens skaitlis.",
             "Pārbaudi ar kalkulatoru, ievadot izteiksmi ar iekavām.",
             "Ja atbildes atšķiras, meklē, kurā rindā tās izšķīrās.",
         ],
         pieze="Kalkulators nezina, ko tu domāji - tas rēķina to, kas "
               "ievadīts. Tāpēc, pārbaudot 3 · 2², jāievada tieši 3 · 2², "
               "nevis 3 · 2 un tad kvadrātā."),

    Paraugs("Rēķini pa soļiem",
            uzd="Aprēķini (12 + 8) : 4 + 3² · 2.",
            soli=[
                ("(12 + 8) : 4 + 3² · 2 = 20 : 4 + 3² · 2",
                 "Vispirms iekavas."),
                ("= 20 : 4 + 9 · 2",
                 "Tad pakāpe: 3² = 9."),
                ("= 5 + 18",
                 "Dalīšana un reizināšana."),
                ("= 23",
                 "Saskaitīšana pēdējā."),
            ],
            atbilde="(12 + 8) : 4 + 3² · 2 = 23"),

    Ievadi("Izrēķini pa soļiem", [
        {"jaut": "Cik ir (12 + 8) : 4 + 3² · 2?", "atb": ["23"],
         "padoms": "20 : 4 = 5, 9 · 2 = 18."},
        {"jaut": "Cik ir 100 − 2³ · 5?", "atb": ["60"],
         "padoms": "8 · 5 = 40."},
        {"jaut": "Cik ir (5 + 5)² : 4?", "atb": ["25"],
         "padoms": "100 : 4."},
        {"jaut": "Cik ir 6 · 5 − 4² + 2?", "atb": ["16"],
         "padoms": "30 − 16 + 2."},
        {"jaut": "Cik ir 2³ + 4 · (10 − 7)?", "atb": ["20"],
         "padoms": "8 + 4 · 3."},
        {"jaut": "Cik ir 144 : (2 · 6) + 3²?", "atb": ["21"],
         "padoms": "144 : 12 = 12, 12 + 9."},
        {"jaut": "Cik ir (7 − 3)² · 2 − 10?", "atb": ["22"],
         "padoms": "16 · 2 = 32."},
        {"jaut": "Cik ir 50 : 5² + 8?", "atb": ["10"],
         "padoms": "50 : 25 = 2."},
    ], pamats=4,
        ievads="Pieraksti katru soli - tā kļūdu var atrast."),

    Varianti("Kur kļūda?", [
        {"jaut": "Skolēns rēķināja 100 − 2³ · 5 un sanāca 460. Kur kļūda?",
         "opcijas": ["Vispirms atņēma, tad reizināja",
                     "Nepareizi izrēķināja 2³",
                     "Aizmirsa iekavas",
                     "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "(100 − 8) · 5 = 460, bet tā nav dotā izteiksme."},
        {"jaut": "Kāpēc katru soli pieraksta atsevišķā rindā?",
         "opcijas": ["Lai varētu atrast, kurā solī radās kļūda",
                     "Lai darbs izskatītos garāks",
                     "Tā prasa kalkulators",
                     "Lai nebūtu jāizmanto iekavas"],
         "pareizi": 0,
         "padoms": "Kļūdu meklē pa rindām."},
        {"jaut": "Kalkulatorā ievadīja 3 · 2 un tad kvadrātā. Ko tas "
                 "izrēķināja?",
         "opcijas": ["(3 · 2)² = 36", "3 · 2² = 12", "3² · 2 = 18",
                     "3 · 2 = 6"],
         "pareizi": 0,
         "padoms": "Kalkulators kāpināja jau iegūto rezultātu."},
        {"jaut": "Ko darīt, ja savs rezultāts un kalkulatora atšķiras?",
         "opcijas": ["Meklēt, kurā solī tie izšķīrās",
                     "Ticēt kalkulatoram",
                     "Ticēt sev",
                     "Rēķināt vēlreiz no gala"],
         "pareizi": 0,
         "padoms": "Soļi tāpēc arī ir pierakstīti."},
    ], pamats=4),

    Pasaule("Cik vietas paliek diskā?",
            Ievadi("", [
                {"jaut": "Diskā 100 GB, aizņemti 2³ · 5 GB. Cik brīvu GB?",
                 "atb": ["60"], "padoms": "8 · 5 = 40."},
                {"jaut": "Ir 12 un vēl 8 faili, tos sadala 4 mapēs. Cik failu "
                         "mapē?",
                 "atb": ["5"], "padoms": "(12 + 8) : 4."},
                {"jaut": "Katra no 3² ikonām aizņem 2 KB. Cik KB kopā?",
                 "atb": ["18"], "padoms": "9 · 2."},
                {"jaut": "Cik KB kopā aizņem abi: 5 failu mape (pa 1 KB) un "
                         "šīs ikonas?",
                 "atb": ["23"], "padoms": "5 + 18."},
            ]),
            pavediens="dati",
            konteksts="Vietas rēķins diskā ir gara izteiksme: kaut kas "
                      "aizņemts, kaut kas dzēsts, kaut kas reizināts.",
            kapec="Pierakstīti soļi ļauj rezultātu pārbaudīt, nevis "
                  "tam akli uzticēties."),

    Kopsavilkums([
        "Aprēķinu izteiksmi ar līdz četrām darbībām.",
        "Pierakstu katru soli atsevišķā rindā.",
        "Pārbaudu rezultātu ar kalkulatoru, ievadot izteiksmi pareizi.",
        "Atrodu, kurā solī radusies kļūda.",
    ]),

    Majas([
        "Izrēķini (20 − 5) : 3 + 2³ · 2 pa soļiem.",
        "Pārbaudi ar kalkulatoru un salīdzini.",
        "Uzraksti izteiksmi ar četrām darbībām, kuras vērtība ir tieši 100.",
    ]),
]
