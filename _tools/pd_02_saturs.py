# -*- coding: utf-8 -*-
"""PD2 — Atoma uzbūve, radioaktivitāte un vielas uzbūve (3.1.–3.12. stunda)."""

PD = {
    "nr": 2,
    "nosaukums": "Atoma uzbūve, radioaktivitāte un vielas uzbūve",
    "mape": "3. Atoma uzbūve, vielas uzbūve, vielas stāvokļi",
    "fails": "PD2. Atoma uzbūve, radioaktivitāte un vielas uzbūve",
    "stundas": "3.1.–3.12.",
    "datums": "16.10.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda atoma un kodola uzbūvi, izotopus, "
                "kodolreakcijas, radioaktivitāti un pussabrukšanu, "
                "starojuma drošību, vielas daudzumu un kristālrežģus.",
    "atgadne": [
        "N = A − Z   ·   Ar = (A₁ · w₁ + A₂ · w₂) / 100 %",
        "N = N₀ / 2ⁿ   ·   A = A₀ / 2ⁿ   ·   n = t / T",
        "n = m / M = N / N_A   ·   N_A = 6,02 · 10²³ mol⁻¹",
        "D = P · t   ·   P₁ · r₁² = P₂ · r₂²   ·   E = hf   ·   "
        "h = 6,63 · 10⁻³⁴ J·s   ·   c = 3,00 · 10⁸ m/s",
    ],
    "struktura": [
        ("1.", "Raksturo atoma un kodola uzbūvi, izotopus, starojuma veidus, "
               "pussabrukšanu, vielas daudzumu un kristālrežģus", "3.1.–3.12.",
         10),
        ("2.", "Nosaka protonu, neitronu un elektronu skaitu pēc A un Z; "
               "aprēķina relatīvo atommasu", "3.1., 3.2.", 5),
        ("3.", "Papildina kodolreakciju vienādojumus, lietojot masas un "
               "lādiņa nezūdamības likumus", "3.4.", 3),
        ("4.", "Aprēķina atlikušo kodolu skaitu vai aktivitāti pēc "
               "pussabrukšanas periodiem", "3.6.", 5),
        ("5.", "Aprēķina vielas daudzumu un daļiņu skaitu", "3.10.", 4),
        ("6.", "Lieto attāluma kvadrāta likumu, izvēlas ekrānu un nosaka "
               "kristālrežģa veidu pēc īpašībām", "3.5., 3.8., 3.11.", 3),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Cik neitronu ir dzelzs kodolā ⁵⁶Fe (Z = 26)?",
                 ["26", "30", "56", "82"], 1),
                ("Ar ko izotopi ir līdzīgi un ar ko atšķiras?",
                 ["vienāds protonu skaits, bet atšķirīgs neitronu skaits",
                  "vienāds neitronu skaits, bet atšķirīgs protonu skaits",
                  "atšķirīgs elektronu skaits neitrālā atomā",
                  "atšķirīgs kārtas skaitlis Z"], 0),
                ("Kas ir alfa daļiņa?",
                 ["ātrs elektrons", "hēlija kodols",
                  "elektromagnētiskais starojums", "neitronu plūsma"], 1),
                ("Kuram starojumam ir vislielākā caurspiešanās spēja?",
                 ["alfa", "bēta", "gamma", "visiem vienāda"], 2),
                ("Bēta sabrukšanā kodola masas skaitlis A",
                 ["palielinās par 1", "samazinās par 4", "samazinās par 1",
                  "nemainās"], 3),
                ("Cik liela daļa vielas ir palikusi pēc diviem "
                 "pussabrukšanas periodiem?",
                 ["1/2", "1/4", "1/8", "nekas nav palicis"], 1),
                ("Kura ir aktivitātes mērvienība?",
                 ["grejs (Gy)", "sīverts (Sv)", "kulons (C)",
                  "bekerels (Bq)"], 3),
                ("Kurš aizsardzības paņēmiens ir vienkāršākais un lētākais?",
                 ["ekranēšana ar svinu", "aizsargbrilles",
                  "attāluma palielināšana",
                  "uzturēšanās laika pagarināšana"], 2),
                ("Cik daļiņu ir vienā molā vielas?",
                 ["6,02 · 10²³", "3,00 · 10⁸", "6,63 · 10⁻³⁴",
                  "1,67 · 10⁻²⁷"], 0),
                ("Kura no vielām ir amorfa?",
                 ["galda sāls", "dzelzs", "stikls", "ledus"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Atoma sastāvs", "punkti": 5,
                 "note": "Aizpildi trūkstošo! Par katru pareizu rindu — "
                         "1 punkts.",
                 "rindas": [
                     ("¹⁴N  (Z = 7, A = 14):   protoni ......   "
                      "neitroni ......   elektroni ......",
                      "p = 7;  n = 7;  e = 7"),
                     ("²³Na  (Z = 11, A = 23):   protoni ......   "
                      "neitroni ......   elektroni ......",
                      "p = 11;  n = 12;  e = 11"),
                     ("²³⁸U  (Z = 92, A = 238):   protoni ......   "
                      "neitroni ......   elektroni ......",
                      "p = 92;  n = 146;  e = 92"),
                     ("Nosauc daļiņas, kas atrodas atoma kodolā, un to "
                      "lādiņus:  ..........................................",
                      "protons (lādiņš +1) un neitrons (lādiņa nav, 0)"),
                     ("Hloram dabā ir ³⁵Cl (75 %) un ³⁷Cl (25 %). Aprēķini "
                      "relatīvo atommasu Ar =  ......",
                      "Ar = (35 · 75 + 37 · 25) / 100 = 3550 / 100 = 35,5"),
                 ],
                 "kriterijs": "Ceturtajā rindā punktu piešķir, ja nosauktas "
                              "abas daļiņas ar pareiziem lādiņiem; piektajā — "
                              "ja parādīts aprēķins un iegūts 35,5."},

                {"tips": "jautajumi", "virs": "Kodolreakciju vienādojumi",
                 "punkti": 3, "vieta": 5.0,
                 "ievads": "Papildini kodolreakciju vienādojumus! Izmanto "
                           "masas skaitļu un lādiņu nezūdamības likumus — "
                           "abām vienādojuma pusēm summām jāsakrīt.",
                 "jaut": [("²³⁸₉₂U → ⁴₂He + ?", 1),
                          ("¹⁴₆C → ⁰₋₁e + ?", 1),
                          ("²³⁵₉₂U + ¹₀n → ¹⁴¹₅₆Ba + ? + 3 ¹₀n", 1)],
                 "atbildes": [
                     "1) A: 238 = 4 + 234;  Z: 92 = 2 + 90  →  ²³⁴₉₀Th "
                     "(torijs).   (1 p)",
                     "2) A: 14 = 0 + 14;  Z: 6 = −1 + 7  →  ¹⁴₇N (slāpeklis). "
                     "Bēta sabrukšanā A nemainās, Z palielinās par 1.   (1 p)",
                     "3) A: 235 + 1 = 141 + A + 3;  Z: 92 = 56 + Z  →  "
                     "⁹²₃₆Kr (kriptons).   (1 p)",
                 ]},

                {"tips": "aprekins", "virs": "Pussabrukšanas periods",
                 "punkti": 5, "vieta": 7.0,
                 "teksts": "Joda-131 pussabrukšanas periods ir T = 8 dienas. "
                           "Sākumā paraugā bija N₀ = 4,8 · 10²⁰ kodolu. Cik "
                           "kodolu paliks pēc t = 32 dienām? Cik procentu no "
                           "sākotnējā daudzuma tas ir?",
                 "risinajums": [
                     "Dots:  T = 8 d;  N₀ = 4,8 · 10²⁰;  t = 32 d",
                     "Jāaprēķina:  N = ?    N/N₀ = ?  (%)",
                     "Formulas:  n = t / T ;   N = N₀ / 2ⁿ",
                     "Aprēķins:  1) n = t / T = 32 d : 8 d = 4",
                     "                   2) 2ⁿ = 2⁴ = 16",
                     "                   3) N = N₀ / 2ⁿ = 4,8 · 10²⁰ : 16 = "
                     "3,0 · 10¹⁹",
                     "                   4) N / N₀ · 100 % = 1/16 · 100 % = "
                     "6,25 %",
                     "Atbilde:  N = 3,0 · 10¹⁹ kodolu, kas ir 6,25 % no "
                     "sākotnējā daudzuma.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas n = t / T un N = N₀ / 2ⁿ;",
                     "1 p — pareizi noteikts periodu skaits n = 4;",
                     "1 p — pareizi aprēķināts N = 3,0 · 10¹⁹;",
                     "1 p — noteikti 6,25 % un uzrakstīta atbilde. "
                     "Ja skolēns rēķina «pusi no sākuma» un iegūst 0 vai "
                     "50 %, par 3.–5. soli punktus nepiešķir.",
                 ]},

                {"tips": "aprekins", "virs": "Vielas daudzums un daļiņu skaits",
                 "punkti": 4, "vieta": 6.0,
                 "teksts": "Aprēķini, cik molekulu ir ūdens paraugā, kura "
                           "masa ir m = 90 g! M(H₂O) = 18 g/mol, "
                           "N_A = 6,02 · 10²³ mol⁻¹.",
                 "risinajums": [
                     "Dots:  m = 90 g;  M = 18 g/mol;  "
                     "N_A = 6,02 · 10²³ mol⁻¹",
                     "Jāaprēķina:  N = ?",
                     "Formulas:  n = m / M ;   N = n · N_A",
                     "Aprēķins:  1) n = m / M = 90 g : 18 g/mol = 5 mol",
                     "                   2) N = n · N_A = 5 mol · "
                     "6,02 · 10²³ mol⁻¹ = 3,01 · 10²⁴",
                     "Atbilde:  N ≈ 3,0 · 10²⁴ molekulu.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas n = m / M un N = n · N_A;",
                     "1 p — pareizi aprēķināts n = 5 mol;",
                     "1 p — pareizs N ≈ 3,0 · 10²⁴ un atbilde.",
                 ]},

                {"tips": "jautajumi", "virs": "Drošība un vielas uzbūve",
                 "punkti": 3, "vieta": 5.5,
                 "ievads": "Atbildi uz jautājumiem! Pirmajā jautājumā parādi "
                           "aprēķinu.",
                 "jaut": [
                     ("Dozimetrs 2 m attālumā no punktveida avota rāda devas "
                      "jaudu P₁ = 36 µSv/h. Cik liela devas jauda būs 6 m "
                      "attālumā?", 1),
                     ("Nosauc materiālu, ar ko aptur bēta starojumu, un "
                      "materiālu, ar ko aptur gamma starojumu!", 1),
                     ("Viela ir cieta un trausla, cietā veidā strāvu nevada, "
                      "bet kausējumā vada. Kāds ir tās kristālrežģa veids?",
                      1),
                 ],
                 "atbildes": [
                     "1) P₁ · r₁² = P₂ · r₂²  →  P₂ = P₁ · r₁² / r₂² = "
                     "36 µSv/h · (2 m)² : (6 m)² = 36 · 4 : 36 = 4 µSv/h. "
                     "Attālinoties 3 reizes, devas jauda samazinās 9 reizes.  "
                     " (1 p)",
                     "2) Bēta starojumu aptur alumīnija plāksne; gamma "
                     "starojumu — biezs svina vai betona slānis.   (1 p)",
                     "3) Jonu kristālrežģis (piemēram, NaCl) — mezglos ir "
                     "joni, kas kļūst kustīgi tikai kausējumā vai šķīdumā.   "
                     "(1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Cik neitronu ir alumīnija kodolā ²⁷Al (Z = 13)?",
                 ["13", "14", "27", "40"], 1),
                ("Ar ko atšķiras viena elementa izotopi?",
                 ["ar protonu skaitu", "ar neitronu skaitu",
                  "ar ķīmiskajām īpašībām", "ar kārtas skaitli Z"], 1),
                ("Kas ir bēta daļiņa?",
                 ["hēlija kodols", "fotons", "ātrs elektrons", "protons"], 2),
                ("Kuru starojumu aptur jau papīra lapa?",
                 ["alfa", "bēta", "gamma", "rentgenstarojumu"], 0),
                ("Alfa sabrukšanā kodola kārtas skaitlis Z",
                 ["nemainās", "samazinās par 2", "palielinās par 1",
                  "samazinās par 4"], 1),
                ("Cik liela daļa vielas ir palikusi pēc trim pussabrukšanas "
                 "periodiem?",
                 ["1/3", "1/6", "1/8", "1/9"], 2),
                ("Kura ir apstarošanas devas mērvienība?",
                 ["bekerels (Bq)", "vats (W)", "mols (mol)",
                  "sīverts (Sv)"], 3),
                ("Attālinoties no punktveida avota divas reizes, devas jauda",
                 ["samazinās 2 reizes", "palielinās 2 reizes", "nemainās",
                  "samazinās 4 reizes"], 3),
                ("Cik liela ir ūdens molmasa M(H₂O)?",
                 ["18 g/mol", "20 g/mol", "32 g/mol", "44 g/mol"], 0),
                ("Kurai vielai ir metāliskais kristālrežģis?",
                 ["dimantam", "varam", "galda sālim", "ledum"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Atoma sastāvs", "punkti": 5,
                 "note": "Aizpildi trūkstošo! Par katru pareizu rindu — "
                         "1 punkts.",
                 "rindas": [
                     ("¹⁶O  (Z = 8, A = 16):   protoni ......   "
                      "neitroni ......   elektroni ......",
                      "p = 8;  n = 8;  e = 8"),
                     ("³¹P  (Z = 15, A = 31):   protoni ......   "
                      "neitroni ......   elektroni ......",
                      "p = 15;  n = 16;  e = 15"),
                     ("²³⁵U  (Z = 92, A = 235):   protoni ......   "
                      "neitroni ......   elektroni ......",
                      "p = 92;  n = 143;  e = 92"),
                     ("Nosauc daļiņu, kas atrodas ap kodolu, un tās lādiņu:  "
                      "..........................................",
                      "elektrons (lādiņš −1)"),
                     ("Varam dabā ir ⁶³Cu (69 %) un ⁶⁵Cu (31 %). Aprēķini "
                      "relatīvo atommasu Ar =  ......",
                      "Ar = (63 · 69 + 65 · 31) / 100 = 6362 / 100 = 63,62 "
                      "≈ 63,6"),
                 ],
                 "kriterijs": "Ceturtajā rindā punktu piešķir, ja nosaukta "
                              "daļiņa un tās lādiņš; piektajā — ja parādīts "
                              "aprēķins un iegūts 63,6."},

                {"tips": "jautajumi", "virs": "Kodolreakciju vienādojumi",
                 "punkti": 3, "vieta": 5.0,
                 "ievads": "Papildini kodolreakciju vienādojumus! Izmanto "
                           "masas skaitļu un lādiņu nezūdamības likumus — "
                           "abām vienādojuma pusēm summām jāsakrīt.",
                 "jaut": [("²²⁶₈₈Ra → ⁴₂He + ?", 1),
                          ("⁴⁰₁₉K → ⁰₋₁e + ?", 1),
                          ("²₁H + ³₁H → ⁴₂He + ?", 1)],
                 "atbildes": [
                     "1) A: 226 = 4 + 222;  Z: 88 = 2 + 86  →  ²²²₈₆Rn "
                     "(radons).   (1 p)",
                     "2) A: 40 = 0 + 40;  Z: 19 = −1 + 20  →  ⁴⁰₂₀Ca "
                     "(kalcijs).   (1 p)",
                     "3) A: 2 + 3 = 4 + 1;  Z: 1 + 1 = 2 + 0  →  ¹₀n "
                     "(neitrons). Tā ir kodolsintēze, kas notiek zvaigznēs.   "
                     "(1 p)",
                 ]},

                {"tips": "aprekins", "virs": "Pussabrukšanas periods",
                 "punkti": 5, "vieta": 7.0,
                 "teksts": "Cēzija-137 pussabrukšanas periods ir T = 30 gadi. "
                           "Sākumā parauga aktivitāte bija "
                           "A₀ = 6,4 · 10⁵ Bq. Cik liela būs aktivitāte pēc "
                           "t = 120 gadiem? Cik procentu no sākotnējās "
                           "aktivitātes tas ir?",
                 "risinajums": [
                     "Dots:  T = 30 gadi;  A₀ = 6,4 · 10⁵ Bq;  t = 120 gadi",
                     "Jāaprēķina:  A = ?  (Bq)    A/A₀ = ?  (%)",
                     "Formulas:  n = t / T ;   A = A₀ / 2ⁿ",
                     "Aprēķins:  1) n = t / T = 120 gadi : 30 gadi = 4",
                     "                   2) 2ⁿ = 2⁴ = 16",
                     "                   3) A = A₀ / 2ⁿ = 6,4 · 10⁵ Bq : 16 = "
                     "4,0 · 10⁴ Bq",
                     "                   4) A / A₀ · 100 % = 1/16 · 100 % = "
                     "6,25 %",
                     "Atbilde:  A = 4,0 · 10⁴ Bq, kas ir 6,25 % no sākotnējās "
                     "aktivitātes.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas n = t / T un A = A₀ / 2ⁿ;",
                     "1 p — pareizi noteikts periodu skaits n = 4;",
                     "1 p — pareizi aprēķināts A = 4,0 · 10⁴ Bq ar "
                     "mērvienību;",
                     "1 p — noteikti 6,25 % un uzrakstīta atbilde. "
                     "Ja skolēns rēķina «pusi no sākuma», par 3.–5. soli "
                     "punktus nepiešķir.",
                 ]},

                {"tips": "aprekins", "virs": "Vielas daudzums un daļiņu skaits",
                 "punkti": 4, "vieta": 6.0,
                 "teksts": "Aprēķini, cik molekulu ir oglekļa dioksīda "
                           "paraugā, kura masa ir m = 88 g! "
                           "M(CO₂) = 44 g/mol, N_A = 6,02 · 10²³ mol⁻¹.",
                 "risinajums": [
                     "Dots:  m = 88 g;  M = 44 g/mol;  "
                     "N_A = 6,02 · 10²³ mol⁻¹",
                     "Jāaprēķina:  N = ?",
                     "Formulas:  n = m / M ;   N = n · N_A",
                     "Aprēķins:  1) n = m / M = 88 g : 44 g/mol = 2 mol",
                     "                   2) N = n · N_A = 2 mol · "
                     "6,02 · 10²³ mol⁻¹ = 1,204 · 10²⁴",
                     "Atbilde:  N ≈ 1,2 · 10²⁴ molekulu.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas n = m / M un N = n · N_A;",
                     "1 p — pareizi aprēķināts n = 2 mol;",
                     "1 p — pareizs N ≈ 1,2 · 10²⁴ un atbilde.",
                 ]},

                {"tips": "jautajumi", "virs": "Drošība un vielas uzbūve",
                 "punkti": 3, "vieta": 5.5,
                 "ievads": "Atbildi uz jautājumiem! Pirmajā jautājumā parādi "
                           "aprēķinu.",
                 "jaut": [
                     ("Dozimetrs 1 m attālumā no punktveida avota rāda devas "
                      "jaudu P₁ = 45 µSv/h. Cik liela devas jauda būs 3 m "
                      "attālumā?", 1),
                     ("Ar ko apstarošana atšķiras no radioaktīvā "
                      "piesārņojuma?", 1),
                     ("Viela kūst ļoti augstā temperatūrā, ir ļoti cieta un "
                      "strāvu nevada. Kāds ir tās kristālrežģa veids?", 1),
                 ],
                 "atbildes": [
                     "1) P₁ · r₁² = P₂ · r₂²  →  P₂ = P₁ · r₁² / r₂² = "
                     "45 µSv/h · (1 m)² : (3 m)² = 45 : 9 = 5 µSv/h.   (1 p)",
                     "2) Apstarošanas laikā cilvēks atrodas starojuma laukā, "
                     "bet pats nekļūst radioaktīvs — aizejot no avota, "
                     "apstarošana beidzas. Piesārņojuma gadījumā radioaktīva "
                     "viela nokļūst uz ķermeņa vai iekšā, un starojums "
                     "turpinās arī pēc aiziešanas; viela jānomazgā.   (1 p)",
                     "3) Atomu kristālrežģis (piemēram, dimants vai kvarcs).  "
                     " (1 p)",
                 ]},
            ],
        },
    ],
}
