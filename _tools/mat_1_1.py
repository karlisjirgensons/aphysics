# -*- coding: utf-8 -*-
"""Matemātika, 1. klase. 1.1. Kā izstāsta un parāda: cik, kur, kāds?

Saturs abiem temata darbiem - formatīvajam darbam (viena lapa, 12 jautājumi
ar atbildēm A-D) un summatīvajam pārbaudes darbam (divas lapas, tests un
četri uzdevumi ar darba vietu).

Sasniedzamie rezultāti un jēdzieni ņemti no oficiālās programmas
(PD_generate/mat_p.pdf, 1. klase, 1.1. temats): skaits un skaitīšana līdz 10,
kārtas skaitļa vārdi, skaita un skaitļu salīdzināšana, garumu salīdzināšana
bez mērīšanas, daudzstūri un to pazīmes, objektu novietojums un virzieni,
ritmiskas virknes, nedēļas dienas.

Pirmklasniekam teksts ir īss, un skaitu rāda ar figūru rindu (● ▲ ■ ◆ ○ □ △),
nevis ar vārdiem - tā uzdevumu var izlasīt arī skolēns, kurš vēl lasa lēni.

Katrā grupā ir četri līdzvērtīgi jautājumi, tāpēc trijos variantos katrai
grupai sanāk cits jautājums (sk. mat_common.py).
"""

PRIEKSMETS = "Matemātika  |  1. klase"
TEMATS = "1.1."
NOSAUKUMS = "Kā izstāsta un parāda: cik, kur, kāds?"

