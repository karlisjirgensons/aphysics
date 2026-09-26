# -*- coding: utf-8 -*-
"""4. klase, 42. stunda: «Kā dalīt trīsciparu skaitli?»

Dalīšana ar viencipara skaitli trīsciparu apjomā - divos veidos: izsakot
dalāmo kā ērtu summu (636 : 6 = 600 : 6 + 36 : 6) vai dalot pakāpeniski
(vispirms simtus, tad to, kas palicis). Abi ceļi sagatavo dalīšanu stūrītī.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā dalīt trīsciparu skaitli?"

MERKIS = ("Dalīsim trīsciparu skaitli ar viencipara skaitli, izsakot dalāmo "
          "kā summu vai dalot pakāpeniski.")

SATURS = [
    Sakums("Kā 4 klases sadala 848 kokus stādīšanai?",
           zimejums=restis([["848", "=", "800", "+", "40", "+", "8"],
                            [": 4", "", "200", "+", "10", "+", "2"]],
                           "848 : 4 = 212"),
           paraksts="Katra šķira dalās ar 4 - rezultāts uzreiz.",
           fakti=["Latvijā katru pavasari stāda miljoniem koku.",
                  "Lielu skaitli dala pa daļām, kas katra dalās."]),

    Doma("Dali pa gabaliem, kas katrs dalās",
         "Izsaki dalāmo kā summu, kurā katrs saskaitāmais dalās ar dalītāju; "
         "izdali katru un saskaiti.",
         soli=[
             "Vieglākais: katra šķira dalās - 848 : 4 = 200 + 10 + 2.",
             "Ja nedalās, pārgrupē: 738 : 3 = 600 : 3 + 138 : 3.",
             "138 : 3 = 120 : 3 + 18 : 3 = 40 + 6.",
             "738 : 3 = 200 + 46 = 246. Pārbaude: 246 · 3 = 738.",
         ],
         pieze="Pakāpeniski: vispirms atņem lielāko ērto daļu (600), tad "
               "strādā ar atlikušo (138)."),

    Paraugs("516 : 4",
            uzd="Izrēķini 516 : 4.",
            soli=[
                ("516 = 400 + 116", "400 dalās ar 4."),
                ("400 : 4 = 100", None),
                ("116 = 80 + 36", "Atlikušo arī sadala."),
                ("80 : 4 = 20, 36 : 4 = 9", None),
                ("100 + 20 + 9 = 129", "Pārbaude: 129 · 4 = 516."),
            ],
            atbilde="129"),

    Slidnis("Pakāpeniski: 945 : 5",
            soli=[
                {"v": "945", "teksts": "Cik lielu ērtu gabalu var atdalīt?",
                 "josla": 100},
                {"v": "945 − 500 = 445", "teksts": "500 : 5 = 100. Paliek "
                 "445.", "josla": 47},
                {"v": "445 − 400 = 45", "teksts": "400 : 5 = 80. Paliek 45.",
                 "josla": 5},
                {"v": "45 : 5 = 9", "teksts": "Pēdējais gabals.", "josla": 0},
                {"v": "100 + 80 + 9 = 189", "teksts": "Saskaita visus "
                 "dalījumus."},
            ],
            ievads="Katrā solī atdala gabalu, ko ērti dalīt ar 5."),

    Ievadi("Dali pa gabaliem", [
        {"jaut": "848 : 4 = ?", "atb": ["212"], "padoms": "200 + 10 + 2."},
        {"jaut": "636 : 6 = ?", "atb": ["106"], "padoms": "600 : 6 + 36 : 6."},
        {"jaut": "738 : 3 = ?", "atb": ["246"], "padoms": "600 + 138."},
        {"jaut": "945 : 5 = ?", "atb": ["189"], "padoms": "500 + 400 + 45."},
        {"jaut": "872 : 8 = ?", "atb": ["109"], "padoms": "800 + 72."},
        {"jaut": "651 : 7 = ?", "atb": ["93"], "padoms": "630 + 21."},
    ], pamats=4),

    Varianti("Kura summa ērtāka?", [
        {"jaut": "Kā sadalīt 752, lai dalītu ar 8?",
         "opcijas": ["720 + 32", "700 + 52", "750 + 2", "400 + 352"],
         "pareizi": 0, "padoms": "720 : 8 = 90, 32 : 8 = 4."},
        {"jaut": "Cik ir 752 : 8?",
         "opcijas": ["94", "904", "84", "95"], "pareizi": 0,
         "padoms": "90 + 4."},
        {"jaut": "Kā pārbaudīt 432 : 6 = 72?",
         "opcijas": ["72 · 6", "432 · 6", "72 + 6", "432 − 72"],
         "pareizi": 0, "padoms": "Dalījums · dalītājs."},
    ]),

    Pasaule("Koku stādīšanas talka",
            Ievadi("", [
                {"jaut": "Talkā 5 klases stāda 945 kociņus vienādi. Cik "
                         "katrai klasei?",
                 "atb": ["189"], "padoms": "945 : 5."},
                {"jaut": "Mežsargs sadala 624 stādus 3 rindās vienādi. Cik "
                         "katrā rindā?",
                 "atb": ["208"], "padoms": "600 : 3 + 24 : 3."},
                {"jaut": "Ūdens 768 l jāsadala 6 mucās. Cik litru katrā?",
                 "atb": ["128"], "padoms": "600 + 168."},
                {"jaut": "Pēc gada no 945 kociņiem izdzīvoja visi, izņemot "
                         "45. Cik izdzīvoja?",
                 "atb": ["900"], "padoms": "945 − 45."},
            ]),
            pavediens="planeta",
            konteksts="Viens koks gadā uzņem apmēram 20 kg oglekļa dioksīda - "
                      "tāpēc talkas rēķina kokus simtiem.",
            kapec="Lielu skaitu var sadalīt godīgi, ja dala pa gabaliem."),

    Kopsavilkums([
        "Dalu trīsciparu skaitli, izsakot to kā ērtu summu.",
        "Dalu pakāpeniski, atdalot lielus gabalus.",
        "Pārbaudu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini 960 : 8 divos veidos.",
        "Izdomā uzdevumu par talku, kurā jādala trīsciparu skaitlis.",
        "Pastāsti mājiniekiem, kā dalīji 945 : 5.",
    ]),
]
