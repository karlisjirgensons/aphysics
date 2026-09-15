# -*- coding: utf-8 -*-
"""Matemātika, 6. klase. 6.2. Kā reizina un dala parastās daļas?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 6. klase, 6.2. temats): divu daļu
reizināšana, reizinājuma modelēšana 1 × 1 kvadrātā, apgrieztais skaitlis,
dalīšana ar daļu kā reizināšana ar apgriezto skaitli, jauktu skaitļu
pierakstīšana kā neīstas daļas, reizinājuma un dalījuma aptuvenā vērtība un
situāciju uzdevumi.
"""

PRIEKSMETS = "Matemātika  |  6. klase"
TEMATS = "6.2."
NOSAUKUMS = "Kā reizina un dala parastās daļas?"

ATGADNE = [
    "Daļas reizina pa skaitītājiem un saucējiem:   {a|b} · {m|n} = "
    "{a · m|b · n}      ·      piemēram   {2|3} · {3|5} = {6|15} = {2|5}",
    "Savstarpēji apgrieztu skaitļu reizinājums ir 1:   {3|4} · {4|3} = 1  "
    " ·   dalīšana:   {a|b} : {m|n} = {a|b} · {n|m}",
    "Jauktu skaitli vispirms pieraksta kā neīstu daļu:   2{1|2} = {5|2}  "
    " ·   rezultātu saīsina un, ja iespējams, pieraksta kā jauktu skaitli.",
]

