# -*- coding: utf-8 -*-
"""PD1 — Pasaule ap mums un tās pētīšana (1.1.–1.6. stunda)."""

PD = {
    "nr": 1,
    "nosaukums": "Pasaule ap mums un tās pētīšana",
    "mape": "1. Pasaule ap mums un tās pētīšana",
    "fails": "PD1. Pasaule ap mums un tās pētīšana",
    "stundas": "1.1.–1.6.",
    "datums": "18.09.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda matērijas jēdzienu (viela un lauks), "
                "pasaules mērogus un organizācijas līmeņus, SI vienības un "
                "mērvienību pārveidi, mikroskopa palielinājumu un "
                "izšķirtspēju, mērījumu kļūdas un pētījuma plānošanu.",
    "atgadne": [
        "Priedēkļi:  k = 10³  ·  M = 10⁶  ·  c = 10⁻²  ·  m = 10⁻³  ·  "
        "µ = 10⁻⁶  ·  n = 10⁻⁹",
        "1 cm² = 10⁻⁴ m²  ·  1 cm³ = 10⁻⁶ m³  ·  no km/h uz m/s dala ar 3,6",
        "ρ = m / V   ·   Γ = Γ(objektīva) · Γ(okulāra)   ·   d = D / Γ   ·   "
        "ε = Δx / x · 100 %",
        "Optiskā mikroskopa izšķirtspēja ≈ 200 nm  ·  acs izšķirtspēja "
        "≈ 0,1 mm  ·  ρ(ūdens) = 1000 kg/m³  ·  ρ(Al) = 2700 kg/m³",
    ],
    "struktura": [
        ("1.", "Skaidro matēriju, klasificē objektus pēc mēroga, lieto SI "
               "vienības, atšķir palielinājumu no izšķirtspējas, novērtē "
               "mērījuma kļūdu, nosaka mainīgos lielumus", "1.1.–1.6.", 10),
        ("2.", "Pārvērš mērvienības, lietojot priedēkļus un standartformu",
         "1.2., 1.3.", 5),
        ("3.", "Pieraksta risinājumu pilnā formā un aprēķina blīvumu SI "
               "vienībās", "1.1., 1.3.", 5),
        ("4.", "Aprēķina mikroskopa palielinājumu un objekta patieso izmēru; "
               "pamato, vai objekts būs saskatāms", "1.4.", 4),
        ("5.", "Nosaka absolūto un relatīvo kļūdu, pieraksta rezultātu formā "
               "x = (x ± Δx)", "1.5.", 3),
        ("6.", "Nosaka neatkarīgo, atkarīgo un nemainīgos lielumus; noformē "
               "datus", "1.6.", 3),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kura matērijas eksistences forma NESASTĀV no daļiņām?",
                 ["viela", "molekula", "lauks", "atoms"], 2),
                ("Kurš no objektiem pieder mikropasaulei?",
                 ["ūdens molekula", "smilšu grauds", "Zeme",
                  "Saules sistēma"], 0),
                ("Kā standartformā metros pieraksta 0,45 nm?",
                 ["4,5 · 10⁻⁹ m", "4,5 · 10⁻¹⁰ m", "45 · 10⁻⁹ m",
                  "4,5 · 10⁻⁷ m"], 1),
                ("Kura no minētajām ir SI pamatvienība?",
                 ["ņūtons", "džouls", "mols", "vats"], 2),
                ("Cik liels tilpums ir 200 cm³, izteikts SI vienībās?",
                 ["2 · 10⁻⁴ m³", "2 · 10⁻² m³", "0,2 m³", "2 · 10⁻⁶ m³"], 0),
                ("Automašīnas ātrums ir 54 km/h. Cik tas ir m/s?",
                 ["5,4 m/s", "15 m/s", "19,4 m/s", "150 m/s"], 1),
                ("Ko raksturo mikroskopa izšķirtspēja?",
                 ["cik reižu attēls ir lielāks par objektu",
                  "mikroskopa lēcu skaitu",
                  "attēla spilgtumu ekrānā",
                  "mazāko attālumu starp diviem punktiem, kurus vēl redz "
                  "atsevišķi"], 3),
                ("Ar kuru mikroskopu var saskatīt atsevišķus atomus?",
                 ["ar optisko", "ar lupu", "ar atomspēku",
                  "ne ar vienu no tiem"], 2),
                ("Lineāla iedaļas vērtība ir 1 mm. Cik liela ir mērījuma "
                 "instrumenta kļūda?",
                 ["1 mm", "0,5 mm", "2 mm", "0,1 mm"], 1),
                ("Pēta, kā ūdens temperatūra ietekmē cukura izšķīšanas "
                 "laiku. Kurš lielums ir neatkarīgais?",
                 ["izšķīšanas laiks", "cukura masa", "trauka tilpums",
                  "ūdens temperatūra"], 3),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Izsaki lielumus SI mērvienībās",
                 "punkti": 5,
                 "rindas": [
                     ("750 g = ..................... kg", "0,75 kg"),
                     ("2,5 km = ..................... m   (standartformā)",
                      "2,5 · 10³ m"),
                     ("400 cm³ = ..................... m³", "4 · 10⁻⁴ m³"),
                     ("90 km/h = ..................... m/s", "25 m/s"),
                     ("120 nm = ..................... m   (standartformā)",
                      "1,2 · 10⁻⁷ m"),
                 ]},

                {"tips": "aprekins", "virs": "Vielas blīvums", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Metāla detaļas masa ir m = 810 g, bet tilpums "
                           "V = 300 cm³. Aprēķini detaļas vielas blīvumu SI "
                           "vienībās un nosaki, vai detaļa varētu būt "
                           "izgatavota no alumīnija (ρ(Al) = 2700 kg/m³)!",
                 "risinajums": [
                     "Dots:  m = 810 g;  V = 300 cm³;  ρ(Al) = 2700 kg/m³",
                     "Jāaprēķina:  ρ = ?  (kg/m³)",
                     "Formulas:  ρ = m / V",
                     "Aprēķins:  1) m = 810 g = 0,810 kg",
                     "                   2) V = 300 cm³ = 300 · 10⁻⁶ m³ = "
                     "3 · 10⁻⁴ m³",
                     "                   3) ρ = m / V = 0,810 kg : "
                     "(3 · 10⁻⁴ m³) = 2700 kg/m³",
                     "Atbilde:  ρ = 2700 kg/m³ = 2,7 · 10³ kg/m³. Blīvums "
                     "sakrīt ar alumīnija blīvumu, tātad detaļa varētu būt "
                     "no alumīnija.",
                 ],
                 "kriteriji": [
                     "1 p — pieraksts «Dots» un «Jāaprēķina»; lielumi "
                     "pārvērsti SI vienībās (0,810 kg un 3 · 10⁻⁴ m³);",
                     "1 p — pierakstīta formula ρ = m / V;",
                     "2 p — pareizs aprēķins ar mērvienībām (2700 kg/m³); ja "
                     "pieļauta tikai skaitļošanas kļūda, bet gaita pareiza — "
                     "1 p;",
                     "1 p — atbilde ar mērvienību un pamatots secinājums par "
                     "alumīniju.",
                 ]},

                {"tips": "jautajumi", "virs": "Mikropasaules pētīšana",
                 "punkti": 4, "vieta": 5.5,
                 "ievads": "Optiskā mikroskopa objektīva palielinājums ir "
                           "40×, bet okulāra — 15×.",
                 "jaut": [
                     ("Aprēķini mikroskopa palielinājumu Γ!", 1),
                     ("Attēlā šūna redzama D = 12 mm gara. Aprēķini šūnas "
                      "patieso izmēru d un izsaki to mikrometros!", 2),
                     ("Vai ar šo mikroskopu varēs saskatīt vīrusu, kura "
                      "izmērs ir 80 nm? Atbildi pamato!", 1),
                 ],
                 "atbildes": [
                     "1) Γ = Γ(ob) · Γ(ok) = 40 · 15 = 600×.   (1 p)",
                     "2) d = D / Γ = 12 mm : 600 = 0,02 mm = 2 · 10⁻⁵ m = "
                     "20 µm.   (1 p — formula un aprēķins; 1 p — pareiza "
                     "pārveide uz µm)",
                     "3) Nē. Vīrusa izmērs 80 nm ir mazāks par optiskā "
                     "mikroskopa izšķirtspēju ≈ 200 nm, tāpēc to atsevišķi "
                     "saskatīt nevar; lielāks palielinājums šeit būtu tukšais "
                     "palielinājums.   (1 p)",
                 ]},

                {"tips": "jautajumi", "virs": "Mērījumu precizitāte",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Ar lineālu, kura iedaļas vērtība ir c = 1 mm, "
                           "izmērīts stieņa garums l = 24,0 cm.",
                 "jaut": [
                     ("Nosaki absolūto kļūdu Δl un pieraksti rezultātu formā "
                      "l = (l ± Δl) cm!", 1),
                     ("Aprēķini mērījuma relatīvo kļūdu ε!", 1),
                     ("Nosauc vienu veidu, kā šo mērījumu varētu padarīt "
                      "precīzāku!", 1),
                 ],
                 "atbildes": [
                     "1) Analogai ierīcei Δl = c / 2 = 0,5 mm = 0,05 cm; "
                     "l = (24,00 ± 0,05) cm.   (1 p)",
                     "2) ε = Δl / l · 100 % = 0,05 cm : 24,00 cm · 100 % ≈ "
                     "0,2 %.   (1 p)",
                     "3) Jebkurš pamatots veids: mērīt vairākas reizes un "
                     "rēķināt vidējo vērtību; izvēlēties ierīci ar mazāku "
                     "iedaļas vērtību; mērīt lielāku garumu, jo tad relatīvā "
                     "kļūda ir mazāka.   (1 p)",
                 ]},

                {"tips": "jautajumi", "virs": "Pētījuma plānošana",
                 "punkti": 3, "vieta": 6.5,
                 "ievads": "Skolēns pēta, kā atsperes pagarinājums ir "
                           "atkarīgs no pakārtā atsvara masas. Viņš pakar "
                           "dažādas masas atsvarus un ar lineālu mēra "
                           "atsperes pagarinājumu.",
                 "jaut": [
                     ("Nosauc pētījuma neatkarīgo un atkarīgo lielumu!", 1),
                     ("Nosauc divus lielumus, kas jātur nemainīgi, lai "
                      "pētījums būtu godīgs!", 1),
                     ("Uz kuras ass atliek neatkarīgo lielumu un kas "
                      "obligāti jānorāda pie katras ass?", 1),
                 ],
                 "atbildes": [
                     "1) Neatkarīgais (maina) — atsvara masa m; atkarīgais "
                     "(mēra) — atsperes pagarinājums Δl.   (1 p par abiem "
                     "pareizi)",
                     "2) Divi no: tā pati atspere; tas pats statīvs un "
                     "stiprinājums; tas pats lineāls un mērīšanas veids; tā "
                     "pati temperatūra; mēra tikai tad, kad atsvars "
                     "apstājies.   (1 p)",
                     "3) Neatkarīgo lielumu (masu) atliek uz x ass, "
                     "atkarīgo — uz y ass; pie katras ass jānorāda lieluma "
                     "nosaukums vai apzīmējums UN mērvienība.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kurš apgalvojums par lauku ir pareizs?",
                 ["lauks sastāv no atomiem", "lauku var nosvērt uz svariem",
                  "lauks nodrošina mijiedarbību attālumā",
                  "laukam nepiemīt enerģija"], 2),
                ("Kurš no objektiem pieder megapasaulei?",
                 ["baktērija", "automašīna", "smilšu grauds", "Galaktika"], 3),
                ("Kā standartformā metros pieraksta 0,32 µm?",
                 ["3,2 · 10⁻⁷ m", "3,2 · 10⁻⁵ m", "32 · 10⁻⁶ m",
                  "3,2 · 10⁻⁹ m"], 0),
                ("Kura no minētajām NAV SI pamatvienība?",
                 ["kilograms", "kelvins", "paskāls", "sekunde"], 2),
                ("Cik liels laukums ir 250 cm², izteikts SI vienībās?",
                 ["2,5 · 10⁻² m²", "2,5 m²", "2,5 · 10⁻⁴ m²", "25 m²"], 0),
                ("Ķermeņa ātrums ir 15 m/s. Cik tas ir km/h?",
                 ["4,2 km/h", "54 km/h", "150 km/h", "900 km/h"], 1),
                ("Ko nozīmē «tukšais palielinājums»?",
                 ["attēls kļūst lielāks, bet izplūdis, un jaunu informāciju "
                  "nedod",
                  "mikroskopam nav okulāra",
                  "objekts ir pārāk liels mikroskopam",
                  "palielinājums ir mazāks par 1"], 0),
                ("Kāpēc ar optisko mikroskopu nevar saskatīt vīrusu?",
                 ["vīruss ir caurspīdīgs",
                  "vīrusa izmērs ir mazāks par mikroskopa izšķirtspēju",
                  "vīruss pārvietojas pārāk ātri",
                  "optiskajam mikroskopam ir pārāk mazs palielinājums"], 1),
                ("Digitālie svari rāda masu ar precizitāti līdz 0,01 g. Cik "
                 "liela ir šo svaru instrumenta kļūda?",
                 ["0,005 g", "0,1 g", "1 g", "0,01 g"], 3),
                ("Ko nozīmē «godīgs pētījums»?",
                 ["mēra tikai vienu reizi",
                  "vienlaikus maina tikai vienu lielumu",
                  "rezultātus noapaļo līdz veseliem skaitļiem",
                  "lieto tikai digitālās mērierīces"], 1),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Izsaki lielumus SI mērvienībās",
                 "punkti": 5,
                 "rindas": [
                     ("250 g = ..................... kg", "0,25 kg"),
                     ("0,75 km = ..................... m   (standartformā)",
                      "7,5 · 10² m"),
                     ("500 cm³ = ..................... m³", "5 · 10⁻⁴ m³"),
                     ("72 km/h = ..................... m/s", "20 m/s"),
                     ("45 µm = ..................... m   (standartformā)",
                      "4,5 · 10⁻⁵ m"),
                 ]},

                {"tips": "aprekins", "virs": "Vielas blīvums", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Ķermeņa masa ir m = 200 g, bet tilpums "
                           "V = 250 cm³. Aprēķini ķermeņa vielas blīvumu SI "
                           "vienībās un nosaki, vai ķermenis peldēs ūdenī "
                           "(ρ(ūdens) = 1000 kg/m³)!",
                 "risinajums": [
                     "Dots:  m = 200 g;  V = 250 cm³;  "
                     "ρ(ūdens) = 1000 kg/m³",
                     "Jāaprēķina:  ρ = ?  (kg/m³)",
                     "Formulas:  ρ = m / V",
                     "Aprēķins:  1) m = 200 g = 0,200 kg",
                     "                   2) V = 250 cm³ = 250 · 10⁻⁶ m³ = "
                     "2,5 · 10⁻⁴ m³",
                     "                   3) ρ = m / V = 0,200 kg : "
                     "(2,5 · 10⁻⁴ m³) = 800 kg/m³",
                     "Atbilde:  ρ = 800 kg/m³ = 8 · 10² kg/m³. Ķermeņa "
                     "blīvums ir mazāks nekā ūdens blīvums, tātad ķermenis "
                     "peldēs.",
                 ],
                 "kriteriji": [
                     "1 p — pieraksts «Dots» un «Jāaprēķina»; lielumi "
                     "pārvērsti SI vienībās (0,200 kg un 2,5 · 10⁻⁴ m³);",
                     "1 p — pierakstīta formula ρ = m / V;",
                     "2 p — pareizs aprēķins ar mērvienībām (800 kg/m³); ja "
                     "pieļauta tikai skaitļošanas kļūda, bet gaita pareiza — "
                     "1 p;",
                     "1 p — atbilde ar mērvienību un pamatots secinājums, ka "
                     "ķermenis peldēs.",
                 ]},

                {"tips": "jautajumi", "virs": "Mikropasaules pētīšana",
                 "punkti": 4, "vieta": 5.5,
                 "ievads": "Optiskā mikroskopa objektīva palielinājums ir "
                           "20×, bet okulāra — 15×.",
                 "jaut": [
                     ("Aprēķini mikroskopa palielinājumu Γ!", 1),
                     ("Attēlā šūna redzama D = 9 mm gara. Aprēķini šūnas "
                      "patieso izmēru d un izsaki to mikrometros!", 2),
                     ("Vai ar šo mikroskopu varēs saskatīt baktēriju, kuras "
                      "izmērs ir 2 µm? Atbildi pamato!", 1),
                 ],
                 "atbildes": [
                     "1) Γ = Γ(ob) · Γ(ok) = 20 · 15 = 300×.   (1 p)",
                     "2) d = D / Γ = 9 mm : 300 = 0,03 mm = 3 · 10⁻⁵ m = "
                     "30 µm.   (1 p — formula un aprēķins; 1 p — pareiza "
                     "pārveide uz µm)",
                     "3) Jā. Baktērijas izmērs 2 µm = 2000 nm ir lielāks par "
                     "optiskā mikroskopa izšķirtspēju ≈ 200 nm, tāpēc to var "
                     "saskatīt.   (1 p)",
                 ]},

                {"tips": "jautajumi", "virs": "Mērījumu precizitāte",
                 "punkti": 3, "vieta": 6.0,
                 "ievads": "Ar digitāliem svariem, kuru pēdējā cipara vienība "
                           "ir c = 0,01 g, izmērīta ķermeņa masa "
                           "m = 50,00 g.",
                 "jaut": [
                     ("Nosaki absolūto kļūdu Δm un pieraksti rezultātu formā "
                      "m = (m ± Δm) g!", 1),
                     ("Aprēķini mērījuma relatīvo kļūdu ε!", 1),
                     ("Vai digitāla ierīce vienmēr ir precīzāka par analogo? "
                      "Atbildi pamato!", 1),
                 ],
                 "atbildes": [
                     "1) Digitālai ierīcei Δm = c = 0,01 g; "
                     "m = (50,00 ± 0,01) g.   (1 p)",
                     "2) ε = Δm / m · 100 % = 0,01 g : 50,00 g · 100 % = "
                     "0,02 %.   (1 p)",
                     "3) Nē. Precizitāti nosaka ierīces kļūda, nevis tas, vai "
                     "rādījums ir skalā vai ciparos; ekrānā var būt daudz "
                     "ciparu, bet ierīces kļūda — liela.   (1 p)",
                 ]},

                {"tips": "jautajumi", "virs": "Pētījuma plānošana",
                 "punkti": 3, "vieta": 6.5,
                 "ievads": "Skolēns pēta, kā ūdens temperatūra ietekmē cukura "
                           "izšķīšanas laiku. Viņš vienādās glāzēs ielej "
                           "ūdeni dažādās temperatūrās un ar hronometru mēra "
                           "laiku, kādā cukurs izšķīst.",
                 "jaut": [
                     ("Nosauc pētījuma neatkarīgo un atkarīgo lielumu!", 1),
                     ("Nosauc divus lielumus, kas jātur nemainīgi, lai "
                      "pētījums būtu godīgs!", 1),
                     ("Kas obligāti jānorāda datu tabulas galvā un kāpēc "
                      "mērījumu atkārto vairākas reizes?", 1),
                 ],
                 "atbildes": [
                     "1) Neatkarīgais (maina) — ūdens temperatūra T; "
                     "atkarīgais (mēra) — cukura izšķīšanas laiks t.   "
                     "(1 p par abiem pareizi)",
                     "2) Divi no: tāda pati cukura masa; tāds pats ūdens "
                     "tilpums; tāds pats cukura graudu izmērs; vienāda "
                     "maisīšana vai bez maisīšanas; vienādas glāzes.   (1 p)",
                     "3) Tabulas galvā jānorāda lieluma nosaukums vai "
                     "apzīmējums UN mērvienība; mērījumu atkārto, lai varētu "
                     "aprēķināt vidējo vērtību un samazināt nejaušo kļūdu.   "
                     "(1 p)",
                 ]},
            ],
        },
    ],
}
