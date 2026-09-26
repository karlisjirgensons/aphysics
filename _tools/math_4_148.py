# -*- coding: utf-8 -*-
"""4. klase, 148. stunda: «Kā pieraksta laukuma formulu?»

No rūtiņu skaitīšanas uz formulu: taisnstūrim a rindas pa b rūtiņām, tātad
S = a · b. Burti a un b ir malu garumi, S - laukums. Pirmā ģeometrijas
formula, ko skolēns pats «atklāj» un pieraksta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura, restis)

TEMA = "Kā pieraksta laukuma formulu?"

MERKIS = ("Formulēsim un lietosim taisnstūra laukuma formulu S = a · b.")

SATURS = [
    Sakums("Kāpēc skaitīt, ja var reizināt?",
           zimejums=figura([(0, 0), (7, 0), (7, 4), (0, 4)],
                           uzraksti=[(3.5, -0.5, "a = 7"),
                                     (7.8, 2, "b = 4")],
                           platums=9, augstums=5),
           paraksts="4 rindas pa 7 rūtiņām: 7 · 4 = 28.",
           fakti=["Rūtiņas skaitīt ilgi - reizināt ātri.",
                  "Taisnstūra laukums = garums · platums."]),

    Doma("S = a · b",
         "Taisnstūra laukums S ir tā garuma a un platuma b reizinājums; "
         "abām malām jābūt vienās vienībās.",
         soli=[
             "Izmēri garumu a un platumu b.",
             "Pārbaudi, vai vienības vienādas.",
             "Ievieto formulā: S = a · b.",
             "Atbildei pieliec kvadrātvienību: cm², m².",
         ],
         pieze="Kvadrātam a = b, tāpēc S = a · a."),

    Paraugs("Taisnstūris 8 cm × 5 cm",
            uzd="Aprēķini taisnstūra laukumu, ja a = 8 cm, b = 5 cm.",
            soli=[
                ("S = a · b", "Formula."),
                ("S = 8 · 5", "Vērtības."),
                ("S = 40 cm²", "Atbilde ar vienību."),
            ],
            atbilde="S = 40 cm²"),

    Zimejums("Formula un rūtiņas",
             restis([["a", "b", "S = a · b"],
                     ["7", "4", "28"],
                     ["5", "5", "25"],
                     ["12", "3", "36"]],
                    "aizpildi galvā"),
             paskaidro="Katrai rindai - viens reizinājums.",
             ievads="Formula aizstāj rūtiņu skaitīšanu."),

    Ievadi("Lieto formulu", [
        {"jaut": "a = 9 cm, b = 6 cm. S = ? cm²", "atb": ["54"],
         "padoms": "9 · 6."},
        {"jaut": "a = 12 m, b = 10 m. S = ? m²", "atb": ["120"],
         "padoms": "12 · 10."},
        {"jaut": "Kvadrāts a = 8 dm. S = ? dm²", "atb": ["64"],
         "padoms": "8 · 8."},
        {"jaut": "a = 2 m, b = 50 cm. S = ? dm²", "atb": ["100"],
         "padoms": "20 dm · 5 dm."},
        {"jaut": "a = 25 m, b = 4 m. S = ? m²", "atb": ["100"],
         "padoms": "25 · 4."},
        {"jaut": "a = 30 cm, b = 30 cm. S = ? cm²", "atb": ["900"],
         "padoms": "30 · 30."},
    ], pamats=4),

    Varianti("Formula un vienības", [
        {"jaut": "Ko nozīmē S formulā S = a · b?",
         "opcijas": ["laukums", "perimetrs", "mala", "garums"],
         "pareizi": 0, "padoms": "S - laukums."},
        {"jaut": "a = 3 m, b = 40 cm. Ko darīt vispirms?",
         "opcijas": ["pārvērst vienādās vienībās", "sareizināt 3 · 40",
                     "saskaitīt"], "pareizi": 0,
         "padoms": "3 m = 300 cm."},
        {"jaut": "Kāda vienība atbildei, ja malas cm?",
         "opcijas": ["cm²", "cm", "m", "dm"], "pareizi": 0,
         "padoms": "Laukums - kvadrātvienības."},
    ]),

    Pasaule("Basketbola laukums",
            Ievadi("", [
                {"jaut": "Laukums 28 m × 15 m. S = ? m²", "atb": ["420"],
                 "padoms": "28 · 15."},
                {"jaut": "Laukuma grīdas lakošana: 2 € par m². Cik €?",
                 "atb": ["840"], "padoms": "420 · 2."},
                {"jaut": "Volejbola laukums 18 m × 9 m. S = ?", "atb": ["162"],
                 "padoms": "18 · 9."},
                {"jaut": "Par cik m² basketbola laukums lielāks?",
                 "atb": ["258"], "padoms": "420 − 162."},
            ]),
            pavediens="sports",
            konteksts="Sporta laukumu izmēri ir noteikti noteikumos - un "
                      "laukumu aprēķina ar formulu.",
            kapec="Formula strādā jebkuram taisnstūrim."),

    Kopsavilkums([
        "Zinu formulu S = a · b.",
        "Pārvēršu malas vienādās vienībās.",
        "Rakstu laukumu kvadrātvienībās.",
    ]),

    Majas([
        "Aprēķini ar formulu 3 taisnstūrveida virsmu laukumus mājās.",
        "Uzraksti kvadrāta laukuma formulu un aprēķini S, ja a = 11 cm.",
        "Paskaidro, kāpēc S = a · b der jebkuram taisnstūrim.",
    ]),
]
