# -*- coding: utf-8 -*-
"""3. klase, 171. stunda: «Ko es zinu par daļām?»

Daļas bija gada jaunākā tēma, tāpēc noslēgumā tās atkārto atsevišķi: daļas
jēga modelī, salīdzināšana un daļa no skaita. Tieši no šī pamata 4. klasē
sāksies daļu saskaitīšana ar dažādiem saucējiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Ko es zinu par daļām?"

MERKIS = ("Atkārtosim daļas jēgu: parādīsim daļu modelī, salīdzināsim daļas "
          "un noteiksim daļu no skaita.")

SATURS = [
    Sakums("Trīs lietas, kas par daļām jāzina droši",
           zimejums=dala(4, 3, "3/4", "četras vienādas daļas"),
           paraksts="Saucējs sadala, skaitītājs skaita.",
           fakti=["Daļa ir vienāda daļa no veselā.",
                  "Lielāks saucējs dod mazāku daļu.",
                  "Daļu no skaita atrod ar dalīšanu un reizināšanu."]),

    Doma("Trīs prasmes, kas noder 4. klasē",
         "Parādīt daļu modelī, salīdzināt divas daļas un atrast daļu no "
         "skaita.",
         soli=[
             "Parādi daļu joslā vai riņķī.",
             "Salīdzini daļas: vienādi saucēji - skaties skaitītājus.",
             "Dažādi saucēji - atceries, ka lielāks saucējs dod mazāku daļu.",
             "Daļu no skaita: dali ar saucēju, reizini ar skaitītāju.",
         ],
         pieze="Un vienmēr atceries jautājumu «no kā?»: daļa bez veselā "
               "neko nenozīmē."),

    Paraugs("Cik ir {3|4} no 60?",
            uzd="Aprēķini {3|4} no 60.",
            soli=[
                ("60 : 4 = 15",
                 "Viena ceturtdaļa."),
                ("3 · 15 = 45",
                 "Trīs ceturtdaļas."),
                ("Atbilde ir 45",
                 "Pārbaude: 45 ir mazāk par 60."),
            ],
            atbilde="45"),

    Ievadi("Daļu atkārtojums", [
        {"jaut": "Cik ir {1|2} no 60?", "atb": ["30"], "padoms": "60 : 2."},
        {"jaut": "Cik ir {3|4} no 60?", "atb": ["45"], "padoms": "3 · 15."},
        {"jaut": "Cik ir {2|5} no 100?", "atb": ["40"], "padoms": "2 · 20."},
        {"jaut": "Kura daļa ir lielāka: {1|3} vai {1|5}? Ieraksti saucēju.",
         "atb": ["3"], "padoms": "Mazāks saucējs - lielāka daļa."},
        {"jaut": "Cik astotdaļu pietrūkst daļai {5|8} līdz veselajam?",
         "atb": ["3"], "padoms": "8 − 5."},
        {"jaut": "Pieraksti {7|10} ar komatu.", "atb": ["0,7", "0.7"],
         "padoms": "Septiņas desmitdaļas."},
        {"jaut": "Cik centu ir 0,45 eiro?", "atb": ["45"],
         "padoms": "Aiz komata ir centi."},
        {"jaut": "Cik minūšu ir {1|4} stundas?", "atb": ["15"],
         "padoms": "60 : 4."},
    ], pamats=6),

    Zimejums("Puse trijos pierakstos",
             dala(10, 5, "5/10 = 1/2 = 0,5", "desmit vienādas daļas"),
             paskaidro="Viena un tā pati puse - parastā daļa, cita parastā "
                       "daļa un decimāldaļa.",
             ievads="Trīs pieraksti, viens skaitlis."),

    Varianti("Ko par daļām zini droši?", [
        {"jaut": "Kura daļa ir lielāka?",
         "opcijas": ["{1|3}", "{1|4}", "{1|8}", "{1|10}"],
         "pareizi": 0, "padoms": "Mazākais saucējs."},
        {"jaut": "Kura daļa ir vienāda ar 1?",
         "opcijas": ["{6|6}", "{1|6}", "{6|1}", "{5|6}"],
         "pareizi": 0, "padoms": "Skaitītājs vienāds ar saucēju."},
        {"jaut": "Cik ir {1|4} no 80?",
         "opcijas": ["20", "40", "4", "60"],
         "pareizi": 0, "padoms": "80 : 4."},
        {"jaut": "Kāda daļa ir vienāda ar 0,5?",
         "opcijas": ["{1|2}", "{1|5}", "{5|100}", "{2|10}"],
         "pareizi": 0, "padoms": "Piecas desmitdaļas."},
    ], pamats=4),

    Pasaule("Cik ir vasaras brīvlaika?",
            Ievadi("", [
                {"jaut": "Vasaras brīvlaiks ir 90 dienas. Cik dienu ir "
                         "{1|3}?",
                 "atb": ["30"], "padoms": "90 : 3."},
                {"jaut": "Cik dienu ir {2|3}?", "atb": ["60"],
                 "padoms": "2 · 30."},
                {"jaut": "Cik dienu ir {1|2} no brīvlaika?", "atb": ["45"],
                 "padoms": "90 : 2."},
                {"jaut": "Cik nedēļu ir 90 dienās? Ieraksti pilnu nedēļu "
                         "skaitu.",
                 "atb": ["12"], "padoms": "12 · 7 = 84."},
            ]),
            pavediens="celojums",
            konteksts="Vasaras brīvlaiku plāno tieši daļās: trešdaļa "
                      "nometnē, trešdaļa laukos, trešdaļa mājās.",
            kapec="Daļa uzreiz pasaka, cik daudz laika kam atvēlēts."),

    Kopsavilkums([
        "Parādu daļu modelī un pierakstu to ar daļsvītru.",
        "Salīdzinu daļas ar vienādiem un dažādiem saucējiem.",
        "Aprēķinu daļu no skaita.",
        "Pārvēršu daļas un decimāldaļas.",
    ]),

    Majas([
        "Izrēķini {1|2}, {1|4} un {3|4} no savu vasaras brīvdienu skaita.",
        "Uzzīmē modeli vienai no šīm daļām.",
        "Atrodi mājās trīs vietas, kur ir daļas vai decimāldaļas.",
    ]),
]
