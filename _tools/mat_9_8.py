# -*- coding: utf-8 -*-
"""Matemātika, 9. klase. 9.8. Kā raksturo riņķa līnijas un daudzstūra
savstarpējo novietojumu?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 9. klase, 9.8. temats): ap daudzstūri
apvilkta un daudzstūrī ievilkta riņķa līnija un to centru novietojums, riņķa
līnijas pieskare un tās īpašība, regulārs daudzstūris, daudzstūra leņķu
summa un sakarība starp regulāra daudzstūra leņķi un leņķu summu.
"""

PRIEKSMETS = "Matemātika  |  9. klase"
TEMATS = "9.8."
NOSAUKUMS = "Kā raksturo riņķa līnijas un daudzstūra savstarpējo novietojumu?"

ATGADNE = [
    "Apvilkta riņķa līnija iet caur visām virsotnēm; centrs ir vienādā "
    "attālumā no virsotnēm — malu vidusperpendikulu krustpunktā.",
    "Ievilkta riņķa līnija pieskaras visām malām; centrs ir vienādā "
    "attālumā no malām — leņķu bisektrišu krustpunktā.",
    "Pieskaršanās punktā vilktais rādiuss ir perpendikulārs pieskarei   ·   "
    "n-stūra leņķu summa   S = (n − 2) · 180°",
]

