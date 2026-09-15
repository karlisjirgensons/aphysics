# -*- coding: utf-8 -*-
"""Matemātika, 4. klase. 4.5. Kā salīdzina, saskaita un atņem daļskaitļus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 4. klase, 4.5. temats): daļas vieta uz
skaitļu taisnes, īsta un neīsta daļa, daļu saskaitīšana un atņemšana ar
vienādiem saucējiem, skaitļa 1 pieraksts ar daļu, neīstas daļas izteikšana
ar veselā un daļas summu, daļa kā pamatdaļu summa un kā reizinājums,
pamatdaļu salīdzināšana (saucēji nepārsniedz 10).
"""

PRIEKSMETS = "Matemātika  |  4. klase"
TEMATS = "4.5."
NOSAUKUMS = "Kā salīdzina, saskaita un atņem daļskaitļus?"

ATGADNE = [
    "Daļai augšā ir skaitītājs, apakšā — saucējs:   {3|4}      ·      "
    "īstai daļai skaitītājs ir mazāks nekā saucējs",
    "Daļas ar vienādiem saucējiem saskaita un atņem, darbību veicot ar "
    "skaitītājiem:   {3|8} + {2|8} = {5|8}",
    "Veselais:   1 = {5|5} = {8|8}      ·      lielāka ir tā pamatdaļa, "
    "kurai saucējs ir mazāks:   {1|3} > {1|5}",
]

