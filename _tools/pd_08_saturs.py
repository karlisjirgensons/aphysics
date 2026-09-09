# -*- coding: utf-8 -*-
"""PD8 — Viļņi dabā un tehnikā (13.1.–13.8. stunda)."""

PD = {
    "nr": 8,
    "nosaukums": "Viļņi dabā un tehnikā",
    "mape": "13. Viļņi dabā un tehnikā",
    "fails": "PD8. Viļņi dabā un tehnikā",
    "stundas": "13.1.–13.8.",
    "datums": "12.03.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda svārstību raksturlielumus, mehāniskos "
                "viļņus, skaņu un eholokāciju, elektromagnētiskos viļņus un "
                "to skalu, kā arī viļņu īpašības un lietojumu.",
    "atgadne": [
        "f = 1 / T   ·   T = 1 / f   ·   T = t / N   ·   f = N / t   ·   "
        "[f] = Hz = 1/s",
        "λ = υ · T = υ / f   ·   υ = λ · f   ·   s = υ · t / 2  (atbalss, "
        "eholokācija)",
        "υ(gaisā) = 343 m/s   ·   υ(ūdenī) = 1480 m/s   ·   "
        "υ(tēraudā) = 5100 m/s   ·   c = 3,00 · 10⁸ m/s",
        "λ = c / f   ·   E = h · f   ·   h = 6,63 · 10⁻³⁴ J·s   ·   "
        "1 kHz = 10³ Hz  ·  1 MHz = 10⁶ Hz  ·  1 GHz = 10⁹ Hz",
    ],
    "struktura": [
        ("1.", "Raksturo svārstības, viļņu veidus, skaņas diapazonus, "
               "elektromagnētisko viļņu skalu un viļņu īpašības",
         "13.1.–13.8.", 10),
        ("2.", "Aprēķina svārstību periodu un frekvenci", "13.1.", 4),
        ("3.", "Aprēķina viļņa garumu dažādās vidēs un nosaka, kas nemainās",
         "13.2., 13.3.", 5),
        ("4.", "Lieto sakarību s = υ·t/2 eholokācijas uzdevumos", "13.4.", 5),
        ("5.", "Aprēķina elektromagnētiskā viļņa garumu pēc frekvences",
         "13.5.", 3),
        ("6.", "Atpazīst viļņu īpašības un orientējas EM viļņu skalā",
         "13.6., 13.7.", 3),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Ko rāda svārstību frekvence?",
                 ["laiku vienai pilnai svārstībai",
                  "lielāko novirzi no līdzsvara stāvokļa",
                  "svārstību skaitu sekundē", "viļņa garumu"], 2),
                ("Ja svārstību periods ir T = 0,02 s, cik liela ir "
                 "frekvence?",
                 ["0,02 Hz", "50 Hz", "2 Hz", "500 Hz"], 1),
                ("Kurš no minētajiem ir garenvilnis?",
                 ["viļņi uz ūdens", "skaņa gaisā", "gaisma",
                  "viļņi uz nostieptas virves"], 1),
                ("Kas vilnī pārvietojas no viena punkta uz otru?",
                 ["enerģija", "viela", "atsevišķas daļiņas", "masa"], 0),
                ("Kas nosaka skaņas augstumu?",
                 ["frekvence", "amplitūda", "izplatīšanās ātrums",
                  "skaļuma līmenis decibelos"], 0),
                ("Kāda ir ultraskaņas frekvence?",
                 ["zem 20 Hz", "no 20 Hz līdz 20 kHz", "virs 20 kHz",
                  "virs 20 MHz"], 2),
                ("Kāpēc kosmosā valda klusums?",
                 ["skaņa tur ir pārāk vāja",
                  "temperatūra ir pārāk zema", "tur nav gravitācijas",
                  "tur nav vides, kurā skaņa varētu izplatīties"], 3),
                ("Cik liels ir elektromagnētiskā viļņa ātrums vakuumā?",
                 ["343 m/s", "1480 m/s", "3,00 · 10⁸ m/s", "5100 m/s"], 2),
                ("Kurš starojums elektromagnētisko viļņu skalā ir "
                 "jonizējošs?",
                 ["radioviļņi", "mikroviļņi", "infrasarkanais starojums",
                  "rentgenstarojums"], 3),
                ("Kāpēc skaņu dzirdam aiz stūra, bet gaismu tur neredzam?",
                 ["skaņa izplatās ātrāk",
                  "skaņas viļņa garums ir daudz lielāks, tāpēc tā vairāk "
                  "liecas ap šķērsli",
                  "gaisma atstarojas no gaisa", "skaņa iet cauri sienai"], 1),
            ],
            "uzdevumi": [
                {"tips": "aprekins", "virs": "Svārstības", "punkti": 4,
                 "vieta": 6.0,
                 "teksts": "Svārsts 30 s laikā veic N = 60 pilnas "
                           "svārstības. Aprēķini svārstību periodu un "
                           "frekvenci!",
                 "risinajums": [
                     "Dots:  t = 30 s;  N = 60",
                     "Jāaprēķina:  T = ?  (s)    f = ?  (Hz)",
                     "Formulas:  T = t / N ;   f = 1 / T",
                     "Aprēķins:  1) T = t / N = 30 s : 60 = 0,5 s",
                     "                   2) f = 1 / T = 1 : 0,5 s = 2 Hz",
                     "Atbilde:  T = 0,5 s;  f = 2 Hz.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas T = t/N un f = 1/T;",
                     "1 p — pareizi aprēķināts T = 0,5 s;",
                     "1 p — pareizi aprēķināts f = 2 Hz un atbilde ar "
                     "mērvienībām (var rēķināt arī f = N/t).",
                 ]},

                {"tips": "aprekins", "virs": "Skaņas viļņa garums",
                 "punkti": 5, "vieta": 7.0,
                 "teksts": "Skaņas frekvence ir f = 686 Hz. Skaņas ātrums "
                           "gaisā ir υ₁ = 343 m/s, bet ūdenī υ₂ = 1480 m/s. "
                           "Aprēķini viļņa garumu gaisā un ūdenī! Kurš "
                           "lielums, skaņai no gaisa pārejot ūdenī, "
                           "nemainās?",
                 "risinajums": [
                     "Dots:  f = 686 Hz;  υ₁ = 343 m/s;  υ₂ = 1480 m/s",
                     "Jāaprēķina:  λ₁ = ?    λ₂ = ?  (m)",
                     "Formulas:  λ = υ / f",
                     "Aprēķins:  1) λ₁ = υ₁ / f = 343 m/s : 686 Hz = 0,50 m",
                     "                   2) λ₂ = υ₂ / f = 1480 m/s : 686 Hz "
                     "≈ 2,16 m",
                     "Atbilde:  λ₁ = 0,50 m;  λ₂ ≈ 2,2 m. Nemainās "
                     "FREKVENCE — to nosaka skaņas avots; mainās ātrums un "
                     "līdz ar to viļņa garums.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīta formula λ = υ / f;",
                     "1 p — pareizi aprēķināts λ₁ = 0,50 m;",
                     "1 p — pareizi aprēķināts λ₂ ≈ 2,2 m;",
                     "1 p — norādīts, ka nemainās frekvence, un uzrakstīta "
                     "atbilde ar mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Eholokācija", "punkti": 5,
                 "vieta": 7.0,
                 "teksts": "Kuģa eholots izstaro ultraskaņas signālu un "
                           "uztver atbalsi pēc t = 0,08 s. Skaņas ātrums "
                           "ūdenī ir υ = 1480 m/s. Aprēķini jūras dziļumu! "
                           "Cik ilgi būtu jāgaida atbalss, ja dziļums būtu "
                           "divreiz lielāks?",
                 "risinajums": [
                     "Dots:  t = 0,08 s;  υ = 1480 m/s",
                     "Jāaprēķina:  s = ?  (m)    t₂ = ?  (s)",
                     "Formulas:  s = υ · t / 2",
                     "Aprēķins:  1) s = 1480 m/s · 0,08 s : 2 = "
                     "118,4 : 2 = 59,2 m",
                     "                   2) ja s₂ = 2s, tad arī laiks aug "
                     "divreiz:  t₂ = 2 · 0,08 s = 0,16 s",
                     "Atbilde:  dziļums s ≈ 59 m;  pie divreiz lielāka "
                     "dziļuma atbalss pienāktu pēc t₂ = 0,16 s.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīta formula s = υ·t/2;",
                     "1 p — saprasts, kāpēc jādala ar 2 (signāls iet turp un "
                     "atpakaļ);",
                     "1 p — pareizi aprēķināts s ≈ 59 m;",
                     "1 p — pareizi noteikts t₂ = 0,16 s un uzrakstīta "
                     "atbilde. Ja skolēns nedala ar 2 un iegūst 118,4 m, "
                     "par 3. un 4. soli punktus nepiešķir.",
                 ]},

                {"tips": "aprekins", "virs": "Elektromagnētiskais vilnis",
                 "punkti": 3, "vieta": 5.5,
                 "teksts": "Wi-Fi raidītājs strādā ar frekvenci "
                           "f = 2,4 GHz. Aprēķini šī viļņa garumu! "
                           "Elektromagnētisko viļņu ātrums vakuumā ir "
                           "c = 3,00 · 10⁸ m/s.",
                 "risinajums": [
                     "Dots:  f = 2,4 GHz;  c = 3,00 · 10⁸ m/s",
                     "Jāaprēķina:  λ = ?  (m)",
                     "Formulas:  λ = c / f",
                     "Aprēķins:  1) f = 2,4 GHz = 2,4 · 10⁹ Hz",
                     "                   2) λ = c / f = 3,00 · 10⁸ m/s : "
                     "(2,4 · 10⁹ Hz) = 0,125 m",
                     "Atbilde:  λ = 0,125 m = 12,5 cm.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula λ = c / f;",
                     "1 p — pareiza pārveide 2,4 GHz = 2,4 · 10⁹ Hz;",
                     "1 p — pareizs λ = 0,125 m = 12,5 cm ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Viļņu īpašības un skala",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem!",
                 "jaut": [
                     ("Kura viļņu īpašība izskaidro gan atbalsi klintī, gan "
                      "attēlu spogulī?", 1),
                     ("Vilnis no gaisa pāriet ūdenī. Kuri lielumi mainās un "
                      "kurš paliek nemainīgs?", 1),
                     ("Kurā elektromagnētisko viļņu skalas diapazonā ir "
                      "robeža starp nejonizējošu un jonizējošu starojumu? "
                      "Kāpēc tieši tur?", 1),
                 ],
                 "atbildes": [
                     "1) Atstarošanās — vilnis atlec no šķēršļa, un krišanas "
                     "leņķis ir vienāds ar atstarošanās leņķi.   (1 p)",
                     "2) Mainās izplatīšanās ātrums un viļņa garums; "
                     "frekvence paliek nemainīga, jo to nosaka avots. Šo "
                     "parādību sauc par laušanu.   (1 p)",
                     "3) Ultravioletajā diapazonā. Fotona enerģija "
                     "E = h · f aug līdz ar frekvenci, un tieši UV apgabalā "
                     "tā kļūst pietiekama, lai izsistu elektronu no atoma "
                     "(jonizētu vielu).   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Ko rāda svārstību periods?",
                 ["svārstību skaitu sekundē",
                  "laiku vienai pilnai svārstībai",
                  "lielāko novirzi no līdzsvara stāvokļa",
                  "viļņa izplatīšanās ātrumu"], 1),
                ("Ja svārstību frekvence ir f = 4 Hz, cik liels ir "
                 "periods?",
                 ["4 s", "0,4 s", "0,25 s", "2,5 s"], 2),
                ("Kurš no minētajiem ir šķērsvilnis?",
                 ["skaņa gaisā", "viļņi uz nostieptas virves",
                  "skaņa ūdenī", "skaņa tēraudā"], 1),
                ("Kas nosaka skaņas skaļumu?",
                 ["amplitūda", "frekvence", "izplatīšanās ātrums",
                  "viļņa garums"], 0),
                ("Kāda ir infraskaņas frekvence?",
                 ["zem 20 Hz", "no 20 Hz līdz 20 kHz", "virs 20 kHz",
                  "virs 1 MHz"], 0),
                ("Kurā vidē skaņa izplatās visātrāk?",
                 ["gaisā", "ūdenī", "tēraudā", "vakuumā"], 2),
                ("Ar ko elektromagnētiskais vilnis atšķiras no mehāniskā?",
                 ["tas izplatās lēnāk", "tam nav frekvences",
                  "tas ir garenvilnis",
                  "tam nav vajadzīga vide — tas izplatās arī vakuumā"], 3),
                ("Kurš diapazons elektromagnētisko viļņu skalā atrodas "
                 "starp mikroviļņiem un redzamo gaismu?",
                 ["radioviļņi", "ultravioletais starojums",
                  "infrasarkanais starojums", "rentgenstarojums"], 2),
                ("Ko izmanto ultrasonogrāfijā?",
                 ["rentgenstarojumu", "gamma starojumu", "infraskaņu",
                  "ultraskaņu"], 3),
                ("Kāpēc ziepju burbulis ir krāsains?",
                 ["laušanas dēļ", "interferences dēļ", "difrakcijas dēļ",
                  "atstarošanās dēļ"], 1),
            ],
            "uzdevumi": [
                {"tips": "aprekins", "virs": "Svārstības", "punkti": 4,
                 "vieta": 6.0,
                 "teksts": "Svārsts 40 s laikā veic N = 100 pilnas "
                           "svārstības. Aprēķini svārstību periodu un "
                           "frekvenci!",
                 "risinajums": [
                     "Dots:  t = 40 s;  N = 100",
                     "Jāaprēķina:  T = ?  (s)    f = ?  (Hz)",
                     "Formulas:  T = t / N ;   f = 1 / T",
                     "Aprēķins:  1) T = t / N = 40 s : 100 = 0,4 s",
                     "                   2) f = 1 / T = 1 : 0,4 s = 2,5 Hz",
                     "Atbilde:  T = 0,4 s;  f = 2,5 Hz.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas T = t/N un f = 1/T;",
                     "1 p — pareizi aprēķināts T = 0,4 s;",
                     "1 p — pareizi aprēķināts f = 2,5 Hz un atbilde ar "
                     "mērvienībām (var rēķināt arī f = N/t).",
                 ]},

                {"tips": "aprekins", "virs": "Skaņas viļņa garums",
                 "punkti": 5, "vieta": 7.0,
                 "teksts": "Skaņas frekvence ir f = 343 Hz. Skaņas ātrums "
                           "gaisā ir υ₁ = 343 m/s, bet tēraudā "
                           "υ₂ = 5100 m/s. Aprēķini viļņa garumu gaisā un "
                           "tēraudā! Kurš lielums, skaņai no gaisa pārejot "
                           "tēraudā, nemainās?",
                 "risinajums": [
                     "Dots:  f = 343 Hz;  υ₁ = 343 m/s;  υ₂ = 5100 m/s",
                     "Jāaprēķina:  λ₁ = ?    λ₂ = ?  (m)",
                     "Formulas:  λ = υ / f",
                     "Aprēķins:  1) λ₁ = υ₁ / f = 343 m/s : 343 Hz = 1,0 m",
                     "                   2) λ₂ = υ₂ / f = 5100 m/s : 343 Hz "
                     "≈ 14,9 m",
                     "Atbilde:  λ₁ = 1,0 m;  λ₂ ≈ 15 m. Nemainās FREKVENCE — "
                     "to nosaka skaņas avots; mainās ātrums un līdz ar to "
                     "viļņa garums.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīta formula λ = υ / f;",
                     "1 p — pareizi aprēķināts λ₁ = 1,0 m;",
                     "1 p — pareizi aprēķināts λ₂ ≈ 15 m;",
                     "1 p — norādīts, ka nemainās frekvence, un uzrakstīta "
                     "atbilde ar mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Eholokācija", "punkti": 5,
                 "vieta": 7.0,
                 "teksts": "Sikspārnis izstaro ultraskaņas signālu un uztver "
                           "atbalsi pēc t = 0,012 s. Skaņas ātrums gaisā ir "
                           "υ = 343 m/s. Aprēķini attālumu līdz šķērslim! "
                           "Cik ilgi būtu jāgaida atbalss, ja šķērslis būtu "
                           "divreiz tuvāk?",
                 "risinajums": [
                     "Dots:  t = 0,012 s;  υ = 343 m/s",
                     "Jāaprēķina:  s = ?  (m)    t₂ = ?  (s)",
                     "Formulas:  s = υ · t / 2",
                     "Aprēķins:  1) s = 343 m/s · 0,012 s : 2 = "
                     "4,116 : 2 ≈ 2,1 m",
                     "                   2) ja s₂ = s/2, tad arī laiks "
                     "samazinās divreiz:  t₂ = 0,012 s : 2 = 0,006 s",
                     "Atbilde:  attālums s ≈ 2,1 m;  pie divreiz tuvāka "
                     "šķēršļa atbalss pienāktu pēc t₂ = 0,006 s.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīta formula s = υ·t/2;",
                     "1 p — saprasts, kāpēc jādala ar 2 (signāls iet turp un "
                     "atpakaļ);",
                     "1 p — pareizi aprēķināts s ≈ 2,1 m;",
                     "1 p — pareizi noteikts t₂ = 0,006 s un uzrakstīta "
                     "atbilde. Ja skolēns nedala ar 2 un iegūst 4,1 m, par "
                     "3. un 4. soli punktus nepiešķir.",
                 ]},

                {"tips": "aprekins", "virs": "Elektromagnētiskais vilnis",
                 "punkti": 3, "vieta": 5.5,
                 "teksts": "FM radio raidītājs strādā ar frekvenci "
                           "f = 100 MHz. Aprēķini šī viļņa garumu! "
                           "Elektromagnētisko viļņu ātrums vakuumā ir "
                           "c = 3,00 · 10⁸ m/s.",
                 "risinajums": [
                     "Dots:  f = 100 MHz;  c = 3,00 · 10⁸ m/s",
                     "Jāaprēķina:  λ = ?  (m)",
                     "Formulas:  λ = c / f",
                     "Aprēķins:  1) f = 100 MHz = 1,00 · 10⁸ Hz",
                     "                   2) λ = c / f = 3,00 · 10⁸ m/s : "
                     "(1,00 · 10⁸ Hz) = 3,0 m",
                     "Atbilde:  λ = 3,0 m.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula λ = c / f;",
                     "1 p — pareiza pārveide 100 MHz = 1,00 · 10⁸ Hz;",
                     "1 p — pareizs λ = 3,0 m ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Viļņu īpašības un skala",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem!",
                 "jaut": [
                     ("Kura viļņu īpašība izskaidro, kāpēc salmiņš ūdens "
                      "glāzē izskatās saliekts?", 1),
                     ("Kāpēc medicīnas attēlveidošanā izmanto ultraskaņu, "
                      "nevis dzirdamo skaņu?", 1),
                     ("Nosauc divus nejonizējošus un divus jonizējošus "
                      "elektromagnētisko viļņu skalas diapazonus!", 1),
                 ],
                 "atbildes": [
                     "1) Laušana — pārejot citā vidē, mainās viļņa ātrums, "
                     "un vilnis maina virzienu.   (1 p)",
                     "2) Ultraskaņai ir daudz īsāks viļņa garums, tāpēc tā "
                     "dod labāku izšķirtspēju — var saskatīt sīkākas "
                     "detaļas. Turklāt tā nav jonizējoša, tāpēc izmeklējums "
                     "ir drošs.   (1 p)",
                     "3) Nejonizējoši (divi no): radioviļņi, mikroviļņi, "
                     "infrasarkanais starojums, redzamā gaisma. Jonizējoši "
                     "(divi no): UV (daļēji), rentgenstarojums, gamma "
                     "starojums.   (1 p)",
                 ]},
            ],
        },
    ],
}
