# -*- coding: utf-8 -*-
"""Matemātika, 9. klase. 9.2. Kas kopīgs četrstūriem, kuriem tieši divas
malas ir paralēlas?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 9. klase, 9.2. temats): trapece, tās
pamati, sānu malas un augstums, vienādsānu un taisnleņķa trapece, trapeces
viduslīnija, laukuma formula, palīglīnijas nezināmo lielumu noteikšanai un
taisna prizma, kuras pamatā ir trapece.
"""

PRIEKSMETS = "Matemātika  |  9. klase"
TEMATS = "9.2."
NOSAUKUMS = "Kas kopīgs četrstūriem, kuriem tieši divas malas ir paralēlas?"

ATGADNE = [
    "Trapece ir četrstūris, kuram tieši divas malas ir paralēlas — pamati "
    "a un b; abas pārējās ir sānu malas.",
    "Viduslīnija savieno sānu malu viduspunktus:   m = {a + b|2}      ·      "
    "laukums   S = {a + b|2} · h = m · h",
    "Vienādsānu trapecei sānu malas un pamata pieleņķi ir vienādi   ·   "
    "sānu malas pieleņķu summa ir 180°",
]

FD = {
    "veids": "fd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 9.2. temata beigās. Pārbauda trapeces "
                "definīciju un elementus, trapeces veidus, leņķu īpašības, "
                "viduslīniju, laukuma formulu un aprēķinus ar palīglīnijām.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina trapeces definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir trapece?",
              ["četrstūris ar tieši divām paralēlām malām",
               "četrstūris ar vienādām malām", "trijstūris",
               "regulārs daudzstūris"], 0),
             ("Vai paralelograms ir trapece?",
              ["nē, tam paralēli ir abi malu pāri", "jā", "tikai taisnstūris",
               "nevar noteikt"], 0),
             ("Cik malu ir trapecei?", ["3", "4", "5", "6"], 1),
         ]},
        {"sr": "Nosauc trapeces elementus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc trapeces paralēlās malas?",
              ["pamati", "sānu malas", "diagonāles", "augstumi"], 0),
             ("Kā sauc trapeces neparalēlās malas?",
              ["sānu malas", "pamati", "viduslīnijas", "bisektrises"], 0),
             ("Kas ir trapeces augstums?",
              ["attālums starp pamatiem", "sānu malas garums", "diagonāle",
               "viduslīnija"], 0),
         ]},
        {"sr": "Atšķir trapeces veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāda ir vienādsānu trapece?",
              ["sānu malas ir vienāda garuma", "pamati ir vienādi",
               "viens leņķis ir taisns", "visas malas ir vienādas"], 0),
             ("Kāda ir taisnleņķa trapece?",
              ["sānu mala ir perpendikulāra pamatiem", "visi leņķi ir taisni",
               "sānu malas ir vienādas", "pamati ir vienādi"], 0),
             ("Cik taisnu leņķu ir taisnleņķa trapecei?",
              ["1", "2", "3", "4"], 1),
         ]},
        {"sr": "Zina vienādsānu trapeces īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādi ir vienādsānu trapeces pamata pieleņķi?",
              ["vienādi", "taisni", "izstiepti", "dažādi"], 0),
             ("Kādas ir vienādsānu trapeces diagonāles?",
              ["vienāda garuma", "perpendikulāras", "paralēlas",
               "dažāda garuma"], 0),
             ("Vienādsānu trapecē pamata pieleņķis ir 65°. Cik liels ir "
              "otrs?", ["65°", "115°", "25°", "90°"], 0),
         ]},
        {"sr": "Lieto trapeces leņķu īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir sānu malas pieleņķu summa?",
              ["180°", "90°", "360°", "270°"], 0),
             ("Trapeces leņķis ir 70°. Cik liels ir tā pieleņķis?",
              ["110°", "70°", "20°", "290°"], 0),
             ("Cik liela ir visu trapeces leņķu summa?",
              ["360°", "180°", "540°", "720°"], 0),
         ]},
        {"sr": "Zina trapeces viduslīniju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir trapeces viduslīnija?",
              ["sānu malu viduspunktu savienojums",
               "pamatu viduspunktu savienojums", "diagonāle", "augstums"], 0),
             ("Kā viduslīnija novietota pret pamatiem?",
              ["paralēli", "perpendikulāri", "šķērsām", "sakrīt ar tiem"], 0),
             ("Ar kuru formulu aprēķina viduslīniju?",
              ["m = {a + b|2}", "m = a + b", "m = {a · b|2}", "m = a − b"], 0),
         ]},
        {"sr": "Aprēķina viduslīniju un pamatus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pamati ir 8 cm un 12 cm. Cik gara ir viduslīnija?",
              ["10 cm", "20 cm", "4 cm", "48 cm"], 0),
             ("Viduslīnija ir 9 cm, viens pamats — 6 cm. Cik garš ir otrs?",
              ["12 cm", "3 cm", "15 cm", "9 cm"], 0),
             ("Pamati ir 5 cm un 11 cm. Cik gara ir viduslīnija?",
              ["8 cm", "6 cm", "16 cm", "55 cm"], 0),
         ]},
        {"sr": "Zina trapeces laukuma formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina trapeces laukumu?",
              ["S = {a + b|2} · h", "S = a · h", "S = {a · h|2}",
               "S = a + b + h"], 0),
             ("Kā laukumu izsaka ar viduslīniju m?",
              ["S = m · h", "S = {m|h}", "S = m + h", "S = 2mh"], 0),
             ("Kurš lielums laukuma formulā ir h?",
              ["augstums", "sānu mala", "diagonāle", "perimetrs"], 0),
         ]},
        {"sr": "Aprēķina trapeces laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pamati 6 cm un 10 cm, augstums 4 cm. Cik liels ir laukums?",
              ["32 cm²", "64 cm²", "16 cm²", "40 cm²"], 0),
             ("Viduslīnija 7 cm, augstums 5 cm. Cik liels ir laukums?",
              ["35 cm²", "12 cm²", "70 cm²", "17,5 cm²"], 0),
             ("Laukums 40 cm², viduslīnija 8 cm. Cik liels ir augstums?",
              ["5 cm", "32 cm", "320 cm", "48 cm"], 0),
         ]},
        {"sr": "Aprēķina trapeces perimetru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina trapeces perimetru?",
              ["saskaita visas četras malas", "saskaita pamatus",
               "sareizina malas", "saskaita pamatus un augstumu"], 0),
             ("Vienādsānu trapecei pamati 6 cm un 10 cm, sānu mala 5 cm. "
              "Cik liels ir perimetrs?", ["26 cm", "21 cm", "31 cm", "16 cm"],
              0),
             ("Perimetrs 30 cm, pamati 7 cm un 11 cm. Cik gara ir sānu mala "
              "vienādsānu trapecē?", ["6 cm", "12 cm", "5 cm", "9 cm"], 0),
         ]},
        {"sr": "Lieto palīglīnijas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko iegūst, vienādsānu trapecē novelkot abus augstumus?",
              ["taisnstūri un divus vienādus trijstūrus", "divus kvadrātus",
               "paralelogramu", "riņķi"], 0),
             ("Kāpēc trapecē velk palīglīnijas?",
              ["lai iegūtu pazīstamas figūras", "lai zīmējums būtu skaistāks",
               "lai palielinātu laukumu", "tas nav vajadzīgs"], 0),
             ("Vienādsānu trapecei pamati 12 cm un 6 cm. Cik garš ir "
              "trijstūra katete uz pamata?", ["3 cm", "6 cm", "9 cm",
                                              "18 cm"], 0),
         ]},
        {"sr": "Lieto trapeci praktiskā kontekstā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā aprēķina prizmas tilpumu, ja pamats ir trapece?",
              ["V = S · h", "V = S + h", "V = {S|h}", "V = 2S"], 0),
             ("Dobe ir trapeces formā. Ko aprēķina ar laukuma formulu?",
              ["dobes platību", "dobes perimetru", "žoga garumu",
               "augsnes svaru"], 0),
             ("Prizmas pamata laukums 20 cm², augstums 5 cm. Cik liels ir "
              "tilpums?", ["100 cm³", "25 cm³", "4 cm³", "200 cm³"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 25 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 9.2. temata noslēgumā. "
                "Pārbauda trapeces elementus un veidus, leņķu īpašības, "
                "viduslīnijas un laukuma formulu, kā arī nezināmo lielumu "
                "aprēķināšanu ar palīglīnijām un Pitagora teorēmu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 25 "
              "punktus. Risinājumu pieraksti tam atvēlētajā vietā; "
              "atļauts kalkulators.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina trapeces definīciju un elementus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir trapece?",
              ["četrstūris ar tieši divām paralēlām malām",
               "četrstūris ar vienādām malām", "paralelograms", "rombs"], 0),
             ("Kā sauc trapeces paralēlās malas?",
              ["pamati", "sānu malas", "diagonāles", "viduslīnijas"], 0),
             ("Kas ir trapeces augstums?",
              ["attālums starp pamatiem", "sānu mala", "diagonāle",
               "perimetra puse"], 0),
         ]},
        {"sr": "Atšķir trapeces veidus un to īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir vienādsānu trapeces sānu malas?",
              ["vienāda garuma", "perpendikulāras", "paralēlas",
               "dažāda garuma"], 0),
             ("Cik taisnu leņķu ir taisnleņķa trapecei?",
              ["2", "1", "3", "4"], 0),
             ("Kādas ir vienādsānu trapeces diagonāles?",
              ["vienādas", "perpendikulāras", "paralēlas", "dažādas"], 0),
         ]},
        {"sr": "Lieto trapeces leņķu īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir sānu malas pieleņķu summa?",
              ["180°", "90°", "360°", "270°"], 0),
             ("Trapeces leņķis ir 55°. Cik liels ir tā pieleņķis?",
              ["125°", "55°", "35°", "305°"], 0),
             ("Vienādsānu trapecē pamata pieleņķis ir 72°. Cik liels ir "
              "leņķis pie otra pamata?", ["108°", "72°", "18°", "90°"], 0),
         ]},
        {"sr": "Lieto viduslīnijas īpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pamati ir 7 cm un 13 cm. Cik gara ir viduslīnija?",
              ["10 cm", "20 cm", "6 cm", "91 cm"], 0),
             ("Viduslīnija ir 12 cm, viens pamats — 9 cm. Cik garš ir otrs?",
              ["15 cm", "3 cm", "21 cm", "6 cm"], 0),
             ("Ar kuru formulu aprēķina viduslīniju?",
              ["m = {a + b|2}", "m = a − b", "m = {a|b}", "m = 2(a + b)"], 0),
         ]},
        {"sr": "Aprēķina trapeces laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pamati 5 cm un 9 cm, augstums 6 cm. Cik liels ir laukums?",
              ["42 cm²", "84 cm²", "21 cm²", "270 cm²"], 0),
             ("Viduslīnija 10 cm, augstums 4 cm. Cik liels ir laukums?",
              ["40 cm²", "20 cm²", "14 cm²", "80 cm²"], 0),
             ("Laukums 36 cm², augstums 4 cm. Cik gara ir viduslīnija?",
              ["9 cm", "18 cm", "32 cm", "144 cm"], 0),
         ]},
        {"sr": "Lieto palīglīnijas un prizmas tilpumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienādsānu trapecei pamati 14 cm un 8 cm. Cik garš ir "
              "trijstūra katete uz pamata?", ["3 cm", "6 cm", "11 cm",
                                              "22 cm"], 0),
             ("Ko iegūst, novelkot abus augstumus?",
              ["taisnstūri un divus trijstūrus", "divus kvadrātus",
               "rombu", "riņķi"], 0),
             ("Prizmas pamata laukums 30 cm², augstums 6 cm. Cik liels ir "
              "tilpums?", ["180 cm³", "36 cm³", "5 cm³", "90 cm³"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina trapeces viduslīniju, laukumu un leņķus",
         "stunda": TEMATS, "punkti": 5, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Pamati 6 cm un 14 cm; viduslīnija ir …… cm", "10"),
                         ("Viduslīnija 9 cm, augstums 4 cm; S = …… cm²",
                          "36"),
                         ("Pamats 8 cm, viduslīnija 11 cm; otrs pamats ir "
                          "…… cm", "14"),
                         ("Trapeces leņķis 80°; tā pieleņķis ir ……°", "100"),
                         ("Vienādsānu trapecei pamati 10 cm un 4 cm; "
                          "trijstūra katete ir …… cm", "3")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Pamati 5 cm un 15 cm; viduslīnija ir …… cm", "10"),
                         ("Viduslīnija 7 cm, augstums 6 cm; S = …… cm²",
                          "42"),
                         ("Pamats 12 cm, viduslīnija 9 cm; otrs pamats ir "
                          "…… cm", "6"),
                         ("Trapeces leņķis 115°; tā pieleņķis ir ……°", "65"),
                         ("Vienādsānu trapecei pamati 20 cm un 12 cm; "
                          "trijstūra katete ir …… cm", "4")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Pamati 9 cm un 13 cm; viduslīnija ir …… cm", "11"),
                         ("Viduslīnija 12 cm, augstums 5 cm; S = …… cm²",
                          "60"),
                         ("Pamats 4 cm, viduslīnija 7,5 cm; otrs pamats ir "
                          "…… cm", "11"),
                         ("Trapeces leņķis 47°; tā pieleņķis ir ……°", "133"),
                         ("Vienādsānu trapecei pamati 18 cm un 8 cm; "
                          "trijstūra katete ir …… cm", "5")]},
         ]},
        {"sr": "Aprēķina trapeces augstumu un laukumu ar Pitagora teorēmu",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Augstums un laukums", "vieta": 5.8,
              "teksts": "Vienādsānu trapeces pamati ir 10 cm un 4 cm, bet "
                        "sānu mala — 5 cm. Aprēķini trapeces augstumu un "
                        "laukumu!",
              "kriteriji": [
                  "Novilkti augstumi; iegūts taisnleņķa trijstūris.   (1 p.)",
                  "Noteikta katete (10 − 4) : 2 = 3 cm.   (1 p.)",
                  "Lietota Pitagora teorēma h = √(5² − 3²).   (1 p.)",
                  "Atbilde h = 4 cm.   (1 p.)",
                  "Laukums S = {10 + 4|2} · 4 = 28 cm².   (1 p.)"]},
             {"tips": "aprekins", "virs": "Augstums un laukums", "vieta": 5.8,
              "teksts": "Vienādsānu trapeces pamati ir 16 cm un 8 cm, bet "
                        "sānu mala — 5 cm. Aprēķini trapeces augstumu un "
                        "laukumu!",
              "kriteriji": [
                  "Novilkti augstumi; iegūts taisnleņķa trijstūris.   (1 p.)",
                  "Noteikta katete (16 − 8) : 2 = 4 cm.   (1 p.)",
                  "Lietota Pitagora teorēma h = √(5² − 4²).   (1 p.)",
                  "Atbilde h = 3 cm.   (1 p.)",
                  "Laukums S = {16 + 8|2} · 3 = 36 cm².   (1 p.)"]},
             {"tips": "aprekins", "virs": "Augstums un laukums", "vieta": 5.8,
              "teksts": "Taisnleņķa trapeces pamati ir 9 cm un 4 cm, bet "
                        "garākā sānu mala — 13 cm. Aprēķini trapeces "
                        "augstumu un laukumu!",
              "kriteriji": [
                  "Novilkts augstums; iegūts taisnleņķa trijstūris.   (1 p.)",
                  "Noteikta katete 9 − 4 = 5 cm.   (1 p.)",
                  "Lietota Pitagora teorēma h = √(13² − 5²).   (1 p.)",
                  "Atbilde h = 12 cm.   (1 p.)",
                  "Laukums S = {9 + 4|2} · 12 = 78 cm².   (1 p.)"]},
         ]},
        {"sr": "Risina praktiska satura uzdevumu par trapeci",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Trapece praksē", "vieta": 5.0,
              "teksts": "Dārza dobe ir trapeces formā: pamati 6 m un 10 m, "
                        "augstums 3 m. Cik liels ir dobes laukums un cik "
                        "maisu mēslojuma vajag, ja vienu maisu izlieto "
                        "6 m²?",
              "kriteriji": [
                  "Lietota laukuma formula S = {a + b|2} · h.   (1 p.)",
                  "Ievietotas vērtības S = {6 + 10|2} · 3.   (1 p.)",
                  "Aprēķināts S = 24 m².   (1 p.)",
                  "Aprēķins 24 : 6 = 4.   (1 p.)",
                  "Atbilde: 24 m² un 4 maisi.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Trapece praksē", "vieta": 5.0,
              "teksts": "Grāvja šķērsgriezums ir trapece: augšas platums "
                        "2,4 m, apakšas platums 1,2 m, dziļums 0,8 m. "
                        "Aprēķini šķērsgriezuma laukumu un grāvja tilpumu, "
                        "ja tā garums ir 50 m!",
              "kriteriji": [
                  "Lietota laukuma formula S = {a + b|2} · h.   (1 p.)",
                  "Ievietotas vērtības S = {2,4 + 1,2|2} · 0,8.   (1 p.)",
                  "Aprēķināts S = 1,44 m².   (1 p.)",
                  "Tilpums V = S · 50.   (1 p.)",
                  "Atbilde: V = 72 m³.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Trapece praksē", "vieta": 5.0,
              "teksts": "Jumta gala siena ir vienādsānu trapece: pamati "
                        "8 m un 5 m, augstums 2 m. Aprēķini sienas laukumu "
                        "un krāsas daudzumu, ja 1 litru izlieto 4 m²!",
              "kriteriji": [
                  "Lietota laukuma formula S = {a + b|2} · h.   (1 p.)",
                  "Ievietotas vērtības S = {8 + 5|2} · 2.   (1 p.)",
                  "Aprēķināts S = 13 m².   (1 p.)",
                  "Aprēķins 13 : 4 = 3,25.   (1 p.)",
                  "Atbilde: 13 m² un 3,25 l krāsas.   (1 p.)"]},
         ]},
        {"sr": "Pamato spriedumu par trapeces īpašībām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Vienādsānu trapecē ABCD (BC ∥ AD) leņķis A ir 62°.",
              "jaut": [("Cik liels ir leņķis D?", 1),
                       ("Cik liels ir leņķis B?", 1),
                       ("Pamato, kāpēc leņķi A un B kopā ir 180°!", 2)],
              "atbildes": ["1) ∠D = 62° — vienādsānu trapeces pamata "
                           "pieleņķi ir vienādi.   (1 p.)",
                           "2) ∠B = 180° − 62° = 118°.   (1 p.)",
                           "3) BC ∥ AD, un AB ir šķēlēja; iekšējie "
                           "vienpusleņķi kopā ir 180°.   (2 p.)"]},
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Trapecē ABCD (BC ∥ AD) novilktas diagonāles, kas "
                        "krustojas punktā O. BC = 6 cm un AD = 15 cm.",
              "jaut": [("Kuri divi trijstūri ir līdzīgi?", 1),
                       ("Ar kuru pazīmi to pamato?", 1),
                       ("Cik liels ir līdzības koeficients?", 2)],
              "atbildes": ["1) △BOC ∼ △DOA.   (1 p.)",
                           "2) Pēc divu leņķu vienādības — šķērsleņķi pie "
                           "paralēlām malām un krustleņķi.   (1 p.)",
                           "3) k = 15 : 6 = 2,5.   (2 p.)"]},
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Trapeces pamati ir 12 cm un 6 cm, bet viduslīnija "
                        "dala trapeci divās mazākās trapecēs ar vienādu "
                        "augstumu.",
              "jaut": [("Cik gara ir viduslīnija?", 1),
                       ("Kādi ir abu mazāko trapeču pamati?", 1),
                       ("Kurai no tām ir lielāks laukums? Pamato!", 2)],
              "atbildes": ["1) m = {12 + 6|2} = 9 cm.   (1 p.)",
                           "2) Augšējai 6 cm un 9 cm; apakšējai 9 cm un "
                           "12 cm.   (1 p.)",
                           "3) Apakšējai — augstumi ir vienādi, bet tās "
                           "viduslīnija ir garāka.   (2 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
