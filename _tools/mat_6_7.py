# -*- coding: utf-8 -*-
"""Matemātika, 6. klase. 6.7. Negatīva skaitļa pieskaitīšana un atņemšana.

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 6. klase, 6.7. temats): «+» un «−» kā
darbības un kā skaitļa zīme, saskaitīšana un atņemšana uz skaitļu taisnes,
atņemšana kā pretējā skaitļa pieskaitīšana, skaitļa un tā pretējā skaitļa
summa, divu negatīvu skaitļu summa, pēc moduļa lielāks un mazāks skaitlis,
izteiksmes ar iekavām līdz četrām darbībām un nezināmā noteikšana.
"""

PRIEKSMETS = "Matemātika  |  6. klase"
TEMATS = "6.7."
NOSAUKUMS = "Ko nozīmē skaitlim pieskaitīt negatīvu skaitli, no skaitļa " \
            "atņemt negatīvu skaitli?"

ATGADNE = [
    "Uz skaitļu taisnes:   pieskaitot pozitīvu skaitli, iet pa labi; "
    "pieskaitot negatīvu — pa kreisi. Atņemot ir otrādi.",
    "Atņemt skaitli nozīmē pieskaitīt tā pretējo skaitli:   "
    "a − (−b) = a + b   ·   a + (−b) = a − b   ·   a + (−a) = 0",
    "Divu negatīvu skaitļu summa ir negatīva. Ja zīmes ir dažādas, summas "
    "zīmi nosaka pēc moduļa lielākais skaitlis.",
]

