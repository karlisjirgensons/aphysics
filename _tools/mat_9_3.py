# -*- coding: utf-8 -*-
"""Matemātika, 9. klase. 9.3. Kā aprēķinos izmanto taisnleņķa trijstūra divu
malu attiecību?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 9. klase, 9.3. temats): šaurā leņķa
pretkatete un piekatete, sinuss, kosinuss un tangenss kā malu attiecības
skaitliskā vērtība, 30°, 45° un 60° precīzās vērtības, nezināmo lielumu
aprēķināšana taisnleņķa trijstūrī un trigonometrisko sakarību lietojums
plaknes figūrās un praktiskās situācijās.
"""

PRIEKSMETS = "Matemātika  |  9. klase"
TEMATS = "9.3."
NOSAUKUMS = "Kā aprēķinos izmanto taisnleņķa trijstūra divu malu attiecību?"

ATGADNE = [
    "sin α = {pretkatete|hipotenūza}      ·      cos α = "
    "{piekatete|hipotenūza}      ·      tg α = {pretkatete|piekatete}",
    "sin 30° = {1|2}   ·   cos 30° = {√3|2}   ·   sin 45° = cos 45° = "
    "{√2|2}   ·   tg 45° = 1",
    "sin 60° = {√3|2}   ·   cos 60° = {1|2}   ·   Pitagora teorēma   "
    "c = √(a² + b²)   ·   šauram leņķim 0 < sin α < 1",
]

