# -*- coding: utf-8 -*-
"""4. klase, 28. stunda: «Kurš pieraksts man ērtāks?»

Trīs pieraksti vienam reizinājumam: rindā, ar starprezultātiem un stabiņā.
Stabiņš te parādās pirmo reizi reizināšanai - tas ir tas pats pa daļām,
tikai saspiests. Skolēns salīdzina un izvēlas; nav «vienīgā pareizā».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kurš pieraksts man ērtāks?"

MERKIS = ("Salīdzināsim reizināšanas pierakstus - rindā, ar "
          "starprezultātiem un stabiņā - un izvēlēsimies ērtāko.")

SATURS = [
    Sakums("Trīs ceļi uz 67 · 4",
           zimejums=restis([["rindā", "67 · 4 = 268"],
                            ["pa daļām", "240 + 28 = 268"],
                            ["stabiņā", "7 · 4 = 28, raksta 8, 2 prātā"]],
                           "viens reizinājums"),
           fakti=["Visi trīs ceļi dod vienu atbildi.",
                  "Ātrākais ir tas, ko tu proti vislabāk."]),

    Doma("Stabiņš ir «pa daļām», tikai īsāk",
         "Stabiņā vispirms reizina vienus, pieraksta vienu ciparu un "
         "desmitus patur prātā; tad reizina desmitus un pieskaita paturēto.",
         soli=[
             "Raksti reizinātāju zem vieniem.",
             "7 · 4 = 28: raksta 8, 2 desmitus patur prātā.",
             "6 · 4 = 24, 24 + 2 = 26: raksta 26.",
             "Rezultāts: 268.",
         ],
         pieze="Pa daļām: 60 · 4 = 240, 7 · 4 = 28, 240 + 28 = 268 - tie paši "
               "skaitļi, tikai citur pierakstīti."),

    Paraugs("58 · 3 stabiņā",
            uzd="Sareizini 58 · 3 stabiņā.",
            soli=[
                ("8 · 3 = 24", "Raksta 4, 2 patur prātā."),
                ("5 · 3 = 15", None),
                ("15 + 2 = 17", "Raksta 17."),
                ("58 · 3 = 174", None),
            ],
            atbilde="174"),

    Zimejums("Tas pats - trīs veidos",
             restis([["", "desmiti", "vieni", "kopā"],
                     ["pa daļām", "50 · 3 = 150", "8 · 3 = 24", "174"],
                     ["stabiņā", "15 + 2", "4 (2 prātā)", "174"]],
                    "58 · 3"),
             paskaidro="Stabiņā «2 prātā» ir tie paši 2 desmiti no 24.",
             ievads="Salīdzini rindas - skaitļi atkārtojas."),

    Ievadi("Izvēlies pierakstu un izrēķini", [
        {"jaut": "67 · 4 = ?", "atb": ["268"], "padoms": "240 + 28."},
        {"jaut": "83 · 5 = ?", "atb": ["415"], "padoms": "400 + 15."},
        {"jaut": "46 · 7 = ?", "atb": ["322"], "padoms": "280 + 42."},
        {"jaut": "95 · 6 = ?", "atb": ["570"], "padoms": "540 + 30."},
        {"jaut": "38 · 9 = ?", "atb": ["342"], "padoms": "270 + 72."},
        {"jaut": "72 · 8 = ?", "atb": ["576"], "padoms": "560 + 16."},
    ], pamats=4),

    Varianti("Ko nozīmē «prātā»?", [
        {"jaut": "74 · 3 stabiņā: 4 · 3 = 12. Ko patur prātā?",
         "opcijas": ["1 desmitu", "2 vienus", "12", "1 simtu"],
         "pareizi": 0, "padoms": "12 = 1 desmits un 2 vieni."},
        {"jaut": "Kurš pieraksts ir ar starprezultātiem?",
         "opcijas": ["70 · 3 + 4 · 3 = 210 + 12",
                     "74 · 3 = 222", "74 + 74 + 74"], "pareizi": 0,
         "padoms": "Starprezultāti - katra daļa atsevišķi."},
        {"jaut": "Cik ir 74 · 3?",
         "opcijas": ["222", "212", "2112", "217"], "pareizi": 0,
         "padoms": "210 + 12."},
    ]),

    Pasaule("Futbola kluba apģērbs",
            Ievadi("", [
                {"jaut": "Viens krekls maksā 36 €. Cik maksā 8 krekli?",
                 "atb": ["288"], "padoms": "240 + 48."},
                {"jaut": "Bikses maksā 27 €. Cik 8 pāri?",
                 "atb": ["216"], "padoms": "160 + 56."},
                {"jaut": "Zeķes maksā 9 € pārim. Cik 8 pāri?",
                 "atb": ["72"], "padoms": "9 · 8."},
                {"jaut": "Cik maksā 8 komplekti (krekls, bikses, zeķes)?",
                 "atb": ["576"], "padoms": "288 + 216 + 72 vai 72 · 8."},
            ]),
            pavediens="sports",
            konteksts="Komanda pērk formas visiem 8 spēlētājiem vienlaikus.",
            kapec="Vienu un to pašu var rēķināt dažādi - galvenais, lai "
                  "atbilde sakrīt."),

    Kopsavilkums([
        "Zinu trīs reizināšanas pierakstus.",
        "Reizinu stabiņā ar «prātā».",
        "Izvēlos sev ērtāko pierakstu un pamatoju izvēli.",
    ]),

    Majas([
        "Izrēķini 49 · 6 visos trijos veidos. Kurš tev ātrāks?",
        "Paskaidro kādam, ko nozīmē «2 prātā».",
        "Izrēķini, cik maksā 7 tev vēlamas lietas pa vienādu cenu.",
    ]),
]
