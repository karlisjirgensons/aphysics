# -*- coding: utf-8 -*-
"""4. temats "Gravitācijas lauks un kustība". A daļa: 4.1.-4.8. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "4. temats. Gravitācijas lauks un kustība"
KICKER = "FIZIKA I · 10. KLASE · 4. TEMATS: GRAVITĀCIJAS LAUKS UN KUSTĪBA"
KURSS = "FIZIKA I · 10. KLASE"
MAPE = "C:/aphysics/Fizika_1/4. Gravitācijas lauks un kustība"

STUNDAS = [

dict(
    nr="4.1", virsraksts="Vispasaules gravitācijas likums",
    jautajums="Kas notur Mēnesi orbītā?",
    apaksraksts="F = Gm₁m₂/r² · G = 6,67·10⁻¹¹ · Universāls likums",
    merkis="Iemācīties lietot vispasaules gravitācijas likumu un saprast "
           "tā universālo raksturu.",
    protu=["formulēt gravitācijas likumu;",
           "aprēķināt gravitācijas spēku;",
           "novērtēt attāluma ietekmi;",
           "pamatot, kāpēc gravitāciju sadzīvē nemanām."],
    atkartojums="3. tematā smaguma spēks bija F = mg ar nemainīgu g. "
                "Tagad noskaidrosim, no kurienes nāk pats g un kas "
                "notiek kosmosā.",
    uzdevumu_apraksts="Gravitācijas spēka aprēķins",
    teorija=[
        ("Gravitācijas likums", [
            ("formula", "VISPASAULES GRAVITĀCIJAS LIKUMS",
             "F = G · m₁ · m₂ / r²        "
             "G = 6,67 · 10⁻¹¹ N·m²/kg²",
             "Jebkuras divas masas pievelkas ar spēku, kas ir tieši "
             "proporcionāls masām un apgriezti proporcionāls attāluma "
             "kvadrātam. r mēra starp masu CENTRIEM.", GOLD),
            ("kartitas", [
                ("UNIVERSĀLS", BLUE,
                 ["Der visām masām.",
                  "Ābolam, Mēnesim, galaktikām.",
                  "Ņūtona lielākais atklājums."]),
                ("ĻOTI VĀJŠ", GREY,
                 ["G ir niecīgs.",
                  "Divi cilvēki 1 m attālumā:",
                  "F ≈ 3·10⁻⁷ N."]),
                ("BEZGALĪGS", GREEN,
                 ["Nekad nekļūst nulle.",
                  "Tikai strauji samazinās.",
                  "r² likums."]),
            ]),
        ]),
        ("Attāluma ietekme", [
            ("tabula",
             ["Attālums", "Spēks", "Piezīme"],
             [["r", "F", "Sākuma vērtība"],
              ["2r", "F/4", "Divreiz tālāk - 4× vājāk"],
              ["3r", "F/9", "Trīsreiz tālāk - 9× vājāk"],
              ["10r", "F/100", "Ļoti strauji sarūk"]],
             [3.40, 3.40, 5.43]),
            ("panelis", "KĀPĒC MĒNESS NEKRĪT",
             ["Mēness patiesībā nepārtraukti «krīt» uz Zemi - bet tam ir "
              "arī sānu ātrums. Kritiena un sānu kustības kombinācija dod "
              "riņķa orbītu. Ja Mēness apstātos, tas nokristu uz Zemi."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēks starp Zemi un Mēnesi",
             teksts="Aprēķini gravitācijas spēku starp Zemi "
                    "(6,0·10²⁴ kg)\nun Mēnesi (7,3·10²² kg), ja attālums "
                    "ir 3,8·10⁸ m!\n(G = 6,67·10⁻¹¹ N·m²/kg²)",
             dots=["M = 6,0·10²⁴ kg", "m = 7,3·10²² kg", "r = 3,8·10⁸ m"],
             jaaprekina=["F = ?"],
             formulas=["F = Gm₁m₂/r²"],
             aprekins=["1)  m₁m₂ = 6,0·10²⁴ · 7,3·10²² = 4,38·10⁴⁷ kg²",
                       "2)  r² = (3,8·10⁸)² = 1,44·10¹⁷ m²",
                       "3)  F = 6,67·10⁻¹¹ · 4,38·10⁴⁷ : 1,44·10¹⁷ ≈ "
                       "2,0·10²⁰ N"],
             atbilde="F ≈ 2,0·10²⁰ N",
             piezime="Milzīgs spēks - un tomēr tas tikai notur Mēnesi "
                     "orbītā."),
        dict(nr=2, virsraksts="Attāluma maiņa",
             teksts="Kā mainīsies gravitācijas spēks, ja attālumu starp\n"
                    "diviem ķermeņiem samazinās 4 reizes?",
             dots=["r₂ = r₁/4"],
             jaaprekina=["F₂/F₁ = ?"],
             formulas=["F ~ 1/r²"],
             aprekins=["1)  F₁ = Gm₁m₂/r₁²",
                       "2)  F₂ = Gm₁m₂/(r₁/4)² = 16·Gm₁m₂/r₁²",
                       "3)  F₂/F₁ = 16"],
             atbilde="Spēks palielināsies 16 reizes.",
             piezime="Kvadrātiskā atkarība - attālums ir izšķirošs."),
        dict(nr=3, virsraksts="Divi cilvēki",
             teksts="Aprēķini gravitācijas spēku starp diviem cilvēkiem\n"
                    "ar masām 70 kg un 60 kg, kas atrodas 1,0 m attālumā!",
             dots=["m₁ = 70 kg", "m₂ = 60 kg", "r = 1,0 m"],
             jaaprekina=["F = ?"],
             formulas=["F = Gm₁m₂/r²"],
             aprekins=["1)  m₁m₂ = 4200 kg²",
                       "2)  r² = 1,0 m²",
                       "3)  F = 6,67·10⁻¹¹ · 4200 = 2,8·10⁻⁷ N"],
             atbilde="F ≈ 2,8·10⁻⁷ N",
             piezime="Miljons reižu mazāks par matiņa svaru - tāpēc to "
                     "nemanām."),
        dict(nr=4, virsraksts="Spēks uz Zemes virsmas",
             teksts="Aprēķini gravitācijas spēku uz 60 kg cilvēku uz "
                    "Zemes\nvirsmas! (M = 6,0·10²⁴ kg; R = 6,4·10⁶ m)\n"
                    "Salīdzini ar mg!",
             dots=["m = 60 kg", "M = 6,0·10²⁴ kg", "R = 6,4·10⁶ m"],
             jaaprekina=["F = ?"],
             formulas=["F = GMm/R²"],
             aprekins=["1)  GMm = 6,67·10⁻¹¹ · 6,0·10²⁴ · 60 = "
                       "2,40·10¹⁶",
                       "2)  R² = 4,10·10¹³ m²",
                       "3)  F = 2,40·10¹⁶ : 4,10·10¹³ ≈ 586 N"],
             atbilde="F ≈ 5,9·10² N;  mg = 60 · 9,8 = 588 N - sakrīt.",
             piezime="Tas pierāda, ka F = mg ir īpašs gadījums no "
                     "gravitācijas likuma."),
        dict(nr=5, virsraksts="Spēks starp Sauli un Zemi",
             teksts="Aprēķini gravitācijas spēku starp Sauli "
                    "(2,0·10³⁰ kg)\nun Zemi (6,0·10²⁴ kg), ja attālums "
                    "ir 1,5·10¹¹ m!\n(G = 6,67·10⁻¹¹ N·m²/kg²)",
             dots=["M = 2,0·10³⁰ kg", "m = 6,0·10²⁴ kg",
                   "r = 1,5·10¹¹ m"],
             jaaprekina=["F = ?"],
             formulas=["F = Gm₁m₂/r²"],
             aprekins=["1)  m₁m₂ = 2,0·10³⁰ · 6,0·10²⁴ = 1,2·10⁵⁵ kg²",
                       "2)  r² = (1,5·10¹¹)² = 2,25·10²² m²",
                       "3)  F = 6,67·10⁻¹¹ · 1,2·10⁵⁵ : 2,25·10²² ≈ "
                       "3,6·10²² N"],
             atbilde="F ≈ 3,6·10²² N",
             piezime="Tas ir 180 reižu lielāks spēks nekā starp Zemi un "
                     "Mēnesi."),
        dict(nr=6, virsraksts="Abas masas un attālums",
             teksts="Kā mainīsies gravitācijas spēks, ja abas masas\n"
                    "palielinās 2 reizes un attālumu arī 2 reizes?",
             dots=["m₁ un m₂ pieaug 2 reizes", "r₂ = 2r₁"],
             jaaprekina=["F₂/F₁ = ?"],
             formulas=["F = Gm₁m₂/r²"],
             aprekins=["1)  Masu devums: 2 · 2 = 4",
                       "2)  Attāluma devums: 1/2² = 1/4",
                       "3)  F₂/F₁ = 4 · 1/4 = 1"],
             atbilde="Spēks nemainīsies.",
             piezime="Divi pretēji efekti tieši izlīdzinās - vienmēr "
                     "rēķini abus atsevišķi."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "F = Gm₁m₂/r²; G = 6,67·10⁻¹¹ N·m²/kg².",
            "Attālumu mēra starp masu centriem.",
            "Spēks ir apgriezti proporcionāls r².",
            "F = mg ir šī likuma īpašs gadījums pie Zemes virsmas.",
        ],
        majasdarbs=[
            "m₁ = 5,0·10³ kg, m₂ = 8,0·10³ kg, r = 20 m. Aprēķini F.",
            "Kā mainīsies F, ja attālumu palielinās 5 reizes?",
            "Aprēķini spēku starp Zemi un 1000 kg satelītu 600 km "
            "augstumā.",
        ],
        pasvertejums=["Protu formulēt gravitācijas likumu",
                      "Protu rēķināt F",
                      "Protu novērtēt attāluma ietekmi",
                      "Protu saistīt ar F = mg"],
        nakama="Nākamā stunda: gravitācijas lauks."),
),

dict(
    nr="4.2", virsraksts="Gravitācijas lauks",
    jautajums="Kā aprakstīt neredzamu lauku?",
    apaksraksts="g = F/m · Lauka intensitāte · Lauka līnijas",
    merkis="Saprast gravitācijas lauku kā matērijas veidu un iemācīties "
           "lietot lauka intensitāti.",
    protu=["definēt gravitācijas lauka intensitāti;",
           "aprēķināt g = GM/r²;",
           "attēlot lauku ar lauka līnijām;",
           "pamatot, ka g nav atkarīgs no ķermeņa masas."],
    atkartojums="4.1. stundā: F = Gm₁m₂/r². Ja spēku dalām ar ķermeņa "
                "masu, iegūstam lielumu, kas raksturo pašu lauku.",
    uzdevumu_apraksts="Lauka intensitāte dažādos attālumos",
    teorija=[
        ("Lauka intensitāte", [
            ("formula", "GRAVITĀCIJAS LAUKA INTENSITĀTE",
             "g = F / m = G · M / r²        [g] = N/kg = m/s²",
             "g raksturo LAUKU, nevis ķermeni tajā. Tā ir spēks uz vienu "
             "masas kilogramu. Pie Zemes virsmas g = 9,8 N/kg.", GOLD),
            ("kartitas", [
                ("VIELA", BLUE,
                 ["Sastāv no daļiņām.",
                  "Ir masa un tilpums.",
                  "Piemērs: akmens, gaiss."]),
                ("LAUKS", GREEN,
                 ["Nepārtraukts telpā.",
                  "Pārnes mijiedarbību.",
                  "Piemērs: gravitācijas lauks."]),
                ("ABI - MATĒRIJA", GOLD,
                 ["Lauks ir tikpat reāls",
                  "kā viela - to var izmērīt",
                  "un tam ir enerģija."]),
            ]),
        ]),
        ("Lauks dažādos attālumos", [
            ("tabula",
             ["Vieta", "g, m/s²", "Piezīme"],
             [["Zemes virsma", "9,81", "R = 6400 km"],
              ["400 km augstumā (KKS)", "8,7", "Tikai 11 % mazāk"],
              ["Ģeostacionārā orbīta", "0,22", "36 000 km"],
              ["Mēness virsma", "1,6", "6 reizes mazāk"],
              ["Marsa virsma", "3,7", "2,6 reizes mazāk"],
              ["Jupitera virsma", "24,8", "2,5 reizes vairāk"]],
             [4.60, 3.10, 4.53]),
            ("panelis", "KĀPĒC KKS IR BEZSVARA STĀVOKLIS",
             ["400 km augstumā g joprojām ir 8,7 m/s² - gandrīz kā uz "
              "Zemes. Bezsvara stāvoklis rodas nevis tāpēc, ka nav "
              "gravitācijas, bet tāpēc, ka stacija nepārtraukti brīvi "
              "krīt ap Zemi."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="g uz Zemes virsmas",
             teksts="Aprēķini gravitācijas lauka intensitāti uz Zemes\n"
                    "virsmas! (M = 6,0·10²⁴ kg; R = 6,4·10⁶ m;\n"
                    "G = 6,67·10⁻¹¹ N·m²/kg²)",
             dots=["M = 6,0·10²⁴ kg", "R = 6,4·10⁶ m"],
             jaaprekina=["g = ?"],
             formulas=["g = GM/R²"],
             aprekins=["1)  GM = 6,67·10⁻¹¹ · 6,0·10²⁴ = 4,00·10¹⁴",
                       "2)  R² = 4,10·10¹³ m²",
                       "3)  g = 4,00·10¹⁴ : 4,10·10¹³ ≈ 9,8 m/s²"],
             atbilde="g ≈ 9,8 m/s²",
             piezime="Precīza sakritība ar tabulas vērtību 9,81 m/s²."),
        dict(nr=2, virsraksts="g augstumā",
             teksts="Aprēķini g 6400 km augstumā virs Zemes virsmas!\n"
                    "(R = 6,4·10⁶ m; g₀ = 9,8 m/s²)",
             dots=["h = R = 6,4·10⁶ m", "g₀ = 9,8 m/s²"],
             jaaprekina=["g = ?"],
             formulas=["g = GM/(R+h)²", "g/g₀ = R²/(R+h)²"],
             aprekins=["1)  R + h = 2R",
                       "2)  g/g₀ = R²/(2R)² = 1/4",
                       "3)  g = 9,8 : 4 = 2,45 m/s²"],
             atbilde="g ≈ 2,5 m/s²",
             piezime="Divkāršā attālumā no centra - četrreiz vājāks "
                     "lauks."),
        dict(nr=3, virsraksts="g uz citas planētas",
             teksts="Planētas masa ir 2 reizes lielāka par Zemes, "
                    "rādiuss\n2 reizes lielāks. Aprēķini g uz tās "
                    "virsmas! (g(Z) = 9,8 m/s²)",
             dots=["M = 2M(Z)", "R = 2R(Z)"],
             jaaprekina=["g = ?"],
             formulas=["g = GM/R²"],
             aprekins=["1)  g = G·2M(Z) / (2R(Z))²",
                       "2)  g = G·2M(Z) / (4R(Z)²) = 0,5 · GM(Z)/R(Z)²",
                       "3)  g = 0,5 · 9,8 = 4,9 m/s²"],
             atbilde="g = 4,9 m/s² - divreiz mazāks nekā uz Zemes.",
             piezime="Rādiuss ietekmē kvadrātā, tāpēc uzvar tas."),
        dict(nr=4, virsraksts="Spēks no lauka",
             teksts="Uz Marsa (g = 3,7 m/s²) astronauts ar aprīkojumu\n"
                    "sver 120 kg. Aprēķini smaguma spēku uz Marsa un uz\n"
                    "Zemes!",
             dots=["m = 120 kg", "g(M) = 3,7 m/s²", "g(Z) = 9,8 m/s²"],
             jaaprekina=["F(M) = ?", "F(Z) = ?"],
             formulas=["F = mg"],
             aprekins=["1)  F(M) = 120 · 3,7 = 444 N",
                       "2)  F(Z) = 120 · 9,8 = 1176 N",
                       "3)  Attiecība 1176 : 444 ≈ 2,6"],
             atbilde="F(M) ≈ 4,4·10² N ;   F(Z) ≈ 1,2·10³ N",
             piezime="Uz Marsa aprīkojums šķiet 2,6 reizes vieglāks - "
                     "masa nemainās."),
        dict(nr=5, virsraksts="g uz Jupitera",
             teksts="Jupitera masa ir 318 Zemes masas, rādiuss - "
                    "11 Zemes\nrādiusi. Aprēķini g uz Jupitera! "
                    "(g(Z) = 9,8 m/s²)",
             dots=["M = 318 M(Z)", "R = 11 R(Z)"],
             jaaprekina=["g = ?"],
             formulas=["g/g(Z) = (M/M(Z)) / (R/R(Z))²"],
             aprekins=["1)  (R/R(Z))² = 11² = 121",
                       "2)  g/g(Z) = 318 : 121 = 2,63",
                       "3)  g = 2,63 · 9,8 ≈ 26 m/s²"],
             atbilde="g ≈ 26 m/s² - gandrīz 3 reizes vairāk nekā uz "
                     "Zemes.",
             piezime="Milzīgā masa uzvar, kaut arī rādiuss ietekmē "
                     "kvadrātā."),
        dict(nr=6, virsraksts="Lauka intensitāte no spēka",
             teksts="Uz 25 kg ķermeni planētas laukā darbojas spēks "
                    "300 N.\nAprēķini lauka intensitāti!",
             dots=["m = 25 kg", "F = 300 N"],
             jaaprekina=["g = ?"],
             formulas=["g = F/m"],
             aprekins=["1)  g = 300 : 25",
                       "2)  g = 12 N/kg",
                       "3)  Skaitliski tas pats, kas 12 m/s²"],
             atbilde="g = 12 N/kg = 12 m/s²",
             piezime="N/kg un m/s² ir viena un tā pati mērvienība, "
                     "tikai uzsver dažādu nozīmi."),
        dict(nr=7, virsraksts="Kur lauks ir uz pusi vājāks",
             teksts="Kādā augstumā virs Zemes virsmas g ir uz pusi "
                    "mazāks?\n(R = 6,4·10⁶ m; √2 = 1,41)",
             dots=["R = 6,4·10⁶ m", "g = g₀/2"],
             jaaprekina=["r = ?", "h = ?"],
             formulas=["g = g₀R²/r²", "r = R√2", "h = r − R"],
             aprekins=["1)  R²/r² = 1/2 → r = R√2",
                       "2)  r = 6,4·10⁶ · 1,41 = 9,02·10⁶ m",
                       "3)  h = 9,02·10⁶ − 6,4·10⁶ ≈ 2,6·10⁶ m"],
             atbilde="h ≈ 2,6·10³ km",
             piezime="Uz pusi vājāks lauks prasa nevis divkāršu, bet "
                     "tikai 1,41 reizes lielāku attālumu no centra."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "g = F/m = GM/r² - lauka intensitāte.",
            "g raksturo lauku, nevis ķermeni tajā.",
            "[g] = N/kg = m/s².",
            "Bezsvara stāvoklis nenozīmē gravitācijas trūkumu.",
        ],
        majasdarbs=[
            "Aprēķini g uz Mēness (M = 7,3·10²² kg; R = 1,7·10⁶ m).",
            "Aprēķini g 3200 km augstumā virs Zemes.",
            "Planētai M = 4M(Z), R = 2R(Z). Aprēķini g.",
        ],
        pasvertejums=["Protu definēt lauka intensitāti",
                      "Protu rēķināt g",
                      "Protu salīdzināt planētas",
                      "Protu izskaidrot bezsvara stāvokli"],
        nakama="Nākamā stunda: brīvās krišanas paātrinājums."),
),

dict(
    nr="4.3", virsraksts="Brīvās krišanas paātrinājums",
    jautajums="Cik smagi būtu uz Marsa?",
    apaksraksts="g = GM/R² · Planētu salīdzinājums · Augstuma ietekme",
    merkis="Nostiprināt g aprēķinus dažādām planētām un augstumiem un "
           "saprast, no kā g ir atkarīgs.",
    protu=["aprēķināt g jebkurai planētai;",
           "salīdzināt planētas pēc masas un rādiusa;",
           "aprēķināt g dotā augstumā;",
           "pamatot, kāpēc g nav atkarīgs no krītošā ķermeņa masas."],
    atkartojums="4.2. stundā: g = GM/r². Šodien šo formulu lietosim "
                "praktiski - salīdzinot planētas un augstumus.",
    uzdevumu_apraksts="g dažādām planētām un augstumiem",
    teorija=[
        ("No kā atkarīgs g", [
            ("formula", "PLANĒTAS LAUKS",
             "g = G · M / R²        Augstumā h:  "
             "g(h) = G · M / (R + h)²",
             "g ir atkarīgs TIKAI no planētas masas un rādiusa (un "
             "attāluma). Krītošā ķermeņa masa nav svarīga - tāpēc visi "
             "ķermeņi krīt vienādi.", GOLD),
            ("divi",
             ("MASA AUG", GREEN,
              ["g aug proporcionāli.",
               "2× masa → 2× g.",
               "Jupiterim g = 24,8 m/s²."]),
             ("RĀDIUSS AUG", RED,
              ["g sarūk kvadrātā.",
               "2× rādiuss → 4× mazāks g.",
               "Tāpēc lielas planētas ne vienmēr",
               "dod lielu g."])),
        ]),
        ("Planētu dati", [
            ("tabula",
             ["Planēta", "M / M(Zemes)", "R / R(Zemes)", "g, m/s²"],
             [["Merkurs", "0,055", "0,38", "3,7"],
              ["Venera", "0,82", "0,95", "8,9"],
              ["Zeme", "1", "1", "9,81"],
              ["Marss", "0,11", "0,53", "3,7"],
              ["Jupiters", "318", "11,2", "24,8"]],
             [3.10, 3.30, 3.30, 2.53]),
            ("panelis", "SALĪDZINĀŠANAS PAŅĒMIENS",
             ["Nav jārēķina ar G un lielajiem skaitļiem - pietiek ar "
              "attiecību pret Zemi:",
              "g/g(Z) = (M/M(Z))/(R/R(Z))²",
              "Piemēram, Marsam: 0,11 : 0,53² = 0,11 : 0,28 ≈ 0,39, "
              "tātad g ≈ 0,39 · 9,8 = 3,8 m/s²."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="g uz Marsa",
             teksts="Marsa masa ir 0,11 no Zemes masas, rādiuss - 0,53 "
                    "no\nZemes rādiusa. Aprēķini g uz Marsa! "
                    "(g(Z) = 9,8 m/s²)",
             dots=["M = 0,11 M(Z)", "R = 0,53 R(Z)"],
             jaaprekina=["g = ?"],
             formulas=["g/g(Z) = (M/M(Z)) / (R/R(Z))²"],
             aprekins=["1)  (R/R(Z))² = 0,53² = 0,281",
                       "2)  g/g(Z) = 0,11 : 0,281 = 0,391",
                       "3)  g = 0,391 · 9,8 = 3,8 m/s²"],
             atbilde="g ≈ 3,8 m/s²",
             piezime="Uz Marsa lēciens būtu 2,6 reizes augstāks nekā uz "
                     "Zemes."),
        dict(nr=2, virsraksts="Krišana uz Mēness",
             teksts="Uz Mēness g = 1,6 m/s². Cik ilgi ķermenis krīt no\n"
                    "10 m augstuma un cik ilgi tas pats notiktu uz Zemes?",
             dots=["h = 10 m", "g(M) = 1,6 m/s²", "g(Z) = 9,8 m/s²"],
             jaaprekina=["t(M) = ?", "t(Z) = ?"],
             formulas=["t = √(2h/g)"],
             aprekins=["1)  t(M) = √(20 : 1,6) = √12,5 = 3,5 s",
                       "2)  t(Z) = √(20 : 9,8) = √2,04 = 1,4 s",
                       "3)  Attiecība 2,5 reizes"],
             atbilde="t(M) ≈ 3,5 s ;   t(Z) ≈ 1,4 s",
             piezime="Tāpēc Apollo astronautu kustības video izskatās "
                     "palēninātas."),
        dict(nr=3, virsraksts="g satelīta augstumā",
             teksts="Aprēķini g Starptautiskās kosmosa stacijas orbītā\n"
                    "400 km augstumā! (R = 6400 km; g₀ = 9,8 m/s²)",
             dots=["h = 400 km", "R = 6400 km", "g₀ = 9,8 m/s²"],
             jaaprekina=["g = ?"],
             formulas=["g = g₀ · R²/(R+h)²"],
             aprekins=["1)  R + h = 6800 km",
                       "2)  (R/(R+h))² = (6400 : 6800)² = 0,886",
                       "3)  g = 9,8 · 0,886 = 8,7 m/s²"],
             atbilde="g ≈ 8,7 m/s² - tikai 11 % mazāk nekā uz Zemes.",
             piezime="Bezsvara stāvoklis KKS nav gravitācijas trūkuma "
                     "dēļ."),
        dict(nr=4, virsraksts="Planētas masa no g",
             teksts="Uz planētas g = 12 m/s², rādiuss 8,0·10⁶ m.\n"
                    "Aprēķini planētas masu! "
                    "(G = 6,67·10⁻¹¹ N·m²/kg²)",
             dots=["g = 12 m/s²", "R = 8,0·10⁶ m"],
             jaaprekina=["M = ?"],
             formulas=["g = GM/R²", "M = gR²/G"],
             aprekins=["1)  R² = 6,4·10¹³ m²",
                       "2)  gR² = 12 · 6,4·10¹³ = 7,68·10¹⁴",
                       "3)  M = 7,68·10¹⁴ : 6,67·10⁻¹¹ ≈ 1,15·10²⁵ kg"],
             atbilde="M ≈ 1,2·10²⁵ kg (aptuveni 2 Zemes masas)",
             piezime="Tā astronomi nosaka planētu masas - pēc to "
                     "gravitācijas ietekmes."),
        dict(nr=5, virsraksts="g uz Veneras",
             teksts="Veneras masa ir 0,82 Zemes masas, rādiuss - 0,95 "
                    "Zemes\nrādiusa. Aprēķini g uz Veneras! "
                    "(g(Z) = 9,8 m/s²)",
             dots=["M = 0,82 M(Z)", "R = 0,95 R(Z)"],
             jaaprekina=["g = ?"],
             formulas=["g/g(Z) = (M/M(Z)) / (R/R(Z))²"],
             aprekins=["1)  0,95² = 0,9025",
                       "2)  g/g(Z) = 0,82 : 0,9025 = 0,908",
                       "3)  g = 0,908 · 9,8 ≈ 8,9 m/s²"],
             atbilde="g ≈ 8,9 m/s²",
             piezime="Venera ir vistuvākā Zemei pēc gravitācijas - "
                     "tikai 9 % atšķirība."),
        dict(nr=6, virsraksts="Svārsts uz Mēness",
             teksts="Metru garš svārsts pārnests uz Mēnesi "
                    "(g = 1,6 m/s²).\nAprēķini periodu un salīdzini ar "
                    "Zemi! (π = 3,14)",
             dots=["l = 1,00 m", "g(M) = 1,6 m/s²", "g(Z) = 9,8 m/s²"],
             jaaprekina=["T(M) = ?", "T(Z) = ?"],
             formulas=["T = 2π√(l/g)"],
             aprekins=["1)  T(M) = 6,28 · √(1,00 : 1,6) = 6,28 · 0,79",
                       "2)  T(M) = 4,96 ≈ 5,0 s",
                       "3)  T(Z) = 6,28 · √0,102 = 2,0 s"],
             atbilde="T(M) ≈ 5,0 s ;   T(Z) ≈ 2,0 s",
             piezime="Vājākā laukā svārsts svārstās lēnāk - T ~ 1/√g."),
        dict(nr=7, virsraksts="Lēciens uz Mēness",
             teksts="Astronauts atgrūžas ar vertikālu ātrumu 2,0 m/s.\n"
                    "Cik augstu viņš uzlec uz Zemes un cik uz Mēness?\n"
                    "(g(Z) = 9,8 m/s²; g(M) = 1,6 m/s²)",
             dots=["v₀ = 2,0 m/s", "g(Z) = 9,8 m/s²",
                   "g(M) = 1,6 m/s²"],
             jaaprekina=["h(Z) = ?", "h(M) = ?"],
             formulas=["h = v₀²/(2g)"],
             aprekins=["1)  v₀² = 4,0 m²/s²",
                       "2)  h(Z) = 4,0 : 19,6 = 0,20 m",
                       "3)  h(M) = 4,0 : 3,2 = 1,25 m"],
             atbilde="h(Z) = 0,20 m ;   h(M) ≈ 1,3 m - 6 reizes "
                     "augstāk.",
             piezime="Augstums apgriezti proporcionāls g - tāpēc "
                     "attiecība ir tieši 9,8 : 1,6."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "g = GM/R² - atkarīgs tikai no planētas masas un rādiusa.",
            "Augstumā: g(h) = GM/(R+h)².",
            "Salīdzinot planētas, ērti lietot attiecības.",
            "Krītošā ķermeņa masa g neietekmē.",
        ],
        majasdarbs=[
            "Venera: M = 0,82 M(Z), R = 0,95 R(Z). Aprēķini g.",
            "h = 1000 km virs Zemes. Aprēķini g.",
            "Uz planētas g = 5,0 m/s², R = 4,0·10⁶ m. Aprēķini M.",
        ],
        pasvertejums=["Protu rēķināt g planētai",
                      "Protu salīdzināt planētas",
                      "Protu rēķināt g augstumā",
                      "Protu atrast planētas masu"],
        nakama="Nākamā stunda: uzdevumi par gravitāciju."),
),

dict(
    nr="4.4", virsraksts="Uzdevumi par gravitāciju",
    jautajums="Cik reižu mainās spēks, mainot attālumu?",
    apaksraksts="Attiecību metode · Kombinēti uzdevumi",
    merkis="Nostiprināt gravitācijas uzdevumus, īpaši attiecību metodi, "
           "kas ietaupa laiku eksāmenā.",
    protu=["lietot attiecību metodi;",
           "risināt uzdevumus bez skaitliskiem datiem;",
           "kombinēt gravitāciju ar dinamiku;",
           "pārbaudīt rezultāta ticamību."],
    atkartojums="Mums ir F = Gm₁m₂/r² un g = GM/r². Šodien mācāmies tās "
                "lietot ātri - ar attiecībām.",
    uzdevumu_apraksts="Attiecību metode un kombinēti uzdevumi",
    teorija=[
        ("Attiecību metode", [
            ("panelis", "KĀPĒC TĀ IR ĒRTA",
             ["Ja jautā «cik reižu», nav jārēķina ar G un lielajiem "
              "skaitļiem. Pietiek uzrakstīt abas formulas un tās dalīt - "
              "konstantes saīsinās. Tas ir ātrāk un mazāk kļūdu."],
             NAVY),
            ("formula", "PIEMĒRS",
             "F₂ / F₁ = (m₂/m₁) · (r₁/r₂)²        "
             "g₂ / g₁ = (M₂/M₁) · (R₁/R₂)²",
             "Uzmanību ar kārtību: masas attiecība tiek TIEŠI, bet "
             "attālumu attiecība - APGRIEZTI un kvadrātā.", GOLD),
        ]),
        ("Tipiskās situācijas", [
            ("tabula",
             ["Izmaiņa", "Kā mainās F", "Aprēķins"],
             [["r palielina 2×", "samazinās 4×", "(1/2)² = 1/4"],
              ["r samazina 3×", "palielinās 9×", "3² = 9"],
              ["Vienu masu palielina 3×", "palielinās 3×", "tieši"],
              ["Abas masas 2×, r 2×", "nemainās", "4 : 4 = 1"]],
             [4.30, 3.60, 4.33]),
            ("kartitas", [
                ("PĀRBAUDE", BLUE,
                 ["Vai atbilde loģiska?",
                  "Tuvāk - vienmēr stiprāk.",
                  "Lielāka masa - stiprāk."]),
                ("MĒRVIENĪBAS", GOLD,
                 ["Attiecībās mērvienību nav.",
                  "Rezultāts - skaitlis."]),
                ("KĻŪDA", RED,
                 ["Aizmirst kvadrātu pie r.",
                  "Sajaukt tiešo un apgriezto."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Attāluma un masas maiņa",
             teksts="Kā mainīsies gravitācijas spēks, ja vienu masu\n"
                    "palielinās 3 reizes, bet attālumu - 2 reizes?",
             dots=["m₂ = 3m₁", "r₂ = 2r₁"],
             jaaprekina=["F₂/F₁ = ?"],
             formulas=["F₂/F₁ = (m₂/m₁)·(r₁/r₂)²"],
             aprekins=["1)  Masas devums: 3",
                       "2)  Attāluma devums: (1/2)² = 1/4",
                       "3)  F₂/F₁ = 3 · 1/4 = 0,75"],
             atbilde="Spēks samazināsies 1,33 reizes (paliks 75 %).",
             piezime="Attāluma ietekme uzvarēja masas ietekmi."),
        dict(nr=2, virsraksts="Kur spēki izlīdzinās",
             teksts="Attālums starp Zemi un Mēnesi ir 3,8·10⁸ m; Zemes\n"
                    "masa ir 81 reizi lielāka. Cik tālu no Zemes atrodas\n"
                    "punkts, kur abu spēki izlīdzinās?",
             dots=["L = 3,8·10⁸ m", "M(Z) = 81 M(M)"],
             jaaprekina=["x = ?"],
             formulas=["GM(Z)m/x² = GM(M)m/(L−x)²",
                       "81/x² = 1/(L−x)²"],
             aprekins=["1)  9/x = 1/(L−x)",
                       "2)  9L − 9x = x → 10x = 9L",
                       "3)  x = 0,9 · 3,8·10⁸ = 3,42·10⁸ m"],
             atbilde="x ≈ 3,4·10⁸ m no Zemes (90 % ceļa).",
             piezime="Šo punktu šķērsojot, kosmosa kuģis sāk «krist» uz "
                     "Mēnesi."),
        dict(nr=3, virsraksts="Svars dažādos augstumos",
             teksts="Cilvēks sver 700 N uz Zemes virsmas. Cik viņš svērs\n"
                    "augstumā, kas vienāds ar Zemes rādiusu?",
             dots=["P₀ = 700 N", "h = R"],
             jaaprekina=["P = ?"],
             formulas=["P ~ 1/r²", "P/P₀ = R²/(2R)²"],
             aprekins=["1)  Attālums no centra: 2R",
                       "2)  P/P₀ = (R/2R)² = 1/4",
                       "3)  P = 700 : 4 = 175 N"],
             atbilde="P = 175 N",
             piezime="Masa paliek tā pati - mainās tikai lauka "
                     "intensitāte."),
        dict(nr=4, virsraksts="Gravitācija un dinamika",
             teksts="Uz planētas ar g = 6,0 m/s² ķermenis (m = 5,0 kg)\n"
                    "krīt no 30 m. Aprēķini krišanas laiku, ātrumu pie\n"
                    "virsmas un smaguma spēku!",
             dots=["g = 6,0 m/s²", "m = 5,0 kg", "h = 30 m"],
             jaaprekina=["t = ?", "v = ?", "F = ?"],
             formulas=["t = √(2h/g)", "v = gt", "F = mg"],
             aprekins=["1)  t = √(60 : 6,0) = √10 = 3,16 ≈ 3,2 s",
                       "2)  v = 6,0 · 3,16 = 19 m/s",
                       "3)  F = 5,0 · 6,0 = 30 N"],
             atbilde="t ≈ 3,2 s ;   v ≈ 19 m/s ;   F = 30 N",
             piezime="Uz Zemes tas pats kritiens ilgtu 2,5 s."),
        dict(nr=5, virsraksts="Cik jāsamazina attālums",
             teksts="Cik reižu jāsamazina attālums starp diviem "
                    "ķermeņiem,\nlai gravitācijas spēks pieaugtu "
                    "9 reizes?",
             dots=["F₂ = 9F₁", "masas nemainās"],
             jaaprekina=["r₁/r₂ = ?"],
             formulas=["F ~ 1/r²", "F₂/F₁ = (r₁/r₂)²"],
             aprekins=["1)  (r₁/r₂)² = 9",
                       "2)  r₁/r₂ = √9",
                       "3)  r₁/r₂ = 3"],
             atbilde="Attālums jāsamazina 3 reizes.",
             piezime="Spēka izmaiņai vienmēr velk kvadrātsakni, lai "
                     "iegūtu attāluma izmaiņu."),
        dict(nr=6, virsraksts="Gravitācija kā centrtieces spēks",
             teksts="Satelīts riņķo 1,0·10⁷ m attālumā no Zemes centra.\n"
                    "Aprēķini paātrinājumu un ātrumu orbītā!\n"
                    "(GM = 4,0·10¹⁴ m³/s²)",
             dots=["r = 1,0·10⁷ m", "GM = 4,0·10¹⁴ m³/s²"],
             jaaprekina=["a = ?", "v = ?"],
             formulas=["a = GM/r²", "v = √(GM/r)"],
             aprekins=["1)  r² = 1,0·10¹⁴ m²",
                       "2)  a = 4,0·10¹⁴ : 1,0·10¹⁴ = 4,0 m/s²",
                       "3)  v = √(4,0·10¹⁴ : 1,0·10⁷) = √(4,0·10⁷) = "
                       "6,3·10³ m/s"],
             atbilde="a = 4,0 m/s² ;   v ≈ 6,3 km/s",
             piezime="Pārbaude: a = v²/r = (6,3·10³)² : 1,0·10⁷ = "
                     "4,0 m/s² ✔"),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Attiecību metode ietaupa laiku un samazina kļūdas.",
            "Masas attiecība - tieši, attālumu - apgriezti kvadrātā.",
            "Spēku izlīdzināšanās punktu atrod, pielīdzinot spēkus.",
            "Svars mainās ar augstumu, masa - nē.",
        ],
        majasdarbs=[
            "Masu palielina 4×, attālumu 2×. Kā mainās F?",
            "Cilvēks sver 800 N uz Zemes. Cik svērs 2R augstumā?",
            "g = 4,0 m/s², h = 20 m, m = 3,0 kg. Aprēķini t, v un F.",
        ],
        pasvertejums=["Protu lietot attiecību metodi",
                      "Protu risināt bez skaitļiem",
                      "Protu apvienot ar dinamiku",
                      "Protu pārbaudīt ticamību"],
        nakama="Nākamā stunda: kustība gravitācijas laukā."),
),

dict(
    nr="4.5", virsraksts="Kustība gravitācijas laukā",
    jautajums="Kāpēc pavadonis nekrīt zemē?",
    apaksraksts="Gravitācija kā centrtieces spēks · GMm/r² = mv²/r",
    merkis="Saprast orbitālo kustību kā brīvu krišanu ar sānu ātrumu un "
           "iemācīties saistīt gravitāciju ar centrtieces spēku.",
    protu=["pamatot, ka orbītā gravitācija ir centrtieces spēks;",
           "pierakstīt GMm/r² = mv²/r;",
           "aprēķināt orbitālo ātrumu;",
           "izskaidrot Ņūtona lielgabala domu eksperimentu."],
    atkartojums="2.11. stundā: riņķa kustībā a = v²/r un tam vajadzīgs "
                "spēks uz centru. 4.1. stundā: gravitācija ir vērsta uz "
                "planētas centru. Salikts kopā - iegūstam orbītu.",
    uzdevumu_apraksts="Orbitālais ātrums un periods",
    teorija=[
        ("Orbītas nosacījums", [
            ("formula", "GRAVITĀCIJA KĀ CENTRTIECES SPĒKS",
             "G · M · m / r² = m · v² / r        ⟹        "
             "v = √(G · M / r)",
             "Masa m saīsinās - orbitālais ātrums nav atkarīgs no "
             "satelīta masas. Tas ir atkarīgs tikai no planētas masas un "
             "orbītas rādiusa.", GOLD),
            ("panelis", "ŅŪTONA LIELGABALS",
             ["Ja no augsta kalna izšauj lodi horizontāli, tā krīt un "
              "nokrīt zemē. Jo lielāks ātrums, jo tālāk. Pie noteikta "
              "ātruma lode krīt tieši tik ātri, cik Zemes virsma «bēg» "
              "prom - un lode nekad nenokrīt. Tā ir orbīta."], NAVY),
        ]),
        ("Orbitālais ātrums un periods", [
            ("formula", "PERIODS ORBĪTĀ",
             "T = 2π · r / v = 2π · √(r³ / (G · M))",
             "Jo tālāka orbīta, jo mazāks ātrums un ilgāks periods. "
             "KKS 400 km augstumā: v ≈ 7,7 km/s, T ≈ 92 min.", GOLD),
            ("tabula",
             ["Orbīta", "Augstums", "v", "Periods"],
             [["KKS (zemā)", "400 km", "7,7 km/s", "92 min"],
              ["Navigācijas (GPS)", "20 200 km", "3,9 km/s", "12 h"],
              ["Ģeostacionārā", "35 800 km", "3,1 km/s", "24 h"],
              ["Mēness", "384 000 km", "1,0 km/s", "27,3 d"]],
             [3.60, 2.90, 2.60, 3.13]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Orbitālais ātrums",
             teksts="Aprēķini satelīta ātrumu 600 km augstumā virs Zemes!\n"
                    "(M = 6,0·10²⁴ kg; R = 6,4·10⁶ m;\n"
                    "G = 6,67·10⁻¹¹ N·m²/kg²)",
             dots=["h = 6,0·10⁵ m", "R = 6,4·10⁶ m", "M = 6,0·10²⁴ kg"],
             jaaprekina=["v = ?"],
             formulas=["r = R + h", "v = √(GM/r)"],
             aprekins=["1)  r = 6,4·10⁶ + 0,6·10⁶ = 7,0·10⁶ m",
                       "2)  GM/r = 4,0·10¹⁴ : 7,0·10⁶ = 5,71·10⁷ m²/s²",
                       "3)  v = 7,56·10³ ≈ 7,6 km/s"],
             atbilde="v ≈ 7,6 km/s",
             piezime="Aptuveni 27 000 km/h - Zemi apriņķo 1,5 stundās."),
        dict(nr=2, virsraksts="Periods orbītā",
             teksts="Izmantojot 1. uzdevuma datus, aprēķini apriņķošanas\n"
                    "periodu! (π ≈ 3,14)",
             dots=["r = 7,0·10⁶ m", "v = 7,56·10³ m/s"],
             jaaprekina=["T = ?"],
             formulas=["T = 2πr/v"],
             aprekins=["1)  2πr = 2 · 3,14 · 7,0·10⁶ = 4,40·10⁷ m",
                       "2)  T = 4,40·10⁷ : 7,56·10³",
                       "3)  T = 5820 s ≈ 97 min"],
             atbilde="T ≈ 5,8·10³ s ≈ 97 minūtes",
             piezime="Tuvu KKS periodam (92 min) - orbīta ir nedaudz "
                     "augstāka."),
        dict(nr=3, virsraksts="Ātrums dažādās orbītās",
             teksts="Kā mainīsies orbitālais ātrums, ja orbītas rādiusu\n"
                    "palielinās 4 reizes?",
             dots=["r₂ = 4r₁"],
             jaaprekina=["v₂/v₁ = ?"],
             formulas=["v = √(GM/r)", "v ~ 1/√r"],
             aprekins=["1)  v₂/v₁ = √(r₁/r₂)",
                       "2)  = √(1/4)",
                       "3)  = 1/2"],
             atbilde="Ātrums samazināsies 2 reizes.",
             piezime="Tāpēc ģeostacionārie satelīti kustas lēnāk par KKS."),
        dict(nr=4, virsraksts="Mēness ātrums",
             teksts="Mēness attālums no Zemes centra 3,8·10⁸ m.\n"
                    "Aprēķini tā ātrumu un periodu!\n"
                    "(GM = 4,0·10¹⁴ m³/s²; π ≈ 3,14)",
             dots=["r = 3,8·10⁸ m", "GM = 4,0·10¹⁴ m³/s²"],
             jaaprekina=["v = ?", "T = ?"],
             formulas=["v = √(GM/r)", "T = 2πr/v"],
             aprekins=["1)  GM/r = 4,0·10¹⁴ : 3,8·10⁸ = 1,05·10⁶",
                       "2)  v = 1,03·10³ m/s ≈ 1,0 km/s",
                       "3)  T = 2·3,14·3,8·10⁸ : 1,03·10³ ≈ 2,32·10⁶ s "
                       "≈ 27 dienas"],
             atbilde="v ≈ 1,0 km/s ;   T ≈ 27 dienas",
             piezime="Sakrīt ar novēroto Mēness apriņķošanas periodu."),
        dict(nr=5, virsraksts="Periods no orbītas rādiusa",
             teksts="Satelīta orbītas rādiuss ir 1,0·10⁷ m.\n"
                    "Aprēķini apriņķošanas periodu!\n"
                    "(GM = 4,0·10¹⁴ m³/s²; π ≈ 3,14)",
             dots=["r = 1,0·10⁷ m", "GM = 4,0·10¹⁴ m³/s²"],
             jaaprekina=["v = ?", "T = ?"],
             formulas=["v = √(GM/r)", "T = 2πr/v"],
             aprekins=["1)  v = √(4,0·10⁷) = 6,32·10³ m/s",
                       "2)  2πr = 6,28 · 1,0·10⁷ = 6,28·10⁷ m",
                       "3)  T = 6,28·10⁷ : 6,32·10³ ≈ 9,9·10³ s ≈ "
                       "2,8 h"],
             atbilde="T ≈ 9,9·10³ s ≈ 2,8 stundas",
             piezime="Jo tālāka orbīta, jo garāks periods - to precīzi "
                     "apraksta trešais Keplera likums."),
        dict(nr=6, virsraksts="Paātrinājums orbītā",
             teksts="Satelīts riņķo 7,0·10⁶ m attālumā no Zemes centra "
                    "ar\nātrumu 7,56 km/s. Pārbaudi, vai centrtieces "
                    "paātrinājums\nsakrīt ar gravitācijas lauka "
                    "intensitāti! (GM = 4,0·10¹⁴)",
             dots=["r = 7,0·10⁶ m", "v = 7,56·10³ m/s"],
             jaaprekina=["a(centr) = ?", "g = ?"],
             formulas=["a = v²/r", "g = GM/r²"],
             aprekins=["1)  v² = 5,72·10⁷ m²/s²",
                       "2)  a = 5,72·10⁷ : 7,0·10⁶ = 8,2 m/s²",
                       "3)  g = 4,0·10¹⁴ : 4,9·10¹³ = 8,2 m/s² ✔"],
             atbilde="Abi rezultāti sakrīt: a = g ≈ 8,2 m/s².",
             piezime="Satelīts nepārtraukti brīvi krīt - tāpēc tajā ir "
                     "bezsvara stāvoklis."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Orbītā gravitācija darbojas kā centrtieces spēks.",
            "v = √(GM/r) - nav atkarīgs no satelīta masas.",
            "T = 2πr/v; jo tālāka orbīta, jo garāks periods.",
            "Orbīta ir nepārtraukta brīvā krišana ar sānu ātrumu.",
        ],
        majasdarbs=[
            "h = 300 km. Aprēķini v un T.",
            "Kā mainīsies v, ja r samazina 9 reizes?",
            "Paskaidro Ņūtona lielgabala domu eksperimentu saviem "
            "vārdiem.",
        ],
        pasvertejums=["Protu pamatot orbītas nosacījumu",
                      "Protu rēķināt orbitālo ātrumu",
                      "Protu rēķināt periodu",
                      "Protu izskaidrot, kāpēc satelīts nekrīt"],
        nakama="Nākamā stunda: pirmais kosmiskais ātrums."),
),

dict(
    nr="4.6", virsraksts="Pirmais kosmiskais ātrums",
    jautajums="Cik ātri jālido, lai paliktu orbītā?",
    apaksraksts="v₁ = √(gR) = 7,9 km/s · Otrais kosmiskais ātrums",
    merkis="Iemācīties aprēķināt pirmo kosmisko ātrumu un saprast otrā "
           "kosmiskā ātruma nozīmi.",
    protu=["aprēķināt pirmo kosmisko ātrumu;",
           "lietot vienkāršoto formulu v₁ = √(gR);",
           "nosaukt otrā kosmiskā ātruma nozīmi;",
           "salīdzināt kosmiskos ātrumus dažādām planētām."],
    atkartojums="4.5. stundā: v = √(GM/r). Ja r = R (orbīta tieši pie "
                "virsmas), iegūstam pirmo kosmisko ātrumu.",
    uzdevumu_apraksts="Kosmiskie ātrumi dažādām planētām",
    teorija=[
        ("Pirmais kosmiskais ātrums", [
            ("formula", "PIRMAIS KOSMISKAIS ĀTRUMS",
             "v₁ = √(G · M / R) = √(g · R)        "
             "Zemei:  v₁ ≈ 7,9 km/s",
             "Tas ir minimālais ātrums, lai ķermenis kļūtu par Zemes "
             "pavadoni. Formula v₁ = √(gR) ir ērtāka, jo neprasa G un M.",
             GOLD),
            ("divi",
             ("PIRMAIS  v₁ = √(gR)", BLUE,
              ["Riņķa orbīta ap planētu.",
               "Zemei 7,9 km/s.",
               "Ķermenis paliek orbītā."]),
             ("OTRAIS  v₂ = √(2gR)", RED,
              ["Aizlidošana no planētas.",
               "Zemei 11,2 km/s.",
               "v₂ = v₁ · √2."])),
        ]),
        ("Kosmiskie ātrumi", [
            ("tabula",
             ["Debess ķermenis", "v₁", "v₂", "Piezīme"],
             [["Zeme", "7,9 km/s", "11,2 km/s", "Standarta"],
              ["Mēness", "1,7 km/s", "2,4 km/s", "Viegli pamest"],
              ["Marss", "3,6 km/s", "5,0 km/s", "Nākotnes misijas"],
              ["Jupiters", "42 km/s", "60 km/s", "Ļoti grūti"]],
             [4.30, 2.60, 2.60, 2.73]),
            ("panelis", "KĀPĒC MĒNESIM NAV ATMOSFĒRAS",
             ["Gāzu molekulu ātrumi ir daži km/s. Uz Mēness otrais "
              "kosmiskais ātrums ir tikai 2,4 km/s, tāpēc ātrākās "
              "molekulas laika gaitā aizlidojušas prom. Zemei ar "
              "11,2 km/s atmosfēra saglabājas."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Pirmais kosmiskais ātrums Zemei",
             teksts="Aprēķini pirmo kosmisko ātrumu Zemei!\n"
                    "(g = 9,8 m/s²; R = 6,4·10⁶ m)",
             dots=["g = 9,8 m/s²", "R = 6,4·10⁶ m"],
             jaaprekina=["v₁ = ?"],
             formulas=["v₁ = √(gR)"],
             aprekins=["1)  gR = 9,8 · 6,4·10⁶ = 6,27·10⁷ m²/s²",
                       "2)  v₁ = √(6,27·10⁷)",
                       "3)  v₁ = 7,92·10³ m/s ≈ 7,9 km/s"],
             atbilde="v₁ ≈ 7,9 km/s",
             piezime="Aptuveni 28 500 km/h - 23 reizes ātrāk par skaņu."),
        dict(nr=2, virsraksts="Otrais kosmiskais ātrums",
             teksts="Aprēķini otro kosmisko ātrumu Zemei un paskaidro,\n"
                    "ko tas nozīmē!",
             dots=["v₁ = 7,9 km/s"],
             jaaprekina=["v₂ = ?"],
             formulas=["v₂ = v₁ · √2"],
             aprekins=["1)  √2 = 1,414",
                       "2)  v₂ = 7,9 · 1,414",
                       "3)  v₂ = 11,2 km/s"],
             atbilde="v₂ ≈ 11,2 km/s - ātrums, lai pilnībā pamestu "
                     "Zemes gravitācijas lauku.",
             piezime="Ar šo ātrumu lidoja Apollo misijas uz Mēnesi."),
        dict(nr=3, virsraksts="Kosmiskais ātrums Mēnesim",
             teksts="Aprēķini pirmo kosmisko ātrumu Mēnesim!\n"
                    "(g = 1,6 m/s²; R = 1,7·10⁶ m)",
             dots=["g = 1,6 m/s²", "R = 1,7·10⁶ m"],
             jaaprekina=["v₁ = ?"],
             formulas=["v₁ = √(gR)"],
             aprekins=["1)  gR = 1,6 · 1,7·10⁶ = 2,72·10⁶ m²/s²",
                       "2)  v₁ = √(2,72·10⁶)",
                       "3)  v₁ = 1,65·10³ ≈ 1,7 km/s"],
             atbilde="v₁ ≈ 1,7 km/s - gandrīz 5 reizes mazāks nekā Zemei.",
             piezime="Tāpēc Apollo lunārais modulis varēja pacelties ar "
                     "nelielu dzinēju."),
        dict(nr=4, virsraksts="Melnais caurums",
             teksts="Ķermenim ar masu M un rādiusu R otrais kosmiskais\n"
                    "ātrums sasniedz gaismas ātrumu. Kāds ir R?\n"
                    "(v₂ = √(2GM/R); c = 3,0·10⁸ m/s;\n"
                    "M = 6,0·10²⁴ kg; G = 6,67·10⁻¹¹)",
             dots=["v₂ = c = 3,0·10⁸ m/s", "M = 6,0·10²⁴ kg"],
             jaaprekina=["R = ?"],
             formulas=["c² = 2GM/R", "R = 2GM/c²"],
             aprekins=["1)  2GM = 2 · 6,67·10⁻¹¹ · 6,0·10²⁴ = 8,0·10¹⁴",
                       "2)  c² = 9,0·10¹⁶ m²/s²",
                       "3)  R = 8,0·10¹⁴ : 9,0·10¹⁶ ≈ 8,9·10⁻³ m ≈ "
                       "9 mm"],
             atbilde="R ≈ 9 mm - Zemei būtu jāsaspiež līdz lodītes "
                     "izmēram.",
             piezime="Šo rādiusu sauc par Švarcšilda rādiusu; tā rodas "
                     "melnie caurumi."),
        dict(nr=5, virsraksts="Kosmiskais ātrums Marsam",
             teksts="Aprēķini pirmo kosmisko ātrumu Marsam!\n"
                    "(g = 3,7 m/s²; R = 3,4·10⁶ m)",
             dots=["g = 3,7 m/s²", "R = 3,4·10⁶ m"],
             jaaprekina=["v₁ = ?"],
             formulas=["v₁ = √(gR)"],
             aprekins=["1)  gR = 3,7 · 3,4·10⁶ = 1,26·10⁷ m²/s²",
                       "2)  v₁ = √(1,26·10⁷)",
                       "3)  v₁ = 3,55·10³ ≈ 3,6 km/s"],
             atbilde="v₁ ≈ 3,6 km/s",
             piezime="Divreiz mazāk nekā Zemei - tāpēc atgriešanās no "
                     "Marsa prasa mazāk degvielas."),
        dict(nr=6, virsraksts="Otrais kosmiskais ātrums Mēnesim",
             teksts="Mēnesim pirmais kosmiskais ātrums ir 1,7 km/s.\n"
                    "Aprēķini otro kosmisko ātrumu! (√2 = 1,41)",
             dots=["v₁ = 1,7 km/s"],
             jaaprekina=["v₂ = ?"],
             formulas=["v₂ = v₁√2"],
             aprekins=["1)  √2 = 1,41",
                       "2)  v₂ = 1,7 · 1,41",
                       "3)  v₂ = 2,4 km/s"],
             atbilde="v₂ ≈ 2,4 km/s",
             piezime="Gāzu molekulu ātrumi ir tuvu šai vērtībai - tāpēc "
                     "Mēness nav noturējis atmosfēru."),
        dict(nr=7, virsraksts="Kosmiskais ātrums no GM",
             teksts="Planētai GM = 1,2·10¹⁴ m³/s² un R = 3,0·10⁶ m.\n"
                    "Aprēķini pirmo kosmisko ātrumu!",
             dots=["GM = 1,2·10¹⁴ m³/s²", "R = 3,0·10⁶ m"],
             jaaprekina=["v₁ = ?"],
             formulas=["v₁ = √(GM/R)"],
             aprekins=["1)  GM/R = 1,2·10¹⁴ : 3,0·10⁶",
                       "2)  = 4,0·10⁷ m²/s²",
                       "3)  v₁ = √(4,0·10⁷) = 6,3·10³ m/s"],
             atbilde="v₁ ≈ 6,3 km/s",
             piezime="Formulas v₁ = √(gR) un v₁ = √(GM/R) ir viena un tā "
                     "pati, jo g = GM/R²."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "v₁ = √(gR) - pirmais kosmiskais ātrums; Zemei 7,9 km/s.",
            "v₂ = v₁·√2 - otrais kosmiskais ātrums; Zemei 11,2 km/s.",
            "v₁ nav atkarīgs no raķetes masas.",
            "Mazs v₂ nozīmē, ka planēta nespēj noturēt atmosfēru.",
        ],
        majasdarbs=[
            "Marss: g = 3,7 m/s², R = 3,4·10⁶ m. Aprēķini v₁ un v₂.",
            "Aprēķini v₁ planētai ar g = 20 m/s² un R = 7,0·10⁶ m.",
            "Paskaidro, kāpēc Merkuram nav biezas atmosfēras.",
        ],
        pasvertejums=["Protu rēķināt v₁",
                      "Protu rēķināt v₂",
                      "Protu salīdzināt planētas",
                      "Protu izskaidrot atmosfēras noturēšanu"],
        nakama="Nākamā stunda: mākslīgie pavadoņi."),
),

dict(
    nr="4.7", virsraksts="Mākslīgie pavadoņi",
    jautajums="Kāpēc daži pavadoņi «karājas» virs viena punkta?",
    apaksraksts="Ģeostacionārā orbīta · Orbītu veidi · Lietojumi",
    merkis="Iemācīties raksturot dažādas satelītu orbītas un saprast "
           "ģeostacionārās orbītas nosacījumu.",
    protu=["nosaukt orbītu veidus un to lietojumus;",
           "aprēķināt ģeostacionārās orbītas rādiusu;",
           "pamatot, kāpēc tā ir tikai viena;",
           "izskaidrot GPS darbības principu."],
    atkartojums="4.5. stundā: T = 2π√(r³/GM). Ja periods ir tieši "
                "24 stundas, satelīts griežas kopā ar Zemi - un no zemes "
                "izskatās nekustīgs.",
    uzdevumu_apraksts="Orbītu aprēķini un lietojumi",
    teorija=[
        ("Orbītu veidi", [
            ("kartitas", [
                ("ZEMĀ (LEO)", BLUE,
                 ["200-2000 km.",
                  "T = 90-120 min.",
                  "KKS, Starlink, novērošana."]),
                ("VIDĒJĀ (MEO)", GREEN,
                 ["2000-35 000 km.",
                  "T = 2-24 h.",
                  "GPS, Galileo navigācija."]),
                ("ĢEOSTACIONĀRĀ (GEO)", GOLD,
                 ["35 786 km virs ekvatora.",
                  "T = 24 h.",
                  "TV, sakari, meteoroloģija."]),
            ]),
            ("formula", "ĢEOSTACIONĀRĀS ORBĪTAS NOSACĪJUMS",
             "T = 24 h = 86 400 s        r = ∛(G·M·T² / (4π²))",
             "Papildus periodam orbītai jābūt virs EKVATORA un kustībai "
             "jānotiek Zemes rotācijas virzienā. Tāpēc ģeostacionārā "
             "orbīta ir tikai viena riņķa līnija.", GOLD),
        ]),
        ("Lietojumi", [
            ("tabula",
             ["Uzdevums", "Piemērota orbīta", "Kāpēc"],
             [["Televīzija, sakari", "Ģeostacionārā", "Antena nav "
               "jāgriež"],
              ["Navigācija (GPS)", "Vidējā", "Redzami vairāki vienlaikus"],
              ["Zemes novērošana", "Zemā polārā", "Augsta izšķirtspēja"],
              ["Kosmosa stacija", "Zemā", "Ātri sasniedzama"]],
             [4.30, 3.60, 4.33]),
            ("panelis", "KĀ DARBOJAS GPS",
             ["Uztvērējs saņem signālus no vismaz 4 satelītiem un mēra "
              "signāla ceļā pavadīto laiku. No laika un gaismas ātruma "
              "aprēķina attālumu līdz katram satelītam; četru sfēru "
              "krustpunkts dod atrašanās vietu."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ģeostacionārās orbītas rādiuss",
             teksts="Aprēķini ģeostacionārās orbītas rādiusu!\n"
                    "(GM = 4,0·10¹⁴ m³/s²; T = 86 400 s; π² ≈ 9,87)",
             dots=["T = 86 400 s", "GM = 4,0·10¹⁴ m³/s²"],
             jaaprekina=["r = ?"],
             formulas=["r³ = GMT²/(4π²)"],
             aprekins=["1)  T² = 7,46·10⁹ s²",
                       "2)  r³ = 4,0·10¹⁴ · 7,46·10⁹ : 39,5 = "
                       "7,56·10²²",
                       "3)  r = ∛(7,56·10²²) ≈ 4,23·10⁷ m"],
             atbilde="r ≈ 4,2·10⁷ m = 42 000 km no Zemes centra",
             piezime="Augstums virs virsmas: 42 000 − 6400 = 35 600 km."),
        dict(nr=2, virsraksts="Ātrums ģeostacionārajā orbītā",
             teksts="Izmantojot 1. uzdevuma rezultātu, aprēķini satelīta\n"
                    "ātrumu! (π ≈ 3,14)",
             dots=["r = 4,23·10⁷ m", "T = 86 400 s"],
             jaaprekina=["v = ?"],
             formulas=["v = 2πr/T"],
             aprekins=["1)  2πr = 2 · 3,14 · 4,23·10⁷ = 2,66·10⁸ m",
                       "2)  v = 2,66·10⁸ : 86 400",
                       "3)  v ≈ 3,08·10³ m/s ≈ 3,1 km/s"],
             atbilde="v ≈ 3,1 km/s",
             piezime="Divarpus reizes lēnāk nekā KKS - tālākā orbītā "
                     "ātrums mazāks."),
        dict(nr=3, virsraksts="Signāla aizture",
             teksts="Cik ilgā laikā signāls no Zemes sasniedz "
                    "ģeostacionāro\nsatelītu un atgriežas? "
                    "(h = 3,6·10⁷ m; c = 3,0·10⁸ m/s)",
             dots=["h = 3,6·10⁷ m", "c = 3,0·10⁸ m/s"],
             jaaprekina=["t = ?"],
             formulas=["t = 2h/c"],
             aprekins=["1)  Ceļš turp un atpakaļ: 2h = 7,2·10⁷ m",
                       "2)  t = 7,2·10⁷ : 3,0·10⁸",
                       "3)  t = 0,24 s"],
             atbilde="t ≈ 0,24 s",
             piezime="Tāpēc satelīta telefonsarunās ir manāma aizture."),
        dict(nr=4, virsraksts="GPS precizitāte",
             teksts="GPS uztvērēja pulkstenis kļūdās par 1,0·10⁻⁸ s.\n"
                    "Cik liela ir attāluma kļūda? (c = 3,0·10⁸ m/s)",
             dots=["Δt = 1,0·10⁻⁸ s", "c = 3,0·10⁸ m/s"],
             jaaprekina=["Δs = ?"],
             formulas=["Δs = c · Δt"],
             aprekins=["1)  Δs = 3,0·10⁸ · 1,0·10⁻⁸",
                       "2)  Δs = 3,0 m"],
             atbilde="Δs = 3,0 m",
             piezime="Tāpēc GPS satelītos ir atomu pulksteņi ar "
                     "precizitāti 10⁻¹⁴ s."),
        dict(nr=5, virsraksts="Augstums no perioda",
             teksts="Satelīta apriņķošanas periods ir 12 h.\n"
                    "Aprēķini orbītas rādiusu un augstumu virs virsmas!\n"
                    "(GM = 4,0·10¹⁴ m³/s²; π² ≈ 9,87; R = 6,4·10⁶ m)",
             dots=["T = 12 h = 43 200 s", "GM = 4,0·10¹⁴ m³/s²"],
             jaaprekina=["r = ?", "h = ?"],
             formulas=["r³ = GMT²/(4π²)", "h = r − R"],
             aprekins=["1)  T² = 1,87·10⁹ s²",
                       "2)  r³ = 4,0·10¹⁴ · 1,87·10⁹ : 39,5 = 1,89·10²²",
                       "3)  r = 2,66·10⁷ m ;  h = 2,66·10⁷ − 6,4·10⁶ ≈ "
                       "2,0·10⁷ m"],
             atbilde="r ≈ 2,7·10⁷ m ;   h ≈ 2,0·10⁴ km",
             piezime="Tieši šādā orbītā atrodas GPS satelīti - divi "
                     "apļi diennaktī."),
        dict(nr=6, virsraksts="Polārā orbīta",
             teksts="Novērošanas satelīts riņķo 800 km augstumā.\n"
                    "Aprēķini ātrumu un periodu!\n"
                    "(GM = 4,0·10¹⁴ m³/s²; R = 6,4·10⁶ m; π ≈ 3,14)",
             dots=["h = 8,0·10⁵ m", "R = 6,4·10⁶ m"],
             jaaprekina=["v = ?", "T = ?"],
             formulas=["r = R + h", "v = √(GM/r)", "T = 2πr/v"],
             aprekins=["1)  r = 7,2·10⁶ m",
                       "2)  v = √(4,0·10¹⁴ : 7,2·10⁶) = 7,45·10³ m/s",
                       "3)  T = 6,28 · 7,2·10⁶ : 7,45·10³ ≈ 6,07·10³ s "
                       "≈ 101 min"],
             atbilde="v ≈ 7,5 km/s ;   T ≈ 1,0·10² minūtes",
             piezime="Zeme zem satelīta pagriežas, tāpēc katrā aplī tas "
                     "redz jaunu joslu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Orbītas iedala zemajās, vidējās un ģeostacionārajās.",
            "Ģeostacionārā orbīta: T = 24 h, r ≈ 42 000 km, virs "
            "ekvatora.",
            "Jo tālāka orbīta, jo mazāks ātrums un garāks periods.",
            "GPS balstās uz ļoti precīzu laika mērīšanu.",
        ],
        majasdarbs=[
            "Aprēķini orbītas rādiusu satelītam ar T = 12 h.",
            "Aprēķini signāla ceļa laiku līdz KKS (400 km) un atpakaļ.",
            "Nosauc, kura orbīta piemērota Zemes meža ugunsgrēku "
            "novērošanai, un pamato.",
        ],
        pasvertejums=["Protu nosaukt orbītu veidus",
                      "Protu rēķināt orbītas rādiusu",
                      "Protu rēķināt ātrumu orbītā",
                      "Protu izskaidrot GPS"],
        nakama="Nākamā stunda: Keplera likumi."),
),

dict(
    nr="4.8", virsraksts="Keplera likumi",
    jautajums="Kā planētas kustas ap Sauli?",
    apaksraksts="Elipse · Laukumu likums · T² ~ a³",
    merkis="Iemācīties Keplera likumus un lietot trešo likumu orbītu "
           "salīdzināšanai.",
    protu=["formulēt visus trīs Keplera likumus;",
           "lietot T₁²/T₂² = a₁³/a₂³;",
           "izskaidrot, kāpēc planēta kustas ātrāk perihēlijā;",
           "saistīt Keplera likumus ar gravitācijas likumu."],
    atkartojums="4.5. stundā ieguvām T = 2π√(r³/GM). Ja to pacel "
                "kvadrātā, iegūstam T² ~ r³ - tieši Keplera trešo "
                "likumu.",
    uzdevumu_apraksts="Keplera trešais likums orbītu salīdzināšanai",
    teorija=[
        ("Trīs likumi", [
            ("kartitas", [
                ("PIRMAIS", BLUE,
                 ["Planētas kustas pa elipsēm.",
                  "Saule - vienā fokusā.",
                  "Riņķis ir īpašs gadījums."]),
                ("OTRAIS", GREEN,
                 ["Rādiusvektors vienādos laikos",
                  "apraksta vienādus laukumus.",
                  "Tuvāk Saulei - ātrāk."]),
                ("TREŠAIS", GOLD,
                 ["T² ~ a³",
                  "a - lielās pusass garums.",
                  "Der visām planētām."]),
            ]),
            ("formula", "KEPLERA TREŠAIS LIKUMS",
             "T₁² / T₂² = a₁³ / a₂³        jeb        "
             "T² / a³ = const",
             "Konstante ir vienāda visiem ķermeņiem, kas riņķo ap vienu "
             "centru. Saules sistēmā ērti mērīt T gados un a "
             "astronomiskajās vienībās - tad T² = a³.", GOLD),
        ]),
        ("Planētu dati", [
            ("tabula",
             ["Planēta", "a, a.v.", "T, gadi", "T²/a³"],
             [["Merkurs", "0,39", "0,24", "1,00"],
              ["Zeme", "1,00", "1,00", "1,00"],
              ["Marss", "1,52", "1,88", "1,00"],
              ["Jupiters", "5,20", "11,86", "1,00"],
              ["Neptūns", "30,1", "165", "1,00"]],
             [3.30, 2.90, 2.90, 3.13]),
            ("panelis", "KĀPĒC OTRAIS LIKUMS",
             ["Tuvāk Saulei gravitācijas spēks ir lielāks, tāpēc planēta "
              "kustas ātrāk. Vienādos laika sprīžos tā veic garāku ceļu, "
              "bet rādiusvektors ir īsāks - laukums iznāk tas pats."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Perioda aprēķins",
             teksts="Planēta atrodas 4,0 a.v. attālumā no Saules.\n"
                    "Aprēķini tās apriņķošanas periodu gados!",
             dots=["a = 4,0 a.v.", "Zemei: a = 1, T = 1"],
             jaaprekina=["T = ?"],
             formulas=["T² = a³ (gados un a.v.)"],
             aprekins=["1)  a³ = 4,0³ = 64",
                       "2)  T² = 64",
                       "3)  T = 8,0 gadi"],
             atbilde="T = 8,0 gadi",
             piezime="Šī vienkāršā forma der tikai Saules sistēmā ar "
                     "gadiem un a.v."),
        dict(nr=2, virsraksts="Attāluma aprēķins",
             teksts="Asteroīda apriņķošanas periods ir 27 gadi.\n"
                    "Aprēķini tā vidējo attālumu no Saules!",
             dots=["T = 27 gadi"],
             jaaprekina=["a = ?"],
             formulas=["a³ = T²"],
             aprekins=["1)  T² = 729",
                       "2)  a³ = 729",
                       "3)  a = ∛729 = 9,0 a.v."],
             atbilde="a = 9,0 a.v.",
             piezime="Starp Saturnu (9,5 a.v.) un Jupiteru - reāls "
                     "asteroīdu apgabals."),
        dict(nr=3, virsraksts="Divi satelīti",
             teksts="Satelītam A orbītas rādiuss ir 8000 km, periods "
                    "2,0 h.\nSatelītam B rādiuss 32 000 km. Aprēķini B "
                    "periodu!",
             dots=["r(A) = 8000 km, T(A) = 2,0 h", "r(B) = 32 000 km"],
             jaaprekina=["T(B) = ?"],
             formulas=["T(B)²/T(A)² = r(B)³/r(A)³"],
             aprekins=["1)  r(B)/r(A) = 4",
                       "2)  T(B)²/T(A)² = 4³ = 64",
                       "3)  T(B) = T(A) · 8 = 16 h"],
             atbilde="T(B) = 16 h",
             piezime="Attiecību metode: kubs zem saknes dod 8."),
        dict(nr=4, virsraksts="Ātrums perihēlijā",
             teksts="Komēta perihēlijā ir 0,5 a.v. no Saules, afēlijā -\n"
                    "5,0 a.v. Cik reižu ātrums perihēlijā ir lielāks?\n"
                    "(Izmanto otro Keplera likumu.)",
             dots=["r₁ = 0,5 a.v.", "r₂ = 5,0 a.v."],
             jaaprekina=["v₁/v₂ = ?"],
             formulas=["Otrais likums: r₁v₁ = r₂v₂"],
             aprekins=["1)  Vienādos laikos vienādi laukumi",
                       "2)  v₁/v₂ = r₂/r₁",
                       "3)  = 5,0 : 0,5 = 10"],
             atbilde="Perihēlijā ātrums ir 10 reizes lielāks.",
             piezime="Tāpēc komētas pie Saules pavada tikai nedaudz "
                     "laika."),
        dict(nr=5, virsraksts="Jupitera periods",
             teksts="Jupitera vidējais attālums no Saules ir 5,2 a.v.\n"
                    "Aprēķini tā apriņķošanas periodu gados!",
             dots=["a = 5,2 a.v."],
             jaaprekina=["T = ?"],
             formulas=["T² = a³ (gados un a.v.)"],
             aprekins=["1)  a³ = 5,2³ = 140,6",
                       "2)  T² = 140,6",
                       "3)  T = √140,6 ≈ 11,9 gadi"],
             atbilde="T ≈ 11,9 gadi",
             piezime="Reālais Jupitera periods ir 11,86 gadi - sakritība "
                       "ļoti laba."),
        dict(nr=6, virsraksts="Halleja komēta",
             teksts="Halleja komētas apriņķošanas periods ir 76 gadi.\n"
                    "Aprēķini tās vidējo attālumu no Saules!",
             dots=["T = 76 gadi"],
             jaaprekina=["a = ?"],
             formulas=["a³ = T²"],
             aprekins=["1)  T² = 5776",
                       "2)  a³ = 5776",
                       "3)  a = ∛5776 ≈ 17,9 a.v."],
             atbilde="a ≈ 18 a.v.",
             piezime="Tas ir tālāk par Urānu - tāpēc komētu redzam tikai "
                     "reizi mūžā."),
        dict(nr=7, virsraksts="Perihēlijs un afēlijs",
             teksts="Komētas vidējais attālums ir 17,9 a.v., perihēlijs -\n"
                    "0,6 a.v. Aprēķini afēlija attālumu!",
             dots=["a = 17,9 a.v.", "r(per) = 0,6 a.v."],
             jaaprekina=["r(af) = ?"],
             formulas=["r(per) + r(af) = 2a"],
             aprekins=["1)  2a = 2 · 17,9 = 35,8 a.v.",
                       "2)  r(af) = 35,8 − 0,6",
                       "3)  r(af) = 35,2 a.v."],
             atbilde="r(af) ≈ 35 a.v.",
             piezime="Elipses lielās ass puse ir tieši abu galējo "
                     "attālumu vidējais aritmētiskais."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Planētas kustas pa elipsēm ar Sauli vienā fokusā.",
            "Rādiusvektors vienādos laikos apraksta vienādus laukumus.",
            "T² ~ a³; Saules sistēmā (gados, a.v.) T² = a³.",
            "Keplera likumi izriet no gravitācijas likuma.",
        ],
        majasdarbs=[
            "a = 9,0 a.v. Aprēķini T.",
            "T = 8,0 gadi. Aprēķini a.",
            "r(A) = 10 000 km, T(A) = 3,0 h; r(B) = 40 000 km. Aprēķini "
            "T(B).",
        ],
        pasvertejums=["Protu formulēt visus trīs likumus",
                      "Protu lietot T² ~ a³",
                      "Protu izskaidrot laukumu likumu",
                      "Protu salīdzināt orbītas"],
        nakama="Nākamā stunda: uzdevumi par pavadoņiem un orbītām."),
),

]
