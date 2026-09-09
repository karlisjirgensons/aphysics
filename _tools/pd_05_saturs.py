# -*- coding: utf-8 -*-
"""PD5 — Spēki un ķermeņu mijiedarbība jeb dinamika (7.9.–7.16. stunda)."""

PD = {
    "nr": 5,
    "nosaukums": "Spēki un ķermeņu mijiedarbība (dinamika)",
    "mape": "7. Cietu ķermeņu kustība un mijiedarbība",
    "fails": "PD5. Spēki un ķermeņu mijiedarbība (dinamika)",
    "stundas": "7.9.–7.16.",
    "datums": "08.01.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda Ņūtona likumus, gravitācijas, elastības un "
                "berzes spēku, impulsu un reaktīvo kustību, spiedienu, spēka "
                "momentu un vienkāršos mehānismus.",
    "atgadne": [
        "F = m · a   ·   a = F / m   ·   F = m · g   ·   g = 10 m/s²   ·   "
        "1 N = 1 kg·m/s²",
        "F = G · m₁ · m₂ / R²   ·   G = 6,67 · 10⁻¹¹ m³/(kg·s²)   ·   "
        "F(elast) = k · Δx   ·   F(berze) = µ · N",
        "p = F / S   ·   1 Pa = 1 N/m²   ·   1 kPa = 10³ Pa   ·   "
        "M = F · l   ·   F₁ · l₁ = F₂ · l₂",
        "p = m · υ   ·   υ = υ₀ + a · t   ·   s = a · t² / 2",
    ],
    "struktura": [
        ("1.", "Formulē Ņūtona likumus, raksturo inerci, berzi, gravitāciju, "
               "spiedienu un vienkāršos mehānismus", "7.9.–7.16.", 10),
        ("2.", "Nosaka rezultējošo spēku un lieto Ņūtona II likumu kopā ar "
               "kinemātikas formulām", "7.10.", 5),
        ("3.", "Aprēķina smaguma spēku dažādās planētās un salīdzina to",
         "7.12.", 4),
        ("4.", "Aprēķina spiedienu un skaidro balsta laukuma nozīmi",
         "7.14.", 4),
        ("5.", "Lieto sviras līdzsvara nosacījumu un nosaka spēka ieguvumu",
         "7.15., 7.16.", 4),
        ("6.", "Skaidro inerci, Ņūtona III likumu un zelta likumu mehānikā",
         "7.9., 7.11., 7.16.", 3),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Ko apgalvo Ņūtona I likums?",
                 ["lai ķermenis kustētos vienmērīgi, vajadzīgs spēks",
                  "ja rezultējošais spēks ir nulle, ķermenis paliek mierā "
                  "vai kustas vienmērīgi taisnvirzienā",
                  "spēks ir proporcionāls masai",
                  "visi spēki dabā ir vienādi"], 1),
                ("Kāda ir spēka mērvienība SI sistēmā?",
                 ["kilograms", "paskāls", "ņūtons", "džouls"], 2),
                ("Ja uz to pašu ķermeni iedarbojas divreiz lielāks "
                 "rezultējošais spēks, paātrinājums",
                 ["palielinās 2 reizes", "nemainās", "samazinās 2 reizes",
                  "palielinās 4 reizes"], 0),
                ("Kāpēc Ņūtona III likuma spēku pāris viens otru "
                 "neizlīdzina?",
                 ["spēki ir dažāda lieluma",
                  "spēki darbojas uz dažādiem ķermeņiem",
                  "spēki ir vērsti vienā virzienā",
                  "viens no spēkiem ir nulle"], 1),
                ("Ja attālums starp diviem ķermeņiem palielinās trīs reizes, "
                 "gravitācijas spēks",
                 ["samazinās 3 reizes", "palielinās 3 reizes", "nemainās",
                  "samazinās 9 reizes"], 3),
                ("Kāpēc slēpes palīdz noturēties uz irdena sniega?",
                 ["tās samazina cilvēka svaru", "tās palielina berzi",
                  "tās samazina cilvēka masu",
                  "tās palielina balsta laukumu un samazina spiedienu"], 3),
                ("Kura berze ir vismazākā?",
                 ["miera berze", "slīdes berze", "rites berze",
                  "visas ir vienādas"], 2),
                ("Kad svira ir līdzsvarā?",
                 ["kad momenti abās pusēs ir vienādi",
                  "kad spēki abās pusēs ir vienādi",
                  "kad pleci abās pusēs ir vienādi",
                  "kad masa abās pusēs ir vienāda"], 0),
                ("Kāds spēka ieguvums ir kustīgajam blokam?",
                 ["1", "2", "4", "nekāda ieguvuma nav"], 1),
                ("Ko apgalvo zelta likums mehānikā?",
                 ["mehānisms rada papildu enerģiju",
                  "mehānisms samazina padarīto darbu",
                  "cik reižu iegūst spēkā, tik reižu zaudē ceļā",
                  "spēks mehānismā vienmēr paliek nemainīgs"], 2),
            ],
            "uzdevumi": [
                {"tips": "aprekins", "virs": "Ņūtona II likums", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Uz ķermeni, kura masa ir m = 4 kg, horizontāli "
                           "iedarbojas vilces spēks F₁ = 30 N, bet pretēji "
                           "kustībai — berzes spēks F₂ = 10 N. Aprēķini "
                           "rezultējošo spēku un paātrinājumu! Cik lielu "
                           "ātrumu ķermenis sasniegs 5 s laikā, ja tas sāk "
                           "kustību no miera?",
                 "risinajums": [
                     "Dots:  m = 4 kg;  F₁ = 30 N;  F₂ = 10 N;  υ₀ = 0;  "
                     "t = 5 s",
                     "Jāaprēķina:  F = ?  (N)    a = ?  (m/s²)    "
                     "υ = ?  (m/s)",
                     "Formulas:  F = F₁ − F₂ ;   a = F / m ;   υ = υ₀ + a · t",
                     "Aprēķins:  1) F = 30 N − 10 N = 20 N",
                     "                   2) a = F / m = 20 N : 4 kg = 5 m/s²",
                     "                   3) υ = 0 + 5 m/s² · 5 s = 25 m/s",
                     "Atbilde:  F = 20 N;  a = 5 m/s²;  υ = 25 m/s.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts (vai spēku "
                     "shēma);",
                     "1 p — pareizi noteikts rezultējošais spēks F = 20 N "
                     "(spēki jāatņem, jo vērsti pretēji);",
                     "1 p — pierakstītas formulas a = F/m un υ = υ₀ + at;",
                     "1 p — pareizi aprēķināts a = 5 m/s²;",
                     "1 p — pareizi aprēķināts υ = 25 m/s un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Gravitācija un svars",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Cilvēka masa ir m = 60 kg. Aprēķini smaguma "
                           "spēku, kas uz viņu darbojas uz Zemes "
                           "(g = 9,8 m/s²) un uz Mēness (g = 1,6 m/s²)! Cik "
                           "reižu smaguma spēks uz Mēness ir mazāks?",
                 "risinajums": [
                     "Dots:  m = 60 kg;  g₁ = 9,8 m/s²;  g₂ = 1,6 m/s²",
                     "Jāaprēķina:  F₁ = ?  F₂ = ?  (N)    F₁/F₂ = ?",
                     "Formulas:  F = m · g",
                     "Aprēķins:  1) F₁ = 60 kg · 9,8 m/s² = 588 N",
                     "                   2) F₂ = 60 kg · 1,6 m/s² = 96 N",
                     "                   3) F₁ / F₂ = 588 N : 96 N ≈ 6,1",
                     "Atbilde:  uz Zemes 588 N, uz Mēness 96 N — aptuveni "
                     "6 reizes mazāk. Masa abās vietās paliek 60 kg.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula F = m·g;",
                     "1 p — pareizi aprēķināts F₁ = 588 N;",
                     "1 p — pareizi aprēķināts F₂ = 96 N;",
                     "1 p — pareiza attiecība ≈ 6 un atbilde. Papildu "
                     "pareiza piezīme, ka masa nemainās, kļūdu nelabo, bet "
                     "apstiprina izpratni.",
                 ]},

                {"tips": "aprekins", "virs": "Spiediens", "punkti": 4,
                 "vieta": 6.5,
                 "teksts": "Cilvēka masa ir m = 70 kg. Stāvot uz abām kājām, "
                           "pēdu kopējais balsta laukums ir "
                           "S₁ = 0,04 m², bet uz slēpēm — S₂ = 0,40 m². "
                           "Aprēķini spiedienu uz sniegu abos gadījumos! "
                           "Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  m = 70 kg;  S₁ = 0,04 m²;  S₂ = 0,40 m²;  "
                     "g = 10 m/s²",
                     "Jāaprēķina:  p₁ = ?  p₂ = ?  (Pa)",
                     "Formulas:  F = m · g ;   p = F / S",
                     "Aprēķins:  1) F = m · g = 70 kg · 10 m/s² = 700 N",
                     "                   2) p₁ = F / S₁ = 700 N : 0,04 m² = "
                     "17 500 Pa = 17,5 kPa",
                     "                   3) p₂ = F / S₂ = 700 N : 0,40 m² = "
                     "1750 Pa = 1,75 kPa",
                     "Atbilde:  p₁ = 17,5 kPa;  p₂ = 1,75 kPa — uz slēpēm "
                     "spiediens ir 10 reižu mazāks, jo laukums ir 10 reižu "
                     "lielāks.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formulas F = m·g, "
                     "p = F/S;",
                     "1 p — pareizi aprēķināts F = 700 N;",
                     "1 p — pareizi aprēķināts p₁ = 17 500 Pa;",
                     "1 p — pareizi aprēķināts p₂ = 1750 Pa un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Svira un spēka moments",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Uz sviras kreisā gala l₁ = 0,80 m attālumā no "
                           "balsta darbojas spēks F₁ = 150 N. Cik liels "
                           "spēks F₂ jāpieliek labajā pusē l₂ = 1,2 m "
                           "attālumā no balsta, lai svira būtu līdzsvarā? "
                           "Cik liels ir spēka ieguvums?",
                 "risinajums": [
                     "Dots:  l₁ = 0,80 m;  F₁ = 150 N;  l₂ = 1,2 m",
                     "Jāaprēķina:  F₂ = ?  (N)    ieguvums = ?",
                     "Formulas:  F₁ · l₁ = F₂ · l₂  →  F₂ = F₁ · l₁ / l₂",
                     "Aprēķins:  1) F₂ = 150 N · 0,80 m : 1,2 m = "
                     "120 : 1,2 = 100 N",
                     "                   2) ieguvums = F₁ / F₂ = "
                     "150 N : 100 N = 1,5",
                     "Atbilde:  F₂ = 100 N;  spēka ieguvums ir 1,5 reizes. "
                     "Pēc zelta likuma tikpat reižu garāks būs ceļš, kas "
                     "jāveic spēka F₂ pielikšanas punktam.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīts līdzsvara nosacījums F₁·l₁ = F₂·l₂;",
                     "1 p — pareizi aprēķināts F₂ = 100 N;",
                     "1 p — noteikts ieguvums 1,5 un uzrakstīta atbilde.",
                 ]},

                {"tips": "jautajumi", "virs": "Ņūtona likumi praksē",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem un katrā nosauc likumu, uz "
                           "kuru atsaucies!",
                 "jaut": [
                     ("Kāpēc, automašīnai strauji bremzējot, pasažieris "
                      "tiecas uz priekšu?", 1),
                     ("Raķete izmet degvielas gāzes atpakaļ. Kāpēc raķete "
                      "kustas uz priekšu arī kosmosā, kur nav gaisa?", 1),
                     ("Ar sviru spēku samazina 4 reizes. Cik reižu garāks "
                      "ceļš jāveic spēka pielikšanas punktam? Kāpēc?", 1),
                 ],
                 "atbildes": [
                     "1) Inerces dēļ — Ņūtona I likums. Pasažiera ķermenis "
                     "saglabā savu ātrumu, kamēr uz to neiedarbojas spēks "
                     "(drošības josta).   (1 p)",
                     "2) Ņūtona III likums un impulsa nezūdamība: raķete "
                     "iedarbojas uz gāzēm, gāzes ar tikpat lielu, bet "
                     "pretēji vērstu spēku — uz raķeti. Atgrūsties no gaisa "
                     "nav vajadzīgs.   (1 p)",
                     "3) 4 reizes garāks ceļš — pēc zelta likuma mehānikā: "
                     "cik reižu iegūst spēkā, tik reižu zaudē ceļā, jo "
                     "padarītais darbs A = F · s paliek tāds pats.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Ko sauc par inerci?",
                 ["ķermeņa īpašību saglabāt savu ātrumu",
                  "spēku, kas aptur ķermeni", "ātruma izmaiņu sekundē",
                  "ķermeņa svaru"], 0),
                ("Kura formula izsaka Ņūtona II likumu?",
                 ["F = m / a", "F = m · a", "F = a / m", "F = m · υ"], 1),
                ("Ja spēks paliek tas pats, bet ķermeņa masa palielinās trīs "
                 "reizes, paātrinājums",
                 ["palielinās 3 reizes", "nemainās", "samazinās 9 reizes",
                  "samazinās 3 reizes"], 3),
                ("Kura formula izsaka ķermeņa impulsu?",
                 ["p = m · υ", "p = F / S", "p = m · a", "p = F · l"], 0),
                ("Kāpēc Zeme praktiski nekustas, kad cilvēks no tās "
                 "atgrūžas?",
                 ["uz Zemi spēks nedarbojas",
                  "Zemes masa ir daudz lielāka, tāpēc paātrinājums ir "
                  "niecīgs",
                  "spēki ir dažāda lieluma", "gravitācija to neļauj"], 1),
                ("Kurš spēks ļauj cilvēkam staigāt?",
                 ["gravitācijas spēks", "elastības spēks", "berzes spēks",
                  "Arhimēda spēks"], 2),
                ("Slidas slīd, jo mazais balsta laukums rada",
                 ["mazu spiedienu", "lielu berzi", "mazu svaru",
                  "lielu spiedienu"], 3),
                ("Kurš vienkāršais mehānisms nemaina spēka lielumu, bet "
                 "maina tā virzienu?",
                 ["nekustīgais bloks", "svira", "kustīgais bloks",
                  "slīpā plakne"], 0),
                ("Kam vienāds slīpās plaknes spēka ieguvums?",
                 ["augstuma un garuma attiecībai",
                  "masas un garuma reizinājumam",
                  "garuma un augstuma attiecībai", "tas vienmēr ir 2"], 2),
                ("Cik liels ir rezultējošais spēks, ja automašīna brauc ar "
                 "nemainīgu ātrumu pa taisnu ceļu?",
                 ["vienāds ar vilces spēku", "vienāds ar berzes spēku",
                  "nulle", "vienāds ar smaguma spēku"], 2),
            ],
            "uzdevumi": [
                {"tips": "aprekins", "virs": "Ņūtona II likums", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Uz ķermeni, kura masa ir m = 5 kg, horizontāli "
                           "iedarbojas vilces spēks F₁ = 40 N, bet pretēji "
                           "kustībai — berzes spēks F₂ = 15 N. Aprēķini "
                           "rezultējošo spēku un paātrinājumu! Cik lielu ceļu "
                           "ķermenis veiks 4 s laikā, ja tas sāk kustību no "
                           "miera?",
                 "risinajums": [
                     "Dots:  m = 5 kg;  F₁ = 40 N;  F₂ = 15 N;  υ₀ = 0;  "
                     "t = 4 s",
                     "Jāaprēķina:  F = ?  (N)    a = ?  (m/s²)    s = ?  (m)",
                     "Formulas:  F = F₁ − F₂ ;   a = F / m ;   s = a · t² / 2",
                     "Aprēķins:  1) F = 40 N − 15 N = 25 N",
                     "                   2) a = F / m = 25 N : 5 kg = 5 m/s²",
                     "                   3) s = a · t² / 2 = 5 m/s² · "
                     "(4 s)² : 2 = 5 · 16 : 2 = 40 m",
                     "Atbilde:  F = 25 N;  a = 5 m/s²;  s = 40 m.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts (vai spēku "
                     "shēma);",
                     "1 p — pareizi noteikts rezultējošais spēks F = 25 N "
                     "(spēki jāatņem, jo vērsti pretēji);",
                     "1 p — pierakstītas formulas a = F/m un s = at²/2;",
                     "1 p — pareizi aprēķināts a = 5 m/s²;",
                     "1 p — pareizi aprēķināts s = 40 m un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Gravitācija un svars",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Cilvēka masa ir m = 80 kg. Aprēķini smaguma "
                           "spēku, kas uz viņu darbojas uz Zemes "
                           "(g = 9,8 m/s²) un uz Marsa (g = 3,7 m/s²)! Cik "
                           "reižu smaguma spēks uz Marsa ir mazāks?",
                 "risinajums": [
                     "Dots:  m = 80 kg;  g₁ = 9,8 m/s²;  g₂ = 3,7 m/s²",
                     "Jāaprēķina:  F₁ = ?  F₂ = ?  (N)    F₁/F₂ = ?",
                     "Formulas:  F = m · g",
                     "Aprēķins:  1) F₁ = 80 kg · 9,8 m/s² = 784 N",
                     "                   2) F₂ = 80 kg · 3,7 m/s² = 296 N",
                     "                   3) F₁ / F₂ = 784 N : 296 N ≈ 2,6",
                     "Atbilde:  uz Zemes 784 N, uz Marsa 296 N — aptuveni "
                     "2,6 reizes mazāk. Masa abās vietās paliek 80 kg.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula F = m·g;",
                     "1 p — pareizi aprēķināts F₁ = 784 N;",
                     "1 p — pareizi aprēķināts F₂ = 296 N;",
                     "1 p — pareiza attiecība ≈ 2,6 un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Spiediens", "punkti": 4,
                 "vieta": 6.5,
                 "teksts": "Traktora masa ir m = 3000 kg. Uz riepām balsta "
                           "laukums ir S₁ = 0,50 m², bet uz kāpurķēdēm — "
                           "S₂ = 2,0 m². Aprēķini spiedienu uz augsni abos "
                           "gadījumos! Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  m = 3000 kg;  S₁ = 0,50 m²;  S₂ = 2,0 m²;  "
                     "g = 10 m/s²",
                     "Jāaprēķina:  p₁ = ?  p₂ = ?  (Pa)",
                     "Formulas:  F = m · g ;   p = F / S",
                     "Aprēķins:  1) F = m · g = 3000 kg · 10 m/s² = 30 000 N",
                     "                   2) p₁ = F / S₁ = 30 000 N : "
                     "0,50 m² = 60 000 Pa = 60 kPa",
                     "                   3) p₂ = F / S₂ = 30 000 N : "
                     "2,0 m² = 15 000 Pa = 15 kPa",
                     "Atbilde:  p₁ = 60 kPa;  p₂ = 15 kPa — uz kāpurķēdēm "
                     "spiediens ir 4 reizes mazāks, tāpēc traktors mazāk "
                     "iegrimst augsnē.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formulas F = m·g, "
                     "p = F/S;",
                     "1 p — pareizi aprēķināts F = 30 000 N;",
                     "1 p — pareizi aprēķināts p₁ = 60 000 Pa;",
                     "1 p — pareizi aprēķināts p₂ = 15 000 Pa un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Svira un spēka moments",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Uz sviras kreisā gala l₁ = 1,5 m attālumā no "
                           "balsta darbojas spēks F₁ = 80 N. Cik liels spēks "
                           "F₂ jāpieliek labajā pusē l₂ = 0,60 m attālumā no "
                           "balsta, lai svira būtu līdzsvarā? Vai šādi "
                           "novietota svira dod spēka ieguvumu?",
                 "risinajums": [
                     "Dots:  l₁ = 1,5 m;  F₁ = 80 N;  l₂ = 0,60 m",
                     "Jāaprēķina:  F₂ = ?  (N)",
                     "Formulas:  F₁ · l₁ = F₂ · l₂  →  F₂ = F₁ · l₁ / l₂",
                     "Aprēķins:  1) F₂ = 80 N · 1,5 m : 0,60 m = "
                     "120 : 0,60 = 200 N",
                     "Atbilde:  F₂ = 200 N. Spēka ieguvuma NAV — otrā spēka "
                     "plecs ir īsāks, tāpēc spēks jāpieliek 2,5 reizes "
                     "lielāks. Toties tikpat reižu īsāks ir ceļš, ko šis "
                     "spēks veic (ceļa un ātruma ieguvums).",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīts līdzsvara nosacījums F₁·l₁ = F₂·l₂;",
                     "1 p — pareizi aprēķināts F₂ = 200 N;",
                     "1 p — pamatots secinājums, ka spēka ieguvuma nav "
                     "(iegūst ceļā jeb ātrumā).",
                 ]},

                {"tips": "jautajumi", "virs": "Ņūtona likumi praksē",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem un pirmajos divos nosauc "
                           "likumu, uz kuru atsaucies!",
                 "jaut": [
                     ("Kāpēc autobusā, tam sākot braukt, pasažieris "
                      "«paliek atpakaļ»?", 1),
                     ("Kāpēc airētājs, atgrūžot airi pret ūdeni atpakaļ, "
                      "virza laivu uz priekšu?", 1),
                     ("Nosauc vienu gadījumu, kad berze ir noderīga, un "
                      "vienu, kad tā ir kaitīga!", 1),
                 ],
                 "atbildes": [
                     "1) Inerces dēļ — Ņūtona I likums. Pasažiera ķermenis "
                     "saglabā miera stāvokli, kamēr uz to neiedarbojas spēks "
                     "no sēdekļa vai roktura.   (1 p)",
                     "2) Ņūtona III likums: airis iedarbojas uz ūdeni "
                     "atpakaļ vērstu spēku, ūdens ar tikpat lielu, bet "
                     "pretēji vērstu spēku — uz airi un laivu.   (1 p)",
                     "3) Noderīga: ļauj staigāt, braukt un bremzēt, notur "
                     "naglas, skrūves un mezglus. Kaitīga: nolieto detaļas, "
                     "rada lieku siltumu un patērē enerģiju — to samazina ar "
                     "eļļošanu un gultņiem.   (1 p)",
                 ]},
            ],
        },
    ],
}
