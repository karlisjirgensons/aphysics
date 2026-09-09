# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD2 - Atoma un vielas uzbūve (6.-12. stunda)."""

PD = {
    "nr": 2,
    "klase": "11. klase",
    "nosaukums": "Atoma un vielas uzbūve",
    "mape": "7. Atoma un vielas uzbūve",
    "fails": "PD2. Atoma un vielas uzbūve_tt",
    "stundas": "6.-11.",
    "datums": "30.09.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda vielas daļiņu modeli, temperatūras skalas, "
                "difūziju un termisko izplešanos, šķidrumu īpašības, gāzes "
                "izoprocesus un ideālās gāzes vienādojumu.",
    "atgadne": [
        "T (K) = t (°C) + 273   ·   n = m / M = N / N(A)   ·   "
        "N(A) = 6,02 · 10²³ mol⁻¹",
        "pV = nRT   ·   R = 8,31 J/(mol·K)   ·   pV / T = const",
        "Izotermisks:  pV = const   ·   Izobārisks:  V / T = const   ·   "
        "Izohorisks:  p / T = const",
        "1 atm ≈ 1,0 · 10⁵ Pa   ·   1 L = 10⁻³ m³   ·   M(O₂) = 32 g/mol",
    ],
    "struktura": [
        ("1.", "Skaidro vielas daļiņu modeli, temperatūras skalas, "
               "difūziju, virsmas spraigumu un izoprocesus", "6.-11.", 10),
        ("2.", "Pārvērš temperatūras un vielas daudzuma lielumus",
         "6., 11.", 5),
        ("3.", "Lieto gāzes stāvokļa vienādojumu vai izoprocesa sakarību",
         "9.-11.", 5),
        ("4.", "Aprēķina vielas daudzumu un daļiņu skaitu", "6., 11.", 5),
        ("5.", "Analizē gāzes procesa grafiku un skaidro daļiņu modeli",
         "9., 10.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Ko raksturo vielas absolūtā temperatūra?",
                 ["daļiņu skaitu", "daļiņu vidējo kinētisko enerģiju",
                  "vielas masu", "vielas tilpumu"], 1),
                ("Cik kelvinos ir 27 °C?",
                 ["27 K", "246 K", "300 K", "573 K"], 2),
                ("Kāda ir zemākā iespējamā temperatūra?",
                 ["0 °C", "−100 °C", "0 K", "−273 K"], 2),
                ("Kāpēc smarža izplatās pa telpu?",
                 ["gaisa daļiņas nekustas",
                  "notiek difūzija - daļiņu haotiskā kustība",
                  "smarža ir vilnis", "gaiss izplešas"], 1),
                ("Kāpēc dzelzceļa sliedēm atstāj spraugas?",
                 ["lai ietaupītu metālu", "termiskās izplešanās dēļ",
                  "lai samazinātu troksni", "lai novadītu ūdeni"], 1),
                ("Kāda parādība izskaidro ūdens pilienu veidošanos?",
                 ["difūzija", "virsmas spraigums", "kapilaritāte",
                  "konvekcija"], 1),
                ("Izotermiskā procesā gāzes tilpumu samazina 2 reizes. Kā "
                 "mainās spiediens?",
                 ["samazinās 2 reizes", "palielinās 2 reizes",
                  "nemainās", "palielinās 4 reizes"], 1),
                ("Kāda ir vielas daudzuma SI mērvienība?",
                 ["grams", "kilograms", "mols", "kilomols"], 2),
                ("Kāpēc, sildot gāzi noslēgtā traukā, palielinās spiediens?",
                 ["daļiņu skaits pieaug", "daļiņas kļūst lielākas",
                  "daļiņas kustas ātrāk un biežāk atsitas pret sienām",
                  "trauks saraujas"], 2),
                ("Grafikā p(V) izotermai atbilst:",
                 ["taisne caur koordinātu sākumpunktu",
                  "horizontāla taisne", "hiperbola", "parabola"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Temperatūra un vielas daudzums",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību! Par katru pareizu "
                         "atbildi - 1 punkts.",
                 "rindas": [
                     ("100 °C = ..................... K", "373 K"),
                     ("0 K = ..................... °C", "−273 °C"),
                     ("2,0 L = ..................... m³", "2,0 · 10⁻³ m³"),
                     ("Vielas daudzums 64 g skābekļa (M = 32 g/mol)  "
                      "n = ..................... mol", "2,0 mol"),
                     ("Daļiņu skaits 0,50 mol vielā  N = ..................."
                      ".. ", "3,0 · 10²³"),
                 ]},

                {"tips": "aprekins", "virs": "Gāzes stāvokļa maiņa",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Noslēgtā traukā ar virzuli atrodas gāze: "
                           "V₁ = 4,0 L, p₁ = 1,0 · 10⁵ Pa, t₁ = 27 °C. Gāzi "
                           "saspiež līdz V₂ = 2,0 L un vienlaikus uzsilda "
                           "līdz t₂ = 127 °C. Aprēķini gala spiedienu!",
                 "risinajums": [
                     "Dots:  V₁ = 4,0 L;  p₁ = 1,0 · 10⁵ Pa;  t₁ = 27 °C;  "
                     "V₂ = 2,0 L;  t₂ = 127 °C",
                     "Jāaprēķina:  p₂ = ?",
                     "Formulas:  T = t + 273;  p₁V₁ / T₁ = p₂V₂ / T₂",
                     "Aprēķins:  1) T₁ = 300 K;  T₂ = 400 K",
                     "                   2) p₂ = p₁V₁T₂ / (T₁V₂)",
                     "                   3) p₂ = 1,0 · 10⁵ · 4,0 · 400 : "
                     "(300 · 2,0)",
                     "                   4) p₂ ≈ 2,7 · 10⁵ Pa",
                     "Atbilde:  p₂ ≈ 2,7 · 10⁵ Pa (aptuveni 2,7 atmosfēras).",
                 ],
                 "kriteriji": [
                     "1 p - temperatūras pārvērstas kelvinos;",
                     "1 p - pierakstīts apvienotais gāzes likums;",
                     "2 p - pareizi izteikts un aprēķināts p₂;",
                     "1 p - atbilde standartformā ar mērvienību.",
                 ]},

                {"tips": "aprekins", "virs": "Ideālās gāzes vienādojums",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Balonā ar tilpumu V = 20 L atrodas n = 1,5 mol "
                           "hēlija temperatūrā t = 27 °C. Aprēķini gāzes "
                           "spiedienu balonā! (R = 8,31 J/(mol·K))",
                 "risinajums": [
                     "Dots:  V = 20 L = 2,0 · 10⁻² m³;  n = 1,5 mol;  "
                     "t = 27 °C;  R = 8,31 J/(mol·K)",
                     "Jāaprēķina:  p = ?",
                     "Formulas:  T = t + 273;  pV = nRT  →  p = nRT / V",
                     "Aprēķins:  1) T = 27 + 273 = 300 K",
                     "                   2) nRT = 1,5 · 8,31 · 300 ≈ 3740 J",
                     "                   3) p = 3740 : 2,0 · 10⁻² ≈ "
                     "1,9 · 10⁵ Pa",
                     "Atbilde:  p ≈ 1,9 · 10⁵ Pa.",
                 ],
                 "kriteriji": [
                     "1 p - tilpums pārvērsts m³ un temperatūra kelvinos;",
                     "1 p - pierakstīts vienādojums pV = nRT;",
                     "2 p - pareizs aprēķins ar mērvienību;",
                     "1 p - atbilde standartformā.",
                 ]},

                {"tips": "jautajumi", "virs": "Daļiņu modelis un grafiki",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Slēgtā traukā ar nekustīgu virzuli gāzi silda no "
                           "300 K līdz 600 K.",
                 "jaut": [
                     ("Nosauc, kurš izoprocess notiek, un pieraksti tā "
                      "sakarību!", 1),
                     ("Cik reižu mainās gāzes spiediens?", 1),
                     ("Ar daļiņu modeli paskaidro, kāpēc spiediens mainās "
                      "tieši tā!", 1),
                     ("Uzzīmē šī procesa grafiku p(T) asīs!", 1),
                     ("Nosauc vienu nosacījumu, kad ideālās gāzes modelis "
                      "vairs nav lietojams!", 1),
                 ],
                 "atbildes": [
                     "1) Izohorisks process (V = const);  p / T = const.   "
                     "(1 p)",
                     "2) Spiediens palielinās 2 reizes (T pieaug 2 reizes).   "
                     "(1 p)",
                     "3) Augstākā temperatūrā daļiņas kustas ātrāk, tāpēc "
                     "biežāk un ar lielāku impulsu atsitas pret trauka "
                     "sienām - spiediens pieaug.   (1 p)",
                     "4) Taisne, kas iziet caur koordinātu sākumpunktu "
                     "(p ~ T).   (1 p)",
                     "5) Ļoti augsts spiediens vai zema temperatūra, kad "
                     "daļiņu izmērs un savstarpējā pievilkšanās kļūst "
                     "būtiska (gāze tuvojas sašķidrināšanās stāvoklim).   "
                     "(1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Ko nosaka vielas daļiņu haotiskā kustība?",
                 ["vielas krāsu", "vielas temperatūru", "vielas masu",
                  "vielas formu"], 1),
                ("Cik kelvinos ir −73 °C?",
                 ["73 K", "200 K", "346 K", "−200 K"], 1),
                ("Cik Celsija grādos ir 350 K?",
                 ["350 °C", "77 °C", "−77 °C", "623 °C"], 1),
                ("Kā difūzija mainās, paaugstinoties temperatūrai?",
                 ["kļūst lēnāka", "kļūst ātrāka", "nemainās",
                  "apstājas"], 1),
                ("Kāpēc ūdens paceļas plānā stikla caurulītē?",
                 ["difūzijas dēļ", "kapilaritātes dēļ",
                  "konvekcijas dēļ", "izplešanās dēļ"], 1),
                ("Kāpēc ūdens lāse gaisā iegūst apaļu formu?",
                 ["gravitācijas dēļ", "virsmas spraiguma dēļ",
                  "difūzijas dēļ", "spiediena dēļ"], 1),
                ("Izobāriskā procesā gāzes absolūto temperatūru palielina "
                 "2 reizes. Kā mainās tilpums?",
                 ["samazinās 2 reizes", "palielinās 2 reizes",
                  "nemainās", "palielinās 4 reizes"], 1),
                ("Cik daļiņu ir vienā molā vielas?",
                 ["10²³", "6,02 · 10²³", "6,02 · 10²⁶", "8,31 · 10²³"], 1),
                ("Kāpēc gāze aizņem visu tai pieejamo tilpumu?",
                 ["daļiņas savstarpēji pievelkas",
                  "daļiņas kustas haotiski un gandrīz nemijiedarbojas",
                  "daļiņas ir ļoti lielas",
                  "gāzei ir noteikta forma"], 1),
                ("Grafikā V(T) izobārai atbilst:",
                 ["hiperbola", "horizontāla taisne",
                  "taisne caur koordinātu sākumpunktu", "parabola"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Temperatūra un vielas daudzums",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību! Par katru pareizu "
                         "atbildi - 1 punkts.",
                 "rindas": [
                     ("20 °C = ..................... K", "293 K"),
                     ("500 K = ..................... °C", "227 °C"),
                     ("250 mL = ..................... m³",
                      "2,5 · 10⁻⁴ m³"),
                     ("Masa 3,0 mol ūdens (M = 18 g/mol)  m = ............."
                      "........ g", "54 g"),
                     ("Vielas daudzums, ja N = 1,2 · 10²⁴ daļiņas  "
                      "n = ..................... mol", "2,0 mol"),
                 ]},

                {"tips": "aprekins", "virs": "Gāzes stāvokļa maiņa",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Noslēgtā traukā ar virzuli atrodas gāze: "
                           "V₁ = 6,0 L, p₁ = 2,0 · 10⁵ Pa, t₁ = 27 °C. Gāzi "
                           "atdzesē līdz t₂ = −73 °C, un tilpums samazinās "
                           "līdz V₂ = 3,0 L. Aprēķini gala spiedienu!",
                 "risinajums": [
                     "Dots:  V₁ = 6,0 L;  p₁ = 2,0 · 10⁵ Pa;  t₁ = 27 °C;  "
                     "V₂ = 3,0 L;  t₂ = −73 °C",
                     "Jāaprēķina:  p₂ = ?",
                     "Formulas:  T = t + 273;  p₁V₁ / T₁ = p₂V₂ / T₂",
                     "Aprēķins:  1) T₁ = 300 K;  T₂ = 200 K",
                     "                   2) p₂ = p₁V₁T₂ / (T₁V₂)",
                     "                   3) p₂ = 2,0 · 10⁵ · 6,0 · 200 : "
                     "(300 · 3,0)",
                     "                   4) p₂ ≈ 2,7 · 10⁵ Pa",
                     "Atbilde:  p₂ ≈ 2,7 · 10⁵ Pa.",
                 ],
                 "kriteriji": [
                     "1 p - temperatūras pārvērstas kelvinos;",
                     "1 p - pierakstīts apvienotais gāzes likums;",
                     "2 p - pareizi izteikts un aprēķināts p₂;",
                     "1 p - atbilde standartformā ar mērvienību.",
                 ]},

                {"tips": "aprekins", "virs": "Ideālās gāzes vienādojums",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Traukā ar tilpumu V = 5,0 L atrodas gāze "
                           "spiedienā p = 4,0 · 10⁵ Pa temperatūrā "
                           "t = 27 °C. Aprēķini gāzes vielas daudzumu! "
                           "(R = 8,31 J/(mol·K))",
                 "risinajums": [
                     "Dots:  V = 5,0 L = 5,0 · 10⁻³ m³;  p = 4,0 · 10⁵ Pa;  "
                     "t = 27 °C",
                     "Jāaprēķina:  n = ?",
                     "Formulas:  T = t + 273;  pV = nRT  →  n = pV / (RT)",
                     "Aprēķins:  1) T = 300 K",
                     "                   2) pV = 4,0 · 10⁵ · 5,0 · 10⁻³ = "
                     "2000 J",
                     "                   3) n = 2000 : (8,31 · 300) ≈ "
                     "0,80 mol",
                     "Atbilde:  n ≈ 0,80 mol.",
                 ],
                 "kriteriji": [
                     "1 p - tilpums pārvērsts m³ un temperatūra kelvinos;",
                     "1 p - pierakstīts vienādojums pV = nRT;",
                     "2 p - pareizs aprēķins ar mērvienību;",
                     "1 p - atbilde ar pareizu precizitāti.",
                 ]},

                {"tips": "jautajumi", "virs": "Daļiņu modelis un grafiki",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Cilindrā ar brīvi kustīgu virzuli gāzi silda no "
                           "250 K līdz 500 K; ārējais spiediens nemainās.",
                 "jaut": [
                     ("Nosauc, kurš izoprocess notiek, un pieraksti tā "
                      "sakarību!", 1),
                     ("Cik reižu mainās gāzes tilpums?", 1),
                     ("Ar daļiņu modeli paskaidro, kāpēc virzulis "
                      "pārvietojas!", 1),
                     ("Uzzīmē šī procesa grafiku V(T) asīs!", 1),
                     ("Paskaidro, kāpēc šajā procesā gāze veic darbu!", 1),
                 ],
                 "atbildes": [
                     "1) Izobārisks process (p = const);  V / T = const.   "
                     "(1 p)",
                     "2) Tilpums palielinās 2 reizes.   (1 p)",
                     "3) Sildot daļiņas kustas ātrāk un spiestu stiprāk, bet "
                     "virzulis ir brīvs, tāpēc gāze izplešas, līdz spiediens "
                     "atkal līdzsvarojas ar ārējo.   (1 p)",
                     "4) Taisne, kas iziet caur koordinātu sākumpunktu "
                     "(V ~ T).   (1 p)",
                     "5) Gāze pārvieto virzuli pret ārējo spiedienu; "
                     "A = pΔV > 0, tāpēc gāze veic darbu.   (1 p)",
                 ]},
            ],
        },
    ],
}
