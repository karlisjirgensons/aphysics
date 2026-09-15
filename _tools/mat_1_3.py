# -*- coding: utf-8 -*-
"""Matemātika, 1. klase. 1.3. Kā mēra garumus un kā iegūst simetrisku figūru?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 1. klase, 1.3. temats): mērīšana ar
lineālu centimetros, nogrieznis, lauzta līnija, taisnstūris un kvadrāts,
garumu salīdzināšana, darbības ar mērījumiem (2 cm + 3 cm = 5 cm), cik
pietrūkst līdz veselam desmitam, simetriska figūra.
"""

PRIEKSMETS = "Matemātika  |  1. klase"
TEMATS = "1.3."
NOSAUKUMS = "Kā mēra garumus un kā iegūst simetrisku figūru?"

ATGADNE = [
    "Garuma mērvienība:  centimetrs (cm)   ·   1 dm = 10 cm   ·   "
    "1 m = 100 cm",
    "Mērot ar lineālu, objekta galu liek pie 0.   ·   Nogrieznis ir taisnas "
    "līnijas daļa starp diviem punktiem.",
    "Figūra ir simetriska, ja to var pārlocīt uz pusēm tā, ka abas puses "
    "sakrīt.",
]

FD = {
    "veids": "fd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 1.3. temata beigās. Pārbauda mērīšanas "
                "jēgu un lineāla lietošanu, garuma mērvienības, nogriežņa un "
                "lauztas līnijas jēdzienu, taisnstūri un kvadrātu, garumu "
                "salīdzināšanu, darbības ar mērījumiem un simetriskas "
                "figūras atpazīšanu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro, ko nozīmē mērīt",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē izmērīt objekta garumu?",
              ["noskaidrot, cik mērvienību tajā ietilpst",
               "noskaidrot, kādā krāsā tas ir", "to pasvērt",
               "to salauzt"], 0),
             ("Kāpēc cilvēki vienojās par vienu mērvienību?",
              ["lai visi saprastu, cik garš ir objekts", "lai būtu skaistāk",
               "lai mērītu ātrāk", "lai nevajadzētu lineālu"], 0),
             ("Ar ko mēra garumu?",
              ["ar lineālu", "ar pulksteni", "ar svariem",
               "ar mērtrauku"], 0),
         ]},
        {"sr": "Pareizi liek lineālu un nolasa mērījumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pie kura skaitļa uz lineāla liek objekta galu?",
              ["pie 0", "pie 1", "pie 10", "vienalga pie kura"], 0),
             ("Nogriežņa sākums ir pie 0, gals pie 6. Cik garš ir "
              "nogrieznis?",
              ["1 cm", "5 cm", "6 cm", "60 cm"], 2),
             ("Ko rāda skaitļi uz lineāla?",
              ["centimetru skaitu", "kilogramu skaitu", "minūšu skaitu",
               "litru skaitu"], 0),
         ]},
        {"sr": "Lieto garuma mērvienības un to apzīmējumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā saīsināti raksta centimetru?", ["c", "cm", "m", "km"], 1),
             ("Cik centimetru ir 1 decimetrā?", ["1", "10", "50", "100"], 1),
             ("Cik centimetru ir 1 metrā?", ["10", "50", "100", "1000"], 2),
         ]},
        {"sr": "Zina, kas ir nogrieznis",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir nogrieznis?",
              ["taisnas līnijas daļa starp diviem punktiem", "līkne",
               "riņķis", "figūra ar 4 malām"], 0),
             ("Cik galu ir nogrieznim?", ["1", "2", "3", "4"], 1),
             ("Ar ko zīmē nogriezni?",
              ["ar lineālu", "ar dzēšgumiju", "ar šķērēm", "ar cirkuli"], 0),
         ]},
        {"sr": "Zina, kas ir lauzta līnija",
         "stunda": TEMATS,
         "jautajumi": [
             ("No kā veido lauztu līniju?",
              ["no nogriežņiem", "no riņķiem", "no punktiem",
               "no kvadrātiem"], 0),
             ("Lauztā līnijā ir 3 nogriežņi: 2 cm, 3 cm un 4 cm. Cik gara "
              "ir līnija?",
              ["5 cm", "7 cm", "9 cm", "12 cm"], 2),
             ("Kā sauc līniju, kas veidota no vairākiem nogriežņiem?",
              ["lauzta līnija", "taisne", "riņķis", "leņķis"], 0),
         ]},
        {"sr": "Atšķir taisnstūri un kvadrātu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik malu ir taisnstūrim?", ["2", "3", "4", "5"], 2),
             ("Kāds ir kvadrāts?",
              ["taisnstūris, kuram visas malas vienāda garuma",
               "figūra ar 3 malām", "figūra bez malām",
               "figūra ar 5 virsotnēm"], 0),
             ("Ar ko zīmē taisnstūri rūtiņu lapā?",
              ["ar lineālu pa rūtiņām", "ar brīvu roku",
               "ar krāsainu zīmuli", "ar šķērēm"], 0),
         ]},
        {"sr": "Salīdzina garumus pēc izmērītajām vērtībām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zīmulis ir 9 cm, pildspalva 7 cm. Kurš ir garāks?",
              ["zīmulis", "pildspalva", "abi vienādi", "nevar zināt"], 0),
             ("Lente A ir 5 cm, lente B ir 8 cm. Kura ir īsāka?",
              ["lente A", "lente B", "abas vienādas", "nevar zināt"], 0),
             ("Kura zīme jāliek:  6 cm …… 6 cm?", [">", "<", "=", "+"], 2),
         ]},
        {"sr": "Nosaka, par cik viens objekts ir garāks vai īsāks",
         "stunda": TEMATS,
         "jautajumi": [
             ("Viens kociņš ir 8 cm, otrs 5 cm. Par cik pirmais ir garāks?",
              ["2 cm", "3 cm", "5 cm", "13 cm"], 1),
             ("Lente ir 4 cm, virve 9 cm. Par cik lente ir īsāka?",
              ["4 cm", "5 cm", "6 cm", "13 cm"], 1),
             ("Nogrieznis ir 7 cm. Otrs ir par 2 cm garāks. Cik garš ir "
              "otrs?",
              ["5 cm", "8 cm", "9 cm", "14 cm"], 2),
         ]},
        {"sr": "Saskaita un atņem mērījumus ar mērvienībām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 cm + 3 cm?", ["5", "5 cm", "6 cm", "23 cm"], 1),
             ("Cik ir 10 cm − 4 cm?", ["4 cm", "6 cm", "14 cm", "6"], 1),
             ("Lauzta līnija: 3 cm un 5 cm. Cik gara tā ir kopā?",
              ["2 cm", "7 cm", "8 cm", "35 cm"], 2),
         ]},
        {"sr": "Nosaka, cik pietrūkst līdz veselam desmitam",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik pietrūkst skaitlim 7 līdz 10?", ["2", "3", "4", "17"], 1),
             ("Cik pietrūkst skaitlim 4 līdz 10?", ["4", "5", "6", "14"], 2),
             ("Nogrieznis ir 6 cm garš. Cik cm pietrūkst līdz 1 dm?",
              ["3 cm", "4 cm", "6 cm", "16 cm"], 1),
         ]},
        {"sr": "Atpazīst simetrisku figūru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad figūra ir simetriska?",
              ["ja to var pārlocīt uz pusēm tā, ka abas puses sakrīt",
               "ja tā ir liela", "ja tai ir 4 malas",
               "ja tā ir uzzīmēta ar lineālu"], 0),
             ("Kura figūra ir simetriska?",
              ["kvadrāts", "figūra bez formas", "burts F", "burts R"], 0),
             ("Kā pārbauda, vai papīra figūra ir simetriska?",
              ["to pārloka uz pusēm", "to pasver", "to nokrāso",
               "to izmēra ar pulksteni"], 0),
         ]},
        {"sr": "Iegūst simetrisku figūru, locot vai zīmējot",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc līniju, pa kuru figūru pārloka?",
              ["simetrijas ass", "nogrieznis", "lauzta līnija", "mala"], 0),
             ("Papīru pārloka uz pusēm un izgriež figūru. Kāda tā būs?",
              ["simetriska", "nesimetriska", "apaļa", "trīsstūraina"], 0),
             ("Cik simetrijas asu ir kvadrātam?", ["1", "2", "4", "0"], 2),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 1.3. temata noslēgumā. "
                "Pārbauda mērīšanu ar lineālu, garuma mērvienības, "
                "nogriežņa un lauztas līnijas zīmēšanu, darbības ar "
                "mērījumiem, garumu salīdzināšanu un simetriskas figūras "
                "iegūšanu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Uzdevumu tekstu lasa skolotājs. Zīmē ar lineālu tam "
              "atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina mērīšanas kārtību un mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pie kura skaitļa uz lineāla liek mērāmā objekta galu?",
              ["pie 0", "pie 1", "pie 5", "pie 10"], 0),
             ("Kā saīsināti raksta centimetru?", ["c", "cm", "m", "cn"], 1),
             ("Cik centimetru ir 1 dm?", ["1", "10", "100", "1000"], 1),
         ]},
        {"sr": "Zina, kas ir nogrieznis un lauzta līnija",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik galu ir nogrieznim?", ["1", "2", "4", "daudz"], 1),
             ("No kā veidota lauzta līnija?",
              ["no nogriežņiem", "no riņķiem", "no punktiem",
               "no leņķiem"], 0),
             ("Ar ko zīmē taisnu līniju?",
              ["ar lineālu", "ar šķērēm", "ar dzēšgumiju", "ar pulksteni"],
              0),
         ]},
        {"sr": "Salīdzina izmērītus garumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zīmulis 8 cm, krītiņš 5 cm. Kurš ir garāks?",
              ["zīmulis", "krītiņš", "abi vienādi", "nevar zināt"], 0),
             ("Kura zīme jāliek:  4 cm …… 9 cm?", [">", "<", "=", "−"], 1),
             ("Lente A 7 cm, lente B 7 cm. Kā ir?",
              ["A garāka", "B garāka", "abas vienāda garuma",
               "nevar salīdzināt"], 2),
         ]},
        {"sr": "Aprēķina, par cik garāks vai īsāks",
         "stunda": TEMATS,
         "jautajumi": [
             ("Viens nogrieznis 9 cm, otrs 6 cm. Par cik pirmais ir garāks?",
              ["2 cm", "3 cm", "6 cm", "15 cm"], 1),
             ("Virve 10 cm, lente 4 cm. Par cik lente ir īsāka?",
              ["4 cm", "5 cm", "6 cm", "14 cm"], 2),
             ("Nogrieznis ir 5 cm. Otrs par 3 cm garāks. Cik garš ir otrs?",
              ["2 cm", "7 cm", "8 cm", "53 cm"], 2),
         ]},
        {"sr": "Saskaita un atņem mērījumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3 cm + 6 cm?", ["8 cm", "9 cm", "36 cm", "9"], 1),
             ("Cik ir 8 cm − 5 cm?", ["3 cm", "4 cm", "13 cm", "3"], 0),
             ("Lauztā līnijā ir 4 cm un 4 cm. Cik gara tā ir?",
              ["4 cm", "8 cm", "16 cm", "44 cm"], 1),
         ]},
        {"sr": "Atpazīst simetrisku figūru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad figūra ir simetriska?",
              ["ja to var pārlocīt tā, ka abas puses sakrīt", "ja tā ir maza",
               "ja tā ir zila", "ja tai ir 3 malas"], 0),
             ("Kā sauc līniju, pa kuru figūru pārloka?",
              ["simetrijas ass", "mala", "virsotne", "nogrieznis"], 0),
             ("Kura figūra noteikti ir simetriska?",
              ["kvadrāts", "burts L", "burts P", "burts G"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita un atņem garumus ar mērvienībām",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini garumus",
              "note": "Ieraksti atbildi kopā ar mērvienību! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("3 cm + 4 cm = ……", "7 cm"),
                         ("9 cm − 5 cm = ……", "4 cm"),
                         ("6 cm + 4 cm = ……", "10 cm"),
                         ("1 dm = …… cm", "10 cm")]},
             {"tips": "parveide", "virs": "Aprēķini garumus",
              "note": "Ieraksti atbildi kopā ar mērvienību! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("2 cm + 6 cm = ……", "8 cm"),
                         ("10 cm − 3 cm = ……", "7 cm"),
                         ("5 cm + 5 cm = ……", "10 cm"),
                         ("1 dm − 4 cm = ……", "6 cm")]},
             {"tips": "parveide", "virs": "Aprēķini garumus",
              "note": "Ieraksti atbildi kopā ar mērvienību! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("4 cm + 4 cm = ……", "8 cm"),
                         ("8 cm − 6 cm = ……", "2 cm"),
                         ("7 cm + 3 cm = ……", "10 cm"),
                         ("1 dm − 2 cm = ……", "8 cm")]},
         ]},
        {"sr": "Salīdzina garumus un ieraksta zīmi",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp garumiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("5 cm  ……  9 cm", "<"), ("8 cm  ……  3 cm", ">"),
                         ("1 dm  ……  10 cm", "=")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp garumiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("7 cm  ……  2 cm", ">"), ("4 cm  ……  6 cm", "<"),
                         ("9 cm  ……  9 cm", "=")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp garumiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [("3 cm  ……  8 cm", "<"), ("1 dm  ……  6 cm", ">"),
                         ("5 cm  ……  5 cm", "=")]},
         ]},
        {"sr": "Zīmē nogriežņus un lauztu līniju ar lineālu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Zīmē ar lineālu", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās un mēri ar lineālu!",
              "jaut": [("Uzzīmē nogriezni, kas ir 6 cm garš!", 1),
                       ("Uzzīmē nogriezni, kas ir par 2 cm īsāks!", 1),
                       ("Uzraksti, cik cm garš ir otrais nogrieznis!", 1),
                       ("Uzzīmē lauztu līniju no diviem nogriežņiem!", 1)],
              "atbildes": [
                  "1) Uzzīmēts 6 cm garš nogrieznis (pieļaujama kļūda "
                  "±2 mm).   (1 p.)",
                  "2) Uzzīmēts 4 cm garš nogrieznis.   (1 p.)",
                  "3) Pierakstīts 4 cm.   (1 p.)",
                  "4) Uzzīmēta lauzta līnija no diviem nogriežņiem.   "
                  "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē ar lineālu", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās un mēri ar lineālu!",
              "jaut": [("Uzzīmē nogriezni, kas ir 5 cm garš!", 1),
                       ("Uzzīmē nogriezni, kas ir par 3 cm garāks!", 1),
                       ("Uzraksti, cik cm garš ir otrais nogrieznis!", 1),
                       ("Uzzīmē lauztu līniju no trim nogriežņiem!", 1)],
              "atbildes": [
                  "1) Uzzīmēts 5 cm garš nogrieznis (pieļaujama kļūda "
                  "±2 mm).   (1 p.)",
                  "2) Uzzīmēts 8 cm garš nogrieznis.   (1 p.)",
                  "3) Pierakstīts 8 cm.   (1 p.)",
                  "4) Uzzīmēta lauzta līnija no trim nogriežņiem.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē ar lineālu", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās un mēri ar lineālu!",
              "jaut": [("Uzzīmē nogriezni, kas ir 7 cm garš!", 1),
                       ("Uzzīmē nogriezni, kas ir par 4 cm īsāks!", 1),
                       ("Uzraksti, cik cm garš ir otrais nogrieznis!", 1),
                       ("Uzzīmē taisnstūri ar lineālu pa rūtiņām!", 1)],
              "atbildes": [
                  "1) Uzzīmēts 7 cm garš nogrieznis (pieļaujama kļūda "
                  "±2 mm).   (1 p.)",
                  "2) Uzzīmēts 3 cm garš nogrieznis.   (1 p.)",
                  "3) Pierakstīts 3 cm.   (1 p.)",
                  "4) Uzzīmēts taisnstūris ar taisnām malām pa rūtiņām.   "
                  "(1 p.)"]},
         ]},
        {"sr": "Iegūst simetrisku figūru un parāda simetrijas asi",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Simetriska figūra", "vieta": 5.5,
              "ievads": "Zīmē rūtiņās!",
              "jaut": [("Uzzīmē simetrisku figūru!", 1),
                       ("Novelc tās simetrijas asi!", 1),
                       ("Uzzīmē figūru, kas nav simetriska!", 1)],
              "atbildes": [
                  "1) Uzzīmēta simetriska figūra, piemēram, kvadrāts.   "
                  "(1 p.)",
                  "2) Novilkta ass, pa kuru abas puses sakrīt.   (1 p.)",
                  "3) Uzzīmēta figūra, kurai nav simetrijas ass.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Simetriska figūra", "vieta": 5.5,
              "ievads": "Zīmē rūtiņās!",
              "jaut": [("Uzzīmē simetrisku figūru ar 4 malām!", 1),
                       ("Novelc tās simetrijas asi!", 1),
                       ("Uzraksti, cik simetrijas asu ir kvadrātam!", 1)],
              "atbildes": [
                  "1) Uzzīmēts kvadrāts vai taisnstūris.   (1 p.)",
                  "2) Novilkta ass, pa kuru abas puses sakrīt.   (1 p.)",
                  "3) Pierakstīts 4.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Simetriska figūra", "vieta": 5.5,
              "ievads": "Zīmē rūtiņās!",
              "jaut": [("Uzzīmē simetrisku figūru!", 1),
                       ("Novelc tās simetrijas asi!", 1),
                       ("Uzraksti, kā pārbaudīt, vai papīra figūra ir "
                        "simetriska!", 1)],
              "atbildes": [
                  "1) Uzzīmēta simetriska figūra.   (1 p.)",
                  "2) Novilkta ass, pa kuru abas puses sakrīt.   (1 p.)",
                  "3) Atbilde: figūru pārloka uz pusēm un skatās, vai puses "
                  "sakrīt.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
