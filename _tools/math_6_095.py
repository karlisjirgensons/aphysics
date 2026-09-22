# -*- coding: utf-8 -*-
"""6. klase, 95. stunda: «Kā izlasīt sarežģītu tekstu?»

Autentisks teksts nav uzdevums: tajā ir lieki skaitļi, daļas un procenti
vienā rindkopā, un dažreiz arī tas, kas nav pateikts. Prasme no tā izvilkt
vajadzīgo ir tieši tā, ko prasa eksāmena teksta uzdevumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kā izlasīt sarežģītu tekstu?"

MERKIS = ("Nolasīsim informāciju no autentiska teksta ar procentiem un "
          "daļām un raksturosim tās lietojumu.")

SATURS = [
    Sakums("Tekstā ne viss ir vajadzīgs",
           fakti=["Pirmais solis - atrast jautājumu, ne skaitļus.",
                  "Otrais - pasvītrot tikai tos skaitļus, kas der.",
                  "Trešais - pārbaudīt, no kā ņemta katra daļa."]),

    Doma("Vispirms jautājums, tad skaitļi",
         "Sarežģītu tekstu lasa no beigām: vispirms saprot jautājumu un "
         "tikai tad meklē tekstā skaitļus, kas tam der.",
         soli=[
             "Izlasi jautājumu un pieraksti, ko meklē.",
             "Pasvītro tekstā skaitļus, kas attiecas uz šo jautājumu.",
             "Katram procentam pieraksti, no kā tas ņemts.",
             "Atzīmē skaitļus, kas uzdevumam nav vajadzīgi.",
             "Sastādi risinājuma plānu un tikai tad rēķini.",
         ],
         pieze="Biežākā slazds: divi procenti tekstā ir ņemti no dažādiem "
               "kopumiem. «40 % skolēnu sporto, no tiem 25 % spēlē futbolu» "
               "- otrais procents ir no pirmās grupas, ne no visas skolas."),

    Paraugs("Izlasi rakstu par skolu",
            uzd="«Skolā mācās 400 skolēni. 40 % no viņiem apmeklē pulciņus, "
                "no tiem ceturtdaļa - sporta pulciņus. Skolā ir 25 "
                "skolotāji.» Cik skolēnu apmeklē sporta pulciņus?",
            soli=[
                ("Jautājums: cik skolēnu sporta pulciņos",
                 "No beigām uz sākumu."),
                ("400 skolēnu, 40 % apmeklē pulciņus",
                 "40 · 4 = 160 skolēnu."),
                ("Ceturtdaļa *no tiem* - no 160, nevis no 400",
                 "Tā ir uzdevuma grūtākā vieta."),
                ("160 : 4 = 40",
                 "Sporta pulciņos."),
                ("25 skolotāji uzdevumam nav vajadzīgi",
                 "Liekais skaitlis."),
            ],
            atbilde="40 skolēni"),

    Ievadi("Izvelc vajadzīgo", [
        {"jaut": "Skolā 400 skolēnu, 40 % apmeklē pulciņus. Cik tas ir?",
         "atb": ["160"], "padoms": "40 · 4."},
        {"jaut": "No tiem ceturtdaļa sporta pulciņos. Cik skolēnu?",
         "atb": ["40"], "padoms": "160 : 4."},
        {"jaut": "Cik procenti no visas skolas tas ir?",
         "atb": ["10"], "padoms": "{40|400}."},
        {"jaut": "Klasē 25 skolēni, 60 % brauc ar autobusu, no tiem "
                 "trešdaļa - ar 5. maršrutu. Cik skolēnu?",
         "atb": ["5"], "padoms": "15 : 3."},
        {"jaut": "Veikalā 200 preces, 30 % ar atlaidi, no tām puse - "
                 "pārtika. Cik preču?",
         "atb": ["30"], "padoms": "60 : 2."},
        {"jaut": "Cik procenti no visām precēm tas ir?",
         "atb": ["15"], "padoms": "{30|200}."},
    ], pamats=4,
        ievads="Katram procentam pieraksti, no kā tas ņemts."),

    Varianti("No kā ņemts procents?", [
        {"jaut": "«40 % skolēnu sporto, no tiem 25 % spēlē futbolu.» 25 % ir "
                 "no...",
         "opcijas": ["sportotājiem", "visas skolas",
                     "futbolistiem", "skolotājiem"],
         "pareizi": 0,
         "padoms": "«No tiem» norāda uz iepriekšējo grupu."},
        {"jaut": "Skolā 400 skolēnu. Cik procenti no visas skolas spēlē "
                 "futbolu?",
         "opcijas": ["10", "25", "40", "65"],
         "pareizi": 0,
         "padoms": "40 no 400."},
        {"jaut": "Ko darīt ar skaitļiem, kas neattiecas uz jautājumu?",
         "opcijas": ["Atzīmēt kā lieku un nelietot",
                     "Iekļaut rēķinā", "Saskaitīt kopā",
                     "Atmest visu tekstu"],
         "pareizi": 0,
         "padoms": "Autentiskā tekstā liekais ir vienmēr."},
        {"jaut": "Ar ko sāk sarežģīta teksta lasīšanu?",
         "opcijas": ["Ar jautājumu", "Ar pirmo teikumu",
                     "Ar skaitļiem", "Ar atbildi"],
         "pareizi": 0,
         "padoms": "Jautājums pasaka, kas vajadzīgs."},
    ], pamats=4),

    Petijums("Izlasi īstu rakstu",
             vajag="ziņu raksts vai etiķete ar procentiem",
             soli=[
                 "Atrodi tekstu, kurā ir vismaz divi procenti.",
                 "Pieraksti katram procentam, no kā tas ņemts.",
                 "Izdomā vienu jautājumu, uz kuru tekstā ir atbilde.",
                 "Atrisini to un pieraksti, kuri skaitļi bija lieki.",
             ],
             secinajums="Autentiskā tekstā gandrīz vienmēr ir skaitļi, kas "
                        "uzdevumam nav vajadzīgi - to atpazīšana ir daļa no "
                        "risinājuma."),

    Pasaule("Ko pasaka ziņas?",
            Ievadi("", [
                {"jaut": "Pilsētā 20 000 iedzīvotāju, 15 % ir skolēni. Cik "
                         "tas ir?",
                 "atb": ["3000", "3 000"], "padoms": "15 · 200."},
                {"jaut": "No skolēniem 40 % mācās sākumskolā. Cik tas ir?",
                 "atb": ["1200", "1 200"], "padoms": "3000 · 0,4."},
                {"jaut": "Cik procenti no visiem iedzīvotājiem mācās "
                         "sākumskolā?",
                 "atb": ["6"], "padoms": "{1200|20000}."},
                {"jaut": "Cik skolēnu *nemācās* sākumskolā?",
                 "atb": ["1800", "1 800"], "padoms": "3000 − 1200."},
            ]),
            pavediens="skola",
            konteksts="Ziņās procentus raksta cits no cita, un tikai "
                      "uzmanīga lasīšana pasaka, no kā katrs ir ņemts.",
            kapec="Otrais procents gandrīz nekad nav no sākotnējā kopuma."),

    Kopsavilkums([
        "Sāku lasīšanu ar jautājumu, ne ar skaitļiem.",
        "Pierakstu katram procentam, no kā tas ņemts.",
        "Atpazīstu liekos skaitļus tekstā.",
        "Sastādu risinājuma plānu pirms rēķināšanas.",
    ]),

    Majas([
        "Atrodi ziņu ar diviem procentiem un pieraksti, no kā katrs ņemts.",
        "Izdomā jautājumu par šo tekstu un atrisini to.",
        "Pieraksti, kuri skaitļi tekstā bija lieki.",
    ]),
]
