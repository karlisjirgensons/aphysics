# -*- coding: utf-8 -*-
"""PD7 — Visuma uzbūve un pētniecība (11.1.–11.8. stunda)."""

PD = {
    "nr": 7,
    "nosaukums": "Visuma uzbūve un pētniecība",
    "mape": "11. Visuma uzbūve un pētniecība",
    "fails": "PD7. Visuma uzbūve un pētniecība",
    "stundas": "11.1.–11.8.",
    "datums": "19.02.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda debess sfēru un zvaigznājus, Zemes "
                "kustības un gadalaikus, Saules sistēmu, attālumus Visumā, "
                "zvaigžņu raksturlielumus, galaktikas, Visuma pētniecības "
                "metodes un dzīvības apstākļus.",
    "atgadne": [
        "α = 15° · t   ·   Zemes rotācija 24 h   ·   riņķošana 365,25 "
        "dienas   ·   Zemes ass slīpums 23,5°",
        "υ = 2πR / T   ·   t = s / c   ·   c = 3,00 · 10⁸ m/s   ·   "
        "F = m · g",
        "1 au = 1,50 · 10¹¹ m   ·   1 ly = 9,46 · 10¹⁵ m   ·   "
        "1 pc = 3,09 · 10¹⁶ m = 3,26 ly",
        "1 diennakts = 86 400 s   ·   1 gads ≈ 3,15 · 10⁷ s   ·   Saules "
        "virsmas temperatūra ≈ 5800 K   ·   jo mazāks m, jo spožāks spīdeklis",
    ],
    "struktura": [
        ("1.", "Raksturo debess sfēras kustību, zvaigžņlielumu, gadalaikus, "
               "Saules sistēmas uzbūvi, zvaigznes un Visuma izplešanos",
         "11.1.–11.8.", 10),
        ("2.", "Aprēķina debess sfēras pagriezienu un skaidro Zemes kustību "
               "sekas", "11.1., 11.2.", 4),
        ("3.", "Rēķina ar astronomiskiem attālumiem un signāla ceļa laiku",
         "11.4.", 5),
        ("4.", "Aprēķina riņķošanas ātrumu pa orbītu", "11.2., 11.3.", 4),
        ("5.", "Saista zvaigznes krāsu ar temperatūru un lasa "
               "Hercšprunga–Rasela diagrammu", "11.5.", 4),
        ("6.", "Salīdzina Visuma pētīšanas metodes un vērtē dzīvības "
               "apstākļus", "11.7., 11.8.", 3),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kāpēc zvaigznes naktī redzami pārvietojas pie debesīm?",
                 ["tās riņķo ap Zemi", "Zeme griežas ap savu asi",
                  "Zeme riņķo ap Sauli", "to izraisa atmosfēras kustība"], 1),
                ("Par cik grādiem debess sfēra pagriežas vienā stundā?",
                 ["1°", "24°", "15°", "360°"], 2),
                ("Zvaigznei A zvaigžņlielums ir m = −1,5, zvaigznei B — "
                 "m = +2,0. Kura ir spožāka?",
                 ["zvaigzne A", "zvaigzne B", "abas vienādi spožas",
                  "pēc m to noteikt nevar"], 0),
                ("Kas rada gadalaikus uz Zemes?",
                 ["attāluma maiņa līdz Saulei", "Zemes ass slīpums 23,5°",
                  "Mēness kustība", "Saules aktivitātes maiņa"], 1),
                ("Cik ilgs ir Zemes riņķošanas periods ap Sauli?",
                 ["24 stundas", "28 dienas", "365,25 dienas", "12 gadi"], 2),
                ("Kura planēta pieder milžu planētām?",
                 ["Merkurs", "Venera", "Marss", "Saturns"], 3),
                ("Cik metru ir viena astronomiskā vienība (au)?",
                 ["1,50 · 10¹¹ m", "9,46 · 10¹⁵ m", "3,09 · 10¹⁶ m",
                  "3,00 · 10⁸ m"], 0),
                ("Kāda ir sarkanas zvaigznes virsmas temperatūra "
                 "salīdzinājumā ar zilganu zvaigzni?",
                 ["augstāka", "zemāka", "tieši tāda pati",
                  "krāsa ar temperatūru nav saistīta"], 1),
                ("Kurā Hercšprunga–Rasela diagrammas apgabalā atrodas "
                 "Saule?",
                 ["galvenajā secībā", "starp baltajiem punduriem",
                  "starp sarkanajiem pārmilžiem", "ārpus diagrammas"], 0),
                ("Ko pierāda tālu galaktiku spektra sarkanā nobīde?",
                 ["Visums saraujas", "Visums izplešas",
                  "galaktikas ir nekustīgas", "Zeme ir Visuma centrs"], 1),
            ],
            "uzdevumi": [
                {"tips": "jautajumi", "virs": "Debess sfēra un Zemes kustības",
                 "punkti": 4, "vieta": 6.5,
                 "ievads": "Atbildi uz jautājumiem! Pirmajā jautājumā parādi "
                           "aprēķinu.",
                 "jaut": [
                     ("Zvaigzni novēro plkst. 21:00. Par cik grādiem debess "
                      "sfēra būs pagriezusies līdz plkst. 24:00?", 1),
                     ("Nosauc abas Zemes kustības un to periodus!", 1),
                     ("Kāpēc Latvijā janvārī ir aukstāks nekā jūlijā, lai "
                      "gan janvārī Zeme atrodas tuvāk Saulei?", 2),
                 ],
                 "atbildes": [
                     "1) α = 15° · t = 15° · 3 h = 45°.   (1 p)",
                     "2) Rotācija ap savu asi — periods 24 h (diennakts); "
                     "riņķošana ap Sauli — periods 365,25 dienas (gads).   "
                     "(1 p par abām)",
                     "3) Gadalaikus nosaka nevis attālums, bet Zemes ass "
                     "slīpums 23,5°. Ziemā Saules stari krīt slīpi, tāpēc tā "
                     "pati enerģija sadalās uz lielāka laukuma (E = E₀·sin h), "
                     "un diena ir īsāka — Zeme saņem mazāk siltuma.   "
                     "(1 p par ass slīpumu, 1 p par staru krišanas leņķi un "
                     "dienas garumu)",
                 ]},

                {"tips": "aprekins", "virs": "Attālumi un signāla laiks",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Attālums no Zemes līdz Marsam tuvākajā stāvoklī "
                           "ir aptuveni s = 7,8 · 10¹⁰ m. Gaismas un "
                           "radioviļņu ātrums ir c = 3,0 · 10⁸ m/s. Cik ilgā "
                           "laikā radiosignāls no Zemes sasniedz Marsa "
                           "roveri? Izsaki atbildi arī minūtēs! Cik ilgi "
                           "operatoram jāgaida atbilde uz nosūtīto komandu?",
                 "risinajums": [
                     "Dots:  s = 7,8 · 10¹⁰ m;  c = 3,0 · 10⁸ m/s",
                     "Jāaprēķina:  t = ?  (s; min)    t(turp un atpakaļ) = ?",
                     "Formulas:  t = s / c",
                     "Aprēķins:  1) t = s / c = 7,8 · 10¹⁰ m : "
                     "(3,0 · 10⁸ m/s) = 260 s",
                     "                   2) 260 s : 60 s/min ≈ 4,3 min",
                     "                   3) atbildi gaida turp un atpakaļ: "
                     "2 · 260 s = 520 s ≈ 8,7 min",
                     "Atbilde:  signāls Marsu sasniedz pēc 260 s ≈ 4,3 min; "
                     "atbilde pienāk pēc ≈ 8,7 min.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstīta formula t = s / c;",
                     "1 p — pareizi aprēķināts t = 260 s;",
                     "1 p — pareiza pārveide minūtēs (≈ 4,3 min);",
                     "1 p — saprasts, ka atbildei ceļš jāveic divreiz "
                     "(≈ 8,7 min), un uzrakstīta atbilde.",
                 ]},

                {"tips": "aprekins", "virs": "Riņķošana pa orbītu",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Zeme riņķo ap Sauli pa aptuveni riņķveida "
                           "orbītu ar rādiusu R = 1,50 · 10¹¹ m. Riņķošanas "
                           "periods ir T = 365 dienas. Aprēķini Zemes "
                           "kustības ātrumu ap Sauli! Izsaki atbildi arī "
                           "kilometros sekundē.",
                 "risinajums": [
                     "Dots:  R = 1,50 · 10¹¹ m;  T = 365 dienas",
                     "Jāaprēķina:  υ = ?  (m/s; km/s)",
                     "Formulas:  υ = 2πR / T",
                     "Aprēķins:  1) T = 365 · 86 400 s ≈ 3,15 · 10⁷ s",
                     "                   2) 2πR = 2 · 3,14 · 1,50 · 10¹¹ m ≈ "
                     "9,42 · 10¹¹ m",
                     "                   3) υ = 9,42 · 10¹¹ m : "
                     "(3,15 · 10⁷ s) ≈ 3,0 · 10⁴ m/s",
                     "Atbilde:  υ ≈ 3,0 · 10⁴ m/s = 30 km/s.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula υ = 2πR/T;",
                     "1 p — perioda pārveide sekundēs (≈ 3,15 · 10⁷ s);",
                     "1 p — pareizi aprēķināts orbītas garums 2πR;",
                     "1 p — pareizs υ ≈ 30 km/s ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Zvaigznes", "punkti": 4,
                 "vieta": 6.5,
                 "ievads": "Zvaigznes A virsmas temperatūra ir 20 000 K, "
                           "zvaigznes B — 3000 K.",
                 "jaut": [
                     ("Kādā krāsā redzama katra no šīm zvaigznēm?", 1),
                     ("Kā astronomi nosaka zvaigznes temperatūru, tur "
                      "nemaz nelidojot?", 1),
                     ("Kāpēc sarkanie pārmilži ir ļoti spoži, lai gan to "
                      "virsma ir vēsa?", 1),
                     ("Nosauc Saules virsmas temperatūru un kurā "
                      "Hercšprunga–Rasela diagrammas apgabalā tā atrodas!",
                      1),
                 ],
                 "atbildes": [
                     "1) Zvaigzne A (20 000 K) ir zilgana, zvaigzne B "
                     "(3000 K) — sarkana. Jo karstāka zvaigzne, jo zilāka "
                     "gaisma.   (1 p par abām)",
                     "2) Pēc zvaigznes krāsas un spektra: krāsa viennozīmīgi "
                     "saistīta ar virsmas temperatūru — tāpat kā karsējot "
                     "metālu (vispirms sarkans, tad balts).   (1 p)",
                     "3) Tāpēc, ka tie ir ļoti lieli — starojošās virsmas "
                     "laukums ir milzīgs, tāpēc kopējā starjauda ir liela, "
                     "lai gan katrs virsmas laukuma kvadrātmetrs izstaro "
                     "maz.   (1 p)",
                     "4) Saules virsmas temperatūra ir ≈ 5800 K; tā atrodas "
                     "galvenās secības vidusdaļā kā dzeltena punduru "
                     "zvaigzne.   (1 p)",
                 ]},

                {"tips": "jautajumi", "virs": "Visuma pētniecība un dzīvība",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem!",
                 "jaut": [
                     ("Kāpēc radioteleskops var strādāt arī dienā un "
                      "mākoņainā laikā, bet optiskais teleskops — nē?", 1),
                     ("Kas ir apdzīvojamā zona un kāpēc Zeme tajā atrodas, "
                      "bet Venera un Marss — ne?", 1),
                     ("Nosauc vienu metodi, ar kuru atklāj citplanētas, un "
                      "paskaidro tās būtību!", 1),
                 ],
                 "atbildes": [
                     "1) Radioteleskops uztver radioviļņus, kuriem mākoņi un "
                     "dienas gaisma netraucē — atmosfēra tos praktiski "
                     "nekavē. Optiskais teleskops uztver redzamo gaismu, "
                     "kuru aizsedz mākoņi un pārspīlē dienas debesu un "
                     "gaismas piesārņojuma spilgtums.   (1 p)",
                     "2) Apdzīvojamā zona ir josla ap zvaigzni, kurā "
                     "temperatūra ļauj ūdenim uz virsmas būt šķidrā "
                     "stāvoklī. Venera atrodas par tuvu (par karstu), "
                     "Marss — par tālu (par aukstu), bet Zeme ir tieši šajā "
                     "joslā.   (1 p)",
                     "3) Tranzīta metode: kad planēta pārvietojas pār "
                     "zvaigzni, tās spožums nedaudz un regulāri samazinās. "
                     "(Var minēt arī radiālo ātrumu metodi: zvaigzne "
                     "planētas ietekmē nedaudz šūpojas.)   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kurā virzienā Zeme rotē ap savu asi?",
                 ["no austrumiem uz rietumiem",
                  "no rietumiem uz austrumiem", "no ziemeļiem uz dienvidiem",
                  "Zeme ap savu asi nerotē"], 1),
                ("Cik zvaigznāju kopā ir pie debesīm?",
                 ["12", "24", "360", "88"], 3),
                ("Kāds zvaigžņlielums ir vājākajai ar neapbruņotu aci "
                 "redzamajai zvaigznei?",
                 ["−26,7", "0", "+6", "+20"], 2),
                ("Kāpēc vasarā ir siltāk nekā ziemā?",
                 ["Zeme ir tuvāk Saulei",
                  "Saule izstaro vairāk enerģijas",
                  "Saules stari krīt stāvāk un diena ir garāka",
                  "atmosfēra ir plānāka"], 2),
                ("Cik ilga ir Zemes rotācija ap savu asi?",
                 ["24 stundas", "365 dienas", "28 dienas", "12 stundas"], 0),
                ("Kura planēta pieder Zemes grupai?",
                 ["Marss", "Jupiters", "Saturns", "Neptūns"], 0),
                ("Cik metru ir viens gaismas gads (ly)?",
                 ["1,50 · 10¹¹ m", "9,46 · 10¹⁵ m", "3,09 · 10¹⁶ m",
                  "3,00 · 10⁸ m"], 1),
                ("Ar kuru metodi mēra attālumu līdz tuvām zvaigznēm?",
                 ["ar paralakses metodi", "ar tranzīta metodi",
                  "pēc sarkanās nobīdes", "ar radiolokāciju"], 0),
                ("Kāda ir Piena Ceļa galaktikas forma?",
                 ["eliptiska", "neregulāra", "lodveida", "spirālveida"], 3),
                ("Kāpēc Venera ir karstāka par Merkuru, lai gan atrodas "
                 "tālāk no Saules?",
                 ["Venerai ir lielāka masa",
                  "Venerai ir blīva CO₂ atmosfēra un spēcīgs siltumnīcas "
                  "efekts",
                  "Venera rotē daudz ātrāk", "Merkuram nav gravitācijas"], 1),
            ],
            "uzdevumi": [
                {"tips": "jautajumi", "virs": "Debess sfēra un Zemes kustības",
                 "punkti": 4, "vieta": 6.5,
                 "ievads": "Atbildi uz jautājumiem! Pirmajā jautājumā parādi "
                           "aprēķinu.",
                 "jaut": [
                     ("Novērojumu sāk plkst. 20:00 un beidz plkst. 4:00. Par "
                      "cik grādiem debess sfēra šajā laikā pagriezīsies?", 1),
                     ("Kāpēc Latvijā ap Polārzvaigzni esošie spīdekļi "
                      "nenoriet?", 1),
                     ("Kāds ir Zemes ass slīpums un ko tas izraisa?", 1),
                     ("Kāpēc 21. decembrī Rīgā diena ir tikai aptuveni "
                      "6,5 stundas gara?", 1),
                 ],
                 "atbildes": [
                     "1) t = 8 h;  α = 15° · 8 = 120°.   (1 p)",
                     "2) Tie atrodas tuvu debess polam, ap kuru notiek "
                     "debess sfēras šķietamā griešanās, tāpēc to diennakts "
                     "apļi nekad nešķērso horizontu — Latvijas platuma grādos "
                     "tie paliek virs horizonta visu diennakti.   (1 p)",
                     "3) Zemes ass slīpums ir 23,5°; tas izraisa gadalaiku "
                     "maiņu, jo mainās Saules staru krišanas leņķis un dienas "
                     "garums.   (1 p)",
                     "4) Ziemas saulgriežos Ziemeļpuslode ir novērsta no "
                     "Saules: Saule paceļas tikai ~10° virs horizonta, tāpēc "
                     "tās ceļš virs horizonta ir īss un diena — ~6,5 h.   "
                     "(1 p)",
                 ]},

                {"tips": "aprekins", "virs": "Attālumi Visumā", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Tuvākā zvaigzne Proksima Kentaura atrodas "
                           "4,24 gaismas gadu attālumā (1 ly = "
                           "9,46 · 10¹⁵ m). Aprēķini šo attālumu metros! Cik "
                           "ilgā laikā to veiktu kosmiskais aparāts, kas lido "
                           "ar ātrumu υ = 20 km/s? Izsaki atbildi arī gados "
                           "(1 gads ≈ 3,15 · 10⁷ s).",
                 "risinajums": [
                     "Dots:  s = 4,24 ly;  1 ly = 9,46 · 10¹⁵ m;  "
                     "υ = 20 km/s",
                     "Jāaprēķina:  s = ?  (m)    t = ?  (s; gados)",
                     "Formulas:  t = s / υ",
                     "Aprēķins:  1) s = 4,24 · 9,46 · 10¹⁵ m ≈ "
                     "4,01 · 10¹⁶ m",
                     "                   2) υ = 20 km/s = 2,0 · 10⁴ m/s",
                     "                   3) t = s / υ = 4,01 · 10¹⁶ m : "
                     "(2,0 · 10⁴ m/s) ≈ 2,0 · 10¹² s",
                     "                   4) t = 2,0 · 10¹² s : "
                     "(3,15 · 10⁷ s/gadā) ≈ 6,4 · 10⁴ gadi",
                     "Atbilde:  s ≈ 4,0 · 10¹⁶ m;  lidojums ilgtu aptuveni "
                     "64 000 gadu.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pareizi aprēķināts s ≈ 4,0 · 10¹⁶ m;",
                     "1 p — pārveide 20 km/s = 2,0 · 10⁴ m/s;",
                     "1 p — pareizi aprēķināts t ≈ 2,0 · 10¹² s;",
                     "1 p — pareizi izteikts gados (≈ 64 000 gadu) un "
                     "uzrakstīta atbilde.",
                 ]},

                {"tips": "aprekins", "virs": "Riņķošana pa orbītu",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Mēness riņķo ap Zemi pa aptuveni riņķveida "
                           "orbītu ar rādiusu R = 3,84 · 10⁸ m. Riņķošanas "
                           "periods ir T = 27,3 dienas. Aprēķini Mēness "
                           "kustības ātrumu! Izsaki atbildi arī kilometros "
                           "sekundē.",
                 "risinajums": [
                     "Dots:  R = 3,84 · 10⁸ m;  T = 27,3 dienas",
                     "Jāaprēķina:  υ = ?  (m/s; km/s)",
                     "Formulas:  υ = 2πR / T",
                     "Aprēķins:  1) T = 27,3 · 86 400 s ≈ 2,36 · 10⁶ s",
                     "                   2) 2πR = 2 · 3,14 · 3,84 · 10⁸ m ≈ "
                     "2,41 · 10⁹ m",
                     "                   3) υ = 2,41 · 10⁹ m : "
                     "(2,36 · 10⁶ s) ≈ 1,0 · 10³ m/s",
                     "Atbilde:  υ ≈ 1,0 · 10³ m/s = 1,0 km/s.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula υ = 2πR/T;",
                     "1 p — perioda pārveide sekundēs (≈ 2,36 · 10⁶ s);",
                     "1 p — pareizi aprēķināts orbītas garums 2πR;",
                     "1 p — pareizs υ ≈ 1,0 km/s ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Zvaigznes", "punkti": 4,
                 "vieta": 6.5,
                 "ievads": "Zvaigznes A virsmas temperatūra ir 10 000 K, "
                           "zvaigznes B — 4000 K.",
                 "jaut": [
                     ("Kādā krāsā redzama katra no šīm zvaigznēm?", 1),
                     ("Kāpēc baltie punduri ir vāji spīdekļi, lai gan to "
                      "virsma ir karsta?", 1),
                     ("Cik liela daļa zvaigžņu atrodas galvenajā secībā un "
                      "kāda tur ir Saule?", 1),
                     ("Kā pēc spektra nosaka, no kādiem ķīmiskajiem "
                      "elementiem zvaigzne sastāv?", 1),
                 ],
                 "atbildes": [
                     "1) Zvaigzne A (10 000 K) ir balta, zvaigzne B "
                     "(4000 K) — oranža (tuvu sarkanai).   (1 p par abām)",
                     "2) Tāpēc, ka tie ir ļoti mazi — starojošās virsmas "
                     "laukums ir niecīgs, tāpēc kopējā starjauda ir maza, "
                     "lai gan katrs kvadrātmetrs izstaro daudz.   (1 p)",
                     "3) Galvenajā secībā atrodas aptuveni 90 % zvaigžņu; "
                     "Saule tur ir dzeltena punduru zvaigzne diagrammas "
                     "vidusdaļā.   (1 p)",
                     "4) Katram elementam ir savs līniju spektrs — kā pirkstu "
                     "nospiedums. Salīdzinot zvaigznes spektra līnijas ar "
                     "laboratorijā zināmajām, nosaka, kuri elementi tur ir.   "
                     "(1 p)",
                 ]},

                {"tips": "jautajumi", "virs": "Visuma pētniecība un dzīvība",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem!",
                 "jaut": [
                     ("Nosauc Irbenes radioteleskopu, tā diametru un "
                      "paskaidro, kāpēc tas ir nozīmīgs!", 1),
                     ("Kāpēc mēs redzam tālus Visuma objektus tādus, kādi "
                      "tie bija pagātnē?", 1),
                     ("Nosauc divus apstākļus, kas nepieciešami dzīvībai uz "
                      "planētas!", 1),
                 ],
                 "atbildes": [
                     "1) RT-32 Ventspils novadā — 32 m diametra "
                     "radioteleskops, lielākais Ziemeļeiropā un astotais "
                     "lielākais pasaulē; tas piedalās starptautiskos "
                     "novērojumu tīklos.   (1 p)",
                     "2) Gaismas ātrums ir galīgs, tāpēc gaismai no tāla "
                     "objekta vajadzīgs ilgs laiks, lai mūs sasniegtu — mēs "
                     "redzam objektu tādu, kāds tas bija brīdī, kad gaisma "
                     "to pameta.   (1 p)",
                     "3) Divi no: zvaigznes starojums kā enerģijas avots; "
                     "šķidrs ūdens uz virsmas; piemērota sastāva atmosfēra; "
                     "magnētiskais lauks aizsardzībai no starojuma; "
                     "pietiekama gravitācija atmosfēras noturēšanai.   (1 p)",
                 ]},
            ],
        },
    ],
}
