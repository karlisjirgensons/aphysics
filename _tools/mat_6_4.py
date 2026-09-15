# -*- coding: utf-8 -*-
"""Matemātika, 6. klase. 6.4. Kā attēlo un raksturo telpiskus ķermeņus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 6. klase, 6.4. temats): telpiska ķermeņa
elementi (skaldne, šķautne, virsotne), daudzskaldnis, piramīda, cilindrs,
konuss, taisnstūra paralēlskaldņa izmēri, virsmas izklājums un virsmas
laukums, tilpums un tā mērvienības (cm³, dm³, m³, l = dm³), mērvienību
pārveidošana un ķermeņa skati dažādās plaknēs.
"""

PRIEKSMETS = "Matemātika  |  6. klase"
TEMATS = "6.4."
NOSAUKUMS = "Kā attēlo un raksturo telpiskus ķermeņus?"

ATGADNE = [
    "Daudzskaldņa virsmu veido skaldnes; skaldņu malas ir šķautnes, to "
    "galapunkti — virsotnes.",
    "Taisnstūra paralēlskaldnis ar izmēriem a, b un c:   V = a · b · c   ·  "
    " S = 2 · (a · b + a · c + b · c)   ·   kubam   V = a³,   S = 6 · a².",
    "Tilpuma mērvienības:   1 dm³ = 1 l   ·   1 l = 1000 cm³   ·   "
    "1 m³ = 1000 dm³   ·   laukuma:   1 dm² = 100 cm².",
]

