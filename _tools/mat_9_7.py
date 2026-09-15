# -*- coding: utf-8 -*-
"""Matemātika, 9. klase. 9.7. Kā skaitļu virkni pieraksta ar formulu?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 9. klase, 9.7. temats): skaitļu virknes
uzdošana ar rekurentu sakarību un ar atkarību no kārtas numura, virkne kā
funkcija un tās grafiskais attēlojums, aritmētiskā progresija un diference,
īpašība par aritmētisko vidējo no vienādi tāliem locekļiem, vispārīgā
locekļa formula un tās lietojums nezināmu lielumu noteikšanai.
"""

PRIEKSMETS = "Matemātika  |  9. klase"
TEMATS = "9.7."
NOSAUKUMS = "Kā skaitļu virkni pieraksta ar formulu?"

ATGADNE = [
    "Virknes locekļus apzīmē a₁, a₂, a₃, …, aₙ;   n ir locekļa kārtas "
    "numurs.",
    "Aritmētiskajā progresijā katru nākamo locekli iegūst, pieskaitot "
    "diferenci:   aₙ₊₁ = aₙ + d      ·      d = a₂ − a₁",
    "Vispārīgā locekļa formula   aₙ = a₁ + (n − 1)d      ·      katrs "
    "loceklis ir aritmētiskais vidējais no abiem kaimiņiem",
]

