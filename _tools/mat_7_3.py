# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.3. Kā raksturo sakarību starp mainīgiem lielumiem?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.3. temats): nemainīgi un
mainīgi lielumi, neatkarīgais un atkarīgais mainīgais, mainīgo apzīmēšana ar
burtiem, sakarības pieraksts ar formulu, mainīgā pieļaujamās vērtības un
pāreja starp tabulu, grafisko attēlu un formulu, arī tieši un apgriezti
proporcionāliem lielumiem.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.3."
NOSAUKUMS = "Kā raksturo sakarību starp mainīgiem lielumiem?"

ATGADNE = [
    "Mainot neatkarīgo mainīgo (parasti x), mainās atkarīgais mainīgais "
    "(parasti y). Nemainīgs lielums situācijā paliek tas pats.",
    "Sakarību pieraksta ar formulu:   y = k · x   (tieši proporcionāli)   ·  "
    " y = {k|x}   (apgriezti proporcionāli)   ·   piemēram   s = v · t",
    "Vienu un to pašu sakarību var attēlot tabulā, grafiski un ar formulu; "
    "grafiks ir atsevišķi punkti vai līnija — to nosaka konteksts.",
]


# ---------------------------------------------------------------- veidnes
def vertiba(k, b, x):
    """Aprēķina y vērtību pēc formulas y = k · x + b."""
    zime = "+" if b >= 0 else "−"
    return ("Sakarību apraksta formula  y = %d · x %s %d. Cik liels ir y, ja "
            "x = %d?" % (k, zime, abs(b), x),
            V.izvele(k * x + b, k * x - b, k + x + b, (k + x) * b,
                     k * x, k * (x + b), k * x + b + 1), 0)


def tiesi(k, x, ko, mervieniba):
    """Tieši proporcionāla sakarība: y = k · x."""
    return ("1 %s maksā %d eiro. Cik maksā %d %s?" % (mervieniba, k, x, ko),
            V.izvele("%d eiro" % (k * x), "%d eiro" % (k + x),
                     "%d eiro" % (x - k), "%d eiro" % (k * x + x),
                     "%d eiro" % (k * x * 2), "%d eiro" % (k * x + 1)), 0)


