# -*- coding: utf-8 -*-
"""Matemātika, 1. klase. 1.6. Ko nozīmē «par tik vairāk», «par tik mazāk»?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 1. klase, 1.6. temats): «par tik vairāk»
nozīmē «tikpat un vēl tik», divu lielumu salīdzināšana, shematisks zīmējums,
situācijas pieraksts ar vienādību, kurā nezināmo aizstāj ar simbolu,
palielināšana un pamazināšana, datu lasīšana tabulā un stabiņu diagrammā.
"""

PRIEKSMETS = "Matemātika  |  1. klase"
TEMATS = "1.6."
NOSAUKUMS = "Ko nozīmē «par tik vairāk», «par tik mazāk»?"

ATGADNE = [
    "«Par 4 vairāk» nozīmē «tikpat un vēl 4»   ·   «par 4 mazāk» nozīmē "
    "«tikpat, bet 4 mazāk»",
    "Palielināt par …  →  saskaita   ·   pamazināt par …  →  atņem",
    "Par cik viens lielāks nekā otrs  →  no lielākā atņem mazāko",
]

FD = {
    "veids": "fd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 1.6. temata beigās. Pārbauda izpratni par "
                "«par tik vairāk» un «par tik mazāk», skaitļa palielināšanu "
                "un pamazināšanu, divu lielumu salīdzināšanu, situācijas "
                "pierakstu ar darbību un datu lasīšanu tabulā.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro, ko nozīmē «par tik vairāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē «par 3 vairāk»?",
              ["tikpat un vēl 3", "3 reizes vairāk", "tikai 3", "par 3 mazāk"],
              0),
             ("Annai ir 5 lelles, Ievai par 2 vairāk. Cik lelles ir Ievai?",
              ["3", "5", "7", "10"], 2),
             ("Kurš skaitlis ir par 4 lielāks nekā 9?",
              ["5", "12", "13", "14"], 2),
         ]},
        {"sr": "Skaidro, ko nozīmē «par tik mazāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē «par 2 mazāk»?",
              ["tikpat, bet 2 mazāk", "2 reizes mazāk", "tikai 2",
               "par 2 vairāk"], 0),
             ("Jānim ir 8 mašīnītes, Pēterim par 3 mazāk. Cik ir Pēterim?",
              ["3", "5", "8", "11"], 1),
             ("Kurš skaitlis ir par 6 mazāks nekā 14?",
              ["6", "7", "8", "20"], 2),
         ]},
        {"sr": "Aprēķina, par cik viens skaitlis lielāks nekā otrs",
         "stunda": TEMATS,
         "jautajumi": [
             ("Par cik 12 ir lielāks nekā 7?", ["4", "5", "6", "19"], 1),
             ("Par cik 6 ir mazāks nekā 15?", ["8", "9", "10", "21"], 1),
             ("Kā aprēķina, par cik viens skaitlis lielāks nekā otrs?",
              ["no lielākā atņem mazāko", "skaitļus saskaita",
               "no mazākā atņem lielāko", "skaitļus salīdzina ar 10"], 0),
         ]},
        {"sr": "Palielina skaitli par doto skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Palielini skaitli 7 par 5!", ["2", "11", "12", "13"], 2),
             ("Palielini skaitli 9 par 8!", ["16", "17", "18", "19"], 1),
             ("Kuru darbību lieto, ja skaitli palielina?",
              ["saskaitīšanu", "atņemšanu", "salīdzināšanu",
               "sakārtošanu"], 0),
         ]},
        {"sr": "Pamazina skaitli par doto skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pamazini skaitli 13 par 4!", ["8", "9", "10", "17"], 1),
             ("Pamazini skaitli 16 par 9!", ["6", "7", "8", "25"], 1),
             ("Kuru darbību lieto, ja skaitli pamazina?",
              ["saskaitīšanu", "atņemšanu", "sakārtošanu",
               "salīdzināšanu"], 1),
         ]},
        {"sr": "Nosaka skaitli, ja zināms, ka tas ir par tik lielāks",
         "stunda": TEMATS,
         "jautajumi": [
             ("Skaitlis ir par 5 lielāks nekā 8. Kurš tas ir?",
              ["3", "12", "13", "14"], 2),
             ("Skaitlis ir par 7 lielāks nekā 6. Kurš tas ir?",
              ["11", "12", "13", "14"], 2),
             ("Skaitlis ir par 9 lielāks nekā 9. Kurš tas ir?",
              ["9", "17", "18", "19"], 2),
         ]},
        {"sr": "Nosaka skaitli, ja zināms, ka tas ir par tik mazāks",
         "stunda": TEMATS,
         "jautajumi": [
             ("Skaitlis ir par 4 mazāks nekā 11. Kurš tas ir?",
              ["6", "7", "8", "15"], 1),
             ("Skaitlis ir par 8 mazāks nekā 17. Kurš tas ir?",
              ["8", "9", "10", "25"], 1),
             ("Skaitlis ir par 6 mazāks nekā 6. Kurš tas ir?",
              ["0", "1", "6", "12"], 0),
         ]},
        {"sr": "Pieraksta situāciju ar vienādību, nezināmo apzīmējot",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kastē bija daži āboli, pielika 4, kopā 12. Kā to pieraksta?",
              ["? + 4 = 12", "? − 4 = 12", "12 + 4 = ?", "4 − ? = 12"], 0),
             ("Bija 9 baloni, daži pārplīsa, palika 5. Kā to pieraksta?",
              ["9 + ? = 5", "9 − ? = 5", "? − 9 = 5", "5 − 9 = ?"], 1),
             ("Ko liek nezināmā skaitļa vietā?",
              ["simbolu, piemēram, «?»", "nulli", "vienu", "neko"], 0),
         ]},
        {"sr": "Attēlo situāciju shematiskā zīmējumā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko shematiskā zīmējumā parāda divas dažāda garuma "
              "sloksnītes?",
              ["ka viens lielums ir lielāks nekā otrs", "ka abi ir vienādi",
               "cik kopā", "kāda ir krāsa"], 0),
             ("Kāpēc pirms aprēķina der uzzīmēt shēmu?",
              ["lai labāk saprastu situāciju", "lai darbs būtu garāks",
               "lai nevajadzētu rēķināt", "lai nezīmētu atbildi"], 0),
             ("Sloksnīte A ir par 3 rūtiņām garāka nekā B. B ir 5 rūtiņas. "
              "Cik gara ir A?",
              ["2", "7", "8", "15"], 2),
         ]},
        {"sr": "Risina salīdzināšanas uzdevumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Klasē ir 9 meitenes un 6 zēni. Par cik meiteņu ir vairāk?",
              ["2", "3", "4", "15"], 1),
             ("Uz galda 7 sarkani un 12 zili klucīši. Par cik zilo ir "
              "vairāk?",
              ["4", "5", "6", "19"], 1),
             ("Vanagam 14 gadi, pūcei 8. Par cik pūce ir jaunāka?",
              ["4", "5", "6", "22"], 2),
         ]},
        {"sr": "Salīdzina summu vai starpību ar skaitli bez precīza aprēķina",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura zīme jāliek:  7 + 8 …… 14?", [">", "<", "=", "+"], 0),
             ("Kura zīme jāliek:  12 − 5 …… 8?", [">", "<", "=", "−"], 1),
             ("Kura zīme jāliek:  6 + 6 …… 12?", [">", "<", "=", "+"], 2),
         ]},
        {"sr": "Lasa datus tabulā un veido jautājumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: Anna 7 uzlīmes, Ilze 10 uzlīmes. Par cik Ilzei ir "
              "vairāk?",
              ["2", "3", "4", "17"], 1),
             ("Tabulā: pirmdienā 5 lietus dienas stundas, otrdienā 3. Cik "
              "kopā?",
              ["2", "7", "8", "9"], 2),
             ("Stabiņu diagrammā zilais stabiņš ir augstāks nekā sarkanais. "
              "Ko tas nozīmē?",
              ["zilo ir vairāk", "sarkano ir vairāk", "abu ir tikpat",
               "nevar zināt"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 1.6. temata noslēgumā. "
                "Pārbauda izpratni par «par tik vairāk» un «par tik mazāk», "
                "skaitļa palielināšanu un pamazināšanu, salīdzināšanas "
                "uzdevuma risināšanu ar shematisku zīmējumu un datu lasīšanu "
                "tabulā.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Uzdevumu tekstu lasa skolotājs. Zīmē un raksti tam atvēlētajā "
              "vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Skaidro «par tik vairāk» un «par tik mazāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē «par 5 vairāk»?",
              ["tikpat un vēl 5", "5 reizes vairāk", "tikai 5",
               "par 5 mazāk"], 0),
             ("Ko nozīmē «par 3 mazāk»?",
              ["tikpat, bet 3 mazāk", "3 reizes mazāk", "tikai 3",
               "par 3 vairāk"], 0),
             ("Kuru darbību lieto, ja skaitli palielina par 4?",
              ["saskaitīšanu", "atņemšanu", "salīdzināšanu",
               "sakārtošanu"], 0),
         ]},
        {"sr": "Palielina un pamazina skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Palielini 8 par 6!", ["12", "13", "14", "15"], 2),
             ("Pamazini 15 par 7!", ["7", "8", "9", "22"], 1),
             ("Palielini 9 par 9!", ["17", "18", "19", "81"], 1),
         ]},
        {"sr": "Aprēķina, par cik lielāks vai mazāks",
         "stunda": TEMATS,
         "jautajumi": [
             ("Par cik 13 ir lielāks nekā 6?", ["6", "7", "8", "19"], 1),
             ("Par cik 5 ir mazāks nekā 11?", ["5", "6", "7", "16"], 1),
             ("Kā aprēķina, par cik viens skaitlis lielāks nekā otrs?",
              ["no lielākā atņem mazāko", "skaitļus saskaita",
               "skaitļus salīdzina ar nulli", "no mazākā atņem lielāko"], 0),
         ]},
        {"sr": "Nosaka skaitli pēc salīdzinājuma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Skaitlis ir par 7 lielāks nekā 8. Kurš tas ir?",
              ["1", "14", "15", "16"], 2),
             ("Skaitlis ir par 5 mazāks nekā 12. Kurš tas ir?",
              ["6", "7", "8", "17"], 1),
             ("Skaitlis ir par 10 lielāks nekā 6. Kurš tas ir?",
              ["4", "15", "16", "60"], 2),
         ]},
        {"sr": "Pieraksta situāciju ar vienādību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Bija daži zīmuļi, pielika 5, kopā 13. Kā to pieraksta?",
              ["? + 5 = 13", "? − 5 = 13", "13 + 5 = ?", "5 − ? = 13"], 0),
             ("Bija 16 ogas, dažas apēda, palika 9. Kā to pieraksta?",
              ["16 + ? = 9", "16 − ? = 9", "? − 16 = 9", "9 − 16 = ?"], 1),
             ("Ar ko pieraksta nezināmo skaitli?",
              ["ar simbolu, piemēram, «?»", "ar nulli", "ar burtu «a»",
               "ar zīmi «=»"], 0),
         ]},
        {"sr": "Lasa datus tabulā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: Kārlim 6 uzlīmes, Ilzei 11. Par cik Ilzei vairāk?",
              ["4", "5", "6", "17"], 1),
             ("Tabulā: pirmdienā 8 grāmatas, otrdienā 5. Cik kopā?",
              ["3", "12", "13", "14"], 2),
             ("Diagrammā zaļais stabiņš ir zemāks nekā dzeltenais. Ko tas "
              "nozīmē?",
              ["zaļo ir mazāk", "zaļo ir vairāk", "abu ir tikpat",
               "nevar zināt"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Palielina un pamazina skaitli par doto skaitli",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitlis 7, palielināts par 6, ir ……", "13"),
                         ("Skaitlis 14, pamazināts par 5, ir ……", "9"),
                         ("Par cik 15 ir lielāks nekā 8?  ……", "7"),
                         ("Par cik 4 ir mazāks nekā 12?  ……", "8")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitlis 9, palielināts par 8, ir ……", "17"),
                         ("Skaitlis 16, pamazināts par 7, ir ……", "9"),
                         ("Par cik 13 ir lielāks nekā 5?  ……", "8"),
                         ("Par cik 6 ir mazāks nekā 14?  ……", "8")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Skaitlis 8, palielināts par 9, ir ……", "17"),
                         ("Skaitlis 17, pamazināts par 8, ir ……", "9"),
                         ("Par cik 11 ir lielāks nekā 3?  ……", "8"),
                         ("Par cik 7 ir mazāks nekā 15?  ……", "8")]},
         ]},
        {"sr": "Salīdzina summu vai starpību ar skaitli",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp izteiksmi un skaitli ieraksti pareizo zīmi! Par "
                      "katru pareizu zīmi — 1 punkts.",
              "rindas": [("8 + 7  ……  14", ">"), ("13 − 6  ……  8", "<"),
                         ("9 + 5  ……  14", "=")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp izteiksmi un skaitli ieraksti pareizo zīmi! Par "
                      "katru pareizu zīmi — 1 punkts.",
              "rindas": [("6 + 6  ……  13", "<"), ("15 − 7  ……  7", ">"),
                         ("10 + 8  ……  18", "=")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp izteiksmi un skaitli ieraksti pareizo zīmi! Par "
                      "katru pareizu zīmi — 1 punkts.",
              "rindas": [("9 + 9  ……  17", ">"), ("12 − 8  ……  5", "<"),
                         ("7 + 6  ……  13", "=")]},
         ]},
        {"sr": "Attēlo salīdzinājumu shematiskā zīmējumā un aprēķina",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzlīmes", "vieta": 6.5,
              "ievads": "Annai ir 6 uzlīmes, bet Ilzei par 5 vairāk.",
              "jaut": [("Uzzīmē abām meitenēm pa sloksnītei no rūtiņām!", 1),
                       ("Pieraksti aprēķinu, cik uzlīmju ir Ilzei!", 1),
                       ("Aprēķini to!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Divas sloksnītes: 6 rūtiņas un 11 rūtiņas.   "
                           "(1 p.)",
                           "2) 6 + 5   (1 p.)", "3) 6 + 5 = 11   (1 p.)",
                           "4) Atbilde: Ilzei ir 11 uzlīmes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Klucīši", "vieta": 6.5,
              "ievads": "Jānim ir 13 klucīši, bet Pēterim par 4 mazāk.",
              "jaut": [("Uzzīmē abiem zēniem pa sloksnītei no rūtiņām!", 1),
                       ("Pieraksti aprēķinu, cik klucīšu ir Pēterim!", 1),
                       ("Aprēķini to!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Divas sloksnītes: 13 rūtiņas un 9 rūtiņas.   "
                           "(1 p.)",
                           "2) 13 − 4   (1 p.)", "3) 13 − 4 = 9   (1 p.)",
                           "4) Atbilde: Pēterim ir 9 klucīši.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Ogas", "vieta": 6.5,
              "ievads": "Pirmajā groziņā ir 8 ogas, otrajā 15 ogas.",
              "jaut": [("Uzzīmē abiem groziņiem pa sloksnītei no rūtiņām!",
                        1),
                       ("Pieraksti aprēķinu, par cik otrajā ir vairāk!", 1),
                       ("Aprēķini to!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) Divas sloksnītes: 8 rūtiņas un 15 rūtiņas.   "
                           "(1 p.)",
                           "2) 15 − 8   (1 p.)", "3) 15 − 8 = 7   (1 p.)",
                           "4) Atbilde: otrajā groziņā ir par 7 ogām "
                           "vairāk.   (1 p.)"]},
         ]},
        {"sr": "Lasa datus un veido jautājumu par tiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Dati par grāmatām", "vieta": 5.5,
              "ievads": "Anna izlasīja 9 grāmatas, Kārlis — 5 grāmatas.",
              "jaut": [("Aprēķini, cik grāmatu izlasīja kopā!", 1),
                       ("Aprēķini, par cik vairāk izlasīja Anna!", 1),
                       ("Uzraksti vēl vienu jautājumu par šiem datiem!", 1)],
              "atbildes": ["1) 9 + 5 = 14 grāmatas.   (1 p.)",
                           "2) 9 − 5 = 4 grāmatas.   (1 p.)",
                           "3) Uzrakstīts jēdzīgs jautājums, piemēram: «Cik "
                           "grāmatu Kārlim vēl jāizlasa, lai būtu tikpat?»   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Dati par ziediem", "vieta": 5.5,
              "ievads": "Dārzā uzziedēja 12 tulpes un 7 narcises.",
              "jaut": [("Aprēķini, cik ziedu ir kopā!", 1),
                       ("Aprēķini, par cik tulpju ir vairāk!", 1),
                       ("Uzraksti vēl vienu jautājumu par šiem datiem!", 1)],
              "atbildes": ["1) 12 + 7 = 19 ziedi.   (1 p.)",
                           "2) 12 − 7 = 5 ziedi.   (1 p.)",
                           "3) Uzrakstīts jēdzīgs jautājums, piemēram: «Cik "
                           "narcišu vēl jāiestāda, lai būtu tikpat, cik "
                           "tulpju?»   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dati par braucieniem",
              "vieta": 5.5,
              "ievads": "Pirmdienā autobusā iekāpa 8 bērni, otrdienā — 14.",
              "jaut": [("Aprēķini, cik bērnu iekāpa abās dienās kopā!", 1),
                       ("Aprēķini, par cik otrdienā bija vairāk!", 1),
                       ("Uzraksti vēl vienu jautājumu par šiem datiem!", 1)],
              "atbildes": ["1) 8 + 14 = 22 bērni.   (1 p.)",
                           "2) 14 − 8 = 6 bērni.   (1 p.)",
                           "3) Uzrakstīts jēdzīgs jautājums, piemēram: «Kurā "
                           "dienā brauca vairāk bērnu?»   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
