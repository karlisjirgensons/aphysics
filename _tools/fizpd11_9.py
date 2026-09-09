# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. PD9 - Atoms un Visums (85.-95. stunda)."""

PD = {
    "nr": 9,
    "klase": "11. klase",
    "nosaukums": "Atoms un Visums",
    "mape": "14. Visums un atoms",
    "fails": "PD9. Atoms un Visums_tt",
    "stundas": "85.-95.",
    "datums": "19.05.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Noslēguma darbs pārbauda atoma modeļus un fotona enerģiju, "
                "spektrus, kodola uzbūvi un izotopus, radioaktivitāti un "
                "pussabrukšanu, kodolu dalīšanos un sintēzi, starojuma "
                "drošību, kā arī Saules sistēmas un zvaigžņu pamatjēdzienus.",
    "atgadne": [
        "E = hf = hc/λ,  kur h = 6,63 · 10⁻³⁴ J·s   ·   1 eV = "
        "1,6 · 10⁻¹⁹ J",
        "Izotopa apzīmējums:  ᴬ𝗓X;  A = Z + N   ·   α-sabrukšana: A−4, Z−2;  "
        "β⁻-sabrukšana: A, Z+1",
        "Pussabrukšana:  N = N₀ / 2ⁿ,  kur n = t/T",
        "Aizsardzība no starojuma: laiks, attālums, ekranēšana",
    ],
    "struktura": [
        ("1.", "Skaidro atoma modeļus, spektrus, radioaktivitāti un "
               "Visuma uzbūvi", "85.-95.", 10),
        ("2.", "Aizpilda atomfizikas lielumu un mērvienību tabulu",
         "85.-88.", 5),
        ("3.", "Aprēķina fotona enerģiju", "86.", 5),
        ("4.", "Risina pussabrukšanas uzdevumu", "88.", 5),
        ("5.", "Analizē kodolreakciju, starojuma drošību un astronomijas "
               "datus", "87.-95.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kas atrodas atoma kodolā?",
                 ["protoni un elektroni", "protoni un neitroni",
                  "tikai neitroni", "tikai elektroni"], 1),
                ("Ko nosaka kārtas skaitlis Z?",
                 ["neitronu skaitu", "protonu skaitu",
                  "nukleonu skaitu", "elektronu masu"], 1),
                ("Ar ko atšķiras viena elementa izotopi?",
                 ["protonu skaitu", "neitronu skaitu",
                  "elektronu lādiņu", "ķīmiskajām īpašībām"], 1),
                ("Kāda ir fotona enerģijas formula?",
                 ["E = mc²", "E = hf", "E = mgh", "E = ½mv²"], 1),
                ("Kāpēc atoms izstaro līniju spektru?",
                 ["kodols ir nestabils",
                  "elektrons pāriet starp diskrētiem enerģijas līmeņiem",
                  "atoms uzsilst", "gaisma tiek absorbēta"], 1),
                ("Kurš starojuma veids ir vissmagāk aizturams?",
                 ["alfa", "beta", "gamma", "visi vienādi"], 2),
                ("Ko nozīmē pussabrukšanas periods?",
                 ["laiks, kad sabrūk visi kodoli",
                  "laiks, kurā sabrūk puse no kodoliem",
                  "kodola izmērs", "starojuma enerģija"], 1),
                ("Kas notiek kodolu sintēzē?",
                 ["smags kodols sadalās",
                  "divi viegli kodoli apvienojas smagākā",
                  "elektrons atdalās", "atoms jonizējas"], 1),
                ("Kā samazina saņemto starojuma devu?",
                 ["palielina laiku pie avota",
                  "samazina attālumu",
                  "palielina attālumu un izmanto ekranējumu",
                  "noņem aizsargtērpu"], 2),
                ("Kas ir gaismas gads?",
                 ["laiks, kādā gaisma veic apli ap Zemi",
                  "attālums, ko gaisma veic vienā gadā",
                  "zvaigznes vecums", "gaismas ātrums"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Atomfizikas lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Planka konstante  h = ..................... J·s",
                      "6,63 · 10⁻³⁴ J·s"),
                     ("Enerģijas mērvienība atomfizikā  ................"
                      ".....", "elektronvolts (eV)"),
                     ("1 eV džoulos  E = ..................... J",
                      "1,6 · 10⁻¹⁹ J"),
                     ("Neitronu skaits kodolā ²³⁵U (Z = 92)  "
                      "N = .....................", "143"),
                     ("Aktivitātes SI mērvienība  [A] = ................"
                      ".....", "bekerels (Bq)"),
                 ]},

                {"tips": "aprekins", "virs": "Fotona enerģija", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Aprēķini zaļas gaismas fotona enerģiju "
                           "džoulos un elektronvoltos, ja viļņa garums ir "
                           "500 nm! (h = 6,63 · 10⁻³⁴ J·s;  "
                           "c = 3,0 · 10⁸ m/s;  1 eV = 1,6 · 10⁻¹⁹ J)",
                 "risinajums": [
                     "Dots:  λ = 500 nm = 5,0 · 10⁻⁷ m;  "
                     "h = 6,63 · 10⁻³⁴ J·s;  c = 3,0 · 10⁸ m/s",
                     "Jāaprēķina:  E = ?",
                     "Formulas:  E = hf;  f = c/λ  ⟹  E = hc/λ",
                     "Aprēķins:  1) hc = 6,63 · 10⁻³⁴ · 3,0 · 10⁸ = "
                     "1,989 · 10⁻²⁵ J·m",
                     "                   2) E = 1,989 · 10⁻²⁵ : "
                     "5,0 · 10⁻⁷ ≈ 3,98 · 10⁻¹⁹ J",
                     "                   3) E = 3,98 · 10⁻¹⁹ : "
                     "1,6 · 10⁻¹⁹ ≈ 2,5 eV",
                     "Atbilde:  E ≈ 4,0 · 10⁻¹⁹ J ≈ 2,5 eV.",
                 ],
                 "kriteriji": [
                     "1 p - viļņa garums pārveidots metros;",
                     "1 p - pareiza formula E = hc/λ;",
                     "2 p - pareizs aprēķins džoulos;",
                     "1 p - pareiza pāreja uz elektronvoltiem.",
                 ]},

                {"tips": "aprekins", "virs": "Pussabrukšana", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Radioaktīva parauga sākotnējā aktivitāte ir "
                           "800 Bq, un izotopa pussabrukšanas periods ir "
                           "8,0 dienas. Aprēķini parauga aktivitāti pēc "
                           "24 dienām un nosaki, pēc cik dienām aktivitāte "
                           "būs 50 Bq!",
                 "risinajums": [
                     "Dots:  A₀ = 800 Bq;  T = 8,0 d;  t = 24 d",
                     "Jāaprēķina:  A = ?;  t₁ (kad A = 50 Bq) = ?",
                     "Formulas:  n = t/T;  A = A₀ / 2ⁿ",
                     "Aprēķins:  1) n = 24 : 8,0 = 3",
                     "                   2) A = 800 : 2³ = 800 : 8 = "
                     "100 Bq",
                     "                   3) 50 = 800 : 2ⁿ ⟹ 2ⁿ = 16 ⟹ "
                     "n = 4;  t₁ = 4 · 8,0 = 32 dienas",
                     "Atbilde:  A = 100 Bq;  50 Bq būs pēc 32 dienām.",
                 ],
                 "kriteriji": [
                     "1 p - aprēķināts periodu skaits n;",
                     "1 p - pareiza formula A = A₀/2ⁿ;",
                     "2 p - pareizi aprēķināta aktivitāte;",
                     "1 p - pareizi noteikts laiks līdz 50 Bq.",
                 ]},

                {"tips": "jautajumi", "virs": "Kodolreakcijas un Visums",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Saules kodolā notiek ūdeņraža kodolu sintēze, "
                           "bet kodolelektrostacijā - urāna kodolu "
                           "dalīšanās.",
                 "jaut": [
                     ("Paskaidro, ar ko sintēze atšķiras no dalīšanās!",
                      1),
                     ("Nosauc, no kurienes abos procesos rodas enerģija!",
                      1),
                     ("Nosauc vienu kodolenerģijas priekšrocību un vienu "
                      "risku!", 1),
                     ("Paskaidro, kāpēc Saules starojums sasniedz Zemi "
                      "apmēram 8 minūtēs!", 1),
                     ("Paskaidro, kā pēc zvaigznes spektra var noteikt tās "
                      "sastāvu!", 1),
                 ],
                 "atbildes": [
                     "1) Sintēzē divi viegli kodoli apvienojas smagākā, "
                     "dalīšanās smags kodols sašķeļas divos vieglākos.   "
                     "(1 p)",
                     "2) Abos procesos daļa masas pārvēršas enerģijā "
                     "(E = mc²) - kodolu saites enerģija kļūst "
                     "izdevīgāka.   (1 p)",
                     "3) Priekšrocība - liels enerģijas daudzums bez CO₂ "
                     "izmešiem; risks - radioaktīvie atkritumi un "
                     "avārijas sekas.   (1 p)",
                     "4) Attālums ≈ 1,5 · 10¹¹ m, un t = s/c = "
                     "1,5 · 10¹¹ : 3,0 · 10⁸ = 500 s ≈ 8,3 min.   (1 p)",
                     "5) Katram elementam ir savas spektra līnijas; pēc "
                     "absorbcijas līniju izvietojuma nosaka, kādi elementi "
                     "ir zvaigznes atmosfērā.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kāda ir atoma galvenā masas daļa?",
                 ["elektronu apvalks", "kodols",
                  "tukšums starp daļiņām", "elektriskais lauks"], 1),
                ("Ko nosaka masas skaitlis A?",
                 ["protonu skaitu", "nukleonu (protonu un neitronu) skaitu",
                  "elektronu skaitu", "izotopu skaitu"], 1),
                ("Kāds spektrs rodas, gaismai izejot cauri aukstai gāzei?",
                 ["nepārtraukts", "absorbcijas līniju",
                  "izstarošanas nepārtraukts", "spektra nerodas"], 1),
                ("Kā mainās fotona enerģija, palielinoties viļņa garumam?",
                 ["palielinās", "samazinās", "nemainās",
                  "kļūst negatīva"], 1),
                ("Kas ir alfa daļiņa?",
                 ["elektrons", "hēlija kodols", "fotons",
                  "neitrons"], 1),
                ("Kā mainās masas skaitlis alfa sabrukšanā?",
                 ["nemainās", "samazinās par 4", "palielinās par 2",
                  "samazinās par 2"], 1),
                ("Pēc diviem pussabrukšanas periodiem paliek:",
                 ["puse kodolu", "ceturtā daļa kodolu",
                  "astotā daļa kodolu", "neviens kodols"], 1),
                ("Ar ko apstarošana atšķiras no radioaktīva "
                 "piesārņojuma?",
                 ["ar to nekas neatšķiras",
                  "apstarošanā cilvēks saņem starojumu, piesārņojumā uz "
                  "cilvēka nonāk radioaktīva viela",
                  "apstarošana ir bīstamāka vienmēr",
                  "piesārņojums nav bīstams"], 1),
                ("Kas notiek ar zvaigzni, kad tās kodolā beidzas "
                 "ūdeņradis?",
                 ["tā nodziest uzreiz", "tā izplešas par sarkano gigantu",
                  "tā kļūst par planētu", "tā sadalās"], 1),
                ("Kāds novērojums liecina, ka Visums izplešas?",
                 ["zvaigžņu mirgošana",
                  "attālo galaktiku spektru sarkanā nobīde",
                  "Mēness fāzes", "Saules plankumi"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide",
                 "virs": "Atomfizikas lielumi un mērvienības",
                 "punkti": 5,
                 "note": "Ieraksti trūkstošo vērtību vai mērvienību! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Fotona enerģijas formula  E = .................."
                      "...", "E = hf jeb E = hc/λ"),
                     ("Absorbētās devas mērvienība  [D] = .............."
                      ".......", "grejs (Gy)"),
                     ("2,0 eV džoulos  E = ..................... J",
                      "3,2 · 10⁻¹⁹ J"),
                     ("Protonu skaits kodolā ¹⁴C (Z = 6)  "
                      "Z = .....................", "6"),
                     ("Ekvivalentās devas mērvienība  [H] = ............"
                      ".........", "zīverts (Sv)"),
                 ]},

                {"tips": "aprekins", "virs": "Fotona enerģija", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Ultravioletā starojuma frekvence ir "
                           "1,2 · 10¹⁵ Hz. Aprēķini fotona enerģiju "
                           "džoulos un elektronvoltos! "
                           "(h = 6,63 · 10⁻³⁴ J·s;  "
                           "1 eV = 1,6 · 10⁻¹⁹ J)",
                 "risinajums": [
                     "Dots:  f = 1,2 · 10¹⁵ Hz;  h = 6,63 · 10⁻³⁴ J·s",
                     "Jāaprēķina:  E = ?",
                     "Formulas:  E = hf",
                     "Aprēķins:  1) E = 6,63 · 10⁻³⁴ · 1,2 · 10¹⁵",
                     "                   2) E ≈ 7,96 · 10⁻¹⁹ J",
                     "                   3) E = 7,96 · 10⁻¹⁹ : "
                     "1,6 · 10⁻¹⁹ ≈ 5,0 eV",
                     "Atbilde:  E ≈ 8,0 · 10⁻¹⁹ J ≈ 5,0 eV.",
                 ],
                 "kriteriji": [
                     "1 p - pierakstīti dotie lielumi;",
                     "1 p - pareiza formula E = hf;",
                     "2 p - pareizs aprēķins džoulos;",
                     "1 p - pareiza pāreja uz elektronvoltiem.",
                 ]},

                {"tips": "aprekins", "virs": "Pussabrukšana", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Paraugā sākumā ir 6,4 · 10²⁰ radioaktīvi "
                           "kodoli; pussabrukšanas periods ir 5,0 gadi. "
                           "Aprēķini nesabrukušo kodolu skaitu pēc "
                           "20 gadiem un sabrukušo kodolu skaitu!",
                 "risinajums": [
                     "Dots:  N₀ = 6,4 · 10²⁰;  T = 5,0 gadi;  t = 20 gadi",
                     "Jāaprēķina:  N = ?;  ΔN = ?",
                     "Formulas:  n = t/T;  N = N₀ / 2ⁿ;  ΔN = N₀ − N",
                     "Aprēķins:  1) n = 20 : 5,0 = 4",
                     "                   2) N = 6,4 · 10²⁰ : 2⁴ = "
                     "6,4 · 10²⁰ : 16 = 4,0 · 10¹⁹",
                     "                   3) ΔN = 6,4 · 10²⁰ − "
                     "0,40 · 10²⁰ = 6,0 · 10²⁰",
                     "Atbilde:  N = 4,0 · 10¹⁹ kodoli;  sabrukuši "
                     "6,0 · 10²⁰ kodoli.",
                 ],
                 "kriteriji": [
                     "1 p - aprēķināts periodu skaits n;",
                     "1 p - pareiza formula N = N₀/2ⁿ;",
                     "2 p - pareizi aprēķināts nesabrukušo kodolu skaits;",
                     "1 p - pareizi aprēķināts sabrukušo kodolu skaits.",
                 ]},

                {"tips": "jautajumi", "virs": "Starojuma drošība un "
                                              "novērojumi",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Ziņu portālā raksta: «Pēc rentgena "
                           "izmeklējuma cilvēks kļūst radioaktīvs un ir "
                           "bīstams apkārtējiem.»",
                 "jaut": [
                     ("Novērtē apgalvojuma pareizību un pamato!", 1),
                     ("Paskaidro atšķirību starp apstarošanu un "
                      "piesārņojumu!", 1),
                     ("Nosauc trīs aizsardzības principus darbam ar "
                      "starojumu!", 1),
                     ("Paskaidro, kāpēc dabiskais fons nav bīstams!", 1),
                     ("Nosauc vienu medicīnisku lietojumu, kur "
                      "radioaktīvu vielu tomēr ievada organismā, un "
                      "paskaidro, kāpēc tas ir pieļaujams!", 1),
                 ],
                 "atbildes": [
                     "1) Nepareizs: rentgenstarojums iziet cauri "
                     "ķermenim, bet neatstāj tajā radioaktīvu vielu.   "
                     "(1 p)",
                     "2) Apstarošana - ķermenis saņem starojumu no ārēja "
                     "avota; piesārņojums - uz ķermeņa vai tajā nonāk "
                     "radioaktīva viela, kas turpina starot.   (1 p)",
                     "3) Īss laiks pie avota, liels attālums no avota un "
                     "ekranēšana ar piemērotu materiālu.   (1 p)",
                     "4) Fona devas (apmēram 2-3 mSv gadā) ir daudz "
                     "mazākas par devām, kurām novērotas veselības sekas; "
                     "organisms ir tām pielāgojies.   (1 p)",
                     "5) Piemēram, scintigrāfija ar īsas pussabrukšanas "
                     "izotopu: deva ir maza, izotops ātri sabrūk un tiek "
                     "izvadīts, bet diagnostiskais ieguvums ir liels.   "
                     "(1 p)",
                 ]},
            ],
        },
    ],
}
