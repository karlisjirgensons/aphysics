# -*- coding: utf-8 -*-
"""6. klase, 57. stunda: «Cik dažādus rezultātus var iegūt?»

Uzdevums ar atvērtu atbildi. Skaitļi ir doti, darbības - nav; skolēns tās
izvēlas pats un skatās, cik tālu rezultāts var aizbēgt. Tas trenē to pašu,
ko iepriekšējās stundas, bet prasa domāt uz priekšu, ne tikai rēķināt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Cik dažādus rezultātus var iegūt?"

MERKIS = ("Mācīsimies starp dotiem skaitļiem ievietot darbību zīmes, lai "
          "iegūtu dažādus rezultātus.")

SATURS = [
    Sakums("Trīs skaitļi, seši rezultāti",
           fakti=["Starp 6; 0,5 un 2 var likt dažādas darbību zīmes.",
                  "6 · 0,5 · 2 = 6, bet 6 : 0,5 : 2 = 6 - sakritība!",
                  "6 : 0,5 · 2 = 24 - tas pats skaitļu komplekts."]),

    Doma("Vispirms paredzi, tad pārbaudi",
         "Lai iegūtu lielāku rezultātu, dala ar skaitli, kas mazāks par 1, "
         "un reizina ar lielāku; lai iegūtu mazāku - otrādi.",
         soli=[
             "Pieraksti dotos skaitļus.",
             "Izlem, vai meklē lielāko vai mazāko rezultātu.",
             "Novieto zīmes tā, lai katra darbība virzītu uz vajadzīgo pusi.",
             "Izrēķini un pieraksti rezultātu.",
             "Pamēģini vēl vienu kombināciju un salīdzini.",
         ],
         pieze="Darbību secība maina visu: 6 : 0,5 · 2 nav tas pats, kas "
               "6 : (0,5 · 2). Iekavas te ir atsevišķs rīks."),

    Paraugs("Meklē lielāko rezultātu",
            uzd="Starp skaitļiem 8; 0,25 un 2 ieliec zīmes tā, lai rezultāts "
                "būtu pēc iespējas lielāks.",
            soli=[
                ("Dalīšana ar 0,25 palielina četrreiz",
                 "0,25 ir mazāks par 1."),
                ("Reizināšana ar 2 palielina divreiz",
                 "2 ir lielāks par 1."),
                ("8 : 0,25 · 2 = 32 · 2 = 64",
                 "Abas darbības virza uz augšu."),
                ("Salīdzinājumam: 8 · 0,25 : 2 = 1",
                 "Tie paši skaitļi, 64 reižu mazāks rezultāts."),
            ],
            atbilde="64"),

    Ievadi("Izrēķini katru kombināciju", [
        {"jaut": "Cik ir 8 · 0,25 · 2?",
         "atb": ["4"], "padoms": "2 · 2."},
        {"jaut": "Cik ir 8 : 0,25 · 2?",
         "atb": ["64"], "padoms": "32 · 2."},
        {"jaut": "Cik ir 8 · 0,25 : 2?",
         "atb": ["1"], "padoms": "2 : 2."},
        {"jaut": "Cik ir 8 : 0,25 : 2?",
         "atb": ["16"], "padoms": "32 : 2."},
        {"jaut": "Kurš no šiem četriem rezultātiem ir lielākais?",
         "atb": ["64"], "padoms": "Abas darbības palielina."},
        {"jaut": "Cik ir 8 : (0,25 · 2)?",
         "atb": ["16"], "padoms": "Iekavās 0,5."},
    ], pamats=4,
        ievads="Tie paši trīs skaitļi - pavisam citi rezultāti."),

    Pasaule("Cik tālu aizlido zonde?",
            Kustiba("", [
                {"jaut": "Bāzes attālums 10, koeficienti 0,5 un 4. Cik ir "
                         "10 · 0,5 · 4?",
                 "atb": 20, "beigas": 100, "iedala": 20, "mers": "vienības",
                 "merkis": "rezultāts", "objekts": "Zonde",
                 "padoms": "5 · 4."},
                {"jaut": "Cik ir 10 : 0,5 · 4?",
                 "atb": 80, "beigas": 100, "iedala": 20, "mers": "vienības",
                 "merkis": "rezultāts", "objekts": "Zonde",
                 "padoms": "20 · 4."},
                {"jaut": "Cik ir 10 · 0,5 : 4?",
                 "atb": 1.25, "beigas": 100, "iedala": 20, "mers": "vienības",
                 "merkis": "rezultāts", "objekts": "Zonde",
                 "padoms": "5 : 4."},
                {"jaut": "Cik ir 10 : (0,5 · 4)?",
                 "atb": 5, "beigas": 100, "iedala": 20, "mers": "vienības",
                 "merkis": "rezultāts", "objekts": "Zonde",
                 "padoms": "Iekavās 2."},
            ]),
            pavediens="kosmoss",
            konteksts="Viens un tas pats skaitļu komplekts aizved zondi "
                      "pavisam dažādi - izšķir zīmju izvietojums.",
            kapec="Darbību izvēle maina rezultātu vairāk nekā paši skaitļi."),

    Petijums("Atrodi visus rezultātus",
             vajag="burtnīca",
             soli=[
                 "Paņem skaitļus 12; 0,5 un 3.",
                 "Pieraksti visas četras zīmju kombinācijas bez iekavām.",
                 "Izrēķini katru un sakārto rezultātus augošā secībā.",
                 "Pieliec iekavas un pieraksti vēl divus rezultātus.",
             ],
             secinajums="Lielākais rezultāts rodas tad, kad dala ar skaitli, "
                        "kas mazāks par 1, un reizina ar lielāku."),

    Varianti("Kā iegūt lielāko?", [
        {"jaut": "Lai rezultāts būtu lielāks, ar 0,2 vajag...",
         "opcijas": ["dalīt", "reizināt", "saskaitīt", "atņemt"],
         "pareizi": 0,
         "padoms": "0,2 ir mazāks par 1."},
        {"jaut": "Lai rezultāts būtu mazāks, ar 5 vajag...",
         "opcijas": ["dalīt", "reizināt", "saskaitīt", "kāpināt"],
         "pareizi": 0,
         "padoms": "5 ir lielāks par 1."},
        {"jaut": "Cik ir 6 : 0,5 : 2?",
         "opcijas": ["6", "24", "1,5", "12"],
         "pareizi": 0,
         "padoms": "12 : 2."},
        {"jaut": "Kāpēc iekavas maina rezultātu?",
         "opcijas": ["Jo tās maina darbību secību",
                     "Jo tās maina skaitļus",
                     "Jo tās maina zīmes", "Tās nemaina"],
         "pareizi": 0,
         "padoms": "6 : 0,5 · 2 nav 6 : (0,5 · 2)."},
    ], pamats=4),

    Kopsavilkums([
        "Ievietoju darbību zīmes, lai iegūtu dažādus rezultātus.",
        "Paredzu, uz kuru pusi katra darbība virzīs rezultātu.",
        "Lietoju iekavas, lai mainītu darbību secību.",
        "Salīdzinu iegūtos rezultātus un pamatoju lielāko.",
    ]),

    Majas([
        "Ar skaitļiem 20; 0,4 un 5 iegūsti pēc iespējas lielāku rezultātu.",
        "Ar tiem pašiem skaitļiem iegūsti pēc iespējas mazāku.",
        "Pieraksti, cik reižu lielākais rezultāts pārsniedz mazāko.",
    ]),
]
