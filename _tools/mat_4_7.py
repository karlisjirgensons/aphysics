# -*- coding: utf-8 -*-
"""Matemātika, 4. klase. 4.7. Kā nosaka dažādu figūru laukumu?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 4. klase, 4.7. temats): laukuma vienība
un laukuma jēdziens, vienlielas figūras, taisnstūra laukums kā blakus malu
garumu reizinājums, malas garuma aprēķināšana pēc laukuma, kombinētas
figūras laukums kā taisnstūru laukumu summa vai starpība un taisnleņķa
trijstūra laukums rūtiņu lapā.
"""

PRIEKSMETS = "Matemātika  |  4. klase"
TEMATS = "4.7."
NOSAUKUMS = "Kā nosaka dažādu figūru laukumu?"

ATGADNE = [
    "Laukuma vienība 1 cm² ir kvadrāts ar malu 1 cm   ·   taisnstūra "
    "laukums   S = a · b   ·   perimetrs   P = a + b + a + b",
    "Nezināmo malu atrod, laukumu dalot ar zināmo malu:   a = S : b",
    "1 dm² = 100 cm²   ·   1 m² = 100 dm²   ·   kombinētu figūru sadala "
    "taisnstūros un laukumus saskaita vai atņem",
]

FD = {
    "veids": "fd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 4.7. temata beigās. Pārbauda laukuma "
                "jēdzienu un mērvienības, taisnstūra un kvadrāta laukumu, "
                "malas noteikšanu pēc laukuma, vienlielas figūras, "
                "kombinētas figūras laukumu un laukumu rūtiņu lapā.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina laukuma jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda figūras laukums?",
              ["cik vienību noklāj figūru", "cik gara ir mala",
               "cik ir virsotņu", "cik ir leņķu"], 0),
             ("Kas ir laukuma vienība 1 cm²?",
              ["kvadrāts ar malu 1 cm", "nogrieznis 1 cm",
               "riņķis ar rādiusu 1 cm", "taisne"], 0),
             ("Ar ko mēra laukumu?",
              ["ar laukuma vienībām", "ar centimetriem", "ar gramiem",
               "ar minūtēm"], 0),
         ]},
        {"sr": "Zina laukuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir laukuma mērvienība?", ["m²", "m", "kg", "min"], 0),
             ("Cik cm² ir 1 dm²?", ["100", "10", "1000", "1"], 0),
             ("Cik dm² ir 1 m²?", ["100", "10", "1000", "1"], 0),
         ]},
        {"sr": "Aprēķina taisnstūra laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina taisnstūra laukumu?",
              ["sareizina blakus malas", "saskaita visas malas",
               "sareizina visas malas", "dala malas"], 0),
             ("Taisnstūra malas ir 5 cm un 4 cm. Cik liels ir laukums?",
              ["20 cm²", "9 cm²", "18 cm²", "20 cm"], 0),
             ("Taisnstūra malas ir 8 cm un 3 cm. Cik liels ir laukums?",
              ["24 cm²", "11 cm²", "22 cm²", "24 cm"], 0),
         ]},
        {"sr": "Aprēķina kvadrāta laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kvadrāta mala ir 6 cm. Cik liels ir laukums?",
              ["36 cm²", "24 cm²", "12 cm²", "6 cm²"], 0),
             ("Kvadrāta laukums ir 49 cm². Cik gara ir mala?",
              ["7 cm", "49 cm", "24 cm", "14 cm"], 0),
             ("Kā aprēķina kvadrāta laukumu?",
              ["malu reizina ar sevi", "malu reizina ar 4",
               "malu saskaita ar sevi", "malu dala ar 4"], 0),
         ]},
        {"sr": "Nosaka malu pēc laukuma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Laukums ir 24 cm², viena mala — 6 cm. Cik gara ir otra?",
              ["4 cm", "18 cm", "30 cm", "12 cm"], 0),
             ("Laukums ir 45 cm², viena mala — 9 cm. Cik gara ir otra?",
              ["5 cm", "36 cm", "54 cm", "9 cm"], 0),
             ("Kā atrod nezināmo malu?",
              ["laukumu dala ar zināmo malu", "laukumu reizina ar malu",
               "malas saskaita", "malu dala ar laukumu"], 0),
         ]},
        {"sr": "Atšķir laukumu no perimetra",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda perimetrs?",
              ["visu malu garumu summu", "cik vienību noklāj figūru",
               "figūras platumu", "virsotņu skaitu"], 0),
             ("Taisnstūra malas ir 5 cm un 3 cm. Cik liels ir perimetrs?",
              ["16 cm", "15 cm", "8 cm", "15 cm²"], 0),
             ("Kurā mērvienībā izsaka laukumu?", ["cm²", "cm", "cm³", "kg"],
              0),
         ]},
        {"sr": "Zina, kas ir vienlielas figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas figūras ir vienlielas?",
              ["ar vienādu laukumu", "ar vienādu formu",
               "ar vienādu perimetru", "ar vienādu virsotņu skaitu"], 0),
             ("Vai divas dažādas formas figūras var būt vienlielas?",
              ["jā", "nē", "tikai kvadrāti", "tikai taisnstūri"], 0),
             ("Figūru sadalīja daļās un salika citādi. Kas notiek ar "
              "laukumu?",
              ["nemainās", "palielinās", "samazinās", "kļūst nulle"], 0),
         ]},
        {"sr": "Aprēķina kombinētas figūras laukumu kā summu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina kombinētas figūras laukumu?",
              ["sadala taisnstūros", "saskaita malas", "reizina malas",
               "mēra ar lineālu"], 0),
             ("Figūru veido taisnstūri 12 cm² un 8 cm². Cik liels ir "
              "laukums?", ["20 cm²", "4 cm²", "96 cm²", "20 cm"], 0),
             ("Kāpēc figūru sadala taisnstūros?",
              ["to laukumu prot aprēķināt", "tā ir skaistāk",
               "lai būtu vairāk figūru", "tā nedara"], 0),
         ]},
        {"sr": "Aprēķina kombinētas figūras laukumu kā starpību",
         "stunda": TEMATS,
         "jautajumi": [
             ("No taisnstūra 30 cm² izgriezts kvadrāts 9 cm². Cik liels ir "
              "atlikums?", ["21 cm²", "39 cm²", "270 cm²", "3 cm²"], 0),
             ("Kad laukumus atņem?",
              ["kad no figūras kaut kas ir izgriezts", "vienmēr", "nekad",
               "kad figūra ir liela"], 0),
             ("Istaba ir 20 m², paklājs — 6 m². Cik m² grīdas nav nosegti?",
              ["14 m²", "26 m²", "120 m²", "6 m²"], 0),
         ]},
        {"sr": "Nosaka taisnleņķa trijstūra laukumu rūtiņās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūrī ir 12 rūtiņas. Cik rūtiņu ir tā puse?",
              ["6", "12", "24", "3"], 0),
             ("Kā rūtiņās nosaka trijstūra laukumu?",
              ["ņem pusi no taisnstūra", "saskaita malas",
               "reizina visas malas", "mēra ar lineālu"], 0),
             ("Trijstūra malas rūtiņās ir 4 un 6 rūtiņas. Cik rūtiņu ir "
              "laukums?", ["12", "24", "10", "5"], 0),
         ]},
        {"sr": "Pārveido laukuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik cm² ir 3 dm²?", ["300", "30", "3000", "3"], 0),
             ("Cik dm² ir 2 m²?", ["200", "20", "2000", "2"], 0),
             ("Kura laukuma mērvienība ir vislielākā?",
              ["m²", "dm²", "cm²", "mm²"], 0),
         ]},
        {"sr": "Risina praktiskus uzdevumus par laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Istaba ir 5 m × 4 m. Cik liels ir grīdas laukums?",
              ["20 m²", "9 m²", "18 m²", "20 m"], 0),
             ("Cik flīžu, kas katra ir 1 m², vajag 20 m² grīdai?",
              ["20", "10", "40", "2"], 0),
             ("Dobe ir 6 m × 3 m. Cik liels ir tās laukums?",
              ["18 m²", "9 m²", "18 m", "36 m²"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 4.7. temata noslēgumā. "
                "Pārbauda laukuma mērvienības, taisnstūra un kvadrāta "
                "laukumu, malas noteikšanu pēc laukuma, laukuma un "
                "perimetra atšķiršanu un kombinētas figūras laukumu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus un zīmējumus veido tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina laukuma jēdzienu un mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir laukuma mērvienība?", ["dm²", "dm", "kg", "s"], 0),
             ("Cik cm² ir 1 dm²?", ["100", "10", "1000", "1"], 0),
             ("Ko rāda figūras laukums?",
              ["cik laukuma vienību noklāj figūru", "cik gara ir mala",
               "cik virsotņu ir", "cik leņķu ir"], 0),
         ]},
        {"sr": "Aprēķina taisnstūra un kvadrāta laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūra malas ir 7 cm un 4 cm. Cik liels ir laukums?",
              ["28 cm²", "11 cm²", "22 cm²", "28 cm"], 0),
             ("Kvadrāta mala ir 9 cm. Cik liels ir laukums?",
              ["81 cm²", "36 cm²", "18 cm²", "9 cm²"], 0),
             ("Kā aprēķina taisnstūra laukumu?",
              ["sareizina blakus malas", "saskaita visas malas",
               "sareizina visas malas", "dala malas"], 0),
         ]},
        {"sr": "Nosaka malu pēc laukuma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Laukums ir 36 cm², viena mala — 4 cm. Cik gara ir otra?",
              ["9 cm", "32 cm", "40 cm", "18 cm"], 0),
             ("Kvadrāta laukums ir 64 cm². Cik gara ir mala?",
              ["8 cm", "16 cm", "32 cm", "64 cm"], 0),
             ("Kā atrod nezināmo malu?",
              ["laukumu dala ar zināmo malu", "laukumu reizina",
               "malas saskaita", "malu dala ar laukumu"], 0),
         ]},
        {"sr": "Atšķir laukumu no perimetra",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūra malas ir 6 cm un 2 cm. Cik liels ir perimetrs?",
              ["16 cm", "12 cm", "8 cm", "12 cm²"], 0),
             ("Ko rāda perimetrs?",
              ["visu malu garumu summu", "cik vienību noklāj figūru",
               "figūras augstumu", "virsotņu skaitu"], 0),
             ("Kurā mērvienībā izsaka perimetru?", ["cm", "cm²", "cm³",
                                                    "kg"], 0),
         ]},
        {"sr": "Aprēķina kombinētas figūras laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Figūru veido taisnstūri 15 cm² un 9 cm². Cik liels ir "
              "laukums?", ["24 cm²", "6 cm²", "135 cm²", "24 cm"], 0),
             ("No taisnstūra 40 cm² izgriezts kvadrāts 16 cm². Cik liels ir "
              "atlikums?", ["24 cm²", "56 cm²", "640 cm²", "4 cm²"], 0),
             ("Kā aprēķina kombinētas figūras laukumu?",
              ["sadala taisnstūros", "saskaita malas", "reizina malas",
               "mēra ar transportieri"], 0),
         ]},
        {"sr": "Risina praktiskus uzdevumus par laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Istaba ir 6 m × 3 m. Cik liels ir grīdas laukums?",
              ["18 m²", "9 m²", "18 m", "36 m²"], 0),
             ("Cik flīžu, kas katra ir 1 m², vajag 24 m² grīdai?",
              ["24", "12", "48", "6"], 0),
             ("Taisnstūrī ir 20 rūtiņu. Cik rūtiņu ir tā puse?",
              ["10", "20", "40", "5"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina laukumu, malu un pārveido mērvienības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 5 cm × 4 cm;  S = …… cm²", "20"),
                         ("Kvadrāts ar malu 6 cm;  S = …… cm²", "36"),
                         ("S = 24 cm², mala 6 cm; otra mala ir …… cm", "4"),
                         ("1 dm² = …… cm²", "100")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 8 cm × 3 cm;  S = …… cm²", "24"),
                         ("Kvadrāts ar malu 7 cm;  S = …… cm²", "49"),
                         ("S = 45 cm², mala 9 cm; otra mala ir …… cm", "5"),
                         ("1 m² = …… dm²", "100")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 9 cm × 5 cm;  S = …… cm²", "45"),
                         ("Kvadrāts ar malu 8 cm;  S = …… cm²", "64"),
                         ("S = 36 cm², mala 4 cm; otra mala ir …… cm", "9"),
                         ("3 dm² = …… cm²", "300")]},
         ]},
        {"sr": "Atšķir laukumu no perimetra",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 5 cm × 3 cm;  P = …… cm", "16"),
                         ("Taisnstūris 5 cm × 3 cm;  S = …… cm²", "15"),
                         ("Kvadrāts ar malu 4 cm;  P = …… cm", "16")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 7 cm × 2 cm;  P = …… cm", "18"),
                         ("Taisnstūris 7 cm × 2 cm;  S = …… cm²", "14"),
                         ("Kvadrāts ar malu 5 cm;  P = …… cm", "20")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 6 cm × 4 cm;  P = …… cm", "20"),
                         ("Taisnstūris 6 cm × 4 cm;  S = …… cm²", "24"),
                         ("Kvadrāts ar malu 3 cm;  P = …… cm", "12")]},
         ]},
        {"sr": "Risina praktisku uzdevumu par laukumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Istaba ir 6 m gara un 4 m plata. Uz grīdas noliek "
                        "paklāju 3 m × 2 m. Cik liels ir istabas laukums? "
                        "Cik liels ir paklāja laukums? Cik m² grīdas paliek "
                        "nenosegti? Cik liels ir istabas perimetrs?",
              "kriteriji": ["Istabas laukums 6 · 4 = 24 m².   (1 p.)",
                            "Paklāja laukums 3 · 2 = 6 m².   (1 p.)",
                            "Nenosegti 24 − 6 = 18 m².   (1 p.)",
                            "Perimetrs 6 + 4 + 6 + 4 = 20 m.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Dobe ir 8 m gara un 3 m plata. Kopā ar celiņu ap "
                        "to laukums ir 40 m². Cik liels ir dobes laukums? "
                        "Cik liels ir celiņa laukums? Cik liels ir dobes "
                        "perimetrs? Cik metru žoga vajag dobei?",
              "kriteriji": ["Dobes laukums 8 · 3 = 24 m².   (1 p.)",
                            "Celiņa laukums 40 − 24 = 16 m².   (1 p.)",
                            "Perimetrs 8 + 3 + 8 + 3 = 22 m.   (1 p.)",
                            "Žoga vajag 22 m.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Figūru veido divi taisnstūri: 5 cm × 4 cm un "
                        "3 cm × 2 cm. Cik liels ir katra taisnstūra "
                        "laukums? Cik liels ir visas figūras laukums? Par "
                        "cik cm² taisnstūru laukumi atšķiras?",
              "kriteriji": ["Pirmā laukums 5 · 4 = 20 cm².   (1 p.)",
                            "Otrā laukums 3 · 2 = 6 cm².   (1 p.)",
                            "Kopā 20 + 6 = 26 cm².   (1 p.)",
                            "Starpība 20 − 6 = 14 cm².   (1 p.)"]},
         ]},
        {"sr": "Zīmē figūru ar dotu laukumu un pamato",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Figūra ar dotu laukumu",
              "vieta": 5.5,
              "ievads": "Rūtiņās jāuzzīmē figūras, kuru laukums ir 12 "
                        "rūtiņas.",
              "jaut": [("Uzzīmē taisnstūri ar laukumu 12 rūtiņas!", 1),
                       ("Pieraksti tā malu garumus rūtiņās!", 1),
                       ("Uzzīmē citu, vienlielu figūru!", 1)],
              "atbildes": ["1) Uzzīmēts taisnstūris, kurā ir 12 rūtiņas. "
                           "  (1 p.)",
                           "2) Pierakstīti malu garumi, piemēram, 6 un 2. "
                           "  (1 p.)",
                           "3) Uzzīmēta cita figūra, kurā arī ir 12 "
                           "rūtiņas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Laukums un perimetrs",
              "vieta": 5.5,
              "ievads": "Taisnstūra laukums ir 20 cm², bet viena mala — "
                        "5 cm.",
              "jaut": [("Cik gara ir otra mala?", 1),
                       ("Cik liels ir taisnstūra perimetrs?", 1),
                       ("Uzzīmē šo taisnstūri rūtiņās!", 1)],
              "atbildes": ["1) 20 : 5 = 4 cm.   (1 p.)",
                           "2) 5 + 4 + 5 + 4 = 18 cm.   (1 p.)",
                           "3) Uzzīmēts taisnstūris 5 × 4 rūtiņas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Trijstūris rūtiņās", "vieta": 5.5,
              "ievads": "Rūtiņās uzzīmēts taisnstūris 6 × 4 rūtiņas, un tam "
                        "novilkta diagonāle.",
              "jaut": [("Cik rūtiņu ir taisnstūra laukums?", 1),
                       ("Cik rūtiņu ir katra trijstūra laukums?", 1),
                       ("Paskaidro, kāpēc tā ir!", 1)],
              "atbildes": ["1) 6 · 4 = 24 rūtiņas.   (1 p.)",
                           "2) 24 : 2 = 12 rūtiņas.   (1 p.)",
                           "3) Diagonāle sadala taisnstūri divās vienādās "
                           "daļās.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
