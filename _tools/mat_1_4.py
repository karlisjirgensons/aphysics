# -*- coding: utf-8 -*-
"""Matemātika, 1. klase. 1.4. Kā pieraksta un salīdzina skaitļus, kuri ir
lielāki nekā 10?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 1. klase, 1.4. temats): skaitļi līdz 100
un to decimālais sastāvs, skaitļu lasīšana un pieraksts, salīdzināšana ar
«<» un «>», sakārtošana, skaitļu virknes, vieta uz skaitļu taisnes,
mērvienības (cm, dm, m), nauda (eiro, centi) un laiks (gads, mēnesis,
nedēļa, diennakts, pilnas stundas).
"""

PRIEKSMETS = "Matemātika  |  1. klase"
TEMATS = "1.4."
NOSAUKUMS = "Kā pieraksta un salīdzina skaitļus, kuri ir lielāki nekā 10?"

ATGADNE = [
    "1 desmits = 10 vieni   ·   1 simts = 10 desmiti = 100 vieni   ·   "
    "zīmes:  >  lielāks   ·   <  mazāks",
    "1 dm = 10 cm   ·   1 m = 10 dm = 100 cm   ·   1 eiro = 100 centi",
    "Gadā ir 12 mēneši   ·   nedēļā 7 dienas   ·   diennaktī 24 stundas",
]

