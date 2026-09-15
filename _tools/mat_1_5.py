# -*- coding: utf-8 -*-
"""Matemātika, 1. klase. 1.5. Kā saskaita un atņem skaitļus, kuri lielāki
nekā 10?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 1. klase, 1.5. temats): saskaitīšana un
atņemšana 20 apjomā ar pāreju pār desmitu, saskaitīšanas paņēmieni, saistība
starp summu un starpību, nezināmā locekļa noteikšana, trīs skaitļu
saskaitīšana, lauztas līnijas garums 10–20 cm.
"""

PRIEKSMETS = "Matemātika  |  1. klase"
TEMATS = "1.5."
NOSAUKUMS = "Kā saskaita un atņem skaitļus, kuri lielāki nekā 10?"

ATGADNE = [
    "Skaitļi:  10  11  12  13  14  15  16  17  18  19  20",
    "Saskaitot līdz desmitam:  8 + 5 = 8 + 2 + 3 = 10 + 3 = 13",
    "Atņemot no desmita:  14 − 6 = 14 − 4 − 2 = 10 − 2 = 8   ·   "
    "saskaitāmos var mainīt vietām",
]

FD = {
    "veids": "fd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 1.5. temata beigās. Pārbauda saskaitīšanu "
                "un atņemšanu 20 apjomā, arī ar pāreju pār desmitu, "
                "saskaitīšanas paņēmienus, saistību starp summu un starpību, "
                "nezināmā locekļa noteikšanu, trīs skaitļu saskaitīšanu un "
                "lauztas līnijas garuma aprēķinu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Saskaita bez pārejas pār desmitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 12 + 5?", ["15", "16", "17", "18"], 2),
             ("Cik ir 13 + 4?", ["16", "17", "18", "19"], 1),
             ("Cik ir 10 + 8?", ["16", "17", "18", "20"], 2),
         ]},
        {"sr": "Saskaita ar pāreju pār desmitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 8 + 5?", ["12", "13", "14", "15"], 1),
             ("Cik ir 7 + 6?", ["12", "13", "14", "15"], 1),
             ("Cik ir 9 + 4?", ["12", "13", "14", "15"], 1),
         ]},
        {"sr": "Atņem bez pārejas pār desmitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 18 − 5?", ["12", "13", "14", "23"], 1),
             ("Cik ir 16 − 4?", ["11", "12", "13", "20"], 1),
             ("Cik ir 19 − 9?", ["9", "10", "11", "28"], 1),
         ]},
        {"sr": "Atņem ar pāreju pār desmitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 14 − 6?", ["7", "8", "9", "20"], 1),
             ("Cik ir 12 − 5?", ["6", "7", "8", "17"], 1),
             ("Cik ir 15 − 8?", ["6", "7", "8", "23"], 1),
         ]},
        {"sr": "Skaidro paņēmienu «saskaitu līdz desmitam»",
         "stunda": TEMATS,
         "jautajumi": [
             ("8 + 5 = 8 + 2 + ……  Kurš skaitlis pietrūkst?",
              ["2", "3", "4", "5"], 1),
             ("Kāpēc, saskaitot 9 + 6, vispirms izdevīgi iegūt 10?",
              ["desmitam viegli pieskaitīt", "desmits ir skaistāks",
               "citādi nedrīkst", "tad summa kļūst mazāka"], 0),
             ("7 + 8 = 7 + 3 + ……  Kurš skaitlis pietrūkst?",
              ["3", "4", "5", "8"], 2),
         ]},
        {"sr": "Skaidro, ka atņemšana ir nezināmā saskaitāmā meklēšana",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē aprēķināt 13 − 8?",
              ["atrast skaitli, kas kopā ar 8 veido 13",
               "atrast skaitli, kas ir par 13 lielāks nekā 8",
               "saskaitīt 13 un 8", "salīdzināt 13 un 8"], 0),
             ("Zināms, ka 6 + 7 = 13. Cik ir 13 − 7?",
              ["5", "6", "7", "20"], 1),
             ("Zināms, ka 9 + 8 = 17. Cik ir 17 − 9?",
              ["7", "8", "9", "26"], 1),
         ]},
        {"sr": "Lieto saskaitāmo pārvietojamību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zināms, ka 4 + 9 = 13. Cik ir 9 + 4?",
              ["5", "9", "13", "18"], 2),
             ("Kā izdevīgāk saskaitīt 3 + 11?",
              ["11 + 3", "3 − 11", "11 − 3", "3 + 3"], 0),
             ("Kas notiek ar summu, ja saskaitāmos samaina vietām?",
              ["tā nemainās", "tā palielinās", "tā samazinās",
               "tā kļūst par starpību"], 0),
         ]},
        {"sr": "Saskaita trīs skaitļus 20 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 4 + 6 + 5?", ["13", "14", "15", "16"], 2),
             ("Cik ir 3 + 7 + 8?", ["16", "17", "18", "19"], 2),
             ("Cik ir 5 + 5 + 9?", ["17", "18", "19", "20"], 2),
         ]},
        {"sr": "Nosaka nezināmo skaitli vienādībā 20 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("9 + …… = 15  Kurš skaitlis jāieraksta?",
              ["5", "6", "7", "24"], 1),
             ("…… + 8 = 14  Kurš skaitlis jāieraksta?",
              ["4", "5", "6", "22"], 2),
             ("16 − …… = 9  Kurš skaitlis jāieraksta?",
              ["6", "7", "8", "25"], 1),
         ]},
        {"sr": "Salīdzina summu vai starpību ar skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  8 + 5 …… 14?", [">", "<", "=", "+"], 1),
             ("Kura zīme jāliek:  17 − 8 …… 9?", [">", "<", "=", "−"], 2),
             ("Kura zīme jāliek:  6 + 7 …… 12?", [">", "<", "=", "+"], 0),
         ]},
        {"sr": "Risina sadzīves uzdevumu 20 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Plauktā bija 8 grāmatas, pielika vēl 7. Cik grāmatu ir kopā?",
              ["13", "14", "15", "16"], 2),
             ("Autobusā brauca 15 cilvēki, 6 izkāpa. Cik palika?",
              ["8", "9", "10", "21"], 1),
             ("Klasē ir 9 meitenes un 8 zēni. Cik bērnu ir klasē?",
              ["16", "17", "18", "19"], 1),
         ]},
        {"sr": "Aprēķina lauztas līnijas garumu 10–20 cm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Lauztā līnijā ir 6 cm un 8 cm. Cik gara tā ir?",
              ["12 cm", "13 cm", "14 cm", "68 cm"], 2),
             ("Lauztā līnijā ir 5 cm, 4 cm un 7 cm. Cik gara tā ir?",
              ["15 cm", "16 cm", "17 cm", "18 cm"], 1),
             ("Lauzta līnija ir 17 cm gara. Viens nogrieznis ir 9 cm. Cik "
              "garš ir otrs?",
              ["6 cm", "7 cm", "8 cm", "26 cm"], 2),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 1.5. temata noslēgumā. "
                "Pārbauda saskaitīšanu un atņemšanu 20 apjomā ar pāreju pār "
                "desmitu, nezināmā locekļa noteikšanu, trīs skaitļu "
                "saskaitīšanu, sadzīves uzdevuma pierakstu un lauztas "
                "līnijas garuma aprēķinu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Uzdevumu tekstu lasa skolotājs. Risinājumu raksti tam "
              "atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Saskaita 20 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 9 + 5?", ["13", "14", "15", "16"], 1),
             ("Cik ir 6 + 8?", ["13", "14", "15", "16"], 1),
             ("Cik ir 7 + 7?", ["13", "14", "15", "16"], 1),
         ]},
        {"sr": "Atņem 20 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 13 − 7?", ["5", "6", "7", "20"], 1),
             ("Cik ir 16 − 9?", ["6", "7", "8", "25"], 1),
             ("Cik ir 15 − 6?", ["8", "9", "10", "21"], 1),
         ]},
        {"sr": "Lieto saistību starp summu un starpību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zināms, ka 8 + 6 = 14. Cik ir 14 − 6?",
              ["6", "8", "14", "20"], 1),
             ("Zināms, ka 5 + 9 = 14. Cik ir 14 − 5?",
              ["5", "8", "9", "19"], 2),
             ("Ko nozīmē aprēķināt 12 − 5?",
              ["atrast skaitli, kas kopā ar 5 veido 12", "saskaitīt 12 un 5",
               "salīdzināt 12 un 5", "atrast skaitli, kas lielāks nekā 12"],
              0),
         ]},
        {"sr": "Saskaita trīs skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 + 8 + 6?", ["14", "15", "16", "17"], 2),
             ("Cik ir 4 + 6 + 9?", ["17", "18", "19", "20"], 2),
             ("Cik ir 3 + 3 + 7?", ["12", "13", "14", "15"], 1),
         ]},
        {"sr": "Nosaka nezināmo skaitli vienādībā",
         "stunda": TEMATS,
         "jautajumi": [
             ("7 + …… = 13", ["5", "6", "7", "20"], 1),
             ("…… + 9 = 16", ["6", "7", "8", "25"], 1),
             ("14 − …… = 8", ["5", "6", "7", "22"], 1),
         ]},
        {"sr": "Salīdzina summu vai starpību ar skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  9 + 6 …… 14?", [">", "<", "=", "+"], 0),
             ("Kura zīme jāliek:  18 − 9 …… 9?", [">", "<", "=", "−"], 2),
             ("Kura zīme jāliek:  5 + 7 …… 13?", [">", "<", "=", "+"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita un atņem 20 apjomā",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("8 + 7 = ……", "15"), ("13 − 5 = ……", "8"),
                         ("9 + 8 = ……", "17"), ("16 − 7 = ……", "9")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("6 + 9 = ……", "15"), ("12 − 4 = ……", "8"),
                         ("7 + 5 = ……", "12"), ("17 − 8 = ……", "9")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("9 + 9 = ……", "18"), ("14 − 8 = ……", "6"),
                         ("8 + 6 = ……", "14"), ("15 − 9 = ……", "6")]},
         ]},
        {"sr": "Nosaka nezināmo skaitli vienādībā",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli tā, lai vienādība būtu patiesa! Par "
                      "katru pareizu skaitli — 1 punkts.",
              "rindas": [("8 + …… = 14", "6"), ("…… + 7 = 15", "8"),
                         ("13 − …… = 6", "7")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli tā, lai vienādība būtu patiesa! Par "
                      "katru pareizu skaitli — 1 punkts.",
              "rindas": [("9 + …… = 17", "8"), ("…… + 6 = 13", "7"),
                         ("15 − …… = 7", "8")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli tā, lai vienādība būtu patiesa! Par "
                      "katru pareizu skaitli — 1 punkts.",
              "rindas": [("7 + …… = 16", "9"), ("…… + 8 = 14", "6"),
                         ("18 − …… = 9", "9")]},
         ]},
        {"sr": "Risina tekstuzdevumu un pieraksta risinājumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 6.0,
              "ievads": "Plauktā bija 8 grāmatas. Pielika vēl 7 grāmatas. "
                        "Pēc tam 5 grāmatas paņēma.",
              "jaut": [("Pieraksti, kā aprēķināt, cik grāmatu bija pēc "
                        "pielikšanas!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik grāmatu palika plauktā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 8 + 7   (1 p.)", "2) 8 + 7 = 15   (1 p.)",
                           "3) 15 − 5 = 10   (1 p.)",
                           "4) Atbilde: plauktā palika 10 grāmatas.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par ogām", "vieta": 6.0,
              "ievads": "Groziņā bija 9 ogas. Ielika vēl 6 ogas. Pēc tam "
                        "4 ogas apēda.",
              "jaut": [("Pieraksti, kā aprēķināt, cik ogu bija pēc "
                        "ielikšanas!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik ogu palika groziņā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 9 + 6   (1 p.)", "2) 9 + 6 = 15   (1 p.)",
                           "3) 15 − 4 = 11   (1 p.)",
                           "4) Atbilde: groziņā palika 11 ogas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par pasažieriem",
              "vieta": 6.0,
              "ievads": "Autobusā brauca 7 pasažieri. Iekāpa vēl 8. Nākamajā "
                        "pieturā izkāpa 6 pasažieri.",
              "jaut": [("Pieraksti, kā aprēķināt, cik pasažieru bija pēc "
                        "iekāpšanas!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik pasažieru palika autobusā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 7 + 8   (1 p.)", "2) 7 + 8 = 15   (1 p.)",
                           "3) 15 − 6 = 9   (1 p.)",
                           "4) Atbilde: autobusā palika 9 pasažieri.   "
                           "(1 p.)"]},
         ]},
        {"sr": "Aprēķina lauztas līnijas garumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Lauztas līnijas garums",
              "vieta": 5.5,
              "ievads": "Lauztu līniju veido divi nogriežņi: 7 cm un 6 cm.",
              "jaut": [("Uzzīmē šādu lauztu līniju ar lineālu!", 1),
                       ("Pieraksti aprēķinu!", 1),
                       ("Uzraksti, cik gara ir lauztā līnija!", 1)],
              "atbildes": ["1) Uzzīmēta lauzta līnija no 7 cm un 6 cm "
                           "nogriežņiem.   (1 p.)",
                           "2) 7 cm + 6 cm   (1 p.)",
                           "3) Atbilde: 13 cm.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Lauztas līnijas garums",
              "vieta": 5.5,
              "ievads": "Lauztu līniju veido divi nogriežņi: 8 cm un 5 cm.",
              "jaut": [("Uzzīmē šādu lauztu līniju ar lineālu!", 1),
                       ("Pieraksti aprēķinu!", 1),
                       ("Uzraksti, cik gara ir lauztā līnija!", 1)],
              "atbildes": ["1) Uzzīmēta lauzta līnija no 8 cm un 5 cm "
                           "nogriežņiem.   (1 p.)",
                           "2) 8 cm + 5 cm   (1 p.)",
                           "3) Atbilde: 13 cm.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Lauztas līnijas garums",
              "vieta": 5.5,
              "ievads": "Lauzta līnija ir 16 cm gara. Viens tās nogrieznis "
                        "ir 9 cm.",
              "jaut": [("Pieraksti aprēķinu otra nogriežņa garumam!", 1),
                       ("Aprēķini to!", 1),
                       ("Uzzīmē otru nogriezni ar lineālu!", 1)],
              "atbildes": ["1) 16 cm − 9 cm   (1 p.)",
                           "2) 16 cm − 9 cm = 7 cm   (1 p.)",
                           "3) Uzzīmēts 7 cm garš nogrieznis.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
