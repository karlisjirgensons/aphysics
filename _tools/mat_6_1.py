# -*- coding: utf-8 -*-
"""Matemātika, 6. klase. 6.1. Kā kopumu sadala noteiktā attiecībā?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 6. klase, 6.1. temats): skaitļu attiecība
un tās pieraksta veidi (a pret b; a : b; {a|b}), vienību kopīgais skaits
attiecībā a : b : c, kopuma sadalīšana dotā attiecībā, tieši un apgriezti
proporcionāli lielumi un nezināmā lieluma aprēķināšana, mērogs un attāluma
aprēķināšana kartē un dabā.
"""

PRIEKSMETS = "Matemātika  |  6. klase"
TEMATS = "6.1."
NOSAUKUMS = "Kā kopumu sadala noteiktā attiecībā?"

ATGADNE = [
    "Attiecību pieraksta dažādi:   3 pret 2   ·   3 : 2   ·   {3|2}   — tā "
    "rāda, cik reižu viens lielums ir lielāks nekā otrs.",
    "Sadalīšana attiecībā 2 : 3:   vienību kopā 2 + 3 = 5   ·   kopumu dala "
    "ar 5   ·   daļas reizina ar 2 un ar 3.",
    "Mērogs 1 : 1000 nozīmē, ka 1 cm kartē ir 1000 cm dabā   ·   attālums "
    "dabā = attālums kartē · mērogs.",
]

