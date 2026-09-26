# -*- coding: utf-8 -*-
"""3. klase, 54. stunda: «Ko nozīmē burti formulā?»

Pirmā formula ar burtiem. Burts te nav noslēpums, bet saīsinājums: a ir
garums, b ir platums, un P = 2 · (a + b) ir tas pats teikums, kas vakar bija
vārdos. Skolēns mācās formulu *lasīt* - pateikt to atpakaļ vārdos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Ko nozīmē burti formulā?"

MERKIS = ("Lasīsim un skaidrosim formulas pierakstu ar burtiem un atradīsim "
          "tam atbilstošo vārdisko formulējumu.")

SATURS = [
    Sakums("Kā vienu teikumu saīsināt līdz sešām zīmēm?",
           zimejums=figura([(0, 0), (7, 0), (7, 4), (0, 4)],
                           [(3.5, -0.6, "a"), (7.8, 2, "b")],
                           "P = 2 · (a + b)"),
           paraksts="a ir garums, b ir platums, P ir perimetrs.",
           fakti=["Burts formulā aizstāj lielumu, nevis konkrētu skaitli.",
                  "P = 2 · (a + b) ir tas pats, ko vakar teicām vārdiem."]),

    Doma("Burts apzīmē lielumu, nevis skaitli",
         "P = 2 · (a + b) lasa tā: perimetrs ir divas reizes garuma un "
         "platuma summa.",
         soli=[
             "Pasaki, ko apzīmē katrs burts.",
             "Izlasi formulu vārdiem, ejot no labās puses uz kreiso.",
             "Ieliec burtu vietā skaitļus.",
             "Aprēķini un pieraksti atbildi ar mērvienību.",
         ],
         pieze="Burtus izvēlas tā, lai tos būtu viegli atcerēties: P ir "
               "perimetrs, a un b - taisnstūra malas. Citos uzdevumos tie "
               "paši burti var nozīmēt ko citu."),

    Paraugs("Kā lietot formulu P = 2 · (a + b)?",
            uzd="Taisnstūrim a = 9 cm un b = 6 cm. Aprēķini P.",
            soli=[
                ("P = 2 · (a + b)",
                 "Vispirms pieraksta formulu."),
                ("P = 2 · (9 + 6)",
                 "Burtu vietā ieliek dotos skaitļus."),
                ("P = 2 · 15 = 30",
                 "Aprēķina vērtību."),
                ("P = 30 cm",
                 "Atbildi raksta ar mērvienību."),
            ],
            atbilde="30 cm"),

    Ievadi("Lieto formulu ar burtiem", [
        {"jaut": "a = 7 cm, b = 5 cm. Cik ir P?", "atb": ["24"],
         "padoms": "2 · 12."},
        {"jaut": "a = 12 cm, b = 3 cm. Cik ir P?", "atb": ["30"],
         "padoms": "2 · 15."},
        {"jaut": "a = 8 cm, b = 8 cm. Cik ir P?", "atb": ["32"],
         "padoms": "2 · 16."},
        {"jaut": "P = 28 cm, a = 9 cm. Cik ir b?", "atb": ["5"],
         "padoms": "28 : 2 = 14; 14 − 9."},
        {"jaut": "a = 15 cm, b = 10 cm. Cik ir P?", "atb": ["50"],
         "padoms": "2 · 25."},
        {"jaut": "P = 40 cm, b = 12 cm. Cik ir a?", "atb": ["8"],
         "padoms": "40 : 2 = 20; 20 − 12."},
    ], pamats=4,
        ievads="Vispirms pieraksti formulu, tad ieliec skaitļus."),

    Zimejums("Formula un tās vārdi",
             figura([(0, 0), (5, 0), (5, 5), (0, 5)],
                    [(2.5, -0.6, "a"), (5.8, 2.5, "a")],
                    "kvadrāts: P = 4 · a"),
             paskaidro="Kvadrātam abas malas ir vienādas, tāpēc formula "
                       "kļūst īsāka: P = 4 · a.",
             ievads="Tā pati doma, tikai īpašam gadījumam."),

    Varianti("Kā izlasīt formulu?", [
        {"jaut": "Ko nozīmē P = 2 · (a + b)?",
         "opcijas": ["Perimetrs ir divas reizes malu summa",
                     "Perimetrs ir divas malas",
                     "Perimetrs ir malu reizinājums",
                     "Perimetrs ir divi plus malas"],
         "pareizi": 0, "padoms": "Iekavas nozīmē «vispirms saskaita»."},
        {"jaut": "Ko nozīmē P = 4 · a?",
         "opcijas": ["Kvadrāta perimetrs ir četras malas",
                     "Kvadrāta laukums", "Četri kvadrāti",
                     "Mala ir četras reizes lielāka"],
         "pareizi": 0, "padoms": "Kvadrātam visas malas vienādas."},
        {"jaut": "Kurš pieraksts *nav* pareizs perimetram?",
         "opcijas": ["P = a · b", "P = 2 · a + 2 · b", "P = 2 · (a + b)",
                     "P = a + b + a + b"],
         "pareizi": 0, "padoms": "Reizinājums dod laukumu, ne perimetru."},
        {"jaut": "Ko formulā apzīmē burts?",
         "opcijas": ["Lielumu", "Vienu konkrētu skaitli", "Mērvienību",
                     "Figūras nosaukumu"],
         "pareizi": 0, "padoms": "Burta vietā var ielikt jebkuru derīgu "
                                 "skaitli."},
    ], pamats=4),

    Pasaule("Cik žoga vajag dārzam?",
            Ievadi("", [
                {"jaut": "Dārzs a = 20 m, b = 15 m. Cik metru ir P?",
                 "atb": ["70"], "padoms": "2 · 35."},
                {"jaut": "Vārti aizņem 3 m. Cik metru žoga vajag?",
                 "atb": ["67"], "padoms": "70 − 3."},
                {"jaut": "Otrs dārzs ir kvadrāts ar malu 18 m. Cik metru ir "
                         "P?",
                 "atb": ["72"], "padoms": "4 · 18."},
                {"jaut": "Par cik metriem garāks ir otrā dārza žogs?",
                 "atb": ["2"], "padoms": "72 − 70."},
            ]),
            pavediens="maja",
            konteksts="Žogu pērk metros, un tā garums ir dārza perimetrs "
                      "mīnus vārti.",
            kapec="Ar formulu vienu un to pašu rēķinu var atkārtot jebkuram "
                  "dārzam."),

    Kopsavilkums([
        "Lasu formulu P = 2 · (a + b) vārdiem.",
        "Zinu, ko apzīmē katrs burts.",
        "Ieliku burtu vietā skaitļus un aprēķinu vērtību.",
        "Zinu kvadrāta formulu P = 4 · a.",
    ]),

    Majas([
        "Uzraksti formulu P = 2 · (a + b) un izskaidro to mājiniekiem.",
        "Izmēri kādu taisnstūrveida priekšmetu un aprēķini P pēc formulas.",
        "Atrodi mājās kvadrātveida priekšmetu un aprēķini tā perimetru.",
    ]),
]
