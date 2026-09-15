# -*- coding: utf-8 -*-
"""Matemātika, 3. klase. 3.3. Kā veido vietas plānu?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 3. klase, 3.3. temats): telpas plāns kā
samazināts attēls, visu lielumu samazināšana vienādu skaitu reižu, trīs un
četru ciparu skaitļi, garuma izteikšana metros un centimetros, reizināšana
un dalīšana ar 10 un 100, mērījumu noapaļošana līdz pilniem desmitiem,
mērījumu tabula.
"""

PRIEKSMETS = "Matemātika  |  3. klase"
TEMATS = "3.3."
NOSAUKUMS = "Kā veido vietas plānu?"

ATGADNE = [
    "Plāns ir samazināts telpas attēls: visi garumi samazināti vienādu "
    "skaitu reižu.",
    "1 m = 100 cm   ·   1 cm = 10 mm   ·   1 tūkstotis = 10 simti = "
    "1000 vieni",
    "Reizinot ar 10, pieraksta vienu nulli; dalot ar 10, vienu nulli noņem.",
]

FD = {
    "veids": "fd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 3.3. temata beigās. Pārbauda plāna "
                "jēdzienu un samazinājumu, trīs un četru ciparu skaitļus, "
                "garuma izteikšanu dažādās mērvienībās, reizināšanu un "
                "dalīšanu ar 10 un 100, noapaļošanu un mērījumu tabulu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro, kas ir vietas plāns",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir telpas plāns?",
              ["samazināts telpas attēls", "telpas fotogrāfija",
               "telpas nosaukums", "telpas krāsa"], 0),
             ("Kas plānā jāparāda obligāti?",
              ["cik liels attālums dabā atbilst attālumam plānā",
               "sienu krāsa", "logu skaits", "telpas nosaukums"], 0),
             ("Kāpēc telpu nezīmē dabiskā lielumā?",
              ["tā neietilptu lapā", "tā ir aizliegts", "tas ir neinteresanti",
               "nevar izmērīt"], 0),
         ]},
        {"sr": "Skaidro samazinājumu plānā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā jāsamazina garumi, veidojot plānu?",
              ["visi vienādu skaitu reižu", "katrs savādāk",
               "tikai garākie", "tikai īsākie"], 0),
             ("Plānā 1 cm atbilst 1 m dabā. Cik cm plānā ir 5 m gara siena?",
              ["1 cm", "5 cm", "50 cm", "500 cm"], 1),
             ("Plānā 1 cm atbilst 1 m. Cik gara dabā ir siena, kas plānā ir "
              "4 cm?",
              ["4 cm", "40 cm", "4 m", "40 m"], 2),
         ]},
        {"sr": "Lasa un raksta trīs un četru ciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā ar cipariem pieraksta «tūkstotis divi simti"
              " piecdesmit»?",
              ["1250", "1025", "12050", "125"], 0),
             ("Cik simtu ir skaitlī 800?", ["8", "80", "800", "0"], 0),
             ("Cik tūkstošu ir skaitlī 3400?", ["3", "34", "300", "3400"], 0),
         ]},
        {"sr": "Zina, kā veidojas tūkstotis",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik simtu ir 1 tūkstotī?", ["10", "100", "1000", "1"], 0),
             ("Cik vienu ir 1 tūkstotī?", ["10", "100", "1000", "10000"], 2),
             ("Kurš skaitlis seko tūlīt pēc 999?",
              ["909", "990", "1000", "1010"], 2),
         ]},
        {"sr": "Izsaka garumu metros un centimetros kā centimetrus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik cm ir 2 m?", ["20", "200", "2000", "2"], 1),
             ("Cik cm ir 3 m 40 cm?", ["43", "340", "304", "3040"], 1),
             ("Cik cm ir 1 m 5 cm?", ["15", "105", "150", "1005"], 1),
         ]},
        {"sr": "Izsaka centimetrus milimetros",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik mm ir 7 cm?", ["7", "17", "70", "700"], 2),
             ("Cik mm ir 12 cm?", ["12", "112", "120", "1200"], 2),
             ("Cik cm ir 250 mm?", ["2,5", "25", "250", "2500"], 1),
         ]},
        {"sr": "Reizina ar 10 un 100",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 24 · 10?", ["34", "204", "240", "2400"], 2),
             ("Cik ir 7 · 100?", ["17", "70", "700", "7000"], 2),
             ("Cik ir 35 · 100?", ["350", "3500", "3050", "35000"], 1),
         ]},
        {"sr": "Dala ar 10 un 100",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 480 : 10?", ["4", "48", "480", "4800"], 1),
             ("Cik ir 600 : 100?", ["6", "60", "600", "6000"], 0),
             ("Cik ir 3200 : 100?", ["3", "32", "320", "3200"], 1),
         ]},
        {"sr": "Noapaļo mērījumus līdz pilniem desmitiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Noapaļo 47 cm līdz pilniem desmitiem!",
              ["40 cm", "45 cm", "50 cm", "47 cm"], 2),
             ("Noapaļo 123 cm līdz pilniem desmitiem!",
              ["100 cm", "120 cm", "125 cm", "130 cm"], 1),
             ("Noapaļo 85 cm līdz pilniem desmitiem!",
              ["80 cm", "85 cm", "90 cm", "100 cm"], 2),
         ]},
        {"sr": "Veic aprēķinus ar garumiem plānā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Istaba ir 4 m un 3 m. Cik metru ir tās perimetrs?",
              ["7 m", "12 m", "14 m", "24 m"], 2),
             ("Plānā istabas mala ir 6 cm; 1 cm atbilst 1 m. Cik metru dabā?",
              ["6 cm", "6 m", "60 m", "600 m"], 1),
             ("Divas sienas ir 250 cm un 320 cm. Cik cm kopā?",
              ["470", "560", "570", "580"], 2),
         ]},
        {"sr": "Lieto kalkulatoru un pārbauda rezultātu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad der izmantot kalkulatoru?",
              ["lieliem skaitļiem un daudziem aprēķiniem",
               "vienmēr, arī 2 + 2", "nekad", "tikai zīmējot"], 0),
             ("Kā pārbaudīt kalkulatora atbildi?",
              ["novērtēt aptuveno rezultātu", "ticēt tam vienmēr",
               "pārrakstīt to skaistāk", "nav jāpārbauda"], 0),
             ("Aptuveni cik ir 297 + 198?", ["ap 300", "ap 400", "ap 500",
                                             "ap 700"], 2),
         ]},
        {"sr": "Apkopo mērījumus tabulā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpēc mērījumus pieraksta tabulā?",
              ["lai tos būtu viegli salīdzināt un lietot", "lai aizņemtu vietu",
               "lai nevajadzētu mērīt", "lai būtu krāsaini"], 0),
             ("Tabulā: garums 350 cm, platums 280 cm. Par cik garums ir "
              "lielāks?",
              ["60 cm", "70 cm", "80 cm", "630 cm"], 1),
             ("Tabulā divas sienas: 2 m un 150 cm. Kura ir garāka?",
              ["2 m siena", "150 cm siena", "abas vienādas",
               "nevar salīdzināt"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 3.3. temata noslēgumā. "
                "Pārbauda plāna jēdzienu un samazinājumu, mērvienību "
                "pārveidošanu, reizināšanu un dalīšanu ar 10 un 100, "
                "noapaļošanu, aprēķinus ar garumiem un plāna zīmēšanu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Zīmē ar lineālu un risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Skaidro plānu un samazinājumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir telpas plāns?",
              ["samazināts telpas attēls", "telpas fotogrāfija",
               "telpas nosaukums", "telpas krāsa"], 0),
             ("Kā samazina garumus plānā?",
              ["visus vienādu skaitu reižu", "katru savādāk", "tikai garākos",
               "tikai īsākos"], 0),
             ("Plānā 1 cm atbilst 1 m. Cik cm plānā ir 7 m siena?",
              ["1 cm", "7 cm", "70 cm", "700 cm"], 1),
         ]},
        {"sr": "Lasa trīs un četru ciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik simtu ir 1 tūkstotī?", ["10", "100", "1000", "1"], 0),
             ("Kā pieraksta «divi tūkstoši četri simti»?",
              ["2400", "2040", "240", "24000"], 0),
             ("Kurš skaitlis seko pēc 999?", ["990", "1000", "1010", "909"],
              1),
         ]},
        {"sr": "Pārveido garuma mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik cm ir 3 m?", ["30", "300", "3000", "3"], 1),
             ("Cik cm ir 2 m 60 cm?", ["62", "260", "206", "2060"], 1),
             ("Cik mm ir 9 cm?", ["9", "19", "90", "900"], 2),
         ]},
        {"sr": "Reizina un dala ar 10 un 100",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 36 · 10?", ["46", "306", "360", "3600"], 2),
             ("Cik ir 8 · 100?", ["18", "80", "800", "8000"], 2),
             ("Cik ir 750 : 10?", ["7", "75", "750", "7500"], 1),
         ]},
        {"sr": "Noapaļo mērījumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Noapaļo 62 cm līdz pilniem desmitiem!",
              ["60 cm", "65 cm", "70 cm", "62 cm"], 0),
             ("Noapaļo 148 cm līdz pilniem desmitiem!",
              ["140 cm", "145 cm", "150 cm", "200 cm"], 2),
             ("Noapaļo 95 cm līdz pilniem desmitiem!",
              ["90 cm", "95 cm", "100 cm", "1000 cm"], 2),
         ]},
        {"sr": "Veic aprēķinus ar garumiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Istaba 5 m un 4 m. Perimetrs?",
              ["9 m", "18 m", "20 m", "45 m"], 1),
             ("Divas sienas 180 cm un 220 cm. Kopā?",
              ["300 cm", "380 cm", "400 cm", "420 cm"], 2),
             ("Siena ir 320 cm. Cik tas ir metros un centimetros?",
              ["3 m 20 cm", "32 m", "3 m 2 cm", "320 m"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pārveido garuma mērvienības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Izsaki norādītajās mērvienībās",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("4 m = …… cm", "400"), ("2 m 30 cm = …… cm", "230"),
                         ("8 cm = …… mm", "80"), ("500 cm = …… m", "5")]},
             {"tips": "parveide", "virs": "Izsaki norādītajās mērvienībās",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("6 m = …… cm", "600"), ("1 m 45 cm = …… cm", "145"),
                         ("12 cm = …… mm", "120"), ("700 cm = …… m", "7")]},
             {"tips": "parveide", "virs": "Izsaki norādītajās mērvienībās",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("9 m = …… cm", "900"), ("3 m 5 cm = …… cm", "305"),
                         ("15 cm = …… mm", "150"), ("400 cm = …… m", "4")]},
         ]},
        {"sr": "Reizina un dala ar 10 un 100, noapaļo",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini un noapaļo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("45 · 10 = ……", "450"), ("2600 : 100 = ……", "26"),
                         ("Noapaļo 78 cm līdz desmitiem:  ……", "80 cm")]},
             {"tips": "parveide", "virs": "Aprēķini un noapaļo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("32 · 100 = ……", "3200"), ("890 : 10 = ……", "89"),
                         ("Noapaļo 134 cm līdz desmitiem:  ……", "130 cm")]},
             {"tips": "parveide", "virs": "Aprēķini un noapaļo",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("64 · 10 = ……", "640"), ("1500 : 100 = ……", "15"),
                         ("Noapaļo 55 cm līdz desmitiem:  ……", "60 cm")]},
         ]},
        {"sr": "Zīmē telpas plānu samazinātā mērogā",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Istabas plāns", "vieta": 7.0,
              "ievads": "Istaba ir taisnstūris 5 m × 3 m. Plānā 1 m atbilst "
                        "1 cm.",
              "jaut": [("Uzzīmē istabas plānu ar lineālu!", 1),
                       ("Pieraksti plānā abu malu garumus!", 1),
                       ("Aprēķini istabas perimetru dabā!", 1),
                       ("Uzraksti, cik reižu plāns ir samazināts!", 1)],
              "atbildes": ["1) Uzzīmēts taisnstūris 5 cm × 3 cm.   (1 p.)",
                           "2) Pierakstīts 5 m un 3 m.   (1 p.)",
                           "3) P = 2 · (5 + 3) = 16 m   (1 p.)",
                           "4) 1 m = 100 cm, plānā 1 cm → samazināts "
                           "100 reižu.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Istabas plāns", "vieta": 7.0,
              "ievads": "Istaba ir taisnstūris 6 m × 4 m. Plānā 1 m atbilst "
                        "1 cm.",
              "jaut": [("Uzzīmē istabas plānu ar lineālu!", 1),
                       ("Pieraksti plānā abu malu garumus!", 1),
                       ("Aprēķini istabas perimetru dabā!", 1),
                       ("Uzraksti, cik reižu plāns ir samazināts!", 1)],
              "atbildes": ["1) Uzzīmēts taisnstūris 6 cm × 4 cm.   (1 p.)",
                           "2) Pierakstīts 6 m un 4 m.   (1 p.)",
                           "3) P = 2 · (6 + 4) = 20 m   (1 p.)",
                           "4) 1 m = 100 cm, plānā 1 cm → samazināts "
                           "100 reižu.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Istabas plāns", "vieta": 7.0,
              "ievads": "Istaba ir taisnstūris 7 m × 2 m. Plānā 1 m atbilst "
                        "1 cm.",
              "jaut": [("Uzzīmē istabas plānu ar lineālu!", 1),
                       ("Pieraksti plānā abu malu garumus!", 1),
                       ("Aprēķini istabas perimetru dabā!", 1),
                       ("Uzzīmē plānā galdu, kas dabā ir 2 m × 1 m!", 1)],
              "atbildes": ["1) Uzzīmēts taisnstūris 7 cm × 2 cm.   (1 p.)",
                           "2) Pierakstīts 7 m un 2 m.   (1 p.)",
                           "3) P = 2 · (7 + 2) = 18 m   (1 p.)",
                           "4) Plānā uzzīmēts taisnstūris 2 cm × 1 cm.   "
                           "(1 p.)"]},
         ]},
        {"sr": "Apkopo mērījumus tabulā un salīdzina",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Mērījumu tabula", "vieta": 5.5,
              "ievads": "Sienu garumi: 320 cm, 2 m 50 cm un 180 cm.",
              "jaut": [("Izsaki visus garumus centimetros!", 1),
                       ("Uzraksti tos augošā secībā!", 1),
                       ("Aprēķini, par cik garākā siena pārsniedz īsāko!", 1)],
              "atbildes": ["1) 320 cm, 250 cm, 180 cm   (1 p.)",
                           "2) 180 cm, 250 cm, 320 cm   (1 p.)",
                           "3) 320 − 180 = 140 cm   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Mērījumu tabula", "vieta": 5.5,
              "ievads": "Sienu garumi: 4 m, 270 cm un 3 m 10 cm.",
              "jaut": [("Izsaki visus garumus centimetros!", 1),
                       ("Uzraksti tos dilstošā secībā!", 1),
                       ("Aprēķini, par cik garākā siena pārsniedz īsāko!", 1)],
              "atbildes": ["1) 400 cm, 270 cm, 310 cm   (1 p.)",
                           "2) 400 cm, 310 cm, 270 cm   (1 p.)",
                           "3) 400 − 270 = 130 cm   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Mērījumu tabula", "vieta": 5.5,
              "ievads": "Sienu garumi: 150 cm, 1 m 90 cm un 2 m.",
              "jaut": [("Izsaki visus garumus centimetros!", 1),
                       ("Uzraksti tos augošā secībā!", 1),
                       ("Aprēķini visu triju sienu kopgarumu!", 1)],
              "atbildes": ["1) 150 cm, 190 cm, 200 cm   (1 p.)",
                           "2) 150 cm, 190 cm, 200 cm   (1 p.)",
                           "3) 150 + 190 + 200 = 540 cm   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
