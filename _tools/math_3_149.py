# -*- coding: utf-8 -*-
"""3. klase, 149. stunda: «Cik gara ir figūras apmale?»

Perimetrs ar lieliem skaitļiem un dažādām malām. Formula te vairs nedarbojas -
malas nav pa pāriem vienādas -, tāpēc jāatgriežas pie definīcijas: perimetrs
ir visu malu summa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Cik gara ir figūras apmale?"

MERKIS = ("Aprēķināsim dažādmalu figūru perimetrus, ja malas ir divciparu un "
          "trīsciparu skaitļi.")

SATURS = [
    Sakums("Cik metru žoga vajag nestandarta laukumam?",
           zimejums=figura([(0, 0), (8, 0), (8, 4), (4, 6), (0, 4)],
                           [(4, -0.7, "120"), (8.8, 2, "85")],
                           "piecstūrveida laukums"),
           paraksts="Visām malām ir savs garums - formula te neder.",
           fakti=["Perimetrs vienmēr ir visu malu summa.",
                  "Formula P = 2 · (a + b) der tikai taisnstūrim."]),

    Doma("Saskaiti visas malas pēc kārtas",
         "Ja malas nav pa pāriem vienādas, perimetru rēķina, saskaitot katru "
         "malu atsevišķi.",
         soli=[
             "Pieraksti visu malu garumus.",
             "Saskaiti tos pēc kārtas, ejot ap figūru.",
             "Neizlaid nevienu malu un neskaiti nevienu divreiz.",
             "Pārbaudi ar aptuveno vērtību.",
         ],
         pieze="Lai neviena mala nepazustu, ej ap figūru vienā virzienā un "
               "atzīmē katru malu, kad to esi saskaitījis."),

    Paraugs("Cik garš ir žogs?",
            uzd="Laukuma malas ir 120 m, 85 m, 96 m un 74 m. Cik metru žoga "
                "vajag?",
            soli=[
                ("120 + 85 = 205",
                 "Pirmās divas malas."),
                ("96 + 74 = 170",
                 "Pārējās divas."),
                ("205 + 170 = 375",
                 "Perimetrs ir 375 m."),
            ],
            atbilde="375 m"),

    Ievadi("Aprēķini perimetru", [
        {"jaut": "Malas 120, 85, 96 un 74 m. Cik ir perimetrs?",
         "atb": ["375"], "padoms": "205 + 170."},
        {"jaut": "Malas 150, 120 un 90 m. Cik ir perimetrs?",
         "atb": ["360"], "padoms": "270 + 90."},
        {"jaut": "Taisnstūris 240 m un 160 m. Cik ir perimetrs?",
         "atb": ["800"], "padoms": "2 · 400."},
        {"jaut": "Kvadrāts ar malu 125 m. Cik ir perimetrs?",
         "atb": ["500"], "padoms": "4 · 125."},
        {"jaut": "Malas 45, 67, 88 un 100 m. Cik ir perimetrs?",
         "atb": ["300"], "padoms": "112 + 188."},
        {"jaut": "Perimetrs 500 m, trīs malas 120, 130 un 150 m. Cik ir "
                 "ceturtā?",
         "atb": ["100"], "padoms": "500 − 400."},
    ], pamats=4),

    Zimejums("Taisnstūris ar lieliem skaitļiem",
             figura([(0, 0), (9, 0), (9, 5), (0, 5)],
                    [(4.5, -0.7, "240 m"), (9.9, 2.5, "160 m")],
                    "P = 2 · (240 + 160)"),
             paskaidro="Taisnstūrim formula joprojām der - un tā ir ātrāka "
                       "nekā četru malu saskaitīšana.",
             ievads="Kad formula der."),

    Varianti("Kurš rēķins der?", [
        {"jaut": "Kurš rēķins der figūrai ar malām 45, 67, 88 un 100?",
         "opcijas": ["45 + 67 + 88 + 100", "2 · (45 + 67)",
                     "4 · 45", "45 · 67"],
         "pareizi": 0, "padoms": "Malas nav pa pāriem vienādas."},
        {"jaut": "Kad der formula P = 2 · (a + b)?",
         "opcijas": ["Taisnstūrim", "Jebkurai figūrai", "Trīsstūrim",
                     "Piecstūrim"],
         "pareizi": 0, "padoms": "Pretējām malām jābūt vienādām."},
        {"jaut": "Kvadrāts ar malu 250 m. Cik ir perimetrs?",
         "opcijas": ["1000 m", "500 m", "750 m", "625 m"],
         "pareizi": 0, "padoms": "4 · 250."},
        {"jaut": "Kā nepazaudēt nevienu malu?",
         "opcijas": ["Ejot ap figūru vienā virzienā", "Skaitot nejauši",
                     "Skaitot divreiz", "Skaitot tikai garās malas"],
         "pareizi": 0, "padoms": "Sistēma neļauj izlaist."},
    ], pamats=4),

    Pasaule("Cik garš ir skolas žogs?",
            Ievadi("", [
                {"jaut": "Skolas laukuma malas 120, 85, 96 un 74 m. Cik ir "
                         "perimetrs?",
                 "atb": ["375"], "padoms": "205 + 170."},
                {"jaut": "Vārti aizņem 5 m. Cik metru žoga vajag?",
                 "atb": ["370"], "padoms": "375 − 5."},
                {"jaut": "Viens žoga posms ir 2 m. Cik posmu vajag?",
                 "atb": ["185"], "padoms": "370 : 2."},
                {"jaut": "Viens posms maksā 20 eiro. Cik eiro maksās žogs?",
                 "atb": ["3700"], "padoms": "185 · 20."},
            ]),
            pavediens="skola",
            konteksts="Skolas laukums reti ir taisnstūrveida - tāpēc žogu "
                      "rēķina pa malām.",
            kapec="Viena aizmirsta mala nozīmē desmitiem metru trūkstoša "
                  "žoga."),

    Kopsavilkums([
        "Aprēķinu dažādmalu figūras perimetru.",
        "Saskaitu visas malas, neizlaižot nevienu.",
        "Zinu, kad der taisnstūra formula.",
        "Atrodu trūkstošo malu, ja zināms perimetrs.",
    ]),

    Majas([
        "Izmēri savas istabas visas malas un izrēķini perimetru.",
        "Uzzīmē piecstūri un izrēķini tā perimetru.",
        "Atrodi mājās figūru, kurai formula neder.",
    ]),
]
