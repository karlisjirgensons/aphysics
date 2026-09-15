# -*- coding: utf-8 -*-
"""Matemātika, 3. klase. 3.4. Ko nozīmē daļa no veselā?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 3. klase, 3.4. temats): veselais un tā
daļas, parastā daļa, skaitītājs un saucējs, īsta daļa, daļas atlikšana uz
skaitļu taisnes, daļas noteikšana zīmējumā un veselā noteikšana pēc daļas,
desmitdaļu un simtdaļu pieraksts decimāldaļās, sakarības 1 mm = {1|10} cm un
1 cents = {1|100} eiro.

Daļas raksta ar {skaitītājs|saucējs}, tāpēc ekrānā un Word failā tās ir
vertikālas (rules_pd.txt).
"""

PRIEKSMETS = "Matemātika  |  3. klase"
TEMATS = "3.4."
NOSAUKUMS = "Ko nozīmē daļa no veselā?"

ATGADNE = [
    "Parastā daļa:  saucējs rāda, cik vienādās daļās veselais sadalīts; "
    "skaitītājs — cik daļu ņemts.",
    "Īsta daļa ir lielāka nekā 0 un mazāka nekā 1, piemēram, {3|4}.",
    "{1|10} = 0,1   ·   {3|100} = 0,03   ·   1 mm = {1|10} cm   ·   "
    "1 cents = {1|100} eiro",
]

