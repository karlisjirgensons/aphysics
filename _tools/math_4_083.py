# -*- coding: utf-8 -*-
"""4. klase, 83. stunda: «Kā dalīt pakāpeniski?»

Pakāpeniskā dalīšana: no dalāmā atņem lielus dalītāja «gabalus» (10 ·, 20 ·,
5 ·), līdz nekas nepaliek, un saskaita, cik reižu atņemts. Skolēns pats
izvēlas gabalu lielumu un veido savu pierakstu - tā ir stūrīša
priekšvēstnese, bet elastīgāka.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā dalīt pakāpeniski?"

MERKIS = ("Dalīsim trīsciparu skaitli ar divciparu skaitli pakāpeniski un "
          "veidosim sev piemērotu pierakstu.")

SATURS = [
    Sakums("Kā ēst lielu picu? Pa gabaliem!",
           zimejums=restis([["paliek", "atņem", "cik reižu"],
                            ["864", "− 360", "10"],
                            ["504", "− 360", "10"],
                            ["144", "− 144", "4"],
                            ["0", "", "24"]],
                           "864 : 36"),
           paraksts="10 + 10 + 4 = 24, tātad 864 : 36 = 24.",
           fakti=["Nav jāzina uzreiz - var atņemt pa gabaliem.",
                  "Katrs gabals ir dalītājs, reizināts ar ērtu skaitli."]),

    Doma("Atņem ērtus gabalus un skaiti, cik reižu",
         "No dalāmā atņem dalītāju, reizinātu ar 10, 5 vai 2, līdz paliek 0; "
         "reizinātāju summa ir dalījums.",
         soli=[
             "Izrēķini ērtus reizinājumus: 36 · 10 = 360, 36 · 5 = 180.",
             "Atņem lielāko, kas vēl der, un pieraksti reizinātāju.",
             "Atkārto, līdz paliek 0 (vai mazāk par dalītāju).",
             "Saskaiti reizinātājus - tas ir dalījums.",
         ],
         pieze="Ja beigās paliek mazāk par dalītāju, tas ir atlikums."),

    Slidnis("744 : 24 pakāpeniski",
            soli=[
                {"v": "744", "teksts": "Sākums.", "josla": 100},
                {"v": "744 − 480 = 264", "teksts": "24 · 20. Kopā 20.",
                 "josla": 35},
                {"v": "264 − 240 = 24", "teksts": "24 · 10. Kopā 30.",
                 "josla": 3},
                {"v": "24 − 24 = 0", "teksts": "24 · 1. Kopā 31.",
                 "josla": 0},
            ],
            ievads="Josla rāda, cik no dalāmā vēl palicis."),

    Paraugs("918 : 27",
            uzd="Izdali pakāpeniski 918 : 27.",
            soli=[
                ("918 − 540 = 378", "27 · 20."),
                ("378 − 270 = 108", "27 · 10."),
                ("108 − 108 = 0", "27 · 4."),
                ("20 + 10 + 4 = 34", None),
            ],
            atbilde="34"),

    Ievadi("Pakāpeniski", [
        {"jaut": "864 : 36 = ?", "atb": ["24"], "padoms": "10 + 10 + 4."},
        {"jaut": "744 : 24 = ?", "atb": ["31"], "padoms": "20 + 10 + 1."},
        {"jaut": "918 : 27 = ?", "atb": ["34"], "padoms": "20 + 10 + 4."},
        {"jaut": "782 : 34 = ?", "atb": ["23"], "padoms": "20 + 3."},
        {"jaut": "936 : 52 = ?", "atb": ["18"], "padoms": "10 + 5 + 3."},
        {"jaut": "Kāds atlikums 500 : 23?", "atb": ["17"],
         "padoms": "23 · 21 = 483."},
    ], pamats=4),

    Varianti("Pakāpeniski ceļi", [
        {"jaut": "Kurš gabals ir ērts, dalot ar 45?",
         "opcijas": ["450", "400", "500", "440"], "pareizi": 0,
         "padoms": "45 · 10."},
        {"jaut": "Juris: atņēma 36 · 10, 36 · 10, 36 · 4. Dalījums?",
         "opcijas": ["24", "3", "360", "14"], "pareizi": 0,
         "padoms": "10 + 10 + 4."},
        {"jaut": "Vai dažādi ceļi dod dažādus dalījumus?",
         "opcijas": ["nē, dalījums vienāds", "jā", "atkarīgs no gabaliem"],
         "pareizi": 0, "padoms": "Mainās tikai soļu skaits."},
    ]),

    Pasaule("Maratona ūdens punkti",
            Ievadi("", [
                {"jaut": "Trasē jāizvieto 864 pudeles 36 punktos vienādi. "
                         "Cik katrā?",
                 "atb": ["24"], "padoms": "864 : 36."},
                {"jaut": "Brīvprātīgie: 744 stundas darba, katrs strādā 24 "
                         "stundas. Cik brīvprātīgo?",
                 "atb": ["31"], "padoms": "744 : 24."},
                {"jaut": "Medaļas: 918 medaļas 27 kastēs. Cik vienā kastē?",
                 "atb": ["34"], "padoms": "918 : 27."},
                {"jaut": "936 banāni 52 galdiem. Cik uz galda?",
                 "atb": ["18"], "padoms": "936 : 52."},
            ]),
            pavediens="sports",
            konteksts="Lielu sacensību organizatori dala tūkstošiem lietu "
                      "vienādi pa punktiem.",
            kapec="Pakāpeniski var dalīt pat tad, ja reizinājumu nezini."),

    Kopsavilkums([
        "Dalu pakāpeniski, atņemot ērtus gabalus.",
        "Veidoju sev saprotamu pierakstu.",
        "Saskaitu reizinātājus un iegūstu dalījumu.",
    ]),

    Majas([
        "Izdali pakāpeniski 960 : 32.",
        "Izmēģini to pašu dalījumu ar citiem gabaliem - vai dalījums sakrīt?",
        "Paskaidro mājiniekiem pakāpenisko dalīšanu ar picas piemēru.",
    ]),
]
