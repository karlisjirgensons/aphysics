# -*- coding: utf-8 -*-
"""Matemātika, 3. klase. 3.5. Kādi lielumi raksturo figūru?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 3. klase, 3.5. temats): leņķi (taisns,
šaurs, plats), laukums ar nosacītu mēru un taisnstūra laukuma aprēķins,
vienādas un vienlielas figūras, riņķa rādiuss, tilpums litros un mililitros,
taisnstūru skaldņa tilpums kubos.
"""

PRIEKSMETS = "Matemātika  |  3. klase"
TEMATS = "3.5."
NOSAUKUMS = "Kādi lielumi raksturo figūru?"

ATGADNE = [
    "Leņķi:  taisns (kā lapas stūris)  ·  šaurs (mazāks nekā taisns)  ·  "
    "plats (lielāks nekā taisns)",
    "Taisnstūra laukums = rūtiņu skaits rindā · rindu skaits   ·   "
    "S = a · b",
    "Tilpumu mēra litros (l) un mililitros (ml);  1 l = 1000 ml   ·   "
    "riņķa lielumu nosaka rādiuss",
]

FD = {
    "veids": "fd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 3.5. temata beigās. Pārbauda leņķu "
                "veidus, laukuma noteikšanu rūtiņās un taisnstūra laukuma "
                "aprēķinu, vienādu un vienlielu figūru atšķirību, riņķa "
                "rādiusu, tilpuma mērvienības un skaldņa tilpumu kubos.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Atpazīst taisnu leņķi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds leņķis ir lapas stūrī?",
              ["taisns", "šaurs", "plats", "nav leņķa"], 0),
             ("Cik taisnu leņķu ir taisnstūrim?", ["2", "3", "4", "6"], 2),
             ("Ar ko pārbauda, vai leņķis ir taisns?",
              ["ar lapas stūri vai lineāla stūri", "ar pulksteni",
               "ar svariem", "ar mērtrauku"], 0),
         ]},
        {"sr": "Atšķir šauru un platu leņķi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir leņķis, kas mazāks nekā taisns?",
              ["šaurs", "plats", "taisns", "nav leņķis"], 0),
             ("Kāds ir leņķis, kas lielāks nekā taisns?",
              ["plats", "šaurs", "taisns", "nav leņķis"], 0),
             ("Kādi leņķi ir kvadrātam?",
              ["visi taisni", "visi šauri", "visi plati", "dažādi"], 0),
         ]},
        {"sr": "Skaidro, ka figūrām ar vienādām malām var atšķirties leņķi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai četrstūriem ar vienādām malām vienmēr ir vienādi leņķi?",
              ["nē", "jā", "vienmēr", "tikai trijstūriem"], 0),
             ("Kvadrātam un rombam malas ir vienādas. Ar ko tie atšķiras?",
              ["ar leņķiem", "ar malu skaitu", "ar virsotņu skaitu",
               "ar krāsu"], 0),
             ("Kas obligāti jāzina, lai figūru uzzīmētu pareizi?",
              ["malu garumi un leņķi", "tikai krāsa", "tikai lielums",
               "tikai nosaukums"], 0),
         ]},
        {"sr": "Nosaka laukumu ar rūtiņām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā nosaka figūras laukumu rūtiņu lapā?",
              ["saskaita rūtiņas figūrā", "saskaita malas",
               "izmēra perimetru", "saskaita virsotnes"], 0),
             ("Figūra aizņem 18 rūtiņas. Cik liels ir tās laukums?",
              ["18 rūtiņas", "9 rūtiņas", "36 rūtiņas", "4 rūtiņas"], 0),
             ("Ar ko laukums atšķiras no perimetra?",
              ["laukums ir rūtiņu skaits, perimetrs — malu garums",
               "tie ir vienādi", "laukumu mēra centimetros",
               "perimetru mēra rūtiņās"], 0),
         ]},
        {"sr": "Aprēķina taisnstūra laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūris ir 6 rūtiņas plats un 4 rindas augsts. Laukums?",
              ["10", "20", "24", "26"], 2),
             ("Taisnstūra malas 7 cm un 3 cm. Cik liels ir laukums?",
              ["10", "20", "21", "24"], 2),
             ("Kvadrāta mala 5 rūtiņas. Cik liels ir laukums?",
              ["10", "20", "25", "50"], 2),
         ]},
        {"sr": "Salīdzina figūru laukumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienam taisnstūrim 2 × 6, otram 3 × 4 rūtiņas. Kā ir ar "
              "laukumiem?",
              ["tie ir vienādi", "pirmajam lielāks", "otrajam lielāks",
               "nevar salīdzināt"], 0),
             ("Vienādām figūrām laukumi ir …",
              ["vienādi", "dažādi", "vienmēr lielāki", "nezināmi"], 0),
             ("Vai atšķirīgiem taisnstūriem var būt vienāds laukums?",
              ["jā", "nē", "tikai kvadrātiem", "nekad"], 0),
         ]},
        {"sr": "Zīmē taisnstūri ar noteiktu laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas malas var būt taisnstūrim ar laukumu 12 rūtiņas?",
              ["3 un 4", "3 un 5", "2 un 5", "6 un 6"], 0),
             ("Kādas malas var būt taisnstūrim ar laukumu 20 rūtiņas?",
              ["4 un 5", "3 un 6", "2 un 9", "5 un 5"], 0),
             ("Cik dažādu taisnstūru ar laukumu 12 rūtiņas var uzzīmēt (malas "
              "veselos skaitļos)?",
              ["1", "2", "3", "6"], 2),
         ]},
        {"sr": "Zīmē riņķi un zina rādiusu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko zīmē riņķi?",
              ["ar cirkuli", "ar lineālu", "ar transportieri", "ar šķērēm"],
              0),
             ("Kas nosaka riņķa lielumu?",
              ["rādiusa garums", "krāsa", "virsotņu skaits", "malu skaits"],
              0),
             ("Rādiuss ir 3 cm. Cik gara ir riņķa līnijas caurmērs "
              "(diametrs)?",
              ["3 cm", "6 cm", "9 cm", "1,5 cm"], 1),
         ]},
        {"sr": "Lieto tilpuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurā mērvienībā mēra šķidruma tilpumu?",
              ["litros", "metros", "kilogramos", "minūtēs"], 0),
             ("Cik mililitru ir 1 litrā?", ["10", "100", "1000", "10000"], 2),
             ("Cik ml ir puslitrā?", ["50", "100", "250", "500"], 3),
         ]},
        {"sr": "Nosaka telpiskas figūras tilpumu kubos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko var izmērīt telpiskas figūras tilpumu?",
              ["ar vienādiem kubiem", "ar lineālu", "ar pulksteni",
               "ar rūtiņām"], 0),
             ("Skaldnis salikts no 2 slāņiem pa 6 kubiem. Cik kubu kopā?",
              ["8", "12", "14", "26"], 1),
             ("Skaldnis ir 3 × 2 × 2 kubi. Cik kubu kopā?",
              ["7", "10", "12", "14"], 2),
         ]},
        {"sr": "Nosaka telpiskas figūras šķautnes un skaldnes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik skaldņu ir taisnstūru skaldnim?", ["4", "6", "8", "12"],
              1),
             ("Cik šķautņu ir kubam?", ["6", "8", "12", "24"], 2),
             ("Cik virsotņu ir kubam?", ["4", "6", "8", "12"], 2),
         ]},
        {"sr": "Risina uzdevumu par laukumu vai tilpumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Istaba 5 m × 4 m. Cik kvadrātmetru ir grīdas laukums?",
              ["9", "18", "20", "40"], 2),
             ("Kannā 3 l sulas, izlej 750 ml. Cik ml palika?",
              ["1250 ml", "2250 ml", "2750 ml", "3750 ml"], 1),
             ("Kastē 4 rindas pa 5 kubiem vienā slānī, slāņi 2. Cik kubu?",
              ["20", "30", "40", "45"], 2),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 3.5. temata noslēgumā. "
                "Pārbauda leņķu veidus, taisnstūra laukuma aprēķinu, "
                "figūru salīdzināšanu pēc laukuma, riņķa rādiusu, tilpuma "
                "mērvienības un skaldņa tilpumu kubos.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Zīmē ar lineālu un risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Atpazīst leņķu veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds leņķis ir lapas stūrī?",
              ["taisns", "šaurs", "plats", "nav leņķa"], 0),
             ("Leņķis, kas mazāks nekā taisns, ir …",
              ["šaurs", "plats", "taisns", "apaļš"], 0),
             ("Cik taisnu leņķu ir kvadrātam?", ["2", "3", "4", "8"], 2),
         ]},
        {"sr": "Nosaka laukumu rūtiņās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūris 5 × 4 rūtiņas. Laukums?",
              ["9", "18", "20", "25"], 2),
             ("Kvadrāts ar malu 6 rūtiņas. Laukums?",
              ["12", "24", "36", "66"], 2),
             ("Kā nosaka laukumu rūtiņu lapā?",
              ["saskaita rūtiņas", "saskaita malas", "mēra perimetru",
               "saskaita virsotnes"], 0),
         ]},
        {"sr": "Salīdzina laukumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūriem 2 × 6 un 3 × 4 laukumi ir …",
              ["vienādi", "dažādi", "pirmajam lielāks", "otrajam lielāks"],
              0),
             ("Vai atšķirīgiem taisnstūriem var būt vienāds laukums?",
              ["jā", "nē", "tikai kvadrātiem", "nekad"], 0),
             ("Kādas malas var būt taisnstūrim ar laukumu 18 rūtiņas?",
              ["3 un 6", "4 un 5", "2 un 8", "3 un 5"], 0),
         ]},
        {"sr": "Zina riņķa rādiusu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko zīmē riņķi?",
              ["ar cirkuli", "ar lineālu", "ar šķērēm", "ar zīmuli brīvroku"],
              0),
             ("Kas nosaka riņķa lielumu?",
              ["rādiuss", "krāsa", "malu skaits", "virsotnes"], 0),
             ("Rādiuss 5 cm. Cik garš ir diametrs?",
              ["2,5 cm", "5 cm", "10 cm", "15 cm"], 2),
         ]},
        {"sr": "Lieto tilpuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ml ir 1 l?", ["10", "100", "1000", "10000"], 2),
             ("Cik ml ir puslitrā?", ["50", "250", "500", "1000"], 2),
             ("Kurā mērvienībā mēra tilpumu?",
              ["litros", "metros", "kilogramos", "stundās"], 0),
         ]},
        {"sr": "Nosaka skaldņa tilpumu kubos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Skaldnis 3 × 2 × 2 kubi. Cik kubu?", ["7", "10", "12", "14"],
              2),
             ("Divi slāņi pa 8 kubiem. Cik kubu kopā?",
              ["10", "16", "18", "64"], 1),
             ("Cik skaldņu ir taisnstūru skaldnim?", ["4", "6", "8", "12"],
              1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina taisnstūra laukumu un perimetru",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 6 × 4 rūtiņas; laukums = ……", "24"),
                         ("Taisnstūris 6 × 4 rūtiņas; perimetrs = ……", "20"),
                         ("Kvadrāts ar malu 7 rūtiņas; laukums = ……", "49"),
                         ("Taisnstūris ar laukumu 15 un malu 3; otra mala = "
                          "……", "5")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 7 × 3 rūtiņas; laukums = ……", "21"),
                         ("Taisnstūris 7 × 3 rūtiņas; perimetrs = ……", "20"),
                         ("Kvadrāts ar malu 8 rūtiņas; laukums = ……", "64"),
                         ("Taisnstūris ar laukumu 24 un malu 4; otra mala = "
                          "……", "6")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūris 5 × 5 rūtiņas; laukums = ……", "25"),
                         ("Taisnstūris 8 × 2 rūtiņas; perimetrs = ……", "20"),
                         ("Kvadrāts ar malu 9 rūtiņas; laukums = ……", "81"),
                         ("Taisnstūris ar laukumu 30 un malu 5; otra mala = "
                          "……", "6")]},
         ]},
        {"sr": "Lieto tilpuma mērvienības",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("1 l = …… ml", "1000"), ("2 l = …… ml", "2000"),
                         ("500 ml ir …… no litra", "puse")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("3 l = …… ml", "3000"), ("1 l 200 ml = …… ml",
                                                   "1200"),
                         ("250 ml ir …… no litra", "ceturtdaļa")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("5 l = …… ml", "5000"), ("2 l 500 ml = …… ml",
                                                   "2500"),
                         ("1000 ml ir …… litrs", "1")]},
         ]},
        {"sr": "Zīmē figūras ar dotu laukumu un leņķiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Zīmē rūtiņās", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri ar laukumu 12 rūtiņas!", 1),
                       ("Uzzīmē citu taisnstūri ar to pašu laukumu!", 1),
                       ("Uzraksti abu taisnstūru malu garumus!", 1),
                       ("Apvelc figūrā vienu taisnu leņķi!", 1)],
              "atbildes": ["1) Piemēram, 3 × 4 rūtiņas.   (1 p.)",
                           "2) Piemēram, 2 × 6 rūtiņas.   (1 p.)",
                           "3) Pierakstīti abi malu pāri.   (1 p.)",
                           "4) Apvilkts taisnstūra stūris.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē rūtiņās", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri ar laukumu 16 rūtiņas!", 1),
                       ("Uzzīmē kvadrātu ar to pašu laukumu!", 1),
                       ("Uzraksti abu figūru malu garumus!", 1),
                       ("Apvelc figūrā vienu taisnu leņķi!", 1)],
              "atbildes": ["1) Piemēram, 2 × 8 rūtiņas.   (1 p.)",
                           "2) Kvadrāts 4 × 4 rūtiņas.   (1 p.)",
                           "3) Pierakstīti malu garumi.   (1 p.)",
                           "4) Apvilkts stūris.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē rūtiņās", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri ar laukumu 20 rūtiņas!", 1),
                       ("Uzzīmē citu taisnstūri ar to pašu laukumu!", 1),
                       ("Aprēķini abu taisnstūru perimetrus!", 1),
                       ("Uzraksti, vai perimetri ir vienādi!", 1)],
              "atbildes": ["1) Piemēram, 4 × 5 rūtiņas.   (1 p.)",
                           "2) Piemēram, 2 × 10 rūtiņas.   (1 p.)",
                           "3) P = 18 un P = 24   (1 p.)",
                           "4) Atbilde: nav vienādi.   (1 p.)"]},
         ]},
        {"sr": "Nosaka telpiskas figūras tilpumu un elementus",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Telpiska figūra", "vieta": 5.5,
              "ievads": "Taisnstūru skaldnis salikts no kubiem: 4 kubi rindā, "
                        "3 rindas, 2 slāņi.",
              "jaut": [("Aprēķini, cik kubu ir vienā slānī!", 1),
                       ("Aprēķini, cik kubu ir visā skaldnī!", 1),
                       ("Uzraksti, cik skaldņu ir skaldnim!", 1)],
              "atbildes": ["1) 4 · 3 = 12   (1 p.)", "2) 12 · 2 = 24   "
                           "(1 p.)",
                           "3) Atbilde: 6 skaldnes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Telpiska figūra", "vieta": 5.5,
              "ievads": "Taisnstūru skaldnis salikts no kubiem: 5 kubi rindā, "
                        "2 rindas, 3 slāņi.",
              "jaut": [("Aprēķini, cik kubu ir vienā slānī!", 1),
                       ("Aprēķini, cik kubu ir visā skaldnī!", 1),
                       ("Uzraksti, cik šķautņu ir kubam!", 1)],
              "atbildes": ["1) 5 · 2 = 10   (1 p.)", "2) 10 · 3 = 30   "
                           "(1 p.)",
                           "3) Atbilde: 12 šķautnes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Telpiska figūra", "vieta": 5.5,
              "ievads": "Kubs salikts no maziem kubiņiem: 3 kubiņi katrā "
                        "šķautnē.",
              "jaut": [("Aprēķini, cik kubiņu ir vienā slānī!", 1),
                       ("Aprēķini, cik kubiņu ir visā kubā!", 1),
                       ("Uzraksti, cik virsotņu ir kubam!", 1)],
              "atbildes": ["1) 3 · 3 = 9   (1 p.)", "2) 9 · 3 = 27   (1 p.)",
                           "3) Atbilde: 8 virsotnes.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
