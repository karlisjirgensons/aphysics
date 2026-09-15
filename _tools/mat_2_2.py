# -*- coding: utf-8 -*-
"""Matemātika, 2. klase. 2.2. Kā nosaka dažādus garumus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 2. klase, 2.2. temats): mērīšana mm, cm,
dm un m, lielāku mērvienību izteikšana mazākās, nogriežņa zīmēšana cm un mm,
garumu salīdzināšana un aprēķini, nogriežņa puse un ceturtdaļa, mērījumu
apkopošana tabulā.
"""

PRIEKSMETS = "Matemātika  |  2. klase"
TEMATS = "2.2."
NOSAUKUMS = "Kā nosaka dažādus garumus?"

ATGADNE = [
    "1 cm = 10 mm   ·   1 dm = 10 cm = 100 mm   ·   1 m = 10 dm = 100 cm",
    "Jo mazāka mērvienība, jo lielāks skaitlis tajā pašā garumā:  "
    "2 cm = 20 mm",
    "Puse no nogriežņa — dala ar 2   ·   ceturtdaļa — dala ar 4",
]

FD = {
    "veids": "fd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 2.2. temata beigās. Pārbauda mērvienības "
                "mm, cm, dm un m, to pārveidošanu, mērīšanu un nogriežņa "
                "zīmēšanu, garumu salīdzināšanu un aprēķinus, nogriežņa "
                "puses un ceturtdaļas noteikšanu un mērījumu pierakstu "
                "tabulā.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina garuma mērvienības un to apzīmējumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā saīsināti raksta milimetru?", ["m", "mm", "cm", "ml"], 1),
             ("Kura mērvienība ir vismazākā?", ["mm", "cm", "dm", "m"], 0),
             ("Kura mērvienība ir vislielākā?", ["mm", "cm", "dm", "m"], 3),
         ]},
        {"sr": "Pārveido centimetrus milimetros",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik mm ir 1 cm?", ["1", "10", "100", "1000"], 1),
             ("Cik mm ir 5 cm?", ["5", "15", "50", "500"], 2),
             ("Cik cm ir 70 mm?", ["7", "17", "70", "700"], 0),
         ]},
        {"sr": "Pārveido decimetrus un metrus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik cm ir 3 dm?", ["3", "13", "30", "300"], 2),
             ("Cik dm ir 1 m?", ["10", "100", "1000", "1"], 0),
             ("Cik cm ir 2 m?", ["20", "102", "200", "2000"], 2),
         ]},
        {"sr": "Pieraksta mērījumu ar mērvienību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpēc mērījumam vienmēr raksta mērvienību?",
              ["bez tās nezina, cik liels ir garums", "lai būtu garāks pieraksts",
               "lai skaistāk izskatītos", "tā nav vajadzīga"], 0),
             ("Nogrieznis ir 8 cm un vēl 5 mm. Kā to pieraksta?",
              ["8 cm 5 mm", "85 cm", "8 mm 5 cm", "13 cm"], 0),
             ("Kurš pieraksts ir nepilnīgs?",
              ["garums 12", "garums 12 cm", "garums 12 mm", "garums 12 m"], 0),
         ]},
        {"sr": "Salīdzina garumus dažādās mērvienībās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  3 cm …… 25 mm?", [">", "<", "=", "+"], 0),
             ("Kura zīme jāliek:  1 dm …… 10 cm?", [">", "<", "=", "−"], 2),
             ("Kurš garums ir vislielākais?",
              ["9 cm", "50 mm", "1 dm", "8 cm"], 2),
         ]},
        {"sr": "Nosaka, par cik viens garums lielāks nekā otrs",
         "stunda": TEMATS,
         "jautajumi": [
             ("Par cik 12 cm ir garāks nekā 7 cm?",
              ["4 cm", "5 cm", "6 cm", "19 cm"], 1),
             ("Par cik 1 dm ir garāks nekā 6 cm?",
              ["2 cm", "3 cm", "4 cm", "16 cm"], 2),
             ("Par cik 45 mm ir garāks nekā 3 cm?",
              ["5 mm", "10 mm", "15 mm", "42 mm"], 2),
         ]},
        {"sr": "Veic aprēķinus ar garumiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 24 cm + 16 cm?", ["30 cm", "38 cm", "40 cm", "44 cm"],
              2),
             ("Cik ir 1 m − 40 cm?", ["40 cm", "50 cm", "60 cm", "96 cm"], 2),
             ("Divas lentes: 35 cm un 45 cm. Cik gara ir abu lente kopā?",
              ["70 cm", "80 cm", "90 cm", "10 cm"], 1),
         ]},
        {"sr": "Nosaka nogriežņa pusi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Nogrieznis ir 10 cm. Cik gara ir tā puse?",
              ["2 cm", "5 cm", "10 cm", "20 cm"], 1),
             ("Nogrieznis ir 8 cm. Cik gara ir tā puse?",
              ["2 cm", "3 cm", "4 cm", "16 cm"], 2),
             ("Kā aprēķina nogriežņa pusi?",
              ["garumu dala ar 2", "garumu reizina ar 2", "garumu dala ar 4",
               "garumam pieskaita 2"], 0),
         ]},
        {"sr": "Nosaka nogriežņa ceturtdaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Nogrieznis ir 12 cm. Cik gara ir tā ceturtdaļa?",
              ["2 cm", "3 cm", "4 cm", "6 cm"], 1),
             ("Nogrieznis ir 20 cm. Cik gara ir tā ceturtdaļa?",
              ["4 cm", "5 cm", "10 cm", "80 cm"], 1),
             ("Kā aprēķina nogriežņa ceturtdaļu?",
              ["garumu dala ar 4", "garumu dala ar 2", "garumu reizina ar 4",
               "garumam pieskaita 4"], 0),
         ]},
        {"sr": "Mēra attālumus, kurus nevar novietot blakus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā salīdzināt divu istabu garumu?",
              ["abas izmērīt un salīdzināt skaitļus", "tās salikt kopā",
               "tās pasvērt", "tās nokrāsot"], 0),
             ("Ar ko mēra garu attālumu, piemēram, klases garumu?",
              ["ar mērlenti", "ar īsu lineālu", "ar pulksteni",
               "ar svariem"], 0),
             ("Istaba A ir 4 m, istaba B ir 380 cm. Kura ir garāka?",
              ["istaba A", "istaba B", "abas vienādas", "nevar zināt"], 0),
         ]},
        {"sr": "Zīmē nogriezni, kas dots cm un mm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik mm garš ir nogrieznis 4 cm 5 mm?",
              ["9 mm", "45 mm", "54 mm", "450 mm"], 1),
             ("Nogrieznis ir 63 mm. Kā to pieraksta cm un mm?",
              ["6 cm 3 mm", "3 cm 6 mm", "63 cm", "6 mm 3 cm"], 0),
             ("Kur uz lineāla beidzas 2 cm 5 mm garš nogrieznis, ja sākums "
              "ir pie 0?",
              ["starp 2 un 3", "starp 5 un 6", "pie 25", "pie 7"], 0),
         ]},
        {"sr": "Apkopo mērījumus tabulā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpēc mērījumus pieraksta tabulā?",
              ["lai tos būtu viegli salīdzināt", "lai aizmirstu",
               "lai tabula būtu krāsaina", "lai nevajadzētu mērīt"], 0),
             ("Tabulā: zīmulis 14 cm, pildspalva 13 cm. Kurš ir garāks?",
              ["zīmulis", "pildspalva", "abi vienādi", "nevar zināt"], 0),
             ("Tabulā: lente A 25 cm, lente B 40 cm. Par cik B ir garāka?",
              ["10 cm", "15 cm", "20 cm", "65 cm"], 1),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 2.2. temata noslēgumā. "
                "Pārbauda mērvienību mm, cm, dm un m pārveidošanu, "
                "nogriežņa zīmēšanu un mērīšanu, garumu salīdzināšanu un "
                "aprēķinus, nogriežņa puses un ceturtdaļas noteikšanu un "
                "mērījumu pierakstu tabulā.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Zīmē ar lineālu un risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina mērvienības un to lielumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura mērvienība ir vismazākā?", ["mm", "cm", "dm", "m"], 0),
             ("Kā saīsināti raksta milimetru?", ["m", "mm", "ml", "mt"], 1),
             ("Cik mm ir 1 cm?", ["1", "10", "100", "1000"], 1),
         ]},
        {"sr": "Pārveido mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik mm ir 4 cm?", ["4", "14", "40", "400"], 2),
             ("Cik cm ir 6 dm?", ["6", "16", "60", "600"], 2),
             ("Cik cm ir 1 m?", ["10", "100", "1000", "1"], 1),
         ]},
        {"sr": "Salīdzina garumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  5 cm …… 45 mm?", [">", "<", "=", "+"], 0),
             ("Kura zīme jāliek:  2 dm …… 20 cm?", [">", "<", "=", "−"], 2),
             ("Kurš garums ir vislielākais?",
              ["7 cm", "80 mm", "1 dm", "6 cm"], 2),
         ]},
        {"sr": "Veic aprēķinus ar garumiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 35 cm + 25 cm?", ["50 cm", "55 cm", "60 cm", "65 cm"],
              2),
             ("Cik ir 1 m − 30 cm?", ["30 cm", "60 cm", "70 cm", "97 cm"], 2),
             ("Par cik 15 cm ir garāks nekā 9 cm?",
              ["5 cm", "6 cm", "7 cm", "24 cm"], 1),
         ]},
        {"sr": "Nosaka nogriežņa pusi un ceturtdaļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Nogrieznis ir 14 cm. Cik gara ir tā puse?",
              ["6 cm", "7 cm", "8 cm", "28 cm"], 1),
             ("Nogrieznis ir 16 cm. Cik gara ir tā ceturtdaļa?",
              ["2 cm", "4 cm", "8 cm", "64 cm"], 1),
             ("Kā aprēķina ceturtdaļu?",
              ["dala ar 4", "dala ar 2", "reizina ar 4", "pieskaita 4"], 0),
         ]},
        {"sr": "Lasa mērījumu tabulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: A 12 cm, B 18 cm. Par cik B ir garāks?",
              ["4 cm", "5 cm", "6 cm", "30 cm"], 2),
             ("Tabulā: zīmulis 15 cm, krītiņš 6 cm. Cik kopā?",
              ["9 cm", "20 cm", "21 cm", "22 cm"], 2),
             ("Kāpēc mērījumus pieraksta tabulā?",
              ["lai tos būtu viegli salīdzināt", "lai aizņemtu vietu",
               "lai nevajadzētu mērīt", "lai būtu krāsaini"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pārveido garuma mērvienības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Izsaki mazākās mērvienībās",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("3 cm = …… mm", "30"), ("5 dm = …… cm", "50"),
                         ("1 m = …… cm", "100"), ("8 cm 4 mm = …… mm", "84")]},
             {"tips": "parveide", "virs": "Izsaki mazākās mērvienībās",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("7 cm = …… mm", "70"), ("4 dm = …… cm", "40"),
                         ("2 m = …… cm", "200"), ("6 cm 5 mm = …… mm", "65")]},
             {"tips": "parveide", "virs": "Izsaki mazākās mērvienībās",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("9 cm = …… mm", "90"), ("8 dm = …… cm", "80"),
                         ("1 m = …… dm", "10"), ("3 cm 7 mm = …… mm", "37")]},
         ]},
        {"sr": "Salīdzina garumus dažādās mērvienībās",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp garumiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("4 cm  ……  35 mm", ">"), ("1 dm  ……  10 cm", "="),
                         ("60 cm  ……  1 m", "<")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp garumiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("2 cm  ……  25 mm", "<"), ("3 dm  ……  30 cm", "="),
                         ("90 cm  ……  1 m", "<")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp garumiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("8 cm  ……  75 mm", ">"), ("5 dm  ……  50 cm", "="),
                         ("1 m  ……  120 cm", "<")]},
         ]},
        {"sr": "Zīmē nogriežņus un nosaka to pusi",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Zīmē un mēri", "vieta": 6.5,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē nogriezni, kas ir 8 cm garš!", 1),
                       ("Atzīmē tā pusi un uzraksti puses garumu!", 1),
                       ("Uzzīmē nogriezni, kas ir 5 cm 5 mm garš!", 1),
                       ("Uzraksti otrā nogriežņa garumu milimetros!", 1)],
              "atbildes": ["1) Uzzīmēts 8 cm nogrieznis.   (1 p.)",
                           "2) Atzīmēta puse; pierakstīts 4 cm.   (1 p.)",
                           "3) Uzzīmēts 5 cm 5 mm nogrieznis.   (1 p.)",
                           "4) Pierakstīts 55 mm.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē un mēri", "vieta": 6.5,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē nogriezni, kas ir 12 cm garš!", 1),
                       ("Atzīmē tā pusi un uzraksti puses garumu!", 1),
                       ("Uzzīmē nogriezni, kas ir 3 cm 5 mm garš!", 1),
                       ("Uzraksti otrā nogriežņa garumu milimetros!", 1)],
              "atbildes": ["1) Uzzīmēts 12 cm nogrieznis.   (1 p.)",
                           "2) Atzīmēta puse; pierakstīts 6 cm.   (1 p.)",
                           "3) Uzzīmēts 3 cm 5 mm nogrieznis.   (1 p.)",
                           "4) Pierakstīts 35 mm.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē un mēri", "vieta": 6.5,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē nogriezni, kas ir 10 cm garš!", 1),
                       ("Atzīmē tā ceturtdaļu un uzraksti tās garumu!", 1),
                       ("Uzzīmē nogriezni, kas ir 4 cm 5 mm garš!", 1),
                       ("Uzraksti otrā nogriežņa garumu milimetros!", 1)],
              "atbildes": ["1) Uzzīmēts 10 cm nogrieznis.   (1 p.)",
                           "2) Atzīmēta ceturtdaļa; pierakstīts 2 cm 5 mm.   "
                           "(1 p.)",
                           "3) Uzzīmēts 4 cm 5 mm nogrieznis.   (1 p.)",
                           "4) Pierakstīts 45 mm.   (1 p.)"]},
         ]},
        {"sr": "Risina uzdevumu par garumiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par lentēm", "vieta": 5.5,
              "ievads": "Viena lente ir 45 cm gara, otra — 35 cm.",
              "jaut": [("Aprēķini abu lenšu kopgarumu!", 1),
                       ("Aprēķini, par cik pirmā ir garāka!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 45 cm + 35 cm = 80 cm   (1 p.)",
                           "2) 45 cm − 35 cm = 10 cm   (1 p.)",
                           "3) Atbilde: kopā 80 cm; pirmā par 10 cm "
                           "garāka.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par auklu", "vieta": 5.5,
              "ievads": "Aukla ir 1 m gara. No tās nogrieza 40 cm.",
              "jaut": [("Aprēķini, cik cm auklas palika!", 1),
                       ("Aprēķini nogrieztā gabala pusi!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 100 cm − 40 cm = 60 cm   (1 p.)",
                           "2) 40 cm : 2 = 20 cm   (1 p.)",
                           "3) Atbilde: palika 60 cm; puse no nogrieztā ir "
                           "20 cm.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par dēli", "vieta": 5.5,
              "ievads": "Dēlis ir 90 cm garš. To sazāģēja divos gabalos; "
                        "viens ir 55 cm.",
              "jaut": [("Aprēķini otra gabala garumu!", 1),
                       ("Aprēķini, par cik viens gabals ir garāks!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 90 cm − 55 cm = 35 cm   (1 p.)",
                           "2) 55 cm − 35 cm = 20 cm   (1 p.)",
                           "3) Atbilde: otrs gabals 35 cm; starpība 20 cm.   "
                           "(1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