FD = {
    "veids": "fd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 9.7. temata beigās. Pārbauda skaitļu "
                "virknes apzīmējumus un uzdošanas veidus, aritmētiskās "
                "progresijas definīciju un diferenci, vispārīgā locekļa "
                "formulu, kārtas numura noteikšanu un virknes grafisko "
                "attēlojumu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina virknes apzīmējumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā apzīmē virknes trešo locekli?",
              ["a₃", "3a", "a · 3", "n₃"], 0),
             ("Ko virknē apzīmē n?",
              ["locekļa kārtas numuru", "locekļa vērtību", "diferenci",
               "summu"], 0),
             ("Kurš ir virknes 2; 5; 8; 11 otrais loceklis?",
              ["5", "2", "8", "11"], 0),
         ]},
        {"sr": "Zina virknes uzdošanas veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā var uzdot skaitļu virkni?",
              ["ar formulu no kārtas numura", "tikai ar zīmējumu",
               "tikai ar tabulu", "nekādi"], 0),
             ("Virkne aₙ = 2n. Kurš ir tās pirmais loceklis?",
              ["2", "1", "0", "4"], 0),
             ("Virkne aₙ = 3n − 1. Kurš ir tās otrais loceklis?",
              ["5", "2", "6", "8"], 0),
         ]},
        {"sr": "Zina aritmētiskās progresijas definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir aritmētiskā progresija?",
              ["virkne, kurā katru nākamo iegūst, pieskaitot vienu skaitli",
               "virkne, kurā katru nākamo reizina", "jebkura skaitļu virkne",
               "virkne ar veseliem skaitļiem"], 0),
             ("Kā sauc skaitli, ko katru reizi pieskaita?",
              ["diference", "reizinātājs", "saucējs", "summa"], 0),
             ("Kura virkne ir aritmētiskā progresija?",
              ["3; 7; 11; 15", "2; 4; 8; 16", "1; 4; 9; 16",
               "1; 1; 2; 3"], 0),
         ]},
        {"sr": "Nosaka diferenci",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir virknes 5; 9; 13; 17 diference?",
              ["4", "5", "9", "2"], 0),
             ("Cik liela ir virknes 20; 17; 14 diference?",
              ["−3", "3", "20", "17"], 0),
             ("Kā aprēķina diferenci?",
              ["d = a₂ − a₁", "d = a₂ + a₁", "d = a₂ · a₁",
               "d = a₁ − a₂"], 0),
         ]},
        {"sr": "Aprēķina nākamo locekli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Virkne 4; 9; 14; … Kurš ir nākamais loceklis?",
              ["19", "18", "20", "24"], 0),
             ("Virkne 30; 25; 20; … Kurš ir nākamais loceklis?",
              ["15", "10", "25", "35"], 0),
             ("Kā aprēķina nākamo locekli?",
              ["pieskaita diferenci", "reizina ar diferenci",
               "atņem kārtas numuru", "dala ar 2"], 0),
         ]},
        {"sr": "Zina vispārīgā locekļa formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir vispārīgā locekļa formula?",
              ["aₙ = a₁ + (n − 1)d", "aₙ = a₁ + nd", "aₙ = a₁ · d",
               "aₙ = a₁ − nd"], 0),
             ("Ko formulā nozīmē a₁?",
              ["pirmo locekli", "diferenci", "kārtas numuru", "summu"], 0),
             ("Kāpēc formulā ir (n − 1)?",
              ["diferenci pieskaita n − 1 reizi", "tā ir kļūda",
               "lai skaitlis būtu mazāks", "lai n būtu vesels"], 0),
         ]},
        {"sr": "Aprēķina n-to locekli",
         "stunda": TEMATS,
         "jautajumi": [
             ("a₁ = 3 un d = 4. Cik liels ir a₅?",
              ["19", "15", "23", "7"], 0),
             ("a₁ = 2 un d = 5. Cik liels ir a₁₀?",
              ["47", "52", "50", "45"], 0),
             ("a₁ = 10 un d = −2. Cik liels ir a₆?",
              ["0", "2", "−2", "20"], 0),
         ]},
        {"sr": "Nosaka pirmo locekli vai diferenci",
         "stunda": TEMATS,
         "jautajumi": [
             ("Virknē a₃ = 11 un d = 4. Cik liels ir a₁?",
              ["3", "7", "15", "1"], 0),
             ("Virknē a₁ = 5 un a₄ = 20. Cik liela ir diference?",
              ["5", "15", "3", "4"], 0),
             ("Kā no a₁ un aₙ atrod diferenci?",
              ["d = {aₙ − a₁|n − 1}", "d = aₙ − a₁", "d = {aₙ|a₁}",
               "d = aₙ + a₁"], 0),
         ]},
        {"sr": "Lieto īpašību par aritmētisko vidējo",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds loceklis, kas atrodas starp diviem kaimiņiem?",
              ["to aritmētisko vidējo", "to summu", "to reizinājumu",
               "to starpību"], 0),
             ("Virknē … 7; x; 15 … Cik liels ir x?",
              ["11", "22", "8", "10"], 0),
             ("Virknē … 4; x; 20 … Cik liels ir x?",
              ["12", "16", "24", "8"], 0),
         ]},
        {"sr": "Nosaka locekļa kārtas numuru",
         "stunda": TEMATS,
         "jautajumi": [
             ("a₁ = 2 un d = 3. Kurš loceklis ir 20?",
              ["7.", "6.", "8.", "5."], 0),
             ("a₁ = 1 un d = 5. Kurš loceklis ir 26?",
              ["6.", "5.", "7.", "26."], 0),
             ("Kā atrod locekļa kārtas numuru?",
              ["atrisina vienādojumu ar formulu",
               "skaita locekļus pēc kārtas", "dala ar diferenci",
               "reizina ar d"], 0),
         ]},
        {"sr": "Saprot virkni kā funkciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas virknei ir arguments?",
              ["kārtas numurs n", "locekļa vērtība", "diference",
               "summa"], 0),
             ("Kāds ir aritmētiskās progresijas grafiks?",
              ["punkti uz vienas taisnes", "nepārtraukta taisne",
               "parabola", "riņķa līnija"], 0),
             ("Kāpēc grafiks ir tikai atsevišķi punkti?",
              ["n ir naturāls skaitlis", "tā ir kļūda", "tā ir vieglāk",
               "punkti ir precīzāki"], 0),
         ]},
        {"sr": "Lieto progresiju praktiskā situācijā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pirmajā rindā ir 20 vietas, katrā nākamajā par 2 vairāk. Cik "
              "vietu ir 5. rindā?", ["28", "30", "26", "24"], 0),
             ("Krājkasē ir 10 eiro; katru nedēļu pieliek 5 eiro. Cik būs "
              "pēc 6 nedēļām?",
              ["40 eiro", "30 eiro", "35 eiro", "45 eiro"], 0),
             ("Kāpēc šo situāciju apraksta aritmētiskā progresija?",
              ["pieaugums katru reizi ir vienāds", "skaitļi ir lieli",
               "runa ir par naudu", "tā nav progresija"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 25 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 9.7. temata noslēgumā. "
                "Pārbauda aritmētiskās progresijas definīciju un diferenci, "
                "vispārīgā locekļa formulas iegūšanu un lietojumu, kārtas "
                "numura noteikšanu, grafisko attēlojumu un progresijas "
                "lietojumu praktiskā situācijā.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 25 "
              "punktus. Risinājumu pieraksti tam atvēlētajā vietā; "
              "atļauts kalkulators.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina virknes apzīmējumus un uzdošanas veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā apzīmē virknes ceturto locekli?",
              ["a₄", "4a", "a · 4", "n₄"], 0),
             ("Virkne aₙ = 4n − 2. Kurš ir tās pirmais loceklis?",
              ["2", "4", "−2", "6"], 0),
             ("Ko virknē apzīmē n?",
              ["kārtas numuru", "locekļa vērtību", "diferenci", "summu"], 0),
         ]},
        {"sr": "Atpazīst aritmētisko progresiju un nosaka diferenci",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura virkne ir aritmētiskā progresija?",
              ["4; 9; 14; 19", "2; 4; 8; 16", "1; 4; 9; 16", "1; 1; 2; 3"],
              0),
             ("Cik liela ir virknes 7; 11; 15 diference?",
              ["4", "7", "11", "3"], 0),
             ("Cik liela ir virknes 25; 20; 15 diference?",
              ["−5", "5", "25", "20"], 0),
         ]},
        {"sr": "Lieto vispārīgā locekļa formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir vispārīgā locekļa formula?",
              ["aₙ = a₁ + (n − 1)d", "aₙ = a₁ + nd", "aₙ = a₁ · d",
               "aₙ = a₁ − nd"], 0),
             ("a₁ = 5 un d = 3. Cik liels ir a₆?",
              ["20", "23", "18", "15"], 0),
             ("a₁ = 1 un d = 4. Cik liels ir a₈?",
              ["29", "33", "32", "25"], 0),
         ]},
        {"sr": "Nosaka pirmo locekli, diferenci un kārtas numuru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Virknē a₄ = 17 un d = 5. Cik liels ir a₁?",
              ["2", "12", "22", "7"], 0),
             ("Virknē a₁ = 3 un a₅ = 19. Cik liela ir diference?",
              ["4", "16", "5", "3"], 0),
             ("a₁ = 2 un d = 3. Kurš loceklis ir 17?",
              ["6.", "5.", "7.", "17."], 0),
         ]},
        {"sr": "Lieto īpašību par aritmētisko vidējo",
         "stunda": TEMATS,
         "jautajumi": [
             ("Virknē … 6; x; 14 … Cik liels ir x?",
              ["10", "20", "8", "7"], 0),
             ("Ar ko vienāds loceklis starp diviem kaimiņiem?",
              ["to aritmētisko vidējo", "to summu", "to reizinājumu",
               "to starpību"], 0),
             ("Virknē … 11; x; 23 … Cik liels ir x?",
              ["17", "34", "12", "6"], 0),
         ]},
        {"sr": "Saprot virkni kā funkciju un lieto praksē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir aritmētiskās progresijas grafiks?",
              ["punkti uz vienas taisnes", "nepārtraukta taisne",
               "parabola", "riņķa līnija"], 0),
             ("Pirmajā rindā ir 18 vietas, katrā nākamajā par 3 vairāk. Cik "
              "vietu ir 4. rindā?", ["27", "30", "24", "21"], 0),
             ("Kāpēc virknes grafiks ir tikai atsevišķi punkti?",
              ["n ir naturāls skaitlis", "tā ir kļūda", "tā ir vieglāk",
               "punkti ir precīzāki"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Nosaka diferenci un aprēķina progresijas locekļus",
         "stunda": TEMATS, "punkti": 5, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Virknei 5; 9; 13; …   d = ……", "4"),
                         ("Tās nākamais loceklis ir ……", "17"),
                         ("a₁ = 3, d = 4;   a₅ = ……", "19"),
                         ("a₁ = 2, d = 5;   a₁₀ = ……", "47"),
                         ("Virknē … 7; x; 15 …   x = ……", "11")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Virknei 20; 17; 14; …   d = ……", "−3"),
                         ("Tās nākamais loceklis ir ……", "11"),
                         ("a₁ = 1, d = 6;   a₄ = ……", "19"),
                         ("a₁ = 10, d = −2;   a₆ = ……", "0"),
                         ("Virknē … 4; x; 20 …   x = ……", "12")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Virknei 2; 8; 14; …   d = ……", "6"),
                         ("Tās nākamais loceklis ir ……", "20"),
                         ("a₁ = 5, d = 3;   a₇ = ……", "23"),
                         ("a₁ = 100, d = −10;   a₅ = ……", "60"),
                         ("Virknē … 9; x; 25 …   x = ……", "17")]},
         ]},
        {"sr": "Iegūst un lieto vispārīgā locekļa formulu",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Vispārīgā locekļa formula",
              "vieta": 5.8,
              "teksts": "Aritmētiskās progresijas pirmais loceklis ir 7, bet "
                        "diference — 5.   a) Pieraksti pirmos četrus "
                        "locekļus.   b) Uzraksti vispārīgā locekļa formulu."
                        "   c) Aprēķini a₂₀.",
              "kriteriji": ["a) 7; 12; 17; 22.   (1 p.)",
                            "b) Lietota formula aₙ = a₁ + (n − 1)d.   "
                            "(1 p.)",
                            "b) Atbilde aₙ = 5n + 2.   (1 p.)",
                            "c) Pieraksts a₂₀ = 7 + 19 · 5.   (1 p.)",
                            "c) Atbilde a₂₀ = 102.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Vispārīgā locekļa formula",
              "vieta": 5.8,
              "teksts": "Aritmētiskajā progresijā a₁ = 4 un a₅ = 24.   "
                        "a) Aprēķini diferenci.   b) Uzraksti vispārīgā "
                        "locekļa formulu.   c) Aprēķini a₁₂.",
              "kriteriji": ["a) Pieraksts 24 = 4 + 4d.   (1 p.)",
                            "a) Atbilde d = 5.   (1 p.)",
                            "b) Atbilde aₙ = 5n − 1.   (1 p.)",
                            "c) Pieraksts a₁₂ = 4 + 11 · 5.   (1 p.)",
                            "c) Atbilde a₁₂ = 59.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Vispārīgā locekļa formula",
              "vieta": 5.8,
              "teksts": "Aritmētiskajā progresijā a₃ = 11 un a₇ = 27.   "
                        "a) Aprēķini diferenci.   b) Aprēķini pirmo "
                        "locekli.   c) Aprēķini a₁₅.",
              "kriteriji": ["a) Pieraksts 27 = 11 + 4d.   (1 p.)",
                            "a) Atbilde d = 4.   (1 p.)",
                            "b) Atbilde a₁ = 3.   (1 p.)",
                            "c) Pieraksts a₁₅ = 3 + 14 · 4.   (1 p.)",
                            "c) Atbilde a₁₅ = 59.   (1 p.)"]},
         ]},
        {"sr": "Lieto progresiju praktiskā situācijā",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.0,
              "teksts": "Teātra pirmajā rindā ir 20 vietas, un katrā "
                        "nākamajā rindā ir par 2 vietām vairāk.   a) Cik "
                        "vietu ir 8. rindā?   b) Kurā rindā ir 40 vietas?   "
                        "c) Cik vietu kopā ir 1. un 8. rindā?",
              "kriteriji": ["Saskatīta progresija: a₁ = 20, d = 2.   (1 p.)",
                            "a) Pieraksts a₈ = 20 + 7 · 2.   (1 p.)",
                            "a) Atbilde 34 vietas.   (1 p.)",
                            "b) 20 + 2(n − 1) = 40, tātad 11. rinda.   "
                            "(1 p.)",
                            "c) 20 + 34 = 54 vietas.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.0,
              "teksts": "Krājkasē sākumā bija 10 eiro, un katru nedēļu tur "
                        "ieliek 5 eiro.   a) Cik naudas būs pēc 6 nedēļām?  "
                        " b) Pēc cik nedēļām būs 60 eiro?   c) Uzraksti "
                        "formulu naudas summai pēc n nedēļām.",
              "kriteriji": ["Saskatīta progresija ar d = 5.   (1 p.)",
                            "a) Pieraksts 10 + 6 · 5.   (1 p.)",
                            "a) Atbilde 40 eiro.   (1 p.)",
                            "b) 10 + 5n = 60, tātad 10 nedēļas.   (1 p.)",
                            "c) Atbilde aₙ = 10 + 5n.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Situāciju uzdevums", "vieta": 5.0,
              "teksts": "Aritmētiskajā progresijā a₁ = 2 un d = 3.   "
                        "a) Kurš loceklis ir 20?   b) Vai 30 ir šīs "
                        "progresijas loceklis? Pamato!   c) Aprēķini a₂₅.",
              "kriteriji": ["a) Vienādojums 2 + 3(n − 1) = 20.   (1 p.)",
                            "a) Atbilde: 7. loceklis.   (1 p.)",
                            "b) 2 + 3(n − 1) = 30 nedod veselu n.   (1 p.)",
                            "b) Atbilde: 30 nav progresijas loceklis.   "
                            "(1 p.)",
                            "c) a₂₅ = 2 + 24 · 3 = 74.   (1 p.)"]},
         ]},
        {"sr": "Pamato un attēlo virkni",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Virknes pieraksts", "vieta": 4.4,
              "ievads": "Dota virkne  3; 7; 11; 15; …",
              "jaut": [("Pamato, ka tā ir aritmētiskā progresija!", 1),
                       ("Uzraksti vispārīgā locekļa formulu!", 2),
                       ("Aprēķini a₃₀!", 1)],
              "atbildes": ["1) Starpība starp kaimiņiem vienmēr ir 4.   "
                           "(1 p.)",
                           "2) aₙ = 3 + (n − 1) · 4 = 4n − 1.   (2 p.)",
                           "3) a₃₀ = 4 · 30 − 1 = 119.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Formula un locekļi", "vieta": 4.4,
              "ievads": "Virknes vispārīgā locekļa formula ir  aₙ = 5n + 2.",
              "jaut": [("Aprēķini pirmos trīs locekļus!", 1),
                       ("Cik liela ir diference?", 1),
                       ("Kurš loceklis ir 52?", 2)],
              "atbildes": ["1) 7; 12; 17.   (1 p.)",
                           "2) d = 5.   (1 p.)",
                           "3) 5n + 2 = 52, tātad 10. loceklis.   (2 p.)"]},
             {"tips": "jautajumi", "virs": "Virknes grafiks", "vieta": 4.4,
              "ievads": "Aritmētiskajā progresijā a₁ = 2 un d = 2.",
              "jaut": [("Pieraksti pirmos piecus locekļus!", 1),
                       ("Attēlo tos kā punktus (n; aₙ)!", 2),
                       ("Kā izvietoti šie punkti?", 1)],
              "atbildes": ["1) 2; 4; 6; 8; 10.   (1 p.)",
                           "2) Atzīmēti punkti (1; 2), (2; 4), (3; 6), "
                           "(4; 8), (5; 10).   (2 p.)",
                           "3) Tie atrodas uz vienas taisnes.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
