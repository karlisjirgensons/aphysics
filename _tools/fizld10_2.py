# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. LD2 - Brīvās krišanas paātrinājuma noteikšana."""

LD = {
    "nr": 2,
    "klase": "10. klase",
    "nosaukums": "Brīvās krišanas paātrinājuma noteikšana",
    "mape": "2. Vienmērīga paātrināta kustība",
    "fails": "LD2. Brīvās krišanas paātrinājuma noteikšana_tt",
    "datums": "02.12.2026.",
    "svars": 9,
    "laiks": 80,
    "kopa": 20,
    "jautajums": "Cik liels ir brīvās krišanas paātrinājums un cik precīzi "
                 "to var noteikt ar skolas mērlīdzekļiem?",
    "merkis": "Noteikt brīvās krišanas paātrinājumu, izmērot matemātiskā "
              "svārsta periodu dažādiem garumiem, un novērtēt mērījuma "
              "kļūdu.",
    "hipoteze": "Pieraksti, cik lielu g vērtību sagaidi un kāda, tavuprāt, "
                "būs novirze no tabulas vērtības 9,81 m/s².",
    "teorija": [
        "Matemātiskā svārsta periods:  T = 2π · √(l / g)   ⟹   "
        "g = 4π² l / T²",
        "Periodu nosaka precīzāk, mērot laiku N svārstībām:  T = t / N.",
        "Relatīvā novirze:  δ = |g(izmērītais) − 9,81| / 9,81 · 100 %",
    ],
    "piederumi": [
        "Statīvs ar turētāju, diegs (1,2 m), neliels smags atsvars vai "
        "metāla lodīte ar cilpiņu.",
        "Mērlente vai lineāls (1 mm), hronometrs (0,01 s), transportieris "
        "novirzes leņķa kontrolei.",
    ],
    "drosiba": [
        "Statīvu nostiprina uz galda tā, lai tas nevar apgāzties; atsvaru "
        "piesien ar drošu mezglu.",
        "Svārstības ierosina ar nelielu novirzi (leņķis līdz 10°) - liela "
        "amplitūda ir gan bīstama, gan sabojā mērījumu.",
        "Ap svārstu atbrīvo vietu; blakus nedrīkst būt trausli priekšmeti.",
    ],
    "gaita": [
        ("Sagatavo svārstu.", "Piestiprini atsvaru pie diega un iekar "
         "statīvā. Svārsta garumu l mēra no piekares punkta līdz atsvara "
         "centram."),
        ("Iestati pirmo garumu.", "Iestati l₁ ≈ 0,30 m un precīzi izmēri "
         "faktisko garumu; ieraksti tabulā."),
        ("Ierosini svārstības.", "Novirzi atsvaru par leņķi, kas nepārsniedz "
         "10°, un atlaid to bez grūdiena."),
        ("Mēri laiku.", "Ar hronometru mēri laiku t 20 pilnām svārstībām. "
         "Skaitīšanu sāc, kad atsvars iet caur līdzsvara stāvokli."),
        ("Atkārto.", "Katram garumam mēri 20 svārstību laiku 2 reizes un "
         "ieraksti abus rezultātus."),
        ("Maini garumu.", "Atkārto 2.-5. soli garumiem aptuveni 0,50 m, "
         "0,70 m, 0,90 m un 1,10 m."),
        ("Aprēķini.", "Katrai rindai aprēķini periodu T = t / 20 un "
         "paātrinājumu g = 4π² l / T²."),
    ],
    "tabula": {
        "galva": ["Nr.", "l, m", "N", "t₁, s", "t₂, s", "t(vid), s",
                  "T, s", "g, m/s²"],
        "rindas": 5,
        "platumi": [1.2, 2.2, 1.4, 2.4, 2.4, 2.6, 2.4, 3.4],
    },
    "apstrade": [
        ("Perioda aprēķins", "Vienai izvēlētai rindai parādi, kā no "
         "20 svārstību laika iegūts periods:  T = t(vid) / N.", 3.6),
        ("Paātrinājuma aprēķins", "Tai pašai rindai pieraksti pilnu "
         "risinājumu:  g = 4π² l / T².", 5.5),
        ("Vidējā vērtība un novirze", "Aprēķini visu piecu g vērtību vidējo "
         "aritmētisko un relatīvo novirzi no 9,81 m/s².", 4.5),
    ],
    "jautajumi": [
        ("Cik lielu g vērtību ieguvi? Salīdzini to ar tabulas vērtību "
         "9,81 m/s² un nosauc novirzi procentos!", 2.4),
        ("Kāpēc laiku mēra 20 svārstībām, nevis vienai? Pamato ar "
         "skaitļiem!", 2.2),
        ("Kā mainītos periods, ja atsvaru nomainītu pret divreiz smagāku? "
         "Atbildi pamato ar formulu!", 2.2),
        ("Nosauc divus kļūdu avotus šajā darbā un piedāvā, kā katru no tiem "
         "samazināt!", 2.4),
        ("Vai tava hipotēze apstiprinājās? Atbildi pamato ar datiem!", 2.0),
    ],
    "sagatavosana": [
        "Katrai grupai: statīvs, 1,2 m diegs, atsvars, mērlente, "
        "hronometrs. Pietiek ar 6-8 komplektiem.",
        "Pirms mērījumiem parāda, kā pareizi skaitīt svārstības (sākot no "
        "līdzsvara stāvokļa) un kā mērīt garumu līdz atsvara centram.",
        "Atgādina, ka formula T = 2π√(l/g) ir spēkā tikai maziem "
        "novirzes leņķiem.",
    ],
    "gaidamie": [
        "Ar rūpīgiem mērījumiem g iznāk 9,5-10,1 m/s²; novirze no tabulas "
        "vērtības parasti ir 1-4 %.",
        "Garumam 0,30 m periods ir aptuveni 1,1 s, garumam 1,10 m - "
        "aptuveni 2,1 s.",
        "Ja g sistemātiski iznāk par mazu, visbiežāk garums izmērīts līdz "
        "atsvara augšmalai, nevis centram.",
        "Ja g iznāk stipri par lielu, parasti sajaukts svārstību skaits "
        "(saskaitītas pusperiodi).",
    ],
    "atbildes": [
        "Atbilde individuāla; jāvērtē pareizs salīdzinājums un korekti "
        "aprēķināta relatīvā novirze δ = |g − 9,81| / 9,81 · 100 %.",
        "Hronometra reakcijas kļūda (≈ 0,2 s) sadalās uz 20 periodiem, "
        "tāpēc perioda kļūda samazinās 20 reižu - no 0,2 s līdz 0,01 s.",
        "Periods nemainītos: T = 2π√(l/g) nav atkarīgs no masas, jo "
        "smaguma spēks un inerce aug vienādi.",
        "Piemēram: reakcijas laiks (samazina, mērot vairāk svārstību) un "
        "neprecīzi izmērīts garums (samazina, mērot ar mērlenti līdz "
        "atsvara centram vairākas reizes).",
        "Atbilde atkarīga no hipotēzes; jāvērtē pamatojums ar iegūtajiem "
        "skaitļiem.",
    ],
    "kriteriji": [
        ("Formulēta pārbaudāma hipotēze ar skaitlisku prognozi", 2),
        ("Pareizi izmērīti visi pieci svārsta garumi", 2),
        ("Katram garumam divi mērījumi pa 20 svārstībām, dati tabulā", 3),
        ("Pareizi aprēķināti periodi", 2),
        ("Pareizi aprēķinātas g vērtības ar pilnu risinājuma pierakstu", 4),
        ("Aprēķināta vidējā vērtība un relatīvā novirze", 2),
        ("Secinājums pamatots ar datiem un salīdzināts ar 9,81 m/s²", 2),
        ("Nosaukti divi kļūdu avoti ar konkrētiem uzlabojumiem", 2),
        ("Protokols noformēts kārtīgi un iesniegts termiņā", 1),
    ],
    "piezimes": [
        "Ja ir pieejamas fotoslēdzes vai telefona lēnās uzņemšanas režīms, "
        "spēcīgākajām grupām var piedāvāt salīdzināt abas metodes.",
        "Alternatīva metode - krītoša ķermeņa filmēšana ar 240 kadru/s; tā "
        "der kā papildu uzdevums, bet pamata mērījums paliek svārsts.",
    ],
}