FD = {
    "veids": "fd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 4.5. temata beigās. Pārbauda daļas "
                "elementus, īstas un neīstas daļas, daļu salīdzināšanu, "
                "saskaitīšanu un atņemšanu ar vienādiem saucējiem, veselā "
                "pierakstu ar daļu un daļas reizināšanu ar veselu skaitli.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosauc daļas elementus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc skaitli virs daļas svītras?",
              ["skaitītājs", "saucējs", "reizinātājs", "dalītājs"], 0),
             ("Kā sauc skaitli zem daļas svītras?",
              ["saucējs", "skaitītājs", "summa", "starpība"], 0),
             ("Ko rāda daļas {3|8} saucējs?",
              ["cik vienādās daļās sadalīts veselais", "cik daļas paņemtas",
               "cik ir kopā", "cik paliek"], 0),
         ]},
        {"sr": "Atšķir īstu un neīstu daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura daļa ir īsta?", ["{3|5}", "{5|3}", "{7|7}", "{9|4}"], 0),
             ("Kura daļa ir neīsta?",
              ["{7|4}", "{2|5}", "{1|3}", "{3|8}"], 0),
             ("Kāda ir īsta daļa?",
              ["lielāka nekā 0 un mazāka nekā 1", "lielāka nekā 1",
               "vienāda ar 1", "mazāka nekā 0"], 0),
         ]},
        {"sr": "Nosaka daļas vietu uz skaitļu taisnes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Starp kuriem skaitļiem atrodas {3|4}?",
              ["starp 0 un 1", "starp 1 un 2", "starp 2 un 3", "aiz 3"], 0),
             ("Starp kuriem skaitļiem atrodas {7|5}?",
              ["starp 1 un 2", "starp 0 un 1", "starp 2 un 3", "aiz 5"], 0),
             ("Kura daļa uz skaitļu taisnes ir vistuvāk 0?",
              ["{1|9}", "{1|2}", "{1|3}", "{1|5}"], 0),
         ]},
        {"sr": "Salīdzina pamatdaļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura daļa ir vislielākā?",
              ["{1|3}", "{1|5}", "{1|8}", "{1|10}"], 0),
             ("Kura pamatdaļa ir vismazākā?",
              ["{1|10}", "{1|2}", "{1|4}", "{1|7}"], 0),
             ("Kāpēc {1|3} ir lielāka nekā {1|5}?",
              ["veselais sadalīts mazāk daļās", "saucējs ir lielāks",
               "skaitītājs ir lielāks", "tā nav"], 0),
         ]},
        {"sr": "Salīdzina daļas ar vienādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura daļa ir lielāka?",
              ["{5|7}", "{3|7}", "{2|7}", "{1|7}"], 0),
             ("Kura zīme jāliek:  {2|9} …… {6|9}?", ["<", ">", "=", "+"], 0),
             ("Kā salīdzina daļas ar vienādiem saucējiem?",
              ["salīdzina skaitītājus", "salīdzina saucējus",
               "tās saskaita", "tās nesalīdzina"], 0),
         ]},
        {"sr": "Saskaita daļas ar vienādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {3|8} + {2|8}?",
              ["{5|8}", "{5|16}", "{6|8}", "{1|8}"], 0),
             ("Cik ir {2|5} + {1|5}?",
              ["{3|5}", "{3|10}", "{2|5}", "{3|25}"], 0),
             ("Kā saskaita daļas ar vienādiem saucējiem?",
              ["saskaita skaitītājus, saucēju atstāj", "saskaita abus",
               "saskaita saucējus", "tās sareizina"], 0),
         ]},
        {"sr": "Atņem daļas ar vienādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {7|9} − {4|9}?",
              ["{3|9}", "{3|18}", "{11|9}", "{4|9}"], 0),
             ("Cik ir {5|6} − {1|6}?",
              ["{4|6}", "{4|12}", "{6|6}", "{5|6}"], 0),
             ("Cik ir 1 − {3|8}?",
              ["{5|8}", "{3|8}", "{8|3}", "{5|16}"], 0),
         ]},
        {"sr": "Pieraksta veselo ar daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā ar daļu pieraksta 1, ja saucējs ir 5?",
              ["{5|5}", "{1|5}", "{5|1}", "{0|5}"], 0),
             ("Cik ir {6|6}?", ["1", "6", "0", "{1|6}"], 0),
             ("Kura daļa ir vienāda ar 1?",
              ["{9|9}", "{9|1}", "{1|9}", "{8|9}"], 0),
         ]},
        {"sr": "Izsaka neīstu daļu ar veselo un daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā izsaka {7|5} ar veselo un daļu?",
              ["1 un {2|5}", "2 un {1|5}", "1 un {5|2}", "7 un {1|5}"], 0),
             ("Kā izsaka {9|4} ar veselo un daļu?",
              ["2 un {1|4}", "4 un {1|9}", "2 un {1|2}", "1 un {5|4}"], 0),
             ("Kura daļa ir lielāka nekā 2?",
              ["{9|4}", "{7|4}", "{5|4}", "{3|4}"], 0),
         ]},
        {"sr": "Pieraksta daļu kā pamatdaļu summu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā {3|4} pieraksta ar pamatdaļām?",
              ["{1|4} + {1|4} + {1|4}", "{1|4} + {1|4}", "{3|4} + {3|4}",
               "{1|3} + {1|4}"], 0),
             ("Cik pamatdaļu {1|8} ir daļā {5|8}?", ["5", "8", "3", "13"],
              0),
             ("Kā {3|4} pieraksta kā reizinājumu?",
              ["3 · {1|4}", "4 · {1|3}", "3 · {1|3}", "{1|4} · {1|4}"], 0),
         ]},
        {"sr": "Reizina daļu ar veselu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3 · {1|5}?",
              ["{3|5}", "{1|15}", "{3|15}", "{5|3}"], 0),
             ("Cik ir 4 · {2|9}?",
              ["{8|9}", "{8|36}", "{6|9}", "{2|36}"], 0),
             ("Cik ir 5 · {1|5}?", ["1", "{1|25}", "5", "{5|25}"], 0),
         ]},
        {"sr": "Lieto daļas praktiskā situācijā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Torte sagriezta 8 vienādos gabalos. Kāda daļa ir viens "
              "gabals?", ["{1|8}", "{8|1}", "{1|4}", "{2|8}"], 0),
             ("Anna apēda {2|8}, Jānis — {3|8} tortes. Cik kopā?",
              ["{5|8}", "{5|16}", "{6|8}", "{1|8}"], 0),
             ("Cik tortes palika, ja apēsti {5|8}?",
              ["{3|8}", "{5|8}", "{8|5}", "{3|16}"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 4.5. temata noslēgumā. "
                "Pārbauda daļas elementus, īstas un neīstas daļas, daļu "
                "salīdzināšanu, saskaitīšanu un atņemšanu ar vienādiem "
                "saucējiem, veselā pierakstu ar daļu un daļas lietojumu "
                "situāciju uzdevumos.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus un zīmējumus veido tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Nosauc daļas elementus un atšķir daļu veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc skaitli zem daļas svītras?",
              ["saucējs", "skaitītājs", "summa", "reizinātājs"], 0),
             ("Kura daļa ir īsta?", ["{2|7}", "{7|2}", "{5|5}", "{8|3}"], 0),
             ("Kura daļa ir neīsta?",
              ["{9|5}", "{3|5}", "{1|5}", "{4|5}"], 0),
         ]},
        {"sr": "Salīdzina daļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura daļa ir lielāka?",
              ["{6|9}", "{4|9}", "{2|9}", "{1|9}"], 0),
             ("Kura pamatdaļa ir vislielākā?",
              ["{1|2}", "{1|4}", "{1|6}", "{1|9}"], 0),
             ("Kura zīme jāliek:  {3|10} …… {8|10}?",
              ["<", ">", "=", "·"], 0),
         ]},
        {"sr": "Saskaita un atņem daļas ar vienādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {2|9} + {5|9}?",
              ["{7|9}", "{7|18}", "{3|9}", "{10|9}"], 0),
             ("Cik ir {8|10} − {3|10}?",
              ["{5|10}", "{5|20}", "{11|10}", "{5|7}"], 0),
             ("Cik ir 1 − {1|4}?", ["{3|4}", "{1|4}", "{4|3}", "{3|8}"], 0),
         ]},
        {"sr": "Pieraksta veselo ar daļu un izsaka neīstu daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {7|7}?", ["1", "7", "0", "{1|7}"], 0),
             ("Kā izsaka {11|4} ar veselo un daļu?",
              ["2 un {3|4}", "3 un {1|4}", "2 un {1|4}", "4 un {3|11}"], 0),
             ("Kā ar daļu pieraksta 1, ja saucējs ir 9?",
              ["{9|9}", "{1|9}", "{9|1}", "{0|9}"], 0),
         ]},
        {"sr": "Pieraksta daļu ar pamatdaļām un reizina ar veselu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik pamatdaļu {1|6} ir daļā {4|6}?", ["4", "6", "2", "10"],
              0),
             ("Cik ir 3 · {2|7}?",
              ["{6|7}", "{6|21}", "{5|7}", "{2|21}"], 0),
             ("Kā {2|5} pieraksta kā reizinājumu?",
              ["2 · {1|5}", "5 · {1|2}", "2 · {1|2}", "{1|5} · {1|5}"], 0),
         ]},
        {"sr": "Lieto daļas praktiskā situācijā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pica sagriezta 6 gabalos. Kāda daļa ir divi gabali?",
              ["{2|6}", "{6|2}", "{1|6}", "{2|3}"], 0),
             ("Klasē no 10 skolēniem 3 brauc ar velosipēdu. Kāda daļa tā "
              "ir?", ["{3|10}", "{10|3}", "{1|3}", "{7|10}"], 0),
             ("Cik grāmatas palika izlasīt, ja izlasīti {4|9}?",
              ["{5|9}", "{4|9}", "{9|4}", "{5|18}"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita, atņem un reizina daļas",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{3|8} + {2|8} = ……", "{5|8}"),
                         ("{7|9} − {4|9} = ……", "{3|9}"),
                         ("1 − {2|5} = ……", "{3|5}"),
                         ("3 · {1|4} = ……", "{3|4}")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{2|7} + {3|7} = ……", "{5|7}"),
                         ("{5|6} − {1|6} = ……", "{4|6}"),
                         ("1 − {3|8} = ……", "{5|8}"),
                         ("4 · {1|5} = ……", "{4|5}")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{4|10} + {3|10} = ……", "{7|10}"),
                         ("{8|9} − {5|9} = ……", "{3|9}"),
                         ("1 − {1|4} = ……", "{3|4}"),
                         ("2 · {3|7} = ……", "{6|7}")]},
         ]},
        {"sr": "Salīdzina daļas",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti zīmi  <,  >  vai  =",
              "note": "Ieraksti pareizo zīmi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{3|7} …… {5|7}", "<"), ("{1|3} …… {1|6}", ">"),
                         ("{4|4} …… 1", "=")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  <,  >  vai  =",
              "note": "Ieraksti pareizo zīmi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{6|9} …… {2|9}", ">"), ("{1|5} …… {1|2}", "<"),
                         ("{7|7} …… 1", "=")]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  <,  >  vai  =",
              "note": "Ieraksti pareizo zīmi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{2|8} …… {7|8}", "<"), ("{1|4} …… {1|9}", ">"),
                         ("{5|5} …… 1", "=")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar daļām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Tortei bija 12 vienādi gabali. Anna paņēma 3 "
                        "gabalus, bet Jānis — 4. Kādu daļu tortes paņēma "
                        "katrs? Kādu daļu viņi paņēma kopā? Kāda daļa "
                        "palika?",
              "kriteriji": ["Anna paņēma {3|12}.   (1 p.)",
                            "Jānis paņēma {4|12}.   (1 p.)",
                            "Kopā {3|12} + {4|12} = {7|12}.   (1 p.)",
                            "Palika {5|12}.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Klasē ir 20 skolēni. Futbolu spēlē 5, bet "
                        "volejbolu — 7 skolēni. Kādu daļu klases veido "
                        "futbolisti? Kādu — volejbolisti? Kādu daļu abi "
                        "kopā? Kāda daļa nespēlē nevienu no šīm spēlēm?",
              "kriteriji": ["Futbolisti {5|20}.   (1 p.)",
                            "Volejbolisti {7|20}.   (1 p.)",
                            "Kopā {5|20} + {7|20} = {12|20}.   (1 p.)",
                            "Nespēlē {8|20}.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Grāmatā ir 60 lappuses. Pirmajā dienā Ieva "
                        "izlasīja 20 lappuses, otrajā — 25. Kādu daļu viņa "
                        "izlasīja pirmajā dienā? Kādu — otrajā? Kādu daļu "
                        "kopā? Cik lappušu palika?",
              "kriteriji": ["Pirmajā dienā {20|60}.   (1 p.)",
                            "Otrajā dienā {25|60}.   (1 p.)",
                            "Kopā {20|60} + {25|60} = {45|60}.   (1 p.)",
                            "Palika 15 lappuses.   (1 p.)"]},
         ]},
        {"sr": "Attēlo daļu zīmējumā vai uz skaitļu taisnes",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Daļas uz skaitļu taisnes",
              "vieta": 5.5,
              "ievads": "Uzzīmē skaitļu taisni no 0 līdz 2 un sadali katru "
                        "vienību 4 vienādās daļās!",
              "jaut": [("Atzīmē uz tās {1|2}!", 1),
                       ("Atzīmē uz tās {5|4}!", 1),
                       ("Kura no abām daļām ir lielāka?", 1)],
              "atbildes": ["1) Atzīmēts punkts starp 0 un 1 — tieši pa "
                           "vidu.   (1 p.)",
                           "2) Atzīmēts punkts starp 1 un 2.   (1 p.)",
                           "3) Lielāka ir {5|4}.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Daļa zīmējumā", "vieta": 5.5,
              "ievads": "Rūtiņās uzzīmē taisnstūri, kas ir 8 rūtiņas plats "
                        "un 1 rūtiņu augsts!",
              "jaut": [("Iekrāso {3|8} no tā!", 1),
                       ("Cik rūtiņu ir iekrāsotas?", 1),
                       ("Kādu daļu veido neiekrāsotās rūtiņas?", 1)],
              "atbildes": ["1) Iekrāsotas 3 rūtiņas no 8.   (1 p.)",
                           "2) Trīs rūtiņas.   (1 p.)",
                           "3) Neiekrāsotās veido {5|8}.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Neīsta daļa", "vieta": 5.5,
              "ievads": "Dota neīsta daļa  {11|4}.",
              "jaut": [("Izsaki to ar veselo un daļu!", 1),
                       ("Starp kuriem veseliem skaitļiem tā atrodas?", 1),
                       ("Atzīmē to uz skaitļu taisnes!", 1)],
              "atbildes": ["1) 2 un {3|4}.   (1 p.)",
                           "2) Starp 2 un 3.   (1 p.)",
                           "3) Atzīmēts punkts starp 2 un 3, tuvāk 3. "
                           "  (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
