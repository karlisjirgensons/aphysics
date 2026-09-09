# -*- coding: utf-8 -*-
"""PD9 — Enerģija dabā un tehnikā (15.1.–15.8. stunda)."""

PD = {
    "nr": 9,
    "nosaukums": "Enerģija dabā un tehnikā",
    "mape": "14.-15. Enerģija dabā un tehnikā",
    "fails": "PD9. Enerģija dabā un tehnikā",
    "stundas": "15.1.–15.8.",
    "datums": "16.04.2027.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda darbu, enerģiju un jaudu, kinētisko un "
                "potenciālo enerģiju, enerģijas nezūdamību, lietderības "
                "koeficientu, kurināmo, elektroenerģijas patēriņu, "
                "elektrodrošību un transformatoru.",
    "atgadne": [
        "A = F · s   ·   P = A / t   ·   F = m · g   ·   g = 10 m/s²   ·   "
        "1 J = 1 N·m   ·   1 W = 1 J/s",
        "Ek = m · υ² / 2   ·   Ep = m · g · h   ·   Ep + Ek = const",
        "η = A(lietderīgais) / A(patērētais) · 100 %   ·   Q = q · m",
        "P = I · U   ·   E = P · t   ·   1 kWh = 3,6 · 10⁶ J   ·   "
        "k = N₁ / N₂ = U₁ / U₂",
    ],
    "struktura": [
        ("1.", "Raksturo darbu, jaudu, enerģijas veidus un pārvērtības, "
               "lietderības koeficientu, elektrodrošību un pārvadi",
         "15.1.–15.8.", 10),
        ("2.", "Aprēķina padarīto darbu un jaudu", "15.1.", 4),
        ("3.", "Lieto enerģijas nezūdamības likumu potenciālās un kinētiskās "
               "enerģijas aprēķinam", "15.2., 15.3.", 5),
        ("4.", "Aprēķina lietderības koeficientu un zudumus", "15.4.", 4),
        ("5.", "Aprēķina elektroenerģijas patēriņu kWh un izmaksas",
         "15.6.", 4),
        ("6.", "Rēķina ar transformatoru un izvērtē elektrodrošību",
         "15.7., 15.8.", 3),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kad tiek veikts mehāniskais darbs?",
                 ["kad spēks pārvieto ķermeni spēka virzienā",
                  "kad somu tur rokā nekustīgi",
                  "kad stumj sienu, kas nekustas",
                  "vienmēr, kad uz ķermeni darbojas spēks"], 0),
                ("Kāda ir jaudas mērvienība?",
                 ["džouls", "ņūtons", "vats", "paskāls"], 2),
                ("Kā kinētiskā enerģija ir atkarīga no ātruma?",
                 ["lineāri", "ar ātruma kvadrātu", "ar ātruma kubu",
                  "no ātruma nav atkarīga"], 1),
                ("Ar kuru formulu aprēķina potenciālo enerģiju?",
                 ["Ep = m · υ² / 2", "Ep = m · g · h", "Ep = F · s",
                  "Ep = P · t"], 1),
                ("Ko apgalvo enerģijas nezūdamības likums?",
                 ["enerģija var rasties no nekā",
                  "enerģija berzē pilnībā pazūd",
                  "enerģija tikai pārvēršas no viena veida citā",
                  "enerģija ar laiku vienmēr palielinās"], 2),
                ("Cik liels ir lietderības koeficients η reālai ierīcei?",
                 ["lielāks par 100 %", "tieši 100 %", "mazāks par 100 %",
                  "atkarīgs no darbības laika"], 2),
                ("Cik džoulu ir vienā kilovatstundā?",
                 ["3600 J", "3,6 · 10⁶ J", "1000 J", "10⁶ J"], 1),
                ("Kurai ierīcei ir vislielākais lietderības koeficients?",
                 ["kvēlspuldzei", "iekšdedzes dzinējam", "saules panelim",
                  "elektromotoram"], 3),
                ("Kāds spriegums ir Latvijas mājsaimniecību elektrotīklā?",
                 ["230 V", "12 V", "110 V", "400 kV"], 0),
                ("Kāpēc elektroenerģiju pārvades līnijās pārvada ar augstu "
                 "spriegumu?",
                 ["lai vadi varētu būt plānāki",
                  "lai samazinātu strāvu un līdz ar to zudumus vados",
                  "lai ierīces strādātu ātrāk",
                  "lai palielinātu pārvadīto jaudu"], 1),
            ],
            "uzdevumi": [
                {"tips": "aprekins", "virs": "Darbs un jauda", "punkti": 4,
                 "vieta": 6.5,
                 "teksts": "Celtnis vienmērīgi paceļ kravu, kuras masa ir "
                           "m = 500 kg, augstumā h = 12 m, un tas aizņem "
                           "t = 20 s. Aprēķini padarīto darbu un celtņa "
                           "jaudu! Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  m = 500 kg;  h = 12 m;  t = 20 s;  g = 10 m/s²",
                     "Jāaprēķina:  A = ?  (J)    P = ?  (W)",
                     "Formulas:  F = m · g ;   A = F · h ;   P = A / t",
                     "Aprēķins:  1) F = 500 kg · 10 m/s² = 5000 N",
                     "                   2) A = F · h = 5000 N · 12 m = "
                     "60 000 J = 60 kJ",
                     "                   3) P = A / t = 60 000 J : 20 s = "
                     "3000 W = 3 kW",
                     "Atbilde:  A = 60 kJ;  P = 3 kW.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formulas F = m·g, "
                     "A = F·h, P = A/t;",
                     "1 p — pareizi aprēķināts F = 5000 N;",
                     "1 p — pareizi aprēķināts A = 60 000 J;",
                     "1 p — pareizi aprēķināts P = 3000 W un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Enerģijas nezūdamība",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Ķermenis, kura masa ir m = 2 kg, brīvi krīt no "
                           "h = 20 m augstuma. Gaisa pretestību neņem vērā, "
                           "g = 10 m/s². Aprēķini potenciālo enerģiju "
                           "sākumā, kinētisko enerģiju tieši pirms zemes un "
                           "ātrumu, ar kādu ķermenis sasniedz zemi!",
                 "risinajums": [
                     "Dots:  m = 2 kg;  h = 20 m;  g = 10 m/s²",
                     "Jāaprēķina:  Ep = ?    Ek = ?  (J)    υ = ?  (m/s)",
                     "Formulas:  Ep = m · g · h ;   Ep = Ek ;   "
                     "Ek = m · υ² / 2  →  υ = √(2 · Ek / m)",
                     "Aprēķins:  1) Ep = 2 kg · 10 m/s² · 20 m = 400 J",
                     "                   2) pēc nezūdamības likuma tieši "
                     "pirms zemes Ek = Ep = 400 J",
                     "                   3) υ = √(2 · 400 J : 2 kg) = "
                     "√400 = 20 m/s",
                     "Atbilde:  Ep = 400 J;  Ek = 400 J;  υ = 20 m/s.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas Ep = mgh un Ek = mυ²/2;",
                     "1 p — pareizi aprēķināts Ep = 400 J;",
                     "1 p — pamatots, ka Ek = Ep = 400 J (enerģijas "
                     "nezūdamība);",
                     "1 p — pareizi aprēķināts υ = 20 m/s un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Lietderības koeficients",
                 "punkti": 4, "vieta": 6.0,
                 "teksts": "Elektromotors patērē A(pat) = 2400 J enerģijas "
                           "un veic lietderīgo darbu A(liet) = 2040 J. "
                           "Aprēķini motora lietderības koeficientu! Cik "
                           "daudz enerģijas pārvēršas siltumā?",
                 "risinajums": [
                     "Dots:  A(pat) = 2400 J;  A(liet) = 2040 J",
                     "Jāaprēķina:  η = ?  (%)    A(zud) = ?  (J)",
                     "Formulas:  η = A(liet) / A(pat) · 100 % ;   "
                     "A(zud) = A(pat) − A(liet)",
                     "Aprēķins:  1) η = 2040 J : 2400 J · 100 % = "
                     "0,85 · 100 % = 85 %",
                     "                   2) A(zud) = 2400 J − 2040 J = 360 J",
                     "Atbilde:  η = 85 %;  siltumā pārvēršas 360 J — "
                     "galvenokārt vados un gultņos.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula η = "
                     "A(liet)/A(pat) · 100 %;",
                     "1 p — pareizi aprēķināts η = 85 %;",
                     "1 p — pareizi aprēķināti zudumi 360 J;",
                     "1 p — atbilde ar mērvienībām un procentiem. Ja iegūts "
                     "η > 100 %, punktus par aprēķinu nepiešķir.",
                 ]},

                {"tips": "aprekins", "virs": "Elektroenerģijas izmaksas",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Elektriskā plīts, kuras jauda ir P = 3000 W, "
                           "darbojas 30 minūtes dienā. Elektroenerģijas "
                           "tarifs ir 0,20 EUR/kWh. Aprēķini dienā patērēto "
                           "enerģiju kilovatstundās un izmaksas mēnesī "
                           "(30 dienas)!",
                 "risinajums": [
                     "Dots:  P = 3000 W;  t = 30 min dienā;  "
                     "tarifs 0,20 EUR/kWh;  30 dienas",
                     "Jāaprēķina:  E(dienā) = ?  (kWh)    izmaksas = ?  (EUR)",
                     "Formulas:  E = P · t ;   izmaksas = E · tarifs",
                     "Aprēķins:  1) P = 3000 W = 3 kW;  t = 30 min = 0,5 h",
                     "                   2) E(dienā) = 3 kW · 0,5 h = "
                     "1,5 kWh",
                     "                   3) E(mēnesī) = 1,5 kWh · 30 = "
                     "45 kWh",
                     "                   4) izmaksas = 45 kWh · "
                     "0,20 EUR/kWh = 9,00 EUR",
                     "Atbilde:  dienā 1,5 kWh;  mēnesī 45 kWh, kas maksā "
                     "9,00 EUR.",
                 ],
                 "kriteriji": [
                     "1 p — pārveides P = 3 kW un t = 0,5 h;",
                     "1 p — pierakstīta formula E = P · t;",
                     "1 p — pareizi aprēķināts E(dienā) = 1,5 kWh un "
                     "E(mēnesī) = 45 kWh;",
                     "1 p — pareizas izmaksas 9,00 EUR un atbilde.",
                 ]},

                {"tips": "jautajumi", "virs": "Transformators un drošība",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem! Pirmajā jautājumā parādi "
                           "aprēķinu.",
                 "jaut": [
                     ("Transformatora primārajā spolē ir N₁ = 1000 vijumu, "
                      "sekundārajā N₂ = 100. Primārais spriegums ir "
                      "U₁ = 2300 V. Aprēķini U₂!", 1),
                     ("Ar ko pārslodze atšķiras no īsslēguma?", 1),
                     ("Kāda ir pirmā darbība, ieraugot cilvēku, kuru skārusi "
                      "elektriskā strāva? Kāpēc tieši tā?", 1),
                 ],
                 "atbildes": [
                     "1) N₁ / N₂ = U₁ / U₂  →  U₂ = U₁ · N₂ / N₁ = "
                     "2300 V · 100 : 1000 = 230 V. Tas ir pazeminošs "
                     "transformators.   (1 p)",
                     "2) Pārslodze — vienā līnijā ieslēgts par daudz ierīču, "
                     "strāva pārsniedz vada izturību, un vadi pakāpeniski "
                     "sakarst. Īsslēgums — fāzes un nulles vadi saskaras, "
                     "pretestība kļūst gandrīz nulle un strāva momentāni "
                     "kļūst milzīga.   (1 p)",
                     "3) Vispirms jāatslēdz strāva (slēdzis vai "
                     "drošinātājs), un tikai tad drīkst pieskarties "
                     "cietušajam — citādi strāva ietu arī caur glābēju. Ja "
                     "atslēgt nevar, cietušo atbīda ar sausu koka vai "
                     "plastmasas priekšmetu, pēc tam zvana 113.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kurā gadījumā mehāniskais darbs NETIEK veikts?",
                 ["ceļot somu augšup", "stumjot ratiņus uz priekšu",
                  "turot somu rokā nekustīgi", "velkot vagonu"], 2),
                ("Kāda ir darba un enerģijas mērvienība?",
                 ["vats", "džouls", "ņūtons", "hercs"], 1),
                ("Ar kuru formulu aprēķina kinētisko enerģiju?",
                 ["Ek = m · g · h", "Ek = m · υ² / 2", "Ek = F · s",
                  "Ek = q · m"], 1),
                ("Ja automašīnas ātrums palielinās divas reizes, tās "
                 "kinētiskā enerģija",
                 ["nemainās", "palielinās 2 reizes", "samazinās 2 reizes",
                  "palielinās 4 reizes"], 3),
                ("Kur «pazūd» enerģija reālās mehāniskās sistēmās?",
                 ["tā tiešām iznīkst",
                  "tā pārvēršas siltumā un izkliedējas apkārtējā vidē",
                  "tā pārvēršas masā", "tā uzkrājas berzes virsmās"], 1),
                ("Kāds ir kvēlspuldzes aptuvenais lietderības koeficients?",
                 ["~5 %", "~40 %", "~85 %", "~95 %"], 0),
                ("Ar kuru formulu aprēķina kurināmā sadegšanā izdalīto "
                 "siltumu?",
                 ["Q = q · m", "Q = m · g · h", "Q = P · t", "Q = F · s"], 0),
                ("Kura ierīce pārvērš mehānisko enerģiju elektriskajā?",
                 ["elektrodzinējs", "transformators", "drošinātājs",
                  "ģenerators"], 3),
                ("Ar kādu strāvu darbojas transformators?",
                 ["tikai ar līdzstrāvu", "tikai ar maiņstrāvu",
                  "ar abām vienādi labi", "tam strāva nav vajadzīga"], 1),
                ("Kāda strāva caur cilvēku jau ir dzīvībai bīstama?",
                 ["0,5 mA", "5 mA", "virs 100 mA", "1 µA"], 2),
            ],
            "uzdevumi": [
                {"tips": "aprekins", "virs": "Darbs un jauda", "punkti": 4,
                 "vieta": 6.5,
                 "teksts": "Iekrāvējs vienmērīgi paceļ kravu, kuras masa ir "
                           "m = 300 kg, augstumā h = 6 m, un tas aizņem "
                           "t = 15 s. Aprēķini padarīto darbu un iekrāvēja "
                           "jaudu! Pieņem, ka g = 10 m/s².",
                 "risinajums": [
                     "Dots:  m = 300 kg;  h = 6 m;  t = 15 s;  g = 10 m/s²",
                     "Jāaprēķina:  A = ?  (J)    P = ?  (W)",
                     "Formulas:  F = m · g ;   A = F · h ;   P = A / t",
                     "Aprēķins:  1) F = 300 kg · 10 m/s² = 3000 N",
                     "                   2) A = F · h = 3000 N · 6 m = "
                     "18 000 J = 18 kJ",
                     "                   3) P = A / t = 18 000 J : 15 s = "
                     "1200 W = 1,2 kW",
                     "Atbilde:  A = 18 kJ;  P = 1,2 kW.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formulas F = m·g, "
                     "A = F·h, P = A/t;",
                     "1 p — pareizi aprēķināts F = 3000 N;",
                     "1 p — pareizi aprēķināts A = 18 000 J;",
                     "1 p — pareizi aprēķināts P = 1200 W un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Enerģijas nezūdamība",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Ķermenis, kura masa ir m = 4 kg, brīvi krīt no "
                           "h = 45 m augstuma. Gaisa pretestību neņem vērā, "
                           "g = 10 m/s². Aprēķini potenciālo enerģiju "
                           "sākumā, kinētisko enerģiju tieši pirms zemes un "
                           "ātrumu, ar kādu ķermenis sasniedz zemi!",
                 "risinajums": [
                     "Dots:  m = 4 kg;  h = 45 m;  g = 10 m/s²",
                     "Jāaprēķina:  Ep = ?    Ek = ?  (J)    υ = ?  (m/s)",
                     "Formulas:  Ep = m · g · h ;   Ep = Ek ;   "
                     "Ek = m · υ² / 2  →  υ = √(2 · Ek / m)",
                     "Aprēķins:  1) Ep = 4 kg · 10 m/s² · 45 m = 1800 J",
                     "                   2) pēc nezūdamības likuma tieši "
                     "pirms zemes Ek = Ep = 1800 J",
                     "                   3) υ = √(2 · 1800 J : 4 kg) = "
                     "√900 = 30 m/s",
                     "Atbilde:  Ep = 1800 J;  Ek = 1800 J;  υ = 30 m/s.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots» un «Jāaprēķina» pieraksts;",
                     "1 p — pierakstītas formulas Ep = mgh un Ek = mυ²/2;",
                     "1 p — pareizi aprēķināts Ep = 1800 J;",
                     "1 p — pamatots, ka Ek = Ep = 1800 J (enerģijas "
                     "nezūdamība);",
                     "1 p — pareizi aprēķināts υ = 30 m/s un atbilde ar "
                     "mērvienībām.",
                 ]},

                {"tips": "aprekins", "virs": "Lietderības koeficients",
                 "punkti": 4, "vieta": 6.0,
                 "teksts": "Iekšdedzes dzinējs patērē A(pat) = 5000 J "
                           "enerģijas un veic lietderīgo darbu "
                           "A(liet) = 1500 J. Aprēķini dzinēja lietderības "
                           "koeficientu! Cik daudz enerģijas aiziet "
                           "zudumos?",
                 "risinajums": [
                     "Dots:  A(pat) = 5000 J;  A(liet) = 1500 J",
                     "Jāaprēķina:  η = ?  (%)    A(zud) = ?  (J)",
                     "Formulas:  η = A(liet) / A(pat) · 100 % ;   "
                     "A(zud) = A(pat) − A(liet)",
                     "Aprēķins:  1) η = 1500 J : 5000 J · 100 % = "
                     "0,30 · 100 % = 30 %",
                     "                   2) A(zud) = 5000 J − 1500 J = "
                     "3500 J",
                     "Atbilde:  η = 30 %;  zudumos aiziet 3500 J — "
                     "galvenokārt ar izplūdes gāzēm un dzesēšanu.",
                 ],
                 "kriteriji": [
                     "1 p — «Dots», «Jāaprēķina» un formula η = "
                     "A(liet)/A(pat) · 100 %;",
                     "1 p — pareizi aprēķināts η = 30 %;",
                     "1 p — pareizi aprēķināti zudumi 3500 J;",
                     "1 p — atbilde ar mērvienībām un procentiem. Ja iegūts "
                     "η > 100 %, punktus par aprēķinu nepiešķir.",
                 ]},

                {"tips": "aprekins", "virs": "Elektroenerģijas izmaksas",
                 "punkti": 4, "vieta": 6.5,
                 "teksts": "Tējkanna, kuras jauda ir P = 2000 W, darbojas "
                           "12 minūtes dienā. Elektroenerģijas tarifs ir "
                           "0,20 EUR/kWh. Aprēķini dienā patērēto enerģiju "
                           "kilovatstundās un izmaksas mēnesī (30 dienas)!",
                 "risinajums": [
                     "Dots:  P = 2000 W;  t = 12 min dienā;  "
                     "tarifs 0,20 EUR/kWh;  30 dienas",
                     "Jāaprēķina:  E(dienā) = ?  (kWh)    izmaksas = ?  (EUR)",
                     "Formulas:  E = P · t ;   izmaksas = E · tarifs",
                     "Aprēķins:  1) P = 2000 W = 2 kW;  t = 12 min = 0,2 h",
                     "                   2) E(dienā) = 2 kW · 0,2 h = "
                     "0,4 kWh",
                     "                   3) E(mēnesī) = 0,4 kWh · 30 = "
                     "12 kWh",
                     "                   4) izmaksas = 12 kWh · "
                     "0,20 EUR/kWh = 2,40 EUR",
                     "Atbilde:  dienā 0,4 kWh;  mēnesī 12 kWh, kas maksā "
                     "2,40 EUR.",
                 ],
                 "kriteriji": [
                     "1 p — pārveides P = 2 kW un t = 0,2 h;",
                     "1 p — pierakstīta formula E = P · t;",
                     "1 p — pareizi aprēķināts E(dienā) = 0,4 kWh un "
                     "E(mēnesī) = 12 kWh;",
                     "1 p — pareizas izmaksas 2,40 EUR un atbilde.",
                 ]},

                {"tips": "jautajumi", "virs": "Transformators un drošība",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Atbildi uz jautājumiem! Pirmajā jautājumā parādi "
                           "aprēķinu.",
                 "jaut": [
                     ("Transformatora primārajā spolē ir N₁ = 200 vijumu, "
                      "sekundārajā N₂ = 2000. Primārais spriegums ir "
                      "U₁ = 230 V. Aprēķini U₂ un nosaki, vai tas ir "
                      "paaugstinošs vai pazeminošs transformators!", 1),
                     ("Ar ko ģenerators atšķiras no elektrodzinēja?", 1),
                     ("Nosauc divas elektroaizsardzības ierīces un "
                      "paskaidro, kā katra darbojas!", 1),
                 ],
                 "atbildes": [
                     "1) N₁ / N₂ = U₁ / U₂  →  U₂ = U₁ · N₂ / N₁ = "
                     "230 V · 2000 : 200 = 2300 V. Tā kā N₂ > N₁, tas ir "
                     "PAAUGSTINOŠS transformators.   (1 p)",
                     "2) Ģenerators pārvērš mehānisko enerģiju "
                     "elektriskajā (spole griežas magnētiskajā laukā); "
                     "elektrodzinējs — otrādi, elektrisko enerģiju "
                     "mehāniskajā (strāva vadā magnētiskajā laukā rada "
                     "spēku).   (1 p)",
                     "3) Divas no: drošinātājs vai automātslēdzis — pārtrauc "
                     "ķēdi, ja strāva pārsniedz nominālo; zemējums — novada "
                     "bīstamo spriegumu zemē; noplūdes strāvas relejs "
                     "(RCD) — atslēdz ķēdi, ja strāva noplūst caur cilvēku.  "
                     " (1 p)",
                 ]},
            ],
        },
    ],
}
