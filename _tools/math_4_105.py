# -*- coding: utf-8 -*-
"""4. klase, 105. stunda: «Ko nozīmē saskaitīt daļas?»

Saskaitīt daļas ar vienādiem saucējiem nozīmē saskaitīt vienāda izmēra
gabalus: {2|8} + {3|8} = {5|8}. Modelis - sloksnītes un lēcieni pa skaitļu
taisni - pasargā no biežās kļūdas saskaitīt arī saucējus ({5|16}).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, dala, taisne)

TEMA = "Ko nozīmē saskaitīt daļas?"

MERKIS = ("Modelēsim daļu saskaitīšanu ar sloksnītēm, zīmējumu vai uz "
          "skaitļu taisnes.")

SATURS = [
    Sakums("{2|8} picas + {3|8} picas = ?",
           zimejums=dala(8, 5, "2/8 + 3/8 = 5/8"),
           paraksts="Divi gabali un vēl trīs - pieci gabali.",
           fakti=["Gabali vienāda lieluma - tos var vienkārši saskaitīt.",
                  "Gabalu izmērs (saucējs) nemainās."]),

    Doma("Saskaita gabalus, nevis gabalu izmēru",
         "Saskaitot daļas ar vienādiem saucējiem, saskaita skaitītājus, bet "
         "saucējs paliek tas pats.",
         soli=[
             "Pārbaudi: saucēji vienādi?",
             "Saskaiti skaitītājus: 2 + 3 = 5.",
             "Saucēju pārraksti: 8.",
             "{2|8} + {3|8} = {5|8}.",
         ],
         pieze="Ja saskaitītu arī saucējus, sanāktu {5|16} - mazāk nekā "
               "puse, lai gan ēdām vairāk nekā pusi picas!"),

    Slidnis("Lēcieni pa taisni",
            soli=[
                {"v": "{2|8}", "zim": taisne(0, 1, 1, [(0.25, "2/8")],
                                               sikas=8),
                 "teksts": "Sākam pie {2|8}."},
                {"v": "{2|8} + {3|8}",
                 "zim": taisne(0, 1, 1, [(0.25, "2/8"), (5 / 8.0, "5/8")],
                               sikas=8,
                               bultas=[(0.25, 5 / 8.0, "+3/8")]),
                 "teksts": "Lecam 3 astotdaļas pa labi."},
                {"v": "= {5|8}", "zim": taisne(0, 1, 1, [(5 / 8.0, "5/8")],
                                               sikas=8),
                 "teksts": "Nonākam pie {5|8}."},
            ]),

    Paraugs("{3|10} + {4|10}",
            uzd="Saskaiti {3|10} + {4|10}.",
            soli=[
                ("3 + 4 = 7", "Skaitītāji."),
                ("{7|10}", "Saucējs paliek 10."),
            ],
            atbilde="{7|10}"),

    Ievadi("Saskaiti", [
        {"jaut": "{1|5} + {2|5} = ?", "atb": ["3/5"], "vieta": "piem., 1/2",
         "padoms": "1 + 2."},
        {"jaut": "{3|7} + {3|7} = ?", "atb": ["6/7"], "vieta": "piem., 1/2",
         "padoms": "3 + 3."},
        {"jaut": "{4|9} + {5|9} = ?", "atb": ["9/9", "1"],
         "vieta": "piem., 1/2", "padoms": "Viss veselais."},
        {"jaut": "{5|12} + {2|12} = ?", "atb": ["7/12"],
         "vieta": "piem., 1/2", "padoms": "5 + 2."},
        {"jaut": "{3|4} + {2|4} = ?", "atb": ["5/4"], "vieta": "piem., 1/2",
         "padoms": "Neīsta daļa."},
        {"jaut": "{1|6} + {1|6} + {1|6} = ?", "atb": ["3/6"],
         "vieta": "piem., 1/2", "padoms": "1 + 1 + 1."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "Toms: {2|5} + {1|5} = {3|10}. Kas nav kārtībā?",
         "opcijas": ["saskaitīja arī saucējus", "viss pareizi",
                     "saskaitīja nepareizi skaitītājus"], "pareizi": 0,
         "padoms": "Pareizi {3|5}."},
        {"jaut": "Kāpēc saucējs paliek tas pats?",
         "opcijas": ["gabalu izmērs nemainās", "tā vienkārši ir",
                     "saucēju nevar saskaitīt"], "pareizi": 0,
         "padoms": "Saskaita gabalus, nevis to izmēru."},
        {"jaut": "Cik ir {1|3} + {1|3}?",
         "opcijas": ["{2|3}", "{2|6}", "{1|6}", "{1|3}"], "pareizi": 0,
         "padoms": "Divas trešdaļas."},
    ]),

    Pasaule("Receptes sastāvdaļas",
            Ievadi("", [
                {"jaut": "Kūkai {1|4} glāzes cukura un vēl {2|4} glāzes. Cik "
                         "kopā? Raksti daļu.",
                 "atb": ["3/4"], "vieta": "piem., 1/2", "padoms": "1 + 2."},
                {"jaut": "Piens: {3|8} l un {3|8} l. Cik kopā?",
                 "atb": ["6/8"], "vieta": "piem., 1/2", "padoms": "3 + 3."},
                {"jaut": "Milti: {2|3} glāzes un {1|3} glāzes. Cik kopā?",
                 "atb": ["3/3", "1"], "vieta": "piem., 1/2",
                 "padoms": "Viena pilna glāze."},
                {"jaut": "Sviests: {1|5} paciņas trīs reizes. Cik kopā?",
                 "atb": ["3/5"], "vieta": "piem., 1/2",
                 "padoms": "1 + 1 + 1."},
            ]),
            pavediens="virtuve",
            konteksts="Receptē sastāvdaļas bieži pievieno pa daļām - un "
                      "tās jāsaskaita.",
            kapec="Pareizi saskaitot daļas, kūka izdodas."),

    Kopsavilkums([
        "Saskaitu daļas ar vienādiem saucējiem.",
        "Zinu, ka saucējs nemainās.",
        "Modelēju saskaitīšanu ar joslu un taisni.",
    ]),

    Majas([
        "Ar papīra sloksnītēm parādi {3|6} + {2|6}.",
        "Atrodi receptē divas daļas un saskaiti.",
        "Paskaidro kādam, kāpēc {1|2} + {1|2} nav {2|4}.",
    ]),
]
