# -*- coding: utf-8 -*-
"""5. klase, 142. stunda: «Kur dzīvē rēķina ar decimāldaļām?»

Mikrotemata noslēgums, un tas atgriež decimāldaļas turp, no kurienes tās
nāca: čekā un mērlentē. Jaunu paņēmienu te nav, bet ir divas prasības, kas
5. klasē bieži pazūd - mērvienība pie katra skaitļa un novērtējums pirms
atbildes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kur dzīvē rēķina ar decimāldaļām?"

MERKIS = ("Mācīsimies lietot decimāldaļu saskaitīšanu un atņemšanu izdevumu "
          "un perimetra aprēķinos.")

SATURS = [
    Sakums("Čeks un mērlente",
           zimejums=figura([(0, 0), (5, 0), (5, 3), (0, 3)],
                           uzraksti=[(2.5, -0.4, "2,5 m"), (5.9, 1.5,
                                                            "1,8 m")],
                           virsraksts="Istabas plāns"),
           paraksts="Perimetrs ir (2,5 + 1,8) · 2 = 8,6 m.",
           fakti=["Čekā decimāldaļas saskaita.",
                  "Mērlentē tās arī saskaita, tikai metros.",
                  "Abās vietās der viens un tas pats rēķins."]),

    Doma("Mērvienība pie katra skaitļa",
         "Dzīves uzdevumos ar decimāldaļām katram skaitlim pieraksta "
         "mērvienību, bet pirms atbildes rezultātu novērtē.",
         soli=[
             "Izraksti visus dotos skaitļus ar mērvienībām.",
             "Novērtē, kādai atbildei apmēram jāsanāk.",
             "Izpildi darbības kolonnā.",
             "Salīdzini atbildi ar novērtējumu.",
             "Uzraksti atbildi teikumā ar mērvienību.",
         ],
         pieze="Perimetru var rēķināt divējādi: saskaitīt visas četras malas "
               "vai saskaitīt divas blakus malas un reizināt ar 2. Otrais "
               "ceļš ir īsāks un ar decimāldaļām drošāks."),

    Paraugs("Istabas perimetrs",
            uzd="Istabas malas ir 2,5 m un 1,8 m. Cik metru ir perimetrs?",
            soli=[
                ("Novērtējums: 3 + 2 = 5, reiz 2 ir ap 10 m",
                 "Aptuvenā atbilde."),
                ("2,5 + 1,8 = 4,3 (m)",
                 "Divas blakus malas."),
                ("4,3 · 2 = 8,6 (m)",
                 "Visas četras malas."),
                ("8,6 m ir tuvu 10 m",
                 "Novērtējums apstiprina."),
            ],
            atbilde="Perimetrs ir 8,6 m"),

    Ievadi("Rēķini ar mērvienībām", [
        {"jaut": "2,5 m + 1,8 m = ? Ieraksti skaitli metros.",
         "atb": ["4,3"], "padoms": "Saskaiti desmitdaļas."},
        {"jaut": "Cik metru ir perimetrs taisnstūrim ar malām 2,5 m un "
                 "1,8 m?",
         "atb": ["8,6"], "padoms": "4,3 · 2."},
        {"jaut": "Pirkumi 3,45 € un 2,8 €. Cik eiro kopā?",
         "atb": ["6,25"], "padoms": "3,45 + 2,80."},
        {"jaut": "Bija 10 €, iztērēti 6,25 €. Cik eiro palika?",
         "atb": ["3,75"], "padoms": "10,00 - 6,25."},
        {"jaut": "Malas 1,2 m un 0,8 m. Cik metru ir perimetrs?",
         "atb": ["4"], "padoms": "(1,2 + 0,8) · 2."},
        {"jaut": "Malas 3,5 m un 2,5 m. Cik metru ir perimetrs?",
         "atb": ["12"], "padoms": "6 · 2."},
        {"jaut": "Trīs pirkumi: 1,5 €, 2,35 € un 0,9 €. Cik eiro kopā?",
         "atb": ["4,75"], "padoms": "1,50 + 2,35 + 0,90."},
        {"jaut": "Bija 20 €, iztērēti 4,75 €. Cik eiro palika?",
         "atb": ["15,25"], "padoms": "20,00 - 4,75."},
    ], pamats=4,
        ievads="Katram skaitlim mērvienība, katrai atbildei novērtējums."),

    Zimejums("Divas malas pietiek",
             figura([(0, 0), (5, 0), (5, 3), (0, 3)],
                    uzraksti=[(2.5, -0.4, "2,5 m"), (5.9, 1.5, "1,8 m")],
                    virsraksts="Pretējās malas ir vienādas"),
             paskaidro="Taisnstūrim pretējās malas ir vienādas, tāpēc pietiek "
                       "izmērīt divas un summu reizināt ar 2.",
             ievads="Perimetru rēķina no divām malām."),

    Varianti("Kāds rēķins te vajadzīgs?", [
        {"jaut": "Kā rēķina taisnstūra perimetru?",
         "opcijas": ["(a + b) · 2", "a · b", "a + b", "(a + b) : 2"],
         "pareizi": 0,
         "padoms": "Četras malas, divas dažādas."},
        {"jaut": "Malas 2,5 m un 1,8 m. Cik ir perimetrs?",
         "opcijas": ["8,6 m", "4,3 m", "4,5 m", "17,2 m"],
         "pareizi": 0,
         "padoms": "4,3 · 2."},
        {"jaut": "Kas jāpieraksta pie katra skaitļa?",
         "opcijas": ["Mērvienība", "Komats", "Nulle", "Nekas"],
         "pareizi": 0,
         "padoms": "Eiro, metri, kilogrami."},
        {"jaut": "Bija 10 €, iztērēti 6,25 €. Cik palika?",
         "opcijas": ["3,75 €", "4,75 €", "3,85 €", "16,25 €"],
         "pareizi": 0,
         "padoms": "10,00 - 6,25."},
        {"jaut": "Ko dara pirms atbildes?",
         "opcijas": ["Salīdzina ar novērtējumu", "Saīsina",
                     "Noapaļo atbildi", "Neko"],
         "pareizi": 0,
         "padoms": "Pārbaude pret aptuveno vērtību."},
        {"jaut": "Kāpēc perimetru rēķina no divām malām?",
         "opcijas": ["Pretējās malas ir vienādas", "Tā ir ātrāk rakstīt",
                     "Pārējās nav zināmas", "Tas nav pareizi"],
         "pareizi": 0,
         "padoms": "Taisnstūra īpašība."},
    ], pamats=4),

    Pasaule("Cik maksās apmale?",
            Ievadi("", [
                {"jaut": "Istaba 4,2 m x 3,5 m. Cik metru ir perimetrs?",
                 "atb": ["15,4"], "padoms": "(4,2 + 3,5) · 2."},
                {"jaut": "Apmale maksā 2 € par metru. Cik eiro maksās 15,4 m? "
                         "Ieraksti skaitli.",
                 "atb": ["30,8"], "padoms": "15,4 · 2."},
                {"jaut": "Cita istaba 3,5 m x 2,5 m. Cik metru ir perimetrs?",
                 "atb": ["12"], "padoms": "6 · 2."},
                {"jaut": "Bija 50 €, apmale maksāja 30,8 €. Cik eiro palika?",
                 "atb": ["19,2"], "padoms": "50,0 - 30,8."},
            ]),
            pavediens="maja",
            konteksts="Remontā viss sākas ar mērlenti un beidzas ar čeku - "
                      "un abās vietās skaitļi ir ar komatu.",
            kapec="Viena prasme der gan garumiem, gan naudai."),

    Kopsavilkums([
        "Lietoju decimāldaļu saskaitīšanu izdevumu aprēķinos.",
        "Aprēķinu perimetru ar decimāldaļām.",
        "Pierakstu mērvienību pie katra skaitļa.",
        "Novērtēju atbildi, pirms to pierakstu.",
    ]),

    Majas([
        "Izmēri savas istabas malas un aprēķini perimetru.",
        "Saskaiti trīs pēdējos pirkumus no čeka.",
        "Pārbaudi abas atbildes ar novērtējumu.",
    ]),
]
