# -*- coding: utf-8 -*-
"""4. klase, 99. stunda: «Kura daļa lielāka, ja saucēji vienādi?»

Vienādi saucēji - vienāda izmēra gabali, tāpēc lielāka ir tā daļa, kurā
gabalu vairāk: {5|8} > {3|8}. Skolēns veido paskaidrojošu spriedumu,
nevis tikai liek zīmi - tā vēlāk pamatos arī sarežģītākus salīdzinājumus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kura daļa lielāka, ja saucēji vienādi?"

MERKIS = ("Salīdzināsim daļas ar vienādiem saucējiem un veidosim "
          "paskaidrojošu spriedumu.")

SATURS = [
    Sakums("Kuram vairāk šokolādes?",
           zimejums=dala(8, 5, "Anna: 5/8") + dala(8, 3, "Juris: 3/8"),
           paraksts="Tāfelītes vienādas, gabali vienādi.",
           fakti=["Abiem tāfelīte sadalīta 8 vienādos gabalos.",
                  "Annai 5 gabali, Jurim 3 - Annai vairāk."]),

    Doma("Vienādi saucēji - salīdzini skaitītājus",
         "No divām daļām ar vienādiem saucējiem lielāka ir tā, kurai "
         "lielāks skaitītājs.",
         soli=[
             "Pārbaudi, vai saucēji vienādi.",
             "Ja jā - gabali ir vienāda izmēra.",
             "Salīdzini skaitītājus: vairāk gabalu - lielāka daļa.",
             "Spriedums: «{5|8} > {3|8}, jo 5 gabali ir vairāk nekā 3».",
         ],
         pieze="Uz skaitļu taisnes lielākā daļa ir tālāk pa labi."),

    Paraugs("{4|9} vai {7|9}?",
            uzd="Salīdzini {4|9} un {7|9} un paskaidro.",
            soli=[
                ("9 = 9", "Saucēji vienādi."),
                ("4 < 7", "Skaitītāji."),
                ("{4|9} < {7|9}", "Mazāk vienāda izmēra gabalu."),
            ],
            atbilde="{4|9} < {7|9}"),

    Varianti("Liec zīmi", [
        {"jaut": "{2|5} ☐ {4|5}", "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "2 < 4."},
        {"jaut": "{7|10} ☐ {3|10}", "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "7 > 3."},
        {"jaut": "{6|6} ☐ {5|6}", "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "{6|6} = 1."},
        {"jaut": "{9|4} ☐ {7|4}", "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "Arī neīstām: 9 > 7."},
        {"jaut": "Kura daļa lielākā: {3|7}, {6|7}, {1|7}, {5|7}?",
         "opcijas": ["{6|7}", "{5|7}", "{3|7}", "{1|7}"], "pareizi": 0,
         "padoms": "Lielākais skaitītājs."},
        {"jaut": "Kurš spriedums pareizs?",
         "opcijas": ["{3|8} < {5|8}, jo 3 gabali ir mazāk nekā 5",
                     "{3|8} > {5|8}, jo 3 ir tuvāk 8",
                     "tās nevar salīdzināt"], "pareizi": 0,
         "padoms": "Vienādi gabali - skaitām tos."},
    ], pamats=4),

    Ievadi("Sakārto", [
        {"jaut": "Kura ir mazākā: {5|12}, {2|12}, {9|12}? Raksti daļu.",
         "atb": ["2/12"], "vieta": "piem., 1/2", "padoms": "Skaitītājs 2."},
        {"jaut": "Kura ir lielākā: {3|5}, {1|5}, {4|5}?",
         "atb": ["4/5"], "vieta": "piem., 1/2", "padoms": "Skaitītājs 4."},
        {"jaut": "Lielākais skaitītājs, lai {?|9} < {5|9}?", "atb": ["4"],
         "padoms": "Mazāks par 5."},
        {"jaut": "Mazākais skaitītājs, lai {?|6} > {3|6}?", "atb": ["4"],
         "padoms": "Lielāks par 3."},
    ]),

    Zimejums("Uz skaitļu taisnes",
             dala(10, 3, "3/10") + dala(10, 7, "7/10"),
             paskaidro="{7|10} josla ir garāka - un uz taisnes tā ir tālāk "
                       "pa labi.",
             ievads="Vienādi saucēji - vienāda izmēra iedaļas."),

    Pasaule("Uzdevumu progress",
            Varianti("", [
                {"jaut": "Anna izpildīja {7|10} mājasdarba, Juris {4|10}. "
                         "Kurš vairāk?",
                 "opcijas": ["Anna", "Juris", "vienādi"], "pareizi": 0,
                 "padoms": "7 > 4."},
                {"jaut": "Telefona baterija: pirms {3|5}, tagad {2|5}. "
                         "Kas notika?",
                 "opcijas": ["uzlāde samazinājās", "palielinājās",
                             "nemainījās"], "pareizi": 0,
                 "padoms": "2 < 3."},
                {"jaut": "Spēlē: līmenis {5|8} vai {6|8} - kurš tuvāk "
                         "beigām?",
                 "opcijas": ["{6|8}", "{5|8}", "vienādi"], "pareizi": 0,
                 "padoms": "Tuvāk {8|8}."},
            ]),
            pavediens="dati",
            konteksts="Progresa joslas lietotnēs un spēlēs ir daļas ar "
                      "vienādiem saucējiem.",
            kapec="Salīdzināt var vienā mirklī - skaitot gabalus."),

    Kopsavilkums([
        "Salīdzinu daļas ar vienādiem saucējiem.",
        "Veidoju spriedumu: «..., jo ... gabalu ir vairāk».",
        "Sakārtoju daļas augošā secībā.",
    ]),

    Majas([
        "Sakārto: {5|11}, {9|11}, {2|11}, {7|11}.",
        "Salīdzini telefona uzlādi rīt un šovakar kā daļas no 10.",
        "Izdomā divas daļas ar saucēju 6 un salīdzini tās.",
    ]),
]
