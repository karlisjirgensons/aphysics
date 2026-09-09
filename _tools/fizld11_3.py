# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. LD3 - Transformatora darbības pētīšana."""

LD = {
    "nr": 3,
    "klase": "11. klase",
    "nosaukums": "Transformatora darbības pētīšana",
    "mape": "11. Elektromagnētisms",
    "fails": "LD3. Transformatora darbības pētīšana_tt",
    "datums": "17.02.2027.",
    "svars": 8,
    "laiks": 80,
    "kopa": 22,
    "jautajums": "Kā transformatora sekundārais spriegums ir atkarīgs no "
                 "tinumu vijumu attiecības?",
    "merkis": "Izmērīt sekundāro spriegumu dažādām vijumu attiecībām, "
              "pārbaudīt sakarību U₁/U₂ = N₁/N₂ un novērtēt reāla "
              "transformatora zudumus.",
    "hipoteze": "Pieraksti, kā mainīsies sekundārais spriegums, palielinot "
                "sekundāro vijumu skaitu, un vai sakarība būs tieši "
                "proporcionāla.",
    "teorija": [
        "Transformatora sakarība:  U₁ / U₂ = N₁ / N₂   ⟹   "
        "U₂ = U₁ · N₂ / N₁",
        "Ideāls transformators:  U₁I₁ = U₂I₂   ·   Reālam:  "
        "η = U₂I₂ / (U₁I₁) · 100 %",
        "Transformators darbojas tikai ar maiņstrāvu - vajadzīga mainīga "
        "magnētiskā plūsma.",
        "N₂ > N₁ - paaugstinošs;  N₂ < N₁ - pazeminošs transformators.",
    ],
    "piederumi": [
        "Sadalāms transformators: U veida serde ar noslēdzošo tiltiņu un "
        "vismaz trīs tinumi ar dažādu vijumu skaitu (piemēram, 300, 600 un "
        "1200 vijumi).",
        "Zemsprieguma maiņstrāvas avots (līdz 12 V AC), voltmetrs "
        "maiņspriegumam (vai multimetrs AC režīmā), savienojošie vadi.",
        "Papildus - ampērmetrs AC un neliela slodze (spuldzīte 12 V).",
    ],
    "drosiba": [
        "Izmanto TIKAI skolas zemsprieguma maiņstrāvas avotu (līdz 12 V "
        "AC). 230 V tīkla spriegumu transformatoram nepieslēdz.",
        "Nekad neatstāj sekundāro tinumu ar lielu vijumu skaitu bez "
        "uzraudzības - paaugstinošā režīmā spriegums var būt bīstams.",
        "Serdi salikt un tiltiņu nostiprināt PIRMS barošanas ieslēgšanas; "
        "pārslēdzot tinumus, barošanu izslēdz.",
        "Ja tinums vai serde sasilst, nekavējoties izslēdz avotu.",
    ],
    "gaita": [
        ("Sagatavo transformatoru.", "Uzliec abus tinumus uz U veida serdes "
         "un nostiprini noslēdzošo tiltiņu. Pieraksti abu tinumu vijumu "
         "skaitu."),
        ("Uzzīmē shēmu.", "Protokolā uzzīmē shēmu: maiņstrāvas avots - "
         "primārais tinums; sekundārais tinums - voltmetrs."),
        ("Iestati primāro spriegumu.", "Ieslēdz avotu un iestati "
         "U₁ = 6,0 V AC. Šo spriegumu visā darbā nemaini un katrā mērījumā "
         "pārbaudi ar voltmetru."),
        ("Mēri sekundāro spriegumu.", "Izmēri U₂ un ieraksti tabulā kopā "
         "ar N₁ un N₂."),
        ("Maini vijumu attiecību.", "Izslēdz avotu, nomaini sekundāro "
         "tinumu un atkārto mērījumu. Veic vismaz 4 dažādas vijumu "
         "attiecības - gan pazeminošas, gan paaugstinošas."),
        ("Aprēķini teorētisko vērtību.", "Katrai rindai aprēķini "
         "U₂(teor) = U₁ · N₂ / N₁ un salīdzini to ar izmērīto."),
        ("Pārbaudi ar slodzi.", "Vienai vijumu attiecībai pieslēdz "
         "sekundārajā ķēdē spuldzīti, izmēri I₁ un I₂ un aprēķini "
         "lietderības koeficientu."),
    ],
    "tabula": {
        "galva": ["Nr.", "N₁", "N₂", "N₂/N₁", "U₁, V", "U₂(izm.), V",
                  "U₂(teor.), V", "Novirze, %"],
        "rindas": 4,
        "platumi": [1.2, 2.0, 2.0, 2.2, 2.2, 2.8, 2.8, 2.8],
    },
    "apstrade": [
        ("Teorētiskā sprieguma aprēķins", "Vienai izvēlētai rindai "
         "pieraksti pilnu risinājumu:  U₂ = U₁ · N₂ / N₁.", 4.5),
        ("Novirzes aprēķins", "Tai pašai rindai aprēķini relatīvo novirzi "
         "δ = |U₂(izm.) − U₂(teor.)| / U₂(teor.) · 100 %.", 4.0),
        ("Lietderības koeficients", "Pieraksti mērījumus ar slodzi (U₁, I₁, "
         "U₂, I₂) un aprēķini η = U₂I₂ / (U₁I₁) · 100 %.", 5.5),
        ("Grafiks", "Uzzīmē grafiku U₂ atkarībā no attiecības N₂/N₁! "
         "Novelc vislabāk atbilstošo taisni.", 8.0),
    ],
    "jautajumi": [
        ("Vai izmērītie spriegumi apstiprina sakarību U₁/U₂ = N₁/N₂? "
         "Atbildi pamato ar diviem skaitļiem no tabulas!", 2.4),
        ("Kāpēc izmērītais U₂ parasti ir nedaudz mazāks par aprēķināto?",
         2.2),
        ("Kāds ir iegūtais lietderības koeficients un kur nonāk zaudētā "
         "enerģija?", 2.4),
        ("Kas notiktu, ja primārajam tinumam pieslēgtu līdzstrāvu? Atbildi "
         "pamato!", 2.2),
        ("Paskaidro, kāpēc elektroenerģijas pārvadē izmanto augstu "
         "spriegumu!", 2.2),
    ],
    "sagatavosana": [
        "Katrai grupai: sadalāms transformators ar 3-4 tinumiem, AC avots, "
        "multimetrs AC režīmā, vadi. Pietiek ar 5-6 komplektiem.",
        "Pirms darba pārbaudīt, vai multimetri ir AC režīmā - DC režīmā "
        "maiņspriegumu tie rāda tuvu nullei un skolēni domā, ka ķēde "
        "nedarbojas.",
        "Uzsvērt, ka primārais spriegums U₁ visos mērījumos jāsaglabā "
        "nemainīgs - tas ir fiksētais lielums.",
        "Paaugstinošajā režīmā ierobežot U₁ līdz 6 V, lai sekundārais "
        "spriegums nepārsniegtu 25 V.",
    ],
    "gaidamie": [
        "Ar N₁ = 600, U₁ = 6,0 V: N₂ = 300 dod U₂ ≈ 2,8-3,0 V; N₂ = 1200 "
        "dod U₂ ≈ 11,3-12,0 V.",
        "Izmērītais U₂ tukšgaitā parasti ir par 2-6 % mazāks nekā "
        "teorētiskais - tinumu pretestība un plūsmas noplūde.",
        "Grafiks U₂(N₂/N₁) ir taisne caur koordinātu sākumpunktu.",
        "Ar spuldzīti kā slodzi η parasti iznāk 70-90 %.",
        "Ja U₂ ir tuvu nullei, visbiežāk nav nostiprināts serdes noslēdzošais "
        "tiltiņš vai multimetrs ir DC režīmā.",
    ],
    "atbildes": [
        "Atbilde individuāla; jāvērtē divi konkrēti skaitļi un secinājums, "
        "ka attiecības sakrīt dažu procentu robežās.",
        "Reālā transformatorā ir zudumi: tinumu pretestība (siltums), "
        "magnētiskās plūsmas noplūde ārpus serdes un virpuļstrāvas serdē.",
        "Atbilde individuāla (parasti 70-90 %); zaudētā enerģija pārvēršas "
        "siltumā tinumos un serdē.",
        "Līdzstrāva rada nemainīgu magnētisko plūsmu, tāpēc sekundārajā "
        "tinumā EDS neinducējas un U₂ = 0. Turklāt primārais tinums var "
        "pārkarst, jo tam ir tikai maza aktīvā pretestība.",
        "Pie tās pašas jaudas P = UI augstāks spriegums nozīmē mazāku "
        "strāvu, bet zudumi līnijā ir P = I²R, tāpēc tie samazinās kvadrātā.",
    ],
    "kriteriji": [
        ("Formulēta hipotēze par sprieguma atkarību no vijumu attiecības",
         2),
        ("Uzzīmēta pareiza transformatora shēma", 2),
        ("Ķēde salikta droši; serde noslēgta, primārais spriegums "
         "nemainīgs", 2),
        ("Veikti vismaz 4 mērījumi ar dažādām vijumu attiecībām, dati "
         "tabulā", 4),
        ("Pareizi aprēķināti teorētiskie spriegumi ar pilnu pierakstu", 3),
        ("Aprēķinātas relatīvās novirzes", 2),
        ("Izmērīti un aprēķināti dati lietderības koeficientam", 3),
        ("Uzzīmēts grafiks ar apzīmētām asīm un taisni", 2),
        ("Secinājums pamatots ar datiem; izskaidroti zudumi", 1),
        ("Protokols noformēts kārtīgi un iesniegts termiņā", 1),
    ],
    "piezimes": [
        "Ja nav sadalāma transformatora, darbu var veikt ar gatavu "
        "skolas transformatoru komplektu ar izvadiem - tad vijumu skaitu "
        "ņem no marķējuma.",
        "Metināšanas un mikroviļņu krāsns transformatoru attēli der kā "
        "ievada piemēri, bet klasē tos NEDRĪKST pieslēgt.",
    ],
}
