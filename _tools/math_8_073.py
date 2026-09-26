# -*- coding: utf-8 -*-
"""8. klase, 73. stunda: «Cik liels ir riņķa gredzens?»

Kombinētas figūras ar riņķi: gredzens π(R^2 − r^2), pusriņķis,
ceturtdaļriņķis, kvadrāts ar ievilktu riņķi, stadions. Zīmējums
gredzens() iekrāso tikai joslu starp abām riņķa līnijām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, gredzens)

TEMA = "Cik liels ir riņķa gredzens?"

MERKIS = "Aprēķināsim kombinētas figūras laukumu, kurā ietilpst riņķis."

SATURS = [
    Sakums("Cik liela ir iekrāsotā josla?",
           zimejums=gredzens("R = 5", "r = 3"),
           paraksts="S = π · 25 − π · 9 = 16π",
           fakti=["Gredzens ir lielais riņķis bez mazā.",
                  "S = πR^2 − πr^2 = π(R^2 − r^2).",
                  "Citas figūras sadala: kvadrāts, pusriņķis, ceturtdaļriņķis."]),

    Doma("Figūra no daļām",
         "Kombinētas figūras laukums ir daļu laukumu summa vai starpība.",
         soli=[
             "Atrodi, no kādām daļām figūra sastāv.",
             "Pusriņķis ir {πr^2|2}, ceturtdaļriņķis - {πr^2|4}.",
             "Saskaiti vai atņem daļu laukumus.",
             "Atbildi atstāj ar π vai noapaļo, kā prasīts.",
         ],
         pieze="Gredzenā nevar atņemt rādiusus: π(5 − 3)^2 = 4π, bet "
               "pareizi ir 16π."),

    Paraugs("Kvadrāta stūri",
            uzd="Kvadrātā ar malu 10 cm ievilkts riņķis. Cik cm² ir četros "
                "stūros ārpus riņķa (π ≈ 3,14)?",
            soli=[
                ("10 · 10 = 100 cm²", "Kvadrāts."),
                ("r = 5; π · 25 ≈ 78,5 cm²", "Riņķis: diametrs = mala."),
                ("100 − 78,5 = 21,5 cm²", "Stūri."),
            ],
            atbilde="21,5 cm²"),

    Ievadi("Aprēķini", [
        {"jaut": "R = 6, r = 4. Gredzens = ?π", "atb": ["20"],
         "padoms": "36 − 16."},
        {"jaut": "R = 10, r = 8. Gredzens = ?π", "atb": ["36"],
         "padoms": "100 − 64."},
        {"jaut": "Pusriņķis ar r = 4. S = ?π", "atb": ["8"],
         "padoms": "{16|2}."},
        {"jaut": "Ceturtdaļriņķis ar r = 6. S = ?π", "atb": ["9"],
         "padoms": "{36|4}."},
        {"jaut": "Taisnstūris 8 × 4 un ārpusē pusriņķis ar d = 4. S (π ≈ "
                 "3,14)?", "atb": ["38,28"], "padoms": "32 + 2π."},
        {"jaut": "Kvadrāts 4 × 4 bez ceturtdaļriņķa ar r = 4. S (π ≈ 3,14)?",
         "atb": ["3,44"], "padoms": "16 − 4π."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Gredzenam R = 5, r = 4. Kurš aprēķins pareizs?",
         "opcijas": ["π(25 − 16)", "π(5 − 4)^2", "π · 1", "2π(5 − 4)"],
         "pareizi": 0, "padoms": "Atņem laukumus, ne rādiusus."},
        {"jaut": "R = 2r. Gredzens ir kāda daļa no lielā riņķa?",
         "opcijas": ["{3|4}", "{1|2}", "{1|4}", "{2|3}"],
         "pareizi": 0, "padoms": "Mazais riņķis ir {1|4} no lielā."},
        {"jaut": "Stadions: taisnstūris un divi pusriņķi galos. Pusriņķi "
                 "kopā ir...",
         "opcijas": ["viens riņķis", "divi riņķi", "puse riņķa",
                     "kvadrāts"],
         "pareizi": 0, "padoms": "Divas puses."},
    ]),

    Pasaule("Stadions",
            Ievadi("", [
                {"jaut": "Laukums: taisnstūris 100 m × 60 m un divi pusriņķi "
                         "ar d = 60 m. S (m², π ≈ 3,14)?",
                 "atb": ["8826"], "padoms": "6000 + 900 · 3,14."},
                {"jaut": "Apļveida celiņš: R = 40 m, r = 36 m. Celiņa "
                         "laukums = ?π m²",
                 "atb": ["304"], "padoms": "1600 − 1296."},
                {"jaut": "Tas aptuveni (m², π ≈ 3,14, veselos)?",
                 "atb": ["955"], "padoms": "304 · 3,14 = 954,56."},
            ]),
            pavediens="sports",
            konteksts="Stadiona, celiņu un fontānu plānos ir riņķi un to "
                      "daļas.",
            kapec="Celiņš ap apli ir gredzens - starpība starp diviem "
                  "riņķiem."),

    Kopsavilkums([
        "Aprēķinu riņķa gredzena laukumu.",
        "Aprēķinu pusriņķa un ceturtdaļriņķa laukumu.",
        "Sadalu kombinētu figūru daļās ar riņķiem.",
    ]),

    Majas([
        "Izmēri CD vai šķīvja malu un aprēķini gredzena laukumu.",
        "Uzzīmē logu - taisnstūris ar pusriņķi augšā - un aprēķini laukumu.",
        "Aprēķini, cik m² aizņem apļveida celiņš tavā parkā.",
    ]),
]
