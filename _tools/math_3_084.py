# -*- coding: utf-8 -*-
"""3. klase, 84. stunda: «Kāda daļa ir iekrāsota un kāda - ne?»

77. stundā to sauca vārdiem, tagad raksta ar daļsvītru. Galvenais atklājums:
abas daļas kopā vienmēr dod veselo, un tās var pierakstīt kā summu ar vienādu
saucēju - no tā 86. stundā izaugs daļu saskaitīšana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kāda daļa ir iekrāsota un kāda - ne?"

MERKIS = ("Pierakstīsim daļskaitli figūras iekrāsotajai un neiekrāsotajai "
          "daļai.")

SATURS = [
    Sakums("Cik pietrūkst līdz veselajam?",
           zimejums=dala(7, 4, "4/7 iekrāsotas", "septiņas vienādas daļas"),
           paraksts="Iekrāsotas {4|7}, neiekrāsotas {3|7}.",
           fakti=["Abām daļām saucējs ir viens un tas pats.",
                  "Iekrāsotās un neiekrāsotās daļas kopā dod veselo."]),

    Doma("Abas daļas kopā dod veselo",
         "Ja iekrāsotas {4|7}, tad neiekrāsotas ir {3|7}, jo "
         "{4|7} + {3|7} = {7|7} = 1.",
         soli=[
             "Pieraksti iekrāsoto daļu.",
             "Atņem skaitītāju no saucēja.",
             "Pieraksti neiekrāsoto daļu ar to pašu saucēju.",
             "Pārbaudi: abu skaitītāju summai jābūt vienādai ar saucēju.",
         ],
         pieze="Daļa, kurā skaitītājs un saucējs ir vienādi, ir viens vesels: "
               "{7|7} = 1, {5|5} = 1, {12|12} = 1."),

    Paraugs("Kāda daļa nav iekrāsota?",
            uzd="Figūrā iekrāsotas {4|7}. Kāda daļa nav iekrāsota?",
            soli=[
                ("Saucējs ir 7",
                 "Veselais sadalīts septiņās daļās."),
                ("7 − 4 = 3",
                 "Tik daļu nav iekrāsotas."),
                ("{3|7}",
                 "Pārbaude: 4 + 3 = 7, tātad kopā sanāk viss veselais."),
            ],
            atbilde="{3|7}"),

    Ievadi("Cik pietrūkst līdz veselajam?", [
        {"jaut": "Iekrāsotas {4|7}. Kāds ir neiekrāsotās daļas skaitītājs?",
         "atb": ["3"], "padoms": "7 − 4."},
        {"jaut": "Iekrāsotas {5|8}. Kāds ir neiekrāsotās daļas skaitītājs?",
         "atb": ["3"], "padoms": "8 − 5."},
        {"jaut": "Iekrāsotas {2|9}. Kāds ir neiekrāsotās daļas skaitītājs?",
         "atb": ["7"], "padoms": "9 − 2."},
        {"jaut": "Iekrāsotas {6|10}. Kāds ir neiekrāsotās daļas skaitītājs?",
         "atb": ["4"], "padoms": "10 − 6."},
        {"jaut": "Iekrāsotas {3|3}. Kāds ir neiekrāsotās daļas skaitītājs?",
         "atb": ["0"], "padoms": "Viss ir iekrāsots."},
        {"jaut": "Iekrāsotas {1|6}. Kāds ir neiekrāsotās daļas skaitītājs?",
         "atb": ["5"], "padoms": "6 − 1."},
    ], pamats=4),

    Zimejums("Viens vesels",
             dala(5, 5, "5/5 = 1", "visas daļas iekrāsotas"),
             paskaidro="Ja skaitītājs un saucējs ir vienādi, daļa ir viens "
                       "vesels.",
             ievads="Tā izskatās {5|5}."),

    Varianti("Cik ir kopā?", [
        {"jaut": "Iekrāsotas {3|8}. Kāda daļa nav iekrāsota?",
         "opcijas": ["{5|8}", "{3|8}", "{8|5}", "{5|3}"],
         "pareizi": 0, "padoms": "8 − 3."},
        {"jaut": "Kurai daļai vērtība ir 1?",
         "opcijas": ["{6|6}", "{1|6}", "{6|1}", "{5|6}"],
         "pareizi": 0, "padoms": "Skaitītājs un saucējs vienādi."},
        {"jaut": "Iekrāsotas {9|10}. Cik daļu nav iekrāsotas?",
         "opcijas": ["1", "9", "10", "19"],
         "pareizi": 0, "padoms": "10 − 9."},
        {"jaut": "Kas notiek ar saucēju, meklējot neiekrāsoto daļu?",
         "opcijas": ["Tas paliek tas pats", "Tas kļūst lielāks",
                     "Tas kļūst mazāks", "Tas pazūd"],
         "pareizi": 0, "padoms": "Veselais taču netiek pārdalīts."},
    ], pamats=4),

    Pasaule("Cik treniņu ir izlaists?",
            Ievadi("", [
                {"jaut": "Mēnesī bija 12 treniņi, apmeklēti 9. Cik treniņu "
                         "izlaists?",
                 "atb": ["3"], "padoms": "12 − 9."},
                {"jaut": "Cik treniņu ir {3|4} no 12?",
                 "atb": ["9"], "padoms": "12 : 4 = 3; 3 · 3."},
                {"jaut": "Nākamajā mēnesī bija 10 treniņi, izlaists 1. Cik "
                         "apmeklēts?",
                 "atb": ["9"], "padoms": "10 − 1."},
                {"jaut": "Cik treniņu bija abos mēnešos kopā?",
                 "atb": ["22"], "padoms": "12 + 10."},
            ]),
            pavediens="sports",
            konteksts="Treneris pieraksta apmeklējumu kā daļu - un abas "
                      "daļas, apmeklētā un izlaistā, kopā dod visus treniņus.",
            kapec="Pēc daļas uzreiz redz, cik regulāri sportists trenējas."),

    Kopsavilkums([
        "Pierakstu iekrāsoto un neiekrāsoto daļu ar daļsvītru.",
        "Zinu, ka abām daļām saucējs ir viens un tas pats.",
        "Zinu, ka abas daļas kopā dod veselo.",
        "Zinu, ka {n|n} = 1.",
    ]),

    Majas([
        "Uzzīmē joslu no 9 daļām, iekrāso 5 un pieraksti abas daļas.",
        "Uzraksti trīs daļas, kuru vērtība ir 1.",
        "Atrodi mājās kaut ko, kur daļa ir izlietota, un pieraksti abas "
        "daļas.",
    ]),
]
