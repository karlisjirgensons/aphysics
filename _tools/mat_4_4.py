# -*- coding: utf-8 -*-
"""Matemātika, 4. klase. 4.4. Kā daudzciparu skaitļus reizina un dala ar
divciparu skaitli?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 4. klase, 4.4. temats): pilni desmiti,
simti un tūkstoši kā reizinājumi ar 10, 100 un 1000; reizināšana ar pilniem
desmitiem; divciparu reizinātāja sadalīšana summā; dalīšana ar divciparu
skaitli un pārbaude ar reizināšanu; rezultāta aptuvenā vērtība; sakarības
«tik reižu vairāk» un «tik reižu mazāk» situāciju uzdevumos.
"""

PRIEKSMETS = "Matemātika  |  4. klase"
TEMATS = "4.4."
NOSAUKUMS = "Kā daudzciparu skaitļus reizina un dala ar divciparu skaitli?"

ATGADNE = [
    "Reizinot ar pilniem desmitiem, vispirms reizina ar ciparu un tad "
    "pieraksta nulli:   23 · 40 = 23 · 4 · 10 = 920",
    "Divciparu reizinātāju var sadalīt summā:   36 · 24 = 36 · 20 + 36 · 4 "
    "= 720 + 144 = 864",
    "Dalījumu pārbauda ar reizināšanu:   816 : 24 = 34,   jo   34 · 24 = 816",
]

