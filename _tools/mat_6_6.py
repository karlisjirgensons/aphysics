# -*- coding: utf-8 -*-
"""Matemātika, 6. klase. 6.6. Kāpēc nepieciešami skaitļi, kas mazāki nekā 0?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 6. klase, 6.6. temats): pozitīvi un
negatīvi skaitļi un to lietojums, pretējs skaitlis un pieraksts −(−a),
skaitļa modulis kā attālums līdz nullei, skaitļu salīdzināšana un
sakārtošana, attālums starp skaitļiem uz skaitļu taisnes, visa koordinātu
plakne (abscisu un ordinātu ass), punkta koordinātas, attālums no punkta līdz
taisnei un simetrija pret taisni un pret punktu.
"""

PRIEKSMETS = "Matemātika  |  6. klase"
TEMATS = "6.6."
NOSAUKUMS = "Kāpēc nepieciešami skaitļi, kuri ir mazāki nekā nulle?"

ATGADNE = [
    "Skaitļi, kas lielāki nekā 0, ir pozitīvi; mazāki nekā 0 — negatīvi. "
    "Pretējiem skaitļiem a un −a attālums līdz nullei ir vienāds.",
    "Modulis ir attālums līdz nullei:   |5| = 5   ·   |−5| = 5   ·   "
    "|0| = 0   ·   −(−6) = 6",
    "Koordinātu plaknē horizontālā ass ir abscisu ass (x), vertikālā — "
    "ordinātu ass (y); punktu pieraksta A(x; y).",
]

