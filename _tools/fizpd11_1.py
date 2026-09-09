# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD1 - Mehāniskās svārstības un viļņi (1.-4. st.)."""

PD = {
    "nr": 1,
    "klase": "11. klase",
    "nosaukums": "Mehāniskās svārstības un viļņi",
    "mape": "6. Mehāniskās svārstības un viļņi",
    "fails": "PD1. Mehāniskās svārstības un viļņi_tt",
    "stundas": "1.-4.",
    "datums": "16.09.2026.",
    "kopa": 20,
    "laiks": 30,
    "apraksts": "Pirmais mācību gada pārbaudes darbs. Pārbauda svārstību "
                "raksturlielumus, rezonansi, šķērsviļņu un garenviļņu "
                "atšķirību, skaņas īpašības un sakarību v = λf.",
    "atgadne": [
        "T = t / N   ·   ν = 1 / T   ·   v = λν   ·   λ = v / ν",
        "Skaņas ātrums gaisā ≈ 340 m/s   ·   ūdenī ≈ 1500 m/s",
        "Matemātiskais svārsts:  T = 2π√(l / g)   ·   g = 9,8 m/s²",
        "Dzirdamā skaņa: 20 Hz - 20 000 Hz   ·   1 kHz = 10³ Hz",
    ],
    "struktura": [
        ("1.", "Atpazīst svārstību raksturlielumus, skaidro rezonansi, "
               "atšķir viļņu veidus un saista skaņas īpašības ar "
               "raksturlielumiem", "1.-4.", 8),
        ("2.", "Nolasa svārstību grafiku un nosaka amplitūdu, periodu un "
               "frekvenci", "3., 4.", 4),
        ("3.", "Lieto sakarību v = λν", "3.", 4),
        ("4.", "Skaidro rezonansi un skaņas izplatīšanos", "1., 2.", 4),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Ko sauc par svārstību amplitūdu?",
                 ["laiku starp divām svārstībām",
                  "lielāko novirzi no līdzsvara stāvokļa",
                  "svārstību skaitu sekundē",
                  "attālumu starp diviem viļņu kalniem"], 1),
                ("Svārsts 20 s laikā veic 10 pilnas svārstības. Cik liels ir "
                 "periods?",
                 ["0,5 s", "2 s", "10 s", "200 s"], 1),
                ("Kāda ir frekvences SI mērvienība?",
                 ["sekunde", "metrs", "hercs", "vats"], 2),
                ("Kad iestājas rezonanse?",
                 ["kad amplitūda ir maza",
                  "kad ārējā spēka frekvence sakrīt ar sistēmas pašfrekvenci",
                  "kad svārstības apstājas",
                  "kad periods ir liels"], 1),
                ("Ar ko garenviļņi atšķiras no šķērsviļņiem?",
                 ["daļiņas svārstās perpendikulāri viļņa izplatīšanās "
                  "virzienam",
                  "daļiņas svārstās gar viļņa izplatīšanās virzienu",
                  "tie neizplatās gaisā",
                  "tiem nav frekvences"], 1),
                ("Kas nosaka skaņas augstumu?",
                 ["amplitūda", "frekvence", "ātrums", "viļņa garums"], 1),
                ("Skaņa nevar izplatīties:",
                 ["gaisā", "ūdenī", "metālā", "vakuumā"], 3),
                ("Viļņa garums ir 2,0 m, frekvence 170 Hz. Cik liels ir "
                 "viļņa ātrums?",
                 ["85 m/s", "170 m/s", "340 m/s", "0,012 m/s"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Svārstību grafiks", "punkti": 4,
                 "note": "Lodītes novirze mainās periodiski: lielākā novirze "
                         "ir 6 cm, un viena pilna svārstība ilgst 0,40 s. "
                         "Aizpildi rindas! Par katru pareizu atbildi - "
                         "1 punkts.",
                 "rindas": [
                     ("Amplitūda  A = ..................... cm", "6 cm"),
                     ("Periods  T = ..................... s", "0,40 s"),
                     ("Frekvence  ν = ..................... Hz", "2,5 Hz"),
                     ("Svārstību skaits 10 s laikā  N = ....................."
                      "", "25"),
                 ]},

                {"tips": "aprekins", "virs": "Viļņa garums", "punkti": 4,
                 "vieta": 7.0,
                 "teksts": "Skaņas viļņa frekvence gaisā ir 850 Hz, skaņas "
                           "ātrums gaisā ir 340 m/s. Aprēķini viļņa garumu! "
                           "Cik liels būtu viļņa garums ūdenī, kur skaņas "
                           "ātrums ir 1500 m/s (frekvence nemainās)?",
                 "risinajums": [
                     "Dots:  ν = 850 Hz;  v₁ = 340 m/s;  v₂ = 1500 m/s",
                     "Jāaprēķina:  λ₁ = ?  λ₂ = ?",
                     "Formulas:  v = λν  →  λ = v / ν",
                     "Aprēķins:  1) λ₁ = 340 : 850 = 0,40 m",
                     "                   2) λ₂ = 1500 : 850 ≈ 1,8 m",
                     "Atbilde:  λ₁ = 0,40 m;  λ₂ ≈ 1,8 m. Ūdenī viļņa garums "
                     "ir lielāks, jo ātrums ir lielāks, bet frekvenci nosaka "
                     "avots.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» un «Jāaprēķina» ar "
                     "mērvienībām;",
                     "1 p - pierakstīta formula λ = v / ν;",
                     "1 p - pareizs λ₁ = 0,40 m ar mērvienību;",
                     "1 p - pareizs λ₂ ≈ 1,8 m un pamatojums, ka frekvence "
                     "nemainās.",
                 ]},

                {"tips": "jautajumi", "virs": "Rezonanse un skaņa",
                 "punkti": 4, "vieta": 6.5,
                 "ievads": "Bērns šūpojas šūpolēs. Viens pilns šūpošanās "
                           "cikls ilgst 2,0 s.",
                 "jaut": [
                     ("Aprēķini šūpoļu svārstību frekvenci!", 1),
                     ("Ar kādu frekvenci jāgrūž šūpoles, lai amplitūda "
                      "pieaugtu visstraujāk? Nosauc parādību!", 1),
                     ("Nosauc vienu piemēru, kur rezonanse ir kaitīga, un "
                      "vienu, kur tā ir noderīga!", 1),
                     ("Paskaidro, kāpēc šūpoļu periods nav atkarīgs no "
                      "bērna masas!", 1),
                 ],
                 "atbildes": [
                     "1) ν = 1 / T = 1 : 2,0 = 0,50 Hz.   (1 p)",
                     "2) Ar frekvenci 0,50 Hz, t. i., sakrītošu ar šūpoļu "
                     "pašfrekvenci; parādību sauc par rezonansi.   (1 p)",
                     "3) Kaitīga: tiltu vai ēku svārstības zemestrīcē, "
                     "mašīnu vibrācijas. Noderīga: mūzikas instrumentu "
                     "rezonatori, radiouztvērēja kontūra noskaņošana, "
                     "mikroviļņu krāsns.   (1 p)",
                     "4) Matemātiskā svārsta periods T = 2π√(l/g) ir "
                     "atkarīgs tikai no garuma un g; masa vienādojumā "
                     "neietilpst, jo lielāka masa dod gan lielāku spēku, gan "
                     "lielāku inerci.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Ko sauc par svārstību periodu?",
                 ["lielāko novirzi no līdzsvara stāvokļa",
                  "laiku, kurā notiek viena pilna svārstība",
                  "svārstību skaitu sekundē",
                  "attālumu starp diviem viļņu kalniem"], 1),
                ("Svārsts 30 s laikā veic 60 pilnas svārstības. Cik liela ir "
                 "frekvence?",
                 ["0,5 Hz", "1 Hz", "2 Hz", "30 Hz"], 2),
                ("Kāda ir perioda SI mērvienība?",
                 ["hercs", "metrs", "sekunde", "vats"], 2),
                ("Kas raksturo skaņas skaļumu?",
                 ["frekvence", "amplitūda", "ātrums", "viļņa garums"], 1),
                ("Kurš no viļņiem ir garenvilnis?",
                 ["vilnis uz ūdens virsmas", "skaņas vilnis gaisā",
                  "gaismas vilnis", "vilnis uz izstieptas auklas"], 1),
                ("Kas ir viļņa garums?",
                 ["attālums, ko vilnis veic vienā periodā",
                  "svārstību skaits sekundē",
                  "lielākā novirze", "viļņa ātrums"], 0),
                ("Kāda ir dzirdamās skaņas frekvenču robeža?",
                 ["0-100 Hz", "20-20 000 Hz", "20-200 Hz",
                  "1000-100 000 Hz"], 1),
                ("Viļņa ātrums ir 340 m/s, viļņa garums 0,50 m. Cik liela "
                 "ir frekvence?",
                 ["170 Hz", "340 Hz", "680 Hz", "0,0015 Hz"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Svārstību grafiks", "punkti": 4,
                 "note": "Lodītes novirze mainās periodiski: lielākā novirze "
                         "ir 8 cm, un 5 pilnas svārstības ilgst 2,0 s. "
                         "Aizpildi rindas! Par katru pareizu atbildi - "
                         "1 punkts.",
                 "rindas": [
                     ("Amplitūda  A = ..................... cm", "8 cm"),
                     ("Periods  T = ..................... s", "0,40 s"),
                     ("Frekvence  ν = ..................... Hz", "2,5 Hz"),
                     ("Ceļš, ko lodīte veic vienā periodā  s = ............"
                      "......... cm", "32 cm  (4 amplitūdas)"),
                 ]},

                {"tips": "aprekins", "virs": "Viļņa frekvence", "punkti": 4,
                 "vieta": 7.0,
                 "teksts": "Skaņas viļņa garums gaisā ir 1,7 m, skaņas ātrums "
                           "gaisā ir 340 m/s. Aprēķini frekvenci! Cik liels "
                           "būtu viļņa garums tērauda sliedē, kur skaņas "
                           "ātrums ir 5000 m/s (frekvence nemainās)?",
                 "risinajums": [
                     "Dots:  λ₁ = 1,7 m;  v₁ = 340 m/s;  v₂ = 5000 m/s",
                     "Jāaprēķina:  ν = ?  λ₂ = ?",
                     "Formulas:  v = λν  →  ν = v / λ;  λ₂ = v₂ / ν",
                     "Aprēķins:  1) ν = 340 : 1,7 = 200 Hz",
                     "                   2) λ₂ = 5000 : 200 = 25 m",
                     "Atbilde:  ν = 200 Hz;  λ₂ = 25 m. Blīvākā vidē skaņa "
                     "izplatās ātrāk, tāpēc viļņa garums ir lielāks.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» un «Jāaprēķina» ar "
                     "mērvienībām;",
                     "1 p - pierakstīta formula ν = v / λ;",
                     "1 p - pareiza frekvence 200 Hz ar mērvienību;",
                     "1 p - pareizs λ₂ = 25 m un pamatojums.",
                 ]},

                {"tips": "jautajumi", "virs": "Rezonanse un skaņa",
                 "punkti": 4, "vieta": 6.5,
                 "ievads": "Ģitāras stīga svārstās ar frekvenci 220 Hz. "
                           "Skaņas ātrums gaisā ir 340 m/s.",
                 "jaut": [
                     ("Aprēķini stīgas svārstību periodu!", 1),
                     ("Aprēķini skaņas viļņa garumu gaisā!", 1),
                     ("Paskaidro, kā mainīsies skaņas augstums, ja stīgu "
                      "nostiepj stingrāk!", 1),
                     ("Paskaidro, kāpēc ģitārai ir dobs korpuss!", 1),
                 ],
                 "atbildes": [
                     "1) T = 1 / ν = 1 : 220 ≈ 4,5 · 10⁻³ s.   (1 p)",
                     "2) λ = v / ν = 340 : 220 ≈ 1,5 m.   (1 p)",
                     "3) Skaņa kļūs augstāka: stingrāk nostiepta stīga "
                     "svārstās ar lielāku frekvenci.   (1 p)",
                     "4) Korpuss ir rezonators - gaiss tajā svārstās "
                     "rezonansē ar stīgu, tāpēc skaņa kļūst skaļāka.   (1 p)",
                 ]},
            ],
        },
    ],
}
