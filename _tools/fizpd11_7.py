# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD7 - Elektromagnētiskie viļņi un difrakcija."""

PD = {
    "nr": 7,
    "klase": "11. klase",
    "nosaukums": "Elektromagnētiskie viļņi un difrakcija",
    "mape": "12. Elektromagnētiskie viļņi",
    "fails": "PD7. Elektromagnētiskie viļņi un difrakcija_tt",
    "stundas": "64.-72.",
    "datums": "24.03.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda elektromagnētisko viļņu rašanos un spektru, "
                "sakarību c = λf, interferenci un difrakciju, difrakcijas "
                "režģa formulu, polarizāciju un starojuma drošu lietošanu.",
    "atgadne": [
        "c = λf,  kur c = 3,0 · 10⁸ m/s   ·   v = λf citā vidē",
        "Difrakcijas režģis:  d · sin α = kλ   ·   d = 1/N",
        "Maksimums: ceļu starpība k·λ   ·   minimums: (2k + 1)·λ/2",
        "Spektrs pēc frekvences augšanas: radioviļņi → mikroviļņi → IS → "
        "redzamā gaisma → UV → rentgena → gamma",
    ],
    "struktura": [
        ("1.", "Skaidro EM viļņus, spektru, interferenci un polarizāciju",
         "64.-72.", 10),
        ("2.", "Aizpilda viļņu lielumu un mērvienību tabulu", "64., 65.", 5),
        ("3.", "Lieto sakarību c = λf", "64.", 5),
        ("4.", "Lieto difrakcijas režģa formulu", "67., 69.", 5),
        ("5.", "Analizē spektru, drošību un mērījuma ticamību",
         "65., 70., 72.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kas ir elektromagnētiskais vilnis?",
                 ["gaisa daļiņu svārstības",
                  "mainīga elektriskā un magnētiskā lauka izplatīšanās",
                  "elektronu plūsma", "skaņas vilnis vakuumā"], 1),
                ("Cik liels ir gaismas ātrums vakuumā?",
                 ["3,0 · 10⁶ m/s", "3,0 · 10⁸ m/s",
                  "3,0 · 10¹⁰ m/s", "340 m/s"], 1),
                ("Kā mainās viļņa garums, palielinoties frekvencei?",
                 ["palielinās", "samazinās", "nemainās",
                  "kļūst nulle"], 1),
                ("Kurš starojums no uzskaitītajiem ir jonizējošs?",
                 ["radioviļņi", "mikroviļņi", "redzamā gaisma",
                  "rentgenstarojums"], 3),
                ("Kas notiek svārstību kontūrā?",
                 ["enerģija pāriet no kondensatora lauka uz spoles lauku "
                  "un atpakaļ",
                  "enerģija tikai pieaug", "lādiņš pazūd",
                  "strāva ir nemainīga"], 0),
                ("Kad interferencē rodas maksimums?",
                 ["kad ceļu starpība ir vesels viļņu garumu skaits",
                  "kad ceļu starpība ir nepāra pusviļņu skaits",
                  "kad viļņi ir dažādu frekvenču",
                  "kad amplitūdas ir dažādas"], 0),
                ("Kas ir difrakcija?",
                 ["viļņa atstarošanās",
                  "viļņa novirze no taisnvirziena izplatīšanās aiz "
                  "šķēršļa vai spraugas",
                  "viļņa laušana", "viļņa polarizācija"], 1),
                ("Kā mainās difrakcijas aina, samazinot režģa periodu d?",
                 ["maksimumi tuvojas viens otram",
                  "maksimumi attālinās viens no otra",
                  "aina nemainās", "maksimumi pazūd"], 1),
                ("Kāda parādība pierāda, ka gaisma ir šķērsvilnis?",
                 ["atstarošanās", "laušana", "polarizācija",
                  "absorbcija"], 2),
                ("Kāpēc mikroviļņu krāsnij ir metāla siets uz durvīm?",
                 ["lai varētu redzēt ēdienu",
                  "sieta atveres ir mazākas par viļņa garumu, tāpēc viļņi "
                  "netiek ārā",
                  "lai durvis būtu stiprākas",
                  "lai novadītu siltumu"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Viļņu lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Frekvences SI mērvienība  [f] = .................."
                      "...", "hercs (Hz)"),
                     ("Gaismas ātrums vakuumā  c = ..................... "
                      "m/s", "3,0 · 10⁸ m/s"),
                     ("Viļņa garums, ja f = 100 MHz  λ = ..............."
                      "...... m", "3,0 m"),
                     ("600 nm metros  λ = ..................... m",
                      "6,0 · 10⁻⁷ m"),
                     ("Režģa periods, ja N = 500 svītru uz mm  "
                      "d = ..................... m", "2,0 · 10⁻⁶ m"),
                 ]},

                {"tips": "aprekins", "virs": "Sakarība c = λf", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Radiostacija raida ar frekvenci 101,7 MHz. "
                           "Aprēķini raidītā viļņa garumu! Kurai spektra "
                           "daļai tas pieder?",
                 "risinajums": [
                     "Dots:  f = 101,7 MHz = 1,017 · 10⁸ Hz;  "
                     "c = 3,0 · 10⁸ m/s",
                     "Jāaprēķina:  λ = ?",
                     "Formulas:  c = λf  ⟹  λ = c/f",
                     "Aprēķins:  1) λ = 3,0 · 10⁸ : 1,017 · 10⁸",
                     "                   2) λ ≈ 2,95 m ≈ 3,0 m",
                     "Atbilde:  λ ≈ 3,0 m; tie ir ultraīsie radioviļņi "
                     "(FM josla).",
                 ],
                 "kriteriji": [
                     "1 p - frekvence pārveidota hercos;",
                     "1 p - pareiza formula;",
                     "2 p - pareizs aprēķins;",
                     "1 p - atbilde ar mērvienību un spektra daļas "
                     "nosaukumu.",
                 ]},

                {"tips": "aprekins", "virs": "Difrakcijas režģis",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Uz difrakcijas režģi, kuram ir 400 svītras uz "
                           "1 mm, krīt lāzera gaisma. Pirmās kārtas "
                           "maksimums novērots leņķī 15°. Aprēķini gaismas "
                           "viļņa garumu! (sin 15° = 0,259)",
                 "risinajums": [
                     "Dots:  N = 400 mm⁻¹;  k = 1;  α = 15°;  "
                     "sin α = 0,259",
                     "Jāaprēķina:  λ = ?",
                     "Formulas:  d = 1/N;  d · sin α = kλ  ⟹  "
                     "λ = d sin α / k",
                     "Aprēķins:  1) d = 1 : (400 · 10³ m⁻¹) = "
                     "2,5 · 10⁻⁶ m",
                     "                   2) λ = 2,5 · 10⁻⁶ · 0,259 : 1",
                     "                   3) λ ≈ 6,5 · 10⁻⁷ m",
                     "Atbilde:  λ ≈ 6,5 · 10⁻⁷ m = 650 nm (sarkana "
                     "gaisma).",
                 ],
                 "kriteriji": [
                     "1 p - aprēķināts režģa periods d;",
                     "1 p - pareiza režģa formula;",
                     "2 p - pareizs aprēķins;",
                     "1 p - atbilde ar mērvienību un krāsas novērtējums.",
                 ]},

                {"tips": "jautajumi", "virs": "Spektrs un drošība",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Skolēns lasa reklāmu: «Mūsu telefona apvalks "
                           "pilnībā aizsargā no kaitīgā mobilo sakaru "
                           "starojuma.»",
                 "jaut": [
                     ("Nosaki, kurai spektra daļai pieder mobilo sakaru "
                      "starojums!", 1),
                     ("Paskaidro, vai šis starojums ir jonizējošs, un "
                      "pamato!", 1),
                     ("Nosauc divus jonizējoša starojuma veidus!", 1),
                     ("Paskaidro, kāpēc apgalvojums par «pilnīgu "
                      "aizsardzību» ir apšaubāms!", 1),
                     ("Nosauc, kāda informācija būtu vajadzīga, lai "
                      "apgalvojumu pārbaudītu!", 1),
                 ],
                 "atbildes": [
                     "1) Mikroviļņi (radioviļņu diapazons, apmēram "
                     "0,8-2,6 GHz).   (1 p)",
                     "2) Nav jonizējošs - fotona enerģija ir daudz mazāka "
                     "par enerģiju, kas vajadzīga elektrona atraušanai no "
                     "atoma.   (1 p)",
                     "3) Rentgenstarojums un gamma starojums (arī īsviļņu "
                     "UV).   (1 p)",
                     "4) Ja apvalks tiešām aizturētu šos viļņus, telefons "
                     "zaudētu sakarus; turklāt «kaitīgums» nav pierādīts "
                     "šajā jaudas diapazonā.   (1 p)",
                     "5) Neatkarīgi mērījumi par signāla jaudas blīvumu ar "
                     "apvalku un bez tā, kā arī atsauce uz recenzētu "
                     "pētījumu vai standartu.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kas rada elektromagnētisko vilni?",
                 ["nemainīgs lādiņš", "paātrināti kustīgs lādiņš",
                  "vienmērīga strāva vadā", "magnēts miera stāvoklī"], 1),
                ("Kurš no uzskaitītajiem viļņiem izplatās arī vakuumā?",
                 ["skaņa", "gaisma", "ūdens virsmas vilnis",
                  "seismiskais vilnis"], 1),
                ("Kāda ir viļņa garuma mērvienība?",
                 ["hercs", "metrs", "sekunde", "vats"], 1),
                ("Kurš starojums ir ar viszemāko frekvenci?",
                 ["gamma", "rentgena", "radioviļņi",
                  "ultravioletais"], 2),
                ("Ko sauc par superpozīciju?",
                 ["viļņu atstarošanos",
                  "vairāku viļņu vienlaicīgu saskaitīšanos vienā punktā",
                  "viļņa laušanu", "viļņa slāpēšanu"], 1),
                ("Kad interferencē rodas minimums?",
                 ["kad ceļu starpība ir vesels viļņu garumu skaits",
                  "kad ceļu starpība ir nepāra pusviļņu garumu skaits",
                  "kad amplitūdas ir vienādas",
                  "kad frekvences atšķiras"], 1),
                ("Kāpēc balta gaisma aiz režģa sadalās krāsās?",
                 ["visas krāsas novirzās vienādi",
                  "dažādiem viļņu garumiem atbilst dažādi novirzes leņķi",
                  "režģis izstaro krāsas",
                  "gaisma tiek absorbēta"], 1),
                ("Kā mainās difrakcijas maksimuma leņķis, palielinot viļņa "
                 "garumu?",
                 ["samazinās", "palielinās", "nemainās",
                  "kļūst nulle"], 1),
                ("Kam izmanto polarizācijas filtrus fotogrāfijā?",
                 ["lai palielinātu spilgtumu",
                  "lai samazinātu atspīdumus no stikla un ūdens",
                  "lai mainītu fokusa attālumu",
                  "lai palielinātu ekspozīcijas laiku"], 1),
                ("Kāpēc ar rentgenstariem drīkst strādāt tikai ar "
                 "aizsardzību?",
                 ["tie ir ļoti spilgti",
                  "tie ir jonizējoši un var bojāt šūnas",
                  "tie ir karsti", "tie ir dārgi"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Viļņu lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Viļņa garuma SI mērvienība  [λ] = ................"
                      ".....", "metrs (m)"),
                     ("Sakarība starp c, λ un f  ...................."
                      ".", "c = λf"),
                     ("Frekvence, ja λ = 0,50 m  f = ..................."
                      ".. Hz", "6,0 · 10⁸ Hz"),
                     ("450 nm metros  λ = ..................... m",
                      "4,5 · 10⁻⁷ m"),
                     ("Režģa periods, ja N = 200 svītru uz mm  "
                      "d = ..................... m", "5,0 · 10⁻⁶ m"),
                 ]},

                {"tips": "aprekins", "virs": "Sakarība c = λf", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Wi-Fi maršrutētājs strādā ar viļņa garumu "
                           "12,5 cm. Aprēķini signāla frekvenci! Kurai "
                           "spektra daļai tas pieder?",
                 "risinajums": [
                     "Dots:  λ = 12,5 cm = 0,125 m;  c = 3,0 · 10⁸ m/s",
                     "Jāaprēķina:  f = ?",
                     "Formulas:  c = λf  ⟹  f = c/λ",
                     "Aprēķins:  1) f = 3,0 · 10⁸ : 0,125",
                     "                   2) f = 2,4 · 10⁹ Hz = 2,4 GHz",
                     "Atbilde:  f = 2,4 GHz; tie ir mikroviļņi.",
                 ],
                 "kriteriji": [
                     "1 p - viļņa garums pārveidots metros;",
                     "1 p - pareiza formula;",
                     "2 p - pareizs aprēķins;",
                     "1 p - atbilde ar mērvienību un spektra daļas "
                     "nosaukumu.",
                 ]},

                {"tips": "aprekins", "virs": "Difrakcijas režģis",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Uz difrakcijas režģi ar periodu "
                           "d = 2,0 · 10⁻⁶ m krīt lāzera gaisma ar viļņa "
                           "garumu 500 nm. Aprēķini pirmās kārtas "
                           "maksimuma novirzes leņķa sinusu un pārbaudi, "
                           "vai iespējams novērot ceturtās kārtas "
                           "maksimumu!",
                 "risinajums": [
                     "Dots:  d = 2,0 · 10⁻⁶ m;  λ = 500 nm = "
                     "5,0 · 10⁻⁷ m;  k = 1",
                     "Jāaprēķina:  sin α₁ = ?;  vai eksistē k = 4?",
                     "Formulas:  d · sin α = kλ  ⟹  sin α = kλ/d",
                     "Aprēķins:  1) sin α₁ = 5,0 · 10⁻⁷ : 2,0 · 10⁻⁶ = "
                     "0,25  (α₁ ≈ 14,5°)",
                     "                   2) k = 4:  sin α₄ = 4 · 0,25 = "
                     "1,00",
                     "                   3) sin α ≤ 1, tāpēc k = 4 ir "
                     "robežgadījums (α = 90°) un praktiski nav novērojams",
                     "Atbilde:  sin α₁ = 0,25; ceturtās kārtas maksimums "
                     "praktiski nav novērojams, jo iznāktu α = 90°.",
                 ],
                 "kriteriji": [
                     "1 p - viļņa garums pārveidots metros;",
                     "1 p - pareiza režģa formula;",
                     "2 p - pareizi aprēķināti abi sinusi;",
                     "1 p - pamatots secinājums par sin α ≤ 1.",
                 ]},

                {"tips": "jautajumi", "virs": "Mērījuma ticamība",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Laboratorijas darbā ar difrakcijas režģi "
                           "skolēns ieguva sarkana lāzera viļņa garumu "
                           "λ = 8,2 · 10⁻⁷ m, lai gan uz lāzera rakstīts "
                           "650 nm.",
                 "jaut": [
                     ("Aprēķini relatīvo novirzi procentos!", 1),
                     ("Nosauc vienu iespējamu mērījuma kļūdas cēloni!", 1),
                     ("Paskaidro, kā mērījumu var padarīt precīzāku!", 1),
                     ("Paskaidro, kāpēc lielāks attālums līdz ekrānam "
                      "samazina relatīvo kļūdu!", 1),
                     ("Nosauc vienu drošības noteikumu darbam ar lāzeru!",
                      1),
                 ],
                 "atbildes": [
                     "1) Novirze = (820 − 650) : 650 · 100 % ≈ 26 %.   "
                     "(1 p)",
                     "2) Piemēram, neprecīzi izmērīts attālums no režģa "
                     "līdz ekrānam vai sajaukta maksimuma kārta.   (1 p)",
                     "3) Mērīt attālumu starp simetriskiem maksimumiem "
                     "abās pusēs un dalīt uz pusēm; atkārtot mērījumu "
                     "vairākas reizes un rēķināt vidējo.   (1 p)",
                     "4) Absolūtā lineāla kļūda paliek tā pati (daži mm), "
                     "bet mērāmais attālums kļūst lielāks, tāpēc "
                     "attiecība kļūda/lielums samazinās.   (1 p)",
                     "5) Nekad neskatīties lāzera starā un nevērst to uz "
                     "citiem; strādāt tā, lai stars neatstarotos no "
                     "spīdīgām virsmām.   (1 p)",
                 ]},
            ],
        },
    ],
}
