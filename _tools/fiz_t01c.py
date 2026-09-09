# -*- coding: utf-8 -*-
"""1. temats. C daļa: 1.14.-1.19. stunda (relatīvā kustība, nostiprināšana)."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t01a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="1.14", virsraksts="Relatīvā kustība",
    jautajums="Cik ātri iet cilvēks kustīgā vilcienā?",
    apaksraksts="Ātrumu saskaitīšana · v⃗ = v⃗₁ + v⃗₂ · Straume un vējš",
    merkis="Iemācīties saskaitīt ātrumus dažādās atskaites sistēmās un "
           "risināt uzdevumus par kustību straumē vai vējā.",
    protu=["saskaitīt ātrumus vienā un pretējos virzienos;",
           "risināt uzdevumus par laivu straumē;",
           "lietot Pitagora teorēmu perpendikulāriem ātrumiem;",
           "norādīt, pret ko ātrums ir mērīts."],
    atkartojums="1.5. stundā: kustība ir relatīva. Tagad iemācīsimies to "
                "izteikt skaitliski - ar ātrumu saskaitīšanu.",
    uzdevumu_apraksts="Ātrumu saskaitīšana straumē, vējā un transportā",
    teorija=[
        ("Ātrumu saskaitīšanas likums", [
            ("formula", "KLASISKAIS LIKUMS",
             "v⃗(pret zemi) = v⃗(pret vidi) + v⃗(vides pret zemi)",
             "Ātrumi ir vektori, tāpēc tos saskaita vektoriāli. Vienā "
             "virzienā - moduļus saskaita, pretēji - atņem.", GOLD),
            ("kartitas", [
                ("PA STRAUMI", GREEN,
                 ["v = v(laivas) + v(straumes)",
                  "Ātrāk nekā stāvošā ūdenī."]),
                ("PRET STRAUMI", RED,
                 ["v = v(laivas) − v(straumes)",
                  "Ja straume stiprāka - nekustas uz priekšu."]),
                ("ŠĶĒRSĀM", BLUE,
                 ["v = √(v₁² + v₂²)",
                  "Laivu aiznes uz leju."]),
            ]),
        ]),
        ("Tipiskas situācijas", [
            ("tabula",
             ["Situācija", "Ātrums pret zemi", "Piemērs"],
             [["Iet vilcienā uz priekšu", "v(vilc.) + v(cilv.)",
               "20 + 1,5 = 21,5 m/s"],
              ["Iet vilcienā atpakaļ", "v(vilc.) − v(cilv.)",
               "20 − 1,5 = 18,5 m/s"],
              ["Lidmašīna pretvējā", "v(lidm.) − v(vēja)",
               "250 − 30 = 220 m/s"],
              ["Laiva šķērso upi", "√(v₁² + v₂²)",
               "√(4² + 3²) = 5 m/s"]],
             [4.90, 4.60, 3.83]),
            ("panelis", "VIENMĒR NORĀDI, PRET KO",
             ["Fizikā apgalvojums «ātrums 5 m/s» ir nepilnīgs. Pareizi: "
              "«ātrums 5 m/s pret krastu» vai «pret ūdeni». Eksāmenā par "
              "trūkstošu norādi zaudē punktus."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Cilvēks vilcienā",
             teksts="Vilciens brauc 72 km/h. Pasažieris iet pa vagonu\n"
                    "1,5 m/s braukšanas virzienā. Cik liels ir viņa "
                    "ātrums\npret zemi?",
             dots=["v₁ = 72 km/h = 20 m/s", "v₂ = 1,5 m/s"],
             jaaprekina=["v = ?"],
             formulas=["v = v₁ + v₂  (viens virziens)"],
             aprekins=["1)  v₁ = 72 : 3,6 = 20 m/s",
                       "2)  v = 20 + 1,5",
                       "3)  v = 21,5 m/s"],
             atbilde="v = 21,5 m/s ≈ 77 km/h pret zemi",
             piezime="Ja ietu pretējā virzienā, būtu 18,5 m/s."),
        dict(nr=2, virsraksts="Laiva pa straumi un pret to",
             teksts="Laivas ātrums stāvošā ūdenī ir 5,0 m/s, straumes\n"
                    "ātrums 2,0 m/s. Aprēķini ātrumu pa straumi un pret "
                    "to!",
             dots=["v(l) = 5,0 m/s", "v(s) = 2,0 m/s"],
             jaaprekina=["v(pa) = ?", "v(pret) = ?"],
             formulas=["v(pa) = v(l) + v(s)", "v(pret) = v(l) − v(s)"],
             aprekins=["1)  v(pa) = 5,0 + 2,0 = 7,0 m/s",
                       "2)  v(pret) = 5,0 − 2,0 = 3,0 m/s",
                       "3)  Attiecība 7 : 3"],
             atbilde="v(pa) = 7,0 m/s ;   v(pret) = 3,0 m/s",
             piezime="Tāpēc atpakaļceļš pret straumi aizņem vairāk laika."),
        dict(nr=3, virsraksts="Upes šķērsošana",
             teksts="Laiva ar ātrumu 4,0 m/s brauc perpendikulāri "
                    "krastam.\nStraumes ātrums 3,0 m/s. Aprēķini ātrumu "
                    "pret krastu\nun laiku 80 m platas upes šķērsošanai!",
             dots=["v₁ = 4,0 m/s", "v₂ = 3,0 m/s", "d = 80 m"],
             jaaprekina=["v = ?", "t = ?"],
             formulas=["v = √(v₁² + v₂²)", "t = d / v₁"],
             aprekins=["1)  v = √(16 + 9) = √25 = 5,0 m/s",
                       "2)  Šķērsošanas laiku nosaka tikai v₁",
                       "3)  t = 80 : 4,0 = 20 s"],
             atbilde="v = 5,0 m/s ;   t = 20 s",
             piezime="Straume laivu aiznes 60 m uz leju, bet laiku "
                     "nemaina."),
        dict(nr=4, virsraksts="Lidmašīna vējā",
             teksts="Lidmašīnas ātrums pret gaisu ir 800 km/h.\n"
                    "Pretvējš 60 km/h. Cik ilgi tā lidos 1480 km?",
             dots=["v₁ = 800 km/h", "v₂ = 60 km/h (pretī)", "s = 1480 km"],
             jaaprekina=["v = ?", "t = ?"],
             formulas=["v = v₁ − v₂", "t = s / v"],
             aprekins=["1)  v = 800 − 60 = 740 km/h",
                       "2)  t = 1480 : 740",
                       "3)  t = 2,0 h"],
             atbilde="v = 740 km/h ;   t = 2,0 h",
             piezime="Ar aizmugures vēju tas pats lidojums prasītu "
                     "1,7 h."),
        dict(nr=5, virsraksts="Divi vilcieni satiekas",
             teksts="Divi vilcieni ar garumiem 150 m un 250 m brauc "
                    "pretim\nviens otram ar 20 m/s un 15 m/s. Cik ilgi "
                    "tie brauc\ngarām viens otram?",
             dots=["l₁ = 150 m", "l₂ = 250 m", "v₁ = 20 m/s",
                   "v₂ = 15 m/s"],
             jaaprekina=["v(rel) = ?", "t = ?"],
             formulas=["v(rel) = v₁ + v₂", "s = l₁ + l₂", "t = s/v(rel)"],
             aprekins=["1)  v(rel) = 20 + 15 = 35 m/s",
                       "2)  s = 150 + 250 = 400 m",
                       "3)  t = 400 : 35 ≈ 11,4 s"],
             atbilde="t ≈ 11 s",
             piezime="Pretimbraucot ātrumus saskaita - tāpēc garāmbrauk"
                     "šana notiek tik ātri."),
        dict(nr=6, virsraksts="Cilvēks uz eskalatora",
             teksts="Eskalators kustas ar 0,50 m/s, cilvēks pa to iet "
                    "ar\n0,80 m/s. Cik ilgā laikā viņš veic 39 m garo "
                    "eskalatoru?",
             dots=["v₁ = 0,50 m/s", "v₂ = 0,80 m/s", "s = 39 m"],
             jaaprekina=["v = ?", "t = ?"],
             formulas=["v = v₁ + v₂", "t = s / v"],
             aprekins=["1)  v = 0,50 + 0,80 = 1,30 m/s",
                       "2)  t = 39 : 1,30",
                       "3)  t = 30 s"],
             atbilde="t = 30 s",
             piezime="Stāvot uz vietas, ceļš prasītu 78 s - gandrīz "
                     "trīs reizes ilgāk."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ātrumus saskaita vektoriāli: v⃗ = v⃗₁ + v⃗₂.",
            "Vienā virzienā - saskaita; pretēji - atņem.",
            "Perpendikulāri - Pitagora teorēma.",
            "Ātrumam vienmēr jānorāda atskaites ķermenis.",
        ],
        majasdarbs=[
            "Eskalators kustas 0,80 m/s, cilvēks iet 1,2 m/s. Cik ātri "
            "viņš kustas pret zemi?",
            "Laiva 6,0 m/s, straume 1,5 m/s. Aprēķini abus ātrumus.",
            "Upe 120 m plata, laiva 3,0 m/s perpendikulāri, straume "
            "4,0 m/s. Aprēķini v un t.",
        ],
        pasvertejums=["Protu saskaitīt ātrumus",
                      "Protu risināt straumes uzdevumus",
                      "Protu lietot Pitagora teorēmu",
                      "Protu norādīt atskaites sistēmu"],
        nakama="Nākamā stunda: kustības uzdevumi."),
),

dict(
    nr="1.15", virsraksts="Kustības uzdevumi",
    jautajums="Kā risināt uzdevumu par diviem ķermeņiem?",
    apaksraksts="Risinājuma soļi · Zīmējums · Pārbaude",
    merkis="Nostiprināt vienmērīgas kustības uzdevumu risināšanu pēc "
           "vienota soļu plāna, kas der arī eksāmenā.",
    protu=["sadalīt uzdevumu soļos;",
           "izvēlēties asi un pierakstīt vienādojumus;",
           "risināt uzdevumus ar diviem ķermeņiem;",
           "pārbaudīt atbildes ticamību."],
    atkartojums="Šajā stundā apvienojam visu apgūto: v = s/t, "
                "x = x₀ + vt, satikšanās nosacījumu un vidējo ātrumu.",
    uzdevumu_apraksts="Kombinēti uzdevumi par vienmērīgu kustību",
    teorija=[
        ("Universāls risinājuma plāns", [
            ("panelis", "SEŠI SOĻI",
             ["1) Izlasi un uzzīmē situāciju.  2) Pieraksti «Dots» SI "
              "vienībās.  3) Nosaki, kas jāaprēķina.  4) Izvēlies formulas "
              "un asi.  5) Rēķini pa soļiem ar mērvienībām.  6) Pārbaudi "
              "ticamību un pieraksti atbildi."], NAVY),
            ("kartitas", [
                ("ZĪMĒJUMS", BLUE,
                 ["Ass, sākumpunkts, virzieni.",
                  "Bez zīmējuma zīmes bieži sajūk."]),
                ("MĒRVIENĪBAS", GOLD,
                 ["Vispirms uz SI.",
                  "km/h : 3,6 = m/s"]),
                ("PĀRBAUDE", GREEN,
                 ["Vai skaitlis reāls?",
                  "Vai mērvienība pareiza?"]),
            ]),
        ]),
        ("Biežākās kļūdas", [
            ("tabula",
             ["Kļūda", "Kā izpaužas", "Kā izvairīties"],
             [["Sajauktas vienības", "km un m vienā formulā",
               "Vispirms viss uz SI"],
              ["Nepareiza zīme", "Atbilde ar mīnusu",
               "Uzzīmē asi un virzienus"],
              ["Vidējais aritmētiskais", "v(vid) = (v₁+v₂)/2",
               "Vienmēr s(kop)/t(kop)"],
              ["Nav mērvienības", "Atbilde «25»",
               "Mērvienība katrā solī"]],
             [4.30, 4.90, 4.13]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Divi posmi ar starpstāvēšanu",
             teksts="Autobuss 40 min brauc ar 54 km/h, 10 min stāv, tad\n"
                    "30 min brauc ar 72 km/h. Aprēķini kopējo ceļu un "
                    "vidējo ātrumu!",
             dots=["v₁ = 54 km/h = 15 m/s, t₁ = 2400 s",
                   "t₂ = 600 s, v₂ = 0",
                   "v₃ = 72 km/h = 20 m/s, t₃ = 1800 s"],
             jaaprekina=["s = ?", "v(vid) = ?"],
             formulas=["s = v·t", "v(vid) = s(kop)/t(kop)"],
             aprekins=["1)  s₁ = 15 · 2400 = 36 000 m",
                       "2)  s₃ = 20 · 1800 = 36 000 m ;  s = 72 000 m",
                       "3)  t = 4800 s ;  v(vid) = 72 000 : 4800 = 15 m/s"],
             atbilde="s = 72 km ;   v(vid) = 15 m/s = 54 km/h",
             piezime="Stāvēšanas laiks samazina vidējo ātrumu."),
        dict(nr=2, virsraksts="Satikšanās ar nobīdi laikā",
             teksts="No A izbrauc velosipēdists ar 15 km/h. Pēc 1,0 h no "
                    "A\ntajā pašā virzienā izbrauc motociklists ar "
                    "45 km/h.\nPēc cik ilga laika viņš panāks "
                    "velosipēdistu?",
             dots=["v₁ = 15 km/h", "v₂ = 45 km/h", "Δt = 1,0 h"],
             jaaprekina=["t = ?", "s = ?"],
             formulas=["L = v₁·Δt", "t = L/(v₂ − v₁)"],
             aprekins=["1)  L = 15 · 1,0 = 15 km",
                       "2)  Δv = 45 − 15 = 30 km/h",
                       "3)  t = 15 : 30 = 0,50 h ;  s = 45 · 0,50 = "
                       "22,5 km"],
             atbilde="t = 0,50 h ;   panāk 22,5 km no A.",
             piezime="Pārbaude: velosipēdists 1,5 h · 15 = 22,5 km ✔"),
        dict(nr=3, virsraksts="No grafika uz aprēķinu",
             teksts="Grafikā v(t): 0-10 s ātrums 8,0 m/s; 10-20 s ātrums\n"
                    "0; 20-40 s ātrums 4,0 m/s. Aprēķini ceļu un vidējo "
                    "ātrumu!",
             dots=["v₁ = 8,0 m/s, t₁ = 10 s", "v₂ = 0, t₂ = 10 s",
                   "v₃ = 4,0 m/s, t₃ = 20 s"],
             jaaprekina=["s = ?", "v(vid) = ?"],
             formulas=["s = laukums zem v(t)", "v(vid) = s/t"],
             aprekins=["1)  s₁ = 8,0 · 10 = 80 m ;  s₂ = 0",
                       "2)  s₃ = 4,0 · 20 = 80 m ;  s = 160 m",
                       "3)  v(vid) = 160 : 40 = 4,0 m/s"],
             atbilde="s = 160 m ;   v(vid) = 4,0 m/s",
             piezime="Grafiku sadala vienkāršās figūrās un summē "
                     "laukumus."),
        dict(nr=4, virsraksts="Vilciens un tilts",
             teksts="Vilciens ar garumu 240 m brauc 20 m/s un šķērso "
                    "360 m\ngaru tiltu. Cik ilgi vilciens atrodas uz "
                    "tilta?",
             dots=["l = 240 m", "L = 360 m", "v = 20 m/s"],
             jaaprekina=["t = ?"],
             formulas=["s = L + l", "t = s/v"],
             aprekins=["1)  Vilcienam jāveic tilta garums PLUS savs "
                       "garums",
                       "2)  s = 360 + 240 = 600 m",
                       "3)  t = 600 : 20 = 30 s"],
             atbilde="t = 30 s",
             piezime="Klasiska slazda situācija - ķermeņa izmērus "
                     "ignorēt nedrīkst."),
        dict(nr=5, virsraksts="Kolonnas apdzīšana",
             teksts="Motociklists ar 20 m/s apdzen 180 m garu kolonnu, "
                    "kas\nbrauc ar 15 m/s. Cik ilgi ilgst apdzīšana un "
                    "cik lielu\nceļu motociklists veic?",
             dots=["v₁ = 20 m/s", "v₂ = 15 m/s", "L = 180 m"],
             jaaprekina=["t = ?", "s = ?"],
             formulas=["v(rel) = v₁ − v₂", "t = L/v(rel)", "s = v₁·t"],
             aprekins=["1)  v(rel) = 20 − 15 = 5,0 m/s",
                       "2)  t = 180 : 5,0 = 36 s",
                       "3)  s = 20 · 36 = 720 m"],
             atbilde="t = 36 s ;   s = 720 m",
             piezime="Apdzīšanai vajadzīgs gandrīz kilometrs ceļa - "
                     "tāpēc to nedrīkst sākt pirms līkuma."),
        dict(nr=6, virsraksts="Laiva turp un atpakaļ",
             teksts="Laivas ātrums stāvošā ūdenī ir 8,0 km/h, straumes "
                    "ātrums\n2,0 km/h. Laiva veic 15 km pa straumi un "
                    "atgriežas.\nAprēķini kopējo laiku un vidējo ātrumu!",
             dots=["v(l) = 8,0 km/h", "v(s) = 2,0 km/h", "s₁ = 15 km"],
             jaaprekina=["t = ?", "v(vid) = ?"],
             formulas=["v(pa) = 10 km/h ;  v(pret) = 6,0 km/h",
                       "t = s/v", "v(vid) = s(kop)/t"],
             aprekins=["1)  t₁ = 15 : 10 = 1,5 h",
                       "2)  t₂ = 15 : 6,0 = 2,5 h ;  t = 4,0 h",
                       "3)  v(vid) = 30 : 4,0 = 7,5 km/h"],
             atbilde="t = 4,0 h ;   v(vid) = 7,5 km/h",
             piezime="Vidējais ātrums ir MAZĀKS par 8,0 km/h, kaut gan "
                     "straume vienā virzienā palīdzēja."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Uzdevumu risina pēc sešiem soļiem, sākot ar zīmējumu.",
            "Vispirms visu pārveido SI vienībās.",
            "Grafiku sadala vienkāršās figūrās.",
            "Ķermeņa garumu ignorē tikai tad, ja tas ir pamatoti.",
        ],
        majasdarbs=[
            "Autobuss 25 min ar 60 km/h, 5 min stāv, 30 min ar 80 km/h. "
            "Aprēķini s un v(vid).",
            "Vilciens 180 m garš, v = 15 m/s, tunelis 320 m. Cik ilgi "
            "tas ir tunelī?",
            "Divi ķermeņi 90 m attālumā brauc pretim ar 4,0 un 5,0 m/s. "
            "Kad satiksies?",
        ],
        pasvertejums=["Protu lietot risinājuma soļus",
                      "Protu strādāt ar diviem ķermeņiem",
                      "Protu lasīt v(t) grafiku",
                      "Protu pārbaudīt ticamību"],
        nakama="Nākamā stunda: grafiku un vienādojumu nostiprināšana."),
),

dict(
    nr="1.16", virsraksts="Grafiku un vienādojumu nostiprināšana",
    jautajums="Kā no grafika uzrakstīt vienādojumu?",
    apaksraksts="Grafiks → vienādojums → aprēķins",
    merkis="Nostiprināt pāreju starp trim kustības aprakstiem: vārdiem, "
           "grafiku un vienādojumu.",
    protu=["no x(t) grafika uzrakstīt vienādojumu;",
           "no vienādojuma uzzīmēt grafiku;",
           "pārveidot x(t) grafiku par v(t) grafiku;",
           "aprakstīt kustību vārdiem pēc grafika."],
    atkartojums="Kustību var aprakstīt trīs veidos: ar vārdiem, ar "
                "grafiku un ar vienādojumu. Eksāmenā jāprot pāriet no "
                "viena uz otru.",
    uzdevumu_apraksts="Pārejas starp grafiku, vienādojumu un aprakstu",
    teorija=[
        ("Trīs apraksta veidi", [
            ("kartitas", [
                ("VĀRDIEM", GREY,
                 ["«Brauc 20 m/s no punkta 50 m pretēji asij.»",
                  "Saprotams, bet neprecīzs."]),
                ("GRAFIKS", BLUE,
                 ["Redzams uzreiz viss brauciens.",
                  "Slīpums = ātrums."]),
                ("VIENĀDOJUMS", GREEN,
                 ["x = 50 − 20t",
                  "Der aprēķinam jebkurā brīdī."]),
            ]),
            ("formula", "PĀREJA GRAFIKS → VIENĀDOJUMS",
             "x₀ - grafika krustpunkts ar x asi;  "
             "vₓ = (x₂ − x₁)/(t₂ − t₁) - slīpums",
             "Divus punktus izvēlas tur, kur līnija krusto rūtiņu "
             "stūrus - tad nolasījums ir precīzs.", GOLD),
        ]),
        ("No x(t) uz v(t)", [
            ("tabula",
             ["x(t) grafikā", "v(t) grafikā", "Kustība"],
             [["Augoša taisne", "Pozitīva horizontāla", "Uz priekšu"],
              ["Dilstoša taisne", "Negatīva horizontāla", "Atpakaļ"],
              ["Horizontāla", "v = 0 (uz ass)", "Miers"],
              ["Stāvāka taisne", "Tālāk no ass", "Ātrāk"]],
             [4.60, 4.60, 4.13]),
            ("panelis", "PĀRBAUDES JAUTĀJUMI",
             ["Vai grafiks sākas virs vai zem nulles? Vai tas aug vai "
              "dilst? Cik stāvs tas ir? Vai ir posmi bez kustības? "
              "Atbildes uz šiem četriem jautājumiem dod visu "
              "vienādojumu."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Grafiks → vienādojums",
             teksts="x(t) taisne iet caur (0 s; −10 m) un (5 s; 15 m).\n"
                    "Uzraksti vienādojumu un aprēķini x pēc 12 s!",
             dots=["(0; −10)", "(5; 15)", "t = 12 s"],
             jaaprekina=["x(t) = ?", "x(12 s) = ?"],
             formulas=["vₓ = Δx/Δt", "x = x₀ + vₓt"],
             aprekins=["1)  vₓ = (15 − (−10)) : 5 = 25 : 5 = 5,0 m/s",
                       "2)  x = −10 + 5t",
                       "3)  x(12) = −10 + 60 = 50 m"],
             atbilde="x = −10 + 5t  (m; s) ;   x(12 s) = 50 m",
             piezime="Negatīva x₀ nozīmē, ka kustība sākas pa kreisi no "
                     "sākumpunkta."),
        dict(nr=2, virsraksts="Vienādojums → apraksts",
             teksts="x = 80 − 16t  (m; s).\n"
                    "Apraksti kustību vārdiem un nosaki, kad ķermenis "
                    "būs punktā x = 0!",
             dots=["x = 80 − 16t"],
             jaaprekina=["apraksts = ?", "t (x=0) = ?"],
             formulas=["x = x₀ + vₓt", "0 = 80 − 16t"],
             aprekins=["1)  x₀ = 80 m ;  vₓ = −16 m/s",
                       "2)  Kustība pretēji asij ar 16 m/s",
                       "3)  16t = 80 → t = 5,0 s"],
             atbilde="Sākas 80 m atzīmē, kustas pretēji asij ar 16 m/s; "
                     "sākumpunktā ir pēc 5,0 s.",
             piezime="Vienādojums der arī negatīvām koordinātām - pēc "
                     "5 s ķermenis turpina uz mīnusa pusi."),
        dict(nr=3, virsraksts="x(t) → v(t)",
             teksts="x(t) grafikā: 0-4 s taisne no 0 līdz 24 m;\n"
                    "4-8 s horizontāla; 8-12 s taisne no 24 m līdz 0.\n"
                    "Uzzīmē v(t) grafiku un nosaki ātrumus!",
             dots=["3 posmi pa 4 s"],
             jaaprekina=["v₁, v₂, v₃ = ?"],
             formulas=["v = Δx/Δt"],
             aprekins=["1)  v₁ = 24 : 4 = 6,0 m/s",
                       "2)  v₂ = 0 (horizontāla taisne)",
                       "3)  v₃ = (0 − 24) : 4 = −6,0 m/s"],
             atbilde="v₁ = 6,0 m/s ;  v₂ = 0 ;  v₃ = −6,0 m/s",
             piezime="v(t) grafikā tie ir trīs horizontāli posmi: virs "
                     "ass, uz ass, zem ass."),
        dict(nr=4, virsraksts="Ceļš un pārvietojums no grafika",
             teksts="Izmantojot 3. uzdevuma grafiku, aprēķini kopējo "
                    "ceļu\nun pārvietojumu 12 sekundēs!",
             dots=["s₁ = 24 m", "s₂ = 0", "s₃ = 24 m"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = Σ|Δx|", "dₓ = x(beigu) − x(sākuma)"],
             aprekins=["1)  s = 24 + 0 + 24 = 48 m",
                       "2)  x(0) = 0 ;  x(12) = 0",
                       "3)  dₓ = 0 − 0 = 0"],
             atbilde="s = 48 m ;   |d⃗| = 0 m",
             piezime="Ķermenis atgriezās sākumā - tāda pati situācija kā "
                     "1.6. stundā."),
        dict(nr=5, virsraksts="Satikšanās no vienādojumiem",
             teksts="x₁ = 12t un x₂ = 300 − 8t  (m; s).\n"
                    "Atrodi satikšanās laiku un vietu, kā arī attālumu "
                    "starp\nķermeņiem pēc 10 s!",
             dots=["x₁ = 12t", "x₂ = 300 − 8t", "t = 10 s"],
             jaaprekina=["t(sat) = ?", "x = ?", "Δx(10 s) = ?"],
             formulas=["x₁ = x₂", "Δx = x₂ − x₁"],
             aprekins=["1)  12t = 300 − 8t → 20t = 300 → t = 15 s",
                       "2)  x = 12 · 15 = 180 m",
                       "3)  Δx(10) = (300 − 80) − 120 = 100 m"],
             atbilde="Satiekas pēc 15 s punktā x = 180 m; pēc 10 s "
                     "attālums ir 100 m.",
             piezime="Pārbaude: x₂(15) = 300 − 120 = 180 m ✔"),
        dict(nr=6, virsraksts="No v(t) uz x(t)",
             teksts="Ķermenis sāk kustību no x₀ = 10 m, un v(t) grafikā\n"
                    "vₓ = 5,0 m/s ir nemainīgs. Uzraksti x(t) un aprēķini "
                    "ceļu\nun koordinātu pēc 8,0 s!",
             dots=["x₀ = 10 m", "vₓ = 5,0 m/s", "t = 8,0 s"],
             jaaprekina=["x(t) = ?", "s = ?", "x(8,0 s) = ?"],
             formulas=["x = x₀ + vₓt", "s = |vₓ|·t"],
             aprekins=["1)  x = 10 + 5t  (m; s)",
                       "2)  s = 5,0 · 8,0 = 40 m",
                       "3)  x = 10 + 40 = 50 m"],
             atbilde="x = 10 + 5t ;   s = 40 m ;   x(8,0 s) = 50 m",
             piezime="Ceļš un koordināta nav viens un tas pats - tos "
                     "atšķir sākuma koordināta."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Kustību var aprakstīt vārdiem, ar grafiku un ar vienādojumu.",
            "x(t) grafika slīpums ir ātrums; krustpunkts ar asi - x₀.",
            "x(t) horizontāls posms nozīmē mieru.",
            "Ceļu skaita kā koordinātas izmaiņu moduļu summu.",
        ],
        majasdarbs=[
            "x(t) iet caur (0; 30) un (6; 6). Uzraksti vienādojumu.",
            "x = −20 + 8t. Apraksti kustību un uzzīmē grafiku 0-6 s.",
            "Uzzīmē v(t) grafiku kustībai: 5 s uz priekšu 4 m/s, 5 s "
            "miers, 5 s atpakaļ 2 m/s.",
        ],
        pasvertejums=["Protu no grafika uzrakstīt vienādojumu",
                      "Protu no vienādojuma uzzīmēt grafiku",
                      "Protu pāriet no x(t) uz v(t)",
                      "Protu aprēķināt ceļu no grafika"],
        nakama="Nākamā stunda: kļūdas pētījumā."),
),

dict(
    nr="1.17", virsraksts="Kļūdas pētījumā",
    jautajums="Cik ticams ir mūsu rezultāts?",
    apaksraksts="Nejaušas · Sistemātiskas · Rupjas kļūdas",
    merkis="Iemācīties atšķirt kļūdu veidus, novērtēt rezultāta "
           "ticamību un piedāvāt konkrētus uzlabojumus.",
    protu=["atšķirt nejaušas, sistemātiskas un rupjas kļūdas;",
           "nosaukt, kā katru no tām samazina;",
           "novērtēt rezultāta ticamību;",
           "pamatot uzlabojumu ar skaitļiem."],
    atkartojums="1.11. stundā rēķinājām kļūdu skaitliski. Tagad "
                "saprotam, no kurienes tā rodas un ko ar to darīt.",
    uzdevumu_apraksts="Kļūdu veidu atpazīšana un ticamības novērtēšana",
    teorija=[
        ("Trīs kļūdu veidi", [
            ("kartitas", [
                ("NEJAUŠAS", BLUE,
                 ["Katrā mērījumā citādas.",
                  "Piemērs: reakcijas laiks.",
                  "Samazina: vairāk atkārtojumu."]),
                ("SISTEMĀTISKAS", RED,
                 ["Vienmēr vienā virzienā.",
                  "Piemērs: nekalibrēti svari.",
                  "Samazina: kalibrēšana, cita metode."]),
                ("RUPJAS", GOLD,
                 ["Pārrakstīšanās, nepareiza skala.",
                  "Piemērs: 2,64 s starp 1,8 s.",
                  "Samazina: pārbaude, atkārtošana."]),
            ]),
            ("panelis", "KĀ TĀS ATPAZĪT DATOS",
             ["Nejaušas kļūdas rada izkliedi ap vidējo vērtību. "
              "Sistemātiskas nobīda VISUS rezultātus vienā pusē - "
              "izkliede paliek maza, bet atbilde ir nepareiza. Tāpēc "
              "maza izkliede vēl nenozīmē precīzu rezultātu."], NAVY),
        ]),
        ("Precizitāte un pareizība", [
            ("divi",
             ("PRECĪZS", BLUE,
              ["Maza izkliede starp mērījumiem.",
               "Rezultāti atkārtojas.",
               "Ietekmē nejaušas kļūdas."]),
             ("PAREIZS", GREEN,
              ["Tuvu patiesajai vērtībai.",
               "Nav sistemātiskas nobīdes.",
               "Pārbauda ar tabulas vērtību."])),
            ("formula", "RELATĪVĀ NOVIRZE",
             "δ = |x(izmērītais) − x(tabulas)| / x(tabulas) · 100 %",
             "Skolas laboratorijā 1-5 % ir labs rezultāts, 5-10 % - "
             "pieņemams, virs 15 % - jāmeklē kļūdas cēlonis.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kļūdas veida noteikšana",
             teksts="Svari bez slodzes rāda 3 g. Visi ķermeņi izsvērti\n"
                    "ar šiem svariem. Kāda tā ir kļūda un kā to novērš?",
             dots=["nulles nobīde 3 g"],
             jaaprekina=["kļūdas veids = ?", "risinājums = ?"],
             formulas=["Vienā virzienā → sistemātiska"],
             aprekins=["1)  Visi rezultāti par 3 g lielāki",
                       "2)  Nobīde vienā virzienā → sistemātiska kļūda",
                       "3)  Novērš, noregulējot nulli vai atņemot 3 g"],
             atbilde="Sistemātiska kļūda; novērš ar svaru nullēšanu.",
             piezime="Atkārtojumi šeit nepalīdz - kļūda paliek."),
        dict(nr=2, virsraksts="Izkliedes novērtējums",
             teksts="Pieci laika mērījumi: 2,10; 2,14; 2,08; 2,12; 2,11 s.\n"
                    "Aprēķini vidējo un novērtē izkliedi!",
             dots=["5 mērījumi"],
             jaaprekina=["t(vid) = ?", "Δt = ?"],
             formulas=["t(vid) = Σt/n", "Δt ≈ (t(max) − t(min))/2"],
             aprekins=["1)  Σt = 10,55 s → t(vid) = 2,11 s",
                       "2)  t(max) − t(min) = 2,14 − 2,08 = 0,06 s",
                       "3)  Δt ≈ 0,03 s ;  δ = 0,03:2,11 ≈ 1,4 %"],
             atbilde="t = (2,11 ± 0,03) s ;   δ ≈ 1,4 %",
             piezime="Maza izkliede - mērījums ir precīzs. Vai tas ir "
                     "pareizs, tā vēl nepasaka."),
        dict(nr=3, virsraksts="Novirze no tabulas vērtības",
             teksts="Laboratorijā iegūts g = 9,42 m/s².\n"
                    "Aprēķini relatīvo novirzi no 9,81 m/s² un novērtē "
                    "rezultātu!",
             dots=["g(izm) = 9,42 m/s²", "g(tab) = 9,81 m/s²"],
             jaaprekina=["δ = ?"],
             formulas=["δ = |Δg|/g(tab) · 100 %"],
             aprekins=["1)  Δg = 9,81 − 9,42 = 0,39 m/s²",
                       "2)  δ = 0,39 : 9,81 · 100 %",
                       "3)  δ ≈ 4,0 %"],
             atbilde="δ ≈ 4,0 % - pieņemams skolas laboratorijai.",
             piezime="Ja visiem g iznāk par mazu, meklē sistemātisku "
                     "kļūdu, piemēram, nepareizi mērītu garumu."),
        dict(nr=4, virsraksts="Uzlabojuma pamatošana",
             teksts="Svārsta periodu mēra vienai svārstībai (t ≈ 2 s),\n"
                    "hronometra kļūda 0,2 s. Piedāvā uzlabojumu un\n"
                    "pamato to ar skaitļiem!",
             dots=["T ≈ 2 s", "Δt = 0,2 s"],
             jaaprekina=["δ pirms = ?", "δ pēc = ?"],
             formulas=["δ = Δt/t · 100 %"],
             aprekins=["1)  δ = 0,2 : 2 · 100 % = 10 %",
                       "2)  Mēra 20 svārstības: t = 40 s",
                       "3)  δ = 0,2 : 40 · 100 % = 0,5 %"],
             atbilde="Mērot 20 svārstības, relatīvā kļūda samazinās no "
                     "10 % līdz 0,5 % - 20 reižu.",
             piezime="Šis ir tipisks eksāmena jautājums par mērījuma "
                     "uzlabošanu."),
        dict(nr=5, virsraksts="Kļūdas veida atpazīšana",
             teksts="a) Hronometru palaiž ar roku;\n"
                    "b) lineālam nolauzts pirmais centimetrs;\n"
                    "c) mērlenta izstiepusies. Kāda kļūda katrā gadījumā?",
             dots=["trīs situācijas"],
             jaaprekina=["kļūdas veids katrā = ?"],
             formulas=["Nejauša mainās; sistemātiska - vienā virzienā"],
             aprekins=["1)  a) reakcijas laiks katru reizi citāds → "
                       "nejauša",
                       "2)  b) visi garumi par 1 cm mazāki → sistemātiska",
                       "3)  c) visi garumi par vienu daļu mazāki → "
                       "sistemātiska"],
             atbilde="a) nejauša;  b) un c) sistemātiskas.",
             piezime="Nejaušo samazina atkārtojumi, sistemātisko - tikai "
                     "ierīces pārbaude."),
        dict(nr=6, virsraksts="Precīzs vai pareizs",
             teksts="Mērījumi: 9,10; 9,12; 9,11 m/s² (tabulā "
                    "9,81 m/s²).\nNovērtē mērījuma precizitāti un "
                    "pareizību!",
             dots=["izkliede ≈ 0,01 m/s²", "g(tab) = 9,81 m/s²"],
             jaaprekina=["izkliede = ?", "novirze = ?"],
             formulas=["Δ = (max − min)/2", "δ = |Δg|/g(tab) · 100 %"],
             aprekins=["1)  Δ = (9,12 − 9,10) : 2 = 0,01 m/s²",
                       "2)  Δg = 9,81 − 9,11 = 0,70 m/s²",
                       "3)  δ = 0,70 : 9,81 · 100 % ≈ 7 %"],
             atbilde="Mērījums ir precīzs (maza izkliede), bet nav "
                     "pareizs - ir sistemātiska kļūda ~7 %.",
             piezime="Precizitāte un pareizība ir divas dažādas lietas - "
                     "to bieži jautā eksāmenā."),
        dict(nr=7, virsraksts="Kļūdu avotu saraksts",
             teksts="Lodītes vidējā ātruma darbā (LD1) nosauc trīs "
                    "kļūdu\navotus un vienu konkrētu uzlabojumu!",
             dots=["mēra s ar lineālu un t ar hronometru"],
             jaaprekina=["3 kļūdu avoti = ?", "uzlabojums = ?"],
             formulas=["δv = δs + δt"],
             aprekins=["1)  Reakcijas laiks palaižot un apturot "
                       "hronometru",
                       "2)  Neprecīzs renītes garuma mērījums un "
                       "starta vieta",
                       "3)  Uzlabojums: garāka renīte un 5 atkārtojumi"],
             atbilde="Galvenais avots - laika mērījums; uzlabojums: "
                     "garāks ceļš un vairāk atkārtojumu.",
             piezime="Vienmēr nosauc, KURŠ mērījums dod lielāko relatīvo "
                     "kļūdu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Nejaušas kļūdas rada izkliedi; samazina ar atkārtojumiem.",
            "Sistemātiskas kļūdas nobīda visus rezultātus vienā pusē.",
            "Rupjas kļūdas atpazīst pēc izlecošas vērtības.",
            "Precīzs nenozīmē pareizs.",
        ],
        majasdarbs=[
            "Nosauc pa vienam katra veida kļūdu piemēram LD1 darbā.",
            "Mērījumi: 5,2; 5,4; 5,3; 6,9; 5,3 cm. Kura vērtība ir "
            "aizdomīga un kāpēc?",
            "Iegūts ρ = 2,52 g/cm³ alumīnijam (2,70). Aprēķini δ.",
        ],
        pasvertejums=["Protu atšķirt kļūdu veidus",
                      "Protu novērtēt izkliedi",
                      "Protu aprēķināt novirzi",
                      "Protu pamatot uzlabojumu"],
        nakama="Nākamā stunda: temata nostiprināšana pirms PD2."),
),

dict(
    nr="1.18", virsraksts="Temata nostiprināšana",
    jautajums="Kā izvēlēties pareizo sakarību?",
    apaksraksts="Atgādne · Formulu izvēle · Eksāmena formāts",
    merkis="Apkopot visu temata saturu vienā atgādnē un nostiprināt "
           "prasmi izvēlēties pareizo sakarību pēc uzdevuma teksta.",
    protu=["izvēlēties formulu pēc dotajiem lielumiem;",
           "risināt kombinētus uzdevumus;",
           "pārbaudīt mērvienības un ticamību;",
           "sagatavoties PD2."],
    atkartojums="Šī ir pēdējā stunda pirms PD2. Apkopojam vektorus, "
                "ceļu un pārvietojumu, vienmērīgu kustību, grafikus, "
                "vidējo ātrumu un mērījumu kļūdas.",
    uzdevumu_apraksts="Kombinēti uzdevumi PD2 formātā",
    teorija=[
        ("Temata atgādne", [
            ("formula", "GALVENĀS SAKARĪBAS",
             "v = s/t   ·   x = x₀ + vₓt   ·   v(vid) = s(kop)/t(kop)   ·   "
             "|d⃗| = √(dₓ² + d_y²)   ·   δ = Δx/x · 100 %",
             "Katrai sakarībai jāzina, KAD to lieto: v = s/t tikai "
             "vienmērīgā kustībā, v(vid) - jebkurā.", GOLD),
            ("tabula",
             ["Ja dots...", "Un jāatrod...", "Lieto"],
             [["s un t (v nemainās)", "v", "v = s/t"],
              ["x₀, v, t", "x", "x = x₀ + vₓt"],
              ["Vairāki posmi", "v(vid)", "s(kop)/t(kop)"],
              ["Divi ķermeņi", "satikšanās", "x₁ = x₂"],
              ["Grafiks v(t)", "s", "laukums zem grafika"]],
             [4.60, 3.90, 4.83]),
        ]),
        ("Kā gatavoties PD2", [
            ("panelis", "PD2 SATURS UN FORMĀTS",
             ["Tests (10 p.) par jēdzieniem un grafikiem; mērvienību "
              "pārveidošana (5 p.); divi aprēķinu uzdevumi ar pilnu "
              "pierakstu (10 p.); uzdevums ar apakšjautājumiem par "
              "grafiku vai mērījumu (5 p.). Kopā 30 punkti, 40 minūtes."],
             NAVY),
            ("kartitas", [
                ("PIRMS DARBA", BLUE,
                 ["Atkārto mērvienību pārveidošanu.",
                  "Pārskati grafiku lasīšanu."]),
                ("DARBA LAIKĀ", GREEN,
                 ["Vispirms viegli uzdevumi.",
                  "Katram - Dots un mērvienības."]),
                ("BIEŽĀKĀS KĻŪDAS", RED,
                 ["km/h nav pārveidoti.",
                  "Vidējais aritmētiskais.",
                  "Trūkst mērvienības atbildē."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Formulas izvēle",
             teksts="Doti: x₀ = 24 m; vₓ = −6,0 m/s; t = 9,0 s.\n"
                    "Kuru sakarību lietosi un kāda ir atbilde?",
             dots=["x₀ = 24 m", "vₓ = −6,0 m/s", "t = 9,0 s"],
             jaaprekina=["x = ?"],
             formulas=["x = x₀ + vₓt"],
             aprekins=["1)  Dota sākuma koordināta un ātrums ar zīmi",
                       "2)  x = 24 + (−6,0)·9,0",
                       "3)  x = 24 − 54 = −30 m"],
             atbilde="x = −30 m (ķermenis ir pa kreisi no sākumpunkta).",
             piezime="Negatīva koordināta ir pilnīgi normāla atbilde."),
        dict(nr=2, virsraksts="Kombinēts uzdevums",
             teksts="Automašīna 15 min brauc ar 80 km/h, tad 45 min ar\n"
                    "40 km/h. Aprēķini ceļu un vidējo ātrumu m/s!",
             dots=["v₁ = 80 km/h, t₁ = 0,25 h", "v₂ = 40 km/h, t₂ = 0,75 h"],
             jaaprekina=["s = ?", "v(vid) = ?"],
             formulas=["s = v·t", "v(vid) = s/t"],
             aprekins=["1)  s₁ = 80·0,25 = 20 km ;  s₂ = 40·0,75 = 30 km",
                       "2)  s = 50 km ;  t = 1,0 h",
                       "3)  v(vid) = 50 km/h = 50:3,6 ≈ 13,9 m/s"],
             atbilde="s = 50 km ;   v(vid) ≈ 13,9 m/s",
             piezime="Vidējais aritmētiskais (60 km/h) būtu nepareizs."),
        dict(nr=3, virsraksts="Vektoru uzdevums",
             teksts="Kuģis nobrauc 60 km uz ziemeļiem un 80 km uz "
                    "austrumiem\n5,0 h laikā. Aprēķini ceļu, pārvietojumu "
                    "un\nvidējo ātrumu pēc pārvietojuma!",
             dots=["s₁ = 60 km", "s₂ = 80 km", "t = 5,0 h"],
             jaaprekina=["s = ?", "|d⃗| = ?", "v = ?"],
             formulas=["s = s₁ + s₂", "|d⃗| = √(s₁² + s₂²)",
                       "v = |d⃗|/t"],
             aprekins=["1)  s = 60 + 80 = 140 km",
                       "2)  |d⃗| = √(3600 + 6400) = √10 000 = 100 km",
                       "3)  v = 100 : 5,0 = 20 km/h ≈ 5,6 m/s"],
             atbilde="s = 140 km ;  |d⃗| = 100 km ;  v ≈ 5,6 m/s",
             piezime="Vidējais ātrums pēc ceļa būtu 28 km/h - atšķirība "
                     "ir būtiska."),
        dict(nr=4, virsraksts="Mērījums ar kļūdu",
             teksts="s = (25,0 ± 0,5) m; t = (5,0 ± 0,1) s.\n"
                    "Aprēķini ātrumu un tā relatīvo kļūdu!",
             dots=["s = 25,0 m, Δs = 0,5 m", "t = 5,0 s, Δt = 0,1 s"],
             jaaprekina=["v = ?", "δv = ?"],
             formulas=["v = s/t", "δv = δs + δt"],
             aprekins=["1)  v = 25,0 : 5,0 = 5,0 m/s",
                       "2)  δs = 2,0 % ;  δt = 2,0 %",
                       "3)  δv = 4,0 % → Δv = 0,2 m/s"],
             atbilde="v = (5,0 ± 0,2) m/s ;   δ = 4,0 %",
             piezime="Netiešā mērījumā relatīvās kļūdas vienmēr "
                     "saskaita."),
        dict(nr=5, virsraksts="Upes šķērsošana",
             teksts="Laiva šķērso 60 m platu upi perpendikulāri krastam "
                    "ar\n3,0 m/s; straumes ātrums 1,5 m/s. Aprēķini "
                    "šķērsošanas\nlaiku, aiznešanu un ātrumu pret "
                    "krastu!",
             dots=["d = 60 m", "v₁ = 3,0 m/s", "v₂ = 1,5 m/s"],
             jaaprekina=["t = ?", "s(aizn) = ?", "v = ?"],
             formulas=["t = d/v₁", "s = v₂·t", "v = √(v₁² + v₂²)"],
             aprekins=["1)  t = 60 : 3,0 = 20 s",
                       "2)  s = 1,5 · 20 = 30 m",
                       "3)  v = √(9,0 + 2,25) = √11,25 ≈ 3,4 m/s"],
             atbilde="t = 20 s ;  aiznes 30 m ;  v ≈ 3,4 m/s",
             piezime="Šķērsošanas laiku straume nemaina - to nosaka "
                     "tikai perpendikulārā projekcija."),
        dict(nr=6, virsraksts="Divi vienādojumi",
             teksts="x₁ = 2t un x₂ = 120 − 4t  (m; s).\n"
                    "Atrodi satikšanās laiku un vietu, kā arī attālumu\n"
                    "starp ķermeņiem pēc 30 s!",
             dots=["x₁ = 2t", "x₂ = 120 − 4t"],
             jaaprekina=["t = ?", "x = ?", "Δx(30 s) = ?"],
             formulas=["x₁ = x₂", "Δx = |x₂ − x₁|"],
             aprekins=["1)  2t = 120 − 4t → 6t = 120 → t = 20 s",
                       "2)  x = 2 · 20 = 40 m",
                       "3)  x₁(30) = 60 m ;  x₂(30) = 0 ;  Δx = 60 m"],
             atbilde="Satiekas pēc 20 s punktā x = 40 m; pēc 30 s "
                     "attālums ir 60 m.",
             piezime="Pēc satikšanās ķermeņi attālinās - tāpēc modulis "
                     "atkal aug."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Formulu izvēlas pēc tā, kas dots un kas jāatrod.",
            "v = s/t der tikai vienmērīgai kustībai.",
            "Vektoru uzdevumos ceļš un pārvietojums atšķiras.",
            "Netiešā mērījumā relatīvās kļūdas saskaita.",
        ],
        majasdarbs=[
            "Atkārto visu temata atgādni pirms PD2.",
            "Izpildi vienu uzdevumu no katra veida: mērvienības, "
            "grafiks, vidējais ātrums, kļūda.",
            "Pārskati LD1 protokolu un PR1 secinājumus.",
        ],
        pasvertejums=["Protu izvēlēties formulu",
                      "Protu risināt kombinētus uzdevumus",
                      "Protu strādāt ar kļūdām",
                      "Esmu gatavs PD2"],
        nakama="Nākamā stunda: PD2 - vienmērīga un nevienmērīga kustība."),
),

dict(
    nr="1.19", virsraksts="Kļūdu analīze",
    jautajums="Ko no pārbaudes darba mācāmies?",
    apaksraksts="Tipiskās kļūdas · Labošana · Atgādne nākamajam tematam",
    merkis="Analizēt PD2 kļūdas, izlabot tipiskākās un sagatavot "
           "personīgu atgādni nākamajam tematam.",
    protu=["atpazīt savu kļūdas veidu;",
           "izlabot risinājumu ar pareizu pierakstu;",
           "izskaidrot kļūdu citam skolēnam;",
           "sastādīt personīgu atgādni."],
    atkartojums="PD2 ir uzrakstīts. Šī stunda nav vērtējuma stunda - tā "
                "ir vieta, kur kļūdas pārvērst prasmē.",
    uzdevumu_apraksts="Kļūdainu risinājumu labošana",
    teorija=[
        ("Biežākās PD kļūdas", [
            ("tabula",
             ["Kļūda", "Kā izskatās", "Pareizi"],
             [["Nav pārveidotas vienības", "v = 90 : 2 = 45",
               "90 km/h = 25 m/s"],
              ["Vidējais aritmētiskais", "(40+60)/2 = 50 km/h",
               "s(kop)/t(kop) = 48 km/h"],
              ["Sajaukts s un |d⃗|", "Aplim |d⃗| = 2πR",
               "Aplim |d⃗| = 0"],
              ["Trūkst mērvienības", "Atbilde: 25",
               "Atbilde: v = 25 m/s"]],
             [4.60, 4.60, 4.13]),
            ("panelis", "KĀ LABOT PAREIZI",
             ["Nepietiek uzrakstīt pareizo atbildi. Jāpieraksta: kāda "
              "bija kļūda, kāpēc tā radās un kā to pamanīt nākamreiz. "
              "Tikai tad kļūda pārvēršas prasmē."], NAVY),
        ]),
        ("Personīgā atgādne", [
            ("kartitas", [
                ("KO PROTU", GREEN,
                 ["Uzdevumu veidi, kur nekļūdījos.",
                  "Tos atkārto reti."]),
                ("KO JĀNOSTIPRINA", GOLD,
                 ["Kļūdas dēļ neuzmanības.",
                  "Vajag 2-3 papildu uzdevumus."]),
                ("KAS NESKAIDRS", RED,
                 ["Nesapratu risinājumu.",
                  "Jautā skolotājam vai klasesbiedram."]),
            ]),
            ("formula", "NĀKAMAIS TEMATS",
             "2. temats: vienmērīgi paātrināta kustība",
             "Tur ātrums vairs nebūs nemainīgs. Viss, ko apguvām par "
             "grafikiem, ceļu un mērvienībām, būs vajadzīgs katrā "
             "stundā.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atrodi kļūdu I",
             teksts="Skolēna risinājums: «v = 108 km/h, t = 20 s,\n"
                    "s = 108 · 20 = 2160 m.»\nAtrodi un izlabo kļūdu!",
             dots=["v = 108 km/h", "t = 20 s"],
             jaaprekina=["s = ?", "kļūda = ?"],
             formulas=["Vispirms v uz m/s", "s = v·t"],
             aprekins=["1)  Kļūda: km/h reizināts ar sekundēm",
                       "2)  v = 108 : 3,6 = 30 m/s",
                       "3)  s = 30 · 20 = 600 m"],
             atbilde="s = 600 m; kļūda - nesaskaņotas mērvienības.",
             piezime="Atbilde 2160 m nozīmētu 2,2 km 20 sekundēs - "
                     "ticamības pārbaude to uzreiz atklāj."),
        dict(nr=2, virsraksts="Atrodi kļūdu II",
             teksts="«Pusi ceļa ar 30 km/h, pusi ar 60 km/h,\n"
                    "tātad v(vid) = (30 + 60)/2 = 45 km/h.»\n"
                    "Izlabo risinājumu!",
             dots=["v₁ = 30 km/h", "v₂ = 60 km/h", "vienādi ceļi"],
             jaaprekina=["v(vid) = ?"],
             formulas=["v(vid) = s(kop)/t(kop)"],
             aprekins=["1)  Pieņem s = 60 km → s₁ = s₂ = 30 km",
                       "2)  t₁ = 30:30 = 1,0 h ;  t₂ = 30:60 = 0,50 h",
                       "3)  v(vid) = 60 : 1,5 = 40 km/h"],
             atbilde="v(vid) = 40 km/h, nevis 45 km/h.",
             piezime="Vidējais aritmētiskais der tikai pie vienādiem "
                     "LAIKIEM."),
        dict(nr=3, virsraksts="Atrodi kļūdu III",
             teksts="«Skrējējs noskrien apli 400 m un atgriežas startā.\n"
                    "Pārvietojums ir 400 m.»\nIzlabo un pamato!",
             dots=["s = 400 m", "starts = finišs"],
             jaaprekina=["|d⃗| = ?"],
             formulas=["d⃗ - vektors no sākuma uz beigām"],
             aprekins=["1)  Sākuma un beigu punkts sakrīt",
                       "2)  Vektora garums starp sakrītošiem punktiem = 0",
                       "3)  |d⃗| = 0 m, bet s = 400 m"],
             atbilde="|d⃗| = 0 m; sajaukts ceļš ar pārvietojumu.",
             piezime="Ceļš ir skalārs un aug vienmēr; pārvietojums ir "
                     "vektors."),
        dict(nr=4, virsraksts="Atrodi kļūdu IV",
             teksts="«s = (25,0 ± 0,5) m; t = (5,0 ± 0,1) s.\n"
                    "δs = 2 %, δt = 2 %, tātad δv = 2 − 2 = 0 %.»\n"
                    "Izlabo risinājumu!",
             dots=["δs = 2 %", "δt = 2 %"],
             jaaprekina=["δv = ?"],
             formulas=["v = s/t", "δv = δs + δt"],
             aprekins=["1)  Kļūda: relatīvās kļūdas atņemtas",
                       "2)  Dalot un reizinot, tās SASKAITA",
                       "3)  δv = 2 + 2 = 4 % → Δv = 0,2 m/s"],
             atbilde="δv = 4 %, nevis 0 %;  v = (5,0 ± 0,2) m/s.",
             piezime="Kļūda nekad nevar samazināties, veicot papildu "
                     "darbības ar mērījumiem."),
        dict(nr=5, virsraksts="Atrodi kļūdu V",
             teksts="«x = 20 − 4t  (m; s), tātad ķermenis bremzē, jo "
                    "ātrums\nir negatīvs.» Izlabo un pamato!",
             dots=["x = 20 − 4t"],
             jaaprekina=["vₓ = ?", "kustības raksturs = ?"],
             formulas=["x = x₀ + vₓt", "v = const → vienmērīga kustība"],
             aprekins=["1)  vₓ = −4 m/s - nemainīgs lielums",
                       "2)  Mīnuss rāda VIRZIENU, nevis bremzēšanu",
                       "3)  Kustība ir vienmērīga pretēji x asij"],
             atbilde="Ķermenis nebremzē - tas kustas vienmērīgi ar "
                     "4 m/s pretēji asij.",
             piezime="Bremzēšanu rādītu mainīgs ātrums, t. i., t² "
                     "loceklis vienādojumā."),
        dict(nr=6, virsraksts="Atrodi kļūdu VI",
             teksts="«Tūrists nostaigāja 300 m, un viņa pārvietojums "
                    "ir\n500 m.» Vai tas ir iespējams? Pamato!",
             dots=["s = 300 m", "|d⃗| = 500 m (apgalvots)"],
             jaaprekina=["Vai iespējams?"],
             formulas=["|d⃗| ≤ s vienmēr"],
             aprekins=["1)  Pārvietojums ir taisnākais ceļš",
                       "2)  Garāks par noieto ceļu tas būt nevar",
                       "3)  Tātad apgalvojums ir kļūdains"],
             atbilde="Nav iespējams: |d⃗| ≤ s, tātad pārvietojums nevar "
                     "pārsniegt 300 m.",
             piezime="Šī nevienādība ir ātrs veids, kā pārbaudīt savu "
                     "atbildi."),
        dict(nr=7, virsraksts="Personīgā atgādne",
             teksts="Sastādi savu atgādni: trīs sakarības, kuras "
                    "jāatceras,\nun divas kļūdas, no kurām jāizvairās "
                    "2. tematā!",
             dots=["PD2 rezultāti"],
             jaaprekina=["atgādne = ?"],
             formulas=["Personīgs saraksts"],
             aprekins=["1)  Sakarības: v = s/t; x = x₀ + vt; "
                       "v(vid) = s(kop)/t(kop)",
                       "2)  Kļūdas: nepārveidotas vienības; "
                       "vidējais aritmētiskais",
                       "3)  Atgādni ielīmē burtnīcas vākā"],
             atbilde="Personīga atgādne ar 3 sakarībām un 2 kļūdām.",
             piezime="Šo atgādni papildināsim pēc katra pārbaudes darba."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Kļūdu labo, izskaidrojot cēloni, ne tikai uzrakstot atbildi.",
            "Ticamības pārbaude atklāj lielāko daļu rupju kļūdu.",
            "Vidējo aritmētisko drīkst lietot tikai pie vienādiem "
            "laikiem.",
            "Ceļš un pārvietojums nav viens un tas pats.",
        ],
        majasdarbs=[
            "Izlabo savas PD2 kļūdas pilnā pierakstā.",
            "Pabeidz personīgo atgādni.",
            "Atkārto v = s/t un grafiku lasīšanu - 2. tematā tie "
            "paplašināsies.",
        ],
        pasvertejums=["Protu atpazīt savu kļūdu",
                      "Protu izlabot risinājumu",
                      "Protu izskaidrot kļūdu citam",
                      "Man ir personīgā atgādne"],
        nakama="Nākamais temats: vienmērīgi paātrināta kustība."),
),

]
