# -*- coding: utf-8 -*-
"""5. klase, 29. stunda: «Kura izteiksme ir lielāka?»

Mikrotemata pēdējā stunda, un vienīgā, kurā atbildi nedrīkst izrēķināt.
Salīdzināt, nerēķinot, nozīmē pamanīt, kas starp abām izteiksmēm mainījies -
tā pati doma, kas 22. stundā summai un starpībai, tagad reizinājumam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kura izteiksme ir lielāka?"

MERKIS = ("Mācīsimies salīdzināt izteiksmju vērtības spriežot, tās precīzi "
          "neaprēķinot.")

SATURS = [
    Sakums("Kura ir lielāka - bez rēķināšanas?",
           fakti=["48 · 12 vai 48 · 11?",
                  "360 : 4 vai 360 : 6?",
                  "Abas var izrēķināt. Bet var arī vienkārši saskatīt."]),

    Doma("Salīdzini locekļus, nevis atbildes",
         "Ja viens reizinātājs abās izteiksmēs ir vienāds, lielāka ir tā, "
         "kurai otrs reizinātājs ir lielāks.",
         soli=[
             "Pieraksti, kas abās izteiksmēs ir vienāds.",
             "Atrodi, ar ko tās atšķiras.",
             "Reizinājumā: lielāks reizinātājs - lielāks reizinājums.",
             "Dalījumā: lielāks dalītājs - mazāks dalījums.",
             "Uzraksti zīmi > vai < un pamato vienā teikumā.",
         ],
         pieze="Dalīšana te apgriež domu otrādi: jo vairāk cilvēku dala vienu "
               "torti, jo mazāks gabals katram. Tāpēc 360 : 4 ir lielāks "
               "nekā 360 : 6."),

    Paraugs("Spried, nerēķini",
            uzd="Kura izteiksme ir lielāka: 48 · 12 vai 48 · 11?",
            soli=[
                ("Abās ir reizinātājs 48",
                 "Tas ir kopīgais."),
                ("Atšķiras otrs reizinātājs: 12 un 11",
                 "12 ir par 1 lielāks."),
                ("Tātad 48 · 12 > 48 · 11",
                 "Lielāks reizinātājs dod lielāku reizinājumu."),
                ("Atšķirība ir tieši 48",
                 "Par vienu reizinātāju vairāk - par vienu 48 vairāk."),
            ],
            atbilde="48 · 12 ir lielāka, un tieši par 48"),

    Ievadi("Uzraksti > vai <", [
        {"jaut": "48 · 12 ? 48 · 11. Raksti > vai <.", "atb": [">"],
         "padoms": "Lielāks reizinātājs."},
        {"jaut": "360 : 4 ? 360 : 6. Raksti > vai <.", "atb": [">"],
         "padoms": "Mazāks dalītājs - lielāks dalījums."},
        {"jaut": "25 · 8 ? 25 · 9. Raksti > vai <.", "atb": ["<"],
         "padoms": "Otrs reizinātājs ir mazāks."},
        {"jaut": "100 : 5 ? 100 : 2. Raksti > vai <.", "atb": ["<"],
         "padoms": "Lielāks dalītājs - mazāks dalījums."},
        {"jaut": "Par cik 48 · 12 ir lielāks nekā 48 · 11?", "atb": ["48"],
         "padoms": "Par vienu reizinātāju vairāk."},
        {"jaut": "Par cik 25 · 9 ir lielāks nekā 25 · 8?", "atb": ["25"],
         "padoms": "Tāpat - par vienu reizinātāju."},
        {"jaut": "7 · 99 ? 7 · 100. Raksti > vai <.", "atb": ["<"],
         "padoms": "99 ir mazāks par 100."},
        {"jaut": "Par cik 7 · 100 ir lielāks nekā 7 · 99?", "atb": ["7"],
         "padoms": "Par vienu septītnieku."},
    ], pamats=4,
        ievads="Nerēķini abas izteiksmes - salīdzini locekļus."),

    Varianti("Kā to var zināt, nerēķinot?", [
        {"jaut": "Kāpēc 360 : 4 ir lielāks nekā 360 : 6?",
         "opcijas": ["Jo dala mazāk daļās",
                     "Jo 4 ir mazāks skaitlis",
                     "Jo 360 dalās ar 4",
                     "Tas nav lielāks"],
         "pareizi": 0,
         "padoms": "Jo mazāk cilvēku dala torti, jo lielāks gabals."},
        {"jaut": "Kura izteiksme ir lielāka: 15 · 20 vai 16 · 20?",
         "opcijas": ["16 · 20", "15 · 20", "Vienādas", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Kopīgais reizinātājs ir 20."},
        {"jaut": "Kura ir lielāka: 900 : 30 vai 900 : 3?",
         "opcijas": ["900 : 3", "900 : 30", "Vienādas", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Mazāks dalītājs dod lielāku dalījumu."},
        {"jaut": "Kura ir lielāka: 12 · 30 vai 13 · 29?",
         "opcijas": ["13 · 29", "12 · 30", "Vienādas", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Šo gan jāizrēķina: 360 un 377. Kad abi locekļi mainās, "
                   "spriest ar aci nepietiek."},
        {"jaut": "Kad izteiksmes salīdzināt, nerēķinot, nevar?",
         "opcijas": ["Kad mainās abi locekļi",
                     "Kad skaitļi ir lieli",
                     "Kad ir dalīšana",
                     "Kad ir iekavas"],
         "pareizi": 0,
         "padoms": "Viens aug, otrs sarūk - virziens vairs nav skaidrs."},
        {"jaut": "Ko nozīmē zīme <?",
         "opcijas": ["Kreisā puse ir mazāka", "Kreisā puse ir lielāka",
                     "Puses ir vienādas", "Puses nav salīdzināmas"],
         "pareizi": 0,
         "padoms": "Šaurais gals rāda uz mazāko."},
    ], pamats=4),

    Pasaule("Kurš pirkums ir izdevīgāks?",
            Ievadi("", [
                {"jaut": "12 paciņas pa 48 centiem vai 11 paciņas pa "
                         "48 centiem - kura summa lielāka? Raksti 12 vai 11.",
                 "atb": ["12"], "padoms": "Vairāk paciņu - lielāka summa."},
                {"jaut": "Par cik centiem lielāka?", "atb": ["48"],
                 "padoms": "Par vienu paciņu."},
                {"jaut": "360 eiro dala 4 vai 6 cilvēki - kurā gadījumā "
                         "katram vairāk? Raksti 4 vai 6.",
                 "atb": ["4"], "padoms": "Mazāk cilvēku - lielāka daļa."},
                {"jaut": "Cik eiro katram, ja dala 4 cilvēki?",
                 "atb": ["90"], "padoms": "360 : 4."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā bieži pietiek zināt, kurš variants ir "
                      "lielāks - precīzu summu skatās tikai kasē.",
            kapec="Salīdzināt var ātrāk nekā izrēķināt."),

    Kopsavilkums([
        "Salīdzinu izteiksmes, tās precīzi neaprēķinot.",
        "Zinu: lielāks reizinātājs - lielāks reizinājums.",
        "Zinu: lielāks dalītājs - mazāks dalījums.",
        "Pamanu gadījumu, kad mainās abi locekļi un spriest vairs nepietiek.",
    ]),

    Majas([
        "Uzraksti divas izteiksmes, kuras var salīdzināt, neizrēķinot.",
        "Uzraksti divas, kuras tā salīdzināt nevar, un paskaidro kāpēc.",
        "Pārbaudi savus spriedumus ar kalkulatoru.",
    ]),
]
