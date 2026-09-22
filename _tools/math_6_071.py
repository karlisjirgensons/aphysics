# -*- coding: utf-8 -*-
"""6. klase, 71. stunda: «Kā rodas tilpuma formula?»

Formulas stunda. Iepriekšējā stundā skolēni skaitīja kubus; tagad tā pati
skaitīšana tiek pierakstīta trīs burtos. Formula te ir saīsinājums, nevis
jauns noteikums - un tieši tā to arī pasniedz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         kermenis)

TEMA = "Kā rodas tilpuma formula?"

MERKIS = ("Iegūsim taisnstūra paralēlskaldņa tilpuma formulu, modelējot ar "
          "vienības kubiem.")

SATURS = [
    Sakums("Trīs izmēri - viena reizināšana",
           zimejums=kermenis("kvadrs",
                             uzraksti=[(20, 54, "a"), (78, 40, "b"),
                                       (55, 8, "c")]),
           paraksts="Tilpums ir a reiz b reiz c - tieši tas pats, ko "
                    "iepriekšējā stundā skaitījām pa slāņiem.",
           fakti=["Slānī ir a · b kubu; slāņu ir c.",
                  "Tāpēc tilpums ir a · b · c.",
                  "Tilpumu mēra kubikvienībās: cm³, dm³, m³."]),

    Doma("Garums reiz platums reiz augstums",
         "Taisnstūra paralēlskaldņa tilpums ir trīs izmēru reizinājums, jo "
         "slāņa kubu skaitu reizina ar slāņu skaitu.",
         soli=[
             "Pieraksti trīs izmērus vienā mērvienībā.",
             "Reizini garumu ar platumu - tas ir slānis.",
             "Reizini ar augstumu - tie ir slāņi.",
             "Pieraksti atbildi kubikvienībās.",
             "Pārbaudi ar novērtējumu.",
         ],
         pieze="Kubam visi trīs izmēri ir vienādi, tāpēc tā tilpums ir "
               "šķautne trešajā pakāpē. Tieši tāpēc tilpuma mērvienībā ir "
               "trijnieks: cm³."),

    Slidnis("Kā aug kuba tilpums",
            [{"v": "šķautne 1 cm", "teksts": "tilpums 1 cm³", "josla": 2},
             {"v": "šķautne 2 cm", "teksts": "tilpums 8 cm³", "josla": 13},
             {"v": "šķautne 3 cm", "teksts": "tilpums 27 cm³", "josla": 42},
             {"v": "šķautne 4 cm", "teksts": "tilpums 64 cm³",
              "josla": 100}],
            ievads="Spied soli pa solim: šķautne aug par vienu centimetru, "
                   "tilpums - daudz straujāk nekā virsma."),

    Paraugs("Izmanto formulu",
            uzd="Kaste ir 6 cm gara, 4 cm plata un 3 cm augsta. Cik liels ir "
                "tās tilpums?",
            soli=[
                ("Slānis: 6 · 4 = 24 kubi",
                 "Garums reiz platums."),
                ("Slāņu ir 3",
                 "Tas ir augstums."),
                ("24 · 3 = 72",
                 "Tilpums kubikcentimetros."),
                ("Pārbaude: 6 · 4 · 3 = 72",
                 "Reizināšanas secība nemaina rezultātu."),
            ],
            atbilde="72 cm³"),

    Ievadi("Aprēķini tilpumu", [
        {"jaut": "Kaste 6 x 4 x 3 cm. Cik cm³ ir tilpums?",
         "atb": ["72"], "padoms": "6 · 4 · 3."},
        {"jaut": "Kubs ar šķautni 4 cm. Cik cm³ ir tilpums?",
         "atb": ["64"], "padoms": "4 · 4 · 4."},
        {"jaut": "Kaste 10 x 5 x 2 cm. Cik cm³ ir tilpums?",
         "atb": ["100"], "padoms": "50 · 2."},
        {"jaut": "Kaste 8 x 3 x 5 cm. Cik cm³ ir tilpums?",
         "atb": ["120"], "padoms": "24 · 5."},
        {"jaut": "Tilpums ir 60 cm³, pamats 5 x 4 cm. Cik cm augsta ir "
                 "kaste?",
         "atb": ["3"], "padoms": "60 : 20."},
        {"jaut": "Kuba tilpums ir 125 cm³. Cik cm gara ir šķautne?",
         "atb": ["5"], "padoms": "5 · 5 · 5."},
    ], pamats=4),

    Varianti("Kas ir kas formulā?", [
        {"jaut": "Ko nozīmē reizinājums a · b?",
         "opcijas": ["Kubu skaitu vienā slānī", "Slāņu skaitu",
                     "Visu tilpumu", "Virsmas laukumu"],
         "pareizi": 0,
         "padoms": "Tas ir pamata laukums."},
        {"jaut": "Kāpēc tilpumu mēra kubikvienībās?",
         "opcijas": ["Jo reizina trīs izmērus",
                     "Jo ķermenis ir kubs",
                     "Jo tā ir pieņemts", "Jo tilpums ir liels"],
         "pareizi": 0,
         "padoms": "Trīs izmēri - trijnieks mērvienībā."},
        {"jaut": "Kuba ar šķautni a tilpums ir...",
         "opcijas": ["a · a · a", "6 · a · a", "3 · a", "a · a"],
         "pareizi": 0,
         "padoms": "Visi trīs izmēri vienādi."},
        {"jaut": "Vai reizināšanas secība maina tilpumu?",
         "opcijas": ["Nē", "Jā", "Tikai kubam", "Tikai lieliem skaitļiem"],
         "pareizi": 0,
         "padoms": "Reizināšanā secība nav svarīga."},
    ], pamats=4),

    Pasaule("Cik ietilpst konteinerā?",
            Ievadi("", [
                {"jaut": "Konteiners 6 x 2 x 2 m. Cik m³ ir tilpums?",
                 "atb": ["24"], "padoms": "12 · 2."},
                {"jaut": "Viena kaste ir 1 m³. Cik kastu ietilpst?",
                 "atb": ["24"], "padoms": "Tilpums kubikmetros."},
                {"jaut": "Cits konteiners 12 x 2 x 2 m. Cik m³ ir tilpums?",
                 "atb": ["48"], "padoms": "24 · 2."},
                {"jaut": "Cik reižu otrais konteiners ir ietilpīgāks?",
                 "atb": ["2"], "padoms": "48 : 24."},
            ]),
            pavediens="tehnika",
            konteksts="Kravas konteineru izvēlas pēc tilpuma, un tas ir "
                      "tieši trīs izmēru reizinājums.",
            kapec="Formula aizstāj kubu skaitīšanu, kad skaitļi ir lieli."),

    Kopsavilkums([
        "Iegūstu tilpuma formulu no kubu skaitīšanas.",
        "Aprēķinu kvadra tilpumu pēc trim izmēriem.",
        "Zinu, kāpēc tilpumu mēra kubikvienībās.",
        "Atrodu trūkstošo izmēru, ja tilpums ir zināms.",
    ]),

    Majas([
        "Izmēri kādu mājas kasti un aprēķini tās tilpumu.",
        "Aprēķini kuba tilpumu, ja šķautne ir 6 cm.",
        "Pieraksti, cik reižu tas ir lielāks nekā kubam ar šķautni 3 cm.",
    ]),
]
