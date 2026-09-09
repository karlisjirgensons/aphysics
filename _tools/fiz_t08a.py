# -*- coding: utf-8 -*-
"""8. temats "Siltums un siltuma procesi". A daļa: 8.1.-8.4. stunda.

8.4. stunda sagatavo LD1 «Siltuma māja» - mērījumi notiek nākamajā
dubultstundā, tāpēc šeit tiek plānots pētījums un datu tabula.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "8. temats. Siltums un siltuma procesi"
KICKER = "FIZIKA I · 11. KLASE · 8. TEMATS: SILTUMS UN SILTUMA PROCESI"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/8. Siltums un siltuma procesi"

STUNDAS = [

dict(
    nr="8.1", virsraksts="Iekšējā enerģija un siltuma pārnese",
    jautajums="Kāpēc siltināšana samazina enerģijas zudumus?",
    apaksraksts="Iekšējā enerģija · Siltumvadīšana · Konvekcija · Starojums",
    merkis="Atšķirt temperatūru no iekšējās enerģijas un salīdzināt trīs "
           "siltuma pārneses veidus mājoklī.",
    protu=["izskaidrot, kas ir iekšējā enerģija;",
           "atšķirt temperatūru no enerģijas;",
           "nosaukt trīs siltuma pārneses veidus;",
           "pamatot, kur mājoklī siltums aizplūst."],
    atkartojums="7. tematā noskaidrojām, ka daļiņas nepārtraukti kustas. "
                "Šo daļiņu enerģiju kopā sauc par iekšējo enerģiju - "
                "un tieši tā aizplūst pa sliktu sienu.",
    uzdevumu_apraksts="Enerģija, temperatūra un siltuma zudumi",
    teorija=[
        ("Iekšējā enerģija", [
            ("panelis", "KAS IR IEKŠĒJĀ ENERĢIJA",
             ["Iekšējā enerģija ir visu vielas daļiņu kustības enerģijas "
              "un savstarpējās mijiedarbības enerģijas summa.",
              "To var mainīt divējādi: nododot siltumu vai veicot darbu "
              "(piemēram, saberžot rokas).",
              "Siltums ir enerģijas pārnese no siltākā ķermeņa uz "
              "aukstāko - tas notiek pats no sevis, nekad otrādi."],
             NAVY),
            ("divi",
             ("TEMPERATŪRA", BLUE,
              ["Raksturo vienas daļiņas",
               "vidējo enerģiju.",
               "Nav atkarīga no masas.",
               "Karsta adata: augsta T,",
               "maza enerģija."]),
             ("IEKŠĒJĀ ENERĢIJA", GREEN,
              ["Raksturo visu daļiņu",
               "enerģiju kopā.",
               "Atkarīga arī no masas.",
               "Silta vanna: zemāka T,",
               "milzīga enerģija."])),
        ]),
        ("Trīs siltuma pārneses veidi", [
            ("kartitas", [
                ("SILTUMVADĪŠANA", BLUE,
                 ["Enerģija iet pa vielu.",
                  "Daļiņa nodod kaimiņam.",
                  "Metāli vada labi,",
                  "gaiss un putas - slikti."]),
                ("KONVEKCIJA", GREEN,
                 ["Pārvietojas pati viela.",
                  "Siltais gaiss ceļas augšup.",
                  "Notiek gāzēs un",
                  "šķidrumos."]),
                ("STAROJUMS", GOLD,
                 ["Enerģija iet ar viļņiem.",
                  "Vide nav vajadzīga.",
                  "Tā Saules siltums",
                  "sasniedz Zemi."]),
            ]),
            ("tabula",
             ["Vieta mājā", "Kā aizplūst siltums", "Risinājums"],
             [["Siena", "Siltumvadīšana", "Siltinājums, putuplasts"],
              ["Logs", "Vadīšana un starojums", "Stikla paketes"],
              ["Jumts", "Konvekcija uz augšu", "Bēniņu siltinājums"],
              ["Spraugas", "Gaisa apmaiņa", "Blīvējums, rekuperācija"]],
             [2.90, 4.10, 3.23]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Adata un vanna",
             teksts="Salīdzini 0,20 kg ūdens 80 °C temperatūrā un 1,0 kg\n"
                    "ūdens 40 °C temperatūrā. Kuram siltuma daudzums,\n"
                    "atdziestot līdz 0 °C, ir lielāks? (c = 4200 J/(kg·K))",
             dots=["m₁ = 0,20 kg;  Δt₁ = 80 K",
                   "m₂ = 1,0 kg;  Δt₂ = 40 K",
                   "c = 4200 J/(kg·K)"],
             jaaprekina=["Q₁ = ?", "Q₂ = ?"],
             formulas=["Q = cmΔT"],
             aprekins=["1)  Q₁ = 4200 · 0,20 · 80 = 67 200 J",
                       "2)  Q₂ = 4200 · 1,0 · 40 = 168 000 J",
                       "3)  Q₂ > Q₁ - lielāka masa uzvar"],
             atbilde="Q₁ ≈ 67 kJ;  Q₂ = 168 kJ",
             piezime="Augstāka temperatūra vēl nenozīmē lielāku "
                     "enerģiju - svarīga ir arī masa."),
        dict(nr=2, virsraksts="Siltināšanas ieguvums",
             teksts="Pirms siltināšanas siena zaudē 1200 W, pēc tās -\n"
                    "400 W. Cik enerģijas ietaupa 8 stundās?",
             dots=["P₁ = 1200 W", "P₂ = 400 W", "t = 8 h = 28 800 s"],
             jaaprekina=["ΔQ = ?"],
             formulas=["Q = Pt", "ΔQ = (P₁ − P₂)·t"],
             aprekins=["1)  ΔP = 1200 − 400 = 800 W",
                       "2)  ΔQ = 800 · 28 800",
                       "3)  ΔQ = 23 040 000 J ≈ 23 MJ"],
             atbilde="ΔQ ≈ 23 MJ",
             piezime="23 megadžouli ir apmēram 6,4 kWh - to var uzreiz "
                     "pārrēķināt naudā."),
        dict(nr=3, virsraksts="Kurš pārneses veids",
             teksts="Nosaki galveno siltuma pārneses veidu:\n"
                    "a) karota tējas glāzē; b) radiators sasilda istabu;\n"
                    "c) sejai silti pie ugunskura.",
             dots=["a) metāla karote", "b) gaiss istabā",
                   "c) attālums no uguns"],
             jaaprekina=["Pārneses veids = ?"],
             formulas=["Vadīšana - pa vielu",
                       "Konvekcija - ar vielas plūsmu",
                       "Starojums - bez vides"],
             aprekins=["1)  a) siltumvadīšana metālā",
                       "2)  b) konvekcija - siltais gaiss ceļas",
                       "3)  c) starojums - gaiss gandrīz nesilda"],
             atbilde="a) vadīšana; b) konvekcija; c) starojums",
             piezime="Praksē visi trīs veidi darbojas kopā; jautājums "
                     "vienmēr ir par galveno."),
        dict(nr=4, virsraksts="Termosa uzbūve",
             teksts="Termosam ir spoguļots iekšējais trauks, vakuuma\n"
                    "starpslānis un plastmasas korķis. Paskaidro, kuru\n"
                    "pārneses veidu katra daļa aptur!",
             dots=["Spoguļots trauks", "Vakuums starp sienām",
                   "Plastmasas korķis"],
             jaaprekina=["Ko aptur katra daļa?"],
             formulas=["Vakuumā nav daļiņu",
                       "Spogulis atstaro starojumu"],
             aprekins=["1)  Vakuums - nav vadīšanas un konvekcijas",
                       "2)  Spogulis - atstaro starojumu atpakaļ",
                       "3)  Korķis - aptur gaisa plūsmu augšup"],
             atbilde="Katra daļa aptur citu pārneses veidu",
             piezime="Tas pats princips darbojas mājas sienā: putas "
                     "aptur konvekciju, folija - starojumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Iekšējā enerģija ir visu daļiņu enerģija kopā.",
            "Temperatūra raksturo vienu daļiņu, enerģija - visu vielu.",
            "Siltums pārnesas ar vadīšanu, konvekciju un starojumu.",
            "Siltināšana samazina zudumus, apturot šos pārneses veidus.",
        ],
        majasdarbs=[
            "Nosauc, kā siltums aizplūst pa logu un kā to samazina.",
            "P = 900 W zudumi 5 h. Aprēķini enerģiju džoulos.",
            "Paskaidro, kāpēc putuplasts silda labāk nekā tikpat bieza "
            "koka plāksne.",
        ],
        pasvertejums=["Zinu, kas ir iekšējā enerģija",
                      "Atšķiru temperatūru no enerģijas",
                      "Zinu trīs pārneses veidus",
                      "Protu pamatot siltināšanu"],
        nakama="Nākamā stunda: siltuma daudzums Q = cmΔT."),
),

dict(
    nr="8.2", virsraksts="Siltuma daudzums",
    jautajums="No kā atkarīga ūdens uzsildīšanai vajadzīgā enerģija?",
    apaksraksts="Q = cmΔT · c ūdenim 4200 J/(kg·K) · Jaudas un laika saite",
    merkis="Lietot sakarību Q = cmΔT un izskaidrot katra lieluma nozīmi.",
    protu=["nosaukt lielumus formulā Q = cmΔT;",
           "aprēķināt siltuma daudzumu;",
           "izteikt masu vai temperatūras izmaiņu;",
           "saistīt siltuma daudzumu ar jaudu un laiku."],
    atkartojums="Iepriekšējā stundā jau salīdzinājām divus ūdens traukus. "
                "Šodien to pašu aprēķinu veiksim precīzi - ar īpatnējo "
                "siltumietilpību.",
    uzdevumu_apraksts="Siltuma daudzuma aprēķini",
    teorija=[
        ("Siltuma daudzums", [
            ("formula", "SILTUMA DAUDZUMS",
             "Q = c · m · ΔT        [Q] = džouls (J)",
             "c ir īpatnējā siltumietilpība - enerģija, kas vajadzīga, "
             "lai vienu kilogramu vielas sasildītu par vienu kelvinu. "
             "ΔT ir temperatūras izmaiņa.", GOLD),
            ("kartitas", [
                ("c - VIELA", BLUE,
                 ["Atkarīga tikai no vielas.",
                  "Ūdenim 4200 J/(kg·K).",
                  "Ūdens silst lēni."]),
                ("m - MASA", GREEN,
                 ["Divreiz vairāk ūdens -",
                  "divreiz vairāk enerģijas.",
                  "Mēra kilogramos."]),
                ("ΔT - IZMAIŅA", GOLD,
                 ["ΔT = t₂ − t₁.",
                  "Grādos un kelvinos",
                  "starpība ir vienāda."]),
            ]),
        ]),
        ("Vielu salīdzinājums", [
            ("tabula",
             ["Viela", "c (J/(kg·K))", "Ko tas nozīmē"],
             [["Ūdens", "4200", "Silst lēni, atdziest lēni"],
              ["Alumīnijs", "920", "Katls sasilst ātri"],
              ["Tērauds", "460", "Pannas ātri sakarst"],
              ["Smiltis", "800", "Pludmale dienā ļoti karsta"]],
             [2.90, 3.20, 4.13]),
            ("panelis", "SILTUMS UN JAUDA",
             ["Ja siltumu dod sildītājs ar jaudu P, tad Q = P · t. No "
              "šejienes var atrast sildīšanas laiku: t = Q/P.",
              "Ūdens lielā siltumietilpība izskaidro, kāpēc jūra vasarā "
              "sasilst lēni, bet rudenī vēl ilgi paliek silta.",
              "Tāpēc arī apkures sistēmās par siltumnesēju izmanto "
              "tieši ūdeni."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ūdens uzsildīšana",
             teksts="Cik daudz siltuma vajag, lai 2,0 kg ūdens sasildītu\n"
                    "no 20 °C līdz 80 °C? (c = 4200 J/(kg·K))",
             dots=["m = 2,0 kg", "t₁ = 20 °C", "t₂ = 80 °C",
                   "c = 4200 J/(kg·K)"],
             jaaprekina=["Q = ?"],
             formulas=["Q = cmΔT", "ΔT = t₂ − t₁"],
             aprekins=["1)  ΔT = 80 − 20 = 60 K",
                       "2)  Q = 4200 · 2,0 · 60",
                       "3)  Q = 504 000 J ≈ 504 kJ"],
             atbilde="Q ≈ 5,0·10⁵ J",
             piezime="Temperatūras STARPĪBU var rēķināt grādos - "
                     "kelvinos tā ir tāda pati."),
        dict(nr=2, virsraksts="Sildīšanas laiks",
             teksts="Elektriskā tējkanna ar jaudu 2000 W sasilda 1,5 kg\n"
                    "ūdens no 20 °C līdz 100 °C. Cik ilgi tas prasa?\n"
                    "(c = 4200 J/(kg·K))",
             dots=["P = 2000 W", "m = 1,5 kg", "ΔT = 80 K"],
             jaaprekina=["t = ?"],
             formulas=["Q = cmΔT", "Q = Pt", "t = Q/P"],
             aprekins=["1)  Q = 4200 · 1,5 · 80 = 504 000 J",
                       "2)  t = 504 000 : 2000",
                       "3)  t = 252 s ≈ 4,2 min"],
             atbilde="t ≈ 252 s",
             piezime="Īstenībā paiet ilgāk - daļa siltuma aizplūst "
                     "apkārtējā gaisā."),
        dict(nr=3, virsraksts="Temperatūras izmaiņa",
             teksts="Alumīnija katlam (m = 0,80 kg) pievada 36 800 J\n"
                    "siltuma. Par cik paaugstinās temperatūra?\n"
                    "(c = 920 J/(kg·K))",
             dots=["m = 0,80 kg", "Q = 36 800 J", "c = 920 J/(kg·K)"],
             jaaprekina=["ΔT = ?"],
             formulas=["Q = cmΔT", "ΔT = Q/cm"],
             aprekins=["1)  cm = 920 · 0,80 = 736",
                       "2)  ΔT = 36 800 : 736",
                       "3)  ΔT = 50 K"],
             atbilde="ΔT = 50 K",
             piezime="Tikpat liels siltuma daudzums ūdenī dotu daudz "
                     "mazāku temperatūras kāpumu."),
        dict(nr=4, virsraksts="Cik ūdens sasildīts",
             teksts="Sildītājs nodeva 1 260 000 J siltuma, un ūdens\n"
                    "temperatūra pieauga par 60 K.\n"
                    "Aprēķini ūdens masu! (c = 4200 J/(kg·K))",
             dots=["Q = 1 260 000 J", "ΔT = 60 K", "c = 4200 J/(kg·K)"],
             jaaprekina=["m = ?"],
             formulas=["Q = cmΔT", "m = Q/cΔT"],
             aprekins=["1)  cΔT = 4200 · 60 = 252 000",
                       "2)  m = 1 260 000 : 252 000",
                       "3)  m = 5,0 kg"],
             atbilde="m = 5,0 kg",
             piezime="No vienas formulas var izteikt jebkuru no "
                     "četriem lielumiem."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Q = cmΔT; siltuma daudzumu mēra džoulos.",
            "Īpatnējā siltumietilpība c ir vielas īpašība.",
            "Ūdenim c = 4200 J/(kg·K) - tas ir ļoti daudz.",
            "Ja zināma jauda, tad Q = Pt un t = Q/P.",
        ],
        majasdarbs=[
            "m = 3,0 kg ūdens, ΔT = 40 K. Aprēķini Q.",
            "Q = 92 000 J, m = 0,50 kg alumīnija. Aprēķini ΔT.",
            "P = 1500 W, Q = 300 000 J. Aprēķini sildīšanas laiku.",
        ],
        pasvertejums=["Zinu formulas lielumus",
                      "Protu aprēķināt Q",
                      "Protu izteikt m un ΔT",
                      "Protu saistīt Q ar jaudu"],
        nakama="Nākamā stunda: agregātstāvokļa maiņa un sildīšanas "
               "grafiks."),
),

dict(
    nr="8.3", virsraksts="Agregātstāvokļa maiņa",
    jautajums="Kāpēc kušanas laikā temperatūra var nemainīties?",
    apaksraksts="Q = λm · Q = Lm · Sildīšanas grafiks",
    merkis="Nolasīt sildīšanas grafiku un pēc parauga lietot sakarības "
           "Q = λm un Q = Lm.",
    protu=["nolasīt sildīšanas grafika posmus;",
           "izskaidrot, kāpēc kūstot temperatūra nemainās;",
           "aprēķināt kušanas siltumu Q = λm;",
           "aprēķināt iztvaikošanas siltumu Q = Lm."],
    atkartojums="Iepriekšējā stundā siltums paaugstināja temperatūru. "
                "Šodien redzēsim, ka daļa siltuma temperatūru nemaina "
                "vispār - tā tiek tērēta saišu saraušanai.",
    uzdevumu_apraksts="Kušana, iztvaikošana un grafiki",
    teorija=[
        ("Kušana un iztvaikošana", [
            ("formula", "AGREGĀTSTĀVOKĻA MAIŅAS SILTUMS",
             "Q = λ · m  (kušana)        Q = L · m  (iztvaikošana)",
             "λ ir īpatnējais kušanas siltums, L - īpatnējais "
             "iztvaikošanas siltums. Šī enerģija tiek tērēta daļiņu "
             "saišu saraušanai, nevis temperatūras celšanai.", GOLD),
            ("tabula",
             ["Process", "Formula", "Ūdenim"],
             [["Kušana (ledus)", "Q = λm", "λ = 3,3·10⁵ J/kg"],
              ["Iztvaikošana", "Q = Lm", "L = 2,3·10⁶ J/kg"],
              ["Sildīšana", "Q = cmΔT", "c = 4200 J/(kg·K)"],
              ["Kondensācija", "Q = Lm (atdod)", "Tvaiks apdedzina"]],
             [3.30, 3.20, 3.73]),
        ]),
        ("Sildīšanas grafiks", [
            ("divi",
             ("SLĪPIE POSMI", BLUE,
              ["Temperatūra mainās.",
               "Enerģija ceļ T.",
               "Lieto Q = cmΔT.",
               "Slīpums rāda, cik ātri",
               "viela silst."]),
             ("HORIZONTĀLIE POSMI", GREEN,
              ["Temperatūra nemainās.",
               "Enerģija rauj saites.",
               "Lieto Q = λm vai Q = Lm.",
               "Notiek kušana vai",
               "vārīšanās."])),
            ("panelis", "KĀPĒC TEMPERATŪRA NEMAINĀS",
             ["Kūstot visa pievadītā enerģija tiek tērēta kristāliskā "
              "režģa saišu saraušanai. Daļiņu vidējā kustības enerģija "
              "nepieaug - tāpēc termometrs rāda to pašu.",
              "Tāpēc ledus ar ūdeni glāzē ilgi notur 0 °C.",
              "Iztvaikošana prasa vēl vairāk enerģijas nekā kušana - "
              "ūdenim gandrīz septiņas reizes vairāk."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ledus kušana",
             teksts="Cik daudz siltuma vajag, lai izkausētu 2,0 kg ledus\n"
                    "0 °C temperatūrā? (λ = 3,3·10⁵ J/kg)",
             dots=["m = 2,0 kg", "λ = 3,3·10⁵ J/kg", "t = 0 °C"],
             jaaprekina=["Q = ?"],
             formulas=["Q = λm"],
             aprekins=["1)  Q = 3,3·10⁵ · 2,0",
                       "2)  Q = 6,6·10⁵ J = 660 kJ"],
             atbilde="Q = 6,6·10⁵ J",
             piezime="Temperatūra visu šo laiku paliek 0 °C - mainās "
                     "tikai agregātstāvoklis."),
        dict(nr=2, virsraksts="Ūdens iztvaikošana",
             teksts="Cik daudz siltuma vajag, lai 0,50 kg ūdens 100 °C\n"
                    "temperatūrā pārvērstu tvaikā? (L = 2,3·10⁶ J/kg)",
             dots=["m = 0,50 kg", "L = 2,3·10⁶ J/kg"],
             jaaprekina=["Q = ?"],
             formulas=["Q = Lm"],
             aprekins=["1)  Q = 2,3·10⁶ · 0,50",
                       "2)  Q = 1,15·10⁶ J ≈ 1,2 MJ"],
             atbilde="Q ≈ 1,2·10⁶ J",
             piezime="Tāpēc 100 °C tvaiks apdedzina daudz smagāk nekā "
                     "100 °C ūdens - kondensējoties tas atdod šo "
                     "enerģiju."),
        dict(nr=3, virsraksts="Divi posmi kopā",
             teksts="Cik daudz siltuma vajag, lai 1,0 kg ledus 0 °C\n"
                    "temperatūrā izkausētu un iegūto ūdeni sasildītu\n"
                    "līdz 20 °C? (λ = 3,3·10⁵ J/kg; c = 4200 J/(kg·K))",
             dots=["m = 1,0 kg", "λ = 3,3·10⁵ J/kg", "ΔT = 20 K",
                   "c = 4200 J/(kg·K)"],
             jaaprekina=["Q = ?"],
             formulas=["Q₁ = λm", "Q₂ = cmΔT", "Q = Q₁ + Q₂"],
             aprekins=["1)  Q₁ = 3,3·10⁵ · 1,0 = 330 000 J",
                       "2)  Q₂ = 4200 · 1,0 · 20 = 84 000 J",
                       "3)  Q = 330 000 + 84 000 = 414 000 J"],
             atbilde="Q ≈ 4,1·10⁵ J",
             piezime="Kušana prasīja gandrīz četras reizes vairāk "
                     "enerģijas nekā sildīšana par 20 grādiem."),
        dict(nr=4, virsraksts="Grafika nolasīšana",
             teksts="Grafikā ledus silst 2 min, tad 8 min temperatūra ir\n"
                    "0 °C, pēc tam ūdens silst. Sildītāja jauda 500 W.\n"
                    "Cik enerģijas iztērēts kušanai?",
             dots=["P = 500 W", "t = 8 min = 480 s",
                   "Horizontāls posms = kušana"],
             jaaprekina=["Q = ?"],
             formulas=["Q = Pt"],
             aprekins=["1)  t = 8 · 60 = 480 s",
                       "2)  Q = 500 · 480",
                       "3)  Q = 240 000 J = 240 kJ"],
             atbilde="Q = 2,4·10⁵ J",
             piezime="Horizontālā posma garums grafikā tieši parāda, cik "
                     "enerģijas prasīja kušana."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Kušanas siltums Q = λm, iztvaikošanas siltums Q = Lm.",
            "Agregātstāvokļa maiņas laikā temperatūra nemainās.",
            "Grafika horizontālie posmi ir kušana vai vārīšanās.",
            "Ūdenim L ir gandrīz septiņas reizes lielāks nekā λ.",
        ],
        majasdarbs=[
            "m = 0,40 kg ledus. Aprēķini kušanas siltumu.",
            "m = 0,20 kg ūdens iztvaicē. Aprēķini Q.",
            "Paskaidro, kāpēc tvaiks apdedzina smagāk nekā verdošs ūdens.",
        ],
        pasvertejums=["Protu lasīt sildīšanas grafiku",
                      "Zinu, kāpēc T nemainās",
                      "Protu rēķināt Q = λm",
                      "Protu rēķināt Q = Lm"],
        nakama="Nākamā stunda: siltuma bilance un LD1 «Siltuma māja» "
               "plānošana."),
),

dict(
    nr="8.4", virsraksts="Siltuma bilance un pētījuma plāns",
    jautajums="Kā godīgi salīdzināt siltumizolāciju?",
    apaksraksts="Q(atdotais) = Q(saņemtais) · Mainīgie · LD1 datu tabula",
    merkis="Ar enerģijas nezūdamību pamatot siltuma bilanci un sagatavot "
           "LD1 «Siltuma māja» pētījuma plānu.",
    protu=["uzrakstīt siltuma bilances vienādojumu;",
           "aprēķināt maisījuma temperatūru;",
           "formulēt pētāmo jautājumu un mainīgos;",
           "sagatavot datu tabulu mērījumiem."],
    atkartojums="5. tematā mācījāmies enerģijas nezūdamību. Siltuma "
                "bilance ir tas pats likums: cik enerģijas viens "
                "ķermenis atdod, tik otrs saņem.",
    uzdevumu_apraksts="Siltuma bilance un LD1 sagatavošana",
    teorija=[
        ("Siltuma bilance", [
            ("formula", "ENERĢIJAS NEZŪDAMĪBA SILTUMA PROCESOS",
             "Q(atdotais) = Q(saņemtais)        c·m₁·(t₁ − t) = c·m₂·(t − t₂)",
             "Siltākais ķermenis atdod tieši tik enerģijas, cik saņem "
             "aukstākais, ja zudumu nav. Kopīgo temperatūru t sauc par "
             "maisījuma temperatūru.", GOLD),
            ("panelis", "KĀ RISINĀT BILANCES UZDEVUMU",
             ["1. Nosaki, kurš ķermenis atdod un kurš saņem siltumu.",
              "2. Pieraksti abus siltuma daudzumus ar Q = cmΔT.",
              "3. Pielīdzini tos un izsaki meklēto lielumu.",
              "4. Pārbaudi: kopīgajai temperatūrai jābūt starp abām "
              "sākuma temperatūrām."], NAVY),
        ]),
        ("LD1 «Siltuma māja» plāns", [
            ("tabula",
             ["Pētījuma daļa", "Mūsu izvēle", "Kāpēc tā"],
             [["Pētāmais jautājums", "Kā izolācija maina atdzišanu",
               "Var izmērīt"],
              ["Neatkarīgais", "Sienas materiāls", "To maināt"],
              ["Atkarīgais", "Temperatūra pēc laika", "To mēra"],
              ["Fiksētie", "Ūdens masa, sākuma T, telpa",
               "Godīgs salīdzinājums"]],
             [3.30, 3.60, 3.33]),
            ("panelis", "DATU TABULA UN DROŠĪBA",
             ["Tabulā ieraksta laiku ik pēc 2 minūtēm un temperatūru "
              "katram modelim; mēra vismaz 20 minūtes.",
              "Katram mērījumam pieraksta arī apstākļus: telpas "
              "temperatūru, ūdens masu un modeļa izmēru.",
              "Drošība: karsts ūdens: lej uzmanīgi, termometru tur "
              "traukā, nevis rokā, un darbu veic uz paliktņa."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Maisījuma temperatūra",
             teksts="Sajauc 2,0 kg ūdens ar 80 °C un 3,0 kg ūdens ar\n"
                    "20 °C. Kāda būs kopīgā temperatūra?",
             dots=["m₁ = 2,0 kg;  t₁ = 80 °C",
                   "m₂ = 3,0 kg;  t₂ = 20 °C"],
             jaaprekina=["t = ?"],
             formulas=["Q(atdotais) = Q(saņemtais)",
                       "m₁(t₁ − t) = m₂(t − t₂)"],
             aprekins=["1)  2,0 · (80 − t) = 3,0 · (t − 20)",
                       "2)  160 − 2t = 3t − 60",
                       "3)  220 = 5t;  t = 44 °C"],
             atbilde="t = 44 °C",
             piezime="Pārbaude: 44 °C ir starp 20 un 80 - un tuvāk "
                     "lielākajai masai."),
        dict(nr=2, virsraksts="Atdotais siltums",
             teksts="1,0 kg ūdens atdziest no 90 °C līdz 45 °C.\n"
                    "Cik siltuma tas atdeva? (c = 4200 J/(kg·K))",
             dots=["m = 1,0 kg", "t₁ = 90 °C", "t₂ = 45 °C",
                   "c = 4200 J/(kg·K)"],
             jaaprekina=["Q = ?"],
             formulas=["Q = cmΔT", "ΔT = t₁ − t₂"],
             aprekins=["1)  ΔT = 90 − 45 = 45 K",
                       "2)  Q = 4200 · 1,0 · 45",
                       "3)  Q = 189 000 J"],
             atbilde="Q = 1,89·10⁵ J",
             piezime="Šo enerģiju saņēma apkārtējais gaiss un trauks - "
                     "tāpēc reālā bilancē ir zudumi."),
        dict(nr=3, virsraksts="Godīgs salīdzinājums",
             teksts="Divi modeļi: vienā 300 g ūdens, otrā 500 g.\n"
                    "Vai atdzišanas līknes var salīdzināt?\n"
                    "Ko vajadzētu mainīt?",
             dots=["m₁ = 300 g", "m₂ = 500 g",
                   "Pārējie apstākļi vienādi"],
             jaaprekina=["Vai salīdzinājums godīgs?"],
             formulas=["Q = cmΔT",
                       "Fiksētajiem lielumiem jāsakrīt"],
             aprekins=["1)  Masa ietekmē atdzišanas ātrumu",
                       "2)  Mainās divi lielumi vienlaikus",
                       "3)  Jāizmanto vienāda ūdens masa"],
             atbilde="Nav godīgs - masai jābūt vienādai",
             piezime="Pētījumā vienlaikus drīkst mainīt tikai vienu "
                     "lielumu - pārējie ir fiksētie."),
        dict(nr=4, virsraksts="Atdzišanas ātrums",
             teksts="Modelī ūdens 20 minūtēs atdziest no 60 °C līdz\n"
                    "42 °C. Aprēķini vidējo atdzišanas ātrumu grādos\n"
                    "minūtē!",
             dots=["t₁ = 60 °C", "t₂ = 42 °C", "τ = 20 min"],
             jaaprekina=["v = ?"],
             formulas=["ΔT = t₁ − t₂", "v = ΔT/τ"],
             aprekins=["1)  ΔT = 60 − 42 = 18 K",
                       "2)  v = 18 : 20",
                       "3)  v = 0,90 grādi minūtē"],
             atbilde="v = 0,90 °C/min",
             piezime="Šis skaitlis ir ērts modeļu salīdzināšanai - jo "
                     "mazāks, jo labāka izolācija."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Siltuma bilance: cik viens atdod, tik otrs saņem.",
            "Maisījuma temperatūra vienmēr ir starp abām sākuma "
            "temperatūrām.",
            "Godīgā pētījumā maina tikai vienu lielumu.",
            "Datus reģistrē tabulā regulāri un pieraksta apstākļus.",
        ],
        majasdarbs=[
            "Sajauc 1,0 kg ar 70 °C un 1,0 kg ar 30 °C. Aprēķini t.",
            "Sagatavo LD1 datu tabulu ar 11 rindām (ik pēc 2 min).",
            "Pieraksti savu pētāmo jautājumu un fiksētos lielumus.",
        ],
        pasvertejums=["Protu rakstīt bilances vienādojumu",
                      "Protu rēķināt maisījuma temperatūru",
                      "Zinu mainīgo veidus",
                      "Esmu sagatavojis datu tabulu"],
        nakama="Nākamā stunda: LD1 «Siltuma māja» - mērījumi "
               "dubultstundā."),
),

]
