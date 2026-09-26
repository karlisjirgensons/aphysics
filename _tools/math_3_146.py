# -*- coding: utf-8 -*-
"""3. klase, 146. stunda: «Cik pietrūkst līdz 1000?»

Papildinājums līdz apaļam skaitlim ir atņemšana, kuru gandrīz vienmēr var
izdarīt galvā: līdz pilnam desmitam, tad līdz pilnam simtam, tad līdz
tūkstotim. Tas pats paņēmiens vēlāk noder atlikuma skaitīšanai kasē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         taisne)

TEMA = "Cik pietrūkst līdz 1000?"

MERKIS = ("Aprēķināsim, cik pietrūkst līdz pilnam simtam vai tūkstotim.")

SATURS = [
    Sakums("Cik pietrūkst līdz tūkstotim?",
           zimejums=taisne(0, 1000, 200, [(640, "640")],
                           bultas=[(640, 1000, "360")]),
           paraksts="No 640 līdz 1000 ir 360.",
           fakti=["Papildinājumu līdz apaļam skaitlim var rēķināt galvā.",
                  "Vispirms līdz desmitam, tad līdz simtam, tad līdz "
                  "tūkstotim."]),

    Doma("Ej pa soļiem līdz apaļam skaitlim",
         "Vispirms papildini līdz pilnam desmitam, tad līdz simtam, tad līdz "
         "tūkstotim - un saskaiti soļus.",
         soli=[
             "Cik pietrūkst līdz pilnam desmitam?",
             "Cik no turienes līdz pilnam simtam?",
             "Cik no turienes līdz 1000?",
             "Saskaiti visus soļus kopā.",
         ],
         pieze="Ja skaitlis jau beidzas ar nulli, pirmais solis nav "
               "vajadzīgs: no 640 uzreiz ej līdz 700."),

    Slidnis("Trīs soļi līdz tūkstotim",
            soli=[
                {"v": "647 + 3 = 650", "teksts": "Līdz pilnam desmitam.",
                 "josla": 65},
                {"v": "650 + 50 = 700", "teksts": "Līdz pilnam simtam.",
                 "josla": 70},
                {"v": "700 + 300 = 1000", "teksts": "Līdz tūkstotim.",
                 "josla": 100},
            ],
            ievads="Kopā 3 + 50 + 300 = 353."),

    Paraugs("Cik pietrūkst līdz 1000?",
            uzd="Cik pietrūkst skaitlim 647 līdz 1000?",
            soli=[
                ("647 + 3 = 650",
                 "Līdz pilnam desmitam."),
                ("650 + 50 = 700",
                 "Līdz pilnam simtam."),
                ("700 + 300 = 1000",
                 "Līdz tūkstotim; kopā 3 + 50 + 300 = 353."),
            ],
            atbilde="353"),

    Ievadi("Cik pietrūkst?", [
        {"jaut": "Cik pietrūkst 640 līdz 1000?", "atb": ["360"],
         "padoms": "60 + 300."},
        {"jaut": "Cik pietrūkst 647 līdz 1000?", "atb": ["353"],
         "padoms": "3 + 50 + 300."},
        {"jaut": "Cik pietrūkst 380 līdz 400?", "atb": ["20"],
         "padoms": "400 − 380."},
        {"jaut": "Cik pietrūkst 725 līdz 800?", "atb": ["75"],
         "padoms": "5 + 70."},
        {"jaut": "Cik pietrūkst 199 līdz 1000?", "atb": ["801"],
         "padoms": "1 + 800."},
        {"jaut": "Cik pietrūkst 555 līdz 1000?", "atb": ["445"],
         "padoms": "5 + 40 + 400."},
    ], pamats=4),

    Zimejums("Lēciens līdz simtam",
             taisne(0, 800, 200, [(725, "725")],
                    bultas=[(725, 800, "75")]),
             paskaidro="Līdz pilnam simtam vienmēr ir mazāk par 100 - tāpēc "
                       "šo soli var izdarīt galvā.",
             ievads="No 725 līdz 800."),

    Varianti("Cik trūkst?", [
        {"jaut": "Cik pietrūkst 450 līdz 1000?",
         "opcijas": ["550", "650", "450", "500"],
         "pareizi": 0, "padoms": "50 + 500."},
        {"jaut": "Cik pietrūkst 890 līdz 900?",
         "opcijas": ["10", "110", "100", "20"],
         "pareizi": 0, "padoms": "900 − 890."},
        {"jaut": "Cik pietrūkst 236 līdz 300?",
         "opcijas": ["64", "74", "54", "164"],
         "pareizi": 0, "padoms": "4 + 60."},
        {"jaut": "Ar ko sākt, papildinot līdz 1000?",
         "opcijas": ["Ar pilnu desmitu", "Ar simtiem", "Ar tūkstoti",
                     "Vienalga"],
         "pareizi": 0, "padoms": "Mazākais solis pirmais."},
    ], pamats=4),

    Pasaule("Cik metru līdz rekordam?",
            Ievadi("", [
                {"jaut": "Skrējējs noskrējis 640 m no 1000 m. Cik atlicis?",
                 "atb": ["360"], "padoms": "60 + 300."},
                {"jaut": "Otrs noskrējis 725 m. Cik viņam atlicis?",
                 "atb": ["275"], "padoms": "75 + 200."},
                {"jaut": "Par cik metriem otrais ir priekšā?",
                 "atb": ["85"], "padoms": "725 − 640."},
                {"jaut": "Cik metru abi noskrējuši kopā?", "atb": ["1365"],
                 "padoms": "640 + 725."},
            ]),
            pavediens="sports",
            konteksts="Sacensībās vienmēr rāda atlikušo distanci - tas ir "
                      "papildinājums līdz apaļam skaitlim.",
            kapec="Pa soļiem rēķinot, atlikumu var pateikt bez papīra."),

    Kopsavilkums([
        "Aprēķinu, cik pietrūkst līdz pilnam simtam vai tūkstotim.",
        "Rēķinu pa soļiem: desmits, simts, tūkstotis.",
        "Saskaitu soļus kopā.",
        "Pārbaudu atbildi ar saskaitīšanu.",
    ]),

    Majas([
        "Izrēķini, cik pietrūkst līdz 1000 skaitļiem 320, 478 un 905.",
        "Pārbaudi katru ar saskaitīšanu.",
        "Izrēķini, cik centu pietrūkst līdz 1 eiro no 37 centiem.",
    ]),
]
