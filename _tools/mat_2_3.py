# -*- coding: utf-8 -*-
"""Matemātika, 2. klase. 2.3. Kā saskaita un atņem divciparu skaitļus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 2. klase, 2.3. temats): saskaitīšana un
atņemšana 100 apjomā arī ar pāreju jaunā desmitā, dažādi rēķināšanas
paņēmieni, rezultāta pārbaude, shematisks zīmējums situāciju uzdevumos,
aprēķini ar naudas summām, kas dotas decimāldaļās.
"""

PRIEKSMETS = "Matemātika  |  2. klase"
TEMATS = "2.3."
NOSAUKUMS = "Kā saskaita un atņem divciparu skaitļus?"

ATGADNE = [
    "Saskaitot:  desmitus pie desmitiem, vienus pie vieniem;  "
    "37 + 25 = 30 + 20 + 7 + 5 = 50 + 12 = 62",
    "Atņemot:  52 − 28 = 52 − 20 − 8 = 32 − 8 = 24   ·   pārbaude:  "
    "24 + 28 = 52",
    "Nauda:  1,50 € ir 1 eiro un 50 centi   ·   1 € = 100 centi",
]

FD = {
    "veids": "fd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 2.3. temata beigās. Pārbauda saskaitīšanu "
                "un atņemšanu 100 apjomā ar pāreju jaunā desmitā, "
                "rēķināšanas paņēmienus, rezultāta pārbaudi, nezināmā "
                "locekļa noteikšanu un aprēķinus ar naudas summām.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Saskaita divciparu skaitļus bez pārejas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 34 + 25?", ["49", "59", "69", "84"], 1),
             ("Cik ir 52 + 16?", ["58", "62", "68", "78"], 2),
             ("Cik ir 41 + 37?", ["68", "74", "78", "88"], 2),
         ]},
        {"sr": "Saskaita divciparu skaitļus ar pāreju jaunā desmitā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 37 + 25?", ["52", "62", "63", "72"], 1),
             ("Cik ir 48 + 26?", ["64", "72", "74", "84"], 2),
             ("Cik ir 59 + 18?", ["67", "76", "77", "87"], 2),
         ]},
        {"sr": "Atņem divciparu skaitļus bez aizņemšanās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 68 − 25?", ["33", "43", "45", "53"], 1),
             ("Cik ir 87 − 34?", ["43", "53", "54", "63"], 1),
             ("Cik ir 96 − 52?", ["34", "42", "44", "54"], 2),
         ]},
        {"sr": "Atņem divciparu skaitļus ar aizņemšanos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 52 − 28?", ["14", "24", "26", "34"], 1),
             ("Cik ir 73 − 47?", ["24", "26", "34", "36"], 1),
             ("Cik ir 61 − 39?", ["12", "22", "28", "32"], 1),
         ]},
        {"sr": "Skaidro rēķināšanas paņēmienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("37 + 25 = 30 + 20 + 7 + ……  Kurš skaitlis pietrūkst?",
              ["2", "5", "7", "25"], 1),
             ("Kā ērti saskaitīt 46 + 30?",
              ["desmitus pieskaita desmitiem", "vienus pieskaita desmitiem",
               "skaitļus reizina", "skaitļus salīdzina"], 0),
             ("Kāpēc, atņemot 52 − 28, «jāsasmalcina» viens desmits?",
              ["jo 2 vieni ir mazāk nekā 8", "jo skaitļi ir lieli",
               "jo tā ir noteikums", "jo 52 ir pāra skaitlis"], 0),
         ]},
        {"sr": "Pārbauda rezultātu ar pretējo darbību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pārbaudīt, vai 64 − 27 = 37?",
              ["saskaitot 37 + 27", "saskaitot 64 + 27", "atņemot 64 − 37",
               "reizinot 37 · 27"], 0),
             ("Kā pārbaudīt, vai 28 + 35 = 63?",
              ["atņemot 63 − 35", "saskaitot 63 + 35", "atņemot 35 − 28",
               "reizinot 28 · 35"], 0),
             ("Skolēns ieguva 45 + 38 = 73. Vai tas ir pareizi?",
              ["nē, pareizi ir 83", "jā", "nē, pareizi ir 63",
               "nevar pārbaudīt"], 0),
         ]},
        {"sr": "Nosaka nezināmo skaitli vienādībā 100 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("45 + …… = 72  Kurš skaitlis jāieraksta?",
              ["17", "27", "37", "117"], 1),
             ("…… + 26 = 61  Kurš skaitlis jāieraksta?",
              ["25", "35", "45", "87"], 1),
             ("83 − …… = 47  Kurš skaitlis jāieraksta?",
              ["26", "36", "44", "130"], 1),
         ]},
        {"sr": "Risina situāciju uzdevumu ar saskaitīšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Skolā bija 38 zēni un 46 meitenes. Cik bērnu kopā?",
              ["74", "82", "84", "86"], 2),
             ("Plauktā 27 grāmatas, pielika vēl 35. Cik ir kopā?",
              ["52", "62", "63", "72"], 1),
             ("Pirmajā dienā 29 km, otrajā 24 km. Cik kopā?",
              ["43", "53", "54", "63"], 1),
         ]},
        {"sr": "Risina situāciju uzdevumu ar atņemšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Bija 75 eiro, iztērēja 28 eiro. Cik palika?",
              ["37", "43", "47", "53"], 2),
             ("Bibliotēkā 92 grāmatas, izsniedza 45. Cik palika?",
              ["37", "47", "53", "57"], 1),
             ("Autobusā brauca 54 cilvēki, izkāpa 27. Cik palika?",
              ["23", "27", "33", "37"], 1),
         ]},
        {"sr": "Veido shematisku zīmējumu situācijai",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpēc pirms rēķināšanas der uzzīmēt shēmu?",
              ["lai saprastu, ko ar ko salīdzina", "lai darbs būtu garāks",
               "lai nevajadzētu rēķināt", "lai izmantotu krāsas"], 0),
             ("Shēmā viena sloksnīte ir 40, otra par 15 garāka. Cik ir otra?",
              ["25", "45", "55", "65"], 2),
             ("Shēmā abas sloksnītes kopā ir 80, viena ir 35. Cik ir otra?",
              ["35", "45", "55", "115"], 1),
         ]},
        {"sr": "Veic aprēķinus ar naudas summām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik centu ir 1,50 €?", ["15", "105", "150", "1500"], 2),
             ("Prece maksā 2,30 €. Cik tas ir centos?",
              ["23", "203", "230", "2300"], 2),
             ("Bija 5 €, iztērēja 2,50 €. Cik palika?",
              ["1,50 €", "2,50 €", "3,50 €", "7,50 €"], 1),
         ]},
        {"sr": "Novērtē, vai rezultāts ir ticams",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aptuveni cik ir 48 + 31?", ["ap 50", "ap 60", "ap 80",
                                           "ap 100"], 2),
             ("Divi skaitļi ir mazāki nekā 50. Vai to summa var būt 120?",
              ["nē", "jā", "vienmēr", "tikai ar iekavām"], 0),
             ("Skolēns aprēķināja 62 − 19 = 81. Kāpēc tas nav ticami?",
              ["atņemot rezultāts nevar būt lielāks", "jo 62 ir pāra",
               "jo 19 ir nepāra", "tas ir ticami"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 2.3. temata noslēgumā. "
                "Pārbauda saskaitīšanu un atņemšanu 100 apjomā ar pāreju "
                "jaunā desmitā, nezināmā locekļa noteikšanu, rezultāta "
                "pārbaudi, situāciju uzdevuma risināšanu ar shematisku "
                "zīmējumu un aprēķinus ar naudu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Saskaita 100 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 46 + 27?", ["63", "73", "74", "83"], 1),
             ("Cik ir 38 + 45?", ["73", "82", "83", "93"], 2),
             ("Cik ir 57 + 29?", ["76", "86", "87", "96"], 1),
         ]},
        {"sr": "Atņem 100 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 64 − 38?", ["24", "26", "34", "36"], 1),
             ("Cik ir 81 − 46?", ["25", "35", "45", "47"], 1),
             ("Cik ir 70 − 23?", ["37", "47", "53", "57"], 1),
         ]},
        {"sr": "Nosaka nezināmo skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("38 + …… = 65", ["17", "27", "37", "103"], 1),
             ("…… + 44 = 72", ["18", "28", "38", "116"], 1),
             ("90 − …… = 54", ["26", "36", "44", "144"], 1),
         ]},
        {"sr": "Pārbauda rezultātu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pārbaudīt, vai 72 − 35 = 37?",
              ["saskaitot 37 + 35", "saskaitot 72 + 35", "atņemot 72 − 37",
               "reizinot 37 · 35"], 0),
             ("Skolēns ieguva 56 + 27 = 73. Vai tas ir pareizi?",
              ["nē, pareizi ir 83", "jā", "nē, pareizi ir 93",
               "nevar pārbaudīt"], 0),
             ("Kura atbilde nav ticama:  45 − 18 = ?",
              ["63", "27", "25", "30"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Bija 63 eiro, iztērēja 27. Cik palika?",
              ["34", "36", "44", "46"], 1),
             ("Vienā kastē 28, otrā 47 āboli. Cik kopā?",
              ["65", "73", "75", "85"], 2),
             ("Klasē 24 skolēni, ekskursijā brauca 19. Cik palika skolā?",
              ["3", "5", "7", "43"], 1),
         ]},
        {"sr": "Veic aprēķinus ar naudu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik centu ir 2,50 €?", ["25", "205", "250", "2500"], 2),
             ("Bija 10 €, iztērēja 4,50 €. Cik palika?",
              ["4,50 €", "5,50 €", "6,50 €", "14,50 €"], 1),
             ("Cik eiro un centi ir 175 centi?",
              ["1,75 €", "17,5 €", "175 €", "0,75 €"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita un atņem 100 apjomā",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("36 + 28 = ……", "64"), ("52 − 27 = ……", "25"),
                         ("45 + 39 = ……", "84"), ("83 − 46 = ……", "37")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("47 + 26 = ……", "73"), ("64 − 38 = ……", "26"),
                         ("58 + 35 = ……", "93"), ("91 − 47 = ……", "44")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("29 + 34 = ……", "63"), ("75 − 29 = ……", "46"),
                         ("67 + 25 = ……", "92"), ("80 − 43 = ……", "37")]},
         ]},
        {"sr": "Nosaka nezināmo skaitli vienādībā",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli tā, lai vienādība būtu patiesa! Par "
                      "katru pareizu skaitli — 1 punkts.",
              "rindas": [("35 + …… = 62", "27"), ("…… + 28 = 74", "46"),
                         ("85 − …… = 49", "36")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli tā, lai vienādība būtu patiesa! Par "
                      "katru pareizu skaitli — 1 punkts.",
              "rindas": [("46 + …… = 83", "37"), ("…… + 35 = 61", "26"),
                         ("72 − …… = 38", "34")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli tā, lai vienādība būtu patiesa! Par "
                      "katru pareizu skaitli — 1 punkts.",
              "rindas": [("27 + …… = 55", "28"), ("…… + 49 = 92", "43"),
                         ("64 − …… = 27", "37")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar shematisku zīmējumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 6.5,
              "ievads": "Vienā plauktā ir 38 grāmatas, otrā — par 17 vairāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Aprēķini, cik grāmatu ir otrajā plauktā!", 1),
                       ("Aprēķini, cik grāmatu ir abos plauktos kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Shēmā otrā sloksnīte par 17 garāka.   (1 p.)",
                           "2) 38 + 17 = 55   (1 p.)",
                           "3) 38 + 55 = 93   (1 p.)",
                           "4) Atbilde: otrajā 55; abos kopā 93 grāmatas.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par ogām", "vieta": 6.5,
              "ievads": "Vienā groziņā ir 45 ogas, otrā — par 18 mazāk.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Aprēķini, cik ogu ir otrajā groziņā!", 1),
                       ("Aprēķini, cik ogu ir abos groziņos kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Shēmā otrā sloksnīte par 18 īsāka.   (1 p.)",
                           "2) 45 − 18 = 27   (1 p.)",
                           "3) 45 + 27 = 72   (1 p.)",
                           "4) Atbilde: otrajā 27; abos kopā 72 ogas.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par skolēniem",
              "vieta": 6.5,
              "ievads": "Divās klasēs kopā ir 47 skolēni; vienā no tām 25.",
              "jaut": [("Uzzīmē shēmu ar divām sloksnītēm!", 1),
                       ("Aprēķini, cik skolēnu ir otrajā klasē!", 1),
                       ("Aprēķini, par cik vienā ir vairāk nekā otrā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Shēmā abas sloksnītes kopā ir 47.   (1 p.)",
                           "2) 47 − 25 = 22   (1 p.)",
                           "3) 25 − 22 = 3   (1 p.)",
                           "4) Atbilde: otrajā 22 skolēni; starpība 3.   "
                           "(1 p.)"]},
         ]},
        {"sr": "Veic aprēķinus ar naudas summām",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Pirkums veikalā", "vieta": 5.5,
              "ievads": "Burtnīca maksā 1,20 €, zīmulis — 0,80 €.",
              "jaut": [("Aprēķini abu preču cenu kopā!", 1),
                       ("Aprēķini, cik atliks no 5 €!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 1,20 € + 0,80 € = 2,00 €   (1 p.)",
                           "2) 5,00 € − 2,00 € = 3,00 €   (1 p.)",
                           "3) Atbilde: preces maksā 2 €; atliek 3 €.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Pirkums veikalā", "vieta": 5.5,
              "ievads": "Sula maksā 1,50 €, maizīte — 0,70 €.",
              "jaut": [("Aprēķini abu preču cenu kopā!", 1),
                       ("Aprēķini, cik atliks no 5 €!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 1,50 € + 0,70 € = 2,20 €   (1 p.)",
                           "2) 5,00 € − 2,20 € = 2,80 €   (1 p.)",
                           "3) Atbilde: preces maksā 2,20 €; atliek "
                           "2,80 €.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Pirkums veikalā", "vieta": 5.5,
              "ievads": "Siers maksā 3,40 €, maize — 1,30 €.",
              "jaut": [("Aprēķini abu preču cenu kopā!", 1),
                       ("Aprēķini, cik atliks no 10 €!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 3,40 € + 1,30 € = 4,70 €   (1 p.)",
                           "2) 10,00 € − 4,70 € = 5,30 €   (1 p.)",
                           "3) Atbilde: preces maksā 4,70 €; atliek "
                           "5,30 €.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
