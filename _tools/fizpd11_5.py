# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD5 - Līdzstrāva (32.-49. stunda)."""

PD = {
    "nr": 5,
    "klase": "11. klase",
    "nosaukums": "Līdzstrāva",
    "mape": "10. Līdzstrāva",
    "fails": "PD5. Līdzstrāva_tt",
    "stundas": "32.-49.",
    "datums": "22.01.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda elektriskās ķēdes lasīšanu, Oma likumu, "
                "vadītāja pretestību, virknes un paralēlo slēgumu, jaudu un "
                "elektroenerģijas patēriņu, pilnas ķēdes Oma likumu un "
                "elektrodrošību.",
    "atgadne": [
        "I = U/R   ·   R = ρl/S   ·   P = UI = I²R = U²/R   ·   E = Pt",
        "Virknē:  I = const;  U = U₁ + U₂;  R = R₁ + R₂",
        "Paralēli:  U = const;  I = I₁ + I₂;  1/R = 1/R₁ + 1/R₂",
        "Pilna ķēde:  I = ε / (R + r)   ·   1 kWh = 3,6 · 10⁶ J",
    ],
    "struktura": [
        ("1.", "Skaidro strāvu, shēmas, vadītspēju un elektrodrošību",
         "32.-49.", 10),
        ("2.", "Aizpilda elektrisko lielumu un mērvienību tabulu",
         "32.-34.", 5),
        ("3.", "Lieto Oma likumu un vadītāja pretestības formulu",
         "33.-35.", 5),
        ("4.", "Aprēķina ekvivalento pretestību jauktā slēgumā",
         "36., 44., 45.", 5),
        ("5.", "Aprēķina jaudu, patēriņu un izmaksas", "39., 46.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kas ir elektriskā strāva metāla vadītājā?",
                 ["jonu kustība", "brīvo elektronu virzīta kustība",
                  "protonu kustība", "molekulu haotiska kustība"], 1),
                ("Kā ķēdē slēdz ampērmetru?",
                 ["paralēli patērētājam", "virknē ar patērētāju",
                  "starp fāzi un zemi", "tikai pie strāvas avota"], 1),
                ("Ko rāda I(U) grafika slīpums vadītājam, kas pakļaujas "
                 "Oma likumam?",
                 ["jaudu", "pretestības apgriezto lielumu",
                  "lādiņu", "enerģiju"], 1),
                ("Kā mainās vada pretestība, tā garumu palielinot 2 reizes?",
                 ["samazinās 2 reizes", "palielinās 2 reizes",
                  "nemainās", "palielinās 4 reizes"], 1),
                ("Kāpēc mājās ierīces slēdz paralēli?",
                 ["tā ir lētāk",
                  "katrai ierīcei ir viss tīkla spriegums un tās var "
                  "ieslēgt atsevišķi",
                  "tā samazinās kopējā strāva",
                  "tā vadi mazāk silst"], 1),
                ("Kāda ir elektriskās pretestības mērvienība?",
                 ["volts", "ampērs", "oms", "vats"], 2),
                ("Kāpēc baterijas spriegums slodzē samazinās?",
                 ["baterija atdziest",
                  "daļa EDS krīt uz avota iekšējās pretestības",
                  "vadi kļūst garāki", "samazinās lādiņš"], 1),
                ("Kas ir galvenie lādiņnesēji elektrolītā?",
                 ["elektroni", "pozitīvie un negatīvie joni",
                  "protoni", "neitroni"], 1),
                ("Kāds ir drošinātāja uzdevums?",
                 ["palielināt spriegumu",
                  "pārtraukt ķēdi, ja strāva kļūst pārāk liela",
                  "samazināt pretestību", "uzkrāt enerģiju"], 1),
                ("Cik enerģijas džoulos atbilst 1 kWh?",
                 ["3600 J", "3,6 · 10⁵ J", "3,6 · 10⁶ J",
                  "1000 J"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Elektriskie lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Strāvas stipruma SI mērvienība  [I] = ............."
                      "........", "ampērs (A)"),
                     ("Īpatnējās pretestības mērvienība  [ρ] = ..........."
                      "..........", "Ω·mm²/m  (arī Ω·m)"),
                     ("Strāva, ja U = 12 V un R = 48 Ω  I = ............."
                      "........ A", "0,25 A"),
                     ("Jauda, ja U = 230 V un I = 0,50 A  P = ..........."
                      ".......... W", "115 W"),
                     ("Enerģija, ja P = 2,0 kW un t = 3,0 h  E = ........"
                      "............. kWh", "6,0 kWh"),
                 ]},

                {"tips": "aprekins", "virs": "Vadītāja pretestība un strāva",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Vara vada garums ir 50 m, šķērsgriezuma "
                           "laukums 0,50 mm², īpatnējā pretestība "
                           "ρ = 0,017 Ω·mm²/m. Vadam pieliek spriegumu "
                           "3,4 V. Aprēķini vada pretestību un strāvas "
                           "stiprumu!",
                 "risinajums": [
                     "Dots:  l = 50 m;  S = 0,50 mm²;  "
                     "ρ = 0,017 Ω·mm²/m;  U = 3,4 V",
                     "Jāaprēķina:  R = ?;  I = ?",
                     "Formulas:  R = ρl/S;  I = U/R",
                     "Aprēķins:  1) R = 0,017 · 50 : 0,50 = 1,7 Ω",
                     "                   2) I = 3,4 : 1,7 = 2,0 A",
                     "Atbilde:  R = 1,7 Ω;  I = 2,0 A.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīti dotie lielumi;",
                     "1 p - pareizas abas formulas;",
                     "2 p - pareizi aprēķināti R un I;",
                     "1 p - abas atbildes ar mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Jaukts rezistoru slēgums",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Rezistori R₁ = 6,0 Ω un R₂ = 3,0 Ω saslēgti "
                           "paralēli, un šai grupai virknē pievienots "
                           "R₃ = 4,0 Ω. Ķēdei pieliek spriegumu 12 V. "
                           "Aprēķini ekvivalento pretestību un kopējo "
                           "strāvu!",
                 "risinajums": [
                     "Dots:  R₁ = 6,0 Ω;  R₂ = 3,0 Ω;  R₃ = 4,0 Ω;  "
                     "U = 12 V",
                     "Jāaprēķina:  R = ?;  I = ?",
                     "Formulas:  1/R₁₂ = 1/R₁ + 1/R₂;  R = R₁₂ + R₃;  "
                     "I = U/R",
                     "Aprēķins:  1) R₁₂ = 6,0 · 3,0 : (6,0 + 3,0) = 2,0 Ω",
                     "                   2) R = 2,0 + 4,0 = 6,0 Ω",
                     "                   3) I = 12 : 6,0 = 2,0 A",
                     "Atbilde:  R = 6,0 Ω;  I = 2,0 A.",
                 ],
                 "kriteriji": [
                     "1 p - shēma sadalīta paralēlajā un virknes daļā;",
                     "1 p - pareiza paralēlā slēguma formula;",
                     "2 p - pareizi aprēķināta ekvivalentā pretestība;",
                     "1 p - pareiza strāva ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Jauda, patēriņš un izmaksas",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Elektriskā tējkanna ar jaudu 2,0 kW darbojas "
                           "6 minūtes dienā, bet ledusskapis ar vidējo "
                           "jaudu 100 W - visu diennakti. Elektroenerģijas "
                           "tarifs ir 0,20 EUR/kWh.",
                 "jaut": [
                     ("Aprēķini tējkannas patērēto enerģiju dienā kWh!", 1),
                     ("Aprēķini ledusskapja patērēto enerģiju dienā kWh!",
                      1),
                     ("Kura ierīce dienā patērē vairāk enerģijas?", 1),
                     ("Aprēķini abu ierīču kopējās izmaksas 30 dienās!", 1),
                     ("Nosauc vienu pamatotu risinājumu patēriņa "
                      "samazināšanai un paskaidro to ar formulu E = Pt!",
                      1),
                 ],
                 "atbildes": [
                     "1) E = Pt = 2,0 · 0,1 = 0,20 kWh.   (1 p)",
                     "2) E = 0,100 · 24 = 2,4 kWh.   (1 p)",
                     "3) Ledusskapis - 2,4 kWh pret 0,20 kWh, jo darbojas "
                     "daudz ilgāk.   (1 p)",
                     "4) Kopā dienā 2,6 kWh; 30 dienās 78 kWh; "
                     "78 · 0,20 = 15,60 EUR.   (1 p)",
                     "5) Piemēram, vārīt tikai vajadzīgo ūdens daudzumu vai "
                     "uzstādīt efektīvāku ledusskapi: E = Pt samazinās, "
                     "samazinot vai nu jaudu P, vai darbības laiku t.   "
                     "(1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kas ir strāvas stiprums?",
                 ["lādiņš, kas šķērso vadītāja šķērsgriezumu laika vienībā",
                  "spriegums uz pretestību", "elektronu skaits vadā",
                  "enerģija uz lādiņu"], 0),
                ("Kā ķēdē slēdz voltmetru?",
                 ["virknē ar patērētāju", "paralēli patērētājam",
                  "avota iekšpusē", "aiz drošinātāja"], 1),
                ("Vadītājam R = 20 Ω pieliek 5,0 V. Cik liela ir strāva?",
                 ["4,0 A", "0,25 A", "100 A", "0,040 A"], 1),
                ("Kā mainās vada pretestība, tā šķērsgriezuma laukumu "
                 "palielinot 2 reizes?",
                 ["palielinās 2 reizes", "samazinās 2 reizes",
                  "nemainās", "samazinās 4 reizes"], 1),
                ("Kā aprēķina kopējo pretestību virknes slēgumā?",
                 ["R = R₁ + R₂", "1/R = 1/R₁ + 1/R₂",
                  "R = R₁R₂", "R = R₁ − R₂"], 0),
                ("Kāda ir jaudas mērvienība?",
                 ["džouls", "vats", "oms", "kulons"], 1),
                ("Ko sauc par elektrodzinējspēku (EDS)?",
                 ["strāvu tukšgaitā",
                  "enerģiju, ko avots piešķir vienam lādiņa kulonam",
                  "avota iekšējo pretestību", "sprieguma kritumu vados"], 1),
                ("Kas nodrošina vadītspēju pusvadītājā?",
                 ["tikai elektroni", "elektroni un caurumi",
                  "tikai joni", "protoni"], 1),
                ("Kāpēc mājas elektroierīcēm vajadzīgs zemējums?",
                 ["lai samazinātu patēriņu",
                  "lai bojājuma gadījumā strāva aizplūstu zemē, nevis caur "
                  "cilvēku",
                  "lai palielinātu spriegumu", "lai ierīce ātrāk uzsiltu"],
                 1),
                ("Kāpēc īsslēgumā strāva ir bīstami liela?",
                 ["palielinās spriegums", "ķēdes pretestība kļūst ļoti maza",
                  "pazūd lādiņš", "samazinās jauda"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Elektriskie lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Sprieguma SI mērvienība  [U] = ..................."
                      "..", "volts (V)"),
                     ("Elektriskās enerģijas mērvienība sadzīvē  [E] = "
                      ".....................", "kilovatstunda (kWh)"),
                     ("Pretestība, ja U = 9,0 V un I = 0,30 A  "
                      "R = ..................... Ω", "30 Ω"),
                     ("Jauda, ja I = 2,0 A un R = 25 Ω  P = ............"
                      "......... W", "100 W"),
                     ("2,5 kWh džoulos  E = ..................... J",
                      "9,0 · 10⁶ J"),
                 ]},

                {"tips": "aprekins", "virs": "Vadītāja pretestība un strāva",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Nihroma spirāles garums ir 4,0 m, "
                           "šķērsgriezuma laukums 0,10 mm², īpatnējā "
                           "pretestība ρ = 1,1 Ω·mm²/m. Spirālei pieliek "
                           "spriegumu 220 V. Aprēķini pretestību un "
                           "strāvas stiprumu!",
                 "risinajums": [
                     "Dots:  l = 4,0 m;  S = 0,10 mm²;  "
                     "ρ = 1,1 Ω·mm²/m;  U = 220 V",
                     "Jāaprēķina:  R = ?;  I = ?",
                     "Formulas:  R = ρl/S;  I = U/R",
                     "Aprēķins:  1) R = 1,1 · 4,0 : 0,10 = 44 Ω",
                     "                   2) I = 220 : 44 = 5,0 A",
                     "Atbilde:  R = 44 Ω;  I = 5,0 A.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīti dotie lielumi;",
                     "1 p - pareizas abas formulas;",
                     "2 p - pareizi aprēķināti R un I;",
                     "1 p - abas atbildes ar mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Jaukts rezistoru slēgums",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Rezistori R₁ = 4,0 Ω un R₂ = 4,0 Ω saslēgti "
                           "paralēli, un šai grupai virknē pievienots "
                           "R₃ = 8,0 Ω. Kopējā strāva ir 1,5 A. Aprēķini "
                           "ekvivalento pretestību un avota spriegumu!",
                 "risinajums": [
                     "Dots:  R₁ = R₂ = 4,0 Ω;  R₃ = 8,0 Ω;  I = 1,5 A",
                     "Jāaprēķina:  R = ?;  U = ?",
                     "Formulas:  R₁₂ = R₁R₂/(R₁ + R₂);  R = R₁₂ + R₃;  "
                     "U = IR",
                     "Aprēķins:  1) R₁₂ = 4,0 · 4,0 : 8,0 = 2,0 Ω",
                     "                   2) R = 2,0 + 8,0 = 10 Ω",
                     "                   3) U = 1,5 · 10 = 15 V",
                     "Atbilde:  R = 10 Ω;  U = 15 V.",
                 ],
                 "kriteriji": [
                     "1 p - shēma sadalīta paralēlajā un virknes daļā;",
                     "1 p - pareiza paralēlā slēguma formula;",
                     "2 p - pareizi aprēķināta ekvivalentā pretestība;",
                     "1 p - pareizs spriegums ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Reāls avots un drošība",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Baterijas EDS ir ε = 4,5 V, iekšējā pretestība "
                           "r = 0,50 Ω. Tai pieslēdz rezistoru R = 4,0 Ω.",
                 "jaut": [
                     ("Aprēķini strāvu ķēdē!", 1),
                     ("Aprēķini spriegumu uz rezistora!", 1),
                     ("Paskaidro, kāpēc šis spriegums ir mazāks par EDS!",
                      1),
                     ("Aprēķini bateriju atdoto lietderīgo jaudu!", 1),
                     ("Paskaidro, kāpēc bateriju nedrīkst saslēgt īssavienojumā!",
                      1),
                 ],
                 "atbildes": [
                     "1) I = ε/(R + r) = 4,5 : 4,5 = 1,0 A.   (1 p)",
                     "2) U = IR = 1,0 · 4,0 = 4,0 V.   (1 p)",
                     "3) Uz iekšējās pretestības krīt Ir = 0,50 V, tāpēc "
                     "ārējā spriegumā paliek 4,0 V.   (1 p)",
                     "4) P = UI = 4,0 · 1,0 = 4,0 W.   (1 p)",
                     "5) Tad R ≈ 0 un I = ε/r = 9 A; visa jauda izdalās "
                     "baterijā, tā pārkarst un var izplūst vai "
                     "uzsprāgt.   (1 p)",
                 ]},
            ],
        },
    ],
}
