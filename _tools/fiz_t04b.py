# -*- coding: utf-8 -*-
"""4. temats. B daļa: 4.9.-4.15. stunda (orbītas, enerģija, PD5)."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t04a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="4.9", virsraksts="Uzdevumi: pavadoņi un orbītas",
    jautajums="Cik ilgs ir pavadoņa apriņķojums?",
    apaksraksts="Kombinēti uzdevumi · Keplera likums · Attiecības",
    merkis="Nostiprināt orbītu uzdevumus, kombinējot gravitācijas "
           "likumu, centrtieces paātrinājumu un Keplera likumus.",
    protu=["izvēlēties piemērotu formulu orbītas uzdevumam;",
           "kombinēt v, T un r sakarības;",
           "lietot attiecību metodi orbītām;",
           "pārbaudīt rezultāta ticamību."],
    atkartojums="Mums ir v = √(GM/r), T = 2πr/v un T² ~ r³. Šodien "
                "mācāmies izvēlēties īsāko ceļu līdz atbildei.",
    uzdevumu_apraksts="Orbītu kombinētie uzdevumi",
    teorija=[
        ("Formulu kopa", [
            ("formula", "ORBITĀLĀS KUSTĪBAS SAKARĪBAS",
             "v = √(G M / r)   ·   T = 2π r / v   ·   "
             "T = 2π √(r³ / (G M))   ·   a = v²/r = G M / r²",
             "Visas izriet no viena nosacījuma: gravitācija ir "
             "centrtieces spēks. Satelīta masa nekur neparādās.", GOLD),
            ("tabula",
             ["Ja dots", "Jāatrod", "Īsākais ceļš"],
             [["M un r", "v", "v = √(GM/r)"],
              ["M un r", "T", "T = 2π√(r³/GM)"],
              ["r un T", "v", "v = 2πr/T"],
              ["Divi satelīti", "T attiecība", "T² ~ r³"],
              ["r un v", "M", "M = v²r/G"]],
             [3.60, 3.30, 5.33]),
        ]),
        ("Ticamības pārbaude", [
            ("panelis", "ORIENTIERI, KAS JĀZINA",
             ["Zemā orbīta: v ≈ 7,7 km/s, T ≈ 90 min. Ģeostacionārā: "
              "v ≈ 3,1 km/s, T = 24 h. Mēness: v ≈ 1,0 km/s, T ≈ 27 d. "
              "Ja atbilde krasi atšķiras, meklē kļūdu."], NAVY),
            ("kartitas", [
                ("BIEŽĀKĀ KĻŪDA", RED,
                 ["r no VIRSMAS, nevis centra.",
                  "Vienmēr r = R + h."]),
                ("OTRĀ KĻŪDA", GOLD,
                 ["km netiek pārveidoti metros.",
                  "GM ir m³/s²."]),
                ("PĀRBAUDE", GREEN,
                 ["Vai v tuvu 7,9 km/s?",
                  "Vai T ir loģisks?"]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Periods no rādiusa",
             teksts="Satelīts riņķo 1600 km augstumā virs Zemes.\n"
                    "Aprēķini ātrumu un periodu!\n"
                    "(R = 6,4·10⁶ m; GM = 4,0·10¹⁴ m³/s²; π ≈ 3,14)",
             dots=["h = 1,6·10⁶ m", "R = 6,4·10⁶ m",
                   "GM = 4,0·10¹⁴ m³/s²"],
             jaaprekina=["v = ?", "T = ?"],
             formulas=["r = R + h", "v = √(GM/r)", "T = 2πr/v"],
             aprekins=["1)  r = 8,0·10⁶ m",
                       "2)  v = √(4,0·10¹⁴ : 8,0·10⁶) = √(5,0·10⁷) = "
                       "7,07·10³ m/s",
                       "3)  T = 2·3,14·8,0·10⁶ : 7,07·10³ = 7,10·10³ s "
                       "≈ 118 min"],
             atbilde="v ≈ 7,1 km/s ;   T ≈ 2,0 h",
             piezime="Augstāka orbīta nekā KKS - tāpēc lēnāk un ilgāk."),
        dict(nr=2, virsraksts="Zemes masa no Mēness kustības",
             teksts="Mēness riņķo 3,8·10⁸ m attālumā ar periodu\n"
                    "2,36·10⁶ s. Aprēķini Zemes masu!\n"
                    "(G = 6,67·10⁻¹¹; π² ≈ 9,87)",
             dots=["r = 3,8·10⁸ m", "T = 2,36·10⁶ s"],
             jaaprekina=["M = ?"],
             formulas=["T² = 4π²r³/(GM)", "M = 4π²r³/(GT²)"],
             aprekins=["1)  r³ = 5,49·10²⁵ m³",
                       "2)  4π²r³ = 39,5 · 5,49·10²⁵ = 2,17·10²⁷",
                       "3)  M = 2,17·10²⁷ : (6,67·10⁻¹¹ · 5,57·10¹²) ≈ "
                       "5,8·10²⁴ kg"],
             atbilde="M ≈ 5,8·10²⁴ kg (tabulas vērtība 5,97·10²⁴ kg)",
             piezime="Tā tiek noteikta debess ķermeņu masa - pēc to "
                     "pavadoņu kustības."),
        dict(nr=3, virsraksts="Divi satelīti",
             teksts="Satelītam A r = 7000 km un T = 97 min.\n"
                    "Satelītam B r = 28 000 km. Aprēķini T(B)!",
             dots=["r(A) = 7000 km, T(A) = 97 min", "r(B) = 28 000 km"],
             jaaprekina=["T(B) = ?"],
             formulas=["T(B)²/T(A)² = (r(B)/r(A))³"],
             aprekins=["1)  r(B)/r(A) = 4",
                       "2)  T(B)/T(A) = √(4³) = √64 = 8",
                       "3)  T(B) = 97 · 8 = 776 min ≈ 12,9 h"],
             atbilde="T(B) ≈ 13 h",
             piezime="Tuvu GPS satelītu periodam (12 h) - orbīta ir "
                     "līdzīga."),
        dict(nr=4, virsraksts="Centrtieces paātrinājums orbītā",
             teksts="Aprēķini KKS centrtieces paātrinājumu 400 km "
                    "augstumā\nun salīdzini to ar g šajā augstumā!\n"
                    "(r = 6,8·10⁶ m; v = 7,7·10³ m/s)",
             dots=["r = 6,8·10⁶ m", "v = 7,7·10³ m/s"],
             jaaprekina=["a = ?"],
             formulas=["a = v²/r"],
             aprekins=["1)  v² = 5,93·10⁷ m²/s²",
                       "2)  a = 5,93·10⁷ : 6,8·10⁶",
                       "3)  a = 8,7 m/s²"],
             atbilde="a ≈ 8,7 m/s² - tieši tik, cik g šajā augstumā.",
             piezime="Tas pierāda, ka orbītā gravitācija pilnībā "
                     "izlietojas centrtiecei."),
        dict(nr=5, virsraksts="Jupitera masa no Io kustības",
             teksts="Pavadonis Io riņķo ap Jupiteru 4,22·10⁸ m attālumā\n"
                    "ar periodu 1,53·10⁵ s. Aprēķini Jupitera masu!\n"
                    "(G = 6,67·10⁻¹¹; π² ≈ 9,87)",
             dots=["r = 4,22·10⁸ m", "T = 1,53·10⁵ s"],
             jaaprekina=["M = ?"],
             formulas=["T² = 4π²r³/(GM)", "M = 4π²r³/(GT²)"],
             aprekins=["1)  r³ = 7,52·10²⁵ m³ ;  4π²r³ = 2,97·10²⁷",
                       "2)  T² = 2,34·10¹⁰ s² ;  GT² = 1,56",
                       "3)  M = 2,97·10²⁷ : 1,56 ≈ 1,9·10²⁷ kg"],
             atbilde="M ≈ 1,9·10²⁷ kg - ap 320 Zemes masas.",
             piezime="Tā pati metode, ko lietoja Mēness kustībai, tikai "
                     "citai planētai."),
        dict(nr=6, virsraksts="Cik apļu diennaktī",
             teksts="Satelīta apriņķošanas periods ir 118 minūtes.\n"
                    "Cik apļus tas veic diennaktī?",
             dots=["T = 118 min", "t = 24 h = 1440 min"],
             jaaprekina=["N = ?"],
             formulas=["N = t/T"],
             aprekins=["1)  t = 24 · 60 = 1440 min",
                       "2)  N = 1440 : 118",
                       "3)  N ≈ 12,2 apļi"],
             atbilde="N ≈ 12 apļi diennaktī",
             piezime="KKS ar 92 min periodu paspēj 16 apļus - "
                       "kosmonauti redz 16 saullēktus dienā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Visas orbītas formulas izriet no GMm/r² = mv²/r.",
            "r vienmēr mēra no planētas CENTRA.",
            "Divu satelītu salīdzināšanai ērti lietot T² ~ r³.",
            "Debess ķermeņu masu nosaka pēc to pavadoņu kustības.",
        ],
        majasdarbs=[
            "h = 800 km. Aprēķini v un T.",
            "r(A) = 9000 km, T(A) = 2,4 h; r(B) = 36 000 km. Aprēķini "
            "T(B).",
            "Marsa pavadonis Fobs: r = 9,4·10⁶ m, T = 2,76·10⁴ s. "
            "Aprēķini Marsa masu.",
        ],
        pasvertejums=["Protu izvēlēties formulu",
                      "Protu rēķināt v un T",
                      "Protu lietot attiecību metodi",
                      "Protu atrast planētas masu"],
        nakama="Nākamā stunda: svars un pārslodze."),
),

dict(
    nr="4.10", virsraksts="Svars un pārslodze",
    jautajums="Kāpēc kosmonauti «peld»?",
    apaksraksts="Bezsvara stāvoklis · Pārslodze startā · Cilvēka robežas",
    merkis="Izprast bezsvara stāvokli un pārslodzi kā svara izmaiņas "
           "paātrinātā kustībā.",
    protu=["izskaidrot bezsvara stāvokli orbītā;",
           "aprēķināt pārslodzi raķetes startā;",
           "novērtēt cilvēka fizioloģiskās robežas;",
           "atšķirt masas un svara izmaiņas."],
    atkartojums="3.6. stundā: P = m(g ± a). Tagad to lietosim kosmosā, "
                "kur a var sasniegt vairākus g.",
    uzdevumu_apraksts="Pārslodze un bezsvara stāvoklis",
    teorija=[
        ("Bezsvara stāvoklis", [
            ("panelis", "KĀPĒC KOSMONAUTI PELD",
             ["KKS orbītā g = 8,7 m/s² - gandrīz kā uz Zemes. Bet gan "
              "stacija, gan kosmonauts brīvi krīt ar to pašu "
              "paātrinājumu, tāpēc kosmonauts nespiež uz grīdu un grīda "
              "nespiež pretī. Svars ir nulle, gravitācija - nav."], NAVY),
            ("divi",
             ("MASA", BLUE,
              ["Nemainās nekad.",
               "Inerces mērs.",
               "Arī orbītā 80 kg cilvēku",
               "grūti pastumt."]),
             ("SVARS", GOLD,
              ["Mainās ar paātrinājumu.",
               "Orbītā nulle.",
               "Startā līdz 4-5 mg.",
               "P = m(g ± a)."])),
        ]),
        ("Pārslodze", [
            ("formula", "PĀRSLODZES KOEFICIENTS",
             "n = P / (m g) = (g + a) / g        "
             "Bezsvara stāvoklī n = 0;  mierā n = 1",
             "Trenēts pilots iztur 8-9 g dažas sekundes; netrenēts "
             "cilvēks zaudē samaņu pie 4-5 g.", GOLD),
            ("tabula",
             ["Situācija", "Pārslodze n", "Ilgums"],
             [["Mierā", "1", "-"],
              ["Lifts sāk kāpt", "1,1-1,2", "2-3 s"],
              ["Raķetes starts", "3-4", "minūtes"],
              ["Iznīcinātāja manevrs", "8-9", "sekundes"],
              ["Orbītā", "0", "visu laiku"]],
             [4.30, 3.60, 4.33]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Pārslodze startā",
             teksts="Raķete paceļas ar paātrinājumu 29,4 m/s².\n"
                    "Aprēķini 75 kg kosmonauta svaru un pārslodzi!\n"
                    "(g = 9,8 m/s²)",
             dots=["m = 75 kg", "a = 29,4 m/s²", "g = 9,8 m/s²"],
             jaaprekina=["P = ?", "n = ?"],
             formulas=["P = m(g + a)", "n = (g+a)/g"],
             aprekins=["1)  g + a = 39,2 m/s²",
                       "2)  P = 75 · 39,2 = 2940 N",
                       "3)  n = 39,2 : 9,8 = 4,0"],
             atbilde="P = 2,9·10³ N ;   n = 4,0",
             piezime="Kosmonauts jūtas 4 reizes smagāks - tāpēc startā "
                     "guļ uz muguras."),
        dict(nr=2, virsraksts="Paātrinājums no pārslodzes",
             teksts="Pilots iztur pārslodzi 6,0 g. Aprēķini "
                    "paātrinājumu\nun 80 kg pilota svaru! (g = 9,8 m/s²)",
             dots=["n = 6,0", "m = 80 kg"],
             jaaprekina=["a = ?", "P = ?"],
             formulas=["n = (g+a)/g", "a = (n−1)g", "P = n·mg"],
             aprekins=["1)  a = (6,0 − 1) · 9,8 = 49 m/s²",
                       "2)  mg = 784 N",
                       "3)  P = 6,0 · 784 = 4704 N ≈ 4,7·10³ N"],
             atbilde="a = 49 m/s² ;   P ≈ 4,7·10³ N",
             piezime="Gandrīz puse tonnas - tāpēc vajadzīgs "
                     "pretpārslodzes tērps."),
        dict(nr=3, virsraksts="Svars orbītā",
             teksts="Kosmonauts (m = 70 kg) atrodas KKS 400 km "
                    "augstumā,\nkur g = 8,7 m/s². Aprēķini smaguma spēku "
                    "un svaru!",
             dots=["m = 70 kg", "g = 8,7 m/s²", "a = g (brīvā krišana)"],
             jaaprekina=["F(sm) = ?", "P = ?"],
             formulas=["F(sm) = mg", "P = m(g − a)"],
             aprekins=["1)  F(sm) = 70 · 8,7 = 609 N",
                       "2)  Stacija un kosmonauts krīt ar a = g",
                       "3)  P = 70 · (8,7 − 8,7) = 0"],
             atbilde="F(sm) ≈ 6,1·10² N ;   P = 0 N",
             piezime="Gravitācijas spēks ir liels, bet svars - nulle."),
        dict(nr=4, virsraksts="Pārslodze līkumā",
             teksts="Lidmašīna izpilda cilpu ar rādiusu 500 m ātrumā\n"
                    "180 m/s. Aprēķini pārslodzi cilpas apakšējā punktā!\n"
                    "(g = 9,8 m/s²)",
             dots=["R = 500 m", "v = 180 m/s", "g = 9,8 m/s²"],
             jaaprekina=["a = ?", "n = ?"],
             formulas=["a = v²/R", "n = (g + a)/g"],
             aprekins=["1)  v² = 3,24·10⁴ m²/s²",
                       "2)  a = 32 400 : 500 = 64,8 m/s²",
                       "3)  n = (9,8 + 64,8) : 9,8 = 7,6"],
             atbilde="n ≈ 7,6 - uz cilvēka robežas.",
             piezime="Tāpēc akrobātikas cilpas rādiusu izvēlas pēc "
                     "pieļaujamās pārslodzes."),
        dict(nr=5, virsraksts="Pārslodze bremzējot",
             teksts="Nolaišanās kapsula bremzē atmosfērā ar "
                    "paātrinājumu\n78,4 m/s². Aprēķini pārslodzi un 80 kg "
                    "kosmonauta svaru!\n(g = 9,8 m/s²)",
             dots=["a = 78,4 m/s²", "m = 80 kg", "g = 9,8 m/s²"],
             jaaprekina=["n = ?", "P = ?"],
             formulas=["n = (g + a)/g", "P = n·mg"],
             aprekins=["1)  g + a = 88,2 m/s²",
                       "2)  n = 88,2 : 9,8 = 9,0",
                       "3)  P = 9,0 · 80 · 9,8 = 7056 N ≈ 7,1·10³ N"],
             atbilde="n = 9,0 ;   P ≈ 7,1·10³ N",
             piezime="Deviņkārtīga pārslodze ir izturama tikai dažas "
                     "sekundes un tikai guļus."),
        dict(nr=6, virsraksts="Svars uz Jupitera",
             teksts="Aprēķini 70 kg cilvēka svaru uz Jupitera "
                    "(g = 26 m/s²)\nun salīdzini to ar svaru uz Zemes! "
                    "(g(Z) = 9,8 m/s²)",
             dots=["m = 70 kg", "g(J) = 26 m/s²", "g(Z) = 9,8 m/s²"],
             jaaprekina=["P(J) = ?", "P(Z) = ?"],
             formulas=["P = mg"],
             aprekins=["1)  P(J) = 70 · 26 = 1820 N",
                       "2)  P(Z) = 70 · 9,8 = 686 N",
                       "3)  P(J)/P(Z) = 1820 : 686 ≈ 2,7"],
             atbilde="P(J) ≈ 1,8·10³ N - 2,7 reizes vairāk nekā uz "
                     "Zemes.",
             piezime="Masa abās vietās ir 70 kg - mainās tikai svars."),
        dict(nr=7, virsraksts="Pārslodze cilpas augšpunktā",
             teksts="Lidmašīna cilpas augšpunktā ar rādiusu 400 m lido\n"
                    "ar 120 m/s. Aprēķini pārslodzi šajā punktā! "
                    "(g = 9,8 m/s²)",
             dots=["R = 400 m", "v = 120 m/s", "g = 9,8 m/s²"],
             jaaprekina=["a = ?", "n = ?"],
             formulas=["a = v²/R", "Augšpunktā N = m(a − g)",
                       "n = (a − g)/g"],
             aprekins=["1)  v² = 1,44·10⁴ m²/s²",
                       "2)  a = 14 400 : 400 = 36 m/s²",
                       "3)  n = (36 − 9,8) : 9,8 ≈ 2,7"],
             atbilde="n ≈ 2,7",
             piezime="Augšpunktā smaguma spēks palīdz centrtiecei, tāpēc "
                     "pārslodze ir mazāka nekā apakšā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Bezsvara stāvoklis rodas brīvā krišanā, ne gravitācijas "
            "trūkumā.",
            "Pārslodze n = (g + a)/g.",
            "Masa nemainās nekad; svars mainās ar paātrinājumu.",
            "Cilvēka robeža ir aptuveni 8-9 g īsu brīdi.",
        ],
        majasdarbs=[
            "a = 19,6 m/s², m = 65 kg. Aprēķini P un n.",
            "n = 3,5, m = 90 kg. Aprēķini a un P.",
            "Cilpa R = 800 m, v = 200 m/s. Aprēķini pārslodzi.",
        ],
        pasvertejums=["Protu izskaidrot bezsvara stāvokli",
                      "Protu rēķināt pārslodzi",
                      "Protu atšķirt masu un svaru",
                      "Protu novērtēt cilvēka robežas"],
        nakama="Nākamā stunda: gravitācijas potenciālā enerģija."),
),

dict(
    nr="4.11", virsraksts="Gravitācijas potenciālā enerģija",
    jautajums="Cik enerģijas vajag, lai paceltu kravu?",
    apaksraksts="Ep = mgh · Ep = −GMm/r · Enerģija orbītā",
    merkis="Iemācīties aprēķināt gravitācijas potenciālo enerģiju gan "
           "pie Zemes virsmas, gan kosmosā.",
    protu=["lietot Ep = mgh nelieliem augstumiem;",
           "izskaidrot, kāpēc kosmosā lieto Ep = −GMm/r;",
           "aprēķināt enerģiju pacelšanai orbītā;",
           "saistīt enerģiju ar otro kosmisko ātrumu."],
    atkartojums="Pamatskolā: Ep = mgh. Bet tā der tikai tad, ja g ir "
                "nemainīgs - proti, nelielos augstumos. Kosmosā vajag "
                "citu formulu.",
    uzdevumu_apraksts="Potenciālā enerģija un pacelšana orbītā",
    teorija=[
        ("Divas formulas", [
            ("divi",
             ("TUVU ZEMEI", BLUE,
              ["Ep = mgh.",
               "g ≈ const.",
               "Der līdz dažiem km.",
               "Atskaites līmeni izvēlas brīvi."]),
             ("KOSMOSĀ", GREEN,
              ["Ep = −G M m / r.",
               "Nulle ir bezgalībā.",
               "Der jebkurā attālumā.",
               "Vienmēr negatīva."])),
            ("formula", "KĀPĒC MĪNUSS",
             "Ep = − G · M · m / r",
             "Nulles līmeni izvēlas bezgalībā, kur mijiedarbības nav. "
             "Tuvojoties planētai, enerģija samazinās, tāpēc tā ir "
             "negatīva. Lai ķermeni aizvestu bezgalībā, jāpieliek "
             "enerģija.", GOLD),
        ]),
        ("Enerģija orbītā", [
            ("formula", "PILNĀ ENERĢIJA ORBĪTĀ",
             "E = Ek + Ep = G M m / (2r) − G M m / r = "
             "− G M m / (2r)",
             "Orbītā pilnā enerģija ir negatīva - tas nozīmē saistītu "
             "stāvokli. Ja E ≥ 0, ķermenis aizlido prom.", GOLD),
            ("tabula",
             ["Situācija", "Enerģija", "Nozīme"],
             [["E < 0", "Saistīts", "Riņķa vai elipses orbīta"],
              ["E = 0", "Robežgadījums", "Otrais kosmiskais ātrums"],
              ["E > 0", "Nesaistīts", "Aizlido bezgalībā"]],
             [3.30, 3.30, 5.63]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Enerģija pacelšanai",
             teksts="Cik enerģijas vajag, lai 500 kg kravu paceltu 40 m\n"
                    "augstumā? (g = 9,8 m/s²)",
             dots=["m = 500 kg", "h = 40 m", "g = 9,8 m/s²"],
             jaaprekina=["Ep = ?"],
             formulas=["Ep = mgh"],
             aprekins=["1)  mg = 500 · 9,8 = 4900 N",
                       "2)  Ep = 4900 · 40",
                       "3)  Ep = 1,96·10⁵ J ≈ 2,0·10⁵ J"],
             atbilde="Ep ≈ 2,0·10⁵ J = 0,20 MJ",
             piezime="Aptuveni tik enerģijas patērē elektriskā tējkanna "
                     "1,5 minūtēs."),
        dict(nr=2, virsraksts="Potenciālā enerģija orbītā",
             teksts="Aprēķini 1000 kg satelīta potenciālo enerģiju\n"
                    "7,0·10⁶ m attālumā no Zemes centra!\n"
                    "(GM = 4,0·10¹⁴ m³/s²)",
             dots=["m = 1000 kg", "r = 7,0·10⁶ m",
                   "GM = 4,0·10¹⁴ m³/s²"],
             jaaprekina=["Ep = ?"],
             formulas=["Ep = −GMm/r"],
             aprekins=["1)  GMm = 4,0·10¹⁴ · 1000 = 4,0·10¹⁷",
                       "2)  Ep = −4,0·10¹⁷ : 7,0·10⁶",
                       "3)  Ep = −5,71·10¹⁰ J"],
             atbilde="Ep ≈ −5,7·10¹⁰ J",
             piezime="Mīnusa zīme nozīmē saistītu stāvokli, nevis kļūdu."),
        dict(nr=3, virsraksts="Enerģija aizlidošanai",
             teksts="Cik enerģijas vajag, lai 1000 kg kosmosa kuģi\n"
                    "pilnībā aizvestu no Zemes virsmas bezgalībā?\n"
                    "(GM = 4,0·10¹⁴ m³/s²; R = 6,4·10⁶ m)",
             dots=["m = 1000 kg", "R = 6,4·10⁶ m"],
             jaaprekina=["E = ?"],
             formulas=["E = 0 − Ep = GMm/R"],
             aprekins=["1)  GMm = 4,0·10¹⁷",
                       "2)  E = 4,0·10¹⁷ : 6,4·10⁶",
                       "3)  E = 6,25·10¹⁰ J"],
             atbilde="E ≈ 6,3·10¹⁰ J = 63 GJ",
             piezime="Pārbaude: E = mv₂²/2 = 1000 · (11,2·10³)² : 2 = "
                     "6,3·10¹⁰ J ✔"),
        dict(nr=4, virsraksts="Enerģijas pārvērtība",
             teksts="Ķermenis (m = 2,0 kg) nokrīt no 45 m augstuma.\n"
                    "Aprēķini kinētisko enerģiju un ātrumu pie zemes!\n"
                    "(g = 9,8 m/s²)",
             dots=["m = 2,0 kg", "h = 45 m", "g = 9,8 m/s²"],
             jaaprekina=["Ek = ?", "v = ?"],
             formulas=["Ek = Ep = mgh", "v = √(2gh)"],
             aprekins=["1)  Ep = 2,0 · 9,8 · 45 = 882 J",
                       "2)  Ek = 882 J (bez gaisa pretestības)",
                       "3)  v = √(2 · 9,8 · 45) = √882 ≈ 29,7 m/s"],
             atbilde="Ek = 8,8·10² J ;   v ≈ 30 m/s",
             piezime="Potenciālā enerģija pilnībā pārvēršas kinētiskajā - "
                     "to sīkāk pētīsim 5. tematā."),
        dict(nr=5, virsraksts="Enerģija pacelšanai orbītā",
             teksts="Cik enerģijas vajag, lai 500 kg satelītu paceltu no\n"
                    "Zemes virsmas (R = 6,4·10⁶ m) līdz r = 2R?\n"
                    "(GM = 4,0·10¹⁴ m³/s²)",
             dots=["m = 500 kg", "r₁ = R = 6,4·10⁶ m", "r₂ = 2R"],
             jaaprekina=["ΔEp = ?"],
             formulas=["Ep = −GMm/r", "ΔEp = GMm/R − GMm/(2R)"],
             aprekins=["1)  GMm = 4,0·10¹⁴ · 500 = 2,0·10¹⁷",
                       "2)  ΔEp = GMm/(2R) = 2,0·10¹⁷ : 1,28·10⁷",
                       "3)  ΔEp ≈ 1,56·10¹⁰ J"],
             atbilde="ΔEp ≈ 1,6·10¹⁰ J",
             piezime="Puse no enerģijas, kas vajadzīga pilnīgai "
                     "aizlidošanai - pārējais paliek saistībā."),
        dict(nr=6, virsraksts="Augstums no enerģijas",
             teksts="Ķermenim (m = 50 kg) potenciālā enerģija attiecībā "
                    "pret\nzemi ir 4,9·10⁴ J. Kādā augstumā tas atrodas? "
                    "(g = 9,8 m/s²)",
             dots=["m = 50 kg", "Ep = 4,9·10⁴ J", "g = 9,8 m/s²"],
             jaaprekina=["h = ?"],
             formulas=["Ep = mgh", "h = Ep/(mg)"],
             aprekins=["1)  mg = 50 · 9,8 = 490 N",
                       "2)  h = 4,9·10⁴ : 490",
                       "3)  h = 100 m"],
             atbilde="h = 1,0·10² m",
             piezime="Aptuveni 33. stāva augstums."),
        dict(nr=7, virsraksts="Atskaites līmeņa izvēle",
             teksts="Grāmata (m = 0,50 kg) atrodas 0,80 m virs grīdas.\n"
                    "Aprēķini Ep attiecībā pret grīdu un pret galdu, kas "
                    "ir\n0,75 m augstumā! (g = 9,8 m/s²)",
             dots=["m = 0,50 kg", "h₁ = 0,80 m", "galds: 0,75 m"],
             jaaprekina=["Ep(grīda) = ?", "Ep(galds) = ?"],
             formulas=["Ep = mgh", "h mēra no izvēlētā līmeņa"],
             aprekins=["1)  Ep₁ = 0,50 · 9,8 · 0,80 = 3,92 J",
                       "2)  h₂ = 0,80 − 0,75 = 0,05 m",
                       "3)  Ep₂ = 0,50 · 9,8 · 0,05 = 0,245 J"],
             atbilde="Ep(grīda) ≈ 3,9 J ;   Ep(galds) ≈ 0,25 J",
             piezime="Potenciālajai enerģijai vienmēr jānorāda atskaites "
                     "līmenis - pati vērtība nav absolūta."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ep = mgh der tikai nelielos augstumos.",
            "Kosmosā Ep = −GMm/r; nulle ir bezgalībā.",
            "Negatīva enerģija nozīmē saistītu stāvokli.",
            "Aizlidošanai vajadzīgā enerģija ir GMm/R.",
        ],
        majasdarbs=[
            "m = 300 kg, h = 25 m. Aprēķini Ep.",
            "m = 500 kg, r = 8,0·10⁶ m. Aprēķini Ep.",
            "Cik enerģijas vajag 2000 kg kuģim aizlidot no Mēness? "
            "(GM = 4,9·10¹² m³/s²; R = 1,7·10⁶ m)",
        ],
        pasvertejums=["Protu lietot Ep = mgh",
                      "Protu lietot Ep = −GMm/r",
                      "Protu rēķināt aizlidošanas enerģiju",
                      "Protu izskaidrot mīnusa zīmi"],
        nakama="Nākamā stunda: uzdevumi par enerģiju gravitācijas laukā."),
),

dict(
    nr="4.12", virsraksts="Uzdevumi: enerģija gravitācijas laukā",
    jautajums="Cik enerģijas vajag palaišanai orbītā?",
    apaksraksts="Ek + Ep · Palaišanas enerģija · Enerģijas bilance",
    merkis="Nostiprināt enerģijas aprēķinus gravitācijas laukā un "
           "iemācīties sastādīt enerģijas bilanci.",
    protu=["aprēķināt pilno enerģiju orbītā;",
           "sastādīt enerģijas bilanci palaišanai;",
           "salīdzināt dažādu orbītu enerģijas;",
           "pamatot, kāpēc augstākas orbītas ir dārgākas."],
    atkartojums="4.11. stundā: Ep = −GMm/r un E = −GMm/(2r). Šodien šīs "
                "formulas lietosim praktiskiem palaišanas aprēķiniem.",
    uzdevumu_apraksts="Enerģijas bilance kosmiskajiem lidojumiem",
    teorija=[
        ("Enerģijas bilance", [
            ("formula", "ENERĢIJA PALAIŠANAI ORBĪTĀ",
             "ΔE = E(orbītā) − E(uz virsmas) = "
             "(− G M m / (2r)) − (− G M m / R)",
             "Jāpieskaita gan potenciālās enerģijas pieaugums, gan "
             "kinētiskā enerģija orbitālajam ātrumam. Zemai orbītai "
             "aptuveni 60 % enerģijas aiziet ātrumam.", GOLD),
            ("tabula",
             ["Orbīta", "Augstums", "Enerģija uz 1 kg"],
             [["Zemā (LEO)", "400 km", "≈ 33 MJ"],
              ["Vidējā (GPS)", "20 200 km", "≈ 57 MJ"],
              ["Ģeostacionārā", "35 800 km", "≈ 58 MJ"],
              ["Aizlidošana", "∞", "≈ 63 MJ"]],
             [3.60, 3.30, 5.33]),
        ]),
        ("Kāpēc kosmoss ir dārgs", [
            ("panelis", "ENERĢIJAS SALĪDZINĀJUMS",
             ["1 kg pacelšanai orbītā vajag ≈ 33 MJ. Benzīna "
              "sadegšanas siltums ir ≈ 44 MJ/kg, bet raķetes dzinēja "
              "lietderība ir zema un lielākā daļa degvielas tiek "
              "izlietota pašas degvielas pacelšanai. Tāpēc reāli uz 1 kg "
              "kravas vajag desmitiem kilogramu degvielas."], NAVY),
            ("kartitas", [
                ("ĀTRUMS", BLUE,
                 ["Ek = mv²/2.",
                  "7,7 km/s → 30 MJ/kg.",
                  "Lielākā enerģijas daļa."]),
                ("AUGSTUMS", GREEN,
                 ["ΔEp ≈ 3,6 MJ/kg (400 km).",
                  "Mazāka daļa."]),
                ("ZUDUMI", RED,
                 ["Gaisa pretestība.",
                  "Dzinēja lietderība.",
                  "Degvielas masa."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kinētiskā enerģija orbītā",
             teksts="Aprēķini 1200 kg satelīta kinētisko enerģiju "
                    "orbītā,\nja tā ātrums ir 7,6 km/s!",
             dots=["m = 1200 kg", "v = 7,6·10³ m/s"],
             jaaprekina=["Ek = ?"],
             formulas=["Ek = mv²/2"],
             aprekins=["1)  v² = 5,78·10⁷ m²/s²",
                       "2)  Ek = 1200 · 5,78·10⁷ : 2",
                       "3)  Ek = 3,47·10¹⁰ J"],
             atbilde="Ek ≈ 3,5·10¹⁰ J = 35 GJ",
             piezime="Tas atbilst aptuveni 1000 litriem benzīna."),
        dict(nr=2, virsraksts="Pilnā enerģija orbītā",
             teksts="Aprēķini tā paša satelīta pilno enerģiju, ja\n"
                    "r = 7,0·10⁶ m! (GM = 4,0·10¹⁴ m³/s²)",
             dots=["m = 1200 kg", "r = 7,0·10⁶ m"],
             jaaprekina=["E = ?"],
             formulas=["E = −GMm/(2r)"],
             aprekins=["1)  GMm = 4,0·10¹⁴ · 1200 = 4,8·10¹⁷",
                       "2)  2r = 1,4·10⁷ m",
                       "3)  E = −4,8·10¹⁷ : 1,4·10⁷ = −3,43·10¹⁰ J"],
             atbilde="E ≈ −3,4·10¹⁰ J",
             piezime="Negatīva - satelīts ir saistīts ar Zemi."),
        dict(nr=3, virsraksts="Enerģija orbītas maiņai",
             teksts="Cik enerģijas vajag, lai 800 kg satelītu pārvietotu\n"
                    "no r₁ = 7,0·10⁶ m uz r₂ = 4,2·10⁷ m?\n"
                    "(GM = 4,0·10¹⁴ m³/s²)",
             dots=["m = 800 kg", "r₁ = 7,0·10⁶ m", "r₂ = 4,2·10⁷ m"],
             jaaprekina=["ΔE = ?"],
             formulas=["E = −GMm/(2r)", "ΔE = E₂ − E₁"],
             aprekins=["1)  E₁ = −4,0·10¹⁴·800 : (1,4·10⁷) = "
                       "−2,29·10¹⁰ J",
                       "2)  E₂ = −3,2·10¹⁷ : (8,4·10⁷) = −3,81·10⁹ J",
                       "3)  ΔE = −3,81·10⁹ − (−2,29·10¹⁰) = 1,91·10¹⁰ J"],
             atbilde="ΔE ≈ 1,9·10¹⁰ J jāpievada.",
             piezime="Pārvietošana uz augstāku orbītu vienmēr prasa "
                     "enerģiju."),
        dict(nr=4, virsraksts="Ātrums no enerģijas bilances",
             teksts="Ķermeni izšauj vertikāli no Zemes virsmas ar ātrumu\n"
                    "5,0 km/s. Cik augstu tas pacelsies?\n"
                    "(g = 9,8 m/s²; pieņem g = const - novērtējums)",
             dots=["v₀ = 5,0·10³ m/s", "g = 9,8 m/s²"],
             jaaprekina=["h = ?"],
             formulas=["mv₀²/2 = mgh", "h = v₀²/(2g)"],
             aprekins=["1)  v₀² = 2,5·10⁷ m²/s²",
                       "2)  h = 2,5·10⁷ : 19,6",
                       "3)  h = 1,28·10⁶ m ≈ 1300 km"],
             atbilde="h ≈ 1,3·10³ km (vienkāršots novērtējums)",
             piezime="Precīzā aprēķinā ar mainīgu g iznāktu ~1600 km - "
                     "g ar augstumu samazinās."),
        dict(nr=5, virsraksts="Ātrums no enerģijas nezūdamības",
             teksts="Ar kādu ātrumu jāizšauj ķermenis no Zemes virsmas,\n"
                    "lai tas paceltos līdz r = 2R?\n"
                    "(GM = 4,0·10¹⁴ m³/s²; R = 6,4·10⁶ m)",
             dots=["r₁ = R = 6,4·10⁶ m", "r₂ = 2R", "v = 0 augšpunktā"],
             jaaprekina=["v₀ = ?"],
             formulas=["mv₀²/2 = GMm/R − GMm/(2R)",
                       "v₀ = √(GM/R)"],
             aprekins=["1)  Enerģijas starpība: GMm/(2R)",
                       "2)  v₀² = GM/R = 4,0·10¹⁴ : 6,4·10⁶ = 6,25·10⁷",
                       "3)  v₀ = 7,9·10³ m/s"],
             atbilde="v₀ ≈ 7,9 km/s",
             piezime="Skaitliski tas sakrīt ar pirmo kosmisko ātrumu, "
                     "kaut fizikāli tā ir cita situācija."),
        dict(nr=6, virsraksts="Ek un Ep attiecība orbītā",
             teksts="Pierādi, ka apļveida orbītā Ep = −2Ek,\n"
                    "un aprēķini abas 1000 kg satelītam pie "
                    "r = 8,0·10⁶ m!\n(GM = 4,0·10¹⁴ m³/s²)",
             dots=["m = 1000 kg", "r = 8,0·10⁶ m"],
             jaaprekina=["Ek = ?", "Ep = ?"],
             formulas=["Ek = GMm/(2r)", "Ep = −GMm/r"],
             aprekins=["1)  GMm = 4,0·10¹⁷",
                       "2)  Ek = 4,0·10¹⁷ : 1,6·10⁷ = 2,5·10¹⁰ J",
                       "3)  Ep = −4,0·10¹⁷ : 8,0·10⁶ = −5,0·10¹⁰ J"],
             atbilde="Ek = 2,5·10¹⁰ J ;  Ep = −5,0·10¹⁰ J ;  "
                     "Ep = −2Ek ✔",
             piezime="Pilnā enerģija E = Ek + Ep = −2,5·10¹⁰ J - "
                     "negatīva, tātad satelīts ir saistīts."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Palaišanas enerģija = kinētiskā + potenciālā daļa.",
            "Lielākā enerģijas daļa aiziet orbitālā ātruma iegūšanai.",
            "E = −GMm/(2r) - pilnā enerģija riņķa orbītā.",
            "Augstāka orbīta prasa vairāk enerģijas.",
        ],
        majasdarbs=[
            "m = 600 kg, v = 7,4 km/s. Aprēķini Ek.",
            "m = 1000 kg, r = 1,0·10⁷ m. Aprēķini E.",
            "Aprēķini enerģiju 500 kg satelīta pārvietošanai no "
            "8,0·10⁶ m uz 2,0·10⁷ m.",
        ],
        pasvertejums=["Protu rēķināt Ek orbītā",
                      "Protu rēķināt pilno enerģiju",
                      "Protu rēķināt orbītas maiņas enerģiju",
                      "Protu sastādīt enerģijas bilanci"],
        nakama="Nākamā stunda: datu un grafiku analīze."),
),

dict(
    nr="4.13", virsraksts="Datu un grafiku analīze",
    jautajums="Ko par planētu pastāsta tās orbīta?",
    apaksraksts="Tabulu lasīšana · Grafiki · Secinājumi no datiem",
    merkis="Iemācīties analizēt astronomiskus datus un no tiem izdarīt "
           "pamatotus secinājumus - tieši tā, kā prasa eksāmens.",
    protu=["nolasīt datus no astronomiskas tabulas;",
           "pārbaudīt Keplera likumu ar datiem;",
           "atpazīt sakarību pēc grafika formas;",
           "pamatot secinājumu ar skaitļiem."],
    atkartojums="1.13. stundā mācījāmies analizēt savus mērījumus. Tagad "
                "analizēsim gatavus datus - tā, kā to dara astronomi un "
                "kā prasa eksāmena uzdevumi.",
    uzdevumu_apraksts="Astronomisku datu analīze",
    teorija=[
        ("Kā lasīt datu tabulu", [
            ("panelis", "ČETRI SOĻI",
             ["1) Izlasi tabulas galveni un mērvienības.  2) Atrodi, "
              "kurš lielums mainās un kā.  3) Pārbaudi kādu sakarību ar "
              "diviem punktiem.  4) Formulē secinājumu ar konkrētiem "
              "skaitļiem no tabulas."], NAVY),
            ("tabula",
             ["Grafika forma", "Sakarība", "Piemērs"],
             [["Taisne caur nulli", "y ~ x", "F(x) atsperei"],
              ["Dilstoša līkne", "y ~ 1/x", "v(r) orbītām"],
              ["Strauji dilstoša", "y ~ 1/x²", "F(r) gravitācijai"],
              ["Augoša līkne", "y ~ x^(3/2)", "T(r) orbītām"]],
             [4.30, 3.30, 4.63]),
        ]),
        ("Sakarības pārbaude", [
            ("formula", "KĀ PĀRBAUDĪT SAKARĪBU",
             "Ja  y ~ xⁿ,  tad  y₂/y₁ = (x₂/x₁)ⁿ",
             "Ņem divus datu punktus, aprēķini abas attiecības un "
             "salīdzini. Ja sakrīt, sakarība apstiprinās.", GOLD),
            ("kartitas", [
                ("PĀRBAUDE", BLUE,
                 ["Ņem vismaz divus punktus.",
                  "Vislabāk - visattālākos."]),
                ("SECINĀJUMS", GREEN,
                 ["Vienmēr ar skaitļiem.",
                  "«Aug» nepietiek."]),
                ("KĻŪDA", RED,
                 ["Jāpieļauj 1-5 % novirze.",
                  "Dati ir noapaļoti."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Keplera likuma pārbaude",
             teksts="Zeme: a = 1,00 a.v., T = 1,00 gads.\n"
                    "Jupiters: a = 5,20 a.v., T = 11,86 gadi.\n"
                    "Pārbaudi Keplera trešo likumu!",
             dots=["Zeme: a=1,00; T=1,00", "Jupiters: a=5,20; T=11,86"],
             jaaprekina=["Vai T² = a³?"],
             formulas=["T² / a³ = const"],
             aprekins=["1)  Jupiteram T² = 11,86² = 140,7",
                       "2)  a³ = 5,20³ = 140,6",
                       "3)  T²/a³ = 1,00 - tāpat kā Zemei"],
             atbilde="Likums apstiprinās: T²/a³ = 1,00 abām planētām.",
             piezime="Novirze 0,1 % - datu noapaļošanas robežās."),
        dict(nr=2, virsraksts="Sakarības noteikšana",
             teksts="Satelītu dati: r = 7000 km → v = 7,6 km/s;\n"
                    "r = 28 000 km → v = 3,8 km/s.\n"
                    "Kāda ir v atkarība no r?",
             dots=["r₁ = 7000, v₁ = 7,6", "r₂ = 28 000, v₂ = 3,8"],
             jaaprekina=["sakarība = ?"],
             formulas=["Pārbauda v ~ 1/√r"],
             aprekins=["1)  r₂/r₁ = 4 ;  v₂/v₁ = 0,50",
                       "2)  Ja v ~ 1/√r, tad v₂/v₁ = 1/√4 = 0,50 ✔",
                       "3)  Sakarība apstiprinās"],
             atbilde="v ~ 1/√r - atbilst formulai v = √(GM/r).",
             piezime="Pārbaude ar diviem punktiem ir pietiekama "
                     "eksponenta noteikšanai."),
        dict(nr=3, virsraksts="Planētas raksturošana",
             teksts="Planētai: R = 2,4·10⁶ m, g = 3,7 m/s².\n"
                    "Aprēķini masu, pirmo kosmisko ātrumu un vidējo\n"
                    "blīvumu! (G = 6,67·10⁻¹¹; V = 4πR³/3; π ≈ 3,14)",
             dots=["R = 2,4·10⁶ m", "g = 3,7 m/s²"],
             jaaprekina=["M = ?", "v₁ = ?", "ρ = ?"],
             formulas=["M = gR²/G", "v₁ = √(gR)", "ρ = M/V"],
             aprekins=["1)  M = 3,7 · 5,76·10¹² : 6,67·10⁻¹¹ = "
                       "3,20·10²³ kg",
                       "2)  v₁ = √(3,7 · 2,4·10⁶) = 2,98·10³ ≈ 3,0 km/s",
                       "3)  V = 4·3,14·1,38·10¹⁹:3 = 5,79·10¹⁹ m³;  "
                       "ρ = 5,5·10³ kg/m³"],
             atbilde="M ≈ 3,2·10²³ kg ;  v₁ ≈ 3,0 km/s ;  "
                     "ρ ≈ 5,5·10³ kg/m³",
             piezime="Blīvums tuvu Merkura blīvumam - akmens planēta ar "
                     "metāla kodolu."),
        dict(nr=4, virsraksts="Secinājums no datiem",
             teksts="Divi Jupitera pavadoņi: Io (r = 4,2·10⁵ km,\n"
                    "T = 1,77 d) un Kallisto (r = 1,88·10⁶ km).\n"
                    "Aprēķini Kallisto periodu!",
             dots=["Io: r₁ = 4,2·10⁵ km, T₁ = 1,77 d",
                   "Kallisto: r₂ = 1,88·10⁶ km"],
             jaaprekina=["T₂ = ?"],
             formulas=["T₂²/T₁² = (r₂/r₁)³"],
             aprekins=["1)  r₂/r₁ = 1,88·10⁶ : 4,2·10⁵ = 4,48",
                       "2)  (r₂/r₁)³ = 89,8",
                       "3)  T₂ = T₁ · √89,8 = 1,77 · 9,48 ≈ 16,8 d"],
             atbilde="T₂ ≈ 16,8 dienas (patiesā vērtība 16,7 d)",
             piezime="Keplera likumi der arī pavadoņiem ap citām "
                     "planētām."),
        dict(nr=5, virsraksts="Trīs planētu pārbaude",
             teksts="Venera: a = 0,72 a.v., T = 0,62 g.\n"
                    "Marss: a = 1,52 a.v., T = 1,88 g.\n"
                    "Pārbaudi, vai abām T²/a³ ir vienāds!",
             dots=["Venera: a=0,72; T=0,62", "Marss: a=1,52; T=1,88"],
             jaaprekina=["T²/a³ abām = ?"],
             formulas=["T²/a³ = const"],
             aprekins=["1)  Venera: T² = 0,384 ;  a³ = 0,373 → "
                       "attiecība 1,03",
                       "2)  Marss: T² = 3,53 ;  a³ = 3,51 → "
                       "attiecība 1,01",
                       "3)  Abas ≈ 1,0"],
             atbilde="T²/a³ ≈ 1,0 abām planētām - likums apstiprinās.",
             piezime="Nelielās novirzes rada datu noapaļošana līdz "
                     "divām zīmīgām zīmēm."),
        dict(nr=6, virsraksts="Planētas vidējais blīvums",
             teksts="Planētai g = 9,8 m/s² un R = 6,4·10⁶ m.\n"
                    "Aprēķini masu un vidējo blīvumu!\n"
                    "(G = 6,67·10⁻¹¹; V = 4πR³/3; π ≈ 3,14)",
             dots=["g = 9,8 m/s²", "R = 6,4·10⁶ m"],
             jaaprekina=["M = ?", "ρ = ?"],
             formulas=["M = gR²/G", "V = 4πR³/3", "ρ = M/V"],
             aprekins=["1)  M = 9,8 · 4,10·10¹³ : 6,67·10⁻¹¹ = "
                       "6,02·10²⁴ kg",
                       "2)  V = 4 · 3,14 · 2,62·10²⁰ : 3 = 1,10·10²¹ m³",
                       "3)  ρ = 6,02·10²⁴ : 1,10·10²¹ ≈ 5,5·10³ kg/m³"],
             atbilde="M ≈ 6,0·10²⁴ kg ;   ρ ≈ 5,5·10³ kg/m³",
             piezime="Zemes vidējais blīvums ir divreiz lielāks par "
                     "virsmas iežu blīvumu - kodols ir metālisks."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Sakarību pārbauda ar divu punktu attiecībām.",
            "T²/a³ ir konstante visiem ķermeņiem ap vienu centru.",
            "Secinājums vienmēr jāpamato ar konkrētiem skaitļiem.",
            "1-5 % novirze ir normāla noapaļotiem datiem.",
        ],
        majasdarbs=[
            "Saturns: a = 9,54 a.v. Aprēķini T un salīdzini ar 29,5 "
            "gadiem.",
            "r = 10 000 km → v = 6,3 km/s. Aprēķini v pie r = 40 000 km.",
            "Planētai R = 6,0·10⁶ m, g = 8,0 m/s². Aprēķini M un v₁.",
        ],
        pasvertejums=["Protu lasīt datu tabulu",
                      "Protu pārbaudīt sakarību",
                      "Protu raksturot planētu",
                      "Protu pamatot secinājumu"],
        nakama="Nākamā stunda: temata nostiprināšana."),
),

dict(
    nr="4.14", virsraksts="Temata nostiprināšana",
    jautajums="Kuru sakarību izvēlēties gravitācijas uzdevumā?",
    apaksraksts="Atgādne · Formulu izvēle · PD5 formāts",
    merkis="Apkopot 4. temata saturu un nostiprināt formulu izvēli pirms "
           "PD5.",
    protu=["izvēlēties formulu pēc dotajiem lielumiem;",
           "risināt kombinētus gravitācijas uzdevumus;",
           "lietot attiecību metodi;",
           "sagatavoties PD5."],
    atkartojums="Temats aptvēra gravitācijas likumu, lauku, orbītas, "
                "kosmiskos ātrumus, Keplera likumus un enerģiju "
                "gravitācijas laukā.",
    uzdevumu_apraksts="Kombinēti uzdevumi PD5 formātā",
    teorija=[
        ("Temata atgādne", [
            ("formula", "GRAVITĀCIJA UN LAUKS",
             "F = G m₁ m₂ / r²   ·   g = G M / r²   ·   "
             "G = 6,67·10⁻¹¹ N·m²/kg²",
             "Attālumu vienmēr mēra no centra: r = R + h.", GOLD),
            ("formula", "ORBĪTAS UN ENERĢIJA",
             "v = √(G M / r)   ·   T = 2π √(r³/(GM))   ·   T² ~ r³   ·   "
             "v₁ = √(gR)   ·   v₂ = v₁√2   ·   Ep = −GMm/r",
             "Satelīta masa orbitālajā ātrumā un periodā neparādās.",
             GOLD),
        ]),
        ("Formulas izvēle", [
            ("tabula",
             ["Jautājums", "Lieto", "Piezīme"],
             [["Spēks starp masām", "F = Gm₁m₂/r²", "r starp centriem"],
              ["g uz planētas", "g = GM/R²", "vai attiecības"],
              ["Ātrums orbītā", "v = √(GM/r)", "nav atkarīgs no m"],
              ["Periods", "T = 2π√(r³/GM)", "vai T² ~ r³"],
              ["Aizlidošana", "v₂ = √(2gR)", "= v₁√2"]],
             [4.30, 3.60, 4.33]),
            ("panelis", "PD5 FORMĀTS",
             ["Tests (10 p.) par gravitāciju, lauku, orbītām un Keplera "
              "likumiem; lielumu un mērvienību tabula (5 p.); divi "
              "aprēķinu uzdevumi ar pilnu pierakstu (10 p.); uzdevums ar "
              "apakšjautājumiem par datu analīzi (5 p.). Kopā 30 punkti, "
              "40 minūtes."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Gravitācijas spēks",
             teksts="Aprēķini spēku starp 2000 kg satelītu un Zemi\n"
                    "8,0·10⁶ m attālumā no centra!\n"
                    "(GM = 4,0·10¹⁴ m³/s²)",
             dots=["m = 2000 kg", "r = 8,0·10⁶ m"],
             jaaprekina=["F = ?"],
             formulas=["F = GMm/r²"],
             aprekins=["1)  GMm = 4,0·10¹⁴ · 2000 = 8,0·10¹⁷",
                       "2)  r² = 6,4·10¹³ m²",
                       "3)  F = 8,0·10¹⁷ : 6,4·10¹³ = 1,25·10⁴ N"],
             atbilde="F ≈ 1,3·10⁴ N",
             piezime="Pārbaude: g = F/m = 6,25 m/s² - atbilst šim "
                     "attālumam."),
        dict(nr=2, virsraksts="Orbitālais ātrums un periods",
             teksts="Satelīts riņķo 1000 km augstumā.\n"
                    "Aprēķini v un T! (R = 6,4·10⁶ m;\n"
                    "GM = 4,0·10¹⁴ m³/s²; π ≈ 3,14)",
             dots=["h = 1,0·10⁶ m", "R = 6,4·10⁶ m"],
             jaaprekina=["v = ?", "T = ?"],
             formulas=["r = R+h", "v = √(GM/r)", "T = 2πr/v"],
             aprekins=["1)  r = 7,4·10⁶ m",
                       "2)  v = √(4,0·10¹⁴ : 7,4·10⁶) = 7,35·10³ m/s",
                       "3)  T = 2·3,14·7,4·10⁶ : 7,35·10³ ≈ 6,32·10³ s "
                       "≈ 105 min"],
             atbilde="v ≈ 7,4 km/s ;   T ≈ 1,8 h",
             piezime="Ticamības pārbaude: tuvu KKS vērtībām ✔"),
        dict(nr=3, virsraksts="Keplera likums",
             teksts="Planētas periods ir 125 gadi. Aprēķini tās vidējo\n"
                    "attālumu no Saules astronomiskajās vienībās!",
             dots=["T = 125 gadi"],
             jaaprekina=["a = ?"],
             formulas=["a³ = T²"],
             aprekins=["1)  T² = 15 625",
                       "2)  a³ = 15 625",
                       "3)  a = ∛15 625 = 25 a.v."],
             atbilde="a = 25 a.v.",
             piezime="Starp Urānu (19 a.v.) un Neptūnu (30 a.v.)."),
        dict(nr=4, virsraksts="Kosmiskais ātrums un enerģija",
             teksts="Planētai g = 5,0 m/s², R = 5,0·10⁶ m.\n"
                    "Aprēķini v₁, v₂ un enerģiju 1000 kg kuģa\n"
                    "aizlidošanai no virsmas!",
             dots=["g = 5,0 m/s²", "R = 5,0·10⁶ m", "m = 1000 kg"],
             jaaprekina=["v₁ = ?", "v₂ = ?", "E = ?"],
             formulas=["v₁ = √(gR)", "v₂ = v₁√2", "E = mv₂²/2"],
             aprekins=["1)  v₁ = √(5,0 · 5,0·10⁶) = 5,0·10³ m/s",
                       "2)  v₂ = 5,0·10³ · 1,414 = 7,07·10³ m/s",
                       "3)  E = 1000 · (7,07·10³)² : 2 = 2,5·10¹⁰ J"],
             atbilde="v₁ = 5,0 km/s ;  v₂ ≈ 7,1 km/s ;  E = 2,5·10¹⁰ J",
             piezime="Vieglāk pamest nekā Zemi (11,2 km/s un 6,3·10¹⁰ J)."),
        dict(nr=5, virsraksts="GM no orbītas datiem",
             teksts="Satelītam r = 7,0·10⁶ m un T = 5,82·10³ s.\n"
                    "Aprēķini GM un g uz planētas virsmas!\n"
                    "(R = 6,4·10⁶ m; π² ≈ 9,87)",
             dots=["r = 7,0·10⁶ m", "T = 5,82·10³ s", "R = 6,4·10⁶ m"],
             jaaprekina=["GM = ?", "g = ?"],
             formulas=["GM = 4π²r³/T²", "g = GM/R²"],
             aprekins=["1)  r³ = 3,43·10²⁰ m³ ;  4π²r³ = 1,35·10²²",
                       "2)  T² = 3,39·10⁷ s² → GM = 4,0·10¹⁴ m³/s²",
                       "3)  g = 4,0·10¹⁴ : 4,10·10¹³ ≈ 9,8 m/s²"],
             atbilde="GM ≈ 4,0·10¹⁴ m³/s² ;   g ≈ 9,8 m/s²",
             piezime="No viena satelīta novērojuma var noteikt visu "
                     "planētas gravitācijas lauku."),
        dict(nr=6, virsraksts="Starts no citas planētas",
             teksts="Uz planētas ar g = 5,0 m/s² raķete paceļas ar\n"
                    "paātrinājumu 15 m/s². Aprēķini 80 kg kosmonauta "
                    "svaru\nun pārslodzi šīs planētas apstākļos!",
             dots=["g = 5,0 m/s²", "a = 15 m/s²", "m = 80 kg"],
             jaaprekina=["P = ?", "n = ?"],
             formulas=["P = m(g + a)", "n = (g + a)/g"],
             aprekins=["1)  g + a = 20 m/s²",
                       "2)  P = 80 · 20 = 1600 N",
                       "3)  n = 20 : 5,0 = 4,0"],
             atbilde="P = 1,6·10³ N ;   n = 4,0",
             piezime="Pārslodzi vienmēr rēķina attiecībā pret TĀS "
                     "planētas g, uz kuras notiek starts."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Visas orbītas formulas izriet no gravitācijas kā "
            "centrtieces spēka.",
            "r vienmēr mēra no centra.",
            "T² ~ r³ ir ātrākais ceļš salīdzinājumiem.",
            "Ticamības pārbaudei noder zināmie orientieri.",
        ],
        majasdarbs=[
            "Atkārto abas atgādnes pirms PD5.",
            "Izpildi pa vienam uzdevumam no katra veida.",
            "Pārskati Keplera likumus un kosmiskos ātrumus.",
        ],
        pasvertejums=["Protu izvēlēties formulu",
                      "Protu rēķināt orbītas",
                      "Protu lietot Keplera likumus",
                      "Esmu gatavs PD5"],
        nakama="Nākamā stunda: PD5 - gravitācijas lauks un kustība."),
),

dict(
    nr="4.15", virsraksts="Kļūdu analīze",
    jautajums="Kur pazuda mērvienības?",
    apaksraksts="PD5 kļūdas · Standartforma · Pāreja uz enerģiju",
    merkis="Analizēt PD5 kļūdas, nostiprināt darbu ar lieliem skaitļiem "
           "un sagatavoties 5. tematam.",
    protu=["strādāt ar standartformu bez kļūdām;",
           "pārbaudīt mērvienības sarežģītās formulās;",
           "izlabot tipiskās gravitācijas kļūdas;",
           "saistīt gravitāciju ar enerģijas tematu."],
    atkartojums="PD5 ir uzrakstīts. Šajā tematā galvenā tehniskā "
                "grūtība bija darbs ar ļoti lieliem un ļoti maziem "
                "skaitļiem.",
    uzdevumu_apraksts="Kļūdainu risinājumu labošana",
    teorija=[
        ("Biežākās PD5 kļūdas", [
            ("tabula",
             ["Kļūda", "Kā izskatās", "Pareizi"],
             [["r no virsmas", "r = h", "r = R + h"],
              ["km nav pārveidoti", "r = 7000 (km)", "r = 7,0·10⁶ m"],
              ["Aizmirsts kvadrāts", "F ~ 1/r", "F ~ 1/r²"],
              ["Satelīta masa formulā", "v = √(GMm/r)", "v = √(GM/r)"],
              ["Sajaukts v₁ un v₂", "v₂ = 2v₁", "v₂ = v₁√2"]],
             [3.60, 3.90, 4.73]),
            ("panelis", "DARBS AR STANDARTFORMU",
             ["Reizinot: mantisas reizina, kārtas saskaita "
              "(2·10³ · 3·10⁵ = 6·10⁸). Dalot: mantisas dala, kārtas "
              "atņem. Kāpinot kvadrātā: mantisu kvadrātā, kārtu reizina "
              "ar 2 ((3·10⁴)² = 9·10⁸)."], NAVY),
        ]),
        ("Tilts uz 5. tematu", [
            ("divi",
             ("4. TEMATS", BLUE,
              ["Gravitācijas spēks un lauks.",
               "Ep = mgh un Ep = −GMm/r.",
               "Enerģija parādījās kā rīks."]),
             ("5. TEMATS", GREEN,
              ["Darbs, enerģija, jauda.",
               "Enerģijas nezūdamība.",
               "Impulss un triecieni.",
               "Enerģija kļūst par galveno tēmu."])),
            ("formula", "SAVIENOJOŠĀ IDEJA",
             "A = ΔE        Ek + Ep = const  (bez berzes)",
             "5. tematā enerģijas nezūdamība kļūs par galveno rīku - un "
             "gravitācijas potenciālā enerģija būs viens no tās "
             "locekļiem.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atrodi kļūdu I",
             teksts="«Satelīts 600 km augstumā; v = √(GM/r) = \n"
                    "√(4,0·10¹⁴ : 6,0·10⁵) = 2,6·10⁴ m/s.»\nIzlabo!",
             dots=["h = 600 km", "R = 6,4·10⁶ m"],
             jaaprekina=["v = ?"],
             formulas=["r = R + h"],
             aprekins=["1)  Kļūda: r ņemts kā augstums, nevis R + h",
                       "2)  r = 6,4·10⁶ + 6,0·10⁵ = 7,0·10⁶ m",
                       "3)  v = √(4,0·10¹⁴ : 7,0·10⁶) = 7,56·10³ m/s"],
             atbilde="v ≈ 7,6 km/s, nevis 26 km/s.",
             piezime="Ticamības pārbaude: 26 km/s pārsniedz otro "
                     "kosmisko ātrumu - acīmredzami nepareizi."),
        dict(nr=2, virsraksts="Atrodi kļūdu II",
             teksts="«Attālumu palielina 3 reizes, tātad spēks\n"
                    "samazinās 3 reizes.»\nIzlabo un pamato!",
             dots=["r₂ = 3r₁"],
             jaaprekina=["F₂/F₁ = ?"],
             formulas=["F ~ 1/r²"],
             aprekins=["1)  Kļūda: aizmirsts kvadrāts",
                       "2)  F₂/F₁ = (r₁/r₂)² = (1/3)²",
                       "3)  = 1/9"],
             atbilde="Spēks samazinās 9 reizes, nevis 3.",
             piezime="Kvadrātiskā atkarība ir gravitācijas likuma "
                     "būtība."),
        dict(nr=3, virsraksts="Atrodi kļūdu III",
             teksts="«Smagākam satelītam vajag lielāku orbitālo ātrumu,\n"
                    "jo uz to darbojas lielāks gravitācijas spēks.»\n"
                    "Izvērtē apgalvojumu!",
             dots=["divi satelīti ar dažādām masām, viena orbīta"],
             jaaprekina=["Vai pareizi?"],
             formulas=["GMm/r² = mv²/r → v = √(GM/r)"],
             aprekins=["1)  Spēks tiešām lielāks smagākam",
                       "2)  Bet arī inerce lielāka - m saīsinās",
                       "3)  v = √(GM/r) - nav atkarīgs no m"],
             atbilde="Apgalvojums nepareizs: orbitālais ātrums nav "
                     "atkarīgs no satelīta masas.",
             piezime="Tā pati ideja kā brīvajā krišanā - visi krīt "
                     "vienādi."),
        dict(nr=4, virsraksts="Atrodi kļūdu IV",
             teksts="«Planētai a = 4,0 a.v.; T² = a³, tātad\n"
                    "T = 4,0³ = 64 gadi.»\nIzlabo risinājumu!",
             dots=["a = 4,0 a.v."],
             jaaprekina=["T = ?"],
             formulas=["T² = a³", "T = √(a³)"],
             aprekins=["1)  Kļūda: aizmirsta kvadrātsakne",
                       "2)  a³ = 64 → T² = 64",
                       "3)  T = √64 = 8,0 gadi"],
             atbilde="T = 8,0 gadi, nevis 64 gadi.",
             piezime="Vienmēr pieraksti, kurā pusē ir kvadrāts un kurā - "
                     "kubs."),
        dict(nr=5, virsraksts="Atrodi kļūdu V",
             teksts="«Ep = −GMm/r iznāca negatīva, tātad aprēķinā ir\n"
                    "kļūda - enerģija nevar būt negatīva.»\n"
                    "Izvērtē apgalvojumu!",
             dots=["Ep = −5,7·10¹⁰ J"],
             jaaprekina=["Vai rezultāts pareizs?"],
             formulas=["Ep = 0 bezgalībā", "Ep < 0 saistītā stāvoklī"],
             aprekins=["1)  Nulles līmenis izvēlēts bezgalībā",
                       "2)  Tuvojoties planētai, Ep samazinās",
                       "3)  Tāpēc saistītā stāvoklī tā ir negatīva"],
             atbilde="Rezultāts ir pareizs: negatīva Ep nozīmē, ka "
                     "ķermenis ir saistīts ar planētu.",
             piezime="Zīme šeit ir informācija par stāvokli, nevis "
                     "aprēķina kļūda."),
        dict(nr=6, virsraksts="Atrodi kļūdu VI",
             teksts="«Kosmonauts KKS ir bezsvara stāvoklī, jo 400 km\n"
                    "augstumā gravitācijas vairs nav.»\n"
                    "Izlabo un pamato ar aprēķinu! (R = 6,4·10⁶ m; "
                    "g₀ = 9,8 m/s²)",
             dots=["h = 4,0·10⁵ m", "R = 6,4·10⁶ m"],
             jaaprekina=["g = ?", "kāpēc bezsvars?"],
             formulas=["g = g₀R²/(R+h)²"],
             aprekins=["1)  (R/(R+h))² = (6400 : 6800)² = 0,886",
                       "2)  g = 9,8 · 0,886 ≈ 8,7 m/s²",
                       "3)  Gravitācija ir gandrīz tikpat liela"],
             atbilde="g ≈ 8,7 m/s²; bezsvars rodas tāpēc, ka stacija "
                     "nepārtraukti brīvi krīt, nevis gravitācijas "
                     "trūkuma dēļ.",
             piezime="Šis ir viens no biežāk pārprastajiem jautājumiem "
                     "visā kursā."),
        dict(nr=7, virsraksts="Atgādnes papildināšana",
             teksts="Papildini personīgo atgādni ar 4. temata "
                    "sakarībām\nun divām kļūdām, kuras tev bija PD5!",
             dots=["PD5 rezultāti"],
             jaaprekina=["atgādne = ?"],
             formulas=["Personīgs saraksts"],
             aprekins=["1)  Sakarības: F = Gm₁m₂/r²; g = GM/r²;",
                       "     v = √(GM/r); T² ~ r³; v₂ = v₁√2",
                       "2)  Kļūdas: r = R + h; kvadrāts pie r"],
             atbilde="Atgādne papildināta ar 5 sakarībām un personīgām "
                     "kļūdām.",
             piezime="Eksāmenā gravitācijas uzdevumi parasti ir viens "
                     "vai divi - bet tie ir «droši» punkti."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "r vienmēr ir R + h, nevis h.",
            "Gravitācijā atkarība no attāluma vienmēr ir kvadrātiska.",
            "Orbitālais ātrums nav atkarīgs no satelīta masas.",
            "Standartformā mantisas un kārtas apstrādā atsevišķi.",
        ],
        majasdarbs=[
            "Izlabo savas PD5 kļūdas pilnā pierakstā.",
            "Papildini personīgo atgādni.",
            "Atkārto Ep = mgh un Ek = mv²/2 - 5. tematā tie būs "
            "galvenie.",
        ],
        pasvertejums=["Protu strādāt ar standartformu",
                      "Protu pārbaudīt mērvienības",
                      "Protu izlabot tipiskās kļūdas",
                      "Esmu gatavs 5. tematam"],
        nakama="Nākamais temats: enerģija un darbs."),
),

]
