# -*- coding: utf-8 -*-
"""Matemātika, 5. klase. 5.8. Kā vizuāli attēlo sakarību starp lielumiem?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 5. klase, 5.8. temats): koordinātu plakne
un asis, punkta koordinātas, ass vienības izvēle pēc lielumu skaitliskajām
vērtībām, sakarības grafiskais attēls kā atsevišķu punktu kopums vai līnija,
vērtību (precīzu un aptuvenu) nolasīšana no grafiskā attēla, sakarības
raksturošana un divu sakarību salīdzināšana vienā koordinātu plaknē.
"""

PRIEKSMETS = "Matemātika  |  5. klase"
TEMATS = "5.8."
NOSAUKUMS = "Kā vizuāli attēlo sakarību starp lielumiem?"

ATGADNE = [
    "Koordinātu plaknē ir divas asis: horizontālā (x) un vertikālā (y); "
    "tās krustojas sākumpunktā O.",
    "Punkta koordinātas raksta iekavās, vispirms x, tad y:   A(3; 5)   — "
    "3 pa labi, 5 uz augšu.",
    "Ass vienību izvēlas pēc lielumu vērtībām; grafiskais attēls ir vai nu "
    "atsevišķu punktu kopums, vai līnija — to nosaka, vai lielums var "
    "pieņemt jebkuru starpvērtību.",
]

