# -*- coding: utf-8 -*-
"""4. klase, 101. stunda: «Kura daļa lielāka, ja skaitītāji vienādi?»

Vispārinājums no pamatdaļām: ja skaitītāji vienādi, ņemts vienāds gabalu
skaits, un lielāka ir daļa ar lielākiem gabaliem - ar mazāku saucēju.
{3|5} > {3|8}. Skolēns to pamato ar iepriekšējās stundas spriedumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, dala)

TEMA = "Kura daļa lielāka, ja skaitītāji vienādi?"

MERKIS = ("Salīdzināsim daļas ar vienādiem skaitītājiem un pamatosim "
          "spriedumu.")

SATURS = [
    Sakums("3 lieli gabali vai 3 mazi?",
           zimejums=dala(5, 3, "3/5") + dala(8, 3, "3/8"),
           paraksts="Abiem 3 gabali - bet dažāda lieluma.",
           fakti=["Piektdaļas ir lielākas nekā astotdaļas.",
                  "Tāpēc {3|5} > {3|8}."]),

    Doma("Vienādi skaitītāji - salīdzini gabalu lielumu",
         "Ja skaitītāji vienādi, lielāka ir daļa ar mazāku saucēju, jo tās "
         "gabali lielāki.",
         soli=[
             "Pārbaudi: skaitītāji vienādi?",
             "Salīdzini saucējus.",
             "Mazāks saucējs - lielāki gabali.",
             "Spriedums: «{3|5} > {3|8}, jo piektdaļas lielākas nekā "
             "astotdaļas».",
         ],
         pieze="Tas pats, kas pamatdaļām, tikai gabalu ir vairāk nekā viens."),

    Paraugs("{4|7} vai {4|9}?",
            uzd="Salīdzini {4|7} un {4|9}.",
            soli=[
                ("4 = 4", "Skaitītāji vienādi."),
                ("7 < 9", "Septītdaļas lielākas."),
                ("{4|7} > {4|9}", None),
            ],
            atbilde="{4|7} > {4|9}"),

    Varianti("Liec zīmi", [
        {"jaut": "{2|3} ☐ {2|5}", "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "Trešdaļas lielākas."},
        {"jaut": "{5|12} ☐ {5|6}", "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "Divpadsmitdaļas mazākas."},
        {"jaut": "{7|10} ☐ {7|10}", "opcijas": ["=", "<", ">"],
         "pareizi": 0, "padoms": "Tās pašas."},
        {"jaut": "Kura lielākā: {3|4}, {3|10}, {3|7}, {3|5}?",
         "opcijas": ["{3|4}", "{3|10}", "{3|7}", "{3|5}"], "pareizi": 0,
         "padoms": "Mazākais saucējs."},
        {"jaut": "Kurā gadījumā salīdzina saucējus un lielāka ir ar mazāko "
                 "saucēju?",
         "opcijas": ["vienādi skaitītāji", "vienādi saucēji",
                     "vienmēr"], "pareizi": 0,
         "padoms": "Vienāds gabalu skaits."},
        {"jaut": "Kura mazākā: {2|9}, {2|3}, {2|5}?",
         "opcijas": ["{2|9}", "{2|3}", "{2|5}"], "pareizi": 0,
         "padoms": "Lielākais saucējs."},
    ], pamats=4),

    Ievadi("Atrodi saucēju", [
        {"jaut": "Lielākais saucējs, lai {3|?} > {3|8}?", "atb": ["7"],
         "padoms": "Mazāks par 8."},
        {"jaut": "Mazākais saucējs, lai {2|?} < {2|5}?", "atb": ["6"],
         "padoms": "Lielāks par 5."},
        {"jaut": "Kura mazākā: {5|6}, {5|11}, {5|8}? Raksti daļu.",
         "atb": ["5/11"], "vieta": "piem., 1/2",
         "padoms": "Lielākais saucējs."},
        {"jaut": "Kura lielākā: {4|9}, {4|5}, {4|7}?", "atb": ["4/5"],
         "vieta": "piem., 1/2", "padoms": "Mazākais saucējs."},
    ]),

    Pasaule("Kuru piedāvājumu ņemt?",
            Varianti("", [
                {"jaut": "Draugi dala 2 picas: 5 draugi vai 8 draugi? Kur "
                         "katram vairāk?",
                 "opcijas": ["5 draugi", "8 draugi", "vienādi"],
                 "pareizi": 0, "padoms": "{2|5} > {2|8}."},
                {"jaut": "Atlaide «{1|3} no cenas» vai «{1|4} no cenas» - "
                         "kur atlaide lielāka?",
                 "opcijas": ["{1|3}", "{1|4}", "vienādi"], "pareizi": 0,
                 "padoms": "Trešdaļa lielāka."},
                {"jaut": "Sulas {3|4} litra vai {3|5} litra - kur vairāk?",
                 "opcijas": ["{3|4}", "{3|5}", "vienādi"], "pareizi": 0,
                 "padoms": "Ceturtdaļas lielākas."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā un draugu lokā bieži jāizvēlas starp daļām "
                      "ar vienādu skaitītāju.",
            kapec="Spriedums par saucēju ļauj izvēlēties pareizi uzreiz."),

    Kopsavilkums([
        "Salīdzinu daļas ar vienādiem skaitītājiem.",
        "Zinu: mazāks saucējs - lielāka daļa.",
        "Pamatoju spriedumu ar gabalu lielumu.",
    ]),

    Majas([
        "Sakārto: {3|4}, {3|9}, {3|6}, {3|5}.",
        "Izdomā dzīves situāciju, kurā jāsalīdzina {2|3} un {2|5}.",
        "Paskaidro kādam atšķirību starp 99. un 101. stundas noteikumu.",
    ]),
]
