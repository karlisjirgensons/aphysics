# -*- coding: utf-8 -*-
"""Matemātika, 2. klase. 2.5. Kā rodas izteiksme?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 2. klase, 2.5. temats): izteiksme un tās
vērtība, divu darbību izteiksmes un darbību secība, iekavas, vienādība un
nevienādība (patiesa vai aplama), nezināmā skaitļa noteikšana, situācijas
pieraksts ar izteiksmi, algoritma soļi un nosacījums.
"""

PRIEKSMETS = "Matemātika  |  2. klase"
TEMATS = "2.5."
NOSAUKUMS = "Kā rodas izteiksme?"

ATGADNE = [
    "Izteiksme:  25 + 13 − 8   ·   izteiksmes vērtība ir tās aprēķina "
    "rezultāts",
    "Darbības izpilda pēc kārtas no kreisās puses; iekavās esošo — vispirms.",
    "Vienādība:  40 + 5 = 45   ·   nevienādība:  40 + 5 > 42   ·   tās var "
    "būt patiesas vai aplamas",
]

FD = {
    "veids": "fd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 2.5. temata beigās. Pārbauda izteiksmes "
                "un tās vērtības jēdzienu, darbību secību, iekavu nozīmi, "
                "vienādības un nevienādības patiesumu, nezināmā skaitļa "
                "noteikšanu un situācijas pierakstu ar izteiksmi.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, kas ir izteiksme un tās vērtība",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir izteiksmes vērtība?",
              ["aprēķina rezultāts", "lielākais skaitlis", "darbību skaits",
               "iekavu skaits"], 0),
             ("Kurš pieraksts ir izteiksme?",
              ["25 + 13 − 8", "25 = 25", "25 > 13", "25"], 0),
             ("Kurš pieraksts NAV izteiksme?",
              ["30 + 12 = 42", "30 + 12", "30 − 12 + 5", "12 + 5"], 0),
         ]},
        {"sr": "Aprēķina divu darbību izteiksmes vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 25 + 13 − 8?", ["20", "30", "38", "46"], 1),
             ("Cik ir 40 − 15 + 20?", ["5", "35", "45", "75"], 2),
             ("Cik ir 18 + 22 − 15?", ["15", "25", "35", "55"], 1),
         ]},
        {"sr": "Ievēro darbību secību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādā secībā izpilda darbības izteiksmē 30 − 10 + 5?",
              ["no kreisās puses pēc kārtas", "vispirms saskaitīšanu",
               "vispirms lielāko skaitli", "vienalga kādā"], 0),
             ("Cik ir 50 − 20 + 10?", ["20", "30", "40", "80"], 2),
             ("Skolēns aprēķināja 50 − 20 + 10 = 20. Kur ir kļūda?",
              ["vispirms saskaitīja", "vispirms atņēma", "sajauca skaitļus",
               "kļūdas nav"], 0),
         ]},
        {"sr": "Skaidro iekavu nozīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpēc izteiksmē lieto iekavas?",
              ["lai parādītu, kura darbība vispirms", "lai būtu skaistāk",
               "lai izteiksme būtu garāka", "lai nebūtu jārēķina"], 0),
             ("Cik ir 50 − (20 + 10)?", ["20", "30", "40", "80"], 0),
             ("Cik ir (35 + 15) − 20?", ["10", "20", "30", "70"], 2),
         ]},
        {"sr": "Salīdzina izteiksmes ar vienu un to pašu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 60 − (20 + 15)?", ["25", "35", "55", "95"], 0),
             ("Cik ir 60 − 20 + 15?", ["25", "35", "55", "95"], 2),
             ("Kāpēc 60 − (20 + 15) un 60 − 20 + 15 vērtības atšķiras?",
              ["iekavas maina darbību secību", "skaitļi ir dažādi",
               "viena izteiksme ir aplama", "tās neatšķiras"], 0),
         ]},
        {"sr": "Veido izteiksmi no dotajiem skaitļiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("No skaitļiem 20, 30 un 10 izveido izteiksmi ar vērtību 40. "
              "Kura tā ir?",
              ["20 + 30 − 10", "20 + 30 + 10", "30 − 20 + 10",
               "30 − 20 − 10"], 0),
             ("Kura izteiksme ar skaitļiem 50, 15 un 5 dod 30?",
              ["50 − 15 − 5", "50 − 15 + 5", "50 + 15 − 5",
               "50 + 15 + 5"], 0),
             ("Kura izteiksme dod vislielāko vērtību?",
              ["20 + 30", "20 − 30", "30 − 20", "20 + 3"], 0),
         ]},
        {"sr": "Nosaka, vai vienādība ir patiesa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura vienādība ir patiesa?",
              ["25 + 15 = 40", "25 + 15 = 30", "25 + 15 = 45",
               "25 + 15 = 35"], 0),
             ("Vienādība 70 − 30 = 50 ir …",
              ["patiesa", "aplama", "nezināma", "nav vienādība"], 1),
             ("Kura vienādība ir aplama?",
              ["18 + 12 = 30", "45 − 15 = 30", "20 + 10 = 30",
               "50 − 25 = 30"], 3),
         ]},
        {"sr": "Nosaka, vai nevienādība ir patiesa",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura nevienādība ir patiesa?",
              ["30 + 10 > 35", "30 + 10 < 35", "30 + 10 > 45",
               "30 + 10 < 40"], 0),
             ("Nevienādība 60 − 20 < 50 ir …",
              ["patiesa", "aplama", "nezināma", "nav nevienādība"], 0),
             ("Kura zīme jāliek:  25 + 25 …… 45?", [">", "<", "=", "+"], 0),
         ]},
        {"sr": "Nosaka nezināmo skaitli vienādībā",
         "stunda": TEMATS,
         "jautajumi": [
             ("25 + …… = 60  Kurš skaitlis jāieraksta?",
              ["25", "35", "45", "85"], 1),
             ("…… − 18 = 42  Kurš skaitlis jāieraksta?",
              ["24", "50", "60", "70"], 2),
             ("(…… + 10) = 45  Kurš skaitlis jāieraksta?",
              ["25", "35", "45", "55"], 1),
         ]},
        {"sr": "Pieraksta situāciju ar izteiksmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Bija 40 €, nopelnīja 15 €, iztērēja 20 €. Kura izteiksme "
              "der?",
              ["40 + 15 − 20", "40 − 15 + 20", "40 + 15 + 20",
               "40 − 15 − 20"], 0),
             ("Plauktā 25 grāmatas, paņēma 8, pielika 12. Kura izteiksme "
              "der?",
              ["25 − 8 + 12", "25 + 8 − 12", "25 + 8 + 12",
               "25 − 8 − 12"], 0),
             ("Autobusā 30 cilvēki, izkāpa 12, iekāpa 9. Cik brauc tālāk?",
              ["21", "27", "33", "51"], 1),
         ]},
        {"sr": "Izdomā situāciju dotai izteiksmei",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura situācija atbilst izteiksmei 50 − 20?",
              ["bija 50 €, iztērēja 20 €", "bija 50 €, nopelnīja 20 €",
               "bija 20 €, nopelnīja 50 €", "bija 50 € un 20 €"], 0),
             ("Kura situācija atbilst izteiksmei 15 + 25?",
              ["bija 15 un pienāca vēl 25", "bija 15, aizgāja 25",
               "bija 25, aizgāja 15", "bija 15 un 25 palika"], 0),
             ("Kura situācija atbilst izteiksmei 60 − 10 − 10?",
              ["divas reizes iztērēja pa 10", "divas reizes nopelnīja 10",
               "nopelnīja 20", "iztērēja 60"], 0),
         ]},
        {"sr": "Lasa un izpilda algoritmu ar nosacījumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Algoritms: «ja skaitlis ir pāra, dali ar 2, citādi pieskaiti "
              "1». Kas sanāk ar 8?",
              ["4", "9", "16", "8"], 0),
             ("Tas pats algoritms ar 7. Kas sanāk?", ["3", "7", "8", "14"], 2),
             ("Kas algoritmā nosaka, kuru soli izpildīt?",
              ["nosacījums", "krāsa", "soļu skaits", "atbilde"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 2.5. temata noslēgumā. "
                "Pārbauda izteiksmes vērtības aprēķinu, darbību secību un "
                "iekavas, vienādību un nevienādību patiesumu, nezināmā "
                "skaitļa noteikšanu un situācijas pierakstu ar izteiksmi.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina izteiksmes jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir izteiksmes vērtība?",
              ["aprēķina rezultāts", "lielākais skaitlis", "darbību skaits",
               "iekavu skaits"], 0),
             ("Kurš pieraksts ir izteiksme?",
              ["18 + 12 − 5", "18 + 12 = 30", "18 > 12", "18"], 0),
             ("Kāpēc lieto iekavas?",
              ["lai parādītu darbību secību", "lai būtu skaistāk",
               "lai izteiksme būtu garāka", "lai nerēķinātu"], 0),
         ]},
        {"sr": "Aprēķina izteiksmes vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 35 + 25 − 10?", ["40", "50", "60", "70"], 1),
             ("Cik ir 80 − 30 + 15?", ["35", "50", "65", "95"], 2),
             ("Cik ir 45 − 15 − 10?", ["20", "25", "30", "40"], 0),
         ]},
        {"sr": "Ievēro iekavas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 70 − (30 + 20)?", ["20", "40", "60", "120"], 0),
             ("Cik ir (40 + 20) − 25?", ["35", "45", "55", "85"], 0),
             ("Cik ir 90 − (40 − 10)?", ["40", "50", "60", "120"], 2),
         ]},
        {"sr": "Nosaka vienādības un nevienādības patiesumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura vienādība ir patiesa?",
              ["30 + 25 = 55", "30 + 25 = 45", "30 + 25 = 65",
               "30 + 25 = 50"], 0),
             ("Nevienādība 40 + 20 > 55 ir …",
              ["patiesa", "aplama", "nezināma", "nav nevienādība"], 0),
             ("Kura zīme jāliek:  50 − 20 …… 35?", [">", "<", "=", "+"], 1),
         ]},
        {"sr": "Nosaka nezināmo skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("30 + …… = 75", ["35", "45", "55", "105"], 1),
             ("…… − 25 = 40", ["15", "55", "65", "75"], 2),
             ("(…… + 15) = 60", ["35", "45", "55", "75"], 1),
         ]},
        {"sr": "Pieraksta situāciju ar izteiksmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Bija 60 €, iztērēja 25 €, nopelnīja 10 €. Kura izteiksme "
              "der?",
              ["60 − 25 + 10", "60 + 25 − 10", "60 − 25 − 10",
               "60 + 25 + 10"], 0),
             ("Kura situācija atbilst izteiksmei 45 − 20?",
              ["bija 45, aizgāja 20", "bija 45, pienāca 20",
               "bija 20, pienāca 45", "bija 45 un 20"], 0),
             ("Autobusā 40 cilvēki, izkāpa 15, iekāpa 8. Cik brauc tālāk?",
              ["23", "33", "47", "63"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina izteiksmju vērtības, ievērojot darbību secību",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Ieraksti izteiksmes vērtību! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("25 + 35 − 20 = ……", "40"),
                         ("80 − (30 + 25) = ……", "25"),
                         ("(45 + 15) − 30 = ……", "30"),
                         ("60 − 20 − 15 = ……", "25")]},
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Ieraksti izteiksmes vērtību! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("40 + 25 − 15 = ……", "50"),
                         ("90 − (20 + 30) = ……", "40"),
                         ("(35 + 25) − 40 = ……", "20"),
                         ("70 − 25 − 10 = ……", "35")]},
             {"tips": "parveide", "virs": "Aprēķini izteiksmes vērtību",
              "note": "Ieraksti izteiksmes vērtību! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("55 + 15 − 30 = ……", "40"),
                         ("100 − (40 + 25) = ……", "35"),
                         ("(50 + 20) − 45 = ……", "25"),
                         ("85 − 30 − 20 = ……", "35")]},
         ]},
        {"sr": "Nosaka, vai vienādība vai nevienādība ir patiesa",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Uzraksti «patiesa» vai «aplama»",
              "note": "Ieraksti, vai pieraksts ir patiess vai aplams! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("35 + 15 = 50  →  ……", "patiesa"),
                         ("70 − 20 < 40  →  ……", "aplama"),
                         ("25 + 25 > 45  →  ……", "patiesa")]},
             {"tips": "parveide", "virs": "Uzraksti «patiesa» vai «aplama»",
              "note": "Ieraksti, vai pieraksts ir patiess vai aplams! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("40 + 30 = 60  →  ……", "aplama"),
                         ("90 − 40 > 45  →  ……", "patiesa"),
                         ("15 + 15 < 35  →  ……", "patiesa")]},
             {"tips": "parveide", "virs": "Uzraksti «patiesa» vai «aplama»",
              "note": "Ieraksti, vai pieraksts ir patiess vai aplams! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("50 − 25 = 25  →  ……", "patiesa"),
                         ("20 + 40 < 55  →  ……", "aplama"),
                         ("80 − 30 > 60  →  ……", "aplama")]},
         ]},
        {"sr": "Veido izteiksmi situācijai un aprēķina tās vērtību",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par naudu", "vieta": 6.0,
              "ievads": "Kārlim bija 50 €. Viņš nopelnīja vēl 15 € un "
                        "iztērēja 20 €.",
              "jaut": [("Pieraksti situāciju ar vienu izteiksmi!", 1),
                       ("Aprēķini tās vērtību!", 1),
                       ("Pieraksti to pašu pa darbībām!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 50 + 15 − 20   (1 p.)",
                           "2) 50 + 15 − 20 = 45   (1 p.)",
                           "3) 1) 50 + 15 = 65;  2) 65 − 20 = 45   (1 p.)",
                           "4) Atbilde: Kārlim palika 45 €.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par grāmatām",
              "vieta": 6.0,
              "ievads": "Plauktā bija 35 grāmatas. Paņēma 12 un pielika "
                        "vēl 20.",
              "jaut": [("Pieraksti situāciju ar vienu izteiksmi!", 1),
                       ("Aprēķini tās vērtību!", 1),
                       ("Pieraksti to pašu pa darbībām!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 35 − 12 + 20   (1 p.)",
                           "2) 35 − 12 + 20 = 43   (1 p.)",
                           "3) 1) 35 − 12 = 23;  2) 23 + 20 = 43   (1 p.)",
                           "4) Atbilde: plauktā ir 43 grāmatas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par pasažieriem",
              "vieta": 6.0,
              "ievads": "Autobusā brauca 45 pasažieri. Izkāpa 18, iekāpa 12.",
              "jaut": [("Pieraksti situāciju ar vienu izteiksmi!", 1),
                       ("Aprēķini tās vērtību!", 1),
                       ("Pieraksti to pašu pa darbībām!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 45 − 18 + 12   (1 p.)",
                           "2) 45 − 18 + 12 = 39   (1 p.)",
                           "3) 1) 45 − 18 = 27;  2) 27 + 12 = 39   (1 p.)",
                           "4) Atbilde: tālāk brauc 39 pasažieri.   (1 p.)"]},
         ]},
        {"sr": "Nosaka nezināmo skaitli un pārbauda to",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Nezināmais skaitlis", "vieta": 5.5,
              "ievads": "Vienādība:  ? + 27 = 63",
              "jaut": [("Uzraksti, kā atrast nezināmo skaitli!", 1),
                       ("Aprēķini to!", 1),
                       ("Pārbaudi savu atbildi!", 1)],
              "atbildes": ["1) No summas atņem zināmo saskaitāmo: 63 − 27.   "
                           "(1 p.)",
                           "2) 63 − 27 = 36   (1 p.)",
                           "3) Pārbaude: 36 + 27 = 63.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Nezināmais skaitlis", "vieta": 5.5,
              "ievads": "Vienādība:  ? − 18 = 45",
              "jaut": [("Uzraksti, kā atrast nezināmo skaitli!", 1),
                       ("Aprēķini to!", 1),
                       ("Pārbaudi savu atbildi!", 1)],
              "atbildes": ["1) Starpībai pieskaita atņemamo: 45 + 18.   "
                           "(1 p.)",
                           "2) 45 + 18 = 63   (1 p.)",
                           "3) Pārbaude: 63 − 18 = 45.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Nezināmais skaitlis", "vieta": 5.5,
              "ievads": "Vienādība:  72 − ? = 39",
              "jaut": [("Uzraksti, kā atrast nezināmo skaitli!", 1),
                       ("Aprēķini to!", 1),
                       ("Pārbaudi savu atbildi!", 1)],
              "atbildes": ["1) No mazināmā atņem starpību: 72 − 39.   (1 p.)",
                           "2) 72 − 39 = 33   (1 p.)",
                           "3) Pārbaude: 72 − 33 = 39.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