FD = {
    "veids": "fd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 5.8. temata beigās. Pārbauda koordinātu "
                "plaknes uzbūvi, punkta koordinātas, ass vienības izvēli, "
                "sakarības grafiskā attēla veidu, vērtību nolasīšanu un "
                "secinājumus par sakarību.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina koordinātu plaknes uzbūvi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik asu ir koordinātu plaknē?", ["divas", "viena", "trīs",
                                                "četras"], 0),
             ("Kā sauc punktu, kurā krustojas asis?",
              ["sākumpunkts", "galapunkts", "viduspunkts", "virsotne"], 0),
             ("Kā koordinātu asis iekārto?",
              ["kā skaitļu taisni", "bez sākumpunkta", "bez vienības",
               "no acs"], 0),
         ]},
        {"sr": "Pieraksta punkta koordinātas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta punktu, kas ir 3 pa labi un 5 uz augšu?",
              ["A(3; 5)", "A(5; 3)", "A(3 + 5)", "A(3 · 5)"], 0),
             ("Kura koordināta ir pirmā?",
              ["horizontālā", "vertikālā", "lielākā", "mazākā"], 0),
             ("Kādas koordinātas ir sākumpunktam?",
              ["O(0; 0)", "O(1; 1)", "O(0; 1)", "O(1; 0)"], 0),
         ]},
        {"sr": "Atliek punktu koordinātu plaknē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kur atrodas punkts B(4; 0)?",
              ["uz horizontālās ass", "uz vertikālās ass", "sākumpunktā",
               "ārpus plaknes"], 0),
             ("Kur atrodas punkts C(0; 6)?",
              ["uz vertikālās ass", "uz horizontālās ass", "sākumpunktā",
               "ārpus plaknes"], 0),
             ("Kā atliek punktu D(2; 7)?",
              ["2 pa labi, tad 7 uz augšu", "7 pa labi, tad 2 uz augšu",
               "2 uz augšu, tad 7 pa labi", "9 pa labi"], 0),
         ]},
        {"sr": "Izvēlas ass vienību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas nosaka, kādai jābūt ass vienībai?",
              ["lielumu skaitliskās vērtības", "lapas krāsa",
               "punktu skaits", "ass nosaukums"], 0),
             ("Lielumu vērtības ir no 0 līdz 500. Kura vienība ir "
              "ērtākā?", ["50", "1", "2", "1000"], 0),
             ("Lielumu vērtības ir no 0 līdz 10. Kura vienība ir ērtākā?",
              ["1", "100", "50", "1000"], 0),
         ]},
        {"sr": "Nosaka grafiskā attēla veidu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir grafiskais attēls sakarībai starp nopirkto biļešu "
              "skaitu un samaksu?",
              ["atsevišķu punktu kopums", "nepārtraukta līnija",
               "riņķa līnija", "sektoru diagramma"], 0),
             ("Kāds ir grafiskais attēls sakarībai starp laiku un gaisa "
              "temperatūru?",
              ["nepārtraukta līnija", "atsevišķu punktu kopums",
               "taisne caur sākumpunktu", "sektoru diagramma"], 0),
             ("Kas nosaka grafiskā attēla veidu?",
              ["vai lielums var pieņemt jebkuru starpvērtību",
               "asu nosaukumi", "punktu krāsa", "lapas izmērs"], 0),
         ]},
        {"sr": "Nolasa precīzas vērtības no grafika",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grafikā punkts ir (4; 12). Kāda ir lieluma y vērtība, ja "
              "x = 4?", ["12", "4", "16", "8"], 0),
             ("Kā no grafika nolasa y, ja zināms x?",
              ["no x uz augšu, tad pa kreisi", "no x pa labi",
               "mēra garumu", "saskaita koordinātas"], 0),
             ("Ko rāda punkts uz grafiskā attēla?",
              ["abu lielumu vērtības vienlaikus", "tikai viena lieluma "
               "vērtību", "asu vienību", "lielumu summu"], 0),
         ]},
        {"sr": "Nolasa aptuvenas vērtības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad no grafika nolasa aptuvenu vērtību?",
              ["kad punkts nesakrīt ar iedaļu", "vienmēr",
               "kad grafiks ir taisne", "kad asis ir vienādas"], 0),
             ("Punkts atrodas starp iedaļām 20 un 30. Kāda ir aptuvenā "
              "vērtība?", ["aptuveni 25", "aptuveni 50", "aptuveni 10",
                           "aptuveni 5"], 0),
             ("Kā panāk, lai nolasījums būtu precīzāks?",
              ["izvēlas sīkāku ass vienību", "izvēlas lielāku ass vienību",
               "zīmē mazāku plakni", "nezīmē asis"], 0),
         ]},
        {"sr": "Raksturo sakarību pēc grafiskā attēla",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grafiks kāpj no kreisās puses uz labo. Ko tas nozīmē?",
              ["kad x aug, arī y aug", "kad x aug, y sarūk",
               "y nemainās", "x nemainās"], 0),
             ("Grafiks krīt no kreisās puses uz labo. Ko tas nozīmē?",
              ["kad x aug, y sarūk", "kad x aug, arī y aug",
               "y nemainās", "x nemainās"], 0),
             ("Grafiks ir horizontāla līnija. Ko tas nozīmē?",
              ["y vērtība nemainās", "x vērtība nemainās",
               "abi lielumi aug", "abi lielumi sarūk"], 0),
         ]},
        {"sr": "Salīdzina divas sakarības vienā plaknē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpēc abas sakarības attēlo vienā plaknē?",
              ["lai tās salīdzinātu", "lai taupītu papīru",
               "lai būtu skaistāk", "lai nebūtu asu"], 0),
             ("Divu grafiku krustpunkts rāda, ka...",
              ["abiem lielumiem ir vienādas vērtības",
               "viens grafiks beidzas", "asis ir vienādas",
               "vienība ir izvēlēta nepareizi"], 0),
             ("Kurš grafiks aug straujāk?",
              ["tas, kas ir stāvāks", "tas, kas ir garāks",
               "tas, kas ir zemāks", "tas, kas ir horizontāls"], 0),
         ]},
        {"sr": "Attēlo tabulā dotus datus grafiski",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā ir 5 vērtību pāri. Cik punktu būs grafiskajā "
              "attēlā?", ["5", "10", "2", "1"], 0),
             ("Kas ir pirmais solis?",
              ["izvēlas asis un vienības", "savieno punktus",
               "raksta virsrakstu", "mēra lapu"], 0),
             ("Kā rinda kļūst par punktu?",
              ["viena vērtība x, otra y", "abas ir x", "abas ir y",
               "tās saskaita"], 0),
         ]},
        {"sr": "Saista grafisko attēlu ar situāciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grafikā attēlots veiktais ceļš atkarībā no laika. Ko rāda "
              "horizontālā līnija?", ["kustība ir apstājusies",
                                      "kustība kļūst ātrāka",
                                      "kustība ir vienmērīga",
                                      "ceļš sarūk"], 0),
             ("Ko koordinātu plaknē nozīmē punkts (0; 0) ceļa grafikā?",
              ["kustības sākumu", "kustības beigas", "apstāšanos",
               "atgriešanos"], 0),
             ("Kā samaksa atkarīga no preču skaita?",
              ["jo vairāk, jo dārgāk", "jo vairāk, jo lētāk", "nemainās",
               "sakarības nav"], 0),
         ]},
        {"sr": "Formulē secinājumus pēc grafiskā attēla",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grafikā augstākais punkts rāda...",
              ["lielāko vērtību", "mazāko vērtību", "vidējo vērtību",
               "ass vienību"], 0),
             ("Kā nosaka, kad vērtība bijusi vislielākā?",
              ["atrod augstāko punktu", "saskaita punktus",
               "mēra garumu", "nolasa sākumu"], 0),
             ("Kāpēc sakarību attēlo grafiski?",
              ["lai to saprastu", "lai skaitļi augtu", "lai nerēķinātu",
               "lai zustu asis"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 5.8. temata noslēgumā. "
                "Pārbauda punkta koordinātas, ass vienības izvēli, "
                "grafiskā attēla veidu, vērtību nolasīšanu, sakarības "
                "raksturošanu un secinājumu formulēšanu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 "
              "punktus. Aprēķinus un skaidrojumus pieraksti tam atvēlētajā "
              "vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina koordinātu plaknes uzbūvi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc punktu, kurā krustojas koordinātu asis?",
              ["sākumpunkts", "galapunkts", "viduspunkts", "virsotne"], 0),
             ("Cik asu ir koordinātu plaknē?",
              ["divas", "viena", "trīs", "četras"], 0),
             ("Kādas koordinātas ir sākumpunktam?",
              ["O(0; 0)", "O(1; 1)", "O(0; 1)", "O(1; 0)"], 0),
         ]},
        {"sr": "Lieto punkta koordinātas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta punktu, kas ir 6 pa labi un 2 uz augšu?",
              ["A(6; 2)", "A(2; 6)", "A(6 + 2)", "A(6 · 2)"], 0),
             ("Kur atrodas punkts B(5; 0)?",
              ["uz horizontālās ass", "uz vertikālās ass", "sākumpunktā",
               "ārpus plaknes"], 0),
             ("Kura koordināta ir pirmā?",
              ["horizontālās ass koordināta", "vertikālās ass koordināta",
               "lielākā koordināta", "mazākā koordināta"], 0),
         ]},
        {"sr": "Izvēlas ass vienību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vērtības ir no 0 līdz 1000. Kura ass vienība ir ērtākā?",
              ["100", "1", "5", "10000"], 0),
             ("Kas nosaka ass vienību?",
              ["lielumu skaitliskās vērtības", "punktu skaits",
               "lapas izmērs", "ass nosaukums"], 0),
             ("Kāpēc izvēlas sīkāku ass vienību?",
              ["lai nolasījums būtu precīzāks", "lai grafiks būtu īsāks",
               "lai punktu būtu mazāk", "lai nevajadzētu asis"], 0),
         ]},
        {"sr": "Nosaka grafiskā attēla veidu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir grafiskais attēls sakarībai starp nopirkto grāmatu "
              "skaitu un samaksu?",
              ["atsevišķu punktu kopums", "nepārtraukta līnija",
               "riņķa līnija", "sektoru diagramma"], 0),
             ("Kāds ir grafiskais attēls sakarībai starp laiku un ūdens "
              "temperatūru?",
              ["nepārtraukta līnija", "atsevišķu punktu kopums",
               "sektoru diagramma", "stabiņu diagramma"], 0),
             ("Kas nosaka grafiskā attēla veidu?",
              ["vai lielums var pieņemt jebkuru starpvērtību",
               "asu nosaukumi", "punktu krāsa", "lapas izmērs"], 0),
         ]},
        {"sr": "Nolasa vērtības no grafiskā attēla",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grafikā ir punkts (3; 18). Kāda ir y vērtība, ja x = 3?",
              ["18", "3", "21", "6"], 0),
             ("Punkts atrodas starp iedaļām 40 un 50. Kāda ir aptuvenā "
              "vērtība?", ["aptuveni 45", "aptuveni 90", "aptuveni 4",
                           "aptuveni 400"], 0),
             ("Ko rāda viens punkts grafiskajā attēlā?",
              ["abu lielumu vērtības vienlaikus", "tikai viena lieluma "
               "vērtību", "ass vienību", "lielumu summu"], 0),
         ]},
        {"sr": "Raksturo un salīdzina sakarības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grafiks kāpj no kreisās puses uz labo. Ko tas nozīmē?",
              ["kad x aug, arī y aug", "kad x aug, y sarūk", "y nemainās",
               "x nemainās"], 0),
             ("Ko nozīmē divu grafiku krustpunkts?",
              ["abiem lielumiem ir vienādas vērtības",
               "viens grafiks beidzas", "asis ir vienādas",
               "vienība ir izvēlēta nepareizi"], 0),
             ("Ceļa grafikā horizontāla līnija rāda, ka...",
              ["kustība ir apstājusies", "kustība kļūst ātrāka",
               "ceļš sarūk", "laiks apstājas"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pieraksta un lasa punktu koordinātas",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Punkti koordinātu plaknē",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Punkts 4 pa labi, 3 uz augšu:   A……", "A(4; 3)"),
                         ("Punkta B(0; 5) atrašanās vieta:   ……",
                          "uz vertikālās ass"),
                         ("Punkta C(7; 0) atrašanās vieta:   ……",
                          "uz horizontālās ass"),
                         ("Sākumpunkta koordinātas:   O……", "O(0; 0)")]},
             {"tips": "parveide", "virs": "Punkti koordinātu plaknē",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Punkts 2 pa labi, 6 uz augšu:   A……", "A(2; 6)"),
                         ("Punkta B(3; 0) atrašanās vieta:   ……",
                          "uz horizontālās ass"),
                         ("Punkta C(0; 8) atrašanās vieta:   ……",
                          "uz vertikālās ass"),
                         ("Pirmā koordināta punkta pierakstā:   ……",
                          "x jeb horizontālā")]},
             {"tips": "parveide", "virs": "Punkti koordinātu plaknē",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Punkts 5 pa labi, 1 uz augšu:   A……", "A(5; 1)"),
                         ("Punkta B(6; 0) atrašanās vieta:   ……",
                          "uz horizontālās ass"),
                         ("Punkta C(0; 0) nosaukums:   ……", "sākumpunkts"),
                         ("Otrā koordināta punkta pierakstā:   ……",
                          "y jeb vertikālā")]},
         ]},
        {"sr": "Izvēlas ass vienību un grafiskā attēla veidu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Asis un attēla veids",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Vērtības no 0 līdz 500; ērta ass vienība:   ……",
                          "50"),
                         ("Biļešu skaits un samaksa; attēla veids:   ……",
                          "atsevišķi punkti"),
                         ("Laiks un temperatūra; attēla veids:   ……",
                          "līnija")]},
             {"tips": "parveide", "virs": "Asis un attēla veids",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Vērtības no 0 līdz 20; ērta ass vienība:   ……",
                          "2"),
                         ("Grāmatu skaits un samaksa; attēla veids:   ……",
                          "atsevišķi punkti"),
                         ("Laiks un veiktais ceļš; attēla veids:   ……",
                          "līnija")]},
             {"tips": "parveide", "virs": "Asis un attēla veids",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Vērtības no 0 līdz 1000; ērta ass vienība:   ……",
                          "100"),
                         ("Skolēnu skaits un galdu skaits; attēla veids:  "
                          " ……", "atsevišķi punkti"),
                         ("Laiks un ūdens tilpums traukā; attēla veids:  "
                          " ……", "līnija")]},
         ]},
        {"sr": "Veido sakarības grafisko attēlu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Sakarība tabulā un grafikā",
              "vieta": 5.6,
              "teksts": "Viena burtnīca maksā 2 eiro.   a) Aizpildi "
                        "tabulu par 1; 2; 3 un 4 burtnīcām!   b) Kāda ir "
                        "ass vienība, ja samaksa ir līdz 10 eiro?   "
                        "c) Uzzīmē grafisko attēlu!   d) Vai tas ir "
                        "punktu kopums vai līnija? Pamato!",
              "kriteriji": ["a) 2; 4; 6; 8 eiro.   (1 p.)",
                            "b) Piemēram, 1 eiro vai 2 eiro.   (1 p.)",
                            "c) Atlikti punkti (1; 2), (2; 4), (3; 6), "
                            "(4; 8).   (1 p.)",
                            "d) Punktu kopums, jo burtnīcu skaits ir "
                            "vesels skaitlis.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Sakarība tabulā un grafikā",
              "vieta": 5.6,
              "teksts": "Automašīna brauc ar ātrumu 60 km/h.   "
                        "a) Aizpildi tabulu par 1; 2; 3 un 4 stundām!   "
                        "b) Kāda ir ass vienība, ja ceļš ir līdz 240 km?   "
                        "c) Uzzīmē grafisko attēlu!   d) Vai tas ir punktu "
                        "kopums vai līnija? Pamato!",
              "kriteriji": ["a) 60; 120; 180; 240 km.   (1 p.)",
                            "b) Piemēram, 20 km vai 60 km.   (1 p.)",
                            "c) Atlikti punkti (1; 60), (2; 120), "
                            "(3; 180), (4; 240).   (1 p.)",
                            "d) Līnija, jo laiks var būt arī starpvērtība. "
                            "  (1 p.)"]},
             {"tips": "aprekins", "virs": "Sakarība tabulā un grafikā",
              "vieta": 5.6,
              "teksts": "Kvadrāta malas garums ir a cm.   a) Aizpildi "
                        "tabulu par perimetru, ja a = 1; 2; 3 un 4 cm!   "
                        "b) Kāda ir ass vienība, ja perimetrs ir līdz "
                        "16 cm?   c) Uzzīmē grafisko attēlu!   d) Kā mainās "
                        "perimetrs, ja mala aug?",
              "kriteriji": ["a) 4; 8; 12; 16 cm.   (1 p.)",
                            "b) Piemēram, 2 cm vai 4 cm.   (1 p.)",
                            "c) Atlikti punkti (1; 4), (2; 8), (3; 12), "
                            "(4; 16).   (1 p.)",
                            "d) Perimetrs aug — 4 reizes ātrāk nekā mala. "
                            "  (1 p.)"]},
         ]},
        {"sr": "Formulē secinājumus pēc grafiskā attēla",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Ceļa grafiks", "vieta": 4.6,
              "ievads": "Grafikā attēlots velosipēdista veiktais ceļš "
                        "atkarībā no laika: pirmajā stundā 15 km, otrajā "
                        "stundā ceļš nemainās, trešajā stundā vēl 15 km.",
              "jaut": [("Cik km velosipēdists veica kopā?", 1),
                       ("Ko nozīmē horizontālā grafika daļa?", 1),
                       ("Cik ilgi velosipēdists atpūtās?", 1)],
              "atbildes": ["1) 15 + 15 = 30 km.   (1 p.)",
                           "2) Kustība ir apstājusies — ceļš nepieaug. "
                           "  (1 p.)",
                           "3) Vienu stundu.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Divas sakarības", "vieta": 4.6,
              "ievads": "Vienā koordinātu plaknē attēlotas divu veikalu "
                        "cenas: A veikalā burtnīca maksā 2 eiro, B veikalā "
                        "— 3 eiro.",
              "jaut": [("Kurš grafiks ir stāvāks?", 1),
                       ("Cik maksās 5 burtnīcas katrā veikalā?", 1),
                       ("Kurā veikalā izdevīgāk pirkt? Pamato!", 1)],
              "atbildes": ["1) B veikala grafiks.   (1 p.)",
                           "2) A: 10 eiro, B: 15 eiro.   (1 p.)",
                           "3) A veikalā, jo par to pašu skaitu jāmaksā "
                           "mazāk.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Temperatūras grafiks",
              "vieta": 4.6,
              "ievads": "Grafikā attēlota gaisa temperatūra dienas laikā: "
                        "plkst. 6 bija 8 °C, plkst. 14 — 20 °C, plkst. 22 "
                        "— 12 °C.",
              "jaut": [("Kad temperatūra bija visaugstākā?", 1),
                       ("Par cik grādiem tā pieauga no plkst. 6 līdz 14?",
                        1),
                       ("Kā mainījās temperatūra pēc plkst. 14?", 1)],
              "atbildes": ["1) Plkst. 14.   (1 p.)",
                           "2) 20 − 8 = 12 °C.   (1 p.)",
                           "3) Tā sāka sarukt — grafiks krīt.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