FD = {
    "veids": "fd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 6.7. temata beigās. Pārbauda pozitīvu "
                "un negatīvu skaitļu saskaitīšanu un atņemšanu, atņemšanas "
                "aizstāšanu ar pretējā skaitļa pieskaitīšanu, izteiksmes ar "
                "iekavām un nezināmā noteikšanu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro saskaitīšanu uz skaitļu taisnes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Uz kuru pusi iet, pieskaitot negatīvu skaitli?",
              ["pa kreisi", "pa labi", "uz augšu", "uz leju"], 0),
             ("Uz kuru pusi iet, pieskaitot pozitīvu skaitli?",
              ["pa labi", "pa kreisi", "uz augšu", "uz leju"], 0),
             ("Uz kuru pusi iet, atņemot negatīvu skaitli?",
              ["pa labi", "pa kreisi", "uz augšu", "uz leju"], 0),
         ]},
        {"sr": "Saskaita divus negatīvus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir −4 + (−3)?", ["−7", "7", "−1", "1"], 0),
             ("Cik ir −9 + (−6)?", ["−15", "15", "−3", "3"], 0),
             ("Kāda ir divu negatīvu skaitļu summa?",
              ["vienmēr negatīva", "vienmēr pozitīva", "vienmēr 0",
               "dažāda"], 0),
         ]},
        {"sr": "Saskaita skaitļus ar dažādām zīmēm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir −8 + 5?", ["−3", "3", "−13", "13"], 0),
             ("Cik ir 7 + (−10)?", ["−3", "3", "17", "−17"], 0),
             ("Kas nosaka summas zīmi, ja zīmes ir dažādas?",
              ["pēc moduļa lielākais skaitlis", "pirmais skaitlis",
               "otrais skaitlis", "mazākais skaitlis"], 0),
         ]},
        {"sr": "Lieto pretēju skaitļu summu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 12 + (−12)?", ["0", "24", "−24", "12"], 0),
             ("Cik ir −7 + 7?", ["0", "14", "−14", "7"], 0),
             ("Cik ir skaitļa un tā pretējā skaitļa summa?",
              ["0", "1", "divkāršs skaitlis", "dažāda"], 0),
         ]},
        {"sr": "Atņem pozitīvu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3 − 8?", ["−5", "5", "11", "−11"], 0),
             ("Cik ir −2 − 6?", ["−8", "8", "4", "−4"], 0),
             ("Vai no skaitļa var atņemt lielāku skaitli?",
              ["jā, iznāk negatīvs skaitlis", "nē", "tikai no nulles",
               "tikai veselos skaitļos"], 0),
         ]},
        {"sr": "Atņem negatīvu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 5 − (−3)?", ["8", "2", "−8", "−2"], 0),
             ("Cik ir −4 − (−9)?", ["5", "−13", "13", "−5"], 0),
             ("Ar ko var aizstāt atņemšanu?",
              ["pretējā skaitļa pieskaitīšanu", "reizināšanu",
               "dalīšanu", "moduļa ņemšanu"], 0),
         ]},
        {"sr": "Pārraksta izteiksmi citādi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds a + (−b)?", ["a − b", "a + b", "b − a",
                                          "−a − b"], 0),
             ("Ar ko vienāds a − (−b)?", ["a + b", "a − b", "b − a",
                                          "−a + b"], 0),
             ("Vai saskaitāmos var mainīt vietām?",
              ["jā, summa nemainās", "nē", "tikai pozitīvus",
               "tikai negatīvus"], 0),
         ]},
        {"sr": "Aprēķina izteiksmi ar iekavām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir −5 + (3 − 8)?", ["−10", "0", "10", "−6"], 0),
             ("Cik ir 7 − (−2 + 5)?", ["4", "10", "−4", "0"], 0),
             ("Cik ir (−6 + 4) − (−3)?", ["1", "−5", "−1", "5"], 0),
         ]},
        {"sr": "Aprēķina izteiksmi ar vairākām darbībām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir −3 + 7 − 5 + 2?", ["1", "−1", "17", "−17"], 0),
             ("Cik ir 10 − 15 + 3 − 8?", ["−10", "10", "0", "−4"], 0),
             ("Cik ir −2 − 3 − 4 − 1?", ["−10", "10", "0", "−2"], 0),
         ]},
        {"sr": "Salīdzina skaitļus pēc moduļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir pēc moduļa lielāks?",
              ["−9", "5", "3", "−2"], 0),
             ("Kuri skaitļi ir pēc moduļa vienādi?",
              ["−6 un 6", "−6 un 3", "6 un 3", "0 un 6"], 0),
             ("Kāda zīme ir summai −12 + 5?",
              ["negatīva", "pozitīva", "nulle", "nevar noteikt"], 0),
         ]},
        {"sr": "Nosaka nezināmo",
         "stunda": TEMATS,
         "jautajumi": [
             ("Atrisini:  x + 5 = −2.", ["x = −7", "x = 3", "x = 7",
                                         "x = −3"], 0),
             ("Atrisini:  x − 4 = −9.", ["x = −5", "x = −13", "x = 5",
                                         "x = 13"], 0),
             ("Atrisini:  −3 + x = 8.", ["x = 11", "x = 5", "x = −11",
                                         "x = −5"], 0),
         ]},
        {"sr": "Lieto darbības sadzīves situācijās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Temperatūra no −9 °C pieauga par 14 °C. Kāda tā ir?",
              ["5 °C", "−23 °C", "23 °C", "−5 °C"], 0),
             ("Kontā −30 eiro; iemaksā 18 eiro. Cik ir kontā?",
              ["−12 eiro", "12 eiro", "−48 eiro", "48 eiro"], 0),
             ("Kalnā 1200 m; ieplakā −50 m. Cik liela ir augstumu "
              "starpība?", ["1250 m", "1150 m", "50 m", "1200 m"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 6.7. temata noslēgumā. "
                "Pārbauda pozitīvu un negatīvu skaitļu saskaitīšanu un "
                "atņemšanu, izteiksmes ar iekavām, nezināmā noteikšanu un "
                "darbības sadzīves situācijās.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Saskaita pozitīvus un negatīvus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir −6 + (−5)?", ["−11", "11", "−1", "1"], 0),
             ("Cik ir −12 + 8?", ["−4", "4", "−20", "20"], 0),
             ("Cik ir 9 + (−15)?", ["−6", "6", "24", "−24"], 0),
         ]},
        {"sr": "Atņem pozitīvus un negatīvus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 4 − 11?", ["−7", "7", "15", "−15"], 0),
             ("Cik ir 6 − (−4)?", ["10", "2", "−10", "−2"], 0),
             ("Cik ir −5 − (−8)?", ["3", "−13", "13", "−3"], 0),
         ]},
        {"sr": "Pārraksta izteiksmi citādi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds a − (−b)?",
              ["a + b", "a − b", "b − a", "−a + b"], 0),
             ("Cik ir skaitļa un tā pretējā skaitļa summa?",
              ["0", "1", "divkāršs skaitlis", "dažāda"], 0),
             ("Ar ko var aizstāt atņemšanu?",
              ["pretējā skaitļa pieskaitīšanu", "reizināšanu",
               "dalīšanu", "moduļa ņemšanu"], 0),
         ]},
        {"sr": "Aprēķina izteiksmes ar iekavām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir −7 + (5 − 9)?", ["−11", "−3", "3", "11"], 0),
             ("Cik ir 8 − (−3 + 6)?", ["5", "11", "−5", "17"], 0),
             ("Cik ir (−4 + 9) − (−2)?", ["7", "3", "−7", "−3"], 0),
         ]},
        {"sr": "Aprēķina izteiksmes ar vairākām darbībām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir −8 + 12 − 6 + 4?", ["2", "−2", "30", "−30"], 0),
             ("Cik ir 5 − 13 + 2 − 7?", ["−13", "13", "−3", "3"], 0),
             ("Cik ir −1 − 2 − 3 − 4?", ["−10", "10", "0", "−2"], 0),
         ]},
        {"sr": "Nosaka nezināmo un lieto darbības situācijās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Atrisini:  x + 7 = −3.", ["x = −10", "x = 4", "x = 10",
                                         "x = −4"], 0),
             ("Atrisini:  x − 5 = −12.", ["x = −7", "x = −17", "x = 7",
                                          "x = 17"], 0),
             ("Temperatūra no −11 °C pieauga par 15 °C. Kāda tā ir?",
              ["4 °C", "−26 °C", "26 °C", "−4 °C"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita un atņem pozitīvus un negatīvus skaitļus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("−7 + (−8) = ……", "−15"),
                         ("−14 + 9 = ……", "−5"),
                         ("6 − (−5) = ……", "11"),
                         ("−3 − 9 = ……", "−12")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("−5 + (−12) = ……", "−17"),
                         ("−8 + 20 = ……", "12"),
                         ("4 − (−7) = ……", "11"),
                         ("−6 − 11 = ……", "−17")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("−9 + (−4) = ……", "−13"),
                         ("−17 + 17 = ……", "0"),
                         ("10 − (−3) = ……", "13"),
                         ("−2 − 15 = ……", "−17")]},
         ]},
        {"sr": "Aprēķina izteiksmes ar iekavām",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Izteiksmes",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("−6 + (4 − 11) = ……", "−13"),
                         ("9 − (−5 + 2) = ……", "12"),
                         ("(−8 + 3) − (−7) = ……", "2")]},
             {"tips": "parveide", "virs": "Izteiksmes",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("−4 + (7 − 13) = ……", "−10"),
                         ("12 − (−3 + 8) = ……", "7"),
                         ("(−5 + 9) − (−6) = ……", "10")]},
             {"tips": "parveide", "virs": "Izteiksmes",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("−10 + (6 − 2) = ……", "−6"),
                         ("5 − (−9 + 4) = ……", "10"),
                         ("(−7 + 2) − (−8) = ……", "3")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar negatīviem skaitļiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Temperatūras maiņa", "vieta": 5.6,
              "teksts": "Rītā bija −12 °C; līdz pusdienlaikam temperatūra "
                        "pieauga par 17 °C, vakarā pazeminājās par 9 °C.   "
                        "a) Kāda bija temperatūra pusdienlaikā?   b) Kāda "
                        "bija temperatūra vakarā?   c) Par cik grādiem "
                        "vakars ir siltāks nekā rīts?   d) Uzraksti visu "
                        "aprēķinu kā vienu izteiksmi!",
              "kriteriji": ["a) −12 + 17 = 5 °C.   (1 p.)",
                            "b) 5 − 9 = −4 °C.   (1 p.)",
                            "c) −4 − (−12) = 8 °C.   (1 p.)",
                            "d) −12 + 17 − 9 = −4.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Konta stāvoklis", "vieta": 5.6,
              "teksts": "Kontā bija 40 eiro; tika samaksāti 65 eiro, tad "
                        "iemaksāti 30 eiro.   a) Cik eiro kontā pēc "
                        "maksājuma?   b) Cik eiro kontā beigās?   c) Par "
                        "cik eiro konta stāvoklis mainījās kopumā?   "
                        "d) Uzraksti visu aprēķinu kā vienu izteiksmi!",
              "kriteriji": ["a) 40 − 65 = −25 eiro.   (1 p.)",
                            "b) −25 + 30 = 5 eiro.   (1 p.)",
                            "c) 5 − 40 = −35 eiro.   (1 p.)",
                            "d) 40 − 65 + 30 = 5.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Augstumi", "vieta": 5.6,
              "teksts": "Zemūdene atradās −80 m dziļumā; tā pacēlās par "
                        "45 m, pēc tam nogrima par 30 m.   a) Kādā dziļumā "
                        "tā bija pēc pacelšanās?   b) Kādā dziļumā tā ir "
                        "beigās?   c) Par cik metriem tās dziļums kopumā "
                        "mainījies?   d) Cik metru līdz jūras virsmai vēl "
                        "jāpaceļas?",
              "kriteriji": ["a) −80 + 45 = −35 m.   (1 p.)",
                            "b) −35 − 30 = −65 m.   (1 p.)",
                            "c) −65 − (−80) = 15 m.   (1 p.)",
                            "d) 65 m.   (1 p.)"]},
         ]},
        {"sr": "Skaidro darbības ar negatīviem skaitļiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Atņemšana un pretējie skaitļi",
              "vieta": 4.6,
              "ievads": "Dota izteiksme  7 − (−5).",
              "jaut": [("Pārraksti to kā saskaitīšanu!", 1),
                       ("Aprēķini vērtību!", 1),
                       ("Paskaidro, kāpēc rezultāts ir lielāks nekā 7!",
                        1)],
              "atbildes": ["1) 7 + 5.   (1 p.)", "2) 12.   (1 p.)",
                           "3) Atņemot negatīvu skaitli, uz skaitļu taisnes "
                           "iet pa labi.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Summas zīme", "vieta": 4.6,
              "ievads": "Dotas summas  −9 + 4  un  −4 + 9.",
              "jaut": [("Aprēķini abas summas!", 1),
                       ("Kāpēc zīmes ir dažādas?", 1),
                       ("Kad divu skaitļu summa ir 0?", 1)],
              "atbildes": ["1) −5 un 5.   (1 p.)",
                           "2) Zīmi nosaka pēc moduļa lielākais skaitlis. "
                           "  (1 p.)",
                           "3) Ja skaitļi ir pretēji.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Nezināmais", "vieta": 4.6,
              "ievads": "Dots vienādojums  x − 6 = −10.",
              "jaut": [("Atrisini vienādojumu!", 1),
                       ("Pārbaudi atrisinājumu!", 1),
                       ("Paskaidro, kā rīkojies!", 1)],
              "atbildes": ["1) x = −4.   (1 p.)",
                           "2) −4 − 6 = −10 — pareizi.   (1 p.)",
                           "3) Abām pusēm pieskaita 6.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
