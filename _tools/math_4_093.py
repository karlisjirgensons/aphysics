# -*- coding: utf-8 -*-
"""4. klase, 93. stunda: «Kā izlasīt un uzrakstīt daļu?»

4.5. temata sākums. Daļu {3|8} lasa «trīs astotdaļas»: saucējs pasaka, cik
vienādās daļās sadalīts veselais, skaitītājs - cik tādu daļu ņemtas.
Skolēns raksta daļu pēc dzirdētā un pēc nosacījumiem - no šī pieraksta
atkarīgs viss tālākais temats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā izlasīt un uzrakstīt daļu?"

MERKIS = ("Lasīsim un pierakstīsim daļas pēc dzirdētā un uzrakstīsim daļu "
          "pēc nosacījumiem.")

SATURS = [
    Sakums("Cik picas palika?",
           zimejums=dala(8, 3, "3/8", "pica 8 gabalos, 3 palika"),
           paraksts="Trīs astotdaļas.",
           fakti=["Saucējs (apakšā) - cik daļās sadalīts veselais.",
                  "Skaitītājs (augšā) - cik daļu paņemts."]),

    Doma("Saucējs dala, skaitītājs skaita",
         "Daļā {a|b} saucējs b pasaka, cik vienādās daļās sadalīts veselais, "
         "bet skaitītājs a - cik tādu daļu ņemts.",
         soli=[
             "Saucēju lasa kā daļas vārdu: 2 - otrdaļa (puse), 3 - trešdaļa, "
             "4 - ceturtdaļa, 8 - astotdaļa.",
             "Skaitītāju lasa kā skaitu: trīs astotdaļas.",
             "Rakstot daļu, svītra atdala skaitītāju no saucēja.",
             "Saucējs nekad nevar būt 0.",
         ],
         pieze="{1|2} ir puse, {1|4} - ceturtdaļa, {3|4} - trīs "
               "ceturtdaļas."),

    Zimejums("Daļu vārdi",
             restis([["saucējs", "daļa", "piemērs"],
                     ["2", "puse", "1/2"],
                     ["3", "trešdaļa", "2/3"],
                     ["5", "piektdaļa", "4/5"],
                     ["10", "desmitdaļa", "7/10"]],
                    "kā lasa"),
             paskaidro="Daļas vārds nāk no saucēja.",
             ievads="Tabula palīdz izlasīt jebkuru daļu."),

    Paraugs("Uzraksti pēc dzirdētā",
            uzd="Uzraksti ar cipariem: «piecas sestdaļas».",
            soli=[
                ("sestdaļas → saucējs 6", None),
                ("piecas → skaitītājs 5", None),
                ("{5|6}", None),
            ],
            atbilde="{5|6}"),

    Ievadi("Raksti daļu", [
        {"jaut": "Trīs ceturtdaļas", "atb": ["3/4"], "vieta": "piem., 1/2",
         "padoms": "Skaitītājs 3, saucējs 4."},
        {"jaut": "Divas piektdaļas", "atb": ["2/5"], "vieta": "piem., 1/2",
         "padoms": "Skaitītājs 2, saucējs 5."},
        {"jaut": "Septiņas desmitdaļas", "atb": ["7/10"],
         "vieta": "piem., 1/2", "padoms": "Saucējs 10."},
        {"jaut": "Daļa ar saucēju 9 un skaitītāju 4", "atb": ["4/9"],
         "vieta": "piem., 1/2", "padoms": "Skaitītājs augšā."},
        {"jaut": "Cik daļās sadalīts veselais daļā {5|12}?", "atb": ["12"],
         "padoms": "Saucējs."},
        {"jaut": "Cik daļu ņemts daļā {5|12}?", "atb": ["5"],
         "padoms": "Skaitītājs."},
    ], pamats=4,
        ievads="Daļu raksti ar slīpsvītru: 3/4."),

    Varianti("Kā lasa?", [
        {"jaut": "Kā izlasa {2|3}?",
         "opcijas": ["divas trešdaļas", "trīs otrdaļas", "divi trīs",
                     "trīs divi"], "pareizi": 0,
         "padoms": "Saucējs 3 - trešdaļas."},
        {"jaut": "Kurš ir skaitītājs daļā {7|8}?",
         "opcijas": ["7", "8", "15", "1"], "pareizi": 0,
         "padoms": "Augšējais."},
        {"jaut": "Kura daļa ir «viena desmitdaļa»?",
         "opcijas": ["{1|10}", "{10|1}", "{1|100}", "{10|10}"],
         "pareizi": 0, "padoms": "Saucējs 10."},
        {"jaut": "Kāda daļa iekrāsota, ja josla 5 daļās un iekrāsotas 2?",
         "opcijas": ["{2|5}", "{5|2}", "{3|5}", "{2|3}"], "pareizi": 0,
         "padoms": "Iekrāsotās virs, visas zem."},
    ], pamats=4),

    Pasaule("Receptes daļas",
            Ievadi("", [
                {"jaut": "Receptē: «trīs ceturtdaļas glāzes cukura». Raksti "
                         "daļu.",
                 "atb": ["3/4"], "vieta": "piem., 1/2",
                 "padoms": "3 augšā, 4 apakšā."},
                {"jaut": "«Puse glāzes piena». Raksti daļu.",
                 "atb": ["1/2"], "vieta": "piem., 1/3",
                 "padoms": "Viena otrdaļa."},
                {"jaut": "«Divas trešdaļas paciņas sviesta». Raksti daļu.",
                 "atb": ["2/3"], "vieta": "piem., 1/2",
                 "padoms": "Saucējs 3."},
                {"jaut": "Kūku sagrieza 12 gabalos, apēda 5. Kāda daļa "
                         "apēsta?",
                 "atb": ["5/12"], "vieta": "piem., 1/2",
                 "padoms": "5 no 12."},
            ]),
            pavediens="virtuve",
            konteksts="Receptēs daļas ir visur - glāzes, karotes un "
                      "paciņas.",
            kapec="Kas neizlasa daļu, tam kūka neizdosies."),

    Kopsavilkums([
        "Lasu daļas: trīs astotdaļas, divas piektdaļas.",
        "Rakstu daļu pēc dzirdētā.",
        "Zinu, ka saucējs dala, bet skaitītājs skaita.",
    ]),

    Majas([
        "Atrodi receptē 3 daļas un uzraksti tās ar cipariem.",
        "Sagriez ābolu 4 daļās, apēd 1 - kāda daļa palika?",
        "Nodiktē mājiniekam 3 daļas un pārbaudi pierakstu.",
    ]),
]
