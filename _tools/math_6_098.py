# -*- coding: utf-8 -*-
"""6. klase, 98. stunda: «Kur dzīvē satiekam skaitļus zem nulles?»

Jauns temats. Negatīvs skaitlis nav «mazāk par neko» - tas ir virziens no
izvēlētās nulles. Stunda sāk ar vietām, kur skolēns tos jau ir redzējis, un
ar galveno jautājumu: kur katrā gadījumā ir nulle?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kur dzīvē satiekam skaitļus zem nulles?"

MERKIS = ("Minēsim piemērus lielumiem, ko raksturo negatīvi skaitļi, un "
          "skaidrosim to nozīmi.")

SATURS = [
    Sakums("Kosmosā ir −270 grādi",
           zimejums=taisne(-30, 30, 10, [(-17, "rīts"), (5, "diena")]),
           paraksts="Termometrs ir skaitļu taisne, kas nolikta gulus: pa "
                    "kreisi no nulles ir sals.",
           fakti=["Visaukstākā vieta Visumā ir apmēram −270 °C.",
                  "Negatīvs skaitlis pasaka virzienu no nulles.",
                  "Katrā situācijā nulli izvēlas cilvēks, ne daba."]),

    Doma("Nulle ir izvēlēta vieta, ne robeža",
         "Negatīvi skaitļi raksturo lielumus, kas var būt abās pusēs no "
         "izvēlētas nulles: temperatūru, augstumu, naudu, laiku.",
         soli=[
             "Nosaki, kas konkrētajā situācijā ir nulle.",
             "Nosaki, kurā virzienā skaitļi aug.",
             "Pretējo virzienu apzīmē ar mīnusa zīmi.",
             "Pieraksti lielumu ar zīmi un mērvienību.",
             "Pārbaudi: vai pretējā zīme maina nozīmi?",
         ],
         pieze="Termometram nulle ir ledus kušanas temperatūra, kartē - "
               "jūras līmenis, kontā - tukšums. Visos gadījumos nulli "
               "izvēlējās cilvēks, un tāpēc tā var būt citur."),

    Paraugs("Pieraksti ar zīmi",
            uzd="Pieraksti ar skaitli: 17 grādi sala; 3 m zem jūras līmeņa; "
                "parāds 20 €.",
            soli=[
                ("Sals: nulle ir ledus kušana",
                 "Zem tās ir mīnuss: −17 °C."),
                ("Zem jūras līmeņa: nulle ir jūras līmenis",
                 "Zemāk ir mīnuss: −3 m."),
                ("Parāds: nulle ir tukšs konts",
                 "Parāds ir mīnuss: −20 €."),
                ("Visos trijos gadījumos nulle ir cita",
                 "Bet mīnusa nozīme ir viena."),
            ],
            atbilde="−17 °C; −3 m; −20 €"),

    Ievadi("Pieraksti ar zīmi", [
        {"jaut": "17 grādi sala. Kā to pieraksta? Raksti skaitli ar zīmi.",
         "atb": ["-17", "−17"], "padoms": "Zem nulles."},
        {"jaut": "5 m zem jūras līmeņa. Kā to pieraksta?",
         "atb": ["-5", "−5"], "padoms": "Zem nulles."},
        {"jaut": "Parāds 30 €. Kā to pieraksta?",
         "atb": ["-30", "−30"], "padoms": "Konts zem nulles."},
        {"jaut": "8 grādi siltuma. Kā to pieraksta?",
         "atb": ["8", "+8"], "padoms": "Virs nulles."},
        {"jaut": "Lifts trešajā pagrabstāvā. Kā to pieraksta?",
         "atb": ["-3", "−3"], "padoms": "Zem pirmā stāva."},
        {"jaut": "Termometrs rāda −12 °C. Cik grādu sala tas ir?",
         "atb": ["12"], "padoms": "Mīnuss pasaka virzienu."},
    ], pamats=4,
        ievads="Vispirms padomā, kur šajā situācijā ir nulle."),

    Varianti("Kur ir nulle?", [
        {"jaut": "Termometram nulle ir...",
         "opcijas": ["ledus kušanas temperatūra", "aukstākā temperatūra",
                     "istabas temperatūra", "gaisa trūkums"],
         "pareizi": 0,
         "padoms": "Tā ir izvēlēta vieta."},
        {"jaut": "Kartē nulle ir...",
         "opcijas": ["jūras līmenis", "zemākā vieta",
                     "kalna virsotne", "ekvators"],
         "pareizi": 0,
         "padoms": "Augstumu mēra no tā."},
        {"jaut": "Ko nozīmē −5 stāvs?",
         "opcijas": ["Piektais pagrabstāvs", "Piektais stāvs",
                     "Nav tāda stāva", "Pirmais stāvs"],
         "pareizi": 0,
         "padoms": "Zem pirmā stāva."},
        {"jaut": "Vai negatīvs skaitlis nozīmē «mazāk par neko»?",
         "opcijas": ["Nē, tas nozīmē virzienu no nulles",
                     "Jā, tas ir mazāk par neko",
                     "Jā, tas ir kļūda", "Tas ir tas pats, kas nulle"],
         "pareizi": 0,
         "padoms": "Nulle ir izvēlēta vieta."},
    ], pamats=4),

    Pasaule("Ko rāda laika ziņas?",
            Ievadi("", [
                {"jaut": "No rīta bija −7 °C, dienā +3 °C. Par cik grādiem "
                         "kļuva siltāks?",
                 "atb": ["10"], "padoms": "No −7 līdz 0 ir 7, tad vēl 3."},
                {"jaut": "Naktī bija −12 °C, no rīta −5 °C. Par cik grādiem "
                         "kļuva siltāks?",
                 "atb": ["7"], "padoms": "Uz taisnes 7 soļi pa labi."},
                {"jaut": "Dienā +4 °C, vakarā −2 °C. Par cik grādiem kļuva "
                         "aukstāks?",
                 "atb": ["6"], "padoms": "No 4 līdz 0 ir 4, tad vēl 2."},
                {"jaut": "Kāda ir starpība starp −17 °C un 5 °C?",
                 "atb": ["22"], "padoms": "17 + 5."},
            ]),
            pavediens="planeta",
            konteksts="Laika ziņās temperatūru salīdzina katru dienu - un "
                      "starpība ir tas, ko cilvēks tiešām jūt.",
            kapec="Attālums uz skaitļu taisnes ir starpība starp skaitļiem."),

    Zimejums("Diena uz skaitļu taisnes",
             taisne(-20, 10, 5, [(-12, "nakts"), (-5, "rīts"), (4, "diena")]),
             paskaidro="Trīs mērījumi vienā dienā. No nakts līdz dienai "
                       "temperatūra pieauga par 16 grādiem.",
             ievads="Uz taisnes visu dienu redz vienā attēlā."),

    Kopsavilkums([
        "Minu piemērus lielumiem ar negatīvām vērtībām.",
        "Nosaku, kur katrā situācijā ir nulle.",
        "Pierakstu lielumu ar zīmi un mērvienību.",
        "Skaidroju, ka mīnuss nozīmē virzienu, ne trūkumu.",
    ]),

    Majas([
        "Atrodi trīs vietas mājās vai ziņās, kur redzami negatīvi skaitļi.",
        "Pieraksti, kur katrā gadījumā ir nulle.",
        "Uzzīmē skaitļu taisni un atzīmē uz tās šodienas temperatūru.",
    ]),
]
