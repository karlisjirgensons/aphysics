# -*- coding: utf-8 -*-
"""3. klase, 90. stunda: «Puse vai trešdaļa?»

Grūtākais salīdzinājums: skaitītāji vienādi, saucēji dažādi. Te intuīcija
maldina - liekas, ka lielāks skaitlis dod lielāku daļu. Modelis to atspēko
uzreiz: jo vairāk daļu, jo mazāka katra.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         dala)

TEMA = "Puse vai trešdaļa?"

MERKIS = ("Salīdzināsim pamatdaļas ar dažādiem saucējiem un skaidrosim, "
          "kāpēc lielāks saucējs dod mazāku daļu.")

SATURS = [
    Sakums("Kurš saņems vairāk - tas, kas dala uz divi, vai tas, kas uz trīs?",
           zimejums=dala(2, 1, "1/2", "puse"),
           paraksts="Jo vairāk cilvēku dala, jo mazāk tiek katram.",
           fakti=["Vienu kūku sadalot 2 daļās, katrs gabals ir liels.",
                  "To pašu kūku sadalot 8 daļās, gabali ir mazi.",
                  "Tāpēc {1|2} > {1|8}."]),

    Doma("Jo lielāks saucējs, jo mazāka daļa",
         "Veselais paliek tas pats, tāpēc, palielinot daļu skaitu, katra daļa "
         "kļūst mazāka.",
         soli=[
             "Pārbaudi, vai skaitītāji ir vienādi.",
             "Salīdzini saucējus.",
             "Lielāks saucējs nozīmē mazāku daļu.",
             "Pieraksti salīdzinājumu ar «<» vai «>».",
         ],
         pieze="Tas ir tieši pretēji veseliem skaitļiem, un tāpēc to jauc: "
               "8 > 2, bet {1|8} < {1|2}."),

    Slidnis("Viena daļa sarūk",
            soli=[
                {"v": "{1|2}", "teksts": "Puse - liels gabals.", "josla": 50},
                {"v": "{1|3}", "teksts": "Trešdaļa - mazāka.", "josla": 33},
                {"v": "{1|4}", "teksts": "Ceturtdaļa - vēl mazāka.",
                 "josla": 25},
                {"v": "{1|8}", "teksts": "Astotdaļa - pavisam maza.",
                 "josla": 12},
            ],
            ievads="Skaitītājs visu laiku ir 1, mainās tikai saucējs."),

    Paraugs("Kura daļa ir lielāka?",
            uzd="Salīdzini {1|3} un {1|5}.",
            soli=[
                ("Skaitītāji ir vienādi - 1",
                 "Abās daļās ņemta viena daļa."),
                ("3 < 5, tātad daļu ir mazāk",
                 "Trijās daļās sadalot, katra daļa ir lielāka."),
                ("{1|3} > {1|5}",
                 "Trešdaļa ir lielāka par piektdaļu."),
            ],
            atbilde="{1|3} ir lielāka"),

    Ievadi("Kura daļa ir lielāka?", [
        {"jaut": "Kura daļa ir lielāka: {1|3} vai {1|5}? Ieraksti saucēju.",
         "atb": ["3"], "padoms": "Mazāks saucējs - lielāka daļa."},
        {"jaut": "Kura daļa ir lielāka: {1|4} vai {1|10}? Ieraksti saucēju.",
         "atb": ["4"], "padoms": "4 < 10."},
        {"jaut": "Kura daļa ir mazāka: {1|6} vai {1|2}? Ieraksti saucēju.",
         "atb": ["6"], "padoms": "Lielāks saucējs - mazāka daļa."},
        {"jaut": "Cik gramu ir {1|2} no 60 g?", "atb": ["30"],
         "padoms": "60 : 2."},
        {"jaut": "Cik gramu ir {1|3} no 60 g?", "atb": ["20"],
         "padoms": "60 : 3."},
        {"jaut": "Cik gramu ir {1|6} no 60 g?", "atb": ["10"],
         "padoms": "60 : 6."},
    ], pamats=4),

    Zimejums("Trešdaļa",
             dala(3, 1, "1/3", "trīs vienādas daļas"),
             paskaidro="Salīdzini ar stundas sākuma zīmējumu: trešdaļa ir "
                       "īsāka par pusi.",
             ievads="Tā izskatās {1|3}."),

    Varianti("Kura ir lielāka?", [
        {"jaut": "Kura daļa ir lielāka?",
         "opcijas": ["{1|2}", "{1|4}", "{1|8}", "{1|10}"],
         "pareizi": 0, "padoms": "Mazākais saucējs."},
        {"jaut": "Kāpēc {1|8} ir mazāks par {1|4}?",
         "opcijas": ["Jo daļu ir vairāk, tāpēc katra mazāka",
                     "Jo 8 ir lielāks skaitlis",
                     "Jo skaitītājs ir mazāks",
                     "Tas nav mazāks"],
         "pareizi": 0, "padoms": "Veselais taču paliek tas pats."},
        {"jaut": "Sakārto no lielākās uz mazāko: {1|5}, {1|2}, {1|10}.",
         "opcijas": ["{1|2}, {1|5}, {1|10}", "{1|10}, {1|5}, {1|2}",
                     "{1|5}, {1|2}, {1|10}", "{1|2}, {1|10}, {1|5}"],
         "pareizi": 0, "padoms": "Mazāks saucējs - lielāka daļa."},
        {"jaut": "Kura daļa ir vismazākā?",
         "opcijas": ["{1|12}", "{1|3}", "{1|6}", "{1|2}"],
         "pareizi": 0, "padoms": "Lielākais saucējs."},
    ], pamats=4),

    Pasaule("Cik tiek katram dzīvniekam?",
            Ievadi("", [
                {"jaut": "12 ogas sadala 2 putniem. Cik ogu saņem katrs?",
                 "atb": ["6"], "padoms": "12 : 2."},
                {"jaut": "Tās pašas 12 ogas sadala 4 putniem. Cik saņem "
                         "katrs?",
                 "atb": ["3"], "padoms": "12 : 4."},
                {"jaut": "Tās pašas 12 ogas sadala 6 putniem. Cik saņem "
                         "katrs?",
                 "atb": ["2"], "padoms": "12 : 6."},
                {"jaut": "Par cik ogām mazāk saņem katrs, ja putnu vietā 2 "
                         "ir 6?",
                 "atb": ["4"], "padoms": "6 − 2."},
            ]),
            pavediens="daba",
            konteksts="Jo vairāk putnu pie barotavas, jo mazāk barības tiek "
                      "katram - lai gan barības daudzums nemainās.",
            kapec="Tieši tāpēc lielāks saucējs dod mazāku daļu."),

    Kopsavilkums([
        "Salīdzinu pamatdaļas ar dažādiem saucējiem.",
        "Zinu, ka lielāks saucējs dod mazāku daļu.",
        "Pamatoju to ar modeli un ar dalīšanu.",
        "Sakārtoju daļas augošā un dilstošā secībā.",
    ]),

    Majas([
        "Salīdzini {1|3} un {1|4}, uzzīmējot abas vienāda garuma joslās.",
        "Sakārto {1|2}, {1|6}, {1|3} no lielākās uz mazāko.",
        "Sadali ābolu vispirms 2, tad 4 daļās un salīdzini gabalus.",
    ]),
]
