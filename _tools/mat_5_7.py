# -*- coding: utf-8 -*-
"""Matemātika, 5. klase. 5.7. Kā lieto decimāldaļas un procentus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 5. klase, 5.7. temats): parastās daļas ar
saucēju 10; 100; 1000 kā decimāldaļas, decimālais sastāvs, decimāldaļa uz
skaitļu taisnes, paplašināšana, salīdzināšana, saskaitīšana un atņemšana,
procents kā simtdaļa un tā pieraksts ar parasto daļu un decimāldaļu, procentu
aprēķināšana no veselā un veselā noteikšana, sektoru diagramma un
aritmētiskais vidējais.
"""

PRIEKSMETS = "Matemātika  |  5. klase"
TEMATS = "5.7."
NOSAUKUMS = "Kā lieto decimāldaļas un procentus?"

ATGADNE = [
    "Decimāldaļa:   0,7 = {7|10}   ·   0,23 = {23|100}   ·   decimālais "
    "sastāvs:   3,12 = 3 + 0,1 + 0,02   ·   paplašina:   0,5 = 0,50",
    "Procents ir viena simtdaļa:   1 % = {1|100} = 0,01   ·   25 % = "
    "{25|100} = 0,25   ·   0,4 = 40 %",
    "20 % no 60 = 60 : 100 · 20 = 12   ·   ja 20 % ir 12, tad veselais ir "
    "12 : 20 · 100 = 60   ·   aritmētiskais vidējais = summa : skaits",
]