# ------------------------------------------------------ formatīvais darbs
FD = {
    "veids": "fd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 1.1. temata beigās. Pārbauda skaitīšanu "
                "līdz 10, kārtas skaitļa vārdus, skaita un skaitļu "
                "salīdzināšanu, garumu salīdzināšanu bez mērīšanas, "
                "daudzstūru pazīmes, novietojumu un virzienus, ritmiskas "
                "virknes un nedēļas dienas.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": [
        "Skaitļi:  1  2  3  4  5  6  7  8  9  10        Zīmes:  >  lielāks "
        "nekā   ·   <  mazāks nekā   ·   =  vienāds ar",
        "Trijstūrim 3 malas   ·   četrstūrim 4 malas   ·   piecstūrim "
        "5 malas        Nedēļā ir 7 dienas.",
    ],
    "grupas": [
        # --------------------------------------------------- 1. cik ir kopā
        {"sr": "Nosaka objektu skaitu, skaitot līdz 10",
         "stunda": "1.1.",
         "jautajumi": [
             ("Cik ir ● ● ● ● ● ● ●?", ["5", "6", "7", "8"], 2),
             ("Cik ir ▲ ▲ ▲ ▲?", ["3", "4", "5", "6"], 1),
             ("Cik ir ■ ■ ■ ■ ■ ■ ■ ■ ■?", ["7", "8", "9", "10"], 2),
             ("Cik ir ◆ ◆ ◆ ◆ ◆ ◆?", ["4", "5", "6", "7"], 2),
         ]},
        # ----------------------------------------- 2. skaitļu rinda 10 apjomā
        {"sr": "Skaita uz priekšu un atpakaļ, nosaka nākamo un iepriekšējo "
               "skaitli",
         "stunda": "1.1.",
         "jautajumi": [
             ("Kurš skaitlis ir tūlīt pēc 7?", ["5", "6", "8", "9"], 2),
             ("Kurš skaitlis ir tūlīt pirms 5?", ["3", "4", "6", "7"], 1),
             ("Skaiti atpakaļ: 9, 8, 7, … Kurš ir nākamais?",
              ["5", "6", "8", "10"], 1),
             ("Kurš skaitlis ir starp 3 un 5?", ["2", "4", "6", "8"], 1),
         ]},
        # ------------------------------------------------- 3. kārtas skaitļi
        {"sr": "Lieto kārtas skaitļa vārdus un nosaka, kurš objekts ir pēc "
               "kārtas",
         "stunda": "1.1.",
         "jautajumi": [
             ("Rindā:  ● ▲ ■ ◆.  Kurš pēc kārtas ir ■?",
              ["pirmais", "otrais", "trešais", "ceturtais"], 2),
             ("Rindā:  ▲ ● ■ ○ ◆.  Kura figūra ir otrā?",
              ["▲", "●", "■", "◆"], 1),
             ("Rindā stāv 6 bērni. Kurš pēc kārtas ir pēdējais?",
              ["ceturtais", "piektais", "sestais", "septītais"], 2),
             ("Rindā:  □ △ ● ■.  Kura figūra ir ceturtā?",
              ["□", "△", "●", "■"], 3),
         ]},
        # ------------------------------------------------ 4. skaita salīdzin.
        {"sr": "Salīdzina objektu skaitu, lietojot «vairāk», «mazāk», "
               "«tikpat»",
         "stunda": "1.1.",
         "jautajumi": [
             ("Kur ir vairāk:  ● ● ● ●  vai  ▲ ▲ ▲ ▲ ▲ ▲?",
              ["● ● ● ●", "▲ ▲ ▲ ▲ ▲ ▲", "tikpat", "nevar zināt"], 1),
             ("● ● ● ● ●  un  ■ ■ ■ ■ ■.  Ko var teikt?",
              ["ripu ir vairāk", "kvadrātu ir vairāk", "ir tikpat",
               "nevar salīdzināt"], 2),
             ("Kur ir mazāk:  ▲ ▲ ▲ ▲ ▲ ▲ ▲  vai  ◆ ◆ ◆?",
              ["▲ ▲ ▲ ▲ ▲ ▲ ▲", "◆ ◆ ◆", "tikpat", "nevar zināt"], 1),
             ("Klasē ir 8 krēsli un 6 galdi. Kā ir?",
              ["krēslu ir vairāk", "galdu ir vairāk", "ir tikpat",
               "nevar zināt"], 0),
         ]},
        # ----------------------------------------------- 5. zīmes >, <, =
        {"sr": "Salīdzina skaitļus un lieto zīmes «>», «<», «=»",
         "stunda": "1.1.",
         "jautajumi": [
             ("Kura zīme jāliek:  6 … 9?", [">", "<", "=", "+"], 1),
             ("Kura zīme jāliek:  10 … 4?", [">", "<", "=", "−"], 0),
             ("Kura zīme jāliek:  7 … 7?", [">", "<", "=", "+"], 2),
             ("Kurš skaitlis ir lielāks nekā 5?", ["2", "3", "5", "8"], 3),
         ]},
        # --------------------------------------------- 6. garumu salīdzināšana
        {"sr": "Salīdzina garumus bez mērīšanas — uzliekot vienu uz otra",
         "stunda": "1.1.",
         "jautajumi": [
             ("Kā bez lineāla pārbauda, kurš kociņš ir garāks?",
              ["pasver tos", "uzliek vienu uz otra un salīdzina galus",
               "saskaita to krāsas", "salauž tos"], 1),
             ("Divas lentes uzliek vienu uz otras. Sākumi sakrīt, bet viena "
              "beidzas tālāk. Kāda tā ir?",
              ["īsāka", "garāka", "tikpat gara", "platāka"], 1),
             ("Kad divi kociņi ir vienāda garuma?",
              ["kad tiem ir viena krāsa",
               "kad, uzliekot vienu uz otra, abi gali sakrīt",
               "kad tie ir resni", "kad tie ir taisni"], 1),
             ("Zīmulis ir īsāks nekā pildspalva. Ko tas nozīmē?",
              ["zīmulis ir garāks", "zīmulis ir mazāka garuma",
               "tie ir vienādi", "pildspalva ir īsāka"], 1),
         ]},
        # ------------------------------------------------------- 7. daudzstūri
        {"sr": "Nosauc daudzstūri pēc malu un virsotņu skaita",
         "stunda": "1.1.",
         "jautajumi": [
             ("Kā sauc figūru, kurai ir 3 malas?",
              ["trijstūris", "četrstūris", "piecstūris", "riņķis"], 0),
             ("Cik malu ir četrstūrim?", ["2", "3", "4", "5"], 2),
             ("Kā sauc figūru, kurai ir 5 virsotnes?",
              ["trijstūris", "četrstūris", "piecstūris", "sešstūris"], 2),
             ("Cik virsotņu ir trijstūrim?", ["2", "3", "4", "6"], 1),
         ]},
        # ------------------------------------------- 8. figūru pazīmes, grupēš.
        {"sr": "Raksturo, salīdzina un grupē figūras pēc pazīmēm",
         "stunda": "1.1.",
         "jautajumi": [
             ("Kurš vārds der visām figūrām, kurām ir 4 malas?",
              ["trijstūris", "četrstūris", "riņķis", "līnija"], 1),
             ("Kura figūra ir lieka:  trijstūris, četrstūris, piecstūris, "
              "riņķis?",
              ["trijstūris", "četrstūris", "piecstūris", "riņķis"], 3),
             ("Kad divas figūras ir vienādas?",
              ["kad tām ir viena krāsa",
               "kad, uzliekot vienu uz otras, tās sakrīt",
               "kad tās ir lielas", "kad tās zīmētas ar lineālu"], 1),
             ("Pēc kā vēl var sagrupēt figūras?",
              ["pēc krāsas un lieluma", "pēc svara", "pēc garšas",
               "pēc skaņas"], 0),
         ]},
        # ----------------------------------------------------- 9. novietojums
        {"sr": "Apraksta objektu novietojumu ar vārdiem «starp», «virs», "
               "«zem», «pa labi», «pa kreisi»",
         "stunda": "1.1.",
         "jautajumi": [
             ("Rindā:  ● ▲ ■.  Kura figūra ir starp ● un ■?",
              ["●", "▲", "■", "neviena"], 1),
             ("Grāmata ir uz galda. Kur ir galds?",
              ["virs grāmatas", "zem grāmatas", "blakus grāmatai",
               "grāmatā"], 1),
             ("Rindā:  ▲ ● ■.  Kura figūra ir pa labi no ●?",
              ["▲", "●", "■", "neviena"], 2),
             ("Soma ir zem sola. Kur tā atrodas?",
              ["sola virspusē", "sola apakšā", "uz sola", "aiz durvīm"], 1),
         ]},
        # ------------------------------------------------------- 10. virzieni
        {"sr": "Lieto virzienu norādes un izpilda soļu virkni",
         "stunda": "1.1.",
         "jautajumi": [
             ("Ko nozīmē bulta ↑?",
              ["uz augšu", "uz leju", "pa labi", "pa kreisi"], 0),
             ("Kurš solis ir pretējs solim «pa labi»?",
              ["uz augšu", "uz leju", "pa kreisi", "pa labi"], 2),
             ("Ceļš:  → → ↓.  Cik soļu ir kopā?", ["2", "3", "4", "5"], 1),
             ("Ceļš:  ↑ ↑ →.  Uz kuru pusi ir pēdējais solis?",
              ["uz augšu", "uz leju", "pa labi", "pa kreisi"], 2),
         ]},
        # -------------------------------------------------------- 11. virknes
        {"sr": "Turpina ritmisku objektu vai skaitļu virkni",
         "stunda": "1.1.",
         "jautajumi": [
             ("Virkne:  ● ▲ ● ▲ ● …  Kurš ir nākamais?",
              ["●", "▲", "■", "◆"], 1),
             ("Virkne:  1, 2, 1, 2, 1, …  Kurš skaitlis ir nākamais?",
              ["1", "2", "3", "4"], 1),
             ("Virkne:  ■ ■ ● ■ ■ ● …  Kurš ir nākamais?",
              ["●", "■", "▲", "◆"], 1),
             ("Virkne:  2, 4, 6, …  Kurš skaitlis ir nākamais?",
              ["7", "8", "9", "10"], 1),
         ]},
        # -------------------------------------------------- 12. nedēļas dienas
        {"sr": "Nosauc nedēļas dienas un to secību",
         "stunda": "1.1.",
         "jautajumi": [
             ("Cik dienu ir nedēļā?", ["5", "6", "7", "10"], 2),
             ("Kura diena ir pēc otrdienas?",
              ["pirmdiena", "trešdiena", "ceturtdiena", "svētdiena"], 1),
             ("Kura diena ir pirms piektdienas?",
              ["trešdiena", "ceturtdiena", "sestdiena", "svētdiena"], 1),
             ("Šodien ir trešdiena. Kura diena būs rīt?",
              ["otrdiena", "ceturtdiena", "piektdiena", "sestdiena"], 1),
         ]},
    ],
}

