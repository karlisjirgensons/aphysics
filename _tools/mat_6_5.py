# -*- coding: utf-8 -*-
"""Matemātika, 6. klase. 6.5. Kā sadzīves situācijās izmanto procentus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 6. klase, 6.5. temats): biežāk lietotās
vienādības (50 % = {1|2}; 25 % = {1|4}; 20 % = {1|5}; 10 % = {1|10}), viena
skaitļa noteikšana kā otra skaitļa procenti, procentu aprēķināšana no
skaitļa, veselā noteikšana pēc procentu skaitliskās vērtības un procentu
lietošana praktiskos kontekstos — atlaidēs, cenu izmaiņās un datu
salīdzināšanā.
"""

PRIEKSMETS = "Matemātika  |  6. klase"
TEMATS = "6.5."
NOSAUKUMS = "Kā sadzīves situācijās izmanto procentus?"

ATGADNE = [
    "Noder no galvas:   50 % = {1|2}   ·   25 % = {1|4}   ·   75 % = {3|4} "
    "  ·   20 % = {1|5}   ·   10 % = {1|10}",
    "a kā b procenti:   {a|b} paplašina vai saīsina līdz simtdaļām   ·   "
    "piemēram   {12|50} = {24|100} = 24 %",
    "Procenti no skaitļa:   30 % no 80 = 80 : 100 · 30 = 24   ·   veselais: "
    "ja 30 % ir 24, tad veselais ir 24 : 30 · 100 = 80.",
]

