# -*- coding: utf-8 -*-
"""6. klase, 152. stunda: «Kā reizina un dala daļskaitļus?»

Mikrotemata noslēgums. Visi likumi jau ir: daļu reizināšana no 6.2. temata,
zīmju likums no šī. Te tie tiek salikti kopā, un vienīgais jaunais solis ir
zīmes noteikšana pirms rēķina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā reizina un dala daļskaitļus?"

MERKIS = ("Reizināsim un dalīsim pozitīvus un negatīvus daļskaitļus.")

SATURS = [
    Sakums("Divi zināmi likumi vienā uzdevumā",
           fakti=["Zīmi nosaka tāpat kā veseliem skaitļiem.",
                  "Daļas reizina un dala tāpat kā 6.2. tematā.",
                  "Decimāldaļām komata likums nemainās."]),

    Doma("Vispirms zīme, tad parastais rēķins",
         "Daļskaitļus ar zīmēm reizina un dala divos soļos: nosaka rezultāta "
         "zīmi un tad veic darbību ar moduļiem pēc zināmajiem likumiem.",
         soli=[
             "Salīdzini zīmes un nosaki rezultāta zīmi.",
             "Turpmāk rēķini tikai ar moduļiem.",
             "Daļām reizini skaitītājus un saucējus vai apgriez dalītāju.",
             "Decimāldaļām saskaiti ciparus aiz komata.",
             "Pieliec rezultātam noteikto zīmi.",
         ],
         pieze="Zīmi nosaka pirmajā solī un pēc tam par to vairs nedomā - "
               "tas ir vienīgais veids, kā garā rēķinā to nepazaudēt."),

    Paraugs("Daļa un decimāldaļa ar zīmēm",
            uzd="Cik ir (−{2|3}) · {3|4} un (−0,6) : (−0,2)?",
            soli=[
                ("Pirmajā: zīmes atšķiras",
                 "Rezultāts negatīvs."),
                ("{2|3} · {3|4} = {6|12} = {1|2}",
                 "Rezultāts −{1|2}."),
                ("Otrajā: zīmes vienādas",
                 "Rezultāts pozitīvs."),
                ("0,6 : 0,2 = 6 : 2 = 3",
                 "Rezultāts 3."),
            ],
            atbilde="−{1|2} un 3"),

    Ievadi("Izrēķini ar zīmēm", [
        {"jaut": "Cik ir (−{2|3}) · {3|4}? Atbildi raksti kā a/b.",
         "atb": ["-1/2", "−1/2", "-6/12"], "padoms": "Dažādas zīmes."},
        {"jaut": "Cik ir (−0,6) : (−0,2)?",
         "atb": ["3"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik ir (−{1|2}) · (−{1|3})? Atbildi raksti kā a/b.",
         "atb": ["1/6"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik ir {3|4} : (−{1|4})?",
         "atb": ["-3", "−3"], "padoms": "Dažādas zīmes; {3|4} · 4."},
        {"jaut": "Cik ir (−2,5) · 4?",
         "atb": ["-10", "−10"], "padoms": "Dažādas zīmes."},
        {"jaut": "Cik ir (−1,2) : 0,4?",
         "atb": ["-3", "−3"], "padoms": "12 : 4, zīme mīnus."},
    ], pamats=4,
        ievads="Vispirms zīme, tikai tad moduļi."),

    Varianti("Kāda būs zīme?", [
        {"jaut": "(−{1|2}) · (−{2|3}). Rezultāta zīme ir...",
         "opcijas": ["pluss", "mīnuss", "nav zīmes", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Vienādas zīmes."},
        {"jaut": "{3|5} : (−{1|5}). Rezultāta zīme ir...",
         "opcijas": ["mīnuss", "pluss", "nav zīmes", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Dažādas zīmes."},
        {"jaut": "(−0,5) · (−0,4) ir...",
         "opcijas": ["0,2", "−0,2", "2", "−2"],
         "pareizi": 0,
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "Kurš solis ir pirmais?",
         "opcijas": ["Zīmes noteikšana", "Saīsināšana",
                     "Kopsaucējs", "Pārbaude"],
         "pareizi": 0,
         "padoms": "Tad zīmi vairs nav jāatceras."},
    ], pamats=4),

    Pasaule("Cik mainās dienā?",
            Ievadi("", [
                {"jaut": "Temperatūra krīt par 1,5 grādiem stundā. Par cik "
                         "grādiem četrās stundās?",
                 "atb": ["-6", "−6"], "padoms": "4 · (−1,5)."},
                {"jaut": "Pēc cik stundām tā nokritīs par 9 grādiem?",
                 "atb": ["6"], "padoms": "(−9) : (−1,5)."},
                {"jaut": "Krājumi sarūk par {1|4} tonnas dienā. Cik tonnu "
                         "sešās dienās? Atbildi raksti kā a/b vai veselu.",
                 "atb": ["-3/2", "−3/2", "-1,5", "−1,5"],
                 "padoms": "6 · (−{1|4})."},
                {"jaut": "Pēc cik dienām sarūk par 2 tonnām?",
                 "atb": ["8"], "padoms": "2 : {1|4}."},
            ]),
            pavediens="planeta",
            konteksts="Vienmērīga izmaiņa dienā ir daļskaitlis ar mīnusu - "
                      "un reizināšana pasaka, cik tas sanāk kopā.",
            kapec="Zīmju likums nemainās no tā, ka skaitlis ir daļa."),

    Kopsavilkums([
        "Reizinu un dalu daļskaitļus ar zīmēm.",
        "Nosaku rezultāta zīmi pirmajā solī.",
        "Tālāk rēķinu tikai ar moduļiem pēc zināmajiem likumiem.",
        "Pārbaudu rezultātu ar pretējo darbību.",
    ]),

    Majas([
        "Izrēķini (−{3|5}) · {5|6}; (−{1|2}) : (−{1|8}); (−0,8) · 0,5.",
        "Katram vispirms pieraksti zīmi.",
        "Pārbaudi vienu no dalījumiem ar reizināšanu.",
    ]),
]
