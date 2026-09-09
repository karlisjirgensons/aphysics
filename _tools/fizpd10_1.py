# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. PD1 - Vektori un fizikālie lielumi (1.-4. stunda)."""

PD = {
    "nr": 1,
    "klase": "10. klase",
    "nosaukums": "Vektori un fizikālie lielumi",
    "mape": "1. Ievads pētniecībā. Vienmērīga un nevienmērīga kustība",
    "fails": "PD1. Vektori un fizikālie lielumi_tt",
    "stundas": "1.-4.",
    "datums": "16.09.2026.",
    "kopa": 20,
    "laiks": 30,
    "apraksts": "Pirmais kursa pārbaudes darbs. Pārbauda fizikālo lielumu "
                "pierakstu, SI vienības un priedēkļus, skalāru un vektoru "
                "nošķiršanu, vektoru saskaitīšanu ģeometriski un vektora "
                "projekcijas uz koordinātu asīm.",
    "atgadne": [
        "Priedēkļi:  k = 10³  ·  M = 10⁶  ·  c = 10⁻²  ·  m = 10⁻³  ·  "
        "µ = 10⁻⁶  ·  n = 10⁻⁹",
        "1 cm² = 10⁻⁴ m²  ·  1 cm³ = 10⁻⁶ m³  ·  no km/h uz m/s dala ar 3,6",
        "Projekcijas:  aₓ = a · cos α  ·  a_y = a · sin α  ·  "
        "a = √(aₓ² + a_y²)",
        "sin 30° = 0,50  ·  cos 30° = 0,87  ·  sin 60° = 0,87  ·  "
        "cos 60° = 0,50  ·  sin 45° = cos 45° = 0,71",
    ],
    "struktura": [
        ("1.", "Nošķir skalārus no vektoriem, lieto SI vienības un "
               "priedēkļus, nosaka vektoru summas virzienu", "1.-4.", 8),
        ("2.", "Pārvērš mērvienības, lietojot priedēkļus un standartformu",
         "1.", 4),
        ("3.", "Saskaita divus vektorus un aprēķina summas moduli", "3.", 4),
        ("4.", "Nosaka vektora projekcijas uz asīm un moduli pēc "
               "projekcijām", "4.", 4),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kurš no lielumiem ir vektoriāls?",
                 ["masa", "temperatūra", "spēks", "laiks"], 2),
                ("Kura ir garuma SI pamatvienība?",
                 ["centimetrs", "kilometrs", "milimetrs", "metrs"], 3),
                ("Kā standartformā metros pieraksta 2,4 km?",
                 ["2,4 · 10² m", "2,4 · 10³ m", "24 · 10² m",
                  "2,4 · 10⁻³ m"], 1),
                ("Automašīnas ātrums ir 72 km/h. Cik tas ir m/s?",
                 ["7,2 m/s", "20 m/s", "26 m/s", "200 m/s"], 1),
                ("Divi vienāda moduļa vektori ir vērsti pretējos virzienos. "
                 "Cik liels ir to summas modulis?",
                 ["nulle", "viena vektora modulis",
                  "divkāršs viena vektora modulis", "nav nosakāms"], 0),
                ("Vektoru reizina ar skaitli −2. Kas notiek ar vektoru?",
                 ["modulis divkāršojas, virziens nemainās",
                  "modulis divkāršojas, virziens kļūst pretējs",
                  "modulis nemainās, virziens kļūst pretējs",
                  "modulis samazinās divas reizes"], 1),
                ("Vektors a veido 60° leņķi ar x asi, tā modulis ir 10 N. "
                 "Cik liela ir projekcija uz x ass?",
                 ["10 N", "8,7 N", "5,0 N", "0"], 2),
                ("Kurā gadījumā divu vektoru summas modulis ir vislielākais?",
                 ["vektori ir perpendikulāri",
                  "vektori vērsti pretējos virzienos",
                  "modulis vienmēr ir vienāds",
                  "vektori vērsti vienā virzienā"], 3),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Izsaki lielumus SI vienībās",
                 "punkti": 4,
                 "rindas": [
                     ("36 km/h = ..................... m/s", "10 m/s"),
                     ("250 g = ..................... kg", "0,25 kg"),
                     ("15 cm² = ..................... m²  (standartformā)",
                      "1,5 · 10⁻³ m²"),
                     ("4,5 ms = ..................... s  (standartformā)",
                      "4,5 · 10⁻³ s"),
                 ]},

                {"tips": "aprekins", "virs": "Divu spēku summa", "punkti": 4,
                 "vieta": 7.0,
                 "teksts": "Uz ķermeni darbojas divi savstarpēji "
                           "perpendikulāri spēki: F₁ = 6,0 N (vērsts pa x "
                           "asi) un F₂ = 8,0 N (vērsts pa y asi). Aprēķini "
                           "kopspēka moduli un noskaidro, cik liela ir "
                           "kopspēka projekcija uz x ass!",
                 "risinajums": [
                     "Dots:  F₁ = 6,0 N;  F₂ = 8,0 N;  F₁ ⊥ F₂",
                     "Jāaprēķina:  F = ?  Fₓ = ?",
                     "Formulas:  F = √(F₁² + F₂²);  Fₓ = F₁",
                     "Aprēķins:  1) F = √(6,0² + 8,0²) N = √(36 + 64) N",
                     "                   2) F = √100 N = 10 N",
                     "                   3) Fₓ = F₁ = 6,0 N",
                     "Atbilde:  kopspēks F = 10 N; tā projekcija uz x ass "
                     "Fₓ = 6,0 N.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» un «Jāaprēķina» ar "
                     "mērvienībām;",
                     "1 p - pierakstīta formula F = √(F₁² + F₂²);",
                     "1 p - pareizs aprēķins ar mērvienību (10 N);",
                     "1 p - pareizi noteikta projekcija Fₓ = 6,0 N.",
                 ]},

                {"tips": "jautajumi", "virs": "Vektora projekcijas",
                 "punkti": 4, "vieta": 6.5,
                 "ievads": "Ķermeni velk ar spēku F = 40 N, kas veido 30° "
                           "leņķi ar horizontu.",
                 "jaut": [
                     ("Uzzīmē spēku un tā projekcijas uz horizontālās un "
                      "vertikālās ass!", 1),
                     ("Aprēķini projekciju uz horizontālās ass Fₓ!", 1),
                     ("Aprēķini projekciju uz vertikālās ass F_y!", 1),
                     ("Pamato, kura projekcija palīdz ķermeni pārvietot pa "
                      "horizontālu virsmu!", 1),
                 ],
                 "atbildes": [
                     "1) Zīmējumā redzams vektors F, leņķis 30° pret "
                     "horizontu un abas projekcijas ar bultiņām.   (1 p)",
                     "2) Fₓ = F · cos 30° = 40 N · 0,87 = 35 N "
                     "(pieļaujams 34,6 N).   (1 p)",
                     "3) F_y = F · sin 30° = 40 N · 0,50 = 20 N.   (1 p)",
                     "4) Pārvietošanu pa horizontālu virsmu nodrošina "
                     "horizontālā projekcija Fₓ, jo tā ir vērsta kustības "
                     "virzienā; vertikālā projekcija tikai samazina "
                     "ķermeņa spiedienu uz virsmu.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kurš no lielumiem ir skalārs?",
                 ["pārvietojums", "ātrums", "ceļš", "paātrinājums"], 2),
                ("Kura ir masas SI pamatvienība?",
                 ["grams", "kilograms", "tonna", "ņūtons"], 1),
                ("Kā standartformā metros pieraksta 750 mm?",
                 ["7,5 · 10⁻¹ m", "7,5 · 10² m", "7,5 · 10⁻³ m",
                  "75 · 10⁻² m"], 0),
                ("Riteņbraucēja ātrums ir 18 km/h. Cik tas ir m/s?",
                 ["1,8 m/s", "6,5 m/s", "50 m/s", "5,0 m/s"], 3),
                ("Divi vienāda moduļa vektori ir vērsti vienā virzienā. Cik "
                 "liels ir to summas modulis?",
                 ["nulle", "viena vektora modulis",
                  "divkāršs viena vektora modulis",
                  "puse no viena vektora moduļa"], 2),
                ("Vektoru reizina ar skaitli 0,5. Kas notiek ar vektoru?",
                 ["modulis samazinās divas reizes, virziens nemainās",
                  "modulis palielinās divas reizes",
                  "virziens kļūst pretējs",
                  "vektors kļūst par skalāru"], 0),
                ("Vektors b veido 60° leņķi ar x asi, tā modulis ir 20 N. "
                 "Cik liela ir projekcija uz y ass?",
                 ["10 N", "17 N", "20 N", "0"], 1),
                ("Kurā gadījumā divu vektoru summas modulis ir vismazākais?",
                 ["vektori ir perpendikulāri",
                  "vektori vērsti vienā virzienā",
                  "vektori vērsti pretējos virzienos",
                  "leņķis starp tiem ir 45°"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Izsaki lielumus SI vienībās",
                 "punkti": 4,
                 "rindas": [
                     ("54 km/h = ..................... m/s", "15 m/s"),
                     ("400 g = ..................... kg", "0,40 kg"),
                     ("25 cm³ = ..................... m³  (standartformā)",
                      "2,5 · 10⁻⁵ m³"),
                     ("120 µs = ..................... s  (standartformā)",
                      "1,2 · 10⁻⁴ s"),
                 ]},

                {"tips": "aprekins", "virs": "Divu spēku summa", "punkti": 4,
                 "vieta": 7.0,
                 "teksts": "Uz ķermeni darbojas divi savstarpēji "
                           "perpendikulāri spēki: F₁ = 9,0 N (vērsts pa x "
                           "asi) un F₂ = 12 N (vērsts pa y asi). Aprēķini "
                           "kopspēka moduli un noskaidro, cik liela ir "
                           "kopspēka projekcija uz y ass!",
                 "risinajums": [
                     "Dots:  F₁ = 9,0 N;  F₂ = 12 N;  F₁ ⊥ F₂",
                     "Jāaprēķina:  F = ?  F_y = ?",
                     "Formulas:  F = √(F₁² + F₂²);  F_y = F₂",
                     "Aprēķins:  1) F = √(9,0² + 12²) N = √(81 + 144) N",
                     "                   2) F = √225 N = 15 N",
                     "                   3) F_y = F₂ = 12 N",
                     "Atbilde:  kopspēks F = 15 N; tā projekcija uz y ass "
                     "F_y = 12 N.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» un «Jāaprēķina» ar "
                     "mērvienībām;",
                     "1 p - pierakstīta formula F = √(F₁² + F₂²);",
                     "1 p - pareizs aprēķins ar mērvienību (15 N);",
                     "1 p - pareizi noteikta projekcija F_y = 12 N.",
                 ]},

                {"tips": "jautajumi", "virs": "Vektora projekcijas",
                 "punkti": 4, "vieta": 6.5,
                 "ievads": "Ragaviņas velk ar spēku F = 60 N, kas veido 60° "
                           "leņķi ar horizontu.",
                 "jaut": [
                     ("Uzzīmē spēku un tā projekcijas uz horizontālās un "
                      "vertikālās ass!", 1),
                     ("Aprēķini projekciju uz horizontālās ass Fₓ!", 1),
                     ("Aprēķini projekciju uz vertikālās ass F_y!", 1),
                     ("Pamato, kā mainītos horizontālā projekcija, ja leņķi "
                      "samazinātu līdz 30°!", 1),
                 ],
                 "atbildes": [
                     "1) Zīmējumā redzams vektors F, leņķis 60° pret "
                     "horizontu un abas projekcijas ar bultiņām.   (1 p)",
                     "2) Fₓ = F · cos 60° = 60 N · 0,50 = 30 N.   (1 p)",
                     "3) F_y = F · sin 60° = 60 N · 0,87 = 52 N "
                     "(pieļaujams 51,9 N).   (1 p)",
                     "4) Fₓ palielinātos: cos 30° = 0,87 > cos 60° = 0,50, "
                     "tāpēc Fₓ = 60 N · 0,87 ≈ 52 N. Jo mazāks leņķis pret "
                     "horizontu, jo lielāka horizontālā projekcija.   (1 p)",
                 ]},
            ],
        },
    ],
}