FD = {
    "veids": "fd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 9.8. temata beigās. Pārbauda apvilktas "
                "un ievilktas riņķa līnijas jēdzienu un centru novietojumu, "
                "pieskares īpašību, daudzstūra leņķu summu un regulāra "
                "daudzstūra leņķa aprēķināšanu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, kas ir apvilkta riņķa līnija",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad riņķa līnija ir apvilkta ap daudzstūri?",
              ["ja tā iet caur visām virsotnēm", "ja tā pieskaras malām",
               "ja tā ir iekšpusē", "ja tā krusto malas"], 0),
             ("Kā sauc daudzstūri, ap kuru apvilkta riņķa līnija?",
              ["riņķī ievilkts", "ap riņķi apvilkts", "regulārs",
               "taisnleņķa"], 0),
             ("Ap kuru figūru riņķa līniju var apvilkt vienmēr?",
              ["ap jebkuru trijstūri", "ap jebkuru četrstūri",
               "ap jebkuru daudzstūri", "ne ap vienu"], 0),
         ]},
        {"sr": "Nosaka apvilktās riņķa līnijas centru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur ir ap trijstūri apvilktās riņķa līnijas centrs?",
              ["vienādi tālu no virsotnēm", "vienādi tālu no malām",
               "virsotnē", "malas vidū"], 0),
             ("Kuru līniju krustpunktā ir apvilktās riņķa līnijas centrs?",
              ["malu vidusperpendikulu", "bisektrišu", "augstumu",
               "mediānu"], 0),
             ("Kas ir apvilktās riņķa līnijas rādiuss?",
              ["attālums līdz virsotnei", "attālums līdz malai",
               "malas garums", "perimetrs"], 0),
         ]},
        {"sr": "Zina, kas ir ievilkta riņķa līnija",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad riņķa līnija ir ievilkta daudzstūrī?",
              ["ja tā pieskaras visām malām", "ja tā iet caur virsotnēm",
               "ja tā ir ārpusē", "ja tā krusto malas"], 0),
             ("Kā sauc daudzstūri, kurā ievilkta riņķa līnija?",
              ["ap riņķa līniju apvilkts", "riņķī ievilkts", "regulārs",
               "vienādsānu"], 0),
             ("Kurā figūrā riņķa līniju var ievilkt vienmēr?",
              ["jebkurā trijstūrī", "jebkurā četrstūrī",
               "jebkurā daudzstūrī", "nevienā"], 0),
         ]},
        {"sr": "Nosaka ievilktās riņķa līnijas centru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur atrodas trijstūrī ievilktās riņķa līnijas centrs?",
              ["vienādi tālu no malām", "vienādi tālu no virsotnēm",
               "virsotnē", "ārpusē"], 0),
             ("Kuru līniju krustpunktā atrodas šis centrs?",
              ["leņķu bisektrišu", "vidusperpendikulu", "augstumu",
               "viduslīniju"], 0),
             ("Kas ir ievilktās riņķa līnijas rādiuss?",
              ["attālums līdz malai", "attālums līdz virsotnei",
               "diagonāle", "perimetrs"], 0),
         ]},
        {"sr": "Spriež par četrstūriem un riņķa līniju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai ap katru četrstūri var apvilkt riņķa līniju?",
              ["nē, tikai ap dažiem", "jā, ap katru", "tikai ap rombu",
               "ne ap vienu"], 0),
             ("Vai ap kvadrātu var apvilkt riņķa līniju?",
              ["jā", "nē", "tikai ap lielu kvadrātu", "nevar noteikt"], 0),
             ("Vai katrā četrstūrī var ievilkt riņķa līniju?",
              ["nē, tikai dažos", "jā, katrā", "tikai taisnstūrī",
               "nevienā"], 0),
         ]},
        {"sr": "Zina, kas ir pieskare",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir riņķa līnijas pieskare?",
              ["taisne ar vienu kopīgu punktu", "taisne ar diviem punktiem",
               "nogrieznis caur centru", "rādiuss"], 0),
             ("Cik kopīgu punktu ir pieskarei un riņķa līnijai?",
              ["viens", "divi", "neviens", "bezgalīgi daudz"], 0),
             ("Cik pieskaru var novilkt vienai riņķa līnijai?",
              ["bezgalīgi daudz", "vienu", "divas", "četras"], 0),
         ]},
        {"sr": "Lieto pieskares īpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir leņķis starp pieskari un pieskaršanās punktā "
              "vilktu rādiusu?", ["90°", "45°", "60°", "180°"], 0),
             ("Ko var apgalvot par rādiusu pieskaršanās punktā?",
              ["tas ir perpendikulārs pieskarei",
               "tas ir paralēls pieskarei", "tas sakrīt ar pieskari",
               "tas ir divreiz garāks"], 0),
             ("Kura mala ir hipotenūza trijstūrī «centrs — pieskaršanās "
              "punkts — ārējs punkts»?",
              ["nogrieznis no centra līdz ārējam punktam", "rādiuss",
               "pieskares nogrieznis", "tādas nav"], 0),
         ]},
        {"sr": "Aprēķina daudzstūra leņķu summu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir trijstūra leņķu summa?",
              ["180°", "360°", "90°", "540°"], 0),
             ("Ar kuru formulu aprēķina n-stūra leņķu summu?",
              ["(n − 2) · 180°", "n · 180°", "(n − 1) · 180°",
               "360° : n"], 0),
             ("Cik liela ir piecstūra leņķu summa?",
              ["540°", "360°", "720°", "180°"], 0),
         ]},
        {"sr": "Zina, kas ir regulārs daudzstūris",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir regulārs daudzstūris?",
              ["visas malas un leņķi ir vienādi", "visas malas ir vienādas",
               "visi leņķi ir taisni", "tam ir četras malas"], 0),
             ("Kurš ir regulārs četrstūris?",
              ["kvadrāts", "taisnstūris", "rombs", "trapece"], 0),
             ("Vai regulāram daudzstūrim var ievilkt un apvilkt riņķa "
              "līniju?", ["jā, abas", "tikai ievilkt", "tikai apvilkt",
                          "nevienu"], 0),
         ]},
        {"sr": "Aprēķina regulāra daudzstūra leņķi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir regulāra sešstūra leņķis?",
              ["120°", "60°", "90°", "135°"], 0),
             ("Cik liels ir regulāra piecstūra leņķis?",
              ["108°", "120°", "72°", "144°"], 0),
             ("Kā aprēķina regulāra n-stūra leņķi?",
              ["leņķu summu dala ar n", "360° dala ar n",
               "n reizina ar 180°", "no 180° atņem n"], 0),
         ]},
        {"sr": "Nosaka malu skaitu pēc leņķu summas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Daudzstūra leņķu summa ir 720°. Cik malu tam ir?",
              ["6", "5", "7", "4"], 0),
             ("Daudzstūra leņķu summa ir 1080°. Cik malu tam ir?",
              ["8", "6", "10", "9"], 0),
             ("Cik liela ir četrstūra leņķu summa?",
              ["360°", "180°", "540°", "720°"], 0),
         ]},
        {"sr": "Risina kombinētus uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur taisnleņķa trijstūrī atrodas apvilktās riņķa līnijas "
              "centrs?",
              ["hipotenūzas viduspunktā", "virsotnē",
               "katetes viduspunktā", "ārpus trijstūra"], 0),
             ("Kāpēc ap katru trijstūri var apvilkt riņķa līniju?",
              ["vidusperpendikuli krustojas vienā punktā",
               "trijstūris ir mazs", "malas ir vienādas", "tā nav"], 0),
             ("Regulāra daudzstūra leņķis ir 120°. Cik tam ir malu?",
              ["6", "5", "8", "4"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 25 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 9.8. temata noslēgumā. "
                "Pārbauda apvilktas un ievilktas riņķa līnijas centru "
                "novietojumu, pieskares īpašības lietojumu aprēķinos, "
                "daudzstūra leņķu summu un regulāra daudzstūra leņķa un "
                "malu skaita noteikšanu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 25 "
              "punktus. Risinājumu pieraksti tam atvēlētajā vietā; "
              "atļauts kalkulators.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina apvilktas riņķa līnijas īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad riņķa līnija ir apvilkta ap daudzstūri?",
              ["ja tā iet caur visām virsotnēm",
               "ja tā pieskaras visām malām", "ja tā ir iekšpusē",
               "ja tā krusto malas"], 0),
             ("Kur atrodas apvilktās riņķa līnijas centrs?",
              ["vienādā attālumā no virsotnēm",
               "vienādā attālumā no malām", "virsotnē", "malas galā"], 0),
             ("Kuru līniju krustpunktā tas atrodas?",
              ["malu vidusperpendikulu", "bisektrišu", "augstumu",
               "mediānu"], 0),
         ]},
        {"sr": "Zina ievilktas riņķa līnijas īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad riņķa līnija ir ievilkta daudzstūrī?",
              ["ja tā pieskaras visām malām", "ja tā iet caur virsotnēm",
               "ja tā ir ārpusē", "ja tā krusto malas"], 0),
             ("Kur atrodas ievilktās riņķa līnijas centrs?",
              ["vienādā attālumā no malām",
               "vienādā attālumā no virsotnēm", "virsotnē", "ārpusē"], 0),
             ("Kuru līniju krustpunktā atrodas šis centrs?",
              ["leņķu bisektrišu", "vidusperpendikulu", "augstumu",
               "viduslīniju"], 0),
         ]},
        {"sr": "Lieto pieskares īpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir riņķa līnijas pieskare?",
              ["taisne ar vienu kopīgu punktu",
               "taisne ar diviem kopīgiem punktiem", "rādiuss",
               "diametrs"], 0),
             ("Cik liels ir leņķis starp pieskari un rādiusu pieskaršanās "
              "punktā?", ["90°", "45°", "60°", "180°"], 0),
             ("Kuru teorēmu lieto, aprēķinot pieskares nogriezni?",
              ["Pitagora teorēmu", "Talesa teorēmu",
               "leņķu summas teorēmu", "Huka likumu"], 0),
         ]},
        {"sr": "Aprēķina daudzstūra leņķu summu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina n-stūra leņķu summu?",
              ["(n − 2) · 180°", "n · 180°", "(n − 1) · 180°",
               "360° : n"], 0),
             ("Cik liela ir sešstūra leņķu summa?",
              ["720°", "540°", "900°", "360°"], 0),
             ("Daudzstūra leņķu summa ir 900°. Cik malu tam ir?",
              ["7", "6", "8", "9"], 0),
         ]},
        {"sr": "Aprēķina regulāra daudzstūra leņķi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liels ir regulāra sešstūra leņķis?",
              ["120°", "60°", "90°", "135°"], 0),
             ("Cik liels ir regulāra astoņstūra leņķis?",
              ["135°", "120°", "144°", "45°"], 0),
             ("Regulāra daudzstūra leņķis ir 108°. Cik tam ir malu?",
              ["5", "6", "8", "4"], 0),
         ]},
        {"sr": "Risina kombinētus uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur taisnleņķa trijstūrī atrodas apvilktās riņķa līnijas "
              "centrs?",
              ["hipotenūzas viduspunktā", "virsotnē",
               "katetes viduspunktā", "ārpus trijstūra"], 0),
             ("Vai ap katru četrstūri var apvilkt riņķa līniju?",
              ["nē, tikai ap dažiem", "jā, ap katru", "tikai ap rombu",
               "ne ap vienu"], 0),
             ("Vai regulāram daudzstūrim var ievilkt riņķa līniju?",
              ["jā", "nē", "tikai kvadrātam", "tikai sešstūrim"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina leņķu summu, leņķi un malu skaitu",
         "stunda": TEMATS, "punkti": 5, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Trijstūra leņķu summa ir ……°", "180"),
                         ("Piecstūra leņķu summa ir ……°", "540"),
                         ("Regulāra sešstūra leņķis ir ……°", "120"),
                         ("Leņķu summa 720°;  malu skaits ir ……", "6"),
                         ("Leņķis starp pieskari un rādiusu ir ……°", "90")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Četrstūra leņķu summa ir ……°", "360"),
                         ("Sešstūra leņķu summa ir ……°", "720"),
                         ("Regulāra piecstūra leņķis ir ……°", "108"),
                         ("Leņķu summa 1080°;  malu skaits ir ……", "8"),
                         ("Pieskarei un riņķa līnijai ir …… kopīgs punkts",
                          "1")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Astoņstūra leņķu summa ir ……°", "1080"),
                         ("Kvadrāta leņķis ir ……°", "90"),
                         ("Regulāra astoņstūra leņķis ir ……°", "135"),
                         ("Leņķu summa 540°;  malu skaits ir ……", "5"),
                         ("Apvilktās riņķa līnijas centrs ir …… "
                          "krustpunktā", "vidusperpendikulu")]},
         ]},
        {"sr": "Aprēķina lielumus figūrā ar riņķa līniju",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Riņķa līnija un daudzstūris",
              "vieta": 5.8,
              "teksts": "Taisnleņķa trijstūrī katetes ir 6 cm un 8 cm.   "
                        "a) Aprēķini hipotenūzu.   b) Kur atrodas ap šo "
                        "trijstūri apvilktās riņķa līnijas centrs?   "
                        "c) Cik liels ir šīs riņķa līnijas rādiuss?",
              "kriteriji": ["a) Lietota Pitagora teorēma c = √(6² + 8²). "
                            "  (1 p.)",
                            "a) Atbilde c = 10 cm.   (1 p.)",
                            "b) Centrs ir hipotenūzas viduspunktā.   (1 p.)",
                            "b) Pamatots ar to, ka centrs ir vienādā "
                            "attālumā no virsotnēm.   (1 p.)",
                            "c) Rādiuss R = 5 cm.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Riņķa līnija un daudzstūris",
              "vieta": 5.8,
              "teksts": "Regulāra sešstūra mala ir 4 cm.   a) Aprēķini tā "
                        "leņķu summu.   b) Cik liels ir viens tā leņķis?   "
                        "c) Cik liels ir sešstūra perimetrs?",
              "kriteriji": ["a) Lietota formula (6 − 2) · 180°.   (1 p.)",
                            "a) Atbilde 720°.   (1 p.)",
                            "b) Pieraksts 720° : 6.   (1 p.)",
                            "b) Atbilde 120°.   (1 p.)",
                            "c) Perimetrs 6 · 4 = 24 cm.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Riņķa līnija un daudzstūris",
              "vieta": 5.8,
              "teksts": "Regulāra daudzstūra leņķu summa ir 1440°.   "
                        "a) Cik malu ir šim daudzstūrim?   b) Cik liels ir "
                        "viens tā leņķis?   c) Cik liels ir tā ārējais "
                        "leņķis?",
              "kriteriji": ["a) Vienādojums (n − 2) · 180° = 1440°.   "
                            "(1 p.)",
                            "a) Atbilde n = 10.   (1 p.)",
                            "b) Pieraksts 1440° : 10.   (1 p.)",
                            "b) Atbilde 144°.   (1 p.)",
                            "c) Ārējais leņķis 180° − 144° = 36°.   (1 p.)"]},
         ]},
        {"sr": "Lieto pieskares īpašību aprēķinos",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Pieskare", "vieta": 5.0,
              "teksts": "No punkta A, kas atrodas 13 cm attālumā no centra "
                        "O, novilkta pieskare ar pieskaršanās punktu B; "
                        "rādiuss OB = 5 cm.   a) Cik liels ir leņķis OBA?  "
                        " b) Aprēķini nogriežņa AB garumu.   c) Pamato, "
                        "kuru teorēmu lietoji.",
              "kriteriji": ["a) Atbilde 90°.   (1 p.)",
                            "a) Pamatots ar pieskares īpašību.   (1 p.)",
                            "b) Pieraksts AB = √(13² − 5²).   (1 p.)",
                            "b) Atbilde AB = 12 cm.   (1 p.)",
                            "c) Lietota Pitagora teorēma taisnleņķa "
                            "trijstūrī OBA.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Pieskare", "vieta": 5.0,
              "teksts": "No punkta M, kas atrodas 10 cm attālumā no centra "
                        "O, novilkta pieskare ar pieskaršanās punktu N; "
                        "MN = 8 cm.   a) Cik liels ir leņķis ONM?   "
                        "b) Aprēķini rādiusu.   c) Pamato risinājumu.",
              "kriteriji": ["a) Atbilde 90°.   (1 p.)",
                            "a) Pamatots ar pieskares īpašību.   (1 p.)",
                            "b) Pieraksts ON = √(10² − 8²).   (1 p.)",
                            "b) Atbilde ON = 6 cm.   (1 p.)",
                            "c) Lietota Pitagora teorēma taisnleņķa "
                            "trijstūrī ONM.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Pieskare", "vieta": 5.0,
              "teksts": "Riņķa līnijas rādiuss ir 9 cm. No punkta P "
                        "novilkta pieskare, un pieskares nogrieznis ir "
                        "12 cm.   a) Cik liels ir leņķis starp rādiusu un "
                        "pieskari?   b) Aprēķini attālumu no P līdz "
                        "centram.   c) Pamato risinājumu.",
              "kriteriji": ["a) Atbilde 90°.   (1 p.)",
                            "a) Pamatots ar pieskares īpašību.   (1 p.)",
                            "b) Pieraksts OP = √(9² + 12²).   (1 p.)",
                            "b) Atbilde OP = 15 cm.   (1 p.)",
                            "c) Lietota Pitagora teorēma; rādiuss un "
                            "pieskare ir katetes.   (1 p.)"]},
         ]},
        {"sr": "Plāno konstrukciju un pamato spriedumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Ievilkta riņķa līnija",
              "vieta": 4.4,
              "ievads": "Trijstūrī ABC jāievelk riņķa līnija.",
              "jaut": [("Kuras līnijas jākonstruē, lai atrastu centru?", 1),
                       ("Kur centrs atrodas attiecībā pret malām?", 1),
                       ("Kā nosaka ievilktās riņķa līnijas rādiusu?", 2)],
              "atbildes": ["1) Leņķu bisektrises.   (1 p.)",
                           "2) Vienādā attālumā no visām malām.   (1 p.)",
                           "3) No centra velk perpendikulu pret malu; tā "
                           "garums ir rādiuss.   (2 p.)"]},
             {"tips": "jautajumi", "virs": "Apvilkta riņķa līnija",
              "vieta": 4.4,
              "ievads": "Ap trijstūri ABC jāapvelk riņķa līnija.",
              "jaut": [("Kuras līnijas jākonstruē, lai atrastu centru?", 1),
                       ("Kur centrs atrodas attiecībā pret virsotnēm?", 1),
                       ("Kur centrs atrodas, ja trijstūris ir taisnleņķa? "
                        "Pamato!", 2)],
              "atbildes": ["1) Malu vidusperpendikuli.   (1 p.)",
                           "2) Vienādā attālumā no visām virsotnēm.   "
                           "(1 p.)",
                           "3) Hipotenūzas viduspunktā, jo tas ir vienādā "
                           "attālumā no visām trim virsotnēm.   (2 p.)"]},
             {"tips": "jautajumi", "virs": "Regulārs daudzstūris",
              "vieta": 4.4,
              "ievads": "Dots regulārs daudzstūris, kura viens leņķis ir "
                        "140°.",
              "jaut": [("Uzraksti vienādojumu malu skaita noteikšanai!", 2),
                       ("Cik malu ir šim daudzstūrim?", 1),
                       ("Cik liela ir tā leņķu summa?", 1)],
              "atbildes": ["1) {(n − 2) · 180°|n} = 140°.   (2 p.)",
                           "2) n = 9.   (1 p.)",
                           "3) Leņķu summa 1260°.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
