# -*- coding: utf-8 -*-
"""Matemātika, 9. klase. 9.6. Kā apraksta situācijas ar diviem nezināmiem
lielumiem?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 9. klase, 9.6. temats): vienādojums ar
diviem nezināmajiem un tā atrisinājums kā skaitļu pāris, atrisinājumu kopas
grafiskais attēlojums, vienādojumu sistēmas atrisinājums kā abu vienādojumu
kopīgais atrisinājums, sistēmas atrisināšana grafiski un analītiski
(ievietošanas un saskaitīšanas paņēmiens) un situāciju uzdevumu modelēšana.
"""

PRIEKSMETS = "Matemātika  |  9. klase"
TEMATS = "9.6."
NOSAUKUMS = "Kā apraksta situācijas ar diviem nezināmiem lielumiem?"

ATGADNE = [
    "Vienādojuma ar diviem nezināmajiem atrisinājums ir skaitļu pāris "
    "(x; y) — secība ir svarīga; visi atrisinājumi veido taisni.",
    "Grafiskais paņēmiens: abus vienādojumus pieraksta kā funkcijas; abu "
    "grafiku kopīgā punkta koordinātas ir sistēmas atrisinājums.",
    "Analītiskie paņēmieni: ievietošana (vienu nezināmo izsaka un ievieto) "
    "un saskaitīšana (viens nezināmais izzūd).",
]

