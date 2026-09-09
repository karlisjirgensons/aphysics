# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. PD5 - Gravitācijas lauks un kustība (67.-82. st.)."""

PD = {
    "nr": 5,
    "klase": "10. klase",
    "nosaukums": "Gravitācijas lauks un kustība",
    "mape": "4. Gravitācijas lauks un kustība",
    "fails": "PD5. Gravitācijas lauks un kustība_tt",
    "stundas": "67.-81.",
    "datums": "14.04.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda vispasaules gravitācijas likumu, "
                "gravitācijas lauka intensitāti, kustību orbītā, pirmo "
                "kosmisko ātrumu un Keplera trešo likumu.",
    "atgadne": [
        "F = G·m₁m₂ / r²   ·   G = 6,67 · 10⁻¹¹ N·m²/kg²",
        "g = F / m = G·M / r²   ·   v = √(G·M / r)   ·   T² / a³ = const",
        "Zeme:  M = 5,97 · 10²⁴ kg;  R = 6,37 · 10⁶ m;  g = 9,8 m/s²",
        "Ep = mgh (tuvu Zemei)   ·   a(centrt.) = v² / r = 4π²r / T²",
    ],
    "struktura": [
        ("1.", "Skaidro gravitācijas lauku, orbītas kustību un svara "
               "izmaiņas", "67.-80.", 10),
        ("2.", "Aizpilda gravitācijas lielumu tabulu", "67.-70.", 5),
        ("3.", "Lieto vispasaules gravitācijas likumu", "67., 70.", 5),
        ("4.", "Aprēķina lauka intensitāti vai kosmisko ātrumu",
         "68., 72.", 5),
        ("5.", "Analizē orbītas datus un lieto Keplera trešo likumu",
         "73.-75.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kā mainās gravitācijas spēks, ja attālumu starp ķermeņiem "
                 "palielina 3 reizes?",
                 ["samazinās 3 reizes", "samazinās 9 reizes",
                  "palielinās 3 reizes", "palielinās 9 reizes"], 1),
                ("Ko raksturo gravitācijas lauka intensitāte g?",
                 ["ķermeņa masu", "spēku uz masas vienību",
                  "lauka enerģiju", "ķermeņa svaru"], 1),
                ("Kāda ir gravitācijas lauka intensitātes SI mērvienība?",
                 ["N", "N/kg", "N·m", "kg/N"], 1),
                ("Kas notur pavadoni orbītā?",
                 ["dzinēju vilce", "gaisa pretestība",
                  "gravitācijas spēks", "centrbēdzes spēks"], 2),
                ("Kāds ir pirmais kosmiskais ātrums Zemei?",
                 ["1,0 km/s", "7,9 km/s", "11,2 km/s", "300 000 km/s"], 1),
                ("Uz planētas ar divreiz lielāku masu un tādu pašu rādiusu "
                 "kā Zemei g būtu:",
                 ["divreiz mazāks", "tāds pats", "divreiz lielāks",
                  "četrreiz lielāks"], 2),
                ("Ģeostacionāra pavadoņa apriņķošanas periods ir:",
                 ["1 stunda", "12 stundas", "24 stundas", "1 mēnesis"], 2),
                ("Ko nosaka Keplera trešais likums?",
                 ["planētas masu", "orbītas perioda un rādiusa saistību",
                  "planētas temperatūru", "gravitācijas konstanti"], 1),
                ("Kāpēc kosmonauts orbītā atrodas bezsvara stāvoklī?",
                 ["tur nav gravitācijas",
                  "viņš kopā ar kuģi brīvi krīt ap Zemi",
                  "viņa masa kļūst nulle",
                  "viņu notur gaiss"], 1),
                ("Lifts kustas augšup ar paātrinājumu. Kā mainās cilvēka "
                 "svars?",
                 ["palielinās", "samazinās", "nemainās", "kļūst nulle"], 0),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Gravitācijas lielumi",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai nosaukumu! Par katru "
                         "pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Gravitācijas konstantes vērtība  G = ..............."
                      "...... ", "6,67 · 10⁻¹¹ N·m²/kg²"),
                     ("Lauka intensitāte uz Zemes virsmas  g ≈ ..........."
                      ".......... N/kg", "9,8 N/kg"),
                     ("Ķermeņa svars uz Mēness, ja tur g = 1,6 N/kg un "
                      "m = 60 kg  P = ..................... N", "96 N"),
                     ("Zemes rādiuss  R ≈ ..................... m",
                      "6,37 · 10⁶ m"),
                     ("Ep 2,0 kg smagam ķermenim 5,0 m augstumā "
                      "(g = 10 m/s²)  Ep = ..................... J", "100 J"),
                 ]},

                {"tips": "aprekins", "virs": "Vispasaules gravitācijas likums",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Divas 2000 kg un 1500 kg smagas kravas mašīnas "
                           "atrodas 10 m attālumā viena no otras. Aprēķini "
                           "gravitācijas spēku starp tām! Salīdzini to ar "
                           "vieglākās mašīnas smaguma spēku (g = 10 m/s²).",
                 "risinajums": [
                     "Dots:  m₁ = 2000 kg;  m₂ = 1500 kg;  r = 10 m;  "
                     "G = 6,67 · 10⁻¹¹ N·m²/kg²",
                     "Jāaprēķina:  F = ?",
                     "Formulas:  F = G·m₁m₂ / r²;  Fs = m₂g",
                     "Aprēķins:  1) m₁m₂ = 2000 · 1500 = 3,0 · 10⁶ kg²",
                     "                   2) F = 6,67 · 10⁻¹¹ · 3,0 · 10⁶ : "
                     "100",
                     "                   3) F = 2,0 · 10⁻⁶ N",
                     "                   4) Fs = 1500 · 10 = 1,5 · 10⁴ N",
                     "Atbilde:  F ≈ 2,0 · 10⁻⁶ N - apmēram 10¹⁰ reižu mazāks "
                     "par smaguma spēku, tāpēc ikdienā to nemana.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» un «Jāaprēķina»;",
                     "1 p - pierakstīta formula F = G·m₁m₂/r²;",
                     "2 p - pareizs aprēķins standartformā ar mērvienību;",
                     "1 p - pamatots salīdzinājums ar smaguma spēku.",
                 ]},

                {"tips": "aprekins", "virs": "Lauka intensitāte uz planētas",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Marsa masa ir M = 6,4 · 10²³ kg, bet rādiuss "
                           "R = 3,4 · 10⁶ m. Aprēķini gravitācijas lauka "
                           "intensitāti uz Marsa virsmas un 60 kg smaga "
                           "cilvēka svaru uz Marsa!",
                 "risinajums": [
                     "Dots:  M = 6,4 · 10²³ kg;  R = 3,4 · 10⁶ m;  m = 60 kg",
                     "Jāaprēķina:  g = ?  P = ?",
                     "Formulas:  g = G·M / R²;  P = mg",
                     "Aprēķins:  1) R² = (3,4 · 10⁶)² = 1,16 · 10¹³ m²",
                     "                   2) g = 6,67 · 10⁻¹¹ · 6,4 · 10²³ : "
                     "1,16 · 10¹³",
                     "                   3) g ≈ 3,7 N/kg",
                     "                   4) P = 60 · 3,7 ≈ 2,2 · 10² N",
                     "Atbilde:  g ≈ 3,7 N/kg;  P ≈ 220 N (uz Zemes būtu "
                     "≈ 590 N).",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» ar skaitļiem standartformā;",
                     "1 p - pierakstīta formula g = G·M / R²;",
                     "2 p - pareizs g ≈ 3,7 N/kg ar mērvienību;",
                     "1 p - pareizi aprēķināts svars uz Marsa.",
                 ]},

                {"tips": "jautajumi", "virs": "Pavadonis orbītā",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Mākslīgais pavadonis riņķo ap Zemi apļveida "
                           "orbītā r = 7,0 · 10⁶ m attālumā no Zemes centra. "
                           "Zemes masa M = 5,97 · 10²⁴ kg.",
                 "jaut": [
                     ("Pieraksti formulu, kas saista gravitācijas spēku ar "
                      "centrtieces paātrinājumu!", 1),
                     ("Aprēķini pavadoņa ātrumu orbītā!", 1),
                     ("Aprēķini apriņķošanas periodu T!", 1),
                     ("Pamato, vai pavadonis ar lielāku masu lidotu ar citu "
                      "ātrumu!", 1),
                     ("Divām planētām lielo pusasu attiecība ir 4:1. Cik "
                      "reižu atšķiras to apriņķošanas periodi?", 1),
                 ],
                 "atbildes": [
                     "1) G·Mm / r² = mv² / r, no kurienes v = √(G·M / r).   "
                     "(1 p)",
                     "2) v = √(6,67 · 10⁻¹¹ · 5,97 · 10²⁴ : 7,0 · 10⁶) = "
                     "√(5,69 · 10⁷) ≈ 7,5 · 10³ m/s = 7,5 km/s.   (1 p)",
                     "3) T = 2πr / v = 2 · 3,14 · 7,0 · 10⁶ : 7,5 · 10³ ≈ "
                     "5,9 · 10³ s ≈ 98 min.   (1 p)",
                     "4) Nē. Pavadoņa masa m izīsinās, tāpēc ātrums ir "
                     "atkarīgs tikai no Zemes masas un orbītas rādiusa.   "
                     "(1 p)",
                     "5) T² ~ a³, tātad T attiecība = 4^(3/2) = 8 reizes.   "
                     "(1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kā mainās gravitācijas spēks, ja attālumu samazina "
                 "2 reizes?",
                 ["samazinās 2 reizes", "palielinās 2 reizes",
                  "palielinās 4 reizes", "nemainās"], 2),
                ("Kā aprēķina gravitācijas lauka intensitāti?",
                 ["g = mF", "g = F / m", "g = F·m", "g = m / F"], 1),
                ("Kas ir gravitācijas konstante G?",
                 ["mainīgs lielums", "vienāds ar 9,8",
                  "universāla konstante 6,67 · 10⁻¹¹ N·m²/kg²",
                  "atkarīga no planētas"], 2),
                ("Kas notiktu ar pavadoni, ja gravitācija pēkšņi pazustu?",
                 ["tas kristu uz Zemi",
                  "tas turpinātu kustību pa taisni",
                  "tas apstātos", "tas riņķotu tāpat"], 1),
                ("Kāds ir otrais kosmiskais ātrums Zemei?",
                 ["7,9 km/s", "9,8 km/s", "11,2 km/s", "16,7 km/s"], 2),
                ("Uz planētas ar tādu pašu masu kā Zemei, bet divreiz "
                 "lielāku rādiusu, g būtu:",
                 ["divreiz lielāks", "divreiz mazāks",
                  "četrreiz mazāks", "tāds pats"], 2),
                ("Ģeostacionārs pavadonis atrodas virs:",
                 ["Ziemeļpola", "ekvatora", "Dienvidpola",
                  "jebkuras vietas"], 1),
                ("Keplera pirmais likums nosaka, ka planētu orbītas ir:",
                 ["riņķa līnijas", "elipses ar Sauli fokusā",
                  "parabolas", "taisnes"], 1),
                ("Cilvēks liftā, kas brīvi krīt, izjūt:",
                 ["divkāršu svaru", "parasto svaru", "bezsvara stāvokli",
                  "pārslodzi"], 2),
                ("Cik liels darbs jāveic, lai 10 kg smagu ķermeni paceltu "
                 "3,0 m augstumā (g = 10 m/s²)?",
                 ["30 J", "300 J", "3,0 J", "3000 J"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Gravitācijas lielumi",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai nosaukumu! Par katru "
                         "pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Gravitācijas konstantes mērvienība  [G] = ........."
                      "............", "N·m²/kg²"),
                     ("Pirmais kosmiskais ātrums Zemei  v ≈ ..............."
                      "...... km/s", "7,9 km/s"),
                     ("Ķermeņa svars uz Marsa, ja g = 3,7 N/kg un m = 80 kg "
                      " P = ..................... N", "296 N ≈ 3,0 · 10² N"),
                     ("Zemes masa  M ≈ ..................... kg",
                      "5,97 · 10²⁴ kg"),
                     ("Ep 5,0 kg smagam ķermenim 4,0 m augstumā "
                      "(g = 10 m/s²)  Ep = ..................... J", "200 J"),
                 ]},

                {"tips": "aprekins", "virs": "Vispasaules gravitācijas likums",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Aprēķini gravitācijas spēku starp Zemi "
                           "(M = 5,97 · 10²⁴ kg) un 1200 kg smagu satelītu, "
                           "kas atrodas r = 8,0 · 10⁶ m attālumā no Zemes "
                           "centra! Salīdzini rezultātu ar satelīta svaru uz "
                           "Zemes virsmas (g = 9,8 m/s²).",
                 "risinajums": [
                     "Dots:  M = 5,97 · 10²⁴ kg;  m = 1200 kg;  "
                     "r = 8,0 · 10⁶ m",
                     "Jāaprēķina:  F = ?",
                     "Formulas:  F = G·Mm / r²;  P = mg",
                     "Aprēķins:  1) r² = 6,4 · 10¹³ m²",
                     "                   2) F = 6,67 · 10⁻¹¹ · 5,97 · 10²⁴ · "
                     "1200 : 6,4 · 10¹³",
                     "                   3) F ≈ 7,5 · 10³ N",
                     "                   4) P = 1200 · 9,8 ≈ 1,2 · 10⁴ N",
                     "Atbilde:  F ≈ 7,5 kN; tas ir mazāks nekā uz virsmas "
                     "(≈ 12 kN), jo attālums no centra ir lielāks.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» un «Jāaprēķina»;",
                     "1 p - pierakstīta formula F = G·Mm/r²;",
                     "2 p - pareizs aprēķins standartformā ar mērvienību;",
                     "1 p - pamatots salīdzinājums ar svaru uz virsmas.",
                 ]},

                {"tips": "aprekins", "virs": "Pirmais kosmiskais ātrums",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Aprēķini pirmo kosmisko ātrumu Mēnesim, ja tā "
                           "masa M = 7,35 · 10²² kg un rādiuss "
                           "R = 1,74 · 10⁶ m! Salīdzini to ar Zemes pirmo "
                           "kosmisko ātrumu 7,9 km/s.",
                 "risinajums": [
                     "Dots:  M = 7,35 · 10²² kg;  R = 1,74 · 10⁶ m",
                     "Jāaprēķina:  v = ?",
                     "Formulas:  v = √(G·M / R)",
                     "Aprēķins:  1) G·M = 6,67 · 10⁻¹¹ · 7,35 · 10²² = "
                     "4,90 · 10¹²",
                     "                   2) G·M / R = 4,90 · 10¹² : "
                     "1,74 · 10⁶ = 2,82 · 10⁶",
                     "                   3) v = √(2,82 · 10⁶) ≈ 1,68 · 10³ m/s",
                     "Atbilde:  v ≈ 1,7 km/s - apmēram 4,7 reižu mazāks nekā "
                     "Zemei, jo Mēness masa ir daudz mazāka.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» ar skaitļiem standartformā;",
                     "1 p - pierakstīta formula v = √(G·M / R);",
                     "2 p - pareizs aprēķins ar mērvienību (≈ 1,7 km/s);",
                     "1 p - pamatots salīdzinājums ar Zemes vērtību.",
                 ]},

                {"tips": "jautajumi", "virs": "Orbītas un Keplera likumi",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Marss riņķo ap Sauli pa orbītu, kuras lielā "
                           "pusass ir 1,52 astronomiskās vienības (a. v.). "
                           "Zemes orbītas lielā pusass ir 1,00 a. v., un "
                           "Zemes apriņķošanas periods ir 1,00 gads.",
                 "jaut": [
                     ("Pieraksti Keplera trešo likumu!", 1),
                     ("Aprēķini Marsa apriņķošanas periodu gados!", 1),
                     ("Nosaki, vai Marss kustas ātrāk vai lēnāk par Zemi, un "
                      "pamato!", 1),
                     ("Kāpēc planētas ātrums perihēlijā ir lielāks nekā "
                      "afēlijā?", 1),
                     ("Nosauc, kas paliek nemainīgs, planētai riņķojot pa "
                      "elipsi ap Sauli!", 1),
                 ],
                 "atbildes": [
                     "1) T₁² / T₂² = a₁³ / a₂³ jeb T² / a³ = const.   (1 p)",
                     "2) T² = 1,52³ = 3,51;  T = √3,51 ≈ 1,87 gadi.   (1 p)",
                     "3) Lēnāk: jo tālāk no Saules, jo mazāks orbitālais "
                     "ātrums (v = √(G·M / r)).   (1 p)",
                     "4) Perihēlijā planēta ir tuvāk Saulei, gravitācijas "
                     "spēks lielāks; pēc Keplera otrā likuma tā pašā laikā "
                     "aizmet vienādu laukumu, tāpēc ātrumam jābūt lielākam.   "
                     "(1 p)",
                     "5) Nemainīga paliek pilnā mehāniskā enerģija (un "
                     "impulsa moments); kinētiskā un potenciālā enerģija "
                     "pārvēršas viena otrā.   (1 p)",
                 ]},
            ],
        },
    ],
}
