# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. PD4 - Mijiedarbība un spēks (42.-66. stunda)."""

PD = {
    "nr": 4,
    "klase": "10. klase",
    "nosaukums": "Mijiedarbība un spēks",
    "mape": "3. Mijiedarbība un spēks",
    "fails": "PD4. Mijiedarbība un spēks_tt",
    "stundas": "42.-65.",
    "datums": "26.02.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda Ņūtona likumus, spēku shēmas, elastības un "
                "berzes spēku, kustību pa slīpo plakni, spiedienu un "
                "Arhimēda spēku.",
    "atgadne": [
        "F = ma   ·   Fs = mg   ·   Fel = kx   ·   Fb = μN   ·   M = Fd",
        "p = F / S   ·   p = ρgh   ·   FA = ρgV   ·   σ = F / S",
        "Uz slīpās plaknes:  F(∥) = mg·sin α   ·   N = mg·cos α",
        "g = 9,8 m/s² (drīkst 10 m/s²)   ·   ρ(ūdens) = 1000 kg/m³   ·   "
        "sin 30° = 0,50  ·  cos 30° = 0,87",
    ],
    "struktura": [
        ("1.", "Lieto Ņūtona likumus, atpazīst spēku veidus, skaidro "
               "spiedienu un cēlējspēku", "42.-65.", 10),
        ("2.", "Aizpilda spēku un mērvienību tabulu", "42.-58.", 5),
        ("3.", "Risina uzdevumu par kustību ar berzi", "51., 52.", 5),
        ("4.", "Lieto Huka likumu un aprēķina stinguma koeficientu",
         "48.", 5),
        ("5.", "Risina hidrostatikas uzdevumu par spiedienu un cēlējspēku",
         "58.-61.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kas notiek ar ķermeni, ja uz to darbojošos spēku summa ir "
                 "nulle?",
                 ["tas noteikti stāv uz vietas",
                  "tas kustas ar paātrinājumu",
                  "tas stāv vai kustas vienmērīgi taisnvirziena kustībā",
                  "tas apstājas pēc kāda laika"], 2),
                ("Uz 4 kg smagu ķermeni darbojas 12 N liels kopspēks. Cik "
                 "liels ir paātrinājums?",
                 ["48 m/s²", "3 m/s²", "0,33 m/s²", "16 m/s²"], 1),
                ("Ņūtona trešā likuma spēku pāris darbojas:",
                 ["uz vienu un to pašu ķermeni",
                  "uz diviem dažādiem ķermeņiem",
                  "tikai miera stāvoklī", "tikai kustībā"], 1),
                ("Kāda ir ķermeņa svara būtība?",
                 ["spēks, ar kādu Zeme pievelk ķermeni",
                  "spēks, ar kādu ķermenis spiež uz balstu vai stiepj "
                  "piekari",
                  "ķermeņa masa", "ķermeņa inerce"], 1),
                ("Atsperes stinguma koeficients ir 200 N/m. Cik liels spēks "
                 "vajadzīgs, lai to izstieptu par 5,0 cm?",
                 ["10 N", "1000 N", "40 N", "4,0 N"], 0),
                ("No kā NAV atkarīgs slīdes berzes spēks?",
                 ["berzes koeficienta", "balsta reakcijas spēka",
                  "saskares laukuma", "virsmas materiāla"], 2),
                ("Kāpēc slēpēm ir liels laukums?",
                 ["lai palielinātu spiedienu", "lai samazinātu spiedienu",
                  "lai palielinātu masu", "lai samazinātu smaguma spēku"], 1),
                ("Cik liels ir ūdens radītais spiediens 2,0 m dziļumā "
                 "(g = 10 m/s²)?",
                 ["2000 Pa", "20 000 Pa", "200 Pa", "100 000 Pa"], 1),
                ("No kā ir atkarīgs Arhimēda spēks?",
                 ["ķermeņa masas", "ķermeņa materiāla",
                  "iegremdētās daļas tilpuma un šķidruma blīvuma",
                  "ķermeņa krāsas"], 2),
                ("Ķermenis peld uz ūdens virsmas. Ko var teikt par spēkiem?",
                 ["Arhimēda spēks lielāks par smaguma spēku",
                  "Arhimēda spēks vienāds ar smaguma spēku",
                  "Arhimēda spēks mazāks par smaguma spēku",
                  "Arhimēda spēka nav"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Spēki un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai nosaukumu! Par katru "
                         "pareizu atbildi - 1 punkts.  (g = 10 m/s²)",
                 "rindas": [
                     ("Smaguma spēks 5,0 kg smagam ķermenim  Fs = ........"
                      "............. N", "50 N"),
                     ("Spēka SI mērvienība  [F] = .....................",
                      "ņūtons (N)"),
                     ("Spiediena SI mērvienība  [p] = ....................."
                      "", "paskāls (Pa)"),
                     ("Stinguma koeficienta mērvienība  [k] = ............"
                      "......... ", "N/m"),
                     ("Spēka momenta mērvienība  [M] = ....................."
                      "", "N·m"),
                 ]},

                {"tips": "aprekins", "virs": "Kustība ar berzi", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Uz horizontālas grīdas atrodas 20 kg smaga kaste. "
                           "Berzes koeficients starp kasti un grīdu ir "
                           "μ = 0,30. Kasti velk horizontāli ar spēku "
                           "F = 80 N. Aprēķini berzes spēku un kastes "
                           "paātrinājumu! (g = 10 m/s²)",
                 "risinajums": [
                     "Dots:  m = 20 kg;  μ = 0,30;  F = 80 N;  g = 10 m/s²",
                     "Jāaprēķina:  Fb = ?  a = ?",
                     "Formulas:  N = mg;  Fb = μN;  ma = F − Fb",
                     "Aprēķins:  1) N = 20 · 10 = 200 N",
                     "                   2) Fb = 0,30 · 200 = 60 N",
                     "                   3) a = (80 − 60) : 20 = 1,0 m/s²",
                     "Atbilde:  Fb = 60 N;  a = 1,0 m/s².",
                 ],
                 "kriteriji": [
                     "1 p - spēku shēma vai pieraksts «Dots» ar visiem "
                     "lielumiem;",
                     "1 p - pareizi noteikts N = mg;",
                     "1 p - pareizi aprēķināts berzes spēks 60 N;",
                     "2 p - pareizi pierakstīts Ņūtona otrais likums "
                     "projekcijās un aprēķināts a = 1,0 m/s².",
                 ]},

                {"tips": "aprekins", "virs": "Huka likums", "punkti": 5,
                 "vieta": 7.0,
                 "teksts": "Pie atsperes pakar 0,60 kg smagu atsvaru, un "
                           "atspere pagarinās par 4,0 cm. Aprēķini atsperes "
                           "stinguma koeficientu un pagarinājumu, ja pakar "
                           "1,5 kg smagu atsvaru! (g = 10 m/s²)",
                 "risinajums": [
                     "Dots:  m₁ = 0,60 kg;  x₁ = 4,0 cm = 0,040 m;  "
                     "m₂ = 1,5 kg;  g = 10 m/s²",
                     "Jāaprēķina:  k = ?  x₂ = ?",
                     "Formulas:  Fel = mg;  k = F / x;  x = F / k",
                     "Aprēķins:  1) F₁ = 0,60 · 10 = 6,0 N",
                     "                   2) k = 6,0 : 0,040 = 150 N/m",
                     "                   3) F₂ = 1,5 · 10 = 15 N",
                     "                   4) x₂ = 15 : 150 = 0,10 m = 10 cm",
                     "Atbilde:  k = 150 N/m;  x₂ = 10 cm.",
                 ],
                 "kriteriji": [
                     "1 p - pagarinājums pārvērsts metros;",
                     "1 p - pierakstīts Huka likums Fel = kx;",
                     "2 p - pareizi aprēķināts k = 150 N/m ar mērvienību;",
                     "1 p - pareizi aprēķināts x₂ = 10 cm.",
                 ]},

                {"tips": "jautajumi", "virs": "Spiediens un cēlējspēks",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Metāla klucis ar tilpumu V = 500 cm³ un masu "
                           "m = 1,35 kg pilnībā iegremdēts ūdenī "
                           "(ρ = 1000 kg/m³, g = 10 m/s²).",
                 "jaut": [
                     ("Aprēķini klucīša blīvumu!", 1),
                     ("Aprēķini Arhimēda spēku, kas darbojas uz klucīti!",
                      1),
                     ("Aprēķini klucīša smaguma spēku!", 1),
                     ("Nosaki, vai klucītis grims vai peldēs, un pamato!",
                      1),
                     ("Aprēķini ūdens spiedienu 1,5 m dziļumā!", 1),
                 ],
                 "atbildes": [
                     "1) ρ = m / V = 1,35 kg : 5,0 · 10⁻⁴ m³ = 2700 kg/m³.   "
                     "(1 p)",
                     "2) FA = ρ(ūd)gV = 1000 · 10 · 5,0 · 10⁻⁴ = 5,0 N.   "
                     "(1 p)",
                     "3) Fs = mg = 1,35 · 10 = 13,5 N.   (1 p)",
                     "4) Grims, jo Fs = 13,5 N > FA = 5,0 N (arī "
                     "ρ(klucis) > ρ(ūdens)).   (1 p)",
                     "5) p = ρgh = 1000 · 10 · 1,5 = 15 000 Pa = 15 kPa.   "
                     "(1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Ķermenis kustas vienmērīgi taisnvirziena kustībā. Ko var "
                 "teikt par spēkiem?",
                 ["spēku nav vispār", "kopspēks ir nulle",
                  "kopspēks vērsts kustības virzienā",
                  "kopspēks vērsts pretēji kustībai"], 1),
                ("Uz 5 kg smagu ķermeni darbojas 20 N liels kopspēks. Cik "
                 "liels ir paātrinājums?",
                 ["100 m/s²", "0,25 m/s²", "4 m/s²", "25 m/s²"], 2),
                ("Ņūtona trešā likuma spēki ir:",
                 ["vienādi pēc moduļa un vērsti vienā virzienā",
                  "vienādi pēc moduļa un vērsti pretējos virzienos",
                  "dažādi pēc moduļa", "vērsti perpendikulāri"], 1),
                ("Kad ķermenis atrodas bezsvara stāvoklī?",
                 ["kad tas stāv uz zemes",
                  "kad tas kustas vienmērīgi",
                  "kad tas brīvi krīt",
                  "kad tā masa ir nulle"], 2),
                ("Atsperi ar stinguma koeficientu 400 N/m izstiepj ar 20 N "
                 "lielu spēku. Par cik tā pagarinās?",
                 ["8,0 m", "0,05 m", "20 m", "0,50 m"], 1),
                ("Kāds ir berzes spēka virziens?",
                 ["kustības virzienā", "pretēji kustībai",
                  "perpendikulāri virsmai", "vertikāli lejup"], 1),
                ("Kāpēc naglai ir smails gals?",
                 ["lai samazinātu spiedienu", "lai palielinātu spiedienu",
                  "lai samazinātu spēku", "lai palielinātu masu"], 1),
                ("Cik liels ir ūdens radītais spiediens 5,0 m dziļumā "
                 "(g = 10 m/s²)?",
                 ["500 Pa", "5000 Pa", "50 000 Pa", "500 000 Pa"], 2),
                ("Ķermenis grimst ūdenī. Ko var teikt par blīvumiem?",
                 ["ķermeņa blīvums mazāks par ūdens blīvumu",
                  "ķermeņa blīvums lielāks par ūdens blīvumu",
                  "blīvumi vienādi", "blīvumam nav nozīmes"], 1),
                ("Ko izsaka spēka moments?",
                 ["spēka lielumu", "spēka griezes iedarbību",
                  "ķermeņa masu", "ķermeņa ātrumu"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Spēki un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai nosaukumu! Par katru "
                         "pareizu atbildi - 1 punkts.  (g = 10 m/s²)",
                 "rindas": [
                     ("Smaguma spēks 8,0 kg smagam ķermenim  Fs = ........"
                      "............. N", "80 N"),
                     ("Masa, ja Fs = 250 N  m = ..................... kg",
                      "25 kg"),
                     ("Mehāniskā sprieguma mērvienība  [σ] = ............."
                      "........", "paskāls (Pa)"),
                     ("Berzes koeficienta mērvienība  [μ] = ..............."
                      "......", "bezdimensijas lielums (nav mērvienības)"),
                     ("Spiediens, ja F = 60 N un S = 0,20 m²  "
                      "p = ..................... Pa", "300 Pa"),
                 ]},

                {"tips": "aprekins", "virs": "Kustība ar berzi", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Uz horizontālas grīdas atrodas 50 kg smaga kaste. "
                           "Berzes koeficients ir μ = 0,20. Kasti stumj "
                           "horizontāli ar spēku F = 150 N. Aprēķini berzes "
                           "spēku un kastes paātrinājumu! (g = 10 m/s²)",
                 "risinajums": [
                     "Dots:  m = 50 kg;  μ = 0,20;  F = 150 N;  g = 10 m/s²",
                     "Jāaprēķina:  Fb = ?  a = ?",
                     "Formulas:  N = mg;  Fb = μN;  ma = F − Fb",
                     "Aprēķins:  1) N = 50 · 10 = 500 N",
                     "                   2) Fb = 0,20 · 500 = 100 N",
                     "                   3) a = (150 − 100) : 50 = 1,0 m/s²",
                     "Atbilde:  Fb = 100 N;  a = 1,0 m/s².",
                 ],
                 "kriteriji": [
                     "1 p - spēku shēma vai pieraksts «Dots» ar visiem "
                     "lielumiem;",
                     "1 p - pareizi noteikts N = mg;",
                     "1 p - pareizi aprēķināts berzes spēks 100 N;",
                     "2 p - pareizi pierakstīts Ņūtona otrais likums "
                     "projekcijās un aprēķināts a = 1,0 m/s².",
                 ]},

                {"tips": "aprekins", "virs": "Huka likums", "punkti": 5,
                 "vieta": 7.0,
                 "teksts": "Pie atsperes pakar 0,80 kg smagu atsvaru, un "
                           "atspere pagarinās par 5,0 cm. Aprēķini atsperes "
                           "stinguma koeficientu un atsvara masu, kas "
                           "atsperi pagarinātu par 12 cm! (g = 10 m/s²)",
                 "risinajums": [
                     "Dots:  m₁ = 0,80 kg;  x₁ = 5,0 cm = 0,050 m;  "
                     "x₂ = 12 cm = 0,12 m;  g = 10 m/s²",
                     "Jāaprēķina:  k = ?  m₂ = ?",
                     "Formulas:  Fel = mg;  k = F / x;  m = kx / g",
                     "Aprēķins:  1) F₁ = 0,80 · 10 = 8,0 N",
                     "                   2) k = 8,0 : 0,050 = 160 N/m",
                     "                   3) F₂ = 160 · 0,12 = 19,2 N",
                     "                   4) m₂ = 19,2 : 10 = 1,92 kg",
                     "Atbilde:  k = 160 N/m;  m₂ ≈ 1,9 kg.",
                 ],
                 "kriteriji": [
                     "1 p - pagarinājums pārvērsts metros;",
                     "1 p - pierakstīts Huka likums Fel = kx;",
                     "2 p - pareizi aprēķināts k = 160 N/m ar mērvienību;",
                     "1 p - pareizi aprēķināta masa ≈ 1,9 kg.",
                 ]},

                {"tips": "jautajumi", "virs": "Spiediens un cēlējspēks",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Koka klucis ar tilpumu V = 800 cm³ un masu "
                           "m = 0,48 kg peld uz ūdens "
                           "(ρ = 1000 kg/m³, g = 10 m/s²).",
                 "jaut": [
                     ("Aprēķini koka blīvumu!", 1),
                     ("Aprēķini klucīša smaguma spēku!", 1),
                     ("Cik liels ir Arhimēda spēks, klucim peldot?", 1),
                     ("Aprēķini iegremdētās daļas tilpumu!", 1),
                     ("Pamato, kā mainītos iegremdētā daļa, ja klucis "
                      "peldētu sālsūdenī ar lielāku blīvumu!", 1),
                 ],
                 "atbildes": [
                     "1) ρ = m / V = 0,48 kg : 8,0 · 10⁻⁴ m³ = 600 kg/m³.   "
                     "(1 p)",
                     "2) Fs = mg = 0,48 · 10 = 4,8 N.   (1 p)",
                     "3) Peldot FA = Fs = 4,8 N.   (1 p)",
                     "4) V(iegr) = FA / (ρ(ūd)g) = 4,8 : (1000 · 10) = "
                     "4,8 · 10⁻⁴ m³ = 480 cm³ (60 % no tilpuma).   (1 p)",
                     "5) Sālsūdenī blīvums lielāks, tāpēc tāda paša "
                     "cēlējspēka radīšanai vajadzīgs mazāks iegremdētais "
                     "tilpums - klucis peldētu augstāk.   (1 p)",
                 ]},
            ],
        },
    ],
}
