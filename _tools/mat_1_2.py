# -*- coding: utf-8 -*-
"""Matemātika, 1. klase. 1.2. Cik kopā, cik palika?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 1. klase, 1.2. temats): skaitļa sastāvs
10 apjomā, saskaitīšana un atņemšana, skaitlis 0, zīmes «+», «−», «=»,
summa, starpība, izteiksme, patiesa un aplama vienādība, sadzīves situāciju
pieraksts ar darbību.
"""

PRIEKSMETS = "Matemātika  |  1. klase"
TEMATS = "1.2."
NOSAUKUMS = "Cik kopā, cik palika?"

ATGADNE = [
    "Skaitļi:  0  1  2  3  4  5  6  7  8  9  10",
    "+  saskaitīšana (cik kopā)   ·   −  atņemšana (cik palika)   ·   "
    "=  tikpat jeb vienāds ar",
    "Saskaitot iegūst summu   ·   atņemot iegūst starpību   ·   "
    "5 + 0 = 5   ·   5 − 0 = 5   ·   5 − 5 = 0",
]

FD = {
    "veids": "fd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 1.2. temata beigās. Pārbauda skaitļa "
                "sastāvu, saskaitīšanu un atņemšanu 10 apjomā, skaitli 0, "
                "summas un starpības jēdzienu, nezināmā locekļa noteikšanu, "
                "patiesu un aplamu vienādību un sadzīves situācijas "
                "pierakstu ar darbību.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosaka skaitļa sastāvu 10 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("5 = 2 + ……  Kurš skaitlis pietrūkst?", ["1", "2", "3", "4"], 2),
             ("7 = …… + 4  Kurš skaitlis pietrūkst?", ["2", "3", "4", "5"], 1),
             ("9 = 6 + ……  Kurš skaitlis pietrūkst?", ["2", "3", "4", "5"], 1),
         ]},
        {"sr": "Saskaita 10 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3 + 4?", ["5", "6", "7", "8"], 2),
             ("Cik ir 6 + 2?", ["7", "8", "9", "4"], 1),
             ("Cik ir 5 + 5?", ["9", "10", "11", "8"], 1),
         ]},
        {"sr": "Atņem 10 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 8 − 3?", ["4", "5", "6", "11"], 1),
             ("Cik ir 10 − 4?", ["5", "6", "7", "14"], 1),
             ("Cik ir 9 − 7?", ["1", "2", "3", "16"], 1),
         ]},
        {"sr": "Skaidro skaitli 0 saskaitīšanā un atņemšanā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 6 + 0?", ["0", "6", "7", "60"], 1),
             ("Cik ir 4 − 4?", ["0", "1", "4", "8"], 0),
             ("Ko nozīmē skaitlis 0?",
              ["necik, nav neviena", "vienu", "desmit", "daudz"], 0),
         ]},
        {"sr": "Zina zīmju «+», «−» un «=» nozīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme apzīmē saskaitīšanu?", ["+", "−", "=", "<"], 0),
             ("Kura zīme apzīmē atņemšanu?", ["+", "−", "=", ">"], 1),
             ("Ko parāda zīme «=»?",
              ["ka ir tikpat", "ka ir vairāk", "ka ir mazāk",
               "ka jāatņem"], 0),
         ]},
        {"sr": "Lieto jēdzienu «summa»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc rezultātu, ko iegūst saskaitot?",
              ["summa", "starpība", "skaitlis", "vienādība"], 0),
             ("Cik liela ir skaitļu 4 un 5 summa?", ["1", "8", "9", "45"], 2),
             ("Kurā izteiksmē ir summa?",
              ["7 − 2", "7 + 2", "7 = 7", "7 > 2"], 1),
         ]},
        {"sr": "Lieto jēdzienu «starpība»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc rezultātu, ko iegūst atņemot?",
              ["summa", "starpība", "vienādība", "izteiksme"], 1),
             ("Cik liela ir skaitļu 9 un 3 starpība?", ["3", "5", "6", "12"],
              2),
             ("Kurā izteiksmē ir starpība?",
              ["6 + 1", "6 − 1", "6 = 6", "6 < 8"], 1),
         ]},
        {"sr": "Nosaka nezināmo skaitli vienādībā",
         "stunda": TEMATS,
         "jautajumi": [
             ("4 + …… = 7  Kurš skaitlis jāieraksta?",
              ["2", "3", "4", "11"], 1),
             ("…… + 5 = 9  Kurš skaitlis jāieraksta?",
              ["3", "4", "5", "14"], 1),
             ("8 − …… = 6  Kurš skaitlis jāieraksta?",
              ["1", "2", "3", "14"], 1),
         ]},
        {"sr": "Pieraksta ar darbību situāciju, kurā kaut kas nāk klāt",
         "stunda": TEMATS,
         "jautajumi": [
             ("Uz zara sēdēja 5 putni, atlidoja vēl 3. Kā to pieraksta?",
              ["5 + 3", "5 − 3", "3 − 5", "5 = 3"], 0),
             ("Anna salika 4 klucīšus un vēl 2 klucīšus. Cik kopā?",
              ["2", "4", "6", "8"], 2),
             ("Kurš vārds norāda, ka jāsaskaita?",
              ["kopā", "palika", "aizgāja", "mazāk"], 0),
         ]},
        {"sr": "Pieraksta ar darbību situāciju, kurā kaut kas aiziet prom",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grozā bija 9 āboli, 4 apēda. Kā to pieraksta?",
              ["9 + 4", "9 − 4", "4 − 9", "9 = 4"], 1),
             ("Laukumā spēlējās 7 bērni, 3 aizgāja mājās. Cik palika?",
              ["3", "4", "5", "10"], 1),
             ("Kurš vārds norāda, ka jāatņem?",
              ["kopā", "pienāk klāt", "aiziet prom", "vēl"], 2),
         ]},
        {"sr": "Nosaka, vai vienādība ir patiesa vai aplama",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura vienādība ir patiesa?",
              ["3 + 4 = 8", "3 + 4 = 7", "3 + 4 = 6", "3 + 4 = 5"], 1),
             ("Kura vienādība ir aplama?",
              ["10 − 2 = 8", "6 + 2 = 8", "5 + 3 = 8", "9 − 2 = 8"], 3),
             ("Vienādība 2 + 5 = 7 ir …",
              ["patiesa", "aplama", "nezināma", "nepilnīga"], 0),
         ]},
        {"sr": "Skaidro, ka saskaitāmos var samainīt vietām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zināms, ka 3 + 6 = 9. Cik ir 6 + 3?",
              ["3", "6", "9", "12"], 2),
             ("Kurā rindā abas puses ir vienādas?",
              ["2 + 7 = 7 + 2", "2 + 7 = 7 − 2", "2 − 7 = 7 − 2",
               "2 + 7 = 9 + 2"], 0),
             ("Kas mainās, ja saskaitāmos samaina vietām?",
              ["nekas — summa ir tā pati", "summa kļūst lielāka",
               "summa kļūst mazāka", "iegūst starpību"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 1.2. temata noslēgumā. "
                "Pārbauda skaitļa sastāvu, saskaitīšanu un atņemšanu "
                "10 apjomā, skaitli 0, nezināmā locekļa noteikšanu, patiesu "
                "un aplamu vienādību un sadzīves situācijas pierakstu ar "
                "aritmētisko darbību.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Uzdevumu tekstu lasa skolotājs. Atbildi raksti un zīmē tam "
              "atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Saskaita 10 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 4 + 3?", ["6", "7", "8", "1"], 1),
             ("Cik ir 2 + 6?", ["7", "8", "9", "4"], 1),
             ("Cik ir 5 + 4?", ["8", "9", "10", "1"], 1),
         ]},
        {"sr": "Atņem 10 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 7 − 4?", ["2", "3", "4", "11"], 1),
             ("Cik ir 10 − 6?", ["3", "4", "5", "16"], 1),
             ("Cik ir 8 − 8?", ["0", "1", "8", "16"], 0),
         ]},
        {"sr": "Nosaka skaitļa sastāvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("6 = 2 + ……", ["3", "4", "5", "8"], 1),
             ("8 = …… + 5", ["2", "3", "4", "13"], 1),
             ("10 = 7 + ……", ["2", "3", "4", "17"], 1),
         ]},
        {"sr": "Skaidro skaitli 0",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 9 − 0?", ["0", "1", "9", "90"], 2),
             ("Cik ir 0 + 7?", ["0", "7", "8", "70"], 1),
             ("Kad iegūst 0?",
              ["kad skaitlim pieskaita to pašu skaitli",
               "kad no skaitļa atņem to pašu skaitli",
               "kad skaitlim pieskaita 1", "kad no skaitļa atņem 0"], 1),
         ]},
        {"sr": "Lieto jēdzienus «summa» un «starpība»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir skaitļu 3 un 6 summa?", ["3", "8", "9", "36"], 2),
             ("Cik liela ir skaitļu 8 un 2 starpība?",
              ["4", "6", "10", "82"], 1),
             ("Kurā izteiksmē ir starpība?",
              ["4 + 4", "4 − 4", "4 = 4", "4 < 8"], 1),
         ]},
        {"sr": "Nosaka, vai vienādība ir patiesa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura vienādība ir patiesa?",
              ["5 + 2 = 6", "5 + 2 = 7", "5 + 2 = 8", "5 + 2 = 9"], 1),
             ("Kura vienādība ir aplama?",
              ["9 − 3 = 6", "4 + 2 = 6", "10 − 4 = 6", "3 + 2 = 6"], 3),
             ("Vienādība 6 − 1 = 4 ir …",
              ["patiesa", "aplama", "gan patiesa, gan aplama",
               "nav vienādība"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita un atņem 10 apjomā",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("3 + 5 = ……", "8"), ("9 − 4 = ……", "5"),
                         ("6 + 4 = ……", "10"), ("7 − 7 = ……", "0")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("4 + 4 = ……", "8"), ("8 − 5 = ……", "3"),
                         ("2 + 8 = ……", "10"), ("6 + 0 = ……", "6")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("5 + 2 = ……", "7"), ("10 − 3 = ……", "7"),
                         ("1 + 9 = ……", "10"), ("9 − 9 = ……", "0")]},
         ]},
        {"sr": "Nosaka nezināmo skaitli vienādībā",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti tukšajā vietā skaitli tā, lai vienādība būtu "
                      "patiesa! Par katru pareizu skaitli — 1 punkts.",
              "rindas": [("5 + …… = 9", "4"), ("…… + 3 = 8", "5"),
                         ("7 − …… = 2", "5")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti tukšajā vietā skaitli tā, lai vienādība būtu "
                      "patiesa! Par katru pareizu skaitli — 1 punkts.",
              "rindas": [("6 + …… = 10", "4"), ("…… + 2 = 7", "5"),
                         ("9 − …… = 5", "4")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti tukšajā vietā skaitli tā, lai vienādība būtu "
                      "patiesa! Par katru pareizu skaitli — 1 punkts.",
              "rindas": [("3 + …… = 8", "5"), ("…… + 6 = 9", "3"),
                         ("10 − …… = 4", "6")]},
         ]},
        {"sr": "Modelē skaitļa sastāvu un pieraksta to kā summu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Skaitļa 7 sastāvs", "vieta": 6.5,
              "ievads": "Zīmē ripas un pieraksti summas!",
              "jaut": [("Uzzīmē 7 ripas divās grupās!", 1),
                       ("Pieraksti summu, kas atbilst tavam zīmējumam!", 1),
                       ("Pieraksti vēl divas citas summas, kuru vērtība "
                        "ir 7!", 2)],
              "atbildes": [
                  "1) Uzzīmētas 7 ripas, sadalītas divās grupās.   (1 p.)",
                  "2) Pierakstīta summa, kas atbilst zīmējumam, "
                  "piemēram, 3 + 4 = 7.   (1 p.)",
                  "3) Divas citas patiesas summas, piemēram, 5 + 2 = 7 un "
                  "6 + 1 = 7.   (2 p.)"]},
             {"tips": "jautajumi", "virs": "Skaitļa 8 sastāvs", "vieta": 6.5,
              "ievads": "Zīmē ripas un pieraksti summas!",
              "jaut": [("Uzzīmē 8 ripas divās grupās!", 1),
                       ("Pieraksti summu, kas atbilst tavam zīmējumam!", 1),
                       ("Pieraksti vēl divas citas summas, kuru vērtība "
                        "ir 8!", 2)],
              "atbildes": [
                  "1) Uzzīmētas 8 ripas, sadalītas divās grupās.   (1 p.)",
                  "2) Pierakstīta summa, kas atbilst zīmējumam, "
                  "piemēram, 5 + 3 = 8.   (1 p.)",
                  "3) Divas citas patiesas summas, piemēram, 6 + 2 = 8 un "
                  "4 + 4 = 8.   (2 p.)"]},
             {"tips": "jautajumi", "virs": "Skaitļa 9 sastāvs", "vieta": 6.5,
              "ievads": "Zīmē ripas un pieraksti summas!",
              "jaut": [("Uzzīmē 9 ripas divās grupās!", 1),
                       ("Pieraksti summu, kas atbilst tavam zīmējumam!", 1),
                       ("Pieraksti vēl divas citas summas, kuru vērtība "
                        "ir 9!", 2)],
              "atbildes": [
                  "1) Uzzīmētas 9 ripas, sadalītas divās grupās.   (1 p.)",
                  "2) Pierakstīta summa, kas atbilst zīmējumam, "
                  "piemēram, 4 + 5 = 9.   (1 p.)",
                  "3) Divas citas patiesas summas, piemēram, 6 + 3 = 9 un "
                  "7 + 2 = 9.   (2 p.)"]},
         ]},
        {"sr": "Sadzīves situāciju pieraksta ar darbību un atbild uz "
               "jautājumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par putniem",
              "vieta": 5.5,
              "ievads": "Uz zara sēdēja 6 putni. Atlidoja vēl 3 putni.",
              "jaut": [("Pieraksti darbību!", 1),
                       ("Aprēķini, cik putnu ir kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 6 + 3   (1 p.)", "2) 6 + 3 = 9   (1 p.)",
                           "3) Atbilde: kopā ir 9 putni.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par āboliem",
              "vieta": 5.5,
              "ievads": "Grozā bija 8 āboli. 5 ābolus apēda.",
              "jaut": [("Pieraksti darbību!", 1),
                       ("Aprēķini, cik ābolu palika!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 8 − 5   (1 p.)", "2) 8 − 5 = 3   (1 p.)",
                           "3) Atbilde: palika 3 āboli.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par bērniem",
              "vieta": 5.5,
              "ievads": "Laukumā spēlējās 9 bērni. 4 bērni aizgāja mājās.",
              "jaut": [("Pieraksti darbību!", 1),
                       ("Aprēķini, cik bērnu palika!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 9 − 4   (1 p.)", "2) 9 − 4 = 5   (1 p.)",
                           "3) Atbilde: palika 5 bērni.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