def apgriezti(kopa_, n):
    """Apgriezti proporcionāla sakarība: y = {kopa|x}."""
    return ("%d konfektes sadala vienādi %d bērniem. Cik konfekšu saņem "
            "katrs?" % (kopa_, n),
            V.izvele(kopa_ // n, kopa_ * n, kopa_ - n, kopa_ + n,
                     n, kopa_ // n + 1, kopa_ // n - 1), 0)


def formula(k, ko, mervieniba):
    """Sakarības pieraksts ar formulu."""
    return ("1 %s maksā %d eiro. Ar kuru formulu aprēķina samaksu y par "
            "x %s?" % (mervieniba, k, ko),
            V.izvele("y = %d · x" % k, "y = x + %d" % k,
                     "y = {%d|x}" % k, "y = x − %d" % k,
                     "y = {x|%d}" % k, "y = %d" % k), 0)


def arguments(k, y):
    """No dotas funkcijas vērtības nosaka argumentu: y = k · x."""
    return ("Sakarību apraksta formula  y = %d · x. Cik liels ir x, ja "
            "y = %d?" % (k, y),
            V.izvele(y // k, y * k, y - k, y + k, k, y // k + 1,
                     y // k - 1), 0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.3. temata beigās. Pārbauda neatkarīgā "
                "un atkarīgā mainīgā jēdzienu, sakarības pierakstu ar "
                "formulu, vērtību aprēķināšanu un pāreju starp tabulu, "
                "grafiku un formulu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Atšķir mainīgus un nemainīgus lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir mainīgs lielums?",
              ["lielums, kas situācijā var mainīties",
               "lielums, kas nemainās", "tikai skaitlis", "tikai burts"], 0),
             ("Braucot ar pastāvīgu ātrumu, kurš lielums ir nemainīgs?",
              ["ātrums", "laiks", "ceļš", "degvielas patēriņš"], 0),
             ("Pērkot burtnīcas, kurš lielums ir nemainīgs?",
              ["vienas burtnīcas cena", "burtnīcu skaits", "samaksa",
               "somas svars"], 0),
             ("Ar ko matemātikā apzīmē mainīgus lielumus?",
              ["ar burtiem", "ar cipariem", "ar krāsām",
               "ar mērvienībām"], 0),
             ("Kāpēc svarīgi zināt, kuras vērtības mainīgais var pieņemt?",
              ["lai spriedumos nekļūdītos", "lai būtu ātrāk",
               "lai skaitļi būtu lieli", "tas nav svarīgi"], 0),
             ("Vai burtnīcu skaits var būt 2,5?",
              ["nē, tas ir vesels skaitlis", "jā", "tikai veikalā",
               "nevar noteikt"], 0),
             ("Vai laiks var būt negatīvs?",
              ["nē", "jā", "tikai aprēķinos", "vienmēr"], 0),
             ("Kurš lielums var pieņemt jebkuru starpvērtību?",
              ["ūdens tilpums", "skolēnu skaits", "burtnīcu skaits",
               "galdu skaits"], 0),
         ]},
        {"sr": "Nosaka neatkarīgo un atkarīgo mainīgo",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc mainīgo, kuru maina pēc izvēles?",
              ["neatkarīgais mainīgais", "atkarīgais mainīgais",
               "nemainīgais lielums", "koeficients"], 0),
             ("Kā sauc mainīgo, kura vērtība izriet no otra?",
              ["atkarīgais mainīgais", "neatkarīgais mainīgais",
               "nemainīgais lielums", "koeficients"], 0),
             ("Pērkot ābolus, kurš ir neatkarīgais mainīgais?",
              ["ābolu daudzums", "samaksa", "ābolu cena", "veikala nosaukums"],
              0),
             ("Pērkot ābolus, kurš ir atkarīgais mainīgais?",
              ["samaksa", "ābolu daudzums", "ābolu cena", "diena"], 0),
             ("Braucot ar pastāvīgu ātrumu, kurš ir atkarīgais mainīgais?",
              ["veiktais ceļš", "ātrums", "auto krāsa", "ceļa segums"], 0),
             ("Uz kuras ass parasti atliek neatkarīgo mainīgo?",
              ["uz horizontālās", "uz vertikālās", "uz abām",
               "ne uz vienas"], 0),
             ("Uz kuras ass parasti atliek atkarīgo mainīgo?",
              ["uz vertikālās", "uz horizontālās", "uz abām",
               "ne uz vienas"], 0),
             ("Ar kuru burtu parasti apzīmē neatkarīgo mainīgo?",
              ["x", "y", "k", "b"], 0),
         ]},
        {"sr": "Pieraksta sakarību ar formulu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(formula, [
             (3, "burtnīcas", "burtnīca"), (5, "grāmatas", "grāmata"),
             (2, "pildspalvas", "pildspalva"), (4, "biļetes", "biļete"),
             (7, "krūzes", "krūze"), (6, "somas", "soma"),
             (8, "cimdu pārus", "cimdu pāris"), (9, "cepures", "cepure"),
             (10, "grāmatzīmes", "grāmatzīme"), (12, "kastes", "kaste"),
             (15, "spilvenus", "spilvens"), (11, "apļus", "aplis"),
             (13, "kilogramus", "kilograms"), (14, "metrus", "metrs"),
             (20, "litrus", "litrs")]),
         },
        {"sr": "Aprēķina atkarīgā mainīgā vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vertiba, [
             (2, 3, 4), (3, -1, 5), (4, 2, 3), (5, -3, 6), (2, 7, 8),
             (6, 1, 2), (3, 5, 7), (7, -2, 4), (4, -5, 9), (8, 3, 2),
             (5, 4, 6), (9, -1, 3), (6, -4, 5), (10, 2, 7), (3, 8, 11)]),
         },
        {"sr": "Aprēķina neatkarīgā mainīgā vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(arguments, [
             (3, 12), (4, 20), (5, 35), (6, 24), (7, 42), (8, 56),
             (2, 18), (9, 27), (10, 80), (11, 44), (12, 60), (13, 39),
             (14, 70), (15, 45), (16, 96)]),
         },
        {"sr": "Lieto tieši proporcionālu sakarību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(tiesi, [
             (3, 4, "burtnīcas", "burtnīca"), (5, 3, "grāmatas", "grāmata"),
             (2, 7, "pildspalvas", "pildspalva"),
             (4, 6, "biļetes", "biļete"), (6, 5, "krūzes", "krūze"),
             (7, 3, "somas", "soma"), (8, 4, "cepures", "cepure"),
             (9, 2, "kastes", "kaste"), (10, 6, "kilogramus", "kilograms"),
             (12, 3, "metrus", "metrs"), (11, 5, "litrus", "litrs"),
             (13, 4, "biļetes", "biļete"), (15, 2, "grāmatas", "grāmata"),
             (14, 6, "krūzes", "krūze"), (20, 3, "somas", "soma")]),
         },
        {"sr": "Lieto apgriezti proporcionālu sakarību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(apgriezti, [
             (24, 6), (36, 4), (48, 8), (60, 5), (72, 9), (30, 6),
             (56, 7), (64, 8), (81, 9), (100, 10), (42, 6), (45, 5),
             (54, 6), (90, 9), (44, 4)]),
         },
        {"sr": "Atpazīst proporcionalitātes veidu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad lielumi ir tieši proporcionāli?",
              ["abi aug tikpat reižu", "viens aug, otrs sarūk",
               "abi nemainās", "tie ir vienādi"], 0),
             ("Kad lielumi ir apgriezti proporcionāli?",
              ["viens aug, otrs sarūk tikpat reižu", "abi aug",
               "abi sarūk", "tie ir vienādi"], 0),
             ("Kāda ir tieši proporcionālu lielumu formula?",
              ["y = k · x", "y = {k|x}", "y = x + k", "y = x − k"], 0),
             ("Kāda ir apgriezti proporcionālu lielumu formula?",
              ["y = {k|x}", "y = k · x", "y = x + k", "y = x − k"], 0),
             ("Kuri lielumi ir tieši proporcionāli?",
              ["ceļš un laiks pie pastāvīga ātruma", "ātrums un laiks",
               "strādnieku skaits un laiks", "malas garums un leņķis"], 0),
             ("Kuri lielumi ir apgriezti proporcionāli?",
              ["ātrums un laiks noteiktā ceļā", "preču skaits un samaksa",
               "malas garums un perimetrs", "laiks un veiktais ceļš"], 0),
             ("Tieši proporcionāliem lielumiem — cik ir y : x?",
              ["pastāvīgs skaitlis", "vienmēr 0", "vienmēr 1",
               "tas mainās"], 0),
             ("Apgriezti proporcionāliem lielumiem — cik ir x · y?",
              ["pastāvīgs skaitlis", "vienmēr 0", "vienmēr 1",
               "tas mainās"], 0),
         ]},
        {"sr": "Pāriet no tabulas uz formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: x = 1, 2, 3;  y = 4, 8, 12. Kāda ir formula?",
              ["y = 4 · x", "y = x + 3", "y = 4 + x", "y = {4|x}"], 0),
             ("Tabulā: x = 1, 2, 3;  y = 5, 10, 15. Kāda ir formula?",
              ["y = 5 · x", "y = x + 4", "y = 5 + x", "y = {5|x}"], 0),
             ("Tabulā: x = 1, 2, 4;  y = 12, 6, 3. Kāda ir formula?",
              ["y = {12|x}", "y = 12 · x", "y = 12 − x", "y = x + 11"], 0),
             ("Tabulā: x = 2, 4, 6;  y = 5, 7, 9. Kāda ir formula?",
              ["y = x + 3", "y = 3 · x", "y = {10|x}", "y = x − 3"], 0),
             ("Tabulā: x = 1, 2, 3;  y = 3, 6, 9. Kāda ir formula?",
              ["y = 3 · x", "y = x + 2", "y = 3 + x", "y = {3|x}"], 0),
             ("Tabulā: x = 1, 2, 3;  y = 20, 10, ... Kāda ir trešā vērtība?",
              ["nedaudz vairāk nekā 6", "5", "30", "0"], 0),
             ("Kas jāpārbauda, meklējot formulu?",
              ["vai tā der visiem tabulas pāriem", "vai tā ir īsa",
               "vai tajā ir x", "vai skaitļi ir veseli"], 0),
             ("Ko rāda koeficients k formulā y = k · x?",
              ["cik reižu y ir lielāks nekā x", "y sākuma vērtību",
               "x lielāko vērtību", "grafika garumu"], 0),
         ]},
        {"sr": "Pāriet no formulas uz tabulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("y = 3 · x. Kādas ir y vērtības, ja x = 1; 2; 3?",
              ["3; 6; 9", "1; 2; 3", "3; 3; 3", "4; 5; 6"], 0),
             ("y = x + 5. Kādas ir y vērtības, ja x = 0; 1; 2?",
              ["5; 6; 7", "0; 1; 2", "5; 5; 5", "5; 10; 15"], 0),
             ("y = {24|x}. Kādas ir y vērtības, ja x = 2; 3; 4?",
              ["12; 8; 6", "2; 3; 4", "24; 24; 24", "48; 72; 96"], 0),
             ("y = 2 · x − 1. Kādas ir y vērtības, ja x = 1; 2; 3?",
              ["1; 3; 5", "2; 4; 6", "0; 1; 2", "1; 2; 3"], 0),
             ("y = 10 − x. Kādas ir y vērtības, ja x = 1; 2; 3?",
              ["9; 8; 7", "11; 12; 13", "10; 10; 10", "1; 2; 3"], 0),
             ("y = 4 · x. Cik ir y, ja x = 0?", ["0", "4", "1", "−4"], 0),
             ("y = {12|x}. Vai x var būt 0?",
              ["nē, ar nulli nedala", "jā", "tikai tabulā",
               "tikai grafikā"], 0),
             ("Cik punktu būs grafikā, ja tabulā ir 6 vērtību pāri?",
              ["6", "12", "3", "1"], 0),
         ]},
        {"sr": "Raksturo sakarību pēc grafika",
         "stunda": TEMATS,
         "jautajumi": [
             ("Grafiks kāpj no kreisās puses uz labo. Ko tas nozīmē?",
              ["kad x aug, arī y aug", "kad x aug, y sarūk", "y nemainās",
               "x nemainās"], 0),
             ("Grafiks krīt no kreisās puses uz labo. Ko tas nozīmē?",
              ["kad x aug, y sarūk", "kad x aug, arī y aug", "y nemainās",
               "x nemainās"], 0),
             ("Kāds ir tieši proporcionālu lielumu grafiks?",
              ["taisne caur sākumpunktu", "līkne", "horizontāla līnija",
               "riņķa līnija"], 0),
             ("Kā no grafika nolasa y vērtību?",
              ["no x iet uz augšu līdz grafikam", "no x iet pa labi",
               "mēra grafika garumu", "saskaita koordinātas"], 0),
             ("Ko rāda grafika horizontālā daļa?",
              ["y vērtība nemainās", "x vērtība nemainās", "abi aug",
               "abi sarūk"], 0),
             ("Kad grafiks ir atsevišķi punkti?",
              ["kad mainīgais ir vesels skaitlis",
               "kad mainīgais ir jebkurš skaitlis", "vienmēr", "nekad"], 0),
             ("Kad grafiks ir nepārtraukta līnija?",
              ["kad mainīgais var pieņemt jebkuru starpvērtību",
               "kad mainīgais ir vesels skaitlis", "vienmēr", "nekad"], 0),
             ("Kāpēc sakarību attēlo grafiski?",
              ["lai to vieglāk saprastu", "lai nerēķinātu",
               "lai skaitļi augtu", "lai zustu asis"], 0),
         ]},
        {"sr": "Saista sakarību ar situāciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu apraksta ceļu pie pastāvīga ātruma?",
              ["s = v · t", "s = v + t", "s = {v|t}", "s = v − t"], 0),
             ("Ar kuru formulu apraksta taisnstūra laukumu?",
              ["S = a · b", "S = a + b", "S = 2 · (a + b)", "S = {a|b}"], 0),
             ("Ar kuru formulu apraksta kvadrāta perimetru?",
              ["P = 4 · a", "P = a²", "P = 2 · a", "P = {4|a}"], 0),
             ("Auto brauc 60 km/h. Cik km tas veiks 3 stundās?",
              ["180 km", "20 km", "63 km", "120 km"], 0),
             ("Ceļš ir 240 km. Cik ilgi brauks ar ātrumu 80 km/h?",
              ["3 h", "4 h", "2 h", "160 h"], 0),
             ("Kvadrāta mala ir 7 cm. Cik garš ir perimetrs?",
              ["28 cm", "49 cm", "14 cm", "21 cm"], 0),
             ("Kā mainās taisnstūra laukums, ja abas malas dubulto?",
              ["aug 4 reizes", "aug 2 reizes", "nemainās",
               "aug 8 reizes"], 0),
             ("Kā mainās ceļš, ja ātrumu dubulto un laiks paliek tas pats?",
              ["aug 2 reizes", "sarūk 2 reizes", "nemainās",
               "aug 4 reizes"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.3. temata noslēgumā. "
                "Pārbauda mainīgo lielumu jēdzienus, sakarības pierakstu ar "
                "formulu, vērtību aprēķināšanu un pāreju starp tabulu, "
                "grafiku un formulu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Nosaka mainīgos lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc mainīgo, kuru maina pēc izvēles?",
              ["neatkarīgais mainīgais", "atkarīgais mainīgais",
               "nemainīgais lielums", "koeficients"], 0),
             ("Kā sauc mainīgo, kura vērtība izriet no otra?",
              ["atkarīgais mainīgais", "neatkarīgais mainīgais",
               "nemainīgais lielums", "koeficients"], 0),
             ("Pērkot ābolus, kurš ir nemainīgs lielums?",
              ["viena kilograma cena", "ābolu daudzums", "samaksa",
               "somas svars"], 0),
             ("Ar ko apzīmē mainīgus lielumus?",
              ["ar burtiem", "ar cipariem", "ar krāsām",
               "ar mērvienībām"], 0),
             ("Uz kuras ass atliek neatkarīgo mainīgo?",
              ["uz horizontālās", "uz vertikālās", "uz abām",
               "ne uz vienas"], 0),
             ("Vai burtnīcu skaits var būt 2,5?",
              ["nē, tas ir vesels skaitlis", "jā", "tikai veikalā",
               "nevar noteikt"], 0),
             ("Kurš lielums var pieņemt jebkuru starpvērtību?",
              ["ūdens tilpums", "skolēnu skaits", "burtnīcu skaits",
               "galdu skaits"], 0),
             ("Ar kuru burtu parasti apzīmē atkarīgo mainīgo?",
              ["y", "x", "k", "b"], 0),
         ]},
        {"sr": "Pieraksta sakarību ar formulu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(formula, [
             (4, "burtnīcas", "burtnīca"), (6, "grāmatas", "grāmata"),
             (3, "pildspalvas", "pildspalva"), (5, "biļetes", "biļete"),
             (8, "krūzes", "krūze"), (7, "somas", "soma"),
             (9, "cimdu pārus", "cimdu pāris"), (10, "cepures", "cepure"),
             (11, "grāmatzīmes", "grāmatzīme"), (13, "kastes", "kaste"),
             (16, "spilvenus", "spilvens"), (12, "apļus", "aplis"),
             (14, "kilogramus", "kilograms"), (15, "metrus", "metrs"),
             (25, "litrus", "litrs")]),
         },
        {"sr": "Aprēķina mainīgo vērtības",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(vertiba, [
             (3, 2, 5), (4, -3, 6), (5, 1, 4), (6, -2, 7), (2, 9, 3),
             (7, 4, 2), (8, -5, 3)])
             + V.kopa(arguments, [
                 (4, 32), (5, 40), (6, 54), (7, 63), (8, 72), (9, 81),
                 (11, 55), (12, 84)])),
         },
        {"sr": "Lieto tieši proporcionālu sakarību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(tiesi, [
             (4, 5, "burtnīcas", "burtnīca"), (6, 3, "grāmatas", "grāmata"),
             (3, 8, "pildspalvas", "pildspalva"),
             (5, 6, "biļetes", "biļete"), (7, 4, "krūzes", "krūze"),
             (8, 3, "somas", "soma"), (9, 5, "cepures", "cepure"),
             (10, 2, "kastes", "kaste"), (11, 6, "kilogramus", "kilograms"),
             (13, 3, "metrus", "metrs"), (12, 5, "litrus", "litrs"),
             (14, 4, "biļetes", "biļete"), (16, 2, "grāmatas", "grāmata"),
             (15, 6, "krūzes", "krūze"), (22, 3, "somas", "soma")]),
         },
        {"sr": "Lieto apgriezti proporcionālu sakarību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(apgriezti, [
             (48, 6), (40, 5), (63, 7), (72, 8), (36, 9), (50, 10),
             (28, 4), (66, 6), (84, 7), (96, 8), (55, 5), (120, 10),
             (39, 3), (77, 7), (108, 9)]),
         },
        {"sr": "Atpazīst proporcionalitātes veidu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāda ir tieši proporcionālu lielumu formula?",
              ["y = k · x", "y = {k|x}", "y = x + k", "y = x − k"], 0),
             ("Kāda ir apgriezti proporcionālu lielumu formula?",
              ["y = {k|x}", "y = k · x", "y = x + k", "y = x − k"], 0),
             ("Kuri lielumi ir apgriezti proporcionāli?",
              ["ātrums un laiks noteiktā ceļā", "preču skaits un samaksa",
               "malas garums un perimetrs", "laiks un veiktais ceļš"], 0),
             ("Tieši proporcionāliem lielumiem — cik ir y : x?",
              ["pastāvīgs skaitlis", "vienmēr 0", "vienmēr 1",
               "tas mainās"], 0),
             ("Kāds ir tieši proporcionālu lielumu grafiks?",
              ["taisne caur sākumpunktu", "līkne", "horizontāla līnija",
               "riņķa līnija"], 0),
             ("Tabulā: x = 1, 2, 3;  y = 6, 12, 18. Kāda ir formula?",
              ["y = 6 · x", "y = x + 5", "y = 6 + x", "y = {6|x}"], 0),
             ("Tabulā: x = 1, 2, 3;  y = 18, 9, 6. Kāda ir formula?",
              ["y = {18|x}", "y = 18 · x", "y = 18 − x", "y = x + 17"], 0),
             ("Apgriezti proporcionāliem lielumiem — cik ir x · y?",
              ["pastāvīgs skaitlis", "vienmēr 0", "vienmēr 1",
               "tas mainās"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina vērtības pēc formulas",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda k, b, x1, x2, y: [
                 ("y = %d · x + %d;  ja x = %d, tad y = ……" % (k, b, x1),
                  V.sk(k * x1 + b)),
                 ("y = %d · x + %d;  ja x = %d, tad y = ……" % (k, b, x2),
                  V.sk(k * x2 + b)),
                 ("y = %d · x;  ja y = %d, tad x = ……" % (k, y),
                  V.sk(y // k)),
                 ("y = {%d|x};  ja x = %d, tad y = ……" % (k * 12, 4),
                  V.sk(k * 3))],
             [(2, 3, 4, 7, 12), (3, 1, 5, 8, 18), (4, 2, 3, 6, 24),
              (5, 4, 2, 9, 35), (6, 1, 4, 7, 42), (7, 3, 5, 8, 49),
              (8, 2, 3, 6, 56), (9, 5, 2, 7, 63), (10, 1, 4, 9, 70),
              (11, 2, 3, 5, 77), (12, 4, 2, 6, 84), (13, 1, 5, 7, 91),
              (14, 3, 4, 8, 98), (15, 2, 3, 9, 105), (16, 5, 2, 4, 96)]),
         },
        {"sr": "Pāriet no tabulas uz formulu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Tabula un formula",
             lambda k, b, kop: [
                 ("x = 1; 2; 3,  y = %d; %d; %d;  formula:   y = ……"
                  % (k, 2 * k, 3 * k), "y = %d · x" % k),
                 ("x = 1; 2; 3,  y = %d; %d; %d;  formula:   y = ……"
                  % (1 + b, 2 + b, 3 + b), "y = x + %d" % b),
                 ("x = 1; 2; %d,  y = %d; %d; %d;  formula:   y = ……"
                  % (4, kop, kop // 2, kop // 4), "y = {%d|x}" % kop)],
             [(4, 3, 12), (5, 2, 20), (6, 4, 24), (7, 5, 28), (8, 1, 16),
              (9, 6, 36), (3, 7, 8), (10, 2, 40), (11, 3, 44), (12, 8, 48),
              (2, 9, 32), (13, 4, 52), (14, 5, 56), (15, 6, 60),
              (16, 7, 64)]),
         },
        {"sr": "Risina uzdevumu ar sakarību starp lielumiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Sakarība situācijā",
             lambda cena, n, kop: {
                 "teksts": "Viena biļete maksā %d eiro.   a) Pieraksti ar "
                           "formulu samaksu y par x biļetēm!   b) Cik maksā "
                           "%d biļetes?   c) Cik biļešu var nopirkt par "
                           "%d eiro?   d) Kurš lielums šeit ir nemainīgs?"
                           % (cena, n, kop),
                 "kriteriji": [
                     "a) y = %d · x.   (1 p.)" % cena,
                     "b) %d · %d = %d eiro.   (1 p.)" % (cena, n, cena * n),
                     "c) %d : %d = %d biļetes.   (1 p.)"
                     % (kop, cena, kop // cena),
                     "d) Vienas biļetes cena — %d eiro.   (1 p.)" % cena]},
             [(4, 5, 40), (6, 3, 42), (3, 8, 27), (5, 6, 45), (7, 4, 56),
              (8, 3, 64), (9, 5, 72), (10, 2, 90), (12, 4, 60), (15, 3, 75),
              (11, 6, 55), (13, 4, 65), (14, 5, 70), (16, 3, 80),
              (20, 4, 100)]),
         },
        {"sr": "Skaidro sakarības attēlojumus",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Trīs attēlojumi",
             lambda k: {
                 "ievads": "Sakarību starp lielumiem apraksta formula  "
                           "y = %d · x." % k,
                 "jaut": [("Aizpildi tabulu, ja x = 1; 2; 3!", 1),
                          ("Kurš ir neatkarīgais mainīgais?", 1),
                          ("Vai lielumi ir tieši proporcionāli? Pamato!",
                           1)],
                 "atbildes": [
                     "1) y = %d; %d; %d.   (1 p.)" % (k, 2 * k, 3 * k),
                     "2) Mainīgais x.   (1 p.)",
                     "3) Jā — y : x = %d ir pastāvīgs.   (1 p.)" % k]},
             [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
