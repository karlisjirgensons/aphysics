# -*- coding: utf-8 -*-
"""Matemātika, 9. klase. 9.4. Kā izmanto izteiksmju sadalīšanu reizinātājos?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 9. klase, 9.4. temats): izteiksme kā
reizinājums, kopīgā reizinātāja iznešana pirms iekavām, saīsinātās
reizināšanas formulas (SRF) abos virzienos, SRF lietojums skaitliskos
aprēķinos, secinājums «ja reizinājums ir 0, tad kāds reizinātājs ir 0» un
nepilno kvadrātvienādojumu atrisināšana ar sadalīšanu reizinātājos.
"""

PRIEKSMETS = "Matemātika  |  9. klase"
TEMATS = "9.4."
NOSAUKUMS = "Kā izmanto izteiksmju sadalīšanu reizinātājos?"

ATGADNE = [
    "Kopīgā reizinātāja iznešana:   ab + ac = a(b + c)",
    "(a + b)² = a² + 2ab + b²   ·   (a − b)² = a² − 2ab + b²   ·   "
    "a² − b² = (a − b)(a + b)",
    "Ja reizinājums ir 0, tad kāds no reizinātājiem ir 0:   x(x − 5) = 0   "
    "⇒   x = 0  vai  x = 5      ·      x² = a   ⇒   x = ±√a",
]

