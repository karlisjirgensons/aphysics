# -*- coding: utf-8 -*-
"""4. klase, 25. stunda: «Kā reizināt bez pārejas citā šķirā?»

Pēc modeļa - pieraksts. Kad katra šķira reizinājumā paliek mazāka par 10,
rezultātu var uzrakstīt uzreiz, bet sākumā pieraksta starprezultātus:
43 · 2 = 40 · 2 + 3 · 2 = 80 + 6 = 86.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā reizināt bez pārejas citā šķirā?"

MERKIS = ("Reizināsim divciparu skaitli ar viencipara skaitli galvā, "
          "pierakstot starprezultātus.")

SATURS = [
    Sakums("Cik krāsu zīmuļu 4 kastītēs pa 12?",
           zimejums=restis([["", "desmiti", "vieni"],
                            ["12", 1, 2],
                            ["· 4", 4, 8]],
                           "12 · 4 = 48"),
           paraksts="Ne vieni, ne desmiti nepārsniedz 9.",
           fakti=["Krāsu zīmuļu kastītē bieži ir 12 krāsas.",
                  "Kad šķira nepārsniedz 9, rezultātu raksta uzreiz."]),

    Doma("Katru šķiru reizina un pieraksta starprezultātu",
         "32 · 3: pieraksti 30 · 3 = 90 un 2 · 3 = 6, tad saskaiti "
         "90 + 6 = 96.",
         soli=[
             "Sadali skaitli desmitos un vienos.",
             "Reizini desmitus - pieraksti.",
             "Reizini vienus - pieraksti.",
             "Saskaiti starprezultātus.",
         ],
         pieze="Kad ir veiklība, starprezultātus var paturēt galvā: "
               "32 · 3 = 96."),

    Paraugs("43 · 2",
            uzd="Izrēķini 43 · 2, pierakstot starprezultātus.",
            soli=[
                ("40 · 2 = 80", "Desmiti."),
                ("3 · 2 = 6", "Vieni."),
                ("80 + 6 = 86", None),
            ],
            atbilde="86"),

    Slidnis("Rindā: 24 · 2",
            soli=[
                {"v": "24 · 2", "teksts": "Sākums."},
                {"v": "20 · 2 + 4 · 2", "teksts": "Sadalām."},
                {"v": "40 + 8", "teksts": "Reizinām katru daļu."},
                {"v": "48", "teksts": "Saskaitām."},
            ],
            ievads="Četri soļi, katrs viegls."),

    Ievadi("Galvā ar starprezultātiem", [
        {"jaut": "34 · 2 = ?", "atb": ["68"], "padoms": "60 + 8."},
        {"jaut": "21 · 3 = ?", "atb": ["63"], "padoms": "60 + 3."},
        {"jaut": "42 · 2 = ?", "atb": ["84"], "padoms": "80 + 4."},
        {"jaut": "11 · 9 = ?", "atb": ["99"], "padoms": "90 + 9."},
        {"jaut": "13 · 3 = ?", "atb": ["39"], "padoms": "30 + 9."},
        {"jaut": "22 · 4 = ?", "atb": ["88"], "padoms": "80 + 8."},
        {"jaut": "31 · 2 = ?", "atb": ["62"], "padoms": "60 + 2."},
        {"jaut": "20 · 4 = ?", "atb": ["80"], "padoms": "2 desmiti · 4."},
    ], pamats=6),

    Varianti("Kurš starprezultāts?", [
        {"jaut": "32 · 3 = 90 + ☐",
         "opcijas": ["6", "9", "5", "32"], "pareizi": 0,
         "padoms": "2 · 3."},
        {"jaut": "14 · 2 = ☐ + 8",
         "opcijas": ["20", "10", "28", "12"], "pareizi": 0,
         "padoms": "10 · 2."},
        {"jaut": "Kurā reizinājumā *nav* pārejas citā šķirā?",
         "opcijas": ["23 · 3", "25 · 3", "18 · 2", "36 · 2"], "pareizi": 0,
         "padoms": "3 · 3 = 9 < 10."},
        {"jaut": "Kurā reizinājumā ir pāreja?",
         "opcijas": ["16 · 2", "12 · 4", "21 · 3", "11 · 5"], "pareizi": 0,
         "padoms": "6 · 2 = 12 - rodas jauns desmits."},
    ], pamats=4),

    Pasaule("Kosmosa stacijas krājumi",
            Ievadi("", [
                {"jaut": "Viens astronauts dienā izdzer 2 l ūdens. Cik litru "
                         "izdzer 4 astronauti 11 dienās? Vispirms: 11 · 2 = ?",
                 "atb": ["22"], "padoms": "Viens astronauts 11 dienās."},
                {"jaut": "Un 4 astronauti: 22 · 4 = ?",
                 "atb": ["88"], "padoms": "80 + 8."},
                {"jaut": "Vienā kravā ir 32 pārtikas pakas. Cik paku 3 "
                         "kravās?",
                 "atb": ["96"], "padoms": "90 + 6."},
                {"jaut": "Stacija aplido Zemi 16 reizes diennaktī. Cik reizes "
                         "2 diennaktīs?",
                 "atb": ["32"], "padoms": "20 + 12."},
            ]),
            pavediens="kosmoss",
            konteksts="Starptautiskā kosmosa stacija ap Zemi apriņķo apmēram "
                      "16 reizes diennaktī.",
            kapec="Krājumus kosmosā plāno ar reizināšanu - veikala tur nav."),

    Kopsavilkums([
        "Reizinu divciparu skaitli ar viencipara skaitli bez pārejas.",
        "Pierakstu starprezultātus.",
        "Atpazīstu, kad pārejas citā šķirā nav.",
    ]),

    Majas([
        "Izdomā piecus reizinājumus, kuros nav pārejas, un atrisini.",
        "Izrēķini, cik dienu ir 4 nedēļās un 3 nedēļās (7 · 4, 7 · 3).",
        "Pastāsti mājiniekam, kā izrēķināji 32 · 3.",
    ]),
]
