# -*- coding: utf-8 -*-
"""8. klase, 74. stunda: «Cik liels ir sektors?»

Bloka noslēgums: sektors ir tāda daļa no riņķa, kāda centra leņķis ir no
360°. Tas pats princips, ko lietoja sektoru diagrammā (8.1): 25 % = 90°.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, rinkis)

TEMA = "Cik liels ir sektors?"

MERKIS = "Aprēķināsim riņķa daļas laukumu, izmantojot centra leņķi."

SATURS = [
    Sakums("Cik liela ir riņķa ceturtdaļa?",
           zimejums=rinkis(radiuss="r", sektors=90),
           paraksts="90° ir {1|4} no 360°, tāpēc sektors ir {1|4} no riņķa.",
           fakti=["Sektors ir riņķa daļa starp diviem rādiusiem.",
                  "Sektora laukums ir {α|360°} daļa no riņķa laukuma.",
                  "S = {πr^2 · α|360°}."]),

    Doma("Sektora laukums",
         "Sektors ir tāda daļa no riņķa, kāda centra leņķis ir no 360°.",
         soli=[
             "Nosaki, kāda daļa no 360° ir centra leņķis.",
             "Tikpat lielu daļu no riņķa laukuma aizņem sektors.",
             "Pusriņķis - 180°, ceturtdaļa - 90°, trešdaļa - 120°.",
         ],
         pieze="Tāpat zīmē sektoru diagrammu: 25 % datu atbilst 90°."),

    Paraugs("Trešdaļa riņķa",
            uzd="r = 6 cm, centra leņķis 120°. Aprēķini sektora laukumu.",
            soli=[
                ("{120°|360°} = {1|3}", "Daļa no riņķa."),
                ("π · 36 = 36π", "Viss riņķis."),
                ("{36π|3} = 12π ≈ 37,68 cm²", "Sektors (π ≈ 3,14)."),
            ],
            atbilde="12π ≈ 37,68 cm²"),

    Ievadi("Aprēķini", [
        {"jaut": "r = 10, α = 90°. S = ?π", "atb": ["25"],
         "padoms": "{100|4}."},
        {"jaut": "r = 6, α = 60°. S = ?π", "atb": ["6"],
         "padoms": "{36|6}."},
        {"jaut": "r = 3, α = 240°. S = ?π", "atb": ["6"],
         "padoms": "9 · {2|3}."},
        {"jaut": "r = 12, α = 30°. S = ?π", "atb": ["12"],
         "padoms": "{144|12}."},
        {"jaut": "Sektors ir 8π, viss riņķis - 24π. Centra leņķis (°)?",
         "atb": ["120"], "padoms": "{1|3} no 360°."},
        {"jaut": "r = 4, α = 45°. S = ?π", "atb": ["2"],
         "padoms": "{16|8}."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Kāda daļa no riņķa ir 72° sektors?",
         "opcijas": ["{1|5}", "{1|4}", "{1|6}", "{1|3}"],
         "pareizi": 0, "padoms": "360 : 72 = 5."},
        {"jaut": "Sektoru diagrammā 25 % atbilst leņķim...",
         "opcijas": ["90°", "25°", "45°", "100°"],
         "pareizi": 0, "padoms": "{1|4} no 360°."},
        {"jaut": "Divkāršojot centra leņķi, sektora laukums...",
         "opcijas": ["divkāršojas", "četrkāršojas", "nemainās",
                     "samazinās"],
         "pareizi": 0, "padoms": "Laukums ir proporcionāls leņķim."},
    ]),

    Pasaule("Zāliena laistītājs",
            Ievadi("", [
                {"jaut": "Laistītājs griežas par 120° un sniedz 9 m tālu. "
                         "Laistītais laukums = ?π m²",
                 "atb": ["27"], "padoms": "{81|3}."},
                {"jaut": "Aptuveni (π ≈ 3,14), veselos m²?",
                 "atb": ["85"], "padoms": "27 · 3,14 = 84,78."},
                {"jaut": "Par cik grādiem jāgriežas, lai aplaistītu 54π m²?",
                 "atb": ["240"], "padoms": "{54|81} = {2|3} no 360°."},
            ]),
            pavediens="maja",
            konteksts="Zāliena laistītājs griežas pa loku un aplaista riņķa "
                      "sektoru.",
            kapec="Sektors ir tāda pati riņķa daļa, kāda leņķis ir no 360°."),

    Kopsavilkums([
        "Nosaku, kāda riņķa daļa ir sektors.",
        "Aprēķinu sektora laukumu pēc centra leņķa.",
        "No sektora laukuma atrodu centra leņķi.",
    ]),

    Majas([
        "Sagriez apaļu kūku vai picu 8 vienādos gabalos. Kāds ir katra "
        "centra leņķis?",
        "Aprēķini viena gabala laukumu, ja d = 24 cm.",
        "Uzzīmē sektoru diagrammu savai dienas kārtībai.",
    ]),
]
