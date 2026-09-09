# -*- coding: utf-8 -*-
"""PD3 — Materiālu veidi un fizikālās īpašības (5.1.–5.8. stunda)."""

PD = {
    "nr": 3,
    "nosaukums": "Materiālu veidi un fizikālās īpašības",
    "mape": "5. Materiālu veidi un īpašības",
    "fails": "PD3. Materiālu veidi un fizikālās īpašības",
    "stundas": "5.1.–5.8.",
    "datums": "13.11.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda materiālu fizikālās īpašības, mehānisko "
                "spriegumu un drošības rezervi, elastību un Huka likumu, "
                "siltumvadītspēju, elektrovadītspēju un materiāla izvēli.",
    "atgadne": [
        "ρ = m / V   ·   F = m · g   ·   σ = F / S   ·   k = σ(max) / σ   ·   "
        "1 MPa = 10⁶ Pa",
        "Huka likums:  F = k · Δx   ·   k = F / Δx  [N/m]",
        "P = λ · S · Δt / d   ·   R = ρ · l / S",
        "g = 10 m/s²   ·   1 mm² = 10⁻⁶ m²   ·   1 cm² = 10⁻⁴ m²",
    ],
    "struktura": [
        ("1.", "Raksturo materiālu īpašības, deformācijas veidus, siltuma un "
               "elektrovadītspēju, materiālu grupas", "5.1.–5.7.", 10),
        ("2.", "Aprēķina mehānisko spriegumu un drošības koeficientu; "
               "izvērtē, vai materiāls ir piemērots", "5.2.", 5),
        ("3.", "Lieto Huka likumu elastības spēka un masas aprēķinam",
         "5.3.", 4),
        ("4.", "Aprēķina siltuma plūsmu caur sienu un skaidro siltuma "
               "zudumu samazināšanu", "5.4.", 4),
        ("5.", "Aprēķina vadītāja pretestību pēc R = ρ·l/S", "5.5.", 4),
        ("6.", "Izvēlas materiālu konkrētam lietojumam un pamato izvēli ar "
               "fizikālajām īpašībām", "5.1., 5.6., 5.7.", 3),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Ar kuru formulu aprēķina mehānisko spriegumu?",
                 ["σ = F · S", "σ = F / S", "σ = S / F", "σ = m / V"], 1),
                ("Kāda ir mehāniskā sprieguma mērvienība?",
                 ["ņūtons (N)", "džouls (J)", "paskāls (Pa)", "vats (W)"], 2),
                ("Elastīga ir tāda deformācija, pēc kuras",
                 ["forma atjaunojas", "forma paliek mainīta",
                  "materiāls plīst", "materiāls izkūst"], 0),
                ("Ko rāda atsperes stinguma koeficients k?",
                 ["cik smaga ir atspere", "cik gara ir atspere",
                  "cik liels spēks vajadzīgs 1 m pagarinājumam",
                  "cik reižu atspere izstiepjas"], 2),
                ("Kurš materiāls vada siltumu vislabāk?",
                 ["koks", "stikls", "minerālvate", "varš"], 3),
                ("Kāpēc metāla krēsls istabā šķiet aukstāks par koka krēslu?",
                 ["metāla temperatūra ir zemāka",
                  "metāls ātri aizvada siltumu no rokas",
                  "metāls izstaro aukstumu", "koks pats ražo siltumu"], 1),
                ("Kura viela ir dielektriķis?",
                 ["varš", "alumīnijs", "gumija", "grafīts"], 2),
                ("Ja vadu pagarina divas reizes, tā pretestība",
                 ["palielinās 2 reizes", "nemainās", "samazinās 2 reizes",
                  "palielinās 4 reizes"], 0),
                ("Kurai materiālu grupai ir raksturīga trauslums un augsta "
                 "karstumizturība?",
                 ["metāliem", "keramikai", "polimēriem", "kompozītiem"], 1),
                ("Kāpēc gaisvadu līnijās lieto alumīniju, nevis varu?",
                 ["alumīnijam ir mazāka īpatnējā pretestība",
                  "alumīnijs nekorodē", "varš strāvu nevada",
                  "alumīnijs ir vieglāks un lētāks"], 3),
            ],
            "uzdevumi": [
                {"tips": "aprekins",
                 "virs": "Mehāniskais spriegums un drošības koeficients",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Tērauda trosi, kuras šķērsgriezuma laukums ir "
                           "S = 2,0 · 10⁻⁴ m², slogo ar kravu, kuras masa "
                           "m = 500 kg. Tērauda stiprības robeža ir "
                           "σ(max) = 500 MPa. Aprēķini spriegumu trosē un "
                           "drošības koeficientu k! Vai šo trosi drīkst "
                           "lietot liftā, kur nepieciešams k ≥ 10? "
                           "Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  S = 2,0 · 10⁻⁴ m²;  m = 500 kg;  "
                     "σ(max) = 500 MPa;  g = 10 m/s²",
                     "Jāaprēķina:  σ = ?  (Pa)    k = ?",
                     "Formulas:  F = m · g ;   σ = F / S ;   k = σ(max) / σ",
                     "Aprēķins:  1) F = m · g = 500 kg · 10 m/s² = 5000 N",
                     "                   2) σ = F / S = 5000 N : "
                     "(2,0 · 10⁻⁴ m²) = 2,5 · 10⁷ Pa = 25 MPa",
                     "                   3) k = σ(max) / σ = 500 MPa : "
                     "25 MPa = 20",
                     "Atbilde:  σ = 25 MPa, k = 20. Tā kā 20 ≥ 10, trosi "
                     "liftā drīkst lietot.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas F = m·g, σ = F/S un "
                     "k = σ(max)/σ;",
                     "1 p — pareizi aprēķināts F = 5000 N;",
                     "1 p — pareizi aprēķināts σ = 2,5 · 10⁷ Pa = 25 MPa "
                     "(MPa un Pa jāsaskaņo);",
                     "1 p — k = 20 un pamatots secinājums, ka troses "
                     "drošības rezerve ir pietiekama.",
                 ]},

                {"tips": "aprekins", "virs": "Huka likums", "punkti": 4,
                 "vieta": 6.5,
                 "teksts": "Atsperi, kuras stinguma koeficients ir "
                           "k = 250 N/m, izstiepj par Δx = 8 cm. Aprēķini "
                           "elastības spēku! Cik liela masa jāpakar atsperei, "
                           "lai iegūtu tieši šādu pagarinājumu? "
                           "Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  k = 250 N/m;  Δx = 8 cm;  g = 10 m/s²",
                     "Jāaprēķina:  F = ?  (N)    m = ?  (kg)",
                     "Formulas:  F = k · Δx ;   F = m · g  →  m = F / g",
                     "Aprēķins:  1) Δx = 8 cm = 0,08 m",
                     "                   2) F = k · Δx = 250 N/m · 0,08 m = "
                     "20 N",
                     "                   3) m = F / g = 20 N : 10 m/s² = 2 kg",
                     "Atbilde:  F = 20 N;  m = 2 kg.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un pārveide 8 cm = 0,08 m;",
                     "1 p — pierakstītas formulas F = k·Δx un m = F/g;",
                     "1 p — pareizi aprēķināts F = 20 N;",
                     "1 p — pareizi aprēķināts m = 2 kg un uzrakstīta atbilde "
                     "ar mērvienībām. Ja Δx nav pārvērsts metros (iegūst "
                     "2000 N), par 3. un 4. soli punktus nepiešķir.",
                 ]},

                {"tips": "jautajumi", "virs": "Siltumvadītspēja un izolācija",
                 "punkti": 4, "vieta": 6.5,
                 "ievads": "Ķieģeļu sienas biezums ir d = 0,25 m, laukums "
                           "S = 20 m², siltumvadītspējas koeficients "
                           "λ = 0,7 W/(m·K). Temperatūru starpība starp "
                           "telpu un āru ir Δt = 20 °C.",
                 "jaut": [
                     ("Aprēķini siltuma plūsmas jaudu P caur sienu!", 2),
                     ("Kā mainīsies siltuma zudumi, ja sienai no ārpuses "
                      "pievienos minerālvates slāni (λ = 0,04 W/(m·K))? "
                      "Pamato bez aprēķina!", 1),
                     ("Kāpēc logā liek vairākas stikla kārtas ar gaisu starp "
                      "tām?", 1),
                 ],
                 "atbildes": [
                     "1) P = λ · S · Δt / d = 0,7 W/(m·K) · 20 m² · 20 K : "
                     "0,25 m = 280 : 0,25 = 1120 W.   "
                     "(1 p — formula, 1 p — pareizs rezultāts ar mērvienību)",
                     "2) Zudumi samazināsies. Minerālvates λ ir daudz mazāks "
                     "(0,04 pret 0,7), un pievienotais slānis palielina arī "
                     "kopējo biezumu d — abi lielumi P formulā samazina "
                     "siltuma plūsmu.   (1 p)",
                     "3) Gaiss vada siltumu ļoti slikti, tāpēc gaisa slānis "
                     "starp stikliem darbojas kā izolators un samazina "
                     "siltuma plūsmu caur logu.   (1 p)",
                 ]},

                {"tips": "aprekins", "virs": "Vadītāja pretestība",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Vara vada garums ir l = 50 m, šķērsgriezuma "
                           "laukums S = 1,5 mm², vara īpatnējā pretestība "
                           "ρ = 1,7 · 10⁻⁸ Ω·m. Aprēķini vada pretestību!",
                 "risinajums": [
                     "Dots:  l = 50 m;  S = 1,5 mm²;  ρ = 1,7 · 10⁻⁸ Ω·m",
                     "Jāaprēķina:  R = ?  (Ω)",
                     "Formulas:  R = ρ · l / S",
                     "Aprēķins:  1) S = 1,5 mm² = 1,5 · 10⁻⁶ m²",
                     "                   2) R = ρ · l / S = "
                     "1,7 · 10⁻⁸ Ω·m · 50 m : (1,5 · 10⁻⁶ m²)",
                     "                   3) R = 8,5 · 10⁻⁷ : 1,5 · 10⁻⁶ ≈ "
                     "0,57 Ω",
                     "Atbilde:  R ≈ 0,57 Ω.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīta formula R = ρ·l/S;",
                     "1 p — pareiza pārveide 1,5 mm² = 1,5 · 10⁻⁶ m²;",
                     "1 p — pareizs R ≈ 0,57 Ω ar mērvienību. Ja mm² nav "
                     "pārvērsti m², par 3. un 4. soli punktus nepiešķir.",
                 ]},

                {"tips": "jautajumi", "virs": "Materiāla izvēle", "punkti": 3,
                 "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem, pamatojot ar materiāla "
                           "fizikālajām īpašībām!",
                 "jaut": [
                     ("Kuru materiālu izvēlēsies lidmašīnas korpusam un "
                      "kāpēc?", 1),
                     ("Nosauc vienu īpašību, kuras dēļ keramika ir piemērota "
                      "krāsnīm, un vienu tās trūkumu!", 1),
                     ("Kas ir kompozītmateriāls un kāpēc tas var būt "
                      "vieglāks par alumīniju, bet izturīgāks par tēraudu?",
                      1),
                 ],
                 "atbildes": [
                     "1) Alumīniju vai kompozītu (ogļšķiedru), jo vajadzīgs "
                     "mazs blīvums (maza masa) kopā ar lielu izturību.   "
                     "(1 p)",
                     "2) Priekšrocība — augsta kušanas temperatūra un "
                     "karstumizturība (turklāt nevada strāvu); trūkums — tā "
                     "ir trausla un plīst no trieciena.   (1 p)",
                     "3) Kompozīts ir divu materiālu apvienojums, kurā katrs "
                     "dod savu labāko īpašību: šķiedra dod izturību, sveķi — "
                     "formu un saistību. Tāpēc kopā iegūst mazu blīvumu un "
                     "lielu izturību vienlaikus.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Ko rāda drošības koeficients k = σ(max) / σ?",
                 ["cik reižu materiāls ir vieglāks",
                  "cik reižu stiprības robeža pārsniedz reālo spriegumu",
                  "cik smaga ir krava", "cik gara ir trose"], 1),
                ("Ja slodze paliek tā pati, bet šķērsgriezuma laukumu "
                 "palielina divas reizes, spriegums",
                 ["palielinās 2 reizes", "samazinās 2 reizes", "nemainās",
                  "palielinās 4 reizes"], 1),
                ("Plastiska ir tāda deformācija, pēc kuras",
                 ["forma paliek mainīta", "forma atjaunojas",
                  "materiāls atdziest", "materiāls kļūst elastīgs"], 0),
                ("Kura formula izsaka Huka likumu?",
                 ["F = m · a", "F = ρ · V", "F = k · Δx", "F = λ · S"], 2),
                ("Kurš materiāls ir vislabākais siltumizolators?",
                 ["varš", "tērauds", "stikls", "minerālvate"], 3),
                ("Kurā materiālā siltumu pārnes brīvie elektroni?",
                 ["metālos", "kokā", "putuplastā", "stiklā"], 0),
                ("Kura viela ir pusvadītājs?",
                 ["varš", "silīcijs", "gumija", "stikls"], 1),
                ("Ja vada šķērsgriezuma laukumu palielina divas reizes, tā "
                 "pretestība",
                 ["palielinās 2 reizes", "nemainās", "samazinās 4 reizes",
                  "samazinās 2 reizes"], 3),
                ("Kurai materiālu grupai ir raksturīgas garas molekulu "
                 "ķēdes?",
                 ["metāliem", "keramikai", "polimēriem", "kompozītiem"], 2),
                ("Pie kuras materiālu grupas pieder formas atmiņas "
                 "sakausējums?",
                 ["pie keramikas", "pie viedajiem materiāliem",
                  "pie dielektriķiem", "pie pusvadītājiem"], 1),
            ],
            "uzdevumi": [
                {"tips": "aprekins",
                 "virs": "Mehāniskais spriegums un drošības koeficients",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Alumīnija stieni, kura šķērsgriezuma laukums ir "
                           "S = 5,0 · 10⁻⁴ m², slogo ar kravu, kuras masa "
                           "m = 1000 kg. Alumīnija stiprības robeža ir "
                           "σ(max) = 200 MPa. Aprēķini spriegumu stienī un "
                           "drošības koeficientu k! Vai stienis der "
                           "konstrukcijai, kurai nepieciešams k ≥ 5? "
                           "Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  S = 5,0 · 10⁻⁴ m²;  m = 1000 kg;  "
                     "σ(max) = 200 MPa;  g = 10 m/s²",
                     "Jāaprēķina:  σ = ?  (Pa)    k = ?",
                     "Formulas:  F = m · g ;   σ = F / S ;   k = σ(max) / σ",
                     "Aprēķins:  1) F = m · g = 1000 kg · 10 m/s² = 10 000 N",
                     "                   2) σ = F / S = 10 000 N : "
                     "(5,0 · 10⁻⁴ m²) = 2,0 · 10⁷ Pa = 20 MPa",
                     "                   3) k = σ(max) / σ = 200 MPa : "
                     "20 MPa = 10",
                     "Atbilde:  σ = 20 MPa, k = 10. Tā kā 10 ≥ 5, stienis "
                     "konstrukcijai der.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas F = m·g, σ = F/S un "
                     "k = σ(max)/σ;",
                     "1 p — pareizi aprēķināts F = 10 000 N;",
                     "1 p — pareizi aprēķināts σ = 2,0 · 10⁷ Pa = 20 MPa;",
                     "1 p — k = 10 un pamatots secinājums, ka stienis der.",
                 ]},

                {"tips": "aprekins", "virs": "Huka likums", "punkti": 4,
                 "vieta": 6.5,
                 "teksts": "Atsperi, kuras stinguma koeficients ir "
                           "k = 300 N/m, izstiepj par Δx = 6 cm. Aprēķini "
                           "elastības spēku! Cik liela masa jāpakar atsperei, "
                           "lai iegūtu tieši šādu pagarinājumu? "
                           "Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  k = 300 N/m;  Δx = 6 cm;  g = 10 m/s²",
                     "Jāaprēķina:  F = ?  (N)    m = ?  (kg)",
                     "Formulas:  F = k · Δx ;   F = m · g  →  m = F / g",
                     "Aprēķins:  1) Δx = 6 cm = 0,06 m",
                     "                   2) F = k · Δx = 300 N/m · 0,06 m = "
                     "18 N",
                     "                   3) m = F / g = 18 N : 10 m/s² = "
                     "1,8 kg",
                     "Atbilde:  F = 18 N;  m = 1,8 kg.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un pārveide 6 cm = 0,06 m;",
                     "1 p — pierakstītas formulas F = k·Δx un m = F/g;",
                     "1 p — pareizi aprēķināts F = 18 N;",
                     "1 p — pareizi aprēķināts m = 1,8 kg un uzrakstīta "
                     "atbilde ar mērvienībām. Ja Δx nav pārvērsts metros, par "
                     "3. un 4. soli punktus nepiešķir.",
                 ]},

                {"tips": "jautajumi", "virs": "Siltumvadītspēja un izolācija",
                 "punkti": 4, "vieta": 6.5,
                 "ievads": "Koka sienas biezums ir d = 0,20 m, laukums "
                           "S = 15 m², siltumvadītspējas koeficients "
                           "λ = 0,15 W/(m·K). Temperatūru starpība starp "
                           "telpu un āru ir Δt = 25 °C.",
                 "jaut": [
                     ("Aprēķini siltuma plūsmas jaudu P caur sienu!", 2),
                     ("Kāpēc putuplasts ar gaisa porām izolē labāk nekā tāda "
                      "paša biezuma ciets plastmasas gabals?", 1),
                     ("Kas ir siltuma tilts un kāpēc no tā būvniecībā "
                      "jāizvairās?", 1),
                 ],
                 "atbildes": [
                     "1) P = λ · S · Δt / d = 0,15 W/(m·K) · 15 m² · 25 K : "
                     "0,20 m = 56,25 : 0,20 ≈ 281 W.   "
                     "(1 p — formula, 1 p — pareizs rezultāts ar mērvienību)",
                     "2) Putuplastā lielāko daļu tilpuma aizņem gaiss, un "
                     "gaisa siltumvadītspēja ir ļoti maza; cietā plastmasā "
                     "gaisa poru nav, tāpēc λ ir lielāks.   (1 p)",
                     "3) Siltuma tilts ir konstrukcijas vieta, kur siltums "
                     "iziet cauri daudz vieglāk nekā apkārtējā sienā "
                     "(piemēram, betona pārsedze vai metāla stiprinājums). "
                     "Tur zudumi ir lieli un var uzkrāties mitrums.   (1 p)",
                 ]},

                {"tips": "aprekins", "virs": "Vadītāja pretestība",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Alumīnija vada garums ir l = 100 m, "
                           "šķērsgriezuma laukums S = 2,5 mm², alumīnija "
                           "īpatnējā pretestība ρ = 2,8 · 10⁻⁸ Ω·m. Aprēķini "
                           "vada pretestību!",
                 "risinajums": [
                     "Dots:  l = 100 m;  S = 2,5 mm²;  ρ = 2,8 · 10⁻⁸ Ω·m",
                     "Jāaprēķina:  R = ?  (Ω)",
                     "Formulas:  R = ρ · l / S",
                     "Aprēķins:  1) S = 2,5 mm² = 2,5 · 10⁻⁶ m²",
                     "                   2) R = ρ · l / S = "
                     "2,8 · 10⁻⁸ Ω·m · 100 m : (2,5 · 10⁻⁶ m²)",
                     "                   3) R = 2,8 · 10⁻⁶ : 2,5 · 10⁻⁶ = "
                     "1,12 Ω",
                     "Atbilde:  R ≈ 1,1 Ω.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīta formula R = ρ·l/S;",
                     "1 p — pareiza pārveide 2,5 mm² = 2,5 · 10⁻⁶ m²;",
                     "1 p — pareizs R ≈ 1,1 Ω ar mērvienību. Ja mm² nav "
                     "pārvērsti m², par 3. un 4. soli punktus nepiešķir.",
                 ]},

                {"tips": "jautajumi", "virs": "Materiāla izvēle", "punkti": 3,
                 "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem, pamatojot ar materiāla "
                           "fizikālajām īpašībām!",
                 "jaut": [
                     ("Kuru materiālu izvēlēsies mājas elektroinstalācijas "
                      "vadiem un kāpēc?", 1),
                     ("Nosauc vienu metālu priekšrocību un vienu trūkumu "
                      "būvkonstrukcijās!", 1),
                     ("Kāpēc nanomateriāliem ir īpašas īpašības, kādu nav "
                      "tam pašam materiālam parastā veidā?", 1),
                 ],
                 "atbildes": [
                     "1) Varu, jo tam ir ļoti maza īpatnējā pretestība "
                     "(1,7 · 10⁻⁸ Ω·m), tātad mazi enerģijas zudumi; mājas "
                     "instalācijā vadu masa nav izšķiroša.   (1 p)",
                     "2) Priekšrocība — liela izturība un kaļamība (arī laba "
                     "siltum- un elektrovadītspēja); trūkums — liels blīvums "
                     "(smagas konstrukcijas) un korozija.   (1 p)",
                     "3) Nanomateriālos daļiņu izmērs ir 1–100 nm, tāpēc "
                     "virsmas laukums attiecībā pret tilpumu ir milzīgs — "
                     "virsmas īpašības kļūst noteicošās.   (1 p)",
                 ]},
            ],
        },
    ],
}