FD = {
    "veids": "fd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 6.1. temata beigās. Pārbauda attiecības "
                "jēdzienu un pieraksta veidus, kopuma sadalīšanu dotā "
                "attiecībā, tieši un apgriezti proporcionālus lielumus un "
                "mēroga lietošanu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro, ko rāda skaitļu attiecība",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda skaitļu attiecība?",
              ["cik reižu viens ir lielāks", "par cik viens ir lielāks",
               "abu summu", "abu starpību"], 0),
             ("Kāda ir skaitļu 12 un 4 attiecība?",
              ["3", "8", "16", "48"], 0),
             ("Kāda ir skaitļu 20 un 5 attiecība?",
              ["4", "15", "25", "100"], 0),
         ]},
        {"sr": "Zina attiecības pieraksta veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kuri pieraksti nozīmē vienu un to pašu?",
              ["3 pret 2,  3 : 2  un  {3|2}", "3 + 2 un {3|2}",
               "3 · 2 un {2|3}", "3 − 2 un {3|2}"], 0),
             ("Kā ar dalīšanas zīmi pieraksta attiecību {5|4}?",
              ["5 : 4", "4 : 5", "5 · 4", "5 + 4"], 0),
             ("Kā vārdiem izlasa pierakstu 7 : 3?",
              ["7 pret 3", "7 un 3", "7 mīnus 3", "7 reiz 3"], 0),
         ]},
        {"sr": "Nosaka divu lielumu attiecību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Klasē ir 12 meitenes un 8 zēni. Kāda ir to attiecība?",
              ["12 : 8", "8 : 12", "12 + 8", "12 − 8"], 0),
             ("Nogriežņi ir 15 cm un 5 cm gari. Kāda ir to attiecība?",
              ["3 : 1", "1 : 3", "5 : 1", "15 : 1"], 0),
             ("Kā nosaka divu lielumu attiecību?",
              ["vienu dala ar otru", "tos saskaita", "tos atņem",
               "tos sareizina"], 0),
         ]},
        {"sr": "Saīsina attiecību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Saīsini attiecību 12 : 8.",
              ["3 : 2", "2 : 3", "6 : 8", "12 : 4"], 0),
             ("Saīsini attiecību 20 : 30.",
              ["2 : 3", "3 : 2", "4 : 6", "10 : 15"], 0),
             ("Kāpēc attiecību saīsina?",
              ["lai skaitļi būtu mazāki", "lai skaitļi augtu",
               "lai zustu kārtība", "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Nosaka vienību kopīgo skaitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik vienību kopā ir attiecībā 2 : 3?",
              ["5", "6", "1", "23"], 0),
             ("Cik vienību kopā ir attiecībā 1 : 2 : 3?",
              ["6", "5", "3", "123"], 0),
             ("Kā nosaka vienību kopīgo skaitu?",
              ["saskaita attiecības locekļus", "tos sareizina",
               "tos atņem", "izvēlas lielāko"], 0),
         ]},
        {"sr": "Sadala kopumu attiecībā a : b",
         "stunda": TEMATS,
         "jautajumi": [
             ("Sadali 20 attiecībā 2 : 3.",
              ["8 un 12", "10 un 10", "5 un 15", "2 un 18"], 0),
             ("Sadali 35 attiecībā 3 : 4.",
              ["15 un 20", "20 un 15", "10 un 25", "7 un 28"], 0),
             ("Kāds ir pirmais solis, sadalot kopumu attiecībā?",
              ["atrod vienas vienības lielumu", "saskaita kopumu",
               "reizina kopumu", "atņem attiecību"], 0),
         ]},
        {"sr": "Sadala kopumu attiecībā a : b : c",
         "stunda": TEMATS,
         "jautajumi": [
             ("Sadali 60 attiecībā 1 : 2 : 3.",
              ["10; 20 un 30", "20; 20 un 20", "15; 20 un 25",
               "5; 10 un 45"], 0),
             ("Sadali 24 attiecībā 1 : 1 : 2.",
              ["6; 6 un 12", "8; 8 un 8", "4; 4 un 16", "12; 6 un 6"], 0),
             ("Cik liela ir viena vienība, sadalot 60 attiecībā 1 : 2 : 3?",
              ["10", "6", "20", "30"], 0),
         ]},
        {"sr": "Atpazīst tieši proporcionālus lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad lielumi ir tieši proporcionāli?",
              ["abi aug tikpat reižu", "viens aug, otrs sarūk",
               "abi nemainās", "tie ir vienādi"], 0),
             ("Kuri lielumi ir tieši proporcionāli?",
              ["preču skaits un samaksa", "ātrums un laiks",
               "strādnieku skaits un laiks", "malas garums un leņķis"], 0),
             ("Preču skaitu palielina 3 reizes. Kā mainās samaksa?",
              ["aug 3 reizes", "sarūk 3 reizes", "nemainās",
               "aug 2 reizes"], 0),
         ]},
        {"sr": "Atpazīst apgriezti proporcionālus lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad lielumi ir apgriezti proporcionāli?",
              ["viens aug, otrs sarūk tikpat reižu", "abi aug",
               "abi sarūk", "tie ir vienādi"], 0),
             ("Kuri lielumi ir apgriezti proporcionāli?",
              ["ātrums un ceļā pavadītais laiks", "preču skaits un cena",
               "malas garums un perimetrs", "laiks un veiktais ceļš"], 0),
             ("Ātrumu palielina 2 reizes. Kā mainās laiks?",
              ["sarūk 2 reizes", "aug 2 reizes", "nemainās",
               "sarūk 4 reizes"], 0),
         ]},
        {"sr": "Aprēķina nezināmo proporcionālu lielumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("3 burtnīcas maksā 6 eiro. Cik maksā 5 burtnīcas?",
              ["10 eiro", "8 eiro", "12 eiro", "15 eiro"], 0),
             ("4 strādnieki darbu paveic 6 stundās. Cik ilgi strādās "
              "8 strādnieki?", ["3 stundas", "12 stundas", "6 stundas",
                                "2 stundas"], 0),
             ("2 kg ābolu maksā 3 eiro. Cik maksā 6 kg?",
              ["9 eiro", "6 eiro", "12 eiro", "18 eiro"], 0),
         ]},
        {"sr": "Skaidro mēroga nozīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda mērogs?",
              ["attiecību starp attālumu kartē un dabā", "kartes lielumu",
               "attālumu dabā", "kartes krāsu"], 0),
             ("Ko nozīmē mērogs 1 : 1000?",
              ["1 cm kartē ir 1000 cm dabā", "1 cm dabā ir 1000 cm kartē",
               "karte ir 1000 cm gara", "dabā ir 1000 objektu"], 0),
             ("Kurš mērogs ir sīkāks?",
              ["1 : 100 000", "1 : 100", "1 : 1000", "1 : 10"], 0),
         ]},
        {"sr": "Aprēķina attālumu kartē un dabā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Mērogs 1 : 1000; kartē 5 cm. Cik ir dabā?",
              ["50 m", "5 m", "500 m", "5 km"], 0),
             ("Mērogs 1 : 100 000; dabā 4 km. Cik ir kartē?",
              ["4 cm", "40 cm", "0,4 cm", "400 cm"], 0),
             ("Kā aprēķina attālumu dabā?",
              ["attālumu kartē reizina ar mērogu",
               "attālumu kartē dala ar mērogu", "abus saskaita",
               "abus atņem"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 6.1. temata noslēgumā. "
                "Pārbauda attiecības noteikšanu un pierakstu, kopuma "
                "sadalīšanu attiecībā a : b un a : b : c, tieši un "
                "apgriezti proporcionālus lielumus un mēroga lietošanu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina attiecības nozīmi un pierakstu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda skaitļu attiecība?",
              ["cik reižu viens ir lielāks", "par cik viens ir lielāks",
               "abu summu", "abu starpību"], 0),
             ("Kā ar dalīšanas zīmi pieraksta {7|2}?",
              ["7 : 2", "2 : 7", "7 · 2", "7 + 2"], 0),
             ("Kāda ir skaitļu 18 un 6 attiecība?",
              ["3", "12", "24", "108"], 0),
         ]},
        {"sr": "Saīsina attiecību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Saīsini attiecību 15 : 25.",
              ["3 : 5", "5 : 3", "5 : 25", "15 : 5"], 0),
             ("Saīsini attiecību 24 : 18.",
              ["4 : 3", "3 : 4", "8 : 6", "12 : 9"], 0),
             ("Cik vienību kopā ir attiecībā 3 : 5?",
              ["8", "15", "2", "35"], 0),
         ]},
        {"sr": "Sadala kopumu dotā attiecībā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Sadali 40 attiecībā 3 : 5.",
              ["15 un 25", "25 un 15", "20 un 20", "10 un 30"], 0),
             ("Sadali 36 attiecībā 1 : 2 : 3.",
              ["6; 12 un 18", "12; 12 un 12", "9; 12 un 15",
               "4; 8 un 24"], 0),
             ("Kāds ir pirmais solis?",
              ["atrod vienas vienības lielumu", "saskaita kopumu",
               "reizina kopumu", "atņem attiecību"], 0),
         ]},
        {"sr": "Lieto tieši proporcionālus lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("5 burtnīcas maksā 10 eiro. Cik maksā 8 burtnīcas?",
              ["16 eiro", "13 eiro", "18 eiro", "20 eiro"], 0),
             ("Kad lielumi ir tieši proporcionāli?",
              ["abi aug tikpat reižu", "viens aug, otrs sarūk",
               "abi nemainās", "tie ir vienādi"], 0),
             ("3 kg kartupeļu maksā 2 eiro. Cik maksā 9 kg?",
              ["6 eiro", "4 eiro", "8 eiro", "18 eiro"], 0),
         ]},
        {"sr": "Lieto apgriezti proporcionālus lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("6 strādnieki darbu paveic 4 stundās. Cik ilgi strādās "
              "12 strādnieki?", ["2 stundas", "8 stundas", "6 stundas",
                                 "3 stundas"], 0),
             ("Kad lielumi ir apgriezti proporcionāli?",
              ["viens aug, otrs sarūk tikpat reižu", "abi aug",
               "abi sarūk", "tie ir vienādi"], 0),
             ("Ātrumu samazina 2 reizes. Kā mainās laiks?",
              ["aug 2 reizes", "sarūk 2 reizes", "nemainās",
               "aug 4 reizes"], 0),
         ]},
        {"sr": "Lieto mērogu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē mērogs 1 : 500?",
              ["1 cm kartē ir 500 cm dabā", "1 cm dabā ir 500 cm kartē",
               "karte ir 500 cm gara", "dabā ir 500 objektu"], 0),
             ("Mērogs 1 : 2000; kartē 3 cm. Cik ir dabā?",
              ["60 m", "6 m", "600 m", "6 km"], 0),
             ("Kā aprēķina attālumu kartē?",
              ["attālumu dabā dala ar mērogu",
               "attālumu dabā reizina ar mērogu", "abus saskaita",
               "abus atņem"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Nosaka, saīsina un lieto attiecību",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitļu 18 un 6 attiecība ir ……", "3"),
                         ("Saīsini attiecību 12 : 8:   ……", "3 : 2"),
                         ("Vienību skaits attiecībā 2 : 5 ir ……", "7"),
                         ("Sadali 21 attiecībā 2 : 5:   ……", "6 un 15")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitļu 24 un 8 attiecība ir ……", "3"),
                         ("Saīsini attiecību 20 : 30:   ……", "2 : 3"),
                         ("Vienību skaits attiecībā 3 : 4 ir ……", "7"),
                         ("Sadali 28 attiecībā 3 : 4:   ……", "12 un 16")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitļu 45 un 9 attiecība ir ……", "5"),
                         ("Saīsini attiecību 18 : 27:   ……", "2 : 3"),
                         ("Vienību skaits attiecībā 1 : 2 : 3 ir ……", "6"),
                         ("Sadali 30 attiecībā 1 : 2 : 3:   ……",
                          "5; 10 un 15")]},
         ]},
        {"sr": "Aprēķina attālumus pēc mēroga",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Mērogs",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Mērogs 1 : 1000; kartē 4 cm; dabā …… m", "40"),
                         ("Mērogs 1 : 100 000; dabā 5 km; kartē …… cm", "5"),
                         ("Mērogs 1 : 200; kartē 6 cm; dabā …… m", "12")]},
             {"tips": "parveide", "virs": "Mērogs",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Mērogs 1 : 500; kartē 8 cm; dabā …… m", "40"),
                         ("Mērogs 1 : 50 000; dabā 3 km; kartē …… cm", "6"),
                         ("Mērogs 1 : 100; kartē 25 cm; dabā …… m", "25")]},
             {"tips": "parveide", "virs": "Mērogs",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Mērogs 1 : 2000; kartē 7 cm; dabā …… m", "140"),
                         ("Mērogs 1 : 25 000; dabā 2 km; kartē …… cm", "8"),
                         ("Mērogs 1 : 400; kartē 5 cm; dabā …… m", "20")]},
         ]},
        {"sr": "Sadala kopumu attiecībā situāciju uzdevumā",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Sadalīšana attiecībā",
              "vieta": 5.6,
              "teksts": "Divi draugi 120 eiro sadala attiecībā 2 : 3.   "
                        "a) Cik vienību ir kopā?   b) Cik liela ir viena "
                        "vienība?   c) Cik eiro saņem katrs?   d) Par cik "
                        "eiro otrs saņem vairāk?",
              "kriteriji": ["a) 2 + 3 = 5 vienības.   (1 p.)",
                            "b) 120 : 5 = 24 eiro.   (1 p.)",
                            "c) 48 eiro un 72 eiro.   (1 p.)",
                            "d) 72 − 48 = 24 eiro.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Sadalīšana attiecībā",
              "vieta": 5.6,
              "teksts": "Nometnē 90 dalībniekus sadala trīs grupās "
                        "attiecībā 1 : 2 : 3.   a) Cik vienību ir kopā?   "
                        "b) Cik liela ir viena vienība?   c) Cik "
                        "dalībnieku ir katrā grupā?   d) Cik dalībnieku ir "
                        "lielākajā grupā vairāk nekā mazākajā?",
              "kriteriji": ["a) 1 + 2 + 3 = 6 vienības.   (1 p.)",
                            "b) 90 : 6 = 15 dalībnieki.   (1 p.)",
                            "c) 15; 30 un 45 dalībnieki.   (1 p.)",
                            "d) 45 − 15 = 30 dalībnieki.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Sadalīšana attiecībā",
              "vieta": 5.6,
              "teksts": "Betona maisījumā cements un smiltis ir attiecībā "
                        "1 : 4; kopā vajag 60 kg maisījuma.   a) Cik "
                        "vienību ir kopā?   b) Cik liela ir viena "
                        "vienība?   c) Cik kilogramu ir cementa un cik "
                        "smilšu?   d) Cik kilogramu cementa vajag 120 kg "
                        "maisījuma?",
              "kriteriji": ["a) 1 + 4 = 5 vienības.   (1 p.)",
                            "b) 60 : 5 = 12 kg.   (1 p.)",
                            "c) 12 kg cementa un 48 kg smilšu.   (1 p.)",
                            "d) 120 : 5 = 24 kg cementa.   (1 p.)"]},
         ]},
        {"sr": "Spriež par proporcionāliem lielumiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Tieši proporcionāli lielumi",
              "vieta": 4.6,
              "ievads": "4 vienādas burtnīcas maksā 6 eiro.",
              "jaut": [("Cik maksā viena burtnīca?", 1),
                       ("Cik maksā 10 burtnīcas?", 1),
                       ("Vai lielumi ir tieši proporcionāli? Pamato!", 1)],
              "atbildes": ["1) 6 : 4 = 1,5 eiro.   (1 p.)",
                           "2) 1,5 · 10 = 15 eiro.   (1 p.)",
                           "3) Jā — jo vairāk burtnīcu, jo lielāka samaksa "
                           "tikpat reižu.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Apgriezti proporcionāli lielumi",
              "vieta": 4.6,
              "ievads": "6 strādnieki darbu paveic 8 stundās.",
              "jaut": [("Cik stundas darbam vajadzīgas vienam "
                        "strādniekam?", 1),
                       ("Cik ilgi strādās 12 strādnieki?", 1),
                       ("Vai lielumi ir apgriezti proporcionāli? Pamato!",
                        1)],
              "atbildes": ["1) 6 · 8 = 48 stundas.   (1 p.)",
                           "2) 48 : 12 = 4 stundas.   (1 p.)",
                           "3) Jā — jo vairāk strādnieku, jo mazāk laika "
                           "tikpat reižu.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Mērogs", "vieta": 4.6,
              "ievads": "Kartes mērogs ir 1 : 50 000; divas pilsētas kartē "
                        "ir 6 cm attālumā.",
              "jaut": [("Cik centimetru tas ir dabā?", 1),
                       ("Cik kilometru tas ir dabā?", 1),
                       ("Cik centimetru kartē būtu 10 km?", 1)],
              "atbildes": ["1) 6 · 50 000 = 300 000 cm.   (1 p.)",
                           "2) 300 000 cm = 3 km.   (1 p.)",
                           "3) 1 000 000 : 50 000 = 20 cm.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