FD = {
    "veids": "fd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 5.7. temata beigās. Pārbauda "
                "decimāldaļas pierakstu un decimālo sastāvu, paplašināšanu, "
                "salīdzināšanu, saskaitīšanu un atņemšanu, procentu "
                "pierakstu un aprēķināšanu, sektoru diagrammas lasīšanu un "
                "aritmētisko vidējo.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Pieraksta parasto daļu kā decimāldaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā decimāldaļu pieraksta {7|10}?",
              ["0,7", "7,0", "0,07", "0,71"], 0),
             ("Kā decimāldaļu pieraksta {23|100}?",
              ["0,23", "2,3", "0,023", "23,0"], 0),
             ("Kā decimāldaļu pieraksta {1|2}?",
              ["0,5", "0,2", "1,2", "0,12"], 0),
         ]},
        {"sr": "Pieraksta decimāldaļu kā parasto daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā parasto daļu pieraksta 0,9?",
              ["{9|10}", "{9|100}", "{1|9}", "{10|9}"], 0),
             ("Kā parasto daļu pieraksta 0,25?",
              ["{1|4}", "{1|25}", "{25|10}", "{4|1}"], 0),
             ("Ko atdala komats?",
              ["vienus no desmitdaļām", "desmitus", "simtus",
               "procentus"], 0),
         ]},
        {"sr": "Skaidro decimāldaļas decimālo sastāvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā summu pieraksta 3,12?",
              ["3 + 0,1 + 0,02", "3 + 1 + 2", "3 + 0,12 + 0,1",
               "0,3 + 0,1 + 0,2"], 0),
             ("Cik desmitdaļu ir skaitlī 4,56?",
              ["5", "6", "4", "56"], 0),
             ("Cik simtdaļu ir skaitlī 0,08?",
              ["8", "0", "80", "800"], 0),
         ]},
        {"sr": "Attēlo decimāldaļu uz skaitļu taisnes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Starp kuriem veseliem skaitļiem atrodas 2,7?",
              ["starp 2 un 3", "starp 1 un 2", "starp 7 un 8",
               "starp 27 un 28"], 0),
             ("Kurš skaitlis uz skaitļu taisnes ir tuvāk 1?",
              ["0,9", "0,5", "0,1", "0,4"], 0),
             ("Cik vienādās daļās sadala vienu vienību, lai atliktu "
              "desmitdaļas?", ["10", "100", "2", "5"], 0),
         ]},
        {"sr": "Paplašina decimāldaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā skaitli 0,5 pieraksta ar simtdaļām?",
              ["0,50", "0,05", "5,00", "0,005"], 0),
             ("Vai 0,3 un 0,30 ir vienādi skaitļi?",
              ["jā, tie ir vienādi", "nē, 0,30 ir lielāks",
               "nē, 0,3 ir lielāks", "to nevar noteikt"], 0),
             ("Kāpēc decimāldaļas paplašina?",
              ["lai varētu salīdzināt", "lai skaitlis augtu",
               "lai skaitlis sarūktu", "lai zustu komats"], 0),
         ]},
        {"sr": "Salīdzina decimāldaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir lielākais?",
              ["0,71", "0,7", "0,17", "0,07"], 0),
             ("Kurš skaitlis ir mazākais?",
              ["0,09", "0,9", "0,19", "0,91"], 0),
             ("Kā salīdzina decimāldaļas?",
              ["salīdzina pa šķirām, sākot ar veseliem",
               "salīdzina ciparu skaitu aiz komata",
               "salīdzina pēdējo ciparu", "salīdzina komata vietu"], 0),
         ]},
        {"sr": "Saskaita un atņem decimāldaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2,4 + 1,3?", ["3,7", "3,8", "2,7", "37"], 0),
             ("Cik ir 5,6 − 2,8?", ["2,8", "3,2", "2,2", "3,8"], 0),
             ("Kā decimāldaļas saskaita rakstos?",
              ["komatu raksta zem komata", "komatu izlaiž",
               "ciparus raksta pēc kārtas", "vispirms noapaļo"], 0),
         ]},
        {"sr": "Skaidro, kas ir procents",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir viens procents?",
              ["viena simtdaļa", "viena desmitdaļa", "viena tūkstošdaļa",
               "viena puse"], 0),
             ("Cik procentu ir viss veselais?",
              ["100 %", "10 %", "1 %", "1000 %"], 0),
             ("Cik procentu ir puse?", ["50 %", "5 %", "25 %", "20 %"], 0),
         ]},
        {"sr": "Pieraksta procentus kā daļu un decimāldaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā parasto daļu pieraksta 25 %?",
              ["{1|4}", "{1|25}", "{25|10}", "{4|25}"], 0),
             ("Kā decimāldaļu pieraksta 7 %?",
              ["0,07", "0,7", "7,0", "0,007"], 0),
             ("Cik procentu ir 0,4?", ["40 %", "4 %", "0,4 %", "400 %"], 0),
         ]},
        {"sr": "Aprēķina procentus no skaitļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 20 % no 60?", ["12", "30", "80", "6"], 0),
             ("Cik ir 50 % no 48?", ["24", "12", "96", "48"], 0),
             ("Kā aprēķina 20 % no skaitļa?",
              ["skaitli dala ar 100 un reizina ar 20",
               "skaitli reizina ar 20", "skaitli dala ar 20",
               "skaitlim pieskaita 20"], 0),
         ]},
        {"sr": "Nosaka veselo, ja zināma procentu vērtība",
         "stunda": TEMATS,
         "jautajumi": [
             ("25 % no skaitļa ir 15. Kāds ir skaitlis?",
              ["60", "40", "75", "30"], 0),
             ("10 % no skaitļa ir 7. Kāds ir skaitlis?",
              ["70", "17", "0,7", "700"], 0),
             ("Kā atrod veselo, ja zināmi 20 % no tā?",
              ["vērtību dala ar 20 un reizina ar 100",
               "vērtību reizina ar 20", "vērtību dala ar 100",
               "vērtībai pieskaita 100"], 0),
         ]},
        {"sr": "Lasa sektoru diagrammu un aprēķina aritmētisko vidējo",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik procentu kopā veido visi sektoru diagrammas sektori?",
              ["100 %", "50 %", "360 %", "10 %"], 0),
             ("Kāds ir skaitļu 4; 6 un 8 aritmētiskais vidējais?",
              ["6", "18", "8", "4"], 0),
             ("Kā aprēķina aritmētisko vidējo?",
              ["skaitļu summu dala ar skaitļu skaitu",
               "saskaita visus skaitļus", "izvēlas lielāko skaitli",
               "izvēlas vidējo pēc kārtas"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 5.7. temata noslēgumā. "
                "Pārbauda decimāldaļu pierakstu, salīdzināšanu un darbības "
                "ar tām, procentu pierakstu ar daļu un decimāldaļu, "
                "procentu un veselā aprēķināšanu, sektoru diagrammas "
                "lasīšanu un aritmētisko vidējo.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Pieraksta daļu kā decimāldaļu un otrādi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā decimāldaļu pieraksta {3|10}?",
              ["0,3", "3,0", "0,03", "0,31"], 0),
             ("Kā parasto daļu pieraksta 0,75?",
              ["{3|4}", "{1|75}", "{75|10}", "{4|3}"], 0),
             ("Kā summu pieraksta 2,45?",
              ["2 + 0,4 + 0,05", "2 + 4 + 5", "0,2 + 0,4 + 0,5",
               "2 + 0,45 + 0,4"], 0),
         ]},
        {"sr": "Salīdzina decimāldaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir lielākais?",
              ["0,62", "0,6", "0,26", "0,06"], 0),
             ("Kā skaitli 0,8 pieraksta ar simtdaļām?",
              ["0,80", "0,08", "8,00", "0,008"], 0),
             ("Kurš apgalvojums ir patiess?",
              ["0,5 = 0,50", "0,5 < 0,50", "0,5 > 0,50", "0,5 = 0,05"], 0),
         ]},
        {"sr": "Saskaita un atņem decimāldaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3,6 + 2,7?", ["6,3", "5,3", "6,13", "5,13"], 0),
             ("Cik ir 7,2 − 3,5?", ["3,7", "4,7", "3,3", "4,3"], 0),
             ("Cik ir 0,45 + 0,55?", ["1", "0,9", "0,1", "1,1"], 0),
         ]},
        {"sr": "Pieraksta procentus ar daļu un decimāldaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā decimāldaļu pieraksta 35 %?",
              ["0,35", "3,5", "0,035", "35,0"], 0),
             ("Cik procentu ir {1|2}?", ["50 %", "12 %", "20 %", "2 %"], 0),
             ("Cik procentu ir 0,06?", ["6 %", "60 %", "0,6 %", "600 %"], 0),
         ]},
        {"sr": "Aprēķina procentus no skaitļa un veselo",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 30 % no 200?", ["60", "30", "600", "70"], 0),
             ("Cik ir 5 % no 80?", ["4", "16", "40", "8"], 0),
             ("20 % no skaitļa ir 14. Kāds ir skaitlis?",
              ["70", "34", "280", "2,8"], 0),
         ]},
        {"sr": "Lasa diagrammu un aprēķina aritmētisko vidējo",
         "stunda": TEMATS,
         "jautajumi": [
             ("Diagrammā viens sektors ir 40 %, otrs — 35 %. Cik procentu "
              "ir trešajam?", ["25 %", "75 %", "5 %", "15 %"], 0),
             ("Kāds ir skaitļu 5; 7; 9 un 11 aritmētiskais vidējais?",
              ["8", "32", "9", "7"], 0),
             ("Kad datus var attēlot sektoru diagrammā?",
              ["kad daļas kopā veido 100 %", "kad datu ir vairāk nekā 10",
               "kad visi dati ir vienādi", "kad dati ir decimāldaļas"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pārveido daļas, decimāldaļas un procentus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{7|10} = ……", "0,7"),
                         ("0,25 = …… (parastā daļa)", "{1|4}"),
                         ("40 % = …… (decimāldaļa)", "0,4"),
                         ("0,09 = …… %", "9")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{3|100} = ……", "0,03"),
                         ("0,5 = …… (parastā daļa)", "{1|2}"),
                         ("75 % = …… (decimāldaļa)", "0,75"),
                         ("0,6 = …… %", "60")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{9|10} = ……", "0,9"),
                         ("0,2 = …… (parastā daļa)", "{1|5}"),
                         ("12 % = …… (decimāldaļa)", "0,12"),
                         ("0,45 = …… %", "45")]},
         ]},
        {"sr": "Izpilda darbības ar decimāldaļām",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("4,3 + 2,9 = ……", "7,2"),
                         ("8,1 − 3,4 = ……", "4,7"),
                         ("0,35 + 0,65 = ……", "1")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("5,7 + 1,8 = ……", "7,5"),
                         ("9,2 − 4,6 = ……", "4,6"),
                         ("0,28 + 0,72 = ……", "1")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("6,4 + 3,7 = ……", "10,1"),
                         ("7,3 − 2,85 = ……", "4,45"),
                         ("0,4 + 0,06 = ……", "0,46")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar procentiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Procenti sadzīvē", "vieta": 5.6,
              "teksts": "Skolā mācās 400 skolēni; 25 % no viņiem apmeklē "
                        "sporta pulciņu.   a) Cik skolēnu apmeklē "
                        "pulciņu?   b) Cik procentu skolēnu to "
                        "neapmeklē?   c) Cik skolēnu neapmeklē pulciņu?   "
                        "d) Pieraksti 25 % kā parasto daļu!",
              "kriteriji": ["a) 400 : 100 · 25 = 100 skolēni.   (1 p.)",
                            "b) 100 % − 25 % = 75 %.   (1 p.)",
                            "c) 400 − 100 = 300 skolēni.   (1 p.)",
                            "d) 25 % = {25|100} = {1|4}.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Procenti sadzīvē", "vieta": 5.6,
              "teksts": "Jaka maksā 60 eiro; tai piešķirta 20 % atlaide.   "
                        "a) Cik liela ir atlaide eiro?   b) Cik maksā jaka "
                        "ar atlaidi?   c) Cik procentu no sākotnējās cenas "
                        "pircējs samaksā?   d) Pieraksti 20 % kā "
                        "decimāldaļu!",
              "kriteriji": ["a) 60 : 100 · 20 = 12 eiro.   (1 p.)",
                            "b) 60 − 12 = 48 eiro.   (1 p.)",
                            "c) 100 % − 20 % = 80 %.   (1 p.)",
                            "d) 20 % = 0,2.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Procenti sadzīvē", "vieta": 5.6,
              "teksts": "Klasē 30 % skolēnu brauc ar autobusu; tie ir "
                        "9 skolēni.   a) Cik skolēnu ir klasē?   b) Cik "
                        "skolēnu nebrauc ar autobusu?   c) Cik procentu "
                        "skolēnu nebrauc ar autobusu?   d) Pieraksti 30 % "
                        "kā parasto daļu!",
              "kriteriji": ["a) 9 : 30 · 100 = 30 skolēni.   (1 p.)",
                            "b) 30 − 9 = 21 skolēns.   (1 p.)",
                            "c) 100 % − 30 % = 70 %.   (1 p.)",
                            "d) 30 % = {30|100} = {3|10}.   (1 p.)"]},
         ]},
        {"sr": "Lasa diagrammu un raksturo datus",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Sektoru diagramma", "vieta": 4.6,
              "ievads": "Aptaujā par mīļāko sporta veidu 45 % izvēlējās "
                        "futbolu, 30 % — basketbolu, pārējie — volejbolu. "
                        "Kopā aptaujāti 200 skolēni.",
              "jaut": [("Cik procentu izvēlējās volejbolu?", 1),
                       ("Cik skolēnu izvēlējās futbolu?", 1),
                       ("Cik skolēnu izvēlējās volejbolu?", 1)],
              "atbildes": ["1) 100 % − 45 % − 30 % = 25 %.   (1 p.)",
                           "2) 200 : 100 · 45 = 90 skolēni.   (1 p.)",
                           "3) 200 : 100 · 25 = 50 skolēni.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Aritmētiskais vidējais",
              "vieta": 4.6,
              "ievads": "Nedēļā skolēns lasīja 12; 8; 10; 6 un 14 lappuses.",
              "jaut": [("Cik lappuses izlasītas kopā?", 1),
                       ("Cik ir aritmētiskais vidējais?", 1),
                       ("Cik dienās izlasīts vairāk nekā vidēji?", 1)],
              "atbildes": ["1) 12 + 8 + 10 + 6 + 14 = 50 lappuses.   (1 p.)",
                           "2) 50 : 5 = 10 lappuses.   (1 p.)",
                           "3) Divās dienās (12 un 14).   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Procenti un daļas", "vieta": 4.6,
              "ievads": "Klasē ir 25 skolēni; 20 % no viņiem spēlē šahu.",
              "jaut": [("Cik skolēnu spēlē šahu?", 1),
                       ("Pieraksti 20 % kā parasto daļu!", 1),
                       ("Cik procentu skolēnu nespēlē šahu?", 1)],
              "atbildes": ["1) 25 : 100 · 20 = 5 skolēni.   (1 p.)",
                           "2) 20 % = {20|100} = {1|5}.   (1 p.)",
                           "3) 100 % − 20 % = 80 %.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
