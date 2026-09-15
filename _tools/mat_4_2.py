# -*- coding: utf-8 -*-
"""Matemātika, 4. klase. 4.2. Kā daudzciparu skaitļus reizina un dala ar
viencipara skaitli?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 4. klase, 4.2. temats): divciparu un
trīsciparu skaitļa reizināšana un dalīšana ar viencipara skaitli, reizinātāju
maiņa vietām un skaitļa sadalīšana reizinātājos, dalīšana ar atlikumu,
aptuvenā vērtība rezultāta pārbaudei, «tik reižu vairāk/mazāk» un situāciju
uzdevumi.
"""

PRIEKSMETS = "Matemātika  |  4. klase"
TEMATS = "4.2."
NOSAUKUMS = "Kā daudzciparu skaitļus reizina un dala ar viencipara skaitli?"

ATGADNE = [
    "Reizinot pa šķirām:  243 · 3 = 200 · 3 + 40 · 3 + 3 · 3 = 600 + 120 + "
    "9 = 729",
    "Dalot pa šķirām:  486 : 2 = 400 : 2 + 80 : 2 + 6 : 2 = 200 + 40 + "
    "3 = 243",
    "Dalot ar atlikumu:  17 : 5 = 3 (atlikums 2), jo 5 · 3 + 2 = 17",
]

