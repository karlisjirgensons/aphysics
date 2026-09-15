# -*- coding: utf-8 -*-
"""Matemātika, 3. klase. 3.6. Kā saskaita un atņem trīsciparu skaitļus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 3. klase, 3.6. temats): trīsciparu skaitļa
sastāvs un pieraksts izvērstā formā, skaitļu salīdzināšana, saskaitīšana un
atņemšana 1000 apjomā (arī rakstveidā citu zem cita), vairāku skaitļu
saskaitīšana un saskaitāmo grupēšana, darbības ar lielumiem un situāciju
uzdevumi.
"""

PRIEKSMETS = "Matemātika  |  3. klase"
TEMATS = "3.6."
NOSAUKUMS = "Kā saskaita un atņem trīsciparu skaitļus?"

ATGADNE = [
    "Trīsciparu skaitlī cipari no kreisās puses:  simti, desmiti, vieni   "
    "·   10 simti = 1 tūkstotis",
    "Izvērstā forma:  456 = 400 + 50 + 6   ·   saskaitāmos var grupēt un "
    "mainīt vietām",
    "Saskaitot un atņemot lielus skaitļus, tos raksta citu zem cita: "
    "vienus zem vieniem, desmitus zem desmitiem.",
]

FD = {
    "veids": "fd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 3.6. temata beigās. Pārbauda trīsciparu "
                "skaitļa sastāvu un pierakstu, skaitļu salīdzināšanu, "
                "saskaitīšanu un atņemšanu 1000 apjomā, vairāku skaitļu "
                "saskaitīšanu, darbības ar lielumiem un situāciju uzdevumus.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosaka trīsciparu skaitļa sastāvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik simtu ir skaitlī 456?", ["4", "5", "6", "456"], 0),
             ("Cik desmitu ir skaitlī 372?", ["3", "7", "2", "37"], 1),
             ("Cik vienu ir skaitlī 508?", ["5", "0", "8", "58"], 2),
         ]},
        {"sr": "Pieraksta skaitli izvērstā formā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā izvērstā formā pieraksta 624?",
              ["600 + 20 + 4", "6 + 2 + 4", "600 + 200 + 4",
               "60 + 20 + 4"], 0),
             ("Kurš skaitlis ir 300 + 40 + 7?",
              ["347", "374", "3407", "3047"], 0),
             ("Kā izvērstā formā pieraksta 905?",
              ["900 + 5", "900 + 50", "90 + 5", "9 + 0 + 5"], 0),
         ]},
        {"sr": "Lasa un raksta skaitļus līdz 1000",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā ar cipariem pieraksta «septiņi simti divdesmit"
              " trīs»?",
              ["723", "732", "7023", "273"], 0),
             ("Kā izlasa skaitli 480?",
              ["četri simti astoņdesmit", "četrdesmit astoņi",
               "četri simti astoņi", "astoņi simti četrdesmit"], 0),
             ("Cik simtu ir 1 tūkstotī?", ["10", "100", "1000", "1"], 0),
         ]},
        {"sr": "Salīdzina trīsciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  345 …… 354?", [">", "<", "=", "+"], 1),
             ("Kurš skaitlis ir lielākais?", ["489", "498", "849", "894"], 3),
             ("Kurš skaitlis ir mazākais?", ["512", "215", "251", "125"], 3),
         ]},
        {"sr": "Saskaita trīsciparu skaitļus bez pārejas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 234 + 145?", ["369", "379", "389", "479"], 1),
             ("Cik ir 512 + 306?", ["808", "818", "828", "918"], 1),
             ("Cik ir 421 + 253?", ["664", "674", "684", "774"], 1),
         ]},
        {"sr": "Saskaita trīsciparu skaitļus ar pāreju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 268 + 157?", ["315", "405", "415", "425"], 3),
             ("Cik ir 349 + 176?", ["415", "425", "515", "525"], 3),
             ("Cik ir 487 + 238?", ["615", "625", "715", "725"], 3),
         ]},
        {"sr": "Atņem trīsciparu skaitļus bez aizņemšanās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 586 − 243?", ["243", "333", "343", "443"], 2),
             ("Cik ir 749 − 526?", ["213", "223", "233", "323"], 1),
             ("Cik ir 875 − 351?", ["414", "424", "514", "524"], 3),
         ]},
        {"sr": "Atņem trīsciparu skaitļus ar aizņemšanos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 523 − 178?", ["245", "335", "345", "445"], 2),
             ("Cik ir 600 − 247?", ["343", "353", "363", "453"], 1),
             ("Cik ir 712 − 385?", ["227", "317", "327", "427"], 2),
         ]},
        {"sr": "Saskaita vairākus skaitļus, tos grupējot",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 25 + 47 + 75?", ["137", "147", "157", "167"], 1),
             ("Kā ērtāk saskaitīt 18 + 35 + 22?",
              ["vispirms 18 + 22", "vispirms 35 + 22", "tikai pēc kārtas",
               "nav nozīmes"], 0),
             ("Cik ir 120 + 380 + 45?", ["535", "545", "555", "645"], 1),
         ]},
        {"sr": "Pārbauda rezultātu ar pretējo darbību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pārbaudīt, vai 645 − 278 = 367?",
              ["saskaitot 367 + 278", "saskaitot 645 + 278",
               "atņemot 645 − 367", "reizinot"], 0),
             ("Skolēns ieguva 348 + 256 = 594. Vai tas ir pareizi?",
              ["nē, pareizi ir 604", "jā", "nē, pareizi ir 504",
               "nevar pārbaudīt"], 0),
             ("Aptuveni cik ir 398 + 205?", ["ap 400", "ap 500", "ap 600",
                                             "ap 800"], 2),
         ]},
        {"sr": "Saskaita un atņem lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 350 g + 480 g?", ["730 g", "830 g", "930 g", "838 g"],
              1),
             ("Cik ir 2 l 500 ml − 800 ml?",
              ["1 l 200 ml", "1 l 700 ml", "2 l 300 ml", "700 ml"], 1),
             ("Cik ir 1 m 20 cm + 85 cm?",
              ["1 m 5 cm", "1 m 95 cm", "2 m 5 cm", "2 m 15 cm"], 2),
         ]},
        {"sr": "Risina situāciju uzdevumu 1000 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Bibliotēkā 480 grāmatas, atveda vēl 165. Cik ir kopā?",
              ["545", "635", "645", "655"], 2),
             ("Skolā 725 skolēni, 348 ir sākumskolā. Cik ir pārējos?",
              ["377", "387", "477", "487"], 0),
             ("Veikalā bija 300 kg kartupeļu, pārdeva 175 kg. Cik palika?",
              ["115 kg", "125 kg", "135 kg", "225 kg"], 1),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 3.6. temata noslēgumā. "
                "Pārbauda trīsciparu skaitļa sastāvu un salīdzināšanu, "
                "saskaitīšanu un atņemšanu 1000 apjomā, vairāku skaitļu "
                "saskaitīšanu, darbības ar lielumiem un situāciju uzdevumu "
                "risināšanu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Nosaka skaitļa sastāvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik simtu ir skaitlī 738?", ["3", "7", "8", "738"], 1),
             ("Cik desmitu ir skaitlī 460?", ["4", "6", "0", "46"], 1),
             ("Kurš skaitlis ir 500 + 30 + 9?",
              ["539", "593", "5039", "935"], 0),
         ]},
        {"sr": "Salīdzina trīsciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  627 …… 672?", [">", "<", "=", "+"], 1),
             ("Kurš skaitlis ir lielākais?", ["398", "389", "839", "893"], 3),
             ("Kurš skaitlis ir mazākais?", ["604", "460", "406", "640"], 2),
         ]},
        {"sr": "Saskaita 1000 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 345 + 238?", ["573", "583", "593", "673"], 1),
             ("Cik ir 476 + 145?", ["511", "611", "621", "631"], 2),
             ("Cik ir 250 + 175?", ["315", "415", "425", "435"], 2),
         ]},
        {"sr": "Atņem 1000 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 634 − 258?", ["376", "386", "476", "486"], 0),
             ("Cik ir 500 − 165?", ["235", "335", "345", "435"], 1),
             ("Cik ir 823 − 419?", ["394", "404", "414", "504"], 1),
         ]},
        {"sr": "Saskaita vairākus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 35 + 68 + 25?", ["118", "128", "138", "148"], 1),
             ("Cik ir 150 + 250 + 60?", ["450", "460", "470", "560"], 1),
             ("Kā ērtāk saskaitīt 27 + 45 + 73?",
              ["vispirms 27 + 73", "vispirms 45 + 73", "tikai pēc kārtas",
               "nav nozīmes"], 0),
         ]},
        {"sr": "Saskaita un atņem lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 450 g + 380 g?", ["730 g", "820 g", "830 g", "930 g"],
              2),
             ("Cik ir 3 l − 750 ml?",
              ["2 l 250 ml", "2 l 750 ml", "1 l 250 ml", "750 ml"], 0),
             ("Cik ir 2 m 40 cm + 75 cm?",
              ["2 m 15 cm", "3 m 5 cm", "3 m 15 cm", "2 m 75 cm"], 2),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita un atņem trīsciparu skaitļus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini rakstveidā, ja vajag! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("348 + 256 = ……", "604"), ("725 − 348 = ……", "377"),
                         ("469 + 175 = ……", "644"), ("800 − 425 = ……", "375")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini rakstveidā, ja vajag! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("267 + 385 = ……", "652"), ("634 − 275 = ……", "359"),
                         ("528 + 194 = ……", "722"), ("700 − 236 = ……", "464")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini rakstveidā, ja vajag! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("456 + 278 = ……", "734"), ("912 − 587 = ……", "325"),
                         ("385 + 246 = ……", "631"), ("600 − 318 = ……", "282")]},
         ]},
        {"sr": "Pieraksta skaitli izvērstā formā un salīdzina skaitļus",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Pieraksti un salīdzini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("647 = …… + 40 + 7", "600"),
                         ("500 + 80 + 3 = ……", "583"),
                         ("734  ……  743  (ieraksti zīmi)", "<")]},
             {"tips": "parveide", "virs": "Pieraksti un salīdzini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("928 = 900 + …… + 8", "20"),
                         ("400 + 60 + 5 = ……", "465"),
                         ("519  ……  491  (ieraksti zīmi)", ">")]},
             {"tips": "parveide", "virs": "Pieraksti un salīdzini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("305 = 300 + ……", "5"),
                         ("700 + 20 + 9 = ……", "729"),
                         ("860  ……  806  (ieraksti zīmi)", ">")]},
         ]},
        {"sr": "Risina divu darbību situāciju uzdevumu 1000 apjomā",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 6.5,
              "ievads": "Bibliotēkā bija 480 grāmatas. Atveda vēl 165, bet "
                        "248 izsniedza lasītājiem.",
              "jaut": [("Aprēķini, cik grāmatu bija pēc atvešanas!", 1),
                       ("Aprēķini, cik grāmatu palika bibliotēkā!", 1),
                       ("Pieraksti abas darbības vienā izteiksmē!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 480 + 165 = 645   (1 p.)",
                           "2) 645 − 248 = 397   (1 p.)",
                           "3) 480 + 165 − 248   (1 p.)",
                           "4) Atbilde: palika 397 grāmatas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par kartupeļiem",
              "vieta": 6.5,
              "ievads": "Noliktavā bija 750 kg kartupeļu. Pārdeva 285 kg, "
                        "bet atveda vēl 130 kg.",
              "jaut": [("Aprēķini, cik kilogramu palika pēc pārdošanas!", 1),
                       ("Aprēķini, cik kilogramu ir tagad!", 1),
                       ("Pieraksti abas darbības vienā izteiksmē!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 750 − 285 = 465 (kg)   (1 p.)",
                           "2) 465 + 130 = 595 (kg)   (1 p.)",
                           "3) 750 − 285 + 130   (1 p.)",
                           "4) Atbilde: noliktavā ir 595 kg.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par skolēniem",
              "vieta": 6.5,
              "ievads": "Skolā ir 625 skolēni. Sākumskolā mācās 238, "
                        "pamatskolā — 297.",
              "jaut": [("Aprēķini, cik skolēnu mācās abās kopā!", 1),
                       ("Aprēķini, cik skolēnu mācās vidusskolā!", 1),
                       ("Pieraksti abas darbības vienā izteiksmē!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 238 + 297 = 535   (1 p.)",
                           "2) 625 − 535 = 90   (1 p.)",
                           "3) 625 − (238 + 297)   (1 p.)",
                           "4) Atbilde: vidusskolā mācās 90 skolēni.   "
                           "(1 p.)"]},
         ]},
        {"sr": "Veic aprēķinus ar lielumiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Aprēķini ar masu", "vieta": 5.5,
              "ievads": "Somā ir divas grāmatas: 450 g un 380 g, un burtnīca "
                        "170 g.",
              "jaut": [("Aprēķini abu grāmatu masu!", 1),
                       ("Aprēķini visu trīs priekšmetu masu!", 1),
                       ("Izsaki atbildi kilogramos un gramos!", 1)],
              "atbildes": ["1) 450 + 380 = 830 (g)   (1 p.)",
                           "2) 830 + 170 = 1000 (g)   (1 p.)",
                           "3) Atbilde: 1 kg.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Aprēķini ar tilpumu",
              "vieta": 5.5,
              "ievads": "Kannā ir 2 l sulas. Izlēja 650 ml un pēc tam vēl "
                        "350 ml.",
              "jaut": [("Aprēķini, cik ml izlēja kopā!", 1),
                       ("Aprēķini, cik ml sulas palika!", 1),
                       ("Izsaki atbildi litros un mililitros!", 1)],
              "atbildes": ["1) 650 + 350 = 1000 (ml)   (1 p.)",
                           "2) 2000 − 1000 = 1000 (ml)   (1 p.)",
                           "3) Atbilde: 1 l.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Aprēķini ar garumu", "vieta": 5.5,
              "ievads": "Auklas garums ir 3 m. Nogrieza 125 cm un pēc tam "
                        "vēl 90 cm.",
              "jaut": [("Aprēķini, cik cm nogrieza kopā!", 1),
                       ("Aprēķini, cik cm auklas palika!", 1),
                       ("Izsaki atbildi metros un centimetros!", 1)],
              "atbildes": ["1) 125 + 90 = 215 (cm)   (1 p.)",
                           "2) 300 − 215 = 85 (cm)   (1 p.)",
                           "3) Atbilde: 85 cm.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
