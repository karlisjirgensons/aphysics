# -*- coding: utf-8 -*-
"""3. klase, 89. stunda: «Kura daļa ir lielāka?»

Salīdzināšana sākas ar vieglāko gadījumu: vienādi saucēji. Tad daļas ir
vienāda lieluma gabali, un izšķir tikai to skaits - tāpēc salīdzināt var
tāpat kā veselus skaitļus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kura daļa ir lielāka?"

MERKIS = ("Salīdzināsim daļas ar vienādiem saucējiem un pamatosim to ar "
          "modeli.")

SATURS = [
    Sakums("Kura daļa ir lielāka - {3|8} vai {5|8}?",
           zimejums=dala(8, 5, "5/8", "astoņas vienādas daļas"),
           paraksts="Daļas ir vienāda lieluma, tāpēc izšķir tikai to skaits.",
           fakti=["Ja saucēji ir vienādi, daļas ir vienāda lieluma gabali.",
                  "Lielāka ir tā daļa, kurai skaitītājs ir lielāks."]),

    Doma("Vienādi saucēji - salīdzini skaitītājus",
         "{5|8} > {3|8}, jo piecas astotdaļas ir vairāk gabalu nekā trīs.",
         soli=[
             "Pārbaudi, vai saucēji ir vienādi.",
             "Salīdzini skaitītājus kā parastus skaitļus.",
             "Lielākais skaitītājs dod lielāko daļu.",
             "Pieraksti salīdzinājumu ar «<» vai «>».",
         ],
         pieze="Tas strādā *tikai* tad, kad saucēji ir vienādi. {1|2} un "
               "{3|8} tā salīdzināt nedrīkst - gabali ir dažāda lieluma."),

    Paraugs("Kura daļa ir lielāka?",
            uzd="Salīdzini {3|8} un {5|8}.",
            soli=[
                ("Saucēji ir vienādi - 8",
                 "Abas daļas ir astotdaļas."),
                ("3 < 5",
                 "Salīdzina skaitītājus."),
                ("{3|8} < {5|8}",
                 "Piecas astotdaļas ir lielākas."),
            ],
            atbilde="{5|8} ir lielāka"),

    Ievadi("Salīdzini daļas", [
        {"jaut": "Kurai daļai skaitītājs ir lielāks: {3|8} vai {5|8}? "
                 "Ieraksti skaitītāju.",
         "atb": ["5"], "padoms": "5 > 3."},
        {"jaut": "Kura daļa ir lielāka: {2|9} vai {7|9}? Ieraksti "
                 "skaitītāju.",
         "atb": ["7"], "padoms": "7 > 2."},
        {"jaut": "Kura daļa ir mazāka: {4|10} vai {9|10}? Ieraksti "
                 "skaitītāju.",
         "atb": ["4"], "padoms": "4 < 9."},
        {"jaut": "Par cik daļām {7|9} ir lielāks nekā {2|9}?",
         "atb": ["5"], "padoms": "7 − 2."},
        {"jaut": "Kura daļa ir lielākā: {1|6}, {5|6} vai {3|6}? Ieraksti "
                 "skaitītāju.",
         "atb": ["5"], "padoms": "Lielākais skaitītājs."},
        {"jaut": "Cik astotdaļu ir starp {2|8} un {7|8}?",
         "atb": ["5"], "padoms": "7 − 2."},
    ], pamats=4),

    Zimejums("Divas daļas ar vienu saucēju",
             dala(8, 3, "3/8", "tās pašas astotdaļas"),
             paskaidro="Salīdzini ar stundas sākuma zīmējumu: gabali vienādi, "
                       "bet iekrāsoto ir mazāk.",
             ievads="Tā izskatās {3|8}."),

    Varianti("Kurš salīdzinājums ir pareizs?", [
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["{5|9} > {4|9}", "{5|9} < {4|9}", "{5|9} = {4|9}",
                     "To nevar salīdzināt"],
         "pareizi": 0, "padoms": "Saucēji vienādi, salīdzina skaitītājus."},
        {"jaut": "Kura daļa ir vislielākā?",
         "opcijas": ["{9|10}", "{7|10}", "{3|10}", "{1|10}"],
         "pareizi": 0, "padoms": "Lielākais skaitītājs."},
        {"jaut": "Kad šo paņēmienu lietot nedrīkst?",
         "opcijas": ["Kad saucēji atšķiras", "Kad skaitītāji atšķiras",
                     "Kad daļas ir mazas", "Vienmēr drīkst"],
         "pareizi": 0, "padoms": "Gabali būtu dažāda lieluma."},
        {"jaut": "Kura daļa ir vismazākā?",
         "opcijas": ["{1|7}", "{3|7}", "{5|7}", "{6|7}"],
         "pareizi": 0, "padoms": "Mazākais skaitītājs."},
    ], pamats=4),

    Pasaule("Kurš koks aug ātrāk?",
            Ievadi("", [
                {"jaut": "Pirmais koks izaudzis {3|10} no plānotā auguma, "
                         "otrais {7|10}. Kurš izaudzis vairāk? Ieraksti "
                         "skaitītāju.",
                 "atb": ["7"], "padoms": "7 > 3."},
                {"jaut": "Plānotais augums ir 20 m. Cik metru ir {7|10}?",
                 "atb": ["14"], "padoms": "20 : 10 = 2; 7 · 2."},
                {"jaut": "Cik metru ir {3|10}?", "atb": ["6"],
                 "padoms": "3 · 2."},
                {"jaut": "Par cik metriem pirmais koks ir zemāks?",
                 "atb": ["8"], "padoms": "14 − 6."},
            ]),
            pavediens="daba",
            konteksts="Mežsargs pieraksta koku augumu kā daļu no pilnā "
                      "auguma - tā var salīdzināt dažādas sugas.",
            kapec="Ja saucējs ir viens, salīdzināt var uzreiz."),

    Kopsavilkums([
        "Salīdzinu daļas ar vienādiem saucējiem.",
        "Pamatoju salīdzinājumu ar modeli.",
        "Pierakstu salīdzinājumu ar «<» vai «>».",
        "Zinu, ka šis paņēmiens der tikai vienādiem saucējiem.",
    ]),

    Majas([
        "Salīdzini {2|7} un {5|7} un uzzīmē modeli.",
        "Sakārto augošā secībā {1|6}, {5|6} un {3|6}.",
        "Atrodi mājās divas daļas ar vienādu saucēju un salīdzini tās.",
    ]),
]
