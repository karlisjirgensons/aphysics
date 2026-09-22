# -*- coding: utf-8 -*-
"""6. klase, 120. stunda: «Kas notiek, figūru pārvietojot?»

Pārvietošana ir pirmā transformācija. Skaitliski tā ir vienkārša -
koordinātām pieskaita vienu un to pašu skaitli -, un tieši tas ir šīs
stundas atklājums: figūras kustība ir saskaitīšana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kas notiek, figūru pārvietojot?"

MERKIS = ("Zīmēsim figūru, kas iegūta, pārvietojot doto par vienībām pa "
          "asīm, un raksturosim koordinātu sakarības.")

SATURS = [
    Sakums("Visas virsotnes kustas vienādi",
           zimejums=plakne(lauzta=[(-3, 1), (-1, 1), (-1, 3), (-3, 3)],
                           aizpildi=True, no_x=-5, lidz_x=5, no_y=-4,
                           lidz_y=4, solis=1),
           paraksts="Ja šo kvadrātu pārvieto par 4 pa labi, katrai virsotnei "
                    "pirmā koordināta pieaug par 4.",
           fakti=["Pārvietojot figūru, tās forma un izmēri nemainās.",
                  "Katrai virsotnei pieskaita vienu un to pašu skaitli.",
                  "Kustība pa labi maina pirmo koordinātu, uz augšu - otro."]),

    Doma("Pārvietot nozīmē pieskaitīt",
         "Pārvietojot figūru par a vienībām horizontāli un b vertikāli, "
         "katras virsotnes pirmajai koordinātai pieskaita a, otrajai - b.",
         soli=[
             "Pieraksti visu virsotņu koordinātas.",
             "Nosaki, par cik vienībām figūra pārvietojas pa katru asi.",
             "Pieskaiti šos skaitļus katrai koordinātai.",
             "Atliec jaunās virsotnes un savieno tās.",
             "Pārbaudi: malu garumiem jāpaliek tādiem pašiem.",
         ],
         pieze="Kustībai pa kreisi un uz leju pieskaita negatīvus skaitļus. "
               "Tāpēc pārvietošana ir vienkārši saskaitīšana - arī ar "
               "negatīviem skaitļiem."),

    Paraugs("Pārvieto kvadrātu",
            uzd="Kvadrāts ar virsotnēm (−3; 1), (−1; 1), (−1; 3), (−3; 3) "
                "jāpārvieto par 4 pa labi un 2 uz leju.",
            soli=[
                ("Pa labi par 4: pirmajai koordinātai +4",
                 "Horizontālā kustība."),
                ("Uz leju par 2: otrajai koordinātai −2",
                 "Vertikālā kustība."),
                ("(−3; 1) → (1; −1); (−1; 1) → (3; −1)",
                 "Pirmās divas virsotnes."),
                ("(−1; 3) → (3; 1); (−3; 3) → (1; 1)",
                 "Pārējās divas."),
                ("Mala joprojām ir 2 vienības",
                 "Forma nemainījās."),
            ],
            atbilde="(1; −1), (3; −1), (3; 1), (1; 1)"),

    Ievadi("Pārvieto punktu", [
        {"jaut": "Punktu (−3; 1) pārvieto par 4 pa labi. Kāda ir jaunā pirmā "
                 "koordināta?",
         "atb": ["1"], "padoms": "−3 + 4."},
        {"jaut": "To pašu punktu pārvieto par 2 uz leju. Kāda ir jaunā otrā "
                 "koordināta?",
         "atb": ["-1", "−1"], "padoms": "1 − 2."},
        {"jaut": "Punktu (2; −3) pārvieto par 5 uz augšu. Kāda ir jaunā otrā "
                 "koordināta?",
         "atb": ["2"], "padoms": "−3 + 5."},
        {"jaut": "Punktu (4; 2) pārvieto par 6 pa kreisi. Kāda ir jaunā "
                 "pirmā koordināta?",
         "atb": ["-2", "−2"], "padoms": "4 − 6."},
        {"jaut": "Punkts (1; 1) pēc pārvietošanas kļuva (5; 1). Par cik "
                 "vienībām tas pārvietots pa labi?",
         "atb": ["4"], "padoms": "5 − 1."},
        {"jaut": "Punkts (0; 3) kļuva (0; −2). Par cik vienībām uz leju?",
         "atb": ["5"], "padoms": "3 + 2."},
    ], pamats=4),

    Pasaule("Kur nonāks robots?",
            Kustiba("", [
                {"jaut": "Robots ir punktā −6 un pārvietojas par 4 pa labi. "
                         "Kurā punktā tas ir?",
                 "atb": -2, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "vienības", "merkis": "jaunā vieta",
                 "objekts": "Robots", "padoms": "−6 + 4."},
                {"jaut": "No −2 tas pārvietojas par 7 pa labi. Kurā punktā?",
                 "atb": 5, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "vienības", "merkis": "jaunā vieta",
                 "objekts": "Robots", "padoms": "−2 + 7."},
                {"jaut": "No 5 tas pārvietojas par 9 pa kreisi. Kurā punktā?",
                 "atb": -4, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "vienības", "merkis": "jaunā vieta",
                 "objekts": "Robots", "padoms": "5 − 9."},
                {"jaut": "No −4 tas pārvietojas par 4 pa labi. Kurā punktā?",
                 "atb": 0, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "vienības", "merkis": "jaunā vieta",
                 "objekts": "Robots", "padoms": "−4 + 4."},
            ]),
            pavediens="tehnika",
            konteksts="Robotam komandu dod kā pārvietojumu: par cik un uz "
                      "kuru pusi - pārējo tas izrēķina pats.",
            kapec="Pārvietojums ir saskaitīšana ar zīmi."),

    Varianti("Kas mainās, kas ne?", [
        {"jaut": "Pārvietojot figūru, nemainās...",
         "opcijas": ["forma un izmēri", "koordinātas",
                     "vieta plaknē", "nekas"],
         "pareizi": 0,
         "padoms": "Mainās tikai vieta."},
        {"jaut": "Kustība pa kreisi nozīmē pieskaitīt...",
         "opcijas": ["negatīvu skaitli", "pozitīvu skaitli",
                     "nulli", "otro koordinātu"],
         "pareizi": 0,
         "padoms": "Pirmā koordināta sarūk."},
        {"jaut": "Punktu (2; 5) pārvieto par 3 uz leju. Jaunais punkts ir...",
         "opcijas": ["(2; 2)", "(5; 5)", "(2; 8)", "(−1; 5)"],
         "pareizi": 0,
         "padoms": "Otrajai koordinātai −3."},
        {"jaut": "Visas figūras virsotnes pārvietojas...",
         "opcijas": ["par vienu un to pašu", "katra citādi",
                     "tikai divas", "nemaz"],
         "pareizi": 0,
         "padoms": "Citādi figūra deformētos."},
    ], pamats=4),

    Zimejums("Figūra jaunā vietā",
             plakne(lauzta=[(1, -1), (3, -1), (3, 1), (1, 1)],
                    aizpildi=True, no_x=-5, lidz_x=5, no_y=-4, lidz_y=4,
                    solis=1),
             paskaidro="Tas pats kvadrāts pēc pārvietošanas par 4 pa labi un "
                       "2 uz leju. Mala joprojām ir 2 vienības.",
             ievads="Salīdzini ar stundas sākuma zīmējumu."),

    Kopsavilkums([
        "Pārvietoju figūru, pieskaitot koordinātām vienu un to pašu skaitli.",
        "Lietoju negatīvus skaitļus kustībai pa kreisi un uz leju.",
        "Pārbaudu, vai forma un izmēri nav mainījušies.",
        "Nosaku pārvietojumu, ja zināmas abas figūras.",
    ]),

    Majas([
        "Uzzīmē trīsstūri un pārvieto to par 3 pa kreisi un 2 uz augšu.",
        "Pieraksti abu figūru virsotņu koordinātas.",
        "Pārbaudi, vai malu garumi nav mainījušies.",
    ]),
]
