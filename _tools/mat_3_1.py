# -*- coding: utf-8 -*-
"""Matemātika, 3. klase. 3.1. Kā reizina un dala ar 6, 7, 8, 9 un 10?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 3. klase, 3.1. temats): reizināšana un
dalīšana reizināšanas tabulas apjomā, sakarības 1 · a = a, a : 1 = a,
0 · a = 0 un dalīšanas ar 0 neiespējamība, reizinātāju pārvietojamība,
divciparu skaitļa reizināšana un dalīšana ar viencipara skaitli pa desmitiem
un vieniem, viena un divu darbību situāciju uzdevumi.
"""

PRIEKSMETS = "Matemātika  |  3. klase"
TEMATS = "3.1."
NOSAUKUMS = "Kā reizina un dala ar 6, 7, 8, 9 un 10?"

ATGADNE = [
    "1 · a = a   ·   a : 1 = a   ·   0 · a = 0   ·   ar 0 dalīt nevar   ·   "
    "a · b = b · a",
    "Reizinot divciparu skaitli:  24 · 3 = 20 · 3 + 4 · 3 = 60 + 12 = 72",
    "Dalot divciparu skaitli:  84 : 4 = 80 : 4 + 4 : 4 = 20 + 1 = 21",
]

FD = {
    "veids": "fd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 3.1. temata beigās. Pārbauda reizināšanu "
                "un dalīšanu tabulas apjomā, sakarības ar 0 un 1, "
                "reizinātāju pārvietojamību, divciparu skaitļa reizināšanu "
                "un dalīšanu ar viencipara skaitli un situāciju uzdevumus.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Reizina ar 6",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 6 · 7?", ["36", "42", "48", "67"], 1),
             ("Cik ir 6 · 8?", ["42", "46", "48", "54"], 2),
             ("Cik ir 6 · 9?", ["48", "54", "56", "63"], 1),
         ]},
        {"sr": "Reizina ar 7",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 7 · 6?", ["36", "42", "48", "76"], 1),
             ("Cik ir 7 · 8?", ["48", "54", "56", "63"], 2),
             ("Cik ir 7 · 9?", ["56", "63", "72", "79"], 1),
         ]},
        {"sr": "Reizina ar 8 un 9",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 8 · 9?", ["64", "72", "81", "89"], 1),
             ("Cik ir 9 · 9?", ["72", "79", "81", "90"], 2),
             ("Cik ir 8 · 8?", ["56", "62", "64", "72"], 2),
         ]},
        {"sr": "Reizina ar 10",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 10 · 7?", ["17", "70", "77", "700"], 1),
             ("Cik ir 10 · 12?", ["22", "112", "120", "1200"], 2),
             ("Kas notiek ar skaitli, ja to reizina ar 10?",
              ["pieraksta vienu nulli", "pieskaita 10", "atņem 10",
               "skaitlis nemainās"], 0),
         ]},
        {"sr": "Zina sakarības ar 0 un 1",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 1 · 9?", ["0", "1", "9", "10"], 2),
             ("Cik ir 0 · 8?", ["0", "1", "8", "80"], 0),
             ("Kāpēc ar 0 dalīt nevar?",
              ["nav skaitļa, kas reizināts ar 0 dotu citu skaitli",
               "jo 0 ir mazs", "jo 0 nav skaitlis", "jo tā ir grūti"], 0),
         ]},
        {"sr": "Lieto reizinātāju pārvietojamību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē pieraksts a · b = b · a?",
              ["reizinātājus var mainīt vietām", "reizinājums palielinās",
               "reizinājums samazinās", "tā ir dalīšana"], 0),
             ("Zināms, ka 7 · 8 = 56. Cik ir 8 · 7?",
              ["15", "49", "56", "78"], 2),
             ("Kura vienādība ir patiesa?",
              ["6 · 9 = 9 · 6", "6 · 9 = 6 + 9", "6 · 9 = 9 : 6",
               "6 · 9 = 69"], 0),
         ]},
        {"sr": "Dala ar 6 un 7",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 42 : 6?", ["6", "7", "8", "36"], 1),
             ("Cik ir 56 : 7?", ["7", "8", "9", "49"], 1),
             ("Cik ir 63 : 7?", ["7", "8", "9", "56"], 2),
         ]},
        {"sr": "Dala ar 8, 9 un 10",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 72 : 8?", ["7", "8", "9", "64"], 2),
             ("Cik ir 81 : 9?", ["8", "9", "10", "72"], 1),
             ("Cik ir 90 : 10?", ["8", "9", "10", "80"], 1),
         ]},
        {"sr": "Lieto saistību starp reizinājumu un dalījumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zināms, ka 8 · 6 = 48. Cik ir 48 : 8?",
              ["6", "8", "40", "48"], 0),
             ("Zināms, ka 9 · 7 = 63. Cik ir 63 : 9?",
              ["7", "9", "54", "63"], 0),
             ("Kā pārbaudīt, vai 54 : 6 = 9?",
              ["aprēķinot 6 · 9", "aprēķinot 54 + 6", "aprēķinot 54 − 9",
               "aprēķinot 9 : 6"], 0),
         ]},
        {"sr": "Reizina divciparu skaitli ar viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 24 · 3?", ["62", "72", "74", "84"], 1),
             ("Cik ir 13 · 4?", ["42", "48", "52", "54"], 2),
             ("Cik ir 21 · 5?", ["85", "95", "105", "115"], 2),
         ]},
        {"sr": "Dala divciparu skaitli ar viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 84 : 4?", ["12", "21", "24", "42"], 1),
             ("Cik ir 96 : 3?", ["23", "32", "33", "36"], 1),
             ("Cik ir 66 : 6?", ["10", "11", "12", "16"], 1),
         ]},
        {"sr": "Risina situāciju uzdevumu ar reizināšanu vai dalīšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Viena biļete maksā 7 €. Cik maksā 8 biļetes?",
              ["15 €", "48 €", "56 €", "78 €"], 2),
             ("54 ābolus izdalīja 6 grozos vienādi. Cik katrā grozā?",
              ["8", "9", "10", "48"], 1),
             ("Klasē 6 rindas pa 4 soliem. Cik solu ir kopā?",
              ["10", "18", "24", "64"], 2),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 3.1. temata noslēgumā. "
                "Pārbauda reizināšanu un dalīšanu tabulas apjomā, sakarības "
                "ar 0 un 1, divciparu skaitļa reizināšanu un dalīšanu ar "
                "viencipara skaitli un divu darbību situāciju uzdevumus.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Reizina tabulas apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 6 · 8?", ["42", "46", "48", "54"], 2),
             ("Cik ir 7 · 7?", ["42", "47", "49", "56"], 2),
             ("Cik ir 9 · 8?", ["64", "72", "81", "98"], 1),
         ]},
        {"sr": "Dala tabulas apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 48 : 6?", ["6", "7", "8", "42"], 2),
             ("Cik ir 63 : 9?", ["6", "7", "8", "54"], 1),
             ("Cik ir 70 : 10?", ["6", "7", "8", "60"], 1),
         ]},
        {"sr": "Zina sakarības ar 0 un 1",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 1 · 7?", ["0", "1", "7", "8"], 2),
             ("Cik ir 0 · 9?", ["0", "1", "9", "90"], 0),
             ("Cik ir 8 : 1?", ["0", "1", "8", "18"], 2),
         ]},
        {"sr": "Reizina divciparu skaitli ar viencipara",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 32 · 3?", ["86", "92", "96", "98"], 2),
             ("Cik ir 14 · 5?", ["60", "70", "74", "80"], 1),
             ("Cik ir 23 · 4?", ["82", "86", "92", "94"], 2),
         ]},
        {"sr": "Dala divciparu skaitli ar viencipara",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 68 : 2?", ["24", "32", "34", "36"], 2),
             ("Cik ir 93 : 3?", ["13", "31", "33", "39"], 1),
             ("Cik ir 88 : 4?", ["18", "21", "22", "24"], 2),
         ]},
        {"sr": "Risina situāciju uzdevumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Viena grāmata maksā 6 €. Cik maksā 7 grāmatas?",
              ["13 €", "36 €", "42 €", "67 €"], 2),
             ("72 konfektes izdala 8 bērniem vienādi. Cik katram?",
              ["8", "9", "10", "64"], 1),
             ("5 kastes pa 9 olām. Cik olu kopā?",
              ["14", "40", "45", "59"], 2),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Reizina un dala tabulas apjomā",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("6 · 9 = ……", "54"), ("7 · 8 = ……", "56"),
                         ("72 : 9 = ……", "8"), ("60 : 10 = ……", "6")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("8 · 7 = ……", "56"), ("9 · 6 = ……", "54"),
                         ("81 : 9 = ……", "9"), ("42 : 7 = ……", "6")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("7 · 9 = ……", "63"), ("8 · 6 = ……", "48"),
                         ("64 : 8 = ……", "8"), ("90 : 9 = ……", "10")]},
         ]},
        {"sr": "Reizina un dala divciparu skaitli ar viencipara skaitli",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Reizini un dali atsevišķi desmitus un vienus! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("24 · 3 = ……", "72"), ("84 : 4 = ……", "21"),
                         ("13 · 5 = ……", "65")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Reizini un dali atsevišķi desmitus un vienus! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("32 · 3 = ……", "96"), ("66 : 3 = ……", "22"),
                         ("21 · 4 = ……", "84")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Reizini un dali atsevišķi desmitus un vienus! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("23 · 3 = ……", "69"), ("96 : 3 = ……", "32"),
                         ("12 · 4 = ……", "48")]},
         ]},
        {"sr": "Risina divu darbību situāciju uzdevumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par biļetēm",
              "vieta": 6.5,
              "ievads": "Viena biļete maksā 7 €. Klase nopirka 8 biļetes un "
                        "samaksāja ar 100 €.",
              "jaut": [("Pieraksti, kā aprēķināt biļešu cenu!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik naudas atdeva atpakaļ!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 8 · 7   (1 p.)", "2) 8 · 7 = 56 (€)   (1 p.)",
                           "3) 100 − 56 = 44 (€)   (1 p.)",
                           "4) Atbilde: biļetes maksā 56 €; atpakaļ atdeva "
                           "44 €.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par konfektēm",
              "vieta": 6.5,
              "ievads": "72 konfektes izdalīja vienādi 8 bērniem. Katrs bērns "
                        "3 konfektes apēda.",
              "jaut": [("Pieraksti, kā aprēķināt, cik konfekšu saņēma "
                        "katrs!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik konfekšu katram palika!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 72 : 8   (1 p.)", "2) 72 : 8 = 9   (1 p.)",
                           "3) 9 − 3 = 6   (1 p.)",
                           "4) Atbilde: katrs saņēma 9; palika 6 konfektes.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par olām", "vieta": 6.5,
              "ievads": "Veikalā ir 6 kastes pa 9 olām. 14 olas pārdeva.",
              "jaut": [("Pieraksti, kā aprēķināt olu skaitu!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik olu palika!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 6 · 9   (1 p.)", "2) 6 · 9 = 54   (1 p.)",
                           "3) 54 − 14 = 40   (1 p.)",
                           "4) Atbilde: bija 54 olas; palika 40.   (1 p.)"]},
         ]},
        {"sr": "Skaidro reizināšanas īpašības un sakarības",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Reizināšanas īpašības",
              "vieta": 5.5,
              "ievads": "Zināms, ka 6 · 8 = 48.",
              "jaut": [("Uzraksti vēl vienu patiesu reizinājumu ar tiem "
                        "pašiem skaitļiem!", 1),
                       ("Uzraksti divas patiesas dalīšanas vienādības!", 1),
                       ("Paskaidro, kāpēc ar 0 dalīt nevar!", 1)],
              "atbildes": ["1) 8 · 6 = 48   (1 p.)",
                           "2) 48 : 6 = 8 un 48 : 8 = 6   (1 p.)",
                           "3) Nav skaitļa, kuru reizinot ar 0, iegūtu "
                           "doto skaitli.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Reizināšanas īpašības",
              "vieta": 5.5,
              "ievads": "Zināms, ka 7 · 9 = 63.",
              "jaut": [("Uzraksti vēl vienu patiesu reizinājumu ar tiem "
                        "pašiem skaitļiem!", 1),
                       ("Uzraksti divas patiesas dalīšanas vienādības!", 1),
                       ("Paskaidro, ko nozīmē 1 · a = a!", 1)],
              "atbildes": ["1) 9 · 7 = 63   (1 p.)",
                           "2) 63 : 7 = 9 un 63 : 9 = 7   (1 p.)",
                           "3) Reizinot skaitli ar 1, tas nemainās.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Reizināšanas īpašības",
              "vieta": 5.5,
              "ievads": "Zināms, ka 8 · 5 = 40.",
              "jaut": [("Uzraksti vēl vienu patiesu reizinājumu ar tiem "
                        "pašiem skaitļiem!", 1),
                       ("Uzraksti divas patiesas dalīšanas vienādības!", 1),
                       ("Paskaidro, kāpēc 0 · a = 0!", 1)],
              "atbildes": ["1) 5 · 8 = 40   (1 p.)",
                           "2) 40 : 5 = 8 un 40 : 8 = 5   (1 p.)",
                           "3) Ja daudzumu ņem 0 reižu, iegūst 0.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
