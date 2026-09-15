# -*- coding: utf-8 -*-
"""Matemātika, 3. klase. 3.2. Kā izmanto visas darbības?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 3. klase, 3.2. temats): četras darbības
100 apjomā, vairākdarbību izteiksmes un darbību secība (iekavas, tad
reizināšana un dalīšana, tad saskaitīšana un atņemšana), situācijas
pieraksts ar izteiksmi, taisnstūra perimetra formula un tas, ka figūras ar
vienādu perimetru var atšķirties.
"""

PRIEKSMETS = "Matemātika  |  3. klase"
TEMATS = "3.2."
NOSAUKUMS = "Kā izmanto visas darbības?"

ATGADNE = [
    "Darbību secība:  1) iekavas,  2) reizināšana un dalīšana,  "
    "3) saskaitīšana un atņemšana",
    "Taisnstūra perimetrs:  P = 2 · (a + b)   ·   kvadrātam  P = 4 · a",
    "Figūrām ar vienādu perimetru var būt dažāda forma.",
]

FD = {
    "veids": "fd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 3.2. temata beigās. Pārbauda četras "
                "darbības 100 apjomā, darbību secību un iekavas, izteiksmes "
                "vērtības aprēķinu, situācijas pierakstu ar izteiksmi un "
                "taisnstūra perimetra formulu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina darbību secību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kuru darbību izpilda vispirms izteiksmē 4 + 3 · 5?",
              ["reizināšanu", "saskaitīšanu", "vienalga kuru",
               "atņemšanu"], 0),
             ("Kuru darbību izpilda vispirms izteiksmē (8 + 2) · 3?",
              ["iekavās esošo", "reizināšanu", "vienalga kuru",
               "dalīšanu"], 0),
             ("Kāda ir pareizā darbību secība?",
              ["iekavas, reizināšana un dalīšana, saskaitīšana un atņemšana",
               "saskaitīšana, reizināšana, iekavas",
               "no labās puses uz kreiso", "vienalga kāda"], 0),
         ]},
        {"sr": "Aprēķina izteiksmi ar reizināšanu un saskaitīšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 4 + 3 · 5?", ["19", "23", "35", "60"], 0),
             ("Cik ir 6 · 4 + 10?", ["34", "40", "60", "64"], 0),
             ("Cik ir 20 + 5 · 6?", ["50", "56", "70", "150"], 0),
         ]},
        {"sr": "Aprēķina izteiksmi ar dalīšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 30 : 5 + 8?", ["14", "16", "38", "46"], 0),
             ("Cik ir 40 − 24 : 4?", ["4", "34", "36", "38"], 1),
             ("Cik ir 9 + 36 : 6?", ["15", "18", "45", "54"], 0),
         ]},
        {"sr": "Aprēķina izteiksmi ar iekavām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir (8 + 2) · 3?", ["14", "26", "30", "38"], 2),
             ("Cik ir (20 − 5) : 3?", ["5", "15", "18", "45"], 0),
             ("Cik ir 50 − (10 + 15)?", ["15", "25", "35", "75"], 1),
         ]},
        {"sr": "Salīdzina izteiksmes ar iekavām un bez tām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 + 3 · 4?", ["14", "20", "24", "9"], 0),
             ("Cik ir (2 + 3) · 4?", ["14", "20", "24", "9"], 1),
             ("Kāpēc abu izteiksmju vērtības atšķiras?",
              ["iekavas maina darbību secību", "skaitļi ir dažādi",
               "viena ir aplama", "tās neatšķiras"], 0),
         ]},
        {"sr": "Veic četras darbības 100 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 48 + 27?", ["65", "71", "75", "85"], 2),
             ("Cik ir 83 − 46?", ["37", "43", "47", "39"], 0),
             ("Cik ir 90 : 9 + 15?", ["10", "24", "25", "26"], 2),
         ]},
        {"sr": "Nosaka nezināmo skaitli izteiksmē",
         "stunda": TEMATS,
         "jautajumi": [
             ("…… · 6 = 42  Kurš skaitlis jāieraksta?", ["6", "7", "8", "36"],
              1),
             ("56 : …… = 8  Kurš skaitlis jāieraksta?", ["6", "7", "8", "48"],
              1),
             ("(…… + 5) · 2 = 20  Kurš skaitlis jāieraksta?",
              ["5", "10", "15", "25"], 0),
         ]},
        {"sr": "Pieraksta situāciju ar vairākdarbību izteiksmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Nopirka 3 burtnīcas pa 2 € un 1 pildspalvu par 4 €. Kura "
              "izteiksme der?",
              ["3 · 2 + 4", "3 + 2 · 4", "(3 + 2) · 4", "3 · (2 + 4)"], 0),
             ("Bija 50 €, nopirka 4 biļetes pa 7 €. Kura izteiksme der?",
              ["50 − 4 · 7", "50 − 4 + 7", "(50 − 4) · 7", "50 · 4 − 7"], 0),
             ("24 ābolus sadalīja 4 grozos, tad no viena paņēma 2. Kura "
              "izteiksme der?",
              ["24 : 4 − 2", "24 − 4 : 2", "(24 − 4) : 2", "24 : (4 − 2)"], 0),
         ]},
        {"sr": "Zina taisnstūra perimetra formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāda ir taisnstūra perimetra formula?",
              ["P = 2 · (a + b)", "P = a · b", "P = a + b", "P = 4 · a"], 0),
             ("Kāda ir kvadrāta perimetra formula?",
              ["P = 4 · a", "P = 2 · a", "P = a · a", "P = a + 4"], 0),
             ("Ko nozīmē burti a un b formulā?",
              ["malu garumus", "virsotņu skaitu", "laukumu", "perimetru"], 0),
         ]},
        {"sr": "Aprēķina taisnstūra perimetru pēc formulas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūra malas 7 cm un 3 cm. Cik liels ir perimetrs?",
              ["10 cm", "20 cm", "21 cm", "24 cm"], 1),
             ("Taisnstūra malas 9 cm un 6 cm. Cik liels ir perimetrs?",
              ["15 cm", "24 cm", "30 cm", "54 cm"], 2),
             ("Kvadrāta mala 8 cm. Cik liels ir perimetrs?",
              ["16 cm", "24 cm", "32 cm", "64 cm"], 2),
         ]},
        {"sr": "Nosaka malu, ja zināms perimetrs",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kvadrāta perimetrs ir 24 cm. Cik gara ir mala?",
              ["4 cm", "6 cm", "8 cm", "12 cm"], 1),
             ("Taisnstūra perimetrs 20 cm, viena mala 6 cm. Cik gara ir "
              "otra?",
              ["3 cm", "4 cm", "7 cm", "14 cm"], 1),
             ("Kvadrāta perimetrs ir 36 cm. Cik gara ir mala?",
              ["6 cm", "9 cm", "12 cm", "18 cm"], 1),
         ]},
        {"sr": "Skaidro, ka figūras ar vienādu perimetru var atšķirties",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai diviem taisnstūriem ar vienādu perimetru vienmēr ir "
              "vienāda forma?",
              ["nē", "jā", "vienmēr", "tikai kvadrātiem"], 0),
             ("Taisnstūriem 1 × 5 un 2 × 4 perimetrs ir …",
              ["vienāds — 12", "dažāds", "vienāds — 10", "vienāds — 20"], 0),
             ("Ko var teikt par diviem taisnstūriem ar perimetru 16 cm?",
              ["to malas var būt dažādas", "tie ir vienādi",
               "abi ir kvadrāti", "to laukumi ir vienādi"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 3.2. temata noslēgumā. "
                "Pārbauda četras darbības 100 apjomā, darbību secību un "
                "iekavas, situācijas pierakstu ar vairākdarbību izteiksmi, "
                "taisnstūra perimetra aprēķinu un figūru salīdzināšanu pēc "
                "perimetra.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti un zīmē tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina darbību secību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kuru darbību izpilda vispirms:  5 + 4 · 2?",
              ["reizināšanu", "saskaitīšanu", "vienalga kuru",
               "atņemšanu"], 0),
             ("Kuru darbību izpilda vispirms:  (7 + 3) : 2?",
              ["iekavās esošo", "dalīšanu", "vienalga kuru",
               "saskaitīšanu"], 0),
             ("Kura secība ir pareiza?",
              ["iekavas, reizināšana un dalīšana, saskaitīšana un atņemšana",
               "saskaitīšana, iekavas, reizināšana",
               "no labās uz kreiso", "vienalga kāda"], 0),
         ]},
        {"sr": "Aprēķina izteiksmes vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 6 + 4 · 5?", ["26", "50", "30", "46"], 0),
             ("Cik ir 45 : 5 + 12?", ["21", "24", "33", "57"], 0),
             ("Cik ir 60 − 3 · 8?", ["36", "24", "48", "456"], 0),
         ]},
        {"sr": "Aprēķina izteiksmi ar iekavām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir (9 + 6) · 2?", ["21", "24", "30", "33"], 2),
             ("Cik ir (40 − 10) : 5?", ["6", "8", "30", "38"], 0),
             ("Cik ir 80 − (25 + 15)?", ["30", "40", "50", "120"], 1),
         ]},
        {"sr": "Veic četras darbības 100 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 56 + 38?", ["84", "92", "94", "104"], 2),
             ("Cik ir 72 − 45?", ["27", "33", "37", "117"], 0),
             ("Cik ir 7 · 8 − 16?", ["40", "42", "48", "56"], 0),
         ]},
        {"sr": "Aprēķina perimetru pēc formulas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūra malas 8 cm un 5 cm. Perimetrs?",
              ["13 cm", "26 cm", "36 cm", "40 cm"], 1),
             ("Kvadrāta mala 7 cm. Perimetrs?",
              ["14 cm", "21 cm", "28 cm", "49 cm"], 2),
             ("Kāda ir taisnstūra perimetra formula?",
              ["P = 2 · (a + b)", "P = a · b", "P = a + b", "P = 4 · a"], 0),
         ]},
        {"sr": "Nosaka malu, ja zināms perimetrs",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kvadrāta perimetrs 28 cm. Mala?",
              ["4 cm", "7 cm", "14 cm", "112 cm"], 1),
             ("Taisnstūra perimetrs 24 cm, viena mala 8 cm. Otra mala?",
              ["3 cm", "4 cm", "8 cm", "16 cm"], 1),
             ("Vai taisnstūriem ar vienādu perimetru ir vienāda forma?",
              ["ne vienmēr", "vienmēr", "nekad", "tikai kvadrātiem"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina izteiksmju vērtības, ievērojot darbību secību",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Ievēro darbību secību! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("5 + 6 · 4 = ……", "29"), ("(12 + 8) : 4 = ……", "5"),
                         ("50 − 3 · 9 = ……", "23"),
                         ("36 : 6 + 14 = ……", "20")]},
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Ievēro darbību secību! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("8 + 5 · 6 = ……", "38"), ("(25 + 5) : 5 = ……", "6"),
                         ("70 − 4 · 8 = ……", "38"),
                         ("48 : 8 + 17 = ……", "23")]},
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Ievēro darbību secību! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("7 + 9 · 3 = ……", "34"), ("(30 + 6) : 6 = ……", "6"),
                         ("90 − 7 · 7 = ……", "41"),
                         ("54 : 9 + 25 = ……", "31")]},
         ]},
        {"sr": "Aprēķina taisnstūra un kvadrāta perimetru",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini perimetru",
              "note": "Lieto formulu P = 2 · (a + b)! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Taisnstūris 6 cm un 4 cm:  P = ……", "20 cm"),
                         ("Kvadrāts ar malu 9 cm:  P = ……", "36 cm"),
                         ("Kvadrāta perimetrs 32 cm; mala = ……", "8 cm")]},
             {"tips": "parveide", "virs": "Aprēķini perimetru",
              "note": "Lieto formulu P = 2 · (a + b)! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Taisnstūris 9 cm un 5 cm:  P = ……", "28 cm"),
                         ("Kvadrāts ar malu 6 cm:  P = ……", "24 cm"),
                         ("Kvadrāta perimetrs 20 cm; mala = ……", "5 cm")]},
             {"tips": "parveide", "virs": "Aprēķini perimetru",
              "note": "Lieto formulu P = 2 · (a + b)! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Taisnstūris 10 cm un 3 cm:  P = ……", "26 cm"),
                         ("Kvadrāts ar malu 11 cm:  P = ……", "44 cm"),
                         ("Kvadrāta perimetrs 40 cm; mala = ……", "10 cm")]},
         ]},
        {"sr": "Pieraksta situāciju ar vairākdarbību izteiksmi",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par pirkumu",
              "vieta": 6.5,
              "ievads": "Nopirka 4 burtnīcas pa 3 € un vienu somu par 25 €. "
                        "Samaksāja ar 50 €.",
              "jaut": [("Pieraksti pirkumu ar vienu izteiksmi!", 1),
                       ("Aprēķini, cik maksā viss pirkums!", 1),
                       ("Aprēķini, cik naudas atdeva atpakaļ!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 4 · 3 + 25   (1 p.)",
                           "2) 4 · 3 + 25 = 12 + 25 = 37 (€)   (1 p.)",
                           "3) 50 − 37 = 13 (€)   (1 p.)",
                           "4) Atbilde: pirkums 37 €; atlikums 13 €.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par ekskursiju",
              "vieta": 6.5,
              "ievads": "Ekskursijā brauc 5 grupas pa 6 skolēniem. Autobusā "
                        "ir 40 vietas.",
              "jaut": [("Pieraksti skolēnu skaitu ar izteiksmi!", 1),
                       ("Aprēķini, cik skolēnu brauc!", 1),
                       ("Aprēķini, cik vietu autobusā paliks brīvas!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 5 · 6   (1 p.)", "2) 5 · 6 = 30   (1 p.)",
                           "3) 40 − 30 = 10   (1 p.)",
                           "4) Atbilde: brauc 30 skolēni; brīvas 10 vietas.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par āboliem",
              "vieta": 6.5,
              "ievads": "48 ābolus izdalīja vienādi 6 grozos. Divus grozus "
                        "aizveda projām.",
              "jaut": [("Pieraksti, cik ābolu ir vienā grozā!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik ābolu aizveda projām!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 48 : 6   (1 p.)", "2) 48 : 6 = 8   (1 p.)",
                           "3) 2 · 8 = 16   (1 p.)",
                           "4) Atbilde: grozā 8 āboli; aizveda 16.   "
                           "(1 p.)"]},
         ]},
        {"sr": "Salīdzina figūras ar vienādu perimetru",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Vienāds perimetrs", "vieta": 5.5,
              "ievads": "Taisnstūra perimetrs ir 16 cm.",
              "jaut": [("Uzzīmē rūtiņās vienu tādu taisnstūri!", 1),
                       ("Uzzīmē citu taisnstūri ar to pašu perimetru!", 1),
                       ("Uzraksti abu malu garumus!", 1)],
              "atbildes": ["1) Piemēram, 5 × 3 rūtiņas.   (1 p.)",
                           "2) Piemēram, 6 × 2 rūtiņas.   (1 p.)",
                           "3) Pierakstīti abi malu pāri; abiem P = 16.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Vienāds perimetrs", "vieta": 5.5,
              "ievads": "Taisnstūra perimetrs ir 20 cm.",
              "jaut": [("Uzzīmē rūtiņās vienu tādu taisnstūri!", 1),
                       ("Uzzīmē citu taisnstūri ar to pašu perimetru!", 1),
                       ("Uzraksti abu malu garumus!", 1)],
              "atbildes": ["1) Piemēram, 6 × 4 rūtiņas.   (1 p.)",
                           "2) Piemēram, 7 × 3 rūtiņas.   (1 p.)",
                           "3) Pierakstīti abi malu pāri; abiem P = 20.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Vienāds perimetrs", "vieta": 5.5,
              "ievads": "Taisnstūra perimetrs ir 24 cm.",
              "jaut": [("Uzzīmē rūtiņās vienu tādu taisnstūri!", 1),
                       ("Uzzīmē kvadrātu ar to pašu perimetru!", 1),
                       ("Uzraksti abu figūru malu garumus!", 1)],
              "atbildes": ["1) Piemēram, 8 × 4 rūtiņas.   (1 p.)",
                           "2) Kvadrāts ar malu 6 rūtiņas.   (1 p.)",
                           "3) Pierakstīti malu garumi; abiem P = 24.   "
                           "(1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