FD = {
    "veids": "fd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 4.2. temata beigās. Pārbauda divciparu un "
                "trīsciparu skaitļa reizināšanu un dalīšanu ar viencipara "
                "skaitli, vairāku skaitļu reizinājumu, dalīšanu ar atlikumu, "
                "aptuveno vērtību un uzdevumus par «tik reižu vairāk».",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Reizina divciparu skaitli ar viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 24 · 3?", ["62", "72", "82", "94"], 1),
             ("Cik ir 36 · 4?", ["124", "134", "144", "154"], 2),
             ("Cik ir 48 · 5?", ["230", "240", "250", "280"], 1),
         ]},
        {"sr": "Reizina trīsciparu skaitli ar viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 243 · 3?", ["629", "719", "729", "739"], 2),
             ("Cik ir 152 · 4?", ["508", "598", "608", "618"], 2),
             ("Cik ir 214 · 5?", ["1060", "1070", "1170", "1080"], 1),
         ]},
        {"sr": "Skaidro reizināšanu pa šķirām",
         "stunda": TEMATS,
         "jautajumi": [
             ("243 · 3 = 200 · 3 + 40 · 3 + ……  Kas pietrūkst?",
              ["3 · 3", "4 · 3", "24 · 3", "3 + 3"], 0),
             ("Kā ērtāk reizināt 125 · 4?",
              ["pa šķirām: 100 · 4 + 20 · 4 + 5 · 4", "saskaitot 125 + 4",
               "atņemot 125 − 4", "dalot 125 : 4"], 0),
             ("Kāpēc reizinot dažkārt jāveic pāreja citā desmitā?",
              ["jo vienu reizinājums var būt lielāks nekā 9",
               "jo skaitlis ir liels", "jo tā ir noteikums",
               "jo reizinātājs ir nepāra"], 0),
         ]},
        {"sr": "Dala divciparu skaitli ar viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 84 : 4?", ["19", "21", "22", "24"], 1),
             ("Cik ir 96 : 6?", ["14", "16", "18", "26"], 1),
             ("Cik ir 75 : 5?", ["13", "15", "17", "25"], 1),
         ]},
        {"sr": "Dala trīsciparu skaitli ar viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 486 : 2?", ["223", "233", "243", "253"], 2),
             ("Cik ir 639 : 3?", ["203", "213", "223", "233"], 1),
             ("Cik ir 850 : 5?", ["150", "160", "170", "180"], 2),
         ]},
        {"sr": "Nosaka triju un četru skaitļu reizinājumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 · 5 · 12?", ["100", "110", "120", "140"], 2),
             ("Cik ir 25 · 2 · 3?", ["120", "130", "150", "160"], 2),
             ("Kā ērtāk aprēķināt 5 · 17 · 2?",
              ["vispirms 5 · 2", "vispirms 17 · 2", "tikai pēc kārtas",
               "nav nozīmes"], 0),
         ]},
        {"sr": "Sadala skaitli reizinātājos, lai atvieglotu aprēķinu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā var pierakstīt 25 · 6, izmantojot sadalīšanu?",
              ["25 · 2 · 3", "25 + 6", "25 : 6", "25 · 6 · 2"], 0),
             ("Cik ir 25 · 6?", ["120", "130", "150", "160"], 2),
             ("Kā ērtāk aprēķināt 16 · 5?",
              ["8 · 2 · 5", "16 + 5", "16 : 5", "16 · 5 · 2"], 0),
         ]},
        {"sr": "Dala ar atlikumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 17 : 5?",
              ["3 un atlikums 2", "3 un atlikums 1", "4 un atlikums 1",
               "2 un atlikums 7"], 0),
             ("Cik ir 29 : 4?",
              ["7 un atlikums 1", "6 un atlikums 5", "7 un atlikums 2",
               "8 un atlikums 3"], 0),
             ("Cik ir 45 : 7?",
              ["6 un atlikums 3", "5 un atlikums 10", "6 un atlikums 2",
               "7 un atlikums 4"], 0),
         ]},
        {"sr": "Skaidro dalīšanu ar atlikumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds var būt atlikums, dalot ar 5?",
              ["no 0 līdz 4", "no 0 līdz 5", "jebkurš", "tikai 1"], 0),
             ("Kā pārbaudīt dalīšanu ar atlikumu 23 : 4 = 5 (atl. 3)?",
              ["4 · 5 + 3", "4 · 5 − 3", "23 + 3", "23 − 5"], 0),
             ("Ko nozīmē atlikums?",
              ["cik paliek pāri pēc vienādas sadalīšanas", "cik reižu ietilpst",
               "cik kopā", "cik vairāk"], 0),
         ]},
        {"sr": "Nosaka reizinājuma un dalījuma aptuveno vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aptuveni cik ir 198 · 5?",
              ["ap 500", "ap 1000", "ap 2000", "ap 100"], 1),
             ("Aptuveni cik ir 612 : 3?",
              ["ap 20", "ap 200", "ap 2000", "ap 600"], 1),
             ("Skolēns ieguva 24 · 3 = 612. Kāpēc tas nav ticami?",
              ["rezultātam jābūt ap 70", "rezultātam jābūt ap 600",
               "rezultāts ir pareizs", "nevar novērtēt"], 0),
         ]},
        {"sr": "Lieto «tik reižu vairāk» un «tik reižu mazāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir 4 reizes lielāks nekā 35?",
              ["120", "130", "140", "150"], 2),
             ("Kurš skaitlis ir 3 reizes mazāks nekā 96?",
              ["24", "32", "36", "288"], 1),
             ("Vienā kastē 45 olas, otrā 3 reizes vairāk. Cik otrā?",
              ["125", "135", "145", "15"], 1),
         ]},
        {"sr": "Risina situāciju uzdevumu ar reizināšanu vai dalīšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Viena biļete maksā 12 €. Cik maksā 6 biļetes?",
              ["62 €", "72 €", "82 €", "18 €"], 1),
             ("372 grāmatas sadalīja 4 plauktos vienādi. Cik vienā plauktā?",
              ["83", "93", "97", "103"], 1),
             ("Autobusā 48 vietas. Cik cilvēku ietilps 3 autobusos?",
              ["124", "134", "144", "154"], 2),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 4.2. temata noslēgumā. "
                "Pārbauda reizināšanu un dalīšanu ar viencipara skaitli, "
                "dalīšanu ar atlikumu, aptuveno vērtību, uzdevumus par «tik "
                "reižu vairāk/mazāk» un risinājuma pierakstu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti un zīmē tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Reizina ar viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 34 · 3?", ["92", "102", "112", "122"], 1),
             ("Cik ir 126 · 4?", ["484", "494", "504", "514"], 2),
             ("Cik ir 215 · 3?", ["635", "645", "655", "665"], 1),
         ]},
        {"sr": "Dala ar viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 96 : 4?", ["22", "24", "26", "28"], 1),
             ("Cik ir 648 : 2?", ["314", "324", "334", "344"], 1),
             ("Cik ir 735 : 5?", ["137", "147", "157", "167"], 1),
         ]},
        {"sr": "Dala ar atlikumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 23 : 4?",
              ["5 un atlikums 3", "5 un atlikums 2", "6 un atlikums 1",
               "4 un atlikums 7"], 0),
             ("Cik ir 38 : 6?",
              ["6 un atlikums 2", "6 un atlikums 3", "5 un atlikums 8",
               "7 un atlikums 4"], 0),
             ("Kāds var būt atlikums, dalot ar 4?",
              ["no 0 līdz 3", "no 0 līdz 4", "jebkurš", "tikai 2"], 0),
         ]},
        {"sr": "Nosaka vairāku skaitļu reizinājumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 · 4 · 15?", ["100", "110", "120", "130"], 2),
             ("Cik ir 5 · 2 · 18?", ["160", "170", "180", "190"], 2),
             ("Kā ērtāk aprēķināt 4 · 13 · 5?",
              ["vispirms 4 · 5", "vispirms 13 · 5", "tikai pēc kārtas",
               "nav nozīmes"], 0),
         ]},
        {"sr": "Nosaka aptuveno vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aptuveni cik ir 297 · 3?",
              ["ap 300", "ap 600", "ap 900", "ap 3000"], 2),
             ("Aptuveni cik ir 803 : 4?",
              ["ap 20", "ap 200", "ap 400", "ap 2000"], 1),
             ("Skolēns ieguva 48 · 5 = 2400. Kāpēc tas nav ticami?",
              ["rezultātam jābūt ap 240", "rezultātam jābūt ap 2400",
               "rezultāts ir pareizs", "nevar novērtēt"], 0),
         ]},
        {"sr": "Lieto «tik reižu vairāk/mazāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir 5 reizes lielāks nekā 46?",
              ["220", "230", "240", "250"], 1),
             ("Kurš skaitlis ir 4 reizes mazāks nekā 128?",
              ["28", "32", "34", "512"], 1),
             ("Vienā grozā 24 āboli, otrā 3 reizes vairāk. Cik otrā?",
              ["62", "72", "82", "8"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Reizina un dala ar viencipara skaitli",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini pa šķirām vai rakstveidā! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("243 · 3 = ……", "729"), ("486 : 2 = ……", "243"),
                         ("36 · 4 = ……", "144"), ("735 : 5 = ……", "147")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini pa šķirām vai rakstveidā! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("152 · 4 = ……", "608"), ("639 : 3 = ……", "213"),
                         ("48 · 5 = ……", "240"), ("896 : 4 = ……", "224")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini pa šķirām vai rakstveidā! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("214 · 3 = ……", "642"), ("945 : 5 = ……", "189"),
                         ("27 · 6 = ……", "162"), ("768 : 2 = ……", "384")]},
         ]},
        {"sr": "Dala ar atlikumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Izdali ar atlikumu",
              "note": "Pieraksti dalījumu un atlikumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("17 : 5 = …… (atl. ……)", "3 (atl. 2)"),
                         ("29 : 4 = …… (atl. ……)", "7 (atl. 1)"),
                         ("45 : 7 = …… (atl. ……)", "6 (atl. 3)")]},
             {"tips": "parveide", "virs": "Izdali ar atlikumu",
              "note": "Pieraksti dalījumu un atlikumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("23 : 4 = …… (atl. ……)", "5 (atl. 3)"),
                         ("38 : 6 = …… (atl. ……)", "6 (atl. 2)"),
                         ("52 : 9 = …… (atl. ……)", "5 (atl. 7)")]},
             {"tips": "parveide", "virs": "Izdali ar atlikumu",
              "note": "Pieraksti dalījumu un atlikumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("19 : 3 = …… (atl. ……)", "6 (atl. 1)"),
                         ("41 : 5 = …… (atl. ……)", "8 (atl. 1)"),
                         ("58 : 8 = …… (atl. ……)", "7 (atl. 2)")]},
         ]},
        {"sr": "Risina uzdevumu par «tik reižu vairāk» ar shēmu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 6.5,
              "ievads": "Vienā plauktā ir 48 grāmatas, otrā — 3 reizes "
                        "vairāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Aprēķini, cik grāmatu ir otrajā plauktā!", 1),
                       ("Aprēķini, cik grāmatu ir abos plauktos kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Otrā sloksnīte 3 reizes garāka.   (1 p.)",
                           "2) 48 · 3 = 144   (1 p.)",
                           "3) 48 + 144 = 192   (1 p.)",
                           "4) Atbilde: otrajā 144; kopā 192 grāmatas.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par ražu", "vieta": 6.5,
              "ievads": "No viena dārza novāca 126 kg ābolu, no otra — "
                        "2 reizes vairāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Aprēķini, cik kilogramu novāca no otra dārza!", 1),
                       ("Aprēķini, cik kilogramu novāca kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Otrā sloksnīte 2 reizes garāka.   (1 p.)",
                           "2) 126 · 2 = 252 (kg)   (1 p.)",
                           "3) 126 + 252 = 378 (kg)   (1 p.)",
                           "4) Atbilde: no otra 252 kg; kopā 378 kg.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par skolēniem",
              "vieta": 6.5,
              "ievads": "Pulciņā ir 245 skolēni. Sporta pulciņā — 5 reizes "
                        "mazāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Aprēķini, cik skolēnu ir sporta pulciņā!", 1),
                       ("Aprēķini, par cik skolēnu ir mazāk!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Otrā sloksnīte 5 reizes īsāka.   (1 p.)",
                           "2) 245 : 5 = 49   (1 p.)",
                           "3) 245 − 49 = 196   (1 p.)",
                           "4) Atbilde: sporta pulciņā 49; par 196 mazāk.   "
                           "(1 p.)"]},
         ]},
        {"sr": "Risina uzdevumu ar dalīšanu un atlikumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par kastēm", "vieta": 5.5,
              "ievads": "Vienā kastē ietilpst 6 olas. Jāsaliek 100 olas.",
              "jaut": [("Pieraksti dalīšanu ar atlikumu!", 1),
                       ("Aprēķini, cik kastu būs pilnas!", 1),
                       ("Uzraksti, cik kastu vajag, lai saliktu visas "
                        "olas!", 1)],
              "atbildes": ["1) 100 : 6 = 16 (atl. 4)   (1 p.)",
                           "2) 16 pilnas kastes   (1 p.)",
                           "3) Atbilde: vajag 17 kastes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par autobusiem",
              "vieta": 5.5,
              "ievads": "Vienā autobusā ietilpst 45 cilvēki. Ekskursijā brauc "
                        "200 cilvēku.",
              "jaut": [("Pieraksti dalīšanu ar atlikumu!", 1),
                       ("Aprēķini, cik autobusu būs pilni!", 1),
                       ("Uzraksti, cik autobusu vajag kopā!", 1)],
              "atbildes": ["1) 200 : 45 = 4 (atl. 20)   (1 p.)",
                           "2) 4 pilni autobusi   (1 p.)",
                           "3) Atbilde: vajag 5 autobusus.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 5.5,
              "ievads": "Vienā plauktā ietilpst 8 grāmatas. Jāsaliek "
                        "50 grāmatas.",
              "jaut": [("Pieraksti dalīšanu ar atlikumu!", 1),
                       ("Aprēķini, cik plauktu būs pilni!", 1),
                       ("Uzraksti, cik plauktu vajag kopā!", 1)],
              "atbildes": ["1) 50 : 8 = 6 (atl. 2)   (1 p.)",
                           "2) 6 pilni plaukti   (1 p.)",
                           "3) Atbilde: vajag 7 plauktus.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
