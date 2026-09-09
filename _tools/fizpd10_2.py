# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. PD2 - Vienmērīga un nevienmērīga kustība (6.-23. st.)."""

PD = {
    "nr": 2,
    "klase": "10. klase",
    "nosaukums": "Vienmērīga un nevienmērīga kustība",
    "mape": "1. Ievads pētniecībā. Vienmērīga un nevienmērīga kustība",
    "fails": "PD2. Vienmērīga un nevienmērīga kustība_tt",
    "stundas": "6.-22.",
    "datums": "04.11.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda mehāniskās kustības aprakstu: ceļu un "
                "pārvietojumu, vienmērīgas kustības vienādojumu un "
                "grafikus, vidējo ātrumu, relatīvo kustību un mērījumu "
                "kļūdas.",
    "atgadne": [
        "v = s / t   ·   x = x₀ + vt   ·   v(vid) = s(kopā) / t(kopā)",
        "No km/h uz m/s dala ar 3,6   ·   no m/s uz km/h reizina ar 3,6",
        "Ātrumu saskaitīšana vienā taisnē:  v = v₁ + v₂ (vienā virzienā), "
        "v = v₁ − v₂ (pretējos virzienos)",
        "Δx = c / 2 analogai ierīcei   ·   ε = Δx / x · 100 %",
    ],
    "struktura": [
        ("1.", "Atšķir ceļu no pārvietojuma, lasa kustības grafikus, "
               "izvēlas atskaites sistēmu, novērtē mērījuma kļūdu",
         "6.-22.", 10),
        ("2.", "Nolasa x(t) grafiku: nosaka sākuma koordinātu, ātrumu un "
               "pieraksta kustības vienādojumu", "9., 10.", 5),
        ("3.", "Aprēķina vidējo ātrumu ceļā ar diviem posmiem", "11.", 5),
        ("4.", "Risina uzdevumu par divu ķermeņu satikšanos", "10., 19.", 5),
        ("5.", "Lieto ātrumu saskaitīšanu un novērtē mērījuma kļūdu",
         "18., 12.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kurš apgalvojums par ceļu un pārvietojumu ir pareizs?",
                 ["ceļš vienmēr ir vienāds ar pārvietojuma moduli",
                  "ceļš nekad nav mazāks par pārvietojuma moduli",
                  "pārvietojums vienmēr ir lielāks par ceļu",
                  "pārvietojums ir skalārs lielums"], 1),
                ("Ķermenis apiet apkārt stadiona apļveida celiņam un "
                 "atgriežas sākuma punktā. Cik liels ir pārvietojums?",
                 ["vienāds ar celiņa garumu", "puse no celiņa garuma",
                  "nulle", "nav nosakāms"], 2),
                ("Kustības vienādojums ir x = 5 + 3t (SI vienībās). Cik "
                 "liels ir ātrums?",
                 ["5 m/s", "8 m/s", "15 m/s", "3 m/s"], 3),
                ("Ko x(t) grafikā nozīmē horizontāla līnija?",
                 ["ķermenis kustas vienmērīgi",
                  "ķermenis atrodas miera stāvoklī",
                  "ķermenis kustas ar paātrinājumu",
                  "ķermenis maina virzienu"], 1),
                ("Ko v(t) grafikā nozīmē laukums zem līnijas?",
                 ["paātrinājumu", "ātrumu", "pārvietojumu", "laiku"], 2),
                ("Ķermenis puse ceļa veic ar ātrumu 20 m/s, otru pusi ar "
                 "60 m/s. Kāds ir vidējais ātrums?",
                 ["40 m/s", "30 m/s", "80 m/s", "20 m/s"], 1),
                ("Laiva peld pret straumi. Laivas ātrums pret ūdeni ir "
                 "5 m/s, straumes ātrums 2 m/s. Cik liels ir laivas ātrums "
                 "pret krastu?",
                 ["7 m/s", "5 m/s", "2,5 m/s", "3 m/s"], 3),
                ("Kurš no lielumiem raksturo mērījuma precizitāti?",
                 ["mērījuma vidējā vērtība", "mērierīces masa",
                  "relatīvā kļūda", "mērījumu skaits"], 2),
                ("Lineāla iedaļas vērtība ir 1 mm. Cik liela ir mērījuma "
                 "instrumenta absolūtā kļūda?",
                 ["1 mm", "0,5 mm", "0,1 mm", "2 mm"], 1),
                ("Kāpēc mērījumu atkārto vairākas reizes?",
                 ["lai iegūtu lielāku skaitli",
                  "lai samazinātu nejaušo kļūdu",
                  "lai mainītu mērierīci",
                  "lai palielinātu absolūto kļūdu"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Kustības vienādojums pēc grafika", "punkti": 5,
                 "note": "Ķermeņa koordināta mainās pēc grafika: pie t = 0 "
                         "x = 20 m, pie t = 10 s x = 70 m. Aizpildi rindas! "
                         "Par katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Sākuma koordināta  x₀ = ..................... m",
                      "20 m"),
                     ("Pārvietojums 10 s laikā  s = ..................... m",
                      "50 m"),
                     ("Ātrums  v = ..................... m/s", "5 m/s"),
                     ("Kustības vienādojums  x = .....................",
                      "x = 20 + 5t  (SI vienībās)"),
                     ("Koordināta pie t = 20 s  x = ..................... m",
                      "120 m"),
                 ]},

                {"tips": "aprekins", "virs": "Vidējais ātrums", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Automašīna 40 km garu ceļa posmu nobrauc ar "
                           "ātrumu 80 km/h, bet nākamos 60 km - ar ātrumu "
                           "60 km/h. Aprēķini vidējo ātrumu visā ceļā! "
                           "Atbildi izsaki arī m/s.",
                 "risinajums": [
                     "Dots:  s₁ = 40 km;  v₁ = 80 km/h;  s₂ = 60 km;  "
                     "v₂ = 60 km/h",
                     "Jāaprēķina:  v(vid) = ?",
                     "Formulas:  t = s / v;  v(vid) = (s₁ + s₂) / (t₁ + t₂)",
                     "Aprēķins:  1) t₁ = 40 km : 80 km/h = 0,50 h",
                     "                   2) t₂ = 60 km : 60 km/h = 1,00 h",
                     "                   3) s = 40 + 60 = 100 km;  "
                     "t = 0,50 + 1,00 = 1,50 h",
                     "                   4) v(vid) = 100 km : 1,50 h ≈ "
                     "66,7 km/h",
                     "                   5) 66,7 : 3,6 ≈ 18,5 m/s",
                     "Atbilde:  v(vid) ≈ 67 km/h ≈ 19 m/s.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» un «Jāaprēķina»;",
                     "1 p - pareiza formula v(vid) = s(kopā) / t(kopā) "
                     "(nevis ātrumu vidējais aritmētiskais);",
                     "2 p - pareizi aprēķināti abi laiki un vidējais ātrums;",
                     "1 p - atbilde ar mērvienību un pareiza pārveide m/s.",
                 ]},

                {"tips": "aprekins", "virs": "Divu ķermeņu satikšanās",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Divi riteņbraucēji vienlaikus izbrauc viens otram "
                           "pretī no punktiem, kas atrodas 900 m attālumā. "
                           "Pirmā ātrums ir 6,0 m/s, otrā - 4,0 m/s. Pēc cik "
                           "ilga laika viņi satiksies un cik tālu no pirmā "
                           "izbraukšanas vietas?",
                 "risinajums": [
                     "Dots:  L = 900 m;  v₁ = 6,0 m/s;  v₂ = 4,0 m/s",
                     "Jāaprēķina:  t = ?  s₁ = ?",
                     "Formulas:  x₁ = v₁t;  x₂ = L − v₂t;  x₁ = x₂",
                     "Aprēķins:  1) v₁t = L − v₂t",
                     "                   2) t = L / (v₁ + v₂) = 900 m : "
                     "10,0 m/s = 90 s",
                     "                   3) s₁ = v₁t = 6,0 m/s · 90 s = 540 m",
                     "Atbilde:  satiksies pēc t = 90 s, 540 m no pirmā "
                     "izbraukšanas vietas.",
                 ],
                 "kriteriji": [
                     "1 p - izvēlēta atskaites sistēma un pierakstīti abi "
                     "kustības vienādojumi;",
                     "1 p - pierakstīts satikšanās nosacījums x₁ = x₂;",
                     "2 p - pareizi aprēķināts laiks t = 90 s;",
                     "1 p - pareizi aprēķināts attālums 540 m ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Relatīvā kustība un kļūdas",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Kuģis peld pa upi ar ātrumu 8,0 m/s pret ūdeni. "
                           "Straumes ātrums ir 2,0 m/s. Attālumu starp "
                           "piestātnēm skolēns izmērīja kartē un ieguva "
                           "s = 4,80 km ar absolūto kļūdu Δs = 0,05 km.",
                 "jaut": [
                     ("Aprēķini kuģa ātrumu pret krastu, peldot pa straumi!",
                      1),
                     ("Aprēķini kuģa ātrumu pret krastu, peldot pret "
                      "straumi!", 1),
                     ("Cik ilgi kuģis peld pa straumi 4,80 km garo posmu?",
                      1),
                     ("Aprēķini attāluma mērījuma relatīvo kļūdu!", 1),
                     ("Pieraksti mērījuma rezultātu formā s = (s ± Δs) km!",
                      1),
                 ],
                 "atbildes": [
                     "1) v = 8,0 + 2,0 = 10,0 m/s.   (1 p)",
                     "2) v = 8,0 − 2,0 = 6,0 m/s.   (1 p)",
                     "3) t = s / v = 4800 m : 10,0 m/s = 480 s = 8,0 min.   "
                     "(1 p)",
                     "4) ε = Δs / s · 100 % = 0,05 : 4,80 · 100 % ≈ 1,0 %.   "
                     "(1 p)",
                     "5) s = (4,80 ± 0,05) km.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kurš apgalvojums par ceļu un pārvietojumu ir pareizs?",
                 ["pārvietojums ir vektors, ceļš - skalārs",
                  "abi lielumi ir vektori",
                  "ceļš var būt negatīvs",
                  "pārvietojums nekad nav mazāks par ceļu"], 0),
                ("Ķermenis pārvietojas 3 m uz austrumiem un pēc tam 4 m uz "
                 "ziemeļiem. Cik liels ir pārvietojuma modulis?",
                 ["7 m", "1 m", "5 m", "12 m"], 2),
                ("Kustības vienādojums ir x = −4 + 2t (SI vienībās). Kāda ir "
                 "sākuma koordināta?",
                 ["2 m", "−4 m", "4 m", "−2 m"], 1),
                ("Ko x(t) grafikā nozīmē līnijas slīpums?",
                 ["pārvietojumu", "laiku", "paātrinājumu", "ātrumu"], 3),
                ("Divu ķermeņu x(t) grafiki krustojas. Ko tas nozīmē?",
                 ["ķermeņiem ir vienāds ātrums",
                  "ķermeņi atrodas vienā vietā vienā laikā",
                  "ķermeņi apstājas",
                  "ķermeņi maina virzienu"], 1),
                ("Ķermenis pirmo stundu brauc ar 40 km/h, otro - ar "
                 "60 km/h. Kāds ir vidējais ātrums?",
                 ["50 km/h", "48 km/h", "100 km/h", "45 km/h"], 0),
                ("Lidmašīna lido ar ātrumu 200 m/s pret gaisu, pretvējš ir "
                 "20 m/s. Cik liels ir ātrums pret zemi?",
                 ["220 m/s", "180 m/s", "200 m/s", "20 m/s"], 1),
                ("Ko nozīmē mērījuma absolūtā kļūda?",
                 ["mērījuma vidējo vērtību",
                  "mērījumu skaitu",
                  "robežu, kādā rezultāts var atšķirties no patiesās "
                  "vērtības",
                  "mērierīces cenu"], 2),
                ("Hronometra iedaļas vērtība ir 0,2 s. Cik liela ir "
                 "instrumenta absolūtā kļūda?",
                 ["0,2 s", "0,4 s", "0,02 s", "0,1 s"], 3),
                ("Kurš mērījums ir precīzāks: 1) 10,0 cm ar Δ = 0,1 cm; "
                 "2) 100,0 cm ar Δ = 0,5 cm?",
                 ["pirmais", "otrais", "abi vienādi", "nav nosakāms"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Kustības vienādojums pēc grafika", "punkti": 5,
                 "note": "Ķermeņa koordināta mainās pēc grafika: pie t = 0 "
                         "x = 60 m, pie t = 20 s x = 20 m. Aizpildi rindas! "
                         "Par katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Sākuma koordināta  x₀ = ..................... m",
                      "60 m"),
                     ("Pārvietojums 20 s laikā  s = ..................... m",
                      "−40 m (modulis 40 m)"),
                     ("Ātrums  v = ..................... m/s", "−2 m/s"),
                     ("Kustības vienādojums  x = .....................",
                      "x = 60 − 2t  (SI vienībās)"),
                     ("Laiks, kad ķermenis būs punktā x = 0:  "
                      "t = ..................... s", "30 s"),
                 ]},

                {"tips": "aprekins", "virs": "Vidējais ātrums", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Vilciens 60 km garu posmu nobrauc ar ātrumu "
                           "120 km/h, bet nākamos 30 km - ar ātrumu "
                           "60 km/h. Aprēķini vidējo ātrumu visā ceļā! "
                           "Atbildi izsaki arī m/s.",
                 "risinajums": [
                     "Dots:  s₁ = 60 km;  v₁ = 120 km/h;  s₂ = 30 km;  "
                     "v₂ = 60 km/h",
                     "Jāaprēķina:  v(vid) = ?",
                     "Formulas:  t = s / v;  v(vid) = (s₁ + s₂) / (t₁ + t₂)",
                     "Aprēķins:  1) t₁ = 60 km : 120 km/h = 0,50 h",
                     "                   2) t₂ = 30 km : 60 km/h = 0,50 h",
                     "                   3) s = 90 km;  t = 1,00 h",
                     "                   4) v(vid) = 90 km : 1,00 h = 90 km/h",
                     "                   5) 90 : 3,6 = 25 m/s",
                     "Atbilde:  v(vid) = 90 km/h = 25 m/s.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» un «Jāaprēķina»;",
                     "1 p - pareiza formula v(vid) = s(kopā) / t(kopā);",
                     "2 p - pareizi aprēķināti abi laiki un vidējais ātrums;",
                     "1 p - atbilde ar mērvienību un pareiza pārveide m/s.",
                 ]},

                {"tips": "aprekins", "virs": "Divu ķermeņu satikšanās",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "No viena punkta vienā virzienā izbrauc "
                           "riteņbraucējs ar ātrumu 5,0 m/s. Pēc 60 s no tā "
                           "paša punkta izbrauc motociklists ar ātrumu "
                           "15 m/s. Pēc cik ilga laika no motociklista "
                           "izbraukšanas viņš panāks riteņbraucēju un cik "
                           "tālu no starta punkta tas notiks?",
                 "risinajums": [
                     "Dots:  v₁ = 5,0 m/s;  v₂ = 15 m/s;  Δt = 60 s",
                     "Jāaprēķina:  t = ?  s = ?",
                     "Formulas:  x₁ = v₁(t + Δt);  x₂ = v₂t;  x₁ = x₂",
                     "Aprēķins:  1) v₁(t + Δt) = v₂t",
                     "                   2) 5,0t + 300 = 15t",
                     "                   3) 10t = 300;  t = 30 s",
                     "                   4) s = v₂t = 15 m/s · 30 s = 450 m",
                     "Atbilde:  panāks pēc 30 s, 450 m no starta punkta.",
                 ],
                 "kriteriji": [
                     "1 p - izvēlēta atskaites sistēma un ņemta vērā "
                     "60 s starpība;",
                     "1 p - pierakstīts nosacījums x₁ = x₂;",
                     "2 p - pareizi atrisināts vienādojums (t = 30 s);",
                     "1 p - pareizi aprēķināts attālums 450 m ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Relatīvā kustība un kļūdas",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Laiva peld pa upi ar ātrumu 6,0 m/s pret ūdeni. "
                           "Straumes ātrums ir 1,5 m/s. Posma garumu skolēns "
                           "izmērīja un ieguva s = 3,00 km ar absolūto kļūdu "
                           "Δs = 0,06 km.",
                 "jaut": [
                     ("Aprēķini laivas ātrumu pret krastu, peldot pa "
                      "straumi!", 1),
                     ("Aprēķini laivas ātrumu pret krastu, peldot pret "
                      "straumi!", 1),
                     ("Cik ilgi laiva peld pret straumi 3,00 km garo posmu?",
                      1),
                     ("Aprēķini attāluma mērījuma relatīvo kļūdu!", 1),
                     ("Pieraksti mērījuma rezultātu formā s = (s ± Δs) km!",
                      1),
                 ],
                 "atbildes": [
                     "1) v = 6,0 + 1,5 = 7,5 m/s.   (1 p)",
                     "2) v = 6,0 − 1,5 = 4,5 m/s.   (1 p)",
                     "3) t = s / v = 3000 m : 4,5 m/s ≈ 667 s ≈ 11 min.   "
                     "(1 p)",
                     "4) ε = Δs / s · 100 % = 0,06 : 3,00 · 100 % = 2,0 %.   "
                     "(1 p)",
                     "5) s = (3,00 ± 0,06) km.   (1 p)",
                 ]},
            ],
        },
    ],
}
