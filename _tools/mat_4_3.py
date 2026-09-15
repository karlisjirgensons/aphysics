# -*- coding: utf-8 -*-
"""Matemātika, 4. klase. 4.3. Kā mēra leņķi?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 4. klase, 4.3. temats): stars un leņķis,
leņķa virsotne un malas, leņķa lieluma mērīšana grādos ar transportieri,
taisns leņķis 90°, šaurs un plats leņķis, paralēlas un perpendikulāras
taisnas līnijas, taisnstūra malu savstarpējais novietojums.
"""

PRIEKSMETS = "Matemātika  |  4. klase"
TEMATS = "4.3."
NOSAUKUMS = "Kā mēra leņķi?"

ATGADNE = [
    "Leņķi veido divi stari ar kopīgu sākumpunktu — leņķa virsotni; stari "
    "ir leņķa malas.",
    "Taisns leņķis ir 90°   ·   šaurs leņķis < 90°   ·   plats leņķis > 90°  "
    " ·   izstiepts leņķis 180°",
    "Paralēlas līnijas nekad nekrustojas; perpendikulāras krustojas taisnā "
    "leņķī.",
]

FD = {
    "veids": "fd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 4.3. temata beigās. Pārbauda stara un "
                "leņķa jēdzienu, leņķa elementus, leņķa mērīšanu grādos, "
                "leņķu veidus, paralēlas un perpendikulāras līnijas un "
                "daudzstūru malu novietojumu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, kas ir stars",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir stars?",
              ["līnija, kurai ir sākums, bet nav gala", "nogrieznis",
               "līkne", "punkts"], 0),
             ("Kāpēc staram nevar izmērīt garumu?",
              ["to vienmēr var turpināt", "tas ir līkums", "tas ir punkts",
               "tam nav sākuma"], 0),
             ("Ar ko stars atšķiras no nogriežņa?",
              ["nogrieznim ir divi gali", "stars ir īsāks", "stars ir līkne",
               "tie neatšķiras"], 0),
         ]},
        {"sr": "Zina, kas ir leņķis un tā elementi",
         "stunda": TEMATS,
         "jautajumi": [
             ("No kā veidojas leņķis?",
              ["no diviem stariem ar kopīgu sākumpunktu", "no diviem punktiem",
               "no riņķa", "no trim nogriežņiem"], 0),
             ("Kā sauc leņķa staru kopīgo sākumpunktu?",
              ["virsotne", "mala", "grāds", "pamats"], 0),
             ("Kā sauc leņķa starus?",
              ["malas", "virsotnes", "grādi", "skaldnes"], 0),
         ]},
        {"sr": "Zina leņķa mērvienību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādā mērvienībā mēra leņķa lielumu?",
              ["grādos", "centimetros", "kilogramos", "minūtēs"], 0),
             ("Cik grādu ir taisnam leņķim?", ["45°", "90°", "180°", "360°"],
              1),
             ("Ar ko mēra leņķa lielumu?",
              ["ar transportieri", "ar lineālu", "ar cirkuli", "ar svariem"],
              0),
         ]},
        {"sr": "Nosaka leņķa veidu pēc tā lieluma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Leņķis ir 45°. Kāds tas ir?",
              ["šaurs", "taisns", "plats", "izstiepts"], 0),
             ("Leņķis ir 120°. Kāds tas ir?",
              ["šaurs", "taisns", "plats", "izstiepts"], 2),
             ("Leņķis ir 90°. Kāds tas ir?",
              ["šaurs", "taisns", "plats", "izstiepts"], 1),
         ]},
        {"sr": "Salīdzina leņķus pēc lieluma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš leņķis ir vislielākais?", ["30°", "75°", "100°", "89°"],
              2),
             ("Kurš leņķis ir šaurākais?", ["95°", "60°", "120°", "90°"], 1),
             ("Kura zīme jāliek:  70° …… 100°?", [">", "<", "=", "+"], 1),
         ]},
        {"sr": "Zina, ka leņķa lielums nemainās, malas pagarinot",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas notiek ar leņķi, ja tā malas pagarina?",
              ["leņķa lielums nemainās", "leņķis palielinās",
               "leņķis samazinās", "leņķis pazūd"], 0),
             ("Kāpēc dažreiz leņķa malas jāpagarina?",
              ["lai tās sasniegtu transportiera skalu", "lai leņķis kļūtu "
               "lielāks", "lai zīmējums būtu skaistāks", "tas nav vajadzīgs"],
              0),
             ("Kas mainās, ja vienu leņķa staru pagriež?",
              ["leņķa lielums", "virsotnes vieta", "malu krāsa",
              "nekas"], 0),
         ]},
        {"sr": "Lieto transportieri leņķa mērīšanai",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur uz leņķa liek transportiera centru?",
              ["uz leņķa virsotnes", "uz leņķa malas gala", "blakus leņķim",
               "vienalga kur"], 0),
             ("Ko dara pēc transportiera novietošanas?",
              ["nolasa skaitli, kur iet otra mala", "izmēra malu garumu",
               "saskaita malas", "nokrāso leņķi"], 0),
             ("Kāds leņķis ir mazāks nekā 180°, bet lielāks nekā 90°?",
              ["plats", "šaurs", "taisns", "nav tāda"], 0),
         ]},
        {"sr": "Zina, kas ir paralēlas līnijas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir paralēlas līnijas?",
              ["tās nekad nekrustojas", "tās krustojas taisnā leņķī",
               "tās krustojas šaurā leņķī", "tās ir līkumainas"], 0),
             ("Kuras taisnstūra malas ir paralēlas?",
              ["pretējās", "blakus esošās", "visas", "neviena"], 0),
             ("Ar ko pārbauda, vai līnijas ir paralēlas?",
              ["ar diviem lineāliem", "ar transportieri", "ar svariem",
               "ar cirkuli"], 0),
         ]},
        {"sr": "Zina, kas ir perpendikulāras līnijas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir perpendikulāras līnijas?",
              ["tās krustojas taisnā leņķī", "tās nekad nekrustojas",
               "tās krustojas platā leņķī", "tās ir vienāda garuma"], 0),
             ("Kuras taisnstūra malas ir perpendikulāras?",
              ["blakus esošās", "pretējās", "neviena", "visas"], 0),
             ("Cik grādu ir leņķis starp perpendikulārām līnijām?",
              ["45°", "90°", "180°", "360°"], 1),
         ]},
        {"sr": "Raksturo daudzstūra malu novietojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik taisnu leņķu ir taisnstūrim?", ["2", "3", "4", "0"], 2),
             ("Kāds apgalvojums par kvadrātu ir pareizs?",
              ["pretējās malas paralēlas, blakus malas perpendikulāras",
               "visas malas paralēlas", "nevienas malas nav paralēlas",
               "tam nav taisnu leņķu"], 0),
             ("Kāpēc malu paralēlumu vajag pārbaudīt, nevis noteikt pēc "
              "acs?",
              ["zīmējums var maldināt", "tā ir ātrāk", "tā ir skaistāk",
               "nav jāpārbauda"], 0),
         ]},
        {"sr": "Zīmē leņķus un līnijas rūtiņu lapā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā rūtiņu lapā viegli uzzīmēt taisnu leņķi?",
              ["pa rūtiņu līnijām", "ar brīvu roku", "ar cirkuli",
               "ar dzēšgumiju"], 0),
             ("Kādas savā starpā ir rūtiņu lapas horizontālās līnijas?",
              ["paralēlas", "perpendikulāras", "šķērsas", "līkas"], 0),
             ("Kādas savā starpā ir rūtiņu lapas horizontālā un vertikālā "
              "līnija?",
              ["perpendikulāras", "paralēlas", "vienādas", "šķības"], 0),
         ]},
        {"sr": "Aprēķina leņķu lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisns leņķis sadalīts divos vienādos leņķos. Cik liels ir "
              "katrs?",
              ["30°", "45°", "60°", "90°"], 1),
             ("Viens leņķis ir 35°, otrs par 25° lielāks. Cik liels ir "
              "otrs?",
              ["50°", "60°", "70°", "85°"], 1),
             ("Izstiepts leņķis ir 180°. Cik liels ir tā puse?",
              ["45°", "90°", "120°", "360°"], 1),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 4,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 4.3. temata noslēgumā. "
                "Pārbauda leņķa jēdzienu un elementus, leņķa mērīšanu un "
                "zīmēšanu ar transportieri, leņķu veidus, paralēlas un "
                "perpendikulāras līnijas un daudzstūra raksturošanu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Zīmē ar lineālu un transportieri tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina leņķa jēdzienu un elementus",
         "stunda": TEMATS,
         "jautajumi": [
             ("No kā veidojas leņķis?",
              ["no diviem stariem ar kopīgu sākumpunktu", "no diviem punktiem",
               "no riņķa", "no trim nogriežņiem"], 0),
             ("Kā sauc staru kopīgo sākumpunktu?",
              ["virsotne", "mala", "grāds", "centrs"], 0),
             ("Kas ir stars?",
              ["līnija ar sākumu, bet bez gala", "nogrieznis", "punkts",
               "līkne"], 0),
         ]},
        {"sr": "Zina leņķa mērvienību un veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik grādu ir taisnam leņķim?",
              ["45°", "90°", "180°", "360°"], 1),
             ("Leņķis 130° ir …", ["plats", "šaurs", "taisns", "izstiepts"],
              0),
             ("Leņķis 55° ir …", ["šaurs", "taisns", "plats", "izstiepts"],
              0),
         ]},
        {"sr": "Mēra leņķi ar transportieri",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur liek transportiera centru?",
              ["uz leņķa virsotnes", "uz malas gala", "blakus leņķim",
               "vienalga kur"], 0),
             ("Ko dara, ja leņķa mala ir pārāk īsa?",
              ["to pagarina", "leņķi nemēra", "leņķi nokrāso",
               "maina virsotni"], 0),
             ("Vai leņķa lielums mainās, ja malas pagarina?",
              ["nē", "jā", "tikai šauram", "tikai platam"], 0),
         ]},
        {"sr": "Zina paralēlas un perpendikulāras līnijas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Paralēlas līnijas …",
              ["nekad nekrustojas", "krustojas taisnā leņķī",
               "krustojas šaurā leņķī", "vienmēr ir īsas"], 0),
             ("Perpendikulāras līnijas krustojas leņķī …",
              ["90°", "45°", "180°", "60°"], 0),
             ("Kuras taisnstūra malas ir paralēlas?",
              ["pretējās", "blakus esošās", "visas", "neviena"], 0),
         ]},
        {"sr": "Raksturo daudzstūri",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik taisnu leņķu ir taisnstūrim?", ["2", "3", "4", "0"], 2),
             ("Kvadrāta blakus malas ir …",
              ["perpendikulāras", "paralēlas", "vienādas garumā un "
               "paralēlas", "šķības"], 0),
             ("Kāpēc paralēlumu jāpārbauda?",
              ["zīmējums var maldināt", "tā ir ātrāk", "tā ir skaistāk",
               "nav jāpārbauda"], 0),
         ]},
        {"sr": "Aprēķina leņķu lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisns leņķis sadalīts divos vienādos. Cik liels ir katrs?",
              ["30°", "45°", "60°", "90°"], 1),
             ("Viens leņķis 40°, otrs par 30° lielāks. Cik liels ir otrs?",
              ["60°", "70°", "80°", "90°"], 1),
             ("Cik liela ir izstiepta leņķa puse?",
              ["45°", "90°", "120°", "180°"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Nosaka leņķu veidus un lielumus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Uzraksti leņķa veidu vai lielumu",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Leņķis 35° ir ……", "šaurs"),
                         ("Leņķis 110° ir ……", "plats"),
                         ("Taisns leņķis ir …… grādi", "90"),
                         ("Taisna leņķa puse ir …… grādi", "45")]},
             {"tips": "parveide", "virs": "Uzraksti leņķa veidu vai lielumu",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Leņķis 75° ir ……", "šaurs"),
                         ("Leņķis 145° ir ……", "plats"),
                         ("Izstiepts leņķis ir …… grādi", "180"),
                         ("Leņķis 90° ir ……", "taisns")]},
             {"tips": "parveide", "virs": "Uzraksti leņķa veidu vai lielumu",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Leņķis 20° ir ……", "šaurs"),
                         ("Leņķis 95° ir ……", "plats"),
                         ("Kvadrāta leņķis ir …… grādi", "90"),
                         ("Divi taisni leņķi kopā ir …… grādi", "180")]},
         ]},
        {"sr": "Raksturo līniju savstarpējo novietojumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti «paralēlas» vai "
                                          "«perpendikulāras»",
              "note": "Ieraksti pareizo vārdu! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūra pretējās malas ir ……", "paralēlas"),
                         ("Taisnstūra blakus malas ir ……", "perpendikulāras"),
                         ("Līnijas, kas nekrustojas, ir ……", "paralēlas")]},
             {"tips": "parveide", "virs": "Ieraksti «paralēlas» vai "
                                          "«perpendikulāras»",
              "note": "Ieraksti pareizo vārdu! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Kvadrāta pretējās malas ir ……", "paralēlas"),
                         ("Līnijas, kas krustojas 90° leņķī, ir ……",
                          "perpendikulāras"),
                         ("Rūtiņu lapas horizontālās līnijas ir ……",
                          "paralēlas")]},
             {"tips": "parveide", "virs": "Ieraksti «paralēlas» vai "
                                          "«perpendikulāras»",
              "note": "Ieraksti pareizo vārdu! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Rūtiņu lapas vertikālā un horizontālā līnija ir "
                          "……", "perpendikulāras"),
                         ("Sliedes ir savā starpā ……", "paralēlas"),
                         ("Kvadrāta blakus malas ir ……",
                          "perpendikulāras")]},
         ]},
        {"sr": "Zīmē leņķus ar transportieri",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Zīmē leņķus", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu un transportieri!",
              "jaut": [("Uzzīmē 60° leņķi!", 1),
                       ("Uzzīmē taisnu leņķi!", 1),
                       ("Uzraksti, kāds ir pirmais leņķis (šaurs, taisns vai "
                        "plats)!", 1),
                       ("Uzzīmē platu leņķi un pieraksti tā lielumu!", 1)],
              "atbildes": ["1) Uzzīmēts 60° leņķis (pieļaujama kļūda ±2°).   "
                           "(1 p.)",
                           "2) Uzzīmēts 90° leņķis.   (1 p.)",
                           "3) Atbilde: šaurs.   (1 p.)",
                           "4) Uzzīmēts leņķis, kas lielāks nekā 90°, ar "
                           "pierakstītu lielumu.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē leņķus", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu un transportieri!",
              "jaut": [("Uzzīmē 120° leņķi!", 1),
                       ("Uzzīmē 45° leņķi!", 1),
                       ("Uzraksti, kāds ir pirmais leņķis!", 1),
                       ("Uzzīmē taisnu leņķi un apzīmē tā virsotni!", 1)],
              "atbildes": ["1) Uzzīmēts 120° leņķis (±2°).   (1 p.)",
                           "2) Uzzīmēts 45° leņķis.   (1 p.)",
                           "3) Atbilde: plats.   (1 p.)",
                           "4) Uzzīmēts 90° leņķis ar apzīmētu virsotni.   "
                           "(1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē leņķus", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu un transportieri!",
              "jaut": [("Uzzīmē 30° leņķi!", 1),
                       ("Uzzīmē 150° leņķi!", 1),
                       ("Uzraksti, kurš no tiem ir šaurs!", 1),
                       ("Uzzīmē divas perpendikulāras līnijas!", 1)],
              "atbildes": ["1) Uzzīmēts 30° leņķis (±2°).   (1 p.)",
                           "2) Uzzīmēts 150° leņķis.   (1 p.)",
                           "3) Atbilde: 30° leņķis.   (1 p.)",
                           "4) Uzzīmētas divas līnijas, kas krustojas 90° "
                           "leņķī.   (1 p.)"]},
         ]},
        {"sr": "Raksturo daudzstūra malas un leņķus",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Daudzstūra raksturošana",
              "vieta": 5.5,
              "ievads": "Zīmē rūtiņās taisnstūri ar malām 5 un 3 rūtiņas.",
              "jaut": [("Uzzīmē to!", 1),
                       ("Apvelc divas paralēlas malas!", 1),
                       ("Uzraksti, cik taisnu leņķu ir šai figūrai!", 1)],
              "atbildes": ["1) Uzzīmēts taisnstūris 5 × 3.   (1 p.)",
                           "2) Apvilktas pretējās malas.   (1 p.)",
                           "3) Atbilde: 4 taisni leņķi.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Daudzstūra raksturošana",
              "vieta": 5.5,
              "ievads": "Zīmē rūtiņās kvadrātu ar malu 4 rūtiņas.",
              "jaut": [("Uzzīmē to!", 1),
                       ("Apvelc divas perpendikulāras malas!", 1),
                       ("Uzraksti, cik grādu ir katrs tā leņķis!", 1)],
              "atbildes": ["1) Uzzīmēts kvadrāts 4 × 4.   (1 p.)",
                           "2) Apvilktas blakus esošas malas.   (1 p.)",
                           "3) Atbilde: 90°.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Daudzstūra raksturošana",
              "vieta": 5.5,
              "ievads": "Zīmē rūtiņās četrstūri, kuram divas malas ir "
                        "paralēlas.",
              "jaut": [("Uzzīmē to!", 1),
                       ("Apvelc paralēlās malas!", 1),
                       ("Uzraksti, vai figūrai ir taisni leņķi!", 1)],
              "atbildes": ["1) Uzzīmēts četrstūris ar divām paralēlām "
                           "malām.   (1 p.)",
                           "2) Apvilktas paralēlās malas.   (1 p.)",
                           "3) Atbilde atbilst zīmējumam.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
