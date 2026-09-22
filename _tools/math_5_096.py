# -*- coding: utf-8 -*-
"""5. klase, 96. stunda: «Kā aug jauktu skaitļu virkne?»

Mikrotemata noslēgums. Virkne te ir veids, kā pārbaudīt visu iepriekšējo
uzreiz: lai pateiktu nākamo locekli, jāprot saskaitīt daļas un jāzina, kas
notiek, kad daļa pāraug veselo. Tieši tas pāreja - no 1{3|4} uz 2 - arī ir
stundas grūtākā vieta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis, taisne)

TEMA = "Kā aug jauktu skaitļu virkne?"

MERKIS = ("Mācīsimies veidot jauktu skaitļu virkni pēc dota nosacījuma un "
          "turpināt to.")

SATURS = [
    Sakums("Katru reizi par ceturtdaļu vairāk",
           zimejums=restis([["1", "1 1/4", "1 1/2", "1 3/4"]],
                           virsraksts="Solis ir 1/4"),
           paraksts="Nākamais virknes loceklis pēc 1{3|4} ir tieši 2.",
           fakti=["Katrs nākamais skaitlis ir par {1|4} lielāks.",
                  "Pēc četriem soļiem pieaug viens vesels.",
                  "Tieši tad daļa pazūd un veselā daļa aug."]),

    Doma("Solis ir daļa, ne vesels skaitlis",
         "Jauktu skaitļu virknē katram nākamajam loceklim pieskaita vienu un "
         "to pašu daļu; kad daļas savācas līdz veselam, veselā daļa aug par "
         "vienu.",
         soli=[
             "Nosaki virknes soli - par cik katrs nākamais atšķiras.",
             "Pieskaiti soli pēdējam loceklim.",
             "Ja daļa kļūst neīsta, atdali no tās veselo.",
             "Pieraksti jauno locekli kā jauktu skaitli.",
             "Pārbaudi, vai starpība starp blakus locekļiem ir tā pati.",
         ],
         pieze="1{3|4} + {1|4} = 1{4|4} = 2. Pieraksts 1{4|4} nav galīgā "
               "atbilde: {4|4} ir vesels, tāpēc to pieskaita veselajai "
               "daļai."),

    Paraugs("Turpini virkni 1; 1{1|4}; 1{1|2}; ...",
            uzd="Nosaki virknes soli un pieraksti nākamos divus locekļus.",
            soli=[
                ("1{1|4} - 1 = {1|4}",
                 "Solis ir ceturtdaļa."),
                ("1{1|2} = 1{2|4}",
                 "Pārraksta ar to pašu saucēju."),
                ("1{2|4} + {1|4} = 1{3|4}",
                 "Nākamais loceklis."),
                ("1{3|4} + {1|4} = 1{4|4} = 2",
                 "Daļa savācās līdz veselam."),
            ],
            atbilde="Nākamie ir 1{3|4} un 2"),

    Slidnis("Virkne ar soli {1|4}",
            [{"v": "1", "teksts": "sākums", "josla": 25},
             {"v": "1{1|4}", "teksts": "+ {1|4}", "josla": 40},
             {"v": "1{1|2}", "teksts": "+ {1|4}", "josla": 55},
             {"v": "1{3|4}", "teksts": "+ {1|4}", "josla": 70},
             {"v": "2", "teksts": "daļa kļuva par veselu", "josla": 85}],
            ievads="Spied soli pa solim: solis ir viens un tas pats, bet "
                   "reizi pa reizei aug veselā daļa."),

    Ievadi("Nosaki nākamo locekli", [
        {"jaut": "1; 1{1|4}; 1{1|2}; ... Kāds ir solis? Atbildi raksti kā "
                 "a/b.",
         "atb": ["1/4"], "padoms": "Starpība starp blakus locekļiem."},
        {"jaut": "Kāds ir nākamais loceklis pēc 1{1|2}? Atbildi raksti kā "
                 "a b/c.",
         "atb": ["1 3/4"], "padoms": "1{2|4} + {1|4}."},
        {"jaut": "Kāds ir nākamais loceklis pēc 1{3|4}? Ieraksti skaitli.",
         "atb": ["2"], "padoms": "1{4|4} = 2."},
        {"jaut": "2; 2{1|3}; 2{2|3}; ... Kāds ir nākamais? Ieraksti skaitli.",
         "atb": ["3"], "padoms": "2{3|3} = 3."},
        {"jaut": "1{1|2}; 2; 2{1|2}; ... Kāds ir solis? Atbildi raksti kā "
                 "a/b.",
         "atb": ["1/2"], "padoms": "Puse."},
        {"jaut": "Kāds ir nākamais loceklis pēc 2{1|2}? Ieraksti skaitli.",
         "atb": ["3"], "padoms": "2{1|2} + {1|2}."},
        {"jaut": "3; 3{1|5}; 3{2|5}; ... Kāds ir ceturtais loceklis? Atbildi "
                 "raksti kā a b/c.",
         "atb": ["3 3/5"], "padoms": "Solis ir {1|5}."},
        {"jaut": "Cik soļu pa {1|4} vajag, lai no 1 nonāktu līdz 2?",
         "atb": ["4"], "padoms": "Četras ceturtdaļas."},
    ], pamats=4,
        ievads="Vispirms atrodi soli, tikai tad rēķini nākamo."),

    Zimejums("Virkne uz skaitļu taisnes",
             taisne(0, 2, 1, [(1.25, "1 1/4"), (1.5, "1 1/2"),
                              (1.75, "1 3/4")],
                    virsraksts="Vienādi soļi pa ceturtdaļai"),
             paskaidro="Attālumi starp punktiem ir vienādi - tāda ir katra "
                       "virkne ar pastāvīgu soli.",
             ievads="Uz taisnes virkne izskatās kā vienādi lēcieni."),

    Varianti("Kas notiek ar veselo daļu?", [
        {"jaut": "Cik ir 1{3|4} + {1|4}?",
         "opcijas": ["2", "1{4|4} un tas ir galīgi", "1{4|8}", "2{1|4}"],
         "pareizi": 0,
         "padoms": "Daļa kļuva par veselu."},
        {"jaut": "Kad virknē aug veselā daļa?",
         "opcijas": ["Kad daļas savācas līdz veselam",
                     "Katrā solī",
                     "Nekad",
                     "Kad solis ir vesels skaitlis"],
         "pareizi": 0,
         "padoms": "{4|4} = 1."},
        {"jaut": "Kāds ir virknes 2; 2{1|3}; 2{2|3} solis?",
         "opcijas": ["{1|3}", "{2|3}", "1", "{1|2}"],
         "pareizi": 0,
         "padoms": "Starpība starp blakus locekļiem."},
        {"jaut": "Cik soļu pa {1|3} vajag, lai pieaugtu viens vesels?",
         "opcijas": ["3", "1", "2", "4"],
         "pareizi": 0,
         "padoms": "Trīs trešdaļas."},
        {"jaut": "Vai pieraksts 2{5|4} ir galīgā atbilde?",
         "opcijas": ["Nav, jāatdala veselais", "Ir", "Ir, ja saucējs ir 4",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "{5|4} ir neīsta daļa."},
        {"jaut": "1{1|2}; 2; 2{1|2}; 3 - kāds ir nākamais?",
         "opcijas": ["3{1|2}", "3{1|4}", "4", "3"],
         "pareizi": 0,
         "padoms": "Solis ir {1|2}."},
    ], pamats=4),

    Pasaule("Cik ilgi cepas?",
            Ievadi("", [
                {"jaut": "Katrs cepiens ilgst {1|4} stundas. Cik stundas "
                         "ilgst divi cepieni? Atbildi raksti kā a/b.",
                 "atb": ["1/2", "2/4"], "padoms": "{2|4} saīsināts."},
                {"jaut": "Cik stundas ilgst pieci cepieni? Atbildi raksti kā "
                         "a b/c.",
                 "atb": ["1 1/4"], "padoms": "{5|4} = 1{1|4}."},
                {"jaut": "Cik cepienu ietilpst vienā stundā?",
                 "atb": ["4"], "padoms": "Četras ceturtdaļas."},
                {"jaut": "Cik stundas ilgst septiņi cepieni? Atbildi raksti "
                         "kā a b/c.",
                 "atb": ["1 3/4"], "padoms": "{7|4} = 1{3|4}."},
            ]),
            pavediens="virtuve",
            konteksts="Cepamā laiku skaita pa ceturtdaļstundām, un tie "
                      "krājas vienādos soļos.",
            kapec="Virkne pasaka, kad kopējais laiks sasniegs veselu "
                  "stundu."),

    Kopsavilkums([
        "Nosaku jauktu skaitļu virknes soli.",
        "Turpinu virkni, pieskaitot soli katram loceklim.",
        "Atdalu veselo, kad daļa kļūst neīsta.",
        "Pārbaudu, vai starpība starp locekļiem ir pastāvīga.",
    ]),

    Majas([
        "Turpini virkni 2{1|5}; 2{2|5}; 2{3|5}; ... par trim locekļiem.",
        "Izveido savu virkni ar soli {1|6} un pieraksti piecus locekļus.",
        "Atrodi, cik soļu pa {1|8} vajag, lai pieaugtu viens vesels.",
    ]),
]
