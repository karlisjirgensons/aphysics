# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. PD6 - Enerģija, darbs un impulss (83.-98. st.)."""

PD = {
    "nr": 6,
    "klase": "10. klase",
    "nosaukums": "Enerģija, darbs un impulss",
    "mape": "5. Enerģija un darbs",
    "fails": "PD6. Enerģija, darbs un impulss_tt",
    "stundas": "83.-96.",
    "datums": "21.05.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Gada noslēguma pārbaudes darbs. Pārbauda mehānisko darbu, "
                "jaudu, lietderības koeficientu, kinētisko un potenciālo "
                "enerģiju, mehāniskās enerģijas un impulsa nezūdamības "
                "likumus.",
    "atgadne": [
        "A = F·s·cos α   ·   P = A / t = F·v   ·   η = A(lietd.) / "
        "A(patēr.) · 100 %",
        "Ek = mv² / 2   ·   Ep = mgh   ·   Ep(atsp.) = kx² / 2",
        "Enerģijas nezūdamība:  Ek₁ + Ep₁ = Ek₂ + Ep₂ (bez berzes)",
        "p = mv   ·   Ft = Δp   ·   m₁v₁ + m₂v₂ = m₁u₁ + m₂u₂   ·   "
        "g = 10 m/s²",
    ],
    "struktura": [
        ("1.", "Skaidro darbu, jaudu, enerģijas veidus un nezūdamības "
               "likumus", "83.-96.", 10),
        ("2.", "Aizpilda enerģijas un jaudas lielumu tabulu", "83.-87.", 5),
        ("3.", "Aprēķina darbu, jaudu un lietderības koeficientu", "84.", 5),
        ("4.", "Lieto mehāniskās enerģijas nezūdamības likumu", "88.", 5),
        ("5.", "Lieto impulsa nezūdamības likumu sadursmē", "92.-95.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kad spēks neveic darbu?",
                 ["kad spēks ir liels",
                  "kad spēks perpendikulārs pārvietojumam",
                  "kad ķermenis kustas ātri",
                  "kad spēks vērsts pa kustību"], 1),
                ("Kāda ir darba SI mērvienība?",
                 ["vats", "ņūtons", "džouls", "paskāls"], 2),
                ("Ķermeņa ātrumu palielina 2 reizes. Kā mainās kinētiskā "
                 "enerģija?",
                 ["palielinās 2 reizes", "palielinās 4 reizes",
                  "nemainās", "samazinās 2 reizes"], 1),
                ("Jauda 500 W nozīmē, ka:",
                 ["darbs ir 500 J", "katrā sekundē veic 500 J darbu",
                  "spēks ir 500 N", "enerģija ir 500 J/kg"], 1),
                ("Lietderības koeficients nekad nevar būt:",
                 ["mazāks par 50 %", "lielāks par 100 %",
                  "vienāds ar 80 %", "mazāks par 10 %"], 1),
                ("Ķermenis brīvi krīt. Kas notiek ar tā mehānisko enerģiju "
                 "(bez gaisa pretestības)?",
                 ["pieaug", "samazinās", "nemainās",
                  "vispirms pieaug, tad samazinās"], 2),
                ("Kāda ir impulsa SI mērvienība?",
                 ["kg·m/s", "N/s", "J·s", "kg/s"], 0),
                ("Kāpēc automašīnās izmanto drošības spilvenus?",
                 ["lai palielinātu impulsa izmaiņu",
                  "lai pagarinātu trieciena laiku un samazinātu spēku",
                  "lai palielinātu ātrumu",
                  "lai samazinātu masu"], 1),
                ("Kurā triecienā saglabājas gan impulss, gan kinētiskā "
                 "enerģija?",
                 ["neelastīgā", "absolūti elastīgā", "jebkurā",
                  "nevienā"], 1),
                ("Divas ragaviņas stumj viena otru uz ledus. Ko var teikt "
                 "par sistēmas impulsu?",
                 ["palielinās", "samazinās", "paliek nemainīgs",
                  "kļūst nulle tikai beigās"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Enerģija, darbs un jauda",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.  (g = 10 m/s²)",
                 "rindas": [
                     ("Ek 4,0 kg smagam ķermenim pie v = 5,0 m/s  "
                      "Ek = ..................... J", "50 J"),
                     ("Ep 2,0 kg smagam ķermenim 8,0 m augstumā  "
                      "Ep = ..................... J", "160 J"),
                     ("Jaudas SI mērvienība  [P] = .....................",
                      "vats (W)"),
                     ("Darbs, ceļot 50 N smagu somu 2,0 m augstumā  "
                      "A = ..................... J", "100 J"),
                     ("Impulss 3,0 kg smagam ķermenim pie v = 4,0 m/s  "
                      "p = ..................... kg·m/s", "12 kg·m/s"),
                 ]},

                {"tips": "aprekins", "virs": "Jauda un lietderība",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Celtnis 30 s laikā paceļ 500 kg smagu kravu 12 m "
                           "augstumā. Celtņa dzinēja patērētā jauda ir "
                           "2,5 kW. Aprēķini lietderīgo darbu, lietderīgo "
                           "jaudu un celtņa lietderības koeficientu! "
                           "(g = 10 m/s²)",
                 "risinajums": [
                     "Dots:  m = 500 kg;  h = 12 m;  t = 30 s;  "
                     "P(pat) = 2,5 kW = 2500 W",
                     "Jāaprēķina:  A = ?  P = ?  η = ?",
                     "Formulas:  A = mgh;  P = A / t;  η = P / P(pat) · 100 %",
                     "Aprēķins:  1) A = 500 · 10 · 12 = 6,0 · 10⁴ J",
                     "                   2) P = 6,0 · 10⁴ : 30 = 2,0 · 10³ W",
                     "                   3) η = 2000 : 2500 · 100 % = 80 %",
                     "Atbilde:  A = 60 kJ;  P = 2,0 kW;  η = 80 %.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» ar SI vienībām;",
                     "1 p - pierakstītas formulas A = mgh un P = A/t;",
                     "2 p - pareizi aprēķināts darbs un lietderīgā jauda;",
                     "1 p - pareizs lietderības koeficients procentos.",
                 ]},

                {"tips": "aprekins", "virs": "Enerģijas nezūdamība",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Bumbiņu bez sākuma ātruma nolaiž no 5,0 m "
                           "augstuma. Gaisa pretestību neievēro, "
                           "g = 10 m/s². Aprēķini bumbiņas ātrumu tieši "
                           "pirms zemes un ātrumu 1,0 m augstumā virs zemes!",
                 "risinajums": [
                     "Dots:  h = 5,0 m;  v₀ = 0;  h₂ = 1,0 m;  g = 10 m/s²",
                     "Jāaprēķina:  v = ?  v₂ = ?",
                     "Formulas:  mgh = mv² / 2;  mgh = mgh₂ + mv₂² / 2",
                     "Aprēķins:  1) v = √(2gh) = √(2 · 10 · 5,0) = √100 = "
                     "10 m/s",
                     "                   2) v₂ = √(2g(h − h₂)) = "
                     "√(2 · 10 · 4,0)",
                     "                   3) v₂ = √80 ≈ 8,9 m/s",
                     "Atbilde:  v = 10 m/s;  v₂ ≈ 8,9 m/s.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīts enerģijas nezūdamības likums;",
                     "1 p - izteikts ātrums v = √(2gh);",
                     "2 p - pareizs ātrums pie zemes ar mērvienību;",
                     "1 p - pareizs ātrums 1,0 m augstumā.",
                 ]},

                {"tips": "jautajumi", "virs": "Impulsa nezūdamība",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Uz gludas horizontālas virsmas 3,0 kg smags "
                           "ratiņš, kas kustas ar ātrumu 4,0 m/s, saduras ar "
                           "stāvošu 1,0 kg smagu ratiņu un pēc sadursmes "
                           "abi kustas kopā.",
                 "jaut": [
                     ("Aprēķini sistēmas impulsu pirms sadursmes!", 1),
                     ("Pieraksti impulsa nezūdamības likumu šai sadursmei!",
                      1),
                     ("Aprēķini ratiņu kopīgo ātrumu pēc sadursmes!", 1),
                     ("Aprēķini kinētisko enerģiju pirms un pēc sadursmes!",
                      1),
                     ("Pamato, kāpēc kinētiskā enerģija nesaglabājas!", 1),
                 ],
                 "atbildes": [
                     "1) p = m₁v₁ = 3,0 · 4,0 = 12 kg·m/s.   (1 p)",
                     "2) m₁v₁ = (m₁ + m₂)u.   (1 p)",
                     "3) u = 12 : 4,0 = 3,0 m/s.   (1 p)",
                     "4) Ek(pirms) = 3,0 · 4,0² : 2 = 24 J;  "
                     "Ek(pēc) = 4,0 · 3,0² : 2 = 18 J.   (1 p)",
                     "5) Sadursme ir neelastīga: daļa kinētiskās enerģijas "
                     "(6 J) pārvēršas iekšējā enerģijā un skaņā, tāpēc "
                     "saglabājas tikai impulss.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kad spēka veiktais darbs ir negatīvs?",
                 ["kad spēks vērsts pa kustību",
                  "kad spēks vērsts pretēji pārvietojumam",
                  "kad spēks perpendikulārs pārvietojumam",
                  "darbs nekad nav negatīvs"], 1),
                ("Kāda ir jaudas SI mērvienība?",
                 ["džouls", "ņūtons", "vats", "kilovatstunda"], 2),
                ("Ķermeņa augstumu palielina 3 reizes. Kā mainās potenciālā "
                 "enerģija?",
                 ["nemainās", "palielinās 3 reizes",
                  "palielinās 9 reizes", "samazinās 3 reizes"], 1),
                ("Ko nozīmē, ka ierīces lietderības koeficients ir 25 %?",
                 ["ceturtā daļa patērētās enerģijas kļūst par lietderīgu "
                  "darbu",
                  "ierīce patērē 25 J", "ierīce strādā 25 minūtes",
                  "ierīces jauda ir 25 W"], 0),
                ("Svārsts svārstās bez berzes. Kur tā kinētiskā enerģija ir "
                 "vislielākā?",
                 ["augstākajā punktā", "zemākajā punktā",
                  "vidū starp tiem", "visur vienāda"], 1),
                ("Kas ir spēka impulss?",
                 ["Fs", "Ft", "mv²", "mgh"], 1),
                ("Kāda ir kinētiskās enerģijas SI mērvienība?",
                 ["vats", "džouls", "ņūtons", "kg·m/s"], 1),
                ("Kad izpildās impulsa nezūdamības likums?",
                 ["vienmēr", "slēgtā sistēmā",
                  "tikai elastīgā triecienā", "tikai miera stāvoklī"], 1),
                ("Divi vienādas masas ķermeņi kustas viens otram pretī ar "
                 "vienādiem ātrumiem un saplūst. Kāds ir to ātrums pēc "
                 "sadursmes?",
                 ["divkāršs", "tāds pats", "nulle", "puse"], 2),
                ("Kāpēc lecot no augstuma jāsaliec ceļi?",
                 ["lai samazinātu impulsa izmaiņu",
                  "lai pagarinātu bremzēšanas laiku un samazinātu spēku",
                  "lai palielinātu enerģiju",
                  "lai palielinātu masu"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Enerģija, darbs un jauda",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.  (g = 10 m/s²)",
                 "rindas": [
                     ("Ek 2,0 kg smagam ķermenim pie v = 6,0 m/s  "
                      "Ek = ..................... J", "36 J"),
                     ("Ep 5,0 kg smagam ķermenim 4,0 m augstumā  "
                      "Ep = ..................... J", "200 J"),
                     ("Enerģijas SI mērvienība  [E] = .....................",
                      "džouls (J)"),
                     ("Jauda, ja A = 900 J un t = 30 s  P = ..............."
                      "...... W", "30 W"),
                     ("Impulss 0,50 kg smagai bumbai pie v = 20 m/s  "
                      "p = ..................... kg·m/s", "10 kg·m/s"),
                 ]},

                {"tips": "aprekins", "virs": "Jauda un lietderība",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Sūknis 60 s laikā pacēla 900 kg ūdens 10 m "
                           "augstumā. Sūkņa patērētā jauda ir 2,0 kW. "
                           "Aprēķini lietderīgo darbu, lietderīgo jaudu un "
                           "sūkņa lietderības koeficientu! (g = 10 m/s²)",
                 "risinajums": [
                     "Dots:  m = 900 kg;  h = 10 m;  t = 60 s;  "
                     "P(pat) = 2,0 kW = 2000 W",
                     "Jāaprēķina:  A = ?  P = ?  η = ?",
                     "Formulas:  A = mgh;  P = A / t;  η = P / P(pat) · 100 %",
                     "Aprēķins:  1) A = 900 · 10 · 10 = 9,0 · 10⁴ J",
                     "                   2) P = 9,0 · 10⁴ : 60 = 1,5 · 10³ W",
                     "                   3) η = 1500 : 2000 · 100 % = 75 %",
                     "Atbilde:  A = 90 kJ;  P = 1,5 kW;  η = 75 %.",
                 ],
                 "kriteriji": [
                     "1 p - pieraksts «Dots» ar SI vienībām;",
                     "1 p - pierakstītas formulas A = mgh un P = A/t;",
                     "2 p - pareizi aprēķināts darbs un lietderīgā jauda;",
                     "1 p - pareizs lietderības koeficients procentos.",
                 ]},

                {"tips": "aprekins", "virs": "Enerģijas nezūdamība",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Bumbiņu izsviež vertikāli augšup ar ātrumu "
                           "12 m/s. Gaisa pretestību neievēro, g = 10 m/s². "
                           "Aprēķini maksimālo pacelšanās augstumu un "
                           "bumbiņas ātrumu 3,0 m augstumā!",
                 "risinajums": [
                     "Dots:  v₀ = 12 m/s;  h₂ = 3,0 m;  g = 10 m/s²",
                     "Jāaprēķina:  h = ?  v₂ = ?",
                     "Formulas:  mv₀² / 2 = mgh;  mv₀²/2 = mgh₂ + mv₂²/2",
                     "Aprēķins:  1) h = v₀² / (2g) = 144 : 20 = 7,2 m",
                     "                   2) v₂² = v₀² − 2gh₂ = 144 − 60 = 84",
                     "                   3) v₂ = √84 ≈ 9,2 m/s",
                     "Atbilde:  h = 7,2 m;  v₂ ≈ 9,2 m/s.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīts enerģijas nezūdamības likums;",
                     "1 p - izteikts augstums h = v₀² / (2g);",
                     "2 p - pareizs augstums 7,2 m ar mērvienību;",
                     "1 p - pareizs ātrums 3,0 m augstumā.",
                 ]},

                {"tips": "jautajumi", "virs": "Impulsa nezūdamība",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Uz gludas horizontālas virsmas 60 kg smags "
                           "cilvēks stāv uz 40 kg smaga plosta. Cilvēks "
                           "atgrūžas un aizpeld ar ātrumu 2,0 m/s. Sistēma "
                           "sākumā atradās miera stāvoklī.",
                 "jaut": [
                     ("Aprēķini sistēmas impulsu pirms atgrūšanās!", 1),
                     ("Pieraksti impulsa nezūdamības likumu šai situācijai!",
                      1),
                     ("Aprēķini plosta ātrumu pēc atgrūšanās!", 1),
                     ("Nosaki plosta kustības virzienu un pamato!", 1),
                     ("Aprēķini sistēmas kinētisko enerģiju pēc "
                      "atgrūšanās un paskaidro, no kurienes tā radusies!",
                      1),
                 ],
                 "atbildes": [
                     "1) p = 0, jo sistēma bija miera stāvoklī.   (1 p)",
                     "2) 0 = m₁v₁ + m₂v₂.   (1 p)",
                     "3) v₂ = −m₁v₁ / m₂ = −60 · 2,0 : 40 = −3,0 m/s "
                     "(modulis 3,0 m/s).   (1 p)",
                     "4) Plosts kustas pretējā virzienā cilvēkam, jo "
                     "kopējam impulsam jāpaliek nullei.   (1 p)",
                     "5) Ek = 60 · 2,0²/2 + 40 · 3,0²/2 = 120 + 180 = 300 J; "
                     "tā radusies no cilvēka muskuļu ķīmiskās (iekšējās) "
                     "enerģijas.   (1 p)",
                 ]},
            ],
        },
    ],
}
