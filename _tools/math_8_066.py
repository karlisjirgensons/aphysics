# -*- coding: utf-8 -*-
"""8. klase, 66. stunda: «Kā aprēķināt taisnleņķa trijstūra laukumu?»

Taisnleņķa trijstūrī katetes ir viena otras augstumi, tāpēc S = {a · b|2}.
Zīmējumā diagonāle sadala taisnstūri 6 × 4 divos vienādos trijstūros.
Ar laukumu atrod arī augstumu pret hipotenūzu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā aprēķināt taisnleņķa trijstūra laukumu?"

MERKIS = "Aprēķināsim taisnleņķa trijstūra laukumu, lietojot katetes."

SATURS = [
    Sakums("Kāpēc pietiek ar katetēm?",
           zimejums=geometrija([("A", 0, 0), ("B", 6, 0), ("C", 0, 4),
                                ("D", 6, 4)],
                               nogriezni=["AB", "AC", "BC", "BD", "CD"],
                               taisni=["BAC"], iekrasot=[("ABC", 0)],
                               malas=[("AB", "6 cm"), ("AC", "4 cm")]),
           paraksts="Diagonāle sadala taisnstūri 6 × 4 divos vienādos "
                    "trijstūros: S = 12 cm².",
           fakti=["Katetes ir viena otras augstumi.",
                  "S = {a · b|2}, kur a un b - katetes.",
                  "Hipotenūza šai formulai nav vajadzīga."]),

    Doma("Taisnleņķa trijstūra laukums",
         "Laukums ir puse no katešu reizinājuma.",
         soli=[
             "Atrodi taisno leņķi - tam blakus ir katetes.",
             "Sareizini katetes un dali ar 2.",
             "Ja zināma hipotenūza c un augstums pret to: S = {c · h|2}.",
         ],
         pieze="Abas formulas dod vienu laukumu, tāpēc no tām atrod augstumu "
               "pret hipotenūzu: h = {a · b|c}."),

    Paraugs("Laukums un augstums",
            uzd="Katetes ir 9 cm un 12 cm, hipotenūza - 15 cm. Aprēķini "
                "laukumu un augstumu pret hipotenūzu.",
            soli=[
                ("S = {9 · 12|2} = 54 cm²", "Katetes."),
                ("{15 · h|2} = 54", "Tas pats laukums ar hipotenūzu."),
                ("h = {108|15} = 7,2 cm", "Atrisina."),
            ],
            atbilde="54 cm² un 7,2 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Katetes 5 cm un 8 cm. S (cm²)?", "atb": ["20"],
         "padoms": "{40|2}."},
        {"jaut": "Katetes 1,2 m un 3 m. S (m²)?", "atb": ["1,8"],
         "padoms": "{3,6|2}."},
        {"jaut": "S = 24 cm², viena katete 6 cm. Otra katete (cm)?",
         "atb": ["8"], "padoms": "{6 · b|2} = 24."},
        {"jaut": "Katetes 6 un 8, hipotenūza 10. Augstums pret hipotenūzu?",
         "atb": ["4,8"], "padoms": "{48|10}."},
        {"jaut": "Vienādsānu taisnleņķa trijstūra katete 10 cm. S (cm²)?",
         "atb": ["50"], "padoms": "{10 · 10|2}."},
    ]),

    Varianti("Izvēlies", [
        {"jaut": "Kuras malas reizina?",
         "opcijas": ["Abas katetes", "Kateti un hipotenūzu", "Visas trīs",
                     "Hipotenūzu ar sevi"],
         "pareizi": 0, "padoms": "Tās ir perpendikulāras."},
        {"jaut": "Kvadrātu ar malu 6 sadala pa diagonāli. Viena trijstūra "
                 "laukums?",
         "opcijas": ["18", "36", "12", "9"],
         "pareizi": 0, "padoms": "{36|2}."},
        {"jaut": "Katetes 3 un 4, hipotenūza 5. Laukums?",
         "opcijas": ["6", "10", "7,5", "12"],
         "pareizi": 0, "padoms": "{3 · 4|2}."},
    ]),

    Pasaule("Stūra plaukts",
            Ievadi("", [
                {"jaut": "Stūra plaukts ir taisnleņķa trijstūris ar katetēm "
                         "40 cm un 40 cm. Laukums (cm²)?",
                 "atb": ["800"], "padoms": "{40 · 40|2}."},
                {"jaut": "Cik dm² tas ir?", "atb": ["8"],
                 "padoms": "1 dm² = 100 cm²."},
                {"jaut": "Cik plauktu iznāk no plāksnes 80 cm × 40 cm?",
                 "atb": ["4"], "padoms": "Divi kvadrāti 40 × 40, katru "
                                         "sadala uz pusēm."},
            ]),
            pavediens="maja",
            konteksts="Stūra plauktu izzāģē no kvadrāta pa diagonāli - tā "
                      "abas katetes piekļaujas sienām.",
            kapec="Taisnleņķa trijstūra laukumam pietiek ar abām katetēm."),

    Kopsavilkums([
        "Aprēķinu taisnleņķa trijstūra laukumu ar katetēm.",
        "No laukuma atrodu nezināmo kateti.",
        "Aprēķinu augstumu pret hipotenūzu.",
    ]),

    Majas([
        "Izmēri trijstūra lineāla katetes un aprēķini tā laukumu.",
        "Katetes 7 cm un 24 cm, hipotenūza 25 cm - atrodi augstumu pret "
        "hipotenūzu.",
        "Uzzīmē trīs dažādus taisnleņķa trijstūrus ar laukumu 12 cm².",
    ]),
]
