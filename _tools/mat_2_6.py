# -*- coding: utf-8 -*-
"""Matemātika, 2. klase. 2.6. Kā veido un raksturo figūras?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 2. klase, 2.6. temats): jaunu figūru
veidošana, savietojot vai sadalot, perimetrs (apkārtmērs) un tā aprēķins,
laukums kā rūtiņu skaits, taisnstūra laukums, cikliska algoritma pieraksts,
telpiskas figūras (taisnstūru skaldnis, piramīda).
"""

PRIEKSMETS = "Matemātika  |  2. klase"
TEMATS = "2.6."
NOSAUKUMS = "Kā veido un raksturo figūras?"

ATGADNE = [
    "Perimetrs ir visu malu garumu summa:  P = a + b + a + b",
    "Laukumu mēra rūtiņās (kvadrātos): laukums ir rūtiņu skaits figūrā.",
    "Taisnstūrim ar malām 4 un 3 rūtiņas:  P = 4 + 3 + 4 + 3 = 14;  "
    "laukums = 12 rūtiņas",
]

FD = {
    "veids": "fd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 2.6. temata beigās. Pārbauda figūru "
                "veidošanu un sadalīšanu, perimetra jēdzienu un aprēķinu, "
                "laukumu rūtiņās, taisnstūra laukumu, cikliska algoritma "
                "izpratni un telpiskas figūras.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Veido jaunas figūras no dotajām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādu figūru var izveidot no diviem vienādiem trijstūriem?",
              ["četrstūri", "riņķi", "piecstūri", "punktu"], 0),
             ("Kā no vienas figūras iegūt divas?",
              ["to sadala", "to nokrāso", "to pagriež", "to izmēra"], 0),
             ("Kādu figūru iegūst, savietojot divus vienādus kvadrātus ar "
              "malu?",
              ["taisnstūri", "trijstūri", "riņķi", "piecstūri"], 0),
         ]},
        {"sr": "Zina, kas ir perimetrs",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir figūras perimetrs?",
              ["visu malu garumu summa", "rūtiņu skaits figūrā",
               "malu skaits", "virsotņu skaits"], 0),
             ("Kā nosaka daudzstūra perimetru?",
              ["izmēra un saskaita visas malas", "saskaita virsotnes",
               "saskaita rūtiņas", "izmēra vienu malu"], 0),
             ("Kurā mērvienībā pieraksta perimetru?",
              ["centimetros", "kvadrātos", "kilogramos", "minūtēs"], 0),
         ]},
        {"sr": "Aprēķina trijstūra un četrstūra perimetru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Trijstūra malas ir 3 cm, 4 cm un 5 cm. Cik liels ir "
              "perimetrs?",
              ["7 cm", "9 cm", "12 cm", "60 cm"], 2),
             ("Četrstūra malas ir 2 cm, 3 cm, 2 cm un 3 cm. Cik liels ir "
              "perimetrs?",
              ["5 cm", "6 cm", "10 cm", "12 cm"], 2),
             ("Trijstūra malas ir 6 cm, 6 cm un 4 cm. Cik liels ir "
              "perimetrs?",
              ["10 cm", "12 cm", "16 cm", "24 cm"], 2),
         ]},
        {"sr": "Aprēķina kvadrāta perimetru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kvadrāta mala ir 5 cm. Cik liels ir perimetrs?",
              ["10 cm", "15 cm", "20 cm", "25 cm"], 2),
             ("Kvadrāta mala ir 3 cm. Cik liels ir perimetrs?",
              ["6 cm", "9 cm", "12 cm", "15 cm"], 2),
             ("Kvadrāta perimetrs ir 16 cm. Cik gara ir viena mala?",
              ["2 cm", "4 cm", "8 cm", "64 cm"], 1),
         ]},
        {"sr": "Aprēķina taisnstūra perimetru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūra malas ir 4 cm un 6 cm. Cik liels ir perimetrs?",
              ["10 cm", "20 cm", "24 cm", "26 cm"], 1),
             ("Taisnstūra malas ir 2 cm un 7 cm. Cik liels ir perimetrs?",
              ["9 cm", "14 cm", "18 cm", "20 cm"], 2),
             ("Taisnstūra malas ir 5 cm un 5 cm. Kā to sauc?",
              ["kvadrāts", "trijstūris", "riņķis", "piecstūris"], 0),
         ]},
        {"sr": "Zina, kas ir laukums",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir figūras laukums?",
              ["rūtiņu skaits figūrā", "malu garumu summa", "malu skaits",
               "virsotņu skaits"], 0),
             ("Ar ko mēra laukumu rūtiņu lapā?",
              ["ar rūtiņām", "ar lineālu", "ar pulksteni", "ar svariem"], 0),
             ("Ar ko perimetrs atšķiras no laukuma?",
              ["perimetrs ir malu garums, laukums — rūtiņu skaits",
               "tie ir viens un tas pats", "laukumu mēra centimetros",
               "perimetru mēra rūtiņās"], 0),
         ]},
        {"sr": "Nosaka figūras laukumu rūtiņās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Figūra aizņem 3 rindas pa 4 rūtiņām. Cik liels ir laukums?",
              ["7 rūtiņas", "10 rūtiņas", "12 rūtiņas", "14 rūtiņas"], 2),
             ("Figūra aizņem 2 rindas pa 5 rūtiņām. Cik liels ir laukums?",
              ["7 rūtiņas", "10 rūtiņas", "12 rūtiņas", "25 rūtiņas"], 1),
             ("Kvadrāts ir 4 rūtiņas plats un 4 augsts. Cik liels ir "
              "laukums?",
              ["8 rūtiņas", "12 rūtiņas", "16 rūtiņas", "20 rūtiņas"], 2),
         ]},
        {"sr": "Salīdzina figūru laukumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienai figūrai 12 rūtiņas, otrai 9. Kurai laukums lielāks?",
              ["pirmajai", "otrajai", "vienādi", "nevar zināt"], 0),
             ("Divām figūrām ir vienāds rūtiņu skaits. Ko var teikt?",
              ["to laukumi ir vienādi", "to perimetri ir vienādi",
               "tās ir vienādas figūras", "tām ir vienāda krāsa"], 0),
             ("Vai figūrām ar vienādu laukumu vienmēr ir vienāds perimetrs?",
              ["nē", "jā", "vienmēr", "tikai kvadrātiem"], 0),
         ]},
        {"sr": "Sadala figūru daļās un veido jaunu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūri sadala divās vienādās daļās. Kādas figūras var "
              "iegūt?",
              ["divus mazākus taisnstūrus", "divus riņķus", "piecstūri",
               "vienu punktu"], 0),
             ("Kvadrātu pārgriež pa diagonāli. Kādas figūras iegūst?",
              ["divus trijstūrus", "divus kvadrātus", "divus riņķus",
               "trīs trijstūrus"], 0),
             ("Cik vienādos kvadrātos var sadalīt taisnstūri 2 × 3 rūtiņas?",
              ["2", "3", "5", "6"], 3),
         ]},
        {"sr": "Lasa un izpilda ciklisku algoritmu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Algoritms: «atkārto 4 reizes: novelc malu, pagriezies». Kāda "
              "figūra sanāk?",
              ["četrstūris", "trijstūris", "riņķis", "līnija"], 0),
             ("Algoritms: «atkārto 3 reizes: novelc 5 cm malu». Kāda figūra?",
              ["trijstūris", "kvadrāts", "piecstūris", "riņķis"], 0),
             ("Ko nozīmē cikls algoritmā?",
              ["soļus atkārto vairākas reizes", "soļus izlaiž",
               "soļus izpilda otrādi", "soļu nav"], 0),
         ]},
        {"sr": "Atpazīst telpiskas figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc telpisku figūru, kuras visas skaldnes ir "
              "taisnstūri?",
              ["taisnstūru skaldnis", "piramīda", "riņķis", "kvadrāts"], 0),
             ("Kura telpiskā figūra beidzas ar vienu virsotni augšā?",
              ["piramīda", "kubs", "taisnstūru skaldnis", "riņķis"], 0),
             ("Cik skaldņu ir kubam?", ["4", "6", "8", "12"], 1),
         ]},
        {"sr": "Risina perimetra uzdevumu sadzīves situācijā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Dārza mala ir taisnstūris 8 m un 5 m. Cik metru žoga vajag?",
              ["13 m", "26 m", "40 m", "80 m"], 1),
             ("Kvadrātveida rāmja mala ir 20 cm. Cik cm lentes vajag apkārt?",
              ["40 cm", "60 cm", "80 cm", "400 cm"], 2),
             ("Ko aprēķina, ja vajag zināt žoga garumu?",
              ["perimetru", "laukumu", "virsotņu skaitu", "augstumu"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 2.6. temata noslēgumā. "
                "Pārbauda perimetra aprēķinu, laukuma noteikšanu rūtiņās, "
                "figūru veidošanu un sadalīšanu, cikliska algoritma "
                "pierakstu un perimetra lietojumu sadzīves uzdevumā.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Zīmē ar lineālu un risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina perimetra un laukuma jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir perimetrs?",
              ["visu malu garumu summa", "rūtiņu skaits", "malu skaits",
               "virsotņu skaits"], 0),
             ("Kas ir laukums?",
              ["rūtiņu skaits figūrā", "malu garumu summa", "malu skaits",
               "figūras krāsa"], 0),
             ("Ko aprēķina, ja vajag zināt žoga garumu?",
              ["perimetru", "laukumu", "augstumu", "virsotnes"], 0),
         ]},
        {"sr": "Aprēķina perimetru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Trijstūra malas 5 cm, 5 cm, 6 cm. Perimetrs?",
              ["11 cm", "15 cm", "16 cm", "150 cm"], 2),
             ("Kvadrāta mala 7 cm. Perimetrs?",
              ["14 cm", "21 cm", "28 cm", "49 cm"], 2),
             ("Taisnstūra malas 3 cm un 8 cm. Perimetrs?",
              ["11 cm", "16 cm", "22 cm", "24 cm"], 2),
         ]},
        {"sr": "Nosaka laukumu rūtiņās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūris 3 rindas pa 5 rūtiņām. Laukums?",
              ["8 rūtiņas", "15 rūtiņas", "16 rūtiņas", "35 rūtiņas"], 1),
             ("Kvadrāts 6 × 6 rūtiņas. Laukums?",
              ["12 rūtiņas", "24 rūtiņas", "36 rūtiņas", "66 rūtiņas"], 2),
             ("Taisnstūris 2 × 9 rūtiņas. Laukums?",
              ["11 rūtiņas", "18 rūtiņas", "22 rūtiņas", "29 rūtiņas"], 1),
         ]},
        {"sr": "Veido un sadala figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kvadrātu pārgriež pa diagonāli. Ko iegūst?",
              ["divus trijstūrus", "divus kvadrātus", "riņķi",
               "piecstūri"], 0),
             ("No diviem vienādiem kvadrātiem izveido …",
              ["taisnstūri", "trijstūri", "riņķi", "piramīdu"], 0),
             ("Cik vienādos kvadrātos sadala taisnstūri 3 × 4 rūtiņas?",
              ["7", "10", "12", "14"], 2),
         ]},
        {"sr": "Izpilda ciklisku algoritmu",
         "stunda": TEMATS,
         "jautajumi": [
             ("«Atkārto 4 reizes: novelc 3 cm malu un pagriezies.» Kāda "
              "figūra?",
              ["kvadrāts", "trijstūris", "piecstūris", "riņķis"], 0),
             ("«Atkārto 3 reizes: novelc malu.» Kāda figūra?",
              ["trijstūris", "četrstūris", "riņķis", "punkts"], 0),
             ("Ko nozīmē cikls?",
              ["soļus atkārto", "soļus izlaiž", "soļus maina vietām",
               "soļu nav"], 0),
         ]},
        {"sr": "Atpazīst telpiskas figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Telpiska figūra ar visām taisnstūra skaldnēm ir …",
              ["taisnstūru skaldnis", "piramīda", "riņķis", "kvadrāts"], 0),
             ("Telpiska figūra ar vienu virsotni augšā ir …",
              ["piramīda", "kubs", "skaldnis", "riņķis"], 0),
             ("Cik skaldņu ir kubam?", ["4", "6", "8", "12"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina daudzstūra perimetru",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini perimetru",
              "note": "Ieraksti perimetru kopā ar mērvienību! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("Kvadrāts ar malu 6 cm:  P = ……", "24 cm"),
                         ("Taisnstūris 4 cm un 7 cm:  P = ……", "22 cm"),
                         ("Trijstūris 3 cm, 4 cm, 5 cm:  P = ……", "12 cm"),
                         ("Kvadrāts ar perimetru 20 cm; mala = ……", "5 cm")]},
             {"tips": "parveide", "virs": "Aprēķini perimetru",
              "note": "Ieraksti perimetru kopā ar mērvienību! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("Kvadrāts ar malu 8 cm:  P = ……", "32 cm"),
                         ("Taisnstūris 5 cm un 9 cm:  P = ……", "28 cm"),
                         ("Trijstūris 6 cm, 6 cm, 7 cm:  P = ……", "19 cm"),
                         ("Kvadrāts ar perimetru 36 cm; mala = ……", "9 cm")]},
             {"tips": "parveide", "virs": "Aprēķini perimetru",
              "note": "Ieraksti perimetru kopā ar mērvienību! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("Kvadrāts ar malu 4 cm:  P = ……", "16 cm"),
                         ("Taisnstūris 3 cm un 10 cm:  P = ……", "26 cm"),
                         ("Trijstūris 8 cm, 5 cm, 5 cm:  P = ……", "18 cm"),
                         ("Kvadrāts ar perimetru 28 cm; mala = ……", "7 cm")]},
         ]},
        {"sr": "Nosaka figūras laukumu rūtiņās",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini laukumu rūtiņās",
              "note": "Ieraksti rūtiņu skaitu! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 4 × 5 rūtiņas:  ……", "20"),
                         ("Kvadrāts 7 × 7 rūtiņas:  ……", "49"),
                         ("Taisnstūris 2 × 8 rūtiņas:  ……", "16")]},
             {"tips": "parveide", "virs": "Aprēķini laukumu rūtiņās",
              "note": "Ieraksti rūtiņu skaitu! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 3 × 6 rūtiņas:  ……", "18"),
                         ("Kvadrāts 5 × 5 rūtiņas:  ……", "25"),
                         ("Taisnstūris 4 × 9 rūtiņas:  ……", "36")]},
             {"tips": "parveide", "virs": "Aprēķini laukumu rūtiņās",
              "note": "Ieraksti rūtiņu skaitu! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 5 × 6 rūtiņas:  ……", "30"),
                         ("Kvadrāts 4 × 4 rūtiņas:  ……", "16"),
                         ("Taisnstūris 3 × 9 rūtiņas:  ……", "27")]},
         ]},
        {"sr": "Zīmē figūru un aprēķina tās perimetru un laukumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Zīmē un aprēķini", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri ar malām 5 un 3 rūtiņas!", 1),
                       ("Aprēķini tā perimetru rūtiņās!", 1),
                       ("Aprēķini tā laukumu rūtiņās!", 1),
                       ("Sadali to divās vienādās daļās!", 1)],
              "atbildes": ["1) Uzzīmēts taisnstūris 5 × 3.   (1 p.)",
                           "2) P = 5 + 3 + 5 + 3 = 16 rūtiņas   (1 p.)",
                           "3) Laukums = 15 rūtiņas   (1 p.)",
                           "4) Novilkta līnija, kas dala to divās vienādās "
                           "daļās.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē un aprēķini", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē kvadrātu ar malu 4 rūtiņas!", 1),
                       ("Aprēķini tā perimetru rūtiņās!", 1),
                       ("Aprēķini tā laukumu rūtiņās!", 1),
                       ("Sadali to četrās vienādās daļās!", 1)],
              "atbildes": ["1) Uzzīmēts kvadrāts 4 × 4.   (1 p.)",
                           "2) P = 4 · 4 = 16 rūtiņas   (1 p.)",
                           "3) Laukums = 16 rūtiņas   (1 p.)",
                           "4) Novilktas divas līnijas, kas dala kvadrātu "
                           "četrās vienādās daļās.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē un aprēķini", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri ar malām 6 un 2 rūtiņas!", 1),
                       ("Aprēķini tā perimetru rūtiņās!", 1),
                       ("Aprēķini tā laukumu rūtiņās!", 1),
                       ("Uzzīmē citu figūru ar tādu pašu laukumu!", 1)],
              "atbildes": ["1) Uzzīmēts taisnstūris 6 × 2.   (1 p.)",
                           "2) P = 6 + 2 + 6 + 2 = 16 rūtiņas   (1 p.)",
                           "3) Laukums = 12 rūtiņas   (1 p.)",
                           "4) Uzzīmēta cita figūra ar 12 rūtiņām, piemēram, "
                           "3 × 4.   (1 p.)"]},
         ]},
        {"sr": "Risina perimetra uzdevumu sadzīves situācijā",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par žogu", "vieta": 5.5,
              "ievads": "Dārzs ir taisnstūris ar malām 9 m un 6 m. Tam apkārt "
                        "liek žogu.",
              "jaut": [("Pieraksti aprēķinu!", 1),
                       ("Aprēķini, cik metru žoga vajag!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) P = 9 + 6 + 9 + 6   (1 p.)",
                           "2) P = 30 m   (1 p.)",
                           "3) Atbilde: vajag 30 m žoga.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par rāmi", "vieta": 5.5,
              "ievads": "Kvadrātveida rāmja mala ir 15 cm. Tam apkārt līmē "
                        "lenti.",
              "jaut": [("Pieraksti aprēķinu!", 1),
                       ("Aprēķini, cik cm lentes vajag!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) P = 15 + 15 + 15 + 15   (1 p.)",
                           "2) P = 60 cm   (1 p.)",
                           "3) Atbilde: vajag 60 cm lentes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par dobi", "vieta": 5.5,
              "ievads": "Dobe ir taisnstūris ar malām 7 m un 4 m. Tai apkārt "
                        "liek apmali.",
              "jaut": [("Pieraksti aprēķinu!", 1),
                       ("Aprēķini, cik metru apmales vajag!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) P = 7 + 4 + 7 + 4   (1 p.)",
                           "2) P = 22 m   (1 p.)",
                           "3) Atbilde: vajag 22 m apmales.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
