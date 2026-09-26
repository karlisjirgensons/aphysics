# -*- coding: utf-8 -*-
"""3. klase, 3. stunda: «Kā modelēt reizinājumu ar 6?»

Pirmā jaunā rinda tabulā. Reizinājumus ar 6 te neiedod kā sarakstu, ko
iekalt, bet uzbūvē: rūtiņu taisnstūris aug pa vienai rindai, un līdzi aug
rezultāts. Tā rinda paliek atmiņā ar attēlu, nevis tikai ar skaņu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā modelēt reizinājumu ar 6?"

MERKIS = ("Modelēsim reizinājumus ar 6 ar rūtiņu taisnstūri un pierakstīsim "
          "visu sešnieku rindu.")

SATURS = [
    Sakums("Kāpēc bites būvē tieši sešstūrus?",
           zimejums=restis([["", "", "", "", "", ""],
                            ["", "", "", "", "", ""],
                            ["", "", "", "", "", ""],
                            ["", "", "", "", "", ""]],
                           "4 rindas pa 6"),
           paraksts="Katra jauna rinda pieliek vēl 6 rūtiņas.",
           fakti=["Bišu šūnai ir tieši 6 malas - tā vaska paiet vismazāk.",
                  "Sešnieku rinda aug pa 6: 6, 12, 18, 24, ..."]),

    Doma("Katra jauna rinda pieliek vēl sešus",
         "Sešnieku rinda ir kāpnes, kurās katrs pakāpiens ir tieši 6.",
         soli=[
             "Uzzīmē vienu rindu no 6 rūtiņām: 1 · 6 = 6.",
             "Pieliec vēl vienu rindu: rūtiņu ir par 6 vairāk, 2 · 6 = 12.",
             "Katra nākamā rinda atkal pieliek 6.",
             "Pieraksti visu rindu: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60.",
         ],
         pieze="Ja kāds reizinājums izkrīt no galvas, atgriezies pie tuvākā, "
               "ko atceries, un ej pa 6 uz priekšu vai atpakaļ."),

    Slidnis("Sešnieku rinda aug pa vienai rindai",
            soli=[
                {"v": "1 · 6 = 6",
                 "teksts": "Viena rinda no sešām rūtiņām.", "josla": 10},
                {"v": "2 · 6 = 12",
                 "teksts": "Vēl viena rinda - par 6 vairāk.", "josla": 20},
                {"v": "3 · 6 = 18", "teksts": "Trīs rindas.", "josla": 30},
                {"v": "4 · 6 = 24", "teksts": "Četras rindas.", "josla": 40},
                {"v": "5 · 6 = 30", "teksts": "Pusceļš - 30.", "josla": 50},
                {"v": "6 · 6 = 36", "teksts": "Kvadrāts 6 x 6.", "josla": 60},
                {"v": "7 · 6 = 42", "teksts": "Septiņas rindas.", "josla": 70},
                {"v": "8 · 6 = 48", "teksts": "Astoņas rindas.", "josla": 80},
                {"v": "9 · 6 = 54", "teksts": "Deviņas rindas.", "josla": 90},
                {"v": "10 · 6 = 60",
                 "teksts": "Desmit rindas - visa rinda.", "josla": 100},
            ],
            ievads="Spied soļus un skaties, kā aug gan rindu skaits, gan "
                   "rezultāts."),

    Paraugs("Cik rūtiņu ir 7 rindās pa 6?",
            uzd="Taisnstūrim ir 7 rindas, katrā 6 rūtiņas. Cik rūtiņu tajā "
                "ir pavisam?",
            soli=[
                ("6 · 6 = 36",
                 "Sešas rindas ir viegli atcerēties - tas ir kvadrāts."),
                ("36 + 6 = 42",
                 "Septītā rinda pieliek vēl sešas rūtiņas."),
                ("7 · 6 = 42",
                 "Tātad septiņas rindas pa sešām ir 42 rūtiņas."),
            ],
            atbilde="42 rūtiņas"),

    Ievadi("Sešnieku rinda", [
        {"jaut": "3 · 6 = ?", "atb": ["18"], "padoms": "6, 12, 18."},
        {"jaut": "5 · 6 = ?", "atb": ["30"], "padoms": "Puse no 60."},
        {"jaut": "8 · 6 = ?", "atb": ["48"], "padoms": "42 + 6."},
        {"jaut": "6 · 6 = ?", "atb": ["36"], "padoms": "Kvadrāts 6 x 6."},
        {"jaut": "9 · 6 = ?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "4 · 6 = ?", "atb": ["24"], "padoms": "18 + 6."},
    ], pamats=4),

    Varianti("Vai modelis atbilst rēķinam?", [
        {"jaut": "Taisnstūrī ir 6 rindas pa 6. Cik rūtiņu?",
         "opcijas": ["36", "12", "30", "66"],
         "pareizi": 0, "padoms": "6 · 6."},
        {"jaut": "Kurš skaitlis sešnieku rindā ir starp 24 un 36?",
         "opcijas": ["30", "28", "32", "27"],
         "pareizi": 0, "padoms": "24 + 6."},
        {"jaut": "Cik rindu pa 6 rūtiņām vajag, lai sanāktu 54 rūtiņas?",
         "opcijas": ["9", "8", "7", "10"],
         "pareizi": 0, "padoms": "54 : 6."},
        {"jaut": "Kurš skaitlis sešnieku rindā *nav*?",
         "opcijas": ["40", "42", "48", "36"],
         "pareizi": 0, "padoms": "Visi rindas skaitļi dalās ar 6."},
    ], pamats=4),

    Pasaule("Cik kāju rāpo pa lapu?",
            Ievadi("", [
                {"jaut": "Skudrai ir 6 kājas. Cik kāju ir 3 skudrām?",
                 "atb": ["18"], "padoms": "3 · 6."},
                {"jaut": "Cik kāju ir 7 skudrām?",
                 "atb": ["42"], "padoms": "7 · 6."},
                {"jaut": "Uz lapas rāpo 10 skudras. Cik kāju kopā?",
                 "atb": ["60"], "padoms": "10 · 6."},
                {"jaut": "Saskaitīja 48 kājas. Cik skudru tur bija?",
                 "atb": ["8"], "padoms": "48 : 6."},
            ]),
            pavediens="daba",
            konteksts="Visiem kukaiņiem ir tieši 6 kājas - tāpēc dabā "
                      "sešnieku rinda noder ļoti bieži.",
            kapec="Kad zini vienas grupas lielumu, skaitīt pa vienam vairs "
                  "nav vajadzīgs."),

    Kopsavilkums([
        "Modelēju reizinājumus ar 6 ar rūtiņu taisnstūri.",
        "Zinu visu sešnieku rindu no 6 līdz 60.",
        "Zinu, ka katra nākamā rinda pieliek tieši 6.",
        "Atrodu, cik grupu vajag, ja zinu kopskaitu.",
    ]),

    Majas([
        "Uzzīmē rūtiņu lapā taisnstūri 6 rūtiņas platu un 8 augstu un "
        "saskaiti rūtiņas.",
        "Pasaki skaļi visu sešnieku rindu uz priekšu un atpakaļ.",
        "Atrodi mājās sešas vienādas lietas un saskaiti, cik to ir trijās "
        "tādās grupās.",
    ]),
]
