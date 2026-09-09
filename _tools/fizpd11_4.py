# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD4 - Elektriskie lādiņi un elektriskais lauks."""

PD = {
    "nr": 4,
    "klase": "11. klase",
    "nosaukums": "Elektriskie lādiņi un elektriskais lauks",
    "mape": "9. Elektriskie lādiņi",
    "fails": "PD4. Elektriskie lādiņi un elektriskais lauks_tt",
    "stundas": "25.-30.",
    "datums": "25.11.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda elektrizāciju un lādiņa nezūdamību, Kulona "
                "likumu, elektriskā lauka intensitāti, spriegumu un darbu "
                "laukā, kā arī kondensatora jēdzienu un elektrostatikas "
                "lietojumus sadzīvē.",
    "atgadne": [
        "F = k · q₁q₂ / r²,  kur k = 9 · 10⁹ N·m²/C²   ·   e = 1,6 · 10⁻¹⁹ C",
        "E = F/q   ·   E = U/d   ·   U = A/q   ·   A = qU",
        "C = q/U   ·   1 F = 1 C/V   ·   1 µF = 10⁻⁶ F",
        "Lauka līnijas sākas uz pozitīva un beidzas uz negatīva lādiņa.",
    ],
    "struktura": [
        ("1.", "Skaidro elektrizāciju, lauku, spriegumu un elektrostatikas "
               "lietojumus", "25.-30.", 10),
        ("2.", "Aizpilda elektrisko lielumu un mērvienību tabulu",
         "25.-28.", 5),
        ("3.", "Lieto Kulona likumu", "26.", 5),
        ("4.", "Aprēķina lauka intensitāti un darbu laukā", "27., 28.", 5),
        ("5.", "Analizē kondensatoru un elektrostatikas piemēru",
         "29., 30.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kas notiek, ebonīta nūjiņu berzējot ar vilnu?",
                 ["rodas jauni lādiņi",
                  "lādiņi pāriet no viena ķermeņa uz otru",
                  "lādiņi pazūd",
                  "abi ķermeņi iegūst vienādas zīmes lādiņu"], 1),
                ("Kurš apgalvojums atbilst lādiņa nezūdamības likumam?",
                 ["lādiņš var rasties no nekā",
                  "slēgtā sistēmā lādiņu algebriskā summa nemainās",
                  "lādiņš vienmēr pieaug",
                  "lādiņš ir atkarīgs no temperatūras"], 1),
                ("Kā mainās Kulona spēks, attālumu starp lādiņiem "
                 "palielinot 3 reizes?",
                 ["samazinās 3 reizes", "samazinās 9 reizes",
                  "palielinās 3 reizes", "nemainās"], 1),
                ("Kāda ir elektriskā lauka intensitātes mērvienība?",
                 ["V·m", "N/C jeb V/m", "C/N", "J/C"], 1),
                ("Kur vērsta lauka intensitāte punktā ap pozitīvu lādiņu?",
                 ["uz lādiņu", "prom no lādiņa",
                  "pa apli ap lādiņu", "virziena nav"], 1),
                ("Ko nozīmē spriegums 12 V?",
                 ["katrs 1 C lādiņš pārnes 12 J enerģijas",
                  "ķēdē plūst 12 A", "pretestība ir 12 Ω",
                  "lādiņš ir 12 C"], 0),
                ("Kāpēc automašīna ir samērā droša vieta negaisā?",
                 ["riepas ir izolators",
                  "metāla virsbūve darbojas kā ekrāns un lādiņš paliek uz "
                  "virsmas",
                  "mašīna ir smaga", "stikls neielaiž zibeni"], 1),
                ("Kur uz vadītāja izvietojas liekais lādiņš?",
                 ["vienmērīgi pa tilpumu", "vadītāja centrā",
                  "uz ārējās virsmas", "netiek izvietots"], 2),
                ("Kas raksturo kondensatora kapacitāti?",
                 ["cik daudz enerģijas tas patērē",
                  "cik lielu lādiņu tas uzkrāj uz katru sprieguma voltu",
                  "cik ātri tas uzlādējas", "kāda ir tā pretestība"], 1),
                ("Kāpēc degvielas cisternai pievieno zemējuma vadu?",
                 ["lai nesabojātu sūkni",
                  "lai novadītu statisko lādiņu un novērstu dzirksteli",
                  "lai mērītu tilpumu", "lai atdzesētu degvielu"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Elektriskie lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Elektriskā lādiņa SI mērvienība  [q] = ............"
                      ".........", "kulons (C)"),
                     ("Lauka intensitātes mērvienība  [E] = .............."
                      ".......", "N/C jeb V/m"),
                     ("Elementārlādiņš  e = ..................... C",
                      "1,6 · 10⁻¹⁹ C"),
                     ("Lādiņš, ja U = 20 V un C = 5,0 µF  q = ..........."
                      ".......... C", "1,0 · 10⁻⁴ C = 100 µC"),
                     ("Darbs, pārvietojot q = 2,0 mC pie U = 50 V  "
                      "A = ..................... J", "0,10 J"),
                 ]},

                {"tips": "aprekins", "virs": "Kulona likums", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Divi punktveida lādiņi q₁ = 4,0 · 10⁻⁸ C un "
                           "q₂ = 6,0 · 10⁻⁸ C vakuumā atrodas 6,0 cm "
                           "attālumā viens no otra. Aprēķini mijiedarbības "
                           "spēku! (k = 9 · 10⁹ N·m²/C²)",
                 "risinajums": [
                     "Dots:  q₁ = 4,0 · 10⁻⁸ C;  q₂ = 6,0 · 10⁻⁸ C;  "
                     "r = 6,0 cm = 0,060 m;  k = 9 · 10⁹ N·m²/C²",
                     "Jāaprēķina:  F = ?",
                     "Formulas:  F = k · q₁q₂ / r²",
                     "Aprēķins:  1) q₁q₂ = 4,0 · 10⁻⁸ · 6,0 · 10⁻⁸ = "
                     "2,4 · 10⁻¹⁵ C²",
                     "                   2) r² = 0,060² = 3,6 · 10⁻³ m²",
                     "                   3) F = 9 · 10⁹ · 2,4 · 10⁻¹⁵ : "
                     "3,6 · 10⁻³ = 6,0 · 10⁻³ N",
                     "Atbilde:  F = 6,0 · 10⁻³ N = 6,0 mN (lādiņi "
                     "atgrūžas).",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīti dotie lielumi SI vienībās;",
                     "1 p - pareiza formula;",
                     "2 p - pareizi ievietotas vērtības un aprēķins;",
                     "1 p - atbilde ar mērvienību un spēka virziena norāde.",
                 ]},

                {"tips": "aprekins", "virs": "Lauks un darbs laukā",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Starp divām plāksnēm, kas atrodas 4,0 mm "
                           "attālumā, uzturēts spriegums 240 V. Aprēķini "
                           "lauka intensitāti starp plāksnēm un darbu, ko "
                           "lauks veic, pārvietojot elektronu no vienas "
                           "plāksnes līdz otrai! (e = 1,6 · 10⁻¹⁹ C)",
                 "risinajums": [
                     "Dots:  U = 240 V;  d = 4,0 mm = 4,0 · 10⁻³ m;  "
                     "q = e = 1,6 · 10⁻¹⁹ C",
                     "Jāaprēķina:  E = ?;  A = ?",
                     "Formulas:  E = U/d;  A = qU",
                     "Aprēķins:  1) E = 240 : 4,0 · 10⁻³ = 6,0 · 10⁴ V/m",
                     "                   2) A = 1,6 · 10⁻¹⁹ · 240 = "
                     "3,84 · 10⁻¹⁷ J",
                     "Atbilde:  E = 6,0 · 10⁴ V/m;  A ≈ 3,8 · 10⁻¹⁷ J.",
                 ],
                 "kriteriji": [
                     "1 p - attālums pārveidots metros;",
                     "1 p - pareizas abas formulas;",
                     "2 p - pareizi aprēķināti E un A;",
                     "1 p - abas atbildes ar mērvienībām.",
                 ]},

                {"tips": "jautajumi",
                 "virs": "Kondensators un lādiņu pārdale",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Kondensatora kapacitāte ir C = 20 µF, un tas "
                           "pieslēgts 12 V spriegumam.",
                 "jaut": [
                     ("Aprēķini kondensatora uzkrāto lādiņu!", 1),
                     ("Kā mainīsies lādiņš, ja spriegumu palielinās "
                      "2 reizes? Pamato ar formulu!", 1),
                     ("Paskaidro, kas notiek ar kondensatoru, ja starp "
                      "plāksnēm ievieto dielektriķi!", 1),
                     ("Nosauc vienu ierīci, kurā kondensators uzkrāj "
                      "enerģiju, un paskaidro, kāpēc tur to izmanto!", 1),
                     ("Paskaidro, kāpēc pēc atslēgšanas no barošanas "
                      "kondensatoru drīkst aiztikt tikai pēc izlādēšanas!",
                      1),
                 ],
                 "atbildes": [
                     "1) q = CU = 20 · 10⁻⁶ · 12 = 2,4 · 10⁻⁴ C = "
                     "240 µC.   (1 p)",
                     "2) Lādiņš palielināsies 2 reizes, jo q = CU un C "
                     "nemainās; q = 4,8 · 10⁻⁴ C.   (1 p)",
                     "3) Kapacitāte palielinās, jo dielektriķis vājina "
                     "lauku starp plāksnēm; pie tā paša sprieguma uzkrājas "
                     "lielāks lādiņš.   (1 p)",
                     "4) Piemēram, fotoaparāta zibspuldze - kondensators "
                     "lēni uzkrāj enerģiju un atdod to ļoti īsā laikā, "
                     "nodrošinot lielu momentāno jaudu.   (1 p)",
                     "5) Uzlādēts kondensators saglabā lādiņu arī pēc "
                     "atslēgšanas, tāpēc pieskaršanās var radīt strāvas "
                     "triecienu; to izlādē caur rezistoru.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kāpēc sausā laikā apģērbs elektrizējas vairāk?",
                 ["gaiss ir siltāks",
                  "sausā gaisā lādiņš neaizplūst un uzkrājas",
                  "audums kļūst smagāks", "samazinās gravitācija"], 1),
                ("Kurš materiāls ir labs elektriskās strāvas vadītājs?",
                 ["stikls", "varš", "gumija", "sauss koks"], 1),
                ("Kā mainās Kulona spēks, ja abus lādiņus palielina "
                 "2 reizes?",
                 ["palielinās 2 reizes", "palielinās 4 reizes",
                  "samazinās 2 reizes", "nemainās"], 1),
                ("Ko rāda elektriskā lauka līniju blīvums?",
                 ["lauka intensitātes lielumu", "lādiņa zīmi",
                  "spriegumu", "vadītāja pretestību"], 0),
                ("Kā vērsts spēks, kas darbojas uz negatīvu lādiņu laukā?",
                 ["lauka intensitātes virzienā",
                  "pretēji lauka intensitātes virzienam",
                  "perpendikulāri laukam", "spēks nedarbojas"], 1),
                ("Kāda ir sprieguma mērvienība?",
                 ["kulons", "volts", "ampērs", "džouls"], 1),
                ("Ko sauc par ekvipotenciālu virsmu?",
                 ["virsmu, kur lauks ir nulle",
                  "virsmu, kuras visos punktos potenciāls ir vienāds",
                  "vadītāja iekšpusi", "lādiņa robežu"], 1),
                ("Kāpēc lidmašīnai ir statiskās elektrības novadītāji?",
                 ["lai samazinātu gaisa pretestību",
                  "lai lidojumā uzkrāto lādiņu droši novadītu gaisā",
                  "lai uzlabotu radiosakarus ar zemi",
                  "lai mērītu augstumu"], 1),
                ("Kā aprēķina kondensatora kapacitāti?",
                 ["C = qU", "C = q/U", "C = U/q", "C = q + U"], 1),
                ("Kāpēc zibensnovedējam ir smails gals?",
                 ["tas ir lētāk",
                  "pie smaila gala lauks ir visstiprākais un izlāde notiek "
                  "tur",
                  "tas mazāk rūsē", "tas ir vieglāks"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Elektriskie lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Kapacitātes SI mērvienība  [C] = .................."
                      "...", "farads (F)"),
                     ("Sprieguma mērvienība ar pamatlielumiem  [U] = ....."
                      "................", "J/C"),
                     ("Kulona konstante  k = ..................... "
                      "N·m²/C²", "9 · 10⁹ N·m²/C²"),
                     ("Lauka intensitāte, ja U = 300 V un d = 2,0 cm  "
                      "E = ..................... V/m", "1,5 · 10⁴ V/m"),
                     ("Lādiņš 5,0 µC kulonos  q = ..................... C",
                      "5,0 · 10⁻⁶ C"),
                 ]},

                {"tips": "aprekins", "virs": "Kulona likums", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Divi vienādi punktveida lādiņi vakuumā 10 cm "
                           "attālumā atgrūžas ar spēku 9,0 · 10⁻³ N. "
                           "Aprēķini katra lādiņa lielumu! "
                           "(k = 9 · 10⁹ N·m²/C²)",
                 "risinajums": [
                     "Dots:  F = 9,0 · 10⁻³ N;  r = 10 cm = 0,10 m;  "
                     "q₁ = q₂ = q;  k = 9 · 10⁹ N·m²/C²",
                     "Jāaprēķina:  q = ?",
                     "Formulas:  F = k · q² / r²  ⟹  q = √(F r² / k)",
                     "Aprēķins:  1) F r² = 9,0 · 10⁻³ · 0,010 = "
                     "9,0 · 10⁻⁵ N·m²",
                     "                   2) q² = 9,0 · 10⁻⁵ : 9 · 10⁹ = "
                     "1,0 · 10⁻¹⁴ C²",
                     "                   3) q = 1,0 · 10⁻⁷ C",
                     "Atbilde:  q = 1,0 · 10⁻⁷ C = 0,10 µC.",
                 ],
                 "kriteriji": [
                     "1 p - dotie lielumi SI vienībās;",
                     "1 p - formula izteikta attiecībā pret q;",
                     "2 p - pareizs aprēķins ar sakni;",
                     "1 p - atbilde ar mērvienību.",
                 ]},

                {"tips": "aprekins", "virs": "Lauks un darbs laukā",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Elektriskajā laukā, kura intensitāte ir "
                           "E = 2,5 · 10⁴ V/m, uz lādiņu darbojas spēks "
                           "F = 5,0 · 10⁻³ N. Aprēķini lādiņa lielumu un "
                           "darbu, pārvietojot šo lādiņu 3,0 cm gar lauka "
                           "līniju!",
                 "risinajums": [
                     "Dots:  E = 2,5 · 10⁴ V/m;  F = 5,0 · 10⁻³ N;  "
                     "d = 3,0 cm = 0,030 m",
                     "Jāaprēķina:  q = ?;  A = ?",
                     "Formulas:  E = F/q  ⟹  q = F/E;  A = F d",
                     "Aprēķins:  1) q = 5,0 · 10⁻³ : 2,5 · 10⁴ = "
                     "2,0 · 10⁻⁷ C",
                     "                   2) A = 5,0 · 10⁻³ · 0,030 = "
                     "1,5 · 10⁻⁴ J",
                     "Atbilde:  q = 2,0 · 10⁻⁷ C;  A = 1,5 · 10⁻⁴ J.",
                 ],
                 "kriteriji": [
                     "1 p - attālums pārveidots metros;",
                     "1 p - pareizas abas formulas;",
                     "2 p - pareizi aprēķināti q un A;",
                     "1 p - abas atbildes ar mērvienībām.",
                 ]},

                {"tips": "jautajumi", "virs": "Elektrostatika sadzīvē",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Lāzerprinterī uz gaismjutīga cilindra izveido "
                           "elektriski uzlādētu attēlu, uz kura pielīp "
                           "tonera daļiņas, un pēc tam attēls tiek pārnests "
                           "uz papīra.",
                 "jaut": [
                     ("Paskaidro, kāpēc tonera daļiņas pielīp tieši "
                      "uzlādētajām cilindra vietām!", 1),
                     ("Nosauc, kāda veida mijiedarbība to nodrošina, un "
                      "pieraksti attiecīgo likumu!", 1),
                     ("Paskaidro, kāpēc mitrā papīrā izdruka ir "
                      "sliktāka!", 1),
                     ("Nosauc vēl vienu tehnikas piemēru, kur izmanto "
                      "elektrostatisko pievilkšanos!", 1),
                     ("Paskaidro, kā no statiskās elektrības pasargā "
                      "elektronikas remontdarbnīcā!", 1),
                 ],
                 "atbildes": [
                     "1) Tonera daļiņas ir uzlādētas pretēji cilindra "
                     "attēla vietām, tāpēc tās pievelkas tikai tur.   (1 p)",
                     "2) Elektrostatiskā mijiedarbība; F = k · q₁q₂ / r² "
                     "(Kulona likums).   (1 p)",
                     "3) Mitrs papīrs vada lādiņu, tas aizplūst, un tonera "
                     "daļiņas netiek noturētas.   (1 p)",
                     "4) Piemēram, elektrostatiskie filtri rūpnīcu dūmeņos "
                     "vai elektrostatiskā krāsošana.   (1 p)",
                     "5) Lieto zemētus darba paklājus un rokas siksnas, "
                     "mitrina gaisu - lādiņš tiek nepārtraukti novadīts un "
                     "neuzkrājas.   (1 p)",
                 ]},
            ],
        },
    ],
}
