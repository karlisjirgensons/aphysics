# -*- coding: utf-8 -*-
"""PD6 — Šķidrumi un vides fizikālie faktori (8.1.–8.6. un 9.1.–9.2. stunda).

Darbs aptver divus tematus, kas plānā apvienoti vienā pārbaudes darbā,
tāpēc tas pats fails tiek ierakstīts gan 8., gan 9. temata mapē.
"""

PD = {
    "nr": 6,
    "nosaukums": "Šķidrumi un vides fizikālie faktori",
    "mape": "8. Šķidrumi dabā un tehnikā",
    "fails": "PD6. Šķidrumi un vides fizikālie faktori",
    # Darbs vērtē abus tematus, tāpēc tas pats fails ir arī 9. temata mapē.
    "papildu_mapes": ["9. Vides faktoru ietekme uz cilvēka organismu"],
    "stundas": "8.1.–8.6. un 9.1.–9.2.",
    "datums": "29.01.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda šķidrumu blīvumu un slāņošanos, "
                "hidrostatisko spiedienu, Paskāla likumu un hidrauliku, "
                "Arhimēda spēku, virsmas spraigumu un kapilaritāti, kā arī "
                "trokšņa, apgaismojuma un starojuma ietekmi uz cilvēku.",
    "atgadne": [
        "ρ = m / V   ·   F = m · g   ·   g = 10 m/s²   ·   "
        "p₀ = 1,0 · 10⁵ Pa",
        "p = ρ · g · h   ·   p(kopā) = p₀ + ρ · g · h   ·   "
        "F(A) = ρ(šķidruma) · g · V(iegremdētā daļa)",
        "F₁ / S₁ = F₂ / S₂   ·   F₁ · s₁ = F₂ · s₂   ·   E = I / r²   ·   "
        "E₁ · r₁² = E₂ · r₂²",
        "1 cm³ = 10⁻⁶ m³  ·  1 cm² = 10⁻⁴ m²  ·  +10 dB = 10 reižu lielāka "
        "skaņas intensitāte",
    ],
    "struktura": [
        ("1.", "Raksturo šķidrumu blīvumu un slāņošanos, hidrostatisko "
               "spiedienu, peldēšanas nosacījumus, kapilaritāti, trokšņa un "
               "starojuma ietekmi", "8.1.–9.2.", 10),
        ("2.", "Aprēķina hidrostatisko un kopējo spiedienu dziļumā",
         "8.2.", 5),
        ("3.", "Aprēķina Arhimēda spēku un nosaka, vai ķermenis peld vai "
               "grimst", "8.4.", 5),
        ("4.", "Lieto Paskāla likumu hidrauliskās sistēmas aprēķinam un "
               "izprot zelta likumu", "8.3.", 4),
        ("5.", "Aprēķina apgaismojumu pēc attāluma un izvērtē trokšņa "
               "līmeni", "9.1.", 3),
        ("6.", "Nošķir jonizējošu starojumu no nejonizējoša un izvērtē "
               "informācijas avota ticamību", "9.2.", 3),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("No kā NAV atkarīgs hidrostatiskais spiediens?",
                 ["no šķidruma blīvuma", "no dziļuma",
                  "no brīvās krišanas paātrinājuma g", "no trauka formas"], 3),
                ("Ko aprēķina pēc formulas p = ρ · g · h?",
                 ["kopējo spiedienu kopā ar atmosfēras spiedienu",
                  "spiedienu, ko rada šķidruma stabs",
                  "cēlējspēku", "virsmas spraigumu"], 1),
                ("Kura blīvumu lieto Arhimēda spēka formulā "
                 "F(A) = ρ · g · V?",
                 ["ķermeņa blīvumu", "gaisa blīvumu", "šķidruma blīvumu",
                  "ķermeņa un šķidruma vidējo blīvumu"], 2),
                ("Kāpēc tērauda kuģis peld, lai gan tērauda blīvums ir "
                 "7800 kg/m³?",
                 ["tērauds ūdenī kļūst vieglāks",
                  "kuģa vidējais blīvums kopā ar gaisu korpusā ir mazāks par "
                  "ūdens blīvumu",
                  "ūdens spiediens kuģi notur virspusē",
                  "kuģis peld tikai tāpēc, ka kustas"], 1),
                ("Kurš šķidrums peldēs virs ūdens (ρ = 1000 kg/m³)?",
                 ["augu eļļa (920 kg/m³)", "dzīvsudrabs (13 600 kg/m³)",
                  "glicerīns (1260 kg/m³)", "jūras ūdens (1025 kg/m³)"], 0),
                ("Ko apgalvo Paskāla likums?",
                 ["spiediens šķidrumā pārnesas tikai lejup",
                  "spiediens šķidrumā pārnesas uz visām pusēm vienādi un "
                  "nemazināts",
                  "spiediens samazinās, attālinoties no virzuļa",
                  "spiediens ir atkarīgs no trauka formas"], 1),
                ("Hidrauliskajā presē S₁ = 5 cm², S₂ = 100 cm². Cik liels ir "
                 "spēka ieguvums?",
                 ["5", "100", "500", "20"], 3),
                ("Kāpēc brīvi krītošs ūdens piliens ir apaļš?",
                 ["gravitācijas dēļ", "gaisa spiediena dēļ",
                  "virsmas spraiguma dēļ — lodei ir vismazākā virsma pie "
                  "dotā tilpuma",
                  "kapilaritātes dēļ"], 2),
                ("Ja attālums no lampas palielinās divas reizes, "
                 "apgaismojums",
                 ["samazinās 4 reizes", "samazinās 2 reizes", "nemainās",
                  "palielinās 2 reizes"], 0),
                ("Kurš starojums ir jonizējošs?",
                 ["radioviļņi", "mikroviļņi", "redzamā gaisma",
                  "rentgenstarojums"], 3),
            ],
            "uzdevumi": [
                {"tips": "aprekins", "virs": "Spiediens šķidrumā",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Nirējs atrodas h = 25 m dziļumā jūrā. Jūras "
                           "ūdens blīvums ir ρ = 1025 kg/m³, atmosfēras "
                           "spiediens p₀ = 1,0 · 10⁵ Pa, g = 10 m/s². "
                           "Aprēķini spiedienu, ko rada ūdens stabs, un "
                           "kopējo spiedienu, kas darbojas uz nirēju!",
                 "risinajums": [
                     "Dots:  h = 25 m;  ρ = 1025 kg/m³;  "
                     "p₀ = 1,0 · 10⁵ Pa;  g = 10 m/s²",
                     "Jāaprēķina:  p = ?    p(kopā) = ?  (Pa)",
                     "Formulas:  p = ρ · g · h ;   p(kopā) = p₀ + ρ · g · h",
                     "Aprēķins:  1) p = 1025 kg/m³ · 10 m/s² · 25 m = "
                     "256 250 Pa ≈ 2,56 · 10⁵ Pa",
                     "                   2) p(kopā) = 1,0 · 10⁵ Pa + "
                     "2,56 · 10⁵ Pa = 3,56 · 10⁵ Pa",
                     "Atbilde:  p ≈ 2,6 · 10⁵ Pa (256 kPa);  p(kopā) ≈ "
                     "3,6 · 10⁵ Pa (356 kPa) — aptuveni 3,5 atmosfēras.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas p = ρgh un "
                     "p(kopā) = p₀ + ρgh;",
                     "2 p — pareizi aprēķināts p ≈ 2,56 · 10⁵ Pa ar "
                     "mērvienību (tikai skaitļošanas kļūda — 1 p);",
                     "1 p — pareizi aprēķināts p(kopā) ≈ 3,56 · 10⁵ Pa un "
                     "uzrakstīta atbilde.",
                 ]},

                {"tips": "aprekins", "virs": "Arhimēda spēks", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Ķermenis, kura tilpums ir V = 500 cm³ un masa "
                           "m = 400 g, pilnībā iegremdēts ūdenī "
                           "(ρ = 1000 kg/m³). Aprēķini Arhimēda spēku un "
                           "smaguma spēku! Nosaki, vai ķermenis peldēs vai "
                           "grims, un pamato atbildi! Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  V = 500 cm³;  m = 400 g;  ρ = 1000 kg/m³;  "
                     "g = 10 m/s²",
                     "Jāaprēķina:  F(A) = ?    F(sm) = ?  (N)",
                     "Formulas:  F(A) = ρ · g · V ;   F(sm) = m · g",
                     "Aprēķins:  1) V = 500 cm³ = 5,0 · 10⁻⁴ m³;  "
                     "m = 400 g = 0,400 kg",
                     "                   2) F(A) = 1000 kg/m³ · 10 m/s² · "
                     "5,0 · 10⁻⁴ m³ = 5 N",
                     "                   3) F(sm) = 0,400 kg · 10 m/s² = 4 N",
                     "Atbilde:  F(A) = 5 N > F(sm) = 4 N, tāpēc ķermenis "
                     "izpeldēs un peldēs daļēji iegremdēts. To pašu rāda "
                     "blīvumi: ρ(ķermeņa) = 0,4 kg : 5·10⁻⁴ m³ = 800 kg/m³ < "
                     "1000 kg/m³.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un abas pārveides "
                     "(500 cm³ = 5·10⁻⁴ m³; 400 g = 0,400 kg);",
                     "1 p — pierakstītas formulas F(A) = ρgV un F(sm) = mg;",
                     "1 p — pareizi aprēķināts F(A) = 5 N (ar ŠĶIDRUMA "
                     "blīvumu);",
                     "1 p — pareizi aprēķināts F(sm) = 4 N;",
                     "1 p — pamatots secinājums, ka ķermenis peld, jo "
                     "F(A) > F(sm).",
                 ]},

                {"tips": "aprekins", "virs": "Hidrauliskā sistēma",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Hidrauliskā domkrata mazā virzuļa laukums ir "
                           "S₁ = 4 cm², bet lielā — S₂ = 200 cm². Uz mazo "
                           "virzuli iedarbojas spēks F₁ = 50 N. Aprēķini "
                           "spēku uz lielā virzuļa un spēka ieguvumu! Cik "
                           "tālu jānospiež mazais virzulis, lai lielais "
                           "paceltos par 1 cm?",
                 "risinajums": [
                     "Dots:  S₁ = 4 cm²;  S₂ = 200 cm²;  F₁ = 50 N;  "
                     "s₂ = 1 cm",
                     "Jāaprēķina:  F₂ = ?  (N)    n = ?    s₁ = ?  (cm)",
                     "Formulas:  F₁ / S₁ = F₂ / S₂  →  F₂ = F₁ · S₂ / S₁ ;   "
                     "F₁ · s₁ = F₂ · s₂",
                     "Aprēķins:  1) F₂ = 50 N · 200 cm² : 4 cm² = 2500 N",
                     "                   2) n = S₂ / S₁ = 200 : 4 = 50",
                     "                   3) s₁ = F₂ · s₂ / F₁ = n · s₂ = "
                     "50 · 1 cm = 50 cm",
                     "Atbilde:  F₂ = 2500 N;  ieguvums 50 reizes;  mazais "
                     "virzulis jānospiež 50 cm. Cik reižu iegūst spēkā, tik "
                     "reižu zaudē ceļā.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula F₁/S₁ = F₂/S₂ "
                     "(laukumus drīkst nepārvērst m², jo tie dalās);",
                     "1 p — pareizi aprēķināts F₂ = 2500 N;",
                     "1 p — noteikts spēka ieguvums 50;",
                     "1 p — pareizi noteikts s₁ = 50 cm ar atsauci uz zelta "
                     "likumu.",
                 ]},

                {"tips": "jautajumi", "virs": "Troksnis un apgaismojums",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem! Otrajā jautājumā parādi "
                           "aprēķinu.",
                 "jaut": [
                     ("Skaņas līmenis pieaug no 60 dB līdz 90 dB. Cik reižu "
                      "palielinās skaņas intensitāte?", 1),
                     ("Lampa 1 m attālumā rada apgaismojumu E₁ = 400 lx. Cik "
                      "liels apgaismojums būs 2 m attālumā?", 1),
                     ("Vai 300 lx ir pietiekams apgaismojums precīzam "
                      "rasēšanas darbam? Pamato!", 1),
                 ],
                 "atbildes": [
                     "1) Starpība ir 30 dB, tātad trīs reizes pa +10 dB: "
                     "10 · 10 · 10 = 1000 reižu.   (1 p)",
                     "2) E₁ · r₁² = E₂ · r₂²  →  E₂ = E₁ · r₁² / r₂² = "
                     "400 lx · (1 m)² : (2 m)² = 400 : 4 = 100 lx.   (1 p)",
                     "3) Nē. Precīzam darbam un rasēšanai vajadzīgi "
                     "750–1000 lx; 300–500 lx ir norma parastam klases vai "
                     "biroja darbam. Pie mazāka apgaismojuma nogurst acis.   "
                     "(1 p)",
                 ]},

                {"tips": "jautajumi", "virs": "Starojums vidē", "punkti": 3,
                 "vieta": 6.5,
                 "ievads": "Atbildi uz jautājumiem par starojuma ietekmi un "
                           "informācijas izvērtēšanu!",
                 "jaut": [
                     ("Ar ko jonizējošs starojums atšķiras no "
                      "nejonizējoša?", 1),
                     ("UV indekss ir 7. Kā šādā dienā jārīkojas?", 1),
                     ("Kā izvērtēsi apgalvojumu «5G tornis rada radiāciju un "
                      "izraisa slimības»?", 1),
                 ],
                 "atbildes": [
                     "1) Jonizējošs starojums (α, β, γ, rentgens, neitroni) "
                     "spēj izsist elektronu no atoma un tieši bojāt DNS; "
                     "nejonizējošs (radioviļņi, mikroviļņi, redzamā gaisma) "
                     "to nespēj — tas var tikai sasildīt audus.   (1 p)",
                     "2) UV indekss 6–7 ir augsts: jālieto saules "
                     "aizsargkrēms, cepure un jāuzturas ēnā; vēlams "
                     "izvairīties no tiešas saules ap dienas vidu.   (1 p)",
                     "3) Apgalvojums sajauc divus starojuma veidus: 5G "
                     "izmanto radioviļņus — nejonizējošu starojumu, kura "
                     "kvanta enerģija ir miljoniem reižu mazāka nekā "
                     "rentgenam. Ticamam avotam būtu jānorāda mērījumi "
                     "(jaudas blīvums W/m²), salīdzinājums ar normu, un tas "
                     "būtu jāapstiprina citiem avotiem.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("No kā ir atkarīgs hidrostatiskais spiediens?",
                 ["no trauka formas", "no šķidruma daudzuma traukā",
                  "no dziļuma un šķidruma blīvuma", "no trauka platuma"], 2),
                ("Par cik aptuveni pieaug spiediens uz katriem 10 m ūdens "
                 "dziļuma?",
                 ["par vienu atmosfēras spiedienu", "par 10 Pa", "par 1 Pa",
                  "spiediens nemainās"], 0),
                ("Ķermenis lidinās šķidrumā (nepeld augšup un negrimst), ja",
                 ["ķermeņa blīvums ir lielāks par šķidruma blīvumu",
                  "ķermeņa blīvums ir vienāds ar šķidruma blīvumu",
                  "ķermeņa blīvums ir mazāks par šķidruma blīvumu",
                  "ķermeņa tilpums ir ļoti liels"], 1),
                ("Kā zemūdene maina savu vidējo blīvumu?",
                 ["maina korpusa formu",
                  "piepilda vai iztukšo balasta tvertnes",
                  "maina kustības ātrumu", "sasilda apkārtējo ūdeni"], 1),
                ("Kurš šķidrums traukā nogrims viszemāk?",
                 ["spirts (790 kg/m³)", "ūdens (1000 kg/m³)",
                  "dzīvsudrabs (13 600 kg/m³)", "nafta (800 kg/m³)"], 2),
                ("Ko dod hidrauliskā sistēma?",
                 ["enerģijas ieguvumu",
                  "spēka ieguvumu, bet ne enerģijas ieguvumu",
                  "padarītā darba ieguvumu", "spiediena zudumu"], 1),
                ("Kāpēc dvielis uzsūc ūdeni?",
                 ["gravitācijas dēļ", "Arhimēda spēka dēļ",
                  "gaisa spiediena dēļ", "kapilaritātes dēļ"], 3),
                ("Ko nozīmē skaņas līmeņa pieaugums par +10 dB?",
                 ["2 reizes lielāku intensitāti",
                  "100 reižu lielāku intensitāti",
                  "10 reižu lielāku intensitāti", "intensitāte nemainās"], 2),
                ("Kāds apgaismojums nepieciešams klasē vai birojā?",
                 ["300–500 lx", "30–50 lx", "100 lx", "5000 lx"], 0),
                ("Kurš starojums NAV jonizējošs?",
                 ["gamma starojums", "rentgenstarojums", "radioviļņi",
                  "alfa starojums"], 2),
            ],
            "uzdevumi": [
                {"tips": "aprekins", "virs": "Spiediens šķidrumā",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Ūdenskrātuves dziļums pie dambja ir h = 20 m. "
                           "Ūdens blīvums ir ρ = 1000 kg/m³, atmosfēras "
                           "spiediens p₀ = 1,0 · 10⁵ Pa, g = 10 m/s². "
                           "Aprēķini spiedienu, ko ūdens stabs rada dambja "
                           "pamatnē, un kopējo spiedienu! Paskaidro, kāpēc "
                           "dambja siena apakšā ir biezāka nekā augšā!",
                 "risinajums": [
                     "Dots:  h = 20 m;  ρ = 1000 kg/m³;  "
                     "p₀ = 1,0 · 10⁵ Pa;  g = 10 m/s²",
                     "Jāaprēķina:  p = ?    p(kopā) = ?  (Pa)",
                     "Formulas:  p = ρ · g · h ;   p(kopā) = p₀ + ρ · g · h",
                     "Aprēķins:  1) p = 1000 kg/m³ · 10 m/s² · 20 m = "
                     "200 000 Pa = 2,0 · 10⁵ Pa",
                     "                   2) p(kopā) = 1,0 · 10⁵ Pa + "
                     "2,0 · 10⁵ Pa = 3,0 · 10⁵ Pa",
                     "Atbilde:  p = 2,0 · 10⁵ Pa (200 kPa);  p(kopā) = "
                     "3,0 · 10⁵ Pa. Siena apakšā ir biezāka, jo spiediens "
                     "p = ρgh aug ar dziļumu — pie pamatnes tas ir "
                     "vislielākais.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas p = ρgh un "
                     "p(kopā) = p₀ + ρgh;",
                     "1 p — pareizi aprēķināts p = 2,0 · 10⁵ Pa ar "
                     "mērvienību;",
                     "1 p — pareizi aprēķināts p(kopā) = 3,0 · 10⁵ Pa;",
                     "1 p — pamatots skaidrojums par sienas biezumu (p aug "
                     "ar dziļumu h).",
                 ]},

                {"tips": "aprekins", "virs": "Arhimēda spēks", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Ķermenis, kura tilpums ir V = 250 cm³ un masa "
                           "m = 300 g, pilnībā iegremdēts ūdenī "
                           "(ρ = 1000 kg/m³). Aprēķini Arhimēda spēku un "
                           "smaguma spēku! Nosaki, vai ķermenis peldēs vai "
                           "grims, un pamato atbildi! Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  V = 250 cm³;  m = 300 g;  ρ = 1000 kg/m³;  "
                     "g = 10 m/s²",
                     "Jāaprēķina:  F(A) = ?    F(sm) = ?  (N)",
                     "Formulas:  F(A) = ρ · g · V ;   F(sm) = m · g",
                     "Aprēķins:  1) V = 250 cm³ = 2,5 · 10⁻⁴ m³;  "
                     "m = 300 g = 0,300 kg",
                     "                   2) F(A) = 1000 kg/m³ · 10 m/s² · "
                     "2,5 · 10⁻⁴ m³ = 2,5 N",
                     "                   3) F(sm) = 0,300 kg · 10 m/s² = 3 N",
                     "Atbilde:  F(A) = 2,5 N < F(sm) = 3 N, tāpēc ķermenis "
                     "grims. To pašu rāda blīvumi: ρ(ķermeņa) = "
                     "0,3 kg : 2,5·10⁻⁴ m³ = 1200 kg/m³ > 1000 kg/m³.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un abas pārveides "
                     "(250 cm³ = 2,5·10⁻⁴ m³; 300 g = 0,300 kg);",
                     "1 p — pierakstītas formulas F(A) = ρgV un F(sm) = mg;",
                     "1 p — pareizi aprēķināts F(A) = 2,5 N (ar ŠĶIDRUMA "
                     "blīvumu);",
                     "1 p — pareizi aprēķināts F(sm) = 3 N;",
                     "1 p — pamatots secinājums, ka ķermenis grimst, jo "
                     "F(A) < F(sm).",
                 ]},

                {"tips": "aprekins", "virs": "Hidrauliskā sistēma",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Hidrauliskās preses mazā virzuļa laukums ir "
                           "S₁ = 10 cm², bet lielā — S₂ = 500 cm². Uz mazo "
                           "virzuli iedarbojas spēks F₁ = 80 N. Aprēķini "
                           "spēku uz lielā virzuļa un spēka ieguvumu! Cik "
                           "tālu jānospiež mazais virzulis, lai lielais "
                           "pārvietotos par 2 mm?",
                 "risinajums": [
                     "Dots:  S₁ = 10 cm²;  S₂ = 500 cm²;  F₁ = 80 N;  "
                     "s₂ = 2 mm",
                     "Jāaprēķina:  F₂ = ?  (N)    n = ?    s₁ = ?  (mm)",
                     "Formulas:  F₁ / S₁ = F₂ / S₂  →  F₂ = F₁ · S₂ / S₁ ;   "
                     "F₁ · s₁ = F₂ · s₂",
                     "Aprēķins:  1) F₂ = 80 N · 500 cm² : 10 cm² = 4000 N",
                     "                   2) n = S₂ / S₁ = 500 : 10 = 50",
                     "                   3) s₁ = n · s₂ = 50 · 2 mm = "
                     "100 mm = 10 cm",
                     "Atbilde:  F₂ = 4000 N;  ieguvums 50 reizes;  mazais "
                     "virzulis jānospiež 10 cm. Cik reižu iegūst spēkā, tik "
                     "reižu zaudē ceļā.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula F₁/S₁ = F₂/S₂ "
                     "(laukumus drīkst nepārvērst m², jo tie dalās);",
                     "1 p — pareizi aprēķināts F₂ = 4000 N;",
                     "1 p — noteikts spēka ieguvums 50;",
                     "1 p — pareizi noteikts s₁ = 100 mm = 10 cm ar atsauci "
                     "uz zelta likumu.",
                 ]},

                {"tips": "jautajumi", "virs": "Troksnis un apgaismojums",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem! Otrajā jautājumā parādi "
                           "aprēķinu.",
                 "jaut": [
                     ("Skaņas līmenis pieaug no 50 dB līdz 80 dB. Cik reižu "
                      "palielinās skaņas intensitāte?", 1),
                     ("Lampa 2 m attālumā rada apgaismojumu E₁ = 200 lx. Cik "
                      "liels apgaismojums būs 4 m attālumā?", 1),
                     ("Nosauc divus veidus, kā uzlabot apgaismojumu darba "
                      "vietā!", 1),
                 ],
                 "atbildes": [
                     "1) Starpība ir 30 dB, tātad trīs reizes pa +10 dB: "
                     "10 · 10 · 10 = 1000 reižu.   (1 p)",
                     "2) E₁ · r₁² = E₂ · r₂²  →  E₂ = E₁ · r₁² / r₂² = "
                     "200 lx · (2 m)² : (4 m)² = 200 · 4 : 16 = 50 lx.   "
                     "(1 p)",
                     "3) Divi no: novietot gaismas avotu tuvāk; izmantot "
                     "vairākus gaismas avotus; izvairīties no ēnas un "
                     "atspīduma; labročiem gaismu virzīt no kreisās puses.   "
                     "(1 p)",
                 ]},

                {"tips": "jautajumi", "virs": "Starojums vidē", "punkti": 3,
                 "vieta": 6.5,
                 "ievads": "Atbildi uz jautājumiem par starojuma ietekmi un "
                           "informācijas izvērtēšanu!",
                 "jaut": [
                     ("Kāpēc mobilā tālruņa radioviļņus un rentgenstarojumu "
                      "nedrīkst salīdzināt pēc bīstamības?", 1),
                     ("UV indekss ir 9. Kā šādā dienā jārīkojas?", 1),
                     ("Nosauc divas pazīmes, kas liecina, ka informācijas "
                      "avots par starojumu ir uzticams!", 1),
                 ],
                 "atbildes": [
                     "1) Radioviļņi ir nejonizējošs starojums — tie var "
                     "tikai sasildīt audus; rentgenstarojums ir jonizējošs — "
                     "tas izsit elektronus no atomiem un var bojāt DNS. Šo "
                     "starojumu kvantu enerģija atšķiras miljoniem reižu.   "
                     "(1 p)",
                     "2) UV indekss 8 un vairāk ir ļoti augsts: no tiešas "
                     "saules jāizvairās aptuveni no 11 līdz 15, jālieto "
                     "aizsargkrēms, cepure un apģērbs, jāuzturas ēnā.   "
                     "(1 p)",
                     "3) Divas no: norādīti mērījumi un skaitļi ar "
                     "mērvienībām; nosaukts avots (pētnieks, iestāde), nevis "
                     "reklāma; secinājums tiešām izriet no datiem; to pašu "
                     "apstiprina citi neatkarīgi avoti.   (1 p)",
                 ]},
            ],
        },
    ],
}
