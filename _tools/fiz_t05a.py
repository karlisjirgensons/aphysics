# -*- coding: utf-8 -*-
"""5. temats "Enerģija un darbs". A daļa: 5.1.-5.7. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "5. temats. Enerģija un darbs"
KICKER = "FIZIKA I · 10. KLASE · 5. TEMATS: ENERĢIJA UN DARBS"
KURSS = "FIZIKA I · 10. KLASE"
MAPE = "C:/aphysics/Fizika_1/5. Enerģija un darbs"

STUNDAS = [

dict(
    nr="5.1", virsraksts="Mehāniskais darbs",
    jautajums="Kad spēks veic darbu?",
    apaksraksts="A = Fs cos α · [A] = džouls · Darbs var būt nulle",
    merkis="Iemācīties aprēķināt mehānisko darbu un saprast, kad spēks "
           "darbu neveic.",
    protu=["definēt mehānisko darbu;",
           "aprēķināt A = Fs cos α;",
           "noteikt darba zīmi;",
           "nosaukt gadījumus, kad darbs ir nulle."],
    atkartojums="3. tematā mācījāmies par spēkiem. Tagad skatīsimies, ko "
                "spēks PAVEIC - un tas ir atkarīgs arī no ceļa.",
    uzdevumu_apraksts="Darba aprēķins dažādos virzienos",
    teorija=[
        ("Mehāniskais darbs", [
            ("formula", "DARBS",
             "A = F · s · cos α        [A] = džouls (J) = N·m",
             "α ir leņķis starp spēka un pārvietojuma virzienu. Darbu "
             "veic tikai spēka komponente PA kustības virzienu.", GOLD),
            ("kartitas", [
                ("A > 0", GREEN,
                 ["α < 90°.",
                  "Spēks palīdz kustībai.",
                  "Piemērs: vilkšana."]),
                ("A < 0", RED,
                 ["α > 90°.",
                  "Spēks pretojas kustībai.",
                  "Piemērs: berze."]),
                ("A = 0", GREY,
                 ["α = 90° vai s = 0.",
                  "Piemērs: somas nešana",
                  "horizontāli."]),
            ]),
        ]),
        ("Kad darbs ir nulle", [
            ("tabula",
             ["Situācija", "Kāpēc A = 0", "Piezīme"],
             [["Turi somu uz vietas", "s = 0", "Nogurums nav darbs"],
              ["Nes somu horizontāli", "α = 90°", "Spēks vertikāli"],
              ["Balsta reakcija", "α = 90°", "Vienmēr perpendikulāra"],
              ["Centrtieces spēks", "α = 90°", "Riņķa kustībā"]],
             [4.30, 3.30, 4.63]),
            ("panelis", "SADZĪVES UN FIZIKAS «DARBS»",
             ["Sadzīvē «strādāt» nozīmē pūlēties. Fizikā darbs ir tikai "
              "tad, ja spēks pārvieto ķermeni. Turot smagumu nekustīgi, "
              "muskuļi nogurst, bet mehāniskais darbs ir nulle."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Darbs kustības virzienā",
             teksts="Kasti velk horizontāli ar 150 N spēku 12 m.\n"
                    "Aprēķini darbu!",
             dots=["F = 150 N", "s = 12 m", "α = 0°"],
             jaaprekina=["A = ?"],
             formulas=["A = Fs cos α", "cos 0° = 1"],
             aprekins=["1)  cos 0° = 1",
                       "2)  A = 150 · 12 · 1",
                       "3)  A = 1800 J = 1,8 kJ"],
             atbilde="A = 1,8·10³ J",
             piezime="Kad spēks vērsts pa kustības virzienu, formula "
                     "vienkāršojas: A = Fs."),
        dict(nr=2, virsraksts="Darbs leņķī",
             teksts="Kasti velk ar 200 N spēku, kas vērsts 60° leņķī pret\n"
                    "horizontu, 15 m attālumā. Aprēķini darbu!\n"
                    "(cos 60° = 0,50)",
             dots=["F = 200 N", "s = 15 m", "α = 60°"],
             jaaprekina=["A = ?"],
             formulas=["A = Fs cos α"],
             aprekins=["1)  cos 60° = 0,50",
                       "2)  A = 200 · 15 · 0,50",
                       "3)  A = 1500 J = 1,5 kJ"],
             atbilde="A = 1,5·10³ J",
             piezime="Puse spēka «pazūd» vertikālajā komponentē, kas "
                     "darbu neveic."),
        dict(nr=3, virsraksts="Berzes darbs",
             teksts="Kaste (m = 30 kg, µ = 0,25) pārvietota 20 m.\n"
                    "Aprēķini berzes spēka darbu! (g = 9,8 m/s²)",
             dots=["m = 30 kg", "µ = 0,25", "s = 20 m"],
             jaaprekina=["A(b) = ?"],
             formulas=["F(b) = µmg", "A = −F(b)·s"],
             aprekins=["1)  F(b) = 0,25 · 30 · 9,8 = 73,5 N",
                       "2)  Berze vērsta pretēji: α = 180°",
                       "3)  A = −73,5 · 20 = −1470 J"],
             atbilde="A(b) = −1,47·10³ J",
             piezime="Negatīvs darbs nozīmē, ka spēks atņem enerģiju."),
        dict(nr=4, virsraksts="Pacelšanas darbs",
             teksts="Cik lielu darbu veic, vienmērīgi paceļot 25 kg kravu\n"
                    "6,0 m augstumā? (g = 9,8 m/s²)",
             dots=["m = 25 kg", "h = 6,0 m", "vienmērīgi"],
             jaaprekina=["A = ?"],
             formulas=["Vienmērīgi: F = mg", "A = mgh"],
             aprekins=["1)  F = 25 · 9,8 = 245 N",
                       "2)  A = 245 · 6,0",
                       "3)  A = 1470 J ≈ 1,5 kJ"],
             atbilde="A ≈ 1,5·10³ J",
             piezime="Šis darbs pārvēršas potenciālajā enerģijā - "
                     "Ep = mgh."),
        dict(nr=5, virsraksts="Kad darbs ir nulle",
             teksts="Cilvēks nes 15 kg somu horizontāli 50 m.\n"
                    "Cik lielu darbu veic somas turēšanas spēks? "
                    "(g = 9,8 m/s²)",
             dots=["m = 15 kg", "s = 50 m", "α = 90°"],
             jaaprekina=["A = ?"],
             formulas=["A = Fs cos α", "cos 90° = 0"],
             aprekins=["1)  Spēks vērsts vertikāli augšup",
                       "2)  Pārvietojums - horizontāls, α = 90°",
                       "3)  A = F · 50 · 0 = 0"],
             atbilde="A = 0 J",
             piezime="Fizikā darbs ir nulle, kaut arī cilvēks nogurst - "
                     "muskuļi enerģiju tērē citam nolūkam."),
        dict(nr=6, virsraksts="Spēks no darba",
             teksts="Veicot 3000 J darbu, ķermenis pārvietots 15 m\n"
                    "spēka virzienā. Cik liels bija spēks?",
             dots=["A = 3000 J", "s = 15 m", "α = 0°"],
             jaaprekina=["F = ?"],
             formulas=["A = Fs", "F = A/s"],
             aprekins=["1)  cos 0° = 1",
                       "2)  F = 3000 : 15",
                       "3)  F = 200 N"],
             atbilde="F = 200 N",
             piezime="Darba formulu var izteikt pret jebkuru no trim "
                     "lielumiem."),
        dict(nr=7, virsraksts="Kopējais darbs",
             teksts="Kasti velk ar 250 N spēku 20 m; berzes spēks "
                    "100 N.\nAprēķini katra spēka darbu un kopējo darbu!",
             dots=["F = 250 N", "F(b) = 100 N", "s = 20 m"],
             jaaprekina=["A(vilk) = ?", "A(b) = ?", "A(kop) = ?"],
             formulas=["A = Fs cos α", "A(kop) = ΣA"],
             aprekins=["1)  A(vilk) = 250 · 20 = 5000 J",
                       "2)  A(b) = −100 · 20 = −2000 J",
                       "3)  A(kop) = 5000 − 2000 = 3000 J"],
             atbilde="A(vilk) = 5,0 kJ ;  A(b) = −2,0 kJ ;  "
                     "A(kop) = 3,0 kJ",
             piezime="Kopējais darbs ir vienāds ar kinētiskās enerģijas "
                     "pieaugumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "A = Fs cos α;  [A] = džouls.",
            "Darbu veic tikai spēka komponente pa kustības virzienu.",
            "Darbs var būt pozitīvs, negatīvs vai nulle.",
            "Turot smagumu nekustīgi, mehāniskais darbs ir nulle.",
        ],
        majasdarbs=[
            "F = 80 N, s = 25 m, α = 0°. Aprēķini A.",
            "F = 120 N, s = 10 m, α = 30° (cos 30° = 0,87). Aprēķini A.",
            "m = 40 kg, µ = 0,30, s = 15 m. Aprēķini berzes darbu.",
        ],
        pasvertejums=["Protu definēt darbu",
                      "Protu rēķināt A ar leņķi",
                      "Protu noteikt darba zīmi",
                      "Protu atpazīt, kad A = 0"],
        nakama="Nākamā stunda: jauda un lietderības koeficients."),
),

dict(
    nr="5.2", virsraksts="Jauda un lietderības koeficients",
    jautajums="Kāpēc jaudīgāks dzinējs ir ātrāks?",
    apaksraksts="P = A/t · P = Fv · η = A(lietd.)/A(patēr.)",
    merkis="Iemācīties aprēķināt jaudu un lietderības koeficientu un "
           "saprast to praktisko nozīmi.",
    protu=["definēt jaudu un nosaukt mērvienību;",
           "lietot P = A/t un P = Fv;",
           "aprēķināt lietderības koeficientu;",
           "izskaidrot, kur nonāk zaudētā enerģija."],
    atkartojums="5.1. stundā: A = Fs. Bet svarīgi ir arī, cik ĀTRI darbs "
                "tiek paveikts - to raksturo jauda.",
    uzdevumu_apraksts="Jauda, ātrums un lietderība",
    teorija=[
        ("Jauda", [
            ("formula", "JAUDA",
             "P = A / t = F · v        [P] = vats (W) = J/s        "
             "1 kW = 1000 W;  1 zirgspēks ≈ 736 W",
             "Jauda rāda, cik ātri tiek veikts darbs. Formula P = Fv der "
             "vienmērīgai kustībai un ir ērta transporta uzdevumos.",
             GOLD),
            ("tabula",
             ["Objekts", "Jauda", "Piezīme"],
             [["Cilvēks ilgstoši", "70-100 W", "Kā kvēlspuldze"],
              ["Cilvēks īsu brīdi", "~1000 W", "Sprints, lēciens"],
              ["Velosipēdists", "150-400 W", "Atkarībā no trases"],
              ["Vieglā automašīna", "60-150 kW", "80-200 zirgspēki"],
              ["Vēja ģenerators", "2-5 MW", "Viena tornis"]],
             [4.60, 3.10, 4.53]),
        ]),
        ("Lietderības koeficients", [
            ("formula", "LIETDERĪBAS KOEFICIENTS",
             "η = A(lietderīgais) / A(patērētais) · 100 %        "
             "vai        η = P(lietd.) / P(patēr.) · 100 %",
             "η vienmēr ir mazāks par 100 % - daļa enerģijas pārvēršas "
             "siltumā berzes dēļ. Perpetuum mobile nav iespējams.", GOLD),
            ("kartitas", [
                ("AUGSTA η", GREEN,
                 ["Elektromotors 90-95 %.",
                  "Ģenerators ~98 %.",
                  "Maz berzes."]),
                ("VIDĒJA η", GOLD,
                 ["Dīzeļdzinējs 40-45 %.",
                  "Benzīna dzinējs 25-35 %."]),
                ("ZEMA η", RED,
                 ["Kvēlspuldze 5 %.",
                  "Tvaika mašīna 8 %.",
                  "Lielākā daļa - siltumā."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Jauda no darba",
             teksts="Celtnis paceļ 800 kg kravu 15 m augstumā 20 s laikā.\n"
                    "Aprēķini jaudu! (g = 9,8 m/s²)",
             dots=["m = 800 kg", "h = 15 m", "t = 20 s"],
             jaaprekina=["A = ?", "P = ?"],
             formulas=["A = mgh", "P = A/t"],
             aprekins=["1)  A = 800 · 9,8 · 15 = 1,176·10⁵ J",
                       "2)  P = 1,176·10⁵ : 20",
                       "3)  P = 5880 W ≈ 5,9 kW"],
             atbilde="P ≈ 5,9 kW",
             piezime="Aptuveni 8 zirgspēki - neliela celtņa jauda."),
        dict(nr=2, virsraksts="Jauda un ātrums",
             teksts="Automašīna brauc vienmērīgi 25 m/s; pretestības "
                    "spēks\n1200 N. Aprēķini dzinēja lietderīgo jaudu!",
             dots=["v = 25 m/s", "F = 1200 N"],
             jaaprekina=["P = ?"],
             formulas=["Vienmērīgi: F(vilces) = F(pretest.)", "P = Fv"],
             aprekins=["1)  F = 1200 N",
                       "2)  P = 1200 · 25",
                       "3)  P = 30 000 W = 30 kW"],
             atbilde="P = 30 kW ≈ 41 zirgspēki",
             piezime="Vienmērīgai braukšanai vajag daudz mazāku jaudu "
                     "nekā paātrināšanai."),
        dict(nr=3, virsraksts="Lietderības koeficients",
             teksts="Celtņa dzinējs patērē 8,0 kW; krava (500 kg) tiek\n"
                    "pacelta 12 m augstumā 10 s laikā.\n"
                    "Aprēķini lietderības koeficientu! (g = 9,8 m/s²)",
             dots=["P(pat) = 8000 W", "m = 500 kg", "h = 12 m",
                   "t = 10 s"],
             jaaprekina=["η = ?"],
             formulas=["A(lietd) = mgh", "P(lietd) = A/t",
                       "η = P(lietd)/P(pat) · 100 %"],
             aprekins=["1)  A = 500 · 9,8 · 12 = 58 800 J",
                       "2)  P(lietd) = 58 800 : 10 = 5880 W",
                       "3)  η = 5880 : 8000 · 100 % = 73,5 %"],
             atbilde="η ≈ 74 %",
             piezime="Pārējie 26 % aiziet berzē un trošu deformācijā."),
        dict(nr=4, virsraksts="Cilvēka jauda",
             teksts="Cilvēks (m = 70 kg) uzskrien pa kāpnēm 12 m augstumā\n"
                    "10 s laikā. Aprēķini viņa jaudu! (g = 9,8 m/s²)",
             dots=["m = 70 kg", "h = 12 m", "t = 10 s"],
             jaaprekina=["P = ?"],
             formulas=["A = mgh", "P = A/t"],
             aprekins=["1)  A = 70 · 9,8 · 12 = 8232 J",
                       "2)  P = 8232 : 10",
                       "3)  P = 823 W ≈ 0,82 kW"],
             atbilde="P ≈ 8,2·10² W",
             piezime="Vairāk nekā 1 zirgspēks - bet tikai dažas sekundes."),
        dict(nr=5, virsraksts="Darbs no jaudas",
             teksts="Dzinējs ar jaudu 2,0 kW darbojas 5,0 minūtes.\n"
                    "Cik lielu darbu tas paveic?",
             dots=["P = 2,0·10³ W", "t = 5,0 min = 300 s"],
             jaaprekina=["A = ?"],
             formulas=["P = A/t", "A = Pt"],
             aprekins=["1)  t = 5,0 · 60 = 300 s",
                       "2)  A = 2000 · 300",
                       "3)  A = 6,0·10⁵ J = 0,60 MJ"],
             atbilde="A = 6,0·10⁵ J",
             piezime="Elektrības skaitītājs to pašu rādītu kā "
                     "0,167 kWh."),
        dict(nr=6, virsraksts="Jauda zirgspēkos",
             teksts="Automašīnas dzinēja jauda ir 90 kW.\n"
                    "Izsaki to zirgspēkos! (1 zs = 735 W)",
             dots=["P = 9,0·10⁴ W", "1 zs = 735 W"],
             jaaprekina=["P (zs) = ?"],
             formulas=["P(zs) = P/735"],
             aprekins=["1)  P = 90 000 W",
                       "2)  P(zs) = 90 000 : 735",
                       "3)  P(zs) ≈ 122 zs"],
             atbilde="P ≈ 1,2·10² zirgspēki",
             piezime="Zirgspēks nav SI vienība, bet tehnikā to joprojām "
                     "lieto."),
        dict(nr=7, virsraksts="η no zudumiem",
             teksts="Dzinējs patērē 2,0 kW, no kuriem 400 W aiziet "
                    "siltumā\nun berzē. Aprēķini lietderības "
                    "koeficientu!",
             dots=["P(pat) = 2000 W", "P(zud) = 400 W"],
             jaaprekina=["P(lietd) = ?", "η = ?"],
             formulas=["P(lietd) = P(pat) − P(zud)",
                       "η = P(lietd)/P(pat) · 100 %"],
             aprekins=["1)  P(lietd) = 2000 − 400 = 1600 W",
                       "2)  η = 1600 : 2000",
                       "3)  η = 0,80 = 80 %"],
             atbilde="η = 80 %",
             piezime="Lietderības koeficients nekad nevar būt 100 % - "
                     "kaut kādi zudumi ir vienmēr."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "P = A/t = Fv;  [P] = vats.",
            "η = A(lietd)/A(patēr) · 100 %; vienmēr < 100 %.",
            "Zaudētā enerģija pārvēršas siltumā.",
            "Cilvēks ilgstoši spēj ~100 W, īsu brīdi ~1000 W.",
        ],
        majasdarbs=[
            "A = 45 kJ, t = 30 s. Aprēķini P.",
            "F = 900 N, v = 20 m/s. Aprēķini P.",
            "P(pat) = 5,0 kW, m = 400 kg, h = 8,0 m, t = 8,0 s. "
            "Aprēķini η.",
        ],
        pasvertejums=["Protu rēķināt jaudu",
                      "Protu lietot P = Fv",
                      "Protu rēķināt η",
                      "Protu izskaidrot enerģijas zudumus"],
        nakama="Nākamā stunda: uzdevumi par darbu un jaudu."),
),

dict(
    nr="5.3", virsraksts="Uzdevumi: darbs un jauda",
    jautajums="Cik jaudīgs ir cilvēks, skrienot pa kāpnēm?",
    apaksraksts="Kombinēti uzdevumi · Jauda transportā · η praksē",
    merkis="Nostiprināt darba, jaudas un lietderības uzdevumus reālās "
           "situācijās.",
    protu=["kombinēt darba un jaudas formulas;",
           "risināt uzdevumus par transportu;",
           "aprēķināt degvielas patēriņu no η;",
           "salīdzināt enerģijas avotus."],
    atkartojums="5.1. un 5.2. stunda: A = Fs cos α, P = A/t = Fv, "
                "η = A(lietd)/A(patēr). Šodien tās kombinēsim.",
    uzdevumu_apraksts="Praktiski uzdevumi par darbu, jaudu un lietderību",
    teorija=[
        ("Risinājuma shēma", [
            ("panelis", "TIPISKS CEĻŠ",
             ["1) Atrodi lietderīgo darbu (parasti mgh vai Fs).",
              "2) Ja dots laiks - aprēķini jaudu.",
              "3) Ja dots η - atrodi patērēto enerģiju:",
              "A(patēr) = A(lietd)/η",
              "4) No patērētās enerģijas var atrast degvielas "
              "daudzumu."], NAVY),
            ("formula", "DEGVIELAS PATĒRIŅŠ",
             "A(patēr) = q · m(degvielas)        ⟹        "
             "m = A(lietd) / (η · q)",
             "q ir īpatnējais sadegšanas siltums: benzīnam 4,6·10⁷ J/kg, "
             "dīzeļdegvielai 4,3·10⁷ J/kg, malkai 1,3·10⁷ J/kg.", GOLD),
        ]),
        ("Enerģijas mērvienības", [
            ("tabula",
             ["Vienība", "Džoulos", "Kur lieto"],
             [["1 J", "1", "SI pamatvienība"],
              ["1 kJ", "10³", "Pārtikas enerģija"],
              ["1 kWh", "3,6·10⁶", "Elektrības rēķini"],
              ["1 kcal", "4184", "Uzturvērtība"],
              ["1 MJ", "10⁶", "Degvielas enerģija"]],
             [3.30, 3.30, 5.63]),
            ("kartitas", [
                ("PĀRBAUDE", BLUE,
                 ["Vai jauda reāla?",
                  "Cilvēks ~100 W,",
                  "auto ~100 kW."]),
                ("η ROBEŽAS", GOLD,
                 ["Vienmēr 0 < η < 100 %.",
                  "Ja iznāk vairāk - kļūda."]),
                ("VIENĪBAS", GREEN,
                 ["kWh → J: ×3,6·10⁶",
                  "kW → W: ×1000"]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Sūkņa jauda",
             teksts="Sūknis 10 minūtēs paceļ 3,0 m³ ūdens 8,0 m augstumā.\n"
                    "Aprēķini lietderīgo jaudu! (ρ = 1000 kg/m³; "
                    "g = 9,8 m/s²)",
             dots=["V = 3,0 m³", "h = 8,0 m", "t = 600 s"],
             jaaprekina=["P = ?"],
             formulas=["m = ρV", "A = mgh", "P = A/t"],
             aprekins=["1)  m = 1000 · 3,0 = 3000 kg",
                       "2)  A = 3000 · 9,8 · 8,0 = 2,352·10⁵ J",
                       "3)  P = 2,352·10⁵ : 600 = 392 W"],
             atbilde="P ≈ 3,9·10² W",
             piezime="Reālam sūknim ar η = 60 % vajadzētu ~650 W."),
        dict(nr=2, virsraksts="Degvielas patēriņš",
             teksts="Automašīnas dzinēja η = 30 %. Cik benzīna vajag, lai\n"
                    "veiktu 2,0·10⁷ J lietderīga darba?\n"
                    "(q = 4,6·10⁷ J/kg)",
             dots=["A(lietd) = 2,0·10⁷ J", "η = 0,30",
                   "q = 4,6·10⁷ J/kg"],
             jaaprekina=["m = ?"],
             formulas=["A(patēr) = A(lietd)/η", "m = A(patēr)/q"],
             aprekins=["1)  A(patēr) = 2,0·10⁷ : 0,30 = 6,67·10⁷ J",
                       "2)  m = 6,67·10⁷ : 4,6·10⁷",
                       "3)  m = 1,45 ≈ 1,5 kg"],
             atbilde="m ≈ 1,5 kg benzīna (aptuveni 2,0 litri)",
             piezime="Divas trešdaļas enerģijas aiziet siltumā un "
                     "izplūdes gāzēs."),
        dict(nr=3, virsraksts="Vilces spēks no jaudas",
             teksts="Vilciena dzinēja jauda 4,0 MW; ātrums 90 km/h.\n"
                    "Aprēķini vilces spēku!",
             dots=["P = 4,0·10⁶ W", "v = 90 km/h = 25 m/s"],
             jaaprekina=["F = ?"],
             formulas=["P = Fv", "F = P/v"],
             aprekins=["1)  v = 90 : 3,6 = 25 m/s",
                       "2)  F = 4,0·10⁶ : 25",
                       "3)  F = 1,6·10⁵ N"],
             atbilde="F = 1,6·10⁵ N = 160 kN",
             piezime="Jo lielāks ātrums, jo mazāks vilces spēks pie tās "
                     "pašas jaudas."),
        dict(nr=4, virsraksts="Kāpnes un uzturs",
             teksts="Cilvēks (70 kg) uzkāpj 20 m augstumā. Cik lielu "
                    "darbu\nviņš veic un cik tas ir kilokalorijās?\n"
                    "(g = 9,8 m/s²; 1 kcal = 4184 J)",
             dots=["m = 70 kg", "h = 20 m"],
             jaaprekina=["A = ?", "A (kcal) = ?"],
             formulas=["A = mgh"],
             aprekins=["1)  A = 70 · 9,8 · 20 = 13 720 J",
                       "2)  A = 13 720 : 4184",
                       "3)  ≈ 3,3 kcal"],
             atbilde="A ≈ 1,4·10⁴ J ≈ 3,3 kcal",
             piezime="Cilvēka muskuļu η ≈ 25 %, tāpēc reāli patērē "
                     "~13 kcal - joprojām maz."),
        dict(nr=5, virsraksts="Lifta dzinēja jauda",
             teksts="Lifts ar kopējo masu 600 kg ceļas vienmērīgi ar\n"
                    "1,5 m/s. Aprēķini dzinēja lietderīgo jaudu! "
                    "(g = 9,8 m/s²)",
             dots=["m = 600 kg", "v = 1,5 m/s", "vienmērīgi"],
             jaaprekina=["F = ?", "P = ?"],
             formulas=["Vienmērīgi: F = mg", "P = Fv"],
             aprekins=["1)  F = 600 · 9,8 = 5880 N",
                       "2)  P = 5880 · 1,5",
                       "3)  P = 8820 W ≈ 8,8 kW"],
             atbilde="P ≈ 8,8 kW",
             piezime="Reālam liftam ar pretsvaru vajadzīgā jauda ir "
                     "vairākas reizes mazāka."),
        dict(nr=6, virsraksts="Ūdenskrituma jauda",
             teksts="Pār 20 m augstu kritumu katru sekundi plūst "
                    "200 kg\nūdens. Aprēķini plūsmas jaudu! "
                    "(g = 9,8 m/s²)",
             dots=["m = 200 kg katrā sekundē", "h = 20 m", "t = 1,0 s"],
             jaaprekina=["A = ?", "P = ?"],
             formulas=["A = mgh", "P = A/t"],
             aprekins=["1)  A = 200 · 9,8 · 20 = 39 200 J",
                       "2)  P = 39 200 : 1,0",
                       "3)  P = 3,92·10⁴ W ≈ 39 kW"],
             atbilde="P ≈ 3,9·10⁴ W",
             piezime="Ar η = 90 % hidroelektrostacija no šī krituma "
                     "iegūtu ap 35 kW."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Lietderīgais darbs parasti ir mgh vai Fs.",
            "A(patēr) = A(lietd)/η.",
            "P = Fv der vienmērīgai kustībai.",
            "1 kWh = 3,6·10⁶ J; 1 kcal = 4184 J.",
        ],
        majasdarbs=[
            "V = 5,0 m³ ūdens, h = 12 m, t = 15 min. Aprēķini P.",
            "η = 25 %, A(lietd) = 3,0·10⁷ J, q = 4,6·10⁷ J/kg. Aprēķini "
            "degvielas masu.",
            "P = 2,5 MW, v = 20 m/s. Aprēķini F.",
        ],
        pasvertejums=["Protu kombinēt formulas",
                      "Protu rēķināt degvielas patēriņu",
                      "Protu rēķināt vilces spēku",
                      "Protu pārveidot enerģijas vienības"],
        nakama="Nākamā stunda: kinētiskā enerģija."),
),

dict(
    nr="5.4", virsraksts="Kinētiskā enerģija",
    jautajums="Kāpēc ātrums ir bīstamāks par masu?",
    apaksraksts="Ek = mv²/2 · A = ΔEk · Drošība",
    merkis="Iemācīties aprēķināt kinētisko enerģiju un lietot darba un "
           "kinētiskās enerģijas teorēmu.",
    protu=["aprēķināt Ek = mv²/2;",
           "lietot A = ΔEk;",
           "pamatot, kāpēc Ek ~ v²;",
           "saistīt kinētisko enerģiju ar satiksmes drošību."],
    atkartojums="5.1. stundā: darbs maina ķermeņa stāvokli. Ja spēks "
                "paātrina ķermeni, darbs pārvēršas kustības enerģijā.",
    uzdevumu_apraksts="Kinētiskā enerģija un darba teorēma",
    teorija=[
        ("Kinētiskā enerģija", [
            ("formula", "KUSTĪBAS ENERĢIJA",
             "Ek = m v² / 2        A = ΔEk = Ek₂ − Ek₁        "
             "[Ek] = džouls",
             "Kinētiskā enerģija ir proporcionāla ātruma KVADRĀTAM. "
             "Divreiz lielāks ātrums nozīmē četrreiz lielāku enerģiju.",
             GOLD),
            ("tabula",
             ["Ātrums", "Ek (auto 1200 kg)", "Attiecība"],
             [["30 km/h", "42 kJ", "1"],
              ["50 km/h", "116 kJ", "2,8"],
              ["90 km/h", "375 kJ", "8,9"],
              ["130 km/h", "782 kJ", "18,6"]],
             [3.30, 4.30, 4.63]),
        ]),
        ("Kāpēc ātrums izšķir", [
            ("panelis", "SATIKSMES DROŠĪBA",
             ["Sadursmē visa kinētiskā enerģija dažos centimetros "
              "pārvēršas deformācijā. Braucot 100 km/h nevis 50 km/h, "
              "enerģija ir 4 reizes lielāka - un tieši tāpēc sekas ir "
              "nesalīdzināmi smagākas. Masas dubultošana enerģiju tikai "
              "divkāršo."], NAVY),
            ("divi",
             ("MASA 2×", BLUE,
              ["Ek 2× lielāka.",
               "Lineāra atkarība.",
               "Ek ~ m."]),
             ("ĀTRUMS 2×", RED,
              ["Ek 4× lielāka.",
               "Kvadrātiska atkarība.",
               "Ek ~ v²."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kinētiskā enerģija",
             teksts="Aprēķini 1400 kg automašīnas kinētisko enerģiju,\n"
                    "braucot ar 90 km/h!",
             dots=["m = 1400 kg", "v = 90 km/h = 25 m/s"],
             jaaprekina=["Ek = ?"],
             formulas=["Ek = mv²/2"],
             aprekins=["1)  v = 90 : 3,6 = 25 m/s",
                       "2)  v² = 625 m²/s²",
                       "3)  Ek = 1400 · 625 : 2 = 4,375·10⁵ J"],
             atbilde="Ek ≈ 4,4·10⁵ J = 0,44 MJ",
             piezime="Tik enerģijas atbrīvojas sadursmē."),
        dict(nr=2, virsraksts="Darbs paātrināšanai",
             teksts="Cik lielu darbu jāveic, lai 800 kg automašīnu\n"
                    "paātrinātu no 10 m/s līdz 30 m/s?",
             dots=["m = 800 kg", "v₁ = 10 m/s", "v₂ = 30 m/s"],
             jaaprekina=["A = ?"],
             formulas=["A = ΔEk = m(v₂² − v₁²)/2"],
             aprekins=["1)  v₂² − v₁² = 900 − 100 = 800 m²/s²",
                       "2)  A = 800 · 800 : 2",
                       "3)  A = 3,2·10⁵ J"],
             atbilde="A = 3,2·10⁵ J",
             piezime="Paātrināšana no 10 līdz 30 m/s prasa 8 reizes "
                     "vairāk enerģijas nekā no 0 līdz 10 m/s."),
        dict(nr=3, virsraksts="Bremzēšanas ceļš no enerģijas",
             teksts="Automašīna (1000 kg) brauc 20 m/s; bremzēšanas "
                    "spēks\n5000 N. Aprēķini bremzēšanas ceļu ar "
                    "enerģijas metodi!",
             dots=["m = 1000 kg", "v = 20 m/s", "F = 5000 N"],
             jaaprekina=["s = ?"],
             formulas=["Ek = Fs", "s = mv²/(2F)"],
             aprekins=["1)  Ek = 1000 · 400 : 2 = 2,0·10⁵ J",
                       "2)  s = Ek : F = 2,0·10⁵ : 5000",
                       "3)  s = 40 m"],
             atbilde="s = 40 m",
             piezime="Enerģijas metode dod to pašu, ko kinemātika - bet "
                     "ātrāk."),
        dict(nr=4, virsraksts="Ātruma ietekme",
             teksts="Cik reižu lielāka ir kinētiskā enerģija, braucot\n"
                    "120 km/h salīdzinājumā ar 40 km/h?",
             dots=["v₁ = 40 km/h", "v₂ = 120 km/h"],
             jaaprekina=["Ek₂/Ek₁ = ?"],
             formulas=["Ek ~ v²"],
             aprekins=["1)  v₂/v₁ = 3",
                       "2)  Ek₂/Ek₁ = 3²",
                       "3)  = 9"],
             atbilde="9 reizes lielāka.",
             piezime="Tāpēc ātruma pārsniegšana ir bīstamāka, nekā "
                     "šķiet."),
        dict(nr=5, virsraksts="Ātrums no kinētiskās enerģijas",
             teksts="Automašīnas (m = 1200 kg) kinētiskā enerģija ir\n"
                    "3,6·10⁵ J. Aprēķini tās ātrumu!",
             dots=["m = 1200 kg", "Ek = 3,6·10⁵ J"],
             jaaprekina=["v = ?"],
             formulas=["Ek = mv²/2", "v = √(2Ek/m)"],
             aprekins=["1)  2Ek = 7,2·10⁵ J",
                       "2)  v² = 7,2·10⁵ : 1200 = 600 m²/s²",
                       "3)  v = 24,5 m/s ≈ 88 km/h"],
             atbilde="v ≈ 24,5 m/s ≈ 88 km/h",
             piezime="Ticamības pārbaude: reāls automašīnas ātrums uz "
                     "šosejas ✔"),
        dict(nr=6, virsraksts="Masas ietekme",
             teksts="Kravas auto (4000 kg) un vieglā automašīna "
                    "(1000 kg)\nbrauc ar vienādu ātrumu 20 m/s. "
                    "Salīdzini to\nkinētiskās enerģijas!",
             dots=["m₁ = 4000 kg", "m₂ = 1000 kg", "v = 20 m/s"],
             jaaprekina=["Ek₁ = ?", "Ek₂ = ?"],
             formulas=["Ek = mv²/2"],
             aprekins=["1)  v² = 400 m²/s²",
                       "2)  Ek₁ = 4000 · 400 : 2 = 8,0·10⁵ J",
                       "3)  Ek₂ = 1000 · 400 : 2 = 2,0·10⁵ J"],
             atbilde="Ek₁ = 8,0·10⁵ J ;  Ek₂ = 2,0·10⁵ J - 4 reizes "
                     "vairāk.",
             piezime="Ek ir tieši proporcionāla masai - atšķirībā no "
                     "ātruma, kas ietekmē kvadrātā."),
        dict(nr=7, virsraksts="Lodes kinētiskā enerģija",
             teksts="Lodes masa ir 9,0 g, ātrums 800 m/s.\n"
                    "Aprēķini tās kinētisko enerģiju!",
             dots=["m = 9,0 g = 0,0090 kg", "v = 800 m/s"],
             jaaprekina=["Ek = ?"],
             formulas=["Ek = mv²/2"],
             aprekins=["1)  m = 0,0090 kg",
                       "2)  v² = 6,4·10⁵ m²/s²",
                       "3)  Ek = 0,0090 · 6,4·10⁵ : 2 = 2880 J"],
             atbilde="Ek ≈ 2,9·10³ J",
             piezime="Tikpat, cik 60 kg cilvēkam, kas skrien 10 m/s - "
                     "izšķir ātrums, nevis masa."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ek = mv²/2.",
            "A = ΔEk - darbs maina kinētisko enerģiju.",
            "Ek ~ v² - ātrums ietekmē kvadrātā.",
            "Enerģijas metode bieži ir ātrāka par kinemātiku.",
        ],
        majasdarbs=[
            "m = 60 kg, v = 8,0 m/s. Aprēķini Ek.",
            "m = 1500 kg, no 15 m/s līdz 25 m/s. Aprēķini A.",
            "Cik reižu mainās Ek, ātrumu palielinot 1,5 reizes?",
        ],
        pasvertejums=["Protu rēķināt Ek",
                      "Protu lietot A = ΔEk",
                      "Protu pamatot Ek ~ v²",
                      "Protu risināt ar enerģijas metodi"],
        nakama="Nākamā stunda: potenciālā enerģija."),
),

dict(
    nr="5.5", virsraksts="Potenciālā enerģija",
    jautajums="Kur «glabājas» pacelta ķermeņa enerģija?",
    apaksraksts="Ep = mgh · Ep = kx²/2 · Atskaites līmenis",
    merkis="Iemācīties aprēķināt gravitācijas un elastības potenciālo "
           "enerģiju.",
    protu=["aprēķināt Ep = mgh;",
           "aprēķināt deformētas atsperes enerģiju Ep = kx²/2;",
           "izvēlēties atskaites līmeni;",
           "pamatot, kāpēc svarīga ir tikai Ep izmaiņa."],
    atkartojums="4.11. stundā jau lietojām Ep = mgh. Tagad pievienosim "
                "arī elastības potenciālo enerģiju un precizēsim "
                "atskaites līmeņa jautājumu.",
    uzdevumu_apraksts="Potenciālā enerģija gravitācijas laukā un atsperē",
    teorija=[
        ("Divi potenciālās enerģijas veidi", [
            ("divi",
             ("GRAVITĀCIJAS", BLUE,
              ["Ep = mgh.",
               "h - augstums virs atskaites līmeņa.",
               "Var būt arī negatīva.",
               "Atskaites līmeni izvēlas brīvi."]),
             ("ELASTĪBAS", GREEN,
              ["Ep = k x² / 2.",
               "x - deformācija.",
               "Vienmēr pozitīva.",
               "Nulle nedeformētā stāvoklī."])),
            ("formula", "KĀPĒC kx²/2",
             "Ep = k x² / 2",
             "Atsperi stiepjot, spēks aug lineāri no 0 līdz kx. Vidējais "
             "spēks ir kx/2, un darbs A = (kx/2)·x = kx²/2. Tā ir "
             "laukums zem F(x) grafika - trijstūris.", GOLD),
        ]),
        ("Atskaites līmenis", [
            ("panelis", "SVARĪGA IR TIKAI IZMAIŅA",
             ["Ep vērtība ir atkarīga no izvēlētā nulles līmeņa, bet "
              "ΔEp - nav. Uzdevumā atskaites līmeni izvēlas ērti: "
              "parasti grīdas, galda vai zemākā punkta līmenī. Galvenais "
              "- to nemainīt uzdevuma vidū."], NAVY),
            ("tabula",
             ["Situācija", "Ep aprēķins", "Piezīme"],
             [["Ķermenis 5 m virs grīdas", "Ep = mg·5", "Nulle - grīda"],
              ["Ķermenis 2 m zem galda", "Ep = −mg·2", "Nulle - galds"],
              ["Atspere izstiepta 0,1 m", "Ep = k·0,01/2", "Vienmēr > 0"],
              ["Atspere saspiesta 0,1 m", "Ep = k·0,01/2", "Tāpat kā "
               "stiepē"]],
             [4.60, 3.60, 4.03]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Gravitācijas potenciālā enerģija",
             teksts="Aprēķini 12 kg ķermeņa potenciālo enerģiju 25 m\n"
                    "augstumā virs zemes! (g = 9,8 m/s²)",
             dots=["m = 12 kg", "h = 25 m", "g = 9,8 m/s²"],
             jaaprekina=["Ep = ?"],
             formulas=["Ep = mgh"],
             aprekins=["1)  mg = 12 · 9,8 = 117,6 N",
                       "2)  Ep = 117,6 · 25",
                       "3)  Ep = 2940 J ≈ 2,9 kJ"],
             atbilde="Ep ≈ 2,9·10³ J",
             piezime="Krītot šī enerģija pārvērtīsies kinētiskajā."),
        dict(nr=2, virsraksts="Atsperes enerģija",
             teksts="Atsperi (k = 400 N/m) saspiež par 15 cm.\n"
                    "Aprēķini uzkrāto potenciālo enerģiju!",
             dots=["k = 400 N/m", "x = 15 cm = 0,15 m"],
             jaaprekina=["Ep = ?"],
             formulas=["Ep = kx²/2"],
             aprekins=["1)  x² = 0,0225 m²",
                       "2)  Ep = 400 · 0,0225 : 2",
                       "3)  Ep = 4,5 J"],
             atbilde="Ep = 4,5 J",
             piezime="Ar šo enerģiju 100 g bumbiņu var izmest 4,6 m "
                     "augstumā."),
        dict(nr=3, virsraksts="Enerģijas izmaiņa",
             teksts="Ķermenis (m = 8,0 kg) pārvietots no 3,0 m augstuma\n"
                    "uz 11 m augstumu. Aprēķini ΔEp! (g = 9,8 m/s²)",
             dots=["m = 8,0 kg", "h₁ = 3,0 m", "h₂ = 11 m"],
             jaaprekina=["ΔEp = ?"],
             formulas=["ΔEp = mg(h₂ − h₁)"],
             aprekins=["1)  Δh = 11 − 3,0 = 8,0 m",
                       "2)  ΔEp = 8,0 · 9,8 · 8,0",
                       "3)  ΔEp = 627 J ≈ 6,3·10² J"],
             atbilde="ΔEp ≈ 6,3·10² J",
             piezime="Atbilde nav atkarīga no atskaites līmeņa izvēles."),
        dict(nr=4, virsraksts="Deformācijas ietekme",
             teksts="Kā mainīsies atsperes enerģija, ja deformāciju\n"
                    "palielinās 3 reizes?",
             dots=["x₂ = 3x₁", "k nemainās"],
             jaaprekina=["Ep₂/Ep₁ = ?"],
             formulas=["Ep = kx²/2", "Ep ~ x²"],
             aprekins=["1)  Ep₁ = kx₁²/2",
                       "2)  Ep₂ = k(3x₁)²/2 = 9kx₁²/2",
                       "3)  Ep₂/Ep₁ = 9"],
             atbilde="Enerģija palielināsies 9 reizes.",
             piezime="Tāpat kā kinētiskajā enerģijā - kvadrātiska "
                     "atkarība."),
        dict(nr=5, virsraksts="Deformācija no enerģijas",
             teksts="Atsperē (k = 250 N/m) uzkrāta enerģija 8,0 J.\n"
                    "Par cik tā ir deformēta?",
             dots=["k = 250 N/m", "Ep = 8,0 J"],
             jaaprekina=["x = ?"],
             formulas=["Ep = kx²/2", "x = √(2Ep/k)"],
             aprekins=["1)  2Ep = 16 J",
                       "2)  x² = 16 : 250 = 0,064 m²",
                       "3)  x = 0,25 m = 25 cm"],
             atbilde="x = 0,25 m",
             piezime="Pārbaude: Ep = 250 · 0,0625 : 2 = 7,8 J ✔"),
        dict(nr=6, virsraksts="Ep uz citas planētas",
             teksts="Ķermeni (m = 5,0 kg) paceļ 10 m augstumā uz Marsa\n"
                    "(g = 3,7 m/s²) un uz Zemes (g = 9,8 m/s²).\n"
                    "Salīdzini potenciālās enerģijas!",
             dots=["m = 5,0 kg", "h = 10 m", "g(M) = 3,7 m/s²"],
             jaaprekina=["Ep(M) = ?", "Ep(Z) = ?"],
             formulas=["Ep = mgh"],
             aprekins=["1)  Ep(M) = 5,0 · 3,7 · 10 = 185 J",
                       "2)  Ep(Z) = 5,0 · 9,8 · 10 = 490 J",
                       "3)  Attiecība 490 : 185 ≈ 2,6"],
             atbilde="Ep(M) = 1,9·10² J ;   Ep(Z) = 4,9·10² J",
             piezime="Vājākā laukā tam pašam augstumam atbilst mazāka "
                     "enerģija."),
        dict(nr=7, virsraksts="Ūdenskrātuves enerģija",
             teksts="Ūdenskrātuvē ir 5,0·10⁵ m³ ūdens, kas atrodas "
                    "vidēji\n40 m virs turbīnas. Aprēķini uzkrāto "
                    "potenciālo enerģiju!\n(ρ = 1000 kg/m³; "
                    "g = 9,8 m/s²)",
             dots=["V = 5,0·10⁵ m³", "h = 40 m", "ρ = 1000 kg/m³"],
             jaaprekina=["m = ?", "Ep = ?"],
             formulas=["m = ρV", "Ep = mgh"],
             aprekins=["1)  m = 1000 · 5,0·10⁵ = 5,0·10⁸ kg",
                       "2)  mg = 4,9·10⁹ N",
                       "3)  Ep = 4,9·10⁹ · 40 = 1,96·10¹¹ J"],
             atbilde="Ep ≈ 2,0·10¹¹ J ≈ 54 MWh",
             piezime="Tieši tā strādā hidroakumulācijas stacijas - "
                     "ūdens ir «baterija»."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ep = mgh gravitācijas laukā; Ep = kx²/2 atsperē.",
            "Atskaites līmeni izvēlas brīvi, bet nemaina uzdevuma vidū.",
            "Svarīga ir Ep IZMAIŅA, ne absolūtā vērtība.",
            "Abas potenciālās enerģijas ir kvadrātiski atkarīgas no "
            "attiecīgā lieluma vai lineāri no h.",
        ],
        majasdarbs=[
            "m = 25 kg, h = 8,0 m. Aprēķini Ep.",
            "k = 250 N/m, x = 20 cm. Aprēķini Ep.",
            "Ķermenis no 12 m uz 4,0 m, m = 15 kg. Aprēķini ΔEp.",
        ],
        pasvertejums=["Protu rēķināt Ep = mgh",
                      "Protu rēķināt atsperes enerģiju",
                      "Protu izvēlēties atskaites līmeni",
                      "Protu rēķināt ΔEp"],
        nakama="Nākamā stunda: enerģijas nezūdamība un LD4 plāns."),
),

dict(
    nr="5.6", virsraksts="Enerģijas nezūdamība un LD4 plāns",
    jautajums="Kur pazūd enerģija?",
    apaksraksts="Ek + Ep = const · Ar berzi: Ep = Ek + Q · LD4",
    merkis="Iemācīties lietot mehāniskās enerģijas nezūdamības likumu un "
           "sagatavot LD4 laboratorijas darbu.",
    protu=["formulēt enerģijas nezūdamības likumu;",
           "lietot Ek + Ep = const bez berzes;",
           "sastādīt enerģijas bilanci ar berzi;",
           "sagatavot LD4 mērījumu plānu."],
    atkartojums="5.4. un 5.5. stunda: Ek = mv²/2 un Ep = mgh. Tagad "
                "noskaidrosim, kā tās pārvēršas viena otrā.",
    uzdevumu_apraksts="Enerģijas nezūdamība un enerģijas bilance",
    teorija=[
        ("Nezūdamības likums", [
            ("formula", "MEHĀNISKĀS ENERĢIJAS NEZŪDAMĪBA",
             "Bez berzes:  Ek + Ep = const        "
             "Ar berzi:  Ek₁ + Ep₁ = Ek₂ + Ep₂ + Q",
             "Slēgtā sistēmā bez berzes mehāniskā enerģija saglabājas. "
             "Ar berzi daļa pārvēršas siltumā Q, bet KOPĒJĀ enerģija "
             "joprojām saglabājas.", GOLD),
            ("kartitas", [
                ("KRĪTOT", BLUE,
                 ["Ep samazinās,",
                  "Ek palielinās.",
                  "Summa nemainās."]),
                ("METOT AUGŠUP", GREEN,
                 ["Ek samazinās,",
                  "Ep palielinās.",
                  "Augšā Ek = 0."]),
                ("AR BERZI", RED,
                 ["Daļa pāriet siltumā.",
                  "Q = F(b)·s.",
                  "Mehāniskā enerģija sarūk."]),
            ]),
        ]),
        ("LD4 sagatavošana", [
            ("panelis", "LD4 BŪTĪBA",
             ["Lodīte noripo no augstuma h (Ep = mgh) un izlido "
              "horizontāli no galda. Pēc lidojuma attāluma nosaka "
              "ātrumu, no tā - Ek.",
              "Salīdzinot Ek ar Ep, iegūst enerģijas saglabāšanās daļu:",
              "η = Ek/Ep · 100 %"], NAVY),
            ("tabula",
             ["LD4 solis", "Mēra", "Aprēķina"],
             [["Lodītes masa", "m", "-"],
              ["Renītes augstums", "h", "Ep = mgh"],
              ["Galda augstums", "H", "-"],
              ["Lidojuma attālums", "s", "v = s√(g/(2H))"],
              ["Rezultāts", "-", "Ek = mv²/2;  η = Ek/Ep"]],
             [3.60, 3.30, 5.33]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātrums no augstuma",
             teksts="Ķermenis brīvi krīt no 20 m. Aprēķini ātrumu pie\n"
                    "zemes ar enerģijas metodi! (g = 9,8 m/s²)",
             dots=["h = 20 m", "v₀ = 0", "berzes nav"],
             jaaprekina=["v = ?"],
             formulas=["mgh = mv²/2", "v = √(2gh)"],
             aprekins=["1)  Masa saīsinās",
                       "2)  v² = 2 · 9,8 · 20 = 392 m²/s²",
                       "3)  v = 19,8 ≈ 20 m/s"],
             atbilde="v ≈ 20 m/s",
             piezime="Rezultāts nav atkarīgs no masas - tāpat kā brīvajā "
                     "krišanā."),
        dict(nr=2, virsraksts="Augstums no ātruma",
             teksts="Bumbu met vertikāli uz augšu ar 18 m/s.\n"
                    "Aprēķini maksimālo augstumu ar enerģijas metodi!\n"
                    "(g = 9,8 m/s²)",
             dots=["v₀ = 18 m/s", "v = 0 augšā"],
             jaaprekina=["h = ?"],
             formulas=["mv₀²/2 = mgh", "h = v₀²/(2g)"],
             aprekins=["1)  v₀² = 324 m²/s²",
                       "2)  h = 324 : (2 · 9,8)",
                       "3)  h = 16,5 ≈ 17 m"],
             atbilde="h ≈ 17 m",
             piezime="Tas pats rezultāts, ko dotu kinemātikas formula."),
        dict(nr=3, virsraksts="Enerģijas bilance ar berzi",
             teksts="Ķermenis (m = 2,0 kg) noslīd no 5,0 m augstuma un\n"
                    "apakšā tā ātrums ir 8,0 m/s. Cik daudz enerģijas\n"
                    "zaudēts berzē? (g = 9,8 m/s²)",
             dots=["m = 2,0 kg", "h = 5,0 m", "v = 8,0 m/s"],
             jaaprekina=["Q = ?"],
             formulas=["Ep = mgh", "Ek = mv²/2", "Q = Ep − Ek"],
             aprekins=["1)  Ep = 2,0 · 9,8 · 5,0 = 98 J",
                       "2)  Ek = 2,0 · 64 : 2 = 64 J",
                       "3)  Q = 98 − 64 = 34 J"],
             atbilde="Q = 34 J (35 % no sākuma enerģijas)",
             piezime="Enerģija nepazūd - tā pārvēršas siltumā."),
        dict(nr=4, virsraksts="Atspere un lodīte",
             teksts="Atspere (k = 500 N/m) saspiesta par 8,0 cm izmet\n"
                    "50 g lodīti vertikāli. Cik augstu tā uzlido?\n"
                    "(g = 9,8 m/s²)",
             dots=["k = 500 N/m", "x = 0,080 m", "m = 0,050 kg"],
             jaaprekina=["h = ?"],
             formulas=["kx²/2 = mgh", "h = kx²/(2mg)"],
             aprekins=["1)  Ep(ats) = 500 · 0,0064 : 2 = 1,6 J",
                       "2)  mg = 0,050 · 9,8 = 0,49 N",
                       "3)  h = 1,6 : 0,49 = 3,27 ≈ 3,3 m"],
             atbilde="h ≈ 3,3 m",
             piezime="Reāli mazāk - daļa enerģijas aiziet gaisa "
                     "pretestībā."),
        dict(nr=5, virsraksts="Ātrums slīpās plaknes galā",
             teksts="Ķermenis noslīd bez berzes no 2,0 m augstuma pa "
                    "slīpu\nplakni. Aprēķini ātrumu apakšā! "
                    "(g = 9,8 m/s²)",
             dots=["h = 2,0 m", "v₀ = 0", "berzes nav"],
             jaaprekina=["v = ?"],
             formulas=["mgh = mv²/2", "v = √(2gh)"],
             aprekins=["1)  Masa saīsinās",
                       "2)  v² = 2 · 9,8 · 2,0 = 39,2 m²/s²",
                       "3)  v = 6,26 ≈ 6,3 m/s"],
             atbilde="v ≈ 6,3 m/s",
             piezime="Plaknes leņķis un garums rezultātu neietekmē - "
                     "svarīgs ir tikai augstums."),
        dict(nr=6, virsraksts="Svārsta ātrums",
             teksts="Svārstu novirza tā, ka lodīte paceļas par 0,20 m.\n"
                    "Aprēķini tās ātrumu zemākajā punktā! "
                    "(g = 9,8 m/s²)",
             dots=["h = 0,20 m", "v₀ = 0"],
             jaaprekina=["v = ?"],
             formulas=["mgh = mv²/2", "v = √(2gh)"],
             aprekins=["1)  2gh = 2 · 9,8 · 0,20 = 3,92 m²/s²",
                       "2)  v = √3,92",
                       "3)  v = 1,98 ≈ 2,0 m/s"],
             atbilde="v ≈ 2,0 m/s",
             piezime="Svārsts ir enerģijas nezūdamības uzskatāmākais "
                     "piemērs: Ep ↔ Ek."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Bez berzes Ek + Ep = const.",
            "Ar berzi Ep = Ek + Q, kur Q = F(b)·s.",
            "Enerģijas metodē masa bieži saīsinās.",
            "Kopējā enerģija saglabājas vienmēr.",
        ],
        majasdarbs=[
            "Sagatavo LD4 protokola hipotēzi un piederumu sarakstu.",
            "h = 30 m brīvā krišana. Aprēķini v ar enerģijas metodi.",
            "m = 3,0 kg, h = 8,0 m, v(apakšā) = 10 m/s. Aprēķini Q.",
        ],
        pasvertejums=["Protu formulēt nezūdamības likumu",
                      "Protu lietot Ek + Ep = const",
                      "Protu sastādīt bilanci ar berzi",
                      "Esmu gatavs LD4"],
        nakama="Nākamā stunda: LD4 - mehāniskās enerģijas nezūdamības "
               "pārbaude."),
),

dict(
    nr="5.7", virsraksts="LD4 datu analīze",
    jautajums="Vai enerģija tiešām saglabājās?",
    apaksraksts="η = Ek/Ep · Zudumu analīze · Secinājumi",
    merkis="Apstrādāt LD4 mērījumus, aprēķināt enerģijas saglabāšanās "
           "daļu un pamatot, kur nonāk trūkstošā enerģija.",
    protu=["aprēķināt ātrumu no lidojuma attāluma;",
           "aprēķināt Ep un Ek;",
           "aprēķināt η un to interpretēt;",
           "pamatot enerģijas zudumu cēloņus."],
    atkartojums="LD4 mērījumi ir veikti. Tagad no tiem jāiegūst atbilde: "
                "cik liela mehāniskās enerģijas daļa saglabājās?",
    uzdevumu_apraksts="LD4 datu apstrāde un interpretācija",
    teorija=[
        ("Aprēķina ceļš", [
            ("formula", "NO MĒRĪJUMIEM UZ ENERĢIJU",
             "v = s · √(g / (2H))        Ep = m g h        "
             "Ek = m v² / 2        η = Ek / Ep · 100 %",
             "H ir galda augstums (vertikālā krišana), h - renītes "
             "augstums (sākuma potenciālā enerģija), s - horizontālais "
             "lidojuma attālums.", GOLD),
            ("tabula",
             ["Tipisks η", "Ko tas nozīmē", "Rīcība"],
             [["85-95 %", "Ļoti labs mērījums", "Rezultāts derīgs"],
              ["60-85 %", "Normāls skolas rezultāts", "Analizē zudumus"],
              ["40-60 %", "Lieli zudumi", "Pārbauda renīti"],
              ["> 100 %", "Kļūda mērījumos", "Pārbauda h un H"]],
             [3.30, 4.60, 4.33]),
        ]),
        ("Kur nonāk enerģija", [
            ("kartitas", [
                ("ROTĀCIJA", BLUE,
                 ["Lodīte griežas.",
                  "Līdz 29 % enerģijas.",
                  "Netiek ieskaitīta Ek = mv²/2."]),
                ("BERZE", RED,
                 ["Renīte un gaiss.",
                  "5-15 %.",
                  "Pārvēršas siltumā."]),
                ("MĒRĪJUMU KĻŪDAS", GOLD,
                 ["h, H un s neprecizitāte.",
                  "3-10 %.",
                  "Samazina ar atkārtojumiem."]),
            ]),
            ("panelis", "SVARĪGAKAIS SECINĀJUMS",
             ["η < 100 % NAV pretrunā ar enerģijas nezūdamības likumu. "
              "Enerģija nepazūd - tā pāriet rotācijā un siltumā. "
              "Nezūdamības likums attiecas uz VISU enerģiju, ne tikai uz "
              "translācijas kinētisko enerģiju."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātrums no lidojuma",
             teksts="Galda augstums H = 0,90 m; lodīte nolidoja "
                    "s = 0,62 m.\nAprēķini izlidošanas ātrumu! "
                    "(g = 9,8 m/s²)",
             dots=["H = 0,90 m", "s = 0,62 m", "g = 9,8 m/s²"],
             jaaprekina=["v = ?"],
             formulas=["t = √(2H/g)", "v = s/t"],
             aprekins=["1)  t = √(1,80 : 9,8) = √0,184 = 0,428 s",
                       "2)  v = 0,62 : 0,428",
                       "3)  v = 1,45 ≈ 1,4 m/s"],
             atbilde="v ≈ 1,4 m/s",
             piezime="Var arī tieši: v = s√(g/(2H)) = 0,62 · 2,33 = "
                     "1,45 m/s ✔"),
        dict(nr=2, virsraksts="Enerģiju salīdzinājums",
             teksts="Lodītes masa 25 g, renītes augstums h = 0,15 m,\n"
                    "izlidošanas ātrums 1,45 m/s. Aprēķini Ep, Ek un η!\n"
                    "(g = 9,8 m/s²)",
             dots=["m = 0,025 kg", "h = 0,15 m", "v = 1,45 m/s"],
             jaaprekina=["Ep = ?", "Ek = ?", "η = ?"],
             formulas=["Ep = mgh", "Ek = mv²/2", "η = Ek/Ep · 100 %"],
             aprekins=["1)  Ep = 0,025 · 9,8 · 0,15 = 0,0368 J",
                       "2)  Ek = 0,025 · 2,10 : 2 = 0,0263 J",
                       "3)  η = 0,0263 : 0,0368 · 100 % = 71 %"],
             atbilde="Ep = 0,037 J ;  Ek = 0,026 J ;  η ≈ 71 %",
             piezime="Tipisks rezultāts - lielākā daļa zudumu ir "
                     "rotācijā."),
        dict(nr=3, virsraksts="Rotācijas devums",
             teksts="Ripojošai lodītei rotācijas enerģija ir 2/5 no\n"
                    "translācijas enerģijas. Kāds būtu η, ja citu\n"
                    "zudumu nebūtu?",
             dots=["Ek(rot) = 0,4 · Ek(transl)"],
             jaaprekina=["η = ?"],
             formulas=["Ep = Ek(transl) + Ek(rot)",
                       "η = Ek(transl)/Ep"],
             aprekins=["1)  Ep = Ek + 0,4Ek = 1,4Ek",
                       "2)  η = Ek : 1,4Ek",
                       "3)  η = 0,714 = 71,4 %"],
             atbilde="η ≈ 71 % - tieši tik, cik izmērīts.",
             piezime="Tas parāda, ka galvenais «zudums» patiesībā ir "
                     "rotācija, nevis berze."),
        dict(nr=4, virsraksts="Secinājuma formulēšana",
             teksts="Uzraksti LD4 secinājumu, izmantojot 2. un "
                    "3. uzdevuma\nrezultātus!",
             dots=["η ≈ 71 %", "rotācija dod ~29 %"],
             jaaprekina=["secinājums = ?"],
             formulas=["Atbilde + skaitļi + skaidrojums"],
             aprekins=["1)  Translācijas Ek ir 71 % no sākuma Ep",
                       "2)  Trūkstošie 29 % nonāk lodītes rotācijā un "
                       "berzē",
                       "3)  Rezultāts nav pretrunā ar nezūdamības "
                       "likumu"],
             atbilde="Mehāniskā enerģija saglabājas; translācijas Ek ir "
                     "71 % no Ep, pārējais - rotācijā un berzē.",
             piezime="Tieši šāda struktūra tiek vērtēta LD4 protokolā."),
        dict(nr=5, virsraksts="LD4 mērījuma kļūda",
             teksts="Mērījumi: s = (0,62 ± 0,01) m un\n"
                    "H = (0,90 ± 0,005) m. Novērtē ātruma relatīvo "
                    "kļūdu!\n(v = s·√(g/(2H)))",
             dots=["δs no Δs = 0,01 m", "δH no ΔH = 0,005 m"],
             jaaprekina=["δs = ?", "δH = ?", "δv = ?"],
             formulas=["δs = Δs/s", "δH = ΔH/H", "δv = δs + ½δH"],
             aprekins=["1)  δs = 0,01 : 0,62 = 1,6 %",
                       "2)  δH = 0,005 : 0,90 = 0,6 % → ½δH = 0,3 %",
                       "3)  δv = 1,6 + 0,3 = 1,9 %"],
             atbilde="δv ≈ 1,9 % → v = (1,45 ± 0,03) m/s",
             piezime="Zem saknes esošā lieluma kļūdu ņem uz pusi - "
                     "tāpēc augstuma mērījums ir mazāk kritisks."),
        dict(nr=6, virsraksts="Divi renītes augstumi",
             teksts="Pie h = 0,15 m izmērīts v = 1,45 m/s.\n"
                    "Kāds ātrums teorētiski būtu pie h = 0,30 m, ja η "
                    "nemainās?\n(√2 = 1,41)",
             dots=["h₁ = 0,15 m, v₁ = 1,45 m/s", "h₂ = 0,30 m"],
             jaaprekina=["v₂ = ?"],
             formulas=["v ~ √h", "v₂ = v₁√(h₂/h₁)"],
             aprekins=["1)  h₂/h₁ = 2",
                       "2)  v₂/v₁ = √2 = 1,41",
                       "3)  v₂ = 1,45 · 1,41 ≈ 2,05 m/s"],
             atbilde="v₂ ≈ 2,0 m/s",
             piezime="Augstums divkāršojas, ātrums pieaug tikai "
                     "1,41 reizes - to pašu redzējām 1.13. stundā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "v = s√(g/(2H)) - ātrums no horizontālā lidojuma.",
            "η = Ek/Ep · 100 % - enerģijas saglabāšanās daļa.",
            "Galvenais «zudums» ripojošai lodītei ir rotācija.",
            "η < 100 % nav pretrunā ar nezūdamības likumu.",
        ],
        majasdarbs=[
            "Pabeidz LD4 protokolu un iesniedz e-klasē.",
            "H = 1,0 m, s = 0,70 m. Aprēķini v.",
            "m = 30 g, h = 0,20 m, v = 1,6 m/s. Aprēķini η.",
        ],
        pasvertejums=["Protu aprēķināt v no lidojuma",
                      "Protu salīdzināt Ep un Ek",
                      "Protu aprēķināt η",
                      "Protu pamatot enerģijas zudumus"],
        nakama="Nākamā stunda: impulss."),
),

]