FD = {
    "veids": "fd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 9.6. temata beigās. Pārbauda vienādojumu "
                "ar diviem nezināmajiem, tā atrisinājumu un grafisko "
                "attēlojumu, vienādojumu sistēmas jēdzienu, grafisko, "
                "ievietošanas un saskaitīšanas paņēmienu un situācijas "
                "modelēšanu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Atpazīst vienādojumu ar diviem nezināmajiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš ir vienādojums ar diviem nezināmajiem?",
              ["2x + y = 8", "2x = 8", "x² = 4", "y = 5"], 0),
             ("Cik nezināmo ir vienādojumā 3x − y = 7?",
              ["divi", "viens", "trīs", "neviens"], 0),
             ("Kā pieraksta šāda vienādojuma atrisinājumu?",
              ["kā skaitļu pāri (x; y)", "kā vienu skaitli", "kā daļu",
               "kā leņķi"], 0),
         ]},
        {"sr": "Saprot atrisinājumu kā skaitļu pāri",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai (2; 3) ir tas pats, kas (3; 2)?",
              ["nē, secība ir svarīga", "jā", "tikai dažreiz",
               "nevar noteikt"], 0),
             ("Ko nozīmē pāris (5; −1)?",
              ["x = 5 un y = −1", "x = −1 un y = 5", "x · y = 5",
               "x + y = 5"], 0),
             ("Cik atrisinājumu ir vienādojumam x + y = 10?",
              ["bezgalīgi daudz", "viens", "divi", "neviens"], 0),
         ]},
        {"sr": "Pārbauda, vai pāris ir atrisinājums",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai (2; 4) ir vienādojuma x + y = 6 atrisinājums?",
              ["jā", "nē", "tikai ja x = 4", "nevar pārbaudīt"], 0),
             ("Vai (1; 3) ir vienādojuma 2x + y = 5 atrisinājums?",
              ["jā", "nē", "tikai grafiski", "nevar noteikt"], 0),
             ("Kā pārbauda, vai pāris ir atrisinājums?",
              ["ievieto vērtības vienādojumā", "zīmē grafiku",
               "saskaita x un y", "dala x ar y"], 0),
         ]},
        {"sr": "Attēlo vienādojuma atrisinājumus grafiski",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir vienādojuma x + y = 5 grafiks?",
              ["taisne", "parabola", "riņķa līnija", "punkts"], 0),
             ("Kā vienādojumu x + y = 5 pieraksta kā funkciju?",
              ["y = 5 − x", "y = 5 + x", "y = x − 5", "y = 5x"], 0),
             ("Ko attēlo katrs taisnes punkts?",
              ["vienu vienādojuma atrisinājumu", "koeficientu", "asi",
               "taisnes slīpumu"], 0),
         ]},
        {"sr": "Zina, kas ir sistēmas atrisinājums",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir vienādojumu sistēmas atrisinājums?",
              ["abiem vienādojumiem kopīgs skaitļu pāris",
               "pirmā vienādojuma atrisinājums", "jebkurš pāris",
               "taisnes garums"], 0),
             ("Ko grafikā nozīmē sistēmas atrisinājums?",
              ["abu taišņu krustpunktu", "taisnes sākumu",
               "asu krustpunktu", "taisnes slīpumu"], 0),
             ("Cik atrisinājumu ir, ja taisnes krustojas vienā punktā?",
              ["viens", "divi", "neviens", "bezgalīgi daudz"], 0),
         ]},
        {"sr": "Lieto grafisko paņēmienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir pirmais solis, risinot sistēmu grafiski?",
              ["abus vienādojumus pieraksta kā funkcijas",
               "saskaita vienādojumus", "izsaka x", "reizina ar 2"], 0),
             ("Taisnes krustojas punktā (2; 3). Kāds ir atrisinājums?",
              ["x = 2 un y = 3", "x = 3 un y = 2", "x = 5",
               "atrisinājuma nav"], 0),
             ("Kāds ir grafiskā paņēmiena trūkums?",
              ["atrisinājums var būt neprecīzs", "tas ir pārāk ātrs",
               "nevar uzzīmēt taisnes", "tam nav trūkumu"], 0),
         ]},
        {"sr": "Lieto ievietošanas paņēmienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko dara, lietojot ievietošanas paņēmienu?",
              ["vienu nezināmo izsaka un ievieto otrā vienādojumā",
               "saskaita abus vienādojumus", "zīmē grafiku",
               "sareizina vienādojumus"], 0),
             ("No y = x + 1 un x + y = 7 iegūst …",
              ["x + (x + 1) = 7", "x + y = 8", "2y = 7", "x = 7"], 0),
             ("Kāds ir sistēmas y = x + 1, x + y = 7 atrisinājums?",
              ["x = 3 un y = 4", "x = 4 un y = 3", "x = 7 un y = 0",
               "atrisinājuma nav"], 0),
         ]},
        {"sr": "Lieto saskaitīšanas paņēmienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko panāk, saskaitot sistēmas vienādojumus?",
              ["viens nezināmais izzūd", "abi nezināmie izzūd",
               "vienādojums kļūst garāks", "nekas nemainās"], 0),
             ("Sistēmā x + y = 10 un x − y = 2. Ko iegūst, tos saskaitot?",
              ["2x = 12", "2y = 12", "x = 10", "2x = 8"], 0),
             ("Kāds ir sistēmas x + y = 10, x − y = 2 atrisinājums?",
              ["x = 6 un y = 4", "x = 4 un y = 6", "x = 12",
               "x = 5 un y = 5"], 0),
         ]},
        {"sr": "Atrisina vienādojumu sistēmu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Atrisini sistēmu:  x + y = 9  un  x − y = 1",
              ["x = 5 un y = 4", "x = 4 un y = 5", "x = 9 un y = 0",
               "x = 10"], 0),
             ("Atrisini sistēmu:  y = 2x  un  x + y = 12",
              ["x = 4 un y = 8", "x = 8 un y = 4", "x = 6 un y = 6",
               "x = 12"], 0),
             ("Kā pārbauda sistēmas atrisinājumu?",
              ["ievieto abos vienādojumos", "ievieto vienā vienādojumā",
               "zīmē grafiku", "to nepārbauda"], 0),
         ]},
        {"sr": "Nosaka atrisinājumu skaitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik atrisinājumu ir, ja taisnes ir paralēlas?",
              ["neviena", "viens", "divi", "bezgalīgi daudz"], 0),
             ("Cik atrisinājumu ir, ja abi vienādojumi dod vienu taisni?",
              ["bezgalīgi daudz", "viens", "neviens", "divi"], 0),
             ("Kas notiek, ja, risinot sistēmu, iegūst 0 = 5?",
              ["atrisinājumu nav", "atrisinājums ir 0",
               "atrisinājums ir 5", "ir bezgalīgi daudz"], 0),
         ]},
        {"sr": "Modelē situāciju ar vienādojumu sistēmu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Divu skaitļu summa ir 20, starpība — 4. Kura sistēma der?",
              ["x + y = 20 un x − y = 4", "x + y = 4 un x − y = 20",
               "xy = 20 un x : y = 4", "x + y = 24"], 0),
             ("Divas pieaugušo un trīs bērnu biļetes maksā 31 eiro. Kurš "
              "vienādojums der?",
              ["2x + 3y = 31", "3x + 2y = 31", "x + y = 31",
               "5xy = 31"], 0),
             ("Kāpēc situācijā apzīmē divus nezināmos?",
              ["jo meklē divus lielumus", "lai uzdevums būtu grūtāks",
               "tā ir tradīcija", "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Divu skaitļu summa ir 20, starpība — 4. Kādi ir skaitļi?",
              ["12 un 8", "10 un 10", "14 un 6", "16 un 4"], 0),
             ("Klasē 25 skolēni; meiteņu par 3 vairāk nekā zēnu. Cik ir "
              "zēnu?", ["11", "14", "12", "13"], 0),
             ("2 kg ābolu un 1 kg bumbieru maksā 7 eiro, bet 1 kg + 1 kg — "
              "5 eiro. Cik maksā ābolu kilograms?",
              ["2 eiro", "3 eiro", "5 eiro", "7 eiro"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 25 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 9.6. temata noslēgumā. "
                "Pārbauda vienādojuma ar diviem nezināmajiem atrisinājumu, "
                "sistēmas atrisināšanu grafiski un analītiski, "
                "atrisinājumu skaita noteikšanu un situāciju uzdevumu "
                "modelēšanu ar vienādojumu sistēmu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 25 "
              "punktus. Risinājumu pieraksti tam atvēlētajā vietā; "
              "atļauts kalkulators.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Atpazīst vienādojumu un tā atrisinājumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš ir vienādojums ar diviem nezināmajiem?",
              ["3x − y = 5", "3x = 5", "x² = 9", "y = 2"], 0),
             ("Ko nozīmē pāris (4; −2)?",
              ["x = 4 un y = −2", "x = −2 un y = 4", "x · y = 4",
               "x + y = 4"], 0),
             ("Vai (3; 2) ir vienādojuma x + y = 5 atrisinājums?",
              ["jā", "nē", "tikai grafiski", "nevar noteikt"], 0),
         ]},
        {"sr": "Attēlo atrisinājumus grafiski",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir vienādojuma 2x + y = 6 grafiks?",
              ["taisne", "parabola", "riņķa līnija", "punkts"], 0),
             ("Kā vienādojumu x + y = 8 pieraksta kā funkciju?",
              ["y = 8 − x", "y = 8 + x", "y = x − 8", "y = 8x"], 0),
             ("Ko grafikā nozīmē sistēmas atrisinājums?",
              ["abu taišņu krustpunktu", "taisnes sākumu",
               "asu krustpunktu", "taisnes slīpumu"], 0),
         ]},
        {"sr": "Lieto saskaitīšanas paņēmienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Sistēmā x + y = 12 un x − y = 4. Ko iegūst, tos saskaitot?",
              ["2x = 16", "2y = 16", "x = 12", "2x = 8"], 0),
             ("Kāds ir sistēmas x + y = 12, x − y = 4 atrisinājums?",
              ["x = 8 un y = 4", "x = 4 un y = 8", "x = 16",
               "x = 6 un y = 6"], 0),
             ("Ko panāk, saskaitot vienādojumus?",
              ["viens nezināmais izzūd", "abi nezināmie izzūd",
               "vienādojums kļūst garāks", "nekas nemainās"], 0),
         ]},
        {"sr": "Lieto ievietošanas paņēmienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("No y = x + 3 un x + y = 11 iegūst …",
              ["x + (x + 3) = 11", "x + y = 14", "2y = 11", "x = 11"], 0),
             ("Kāds ir sistēmas y = x + 3, x + y = 11 atrisinājums?",
              ["x = 4 un y = 7", "x = 7 un y = 4", "x = 11 un y = 0",
               "atrisinājuma nav"], 0),
             ("Ko dara, lietojot ievietošanas paņēmienu?",
              ["vienu nezināmo izsaka un ievieto", "saskaita vienādojumus",
               "zīmē grafiku", "sareizina vienādojumus"], 0),
         ]},
        {"sr": "Nosaka atrisinājumu skaitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik atrisinājumu ir, ja taisnes ir paralēlas?",
              ["neviena", "viens", "divi", "bezgalīgi daudz"], 0),
             ("Kas notiek, ja, risinot sistēmu, iegūst 0 = 7?",
              ["atrisinājumu nav", "atrisinājums ir 0",
               "atrisinājums ir 7", "ir bezgalīgi daudz"], 0),
             ("Cik atrisinājumu ir, ja abi vienādojumi dod vienu taisni?",
              ["bezgalīgi daudz", "viens", "neviens", "divi"], 0),
         ]},
        {"sr": "Modelē situāciju ar sistēmu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Divu skaitļu summa ir 30, starpība — 6. Kura sistēma der?",
              ["x + y = 30 un x − y = 6", "x + y = 6 un x − y = 30",
               "xy = 30", "x + y = 36"], 0),
             ("Kādi ir šie skaitļi?",
              ["18 un 12", "20 un 10", "24 un 6", "15 un 15"], 0),
             ("Kāpēc atrisinājumu ievieto abos vienādojumos?",
              ["lai pārbaudītu, vai tas der abiem", "lai iegūtu grafiku",
               "lai saīsinātu risinājumu", "tas nav vajadzīgs"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pārbauda atrisinājumu un pārveido vienādojumus",
         "stunda": TEMATS, "punkti": 5, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Vai (2; 3) ir vienādojuma x + y = 5 "
                          "atrisinājums?  ……", "jā"),
                         ("Vienādojumu x + y = 7 pieraksta kā  y = ……",
                          "7 − x"),
                         ("Sistēmā x + y = 10 un x − y = 2, saskaitot, "
                          "iegūst ……", "2x = 12"),
                         ("Šīs sistēmas atrisinājums ir  x = …… un y = ……",
                          "6 un 4"),
                         ("Taisnes krustojas punktā (3; 1); atrisinājums "
                          "ir ……", "x = 3, y = 1")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Vai (1; 4) ir vienādojuma 2x + y = 6 "
                          "atrisinājums?  ……", "jā"),
                         ("Vienādojumu x − y = 3 pieraksta kā  y = ……",
                          "x − 3"),
                         ("Sistēmā x + y = 9 un x − y = 1, saskaitot, "
                          "iegūst ……", "2x = 10"),
                         ("Šīs sistēmas atrisinājums ir  x = …… un y = ……",
                          "5 un 4"),
                         ("Ja taisnes ir paralēlas, atrisinājumu skaits "
                          "ir ……", "0")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Vai (3; 2) ir vienādojuma x − y = 1 "
                          "atrisinājums?  ……", "jā"),
                         ("Vienādojumu 2x + y = 8 pieraksta kā  y = ……",
                          "8 − 2x"),
                         ("Sistēmā x + y = 12 un x − y = 4, saskaitot, "
                          "iegūst ……", "2x = 16"),
                         ("Šīs sistēmas atrisinājums ir  x = …… un y = ……",
                          "8 un 4"),
                         ("Ja iegūst 0 = 5, atrisinājumu skaits ir ……",
                          "0")]},
         ]},
        {"sr": "Atrisina vienādojumu sistēmu analītiski",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Vienādojumu sistēma", "vieta": 5.8,
              "teksts": "Atrisini sistēmu ar ievietošanas paņēmienu!   "
                        "y = x + 2   un   3x + y = 14.   Pieraksti visus "
                        "soļus un pārbaudi atrisinājumu.",
              "kriteriji": [
                  "Izvēlēts paņēmiens; y aizstāts ar x + 2.   (1 p.)",
                  "Iegūts 3x + (x + 2) = 14.   (1 p.)",
                  "Iegūts 4x = 12 un x = 3.   (1 p.)",
                  "Aprēķināts y = 5.   (1 p.)",
                  "Pārbaudīts abos vienādojumos; atbilde (3; 5).   (1 p.)"]},
             {"tips": "aprekins", "virs": "Vienādojumu sistēma", "vieta": 5.8,
              "teksts": "Atrisini sistēmu ar saskaitīšanas paņēmienu!   "
                        "2x + y = 11   un   x − y = 1.   Pieraksti visus "
                        "soļus un pārbaudi atrisinājumu.",
              "kriteriji": [
                  "Vienādojumi saskaitīti; y izzūd.   (1 p.)",
                  "Iegūts 3x = 12.   (1 p.)",
                  "Aprēķināts x = 4.   (1 p.)",
                  "Aprēķināts y = 3.   (1 p.)",
                  "Pārbaudīts abos vienādojumos; atbilde (4; 3).   (1 p.)"]},
             {"tips": "aprekins", "virs": "Vienādojumu sistēma", "vieta": 5.8,
              "teksts": "Atrisini sistēmu!   x + 2y = 11   un   "
                        "3x − 2y = 9.   Pieraksti visus soļus un pārbaudi "
                        "atrisinājumu.",
              "kriteriji": [
                  "Vienādojumi saskaitīti; y izzūd.   (1 p.)",
                  "Iegūts 4x = 20.   (1 p.)",
                  "Aprēķināts x = 5.   (1 p.)",
                  "Aprēķināts y = 3.   (1 p.)",
                  "Pārbaudīts abos vienādojumos; atbilde (5; 3).   (1 p.)"]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar diviem nezināmajiem",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.0,
              "teksts": "Par 2 pieaugušo un 3 bērnu biļetēm samaksāja "
                        "31 eiro, bet par 1 pieaugušā un 2 bērnu biļetēm — "
                        "18 eiro. Cik maksā katra biļete?",
              "kriteriji": [
                  "Apzīmēts x — pieaugušā, y — bērna biļete.   (1 p.)",
                  "Sastādīta sistēma 2x + 3y = 31 un x + 2y = 18.   (1 p.)",
                  "Izteikts x = 18 − 2y un ievietots.   (1 p.)",
                  "Aprēķināts y = 5.   (1 p.)",
                  "Atbilde: pieaugušā 8 eiro, bērna 5 eiro.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.0,
              "teksts": "Divu skaitļu summa ir 34, bet to starpība — 8. "
                        "Kādi ir šie skaitļi? Pieraksti sistēmu un "
                        "atrisini to.",
              "kriteriji": [
                  "Apzīmēti nezināmie x un y.   (1 p.)",
                  "Sastādīta sistēma x + y = 34 un x − y = 8.   (1 p.)",
                  "Vienādojumi saskaitīti; 2x = 42.   (1 p.)",
                  "Aprēķināts x = 21.   (1 p.)",
                  "Atbilde: skaitļi ir 21 un 13.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.0,
              "teksts": "Klasē ir 28 skolēni, un meiteņu ir par 4 vairāk "
                        "nekā zēnu. Cik klasē ir zēnu un cik meiteņu? "
                        "Pieraksti sistēmu un atrisini to.",
              "kriteriji": [
                  "Apzīmēts x — zēni, y — meitenes.   (1 p.)",
                  "Sastādīta sistēma x + y = 28 un y = x + 4.   (1 p.)",
                  "Ievietots x + (x + 4) = 28.   (1 p.)",
                  "Aprēķināts x = 12.   (1 p.)",
                  "Atbilde: 12 zēni un 16 meitenes.   (1 p.)"]},
         ]},
        {"sr": "Atrisina sistēmu grafiski",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Grafiskais paņēmiens",
              "vieta": 4.4,
              "ievads": "Dota sistēma:   y = x + 1   un   y = −x + 5.",
              "jaut": [("Uzzīmē abu funkciju grafikus!", 2),
                       ("Nosaki krustpunkta koordinātas!", 1),
                       ("Pieraksti sistēmas atrisinājumu!", 1)],
              "atbildes": ["1) Uzzīmētas abas taisnes.   (2 p.)",
                           "2) Krustpunkts (2; 3).   (1 p.)",
                           "3) x = 2 un y = 3.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Grafiskais paņēmiens",
              "vieta": 4.4,
              "ievads": "Dota sistēma:   y = 2x   un   y = x + 3.",
              "jaut": [("Uzzīmē abu funkciju grafikus!", 2),
                       ("Nosaki krustpunkta koordinātas!", 1),
                       ("Pārbaudi atrisinājumu abos vienādojumos!", 1)],
              "atbildes": ["1) Uzzīmētas abas taisnes.   (2 p.)",
                           "2) Krustpunkts (3; 6).   (1 p.)",
                           "3) 6 = 2 · 3 un 6 = 3 + 3 — der abiem.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Grafiskais paņēmiens",
              "vieta": 4.4,
              "ievads": "Dota sistēma:   y = x + 2   un   y = x − 1.",
              "jaut": [("Uzzīmē abu funkciju grafikus!", 2),
                       ("Kā savstarpēji novietotas abas taisnes?", 1),
                       ("Cik atrisinājumu ir sistēmai? Pamato!", 1)],
              "atbildes": ["1) Uzzīmētas abas taisnes.   (2 p.)",
                           "2) Tās ir paralēlas — vienāds slīpums.   "
                           "(1 p.)",
                           "3) Atrisinājumu nav, jo taisnes nekrustojas. "
                           "  (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
