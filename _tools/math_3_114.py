# -*- coding: utf-8 -*-
"""3. klase, 114. stunda: «Kā aprēķināt, nenoklājot visu?»

No skaitīšanas uz reizināšanu. Ja rindas ir vienādas, pietiek zināt vienas
rindas rūtiņu skaitu un rindu skaitu - pārējo izdara reizināšana. Tā ir tā
pati doma, kas 3.1. tematā, tikai tagad ģeometrijā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā aprēķināt, nenoklājot visu?"

MERKIS = ("Saskatīsim, ka laukumu var iegūt, rindas rūtiņu skaitu reizinot "
          "ar rindu skaitu.")

SATURS = [
    Sakums("Vai visas rūtiņas tiešām jāsaskaita?",
           zimejums=restis([["", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", ""]],
                           "4 rindas pa 7"),
           paraksts="Pietiek saskaitīt vienu rindu un rindu skaitu.",
           fakti=["Ja rindas ir vienādas, laukumu var reizināt.",
                  "4 rindas pa 7 rūtiņām ir 4 · 7 = 28 rūtiņas."]),

    Doma("Laukums ir rindu skaits reiz rūtiņas rindā",
         "Ja visas rindas ir vienādas, laukumu iegūst ar vienu reizināšanu.",
         soli=[
             "Saskaiti rūtiņas vienā rindā.",
             "Saskaiti rindas.",
             "Reizini abus skaitļus.",
             "Pārbaudi ar skaitīšanu vienā malā.",
         ],
         pieze="Tas strādā tikai taisnstūrim: tur visas rindas ir vienāda "
               "garuma. Neregulārai figūrai rūtiņas jāskaita."),

    Slidnis("Kā aug laukums",
            soli=[
                {"v": "1 rinda pa 7 = 7", "teksts": "Viena rinda.",
                 "josla": 25},
                {"v": "2 rindas = 14", "teksts": "Divas rindas.",
                 "josla": 50},
                {"v": "3 rindas = 21", "teksts": "Trīs rindas.",
                 "josla": 75},
                {"v": "4 rindas = 28", "teksts": "Četras rindas.",
                 "josla": 100},
            ],
            ievads="Katra rinda pieliek vēl 7 rūtiņas."),

    Paraugs("Cik rūtiņu ir 4 rindās pa 7?",
            uzd="Taisnstūris ir 7 rūtiņas plats un 4 augsts. Cik rūtiņu tajā "
                "ir?",
            soli=[
                ("Vienā rindā 7 rūtiņas",
                 "Saskaita tikai vienu rindu."),
                ("Rindu ir 4",
                 "Saskaita rindas."),
                ("4 · 7 = 28",
                 "Laukums ir 28 rūtiņas."),
            ],
            atbilde="28 rūtiņas"),

    Ievadi("Aprēķini laukumu", [
        {"jaut": "Taisnstūris 7 x 4 rūtiņas. Cik ir laukums?", "atb": ["28"],
         "padoms": "4 · 7."},
        {"jaut": "Taisnstūris 9 x 6 rūtiņas. Cik ir laukums?", "atb": ["54"],
         "padoms": "9 · 6."},
        {"jaut": "Kvadrāts 8 x 8 rūtiņas. Cik ir laukums?", "atb": ["64"],
         "padoms": "8 · 8."},
        {"jaut": "Laukums 42 rūtiņas, platums 6. Cik ir augstums?",
         "atb": ["7"], "padoms": "42 : 6."},
        {"jaut": "Laukums 36 rūtiņas, augstums 4. Cik ir platums?",
         "atb": ["9"], "padoms": "36 : 4."},
        {"jaut": "Taisnstūris 12 x 5 rūtiņas. Cik ir laukums?",
         "atb": ["60"], "padoms": "12 · 5."},
    ], pamats=4),

    Zimejums("Laukums un perimetrs blakus",
             restis([["figūra", "laukums", "perimetrs"],
                     ["7 x 4", 28, 22],
                     ["9 x 6", 54, 30]],
                    "divi dažādi lielumi"),
             paskaidro="Laukumu iegūst ar reizināšanu, perimetru - ar "
                       "saskaitīšanu.",
             ievads="Vienai figūrai divi mērījumi."),

    Varianti("Kurš rēķins der?", [
        {"jaut": "Kurš rēķins dod taisnstūra 6 x 5 laukumu?",
         "opcijas": ["6 · 5", "2 · (6 + 5)", "6 + 5", "6 − 5"],
         "pareizi": 0, "padoms": "Rindas reiz rūtiņas rindā."},
        {"jaut": "Kurš rēķins dod to pašu perimetru?",
         "opcijas": ["2 · (6 + 5)", "6 · 5", "6 + 5", "5 · 5"],
         "pareizi": 0, "padoms": "Perimetrs ir apmale."},
        {"jaut": "Kad laukumu var reizināt?",
         "opcijas": ["Kad visas rindas ir vienādas", "Vienmēr",
                     "Kad figūra ir maza", "Nekad"],
         "pareizi": 0, "padoms": "Taisnstūrim."},
        {"jaut": "Laukums 45 rūtiņas, platums 9. Cik ir augstums?",
         "opcijas": ["5", "9", "36", "54"],
         "pareizi": 0, "padoms": "45 : 9."},
    ], pamats=4),

    Pasaule("Cik tapetes vajag sienai?",
            Ievadi("", [
                {"jaut": "Siena ir 4 m plata un 3 m augsta. Cik "
                         "kvadrātmetru ir laukums?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Otra siena ir 5 m plata un 3 m augsta. Cik "
                         "kvadrātmetru?",
                 "atb": ["15"], "padoms": "5 · 3."},
                {"jaut": "Cik kvadrātmetru ir abām sienām kopā?",
                 "atb": ["27"], "padoms": "12 + 15."},
                {"jaut": "Viena tapešu rulle noklāj 5 m². Cik ruļļu vajag?",
                 "atb": ["6"], "padoms": "27 : 5 = 5 un atlikums."},
            ]),
            pavediens="maja",
            konteksts="Tapetes pērk pēc sienas laukuma - un laukumu rēķina "
                      "tieši tā: platums reiz augstums.",
            kapec="Ja laukumu izrēķina nepareizi, tapetes vai nepietiek, vai "
                  "paliek pāri."),

    Kopsavilkums([
        "Aprēķinu laukumu, reizinot rindu skaitu ar rūtiņām rindā.",
        "Atrodu trūkstošo malu, ja zināms laukums.",
        "Atšķiru laukuma un perimetra rēķinu.",
        "Zinu, ka reizināt var tikai vienādas rindas.",
    ]),

    Majas([
        "Izmēri savas istabas garumu un platumu un izrēķini laukumu.",
        "Izrēķini arī perimetru un salīdzini abus skaitļus.",
        "Atrodi mājās sienu, kuras laukums ir apmēram 10 m².",
    ]),
]
