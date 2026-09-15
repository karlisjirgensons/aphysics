# -*- coding: utf-8 -*-
"""Matemātika, 9. klase. 9.5. Kā skaidro un izmanto formulas darbā ar
kvadrātvienādojumu, kvadrātfunkciju?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 9. klase, 9.5. temats): kvadrātvienādojuma
pamatforma un koeficienti, diskriminants un sakņu skaits, sakņu formula,
ekvivalenti pārveidojumi, kvadrātfunkcijas grafiks, zaru vērsums, virsotnes
formula un funkcijas nulles, kvadrātnevienādības atrisinājuma nolasīšana no
grafika skices un situāciju uzdevumu modelēšana ar kvadrātvienādojumu.
"""

PRIEKSMETS = "Matemātika  |  9. klase"
TEMATS = "9.5."
NOSAUKUMS = ("Kā skaidro un izmanto formulas darbā ar kvadrātvienādojumu, "
             "kvadrātfunkciju?")

ATGADNE = [
    "Kvadrātvienādojums   ax² + bx + c = 0      ·      diskriminants   "
    "D = b² − 4ac      ·      saknes   x = {−b ± √D|2a}",
    "D > 0 — divas saknes   ·   D = 0 — viena sakne   ·   D < 0 — sakņu nav",
    "Parabolas virsotne   x₀ = {−b|2a}   ·   zari vērsti uz augšu, ja "
    "a > 0, un uz leju, ja a < 0",
]