FD = {
    "veids": "fd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 6.4. temata beigās. Pārbauda telpisku "
                "ķermeņu elementus un īpašības, taisnstūra paralēlskaldņa "
                "izklājumu, virsmas laukumu un tilpumu, tilpuma "
                "mērvienības un ķermeņa skatus.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosauc telpiska ķermeņa elementus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc daudzskaldņa virsmas daudzstūri?",
              ["skaldne", "šķautne", "virsotne", "izklājums"], 0),
             ("Kā sauc skaldnes malu?",
              ["šķautne", "skaldne", "virsotne", "rādiuss"], 0),
             ("Kā sauc šķautnes galapunktu?",
              ["virsotne", "šķautne", "skaldne", "centrs"], 0),
         ]},
        {"sr": "Raksturo taisnstūra paralēlskaldni",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik skaldņu ir taisnstūra paralēlskaldnim?",
              ["6", "8", "12", "4"], 0),
             ("Cik šķautņu ir taisnstūra paralēlskaldnim?",
              ["12", "6", "8", "4"], 0),
             ("Cik virsotņu ir taisnstūra paralēlskaldnim?",
              ["8", "6", "12", "4"], 0),
         ]},
        {"sr": "Atpazīst telpiskus ķermeņus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kuram ķermenim nav skaldņu?",
              ["lodei", "kubam", "piramīdai", "prizmai"], 0),
             ("Kāda figūra ir cilindra pamats?",
              ["riņķis", "kvadrāts", "trijstūris", "taisnstūris"], 0),
             ("Kāda figūra ir konusa pamats?",
              ["riņķis", "kvadrāts", "trijstūris", "taisnstūris"], 0),
         ]},
        {"sr": "Zina, kas ir izklājums",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir ķermeņa virsmas izklājums?",
              ["virsma, izklāta plaknē", "ķermeņa tilpums",
               "ķermeņa skats", "šķautņu garumu summa"], 0),
             ("No cik taisnstūriem sastāv paralēlskaldņa izklājums?",
              ["6", "4", "8", "12"], 0),
             ("Ko rāda izklājuma laukums?",
              ["virsmas laukumu", "tilpumu", "šķautņu skaitu",
               "augstumu"], 0),
         ]},
        {"sr": "Aprēķina paralēlskaldņa virsmas laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Izmēri ir 2 cm, 3 cm un 4 cm. Cik liels ir virsmas laukums?",
              ["52 cm²", "24 cm²", "26 cm²", "48 cm²"], 0),
             ("Kuba šķautne ir 3 cm. Cik liels ir virsmas laukums?",
              ["54 cm²", "27 cm²", "9 cm²", "36 cm²"], 0),
             ("Ar kuru formulu aprēķina kuba virsmas laukumu?",
              ["S = 6 · a²", "S = a³", "S = 4 · a", "S = 2 · a"], 0),
         ]},
        {"sr": "Aprēķina paralēlskaldņa tilpumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Izmēri ir 2 cm, 3 cm un 4 cm. Cik liels ir tilpums?",
              ["24 cm³", "9 cm³", "52 cm³", "12 cm³"], 0),
             ("Kuba šķautne ir 5 cm. Cik liels ir tilpums?",
              ["125 cm³", "25 cm³", "150 cm³", "15 cm³"], 0),
             ("Ar kuru formulu aprēķina paralēlskaldņa tilpumu?",
              ["V = a · b · c", "V = a + b + c", "V = 6 · a · b",
               "V = 2 · (a + b)"], 0),
         ]},
        {"sr": "Zina tilpuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik litru ir 1 dm³?", ["1 l", "10 l", "100 l", "1000 l"], 0),
             ("Cik kubikcentimetru ir 1 litrā?",
              ["1000 cm³", "100 cm³", "10 cm³", "1 cm³"], 0),
             ("Cik kubikdecimetru ir 1 m³?",
              ["1000 dm³", "100 dm³", "10 dm³", "1 dm³"], 0),
         ]},
        {"sr": "Pārveido tilpuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik litru ir 5000 cm³?", ["5 l", "50 l", "0,5 l", "500 l"], 0),
             ("Cik kubikdecimetru ir 2 m³?",
              ["2000 dm³", "200 dm³", "20 dm³", "2 dm³"], 0),
             ("Cik kubikcentimetru ir 3 l?",
              ["3000 cm³", "300 cm³", "30 cm³", "3 cm³"], 0),
         ]},
        {"sr": "Pārveido laukuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik kvadrātcentimetru ir 1 dm²?",
              ["100 cm²", "10 cm²", "1000 cm²", "1 cm²"], 0),
             ("Cik kvadrātdecimetru ir 1 m²?",
              ["100 dm²", "10 dm²", "1000 dm²", "1 dm²"], 0),
             ("Cik kvadrātcentimetru ir 3 dm²?",
              ["300 cm²", "30 cm²", "3000 cm²", "3 cm²"], 0),
         ]},
        {"sr": "Raksturo ķermeņa skatus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir kuba skats no priekšas?",
              ["kvadrāts", "kubs", "trijstūris", "riņķis"], 0),
             ("Kāds ir cilindra skats no augšas?",
              ["riņķis", "taisnstūris", "kvadrāts", "trijstūris"], 0),
             ("Kāpēc telpisku ķermeni zīmē uzskatāmi?",
              ["to nevar attēlot pilnībā", "tas ir ātrāk",
               "tas ir skaistāk", "tā prasa mērvienības"], 0),
         ]},
        {"sr": "Spriež par izmēru maiņu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kuba šķautni palielina 2 reizes. Cik reižu aug tilpums?",
              ["8", "2", "4", "6"], 0),
             ("Kuba šķautni palielina 2 reizes. Cik reižu aug virsmas "
              "laukums?", ["4", "2", "8", "6"], 0),
             ("Kuba šķautni samazina 3 reizes. Cik reižu sarūk tilpums?",
              ["27", "3", "9", "6"], 0),
         ]},
        {"sr": "Lieto tilpumu situāciju uzdevumos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Akvārijs ir 50 cm, 20 cm un 30 cm. Cik litru ūdens tajā "
              "ietilpst?", ["30 l", "3 l", "300 l", "100 l"], 0),
             ("Kastē 40 cm, 30 cm un 20 cm. Cik liels ir tilpums?",
              ["24 000 cm³", "2400 cm³", "90 cm³", "240 cm³"], 0),
             ("Kastē ietilpst 8 kubi ar šķautni 1 dm. Cik litru tas ir?",
              ["8 l", "1 l", "80 l", "800 l"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 6.4. temata noslēgumā. "
                "Pārbauda telpisku ķermeņu elementus, taisnstūra "
                "paralēlskaldņa virsmas laukumu un tilpumu, mērvienību "
                "pārveidošanu un spriedumus par izmēru maiņu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Nosauc ķermeņa elementus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc daudzskaldņa virsmas daudzstūri?",
              ["skaldne", "šķautne", "virsotne", "izklājums"], 0),
             ("Cik šķautņu ir kubam?", ["12", "6", "8", "4"], 0),
             ("Cik virsotņu ir taisnstūra paralēlskaldnim?",
              ["8", "6", "12", "4"], 0),
         ]},
        {"sr": "Aprēķina virsmas laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Izmēri ir 3 cm, 4 cm un 5 cm. Cik liels ir virsmas laukums?",
              ["94 cm²", "60 cm²", "47 cm²", "12 cm²"], 0),
             ("Kuba šķautne ir 4 cm. Cik liels ir virsmas laukums?",
              ["96 cm²", "64 cm²", "16 cm²", "48 cm²"], 0),
             ("Ar kuru formulu aprēķina kuba virsmas laukumu?",
              ["S = 6 · a²", "S = a³", "S = 4 · a", "S = 2 · a"], 0),
         ]},
        {"sr": "Aprēķina tilpumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Izmēri ir 3 cm, 4 cm un 5 cm. Cik liels ir tilpums?",
              ["60 cm³", "12 cm³", "94 cm³", "20 cm³"], 0),
             ("Kuba šķautne ir 6 cm. Cik liels ir tilpums?",
              ["216 cm³", "36 cm³", "216 cm²", "18 cm³"], 0),
             ("Ar kuru formulu aprēķina paralēlskaldņa tilpumu?",
              ["V = a · b · c", "V = a + b + c", "V = 6 · a · b",
               "V = 2 · (a + b)"], 0),
         ]},
        {"sr": "Pārveido tilpuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik litru ir 1 dm³?", ["1 l", "10 l", "100 l", "1000 l"], 0),
             ("Cik kubikcentimetru ir 2 l?",
              ["2000 cm³", "200 cm³", "20 cm³", "2 cm³"], 0),
             ("Cik kubikdecimetru ir 5 m³?",
              ["5000 dm³", "500 dm³", "50 dm³", "5 dm³"], 0),
         ]},
        {"sr": "Raksturo izklājumu un skatus",
         "stunda": TEMATS,
         "jautajumi": [
             ("No cik taisnstūriem sastāv paralēlskaldņa izklājums?",
              ["6", "4", "8", "12"], 0),
             ("Kāds ir cilindra skats no augšas?",
              ["riņķis", "taisnstūris", "kvadrāts", "trijstūris"], 0),
             ("Ko rāda izklājuma laukums?",
              ["virsmas laukumu", "tilpumu", "šķautņu skaitu",
               "augstumu"], 0),
         ]},
        {"sr": "Spriež par izmēru maiņu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kuba šķautni palielina 3 reizes. Cik reižu aug tilpums?",
              ["27", "3", "9", "6"], 0),
             ("Kuba šķautni palielina 2 reizes. Cik reižu aug virsmas "
              "laukums?", ["4", "2", "8", "6"], 0),
             ("Akvārijs ir 40 cm, 25 cm un 30 cm. Cik litru tajā ietilpst?",
              ["30 l", "3 l", "300 l", "95 l"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina virsmas laukumu un tilpumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Izmēri 2 cm, 3 cm, 5 cm:  V = …… cm³", "30"),
                         ("Tie paši izmēri:  S = …… cm²", "62"),
                         ("Kubs ar šķautni 4 cm:  V = …… cm³", "64"),
                         ("Tas pats kubs:  S = …… cm²", "96")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Izmēri 3 cm, 4 cm, 6 cm:  V = …… cm³", "72"),
                         ("Tie paši izmēri:  S = …… cm²", "108"),
                         ("Kubs ar šķautni 5 cm:  V = …… cm³", "125"),
                         ("Tas pats kubs:  S = …… cm²", "150")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Izmēri 2 cm, 4 cm, 10 cm:  V = …… cm³", "80"),
                         ("Tie paši izmēri:  S = …… cm²", "136"),
                         ("Kubs ar šķautni 3 cm:  V = …… cm³", "27"),
                         ("Tas pats kubs:  S = …… cm²", "54")]},
         ]},
        {"sr": "Pārveido tilpuma un laukuma mērvienības",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Mērvienības",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("3 l = …… cm³", "3000"),
                         ("2 m³ = …… dm³", "2000"),
                         ("5 dm² = …… cm²", "500")]},
             {"tips": "parveide", "virs": "Mērvienības",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("4000 cm³ = …… l", "4"),
                         ("6 m³ = …… dm³", "6000"),
                         ("2 m² = …… dm²", "200")]},
             {"tips": "parveide", "virs": "Mērvienības",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("7 l = …… dm³", "7"),
                         ("500 dm³ = …… m³", "0,5"),
                         ("8 dm² = …… cm²", "800")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar tilpumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Akvārija izmēri ir 60 cm, 30 cm un 40 cm.   "
                        "a) Aprēķini tilpumu kubikcentimetros!   b) Cik "
                        "litru tas ir?   c) Cik litru ūdens ielej, ja "
                        "piepilda {3|4} no tilpuma?   d) Cik liels ir "
                        "akvārija dibena laukums?",
              "kriteriji": ["a) 60 · 30 · 40 = 72 000 cm³.   (1 p.)",
                            "b) 72 000 cm³ = 72 l.   (1 p.)",
                            "c) 72 · {3|4} = 54 l.   (1 p.)",
                            "d) 60 · 30 = 1800 cm².   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Kaste ir taisnstūra paralēlskaldnis ar izmēriem "
                        "50 cm, 40 cm un 20 cm.   a) Aprēķini tilpumu!   "
                        "b) Cik litru tas ir?   c) Cik liels ir virsmas "
                        "laukums?   d) Cik kvadrātmetru kartona vajag "
                        "kastei?",
              "kriteriji": ["a) 50 · 40 · 20 = 40 000 cm³.   (1 p.)",
                            "b) 40 000 cm³ = 40 l.   (1 p.)",
                            "c) 2 · (2000 + 1000 + 800) = 7600 cm². "
                            "  (1 p.)",
                            "d) 7600 cm² = 0,76 m².   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Kuba formas trauka šķautne ir 20 cm.   "
                        "a) Aprēķini tilpumu!   b) Cik litru tas ir?   "
                        "c) Cik liels ir virsmas laukums?   d) Cik reižu "
                        "augs tilpums, ja šķautni palielinās 2 reizes?",
              "kriteriji": ["a) 20³ = 8000 cm³.   (1 p.)",
                            "b) 8000 cm³ = 8 l.   (1 p.)",
                            "c) 6 · 400 = 2400 cm².   (1 p.)",
                            "d) 8 reizes.   (1 p.)"]},
         ]},
        {"sr": "Skaidro ķermeņa uzbūvi un lielumus",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Kuba lielumi", "vieta": 4.6,
              "ievads": "Kuba šķautne ir 3 cm.",
              "jaut": [("Cik liels ir tilpums?", 1),
                       ("Cik liels ir virsmas laukums?", 1),
                       ("Kā mainīsies tilpums, ja šķautni dubultos?", 1)],
              "atbildes": ["1) 3³ = 27 cm³.   (1 p.)",
                           "2) 6 · 9 = 54 cm².   (1 p.)",
                           "3) Augs 8 reizes — 2³ = 8.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Izklājums", "vieta": 4.6,
              "ievads": "Taisnstūra paralēlskaldņa izmēri ir 4 cm, 3 cm un "
                        "2 cm.",
              "jaut": [("No cik taisnstūriem sastāv izklājums?", 1),
                       ("Cik liels ir izklājuma laukums?", 1),
                       ("Kā šo laukumu sauc citiem vārdiem?", 1)],
              "atbildes": ["1) No 6 taisnstūriem.   (1 p.)",
                           "2) 2 · (12 + 8 + 6) = 52 cm².   (1 p.)",
                           "3) Virsmas laukums.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Tilpuma mērvienības",
              "vieta": 4.6,
              "ievads": "Traukā ietilpst 2500 cm³ ūdens.",
              "jaut": [("Cik litru tas ir?", 1),
                       ("Cik kubikdecimetru tas ir?", 1),
                       ("Cik šādu trauku vajag, lai piepildītu 10 l "
                        "kannu?", 1)],
              "atbildes": ["1) 2,5 l.   (1 p.)", "2) 2,5 dm³.   (1 p.)",
                           "3) 10 : 2,5 = 4 trauki.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