FD = {
    "veids": "fd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 4.4. temata beigās. Pārbauda reizināšanu "
                "ar 10, 100 un pilniem desmitiem, divciparu skaitļu "
                "reizināšanu un dalīšanu, pārbaudi ar reizināšanu, aptuveno "
                "vērtību un situāciju uzdevumus.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, kā veidojas pilni desmiti, simti un tūkstoši",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik desmitu veido 100?", ["10", "100", "1000", "1"], 0),
             ("Cik simtu veido 1000?", ["10", "100", "1000", "1"], 0),
             ("Cik ir 10 · 1000?", ["10 000", "1000", "100 000", "110"], 0),
         ]},
        {"sr": "Reizina ar 10, 100 un 1000",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 47 · 10?", ["470", "4700", "57", "407"], 0),
             ("Cik ir 36 · 100?", ["3600", "360", "36 000", "136"], 0),
             ("Kā reizina ar 1000?",
              ["pieraksta trīs nulles", "pieraksta vienu nulli",
               "nosvītro trīs nulles", "pieskaita 1000"], 0),
         ]},
        {"sr": "Reizina ar pilniem desmitiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 23 · 40?", ["920", "92", "9200", "630"], 0),
             ("Cik ir 15 · 30?", ["450", "45", "4500", "180"], 0),
             ("Kā ērti aprēķināt 18 · 50?",
              ["18 · 5 un pieraksta nulli", "18 + 50", "18 · 5 · 5",
               "50 : 18"], 0),
         ]},
        {"sr": "Sadala reizinātāju summā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sadala reizinājumu 36 · 24?",
              ["36 · 20 + 36 · 4", "36 · 20 · 4", "36 + 20 + 4",
               "36 · 2 + 36 · 4"], 0),
             ("Cik ir 36 · 20?", ["720", "360", "72", "7200"], 0),
             ("Cik ir 36 · 24?", ["864", "144", "720", "840"], 0),
         ]},
        {"sr": "Reizina daudzciparu skaitli ar divciparu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 24 · 12?", ["288", "244", "240", "268"], 0),
             ("Cik ir 45 · 21?", ["945", "900", "495", "845"], 0),
             ("Cik ir 120 · 30?", ["3600", "360", "36 000", "1500"], 0),
         ]},
        {"sr": "Dala ar pilniem desmitiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 600 : 20?", ["30", "300", "3", "60"], 0),
             ("Cik ir 840 : 40?", ["21", "210", "84", "24"], 0),
             ("Kā ērti izdalīt 900 : 30?",
              ["90 : 3", "9 : 3", "900 : 3", "30 : 9"], 0),
         ]},
        {"sr": "Dala ar divciparu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 288 : 24?", ["12", "14", "24", "28"], 0),
             ("Cik ir 816 : 24?", ["34", "24", "36", "43"], 0),
             ("Cik ir 546 : 13?", ["42", "43", "52", "24"], 0),
         ]},
        {"sr": "Pārbauda aprēķinu ar pretējo darbību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pārbauda dalījumu?",
              ["reizina to ar dalītāju", "saskaita ar dalītāju",
               "dala vēlreiz", "to nepārbauda"], 0),
             ("Dalījums ir 34, dalītājs — 24. Kāds ir dalāmais?",
              ["816", "58", "10", "10 : 4"], 0),
             ("Kā pārbauda reizinājumu?",
              ["dala ar vienu reizinātāju", "reizina vēlreiz",
               "saskaita reizinātājus", "to nepārbauda"], 0),
         ]},
        {"sr": "Novērtē rezultāta aptuveno vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aptuveni cik ir 39 · 21?",
              ["ap 800", "ap 80", "ap 8000", "ap 60"], 0),
             ("Aptuveni cik ir 612 : 29?",
              ["ap 20", "ap 200", "ap 2", "ap 60"], 0),
             ("Kāpēc aprēķina aptuveno vērtību?",
              ["lai pārbaudītu, vai atbilde ir ticama",
               "lai atbilde būtu precīza", "lai rēķinātu ilgāk",
               "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Nosaka vairāku skaitļu reizinājumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 · 25 · 4?", ["200", "50", "100", "250"], 0),
             ("Kurā secībā ērtāk reizināt 5 · 17 · 20?",
              ["vispirms 5 · 20", "vispirms 17 · 5", "tikai pēc kārtas",
               "ir tikai viens veids"], 0),
             ("Cik ir 5 · 17 · 20?", ["1700", "170", "850", "3400"], 0),
         ]},
        {"sr": "Lieto sakarības «tik reižu vairāk» un «tik reižu mazāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā atrod skaitli, kas ir 12 reižu lielāks nekā 25?",
              ["reizina", "dala", "saskaita", "atņem"], 0),
             ("Skaitlis 480 ir 20 reižu lielāks nekā ……",
              ["24", "460", "500", "96"], 0),
             ("Cik reižu 720 ir lielāks nekā 30?",
              ["24", "690", "750", "12"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienā kastē ir 24 olas. Cik olu ir 15 kastēs?",
              ["360", "39", "240", "300"], 0),
             ("Biļete maksā 35 eiro. Cik maksā 12 biļetes?",
              ["420 eiro", "47 eiro", "350 eiro", "400 eiro"], 0),
             ("864 grāmatas vienādi saliek 24 plauktos. Cik ir vienā "
              "plauktā?", ["36", "840", "24", "42"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 4.4. temata noslēgumā. "
                "Pārbauda reizināšanu ar pilniem desmitiem, daudzciparu "
                "skaitļu reizināšanu un dalīšanu ar divciparu skaitli, "
                "pārbaudi ar pretējo darbību, aptuveno vērtību un situāciju "
                "uzdevumus.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Reizina ar 10, 100 un pilniem desmitiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 58 · 10?", ["580", "5800", "68", "508"], 0),
             ("Cik ir 42 · 100?", ["4200", "420", "42 000", "142"], 0),
             ("Cik ir 17 · 30?", ["510", "51", "5100", "470"], 0),
         ]},
        {"sr": "Reizina ar divciparu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 32 · 14?", ["448", "446", "320", "468"], 0),
             ("Cik ir 25 · 24?", ["600", "500", "610", "480"], 0),
             ("Kā sadala reizinājumu 43 · 12?",
              ["43 · 10 + 43 · 2", "43 · 10 · 2", "43 + 10 + 2",
               "43 · 1 + 43 · 2"], 0),
         ]},
        {"sr": "Dala ar divciparu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 480 : 20?", ["24", "240", "4", "26"], 0),
             ("Cik ir 448 : 14?", ["32", "34", "42", "28"], 0),
             ("Cik ir 750 : 25?", ["30", "25", "35", "3"], 0),
         ]},
        {"sr": "Pārbauda aprēķinu ar pretējo darbību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pārbauda dalījumu?",
              ["reizina to ar dalītāju", "saskaita ar dalītāju",
               "dala vēlreiz", "to nepārbauda"], 0),
             ("Dalījums ir 12, dalītājs — 15. Kāds ir dalāmais?",
              ["180", "27", "3", "150"], 0),
             ("Kā pārbauda reizinājumu 24 · 12 = 288?",
              ["288 : 12 = 24", "288 + 12", "24 + 12", "288 · 12"], 0),
         ]},
        {"sr": "Novērtē aptuveno vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aptuveni cik ir 41 · 19?",
              ["ap 800", "ap 80", "ap 8000", "ap 60"], 0),
             ("Aptuveni cik ir 810 : 41?",
              ["ap 20", "ap 200", "ap 2", "ap 40"], 0),
             ("Kāpēc noder aptuvenā vērtība?",
              ["var pamanīt rupju kļūdu", "atbilde kļūst precīzāka",
               "aprēķins ir garāks", "tā nav vajadzīga"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienā paketē ir 18 zīmuļu. Cik zīmuļu ir 25 paketēs?",
              ["450", "43", "180", "400"], 0),
             ("Cik reižu 960 ir lielāks nekā 40?",
              ["24", "920", "1000", "12"], 0),
             ("Grāmata maksā 12 eiro. Cik grāmatu nopirks par 156 eiro?",
              ["13", "12", "144", "168"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Reizina un dala daudzciparu skaitļus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("23 · 40 = ……", "920"), ("36 · 24 = ……", "864"),
                         ("600 : 20 = ……", "30"), ("288 : 24 = ……", "12")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("15 · 30 = ……", "450"), ("45 · 21 = ……", "945"),
                         ("840 : 40 = ……", "21"), ("546 : 13 = ……", "42")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("18 · 50 = ……", "900"), ("24 · 32 = ……", "768"),
                         ("720 : 30 = ……", "24"), ("816 : 24 = ……", "34")]},
         ]},
        {"sr": "Nosaka trūkstošo reizinātāju vai dalāmo",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("12 · …… = 240", "20"), ("…… : 15 = 6", "90"),
                         ("720 ir …… reižu lielāks nekā 30", "24")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("25 · …… = 750", "30"), ("…… : 12 = 8", "96"),
                         ("480 ir …… reižu lielāks nekā 20", "24")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("14 · …… = 420", "30"), ("…… : 18 = 5", "90"),
                         ("960 ir …… reižu lielāks nekā 40", "24")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar divām darbībām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 6.0,
              "teksts": "Vienā kastē ir 24 olas. Skolai atveda 15 kastes. "
                        "Cik olu atveda? Cik kastu vajadzēs 600 olām?",
              "kriteriji": ["Pieraksts 24 · 15.   (1 p.)",
                            "Atbilde: 360 olas.   (1 p.)",
                            "Pieraksts 600 : 24.   (1 p.)",
                            "Atbilde: 25 kastes.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 6.0,
              "teksts": "Biļete uz teātri maksā 35 eiro. Klase nopirka 12 "
                        "biļetes. Cik jāmaksā? Cik biļešu var nopirkt par "
                        "700 eiro?",
              "kriteriji": ["Pieraksts 35 · 12.   (1 p.)",
                            "Atbilde: 420 eiro.   (1 p.)",
                            "Pieraksts 700 : 35.   (1 p.)",
                            "Atbilde: 20 biļetes.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 6.0,
              "teksts": "Bibliotēkā 864 grāmatas vienādi saliek 24 "
                        "plauktos. Cik grāmatu ir vienā plauktā? Cik "
                        "grāmatu būtu 15 tādos plauktos?",
              "kriteriji": ["Pieraksts 864 : 24.   (1 p.)",
                            "Atbilde: 36 grāmatas.   (1 p.)",
                            "Pieraksts 36 · 15.   (1 p.)",
                            "Atbilde: 540 grāmatas.   (1 p.)"]},
         ]},
        {"sr": "Atrod un izlabo kļūdu aprēķinā",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Atrodi kļūdu", "vieta": 5.0,
              "ievads": "Apskati aprēķinu:   28 · 30 = 84.",
              "jaut": [("Vai aprēķins ir pareizs?", 1),
                       ("Uzraksti pareizo atbildi!", 1),
                       ("Paskaidro, kāda kļūda pieļauta!", 1)],
              "atbildes": ["1) Nē.   (1 p.)", "2) 840.   (1 p.)",
                           "3) Aizmirsta nulle — nav reizināts ar 10. "
                           "  (1 p.)"]},
             {"tips": "jautajumi", "virs": "Aptuvenā un precīzā vērtība",
              "vieta": 5.0,
              "ievads": "Jānis vispirms grib aprēķināt aptuveni:   41 · 19.",
              "jaut": [("Ar kuriem skaitļiem viņš rēķinās aptuveni?", 1),
                       ("Cik liela ir aptuvenā vērtība?", 1),
                       ("Aprēķini precīzo vērtību!", 1)],
              "atbildes": ["1) 40 un 20.   (1 p.)", "2) 800.   (1 p.)",
                           "3) 779.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dalīšana un pārbaude",
              "vieta": 5.0,
              "ievads": "Dalījums ir 32, bet dalītājs — 15.",
              "jaut": [("Aprēķini dalāmo!", 1),
                       ("Pieraksti dalīšanas darbību!", 1),
                       ("Kā pārbaudīt dalījumu?", 1)],
              "atbildes": ["1) 480.   (1 p.)", "2) 480 : 15 = 32.   (1 p.)",
                           "3) Reizinot 32 · 15 = 480.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