FD = {
    "veids": "fd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 9.5. temata beigās. Pārbauda "
                "kvadrātvienādojuma pamatformu un koeficientus, "
                "diskriminantu un sakņu skaitu, sakņu formulu, "
                "kvadrātfunkcijas grafiku, virsotni un funkcijas nulles.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina kvadrātvienādojuma pamatformu un koeficientus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir kvadrātvienādojuma pamatforma?",
              ["ax² + bx + c = 0", "ax + b = 0", "ax³ + b = 0",
               "ax² = bx"], 0),
             ("Kādi ir koeficienti vienādojumā 2x² − 5x + 3 = 0?",
              ["a = 2, b = −5, c = 3", "a = 2, b = 5, c = 3",
               "a = 2, b = −5, c = −3", "a = −2, b = 5, c = 3"], 0),
             ("Kāds ir koeficients b vienādojumā x² − 7 = 0?",
              ["0", "−7", "1", "7"], 0),
         ]},
        {"sr": "Zina diskriminanta formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina diskriminantu?",
              ["D = b² − 4ac", "D = b² + 4ac", "D = b − 4ac",
               "D = 4ac − b"], 0),
             ("Cik liels ir D vienādojumam x² − 5x + 6 = 0?",
              ["1", "49", "−1", "25"], 0),
             ("Cik liels ir D vienādojumam x² + 2x + 1 = 0?",
              ["0", "4", "8", "−4"], 0),
         ]},
        {"sr": "Nosaka sakņu skaitu pēc diskriminanta",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik sakņu ir, ja D > 0?",
              ["divas", "viena", "nevienas", "bezgalīgi daudz"], 0),
             ("Cik sakņu ir, ja D = 0?",
              ["viena", "divas", "nevienas", "trīs"], 0),
             ("Cik sakņu ir, ja D < 0?",
              ["nevienas", "viena", "divas", "trīs"], 0),
         ]},
        {"sr": "Zina sakņu formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir sakņu formula?",
              ["x = {−b ± √D|2a}", "x = {b ± √D|2a}", "x = {−b ± √D|a}",
               "x = {−b ± D|2a}"], 0),
             ("Kas atrodas zem saknes zīmes?",
              ["diskriminants", "koeficients a", "koeficients b",
               "brīvais loceklis"], 0),
             ("Kāpēc formulā ir zīme ±?",
              ["sakņu var būt divas", "lai atbilde būtu pozitīva",
               "tā ir kļūda", "lai saīsinātu pierakstu"], 0),
         ]},
        {"sr": "Atrisina kvadrātvienādojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Atrisini:  x² − 5x + 6 = 0",
              ["x = 2 vai x = 3", "x = −2 vai x = −3", "x = 1 vai x = 6",
               "x = 5"], 0),
             ("Atrisini:  x² − 4x + 4 = 0",
              ["x = 2", "x = −2", "x = 4", "x = 2 vai x = −2"], 0),
             ("Atrisini:  x² + x + 5 = 0",
              ["sakņu nav", "x = 5", "x = −1", "x = 0"], 0),
         ]},
        {"sr": "Veic ekvivalentus pārveidojumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas jādara vispirms ar vienādojumu x² = 3x + 10?",
              ["pārveido pamatformā", "dala ar x", "atņem 10",
               "reizina ar 3"], 0),
             ("Kāda ir vienādojuma x² = 3x + 10 pamatforma?",
              ["x² − 3x − 10 = 0", "x² + 3x + 10 = 0", "x² − 3x + 10 = 0",
               "x² + 3x − 10 = 0"], 0),
             ("Atrisini:  x² = 3x + 10",
              ["x = 5 vai x = −2", "x = −5 vai x = 2", "x = 5", "x = 10"],
              0),
         ]},
        {"sr": "Zina kvadrātfunkciju un tās grafiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir kvadrātfunkcijas grafiks?",
              ["parabola", "taisne", "riņķa līnija", "hiperbola"], 0),
             ("Kura no funkcijām ir kvadrātfunkcija?",
              ["y = x² − 3x + 2", "y = 2x + 1", "y = {1|x}", "y = 3"], 0),
             ("Kā sauc parabolas zemāko vai augstāko punktu?",
              ["virsotne", "nulle", "ass", "fokuss"], 0),
         ]},
        {"sr": "Nosaka parabolas zaru vērsumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurp vērsti parabolas zari, ja a > 0?",
              ["uz augšu", "uz leju", "pa kreisi", "pa labi"], 0),
             ("Kurp vērsti zari funkcijai y = −2x² + 3?",
              ["uz leju", "uz augšu", "pa labi", "pa kreisi"], 0),
             ("Kad funkcijai ir mazākā vērtība?",
              ["ja zari vērsti uz augšu", "ja zari vērsti uz leju",
               "vienmēr", "nekad"], 0),
         ]},
        {"sr": "Aprēķina virsotnes abscisu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina virsotnes abscisu?",
              ["x₀ = {−b|2a}", "x₀ = {b|2a}", "x₀ = {−b|a}",
               "x₀ = {−2a|b}"], 0),
             ("Cik liela ir virsotnes abscisa funkcijai y = x² − 6x + 5?",
              ["3", "−3", "6", "−6"], 0),
             ("Funkcijas nulles ir 1 un 5. Cik liela ir virsotnes abscisa?",
              ["3", "2", "5", "6"], 0),
         ]},
        {"sr": "Nosaka funkcijas nulles",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir funkcijas nulles?",
              ["x vērtības, kurās y = 0", "y vērtības, kurās x = 0",
               "virsotnes koordinātas", "grafika galapunkti"], 0),
             ("Kā atrod funkcijas y = x² − 5x + 6 nulles?",
              ["atrisina x² − 5x + 6 = 0", "ievieto x = 0",
               "ievieto y = 1", "atņem 6"], 0),
             ("Kādas ir funkcijas y = x² − 9 nulles?",
              ["x = 3 un x = −3", "x = 9", "x = 3", "x = 0"], 0),
         ]},
        {"sr": "Atrisina kvadrātnevienādību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur no grafika nolasa nevienādības x² − 4 > 0 atrisinājumu?",
              ["kur parabola ir virs x ass", "kur parabola ir zem x ass",
               "virsotnē", "uz y ass"], 0),
             ("Atrisini:  x² − 4 > 0",
              ["x < −2 vai x > 2", "−2 < x < 2", "x > 2", "x < 2"], 0),
             ("Atrisini:  x² − 9 < 0",
              ["−3 < x < 3", "x < −3 vai x > 3", "x < 3", "x > 3"], 0),
         ]},
        {"sr": "Modelē situāciju ar kvadrātvienādojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Laukums ir 24 m², garums par 2 m lielāks nekā platums x. "
              "Kurš vienādojums der?",
              ["x(x + 2) = 24", "x + (x + 2) = 24", "x² = 24",
               "2x + 2 = 24"], 0),
             ("Kāpēc negatīvu sakni situācijas uzdevumā noraida?",
              ["garums nevar būt negatīvs", "tā ir kļūdaina",
               "tā ir pārāk maza", "to nenoraida"], 0),
             ("Saknes ir −4 un 6. Kura der taisnstūra malas garumam?",
              ["6", "−4", "abas", "neviena"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 25 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 9.5. temata noslēgumā. "
                "Pārbauda diskriminantu un sakņu skaitu, sakņu formulas "
                "lietojumu, ekvivalentus pārveidojumus, kvadrātfunkcijas "
                "nulles, virsotni un grafika skici un situāciju uzdevumu "
                "modelēšanu ar kvadrātvienādojumu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 25 "
              "punktus. Risinājumu pieraksti tam atvēlētajā vietā; "
              "atļauts kalkulators.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina pamatformu, koeficientus un diskriminantu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir kvadrātvienādojuma pamatforma?",
              ["ax² + bx + c = 0", "ax + b = 0", "ax³ + b = 0",
               "ax² = bx"], 0),
             ("Ar kuru formulu aprēķina diskriminantu?",
              ["D = b² − 4ac", "D = b² + 4ac", "D = b − 4ac",
               "D = 4ac − b²"], 0),
             ("Kādi ir koeficienti vienādojumā 3x² − 4x + 1 = 0?",
              ["a = 3, b = −4, c = 1", "a = 3, b = 4, c = 1",
               "a = 3, b = −4, c = −1", "a = −3, b = 4, c = 1"], 0),
         ]},
        {"sr": "Nosaka sakņu skaitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik sakņu ir, ja D = 0?",
              ["viena", "divas", "nevienas", "trīs"], 0),
             ("Cik liels ir D vienādojumam x² − 6x + 9 = 0?",
              ["0", "36", "72", "−36"], 0),
             ("Cik sakņu ir vienādojumam, kuram D = −5?",
              ["nevienas", "viena", "divas", "piecas"], 0),
         ]},
        {"sr": "Lieto sakņu formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura ir sakņu formula?",
              ["x = {−b ± √D|2a}", "x = {b ± √D|2a}", "x = {−b ± √D|a}",
               "x = {−b ± D|2a}"], 0),
             ("Atrisini:  x² − 7x + 12 = 0",
              ["x = 3 vai x = 4", "x = −3 vai x = −4", "x = 2 vai x = 6",
               "x = 12"], 0),
             ("Atrisini:  x² − 2x − 8 = 0",
              ["x = 4 vai x = −2", "x = −4 vai x = 2", "x = 8",
               "sakņu nav"], 0),
         ]},
        {"sr": "Veic ekvivalentus pārveidojumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāda ir vienādojuma x² = 5x − 6 pamatforma?",
              ["x² − 5x + 6 = 0", "x² + 5x − 6 = 0", "x² − 5x − 6 = 0",
               "x² + 5x + 6 = 0"], 0),
             ("Kas jādara vispirms ar vienādojumu 2x² = 8x?",
              ["pārveido pamatformā", "dala ar x", "dala ar 2",
               "atņem 8"], 0),
             ("Kāpēc vienādojumu nedrīkst dalīt ar x?",
              ["var pazaudēt sakni x = 0", "mainās zīme",
               "atbilde kļūst lielāka", "to drīkst"], 0),
         ]},
        {"sr": "Raksturo kvadrātfunkcijas grafiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir kvadrātfunkcijas grafiks?",
              ["parabola", "taisne", "riņķa līnija", "hiperbola"], 0),
             ("Kurp vērsti zari funkcijai y = −x² + 2x?",
              ["uz leju", "uz augšu", "pa labi", "pa kreisi"], 0),
             ("Ar kuru formulu aprēķina virsotnes abscisu?",
              ["x₀ = {−b|2a}", "x₀ = {b|2a}", "x₀ = {−b|a}",
               "x₀ = {−2a|b}"], 0),
         ]},
        {"sr": "Nosaka funkcijas nulles un atrisina nevienādību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir funkcijas y = x² − 16 nulles?",
              ["x = 4 un x = −4", "x = 16", "x = 4", "x = 0"], 0),
             ("Atrisini:  x² − 25 < 0",
              ["−5 < x < 5", "x < −5 vai x > 5", "x < 5", "x > 5"], 0),
             ("Kas ir funkcijas nulles?",
              ["x vērtības, kurās y = 0", "y vērtības, kurās x = 0",
               "virsotnes koordinātas", "grafika galapunkti"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina diskriminantu, saknes un virsotni",
         "stunda": TEMATS, "punkti": 5, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("x² − 5x + 6 = 0;   D = ……", "1"),
                         ("x² − 5x + 6 = 0;   x = ……", "2 un 3"),
                         ("x² + 2x + 1 = 0;   D = ……", "0"),
                         ("y = x² − 6x + 5;   x₀ = ……", "3"),
                         ("y = −x² + 4;   zari vērsti ……", "uz leju")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("x² − 7x + 12 = 0;   D = ……", "1"),
                         ("x² − 7x + 12 = 0;   x = ……", "3 un 4"),
                         ("x² + x + 3 = 0;   D = ……", "−11"),
                         ("y = x² − 8x + 7;   x₀ = ……", "4"),
                         ("y = 3x² − 1;   zari vērsti ……", "uz augšu")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("x² − 2x − 8 = 0;   D = ……", "36"),
                         ("x² − 2x − 8 = 0;   x = ……", "4 un −2"),
                         ("x² − 6x + 9 = 0;   D = ……", "0"),
                         ("y = x² + 4x + 1;   x₀ = ……", "−2"),
                         ("y = −2x² + 5;   zari vērsti ……", "uz leju")]},
         ]},
        {"sr": "Atrisina kvadrātvienādojumu ar sakņu formulu",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Kvadrātvienādojums", "vieta": 5.8,
              "teksts": "Atrisini vienādojumu  x² − 3x − 10 = 0, lietojot "
                        "sakņu formulu! Pieraksti visus risinājuma soļus.",
              "kriteriji": [
                  "Noteikti koeficienti a = 1, b = −3, c = −10.   (1 p.)",
                  "Pieraksts D = (−3)² − 4 · 1 · (−10).   (1 p.)",
                  "Aprēķināts D = 49 un √D = 7.   (1 p.)",
                  "Lietota formula x = {3 ± 7|2}.   (1 p.)",
                  "Atbilde x = 5 vai x = −2.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Kvadrātvienādojums", "vieta": 5.8,
              "teksts": "Atrisini vienādojumu  2x² − 7x + 3 = 0, lietojot "
                        "sakņu formulu! Pieraksti visus risinājuma soļus.",
              "kriteriji": [
                  "Noteikti koeficienti a = 2, b = −7, c = 3.   (1 p.)",
                  "Pieraksts D = (−7)² − 4 · 2 · 3.   (1 p.)",
                  "Aprēķināts D = 25 un √D = 5.   (1 p.)",
                  "Lietota formula x = {7 ± 5|4}.   (1 p.)",
                  "Atbilde x = 3 vai x = 0,5.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Kvadrātvienādojums", "vieta": 5.8,
              "teksts": "Atrisini vienādojumu  x² = 4x + 12, lietojot sakņu "
                        "formulu! Pieraksti visus risinājuma soļus.",
              "kriteriji": [
                  "Pārveidots pamatformā x² − 4x − 12 = 0.   (1 p.)",
                  "Pieraksts D = (−4)² − 4 · 1 · (−12).   (1 p.)",
                  "Aprēķināts D = 64 un √D = 8.   (1 p.)",
                  "Lietota formula x = {4 ± 8|2}.   (1 p.)",
                  "Atbilde x = 6 vai x = −2.   (1 p.)"]},
         ]},
        {"sr": "Pēta kvadrātfunkciju un zīmē tās grafika skici",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Kvadrātfunkcija", "vieta": 5.0,
              "teksts": "Dota funkcija  y = x² − 4x + 3. Aprēķini funkcijas "
                        "nulles un virsotnes koordinātas, nosaki zaru "
                        "vērsumu un uzzīmē grafika skici!",
              "kriteriji": ["Nulles: x = 1 un x = 3.   (1 p.)",
                            "Virsotnes abscisa x₀ = 2.   (1 p.)",
                            "Virsotnes ordināta y₀ = −1.   (1 p.)",
                            "Zari vērsti uz augšu, jo a > 0.   (1 p.)",
                            "Uzzīmēta skice ar nullēm un virsotni.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Kvadrātfunkcija", "vieta": 5.0,
              "teksts": "Dota funkcija  y = x² − 2x − 3. Aprēķini funkcijas "
                        "nulles un virsotnes koordinātas, nosaki zaru "
                        "vērsumu un uzzīmē grafika skici!",
              "kriteriji": ["Nulles: x = 3 un x = −1.   (1 p.)",
                            "Virsotnes abscisa x₀ = 1.   (1 p.)",
                            "Virsotnes ordināta y₀ = −4.   (1 p.)",
                            "Zari vērsti uz augšu, jo a > 0.   (1 p.)",
                            "Uzzīmēta skice ar nullēm un virsotni.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Kvadrātfunkcija", "vieta": 5.0,
              "teksts": "Dota funkcija  y = −x² + 4x. Aprēķini funkcijas "
                        "nulles un virsotnes koordinātas, nosaki zaru "
                        "vērsumu un uzzīmē grafika skici!",
              "kriteriji": ["Nulles: x = 0 un x = 4.   (1 p.)",
                            "Virsotnes abscisa x₀ = 2.   (1 p.)",
                            "Virsotnes ordināta y₀ = 4.   (1 p.)",
                            "Zari vērsti uz leju, jo a < 0.   (1 p.)",
                            "Uzzīmēta skice ar nullēm un virsotni.   (1 p.)"]},
         ]},
        {"sr": "Lieto kvadrātvienādojumu situācijas aprakstam",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Situācijas modelis", "vieta": 4.4,
              "ievads": "Taisnstūra laukums ir 24 m², un tā garums ir par "
                        "2 m lielāks nekā platums.",
              "jaut": [("Apzīmē platumu ar x un pieraksti vienādojumu!", 1),
                       ("Pārveido to pamatformā!", 1),
                       ("Atrisini vienādojumu!", 1),
                       ("Nosauc taisnstūra malu garumus!", 1)],
              "atbildes": ["1) x(x + 2) = 24.   (1 p.)",
                           "2) x² + 2x − 24 = 0.   (1 p.)",
                           "3) x = 4 vai x = −6.   (1 p.)",
                           "4) Malas ir 4 m un 6 m; sakni −6 noraida. "
                           "  (1 p.)"]},
             {"tips": "jautajumi", "virs": "Funkcija un nevienādība",
              "vieta": 4.4,
              "ievads": "Dota funkcija  y = x² − 6x + 8.",
              "jaut": [("Aprēķini funkcijas nulles!", 2),
                       ("Cik liela ir virsotnes abscisa?", 1),
                       ("Atrisini nevienādību x² − 6x + 8 < 0!", 1)],
              "atbildes": ["1) D = 4; nulles x = 2 un x = 4.   (2 p.)",
                           "2) x₀ = 3.   (1 p.)",
                           "3) 2 < x < 4.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Diskriminants un koeficients",
              "vieta": 4.4,
              "ievads": "Kvadrātvienādojuma  x² + bx + 9 = 0  diskriminants "
                        "ir 0.",
              "jaut": [("Pieraksti diskriminanta formulu šim "
                        "vienādojumam!", 1),
                       ("Aprēķini koeficientu b!", 2),
                       ("Cik sakņu ir šim vienādojumam?", 1)],
              "atbildes": ["1) D = b² − 36.   (1 p.)",
                           "2) b² = 36, tātad b = 6 vai b = −6.   (2 p.)",
                           "3) Viena sakne.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
