# -*- coding: utf-8 -*-
"""6. klase, 107. stunda: «Cik tālu viens no otra?»

Attālums starp skaitļiem ir tas pats, ko iepriekšējās stundās sauca par
temperatūras starpību un stāvu skaitu. Te tam tiek dots viens likums, kas
strādā arī tad, kad abi skaitļi ir negatīvi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Cik tālu viens no otra?"

MERKIS = ("Iemācīsimies noteikt attālumu starp diviem skaitļiem uz skaitļu "
          "taisnes.")

SATURS = [
    Sakums("Attālums nav atkarīgs no virziena",
           zimejums=taisne(-8, 4, 4, [(-6, "−6"), (2, "2")]),
           paraksts="No −6 līdz 2 ir astoņi soļi - tikpat, cik no 2 līdz −6.",
           fakti=["Attālums vienmēr ir pozitīvs skaitlis.",
                  "To atrod, no lielākā atņemot mazāko.",
                  "Ja skaitļiem ir dažādas zīmes, moduļus saskaita."]),

    Doma("No lielākā atņem mazāko",
         "Attālums starp diviem skaitļiem uz skaitļu taisnes ir lielākā un "
         "mazākā skaitļa starpība; tā vienmēr ir pozitīva.",
         soli=[
             "Nosaki, kurš skaitlis ir lielāks.",
             "No lielākā atņem mazāko.",
             "Ja abi ir vienā pusē no nulles, moduļus atņem.",
             "Ja dažādās pusēs, moduļus saskaita.",
             "Pārbaudi uz taisnes, saskaitot soļus.",
         ],
         pieze="No −6 līdz 2: no −6 līdz 0 ir 6 soļi, no 0 līdz 2 vēl 2 - "
               "kopā 8. Tāpēc dažādu zīmju gadījumā moduļus saskaita, nevis "
               "atņem."),

    Paraugs("Divi gadījumi",
            uzd="Cik tālu viens no otra ir −6 un 2? Un cik tālu −9 un −4?",
            soli=[
                ("−6 un 2 ir dažādās pusēs no nulles",
                 "Moduļi 6 un 2."),
                ("6 + 2 = 8",
                 "Attālums pirmajam pārim."),
                ("−9 un −4 ir vienā pusē",
                 "Moduļi 9 un 4."),
                ("9 − 4 = 5",
                 "Attālums otrajam pārim."),
            ],
            atbilde="8 un 5"),

    Ievadi("Cik soļu starp tiem?", [
        {"jaut": "Cik tālu viens no otra ir −6 un 2?",
         "atb": ["8"], "padoms": "6 + 2."},
        {"jaut": "Cik tālu viens no otra ir −9 un −4?",
         "atb": ["5"], "padoms": "9 − 4."},
        {"jaut": "Cik tālu viens no otra ir −3 un 3?",
         "atb": ["6"], "padoms": "3 + 3."},
        {"jaut": "Cik tālu viens no otra ir 0 un −7?",
         "atb": ["7"], "padoms": "Attālums līdz nullei."},
        {"jaut": "Cik tālu viens no otra ir −2,5 un 1,5?",
         "atb": ["4"], "padoms": "2,5 + 1,5."},
        {"jaut": "Cik tālu viens no otra ir −15 un −8?",
         "atb": ["7"], "padoms": "15 − 8."},
    ], pamats=4,
        ievads="Vispirms paskaties, vai skaitļi ir vienā pusē no nulles."),

    Pasaule("Cik jāpaceļas zondei?",
            Kustiba("", [
                {"jaut": "Zonde ir −60 m dziļumā, kuģis - virspusē (0 m). "
                         "Cik metru jāpaceļas?",
                 "atb": 60, "beigas": 200, "iedala": 50, "mers": "metri",
                 "merkis": "ceļš", "objekts": "Zonde",
                 "padoms": "Attālums līdz nullei."},
                {"jaut": "Zonde ir −120 m, mērījumu punkts −45 m. Cik metru "
                         "jāpaceļas?",
                 "atb": 75, "beigas": 200, "iedala": 50, "mers": "metri",
                 "merkis": "ceļš", "objekts": "Zonde",
                 "padoms": "120 − 45."},
                {"jaut": "Zonde ir −80 m, bet dronu jāpaceļ līdz +20 m. Cik "
                         "metru ir starp tiem?",
                 "atb": 100, "beigas": 200, "iedala": 50, "mers": "metri",
                 "merkis": "ceļš", "objekts": "Zonde",
                 "padoms": "80 + 20."},
                {"jaut": "Zonde ir −150 m, otra - −30 m. Cik metru ir starp "
                         "tām?",
                 "atb": 120, "beigas": 200, "iedala": 50, "mers": "metri",
                 "merkis": "ceļš", "objekts": "Zonde",
                 "padoms": "150 − 30."},
            ]),
            pavediens="planeta",
            konteksts="Jūras pētnieki attālumu starp diviem dziļumiem rēķina "
                      "katru dienu - un zīme te nav vienalga.",
            kapec="Attālums vienmēr ir pozitīvs, arī zem nulles."),

    Varianti("Saskaitīt vai atņemt?", [
        {"jaut": "Skaitļi ir dažādās pusēs no nulles. Moduļus...",
         "opcijas": ["saskaita", "atņem", "reizina", "dala"],
         "pareizi": 0,
         "padoms": "Ceļš iet caur nulli."},
        {"jaut": "Skaitļi ir vienā pusē no nulles. Moduļus...",
         "opcijas": ["atņem", "saskaita", "reizina", "dala"],
         "pareizi": 0,
         "padoms": "Viens ir tuvāk nullei."},
        {"jaut": "Vai attālums var būt negatīvs?",
         "opcijas": ["Nē, nekad", "Jā, ja abi skaitļi ir negatīvi",
                     "Jā, dažreiz", "Tikai nullei"],
         "pareizi": 0,
         "padoms": "Attālums ir soļu skaits."},
        {"jaut": "Attālums starp −4 un −4 ir...",
         "opcijas": ["0", "8", "4", "−8"],
         "pareizi": 0,
         "padoms": "Tas pats punkts."},
    ], pamats=4),

    Zimejums("Ceļš caur nulli",
             taisne(-6, 4, 2, [(-5, "−5"), (0, "0"), (3, "3")]),
             paskaidro="No −5 līdz 0 ir 5 soļi, no 0 līdz 3 vēl 3 - kopā 8. "
                       "Tāpēc moduļus saskaita.",
             ievads="Ja skaitļi ir dažādās pusēs, ceļš iet caur nulli."),

    Kopsavilkums([
        "Nosaku attālumu starp diviem skaitļiem uz skaitļu taisnes.",
        "Saskaitu moduļus, ja skaitļi ir dažādās pusēs no nulles.",
        "Atņemu moduļus, ja tie ir vienā pusē.",
        "Zinu, ka attālums vienmēr ir pozitīvs.",
    ]),

    Majas([
        "Atrodi attālumu starp −11 un 4.",
        "Atrodi attālumu starp −11 un −4.",
        "Pieraksti divus skaitļus, kuru attālums ir tieši 10.",
    ]),
]
