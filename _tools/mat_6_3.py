# -*- coding: utf-8 -*-
"""Matemātika, 6. klase. 6.3. Komats, reizinot un dalot decimāldaļas.

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 6. klase, 6.3. temats): decimāldaļu
reizināšana un dalīšana, komata vieta reizinājumā pēc ciparu skaita aiz
komata, reizināšana un dalīšana ar 10; 100; 1000 un ar 0,1; 0,01; 0,001,
dalāmā un dalītāja pareizināšana ar vienu skaitli, dalījums, kas mazāks nekā
1, aptuvenās vērtības novērtēšana un pāreja starp parasto daļu un
decimāldaļu.
"""

PRIEKSMETS = "Matemātika  |  6. klase"
TEMATS = "6.3."
NOSAUKUMS = "Kā izpratne par komata lietojumu palīdz, ja reizina un dala " \
            "decimāldaļas?"

ATGADNE = [
    "Reizinot: sareizina kā veselus skaitļus; reizinājumā aiz komata ir "
    "tikpat ciparu, cik abiem reizinātājiem kopā.   0,3 · 0,4 = 0,12",
    "Reizinot ar 10; 100; 1000, komatu pārceļ pa labi; dalot ar tiem — pa "
    "kreisi. Reizināt ar 0,1 ir tas pats, kas dalīt ar 10.",
    "Dalot dalāmo un dalītāju var pareizināt ar vienu skaitli — dalījums "
    "nemainās:   1,2 : 0,4 = 12 : 4 = 3   ·   ja dala ar lielāku skaitli, "
    "dalījums ir mazāks nekā 1.",
]

