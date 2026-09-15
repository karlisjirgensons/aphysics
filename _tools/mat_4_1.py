# -*- coding: utf-8 -*-
"""Matemātika, 4. klase. 4.1. Kā saskaita un atņem daudzciparu skaitļus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 4. klase, 4.1. temats): skaitļu šķiras,
skaitļi līdz 10 000 un to pieraksts izvērstā formā, salīdzināšana,
saskaitīšana un atņemšana 10 000 apjomā, aptuvenā vērtība un rezultāta
pārbaude, vienādību un nevienādību patiesums, datu lasīšana un attēlošana
stabiņu diagrammā, shematisks zīmējums un situāciju uzdevumi.
"""

PRIEKSMETS = "Matemātika  |  4. klase"
TEMATS = "4.1."
NOSAUKUMS = "Kā saskaita un atņem daudzciparu skaitļus?"

ATGADNE = [
    "Skaitļu šķiras:  vieni, desmiti, simti, tūkstoši, desmittūkstoši   ·   "
    "10 tūkstoši = 1 desmittūkstotis",
    "Izvērstā forma:  3746 = 3000 + 700 + 40 + 6",
    "Aptuvenā vērtība palīdz pārbaudīt rezultātu:  2987 + 1012 ≈ 3000 + "
    "1000 = 4000",
]

