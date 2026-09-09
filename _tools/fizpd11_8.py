# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD8 - Apgaismojums un attēli (74.-83. stunda)."""

PD = {
    "nr": 8,
    "klase": "11. klase",
    "nosaukums": "Apgaismojums un attēli",
    "mape": "13. Apgaismojums un attēli",
    "fails": "PD8. Apgaismojums un attēli_tt",
    "stundas": "74.-83.",
    "datums": "21.04.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda gaismas avotus un apgaismojumu, krāsu "
                "rašanos, atstarošanās un laušanas likumus, pilnīgo iekšējo "
                "atstarošanos, lēcas un attēla konstruēšanu, kā arī acs un "
                "fotoaparāta darbību.",
    "atgadne": [
        "Atstarošanās:  α = β   ·   Laušana:  n = sin α / sin β",
        "n = c/v   ·   Pilnīga iekšējā atstarošanās, ja α > α(rob), "
        "sin α(rob) = 1/n",
        "Lēcas formula:  1/f = 1/d + 1/f′  (d - attālums līdz priekšmetam, "
        "f′ - līdz attēlam)",
        "Palielinājums:  Γ = h′/h = f′/d   ·   Optiskais stiprums:  "
        "D = 1/f,  [D] = dioptrija",
    ],
    "struktura": [
        ("1.", "Skaidro apgaismojumu, krāsas, atstarošanos, laušanu un "
               "redzi", "74.-83.", 10),
        ("2.", "Aizpilda optikas lielumu un mērvienību tabulu",
         "74.-80.", 5),
        ("3.", "Lieto laušanas likumu un aprēķina laušanas koeficientu",
         "77.", 5),
        ("4.", "Lieto lēcas formulu un aprēķina palielinājumu",
         "79., 82.", 5),
        ("5.", "Analizē staru gaitu, redzi un briļļu izvēli",
         "78., 80., 83.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kurš no uzskaitītajiem ir gaismas avots?",
                 ["Mēness", "svece", "spogulis", "balta siena"], 1),
                ("Kā mainās apgaismojums, attālumu no punktveida avota "
                 "palielinot 2 reizes?",
                 ["samazinās 2 reizes", "samazinās 4 reizes",
                  "palielinās 2 reizes", "nemainās"], 1),
                ("Kāpēc sarkans priekšmets zaļā gaismā izskatās melns?",
                 ["tas izstaro melnu gaismu",
                  "tas absorbē zaļo gaismu un sarkano atstarot nevar, jo "
                  "tās nav",
                  "tas kļūst caurspīdīgs", "acs nespēj to redzēt"], 1),
                ("Kā formulē atstarošanās likumu?",
                 ["krišanas leņķis ir lielāks par atstarošanās leņķi",
                  "krišanas leņķis ir vienāds ar atstarošanās leņķi",
                  "krišanas leņķis ir mazāks par atstarošanās leņķi",
                  "leņķi nav saistīti"], 1),
                ("Kāds attēls rodas plakanā spogulī?",
                 ["īsts, apgriezts", "šķietams, taisns, tikpat liels",
                  "īsts, palielināts", "šķietams, samazināts"], 1),
                ("Kāpēc salmiņš ūdenī izskatās saliekts?",
                 ["ūdens to saliec",
                  "gaisma uz vidu robežas lūst",
                  "ūdens palielina", "salmiņš uzbriest"], 1),
                ("Kas notiek ar gaismas ātrumu, tai ieejot no gaisa ūdenī?",
                 ["palielinās", "samazinās", "nemainās",
                  "kļūst nulle"], 1),
                ("Kad notiek pilnīga iekšējā atstarošanās?",
                 ["ejot no optiski retākas vidē blīvākā",
                  "ejot no optiski blīvākas vides retākā, ja leņķis "
                  "pārsniedz robežleņķi",
                  "vienmēr uz stikla virsmas", "tikai vakuumā"], 1),
                ("Kāds attēls rodas savācējlēcā, ja priekšmets ir tālāk "
                 "par divkāršu fokusa attālumu?",
                 ["šķietams, palielināts",
                  "īsts, apgriezts, samazināts",
                  "īsts, taisns, palielināts", "attēls nerodas"], 1),
                ("Kādas brilles nēsā tuvredzīgs cilvēks?",
                 ["ar savācējlēcām", "ar izkliedētājlēcām",
                  "ar plakaniem stikliem", "ar krāsainiem filtriem"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Optikas lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Optiskā stipruma SI mērvienība  [D] = ............"
                      ".........", "dioptrija (dpt), 1/m"),
                     ("Apgaismojuma mērvienība  [E] = ..................."
                      "..", "lukss (lx)"),
                     ("Optiskais stiprums, ja f = 0,25 m  D = ..........."
                      ".......... dpt", "4,0 dpt"),
                     ("Gaismas ātrums ūdenī, ja n = 1,33  v = ..........."
                      ".......... m/s", "≈ 2,26 · 10⁸ m/s"),
                     ("Palielinājums, ja h = 2,0 cm un h′ = 6,0 cm  "
                      "Γ = .....................", "3,0"),
                 ]},

                {"tips": "aprekins", "virs": "Gaismas laušana", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Gaismas stars krīt no gaisa uz stikla virsmu "
                           "leņķī 45°. Laušanas leņķis stiklā ir 28°. "
                           "Aprēķini stikla laušanas koeficientu un gaismas "
                           "ātrumu stiklā! (sin 45° = 0,707;  "
                           "sin 28° = 0,469;  c = 3,0 · 10⁸ m/s)",
                 "risinajums": [
                     "Dots:  α = 45°;  β = 28°;  c = 3,0 · 10⁸ m/s",
                     "Jāaprēķina:  n = ?;  v = ?",
                     "Formulas:  n = sin α / sin β;  n = c/v  ⟹  v = c/n",
                     "Aprēķins:  1) n = 0,707 : 0,469 ≈ 1,51",
                     "                   2) v = 3,0 · 10⁸ : 1,51 ≈ "
                     "1,99 · 10⁸ m/s",
                     "Atbilde:  n ≈ 1,5;  v ≈ 2,0 · 10⁸ m/s.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīti dotie lielumi;",
                     "1 p - pareizas abas formulas;",
                     "2 p - pareizi aprēķināti n un v;",
                     "1 p - atbildes ar mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Attēls savācējlēcā",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Priekšmets, kura augstums ir 3,0 cm, novietots "
                           "30 cm attālumā no savācējlēcas ar fokusa "
                           "attālumu 10 cm. Aprēķini attālumu līdz attēlam "
                           "un attēla augstumu!",
                 "risinajums": [
                     "Dots:  h = 3,0 cm;  d = 30 cm;  f = 10 cm",
                     "Jāaprēķina:  f′ = ?;  h′ = ?",
                     "Formulas:  1/f = 1/d + 1/f′;  Γ = f′/d = h′/h",
                     "Aprēķins:  1) 1/f′ = 1/10 − 1/30 = 3/30 − 1/30 = "
                     "2/30",
                     "                   2) f′ = 15 cm",
                     "                   3) Γ = 15 : 30 = 0,50;  "
                     "h′ = 0,50 · 3,0 = 1,5 cm",
                     "Atbilde:  f′ = 15 cm;  h′ = 1,5 cm; attēls ir īsts, "
                     "apgriezts un samazināts.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīta lēcas formula;",
                     "1 p - pareizi izteikts 1/f′;",
                     "2 p - pareizi aprēķināti f′ un h′;",
                     "1 p - raksturots attēls (īsts, apgriezts, "
                     "samazināts).",
                 ]},

                {"tips": "jautajumi", "virs": "Acs, brilles un staru gaita",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Skolēns skaidri redz tikai tuvumā esošus "
                           "priekšmetus; tāli objekti izskatās izplūduši. "
                           "Ārsts izraksta brilles ar optisko stiprumu "
                           "−2,0 dpt.",
                 "jaut": [
                     ("Nosauc redzes defektu!", 1),
                     ("Paskaidro, kur šādai acij veidojas tāla priekšmeta "
                      "attēls!", 1),
                     ("Nosaki, kāda veida lēca ir briļļu stiklā, un pamato "
                      "ar zīmes vērtību!", 1),
                     ("Aprēķini šīs lēcas fokusa attālumu!", 1),
                     ("Paskaidro, kā lēca izlabo staru gaitu!", 1),
                 ],
                 "atbildes": [
                     "1) Tuvredzība (miopija).   (1 p)",
                     "2) Attēls veidojas pirms tīklenes, tāpēc uz tīklenes "
                     "krīt izplūdis attēls.   (1 p)",
                     "3) Izkliedētājlēca, jo D < 0.   (1 p)",
                     "4) f = 1/D = 1 : (−2,0) = −0,50 m = −50 cm.   (1 p)",
                     "5) Izkliedētājlēca padara starus mazāk saplūstošus, "
                     "tāpēc acs lēcas veidotais attēls pārvietojas atpakaļ "
                     "tieši uz tīkleni.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kurš no uzskaitītajiem ir apgaismots ķermenis, nevis "
                 "gaismas avots?",
                 ["Saule", "Mēness", "kvēlspuldze", "lāzers"], 1),
                ("Kāpēc darba vietā ieteicams lielāks apgaismojums?",
                 ["lai taupītu enerģiju",
                  "lai acij būtu vieglāk saskatīt sīkas detaļas un mazāk "
                  "nogurtu",
                  "lai telpa būtu siltāka", "lai krāsas izbalētu"], 1),
                ("Kāpēc balts priekšmets izskatās balts?",
                 ["tas absorbē visas krāsas",
                  "tas atstaro visas redzamās gaismas krāsas",
                  "tas izstaro balto gaismu",
                  "tas laiž gaismu cauri"], 1),
                ("Kas ir difūzā atstarošanās?",
                 ["atstarošanās no gluda spoguļa",
                  "atstarošanās no raupjas virsmas visos virzienos",
                  "gaismas laušana", "gaismas absorbcija"], 1),
                ("Cik tālu aiz spoguļa atrodas attēls, ja priekšmets ir "
                 "40 cm priekšā?",
                 ["20 cm", "40 cm", "80 cm", "attēla nav"], 1),
                ("Ko rāda vielas absolūtais laušanas koeficients?",
                 ["cik reižu gaismas ātrums vielā ir mazāks nekā vakuumā",
                  "cik daudz gaismas absorbējas",
                  "vielas blīvumu", "vielas caurspīdīgumu"], 0),
                ("Kur izmanto pilnīgo iekšējo atstarošanos?",
                 ["kvēlspuldzēs", "optiskajās šķiedrās",
                  "spoguļos", "polarizācijas filtros"], 1),
                ("Kāds ir savācējlēcas optiskā stipruma zīme?",
                 ["negatīva", "pozitīva", "nulle", "mainīga"], 1),
                ("Kāds attēls rodas savācējlēcā, ja priekšmets atrodas "
                 "starp lēcu un fokusu?",
                 ["īsts, apgriezts",
                  "šķietams, taisns, palielināts",
                  "īsts, samazināts", "attēls nerodas"], 1),
                ("Kā fotoaparāts fokusē attēlu?",
                 ["maina fotomatricas izmēru",
                  "maina attālumu starp objektīvu un matricu",
                  "maina gaismas ātrumu", "maina krāsu filtru"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Optikas lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Fokusa attāluma SI mērvienība  [f] = ............."
                      "........", "metrs (m)"),
                     ("Gaismas plūsmas mērvienība  [Φ] = ................"
                      ".....", "lūmens (lm)"),
                     ("Fokusa attālums, ja D = −2,5 dpt  f = ............"
                      "......... m", "−0,40 m"),
                     ("Laušanas koeficients, ja v = 2,0 · 10⁸ m/s  "
                      "n = .....................", "1,5"),
                     ("Robežleņķa sinuss stiklam ar n = 1,5  "
                      "sin α(rob) = .....................", "≈ 0,67"),
                 ]},

                {"tips": "aprekins", "virs": "Gaismas laušana", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Gaismas stars iziet no ūdens (n = 1,33) gaisā. "
                           "Aprēķini robežleņķa sinusu un noskaidro, vai "
                           "stars, kas krīt uz virsmu leņķī 50°, izies "
                           "gaisā!",
                 "risinajums": [
                     "Dots:  n = 1,33;  α = 50°  (sin 50° = 0,766)",
                     "Jāaprēķina:  sin α(rob) = ?;  vai stars iziet?",
                     "Formulas:  sin α(rob) = 1/n",
                     "Aprēķins:  1) sin α(rob) = 1 : 1,33 ≈ 0,752  "
                     "(α(rob) ≈ 48,8°)",
                     "                   2) sin 50° = 0,766 > 0,752, "
                     "tātad α > α(rob)",
                     "Atbilde:  sin α(rob) ≈ 0,75; stars gaisā neizies - "
                     "notiks pilnīga iekšējā atstarošanās.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīta robežleņķa formula;",
                     "1 p - pareizi aprēķināts sin α(rob);",
                     "2 p - pareizs salīdzinājums ar doto leņķi;",
                     "1 p - pamatots secinājums.",
                 ]},

                {"tips": "aprekins", "virs": "Attēls savācējlēcā",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Priekšmets, kura augstums ir 4,0 cm, novietots "
                           "15 cm attālumā no savācējlēcas ar fokusa "
                           "attālumu 10 cm. Aprēķini attālumu līdz attēlam "
                           "un attēla augstumu!",
                 "risinajums": [
                     "Dots:  h = 4,0 cm;  d = 15 cm;  f = 10 cm",
                     "Jāaprēķina:  f′ = ?;  h′ = ?",
                     "Formulas:  1/f = 1/d + 1/f′;  Γ = f′/d = h′/h",
                     "Aprēķins:  1) 1/f′ = 1/10 − 1/15 = 3/30 − 2/30 = "
                     "1/30",
                     "                   2) f′ = 30 cm",
                     "                   3) Γ = 30 : 15 = 2,0;  "
                     "h′ = 2,0 · 4,0 = 8,0 cm",
                     "Atbilde:  f′ = 30 cm;  h′ = 8,0 cm; attēls ir īsts, "
                     "apgriezts un palielināts.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīta lēcas formula;",
                     "1 p - pareizi izteikts 1/f′;",
                     "2 p - pareizi aprēķināti f′ un h′;",
                     "1 p - raksturots attēls (īsts, apgriezts, "
                     "palielināts).",
                 ]},

                {"tips": "jautajumi", "virs": "Optiskā šķiedra un redze",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Interneta signālu pārvada pa optisko šķiedru, "
                           "kuras serdes laušanas koeficients ir lielāks "
                           "nekā apvalka laušanas koeficients.",
                 "jaut": [
                     ("Paskaidro, kāda parādība notur gaismu šķiedras "
                      "iekšpusē!", 1),
                     ("Paskaidro, kāpēc serdei jābūt optiski blīvākai par "
                      "apvalku!", 1),
                     ("Nosauc vienu optiskās šķiedras priekšrocību "
                      "salīdzinājumā ar vara vadu!", 1),
                     ("Paskaidro, kāpēc pārāk stiprs šķiedras līkums "
                      "izraisa signāla zudumus!", 1),
                     ("Nosauc vienu citu pilnīgās iekšējās atstarošanās "
                      "lietojumu!", 1),
                 ],
                 "atbildes": [
                     "1) Pilnīga iekšējā atstarošanās uz serdes un apvalka "
                     "robežas.   (1 p)",
                     "2) Pilnīga iekšējā atstarošanās iespējama tikai, "
                     "gaismai ejot no optiski blīvākas vides retākā.   "
                     "(1 p)",
                     "3) Piemēram, daudz lielāks datu pārraides ātrums un "
                     "nejutība pret elektromagnētiskiem traucējumiem.   "
                     "(1 p)",
                     "4) Līkumā krišanas leņķis kļūst mazāks par "
                     "robežleņķi, tāpēc daļa gaismas iziet ārā caur "
                     "apvalku.   (1 p)",
                     "5) Piemēram, endoskops medicīnā vai taisnleņķa "
                     "prizmas binoklī.   (1 p)",
                 ]},
            ],
        },
    ],
}