FD = {
    "veids": "fd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 6.5. temata beigās. Pārbauda procentu "
                "un daļu saistību, viena skaitļa izteikšanu kā otra "
                "procentus, procentu aprēķināšanu no skaitļa, veselā "
                "noteikšanu un procentu lietošanu sadzīves situācijās.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina biežāk lietotās procentu un daļu vienādības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā parasto daļu pieraksta 50 %?",
              ["{1|2}", "{1|5}", "{1|4}", "{5|10}"], 0),
             ("Kā parasto daļu pieraksta 20 %?",
              ["{1|5}", "{1|2}", "{1|4}", "{2|10}"], 0),
             ("Cik procentu ir {3|4}?", ["75 %", "34 %", "43 %", "25 %"], 0),
         ]},
        {"sr": "Pieraksta procentus kā decimāldaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā decimāldaļu pieraksta 45 %?",
              ["0,45", "4,5", "0,045", "45,0"], 0),
             ("Cik procentu ir 0,08?", ["8 %", "80 %", "0,8 %", "800 %"], 0),
             ("Cik procentu ir 1,2?", ["120 %", "12 %", "1,2 %", "20 %"], 0),
         ]},
        {"sr": "Izsaka vienu skaitli kā otra procentus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik procentu no 50 ir 12?", ["24 %", "12 %", "38 %", "60 %"], 0),
             ("Cik procentu no 20 ir 5?", ["25 %", "5 %", "20 %", "15 %"], 0),
             ("Kā skaitli izsaka kā otra procentus?",
              ["daļu paplašina līdz simtdaļām", "skaitļus saskaita",
               "skaitļus atņem", "skaitli reizina ar 10"], 0),
         ]},
        {"sr": "Aprēķina procentus no skaitļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 30 % no 80?", ["24", "30", "240", "50"], 0),
             ("Cik ir 15 % no 200?", ["30", "15", "300", "185"], 0),
             ("Cik ir 4 % no 50?", ["2", "4", "20", "46"], 0),
         ]},
        {"sr": "Nosaka veselo pēc procentu vērtības",
         "stunda": TEMATS,
         "jautajumi": [
             ("30 % no skaitļa ir 24. Kāds ir skaitlis?",
              ["80", "54", "720", "8"], 0),
             ("40 % no skaitļa ir 18. Kāds ir skaitlis?",
              ["45", "58", "720", "7,2"], 0),
             ("Kā atrod veselo?",
              ["vērtību dala ar procentiem un reizina ar 100",
               "vērtību reizina ar procentiem", "vērtību dala ar 100",
               "vērtībai pieskaita 100"], 0),
         ]},
        {"sr": "Aprēķina atlaidi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Prece maksā 40 eiro, atlaide 25 %. Cik liela ir atlaide?",
              ["10 eiro", "15 eiro", "25 eiro", "30 eiro"], 0),
             ("Prece maksā 60 eiro, atlaide 10 %. Cik maksā prece?",
              ["54 eiro", "50 eiro", "6 eiro", "66 eiro"], 0),
             ("Cik procentu no cenas samaksā, ja atlaide ir 20 %?",
              ["80 %", "20 %", "120 %", "100 %"], 0),
         ]},
        {"sr": "Aprēķina cenas pieaugumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cena 50 eiro pieaug par 10 %. Kāda ir jaunā cena?",
              ["55 eiro", "45 eiro", "60 eiro", "5 eiro"], 0),
             ("Cena 200 eiro pieaug par 25 %. Par cik eiro tā pieaug?",
              ["50 eiro", "25 eiro", "250 eiro", "150 eiro"], 0),
             ("Cik procentu no sākotnējās cenas ir jaunā cena, ja tā "
              "pieaug par 15 %?", ["115 %", "15 %", "85 %", "100 %"], 0),
         ]},
        {"sr": "Salīdzina daļas un procentus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura vērtība ir lielākā?",
              ["60 %", "{1|2}", "0,55", "{1|4}"], 0),
             ("Kura vērtība ir mazākā?",
              ["{1|5}", "25 %", "0,3", "{1|2}"], 0),
             ("Kas ir lielāks: 40 % no 50 vai {1|2} no 50?",
              ["{1|2} no 50", "40 % no 50", "abi vienādi",
               "nevar salīdzināt"], 0),
         ]},
        {"sr": "Lieto procentus datu salīdzināšanā",
         "stunda": TEMATS,
         "jautajumi": [
             ("A klasē no 25 skolēniem 5 spēlē šahu. Cik procentu tie ir?",
              ["20 %", "5 %", "25 %", "80 %"], 0),
             ("B klasē no 20 skolēniem 5 spēlē šahu. Cik procentu tie ir?",
              ["25 %", "5 %", "20 %", "75 %"], 0),
             ("Kāpēc daļas pārvērš procentos?",
              ["lai varētu salīdzināt dažādus veselos",
               "lai skaitļi būtu lielāki", "lai nebūtu jārēķina",
               "lai zustu daļsvītra"], 0),
         ]},
        {"sr": "Aprēķina daļu pēc procentiem sadzīvē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Algai 800 eiro nodoklis ir 20 %. Cik liels ir nodoklis?",
              ["160 eiro", "80 eiro", "200 eiro", "640 eiro"], 0),
             ("Klasē 60 % no 25 skolēniem ir meitenes. Cik ir meiteņu?",
              ["15", "10", "6", "60"], 0),
             ("Krājumā 2000 eiro; gadā pieaug par 3 %. Par cik tas pieaug?",
              ["60 eiro", "6 eiro", "600 eiro", "300 eiro"], 0),
         ]},
        {"sr": "Spriež par procentu maiņu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cena vispirms pieaug par 10 %, tad sarūk par 10 %. Kāda tā "
              "ir?", ["mazāka nekā sākumā", "tāda pati", "lielāka nekā "
                       "sākumā", "divreiz mazāka"], 0),
             ("Ko nozīmē 100 % no skaitļa?",
              ["visu skaitli", "pusi skaitļa", "divreiz vairāk", "nulli"], 0),
             ("Ko nozīmē 200 % no skaitļa?",
              ["divreiz vairāk", "visu skaitli", "pusi skaitļa",
               "divreiz mazāk"], 0),
         ]},
        {"sr": "Pārbauda rezultāta atbilstību situācijai",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai atlaide var būt lielāka nekā sākotnējā cena?",
              ["nē", "jā", "vienmēr", "tikai veikalā"], 0),
             ("Prece maksāja 20 eiro; pēc 50 % atlaides tā maksā 15 eiro. "
              "Vai tas ir pareizi?", ["nē, jābūt 10 eiro", "jā",
                                      "nē, jābūt 5 eiro",
                                      "nevar noteikt"], 0),
             ("Kā pārbauda procentu aprēķinu?",
              ["novērtē, vai rezultāts ir ticams", "pārraksta uzdevumu",
               "maina mērvienības", "saskaita procentus"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 6.5. temata noslēgumā. "
                "Pārbauda procentu un daļu saistību, viena skaitļa "
                "izteikšanu kā otra procentus, procentu un veselā "
                "aprēķināšanu un procentu lietošanu atlaidēs, cenu "
                "izmaiņās un datu salīdzināšanā.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Saista procentus ar daļām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā parasto daļu pieraksta 25 %?",
              ["{1|4}", "{1|2}", "{1|5}", "{2|5}"], 0),
             ("Cik procentu ir {1|10}?", ["10 %", "1 %", "100 %", "110 %"], 0),
             ("Kā decimāldaļu pieraksta 8 %?",
              ["0,08", "0,8", "8,0", "0,008"], 0),
         ]},
        {"sr": "Izsaka skaitli kā otra procentus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik procentu no 40 ir 10?", ["25 %", "10 %", "40 %", "30 %"], 0),
             ("Cik procentu no 200 ir 30?",
              ["15 %", "30 %", "20 %", "170 %"], 0),
             ("Kā skaitli izsaka kā otra procentus?",
              ["daļu paplašina līdz simtdaļām", "skaitļus saskaita",
               "skaitļus atņem", "skaitli reizina ar 10"], 0),
         ]},
        {"sr": "Aprēķina procentus no skaitļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 35 % no 400?", ["140", "35", "1400", "365"], 0),
             ("Cik ir 6 % no 50?", ["3", "6", "30", "44"], 0),
             ("Cik ir 120 % no 50?", ["60", "50", "12", "70"], 0),
         ]},
        {"sr": "Nosaka veselo",
         "stunda": TEMATS,
         "jautajumi": [
             ("20 % no skaitļa ir 16. Kāds ir skaitlis?",
              ["80", "36", "320", "3,2"], 0),
             ("75 % no skaitļa ir 30. Kāds ir skaitlis?",
              ["40", "105", "22,5", "45"], 0),
             ("Kā atrod veselo?",
              ["vērtību dala ar procentiem un reizina ar 100",
               "vērtību reizina ar procentiem", "vērtību dala ar 100",
               "vērtībai pieskaita 100"], 0),
         ]},
        {"sr": "Aprēķina atlaidi un cenas pieaugumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Prece maksā 80 eiro, atlaide 15 %. Cik liela ir atlaide?",
              ["12 eiro", "15 eiro", "68 eiro", "20 eiro"], 0),
             ("Cena 120 eiro pieaug par 10 %. Kāda ir jaunā cena?",
              ["132 eiro", "130 eiro", "108 eiro", "12 eiro"], 0),
             ("Cik procentu no cenas samaksā, ja atlaide ir 30 %?",
              ["70 %", "30 %", "130 %", "100 %"], 0),
         ]},
        {"sr": "Salīdzina datus ar procentiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("A klasē no 20 skolēniem 4 kavē, B klasē no 25 skolēniem 5. "
              "Kur daļa lielāka?", ["abās vienāda", "A klasē", "B klasē",
                                    "nevar salīdzināt"], 0),
             ("Kura vērtība ir lielākā?",
              ["70 %", "{2|3}", "0,65", "{1|2}"], 0),
             ("Kāpēc daļas pārvērš procentos?",
              ["lai varētu salīdzināt dažādus veselos",
               "lai skaitļi būtu lielāki", "lai nebūtu jārēķina",
               "lai zustu daļsvītra"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pārveido daļas, decimāldaļas un procentus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("25 % = …… (parastā daļa)", "{1|4}"),
                         ("{1|5} = …… %", "20"),
                         ("0,35 = …… %", "35"),
                         ("12 no 50 ir …… %", "24")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("50 % = …… (parastā daļa)", "{1|2}"),
                         ("{3|4} = …… %", "75"),
                         ("0,06 = …… %", "6"),
                         ("9 no 30 ir …… %", "30")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("10 % = …… (parastā daļa)", "{1|10}"),
                         ("{2|5} = …… %", "40"),
                         ("1,5 = …… %", "150"),
                         ("18 no 40 ir …… %", "45")]},
         ]},
        {"sr": "Aprēķina procentus no skaitļa un veselo",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("20 % no 350 = ……", "70"),
                         ("5 % no 80 = ……", "4"),
                         ("40 % no skaitļa ir 20; skaitlis ir ……", "50")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("30 % no 250 = ……", "75"),
                         ("8 % no 50 = ……", "4"),
                         ("25 % no skaitļa ir 15; skaitlis ir ……", "60")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("15 % no 400 = ……", "60"),
                         ("2 % no 150 = ……", "3"),
                         ("10 % no skaitļa ir 7; skaitlis ir ……", "70")]},
         ]},
        {"sr": "Risina praktisku uzdevumu ar procentiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Atlaide veikalā", "vieta": 5.6,
              "teksts": "Velosipēds maksā 240 eiro; tam ir 15 % atlaide.   "
                        "a) Cik liela ir atlaide eiro?   b) Cik maksā "
                        "velosipēds ar atlaidi?   c) Cik procentu no "
                        "sākotnējās cenas pircējs samaksā?   d) Cik eiro "
                        "vajadzētu, lai nopirktu divus šādus velosipēdus "
                        "ar atlaidi?",
              "kriteriji": ["a) 240 : 100 · 15 = 36 eiro.   (1 p.)",
                            "b) 240 − 36 = 204 eiro.   (1 p.)",
                            "c) 100 % − 15 % = 85 %.   (1 p.)",
                            "d) 204 · 2 = 408 eiro.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Cenas pieaugums", "vieta": 5.6,
              "teksts": "Biļete maksāja 8 eiro; cena pieauga par 25 %.   "
                        "a) Par cik eiro cena pieauga?   b) Kāda ir jaunā "
                        "cena?   c) Cik procentu no vecās cenas ir jaunā "
                        "cena?   d) Cik maksās 5 biļetes par jauno cenu?",
              "kriteriji": ["a) 8 : 100 · 25 = 2 eiro.   (1 p.)",
                            "b) 8 + 2 = 10 eiro.   (1 p.)",
                            "c) 125 %.   (1 p.)",
                            "d) 10 · 5 = 50 eiro.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Procenti klasē", "vieta": 5.6,
              "teksts": "Skolā ir 500 skolēnu; 12 % no viņiem apmeklē kora "
                        "nodarbības, bet 45 skolēni — sporta pulciņu.   "
                        "a) Cik skolēnu dzied korī?   b) Cik procentu "
                        "skolēnu apmeklē sporta pulciņu?   c) Kurš "
                        "pulciņš ir apmeklētāks?   d) Cik procentu skolēnu "
                        "neapmeklē nevienu no tiem?",
              "kriteriji": ["a) 500 : 100 · 12 = 60 skolēni.   (1 p.)",
                            "b) 45 : 500 = 9 %.   (1 p.)",
                            "c) Koris — 60 > 45.   (1 p.)",
                            "d) 100 % − 12 % − 9 % = 79 %.   (1 p.)"]},
         ]},
        {"sr": "Skaidro un pārbauda procentu aprēķinus",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Divas atlaides", "vieta": 4.6,
              "ievads": "Prece maksā 100 eiro. Vienā veikalā tai ir 20 % "
                        "atlaide, otrā — vispirms 10 %, tad vēl 10 % no "
                        "jaunās cenas.",
              "jaut": [("Cik maksā prece pirmajā veikalā?", 1),
                       ("Cik maksā prece otrajā veikalā?", 1),
                       ("Kurā veikalā izdevīgāk? Pamato!", 1)],
              "atbildes": ["1) 100 − 20 = 80 eiro.   (1 p.)",
                           "2) 90, tad 90 − 9 = 81 eiro.   (1 p.)",
                           "3) Pirmajā — otrā atlaide rēķināta no mazākas "
                           "cenas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Skaitlis kā procenti",
              "vieta": 4.6,
              "ievads": "Klasē ir 25 skolēni; 15 no viņiem ir meitenes.",
              "jaut": [("Kādu daļu veido meitenes?", 1),
                       ("Cik procentu tie ir?", 1),
                       ("Cik procentu ir zēnu?", 1)],
              "atbildes": ["1) {15|25} = {3|5}.   (1 p.)",
                           "2) {3|5} = {60|100} = 60 %.   (1 p.)",
                           "3) 100 % − 60 % = 40 %.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Pārbaudi rezultātu", "vieta": 4.6,
              "ievads": "Skolēns apgalvo: «30 % no 60 ir 30.»",
              "jaut": [("Vai apgalvojums ir pareizs?", 1),
                       ("Aprēķini pareizo vērtību!", 1),
                       ("Paskaidro, kur ir kļūda!", 1)],
              "atbildes": ["1) Nē, tas ir aplams.   (1 p.)",
                           "2) 60 : 100 · 30 = 18.   (1 p.)",
                           "3) 30 % nav puse; puse būtu 50 %.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