FD = {
    "veids": "fd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 4.1. temata beigās. Pārbauda skaitļu "
                "šķiras un skaitļu pierakstu līdz 10 000, salīdzināšanu, "
                "saskaitīšanu un atņemšanu, aptuvenās vērtības noteikšanu, "
                "vienādību patiesumu un datu lasīšanu stabiņu diagrammā.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina skaitļu šķiras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura no tām ir skaitļu šķira?",
              ["tūkstoši", "trijstūri", "leņķi", "grādi"], 0),
             ("Cik tūkstošu veido vienu desmittūkstoti?",
              ["10", "100", "1000", "10000"], 0),
             ("Kurā šķirā ir cipars 7 skaitlī 3728?",
              ["simtu", "tūkstošu", "desmitu", "vienu"], 0),
         ]},
        {"sr": "Nosaka četrciparu skaitļa sastāvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik tūkstošu ir skaitlī 4562?", ["4", "5", "6", "2"], 0),
             ("Cik simtu ir skaitlī 2380?", ["2", "3", "8", "0"], 1),
             ("Cik desmitu ir skaitlī 1450?", ["1", "4", "5", "0"], 2),
         ]},
        {"sr": "Pieraksta skaitli izvērstā formā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā izvērstā formā pieraksta 3746?",
              ["3000 + 700 + 40 + 6", "300 + 70 + 4 + 6",
               "3000 + 70 + 40 + 6", "3 + 7 + 4 + 6"], 0),
             ("Kurš skaitlis ir 5000 + 200 + 30 + 8?",
              ["5238", "5328", "50238", "523"], 0),
             ("Kā izvērstā formā pieraksta 6005?",
              ["6000 + 5", "6000 + 50", "600 + 5", "6 + 0 + 0 + 5"], 0),
         ]},
        {"sr": "Lasa un raksta skaitļus līdz 10 000",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā ar cipariem pieraksta «divi tūkstoši četri simti "
              "piecdesmit»?",
              ["2450", "2045", "24050", "2405"], 0),
             ("Kā izlasa skaitli 7030?",
              ["septiņi tūkstoši trīsdesmit", "septiņi tūkstoši trīs simti",
               "septiņdesmit trīs", "septiņi simti trīsdesmit"], 0),
             ("Kurš skaitlis seko tūlīt pēc 9999?",
              ["9990", "10000", "10010", "99910"], 1),
         ]},
        {"sr": "Salīdzina četrciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  3456 …… 3465?", [">", "<", "=", "+"], 1),
             ("Kurš skaitlis ir lielākais?",
              ["4870", "4807", "4780", "4078"], 0),
             ("Kurš skaitlis ir mazākais?",
              ["2100", "1200", "2010", "1020"], 3),
         ]},
        {"sr": "Saskaita 10 000 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2345 + 1234?", ["3479", "3579", "3679", "4579"], 1),
             ("Cik ir 1678 + 2456?", ["3134", "4034", "4134", "4234"], 2),
             ("Cik ir 3750 + 2250?", ["5000", "5900", "6000", "6100"], 2),
         ]},
        {"sr": "Atņem 10 000 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 5678 − 2345?", ["3233", "3333", "3433", "4333"], 1),
             ("Cik ir 4000 − 1650?", ["2250", "2350", "2450", "3350"], 1),
             ("Cik ir 7231 − 4568?", ["2563", "2663", "2763", "3663"], 1),
         ]},
        {"sr": "Nosaka summas un starpības aptuveno vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aptuveni cik ir 2987 + 1012?",
              ["ap 3000", "ap 4000", "ap 5000", "ap 40000"], 1),
             ("Aptuveni cik ir 5980 − 2010?",
              ["ap 2000", "ap 3000", "ap 4000", "ap 8000"], 2),
             ("Kāpēc noder aptuvenā vērtība?",
              ["var pārbaudīt, vai rezultāts ir ticams",
               "tā vienmēr ir precīza", "tā aizstāj aprēķinu",
               "tā ir ātrāka par kalkulatoru"], 0),
         ]},
        {"sr": "Nosaka, vai vienādība vai nevienādība ir patiesa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura vienādība ir patiesa?",
              ["1500 + 2500 = 4000", "1500 + 2500 = 3000",
               "1500 + 2500 = 4500", "1500 + 2500 = 5000"], 0),
             ("Nevienādība 3200 − 1200 > 1500 ir …",
              ["patiesa", "aplama", "nezināma", "nav nevienādība"], 0),
             ("Kura zīme jāliek:  2500 + 2500 …… 4900?",
              [">", "<", "=", "+"], 0),
         ]},
        {"sr": "Salīdzina summas un starpības, neaprēķinot precīzi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura summa ir lielāka:  2400 + 1300  vai  2400 + 1500?",
              ["otrā", "pirmā", "vienādas", "nevar zināt"], 0),
             ("Kura starpība ir lielāka:  5000 − 1200  vai  5000 − 2200?",
              ["pirmā", "otrā", "vienādas", "nevar zināt"], 0),
             ("Kā mainās summa, ja vienu saskaitāmo palielina?",
              ["palielinās", "samazinās", "nemainās", "kļūst par starpību"],
              0),
         ]},
        {"sr": "Lasa datus stabiņu diagrammā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Diagrammā viens stabiņš rāda 1500, otrs 2500. Cik kopā?",
              ["3000", "3500", "4000", "4500"], 2),
             ("Diagrammā stabiņi: 1200, 1800, 900. Kurš ir vislielākais?",
              ["1800", "1200", "900", "visi vienādi"], 0),
             ("Ko diagrammā rāda stabiņa augstums?",
              ["datu vērtību", "datu nosaukumu", "krāsu", "gadu"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumu ar daudzciparu skaitļiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pilsētā 4500 iedzīvotāju, ciematā par 1200 mazāk. Cik "
              "ciematā?",
              ["3300", "3400", "5700", "2300"], 0),
             ("Bibliotēkā 3250 grāmatas, atveda vēl 1750. Cik ir kopā?",
              ["4000", "4500", "5000", "5500"], 2),
             ("Kontā bija 2800 €, iztērēja 950 €. Cik palika?",
              ["1750 €", "1850 €", "1950 €", "3750 €"], 1),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 4.1. temata noslēgumā. "
                "Pārbauda skaitļu šķiras un pierakstu līdz 10 000, "
                "salīdzināšanu, saskaitīšanu un atņemšanu, aptuvenās "
                "vērtības noteikšanu, datu attēlošanu diagrammā un situāciju "
                "uzdevumu risināšanu ar shematisku zīmējumu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti un zīmē tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina skaitļu šķiras un skaitļa sastāvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurā šķirā ir cipars 5 skaitlī 5284?",
              ["tūkstošu", "simtu", "desmitu", "vienu"], 0),
             ("Cik simtu ir skaitlī 3620?", ["3", "6", "2", "0"], 1),
             ("Cik tūkstošu veido desmittūkstoti?",
              ["10", "100", "1000", "10000"], 0),
         ]},
        {"sr": "Pieraksta skaitli izvērstā formā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir 4000 + 300 + 20 + 7?",
              ["4327", "4372", "40327", "437"], 0),
             ("Kā izvērstā formā pieraksta 5083?",
              ["5000 + 80 + 3", "5000 + 800 + 3", "500 + 83",
               "5 + 0 + 8 + 3"], 0),
             ("Kā izlasa 6400?",
              ["seši tūkstoši četri simti", "sešdesmit četri",
               "seši simti četrdesmit", "seši tūkstoši četrdesmit"], 0),
         ]},
        {"sr": "Salīdzina četrciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  4581 …… 4518?", [">", "<", "=", "−"], 0),
             ("Kurš skaitlis ir lielākais?",
              ["3900", "3090", "3009", "3990"], 3),
             ("Kurš skaitlis ir mazākais?",
              ["5100", "1500", "5010", "1050"], 3),
         ]},
        {"sr": "Saskaita un atņem 10 000 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3456 + 2345?", ["5701", "5801", "5811", "6801"], 1),
             ("Cik ir 6000 − 2350?", ["3550", "3650", "3750", "4650"], 1),
             ("Cik ir 4278 + 1345?", ["5523", "5613", "5623", "5723"], 2),
         ]},
        {"sr": "Nosaka aptuveno vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aptuveni cik ir 3980 + 2015?",
              ["ap 5000", "ap 6000", "ap 7000", "ap 60000"], 1),
             ("Aptuveni cik ir 7950 − 1980?",
              ["ap 5000", "ap 6000", "ap 7000", "ap 9000"], 1),
             ("Kāpēc noder aptuvenā vērtība?",
              ["var pārbaudīt rezultāta ticamību", "tā ir precīza",
               "tā aizstāj aprēķinu", "tā nav vajadzīga"], 0),
         ]},
        {"sr": "Lasa datus diagrammā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Stabiņi: 2500 un 1500. Par cik pirmais lielāks?",
              ["500", "1000", "1500", "4000"], 1),
             ("Stabiņi: 1200, 2400, 1800. Kurš ir vismazākais?",
              ["1200", "1800", "2400", "visi vienādi"], 0),
             ("Ko rāda stabiņa augstums?",
              ["datu vērtību", "nosaukumu", "krāsu", "datumu"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita un atņem daudzciparu skaitļus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini rakstveidā, ja vajag! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("2456 + 1378 = ……", "3834"),
                         ("5000 − 2345 = ……", "2655"),
                         ("3627 + 2485 = ……", "6112"),
                         ("8134 − 4567 = ……", "3567")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini rakstveidā, ja vajag! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("3572 + 1649 = ……", "5221"),
                         ("6000 − 1875 = ……", "4125"),
                         ("2789 + 3456 = ……", "6245"),
                         ("7215 − 3648 = ……", "3567")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Rēķini rakstveidā, ja vajag! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("4185 + 2736 = ……", "6921"),
                         ("7000 − 3425 = ……", "3575"),
                         ("1968 + 2547 = ……", "4515"),
                         ("9302 − 5678 = ……", "3624")]},
         ]},
        {"sr": "Pieraksta skaitli izvērstā formā un salīdzina",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Pieraksti un salīdzini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("3746 = 3000 + …… + 40 + 6", "700"),
                         ("5000 + 200 + 8 = ……", "5208"),
                         ("4381  ……  4318  (ieraksti zīmi)", ">")]},
             {"tips": "parveide", "virs": "Pieraksti un salīdzini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2905 = 2000 + …… + 5", "900"),
                         ("6000 + 40 + 3 = ……", "6043"),
                         ("2789  ……  2798  (ieraksti zīmi)", "<")]},
             {"tips": "parveide", "virs": "Pieraksti un salīdzini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("8264 = 8000 + 200 + …… + 4", "60"),
                         ("3000 + 500 + 70 = ……", "3570"),
                         ("5040  ……  5400  (ieraksti zīmi)", "<")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar shematisku zīmējumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par iedzīvotājiem",
              "vieta": 6.5,
              "ievads": "Pilsētā ir 4500 iedzīvotāju, ciematā — par 1750 "
                        "mazāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Aprēķini, cik iedzīvotāju ir ciematā!", 1),
                       ("Aprēķini, cik iedzīvotāju ir abās vietās kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Ciemata sloksnīte par 1750 īsāka.   (1 p.)",
                           "2) 4500 − 1750 = 2750   (1 p.)",
                           "3) 4500 + 2750 = 7250   (1 p.)",
                           "4) Atbilde: ciematā 2750; kopā 7250 "
                           "iedzīvotāji.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 6.5,
              "ievads": "Bibliotēkā ir 3250 grāmatas, arhīvā — par 1480 "
                        "vairāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Aprēķini, cik grāmatu ir arhīvā!", 1),
                       ("Aprēķini, cik grāmatu ir abās vietās kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Arhīva sloksnīte par 1480 garāka.   (1 p.)",
                           "2) 3250 + 1480 = 4730   (1 p.)",
                           "3) 3250 + 4730 = 7980   (1 p.)",
                           "4) Atbilde: arhīvā 4730; kopā 7980 grāmatas.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par naudu", "vieta": 6.5,
              "ievads": "Skolas kontā bija 5200 €. Iztērēja 1850 €, pēc tam "
                        "saņēma 900 €.",
              "jaut": [("Uzzīmē shēmu situācijai!", 1),
                       ("Aprēķini, cik naudas palika pēc izdevumiem!", 1),
                       ("Aprēķini, cik naudas ir tagad!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Shēmā parādīts izdevums un ieņēmums.   (1 p.)",
                           "2) 5200 − 1850 = 3350 (€)   (1 p.)",
                           "3) 3350 + 900 = 4250 (€)   (1 p.)",
                           "4) Atbilde: kontā ir 4250 €.   (1 p.)"]},
         ]},
        {"sr": "Attēlo datus stabiņu diagrammā un novērtē rezultātu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Dati par apmeklētājiem",
              "vieta": 5.5,
              "ievads": "Muzeju apmeklēja: janvārī 1200, februārī 1800, "
                        "martā 2400 cilvēki.",
              "jaut": [("Uzzīmē stabiņu diagrammu!", 1),
                       ("Aprēķini kopējo apmeklētāju skaitu!", 1),
                       ("Novērtē aptuveni, cik apmeklētāju bija vidēji "
                        "mēnesī!", 1)],
              "atbildes": ["1) Trīs stabiņi 1200, 1800 un 2400.   (1 p.)",
                           "2) 1200 + 1800 + 2400 = 5400   (1 p.)",
                           "3) 5400 : 3 = 1800 apmeklētāji.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dati par pārdošanu", "vieta": 5.5,
              "ievads": "Pārdeva: pirmdien 2500, otrdien 1500, trešdien 2000 "
                        "biļetes.",
              "jaut": [("Uzzīmē stabiņu diagrammu!", 1),
                       ("Aprēķini kopējo biļešu skaitu!", 1),
                       ("Aprēķini, par cik pirmdien pārdeva vairāk nekā "
                        "otrdien!", 1)],
              "atbildes": ["1) Trīs stabiņi 2500, 1500 un 2000.   (1 p.)",
                           "2) 2500 + 1500 + 2000 = 6000   (1 p.)",
                           "3) 2500 − 1500 = 1000 biļetes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dati par iedzīvotājiem",
              "vieta": 5.5,
              "ievads": "Trijos ciemos dzīvo 1400, 2600 un 2000 iedzīvotāju.",
              "jaut": [("Uzzīmē stabiņu diagrammu!", 1),
                       ("Aprēķini kopējo iedzīvotāju skaitu!", 1),
                       ("Aprēķini, par cik lielākajā ciemā ir vairāk nekā "
                        "mazākajā!", 1)],
              "atbildes": ["1) Trīs stabiņi 1400, 2600 un 2000.   (1 p.)",
                           "2) 1400 + 2600 + 2000 = 6000   (1 p.)",
                           "3) 2600 − 1400 = 1200 iedzīvotāji.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