FD = {
    "veids": "fd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 1.4. temata beigās. Pārbauda skaitļu līdz "
                "100 pierakstu un decimālo sastāvu, salīdzināšanu un "
                "sakārtošanu, skaitļu virknes, vietu skaitļu rindā, garuma "
                "mērvienības, naudu un laika vienības.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Pieraksta ar cipariem nosauktu skaitli līdz 100",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā ar cipariem pieraksta skaitli «piecdesmit trīs»?",
              ["35", "53", "503", "530"], 1),
             ("Kā ar cipariem pieraksta skaitli «septiņdesmit»?",
              ["7", "17", "70", "77"], 2),
             ("Kā ar cipariem pieraksta skaitli «astoņpadsmit»?",
              ["8", "18", "81", "108"], 1),
         ]},
        {"sr": "Nosaka skaitļa decimālo sastāvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik desmitu ir skaitlī 47?", ["4", "7", "11", "47"], 0),
             ("Cik vienu ir skaitlī 62?", ["2", "6", "8", "62"], 0),
             ("Cik desmitu ir skaitlī 90?", ["0", "9", "10", "90"], 1),
         ]},
        {"sr": "Veido skaitli no desmitiem un vieniem",
         "stunda": TEMATS,
         "jautajumi": [
             ("4 desmiti un 6 vieni — kurš tas ir skaitlis?",
              ["10", "46", "64", "406"], 1),
             ("8 desmiti un 0 vieni — kurš tas ir skaitlis?",
              ["8", "18", "80", "800"], 2),
             ("3 desmiti un 9 vieni — kurš tas ir skaitlis?",
              ["12", "39", "93", "309"], 1),
         ]},
        {"sr": "Skaidro skaitļu 11–19 uzbūvi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik desmitu ir katrā skaitlī no 11 līdz 19?",
              ["1", "2", "10", "19"], 0),
             ("Skaitlis 13 ir 1 desmits un …",
              ["1 viens", "3 vieni", "10 vieni", "13 vieni"], 1),
             ("Kurš skaitlis ir 1 desmits un 7 vieni?",
              ["7", "17", "71", "107"], 1),
         ]},
        {"sr": "Zina, kā veidojas simts",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik desmitu ir vienā simtā?", ["1", "10", "100", "1000"], 1),
             ("Cik vienu ir vienā simtā?", ["10", "50", "100", "1000"], 2),
             ("Kurš skaitlis seko tūlīt pēc 99?",
              ["90", "98", "100", "109"], 2),
         ]},
        {"sr": "Salīdzina divciparu skaitļus ar zīmēm «<» un «>»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  34 …… 43?", [">", "<", "=", "+"], 1),
             ("Kura zīme jāliek:  70 …… 7?", [">", "<", "=", "−"], 0),
             ("Kurš skaitlis ir lielākais?", ["19", "29", "82", "78"], 2),
         ]},
        {"sr": "Sakārto skaitļus augošā un dilstošā secībā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurā rindā skaitļi ir augošā secībā?",
              ["12, 21, 34, 40", "40, 34, 21, 12", "21, 12, 40, 34",
               "34, 12, 40, 21"], 0),
             ("Kurā rindā skaitļi ir dilstošā secībā?",
              ["15, 25, 35, 45", "45, 35, 25, 15", "25, 15, 45, 35",
               "35, 45, 15, 25"], 1),
             ("Kurš skaitlis ir mazākais?", ["61", "16", "60", "66"], 1),
         ]},
        {"sr": "Nosaka skaitļa kaimiņus skaitļu rindā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir tūlīt pirms 40?", ["30", "39", "41", "50"],
              1),
             ("Kurš skaitlis ir tūlīt pēc 59?", ["50", "58", "60", "69"], 2),
             ("Starp kuriem skaitļiem atrodas 75?",
              ["74 un 76", "70 un 80", "65 un 85", "75 un 76"], 0),
         ]},
        {"sr": "Turpina skaitļu virkni",
         "stunda": TEMATS,
         "jautajumi": [
             ("Virkne:  10, 20, 30, …  Kurš skaitlis ir nākamais?",
              ["31", "35", "40", "50"], 2),
             ("Virkne:  5, 10, 15, …  Kurš skaitlis ir nākamais?",
              ["16", "18", "20", "25"], 2),
             ("Virkne:  100, 90, 80, …  Kurš skaitlis ir nākamais?",
              ["60", "70", "79", "81"], 1),
         ]},
        {"sr": "Lieto garuma mērvienības cm, dm un m",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik centimetru ir 1 dm?", ["1", "10", "100", "1000"], 1),
             ("Cik decimetru ir 1 m?", ["10", "50", "100", "1000"], 0),
             ("Cik centimetru ir 1 m?", ["10", "50", "100", "1000"], 2),
         ]},
        {"sr": "Lieto naudas vienības — eiro un centus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik centu ir 1 eiro?", ["10", "50", "100", "1000"], 2),
             ("Cik centu ir 2 eiro?", ["20", "100", "200", "2000"], 2),
             ("Konfekte maksā 50 centus. Cik konfekšu var nopirkt "
              "par 1 eiro?",
              ["1", "2", "5", "10"], 1),
         ]},
        {"sr": "Zina laika vienības un nolasa pilnas stundas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik mēnešu ir gadā?", ["7", "10", "12", "24"], 2),
             ("Cik stundu ir diennaktī?", ["7", "12", "24", "60"], 2),
             ("Stundu rādītājs rāda uz 3, minūšu rādītājs uz 12. Cik ir "
              "pulkstenis?",
              ["3:00", "3:12", "12:03", "12:15"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 1.4. temata noslēgumā. "
                "Pārbauda skaitļu līdz 100 pierakstu un decimālo sastāvu, "
                "salīdzināšanu un sakārtošanu, skaitļu virknes, mērvienību, "
                "naudas un laika vienību lietojumu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Uzdevumu tekstu lasa skolotājs. Atbildi raksti tam atvēlētajā "
              "vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Pieraksta un lasa skaitļus līdz 100",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā ar cipariem pieraksta «sešdesmit astoņi»?",
              ["68", "86", "608", "680"], 0),
             ("Kā ar cipariem pieraksta «deviņpadsmit»?",
              ["9", "19", "91", "109"], 1),
             ("Kā ar cipariem pieraksta «četrdesmit»?",
              ["4", "14", "40", "44"], 2),
         ]},
        {"sr": "Nosaka skaitļa decimālo sastāvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik desmitu ir skaitlī 56?", ["5", "6", "11", "56"], 0),
             ("Cik vienu ir skaitlī 83?", ["3", "8", "11", "83"], 0),
             ("5 desmiti un 4 vieni — kurš tas ir skaitlis?",
              ["45", "54", "504", "9"], 1),
         ]},
        {"sr": "Salīdzina divciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  27 …… 72?", [">", "<", "=", "+"], 1),
             ("Kurš skaitlis ir lielākais?", ["48", "84", "44", "80"], 1),
             ("Kurš skaitlis ir mazākais?", ["31", "13", "30", "33"], 1),
         ]},
        {"sr": "Nosaka skaitļa vietu skaitļu rindā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir tūlīt pēc 79?", ["70", "78", "80", "89"], 2),
             ("Kurš skaitlis ir tūlīt pirms 50?", ["40", "49", "51", "60"],
              1),
             ("Virkne:  20, 30, 40, …  Kurš skaitlis ir nākamais?",
              ["41", "45", "50", "60"], 2),
         ]},
        {"sr": "Lieto garuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik cm ir 1 dm?", ["1", "10", "100", "1000"], 1),
             ("Cik cm ir 1 m?", ["10", "50", "100", "1000"], 2),
             ("Cik dm ir 1 m?", ["10", "20", "100", "1000"], 0),
         ]},
        {"sr": "Lieto naudas un laika vienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik centu ir 1 eiro?", ["10", "50", "100", "1000"], 2),
             ("Cik dienu ir nedēļā?", ["5", "7", "12", "24"], 1),
             ("Cik stundu ir diennaktī?", ["12", "20", "24", "60"], 2),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pieraksta skaitli pēc tā decimālā sastāva un pārveido "
               "mērvienības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti tukšajā vietā pareizo skaitli! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("7 desmiti un 2 vieni = ……", "72"),
                         ("«Trīsdesmit deviņi» ar cipariem = ……", "39"),
                         ("Skaitlī 64 ir …… desmiti", "6"),
                         ("1 m = …… cm", "100")]},
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti tukšajā vietā pareizo skaitli! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("5 desmiti un 8 vieni = ……", "58"),
                         ("«Divdesmit seši» ar cipariem = ……", "26"),
                         ("Skaitlī 91 ir …… desmiti", "9"),
                         ("1 dm = …… cm", "10")]},
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti tukšajā vietā pareizo skaitli! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("6 desmiti un 3 vieni = ……", "63"),
                         ("«Astoņdesmit viens» ar cipariem = ……", "81"),
                         ("Skaitlī 47 ir …… vieni", "7"),
                         ("1 eiro = …… centi", "100")]},
         ]},
        {"sr": "Salīdzina divciparu skaitļus",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp skaitļiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("35  ……  53", "<"), ("80  ……  8", ">"),
                         ("46  ……  46", "=")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp skaitļiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("62  ……  26", ">"), ("19  ……  91", "<"),
                         ("70  ……  70", "=")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp skaitļiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("48  ……  84", "<"), ("57  ……  55", ">"),
                         ("100  ……  100", "=")]},
         ]},
        {"sr": "Veido skaitļu virkni un sakārto skaitļus",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Skaitļu virknes", "vieta": 6.0,
              "ievads": "Dota virkne:  10,  20,  30,  40",
              "jaut": [("Pieraksti divus nākamos virknes skaitļus!", 1),
                       ("Pieraksti skaitli, kas ir tūlīt pirms 30!", 1),
                       ("Sakārto augošā secībā skaitļus  45,  14,  41!", 1),
                       ("Pieraksti lielāko divciparu skaitli!", 1)],
              "atbildes": ["1) 50 un 60.   (1 p.)", "2) 29.   (1 p.)",
                           "3) 14,  41,  45.   (1 p.)", "4) 99.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Skaitļu virknes", "vieta": 6.0,
              "ievads": "Dota virkne:  5,  10,  15,  20",
              "jaut": [("Pieraksti divus nākamos virknes skaitļus!", 1),
                       ("Pieraksti skaitli, kas ir tūlīt pēc 19!", 1),
                       ("Sakārto augošā secībā skaitļus  63,  36,  60!", 1),
                       ("Pieraksti mazāko divciparu skaitli!", 1)],
              "atbildes": ["1) 25 un 30.   (1 p.)", "2) 20.   (1 p.)",
                           "3) 36,  60,  63.   (1 p.)", "4) 10.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Skaitļu virknes", "vieta": 6.0,
              "ievads": "Dota virkne:  100,  90,  80,  70",
              "jaut": [("Pieraksti divus nākamos virknes skaitļus!", 1),
                       ("Pieraksti skaitli, kas ir tūlīt pirms 60!", 1),
                       ("Sakārto dilstošā secībā skaitļus  28,  82,  20!",
                        1),
                       ("Pieraksti skaitli, kas ir par 10 lielāks nekā 45!",
                        1)],
              "atbildes": ["1) 60 un 50.   (1 p.)", "2) 59.   (1 p.)",
                           "3) 82,  28,  20.   (1 p.)", "4) 55.   (1 p.)"]},
         ]},
        {"sr": "Lieto naudas un laika vienības sadzīves situācijā",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Nauda un laiks", "vieta": 5.5,
              "ievads": "Atbildi uz jautājumiem un pieraksti risinājumu!",
              "jaut": [("Cik centu ir 1 eiro?", 1),
                       ("Cepums maksā 20 centus. Cik maksā 3 cepumi?", 1),
                       ("Cik mēnešu ir gadā?", 1)],
              "atbildes": ["1) 100 centi.   (1 p.)",
                           "2) 20 + 20 + 20 = 60; atbilde: 60 centi.   "
                           "(1 p.)",
                           "3) 12 mēneši.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Nauda un laiks", "vieta": 5.5,
              "ievads": "Atbildi uz jautājumiem un pieraksti risinājumu!",
              "jaut": [("Cik stundu ir diennaktī?", 1),
                       ("Zīmulis maksā 30 centus. Cik maksā 2 zīmuļi?", 1),
                       ("Cik dienu ir nedēļā?", 1)],
              "atbildes": ["1) 24 stundas.   (1 p.)",
                           "2) 30 + 30 = 60; atbilde: 60 centi.   (1 p.)",
                           "3) 7 dienas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Nauda un laiks", "vieta": 5.5,
              "ievads": "Atbildi uz jautājumiem un pieraksti risinājumu!",
              "jaut": [("Cik centu ir 2 eiro?", 1),
                       ("Burtnīca maksā 50 centus. Cik burtnīcu var nopirkt "
                        "par 1 eiro?", 1),
                       ("Cik dienu ir divās nedēļās?", 1)],
              "atbildes": ["1) 200 centi.   (1 p.)",
                           "2) 100 : 50 = 2; atbilde: 2 burtnīcas.   (1 p.)",
                           "3) 7 + 7 = 14; atbilde: 14 dienas.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