FD = {
    "veids": "fd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 3.4. temata beigās. Pārbauda parastās "
                "daļas pierakstu un lasīšanu, skaitītāja un saucēja nozīmi, "
                "īstas daļas jēdzienu, daļas noteikšanu zīmējumā un no "
                "skaitļa, veselā noteikšanu pēc daļas un desmitdaļu "
                "pierakstu decimāldaļās.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro, kā rodas parastā daļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā iegūst parasto daļu?",
              ["veselo sadala vienādās daļās", "veselo saskaita",
               "veselo reizina", "veselo noapaļo"], 0),
             ("Kurš skaitlis ir daļskaitlis?",
              ["{3|4}", "5", "12", "0"], 0),
             ("Ko nozīmē daļsvītra?",
              ["dalīšanu vienādās daļās", "saskaitīšanu", "atņemšanu",
               "salīdzināšanu"], 0),
         ]},
        {"sr": "Zina, ko rāda saucējs",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda daļas saucējs?",
              ["cik vienādās daļās veselais sadalīts", "cik daļu ņemts",
               "cik veselo", "cik daļsvītru"], 0),
             ("Daļā {2|5} saucējs ir …", ["2", "5", "25", "7"], 1),
             ("Kurā daļā veselais sadalīts 8 daļās?",
              ["{3|8}", "{8|3}", "{1|3}", "{8|1}"], 0),
         ]},
        {"sr": "Zina, ko rāda skaitītājs",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda daļas skaitītājs?",
              ["cik daļu ņemts", "cik vienādās daļās sadalīts", "cik veselo",
               "cik daļsvītru"], 0),
             ("Daļā {3|7} skaitītājs ir …", ["3", "7", "37", "10"], 0),
             ("Kurā daļā ņemtas 5 daļas?",
              ["{5|6}", "{6|5}", "{1|5}", "{5|5}"], 0),
         ]},
        {"sr": "Lasa un pieraksta parastās daļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta «trīs ceturtdaļas»?",
              ["{3|4}", "{4|3}", "{1|4}", "{3|1}"], 0),
             ("Kā izlasa {2|3}?",
              ["divas trešdaļas", "trīs otrdaļas", "divi trīs",
               "divas desmitdaļas"], 0),
             ("Kā pieraksta «viena desmitdaļa»?",
              ["{1|10}", "{10|1}", "{1|100}", "0,10"], 0),
         ]},
        {"sr": "Atpazīst īstu daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura daļa ir īsta daļa?",
              ["{3|5}", "{5|3}", "{7|7}", "{9|4}"], 0),
             ("Starp kuriem skaitļiem uz skaitļu taisnes atrodas īsta daļa?",
              ["starp 0 un 1", "starp 1 un 2", "aiz 2", "pirms 0"], 0),
             ("Kāda ir īsta daļa?",
              ["skaitītājs mazāks nekā saucējs",
               "skaitītājs lielāks nekā saucējs", "skaitītājs vienāds ar "
               "saucēju", "saucējs ir 0"], 0),
         ]},
        {"sr": "Nosaka daļu zīmējumā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kvadrāts sadalīts 4 vienādās daļās, 1 iekrāsota. Kāda daļa "
              "iekrāsota?",
              ["{1|4}", "{4|1}", "{1|3}", "{3|4}"], 0),
             ("Riņķis sadalīts 8 daļās, 3 iekrāsotas. Kāda daļa iekrāsota?",
              ["{3|8}", "{8|3}", "{1|8}", "{5|8}"], 0),
             ("Josla sadalīta 5 daļās, 2 iekrāsotas. Kāda daļa NAV "
              "iekrāsota?",
              ["{3|5}", "{2|5}", "{5|3}", "{1|5}"], 0),
         ]},
        {"sr": "Nosaka daļu no skaitļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {1|4} no 20?", ["4", "5", "16", "80"], 1),
             ("Cik ir {1|3} no 18?", ["3", "6", "15", "54"], 1),
             ("Cik ir {1|5} no 40?", ["5", "8", "35", "200"], 1),
         ]},
        {"sr": "Nosaka vairākas daļas no skaitļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {2|5} no 20?", ["4", "8", "10", "40"], 1),
             ("Cik ir {3|4} no 16?", ["4", "8", "12", "48"], 2),
             ("Cik ir {2|3} no 12?", ["4", "6", "8", "24"], 2),
         ]},
        {"sr": "Nosaka veselo, ja dota daļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("{1|4} no skaitļa ir 5. Cik liels ir viss skaitlis?",
              ["9", "15", "20", "25"], 2),
             ("{1|3} no skaitļa ir 6. Cik liels ir viss skaitlis?",
              ["9", "12", "18", "24"], 2),
             ("{1|5} no skaitļa ir 4. Cik liels ir viss skaitlis?",
              ["9", "16", "20", "24"], 2),
         ]},
        {"sr": "Atliek daļu uz skaitļu taisnes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur uz skaitļu taisnes atrodas {1|2}?",
              ["starp 0 un 1", "starp 1 un 2", "pie 2", "pirms 0"], 0),
             ("Nogriezni no 0 līdz 1 sadala 4 daļās. Kur ir {3|4}?",
              ["trešajā iedaļā no 0", "pirmajā iedaļā", "aiz 1", "pie 0"], 0),
             ("Kura daļa ir vistuvāk skaitlim 1?",
              ["{7|8}", "{1|8}", "{1|2}", "{3|8}"], 0),
         ]},
        {"sr": "Pieraksta desmitdaļas un simtdaļas ar decimāldaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā decimāldaļā pieraksta {1|10}?",
              ["0,1", "1,0", "0,01", "10,0"], 0),
             ("Kā decimāldaļā pieraksta {3|100}?",
              ["0,03", "0,3", "3,0", "0,003"], 0),
             ("Kā izlasa 0,7?",
              ["septiņas desmitdaļas", "septiņas simtdaļas", "septiņi veseli",
               "septiņdesmit"], 0),
         ]},
        {"sr": "Lieto daļas mērvienībās un naudā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāda daļa no centimetra ir 1 mm?",
              ["{1|10}", "{1|100}", "{1|2}", "{10|1}"], 0),
             ("Kāda daļa no eiro ir 1 cents?",
              ["{1|100}", "{1|10}", "{1|2}", "{100|1}"], 0),
             ("Cik centu ir {1|2} eiro?", ["10", "25", "50", "100"], 2),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 3.4. temata noslēgumā. "
                "Pārbauda parastās daļas pierakstu, skaitītāja un saucēja "
                "nozīmi, daļas noteikšanu zīmējumā un no skaitļa, veselā "
                "noteikšanu pēc daļas, daļas atlikšanu uz skaitļu taisnes un "
                "decimāldaļu pierakstu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Zīmē ar lineālu un risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina daļas pieraksta nozīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda saucējs?",
              ["cik vienādās daļās veselais sadalīts", "cik daļu ņemts",
               "cik veselo", "cik daļsvītru"], 0),
             ("Ko rāda skaitītājs?",
              ["cik daļu ņemts", "cik vienādās daļās sadalīts", "cik veselo",
               "cik nulles"], 0),
             ("Daļā {3|8} saucējs ir …", ["3", "8", "38", "11"], 1),
         ]},
        {"sr": "Lasa un pieraksta daļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta «divas piektdaļas»?",
              ["{2|5}", "{5|2}", "{1|5}", "{2|2}"], 0),
             ("Kā izlasa {3|4}?",
              ["trīs ceturtdaļas", "četras trešdaļas", "trīs četri",
               "trīs desmitdaļas"], 0),
             ("Kura daļa ir īsta daļa?", ["{2|7}", "{7|2}", "{5|5}",
                                          "{9|4}"], 0),
         ]},
        {"sr": "Nosaka daļu zīmējumā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Figūra sadalīta 6 daļās, 1 iekrāsota. Kāda daļa iekrāsota?",
              ["{1|6}", "{6|1}", "{1|5}", "{5|6}"], 0),
             ("Josla sadalīta 4 daļās, 3 iekrāsotas. Kāda daļa iekrāsota?",
              ["{3|4}", "{4|3}", "{1|4}", "{1|3}"], 0),
             ("Riņķis sadalīts 10 daļās, 7 iekrāsotas. Kāda daļa NAV "
              "iekrāsota?",
              ["{3|10}", "{7|10}", "{10|3}", "{1|10}"], 0),
         ]},
        {"sr": "Nosaka daļu no skaitļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {1|3} no 21?", ["3", "7", "18", "63"], 1),
             ("Cik ir {1|4} no 32?", ["4", "8", "28", "128"], 1),
             ("Cik ir {2|5} no 25?", ["5", "10", "15", "50"], 1),
         ]},
        {"sr": "Nosaka veselo pēc daļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("{1|5} no skaitļa ir 6. Cik liels ir skaitlis?",
              ["11", "24", "30", "36"], 2),
             ("{1|4} no skaitļa ir 7. Cik liels ir skaitlis?",
              ["11", "21", "28", "35"], 2),
             ("{1|2} no skaitļa ir 9. Cik liels ir skaitlis?",
              ["11", "18", "19", "27"], 1),
         ]},
        {"sr": "Pieraksta decimāldaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā decimāldaļā pieraksta {1|10}?",
              ["0,1", "1,0", "0,01", "10"], 0),
             ("Kā decimāldaļā pieraksta {7|100}?",
              ["0,07", "0,7", "7,0", "0,007"], 0),
             ("Kāda daļa no eiro ir 1 cents?",
              ["{1|100}", "{1|10}", "{1|2}", "{100|1}"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Nosaka daļu no skaitļa un veselo pēc daļas",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|4} no 24 ir ……", "6"),
                         ("{1|3} no 27 ir ……", "9"),
                         ("{2|5} no 30 ir ……", "12"),
                         ("{1|5} no skaitļa ir 8; skaitlis ir ……", "40")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|3} no 24 ir ……", "8"),
                         ("{1|4} no 36 ir ……", "9"),
                         ("{3|4} no 20 ir ……", "15"),
                         ("{1|4} no skaitļa ir 6; skaitlis ir ……", "24")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|5} no 35 ir ……", "7"),
                         ("{1|2} no 46 ir ……", "23"),
                         ("{2|3} no 18 ir ……", "12"),
                         ("{1|3} no skaitļa ir 5; skaitlis ir ……", "15")]},
         ]},
        {"sr": "Pieraksta daļas ar vārdiem un decimāldaļās",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Pieraksti daļu",
              "note": "Ieraksti pareizo pierakstu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("«Trīs piektdaļas» ar cipariem:  ……", "{3|5}"),
                         ("{1|10} decimāldaļā:  ……", "0,1"),
                         ("{9|100} decimāldaļā:  ……", "0,09")]},
             {"tips": "parveide", "virs": "Pieraksti daļu",
              "note": "Ieraksti pareizo pierakstu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("«Divas septītdaļas» ar cipariem:  ……", "{2|7}"),
                         ("{3|10} decimāldaļā:  ……", "0,3"),
                         ("{5|100} decimāldaļā:  ……", "0,05")]},
             {"tips": "parveide", "virs": "Pieraksti daļu",
              "note": "Ieraksti pareizo pierakstu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("«Piecas sestdaļas» ar cipariem:  ……", "{5|6}"),
                         ("{7|10} decimāldaļā:  ……", "0,7"),
                         ("{1|100} decimāldaļā:  ……", "0,01")]},
         ]},
        {"sr": "Attēlo daļu zīmējumā un uz skaitļu taisnes",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Daļas attēlošana", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri un sadali to 4 vienādās daļās!",
                        1),
                       ("Iekrāso {3|4} no tā!", 1),
                       ("Uzzīmē skaitļu taisni no 0 līdz 1 un atzīmē {1|2}!",
                        1),
                       ("Uzraksti, kāda daļa palika neiekrāsota!", 1)],
              "atbildes": ["1) Taisnstūris sadalīts 4 vienādās daļās.   "
                           "(1 p.)",
                           "2) Iekrāsotas 3 no 4 daļām.   (1 p.)",
                           "3) Skaitļu taisne ar atzīmi vidū.   (1 p.)",
                           "4) Atbilde: {1|4}.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Daļas attēlošana", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri un sadali to 5 vienādās daļās!",
                        1),
                       ("Iekrāso {2|5} no tā!", 1),
                       ("Uzzīmē skaitļu taisni no 0 līdz 1 un atzīmē {1|4}!",
                        1),
                       ("Uzraksti, kāda daļa palika neiekrāsota!", 1)],
              "atbildes": ["1) Taisnstūris sadalīts 5 vienādās daļās.   "
                           "(1 p.)",
                           "2) Iekrāsotas 2 no 5 daļām.   (1 p.)",
                           "3) Skaitļu taisne ar atzīmi pirmajā ceturtdaļā.   "
                           "(1 p.)",
                           "4) Atbilde: {3|5}.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Daļas attēlošana", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri un sadali to 6 vienādās daļās!",
                        1),
                       ("Iekrāso {5|6} no tā!", 1),
                       ("Uzzīmē skaitļu taisni no 0 līdz 1 un atzīmē {3|4}!",
                        1),
                       ("Uzraksti, kāda daļa palika neiekrāsota!", 1)],
              "atbildes": ["1) Taisnstūris sadalīts 6 vienādās daļās.   "
                           "(1 p.)",
                           "2) Iekrāsotas 5 no 6 daļām.   (1 p.)",
                           "3) Skaitļu taisne ar atzīmi trešajā "
                           "ceturtdaļā.   (1 p.)",
                           "4) Atbilde: {1|6}.   (1 p.)"]},
         ]},
        {"sr": "Risina uzdevumu par daļu no veselā",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par skolēniem",
              "vieta": 5.5,
              "ievads": "Klasē ir 24 skolēni. Trešdaļa no viņiem spēlē "
                        "futbolu.",
              "jaut": [("Pieraksti, kā aprēķināt futbolistu skaitu!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik skolēnu nespēlē futbolu!", 1)],
              "atbildes": ["1) 24 : 3   (1 p.)", "2) 24 : 3 = 8   (1 p.)",
                           "3) 24 − 8 = 16 skolēni.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 5.5,
              "ievads": "Plauktā ir 30 grāmatas. Piektdaļa no tām ir pasakas.",
              "jaut": [("Pieraksti, kā aprēķināt pasaku skaitu!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik grāmatu nav pasakas!", 1)],
              "atbildes": ["1) 30 : 5   (1 p.)", "2) 30 : 5 = 6   (1 p.)",
                           "3) 30 − 6 = 24 grāmatas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par naudu", "vieta": 5.5,
              "ievads": "Kārlim bija 40 €. Ceturtdaļu no naudas viņš "
                        "iztērēja.",
              "jaut": [("Pieraksti, kā aprēķināt iztērēto summu!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik naudas palika!", 1)],
              "atbildes": ["1) 40 : 4   (1 p.)", "2) 40 : 4 = 10 (€)   "
                           "(1 p.)",
                           "3) 40 − 10 = 30 €.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