FD = {
    "veids": "fd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 6.3. temata beigās. Pārbauda "
                "decimāldaļu reizināšanu un dalīšanu, komata vietu "
                "rezultātā, reizināšanu un dalīšanu ar 10; 100; 1000 un ar "
                "0,1; 0,01, kā arī rezultāta novērtēšanu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosaka ciparu skaitu aiz komata",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ciparu aiz komata ir reizinājumā 0,3 · 0,4?",
              ["2", "1", "3", "0"], 0),
             ("Cik ciparu aiz komata ir reizinājumā 1,25 · 0,2?",
              ["3", "2", "1", "4"], 0),
             ("Kas nosaka ciparu skaitu aiz komata reizinājumā?",
              ["abu reizinātāju ciparu skaits", "lielākais reizinātājs",
               "mazākais reizinātājs", "veselo daļa"], 0),
         ]},
        {"sr": "Reizina decimāldaļu ar veselu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 0,7 · 3?", ["2,1", "21", "0,21", "3,7"], 0),
             ("Cik ir 1,2 · 4?", ["4,8", "48", "0,48", "5,2"], 0),
             ("Cik ir 2,5 · 6?", ["15", "1,5", "150", "8,5"], 0),
         ]},
        {"sr": "Reizina divas decimāldaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 0,3 · 0,4?", ["0,12", "1,2", "12", "0,7"], 0),
             ("Cik ir 0,5 · 0,6?", ["0,3", "3", "0,03", "1,1"], 0),
             ("Cik ir 1,5 · 0,2?", ["0,3", "3", "0,03", "1,7"], 0),
         ]},
        {"sr": "Reizina ar 10; 100; 1000",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 0,45 · 100?", ["45", "4,5", "450", "0,45"], 0),
             ("Cik ir 3,6 · 10?", ["36", "3,6", "360", "0,36"], 0),
             ("Uz kuru pusi pārceļ komatu, reizinot ar 100?",
              ["pa labi par 2 vietām", "pa kreisi par 2 vietām",
               "pa labi par 1 vietu", "komatu nepārceļ"], 0),
         ]},
        {"sr": "Reizina ar 0,1; 0,01",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 25 · 0,1?", ["2,5", "250", "0,25", "25"], 0),
             ("Cik ir 8 · 0,01?", ["0,08", "0,8", "80", "8"], 0),
             ("Ar ko ir līdzvērtīga reizināšana ar 0,1?",
              ["dalīšanai ar 10", "reizināšanai ar 10", "dalīšanai ar 100",
               "saskaitīšanai ar 10"], 0),
         ]},
        {"sr": "Dala decimāldaļu ar veselu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 4,8 : 4?", ["1,2", "12", "0,12", "2,4"], 0),
             ("Cik ir 7,5 : 5?", ["1,5", "15", "0,15", "2,5"], 0),
             ("Cik ir 0,9 : 3?", ["0,3", "3", "0,03", "0,6"], 0),
         ]},
        {"sr": "Dala ar 10; 100; 1000",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 45 : 100?", ["0,45", "4,5", "450", "0,045"], 0),
             ("Cik ir 6,2 : 10?", ["0,62", "62", "0,062", "620"], 0),
             ("Uz kuru pusi pārceļ komatu, dalot ar 10?",
              ["pa kreisi par 1 vietu", "pa labi par 1 vietu",
               "pa kreisi par 2 vietām", "komatu nepārceļ"], 0),
         ]},
        {"sr": "Dala ar decimāldaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 1,2 : 0,4?", ["3", "0,3", "30", "0,48"], 0),
             ("Cik ir 2,4 : 0,6?", ["4", "0,4", "40", "1,44"], 0),
             ("Kas jādara vispirms, dalot ar decimāldaļu?",
              ["abus pareizina, lai dalītājs būtu vesels",
               "dalāmo noapaļo", "komatu izlaiž", "dalītāju saīsina"], 0),
         ]},
        {"sr": "Zina, ka pareizināšana nemaina dalījumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds 1,2 : 0,4, ja abus pareizina ar 10?",
              ["12 : 4", "12 : 0,4", "1,2 : 4", "120 : 4"], 0),
             ("Kas mainās, ja dalāmo un dalītāju pareizina ar 10?",
              ["nekas — dalījums paliek tas pats", "dalījums aug 10 reižu",
               "dalījums sarūk 10 reižu", "dalījums kļūst vesels"], 0),
             ("Uz kuru īpašību balstās šis paņēmiens?",
              ["daļas pamatīpašību", "reizināšanas secību",
               "saskaitīšanas likumu", "komata likumu"], 0),
         ]},
        {"sr": "Spriež par dalījuma lielumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir dalījums, ja dala ar lielāku skaitli?",
              ["mazāks nekā 1", "lielāks nekā 1", "vienāds ar 1",
               "vienāds ar 0"], 0),
             ("Kurš dalījums ir lielāks nekā 1?",
              ["6 : 0,5", "0,5 : 6", "3 : 4", "2 : 8"], 0),
             ("Ar ko sākas pieraksts dalījumam, kas mazāks nekā 1?",
              ["ar 0,...", "ar 1,...", "ar veselu skaitli", "ar mīnusu"], 0),
         ]},
        {"sr": "Novērtē rezultāta aptuveno vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik aptuveni ir 4,9 · 2,1?", ["aptuveni 10", "aptuveni 7",
                                             "aptuveni 100", "aptuveni 2"], 0),
             ("Cik aptuveni ir 11,8 : 3,9?", ["aptuveni 3", "aptuveni 30",
                                              "aptuveni 8", "aptuveni 15"], 0),
             ("Kāpēc rezultātu novērtē?",
              ["lai pamanītu rupju kļūdu", "lai ietaupītu laiku",
               "lai nebūtu jārēķina", "lai zustu komats"], 0),
         ]},
        {"sr": "Lieto decimāldaļas situāciju uzdevumos",
         "stunda": TEMATS,
         "jautajumi": [
             ("1 kg ābolu maksā 1,20 eiro. Cik maksā 2,5 kg?",
              ["3 eiro", "2,4 eiro", "3,7 eiro", "30 eiro"], 0),
             ("Auto patērē 6,5 l uz 100 km. Cik patērēs 200 km?",
              ["13 l", "6,5 l", "65 l", "3,25 l"], 0),
             ("Lentu 4,5 m sagriež 0,5 m gabalos. Cik gabalu sanāk?",
              ["9", "4", "2,25", "5"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 6.3. temata noslēgumā. "
                "Pārbauda decimāldaļu reizināšanu un dalīšanu, komata vietu "
                "rezultātā, reizināšanu un dalīšanu ar 10; 100; 1000 un ar "
                "0,1; 0,01 un situāciju uzdevumus ar decimāldaļām.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Reizina decimāldaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 0,6 · 0,5?", ["0,3", "3", "0,03", "1,1"], 0),
             ("Cik ir 1,4 · 3?", ["4,2", "42", "0,42", "4,4"], 0),
             ("Cik ciparu aiz komata ir reizinājumā 0,25 · 0,4?",
              ["3", "2", "1", "4"], 0),
         ]},
        {"sr": "Reizina un dala ar 10; 100; 1000",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 0,38 · 100?", ["38", "3,8", "380", "0,038"], 0),
             ("Cik ir 74 : 1000?", ["0,074", "0,74", "7,4", "740"], 0),
             ("Cik ir 5,6 · 10?", ["56", "5,6", "560", "0,56"], 0),
         ]},
        {"sr": "Reizina un dala ar 0,1; 0,01",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 42 · 0,1?", ["4,2", "420", "0,42", "42"], 0),
             ("Cik ir 3 : 0,1?", ["30", "0,3", "3", "0,03"], 0),
             ("Ar ko ir līdzvērtīga reizināšana ar 0,01?",
              ["dalīšanai ar 100", "reizināšanai ar 100",
               "dalīšanai ar 10", "reizināšanai ar 10"], 0),
         ]},
        {"sr": "Dala decimāldaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 6,3 : 7?", ["0,9", "9", "0,09", "1,9"], 0),
             ("Cik ir 3,6 : 0,9?", ["4", "0,4", "40", "3,24"], 0),
             ("Kas jādara vispirms, dalot ar decimāldaļu?",
              ["abus pareizina, lai dalītājs būtu vesels",
               "dalāmo noapaļo", "komatu izlaiž", "dalītāju saīsina"], 0),
         ]},
        {"sr": "Spriež par rezultāta lielumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš dalījums ir lielāks nekā 1?",
              ["8 : 0,4", "0,4 : 8", "3 : 5", "1 : 4"], 0),
             ("Cik aptuveni ir 5,1 · 1,9?",
              ["aptuveni 10", "aptuveni 7", "aptuveni 100", "aptuveni 3"], 0),
             ("Vai 12 · 0,8 ir lielāks nekā 12?",
              ["nē", "jā", "vienāds", "nevar noteikt"], 0),
         ]},
        {"sr": "Lieto decimāldaļas uzdevumos",
         "stunda": TEMATS,
         "jautajumi": [
             ("1 m auduma maksā 4,50 eiro. Cik maksā 3 m?",
              ["13,50 eiro", "7,50 eiro", "1,50 eiro", "135 eiro"], 0),
             ("Lentu 6,4 m sagriež 0,8 m gabalos. Cik gabalu sanāk?",
              ["8", "5,12", "6", "0,8"], 0),
             ("Cik maksā 0,5 kg konfekšu, ja 1 kg maksā 8,40 eiro?",
              ["4,20 eiro", "16,80 eiro", "8,90 eiro", "0,42 eiro"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Reizina un dala decimāldaļas",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("0,4 · 0,7 = ……", "0,28"),
                         ("2,5 · 4 = ……", "10"),
                         ("8,4 : 4 = ……", "2,1"),
                         ("1,8 : 0,6 = ……", "3")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("0,6 · 0,3 = ……", "0,18"),
                         ("1,25 · 8 = ……", "10"),
                         ("9,6 : 3 = ……", "3,2"),
                         ("4,5 : 0,9 = ……", "5")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("0,8 · 0,5 = ……", "0,4"),
                         ("3,5 · 6 = ……", "21"),
                         ("7,2 : 6 = ……", "1,2"),
                         ("2,4 : 0,8 = ……", "3")]},
         ]},
        {"sr": "Reizina un dala ar 10; 100 un ar 0,1; 0,01",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Komata pārcelšana",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("0,74 · 100 = ……", "74"),
                         ("56 : 1000 = ……", "0,056"),
                         ("3 : 0,1 = ……", "30")]},
             {"tips": "parveide", "virs": "Komata pārcelšana",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("0,9 · 1000 = ……", "900"),
                         ("48 : 100 = ……", "0,48"),
                         ("7 · 0,01 = ……", "0,07")]},
             {"tips": "parveide", "virs": "Komata pārcelšana",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2,35 · 10 = ……", "23,5"),
                         ("6 : 10 = ……", "0,6"),
                         ("25 · 0,1 = ……", "2,5")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar decimāldaļām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Veikalā 1 kg ābolu maksā 1,40 eiro, 1 kg bumbieru "
                        "— 2,20 eiro.   a) Cik maksā 2,5 kg ābolu?   "
                        "b) Cik maksā 1,5 kg bumbieru?   c) Cik jāmaksā "
                        "kopā?   d) Cik atliks no 10 eiro?",
              "kriteriji": ["a) 1,40 · 2,5 = 3,50 eiro.   (1 p.)",
                            "b) 2,20 · 1,5 = 3,30 eiro.   (1 p.)",
                            "c) 3,50 + 3,30 = 6,80 eiro.   (1 p.)",
                            "d) 10 − 6,80 = 3,20 eiro.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Automašīna patērē 7,5 l degvielas uz 100 km; "
                        "1 l maksā 1,60 eiro.   a) Cik litru patērēs "
                        "300 km?   b) Cik tas maksās?   c) Cik litru "
                        "patērēs 50 km?   d) Cik kilometrus var nobraukt "
                        "ar 15 l?",
              "kriteriji": ["a) 7,5 · 3 = 22,5 l.   (1 p.)",
                            "b) 22,5 · 1,60 = 36 eiro.   (1 p.)",
                            "c) 7,5 : 2 = 3,75 l.   (1 p.)",
                            "d) 15 : 7,5 · 100 = 200 km.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Auduma gabals ir 12,6 m garš; to sagriež 0,7 m "
                        "gabalos.   a) Cik gabalu sanāk?   b) Cik maksās "
                        "viss audums, ja 1 m maksā 3,50 eiro?   c) Cik "
                        "maksā viens gabals?   d) Cik maksās 5 gabali?",
              "kriteriji": ["a) 12,6 : 0,7 = 18 gabali.   (1 p.)",
                            "b) 12,6 · 3,50 = 44,10 eiro.   (1 p.)",
                            "c) 0,7 · 3,50 = 2,45 eiro.   (1 p.)",
                            "d) 2,45 · 5 = 12,25 eiro.   (1 p.)"]},
         ]},
        {"sr": "Skaidro komata lietojumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Komats reizinājumā", "vieta": 4.6,
              "ievads": "Zināms, ka 24 · 15 = 360.",
              "jaut": [("Cik ir 2,4 · 1,5?", 1), ("Cik ir 0,24 · 0,15?", 1),
                       ("Paskaidro, kā noteici komata vietu!", 1)],
              "atbildes": ["1) 3,6.   (1 p.)", "2) 0,036.   (1 p.)",
                           "3) Aiz komata ir tikpat ciparu, cik abiem "
                           "reizinātājiem kopā.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dalīšana ar decimāldaļu",
              "vieta": 4.6,
              "ievads": "Dota izteiksme  3,6 : 0,4.",
              "jaut": [("Ar ko pareizina dalāmo un dalītāju?", 1),
                       ("Uzraksti jauno dalījumu un aprēķini to!", 1),
                       ("Kāpēc dalījums nemainās?", 1)],
              "atbildes": ["1) Ar 10.   (1 p.)",
                           "2) 36 : 4 = 9.   (1 p.)",
                           "3) To pamato daļas pamatīpašība.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Novērtē rezultātu", "vieta": 4.6,
              "ievads": "Dotas izteiksmes  20 · 0,9  un  20 : 0,9.",
              "jaut": [("Kura vērtība ir mazāka nekā 20?", 1),
                       ("Aprēķini reizinājumu!", 1),
                       ("Paskaidro secinājumu!", 1)],
              "atbildes": ["1) Reizinājums 20 · 0,9.   (1 p.)",
                           "2) 20 · 0,9 = 18.   (1 p.)",
                           "3) Reizinot ar skaitli, kas mazāks nekā 1, "
                           "rezultāts sarūk.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