# --------------------------------------------------- summatīvais pārbaudes d.
PD = {
    "veids": "pd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 1.1. temata noslēgumā. "
                "Pārbauda skaitīšanu un skaita noteikšanu līdz 10, skaitļu "
                "salīdzināšanu ar zīmēm «>», «<», «=», daudzstūru pazīmes, "
                "objektu novietojumu un virzienus, kā arī prasmi paskaidrot "
                "savu domu ar zīmējumu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Uzdevumu tekstu lasa skolotājs. Atbildi raksti un zīmē tam "
              "atvēlētajā vietā!",
    "atgadne": [
        "Skaitļi:  1  2  3  4  5  6  7  8  9  10",
        "Zīmes:  >  lielāks nekā   ·   <  mazāks nekā   ·   =  vienāds ar",
        "Trijstūris — 3 malas   ·   četrstūris — 4 malas   ·   piecstūris — "
        "5 malas",
    ],
    # 1. uzdevums - tests. Sešas grupas; variantā no katras viens jautājums.
    "tests": [
        {"sr": "Nosaka objektu skaitu līdz 10",
         "stunda": "1.1.",
         "jautajumi": [
             ("Cik ir ● ● ● ● ●?", ["3", "4", "5", "6"], 2),
             ("Cik ir ■ ■ ■ ■ ■ ■ ■ ■?", ["6", "7", "8", "9"], 2),
             ("Cik ir △ △ △?", ["2", "3", "4", "5"], 1),
             ("Cik ir ○ ○ ○ ○ ○ ○ ○ ○ ○ ○?", ["8", "9", "10", "11"], 2),
         ]},
        {"sr": "Nosaka nākamo un iepriekšējo skaitli",
         "stunda": "1.1.",
         "jautajumi": [
             ("Kurš skaitlis ir tūlīt pēc 4?", ["2", "3", "5", "6"], 2),
             ("Kurš skaitlis ir tūlīt pirms 9?", ["7", "8", "10", "11"], 1),
             ("Kurš skaitlis ir starp 6 un 8?", ["5", "7", "9", "10"], 1),
             ("Skaiti atpakaļ: 5, 4, 3, … Kurš ir nākamais?",
              ["1", "2", "4", "6"], 1),
         ]},
        {"sr": "Salīdzina skaitļus ar zīmēm «>», «<», «=»",
         "stunda": "1.1.",
         "jautajumi": [
             ("Kura zīme jāliek:  3 … 8?", [">", "<", "=", "+"], 1),
             ("Kura zīme jāliek:  9 … 2?", [">", "<", "=", "−"], 0),
             ("Kura zīme jāliek:  5 … 5?", [">", "<", "=", "+"], 2),
             ("Kurš skaitlis ir mazāks nekā 4?", ["2", "4", "6", "9"], 0),
         ]},
        {"sr": "Nosauc daudzstūri pēc malu skaita",
         "stunda": "1.1.",
         "jautajumi": [
             ("Cik malu ir trijstūrim?", ["2", "3", "4", "5"], 1),
             ("Kā sauc figūru ar 4 virsotnēm?",
              ["trijstūris", "četrstūris", "piecstūris", "riņķis"], 1),
             ("Kurai figūrai ir visvairāk malu?",
              ["trijstūris", "četrstūris", "piecstūris", "visām tikpat"], 2),
             ("Kurai figūrai nav malu un virsotņu?",
              ["trijstūris", "četrstūris", "piecstūris", "riņķis"], 3),
         ]},
        {"sr": "Apraksta objektu novietojumu un virzienu",
         "stunda": "1.1.",
         "jautajumi": [
             ("Rindā:  ▲ ● ■.  Kura figūra ir pa kreisi no ●?",
              ["▲", "●", "■", "neviena"], 0),
             ("Rindā:  ○ □ △.  Kura figūra ir vidū?",
              ["○", "□", "△", "neviena"], 1),
             ("Ko nozīmē bulta ↓?",
              ["uz augšu", "uz leju", "pa labi", "pa kreisi"], 1),
             ("Burtnīca ir zem grāmatas. Kur ir grāmata?",
              ["zem burtnīcas", "virs burtnīcas", "blakus solam",
               "somā"], 1),
         ]},
        {"sr": "Turpina virkni un zina nedēļas dienu secību",
         "stunda": "1.1.",
         "jautajumi": [
             ("Virkne:  ▲ ■ ▲ ■ ▲ …  Kurš ir nākamais?",
              ["▲", "■", "●", "○"], 1),
             ("Virkne:  2, 4, 6, 8, …  Kurš skaitlis ir nākamais?",
              ["9", "10", "11", "12"], 1),
             ("Cik dienu ir nedēļā?", ["5", "6", "7", "8"], 2),
             ("Kura diena ir pēc ceturtdienas?",
              ["trešdiena", "piektdiena", "sestdiena", "svētdiena"], 1),
         ]},
    ],
    # 2.-5. uzdevums. Katram uzdevumam trīs līdzvērtīgi varianti.
    "uzdevumi": [
        {"sr": "Ieraksta trūkstošos skaitļus skaitļu rindā 10 apjomā",
         "stunda": "1.1.", "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošos skaitļus",
              "note": "Ieraksti tukšajā vietā pareizo skaitli! Par katru "
                      "pareizu skaitli — 1 punkts.",
              "rindas": [
                  ("2,  3,  ……,  5", "4"),
                  ("6,  ……,  8,  9", "7"),
                  ("10,  9,  ……,  7", "8"),
                  ("……,  2,  3,  4", "1"),
              ]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošos skaitļus",
              "note": "Ieraksti tukšajā vietā pareizo skaitli! Par katru "
                      "pareizu skaitli — 1 punkts.",
              "rindas": [
                  ("1,  2,  ……,  4", "3"),
                  ("5,  ……,  7,  8", "6"),
                  ("9,  8,  ……,  6", "7"),
                  ("……,  7,  8,  9", "6"),
              ]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošos skaitļus",
              "note": "Ieraksti tukšajā vietā pareizo skaitli! Par katru "
                      "pareizu skaitli — 1 punkts.",
              "rindas": [
                  ("3,  4,  ……,  6", "5"),
                  ("7,  ……,  9,  10", "8"),
                  ("8,  7,  ……,  5", "6"),
                  ("……,  4,  5,  6", "3"),
              ]},
         ]},
        {"sr": "Salīdzina skaitļus un ieraksta zīmi «>», «<» vai «=»",
         "stunda": "1.1.", "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp skaitļiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [
                  ("4  ……  7", "<"),
                  ("9  ……  6", ">"),
                  ("5  ……  5", "="),
              ]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp skaitļiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [
                  ("8  ……  3", ">"),
                  ("2  ……  6", "<"),
                  ("7  ……  7", "="),
              ]},
             {"tips": "parveide", "virs": "Ieraksti zīmi  >,  <  vai  =",
              "note": "Starp skaitļiem ieraksti pareizo zīmi! Par katru "
                      "pareizu zīmi — 1 punkts.",
              "rindas": [
                  ("6  ……  9", "<"),
                  ("10  ……  4", ">"),
                  ("3  ……  3", "="),
              ]},
         ]},
        {"sr": "Zīmē un raksturo daudzstūri pēc malu un virsotņu skaita",
         "stunda": "1.1.", "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Figūras", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu!",
              "jaut": [
                  ("Uzzīmē trijstūri!", 1),
                  ("Uzzīmē četrstūri!", 1),
                  ("Uzraksti, cik malu ir tavam četrstūrim!", 1),
                  ("Apvelc to figūru, kurai ir vairāk virsotņu!", 1),
              ],
              "atbildes": [
                  "1) Uzzīmēta figūra ar 3 malām un 3 virsotnēm.   (1 p.)",
                  "2) Uzzīmēta figūra ar 4 malām un 4 virsotnēm.   (1 p.)",
                  "3) Pierakstīts skaitlis 4.   (1 p.)",
                  "4) Apvilkts četrstūris — tam ir 4 virsotnes, "
                  "trijstūrim 3.   (1 p.)",
              ]},
             {"tips": "jautajumi", "virs": "Figūras", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu!",
              "jaut": [
                  ("Uzzīmē četrstūri!", 1),
                  ("Uzzīmē piecstūri!", 1),
                  ("Uzraksti, cik virsotņu ir tavam piecstūrim!", 1),
                  ("Apvelc to figūru, kurai ir mazāk malu!", 1),
              ],
              "atbildes": [
                  "1) Uzzīmēta figūra ar 4 malām un 4 virsotnēm.   (1 p.)",
                  "2) Uzzīmēta figūra ar 5 malām un 5 virsotnēm.   (1 p.)",
                  "3) Pierakstīts skaitlis 5.   (1 p.)",
                  "4) Apvilkts četrstūris — tam ir 4 malas, "
                  "piecstūrim 5.   (1 p.)",
              ]},
             {"tips": "jautajumi", "virs": "Figūras", "vieta": 7.0,
              "ievads": "Zīmē ar lineālu!",
              "jaut": [
                  ("Uzzīmē trijstūri!", 1),
                  ("Uzzīmē piecstūri!", 1),
                  ("Uzraksti, cik malu ir tavam trijstūrim!", 1),
                  ("Apvelc to figūru, kurai ir vairāk malu!", 1),
              ],
              "atbildes": [
                  "1) Uzzīmēta figūra ar 3 malām un 3 virsotnēm.   (1 p.)",
                  "2) Uzzīmēta figūra ar 5 malām un 5 virsotnēm.   (1 p.)",
                  "3) Pierakstīts skaitlis 3.   (1 p.)",
                  "4) Apvilkts piecstūris — tam ir 5 malas, "
                  "trijstūrim 3.   (1 p.)",
              ]},
         ]},
        {"sr": "Attēlo un skaidro objektu novietojumu un pārvietošanos",
         "stunda": "1.1.", "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Kur un uz kuru pusi",
              "vieta": 6.0,
              "ievads": "Rindā ir trīs figūras:   ● ▲ ■",
              "jaut": [
                  ("Uzzīmē to figūru, kas ir starp ● un ■!", 1),
                  ("Uzzīmē ○ pa labi no ■!", 1),
                  ("Ar bultām parādi ceļu: divi soļi pa labi un viens solis "
                   "uz augšu!", 1),
              ],
              "atbildes": [
                  "1) Uzzīmēts ▲.   (1 p.)",
                  "2) ○ uzzīmēts pa labi no ■.   (1 p.)",
                  "3) Uzzīmētas bultas  → → ↑.   (1 p.)",
              ]},
             {"tips": "jautajumi", "virs": "Kur un uz kuru pusi",
              "vieta": 6.0,
              "ievads": "Rindā ir trīs figūras:   ▲ ○ ■",
              "jaut": [
                  ("Uzzīmē to figūru, kas ir pa kreisi no ○!", 1),
                  ("Uzzīmē ● zem ■!", 1),
                  ("Ar bultām parādi ceļu: viens solis pa kreisi un divi "
                   "soļi uz leju!", 1),
              ],
              "atbildes": [
                  "1) Uzzīmēts ▲.   (1 p.)",
                  "2) ● uzzīmēts zem ■.   (1 p.)",
                  "3) Uzzīmētas bultas  ← ↓ ↓.   (1 p.)",
              ]},
             {"tips": "jautajumi", "virs": "Kur un uz kuru pusi",
              "vieta": 6.0,
              "ievads": "Rindā ir trīs figūras:   ■ ● △",
              "jaut": [
                  ("Uzzīmē to figūru, kas ir pa labi no ●!", 1),
                  ("Uzzīmē □ virs ■!", 1),
                  ("Ar bultām parādi ceļu: divi soļi uz augšu un viens solis "
                   "pa kreisi!", 1),
              ],
              "atbildes": [
                  "1) Uzzīmēts △.   (1 p.)",
                  "2) □ uzzīmēts virs ■.   (1 p.)",
                  "3) Uzzīmētas bultas  ↑ ↑ ←.   (1 p.)",
              ]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