FD = {
    "veids": "fd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 6.2. temata beigās. Pārbauda daļu "
                "reizināšanu un dalīšanu, apgriezto skaitli, jauktu skaitļu "
                "pārveidošanu, rezultāta saīsināšanu un novērtēšanu, kā arī "
                "situāciju uzdevumus ar daļām.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina daļu reizināšanas noteikumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā reizina divas daļas?",
              ["skaitītāju ar skaitītāju", "skaitītāju ar saucēju",
               "saucēju ar skaitītāju", "tās saskaita"], 0),
             ("Cik ir {2|3} · {1|5}?",
              ["{2|15}", "{3|15}", "{2|8}", "{5|6}"], 0),
             ("Cik ir {3|4} · {2|5}?",
              ["{3|10}", "{6|9}", "{5|9}", "{3|20}"], 0),
         ]},
        {"sr": "Reizina daļu ar veselu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {2|7} · 3?", ["{6|7}", "{2|21}", "{5|7}", "{6|21}"], 0),
             ("Cik ir {3|8} · 4?", ["{3|2}", "{3|32}", "{7|8}", "{12|32}"], 0),
             ("Kā daļu reizina ar veselu skaitli?",
              ["skaitītāju reizina ar to", "saucēju reizina ar to",
               "abus reizina", "abus saskaita"], 0),
         ]},
        {"sr": "Modelē daļu reizinājumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda reizinātāji 1 × 1 kvadrātā?",
              ["kādu daļu ņem no katras malas", "kvadrāta laukumu",
               "kvadrāta perimetru", "malu garumu"], 0),
             ("Ko rāda rezultāts 1 × 1 kvadrātā?",
              ["daļu no kvadrāta laukuma", "malas garumu", "perimetru",
               "virsotņu skaitu"], 0),
             ("Cik liela ir puse no {1|2}?",
              ["{1|4}", "{1|2}", "{2|2}", "{1|3}"], 0),
         ]},
        {"sr": "Spriež par reizinājuma lielumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko reizinot, rezultāts ir mazāks nekā skaitlis?",
              ["ar īstu daļu", "ar veselu skaitli", "ar neīstu daļu",
               "ar 1"], 0),
             ("Vai {3|4} · 8 ir lielāks nekā 8?",
              ["nē", "jā", "vienāds", "nevar noteikt"], 0),
             ("Kurš reizinājums ir lielāks nekā 10?",
              ["{5|4} · 10", "{3|4} · 10", "{1|2} · 10", "{2|5} · 10"], 0),
         ]},
        {"sr": "Nosaka apgriezto skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir skaitļa {3|5} apgrieztais skaitlis?",
              ["{5|3}", "{3|5}", "{1|5}", "{1|3}"], 0),
             ("Kāds ir skaitļa 4 apgrieztais skaitlis?",
              ["{1|4}", "4", "{4|1}", "−4"], 0),
             ("Cik ir savstarpēji apgrieztu skaitļu reizinājums?",
              ["1", "0", "2", "tas ir dažāds"], 0),
         ]},
        {"sr": "Dala ar daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā dala ar daļu?",
              ["reizina ar apgriezto skaitli", "reizina ar to pašu daļu",
               "saskaita daļas", "atņem daļas"], 0),
             ("Cik ir {1|2} : {1|4}?", ["2", "{1|8}", "{1|2}", "8"], 0),
             ("Cik ir {3|5} : {2|5}?",
              ["{3|2}", "{2|3}", "{6|25}", "{5|3}"], 0),
         ]},
        {"sr": "Dala daļu ar veselu skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {4|5} : 2?", ["{2|5}", "{8|5}", "{4|10}", "{2|10}"], 0),
             ("Cik ir {6|7} : 3?", ["{2|7}", "{18|7}", "{6|21}", "{2|21}"], 0),
             ("Kā daļu dala ar veselu skaitli?",
              ["saucēju reizina ar to", "skaitītāju reizina ar to",
               "abus dala", "abus saskaita"], 0),
         ]},
        {"sr": "Pārveido jauktu skaitli par neīstu daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā neīstu daļu pieraksta 2{1|2}?",
              ["{5|2}", "{3|2}", "{2|5}", "{4|2}"], 0),
             ("Kā neīstu daļu pieraksta 1{2|3}?",
              ["{5|3}", "{3|5}", "{2|3}", "{6|3}"], 0),
             ("Kā jauktu skaitli pārveido par neīstu daļu?",
              ["veselos reizina ar saucēju un pieskaita skaitītāju",
               "veselos saskaita ar saucēju", "veselos dala ar saucēju",
               "skaitītāju reizina ar saucēju"], 0),
         ]},
        {"sr": "Reizina jauktus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 1{1|2} · 2?", ["3", "2{1|2}", "1{1|4}", "{3|4}"], 0),
             ("Cik ir 2{1|3} · 3?", ["7", "6{1|3}", "2{1|9}", "{7|9}"], 0),
             ("Kas jādara vispirms, reizinot jauktus skaitļus?",
              ["jāpieraksta kā neīstas daļas", "jāsaskaita veselie",
               "jāsaīsina saucēji", "jādala ar saucēju"], 0),
         ]},
        {"sr": "Dala jauktus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 1{1|2} : {1|2}?", ["3", "{3|4}", "{1|3}", "2"], 0),
             ("Cik ir 2{1|2} : 5?", ["{1|2}", "2", "{5|2}", "{1|5}"], 0),
             ("Cik ir {3|4} : 1{1|2}?",
              ["{1|2}", "2", "{9|8}", "{4|3}"], 0),
         ]},
        {"sr": "Saīsina un novērtē rezultātu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Saīsini {6|15}.", ["{2|5}", "{5|2}", "{3|5}", "{1|5}"], 0),
             ("Cik aptuveni ir {1|3} · 9?", ["3", "9", "27", "12"], 0),
             ("Cik aptuveni ir 10 : {1|2}?", ["20", "5", "10", "2"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus ar daļām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {2|3} no 45 kg?",
              ["30 kg", "15 kg", "67 kg", "22 kg"], 0),
             ("Lentu 6 m sagriež {1|2} m gabalos. Cik gabalu sanāk?",
              ["12", "3", "6", "8"], 0),
             ("Recepte prasa {3|4} l piena; gatavo pusi devas. Cik piena "
              "vajag?", ["{3|8} l", "{3|2} l", "{1|4} l", "{6|4} l"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 6.2. temata noslēgumā. "
                "Pārbauda daļu un jauktu skaitļu reizināšanu un dalīšanu, "
                "apgriezto skaitli, rezultāta saīsināšanu un novērtēšanu un "
                "situāciju uzdevumus ar daļām.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus pieraksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Reizina parastās daļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {3|5} · {1|2}?",
              ["{3|10}", "{4|7}", "{3|7}", "{5|6}"], 0),
             ("Cik ir {2|9} · 3?", ["{2|3}", "{6|27}", "{5|9}", "{2|27}"], 0),
             ("Kā reizina divas daļas?",
              ["skaitītāju ar skaitītāju", "skaitītāju ar saucēju",
               "saucēju ar skaitītāju", "tās saskaita"], 0),
         ]},
        {"sr": "Nosaka apgriezto skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir skaitļa {2|7} apgrieztais skaitlis?",
              ["{7|2}", "{2|7}", "{1|7}", "{1|2}"], 0),
             ("Kāds ir skaitļa 5 apgrieztais skaitlis?",
              ["{1|5}", "5", "{5|1}", "−5"], 0),
             ("Cik ir savstarpēji apgrieztu skaitļu reizinājums?",
              ["1", "0", "2", "tas ir dažāds"], 0),
         ]},
        {"sr": "Dala ar daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {3|4} : {1|4}?", ["3", "{3|16}", "{1|3}", "4"], 0),
             ("Cik ir {5|6} : 5?", ["{1|6}", "{25|6}", "{5|30}", "6"], 0),
             ("Kā dala ar daļu?",
              ["reizina ar apgriezto skaitli", "reizina ar to pašu daļu",
               "saskaita daļas", "atņem daļas"], 0),
         ]},
        {"sr": "Lieto jauktus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā neīstu daļu pieraksta 3{1|2}?",
              ["{7|2}", "{4|2}", "{3|2}", "{6|2}"], 0),
             ("Cik ir 1{1|4} · 4?", ["5", "4{1|4}", "1", "{5|16}"], 0),
             ("Cik ir 2{1|2} : {1|2}?", ["5", "{5|4}", "{1|5}", "2"], 0),
         ]},
        {"sr": "Saīsina un novērtē rezultātu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Saīsini {8|20}.", ["{2|5}", "{5|2}", "{4|5}", "{1|5}"], 0),
             ("Vai {2|3} · 12 ir lielāks nekā 12?",
              ["nē", "jā", "vienāds", "nevar noteikt"], 0),
             ("Cik ir 8 : {1|4}?", ["32", "2", "{1|32}", "4"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {3|4} no 60 eiro?",
              ["45 eiro", "15 eiro", "80 eiro", "20 eiro"], 0),
             ("Auklu 9 m sagriež {3|4} m gabalos. Cik gabalu sanāk?",
              ["12", "6", "9", "27"], 0),
             ("Cik ir {1|3} no 2{1|4} l?",
              ["{3|4} l", "{1|4} l", "{9|4} l", "{2|3} l"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Izpilda darbības ar daļām",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi nesaīsināmas daļas veidā! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("{2|3} · {3|4} = ……", "{1|2}"),
                         ("{4|5} · 10 = ……", "8"),
                         ("{3|4} : {1|2} = ……", "{3|2}"),
                         ("{5|6} : 5 = ……", "{1|6}")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi nesaīsināmas daļas veidā! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("{3|5} · {5|6} = ……", "{1|2}"),
                         ("{2|7} · 14 = ……", "4"),
                         ("{5|8} : {1|4} = ……", "{5|2}"),
                         ("{9|10} : 3 = ……", "{3|10}")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi nesaīsināmas daļas veidā! Par katru "
                      "pareizu atbildi — 1 punkts.",
              "rindas": [("{4|9} · {3|8} = ……", "{1|6}"),
                         ("{5|6} · 12 = ……", "10"),
                         ("{7|10} : {7|5} = ……", "{1|2}"),
                         ("{8|9} : 4 = ……", "{2|9}")]},
         ]},
        {"sr": "Lieto jauktus un apgrieztus skaitļus",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Pārveido un aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2{1|3} = …… (neīsta daļa)", "{7|3}"),
                         ("Skaitļa {4|5} apgrieztais skaitlis ir ……",
                          "{5|4}"),
                         ("1{1|2} · 4 = ……", "6")]},
             {"tips": "parveide", "virs": "Pārveido un aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("3{1|4} = …… (neīsta daļa)", "{13|4}"),
                         ("Skaitļa {2|9} apgrieztais skaitlis ir ……",
                          "{9|2}"),
                         ("2{1|2} · 4 = ……", "10")]},
             {"tips": "parveide", "virs": "Pārveido un aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("1{5|6} = …… (neīsta daļa)", "{11|6}"),
                         ("Skaitļa 7 apgrieztais skaitlis ir ……", "{1|7}"),
                         ("1{1|3} · 6 = ……", "8")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar daļām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Auduma gabalā ir 12 m; kleitai izlieto {2|3} no "
                        "tā.   a) Cik metru izlietoja kleitai?   b) Cik "
                        "metru palika?   c) No atlikuma šuj lakatiņus pa "
                        "{1|2} m. Cik lakatiņu sanāk?   d) Kādu daļu no "
                        "sākotnējā auduma veido viens lakatiņš?",
              "kriteriji": ["a) 12 · {2|3} = 8 m.   (1 p.)",
                            "b) 12 − 8 = 4 m.   (1 p.)",
                            "c) 4 : {1|2} = 8 lakatiņi.   (1 p.)",
                            "d) {1|2} : 12 = {1|24}.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Tvertnē ir 18 l sulas; {1|3} no tās izlej "
                        "pudelēs.   a) Cik litru izlēja?   b) Cik litru "
                        "palika?   c) Atlikumu lej {3|4} l pudelēs. Cik "
                        "pudeļu sanāk?   d) Kādu daļu no sākotnējā "
                        "daudzuma ir viena pudele?",
              "kriteriji": ["a) 18 · {1|3} = 6 l.   (1 p.)",
                            "b) 18 − 6 = 12 l.   (1 p.)",
                            "c) 12 : {3|4} = 16 pudeles.   (1 p.)",
                            "d) {3|4} : 18 = {1|24}.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Grāmatā ir 240 lappuses; pirmajā dienā izlasa "
                        "{1|4}, otrajā — {1|3} no atlikuma.   a) Cik "
                        "lappušu izlasīja pirmajā dienā?   b) Cik lappušu "
                        "palika?   c) Cik lappušu izlasīja otrajā dienā?   "
                        "d) Cik lappušu vēl atlicis?",
              "kriteriji": ["a) 240 · {1|4} = 60 lappuses.   (1 p.)",
                            "b) 240 − 60 = 180 lappuses.   (1 p.)",
                            "c) 180 · {1|3} = 60 lappuses.   (1 p.)",
                            "d) 180 − 60 = 120 lappuses.   (1 p.)"]},
         ]},
        {"sr": "Skaidro darbības ar daļām",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Reizinājums un dalījums",
              "vieta": 4.6,
              "ievads": "Dotas izteiksmes  {2|3} · 9  un  {2|3} : 9.",
              "jaut": [("Aprēķini abas izteiksmes!", 1),
                       ("Kura vērtība ir lielāka?", 1),
                       ("Paskaidro, kāpēc!", 1)],
              "atbildes": ["1) {2|3} · 9 = 6;  {2|3} : 9 = {2|27}.   (1 p.)",
                           "2) Lielāks ir reizinājums.   (1 p.)",
                           "3) Dalot ar skaitli, kas lielāks nekā 1, "
                           "rezultāts sarūk.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Apgrieztie skaitļi", "vieta": 4.6,
              "ievads": "Dots skaitlis {3|8}.",
              "jaut": [("Uzraksti tā apgriezto skaitli!", 1),
                       ("Pārbaudi, ka reizinājums ir 1!", 1),
                       ("Ar ko var aizstāt dalīšanu ar {3|8}?", 1)],
              "atbildes": ["1) {8|3}.   (1 p.)",
                           "2) {3|8} · {8|3} = {24|24} = 1.   (1 p.)",
                           "3) Ar reizināšanu ar {8|3}.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Novērtē rezultātu", "vieta": 4.6,
              "ievads": "Dotas izteiksmes  20 · {3|4}  un  20 : {3|4}.",
              "jaut": [("Kura vērtība ir mazāka nekā 20?", 1),
                       ("Aprēķini abas vērtības!", 1),
                       ("Paskaidro secinājumu!", 1)],
              "atbildes": ["1) Reizinājums 20 · {3|4}.   (1 p.)",
                           "2) 15 un {80|3} = 26{2|3}.   (1 p.)",
                           "3) Reizinot ar īstu daļu, skaitlis sarūk; dalot "
                           "ar to — aug.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
