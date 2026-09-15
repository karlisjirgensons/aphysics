# -*- coding: utf-8 -*-
"""Matemātika, 1. klase. 1.7. Kur sastopamies ar lieliem skaitļiem?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 1. klase, 1.7. temats): saskaitīšana un
atņemšana 100 apjomā (pilni desmiti, divciparu skaitlim pieskaita vienus un
desmitus), laiks (stundā 60 minūtes, analogais un digitālais pulkstenis,
5 minūšu intervāli), masa kilogramos, tilpums litros, garums līdz 100 cm un
pilnos metros, cena un iepirkumu saraksts, dati tabulā.
"""

PRIEKSMETS = "Matemātika  |  1. klase"
TEMATS = "1.7."
NOSAUKUMS = "Kur sastopamies ar lieliem skaitļiem?"

ATGADNE = [
    "Pilnus desmitus saskaita tāpat kā vienus:  30 + 40 = 70   ·   "
    "desmitus pie desmitiem, vienus pie vieniem",
    "1 stunda = 60 minūtes   ·   masu mēra kilogramos (kg)   ·   tilpumu "
    "mēra litros (l)",
    "1 m = 100 cm   ·   1 eiro = 100 centi",
]

FD = {
    "veids": "fd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 1.7. temata beigās. Pārbauda saskaitīšanu "
                "un atņemšanu 100 apjomā, laika noteikšanu un laika "
                "vienības, masas un tilpuma mērvienības, garuma mērvienības, "
                "aprēķinus ar naudu un datu lasīšanu tabulā.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Saskaita un atņem pilnus desmitus 100 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 30 + 40?", ["34", "70", "74", "340"], 1),
             ("Cik ir 90 − 50?", ["4", "40", "44", "140"], 1),
             ("Cik ir 60 + 20?", ["62", "80", "82", "620"], 1),
         ]},
        {"sr": "Divciparu skaitlim pieskaita un atņem pilnus desmitus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 34 + 20?", ["36", "44", "54", "56"], 2),
             ("Cik ir 78 − 30?", ["45", "48", "75", "108"], 1),
             ("Kurš skaitlis ir par 10 lielāks nekā 46?",
              ["36", "47", "56", "146"], 2),
         ]},
        {"sr": "Divciparu skaitlim pieskaita un atņem viencipara skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 42 + 5?", ["37", "47", "92", "425"], 1),
             ("Cik ir 56 − 4?", ["16", "52", "60", "564"], 1),
             ("Cik ir 63 + 6?", ["57", "69", "123", "636"], 1),
         ]},
        {"sr": "Zina, ka stundā ir 60 minūtes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik minūšu ir 1 stundā?", ["10", "24", "60", "100"], 2),
             ("Cik minūšu ir pusstundā?", ["15", "30", "45", "60"], 1),
             ("Mācību stunda ilgst 40 minūtes. Cik minūšu tad pietrūkst "
              "līdz pilnai stundai?",
              ["10", "20", "30", "40"], 1),
         ]},
        {"sr": "Nolasa laiku no analogā pulksteņa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Stundu rādītājs ir uz 5, minūšu rādītājs uz 12. Cik ir "
              "pulkstenis?",
              ["5:00", "5:12", "12:05", "12:25"], 0),
             ("Minūšu rādītājs ir uz 6. Cik minūtes ir pagājušas?",
              ["6", "12", "30", "60"], 2),
             ("Minūšu rādītājs ir uz 3. Cik minūtes ir pagājušas?",
              ["3", "15", "30", "45"], 1),
         ]},
        {"sr": "Aprēķina laiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Filma sākas 15:00 un ilgst 20 minūtes. Kad tā beigsies?",
              ["15:20", "15:30", "16:20", "20:15"], 0),
             ("Nodarbība sākās 10:00, beidzās 10:45. Cik ilgi tā bija?",
              ["10 minūtes", "15 minūtes", "45 minūtes", "60 minūtes"], 2),
             ("Cik minūšu ir no 8:30 līdz 9:00?",
              ["15", "30", "45", "60"], 1),
         ]},
        {"sr": "Lieto masas mērvienību kilogramu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurā mērvienībā mēra masu?",
              ["centimetros", "kilogramos", "litros", "minūtēs"], 1),
             ("Kā saīsināti raksta kilogramu?", ["k", "kg", "km", "kl"], 1),
             ("Maisā ir 20 kg kartupeļu, paņēma 5 kg. Cik palika?",
              ["10 kg", "15 kg", "25 kg", "205 kg"], 1),
         ]},
        {"sr": "Lieto tilpuma mērvienību litru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurā mērvienībā mēra tilpumu?",
              ["kilogramos", "litros", "metros", "stundās"], 1),
             ("Kā saīsināti raksta litru?", ["l", "lt", "li", "lr"], 0),
             ("Kannā ir 10 l ūdens, ielej vēl 5 l. Cik ir kopā?",
              ["5 l", "10 l", "15 l", "105 l"], 2),
         ]},
        {"sr": "Lieto garuma mērvienības 100 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik centimetru ir 1 metrā?", ["10", "60", "100", "1000"], 2),
             ("Auklas garums ir 100 cm. Cik tas ir metros?",
              ["1 m", "10 m", "100 m", "1000 m"], 0),
             ("Dēlis ir 80 cm garš. Cik cm pietrūkst līdz 1 m?",
              ["8 cm", "20 cm", "80 cm", "180 cm"], 1),
         ]},
        {"sr": "Veic aprēķinus ar naudu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Maize maksā 2 eiro, piens 1 eiro. Cik maksā abi kopā?",
              ["1 eiro", "2 eiro", "3 eiro", "21 eiro"], 2),
             ("Bija 50 centi, iztērēja 30 centus. Cik palika?",
              ["10 centi", "20 centi", "30 centi", "80 centi"], 1),
             ("Cepumu paciņa maksā 70 centus. Cik pietrūkst līdz 1 eiro?",
              ["20 centi", "30 centi", "70 centi", "170 centi"], 1),
         ]},
        {"sr": "Nosaka aptuveno rezultātu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aptuveni cik ir 39 + 21?", ["ap 20", "ap 40", "ap 60",
                                           "ap 100"], 2),
             ("Aptuveni cik ir 82 − 19?", ["ap 20", "ap 40", "ap 60",
                                           "ap 100"], 2),
             ("Kurš rezultāts ir tuvāks patiesībai:  48 + 31?",
              ["ap 30", "ap 50", "ap 80", "ap 150"], 2),
         ]},
        {"sr": "Lasa datus tabulā un veic aprēķinu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: ābols 40 centi, bumbieris 30 centi. Cik maksā abi?",
              ["10 centi", "60 centi", "70 centi", "80 centi"], 2),
             ("Tabulā: soma 20 eiro, penālis 5 eiro. Par cik soma ir "
              "dārgāka?",
              ["5 eiro", "15 eiro", "25 eiro", "205 eiro"], 1),
             ("Kāpēc datus pieraksta tabulā?",
              ["lai tos būtu viegli salīdzināt", "lai aizņemtu vairāk vietas",
               "lai nevajadzētu rēķināt", "lai būtu krāsaini"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 1.7. temata noslēgumā. "
                "Pārbauda saskaitīšanu un atņemšanu 100 apjomā, laika "
                "noteikšanu un aprēķinus, masas, tilpuma un garuma "
                "mērvienības, kā arī aprēķinus ar cenām.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Uzdevumu tekstu lasa skolotājs. Risinājumu raksti tam "
              "atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Saskaita un atņem pilnus desmitus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 40 + 30?", ["43", "70", "73", "430"], 1),
             ("Cik ir 80 − 20?", ["6", "60", "62", "180"], 1),
             ("Cik ir 50 + 50?", ["55", "90", "100", "550"], 2),
         ]},
        {"sr": "Saskaita un atņem 100 apjomā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 45 + 20?", ["47", "55", "65", "425"], 2),
             ("Cik ir 67 − 5?", ["17", "62", "72", "675"], 1),
             ("Cik ir 32 + 6?", ["26", "38", "92", "326"], 1),
         ]},
        {"sr": "Zina laika vienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik minūšu ir 1 stundā?", ["10", "30", "60", "100"], 2),
             ("Cik minūšu ir pusstundā?", ["15", "30", "45", "60"], 1),
             ("Cik stundu ir diennaktī?", ["12", "24", "60", "100"], 1),
         ]},
        {"sr": "Nolasa un aprēķina laiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Stundu rādītājs uz 7, minūšu rādītājs uz 12. Cik ir "
              "pulkstenis?",
              ["7:00", "7:12", "12:07", "12:35"], 0),
             ("Nodarbība sākās 9:00 un ilga 30 minūtes. Kad tā beidzās?",
              ["9:30", "9:45", "10:00", "12:30"], 0),
             ("Cik minūšu ir no 11:15 līdz 11:45?",
              ["15", "30", "45", "60"], 1),
         ]},
        {"sr": "Lieto masas, tilpuma un garuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurā mērvienībā mēra masu?",
              ["kilogramos", "litros", "metros", "minūtēs"], 0),
             ("Kurā mērvienībā mēra tilpumu?",
              ["kilogramos", "litros", "centimetros", "stundās"], 1),
             ("Cik cm ir 1 m?", ["10", "60", "100", "1000"], 2),
         ]},
        {"sr": "Veic aprēķinus ar naudu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Maize 2 eiro, siers 4 eiro. Cik maksā abi kopā?",
              ["2 eiro", "6 eiro", "8 eiro", "24 eiro"], 1),
             ("Bija 80 centi, iztērēja 50. Cik palika?",
              ["20 centi", "30 centi", "40 centi", "130 centi"], 1),
             ("Cik centu pietrūkst no 60 centiem līdz 1 eiro?",
              ["20", "30", "40", "60"], 2),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita un atņem 100 apjomā",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("30 + 50 = ……", "80"), ("90 − 40 = ……", "50"),
                         ("47 + 20 = ……", "67"), ("65 − 3 = ……", "62")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("20 + 60 = ……", "80"), ("70 − 30 = ……", "40"),
                         ("53 + 30 = ……", "83"), ("78 − 6 = ……", "72")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("40 + 40 = ……", "80"), ("100 − 50 = ……", "50"),
                         ("36 + 40 = ……", "76"), ("89 − 7 = ……", "82")]},
         ]},
        {"sr": "Pārveido mērvienības",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("1 stunda = …… minūtes", "60"),
                         ("1 m = …… cm", "100"),
                         ("1 eiro = …… centi", "100")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Pusstunda = …… minūtes", "30"),
                         ("1 dm = …… cm", "10"),
                         ("2 eiro = …… centi", "200")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("1 diennakts = …… stundas", "24"),
                         ("1 m = …… dm", "10"),
                         ("1 nedēļa = …… dienas", "7")]},
         ]},
        {"sr": "Risina uzdevumu par pirkumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Iepirkumu saraksts", "vieta": 6.0,
              "ievads": "Ābols maksā 40 centus, bumbieris — 30 centus.",
              "jaut": [("Pieraksti, kā aprēķināt abu augļu cenu kopā!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik atliks no 1 eiro!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 40 + 30   (1 p.)",
                           "2) 40 + 30 = 70 (centi)   (1 p.)",
                           "3) 100 − 70 = 30 (centi)   (1 p.)",
                           "4) Atbilde: augļi maksā 70 centus, atliek "
                           "30 centi.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Iepirkumu saraksts", "vieta": 6.0,
              "ievads": "Burtnīca maksā 50 centus, zīmulis — 20 centus.",
              "jaut": [("Pieraksti, kā aprēķināt abu preču cenu kopā!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik atliks no 1 eiro!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 50 + 20   (1 p.)",
                           "2) 50 + 20 = 70 (centi)   (1 p.)",
                           "3) 100 − 70 = 30 (centi)   (1 p.)",
                           "4) Atbilde: preces maksā 70 centus, atliek "
                           "30 centi.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Iepirkumu saraksts", "vieta": 6.0,
              "ievads": "Sula maksā 60 centus, maizīte — 30 centus.",
              "jaut": [("Pieraksti, kā aprēķināt abu preču cenu kopā!", 1),
                       ("Aprēķini to!", 1),
                       ("Aprēķini, cik atliks no 1 eiro!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 60 + 30   (1 p.)",
                           "2) 60 + 30 = 90 (centi)   (1 p.)",
                           "3) 100 − 90 = 10 (centi)   (1 p.)",
                           "4) Atbilde: preces maksā 90 centus, atliek "
                           "10 centi.   (1 p.)"]},
         ]},
        {"sr": "Risina uzdevumu par laiku vai lielumiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par laiku", "vieta": 5.5,
              "ievads": "Nodarbība sākās plkst. 10:00 un ilga 40 minūtes.",
              "jaut": [("Uzraksti, cikos nodarbība beidzās!", 1),
                       ("Aprēķini, cik minūšu pietrūkst līdz pilnai "
                        "stundai!", 1),
                       ("Uzzīmē pulksteni, kas rāda nodarbības sākumu!", 1)],
              "atbildes": ["1) 10:40   (1 p.)", "2) 60 − 40 = 20 minūtes   "
                           "(1 p.)",
                           "3) Uzzīmēts pulkstenis: stundu rādītājs uz 10, "
                           "minūšu rādītājs uz 12.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par masu", "vieta": 5.5,
              "ievads": "Maisā bija 30 kg kartupeļu. Pārdeva 20 kg.",
              "jaut": [("Pieraksti aprēķinu!", 1),
                       ("Aprēķini, cik kilogramu palika!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 30 kg − 20 kg   (1 p.)",
                           "2) 30 kg − 20 kg = 10 kg   (1 p.)",
                           "3) Atbilde: palika 10 kg kartupeļu.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par tilpumu",
              "vieta": 5.5,
              "ievads": "Kannā bija 10 l ūdens. Ielēja vēl 8 l.",
              "jaut": [("Pieraksti aprēķinu!", 1),
                       ("Aprēķini, cik litru ir kopā!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 10 l + 8 l   (1 p.)",
                           "2) 10 l + 8 l = 18 l   (1 p.)",
                           "3) Atbilde: kannā ir 18 l ūdens.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
