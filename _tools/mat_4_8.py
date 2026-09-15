# -*- coding: utf-8 -*-
"""Matemātika, 4. klase. 4.8. Kas kopīgs iepirkšanās un kustības
matemātiskajā aprakstā?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 4. klase, 4.8. temats): ātrums kā 1
stundā (minūtē, sekundē) veiktais ceļš un tā mērvienības lasīšana; ceļa,
laika un ātruma savstarpējā saistība; savstarpēji atkarīgi lielumi
iepirkšanās aprakstā (cena, skaits, samaksa) un kustības aprakstā (ceļš,
laiks, ātrums); ātrumu salīdzināšana.
"""

PRIEKSMETS = "Matemātika  |  4. klase"
TEMATS = "4.8."
NOSAUKUMS = "Kas kopīgs iepirkšanās un kustības matemātiskajā aprakstā?"

ATGADNE = [
    "Kustība:   s = v · t      ·      v = s : t      ·      t = s : v",
    "Iepirkšanās:   samaksa = cena · skaits   ·   cena = samaksa : skaits   "
    "·   skaits = samaksa : cena",
    "60 km/h lasa «sešdesmit kilometri stundā» — tik kilometru veic vienā "
    "stundā.",
]

FD = {
    "veids": "fd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 4.8. temata beigās. Pārbauda ātruma "
                "jēdzienu un mērvienības, ceļa, laika un ātruma "
                "aprēķināšanu, ātrumu salīdzināšanu un cenas, skaita un "
                "samaksas savstarpējo saistību.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro ātruma nozīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda ātrums 60 km/h?",
              ["1 stundā veic 60 km", "60 stundās veic 1 km",
               "kopā veic 60 km", "brauc 60 stundas"], 0),
             ("Kā lasa mērvienību km/h?",
              ["kilometri stundā", "kilometri un stundas",
               "stundas kilometrā", "kilogrami stundā"], 0),
             ("Ar kuru burtu apzīmē ātrumu?", ["v", "s", "t", "m"], 0),
         ]},
        {"sr": "Zina kustības lielumu mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir ātruma mērvienība?", ["km/h", "km", "h", "kg"], 0),
             ("Kurā mērvienībā mēra ceļu?", ["km", "km/h", "h", "min"], 0),
             ("Kurā mērvienībā mēra laiku?", ["h", "km", "km/h", "m"], 0),
         ]},
        {"sr": "Aprēķina ceļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina ceļu?",
              ["s = v · t", "s = v : t", "s = t : v", "s = v + t"], 0),
             ("Automašīna brauc 60 km/h 3 stundas. Cik km tā nobrauc?",
              ["180 km", "20 km", "63 km", "30 km"], 0),
             ("Velosipēdists brauc 15 km/h 2 stundas. Cik km viņš nobrauc?",
              ["30 km", "7 km", "17 km", "13 km"], 0),
         ]},
        {"sr": "Aprēķina laiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina laiku?",
              ["t = s : v", "t = s · v", "t = v : s", "t = s + v"], 0),
             ("Ceļš ir 120 km, ātrums — 40 km/h. Cik ilgi jābrauc?",
              ["3 h", "80 h", "160 h", "4 h"], 0),
             ("Ceļš ir 100 km, ātrums — 50 km/h. Cik ilgi jābrauc?",
              ["2 h", "50 h", "150 h", "5 h"], 0),
         ]},
        {"sr": "Aprēķina ātrumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina ātrumu?",
              ["v = s : t", "v = s · t", "v = t : s", "v = s + t"], 0),
             ("Nobraukti 150 km 3 stundās. Cik liels ir ātrums?",
              ["50 km/h", "450 km/h", "153 km/h", "5 km/h"], 0),
             ("Nobraukti 80 km 2 stundās. Cik liels ir ātrums?",
              ["40 km/h", "160 km/h", "82 km/h", "78 km/h"], 0),
         ]},
        {"sr": "Salīdzina ātrumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš brauc ātrāk: 60 km/h vai 80 km/h?",
              ["80 km/h", "60 km/h", "vienādi", "nevar noteikt"], 0),
             ("Kurš 2 stundās veic garāku ceļu: 50 km/h vai 70 km/h?",
              ["70 km/h", "50 km/h", "vienādi", "nevar noteikt"], 0),
             ("Divi veic vienādu ceļu. Kurš brauc mazāk laika?",
              ["ātrākais", "lēnākais", "abi vienādi", "nevar noteikt"], 0),
         ]},
        {"sr": "Aprēķina samaksu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina samaksu?",
              ["cena · skaits", "cena : skaits", "skaits : cena",
               "cena + skaits"], 0),
             ("Burtnīca maksā 2 eiro. Cik maksā 7 burtnīcas?",
              ["14 eiro", "9 eiro", "5 eiro", "3 eiro"], 0),
             ("Kilograms ābolu maksā 3 eiro. Cik maksā 4 kg?",
              ["12 eiro", "7 eiro", "1 eiro", "34 eiro"], 0),
         ]},
        {"sr": "Aprēķina cenu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina cenu?",
              ["samaksa : skaits", "samaksa · skaits", "skaits : samaksa",
               "samaksa + skaits"], 0),
             ("Par 5 pildspalvām samaksāja 10 eiro. Cik maksā viena?",
              ["2 eiro", "50 eiro", "5 eiro", "15 eiro"], 0),
             ("Par 3 kg kartupeļu samaksāja 6 eiro. Cik maksā 1 kg?",
              ["2 eiro", "18 eiro", "9 eiro", "3 eiro"], 0),
         ]},
        {"sr": "Aprēķina skaitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina skaitu?",
              ["samaksa : cena", "samaksa · cena", "cena : samaksa",
               "samaksa − cena"], 0),
             ("Biļete maksā 4 eiro. Cik biļešu nopirks par 20 eiro?",
              ["5", "80", "16", "24"], 0),
             ("Grāmata maksā 8 eiro. Cik grāmatu nopirks par 40 eiro?",
              ["5", "320", "32", "48"], 0),
         ]},
        {"sr": "Spriež par savstarpēji atkarīgiem lielumiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ātrums nemainās, laiks palielinās 2 reizes. Kas notiek ar "
              "ceļu?",
              ["palielinās 2 reizes", "samazinās 2 reizes", "nemainās",
               "palielinās 4 reizes"], 0),
             ("Cena nemainās, skaits palielinās 3 reizes. Kas notiek ar "
              "samaksu?",
              ["palielinās 3 reizes", "samazinās 3 reizes", "nemainās",
               "palielinās 9 reizes"], 0),
             ("Ceļš nemainās, ātrums palielinās 2 reizes. Kas notiek ar "
              "laiku?",
              ["samazinās 2 reizes", "palielinās 2 reizes", "nemainās",
               "kļūst nulle"], 0),
         ]},
        {"sr": "Saskata kopīgo abos aprakstos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas kopīgs kustības un iepirkšanās aprakstam?",
              ["trīs lielumi ir savstarpēji saistīti", "abos ir kilometri",
               "abos ir nauda", "tiem nav nekā kopīga"], 0),
             ("Kurš iepirkšanās lielums atbilst ātrumam?",
              ["cena", "skaits", "samaksa", "laiks"], 0),
             ("Kurš iepirkšanās lielums atbilst ceļam?",
              ["samaksa", "cena", "skaits", "ātrums"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vilciens brauc 80 km/h 4 stundas. Cik km tas nobrauc?",
              ["320 km", "20 km", "84 km", "76 km"], 0),
             ("Gājējs 12 km noiet 3 stundās. Cik liels ir viņa ātrums?",
              ["4 km/h", "36 km/h", "15 km/h", "9 km/h"], 0),
             ("Cik maksā 6 kg banānu, ja 1 kg maksā 2 eiro?",
              ["12 eiro", "8 eiro", "3 eiro", "4 eiro"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 4.8. temata noslēgumā. "
                "Pārbauda ātruma nozīmi un mērvienības, ceļa, laika un "
                "ātruma aprēķināšanu, cenas, skaita un samaksas saistību un "
                "spriešanu par savstarpēji atkarīgiem lielumiem.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Skaidro ātruma nozīmi un mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda ātrums 45 km/h?",
              ["1 stundā veic 45 km", "45 stundās veic 1 km",
               "kopā veic 45 km", "brauc 45 stundas"], 0),
             ("Kura ir ātruma mērvienība?", ["km/h", "km", "h", "kg"], 0),
             ("Kurā mērvienībā mēra ceļu?", ["km", "km/h", "h", "kg"], 0),
         ]},
        {"sr": "Aprēķina ceļu un laiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Automašīna brauc 70 km/h 2 stundas. Cik km tā nobrauc?",
              ["140 km", "35 km", "72 km", "68 km"], 0),
             ("Ceļš ir 90 km, ātrums — 30 km/h. Cik ilgi jābrauc?",
              ["3 h", "60 h", "120 h", "2 h"], 0),
             ("Kā aprēķina ceļu?",
              ["s = v · t", "s = v : t", "s = t : v", "s = v + t"], 0),
         ]},
        {"sr": "Aprēķina ātrumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Nobraukti 200 km 4 stundās. Cik liels ir ātrums?",
              ["50 km/h", "800 km/h", "204 km/h", "196 km/h"], 0),
             ("Gājējs 15 km noiet 3 stundās. Cik liels ir ātrums?",
              ["5 km/h", "45 km/h", "18 km/h", "12 km/h"], 0),
             ("Kā aprēķina ātrumu?",
              ["v = s : t", "v = s · t", "v = t : s", "v = s + t"], 0),
         ]},
        {"sr": "Aprēķina samaksu, cenu un skaitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zīmulis maksā 3 eiro. Cik maksā 6 zīmuļi?",
              ["18 eiro", "9 eiro", "2 eiro", "3 eiro"], 0),
             ("Par 4 biļetēm samaksāja 24 eiro. Cik maksā viena?",
              ["6 eiro", "96 eiro", "20 eiro", "28 eiro"], 0),
             ("Grāmata maksā 5 eiro. Cik grāmatu nopirks par 35 eiro?",
              ["7", "175", "30", "40"], 0),
         ]},
        {"sr": "Spriež par savstarpēji atkarīgiem lielumiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cena nemainās, skaits palielinās 2 reizes. Kas notiek ar "
              "samaksu?",
              ["palielinās 2 reizes", "samazinās 2 reizes", "nemainās",
               "palielinās 4 reizes"], 0),
             ("Ceļš nemainās, ātrums palielinās 3 reizes. Kas notiek ar "
              "laiku?",
              ["samazinās 3 reizes", "palielinās 3 reizes", "nemainās",
               "kļūst nulle"], 0),
             ("Kas kopīgs kustības un iepirkšanās aprakstam?",
              ["trīs lielumi ir saistīti", "abos ir kilometri",
               "abos ir nauda", "nekas"], 0),
         ]},
        {"sr": "Salīdzina ātrumus un risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš brauc ātrāk: 50 km/h vai 65 km/h?",
              ["65 km/h", "50 km/h", "vienādi", "nevar noteikt"], 0),
             ("Vilciens brauc 90 km/h 3 stundas. Cik km tas nobrauc?",
              ["270 km", "30 km", "93 km", "87 km"], 0),
             ("Cik maksā 5 kg burkānu, ja 1 kg maksā 2 eiro?",
              ["10 eiro", "7 eiro", "3 eiro", "2 eiro"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina ceļu, laiku, ātrumu un samaksu",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("v = 60 km/h, t = 3 h;   s = …… km", "180"),
                         ("s = 120 km, v = 40 km/h;   t = …… h", "3"),
                         ("s = 150 km, t = 3 h;   v = …… km/h", "50"),
                         ("Cena 2 eiro, skaits 7;   samaksa …… eiro", "14")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("v = 15 km/h, t = 2 h;   s = …… km", "30"),
                         ("s = 100 km, v = 50 km/h;   t = …… h", "2"),
                         ("s = 80 km, t = 2 h;   v = …… km/h", "40"),
                         ("Cena 3 eiro, skaits 4;   samaksa …… eiro", "12")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("v = 80 km/h, t = 4 h;   s = …… km", "320"),
                         ("s = 90 km, v = 30 km/h;   t = …… h", "3"),
                         ("s = 12 km, t = 3 h;   v = …… km/h", "4"),
                         ("Cena 5 eiro, skaits 6;   samaksa …… eiro", "30")]},
         ]},
        {"sr": "Nosaka cenu, skaitu un skaidro ātruma nozīmi",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Samaksa 10 eiro, skaits 5;  cena …… eiro", "2"),
                         ("Samaksa 20 eiro, cena 4 eiro;  skaits ……", "5"),
                         ("60 km/h nozīmē, ka 1 stundā veic …… km", "60")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Samaksa 6 eiro, skaits 3;  cena …… eiro", "2"),
                         ("Samaksa 40 eiro, cena 8 eiro;  skaits ……", "5"),
                         ("45 km/h nozīmē, ka 1 stundā veic …… km", "45")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Samaksa 24 eiro, skaits 6;  cena …… eiro", "4"),
                         ("Samaksa 35 eiro, cena 7 eiro;  skaits ……", "5"),
                         ("30 km/h nozīmē, ka 1 stundā veic …… km", "30")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar vairākiem soļiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Automašīna brauc ar ātrumu 70 km/h.   a) Cik km tā "
                        "nobrauks 3 stundās?   b) Cik ilgi tā brauks "
                        "350 km?   c) Cik km tā nobrauks 30 minūtēs?   "
                        "d) Kurš no šiem ceļiem ir visgarākais?",
              "kriteriji": ["a) 70 · 3 = 210 km.   (1 p.)",
                            "b) 350 : 70 = 5 h.   (1 p.)",
                            "c) 70 : 2 = 35 km.   (1 p.)",
                            "d) Visgarākais ir 350 km.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Veikalā 1 kg ābolu maksā 3 eiro.   a) Cik maksā "
                        "4 kg?   b) Cik kg var nopirkt par 27 eiro?   "
                        "c) Cik maksā 500 g?   d) Kurš pirkums ir "
                        "dārgākais?",
              "kriteriji": ["a) 3 · 4 = 12 eiro.   (1 p.)",
                            "b) 27 : 3 = 9 kg.   (1 p.)",
                            "c) 3 : 2 = 1,50 eiro.   (1 p.)",
                            "d) Dārgākais ir pirkums par 27 eiro.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Gājējs iet ar ātrumu 5 km/h.   a) Cik km viņš "
                        "noiet 3 stundās?   b) Cik ilgi viņš ies 20 km?   "
                        "c) Cik km viņš noiet 2 stundās?   d) Par cik km "
                        "pirmais ceļš ir garāks nekā trešais?",
              "kriteriji": ["a) 5 · 3 = 15 km.   (1 p.)",
                            "b) 20 : 5 = 4 h.   (1 p.)",
                            "c) 5 · 2 = 10 km.   (1 p.)",
                            "d) 15 − 10 = 5 km.   (1 p.)"]},
         ]},
        {"sr": "Skaidro risinājuma gaitu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Kustība un laiks", "vieta": 5.0,
              "ievads": "Vilciens izbrauca plkst. 9.00 un brauc ar ātrumu "
                        "60 km/h.",
              "jaut": [("Cik km tas nobrauc līdz plkst. 12.00?", 1),
                       ("Cikos tas būs nobraucis 300 km?", 1),
                       ("Paskaidro, kā aprēķināji laiku!", 1)],
              "atbildes": ["1) 3 · 60 = 180 km.   (1 p.)",
                           "2) Plkst. 14.00.   (1 p.)",
                           "3) Ceļu dala ar ātrumu: 300 : 60 = 5 h.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Iepirkšanās", "vieta": 5.0,
              "ievads": "Burtnīca maksā 2 eiro, bet pildspalva — 3 eiro.",
              "jaut": [("Cik maksā 4 burtnīcas un 2 pildspalvas?", 1),
                       ("Cik naudas atliks no 20 eiro?", 1),
                       ("Cik pildspalvu var nopirkt par atlikušo naudu?",
                        1)],
              "atbildes": ["1) 8 + 6 = 14 eiro.   (1 p.)",
                           "2) 20 − 14 = 6 eiro.   (1 p.)",
                           "3) 6 : 3 = 2 pildspalvas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Divi velosipēdisti",
              "vieta": 5.0,
              "ievads": "Divi velosipēdisti brauc 2 stundas: pirmais ar "
                        "12 km/h, otrs — ar 15 km/h.",
              "jaut": [("Cik km nobrauc katrs?", 1),
                       ("Par cik km vairāk nobrauc otrs?", 1),
                       ("Kurš 36 km veiks ātrāk? Kāpēc?", 1)],
              "atbildes": ["1) 24 km un 30 km.   (1 p.)",
                           "2) 30 − 24 = 6 km.   (1 p.)",
                           "3) Otrs, jo viņa ātrums ir lielāks.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
