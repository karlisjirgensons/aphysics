# -*- coding: utf-8 -*-
"""PD4 — Kustības apraksts jeb kinemātika (7.1.–7.8. stunda)."""

PD = {
    "nr": 4,
    "nosaukums": "Kustības apraksts (kinemātika)",
    "mape": "7. Cietu ķermeņu kustība un mijiedarbība",
    "fails": "PD4. Kustības apraksts (kinemātika)",
    "stundas": "7.1.–7.8.",
    "datums": "04.12.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda vektorus un skalārus, ceļu un pārvietojumu, "
                "vienmērīgu un vienmērīgi paātrinātu kustību, kustības "
                "grafikus, brīvo krišanu un apstāšanās ceļu.",
    "atgadne": [
        "υ = s / t   ·   s = υ · t   ·   no km/h uz m/s dala ar 3,6; "
        "no m/s uz km/h reizina ar 3,6",
        "a = (υ − υ₀) / t   ·   υ = υ₀ + a · t   ·   s = υ₀ · t + a · t² / 2  "
        " ·   s = (υ₀ + υ) / 2 · t",
        "Brīvā krišana:  h = g · t² / 2   ·   υ = g · t   ·   t = √(2h / g)",
        "Apstāšanās ceļš:  s = υ · t(reakcijas) + υ² / (2a)   ·   "
        "g = 10 m/s²",
    ],
    "struktura": [
        ("1.", "Atšķir vektorus no skalāriem, lasa kustības grafikus, "
               "raksturo paātrinājumu, brīvo krišanu un apstāšanās ceļu",
         "7.1.–7.8.", 10),
        ("2.", "Nosaka ceļu un pārvietojumu, arī saskaitot perpendikulārus "
               "vektorus", "7.1., 7.2.", 3),
        ("3.", "Lieto sakarību υ = s / t un pārvērš mērvienības", "7.3.", 4),
        ("4.", "Aprēķina paātrinājumu un ceļu vienmērīgi paātrinātā "
               "kustībā", "7.5., 7.6.", 5),
        ("5.", "Aprēķina brīvās krišanas augstumu, laiku un ātrumu",
         "7.7.", 4),
        ("6.", "Aprēķina reakcijas, bremzēšanas un apstāšanās ceļu; izvērtē "
               "drošību", "7.8.", 4),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kurš no lielumiem ir vektors?",
                 ["ceļš", "laiks", "masa", "pārvietojums"], 3),
                ("Skrējējs noskrien vienu pilnu apli pa 400 m garu stadiona "
                 "celiņu. Cik liels ir viņa pārvietojums?",
                 ["400 m", "200 m", "0 m", "800 m"], 2),
                ("Cik m/s ir 90 km/h?",
                 ["9 m/s", "25 m/s", "32,4 m/s", "250 m/s"], 1),
                ("Ko x(t) grafikā nozīmē horizontāla līnija?",
                 ["ķermenis stāv", "ķermenis brauc vienmērīgi",
                  "ķermenis paātrinās", "ķermenis bremzē"], 0),
                ("Ko rāda υ(t) grafika slīpums?",
                 ["ceļu", "paātrinājumu", "laiku", "masu"], 1),
                ("Ko nozīmē paātrinājums a = 4 m/s²?",
                 ["ķermenis veic 4 m katrā sekundē",
                  "ķermenis brauc ar ātrumu 4 m/s",
                  "ātrums katrā sekundē pieaug par 4 m/s",
                  "ātrums ir 4 reizes lielāks nekā sākumā"], 2),
                ("Cik liels ir paātrinājums kustībā x = 5 + 2t + 3t²?",
                 ["3 m/s²", "6 m/s²", "2 m/s²", "1,5 m/s²"], 1),
                ("Kā vakuumā krīt spalva un tērauda lodīte?",
                 ["spalva lēnāk", "lodīte lēnāk", "abas vienādi ātri",
                  "atkarībā no masas"], 2),
                ("Ja automašīnas ātrums palielinās divas reizes, "
                 "bremzēšanas ceļš",
                 ["palielinās 4 reizes", "nemainās", "palielinās 2 reizes",
                  "samazinās 2 reizes"], 0),
                ("Kurš faktors palielina tieši REAKCIJAS ceļu?",
                 ["slapjš ceļa segums", "nolietotas riepas",
                  "nogurums vai telefona lietošana", "liela kravas masa"], 2),
            ],
            "uzdevumi": [
                {"tips": "jautajumi", "virs": "Ceļš un pārvietojums",
                 "punkti": 3, "vieta": 5.5,
                 "ievads": "Skolēns no mājām aiziet 300 m uz austrumiem līdz "
                           "veikalam un pa to pašu ceļu atgriežas mājās.",
                 "jaut": [
                     ("Cik liels ir viņa veiktais ceļš s?", 1),
                     ("Cik liels ir viņa pārvietojums? Pamato atbildi!", 1),
                     ("Cits cilvēks noiet 30 m uz ziemeļiem un tad 40 m uz "
                      "austrumiem. Cik liels ir viņa pārvietojums?", 1),
                 ],
                 "atbildes": [
                     "1) s = 300 m + 300 m = 600 m.   (1 p)",
                     "2) Pārvietojums ir 0, jo sākuma un beigu punkts sakrīt "
                     "— pārvietojums ir vektors no sākuma uz beigu punktu.   "
                     "(1 p)",
                     "3) Vektori ir perpendikulāri, tāpēc lieto Pitagora "
                     "teorēmu: s = √(30² + 40²) = √(900 + 1600) = √2500 = "
                     "50 m.   (1 p)",
                 ]},

                {"tips": "aprekins", "virs": "Vienmērīga kustība",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Velosipēdists brauc vienmērīgi ar ātrumu "
                           "υ = 18 km/h. Cik lielu ceļu viņš veiks 25 "
                           "minūtēs? Izsaki atbildi arī kilometros!",
                 "risinajums": [
                     "Dots:  υ = 18 km/h;  t = 25 min",
                     "Jāaprēķina:  s = ?  (m; km)",
                     "Formulas:  s = υ · t",
                     "Aprēķins:  1) υ = 18 km/h = 18 : 3,6 = 5 m/s",
                     "                   2) t = 25 min = 25 · 60 s = 1500 s",
                     "                   3) s = υ · t = 5 m/s · 1500 s = "
                     "7500 m = 7,5 km",
                     "Atbilde:  s = 7500 m = 7,5 km.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — abas pārveides: 18 km/h = 5 m/s un "
                     "25 min = 1500 s;",
                     "1 p — pierakstīta formula s = υ·t un pareizs aprēķins;",
                     "1 p — atbilde ar mērvienībām, tostarp kilometros.",
                 ]},

                {"tips": "aprekins",
                 "virs": "Vienmērīgi paātrināta kustība", "punkti": 5,
                 "vieta": 7.0,
                 "teksts": "Automašīna sāk kustību no miera un 8 s laikā "
                           "sasniedz ātrumu 72 km/h. Aprēķini automašīnas "
                           "paātrinājumu un ceļu, ko tā veic šajā laikā!",
                 "risinajums": [
                     "Dots:  υ₀ = 0;  υ = 72 km/h;  t = 8 s",
                     "Jāaprēķina:  a = ?  (m/s²)    s = ?  (m)",
                     "Formulas:  a = (υ − υ₀) / t ;   s = a · t² / 2",
                     "Aprēķins:  1) υ = 72 km/h = 72 : 3,6 = 20 m/s",
                     "                   2) a = (20 m/s − 0) : 8 s = "
                     "2,5 m/s²",
                     "                   3) s = a · t² / 2 = 2,5 m/s² · "
                     "(8 s)² : 2 = 2,5 · 64 : 2 = 80 m",
                     "Atbilde:  a = 2,5 m/s²;  s = 80 m.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pārveide 72 km/h = 20 m/s;",
                     "1 p — pierakstītas abas formulas;",
                     "1 p — pareizi aprēķināts a = 2,5 m/s²;",
                     "1 p — pareizi aprēķināts s = 80 m un uzrakstīta "
                     "atbilde. Ceļu drīkst rēķināt arī caur vidējo ātrumu: "
                     "s = (0 + 20)/2 · 8 = 80 m.",
                 ]},

                {"tips": "aprekins", "virs": "Brīvā krišana", "punkti": 4,
                 "vieta": 6.5,
                 "teksts": "Akmeni bez sākuma ātruma nomet no tilta, un tas "
                           "krīt t = 2,0 s līdz ūdenim. Aprēķini tilta "
                           "augstumu virs ūdens un ātrumu, ar kādu akmens "
                           "sasniedz ūdeni! Pieņem, ka g = 10 m/s², gaisa "
                           "pretestību neņem vērā.",
                 "risinajums": [
                     "Dots:  υ₀ = 0;  t = 2,0 s;  g = 10 m/s²",
                     "Jāaprēķina:  h = ?  (m)    υ = ?  (m/s)",
                     "Formulas:  h = g · t² / 2 ;   υ = g · t",
                     "Aprēķins:  1) h = g · t² / 2 = 10 m/s² · (2,0 s)² : 2 = "
                     "10 · 4 : 2 = 20 m",
                     "                   2) υ = g · t = 10 m/s² · 2,0 s = "
                     "20 m/s",
                     "Atbilde:  h = 20 m;  υ = 20 m/s (jeb 72 km/h).",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas h = gt²/2 un υ = gt;",
                     "1 p — pareizi aprēķināts h = 20 m;",
                     "1 p — pareizi aprēķināts υ = 20 m/s un uzrakstīta "
                     "atbilde ar mērvienībām.",
                 ]},

                {"tips": "jautajumi", "virs": "Apstāšanās ceļš un drošība",
                 "punkti": 4, "vieta": 7.0,
                 "ievads": "Automašīna brauc ar ātrumu υ = 20 m/s. Vadītāja "
                           "reakcijas laiks ir t = 1,0 s, bet bremzēšanas "
                           "paātrinājuma modulis a = 5 m/s².",
                 "jaut": [
                     ("Aprēķini reakcijas ceļu s₁!", 1),
                     ("Aprēķini bremzēšanas ceļu s₂!", 1),
                     ("Aprēķini apstāšanās ceļu s!", 1),
                     ("Nosauc vienu faktoru, kas šo apstāšanās ceļu "
                      "palielinātu, un paskaidro, kāpēc!", 1),
                 ],
                 "atbildes": [
                     "1) s₁ = υ · t = 20 m/s · 1,0 s = 20 m.   (1 p)",
                     "2) s₂ = υ² / (2a) = (20 m/s)² : (2 · 5 m/s²) = "
                     "400 : 10 = 40 m.   (1 p)",
                     "3) s = s₁ + s₂ = 20 m + 40 m = 60 m.   (1 p)",
                     "4) Jebkurš pamatots faktors, piemēram: slapjš vai "
                     "apledojis ceļš — samazinās berze, tātad arī bremzēšanas "
                     "paātrinājums a, un s₂ = υ²/(2a) kļūst lielāks; vai "
                     "nogurums un telefona lietošana — aug reakcijas laiks, "
                     "tātad s₁.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kurš no lielumiem ir skalārs?",
                 ["ātrums", "spēks", "ceļš", "paātrinājums"], 2),
                ("Ķermenis pārvietojas pa pusapli ar rādiusu R. Cik liels ir "
                 "tā pārvietojums?",
                 ["πR", "2R", "2πR", "0"], 1),
                ("Cik km/h ir 20 m/s?",
                 ["72 km/h", "5,6 km/h", "200 km/h", "720 km/h"], 0),
                ("Ko υ(t) grafikā nozīmē horizontāla līnija?",
                 ["ķermenis stāv", "ķermenis brauc ar nemainīgu ātrumu",
                  "ķermenis paātrinās", "ķermenis bremzē"], 1),
                ("Ko rāda laukums zem υ(t) grafika?",
                 ["paātrinājumu", "masu", "ceļu", "laiku"], 2),
                ("Ja ķermenis bremzē, tad tā paātrinājums",
                 ["ir vērsts pretēji ātrumam", "ir nulle",
                  "ir vērsts tāpat kā ātrums", "vienmēr ir 9,8 m/s²"], 0),
                ("Cik liels ir sākuma ātrums kustībā x = 2 + 6t + 4t²?",
                 ["2 m/s", "4 m/s", "6 m/s", "8 m/s"], 2),
                ("Kāpēc gaisā papīra lapa krīt lēnāk par akmeni?",
                 ["papīram ir mazāka masa", "papīram ir mazāks g",
                  "akmenim ir lielāks brīvās krišanas paātrinājums",
                  "uz papīru gaisa pretestība iedarbojas relatīvi vairāk"], 3),
                ("Izpletņlēcēja robežātrums iestājas tad, kad",
                 ["gaisa pretestība kļūst vienāda ar smaguma spēku",
                  "atveras izpletnis", "samazinās lēcēja masa",
                  "gaisa pretestība kļūst nulle"], 0),
                ("Kurš faktors samazina tieši bremzēšanas paātrinājumu?",
                 ["liels braukšanas ātrums", "liels reakcijas laiks",
                  "gaišs diennakts laiks", "apledojis ceļa segums"], 3),
            ],
            "uzdevumi": [
                {"tips": "jautajumi", "virs": "Ceļš un pārvietojums",
                 "punkti": 3, "vieta": 5.5,
                 "ievads": "Skrējējs noskrien trīs pilnus apļus pa 400 m garu "
                           "stadiona celiņu un apstājas starta vietā.",
                 "jaut": [
                     ("Cik liels ir viņa veiktais ceļš s?", 1),
                     ("Cik liels ir viņa pārvietojums? Pamato atbildi!", 1),
                     ("Cits cilvēks noiet 60 m uz ziemeļiem un tad 80 m uz "
                      "austrumiem. Cik liels ir viņa pārvietojums?", 1),
                 ],
                 "atbildes": [
                     "1) s = 3 · 400 m = 1200 m.   (1 p)",
                     "2) Pārvietojums ir 0, jo skrējējs atgriežas starta "
                     "punktā — pārvietojums ir vektors no sākuma uz beigu "
                     "punktu, nevis trajektorijas garums.   (1 p)",
                     "3) Vektori ir perpendikulāri: s = √(60² + 80²) = "
                     "√(3600 + 6400) = √10000 = 100 m.   (1 p)",
                 ]},

                {"tips": "aprekins", "virs": "Vienmērīga kustība",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Vilciens brauc vienmērīgi ar ātrumu "
                           "υ = 108 km/h. Cik ilgā laikā tas veiks 45 km "
                           "garu ceļu? Izsaki atbildi arī minūtēs!",
                 "risinajums": [
                     "Dots:  υ = 108 km/h;  s = 45 km",
                     "Jāaprēķina:  t = ?  (s; min)",
                     "Formulas:  t = s / υ",
                     "Aprēķins:  1) υ = 108 km/h = 108 : 3,6 = 30 m/s",
                     "                   2) s = 45 km = 45 000 m",
                     "                   3) t = s / υ = 45 000 m : 30 m/s = "
                     "1500 s = 25 min",
                     "Atbilde:  t = 1500 s = 25 min.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — abas pārveides: 108 km/h = 30 m/s un "
                     "45 km = 45 000 m;",
                     "1 p — pierakstīta formula t = s/υ un pareizs aprēķins;",
                     "1 p — atbilde ar mērvienībām, tostarp minūtēs.",
                 ]},

                {"tips": "aprekins",
                 "virs": "Vienmērīgi paātrināta kustība", "punkti": 5,
                 "vieta": 7.0,
                 "teksts": "Automašīna, kas brauc ar ātrumu 54 km/h, "
                           "vienmērīgi bremzē un apstājas 6 s laikā. "
                           "Aprēķini paātrinājuma moduli un bremzēšanas ceļu!",
                 "risinajums": [
                     "Dots:  υ₀ = 54 km/h;  υ = 0;  t = 6 s",
                     "Jāaprēķina:  a = ?  (m/s²)    s = ?  (m)",
                     "Formulas:  a = (υ − υ₀) / t ;   s = (υ₀ + υ) / 2 · t",
                     "Aprēķins:  1) υ₀ = 54 km/h = 54 : 3,6 = 15 m/s",
                     "                   2) a = (0 − 15 m/s) : 6 s = "
                     "−2,5 m/s²;  modulis 2,5 m/s²",
                     "                   3) s = (15 m/s + 0) : 2 · 6 s = "
                     "7,5 m/s · 6 s = 45 m",
                     "Atbilde:  |a| = 2,5 m/s² (vērsts pretēji kustībai);  "
                     "s = 45 m.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pārveide 54 km/h = 15 m/s;",
                     "1 p — pierakstītas abas formulas;",
                     "1 p — pareizs a = −2,5 m/s² (vai modulis 2,5 m/s² ar "
                     "norādi, ka vērsts pretēji kustībai);",
                     "1 p — pareizs s = 45 m un uzrakstīta atbilde. Ceļu "
                     "drīkst rēķināt arī pēc s = υ₀t + at²/2.",
                 ]},

                {"tips": "aprekins", "virs": "Brīvā krišana", "punkti": 4,
                 "vieta": 6.5,
                 "teksts": "Ķermenis brīvi krīt no h = 45 m augstuma bez "
                           "sākuma ātruma. Aprēķini krišanas laiku un ātrumu, "
                           "ar kādu ķermenis sasniedz zemi! Pieņem, ka "
                           "g = 10 m/s², gaisa pretestību neņem vērā.",
                 "risinajums": [
                     "Dots:  υ₀ = 0;  h = 45 m;  g = 10 m/s²",
                     "Jāaprēķina:  t = ?  (s)    υ = ?  (m/s)",
                     "Formulas:  t = √(2h / g) ;   υ = g · t",
                     "Aprēķins:  1) t = √(2 · 45 m : 10 m/s²) = √9 s² = 3 s",
                     "                   2) υ = g · t = 10 m/s² · 3 s = "
                     "30 m/s",
                     "Atbilde:  t = 3 s;  υ = 30 m/s (jeb 108 km/h).",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas t = √(2h/g) un υ = gt;",
                     "1 p — pareizi aprēķināts t = 3 s;",
                     "1 p — pareizi aprēķināts υ = 30 m/s un uzrakstīta "
                     "atbilde ar mērvienībām.",
                 ]},

                {"tips": "jautajumi", "virs": "Apstāšanās ceļš un drošība",
                 "punkti": 4, "vieta": 7.0,
                 "ievads": "Automašīna brauc ar ātrumu υ = 15 m/s. Vadītāja "
                           "reakcijas laiks ir t = 1,2 s, bet bremzēšanas "
                           "paātrinājuma modulis a = 5 m/s².",
                 "jaut": [
                     ("Aprēķini reakcijas ceļu s₁!", 1),
                     ("Aprēķini bremzēšanas ceļu s₂!", 1),
                     ("Aprēķini apstāšanās ceļu s!", 1),
                     ("Kāpēc apdzīvotās vietās ātrums ir ierobežots līdz "
                      "50 km/h? Pamato ar formulu!", 1),
                 ],
                 "atbildes": [
                     "1) s₁ = υ · t = 15 m/s · 1,2 s = 18 m.   (1 p)",
                     "2) s₂ = υ² / (2a) = (15 m/s)² : (2 · 5 m/s²) = "
                     "225 : 10 = 22,5 m.   (1 p)",
                     "3) s = s₁ + s₂ = 18 m + 22,5 m = 40,5 m.   (1 p)",
                     "4) Tāpēc, ka s₂ = υ²/(2a) — bremzēšanas ceļš aug ar "
                     "ātruma KVADRĀTU: divreiz lielāks ātrums nozīmē "
                     "četrreiz garāku bremzēšanas ceļu (50 km/h ≈ 12 m, "
                     "100 km/h ≈ 48 m).   (1 p)",
                 ]},
            ],
        },
    ],
}