FD = {
    "veids": "fd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 9.3. temata beigās. Pārbauda pretkatetes "
                "un piekatetes jēdzienu, sinusa, kosinusa un tangensa "
                "definīciju, 30°, 45° un 60° vērtības un nezināmo lielumu "
                "aprēķināšanu taisnleņķa trijstūrī.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosauc taisnleņķa trijstūra malas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc taisnleņķa trijstūra garāko malu?",
              ["hipotenūza", "katete", "pretkatete", "augstums"], 0),
             ("Kura mala ir leņķa α pretkatete?",
              ["katete pretī leņķim α", "katete pie leņķa α", "hipotenūza",
               "viduslīnija"], 0),
             ("Kura mala ir leņķa α piekatete?",
              ["katete pie leņķa α", "katete pretī leņķim α", "hipotenūza",
               "bisektrise"], 0),
         ]},
        {"sr": "Zina sinusa definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds šaurā leņķa sinuss?",
              ["{pretkatete|hipotenūza}", "{piekatete|hipotenūza}",
               "{pretkatete|piekatete}", "{hipotenūza|pretkatete}"], 0),
             ("Pretkatete 3 cm, hipotenūza 5 cm. Cik liels ir sin α?",
              ["0,6", "0,8", "0,75", "1,67"], 0),
             ("Kas ir šaurā leņķa sinuss?",
              ["skaitlis", "garums centimetros", "leņķis grādos",
               "laukums"], 0),
         ]},
        {"sr": "Zina kosinusa definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds šaurā leņķa kosinuss?",
              ["{piekatete|hipotenūza}", "{pretkatete|hipotenūza}",
               "{piekatete|pretkatete}", "{hipotenūza|piekatete}"], 0),
             ("Piekatete 8 cm, hipotenūza 10 cm. Cik liels ir cos α?",
              ["0,8", "0,6", "1,25", "0,75"], 0),
             ("Kā mainās kosinuss, ja šaurais leņķis palielinās?",
              ["samazinās", "palielinās", "nemainās", "kļūst negatīvs"], 0),
         ]},
        {"sr": "Zina tangensa definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds šaurā leņķa tangenss?",
              ["{pretkatete|piekatete}", "{piekatete|pretkatete}",
               "{pretkatete|hipotenūza}", "{hipotenūza|piekatete}"], 0),
             ("Pretkatete 6 cm, piekatete 8 cm. Cik liels ir tg α?",
              ["0,75", "1,33", "0,6", "0,8"], 0),
             ("Cik liels ir tg 45°?", ["1", "0", "0,5", "√2"], 0),
         ]},
        {"sr": "Zina 30° leņķa vērtības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir sin 30°?",
              ["{1|2}", "{√3|2}", "{√2|2}", "1"], 0),
             ("Cik liels ir cos 30°?",
              ["{√3|2}", "{1|2}", "{√2|2}", "√3"], 0),
             ("Kāda ir katete pret 30° leņķi?",
              ["hipotenūzas puse", "vienāda ar hipotenūzu",
               "divreiz garāka par hipotenūzu", "vienāda ar otru kateti"], 0),
         ]},
        {"sr": "Zina 45° leņķa vērtības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir sin 45°?",
              ["{√2|2}", "{1|2}", "{√3|2}", "1"], 0),
             ("Kā saistīti sin 45° un cos 45°?",
              ["tie ir vienādi", "sinuss ir lielāks", "kosinuss ir lielāks",
               "tie nav saistīti"], 0),
             ("Cik liels ir vienādsānu taisnleņķa trijstūra šaurais leņķis?",
              ["45°", "30°", "60°", "90°"], 0),
         ]},
        {"sr": "Zina 60° leņķa vērtības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir sin 60°?",
              ["{√3|2}", "{1|2}", "{√2|2}", "√3"], 0),
             ("Cik liels ir cos 60°?",
              ["{1|2}", "{√3|2}", "{√2|2}", "1"], 0),
             ("Cik liels ir tg 60°?", ["√3", "{√3|3}", "1", "{1|2}"], 0),
         ]},
        {"sr": "Zina sinusa un kosinusa robežas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādās robežās ir šaurā leņķa sinuss?",
              ["no 0 līdz 1", "no 0 līdz 90", "no 1 līdz 2",
               "jebkurš skaitlis"], 0),
             ("Vai sin α var būt 1,5?",
              ["nē", "jā", "tikai platam leņķim", "to nevar noteikt"], 0),
             ("Kā mainās sinuss, ja šaurais leņķis palielinās?",
              ["palielinās", "samazinās", "nemainās", "kļūst 0"], 0),
         ]},
        {"sr": "Aprēķina kateti pēc leņķa un hipotenūzas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Hipotenūza 10 cm, leņķis 30°. Cik gara ir pretkatete?",
              ["5 cm", "10 cm", "20 cm", "8,7 cm"], 0),
             ("Ar kuru formulu aprēķina pretkateti a?",
              ["a = c · sin α", "a = {c|sin α}", "a = c · tg α",
               "a = c + sin α"], 0),
             ("Hipotenūza 12 cm, leņķis 60°. Cik gara ir piekatete?",
              ["6 cm", "12 cm", "10,4 cm", "24 cm"], 0),
         ]},
        {"sr": "Aprēķina hipotenūzu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina hipotenūzu, ja zināma pretkatete a?",
              ["c = {a|sin α}", "c = a · sin α", "c = {sin α|a}",
               "c = a + sin α"], 0),
             ("Pretkatete 5 cm, leņķis 30°. Cik gara ir hipotenūza?",
              ["10 cm", "2,5 cm", "5 cm", "15 cm"], 0),
             ("Katetes 3 cm un 4 cm. Cik gara ir hipotenūza?",
              ["5 cm", "7 cm", "12 cm", "√7 cm"], 0),
         ]},
        {"sr": "Nosaka leņķi pēc malu attiecības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pretkatete 4 cm, hipotenūza 8 cm. Cik liels ir leņķis α?",
              ["30°", "45°", "60°", "90°"], 0),
             ("Pretkatete un piekatete ir vienādas. Cik liels ir leņķis α?",
              ["45°", "30°", "60°", "90°"], 0),
             ("Ar ko nosaka leņķi, ja zināms tā sinuss?",
              ["ar tabulu vai kalkulatoru", "ar lineālu", "ar cirkuli",
               "ar svariem"], 0),
         ]},
        {"sr": "Lieto trigonometriju praktiskā situācijā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpnes 6 m garas veido ar zemi 30° leņķi. Cik augstu tās "
              "sniedzas?", ["3 m", "6 m", "12 m", "5,2 m"], 0),
             ("Ko nozīmē ceļa slīpums 5 %?",
              ["uz 100 m ceļa pacēlums ir 5 m", "ceļš ir 5 m garš",
               "leņķis ir 5°", "ceļš ir 5 % šaurāks"], 0),
             ("Kā aprēķina torņa augstumu, ja zināms attālums d un leņķis?",
              ["h = d · tg α", "h = d · sin α", "h = {d|tg α}",
               "h = d + α"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 25 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 9.3. temata noslēgumā. "
                "Pārbauda sinusa, kosinusa un tangensa definīciju, 30°, 45° "
                "un 60° vērtības, nezināmo malu un leņķu aprēķināšanu "
                "taisnleņķa trijstūrī un lietojumu praktiskā situācijā.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 25 "
              "punktus. Risinājumu pieraksti tam atvēlētajā vietā; "
              "atļauts kalkulators.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina malu nosaukumus un sinusa definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura mala ir leņķa α pretkatete?",
              ["katete pretī leņķim α", "katete pie leņķa α", "hipotenūza",
               "augstums"], 0),
             ("Ar ko vienāds sin α?",
              ["{pretkatete|hipotenūza}", "{piekatete|hipotenūza}",
               "{pretkatete|piekatete}", "{hipotenūza|pretkatete}"], 0),
             ("Pretkatete 6 cm, hipotenūza 10 cm. Cik liels ir sin α?",
              ["0,6", "0,8", "1,67", "0,75"], 0),
         ]},
        {"sr": "Zina kosinusa un tangensa definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds cos α?",
              ["{piekatete|hipotenūza}", "{pretkatete|hipotenūza}",
               "{piekatete|pretkatete}", "{hipotenūza|piekatete}"], 0),
             ("Ar ko vienāds tg α?",
              ["{pretkatete|piekatete}", "{piekatete|pretkatete}",
               "{pretkatete|hipotenūza}", "{hipotenūza|piekatete}"], 0),
             ("Pretkatete 9 cm, piekatete 12 cm. Cik liels ir tg α?",
              ["0,75", "1,33", "0,6", "0,8"], 0),
         ]},
        {"sr": "Zina 30°, 45° un 60° vērtības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir sin 30°?", ["{1|2}", "{√3|2}", "{√2|2}", "1"], 0),
             ("Cik liels ir cos 45°?", ["{√2|2}", "{1|2}", "{√3|2}", "1"], 0),
             ("Cik liels ir sin 60°?", ["{√3|2}", "{1|2}", "{√2|2}", "√3"],
              0),
         ]},
        {"sr": "Aprēķina katetes garumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Hipotenūza 16 cm, leņķis 30°. Cik gara ir pretkatete?",
              ["8 cm", "16 cm", "32 cm", "13,9 cm"], 0),
             ("Ar kuru formulu aprēķina piekateti b?",
              ["b = c · cos α", "b = c · sin α", "b = {c|cos α}",
               "b = c + cos α"], 0),
             ("Hipotenūza 20 cm, leņķis 60°. Cik gara ir piekatete?",
              ["10 cm", "20 cm", "17,3 cm", "40 cm"], 0),
         ]},
        {"sr": "Aprēķina hipotenūzu un nosaka leņķi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Katetes 6 cm un 8 cm. Cik gara ir hipotenūza?",
              ["10 cm", "14 cm", "48 cm", "√14 cm"], 0),
             ("Pretkatete 7 cm, leņķis 30°. Cik gara ir hipotenūza?",
              ["14 cm", "3,5 cm", "7 cm", "21 cm"], 0),
             ("Pretkatete 5 cm, hipotenūza 10 cm. Cik liels ir leņķis α?",
              ["30°", "45°", "60°", "90°"], 0),
         ]},
        {"sr": "Lieto trigonometriju praktiskā situācijā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpnes 8 m garas veido ar zemi 30° leņķi. Cik augstu tās "
              "sniedzas?", ["4 m", "8 m", "16 m", "6,9 m"], 0),
             ("Ar kuru formulu aprēķina torņa augstumu no attāluma d?",
              ["h = d · tg α", "h = d · sin α", "h = {d|tg α}",
               "h = d · cos α"], 0),
             ("Kāpēc nogāzes garums vienmēr ir lielāks par pacēlumu?",
              ["tā ir hipotenūza", "tā ir katete", "tā ir viduslīnija",
               "tas tā nav"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Lieto trigonometriskās sakarības un precīzās vērtības",
         "stunda": TEMATS, "punkti": 5, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("sin 30° = ……", "{1|2}"),
                         ("cos 45° = ……", "{√2|2}"),
                         ("tg 45° = ……", "1"),
                         ("Pretkatete 4 cm, hipotenūza 8 cm; sin α = ……",
                          "0,5"),
                         ("Katetes 5 cm un 12 cm; hipotenūza ir …… cm",
                          "13")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("cos 60° = ……", "{1|2}"),
                         ("sin 45° = ……", "{√2|2}"),
                         ("sin 60° = ……", "{√3|2}"),
                         ("Piekatete 6 cm, hipotenūza 10 cm; cos α = ……",
                          "0,6"),
                         ("Katetes 9 cm un 12 cm; hipotenūza ir …… cm",
                          "15")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("cos 30° = ……", "{√3|2}"),
                         ("sin 30° + cos 60° = ……", "1"),
                         ("tg 45° · sin 30° = ……", "{1|2}"),
                         ("Pretkatete 7 cm, piekatete 7 cm; α = ……°", "45"),
                         ("Katetes 8 cm un 15 cm; hipotenūza ir …… cm",
                          "17")]},
         ]},
        {"sr": "Aprēķina taisnleņķa trijstūra nezināmos lielumus",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Trijstūra malas un leņķi",
              "vieta": 5.8,
              "teksts": "Taisnleņķa trijstūrī ABC ∠C = 90°, ∠A = 30° un "
                        "hipotenūza AB = 14 cm. Aprēķini abas katetes un "
                        "otru šauro leņķi!",
              "kriteriji": [
                  "Uzzīmēts trijstūris un apzīmētas malas.   (1 p.)",
                  "BC = AB · sin 30° = 14 · {1|2}.   (1 p.)",
                  "Atbilde BC = 7 cm.   (1 p.)",
                  "AC = AB · cos 30° = 7√3 ≈ 12,1 cm.   (1 p.)",
                  "∠B = 60°.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Trijstūra malas un leņķi",
              "vieta": 5.8,
              "teksts": "Taisnleņķa trijstūrī ABC ∠C = 90°, katetes ir "
                        "BC = 5 cm un AC = 12 cm. Aprēķini hipotenūzu un "
                        "leņķa A sinusu, kosinusu un tangensu!",
              "kriteriji": [
                  "Lietota Pitagora teorēma AB = √(5² + 12²).   (1 p.)",
                  "Atbilde AB = 13 cm.   (1 p.)",
                  "sin A = {5|13} ≈ 0,385.   (1 p.)",
                  "cos A = {12|13} ≈ 0,923.   (1 p.)",
                  "tg A = {5|12} ≈ 0,417.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Trijstūra malas un leņķi",
              "vieta": 5.8,
              "teksts": "Taisnleņķa trijstūrī ABC ∠C = 90°, ∠A = 45° un "
                        "katete AC = 8 cm. Aprēķini otru kateti, hipotenūzu "
                        "un trijstūra laukumu!",
              "kriteriji": [
                  "Secināts, ka ∠B = 45° un trijstūris ir vienādsānu. "
                  "  (1 p.)",
                  "BC = 8 cm.   (1 p.)",
                  "AB = 8√2 ≈ 11,3 cm.   (1 p.)",
                  "Lietota laukuma formula S = {8 · 8|2}.   (1 p.)",
                  "Atbilde S = 32 cm².   (1 p.)"]},
         ]},
        {"sr": "Risina praktiska satura uzdevumu",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Trigonometrija praksē",
              "vieta": 5.0,
              "teksts": "Kāpnes ir 6,5 m garas un veido ar zemi 65° leņķi. "
                        "Cik augstu pie sienas tās sniedzas? "
                        "(sin 65° ≈ 0,906)",
              "kriteriji": [
                  "Uzzīmēts taisnleņķa trijstūris.   (1 p.)",
                  "Saskatīts, ka augstums ir pretkatete.   (1 p.)",
                  "Pieraksts h = 6,5 · sin 65°.   (1 p.)",
                  "Aprēķins h ≈ 5,89.   (1 p.)",
                  "Atbilde: aptuveni 5,9 m.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Trigonometrija praksē",
              "vieta": 5.0,
              "teksts": "No 40 m attāluma torņa virsotne redzama 32° leņķī "
                        "pret horizontu. Cik augsts ir tornis? "
                        "(tg 32° ≈ 0,625)",
              "kriteriji": [
                  "Uzzīmēts taisnleņķa trijstūris.   (1 p.)",
                  "Saskatīts, ka augstums ir pretkatete, 40 m — piekatete. "
                  "  (1 p.)",
                  "Pieraksts h = 40 · tg 32°.   (1 p.)",
                  "Aprēķins h = 25.   (1 p.)",
                  "Atbilde: 25 m.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Trigonometrija praksē",
              "vieta": 5.0,
              "teksts": "Slēpošanas nogāze ir 200 m gara, un tās slīpuma "
                        "leņķis ir 18°. Par cik metriem slēpotājs nolaižas? "
                        "(sin 18° ≈ 0,309)",
              "kriteriji": [
                  "Uzzīmēts taisnleņķa trijstūris.   (1 p.)",
                  "Saskatīts, ka nogāze ir hipotenūza.   (1 p.)",
                  "Pieraksts h = 200 · sin 18°.   (1 p.)",
                  "Aprēķins h = 61,8.   (1 p.)",
                  "Atbilde: aptuveni 61,8 m.   (1 p.)"]},
         ]},
        {"sr": "Spriež par malu un leņķu sakarībām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Taisnleņķa trijstūra katetes ir 3 cm un 4 cm; "
                        "leņķis α atrodas pret 3 cm garo kateti.",
              "jaut": [("Aprēķini hipotenūzu!", 1),
                       ("Aprēķini sin α!", 1),
                       ("Aprēķini cos α un tg α!", 2)],
              "atbildes": ["1) c = √(3² + 4²) = 5 cm.   (1 p.)",
                           "2) sin α = {3|5} = 0,6.   (1 p.)",
                           "3) cos α = {4|5} = 0,8 un tg α = {3|4} = 0,75. "
                           "  (2 p.)"]},
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Vienādsānu taisnleņķa trijstūra katete ir 6 cm.",
              "jaut": [("Cik lieli ir abi šaurie leņķi?", 1),
                       ("Aprēķini hipotenūzu!", 2),
                       ("Cik liels ir tg 45°?", 1)],
              "atbildes": ["1) Abi ir 45°.   (1 p.)",
                           "2) c = √(6² + 6²) = 6√2 ≈ 8,5 cm.   (2 p.)",
                           "3) tg 45° = 1.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Taisnleņķa trijstūrī hipotenūza ir 20 cm, bet "
                        "viens šaurais leņķis — 30°.",
              "jaut": [("Cik liels ir otrs šaurais leņķis?", 1),
                       ("Aprēķini kateti pret 30° leņķi!", 1),
                       ("Aprēķini otru kateti!", 2)],
              "atbildes": ["1) 60°.   (1 p.)",
                           "2) 20 · {1|2} = 10 cm.   (1 p.)",
                           "3) 20 · cos 30° = 10√3 ≈ 17,3 cm.   (2 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
