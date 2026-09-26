# -*- coding: utf-8 -*-
"""2. klase, 29. stunda: «Rindā vai stabiņā?»

Vienu darbību var pierakstīt rindā (14 + 5 = 19) un stabiņā - vieni zem
vieniem, desmiti zem desmitiem. Stabiņš šodien ir vienkāršs, bet tas ir
sagatavošana divciparu skaitļu rēķiniem, kuros to lietos visu laiku.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, stabins)

TEMA = "Rindā vai stabiņā?"

MERKIS = ("Šodien pierakstīsim saskaitīšanu un atņemšanu gan rindā, gan "
          "stabiņā un sapratīsim, kāpēc stabiņā cipari stāv viens zem otra.")

SATURS = [
    Sakums("Kāpēc veikala čekā cenas raksta vienu zem otras?",
           zimejums=stabins(14, 5),
           paraksts="14 + 5 = 19 stabiņā.",
           fakti=["Stabiņā vieni stāv zem vieniem.",
                  "Desmiti stāv zem desmitiem.",
                  "Tā garas summas nesajūk."]),

    Doma("Pieraksts stabiņā",
         "Cipari stāv tā, lai vieni būtu zem vieniem un desmiti zem desmitiem.",
         soli=[
             "Uzraksti pirmo skaitli.",
             "Zem tā - otro, pēdējo ciparu zem pēdējā.",
             "Pa kreisi zīme «+» vai «−», zem skaitļiem - svītra.",
             "Rēķini no labās: vispirms vienus, tad desmitus.",
         ]),

    Slidnis("No rindas uz stabiņu", [
        {"v": "13 + 6", "teksts": "Uzdevums rindā.",
         "zim": stabins(13, 6, rezultats=False)},
        {"v": "3 + 6 = 9", "teksts": "Vieni ar vieniem.",
         "zim": stabins(13, 6, rezultats=False)},
        {"v": "19", "teksts": "Desmits paliek - atbilde 19.",
         "zim": stabins(13, 6)},
    ]),

    Ievadi("Izrēķini stabiņā", [
        {"jaut": "Cik ir rezultāts?", "zim": stabins(12, 7, rezultats=False),
         "atb": ["19"], "padoms": "2 + 7 = 9."},
        {"jaut": "Cik ir rezultāts?",
         "zim": stabins(18, 5, "-", rezultats=False), "atb": ["13"],
         "padoms": "8 − 5 = 3."},
        {"jaut": "Cik ir rezultāts?", "zim": stabins(11, 8, rezultats=False),
         "atb": ["19"], "padoms": "1 + 8 = 9."},
        {"jaut": "Cik ir rezultāts?",
         "zim": stabins(17, 4, "-", rezultats=False), "atb": ["13"],
         "padoms": "7 − 4 = 3."},
        {"jaut": "Cik ir rezultāts?", "zim": stabins(15, 4, rezultats=False),
         "atb": ["19"], "padoms": "5 + 4."},
        {"jaut": "Cik ir rezultāts?",
         "zim": stabins(19, 6, "-", rezultats=False), "atb": ["13"],
         "padoms": "9 − 6."},
    ], pamats=4),

    Varianti("Kurš pieraksts pareizs?", [
        {"jaut": "Kā pareizi uzrakstīt 16 + 3 stabiņā?",
         "opcijas": ["3 zem 6", "3 zem 1", "3 pa kreisi no 1"],
         "pareizi": 0, "padoms": "Vieni zem vieniem."},
        {"jaut": "No kuras puses sāk rēķināt stabiņā?",
         "opcijas": ["no labās - ar vieniem", "no kreisās - ar desmitiem",
                     "vienalga"], "pareizi": 0,
         "padoms": "Vispirms vieni."},
    ]),

    Pasaule("Čeks no veikala",
            Ievadi("", [
                {"jaut": "Āboli maksāja 13 €, medus - 6 €. Cik kopā?", "atb": ["19"],
                 "mers": "€", "padoms": "13 + 6 stabiņā."},
                {"jaut": "Samaksāja ar 20 €. Cik atdeva atpakaļ?",
                 "atb": ["1"], "mers": "€", "padoms": "20 − 19."},
            ]),
            pavediens="veikals",
            konteksts="Tirgū mamma pirka ābolu kasti un medu.",
            kapec="Čekā cenas stāv stabiņā - tās saskaita tāpat."),

    Kopsavilkums([
        "Pierakstu darbību rindā un stabiņā.",
        "Stabiņā lieku vienus zem vieniem.",
        "Rēķinu no labās puses.",
    ]),

    Majas([
        "Atrodi mājās veikala čeku un apskati, kā stāv cenas.",
        "Pieraksti stabiņā: 14 + 5, 16 + 2, 19 − 7.",
        "Izrēķini un pārbaudi rindā.",
    ]),
]
