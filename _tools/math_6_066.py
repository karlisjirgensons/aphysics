# -*- coding: utf-8 -*-
"""6. klase, 66. stunda: «Kā aprēķināt virsmas laukumu?»

Formula te nenāk no grāmatas - tā izaug no izklājuma, ko skolēni uzzīmēja
iepriekšējā stundā. Tāpēc svarīgākais uzdevums nav izrēķināt, bet paskaidrot
savu izteiksmi: kāpēc tur ir divnieks un kāpēc trīs reizinājumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         izklajums)

TEMA = "Kā aprēķināt virsmas laukumu?"

MERKIS = ("Mācīsimies aprēķināt taisnstūra paralēlskaldņa virsmas laukumu "
          "un skaidrot savu izteiksmi.")

SATURS = [
    Sakums("Trīs reizinājumi, reizināti ar diviem",
           zimejums=izklajums(4, 3, 2),
           paraksts="Virsmas laukums ir visu sešu taisnstūru laukumu summa - "
                    "un to ir trīs vienādu pāri.",
           fakti=["Virsmas laukumu mēra kvadrātvienībās: cm², m².",
                  "Kvadram tas ir divas reizes trīs dažādu skaldņu summa.",
                  "Kubam visas sešas skaldnes ir vienādas."]),

    Doma("Saskaiti trīs skaldnes un reizini ar divi",
         "Kvadra virsmas laukums ir divas reizes trīs dažādo skaldņu laukumu "
         "summa, jo pretējās skaldnes ir vienādas.",
         soli=[
             "Pieraksti trīs izmērus: garumu, platumu un augstumu.",
             "Izrēķini trīs dažādos laukumus: a · b, a · c un b · c.",
             "Saskaiti tos.",
             "Reizini summu ar 2.",
             "Pieraksti atbildi kvadrātvienībās.",
         ],
         pieze="Kubam ar šķautni a formula kļūst īsāka: sešas vienādas "
               "skaldnes, tātad 6 · a · a. Tas ir tas pats likums, tikai "
               "visi trīs izmēri ir vienādi."),

    Slidnis("Kā aug kuba virsma",
            [{"v": "šķautne 1 cm", "teksts": "virsma 6 cm²", "josla": 6},
             {"v": "šķautne 2 cm", "teksts": "virsma 24 cm²", "josla": 24},
             {"v": "šķautne 3 cm", "teksts": "virsma 54 cm²", "josla": 54},
             {"v": "šķautne 4 cm", "teksts": "virsma 96 cm²", "josla": 96}],
            ievads="Spied soli pa solim: šķautne aug pa vienam centimetram, "
                   "virsma - daudz straujāk."),

    Paraugs("Aprēķini virsmas laukumu",
            uzd="Kaste ir 4 cm gara, 3 cm plata un 2 cm augsta. Cik liels ir "
                "tās virsmas laukums?",
            soli=[
                ("Augša un apakša: 4 · 3 = 12 cm²",
                 "Garums reiz platums."),
                ("Priekša un aizmugure: 4 · 2 = 8 cm²",
                 "Garums reiz augstums."),
                ("Sāni: 3 · 2 = 6 cm²",
                 "Platums reiz augstums."),
                ("12 + 8 + 6 = 26 cm²",
                 "Trīs dažādās skaldnes."),
                ("2 · 26 = 52 cm²",
                 "Katras ir pa divām."),
            ],
            atbilde="52 cm²"),

    Ievadi("Izrēķini virsmas laukumu", [
        {"jaut": "Kaste 4 x 3 x 2 cm. Cik cm² ir virsmas laukums?",
         "atb": ["52"], "padoms": "2 · (12 + 8 + 6)."},
        {"jaut": "Kubs ar šķautni 3 cm. Cik cm² ir virsmas laukums?",
         "atb": ["54"], "padoms": "6 · 9."},
        {"jaut": "Kaste 5 x 4 x 2 cm. Cik cm² ir virsmas laukums?",
         "atb": ["76"], "padoms": "2 · (20 + 10 + 8)."},
        {"jaut": "Kubs ar šķautni 5 cm. Cik cm² ir virsmas laukums?",
         "atb": ["150"], "padoms": "6 · 25."},
        {"jaut": "Kaste 10 x 10 x 5 cm. Cik cm² ir virsmas laukums?",
         "atb": ["400"], "padoms": "2 · (100 + 50 + 50)."},
        {"jaut": "Kuba virsma ir 24 cm². Cik cm gara ir šķautne?",
         "atb": ["2"], "padoms": "24 : 6 = 4; mala ir 2."},
    ], pamats=4),

    Varianti("Kāpēc izteiksme ir tāda?", [
        {"jaut": "Kāpēc formulā ir divnieks?",
         "opcijas": ["Jo pretējās skaldnes ir vienādas",
                     "Jo ir divi izmēri",
                     "Jo laukumu mēra kvadrātos", "Tas ir nejauši"],
         "pareizi": 0,
         "padoms": "Katra skaldne ir pa pāriem."},
        {"jaut": "Kāpēc saskaita tieši trīs reizinājumus?",
         "opcijas": ["Jo dažādu skaldņu ir trīs",
                     "Jo izmēru ir trīs",
                     "Jo virsotņu ir astoņas", "Jo tā ir tradīcija"],
         "pareizi": 0,
         "padoms": "Seši taisnstūri veido trīs pārus."},
        {"jaut": "Kubam ar šķautni a virsma ir...",
         "opcijas": ["6 · a · a", "a · a · a", "4 · a", "2 · a · a"],
         "pareizi": 0,
         "padoms": "Sešas vienādas skaldnes."},
        {"jaut": "Kādās mērvienībās mēra virsmas laukumu?",
         "opcijas": ["cm² un m²", "cm un m", "cm³ un m³", "litros"],
         "pareizi": 0,
         "padoms": "Laukums ir kvadrātvienībās."},
    ], pamats=4),

    Pasaule("Cik krāsas vajag kastei?",
            Ievadi("", [
                {"jaut": "Kaste 50 x 40 x 30 cm. Cik cm² ir augšas laukums?",
                 "atb": ["2000"], "padoms": "50 · 40."},
                {"jaut": "Cik cm² ir visu sešu skaldņu laukums?",
                 "atb": ["9400"], "padoms": "2 · (2000 + 1500 + 1200)."},
                {"jaut": "Cik cm² ir jānokrāso, ja apakšu nekrāso?",
                 "atb": ["7400"], "padoms": "9400 − 2000."},
                {"jaut": "Viena krāsas bundža pietiek 5000 cm². Cik bundžu "
                         "vajag?",
                 "atb": ["2"], "padoms": "7400 : 5000 - vajag divas."},
            ]),
            pavediens="maja",
            konteksts="Krāsas patēriņu rēķina pēc virsmas laukuma, nevis pēc "
                      "priekšmeta lieluma.",
            kapec="Viena skaldne mazāk maina rezultātu par veselu bundžu."),

    Kopsavilkums([
        "Aprēķinu kvadra virsmas laukumu pēc trim izmēriem.",
        "Skaidroju, kāpēc izteiksmē ir divnieks un trīs reizinājumi.",
        "Lietoju īsāko formulu kubam.",
        "Pierakstu atbildi kvadrātvienībās.",
    ]),

    Majas([
        "Izmēri kādu mājas kasti un aprēķini tās virsmas laukumu.",
        "Aprēķini kuba virsmu, ja šķautne ir 10 cm.",
        "Pieraksti, cik reižu tā atšķiras no kuba ar šķautni 5 cm.",
    ]),
]
