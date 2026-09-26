# -*- coding: utf-8 -*-
"""4. klase, 108. stunda: «Cik dažādi var pierakstīt vienu daļu?»

Radošā stunda: {5|8} = {1|8} + {4|8} = {2|8} + {3|8} = {7|8} − {2|8} ...
Vienu daļu var uzrakstīt kā summu vai starpību ļoti daudzos veidos, un
skaitli 1 - vēl vairāk. Skolēns meklē visus variantus sistemātiski.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Cik dažādi var pierakstīt vienu daļu?"

MERKIS = ("Uzrakstīsim doto daļu vai skaitli 1 kā summu vai starpību "
          "dažādos veidos.")

SATURS = [
    Sakums("Cik veidos {5|8} var salikt no divām daļām?",
           zimejums=restis([["1/8 + 4/8"], ["2/8 + 3/8"],
                            ["3/8 + 2/8"], ["4/8 + 1/8"]],
                           "visas summas ar 2 saskaitāmajiem"),
           paraksts="Skaitītāji kopā - 5.",
           fakti=["Vienam skaitlim ir daudz pierakstu.",
                  "Sistemātiski - sāc ar 1 un palielini."]),

    Doma("Sadali skaitītāju",
         "Lai uzrakstītu {a|n} kā summu, sadali skaitītāju a divos (vai "
         "vairākos) saskaitāmajos; saucējs paliek n.",
         soli=[
             "5 = 1 + 4 = 2 + 3 = 3 + 2 = 4 + 1.",
             "Katram - saucējs 8.",
             "Starpība: 5 = 6 − 1 = 7 − 2 = 8 − 3 ...",
             "Arī ar trim saskaitāmajiem: 5 = 1 + 1 + 3.",
         ],
         pieze="Skaitli 1 ar saucēju 8 var uzrakstīt kā {1|8} + {7|8}, "
               "{2|8} + {6|8} ... un pat {9|8} − {1|8}."),

    Paraugs("1 kā summa",
            uzd="Uzraksti 1 kā divu daļu summu ar saucēju 5 visos veidos.",
            soli=[
                ("{1|5} + {4|5}", None),
                ("{2|5} + {3|5}", None),
                ("{3|5} + {2|5}", None),
                ("{4|5} + {1|5}", None),
            ],
            atbilde="4 veidi (vai 2, ja secība nav svarīga)"),

    Ievadi("Cik veidu?", [
        {"jaut": "Cik veidos {6|10} uzrakstīt kā divu daļu summu (skaitītāji "
                 "≥ 1, secība svarīga)?", "atb": ["5"],
         "padoms": "1 + 5, 2 + 4, 3 + 3, 4 + 2, 5 + 1."},
        {"jaut": "{4|7} = {1|7} + {?|7}", "atb": ["3"], "padoms": "4 − 1."},
        {"jaut": "{4|7} = {9|7} − {?|7}", "atb": ["5"], "padoms": "9 − 4."},
        {"jaut": "1 = {3|8} + {?|8}", "atb": ["5"], "padoms": "8 − 3."},
    ]),

    Varianti("Vai tas ir tas pats?", [
        {"jaut": "Vai {2|9} + {5|9} = {7|9}?",
         "opcijas": ["jā", "nē"], "pareizi": 0, "padoms": "2 + 5 = 7."},
        {"jaut": "Vai {10|9} − {3|9} = {7|9}?",
         "opcijas": ["jā", "nē"], "pareizi": 0, "padoms": "10 − 3 = 7."},
        {"jaut": "Vai {1|9} + {1|9} + {5|9} = {7|9}?",
         "opcijas": ["jā", "nē"], "pareizi": 0, "padoms": "1 + 1 + 5 = 7."},
        {"jaut": "Vai {3|9} + {3|9} = {7|9}?",
         "opcijas": ["nē", "jā"], "pareizi": 0, "padoms": "3 + 3 = 6."},
    ], pamats=4),

    Pasaule("Monētu kombinācijas",
            Ievadi("", [
                {"jaut": "1 € = 100 ct. 50 ct ir {50|100} €. Cik 50 centu "
                         "monētu ir 1 €?",
                 "atb": ["2"], "padoms": "{50|100} + {50|100}."},
                {"jaut": "20 ct = {20|100} €. Cik 20 centu monētu ir 1 €?",
                 "atb": ["5"], "padoms": "100 : 20."},
                {"jaut": "Ar 50 ct un 20 ct monētām: 50 + 20 + 20 + ? = 100. "
                         "Kāda monēta trūkst (centos)?",
                 "atb": ["10"], "padoms": "100 − 90."},
                {"jaut": "Cik 10 centu monētu ir {1|2} €?", "atb": ["5"],
                 "padoms": "50 : 10."},
            ]),
            pavediens="veikals",
            konteksts="Vienu eiro var samaksāt ar ļoti dažādām monētu "
                      "kombinācijām - tās ir daļas no eiro.",
            kapec="Viens skaitlis - daudz pierakstu, tāpat kā nauda."),

    Kopsavilkums([
        "Uzrakstu daļu kā summu vai starpību vairākos veidos.",
        "Meklēju variantus sistemātiski.",
        "Uzrakstu 1 kā daļu summu.",
    ]),

    Majas([
        "Uzraksti 1 kā divu daļu summu ar saucēju 6 visos veidos.",
        "Atrodi 3 veidus, kā samaksāt 1 € ar monētām.",
        "Uzraksti {3|4} kā trīs daļu summu.",
    ]),
]
