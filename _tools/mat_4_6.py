# -*- coding: utf-8 -*-
"""Matemātika, 4. klase. 4.6. Ko nozīmē daļa no veselā?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 4. klase, 4.6. temats): veselais un tā
skaitliskā vērtība, pamatdaļas vērtības aprēķināšana (saucējs nepārsniedz 6),
daļas vērtība, veselā noteikšana, ja zināma pamatdaļa, pamatdaļas
pārveidošana lieluma mazākajās mērvienībās un daļas noteikšana no figūras
laukuma rūtiņu lapā.
"""

PRIEKSMETS = "Matemātika  |  4. klase"
TEMATS = "4.6."
NOSAUKUMS = "Ko nozīmē daļa no veselā?"

ATGADNE = [
    "Pamatdaļu atrod, veselo dalot ar saucēju:   {1|4} no 20  =  20 : 4  "
    "=  5",
    "Daļu atrod, pamatdaļu reizinot ar skaitītāju:   {3|4} no 20  =  "
    "20 : 4 · 3  =  15",
    "Ja zināma pamatdaļa, veselo atrod, reizinot ar saucēju:   {1|5} ir 6  "
    "⇒  veselais ir 6 · 5 = 30",
]

FD = {
    "veids": "fd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 4.6. temata beigās. Pārbauda veselā "
                "jēdzienu, pamatdaļas un daļas vērtības aprēķināšanu, "
                "veselā noteikšanu pēc pamatdaļas, daļu no garuma, masas, "
                "laika un naudas, kā arī daļu no figūras laukuma.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosaka, kas situācijā ir veselais",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas uzdevumā ir veselais?",
              ["viss daudzums, par ko runā", "tikai viens elements",
               "atbilde", "daļas saucējs"], 0),
             ("Grozā ir 24 āboli. Kas ir veselais?",
              ["24 āboli", "1 ābols", "{1|24}", "24 daļas"], 0),
             ("Kāpēc vispirms noskaidro veselo?",
              ["citādi nevar aprēķināt daļu", "lai uzdevums būtu garāks",
               "lai zinātu skaitītāju", "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Aprēķina pamatdaļas vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {1|4} no 20?", ["5", "4", "16", "80"], 0),
             ("Cik ir {1|6} no 30?", ["5", "6", "24", "180"], 0),
             ("Kā aprēķina pamatdaļu?",
              ["veselo dala ar saucēju", "veselo reizina ar saucēju",
               "veselo saskaita ar saucēju", "no veselā atņem saucēju"], 0),
         ]},
        {"sr": "Aprēķina daļas vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {3|4} no 20?", ["15", "5", "60", "80"], 0),
             ("Cik ir {2|5} no 30?", ["12", "6", "15", "60"], 0),
             ("Kā aprēķina {3|5} no skaitļa?",
              ["dala ar 5 un reizina ar 3", "reizina ar 5 un dala ar 3",
               "dala ar 3", "reizina ar 15"], 0),
         ]},
        {"sr": "Nosaka veselo, ja zināma pamatdaļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("{1|5} no skaitļa ir 6. Kāds ir skaitlis?",
              ["30", "11", "5", "1"], 0),
             ("{1|3} no skaitļa ir 9. Kāds ir skaitlis?",
              ["27", "12", "3", "6"], 0),
             ("Kā atrod veselo, ja zināma pamatdaļa?",
              ["reizina ar saucēju", "dala ar saucēju",
               "saskaita ar saucēju", "atņem saucēju"], 0),
         ]},
        {"sr": "Nosaka veselo, ja zināma daļa",
         "stunda": TEMATS,
         "jautajumi": [
             ("{2|5} no skaitļa ir 8. Kāds ir skaitlis?",
              ["20", "10", "16", "40"], 0),
             ("{3|4} no skaitļa ir 12. Kāds ir skaitlis?",
              ["16", "9", "48", "15"], 0),
             ("Kāds ir pirmais solis, ja zināma daļa {3|4}?",
              ["aprēķina pamatdaļu", "reizina ar 4", "saskaita 3 un 4",
               "nekas nav jādara"], 0),
         ]},
        {"sr": "Nosaka daļu no garuma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik metru ir {1|2} km?",
              ["500 m", "50 m", "5 m", "100 m"], 0),
             ("Cik metru ir {1|4} km?",
              ["250 m", "400 m", "25 m", "4 m"], 0),
             ("Cik centimetru ir {1|5} m?",
              ["20 cm", "5 cm", "50 cm", "25 cm"], 0),
         ]},
        {"sr": "Nosaka daļu no masas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik gramu ir {1|2} kg?",
              ["500 g", "50 g", "200 g", "250 g"], 0),
             ("Cik gramu ir {1|4} kg?",
              ["250 g", "400 g", "25 g", "750 g"], 0),
             ("Cik gramu ir {3|4} kg?",
              ["750 g", "250 g", "340 g", "430 g"], 0),
         ]},
        {"sr": "Nosaka daļu no laika",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik minūšu ir {1|2} stunda?",
              ["30 min", "50 min", "20 min", "15 min"], 0),
             ("Cik minūšu ir {1|4} stunda?",
              ["15 min", "25 min", "40 min", "20 min"], 0),
             ("Cik minūšu ir {3|4} stunda?",
              ["45 min", "34 min", "30 min", "75 min"], 0),
         ]},
        {"sr": "Nosaka daļu no naudas summas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik centu ir {1|2} eiro?",
              ["50 centi", "20 centi", "25 centi", "5 centi"], 0),
             ("Grāmata maksā 24 eiro. Cik ir {1|3} no cenas?",
              ["8 eiro", "3 eiro", "12 eiro", "21 eiro"], 0),
             ("Cepure maksā 20 eiro, atlaide — {1|4}. Cik liela ir atlaide?",
              ["5 eiro", "4 eiro", "15 eiro", "16 eiro"], 0),
         ]},
        {"sr": "Nosaka daļu no figūras laukuma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūrī ir 12 rūtiņas. Cik rūtiņu ir {1|3} no tā?",
              ["4", "3", "9", "36"], 0),
             ("Figūrā ir 20 rūtiņu, iekrāsotas 5. Kāda daļa ir iekrāsota?",
              ["{5|20}", "{20|5}", "{1|5}", "{15|20}"], 0),
             ("Kvadrāts sadalīts 4 vienādās daļās. Kāda daļa ir viena no "
              "tām?", ["{1|4}", "{4|1}", "{1|2}", "{3|4}"], 0),
         ]},
        {"sr": "Salīdzina daļu vērtības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir vairāk: {1|2} no 20 vai {1|4} no 20?",
              ["{1|2} no 20", "{1|4} no 20", "tie ir vienādi",
               "nevar salīdzināt"], 0),
             ("Kas ir vairāk: {1|2} no 10 vai {1|4} no 40?",
              ["{1|4} no 40", "{1|2} no 10", "tie ir vienādi",
               "nevar salīdzināt"], 0),
             ("Kāpēc {1|2} no 10 un {1|5} no 25 ir vienādi?",
              ["abi ir 5", "abi ir 10", "saucēji ir vienādi",
               "tie nav vienādi"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus par daļu no veselā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Klasē ir 24 skolēni, {1|3} no tiem ir zēni. Cik ir zēnu?",
              ["8", "3", "16", "21"], 0),
             ("Naudas somā ir 60 eiro; iztērēti {2|3}. Cik ir iztērēts?",
              ["40 eiro", "20 eiro", "30 eiro", "45 eiro"], 0),
             ("Ceļš ir 36 km; nobraukta {1|4} daļa. Cik km ir nobraukts?",
              ["9 km", "4 km", "27 km", "12 km"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 4.6. temata noslēgumā. "
                "Pārbauda pamatdaļas un daļas vērtības aprēķināšanu, veselā "
                "noteikšanu, daļu no garuma, masas un laika mērvienībām un "
                "daļas lietojumu situāciju uzdevumos.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus un zīmējumus veido tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Aprēķina pamatdaļas vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {1|3} no 18?", ["6", "3", "12", "54"], 0),
             ("Cik ir {1|5} no 40?", ["8", "5", "32", "200"], 0),
             ("Kā aprēķina pamatdaļu?",
              ["veselo dala ar saucēju", "veselo reizina ar saucēju",
               "veselo saskaita", "veselo atņem"], 0),
         ]},
        {"sr": "Aprēķina daļas vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {2|3} no 18?", ["12", "6", "9", "27"], 0),
             ("Cik ir {3|5} no 40?", ["24", "8", "15", "120"], 0),
             ("Kā aprēķina {2|5} no skaitļa?",
              ["dala ar 5 un reizina ar 2", "reizina ar 5 un dala ar 2",
               "dala ar 2", "reizina ar 10"], 0),
         ]},
        {"sr": "Nosaka veselo",
         "stunda": TEMATS,
         "jautajumi": [
             ("{1|4} no skaitļa ir 7. Kāds ir skaitlis?",
              ["28", "11", "3", "4"], 0),
             ("{2|3} no skaitļa ir 10. Kāds ir skaitlis?",
              ["15", "20", "30", "5"], 0),
             ("Kā atrod veselo, ja zināma pamatdaļa?",
              ["reizina ar saucēju", "dala ar saucēju", "saskaita",
               "atņem"], 0),
         ]},
        {"sr": "Nosaka daļu no mērvienībām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik gramu ir {1|2} kg?",
              ["500 g", "50 g", "200 g", "250 g"], 0),
             ("Cik minūšu ir {3|4} stunda?",
              ["45 min", "34 min", "30 min", "75 min"], 0),
             ("Cik metru ir {1|4} km?",
              ["250 m", "400 m", "25 m", "4 m"], 0),
         ]},
        {"sr": "Nosaka daļu no figūras laukuma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūrī ir 18 rūtiņu. Cik rūtiņu ir {1|3} no tā?",
              ["6", "3", "9", "54"], 0),
             ("Figūrā ir 16 rūtiņu, iekrāsotas 4. Kāda daļa ir iekrāsota?",
              ["{4|16}", "{16|4}", "{1|16}", "{12|16}"], 0),
             ("Kvadrāts sadalīts 6 vienādās daļās. Kāda daļa ir viena no "
              "tām?", ["{1|6}", "{6|1}", "{1|3}", "{5|6}"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Klasē ir 30 skolēni, {1|5} no tiem kavē. Cik skolēnu kavē?",
              ["6", "5", "24", "25"], 0),
             ("Somā ir 45 eiro; iztērēta {1|3} daļa. Cik ir iztērēts?",
              ["15 eiro", "3 eiro", "30 eiro", "42 eiro"], 0),
             ("Cik ir vairāk: {1|2} no 12 vai {1|3} no 24?",
              ["{1|3} no 24", "{1|2} no 12", "tie ir vienādi",
               "nevar salīdzināt"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina daļu no skaitļa un no mērvienības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|4} no 20 = ……", "5"),
                         ("{3|4} no 20 = ……", "15"),
                         ("{1|2} kg = …… g", "500"),
                         ("{1|4} stunda = …… min", "15")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|6} no 30 = ……", "5"),
                         ("{2|5} no 30 = ……", "12"),
                         ("{1|4} kg = …… g", "250"),
                         ("{1|2} stunda = …… min", "30")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|5} no 45 = ……", "9"),
                         ("{3|5} no 45 = ……", "27"),
                         ("{3|4} kg = …… g", "750"),
                         ("{3|4} stunda = …… min", "45")]},
         ]},
        {"sr": "Nosaka veselo, ja zināma daļa",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|5} no skaitļa ir 6; skaitlis ir ……", "30"),
                         ("{1|3} no skaitļa ir 9; skaitlis ir ……", "27"),
                         ("{2|5} no skaitļa ir 8; skaitlis ir ……", "20")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|4} no skaitļa ir 7; skaitlis ir ……", "28"),
                         ("{1|6} no skaitļa ir 5; skaitlis ir ……", "30"),
                         ("{3|4} no skaitļa ir 12; skaitlis ir ……", "16")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("{1|2} no skaitļa ir 14; skaitlis ir ……", "28"),
                         ("{1|5} no skaitļa ir 8; skaitlis ir ……", "40"),
                         ("{2|3} no skaitļa ir 10; skaitlis ir ……", "15")]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar vairākām daļām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Klasē ir 24 skolēni. Futbolu spēlē {1|3} no viņiem, "
                        "bet basketbolu — {1|4}. Cik skolēnu spēlē katru "
                        "spēli? Cik spēlē abas spēles kopā? Cik nespēlē "
                        "nevienu no tām?",
              "kriteriji": ["Futbolu spēlē 24 : 3 = 8 skolēni.   (1 p.)",
                            "Basketbolu spēlē 24 : 4 = 6 skolēni.   (1 p.)",
                            "Kopā 8 + 6 = 14 skolēni.   (1 p.)",
                            "Nespēlē 24 − 14 = 10 skolēni.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Naudas somā ir 60 eiro. Anna iztērēja {2|3}, bet "
                        "Jānis — {1|5} no šīs naudas. Cik iztērēja katrs? "
                        "Cik viņi iztērēja kopā? Cik naudas palika?",
              "kriteriji": ["Anna iztērēja 60 : 3 · 2 = 40 eiro.   (1 p.)",
                            "Jānis iztērēja 60 : 5 = 12 eiro.   (1 p.)",
                            "Kopā 40 + 12 = 52 eiro.   (1 p.)",
                            "Palika 60 − 52 = 8 eiro.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.6,
              "teksts": "Ceļš ir 36 km garš. Pirmajā dienā nobrauca {1|4}, "
                        "bet otrajā — {1|3} no ceļa. Cik km nobrauca katrā "
                        "dienā? Cik km nobrauca kopā? Cik km palika?",
              "kriteriji": ["Pirmajā dienā 36 : 4 = 9 km.   (1 p.)",
                            "Otrajā dienā 36 : 3 = 12 km.   (1 p.)",
                            "Kopā 9 + 12 = 21 km.   (1 p.)",
                            "Palika 36 − 21 = 15 km.   (1 p.)"]},
         ]},
        {"sr": "Skaidro, kā aprēķināta daļa vai veselais",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Daļa no figūras", "vieta": 5.5,
              "ievads": "Rūtiņās uzzīmē taisnstūri, kas ir 6 rūtiņas plats "
                        "un 2 rūtiņas augsts!",
              "jaut": [("Cik rūtiņu ir figūrā?", 1),
                       ("Iekrāso {1|3} no tās!", 1),
                       ("Cik rūtiņu palika neiekrāsotas?", 1)],
              "atbildes": ["1) 12 rūtiņas.   (1 p.)",
                           "2) Iekrāsotas 4 rūtiņas.   (1 p.)",
                           "3) Neiekrāsotas 8 rūtiņas.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Daļa un atlikums", "vieta": 5.5,
              "ievads": "Jānim bija 20 konfektes. Viņš iedeva māsai {1|4} "
                        "no tām.",
              "jaut": [("Cik konfekšu viņš iedeva?", 1),
                       ("Cik konfekšu viņam palika?", 1),
                       ("Kādu daļu konfekšu viņš paturēja?", 1)],
              "atbildes": ["1) 20 : 4 = 5 konfektes.   (1 p.)",
                           "2) Palika 15 konfektes.   (1 p.)",
                           "3) Viņš paturēja {3|4}.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Veselā noteikšana", "vieta": 5.5,
              "ievads": "Zināms, ka {1|6} no ceļa ir 4 km.",
              "jaut": [("Cik garš ir viss ceļš?", 1),
                       ("Cik garas ir {2|6} no ceļa?", 1),
                       ("Paskaidro, kā atradi visu ceļu!", 1)],
              "atbildes": ["1) 4 · 6 = 24 km.   (1 p.)",
                           "2) 4 · 2 = 8 km.   (1 p.)",
                           "3) Pamatdaļu reizina ar saucēju.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