FD = {
    "veids": "fd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 9.4. temata beigās. Pārbauda kopīgā "
                "reizinātāja iznešanu, saīsinātās reizināšanas formulas "
                "abos virzienos, to lietojumu skaitliskos aprēķinos un "
                "nepilno kvadrātvienādojumu atrisināšanu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Atpazīst izteiksmi, kas ir reizinājums",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad izteiksme ir sadalīta reizinātājos?",
              ["ja pēdējā darbība ir reizināšana",
               "ja pēdējā darbība ir saskaitīšana", "ja tajā ir iekavas",
               "ja tajā ir pakāpe"], 0),
             ("Kura izteiksme ir reizinājums?",
              ["3a(a + 2)", "3a + 2", "a² + 2a + 1", "a − b"], 0),
             ("Kura izteiksme NAV sadalīta reizinātājos?",
              ["x² + 4x", "x(x + 4)", "(x − 1)(x + 1)", "2(x + 3)"], 0),
         ]},
        {"sr": "Iznes kopīgo reizinātāju pirms iekavām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Sadali reizinātājos:  5x + 5y",
              ["5(x + y)", "5xy", "x + y", "10(x + y)"], 0),
             ("Sadali reizinātājos:  a² + ab",
              ["a(a + b)", "a²b", "a + b", "ab(a + 1)"], 0),
             ("Sadali reizinātājos:  6x − 9",
              ["3(2x − 3)", "3(2x − 9)", "6(x − 9)", "2(3x − 9)"], 0),
         ]},
        {"sr": "Nosaka lielāko kopīgo reizinātāju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir lielākais kopīgais reizinātājs izteiksmē 12a² + 8a?",
              ["4a", "4", "a", "12a"], 0),
             ("Sadali reizinātājos:  12a² + 8a",
              ["4a(3a + 2)", "4a(3a + 8)", "2a(6a + 8)", "4(3a² + 2a)"], 0),
             ("Kāpēc kopīgo reizinātāju iznes pirms iekavām?",
              ["lai izteiksmi pierakstītu kā reizinājumu",
               "lai izteiksme kļūtu garāka", "lai mainītu tās vērtību",
               "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Lieto binoma kvadrāta formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds (a + b)²?",
              ["a² + 2ab + b²", "a² + b²", "a² − 2ab + b²", "2a + 2b"], 0),
             ("Izvērs:  (x + 3)²",
              ["x² + 6x + 9", "x² + 9", "x² + 3x + 9", "x² + 6x + 6"], 0),
             ("Sadali reizinātājos:  x² + 10x + 25",
              ["(x + 5)²", "(x − 5)²", "(x + 25)²", "(x + 10)²"], 0),
         ]},
        {"sr": "Lieto starpības kvadrāta formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds (a − b)²?",
              ["a² − 2ab + b²", "a² − b²", "a² + 2ab + b²", "a² + b²"], 0),
             ("Izvērs:  (y − 4)²",
              ["y² − 8y + 16", "y² − 16", "y² − 4y + 16", "y² + 8y + 16"], 0),
             ("Sadali reizinātājos:  x² − 12x + 36",
              ["(x − 6)²", "(x + 6)²", "(x − 36)²", "(x − 12)²"], 0),
         ]},
        {"sr": "Lieto kvadrātu starpības formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds a² − b²?",
              ["(a − b)(a + b)", "(a − b)²", "(a + b)²", "a² + b²"], 0),
             ("Sadali reizinātājos:  x² − 49",
              ["(x − 7)(x + 7)", "(x − 49)(x + 49)", "(x − 7)²",
               "x(x − 49)"], 0),
             ("Sadali reizinātājos:  9a² − 16",
              ["(3a − 4)(3a + 4)", "(9a − 16)(9a + 16)", "(3a − 4)²",
               "3(3a² − 16)"], 0),
         ]},
        {"sr": "Lieto SRF abos virzienos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē lietot SRF otrā virzienā?",
              ["summu pierakstīt kā reizinājumu", "vienmēr atvērt iekavas",
               "saskaitīt locekļus", "izsvītrot pakāpes"], 0),
             ("Sadali reizinātājos:  4x² − 25y²",
              ["(2x − 5y)(2x + 5y)", "(4x − 25y)(4x + 25y)", "(2x − 5y)²",
               "4(x² − 25y²)"], 0),
             ("Kura izteiksme ir binoma kvadrāts?",
              ["x² + 14x + 49", "x² + 14x + 47", "x² − 49", "x² + 49"], 0),
         ]},
        {"sr": "Lieto SRF skaitliskos aprēķinos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aprēķini:  51² − 49²", ["200", "100", "2", "400"], 0),
             ("Aprēķini:  102²", ["10404", "10004", "10204", "1024"], 0),
             ("Kāpēc SRF palīdz skaitliskos aprēķinos?",
              ["reizināšana kļūst vienkāršāka", "skaitļi kļūst lielāki",
               "atbilde mainās", "aprēķins ir ilgāks"], 0),
         ]},
        {"sr": "Sadala reizinātājos vairākos soļos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Sadali reizinātājos:  2x² − 8",
              ["2(x − 2)(x + 2)", "2(x² − 8)", "(2x − 8)(2x + 8)",
               "2(x − 4)(x + 4)"], 0),
             ("Sadali reizinātājos:  ax + ay + bx + by",
              ["(a + b)(x + y)", "ab(x + y)", "(a + x)(b + y)",
               "a(x + y) + b"], 0),
             ("Kāds ir pirmais solis, sadalot 3x² − 27?",
              ["iznest 3 pirms iekavām", "lietot binoma kvadrātu",
               "dalīt ar x", "saskaitīt locekļus"], 0),
         ]},
        {"sr": "Lieto secinājumu par reizinājumu, kas vienāds ar nulli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ja ab = 0, ko var secināt?",
              ["a = 0 vai b = 0", "a = b", "a = 1 un b = 0", "neko"], 0),
             ("Atrisini:  x(x − 3) = 0",
              ["x = 0 vai x = 3", "x = 3", "x = 0", "x = −3"], 0),
             ("Atrisini:  (x + 2)(x − 5) = 0",
              ["x = −2 vai x = 5", "x = 2 vai x = −5", "x = 10",
               "x = −3"], 0),
         ]},
        {"sr": "Atrisina vienādojumu ax² + bx = 0",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā atrisina vienādojumu  x² − 6x = 0?",
              ["iznes x pirms iekavām", "dala abas puses ar x",
               "lieto kvadrātu starpību", "saskaita locekļus"], 0),
             ("Atrisini:  x² − 6x = 0",
              ["x = 0 vai x = 6", "x = 6", "x = −6", "x = 0"], 0),
             ("Kāpēc vienādojumu nedrīkst dalīt ar x?",
              ["var pazaudēt sakni x = 0", "atbilde kļūst lielāka",
               "tas ir atļauts", "mainās zīme"], 0),
         ]},
        {"sr": "Atrisina vienādojumu ax² + c = 0",
         "stunda": TEMATS,
         "jautajumi": [
             ("Atrisini:  x² = 49",
              ["x = 7 vai x = −7", "x = 7", "x = 24,5", "x = −7"], 0),
             ("Atrisini:  x² − 5 = 0",
              ["x = √5 vai x = −√5", "x = 5", "x = 2,5", "x = 25"], 0),
             ("Cik sakņu ir vienādojumam  x² + 9 = 0?",
              ["nevienas", "viena", "divas", "bezgalīgi daudz"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 25 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 9.4. temata noslēgumā. "
                "Pārbauda kopīgā reizinātāja iznešanu, saīsinātās "
                "reizināšanas formulas abos virzienos, to lietojumu "
                "skaitliskos aprēķinos un nepilno kvadrātvienādojumu "
                "atrisināšanu ar sadalīšanu reizinātājos.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 25 "
              "punktus. Risinājumu pieraksti tam atvēlētajā vietā; "
              "atļauts kalkulators.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Atpazīst reizinājumu un iznes kopīgo reizinātāju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura izteiksme ir sadalīta reizinātājos?",
              ["2x(x − 1)", "2x² − x", "x² + 5", "x − 7"], 0),
             ("Sadali reizinātājos:  8a + 8b",
              ["8(a + b)", "8ab", "16(a + b)", "a + b"], 0),
             ("Sadali reizinātājos:  x² − 5x",
              ["x(x − 5)", "x(x + 5)", "5x(x − 1)", "(x − 5)²"], 0),
         ]},
        {"sr": "Lieto binoma kvadrāta formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds (a − b)²?",
              ["a² − 2ab + b²", "a² − b²", "a² + 2ab + b²", "a² + b²"], 0),
             ("Izvērs:  (x + 6)²",
              ["x² + 12x + 36", "x² + 36", "x² + 6x + 36", "x² + 12x + 12"],
              0),
             ("Sadali reizinātājos:  x² − 8x + 16",
              ["(x − 4)²", "(x + 4)²", "(x − 16)²", "(x − 8)²"], 0),
         ]},
        {"sr": "Lieto kvadrātu starpības formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds a² − b²?",
              ["(a − b)(a + b)", "(a − b)²", "(a + b)²", "a² + b²"], 0),
             ("Sadali reizinātājos:  x² − 64",
              ["(x − 8)(x + 8)", "(x − 8)²", "(x − 64)(x + 64)",
               "x(x − 64)"], 0),
             ("Sadali reizinātājos:  16a² − 9",
              ["(4a − 3)(4a + 3)", "(4a − 3)²", "(16a − 9)(16a + 9)",
               "4(4a² − 9)"], 0),
         ]},
        {"sr": "Lieto SRF skaitliskos aprēķinos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aprēķini:  61² − 39²", ["2200", "1100", "22", "484"], 0),
             ("Aprēķini:  99²", ["9801", "9081", "9901", "8901"], 0),
             ("Ar kuru formulu ātri aprēķina 47² − 43²?",
              ["a² − b² = (a − b)(a + b)", "(a + b)² = a² + 2ab + b²",
               "(a − b)² = a² − 2ab + b²", "ab + ac = a(b + c)"], 0),
         ]},
        {"sr": "Lieto secinājumu par reizinājumu, kas vienāds ar nulli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ja ab = 0, ko var secināt?",
              ["a = 0 vai b = 0", "a = b", "a = 1", "neko"], 0),
             ("Atrisini:  (x − 4)(x + 7) = 0",
              ["x = 4 vai x = −7", "x = −4 vai x = 7", "x = 28", "x = 3"],
              0),
             ("Atrisini:  x(x + 9) = 0",
              ["x = 0 vai x = −9", "x = 0 vai x = 9", "x = −9", "x = 9"],
              0),
         ]},
        {"sr": "Atrisina nepilnu kvadrātvienādojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Atrisini:  x² − 8x = 0",
              ["x = 0 vai x = 8", "x = 8", "x = −8", "x = 0"], 0),
             ("Atrisini:  x² = 36",
              ["x = 6 vai x = −6", "x = 6", "x = 18", "x = −6"], 0),
             ("Cik sakņu ir vienādojumam  x² + 4 = 0?",
              ["nevienas", "viena", "divas", "bezgalīgi daudz"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Sadala izteiksmi reizinātājos un izvērš binoma kvadrātu",
         "stunda": TEMATS, "punkti": 5, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Sadali reizinātājos vai izvērs",
              "note": "Ieraksti atbildi! Par katru pareizu pārveidojumu — "
                      "1 punkts.",
              "rindas": [("7x + 7y = ……", "7(x + y)"),
                         ("x² − 36 = ……", "(x − 6)(x + 6)"),
                         ("x² + 8x + 16 = ……", "(x + 4)²"),
                         ("a² − 10a = ……", "a(a − 10)"),
                         ("(x − 3)² = ……", "x² − 6x + 9")]},
             {"tips": "parveide", "virs": "Sadali reizinātājos vai izvērs",
              "note": "Ieraksti atbildi! Par katru pareizu pārveidojumu — "
                      "1 punkts.",
              "rindas": [("5a − 5b = ……", "5(a − b)"),
                         ("y² − 81 = ……", "(y − 9)(y + 9)"),
                         ("y² − 14y + 49 = ……", "(y − 7)²"),
                         ("3x² + 6x = ……", "3x(x + 2)"),
                         ("(x + 5)² = ……", "x² + 10x + 25")]},
             {"tips": "parveide", "virs": "Sadali reizinātājos vai izvērs",
              "note": "Ieraksti atbildi! Par katru pareizu pārveidojumu — "
                      "1 punkts.",
              "rindas": [("4m + 4n = ……", "4(m + n)"),
                         ("25 − x² = ……", "(5 − x)(5 + x)"),
                         ("x² + 12x + 36 = ……", "(x + 6)²"),
                         ("2a² − 8a = ……", "2a(a − 4)"),
                         ("(2x − 1)² = ……", "4x² − 4x + 1")]},
         ]},
        {"sr": "Sadala reizinātājos vairākos soļos un lieto SRF aprēķinos",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Sadalīšana un ātrais aprēķins",
              "vieta": 5.8,
              "teksts": "a) Sadali reizinātājos izteiksmi  5x² − 45.   "
                        "b) Ar saīsinātās reizināšanas formulu aprēķini  "
                        "63² − 37².",
              "kriteriji": [
                  "a) Iznests kopīgais reizinātājs 5(x² − 9).   (1 p.)",
                  "a) Lietota kvadrātu starpība x² − 9 = (x − 3)(x + 3). "
                  "  (1 p.)",
                  "a) Atbilde 5(x − 3)(x + 3).   (1 p.)",
                  "b) Pieraksts (63 − 37)(63 + 37) = 26 · 100.   (1 p.)",
                  "b) Atbilde 2600.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Sadalīšana un ātrais aprēķins",
              "vieta": 5.8,
              "teksts": "a) Sadali reizinātājos izteiksmi  3a² − 12a + 12."
                        "   b) Ar saīsinātās reizināšanas formulu aprēķini  "
                        "98².",
              "kriteriji": [
                  "a) Iznests kopīgais reizinātājs 3(a² − 4a + 4).   (1 p.)",
                  "a) Lietots binoma kvadrāts a² − 4a + 4 = (a − 2)². "
                  "  (1 p.)",
                  "a) Atbilde 3(a − 2)².   (1 p.)",
                  "b) Pieraksts (100 − 2)² = 10 000 − 400 + 4.   (1 p.)",
                  "b) Atbilde 9604.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Sadalīšana un ātrais aprēķins",
              "vieta": 5.8,
              "teksts": "a) Sadali reizinātājos izteiksmi  2x³ − 18x.   "
                        "b) Ar saīsinātās reizināšanas formulu aprēķini  "
                        "45² − 35².",
              "kriteriji": [
                  "a) Iznests kopīgais reizinātājs 2x(x² − 9).   (1 p.)",
                  "a) Lietota kvadrātu starpība x² − 9 = (x − 3)(x + 3). "
                  "  (1 p.)",
                  "a) Atbilde 2x(x − 3)(x + 3).   (1 p.)",
                  "b) Pieraksts (45 − 35)(45 + 35) = 10 · 80.   (1 p.)",
                  "b) Atbilde 800.   (1 p.)"]},
         ]},
        {"sr": "Atrisina nepilnus kvadrātvienādojumus",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Vienādojumi", "vieta": 5.0,
              "teksts": "Atrisini vienādojumus!   a) x² − 7x = 0;   "
                        "b) x² − 64 = 0;   c) 3x² − 27 = 0.",
              "kriteriji": [
                  "a) Sadalīts reizinātājos x(x − 7) = 0.   (1 p.)",
                  "a) Atbilde x = 0 vai x = 7.   (1 p.)",
                  "b) Atbilde x = 8 vai x = −8.   (1 p.)",
                  "c) Pārveidots x² = 9.   (1 p.)",
                  "c) Atbilde x = 3 vai x = −3.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Vienādojumi", "vieta": 5.0,
              "teksts": "Atrisini vienādojumus!   a) 2x² + 10x = 0;   "
                        "b) x² − 11 = 0;   c) (x − 4)(x + 6) = 0.",
              "kriteriji": [
                  "a) Sadalīts reizinātājos 2x(x + 5) = 0.   (1 p.)",
                  "a) Atbilde x = 0 vai x = −5.   (1 p.)",
                  "b) Pārveidots x² = 11.   (1 p.)",
                  "b) Atbilde x = √11 vai x = −√11.   (1 p.)",
                  "c) Atbilde x = 4 vai x = −6.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Vienādojumi", "vieta": 5.0,
              "teksts": "Atrisini vienādojumus!   a) x² + 9x = 0;   "
                        "b) 5x² − 20 = 0;   c) x² − 13 = 0.",
              "kriteriji": [
                  "a) Sadalīts reizinātājos x(x + 9) = 0.   (1 p.)",
                  "a) Atbilde x = 0 vai x = −9.   (1 p.)",
                  "b) Pārveidots x² = 4.   (1 p.)",
                  "b) Atbilde x = 2 vai x = −2.   (1 p.)",
                  "c) Atbilde x = √13 vai x = −√13.   (1 p.)"]},
         ]},
        {"sr": "Lieto sadalīšanu reizinātājos situācijas uzdevumā",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Dota izteiksme  x² − 6x + 9.",
              "jaut": [("Sadali izteiksmi reizinātājos!", 1),
                       ("Aprēķini tās vērtību, ja x = 13!", 1),
                       ("Paskaidro, kāpēc šī izteiksme nekad nav negatīva!",
                        2)],
              "atbildes": ["1) (x − 3)².   (1 p.)",
                           "2) (13 − 3)² = 100.   (1 p.)",
                           "3) Tā ir kvadrāts, bet kvadrāts nekad nav "
                           "negatīvs; mazākā vērtība 0 ir pie x = 3. "
                           "  (2 p.)"]},
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Taisnstūra laukums ir (x² − 25) cm², un tā viena "
                        "mala ir (x − 5) cm.",
              "jaut": [("Sadali laukuma izteiksmi reizinātājos!", 1),
                       ("Cik gara ir otra mala?", 1),
                       ("Aprēķini taisnstūra perimetru, ja x = 9!", 2)],
              "atbildes": ["1) (x − 5)(x + 5).   (1 p.)",
                           "2) (x + 5) cm.   (1 p.)",
                           "3) Malas ir 4 cm un 14 cm, tāpēc P = 36 cm. "
                           "  (2 p.)"]},
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Dota izteiksme  4x² − 12x.",
              "jaut": [("Sadali izteiksmi reizinātājos!", 1),
                       ("Atrisini vienādojumu 4x² − 12x = 0!", 2),
                       ("Cik sakņu ir šim vienādojumam?", 1)],
              "atbildes": ["1) 4x(x − 3).   (1 p.)",
                           "2) 4x(x − 3) = 0, tātad x = 0 vai x = 3. "
                           "  (2 p.)",
                           "3) Divas saknes.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
