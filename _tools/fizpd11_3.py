# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD3 - Siltums un siltuma procesi (13.-24. stunda)."""

PD = {
    "nr": 3,
    "klase": "11. klase",
    "nosaukums": "Siltums un siltuma procesi",
    "mape": "8. Siltums un siltuma procesi",
    "fails": "PD3. Siltums un siltuma procesi_tt",
    "stundas": "13.-23.",
    "datums": "04.11.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda iekšējo enerģiju un siltuma pārnesi, "
                "siltuma daudzumu, agregātstāvokļa maiņu, siltuma bilanci, "
                "pirmo termodinamikas likumu un lietderības koeficientu. "
                "Šis vērtējums ir atsevišķs no Siltuma mājas projekta "
                "vērtējumiem (LD1 un PR1).",
    "atgadne": [
        "Q = cmΔT   ·   Q = λm (kušana)   ·   Q = Lm (iztvaikošana)   ·   "
        "Q = qm (degšana)",
        "c(ūdens) = 4200 J/(kg·°C)   ·   c(alumīnija) = 920 J/(kg·°C)   ·   "
        "λ(ledus) = 3,3 · 10⁵ J/kg",
        "ΔU = Q + A   ·   A(gāzes) = pΔV   ·   "
        "η = A(lietd.) / Q(patēr.) · 100 %",
        "Siltuma bilance:  Q(atdotais) = Q(saņemtais)",
    ],
    "struktura": [
        ("1.", "Skaidro siltuma pārnesi, agregātstāvokļa maiņu, iekšējo "
               "enerģiju un lietderību", "13.-23.", 10),
        ("2.", "Aizpilda siltuma lielumu un mērvienību tabulu",
         "13.-15.", 5),
        ("3.", "Aprēķina siltuma daudzumu ar agregātstāvokļa maiņu",
         "14., 15.", 5),
        ("4.", "Risina siltuma bilances uzdevumu", "16., 23.", 5),
        ("5.", "Lieto pirmo termodinamikas likumu un lietderības "
               "koeficientu", "21., 22.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Ar ko temperatūra atšķiras no iekšējās enerģijas?",
                 ["tas ir viens un tas pats",
                  "temperatūra raksturo daļiņu vidējo kinētisko enerģiju, "
                  "iekšējā enerģija - visu daļiņu enerģiju kopā",
                  "iekšējā enerģija nav atkarīga no masas",
                  "temperatūru mēra džoulos"], 1),
                ("Kurš siltuma pārneses veids notiek arī vakuumā?",
                 ["siltumvadīšana", "konvekcija", "starojums",
                  "difūzija"], 2),
                ("Kāpēc metāls šķiet aukstāks par koku vienā temperatūrā?",
                 ["metālam ir zemāka temperatūra",
                  "metālam ir lielāka siltumvadītspēja",
                  "koks ir smagāks", "metāls izstaro mazāk"], 1),
                ("Ko nozīmē c = 4200 J/(kg·°C)?",
                 ["1 kg vielas sasildīšanai par 1 °C vajag 4200 J",
                  "vielā ir 4200 J enerģijas",
                  "viela kūst 4200 °C temperatūrā",
                  "1 kg vielas izdala 4200 W"], 0),
                ("Kāpēc kušanas laikā temperatūra nemainās?",
                 ["siltums netiek pievadīts",
                  "pievadītā enerģija tiek izlietota saišu saraušanai",
                  "viela zaudē masu",
                  "siltums aizplūst apkārtējā vidē"], 1),
                ("Kāda ir siltuma daudzuma SI mērvienība?",
                 ["kalorija", "vats", "džouls", "kelvins"], 2),
                ("Kā pieraksta pirmo termodinamikas likumu?",
                 ["ΔU = Q + A", "ΔU = Q · A", "Q = ΔU · A",
                  "A = ΔU · Q"], 0),
                ("Izotermiskā procesā gāzei pievada siltumu. Kam tas tiek "
                 "izlietots?",
                 ["iekšējās enerģijas palielināšanai", "darba veikšanai",
                  "abiem vienādi", "siltuma uzkrāšanai"], 1),
                ("Kāpēc siltuma dzinēja lietderības koeficients nevar būt "
                 "100 %?",
                 ["dzinēji ir slikti izgatavoti",
                  "daļa siltuma vienmēr jāatdod dzesētājam",
                  "enerģija pazūd", "degviela ir slikta"], 1),
                ("Kurš risinājums visvairāk samazina mājas siltuma zudumus?",
                 ["biezāku aizkaru izmantošana",
                  "sienu un jumta siltināšana",
                  "gaišāka sienu krāsa", "lielāki logi"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Siltuma lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Īpatnējās siltumietilpības mērvienība  [c] = ......"
                      "...............", "J/(kg·°C)"),
                     ("Kušanas īpatnējā siltuma mērvienība  [λ] = ........"
                      ".............", "J/kg"),
                     ("Q, sildot 2,0 kg ūdens par 10 °C  Q = ............."
                      "........ J", "84 000 J = 84 kJ"),
                     ("Q, izkausējot 0,50 kg ledus (λ = 3,3 · 10⁵ J/kg)  "
                      "Q = ..................... J", "1,65 · 10⁵ J"),
                     ("Lietderības koeficients, ja A = 300 J un Q = 1200 J  "
                      "η = ..................... %", "25 %"),
                 ]},

                {"tips": "aprekins", "virs": "Ledus kušana un sildīšana",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Cik liels siltuma daudzums jāpievada 0,40 kg "
                           "ledus, kura temperatūra ir 0 °C, lai to "
                           "izkausētu un iegūto ūdeni sasildītu līdz 20 °C? "
                           "(λ = 3,3 · 10⁵ J/kg;  c = 4200 J/(kg·°C))",
                 "risinajums": [
                     "Dots:  m = 0,40 kg;  λ = 3,3 · 10⁵ J/kg;  "
                     "c = 4200 J/(kg·°C);  ΔT = 20 °C",
                     "Jāaprēķina:  Q = ?",
                     "Formulas:  Q₁ = λm;  Q₂ = cmΔT;  Q = Q₁ + Q₂",
                     "Aprēķins:  1) Q₁ = 3,3 · 10⁵ · 0,40 = 1,32 · 10⁵ J",
                     "                   2) Q₂ = 4200 · 0,40 · 20 = "
                     "3,36 · 10⁴ J",
                     "                   3) Q = 1,32 · 10⁵ + 0,336 · 10⁵ = "
                     "1,66 · 10⁵ J",
                     "Atbilde:  Q ≈ 1,7 · 10⁵ J = 170 kJ.",
                 ],
                 "kriteriji": [
                     "1 p - process sadalīts divos posmos (kušana un "
                     "sildīšana);",
                     "1 p - pierakstītas abas formulas;",
                     "2 p - pareizi aprēķināti abi siltuma daudzumi;",
                     "1 p - pareiza summa ar mērvienību.",
                 ]},

                {"tips": "aprekins", "virs": "Siltuma bilance", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Traukā ar 2,0 kg ūdens 20 °C temperatūrā ielej "
                           "1,0 kg ūdens 80 °C temperatūrā. Siltuma zudumus "
                           "neievēro. Aprēķini maisījuma temperatūru!",
                 "risinajums": [
                     "Dots:  m₁ = 2,0 kg;  t₁ = 20 °C;  m₂ = 1,0 kg;  "
                     "t₂ = 80 °C",
                     "Jāaprēķina:  t = ?",
                     "Formulas:  Q(saņ) = Q(atd);  cm₁(t − t₁) = "
                     "cm₂(t₂ − t)",
                     "Aprēķins:  1) 2,0(t − 20) = 1,0(80 − t)",
                     "                   2) 2t − 40 = 80 − t",
                     "                   3) 3t = 120;  t = 40 °C",
                     "Atbilde:  maisījuma temperatūra t = 40 °C.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīts siltuma bilances nosacījums;",
                     "1 p - pareizi pierakstīti abi siltuma daudzumi;",
                     "2 p - pareizi atrisināts vienādojums;",
                     "1 p - atbilde ar mērvienību un ticamības pārbaude "
                     "(20 °C < t < 80 °C).",
                 ]},

                {"tips": "jautajumi", "virs": "Termodinamika un lietderība",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Gāze cilindrā pie nemainīga spiediena "
                           "p = 1,0 · 10⁵ Pa izplešas no 2,0 L līdz 5,0 L. "
                           "Šajā procesā gāzei pievadīti Q = 800 J siltuma.",
                 "jaut": [
                     ("Aprēķini gāzes veikto darbu!", 1),
                     ("Aprēķini gāzes iekšējās enerģijas izmaiņu!", 1),
                     ("Nosaki, vai gāzes temperatūra pieauga vai "
                      "samazinājās, un pamato!", 1),
                     ("Cik liels ir šī procesa lietderības koeficients, ja "
                      "par lietderīgo uzskata gāzes veikto darbu?", 1),
                     ("Nosauc, kur nonāk pārējā enerģija reālā siltuma "
                      "dzinējā!", 1),
                 ],
                 "atbildes": [
                     "1) A = pΔV = 1,0 · 10⁵ · 3,0 · 10⁻³ = 300 J.   (1 p)",
                     "2) ΔU = Q − A = 800 − 300 = 500 J.   (1 p)",
                     "3) Pieauga, jo ΔU > 0 - daļiņu vidējā kinētiskā "
                     "enerģija palielinājās.   (1 p)",
                     "4) η = A / Q · 100 % = 300 : 800 · 100 % = 37,5 % ≈ "
                     "38 %.   (1 p)",
                     "5) Pārējā enerģija paliek gāzes iekšējā enerģijā un "
                     "reālā dzinējā tiek atdota dzesētājam (izplūdes gāzēm, "
                     "radiatoram) un zaudēta berzē.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kas ir ķermeņa iekšējā enerģija?",
                 ["tikai daļiņu kinētiskā enerģija",
                  "visu daļiņu kinētiskās un potenciālās enerģijas summa",
                  "ķermeņa kinētiskā enerģija",
                  "ķermeņa potenciālā enerģija gravitācijas laukā"], 1),
                ("Kurš siltuma pārneses veids notiek tikai šķidrumos un "
                 "gāzēs?",
                 ["siltumvadīšana", "konvekcija", "starojums",
                  "kondensācija"], 1),
                ("Kāpēc siltumizolācijas materiāli ir poraini?",
                 ["tie ir lēti", "gaiss porās slikti vada siltumu",
                  "tie ir viegli", "tie labi izstaro siltumu"], 1),
                ("Divas vielas ar vienādu masu sasilda par vienādu "
                 "temperatūru. Kurai vajag vairāk siltuma?",
                 ["ar mazāku īpatnējo siltumietilpību",
                  "ar lielāku īpatnējo siltumietilpību",
                  "abām vienādi", "ar lielāku blīvumu"], 1),
                ("Kas notiek ar enerģiju kondensācijas laikā?",
                 ["tā tiek uzņemta", "tā tiek atbrīvota",
                  "tā nemainās", "tā pazūd"], 1),
                ("Kāda ir īpatnējās siltumietilpības mērvienība?",
                 ["J/kg", "J/(kg·°C)", "J·kg", "W/(m·K)"], 1),
                ("Gāzei veic darbu, to saspiežot adiabātiski (Q = 0). Kas "
                 "notiek ar iekšējo enerģiju?",
                 ["samazinās", "palielinās", "nemainās",
                  "kļūst nulle"], 1),
                ("Kā aprēķina gāzes darbu izobāriskā procesā?",
                 ["A = pV", "A = pΔV", "A = ΔpV", "A = ΔpΔV"], 1),
                ("Siltuma dzinējs no sildītāja saņem 1000 J un veic 250 J "
                 "darba. Cik liels ir lietderības koeficients?",
                 ["4 %", "25 %", "40 %", "75 %"], 1),
                ("Kurš apgalvojums par siltuma pāreju ir pareizs?",
                 ["siltums pats no sevis pāriet no aukstāka uz siltāku "
                  "ķermeni",
                  "siltums pats no sevis pāriet no siltāka uz aukstāku "
                  "ķermeni",
                  "siltums nepāriet vispār",
                  "siltums pāriet tikai vakuumā"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Siltuma lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Siltuma daudzuma SI mērvienība  [Q] = .............."
                      ".......", "džouls (J)"),
                     ("Kurināmā sadegšanas siltuma mērvienība  [q] = ....."
                      "................", "J/kg"),
                     ("Q, sildot 0,50 kg alumīnija par 40 °C "
                      "(c = 920 J/(kg·°C))  Q = ..................... J",
                      "18 400 J ≈ 18 kJ"),
                     ("Q, sadedzinot 2,0 kg malkas (q = 1,3 · 10⁷ J/kg)  "
                      "Q = ..................... J", "2,6 · 10⁷ J"),
                     ("Lietderīgais darbs, ja Q = 5000 J un η = 30 %  "
                      "A = ..................... J", "1500 J"),
                 ]},

                {"tips": "aprekins", "virs": "Ūdens sildīšana un iztvaikošana",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Cik liels siltuma daudzums jāpievada 0,50 kg "
                           "ūdens, kura temperatūra ir 80 °C, lai to "
                           "uzsildītu līdz 100 °C un pēc tam pilnībā "
                           "iztvaicētu? (c = 4200 J/(kg·°C);  "
                           "L = 2,3 · 10⁶ J/kg)",
                 "risinajums": [
                     "Dots:  m = 0,50 kg;  ΔT = 20 °C;  c = 4200 J/(kg·°C);  "
                     "L = 2,3 · 10⁶ J/kg",
                     "Jāaprēķina:  Q = ?",
                     "Formulas:  Q₁ = cmΔT;  Q₂ = Lm;  Q = Q₁ + Q₂",
                     "Aprēķins:  1) Q₁ = 4200 · 0,50 · 20 = 4,2 · 10⁴ J",
                     "                   2) Q₂ = 2,3 · 10⁶ · 0,50 = "
                     "1,15 · 10⁶ J",
                     "                   3) Q = 1,15 · 10⁶ + 0,042 · 10⁶ ≈ "
                     "1,19 · 10⁶ J",
                     "Atbilde:  Q ≈ 1,2 · 10⁶ J = 1,2 MJ.",
                 ],
                 "kriteriji": [
                     "1 p - process sadalīts divos posmos;",
                     "1 p - pierakstītas abas formulas;",
                     "2 p - pareizi aprēķināti abi siltuma daudzumi;",
                     "1 p - pareiza summa ar mērvienību.",
                 ]},

                {"tips": "aprekins", "virs": "Siltuma bilance", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Traukā ar 3,0 kg ūdens 15 °C temperatūrā ielej "
                           "1,0 kg ūdens 95 °C temperatūrā. Siltuma zudumus "
                           "neievēro. Aprēķini maisījuma temperatūru!",
                 "risinajums": [
                     "Dots:  m₁ = 3,0 kg;  t₁ = 15 °C;  m₂ = 1,0 kg;  "
                     "t₂ = 95 °C",
                     "Jāaprēķina:  t = ?",
                     "Formulas:  Q(saņ) = Q(atd);  cm₁(t − t₁) = "
                     "cm₂(t₂ − t)",
                     "Aprēķins:  1) 3,0(t − 15) = 1,0(95 − t)",
                     "                   2) 3t − 45 = 95 − t",
                     "                   3) 4t = 140;  t = 35 °C",
                     "Atbilde:  maisījuma temperatūra t = 35 °C.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīts siltuma bilances nosacījums;",
                     "1 p - pareizi pierakstīti abi siltuma daudzumi;",
                     "2 p - pareizi atrisināts vienādojums;",
                     "1 p - atbilde ar mērvienību un ticamības pārbaude.",
                 ]},

                {"tips": "jautajumi", "virs": "Termodinamika un lietderība",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Gāze cilindrā pie nemainīga spiediena "
                           "p = 2,0 · 10⁵ Pa izplešas no 1,0 L līdz 4,0 L. "
                           "Gāzes iekšējā enerģija palielinājās par 900 J.",
                 "jaut": [
                     ("Aprēķini gāzes veikto darbu!", 1),
                     ("Aprēķini gāzei pievadīto siltuma daudzumu!", 1),
                     ("Pieraksti pirmo termodinamikas likumu šim procesam!",
                      1),
                     ("Cik liels ir lietderības koeficients, ja par "
                      "lietderīgo uzskata gāzes darbu?", 1),
                     ("Paskaidro, kāpēc siltuma dzinējam nepieciešams "
                      "dzesētājs!", 1),
                 ],
                 "atbildes": [
                     "1) A = pΔV = 2,0 · 10⁵ · 3,0 · 10⁻³ = 600 J.   (1 p)",
                     "2) Q = ΔU + A = 900 + 600 = 1500 J.   (1 p)",
                     "3) ΔU = Q − A jeb Q = ΔU + A.   (1 p)",
                     "4) η = 600 : 1500 · 100 % = 40 %.   (1 p)",
                     "5) Cikliskā procesā darbmaisījums jāatgriež sākuma "
                     "stāvoklī; to var izdarīt, tikai atdodot daļu siltuma "
                     "aukstākam ķermenim, tāpēc daļa enerģijas vienmēr "
                     "aizplūst uz dzesētāju.   (1 p)",
                 ]},
            ],
        },
    ],
}
