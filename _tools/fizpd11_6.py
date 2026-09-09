# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD6 - Elektromagnētisms (51.-62. stunda)."""

PD = {
    "nr": 6,
    "klase": "11. klase",
    "nosaukums": "Elektromagnētisms",
    "mape": "11. Elektromagnētisms",
    "fails": "PD6. Elektromagnētisms_tt",
    "stundas": "51.-62.",
    "datums": "24.02.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda magnētisko lauku ap strāvas vadītāju, spēku "
                "uz vadu un lādētu daļiņu, elektromagnētisko indukciju, "
                "ģeneratora un motora darbību, maiņstrāvu, transformatoru "
                "un elektroenerģijas pārvadi.",
    "atgadne": [
        "F = BIl sin α   ·   F = qvB sin α   ·   Φ = BS cos α",
        "Indukcijas EDS:  ε = −ΔΦ/Δt   ·   Lenca likums: inducētā strāva "
        "pretojas plūsmas izmaiņai",
        "Transformators:  U₁/U₂ = N₁/N₂   ·   ideālam:  U₁I₁ = U₂I₂",
        "Zudumi līnijā:  P = I²R   ·   maiņstrāvas frekvence Latvijā 50 Hz",
    ],
    "struktura": [
        ("1.", "Skaidro magnētisko lauku, indukciju, maiņstrāvu un "
               "pārvadi", "51.-62.", 10),
        ("2.", "Aizpilda magnētisko lielumu un mērvienību tabulu",
         "51.-54.", 5),
        ("3.", "Aprēķina spēku uz strāvas vadītāju magnētiskajā laukā",
         "52.", 5),
        ("4.", "Lieto transformatora vijumu un spriegumu attiecību",
         "57.", 5),
        ("5.", "Analizē indukciju un elektroenerģijas pārvadi",
         "54., 55., 58.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kas rada magnētisko lauku ap taisnu vadu?",
                 ["statisks lādiņš", "elektriskā strāva vadā",
                  "vada masa", "vada pretestība"], 1),
                ("Kā vērstas magnētiskā lauka līnijas ap taisnu strāvas "
                 "vadu?",
                 ["radiāli prom no vada", "koncentriskās riņķa līnijās ap "
                  "vadu", "paralēli vadam", "lauka nav"], 1),
                ("No kā ir atkarīgs spēks uz strāvas vadītāju magnētiskajā "
                 "laukā?",
                 ["tikai no strāvas",
                  "no indukcijas, strāvas, vada garuma un leņķa",
                  "tikai no vada masas", "no vada pretestības"], 1),
                ("Kāda ir magnētiskās indukcijas mērvienība?",
                 ["vēbers", "tesla", "henrijs", "tesla uz metru"], 1),
                ("Kad uz lādētu daļiņu magnētiskajā laukā spēks nedarbojas?",
                 ["kad tā kustas perpendikulāri laukam",
                  "kad tā kustas paralēli lauka līnijām",
                  "kad tā ir negatīva", "vienmēr darbojas"], 1),
                ("Kas ir magnētiskā plūsma?",
                 ["strāvas stiprums cauri spolei",
                  "lielums, kas raksturo lauka līniju daudzumu cauri "
                  "laukumam",
                  "lauka enerģija", "spole ar dzelzs serdi"], 1),
                ("Kad spolē rodas indukcijas EDS?",
                 ["kad magnētiskā plūsma cauri spolei mainās",
                  "kad plūsma ir liela un nemainīga",
                  "kad spole ir ieslēgta līdzstrāvā",
                  "kad spolei ir liela pretestība"], 0),
                ("Ko nosaka Lenca likums?",
                 ["indukcijas EDS lielumu",
                  "inducētās strāvas virzienu",
                  "spoles pretestību", "lauka indukciju"], 1),
                ("Ar ko maiņstrāva atšķiras no līdzstrāvas?",
                 ["tā ir stiprāka",
                  "tās virziens un vērtība periodiski mainās",
                  "tā plūst tikai pusvadītājos",
                  "tai nav frekvences"], 1),
                ("Kāpēc transformators nedarbojas ar līdzstrāvu?",
                 ["līdzstrāva ir par vāju",
                  "nemainīga strāva nerada mainīgu magnētisko plūsmu",
                  "serde uzkarst", "vijumi ir pārāk plāni"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Magnētiskie lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Magnētiskās indukcijas SI mērvienība  [B] = ......"
                      "...............", "tesla (T)"),
                     ("Magnētiskās plūsmas mērvienība  [Φ] = ..........."
                      "..........", "vēbers (Wb)"),
                     ("Spēks, ja B = 0,20 T, I = 3,0 A, l = 0,50 m, "
                      "α = 90°  F = ..................... N", "0,30 N"),
                     ("Plūsma, ja B = 0,50 T, S = 0,020 m², α = 0°  "
                      "Φ = ..................... Wb", "0,010 Wb"),
                     ("Maiņstrāvas frekvence Latvijas tīklā  "
                      "f = ..................... Hz", "50 Hz"),
                 ]},

                {"tips": "aprekins",
                 "virs": "Spēks uz strāvas vadītāju", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Taisns vads, kura aktīvais garums magnētiskajā "
                           "laukā ir 25 cm, atrodas laukā ar indukciju "
                           "0,40 T perpendikulāri lauka līnijām. Vadā plūst "
                           "strāva 6,0 A. Aprēķini spēku, kas darbojas uz "
                           "vadu!",
                 "risinajums": [
                     "Dots:  l = 25 cm = 0,25 m;  B = 0,40 T;  I = 6,0 A;  "
                     "α = 90°",
                     "Jāaprēķina:  F = ?",
                     "Formulas:  F = BIl sin α",
                     "Aprēķins:  1) sin 90° = 1",
                     "                   2) F = 0,40 · 6,0 · 0,25 · 1 = "
                     "0,60 N",
                     "Atbilde:  F = 0,60 N; spēks vērsts perpendikulāri gan "
                     "vadam, gan lauka līnijām (kreisās rokas likums).",
                 ],
                 "kriteriji": [
                     "1 p - garums pārveidots metros;",
                     "1 p - pareiza formula ar sin α;",
                     "2 p - pareizs aprēķins;",
                     "1 p - atbilde ar mērvienību un spēka virziena "
                     "norāde.",
                 ]},

                {"tips": "aprekins", "virs": "Transformators", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Transformatora primārajā tinumā ir 1100 vijumi, "
                           "un tam pieliek spriegumu 220 V. Sekundārajā "
                           "tinumā ir 60 vijumi. Aprēķini sekundāro "
                           "spriegumu un sekundāro strāvu, ja primārā "
                           "strāva ir 0,30 A un zudumus neievēro!",
                 "risinajums": [
                     "Dots:  N₁ = 1100;  U₁ = 220 V;  N₂ = 60;  "
                     "I₁ = 0,30 A",
                     "Jāaprēķina:  U₂ = ?;  I₂ = ?",
                     "Formulas:  U₁/U₂ = N₁/N₂;  U₁I₁ = U₂I₂",
                     "Aprēķins:  1) U₂ = U₁ · N₂/N₁ = 220 · 60 : 1100 = "
                     "12 V",
                     "                   2) I₂ = U₁I₁ : U₂ = "
                     "220 · 0,30 : 12 = 5,5 A",
                     "Atbilde:  U₂ = 12 V;  I₂ = 5,5 A (pazeminošs "
                     "transformators).",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīti dotie lielumi;",
                     "1 p - pareiza vijumu attiecības formula;",
                     "2 p - pareizi aprēķināti U₂ un I₂;",
                     "1 p - atbildes ar mērvienībām un secinājums par "
                     "transformatora veidu.",
                 ]},

                {"tips": "jautajumi",
                 "virs": "Indukcija un enerģijas pārvade",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Magnētu strauji iebīda spolē, kas savienota ar "
                           "jutīgu galvanometru. Pēc tam to pašu magnētu "
                           "iebīda lēnām.",
                 "jaut": [
                     ("Paskaidro, kāpēc galvanometrs rāda strāvu!", 1),
                     ("Kurā gadījumā strāva ir lielāka un kāpēc?", 1),
                     ("Nosaki, kā mainīsies strāvas virziens, magnētu "
                      "izvelkot, un pamato ar Lenca likumu!", 1),
                     ("Nosauc ierīci, kuras darbība balstās uz šo "
                      "parādību!", 1),
                     ("Paskaidro, kāpēc elektroenerģiju pārvada ar augstu "
                      "spriegumu!", 1),
                 ],
                 "atbildes": [
                     "1) Mainās magnētiskā plūsma cauri spolei, tāpēc "
                     "spolē inducējas EDS un plūst strāva.   (1 p)",
                     "2) Strauji bīdot, jo ε = −ΔΦ/Δt - jo ātrāk mainās "
                     "plūsma, jo lielāks EDS.   (1 p)",
                     "3) Virziens mainās uz pretējo: inducētā strāva "
                     "vienmēr pretojas plūsmas izmaiņai, tāpēc, izvelkot "
                     "magnētu, tā cenšas plūsmu uzturēt.   (1 p)",
                     "4) Piemēram, elektroģenerators (arī indukcijas plīts, "
                     "mikrofons, transformators).   (1 p)",
                     "5) Pie tās pašas jaudas P = UI augstāks spriegums "
                     "nozīmē mazāku strāvu, bet zudumi līnijā "
                     "P = I²R, tāpēc tie strauji samazinās.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kas notiek ar dzelzs serdi spoles iekšpusē, plūstot "
                 "strāvai?",
                 ["tā atdziest", "tā pastiprina magnētisko lauku",
                  "tā vājina lauku", "tā uzlādējas elektriski"], 1),
                ("Ar kuru likumu nosaka lauka līniju virzienu ap strāvas "
                 "vadu?",
                 ["kreisās rokas likumu", "labās rokas (bura) likumu",
                  "Oma likumu", "Lenca likumu"], 1),
                ("Kad spēks uz strāvas vadītāju laukā ir vislielākais?",
                 ["kad vads ir paralēls lauka līnijām",
                  "kad vads ir perpendikulārs lauka līnijām",
                  "kad strāva ir nulle", "kad lauks ir nulle"], 1),
                ("Kāda ir magnētiskās plūsmas mērvienība?",
                 ["tesla", "vēbers", "henrijs", "džouls"], 1),
                ("Kāpēc lādēta daļiņa perpendikulārā magnētiskajā laukā "
                 "kustas pa riņķa līniju?",
                 ["spēks ir vērsts kustības virzienā",
                  "spēks vienmēr ir perpendikulārs ātrumam",
                  "daļiņa zaudē enerģiju", "lauks to pievelk"], 1),
                ("Kas ir ģenerators?",
                 ["ierīce, kas elektroenerģiju pārvērš mehāniskajā",
                  "ierīce, kas mehānisko enerģiju pārvērš elektriskajā",
                  "ierīce, kas maina spriegumu",
                  "ierīce, kas uzkrāj lādiņu"], 1),
                ("Ko rāda maiņstrāvas efektīvā vērtība?",
                 ["maksimālo strāvu",
                  "līdzstrāvu, kas dotu tādu pašu siltuma efektu",
                  "vidējo strāvu par periodu",
                  "strāvu tukšgaitā"], 1),
                ("Transformatoram N₂ > N₁. Kāds tas ir?",
                 ["pazeminošs", "paaugstinošs", "neitrāls",
                  "nedarbojas"], 1),
                ("Kāpēc transformatora serdi veido no plānām, izolētām "
                 "plāksnēm?",
                 ["lai tā būtu vieglāka",
                  "lai samazinātu virpuļstrāvu zudumus",
                  "lai palielinātu vijumu skaitu",
                  "lai tā labāk vadītu strāvu"], 1),
                ("Kāpēc ziemeļblāzma redzama polos?",
                 ["tur ir aukstāks",
                  "Zemes magnētiskais lauks novirza lādētās daļiņas uz "
                  "poliem",
                  "tur ir plānāka atmosfēra",
                  "Saule tur ir tuvāk"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Magnētiskie lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Magnētiskās plūsmas SI mērvienība  [Φ] = ........."
                      "............", "vēbers (Wb)"),
                     ("Spēka uz lādētu daļiņu formula  F = ............."
                      "........", "F = qvB sin α"),
                     ("Spēks, ja B = 0,50 T, I = 2,0 A, l = 0,20 m, "
                      "α = 90°  F = ..................... N", "0,20 N"),
                     ("Sekundārais spriegums, ja U₁ = 230 V, N₁ = 460, "
                      "N₂ = 24  U₂ = ..................... V", "12 V"),
                     ("Maiņstrāvas periods, ja f = 50 Hz  "
                      "T = ..................... s", "0,02 s"),
                 ]},

                {"tips": "aprekins",
                 "virs": "Spēks uz strāvas vadītāju", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Vads ar aktīvo garumu 40 cm atrodas "
                           "magnētiskajā laukā perpendikulāri lauka "
                           "līnijām. Vadā plūst strāva 2,5 A, un uz vadu "
                           "darbojas spēks 0,30 N. Aprēķini magnētiskā "
                           "lauka indukciju!",
                 "risinajums": [
                     "Dots:  l = 40 cm = 0,40 m;  I = 2,5 A;  F = 0,30 N;  "
                     "α = 90°",
                     "Jāaprēķina:  B = ?",
                     "Formulas:  F = BIl sin α  ⟹  B = F / (I l sin α)",
                     "Aprēķins:  1) I l = 2,5 · 0,40 = 1,0 A·m",
                     "                   2) B = 0,30 : 1,0 = 0,30 T",
                     "Atbilde:  B = 0,30 T.",
                 ],
                 "kriteriji": [
                     "1 p - garums pārveidots metros;",
                     "1 p - formula izteikta attiecībā pret B;",
                     "2 p - pareizs aprēķins;",
                     "1 p - atbilde ar mērvienību.",
                 ]},

                {"tips": "aprekins", "virs": "Transformators", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Metināšanas transformatora primārajā tinumā ir "
                           "920 vijumi un spriegums 230 V; sekundārajā "
                           "tinumā spriegums ir 25 V. Aprēķini sekundāro "
                           "vijumu skaitu un primāro strāvu, ja sekundārā "
                           "strāva ir 40 A un zudumus neievēro!",
                 "risinajums": [
                     "Dots:  N₁ = 920;  U₁ = 230 V;  U₂ = 25 V;  "
                     "I₂ = 40 A",
                     "Jāaprēķina:  N₂ = ?;  I₁ = ?",
                     "Formulas:  U₁/U₂ = N₁/N₂;  U₁I₁ = U₂I₂",
                     "Aprēķins:  1) N₂ = N₁ · U₂/U₁ = 920 · 25 : 230 = "
                     "100 vijumi",
                     "                   2) I₁ = U₂I₂ : U₁ = "
                     "25 · 40 : 230 ≈ 4,3 A",
                     "Atbilde:  N₂ = 100 vijumi;  I₁ ≈ 4,3 A.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīti dotie lielumi;",
                     "1 p - pareiza vijumu attiecības formula;",
                     "2 p - pareizi aprēķināti N₂ un I₁;",
                     "1 p - atbildes ar mērvienībām.",
                 ]},

                {"tips": "jautajumi",
                 "virs": "Motors, ģenerators un pārvade",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Vēja ģenerators ražo elektroenerģiju un padod "
                           "to pārvades līnijā; pie patērētāja spriegumu "
                           "pazemina ar transformatoru.",
                 "jaut": [
                     ("Nosauc enerģijas pārvērtības ģeneratorā!", 1),
                     ("Paskaidro, ar ko ģenerators atšķiras no "
                      "elektromotora!", 1),
                     ("Paskaidro, kāpēc pirms pārvades spriegumu "
                      "paaugstina!", 1),
                     ("Aprēķini, cik reižu samazināsies jaudas zudumi "
                      "līnijā, spriegumu palielinot 10 reizes!", 1),
                     ("Paskaidro, kāpēc transformators nemaina pārvadīto "
                      "jaudu (ideālā gadījumā)!", 1),
                 ],
                 "atbildes": [
                     "1) Vēja kinētiskā enerģija → rotora mehāniskā "
                     "enerģija → elektriskā enerģija.   (1 p)",
                     "2) Ģenerators mehānisko enerģiju pārvērš "
                     "elektriskajā, motors - otrādi; abi izmanto to pašu "
                     "magnētiskā lauka mijiedarbību.   (1 p)",
                     "3) Pie tās pašas jaudas augstāks spriegums nozīmē "
                     "mazāku strāvu, un zudumi P = I²R samazinās.   (1 p)",
                     "4) Strāva samazinās 10 reizes, tāpēc zudumi "
                     "samazinās 10² = 100 reizes.   (1 p)",
                     "5) Enerģija netiek radīta: U₁I₁ = U₂I₂, tāpēc, "
                     "spriegumam palielinoties, strāva samazinās tikpat "
                     "reižu.   (1 p)",
                 ]},
            ],
        },
    ],
}
