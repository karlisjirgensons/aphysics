# -*- coding: utf-8 -*-
"""5. klase, 143. stunda: «Ko nozīmē procents?»

Jauns mikrotemats, bet nekāds jauns skaitlis: procents ir viena simtdaļa, un
viss pārējais izriet no tā. Tāpēc stunda sākas ar simta kvadrātu - simt
rūtiņām, no kurām katra ir viens procents. Kad tas ir redzēts, 25 % vairs
nav jāmācās, bet tikai jāsaskaita.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         kvadrats)

TEMA = "Ko nozīmē procents?"

MERKIS = ("Iemācīsimies skaidrot, ka procents ir viena simtdaļa, un modelēt "
          "procentus simta kvadrātā.")

SATURS = [
    Sakums("Simts rūtiņu, katra viens procents",
           zimejums=kvadrats(10, 10, 5, 5, virsraksts="Iekrāsotas 25 rūtiņas",
                             paraksts="25 %"),
           paraksts="Viena rūtiņa no simts ir viens procents.",
           fakti=["Simta kvadrātā ir 100 vienādas rūtiņas.",
                  "Katra rūtiņa ir {1|100} jeb 1 %.",
                  "25 iekrāsotas rūtiņas ir 25 %."]),

    Doma("Procents ir simtdaļa",
         "Viens procents ir viena simtdaļa no veselā; procentu zīme % nozīmē "
         "to pašu, ko saucējs 100.",
         soli=[
             "Iedomājies veselo kā 100 vienādas daļas.",
             "Viena daļa ir 1 %.",
             "Cik daļu paņem - tik procentu.",
             "Viss veselais ir 100 %.",
             "Puse veselā ir 50 %.",
         ],
         pieze="Procents nav mērvienība: 25 % no 400 € ir 100 €, bet 25 % no "
               "40 kg ir 10 kg. Tāpat kā daļa, procents vienmēr ir no kaut "
               "kā."),

    Slidnis("Cik rūtiņu ir iekrāsots?",
            [{"v": "10 %", "teksts": "10 rūtiņas no 100", "josla": 10,
              "zim": kvadrats(10, 10, 10, 1)},
             {"v": "25 %", "teksts": "25 rūtiņas no 100", "josla": 25,
              "zim": kvadrats(10, 10, 5, 5)},
             {"v": "50 %", "teksts": "50 rūtiņas no 100", "josla": 50,
              "zim": kvadrats(10, 10, 10, 5)},
             {"v": "100 %", "teksts": "viss kvadrāts", "josla": 100,
              "zim": kvadrats(10, 10, 10, 10)}],
            ievads="Spied soli pa solim: jo vairāk procentu, jo vairāk "
                   "rūtiņu."),

    Paraugs("Cik procentu ir iekrāsots?",
            uzd="Simta kvadrātā iekrāsotas 25 rūtiņas. Cik tas ir procentu?",
            soli=[
                ("Visā kvadrātā ir 100 rūtiņu",
                 "Veselais."),
                ("Katra rūtiņa ir 1 %",
                 "Viena simtdaļa."),
                ("Iekrāsotas 25 rūtiņas",
                 "Tātad 25 %."),
                ("25 % = {25|100} = {1|4}",
                 "Tā pati ceturtdaļa."),
            ],
            atbilde="Iekrāsoti 25 %"),

    Ievadi("Procenti un rūtiņas", [
        {"jaut": "Cik rūtiņu ir simta kvadrātā?",
         "atb": ["100"], "padoms": "10 · 10."},
        {"jaut": "Cik procentu ir viena rūtiņa?",
         "atb": ["1"], "padoms": "Viena simtdaļa."},
        {"jaut": "Iekrāsotas 25 rūtiņas. Cik tas ir procentu?",
         "atb": ["25"], "padoms": "Katra rūtiņa - viens procents."},
        {"jaut": "Iekrāsotas 50 rūtiņas. Cik tas ir procentu?",
         "atb": ["50"], "padoms": "Puse kvadrāta."},
        {"jaut": "Cik procentu ir viss kvadrāts?",
         "atb": ["100"], "padoms": "Visas rūtiņas."},
        {"jaut": "Iekrāsoti 40 %. Cik rūtiņu tas ir?",
         "atb": ["40"], "padoms": "Tikpat, cik procentu."},
        {"jaut": "Iekrāsoti 25 %. Cik rūtiņu palika balta?",
         "atb": ["75"], "padoms": "100 - 25."},
        {"jaut": "Cik procentu ir puse no veselā?",
         "atb": ["50"], "padoms": "100 : 2."},
    ], pamats=4,
        ievads="Simta kvadrātā procentu skaits ir rūtiņu skaits."),

    Zimejums("Puse simta kvadrāta",
             kvadrats(10, 10, 10, 5, virsraksts="50 rūtiņas no 100",
                      paraksts="50 %"),
             paskaidro="Piecas rindas no desmit ir puse kvadrāta - tātad "
                       "50 %. Tā pati puse, tikai citā pierakstā.",
             ievads="Puse veselā vienmēr ir 50 %."),

    Varianti("Ko nozīmē procents?", [
        {"jaut": "Viens procents ir...",
         "opcijas": ["Viena simtdaļa", "Viena desmitdaļa", "Viens vesels",
                     "Viena tūkstošdaļa"],
         "pareizi": 0,
         "padoms": "Saucējs ir 100."},
        {"jaut": "Cik procentu ir viss veselais?",
         "opcijas": ["100 %", "1 %", "50 %", "10 %"],
         "pareizi": 0,
         "padoms": "Visas simt daļas."},
        {"jaut": "25 % kā parastā daļa ir...",
         "opcijas": ["{1|4}", "{1|25}", "{25|10}", "{1|2}"],
         "pareizi": 0,
         "padoms": "{25|100}."},
        {"jaut": "Vai procents ir mērvienība?",
         "opcijas": ["Nav, tā ir daļa no kaut kā", "Ir, tas mēra daudzumu",
                     "Ir, tāpat kā metrs", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "25 % no 400 € un no 40 kg atšķiras."},
        {"jaut": "Iekrāsotas 75 rūtiņas no 100. Cik tas ir procentu?",
         "opcijas": ["75 %", "25 %", "7,5 %", "100 %"],
         "pareizi": 0,
         "padoms": "Rūtiņu skaits."},
        {"jaut": "Cik procentu ir ceturtdaļa?",
         "opcijas": ["25 %", "4 %", "40 %", "14 %"],
         "pareizi": 0,
         "padoms": "100 : 4."},
    ], pamats=4),

    Pasaule("Ko nozīmē atlaide 25 %?",
            Ievadi("", [
                {"jaut": "Atlaide ir 25 %. Cik simtdaļas no cenas tas ir?",
                 "atb": ["25"], "padoms": "Procents ir simtdaļa."},
                {"jaut": "Cik procentu no cenas būs jāmaksā?",
                 "atb": ["75"], "padoms": "100 - 25."},
                {"jaut": "Atlaide ir 50 %. Cik procentu būs jāmaksā?",
                 "atb": ["50"], "padoms": "100 - 50."},
                {"jaut": "Atlaide ir 10 %. Cik procentu būs jāmaksā?",
                 "atb": ["90"], "padoms": "100 - 10."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā atlaidi vienmēr raksta procentos, nevis "
                      "daļās.",
            kapec="Procents ir viena simtdaļa, tāpēc atlaidi var salīdzināt "
                  "jebkurai precei."),

    Kopsavilkums([
        "Skaidroju, ka procents ir viena simtdaļa.",
        "Modelēju procentus simta kvadrātā.",
        "Nosaku procentu skaitu pēc iekrāsoto rūtiņu skaita.",
        "Zinu, ka viss veselais ir 100 %.",
    ]),

    Majas([
        "Uzzīmē simta kvadrātu un iekrāso 30 %.",
        "Pieraksti, cik rūtiņu palika balta.",
        "Atrodi veikala reklāmā trīs dažādas atlaides procentos.",
    ]),
]
