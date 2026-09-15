# -*- coding: utf-8 -*-
"""Matemātika, 2. klase. 2.8. Kā reizina un dala ar 3, 4 un 5?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 2. klase, 2.8. temats): reizināšana ar 3,
4 un 5, reizinātāju pārvietojamība, dalīšana ar 2, 3, 4 un 5 (līdz 50, bez
atlikuma), saistība starp reizinājumu un dalījumu, darbību secība
vairākdarbību izteiksmē, jēdzieni «3, 4 vai 5 reizes vairāk/mazāk»,
trešdaļa, ceturtdaļa un piektdaļa.
"""

PRIEKSMETS = "Matemātika  |  2. klase"
TEMATS = "2.8."
NOSAUKUMS = "Kā reizina un dala ar 3, 4 un 5?"

ATGADNE = [
    "3 · 5 = 5 + 5 + 5 = 15   ·   reizinātājus var mainīt vietām:  "
    "4 · 3 = 3 · 4",
    "Dalīšana:  20 : 4 = 5, jo 4 · 5 = 20   ·   trešdaļa {1|3}, "
    "ceturtdaļa {1|4}, piektdaļa {1|5}",
    "Izteiksmē vispirms reizina un dala, tikai tad saskaita un atņem.",
]

FD = {
    "veids": "fd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 2.8. temata beigās. Pārbauda reizināšanu "
                "ar 3, 4 un 5, reizinātāju pārvietojamību, dalīšanu bez "
                "atlikuma, saistību starp reizinājumu un dalījumu, darbību "
                "secību, jēdzienus «reizes vairāk/mazāk» un daļas "
                "{1|3}, {1|4}, {1|5}.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro reizināšanas jēgu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē 3 · 5?",
              ["5 + 5 + 5", "5 + 3", "5 − 3", "5 : 3"], 0),
             ("Kā citādi pieraksta 4 + 4 + 4?",
              ["3 · 4", "4 · 4", "4 + 3", "4 : 3"], 0),
             ("Kā citādi pieraksta 5 · 3?",
              ["3 + 3 + 3 + 3 + 3", "3 + 5", "5 + 5 + 5", "5 − 3"], 0),
         ]},
        {"sr": "Reizina ar 3",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3 · 6?", ["15", "18", "21", "24"], 1),
             ("Cik ir 3 · 8?", ["21", "24", "27", "32"], 1),
             ("Cik ir 3 · 9?", ["24", "27", "30", "39"], 1),
         ]},
        {"sr": "Reizina ar 4",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 4 · 5?", ["16", "20", "24", "45"], 1),
             ("Cik ir 4 · 7?", ["24", "28", "32", "47"], 1),
             ("Cik ir 4 · 9?", ["32", "36", "40", "49"], 1),
         ]},
        {"sr": "Reizina ar 5",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 5 · 6?", ["25", "30", "35", "56"], 1),
             ("Cik ir 5 · 8?", ["35", "40", "45", "58"], 1),
             ("Cik ir 5 · 9?", ["40", "45", "50", "59"], 1),
         ]},
        {"sr": "Lieto reizinātāju pārvietojamību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zināms, ka 4 · 3 = 12. Cik ir 3 · 4?",
              ["7", "12", "34", "43"], 1),
             ("Kura vienādība ir patiesa?",
              ["5 · 3 = 3 · 5", "5 · 3 = 5 + 3", "5 · 3 = 3 : 5",
               "5 · 3 = 5 − 3"], 0),
             ("Kas notiek ar reizinājumu, ja reizinātājus maina vietām?",
              ["tas nemainās", "tas palielinās", "tas samazinās",
               "tas kļūst par dalījumu"], 0),
         ]},
        {"sr": "Dala ar 3",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 21 : 3?", ["6", "7", "8", "18"], 1),
             ("Cik ir 27 : 3?", ["7", "8", "9", "24"], 2),
             ("Cik ir 30 : 3?", ["3", "9", "10", "27"], 2),
         ]},
        {"sr": "Dala ar 4",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 24 : 4?", ["4", "6", "8", "20"], 1),
             ("Cik ir 36 : 4?", ["6", "8", "9", "32"], 2),
             ("Cik ir 40 : 4?", ["4", "8", "10", "36"], 2),
         ]},
        {"sr": "Dala ar 5",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 35 : 5?", ["5", "6", "7", "30"], 2),
             ("Cik ir 45 : 5?", ["7", "8", "9", "40"], 2),
             ("Cik ir 50 : 5?", ["5", "9", "10", "45"], 2),
         ]},
        {"sr": "Lieto saistību starp reizinājumu un dalījumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zināms, ka 4 · 6 = 24. Cik ir 24 : 4?",
              ["4", "6", "24", "28"], 1),
             ("Zināms, ka 5 · 7 = 35. Cik ir 35 : 7?",
              ["5", "7", "30", "35"], 0),
             ("Kā pārbaudīt, vai 32 : 4 = 8?",
              ["aprēķinot 4 · 8", "aprēķinot 32 + 4", "aprēķinot 32 − 8",
               "aprēķinot 8 : 4"], 0),
         ]},
        {"sr": "Ievēro darbību secību izteiksmē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 + 3 · 4?", ["14", "20", "24", "9"], 0),
             ("Cik ir 20 − 4 · 3?", ["8", "12", "48", "16"], 0),
             ("Kuru darbību izpilda vispirms izteiksmē 10 + 15 : 5?",
              ["dalīšanu", "saskaitīšanu", "vienalga kuru",
               "atņemšanu"], 0),
         ]},
        {"sr": "Lieto «3, 4 vai 5 reizes vairāk/mazāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir 3 reizes lielāks nekā 7?",
              ["10", "21", "24", "37"], 1),
             ("Kurš skaitlis ir 4 reizes mazāks nekā 28?",
              ["6", "7", "24", "32"], 1),
             ("Annai 5 lelles, Ievai 3 reizes vairāk. Cik ir Ievai?",
              ["8", "12", "15", "53"], 2),
         ]},
        {"sr": "Nosaka trešdaļu, ceturtdaļu un piektdaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta trešdaļu?",
              ["{1|3}", "{3|1}", "{1|4}", "{1|5}"], 0),
             ("Cik ir {1|4} no 20?", ["4", "5", "10", "80"], 1),
             ("Cik ir {1|5} no 45?", ["5", "9", "15", "40"], 1),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 2.8. temata noslēgumā. "
                "Pārbauda reizināšanu ar 3, 4 un 5, dalīšanu bez atlikuma, "
                "saistību starp reizinājumu un dalījumu, darbību secību, "
                "daļas noteikšanu no skaitļa un situāciju uzdevumus, kuros "
                "viens lielums ir vairākas reizes lielāks.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti un zīmē tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Reizina ar 3 un 4",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3 · 7?", ["18", "21", "24", "37"], 1),
             ("Cik ir 4 · 6?", ["20", "24", "28", "46"], 1),
             ("Cik ir 4 · 8?", ["28", "32", "36", "48"], 1),
         ]},
        {"sr": "Reizina ar 5",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 5 · 7?", ["30", "35", "40", "57"], 1),
             ("Cik ir 5 · 9?", ["40", "45", "50", "59"], 1),
             ("Cik ir 5 · 4?", ["16", "20", "25", "54"], 1),
         ]},
        {"sr": "Dala bez atlikuma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 24 : 3?", ["6", "7", "8", "21"], 2),
             ("Cik ir 32 : 4?", ["6", "7", "8", "28"], 2),
             ("Cik ir 40 : 5?", ["5", "7", "8", "35"], 2),
         ]},
        {"sr": "Lieto saistību starp reizinājumu un dalījumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zināms, ka 3 · 8 = 24. Cik ir 24 : 3?",
              ["3", "8", "21", "24"], 1),
             ("Zināms, ka 5 · 6 = 30. Cik ir 30 : 6?",
              ["5", "6", "24", "30"], 0),
             ("Kā pārbaudīt, vai 45 : 5 = 9?",
              ["aprēķinot 5 · 9", "aprēķinot 45 + 5", "aprēķinot 45 − 9",
               "aprēķinot 9 : 5"], 0),
         ]},
        {"sr": "Ievēro darbību secību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 5 + 4 · 3?", ["17", "27", "12", "20"], 0),
             ("Cik ir 30 − 5 · 4?", ["10", "20", "100", "25"], 0),
             ("Kuru darbību izpilda vispirms:  12 + 8 : 4?",
              ["dalīšanu", "saskaitīšanu", "vienalga kuru", "atņemšanu"], 0),
         ]},
        {"sr": "Nosaka daļu no skaitļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {1|3} no 15?", ["3", "5", "12", "45"], 1),
             ("Cik ir {1|4} no 24?", ["4", "6", "20", "96"], 1),
             ("Cik ir {1|5} no 35?", ["5", "7", "30", "40"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Reizina un dala ar 3, 4 un 5",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("3 · 7 = ……", "21"), ("4 · 8 = ……", "32"),
                         ("35 : 5 = ……", "7"), ("36 : 4 = ……", "9")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("3 · 9 = ……", "27"), ("5 · 6 = ……", "30"),
                         ("28 : 4 = ……", "7"), ("27 : 3 = ……", "9")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("4 · 7 = ……", "28"), ("5 · 8 = ……", "40"),
                         ("45 : 5 = ……", "9"), ("24 : 3 = ……", "8")]},
         ]},
        {"sr": "Aprēķina izteiksmes vērtību, ievērojot darbību secību",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Vispirms reizini un dali, tikai tad saskaiti un atņem! "
                      "Par katru pareizu atbildi — 1 punkts.",
              "rindas": [("4 + 3 · 5 = ……", "19"), ("20 − 4 · 4 = ……", "4"),
                         ("15 : 3 + 8 = ……", "13")]},
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Vispirms reizini un dali, tikai tad saskaiti un atņem! "
                      "Par katru pareizu atbildi — 1 punkts.",
              "rindas": [("6 + 4 · 3 = ……", "18"), ("30 − 5 · 3 = ……", "15"),
                         ("24 : 4 + 7 = ……", "13")]},
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Vispirms reizini un dali, tikai tad saskaiti un atņem! "
                      "Par katru pareizu atbildi — 1 punkts.",
              "rindas": [("9 + 5 · 4 = ……", "29"), ("40 − 3 · 6 = ……", "22"),
                         ("35 : 5 + 6 = ……", "13")]},
         ]},
        {"sr": "Risina uzdevumu, kurā viens lielums ir vairākas reizes "
               "lielāks",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par uzlīmēm",
              "vieta": 6.5,
              "ievads": "Annai ir 6 uzlīmes, bet Ilzei 4 reizes vairāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Pieraksti aprēķinu, cik uzlīmju ir Ilzei!", 1),
                       ("Aprēķini, cik uzlīmju ir abām kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Ilzes sloksnīte 4 reizes garāka.   (1 p.)",
                           "2) 4 · 6 = 24   (1 p.)",
                           "3) 6 + 24 = 30   (1 p.)",
                           "4) Atbilde: Ilzei 24; abām kopā 30 uzlīmes.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 6.5,
              "ievads": "Vienā plauktā ir 5 grāmatas, otrā 3 reizes vairāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Pieraksti aprēķinu, cik grāmatu ir otrajā "
                        "plauktā!", 1),
                       ("Aprēķini, cik grāmatu ir abos plauktos kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Otrā sloksnīte 3 reizes garāka.   (1 p.)",
                           "2) 3 · 5 = 15   (1 p.)",
                           "3) 5 + 15 = 20   (1 p.)",
                           "4) Atbilde: otrajā 15; abos kopā 20 grāmatas.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par ogām", "vieta": 6.5,
              "ievads": "Vienā groziņā ir 7 ogas, otrā 5 reizes vairāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Pieraksti aprēķinu, cik ogu ir otrajā groziņā!", 1),
                       ("Aprēķini, cik ogu ir abos groziņos kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Otrā sloksnīte 5 reizes garāka.   (1 p.)",
                           "2) 5 · 7 = 35   (1 p.)",
                           "3) 7 + 35 = 42   (1 p.)",
                           "4) Atbilde: otrajā 35; abos kopā 42 ogas.   "
                           "(1 p.)"]},
         ]},
        {"sr": "Nosaka daļu no skaitļa un pieraksta dalīšanu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Daļa no skaitļa", "vieta": 5.5,
              "ievads": "Klasē ir 20 skolēni. Ceturtdaļa no viņiem brauc "
                        "ekskursijā.",
              "jaut": [("Pieraksti, kā aprēķina {1|4} no 20!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik skolēnu nebrauc!", 1)],
              "atbildes": ["1) 20 : 4   (1 p.)", "2) 20 : 4 = 5   (1 p.)",
                           "3) 20 − 5 = 15 skolēni.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Daļa no skaitļa", "vieta": 5.5,
              "ievads": "Grozā ir 15 āboli. Trešdaļu no tiem apēda.",
              "jaut": [("Pieraksti, kā aprēķina {1|3} no 15!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik ābolu palika!", 1)],
              "atbildes": ["1) 15 : 3   (1 p.)", "2) 15 : 3 = 5   (1 p.)",
                           "3) 15 − 5 = 10 āboli.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Daļa no skaitļa", "vieta": 5.5,
              "ievads": "Maisā ir 25 riekstu. Piektdaļu no tiem izdalīja.",
              "jaut": [("Pieraksti, kā aprēķina {1|5} no 25!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik riekstu palika!", 1)],
              "atbildes": ["1) 25 : 5   (1 p.)", "2) 25 : 5 = 5   (1 p.)",
                           "3) 25 − 5 = 20 riekstu.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
