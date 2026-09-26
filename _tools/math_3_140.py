# -*- coding: utf-8 -*-
"""3. klase, 140. stunda: «Cik apmēram sanāks?»

Novērtēšana ar noapaļošanu līdz simtiem - tas pats paņēmiens, kas 28. stundā
bija ar desmitiem, tikai tagad lielākiem skaitļiem. Galvenais ieguvums ir
pārbaude: rupju kļūdu redz uzreiz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Cik apmēram sanāks?"

MERKIS = ("Novērtēsim summas aptuveno vērtību un izmantosim to pārbaudei.")

SATURS = [
    Sakums("Vai atbilde vispār ir ticama?",
           zimejums=kolonnas([("apmēram", 700), ("precīzi", 683)]),
           paraksts="268 + 415 ir apmēram 300 + 400 = 700.",
           fakti=["Noapaļo abus saskaitāmos līdz simtiem.",
                  "Ja precīzā atbilde ir tālu no aptuvenās, meklē kļūdu."]),

    Doma("Noapaļo līdz simtiem un saskaiti galvā",
         "Noapaļots rēķins ir tik vienkāršs, ka to var izdarīt galvā - un tas "
         "pasaka, kādai jābūt īstajai atbildei.",
         soli=[
             "Noapaļo katru skaitli līdz tuvākajam simtam.",
             "Saskaiti apaļos skaitļus.",
             "Izrēķini precīzo summu.",
             "Salīdzini abus rezultātus.",
         ],
         pieze="Ja abus noapaļoja uz augšu, precīzā summa būs mazāka; ja uz "
               "leju - lielāka. Tas pasaka, kurā pusē gaidīt atbildi."),

    Paraugs("Cik apmēram ir 268 + 415?",
            uzd="Novērtē 268 + 415 un tad izrēķini precīzi.",
            soli=[
                ("268 ≈ 300, 415 ≈ 400",
                 "Noapaļo abus līdz simtiem."),
                ("300 + 400 = 700",
                 "Aptuvenā vērtība."),
                ("268 + 415 = 683",
                 "Precīzā summa - tuvu septiņiem simtiem."),
            ],
            atbilde="apmēram 700, precīzi 683"),

    Ievadi("Novērtē un izrēķini", [
        {"jaut": "Noapaļo 268 līdz simtiem. Cik sanāk?", "atb": ["300"],
         "padoms": "Desmitu vietā ir 6."},
        {"jaut": "Noapaļo 415 līdz simtiem. Cik sanāk?", "atb": ["400"],
         "padoms": "Desmitu vietā ir 1."},
        {"jaut": "Cik apmēram ir 268 + 415?", "atb": ["700"],
         "padoms": "300 + 400."},
        {"jaut": "Cik precīzi ir 268 + 415?", "atb": ["683"],
         "padoms": "Stabiņā."},
        {"jaut": "Cik apmēram ir 349 + 236?", "atb": ["500"],
         "padoms": "300 + 200."},
        {"jaut": "Cik precīzi ir 349 + 236?", "atb": ["585"],
         "padoms": "Stabiņā."},
    ], pamats=4),

    Zimejums("Aptuveni un precīzi",
             kolonnas([("300 + 400", 700), ("268 + 415", 683),
                       ("200 + 400", 600)]),
             paskaidro="Precīzā summa vienmēr ir starp abām apaļajām "
                       "vērtībām.",
             ievads="Trīs rēķini par vienu un to pašu."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "Skolēns uzrakstīja 268 + 415 = 6813. Kā to pamanīt?",
         "opcijas": ["Aptuvenā vērtība ir tikai 700",
                     "Atbilde ir par mazu", "Kļūdas nav",
                     "Summai jābūt pāra skaitlim"],
         "pareizi": 0, "padoms": "Kļūda ir desmit reižu."},
        {"jaut": "Noapaļo 651 līdz simtiem.",
         "opcijas": ["700", "600", "650", "660"],
         "pareizi": 0, "padoms": "Desmitu vietā ir 5."},
        {"jaut": "Cik apmēram ir 498 + 305?",
         "opcijas": ["800", "700", "900", "750"],
         "pareizi": 0, "padoms": "500 + 300."},
        {"jaut": "Kad precīzā summa ir mazāka par aptuveno?",
         "opcijas": ["Kad abi noapaļoti uz augšu",
                     "Kad abi noapaļoti uz leju",
                     "Vienmēr", "Nekad"],
         "pareizi": 0, "padoms": "Uz augšu noapaļots skaitlis ir lielāks."},
    ], pamats=4),

    Pasaule("Vai degvielas pietiks?",
            Ievadi("", [
                {"jaut": "Posmi 268 km un 415 km. Cik apmēram ir kopā?",
                 "atb": ["700"], "padoms": "300 + 400."},
                {"jaut": "Cik precīzi ir kopā?", "atb": ["683"],
                 "padoms": "Stabiņā."},
                {"jaut": "Ar pilnu bāku var nobraukt 700 km. Vai pietiks? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "683 < 700.",
                 "tastatura": "text"},
                {"jaut": "Cik kilometru rezerves paliek?", "atb": ["17"],
                 "padoms": "700 − 683."},
            ]),
            pavediens="celojums",
            konteksts="Pirms garā brauciena vispirms novērtē, tikai tad "
                      "rēķina precīzi.",
            kapec="Aptuvenā vērtība atbild uz galveno jautājumu: vai pietiks."),

    Kopsavilkums([
        "Noapaļoju skaitļus līdz simtiem.",
        "Novērtēju summas aptuveno vērtību.",
        "Salīdzinu precīzo atbildi ar aptuveno.",
        "Pamanu rupjas kļūdas.",
    ]),

    Majas([
        "Novērtē un izrēķini 376 + 218 un 542 + 389.",
        "Salīdzini abas atbildes ar aptuvenajām.",
        "Novērtē mājas pirkuma summu, pirms paskaties čekā.",
    ]),
]
