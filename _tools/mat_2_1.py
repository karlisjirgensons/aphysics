# -*- coding: utf-8 -*-
"""Matemātika, 2. klase. 2.1. Kā grupē objektus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 2. klase, 2.1. temats): objektu kopīgās
un atšķirīgās īpašības, grupēšana pēc kopīgas pazīmes, grupas pazīmes
nosaukšana, objekta piederības pārbaude, Venna diagramma, informācijas
lasīšana tabulā un diagrammā.
"""

PRIEKSMETS = "Matemātika  |  2. klase"
TEMATS = "2.1."
NOSAUKUMS = "Kā grupē objektus?"

ATGADNE = [
    "Grupēt nozīmē vienā grupā apvienot tos objektus, kuriem ir kopīga "
    "pazīme.",
    "Salīdzināt nozīmē saskatīt kopīgo un atšķirīgo.",
    "Venna diagrammā divi riņķi pārklājas: pārklājumā liek objektus, kuriem "
    "piemīt abas pazīmes.",
]

FD = {
    "veids": "fd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 2.1. temata beigās. Pārbauda objektu "
                "kopīgo un atšķirīgo īpašību noteikšanu, grupēšanu pēc "
                "pazīmes, grupas pazīmes nosaukšanu, piederības pārbaudi, "
                "Venna diagrammas lasīšanu un datu lasīšanu tabulā.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro, ko nozīmē grupēt objektus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē grupēt objektus?",
              ["apvienot tos ar kopīgu pazīmi", "tos saskaitīt", "tos izmērīt",
               "tos nokrāsot"], 0),
             ("Kas jādara, pirms objektus sagrupē?",
              ["tie jāsalīdzina", "tie jāizmēra", "tie jāpaslēpj",
               "tie jāsaskaita"], 0),
             ("Ko nozīmē salīdzināt?",
              ["saskatīt kopīgo un atšķirīgo", "saskaitīt objektus",
               "objektus sadalīt", "uzzīmēt objektus"], 0),
         ]},
        {"sr": "Nosauc objektu kopīgās īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas kopīgs skaitļiem 12, 24 un 36?",
              ["tie ir pāra skaitļi", "tie ir nepāra skaitļi",
               "tie ir mazāki nekā 10", "tie ir viencipara"], 0),
             ("Kas kopīgs kvadrātam un taisnstūrim?",
              ["4 malas", "3 malas", "nav virsotņu", "vienāda krāsa"], 0),
             ("Kas kopīgs skaitļiem 20, 50 un 80?",
              ["tie ir pilni desmiti", "tie ir nepāra", "tie ir viencipara",
               "tie ir lielāki nekā 100"], 0),
         ]},
        {"sr": "Nosauc objektu atšķirīgās īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko atšķiras kvadrāts un trijstūris?",
              ["malu skaits", "krāsa", "lielums", "novietojums"], 0),
             ("Ar ko atšķiras skaitļi 7 un 70?",
              ["ciparu skaits", "abi ir pāra", "abi ir nepāra",
               "tie neatšķiras"], 0),
             ("Ar ko atšķiras 5 cm un 5 kg?",
              ["mērvienība", "skaitlis", "krāsa", "nekas"], 0),
         ]},
        {"sr": "Nosauc grupas kopīgo pazīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grupā: 2, 4, 6, 8. Kāda ir kopīgā pazīme?",
              ["pāra skaitļi", "nepāra skaitļi", "divciparu skaitļi",
               "pilni desmiti"], 0),
             ("Grupā: 11, 13, 15. Kāda ir kopīgā pazīme?",
              ["nepāra skaitļi", "pāra skaitļi", "pilni desmiti",
               "viencipara skaitļi"], 0),
             ("Grupā: trijstūris, četrstūris, piecstūris. Kāda ir pazīme?",
              ["daudzstūri", "riņķi", "telpiskas figūras", "līnijas"], 0),
         ]},
        {"sr": "Pārbauda objekta piederību grupai",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grupā ir pāra skaitļi. Kurš skaitlis tajā NEDERĒS?",
              ["14", "20", "36", "27"], 3),
             ("Grupā ir divciparu skaitļi. Kurš skaitlis tajā NEDERĒS?",
              ["19", "45", "7", "88"], 2),
             ("Grupā ir figūras ar 4 malām. Kura figūra tajā NEDERĒS?",
              ["kvadrāts", "taisnstūris", "trijstūris", "četrstūris"], 2),
         ]},
        {"sr": "Grupē skaitļus pēc dotas pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis der grupai «pāra skaitļi»?",
              ["15", "21", "34", "47"], 2),
             ("Kurš skaitlis der grupai «pilni desmiti»?",
              ["25", "40", "51", "73"], 1),
             ("Kurš skaitlis der grupai «lielāks nekā 50»?",
              ["12", "38", "50", "64"], 3),
         ]},
        {"sr": "Grupē figūras pēc dotas pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura figūra der grupai «figūras bez virsotnēm»?",
              ["riņķis", "kvadrāts", "trijstūris", "piecstūris"], 0),
             ("Kura figūra der grupai «figūras ar 3 malām»?",
              ["trijstūris", "kvadrāts", "riņķis", "sešstūris"], 0),
             ("Kura figūra der grupai «telpiskas figūras»?",
              ["kubs", "kvadrāts", "trijstūris", "riņķis"], 0),
         ]},
        {"sr": "Lasa Venna diagrammu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko liek Venna diagrammas pārklājumā?",
              ["objektus ar abām pazīmēm", "objektus bez pazīmēm",
               "visus objektus", "tikai skaitļus"], 0),
             ("Venna diagrammā: «pāra skaitļi» un «lielāki nekā 10». Kurš "
              "skaitlis ir pārklājumā?",
              ["4", "9", "12", "15"], 2),
             ("Venna diagrammā: «pāra» un «pilni desmiti». Kurš skaitlis ir "
              "pārklājumā?",
              ["25", "30", "33", "41"], 1),
         ]},
        {"sr": "Grupē objektus pēc divām pazīmēm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir gan pāra, gan lielāks nekā 20?",
              ["18", "21", "24", "35"], 2),
             ("Kura figūra ir gan četrstūris, gan ar vienādām malām?",
              ["kvadrāts", "trijstūris", "riņķis", "piecstūris"], 0),
             ("Kurš skaitlis ir gan nepāra, gan mazāks nekā 10?",
              ["4", "7", "12", "15"], 1),
         ]},
        {"sr": "Lasa datus tabulā par grupām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: sarkani 7, zili 5 klucīši. Cik klucīšu ir kopā?",
              ["2", "10", "12", "75"], 2),
             ("Tabulā: meitenes 12, zēni 9. Par cik meiteņu vairāk?",
              ["2", "3", "4", "21"], 1),
             ("Tabulā: pirmdien 8, otrdien 8 grāmatas. Ko var teikt?",
              ["abās dienās tikpat", "pirmdien vairāk", "otrdien vairāk",
               "nevar zināt"], 0),
         ]},
        {"sr": "Lasa stabiņu diagrammu par grupām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Diagrammā augstākais stabiņš nozīmē, ka …",
              ["tajā grupā ir visvairāk", "tajā grupā ir vismazāk",
               "grupas ir vienādas", "nav datu"], 0),
             ("Diagrammā zilais stabiņš ir 6, sarkanais 4. Par cik zilo "
              "vairāk?",
              ["2", "4", "6", "10"], 0),
             ("Kāpēc datus attēlo diagrammā?",
              ["lai tos būtu viegli salīdzināt", "lai aizņemtu vietu",
               "lai nevajadzētu skaitīt", "lai būtu krāsaini"], 0),
         ]},
        {"sr": "Izvēlas pazīmi, pēc kuras sagrupēt",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pēc kuras pazīmes var sagrupēt skaitļus?",
              ["pāra un nepāra", "pēc krāsas", "pēc garšas", "pēc svara"], 0),
             ("Pēc kuras pazīmes var sagrupēt figūras?",
              ["pēc malu skaita", "pēc skaņas", "pēc garšas",
               "pēc temperatūras"], 0),
             ("Vai vienus un tos pašus objektus var grupēt dažādi?",
              ["jā, pēc dažādām pazīmēm", "nē, tikai vienā veidā",
               "jā, bet tikai pēc krāsas", "nē, tas ir aizliegts"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 2.1. temata noslēgumā. "
                "Pārbauda objektu salīdzināšanu, grupēšanu pēc pazīmes, "
                "grupas pazīmes nosaukšanu, piederības pārbaudi, Venna "
                "diagrammas aizpildīšanu un datu lasīšanu tabulā.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Atbildi raksti un zīmē tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Skaidro grupēšanu un salīdzināšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē grupēt?",
              ["apvienot objektus ar kopīgu pazīmi", "tos saskaitīt",
               "tos izmērīt", "tos nokrāsot"], 0),
             ("Ko nozīmē salīdzināt?",
              ["saskatīt kopīgo un atšķirīgo", "saskaitīt", "izmērīt",
               "sadalīt"], 0),
             ("Vai vienus objektus var grupēt vairākos veidos?",
              ["jā", "nē", "tikai skaitļus", "tikai figūras"], 0),
         ]},
        {"sr": "Nosaka kopīgo pazīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grupā: 10, 20, 30. Kāda ir pazīme?",
              ["pilni desmiti", "nepāra skaitļi", "viencipara skaitļi",
               "lielāki nekā 100"], 0),
             ("Grupā: 3, 5, 7. Kāda ir pazīme?",
              ["nepāra skaitļi", "pāra skaitļi", "divciparu skaitļi",
               "pilni desmiti"], 0),
             ("Grupā: kvadrāts, taisnstūris. Kāda ir pazīme?",
              ["4 malas", "3 malas", "nav malu", "telpiskas figūras"], 0),
         ]},
        {"sr": "Pārbauda piederību grupai",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grupā ir pāra skaitļi. Kurš NEDERĒS?",
              ["16", "24", "31", "48"], 2),
             ("Grupā ir divciparu skaitļi. Kurš NEDERĒS?",
              ["23", "9", "56", "90"], 1),
             ("Grupā ir daudzstūri. Kurš objekts NEDERĒS?",
              ["trijstūris", "kvadrāts", "riņķis", "piecstūris"], 2),
         ]},
        {"sr": "Grupē pēc divām pazīmēm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir gan pāra, gan lielāks nekā 30?",
              ["28", "31", "42", "55"], 2),
             ("Kurš skaitlis ir gan nepāra, gan mazāks nekā 20?",
              ["12", "17", "22", "31"], 1),
             ("Kura figūra ir gan četrstūris, gan ar vienādām malām?",
              ["kvadrāts", "trijstūris", "riņķis", "sešstūris"], 0),
         ]},
        {"sr": "Lasa Venna diagrammu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko liek Venna diagrammas pārklājumā?",
              ["objektus ar abām pazīmēm", "visus objektus",
               "objektus bez pazīmēm", "tikai figūras"], 0),
             ("Riņķi «pāra» un «lielāki nekā 20». Kurš ir pārklājumā?",
              ["18", "21", "26", "35"], 2),
             ("Riņķi «nepāra» un «pilni desmiti». Kurš skaitlis ir "
              "pārklājumā?",
              ["neviens", "20", "35", "40"], 0),
         ]},
        {"sr": "Lasa datus tabulā un diagrammā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: sarkani 9, zili 6. Cik kopā?", ["3", "15", "16", "96"],
              1),
             ("Tabulā: zēni 11, meitenes 14. Par cik meiteņu vairāk?",
              ["2", "3", "4", "25"], 1),
             ("Diagrammā augstākais stabiņš rāda, ka …",
              ["tajā grupā ir visvairāk", "tajā grupā ir vismazāk",
               "grupas vienādas", "nav datu"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Nosaka grupas kopīgo pazīmi",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Uzraksti grupas kopīgo pazīmi",
              "note": "Ieraksti, kas visiem grupas objektiem ir kopīgs! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("2, 8, 14, 30  →  ……", "pāra skaitļi"),
                         ("10, 40, 70  →  ……", "pilni desmiti"),
                         ("trijstūris, kvadrāts, piecstūris  →  ……",
                          "daudzstūri"),
                         ("5, 15, 25  →  ……", "nepāra skaitļi")]},
             {"tips": "parveide", "virs": "Uzraksti grupas kopīgo pazīmi",
              "note": "Ieraksti, kas visiem grupas objektiem ir kopīgs! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("3, 9, 21, 45  →  ……", "nepāra skaitļi"),
                         ("20, 50, 90  →  ……", "pilni desmiti"),
                         ("kvadrāts, taisnstūris  →  ……", "četrstūri"),
                         ("4, 16, 28  →  ……", "pāra skaitļi")]},
             {"tips": "parveide", "virs": "Uzraksti grupas kopīgo pazīmi",
              "note": "Ieraksti, kas visiem grupas objektiem ir kopīgs! Par "
                      "katru pareizu atbildi — 1 punkts.",
              "rindas": [("11, 12, 13, 14  →  ……", "divciparu skaitļi"),
                         ("6, 12, 18  →  ……", "pāra skaitļi"),
                         ("kubs, bumba  →  ……", "telpiskas figūras"),
                         ("30, 60, 90  →  ……", "pilni desmiti")]},
         ]},
        {"sr": "Atrod grupai nepiederošo objektu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Uzraksti lieko objektu",
              "note": "Ieraksti to objektu, kas grupā neiederas! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("4, 10, 15, 22  →  ……", "15"),
                         ("kvadrāts, riņķis, taisnstūris  →  ……", "riņķis"),
                         ("20, 30, 35, 40  →  ……", "35")]},
             {"tips": "parveide", "virs": "Uzraksti lieko objektu",
              "note": "Ieraksti to objektu, kas grupā neiederas! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("3, 7, 8, 11  →  ……", "8"),
                         ("trijstūris, kvadrāts, kubs  →  ……", "kubs"),
                         ("50, 60, 65, 70  →  ……", "65")]},
             {"tips": "parveide", "virs": "Uzraksti lieko objektu",
              "note": "Ieraksti to objektu, kas grupā neiederas! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("12, 24, 33, 46  →  ……", "33"),
                         ("cm, dm, kg  →  ……", "kg"),
                         ("5, 15, 25, 26  →  ……", "26")]},
         ]},
        {"sr": "Aizpilda Venna diagrammu pēc divām pazīmēm",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Venna diagramma", "vieta": 6.5,
              "ievads": "Dotie skaitļi:  4,  9,  12,  20,  25,  30. "
                        "Pazīmes: «pāra skaitļi» un «pilni desmiti».",
              "jaut": [("Uzzīmē divus riņķus, kas pārklājas!", 1),
                       ("Ieraksti pārklājumā tos skaitļus, kuriem ir abas "
                        "pazīmes!", 1),
                       ("Ieraksti pārējos skaitļus pareizajā vietā!", 1),
                       ("Uzraksti, cik skaitļu ir pārklājumā!", 1)],
              "atbildes": [
                  "1) Uzzīmēti divi pārklājušies riņķi ar nosaukumiem.   "
                  "(1 p.)",
                  "2) Pārklājumā: 20 un 30.   (1 p.)",
                  "3) Tikai «pāra»: 4 un 12; ārpus riņķiem: 9 un 25.   "
                  "(1 p.)",
                  "4) Atbilde: 2 skaitļi.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Venna diagramma", "vieta": 6.5,
              "ievads": "Dotie skaitļi:  5,  8,  15,  16,  40,  45. "
                        "Pazīmes: «nepāra skaitļi» un «lielāki nekā 10».",
              "jaut": [("Uzzīmē divus riņķus, kas pārklājas!", 1),
                       ("Ieraksti pārklājumā tos skaitļus, kuriem ir abas "
                        "pazīmes!", 1),
                       ("Ieraksti pārējos skaitļus pareizajā vietā!", 1),
                       ("Uzraksti, cik skaitļu ir pārklājumā!", 1)],
              "atbildes": [
                  "1) Uzzīmēti divi pārklājušies riņķi ar nosaukumiem.   "
                  "(1 p.)",
                  "2) Pārklājumā: 15 un 45.   (1 p.)",
                  "3) Tikai «nepāra»: 5; tikai «lielāki nekā 10»: 16 un 40; "
                  "ārpusē: 8.   (1 p.)",
                  "4) Atbilde: 2 skaitļi.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Venna diagramma", "vieta": 6.5,
              "ievads": "Dotie skaitļi:  6,  11,  18,  22,  35,  60. "
                        "Pazīmes: «pāra skaitļi» un «lielāki nekā 20».",
              "jaut": [("Uzzīmē divus riņķus, kas pārklājas!", 1),
                       ("Ieraksti pārklājumā tos skaitļus, kuriem ir abas "
                        "pazīmes!", 1),
                       ("Ieraksti pārējos skaitļus pareizajā vietā!", 1),
                       ("Uzraksti, cik skaitļu ir pārklājumā!", 1)],
              "atbildes": [
                  "1) Uzzīmēti divi pārklājušies riņķi ar nosaukumiem.   "
                  "(1 p.)",
                  "2) Pārklājumā: 22 un 60.   (1 p.)",
                  "3) Tikai «pāra»: 6 un 18; tikai «lielāki nekā 20»: 35; "
                  "ārpusē: 11.   (1 p.)",
                  "4) Atbilde: 2 skaitļi.   (1 p.)"]},
         ]},
        {"sr": "Lasa un salīdzina datus tabulā",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Dati par klucīšiem", "vieta": 5.5,
              "ievads": "Tabulā: sarkani — 12, zili — 8, dzelteni — 5.",
              "jaut": [("Aprēķini, cik klucīšu ir kopā!", 1),
                       ("Aprēķini, par cik sarkano ir vairāk nekā zilo!", 1),
                       ("Uzraksti, kurā grupā ir vismazāk!", 1)],
              "atbildes": ["1) 12 + 8 + 5 = 25   (1 p.)",
                           "2) 12 − 8 = 4   (1 p.)",
                           "3) Atbilde: dzelteno (5).   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dati par grāmatām", "vieta": 5.5,
              "ievads": "Tabulā: pasakas — 9, dzejoļi — 6, stāsti — 14.",
              "jaut": [("Aprēķini, cik grāmatu ir kopā!", 1),
                       ("Aprēķini, par cik stāstu ir vairāk nekā dzejoļu!",
                        1),
                       ("Uzraksti, kurā grupā ir visvairāk!", 1)],
              "atbildes": ["1) 9 + 6 + 14 = 29   (1 p.)",
                           "2) 14 − 6 = 8   (1 p.)",
                           "3) Atbilde: stāsti (14).   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dati par ziediem", "vieta": 5.5,
              "ievads": "Tabulā: tulpes — 15, narcises — 10, krokusi — 7.",
              "jaut": [("Aprēķini, cik ziedu ir kopā!", 1),
                       ("Aprēķini, par cik tulpju ir vairāk nekā krokusu!",
                        1),
                       ("Uzraksti, kurā grupā ir vismazāk!", 1)],
              "atbildes": ["1) 15 + 10 + 7 = 32   (1 p.)",
                           "2) 15 − 7 = 8   (1 p.)",
                           "3) Atbilde: krokusi (7).   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