FD = {
    "veids": "fd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 6.6. temata beigās. Pārbauda pozitīvus "
                "un negatīvus skaitļus, pretējo skaitli un moduli, skaitļu "
                "salīdzināšanu un attālumu uz skaitļu taisnes, koordinātu "
                "plakni un simetriju.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Atpazīst pozitīvus un negatīvus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir negatīvs?", ["−7", "7", "0", "0,7"], 0),
             ("Kāds skaitlis ir 0?",
              ["ne pozitīvs, ne negatīvs", "pozitīvs", "negatīvs",
               "pretējs"], 0),
             ("Kur sadzīvē lieto negatīvus skaitļus?",
              ["temperatūrai zem nulles", "cenām veikalā",
               "skolēnu skaitam", "laukuma mērīšanai"], 0),
         ]},
        {"sr": "Nosaka pretējo skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir skaitļa 8 pretējais skaitlis?",
              ["−8", "8", "{1|8}", "0"], 0),
             ("Kāds ir skaitļa −3 pretējais skaitlis?",
              ["3", "−3", "{1|3}", "0"], 0),
             ("Ar ko vienāds −(−6)?", ["6", "−6", "0", "12"], 0),
         ]},
        {"sr": "Nosaka skaitļa moduli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir |−5|?", ["5", "−5", "0", "10"], 0),
             ("Cik ir |9|?", ["9", "−9", "0", "18"], 0),
             ("Ko rāda skaitļa modulis?",
              ["attālumu līdz nullei", "skaitļa zīmi",
               "pretējo skaitli", "skaitļa daļu"], 0),
         ]},
        {"sr": "Salīdzina pozitīvus un negatīvus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir lielākais?", ["2", "−2", "−5", "−10"], 0),
             ("Kurš skaitlis ir mazākais?", ["−9", "−4", "0", "4"], 0),
             ("Kurš apgalvojums ir patiess?",
              ["−3 > −8", "−3 < −8", "−3 = −8", "−8 > 0"], 0),
         ]},
        {"sr": "Sakārto skaitļus secībā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurā rindā skaitļi ir augošā secībā?",
              ["−5; −2; 0; 3", "3; 0; −2; −5", "−2; −5; 0; 3",
               "0; −2; −5; 3"], 0),
             ("Kurā rindā skaitļi ir dilstošā secībā?",
              ["4; 1; −1; −6", "−6; −1; 1; 4", "1; 4; −1; −6",
               "−1; −6; 1; 4"], 0),
             ("Kurš skaitlis atrodas pa kreisi no −4 uz skaitļu taisnes?",
              ["−7", "−1", "0", "4"], 0),
         ]},
        {"sr": "Skaita ar soli uz skaitļu taisnes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds skaitlis ir par 5 lielāks nekā −8?",
              ["−3", "−13", "3", "13"], 0),
             ("Kāds skaitlis ir par 3 mazāks nekā −2?",
              ["−5", "1", "5", "−1"], 0),
             ("Turpini virkni: −10; −8; −6; ……",
              ["−4", "−2", "0", "−8"], 0),
         ]},
        {"sr": "Nosaka attālumu starp skaitļiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir attālums starp −3 un 4?",
              ["7", "1", "−7", "12"], 0),
             ("Cik liels ir attālums starp −6 un −2?",
              ["4", "8", "−4", "12"], 0),
             ("Cik liels ir attālums no −9 līdz 0?",
              ["9", "−9", "0", "18"], 0),
         ]},
        {"sr": "Lieto negatīvus skaitļus sadzīvē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Temperatūra bija −5 °C, pieauga par 8 °C. Kāda tā ir?",
              ["3 °C", "−13 °C", "13 °C", "−3 °C"], 0),
             ("Kontā ir −20 eiro; iemaksā 50 eiro. Cik ir kontā?",
              ["30 eiro", "70 eiro", "−70 eiro", "−30 eiro"], 0),
             ("Lifts no 3. stāva nobrauc 5 stāvus. Kurā stāvā tas ir?",
              ["−2", "2", "8", "−8"], 0),
         ]},
        {"sr": "Zina koordinātu asu nosaukumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc horizontālo asi?",
              ["abscisu ass", "ordinātu ass", "simetrijas ass",
               "skaitļu ass"], 0),
             ("Kā sauc vertikālo asi?",
              ["ordinātu ass", "abscisu ass", "simetrijas ass",
               "skaitļu ass"], 0),
             ("Kā pieraksta punkta koordinātas?",
              ["A(x; y)", "A(y; x)", "A(x · y)", "A(x + y)"], 0),
         ]},
        {"sr": "Nolasa un atliek punktus visā plaknē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur atrodas punkts A(−3; 2)?",
              ["pa kreisi un uz augšu", "pa labi un uz augšu",
               "pa kreisi un uz leju", "pa labi un uz leju"], 0),
             ("Kur atrodas punkts B(2; −4)?",
              ["pa labi un uz leju", "pa kreisi un uz leju",
               "pa labi un uz augšu", "uz ass"], 0),
             ("Kur atrodas punkts C(0; −5)?",
              ["uz ordinātu ass", "uz abscisu ass", "sākumpunktā",
               "pa labi"], 0),
         ]},
        {"sr": "Nosaka attālumu no punkta līdz taisnei",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir attālums no punkta līdz taisnei?",
              ["īsākais nogrieznis starp tiem", "jebkurš nogrieznis",
               "taisnes garums", "punkta koordināta"], 0),
             ("Cik liels ir attālums no A(3; 4) līdz abscisu asij?",
              ["4", "3", "7", "5"], 0),
             ("Cik liels ir attālums no B(−6; 2) līdz ordinātu asij?",
              ["6", "2", "8", "−6"], 0),
         ]},
        {"sr": "Lieto simetriju koordinātu plaknē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds punkts ir simetrisks A(3; 5) pret abscisu asi?",
              ["(3; −5)", "(−3; 5)", "(−3; −5)", "(5; 3)"], 0),
             ("Kāds punkts ir simetrisks A(3; 5) pret sākumpunktu?",
              ["(−3; −5)", "(3; −5)", "(−3; 5)", "(5; 3)"], 0),
             ("Kad figūras ir simetriskas pret punktu?",
              ["ja vienu pagriež par 180° ap to", "ja tās ir vienādas",
               "ja tās ir blakus", "ja tās ir uz vienas ass"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 6.6. temata noslēgumā. "
                "Pārbauda pozitīvus un negatīvus skaitļus, pretējo skaitli "
                "un moduli, salīdzināšanu un attālumu uz skaitļu taisnes, "
                "koordinātu plakni un simetriju.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Atpazīst skaitļus un to pretējos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir negatīvs?", ["−12", "12", "0", "1,2"], 0),
             ("Kāds ir skaitļa −7 pretējais skaitlis?",
              ["7", "−7", "{1|7}", "0"], 0),
             ("Ar ko vienāds −(−9)?", ["9", "−9", "0", "18"], 0),
         ]},
        {"sr": "Nosaka moduli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir |−11|?", ["11", "−11", "0", "22"], 0),
             ("Ko rāda skaitļa modulis?",
              ["attālumu līdz nullei", "skaitļa zīmi", "pretējo skaitli",
               "skaitļa daļu"], 0),
             ("Kuriem skaitļiem moduļi ir vienādi?",
              ["−4 un 4", "−4 un 0", "4 un 8", "0 un 4"], 0),
         ]},
        {"sr": "Salīdzina un sakārto skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš apgalvojums ir patiess?",
              ["−2 > −9", "−2 < −9", "−2 = −9", "−9 > 0"], 0),
             ("Kurā rindā skaitļi ir augošā secībā?",
              ["−7; −3; 0; 5", "5; 0; −3; −7", "−3; −7; 0; 5",
               "0; −3; −7; 5"], 0),
             ("Kurš skaitlis ir mazākais?", ["−8", "−1", "0", "8"], 0),
         ]},
        {"sr": "Nosaka attālumu uz skaitļu taisnes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir attālums starp −5 un 3?",
              ["8", "2", "−8", "15"], 0),
             ("Cik liels ir attālums starp −9 un −4?",
              ["5", "13", "−5", "36"], 0),
             ("Kāds skaitlis ir par 6 lielāks nekā −10?",
              ["−4", "−16", "4", "16"], 0),
         ]},
        {"sr": "Lieto koordinātu plakni",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc horizontālo asi?",
              ["abscisu ass", "ordinātu ass", "simetrijas ass",
               "skaitļu ass"], 0),
             ("Kur atrodas punkts A(−4; −2)?",
              ["pa kreisi un uz leju", "pa labi un uz leju",
               "pa kreisi un uz augšu", "uz ass"], 0),
             ("Cik liels ir attālums no B(5; −3) līdz abscisu asij?",
              ["3", "5", "8", "−3"], 0),
         ]},
        {"sr": "Lieto simetriju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds punkts ir simetrisks A(2; 6) pret ordinātu asi?",
              ["(−2; 6)", "(2; −6)", "(−2; −6)", "(6; 2)"], 0),
             ("Kāds punkts ir simetrisks A(2; 6) pret sākumpunktu?",
              ["(−2; −6)", "(2; −6)", "(−2; 6)", "(6; 2)"], 0),
             ("Kad figūras ir simetriskas pret taisni?",
              ["ja tās sakrīt, pārlokot pa taisni", "ja tās ir vienādas",
               "ja tās ir blakus", "ja tām ir kopīga virsotne"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Lieto pretējo skaitli, moduli un salīdzināšanu",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitļa −6 pretējais skaitlis ir ……", "6"),
                         ("|−15| = ……", "15"),
                         ("−(−4) = ……", "4"),
                         ("Attālums starp −3 un 5 ir ……", "8")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitļa 11 pretējais skaitlis ir ……", "−11"),
                         ("|−8| = ……", "8"),
                         ("−(−12) = ……", "12"),
                         ("Attālums starp −7 un −2 ir ……", "5")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitļa −20 pretējais skaitlis ir ……", "20"),
                         ("|0| = ……", "0"),
                         ("−(−7) = ……", "7"),
                         ("Attālums starp −10 un 4 ir ……", "14")]},
         ]},
        {"sr": "Nolasa un atliek punktus koordinātu plaknē",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Koordinātu plakne",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Punkts pa kreisi 3, uz leju 2:   A……",
                          "A(−3; −2)"),
                         ("Attālums no B(4; −5) līdz abscisu asij:   ……",
                          "5"),
                         ("Punkts, simetrisks C(2; 3) pret abscisu asi:  "
                          " ……", "(2; −3)")]},
             {"tips": "parveide", "virs": "Koordinātu plakne",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Punkts pa labi 5, uz leju 1:   A……", "A(5; −1)"),
                         ("Attālums no B(−6; 2) līdz ordinātu asij:   ……",
                          "6"),
                         ("Punkts, simetrisks C(4; 1) pret ordinātu asi:  "
                          " ……", "(−4; 1)")]},
             {"tips": "parveide", "virs": "Koordinātu plakne",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Punkts pa kreisi 2, uz augšu 6:   A……",
                          "A(−2; 6)"),
                         ("Attālums no B(3; 7) līdz abscisu asij:   ……",
                          "7"),
                         ("Punkts, simetrisks C(1; 5) pret sākumpunktu:  "
                          " ……", "(−1; −5)")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar negatīviem skaitļiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Temperatūra", "vieta": 5.6,
              "teksts": "Naktī bija −7 °C; dienā temperatūra pieauga par "
                        "12 °C, bet vakarā pazeminājās par 5 °C.   a) Kāda "
                        "temperatūra bija dienā?   b) Kāda temperatūra bija "
                        "vakarā?   c) Par cik grādiem vakara temperatūra "
                        "atšķiras no nakts?   d) Kura temperatūra bija "
                        "viszemākā?",
              "kriteriji": ["a) −7 + 12 = 5 °C.   (1 p.)",
                            "b) 5 − 5 = 0 °C.   (1 p.)",
                            "c) 0 − (−7) = 7 °C.   (1 p.)",
                            "d) Nakts temperatūra −7 °C.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Konta stāvoklis", "vieta": 5.6,
              "teksts": "Kontā bija −45 eiro; tika iemaksāti 100 eiro, tad "
                        "izņemti 30 eiro.   a) Cik eiro kontā pēc "
                        "iemaksas?   b) Cik eiro kontā beigās?   c) Par cik "
                        "eiro konta stāvoklis kopumā mainījās?   d) Cik eiro "
                        "vēl vajadzēja iemaksāt sākumā, lai konts kļūtu "
                        "par 0?",
              "kriteriji": ["a) −45 + 100 = 55 eiro.   (1 p.)",
                            "b) 55 − 30 = 25 eiro.   (1 p.)",
                            "c) 25 − (−45) = 70 eiro.   (1 p.)",
                            "d) 45 eiro.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Figūra plaknē", "vieta": 5.6,
              "teksts": "Koordinātu plaknē doti punkti A(−3; 2), B(3; 2) "
                        "un C(3; −1).   a) Cik garš ir nogrieznis AB?   "
                        "b) Cik garš ir nogrieznis BC?   c) Cik liels ir "
                        "taisnstūra ABCD laukums, ja D(−3; −1)?   d) Kādas "
                        "koordinātas ir punktam, kas simetrisks A pret "
                        "abscisu asi?",
              "kriteriji": ["a) AB = 6.   (1 p.)", "b) BC = 3.   (1 p.)",
                            "c) 6 · 3 = 18 kvadrātvienības.   (1 p.)",
                            "d) (−3; −2).   (1 p.)"]},
         ]},
        {"sr": "Skaidro skaitļu novietojumu un simetriju",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Skaitļu taisne", "vieta": 4.6,
              "ievads": "Doti skaitļi  −6;  2;  −1  un  5.",
              "jaut": [("Sakārto tos augošā secībā!", 1),
                       ("Kuram skaitlim ir lielākais modulis?", 1),
                       ("Cik liels ir attālums starp mazāko un lielāko?",
                        1)],
              "atbildes": ["1) −6; −1; 2; 5.   (1 p.)",
                           "2) Skaitlim −6, jo |−6| = 6.   (1 p.)",
                           "3) 5 − (−6) = 11.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Pretēji skaitļi", "vieta": 4.6,
              "ievads": "Dots skaitlis a = −4.",
              "jaut": [("Uzraksti tam pretējo skaitli!", 1),
                       ("Cik ir |a|?", 1),
                       ("Paskaidro, kāpēc a un −a moduļi ir vienādi!", 1)],
              "atbildes": ["1) 4.   (1 p.)", "2) |−4| = 4.   (1 p.)",
                           "3) Abi atrodas vienādā attālumā no nulles. "
                           "  (1 p.)"]},
             {"tips": "jautajumi", "virs": "Simetrija plaknē", "vieta": 4.6,
              "ievads": "Koordinātu plaknē dots punkts A(−5; 3).",
              "jaut": [("Kāds punkts ir simetrisks A pret abscisu asi?", 1),
                       ("Kāds punkts ir simetrisks A pret ordinātu asi?",
                        1),
                       ("Kāds punkts ir simetrisks A pret sākumpunktu?",
                        1)],
              "atbildes": ["1) (−5; −3).   (1 p.)", "2) (5; 3).   (1 p.)",
                           "3) (5; −3).   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
