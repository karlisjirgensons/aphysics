# -*- coding: utf-8 -*-
"""4. klase, 6. stunda: «Kā izlasīt un uzrakstīt četrciparu skaitli?»

Pirmais solis pāri tūkstotim. Četrciparu skaitli lasa tāpat kā trīsciparu,
tikai priekšā pieliek tūkstošus: 2026 - divi tūkstoši divdesmit seši.
Grūtākais ir nulles: «trīs tūkstoši pieci» ir 3005, nevis 35 vai 305.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izlasīt un uzrakstīt četrciparu skaitli?"

MERKIS = ("Lasīsim un rakstīsim skaitļus līdz 10 000 ar cipariem un "
          "vārdiem, arī tad, ja skaitlī ir nulles.")

SATURS = [
    Sakums("Cik gadu ir Rīgai?",
           zimejums=restis([["tūkstoši", "simti", "desmiti", "vieni"],
                            [1, 2, 0, 1]],
                           "Rīga dibināta 1201. gadā"),
           paraksts="Tūkstotis divi simti viens.",
           fakti=["2026. gadā Rīgai ir 825 gadi.",
                  "Gadu skaitļi ir četrciparu skaitļi.",
                  "Četrciparu skaitlim priekšā ir vēl viena šķira - tūkstoši."]),

    Doma("Tūkstošus lasa pirmos, tad kā trīsciparu skaitli",
         "Četrciparu skaitli izrunā pa šķirām no kreisās: tūkstoši, simti, "
         "desmiti, vieni.",
         soli=[
             "Nosauc pirmo ciparu ar vārdu «tūkstoši».",
             "Atlikušos trīs ciparus lasi kā trīsciparu skaitli.",
             "Šķiras, kurās ir 0, izrunājot izlaiž.",
             "Rakstot ar cipariem, izlaisto šķiru vietā liek 0.",
         ],
         pieze="«Četri tūkstoši septiņdesmit» - simtu nav, vienu nav: 4070."),

    Paraugs("Uzraksti ar cipariem",
            uzd="Uzraksti ar cipariem: «seši tūkstoši divi simti trīs».",
            soli=[
                ("6 tūkstoši → 6 _ _ _",
                 "Tūkstoši ir pirmais cipars."),
                ("2 simti → 6 2 _ _", None),
                ("desmitu nav → 6 2 0 _",
                 "Tukšo vietu aizpilda ar nulli."),
                ("3 vieni → 6203", None),
            ],
            atbilde="6203"),

    Ievadi("Raksti ar cipariem", [
        {"jaut": "Trīs tūkstoši četri simti piecdesmit seši",
         "atb": ["3456"], "padoms": "3 | 4 | 5 | 6."},
        {"jaut": "Septiņi tūkstoši astoņpadsmit",
         "atb": ["7018"], "padoms": "Simtu nav - tur 0."},
        {"jaut": "Pieci tūkstoši seši", "atb": ["5006"],
         "padoms": "Simtu un desmitu nav."},
        {"jaut": "Deviņi tūkstoši deviņi simti deviņdesmit deviņi",
         "atb": ["9999"], "padoms": "Lielākais četrciparu skaitlis."},
        {"jaut": "Divi tūkstoši trīs simti", "atb": ["2300"],
         "padoms": "Desmitu un vienu nav."},
        {"jaut": "Desmit tūkstoši", "atb": ["10000", "10 000"],
         "padoms": "Pirmais piecciparu skaitlis."},
    ], pamats=4,
        ievads="Klausies «ausīs» un raksti ciparus - nulles neaizmirsti."),

    Zimejums("Kur paslēpušās nulles",
             restis([["skaitlis", "T", "S", "D", "V"],
                     ["4070", 4, 0, 7, 0],
                     ["3005", 3, 0, 0, 5],
                     ["8600", 8, 6, 0, 0]],
                    "T - tūkstoši, S - simti, D - desmiti, V - vieni"),
             paskaidro="Katra nulle ir šķira, ko izrunājot nepiemin, bet "
                       "rakstot nedrīkst izlaist.",
             ievads="Šķiru tabula parāda, kāpēc nulles ir vajadzīgas."),

    Varianti("Kā to izlasa?", [
        {"jaut": "Kā izlasa 2026?",
         "opcijas": ["divi tūkstoši divdesmit seši",
                     "divi simti divdesmit seši",
                     "divdesmit divi tūkstoši seši",
                     "divi tūkstoši divi simti seši"], "pareizi": 0,
         "padoms": "Simtu vietā ir 0."},
        {"jaut": "Kurš skaitlis ir «viens tūkstotis viens»?",
         "opcijas": ["1001", "1010", "1100", "11"], "pareizi": 0,
         "padoms": "Tikai tūkstoši un vieni."},
        {"jaut": "Kā izlasa 5300?",
         "opcijas": ["pieci tūkstoši trīs simti", "pieci simti trīsdesmit",
                     "piecdesmit trīs simti", "pieci tūkstoši trīsdesmit"],
         "pareizi": 0, "padoms": "5 | 3 | 0 | 0."},
        {"jaut": "Cik ciparu ir skaitlim «deviņi tūkstoši deviņi»?",
         "opcijas": ["4", "2", "3", "5"], "pareizi": 0,
         "padoms": "9009."},
    ], pamats=4),

    Pasaule("Gadskaitļi Latvijas vēsturē",
            Ievadi("", [
                {"jaut": "Latvijas valsts dibināta tūkstoš deviņi simti "
                         "astoņpadsmitajā gadā. Raksti ar cipariem.",
                 "atb": ["1918"], "padoms": "1 | 9 | 1 | 8."},
                {"jaut": "Cik gadu Latvijai ir 2026. gadā?",
                 "atb": ["108"], "padoms": "2026 − 1918."},
                {"jaut": "Pirmie Dziesmu svētki bija 1873. gadā. Cik gadu "
                         "pagājis līdz 2026. gadam?",
                 "atb": ["153"], "padoms": "2026 − 1873."},
                {"jaut": "Rīga dibināta 1201. gadā. Kurā gadā tai būs "
                         "1000 gadu?",
                 "atb": ["2201"], "padoms": "1201 + 1000."},
            ]),
            pavediens="celojums",
            konteksts="Vēsture ir skaitļu taisne, kurā katrs gads ir "
                      "četrciparu skaitlis.",
            kapec="Gadskaitli uzrakstīt ar cipariem ir pirmais solis, lai "
                  "aprēķinātu, cik laika pagājis."),

    Kopsavilkums([
        "Lasu četrciparu skaitļus pa šķirām.",
        "Rakstu skaitli ar cipariem pēc dzirdētā.",
        "Zinu, kur jāliek nulle, ja šķiras nav.",
        "Zinu, ka 10 000 ir pirmais piecciparu skaitlis.",
    ]),

    Majas([
        "Uzraksti ar vārdiem savu, mammas un vecmāmiņas dzimšanas gadu.",
        "Atrodi mājās četrciparu skaitli (pasta indekss, PIN nav jāraksta!).",
        "Nodiktē mājiniekam trīs skaitļus ar nullēm un pārbaudi pierakstu.",
    ]),
]
