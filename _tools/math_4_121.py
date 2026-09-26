# -*- coding: utf-8 -*-
"""4. klase, 121. stunda: «Kāda daļa no stundas?»

Pulksteņa ciparnīca ir ideāls daļu modelis: stunda ir 60 minūšu, un tās
pamatdaļas - puse (30), ceturtdaļa (15), trešdaļa (20), sestdaļa (10),
divpadsmitā daļa (5) - visas ir veselas minūtes. Tāpēc laiku runā daļās:
«ceturksnis pāri».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis, rinkis)

TEMA = "Kāda daļa no stundas?"

MERKIS = ("Noteiksim pamatdaļu no stundas, izmantojot pulksteņa modeli.")

SATURS = [
    Sakums("Kāpēc saka «ceturksnis pāri»?",
           zimejums=rinkis(sektors=90, virsraksts="15 minūtes",
                           paraksts="1/4 stundas"),
           paraksts="Minūšu rādītājs apgājis ceturtdaļu apļa.",
           fakti=["Stunda - 60 minūtes.",
                  "{1|4} stundas = 60 : 4 = 15 minūtes."]),

    Doma("Daļa no stundas = 60 : saucējs",
         "Pamatdaļu no stundas atrod, dalot 60 minūtes ar saucēju; citas "
         "daļas - reizinot ar skaitītāju.",
         soli=[
             "{1|2} h = 60 : 2 = 30 min.",
             "{1|3} h = 60 : 3 = 20 min.",
             "{1|4} h = 15 min, {1|6} h = 10 min.",
             "{3|4} h = 3 · 15 = 45 min.",
         ],
         pieze="Ciparnīcā 12 skaitļi - katrs ir {1|12} stundas jeb 5 "
               "minūtes."),

    Slidnis("Rādītājs apiet daļas",
            soli=[
                {"v": "{1|12} h = 5 min", "zim": rinkis(sektors=30),
                 "teksts": "Iekrāsots 30° no 360°."},
                {"v": "{1|6} h = 10 min", "zim": rinkis(sektors=60),
                 "teksts": "Iekrāsots 60° no 360°."},
                {"v": "{1|4} h = 15 min", "zim": rinkis(sektors=90),
                 "teksts": "Iekrāsots 90° no 360°."},
                {"v": "{1|3} h = 20 min", "zim": rinkis(sektors=120),
                 "teksts": "Iekrāsots 120° no 360°."},
                {"v": "{1|2} h = 30 min", "zim": rinkis(sektors=180),
                 "teksts": "Iekrāsots 180° no 360°."},
                {"v": "{3|4} h = 45 min", "zim": rinkis(sektors=270),
                 "teksts": "Iekrāsots 270° no 360°."},
            ],
            ievads="Iekrāsotā daļa - cik stundas pagājis."),

    Paraugs("{5|6} stundas",
            uzd="Cik minūšu ir {5|6} stundas?",
            soli=[
                ("{1|6} h = 60 : 6 = 10 min", None),
                ("{5|6} h = 5 · 10 = 50 min", None),
            ],
            atbilde="50 minūtes"),

    Ievadi("Minūtes", [
        {"jaut": "{1|2} h = ? min", "atb": ["30"], "padoms": "60 : 2."},
        {"jaut": "{1|5} h = ? min", "atb": ["12"], "padoms": "60 : 5."},
        {"jaut": "{2|3} h = ? min", "atb": ["40"], "padoms": "2 · 20."},
        {"jaut": "{3|4} h = ? min", "atb": ["45"], "padoms": "3 · 15."},
        {"jaut": "{7|12} h = ? min", "atb": ["35"], "padoms": "7 · 5."},
        {"jaut": "{3|10} h = ? min", "atb": ["18"], "padoms": "3 · 6."},
    ], pamats=4),

    Varianti("Kāda daļa stundas?", [
        {"jaut": "20 min ir ... stundas",
         "opcijas": ["{1|3}", "{1|2}", "{1|4}", "{1|20}"], "pareizi": 0,
         "padoms": "60 : 20 = 3."},
        {"jaut": "10 min ir ... stundas",
         "opcijas": ["{1|6}", "{1|10}", "{1|5}", "{1|4}"], "pareizi": 0,
         "padoms": "60 : 10 = 6."},
        {"jaut": "45 min ir ... stundas",
         "opcijas": ["{3|4}", "{4|5}", "{1|4}", "{2|3}"], "pareizi": 0,
         "padoms": "3 ceturkšņi."},
        {"jaut": "Mācību stunda 40 min. Kāda daļa stundas?",
         "opcijas": ["{2|3}", "{3|4}", "{1|2}", "{4|6}"], "pareizi": 0,
         "padoms": "2 · 20."},
    ], pamats=4),

    Zimejums("Stundas daļu tabula",
             restis([["daļa", "1/2", "1/3", "1/4", "1/5", "1/6", "1/12"],
                     ["min", 30, 20, 15, 12, 10, 5]],
                    "60 minūšu pamatdaļas"),
             paskaidro="60 dalās ar ļoti daudziem skaitļiem - tāpēc stundu "
                       "ērti dalīt.",
             ievads="Iegaumē šo tabulu - tā noder katru dienu."),

    Pasaule("Futbola spēles laiks",
            Ievadi("", [
                {"jaut": "Futbola puslaiks ir 45 min. Kāda daļa stundas? "
                         "Raksti daļu ar saucēju 4.",
                 "atb": ["3/4"], "vieta": "piem., 1/2",
                 "padoms": "45 = 3 · 15."},
                {"jaut": "Hokeja periods - 20 min. Kāda daļa stundas?",
                 "atb": ["1/3"], "vieta": "piem., 1/2",
                 "padoms": "60 : 20 = 3."},
                {"jaut": "Basketbola ceturtdaļa - 10 min. Kāda daļa stundas?",
                 "atb": ["1/6"], "vieta": "piem., 1/2",
                 "padoms": "60 : 10 = 6."},
                {"jaut": "Cik minūšu ir 3 hokeja periodi?", "atb": ["60"],
                 "padoms": "3 · 20 = veselā stunda."},
            ]),
            pavediens="sports",
            konteksts="Katrs sporta veids spēles laiku dala savās daļās - "
                      "puslaikos, periodos, ceturtdaļās.",
            kapec="Stunda ir veselais, ko sports dala visdažādāk."),

    Kopsavilkums([
        "Nosaku daļu no stundas minūtēs.",
        "Nosaku, kāda daļa stundas ir dotās minūtes.",
        "Lietoju pulksteņa modeli.",
    ]),

    Majas([
        "Pieraksti, kāda daļa stundas aizņem tava ceļš uz skolu.",
        "Atrodi 3 TV raidījumu garumus un izsaki tos stundas daļās.",
        "Iemāci mājiniekam: cik minūšu ir {5|12} stundas?",
    ]),
]
