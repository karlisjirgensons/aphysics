# -*- coding: utf-8 -*-
"""5. temats. B daļa: 5.8.-5.13. stunda un gada noslēgums (5.14.-5.15.)."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t05a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="5.8", virsraksts="Impulss",
    jautajums="Kāpēc smagu ķermeni grūti apturēt?",
    apaksraksts="p = mv · Ft = Δp · Spēka impulss",
    merkis="Iemācīties aprēķināt ķermeņa impulsu un lietot spēka "
           "impulsa un impulsa izmaiņas sakarību.",
    protu=["definēt impulsu un nosaukt mērvienību;",
           "aprēķināt p = mv;",
           "lietot Ft = Δp;",
           "izskaidrot drošības spilvena darbību."],
    atkartojums="5.4. stundā enerģija bija skalārs. Impulss ir VEKTORS - "
                "un tas dod citu skatījumu uz sadursmēm.",
    uzdevumu_apraksts="Impulss un spēka impulss",
    teorija=[
        ("Impulss", [
            ("formula", "IMPULSS UN SPĒKA IMPULSS",
             "p⃗ = m · v⃗        F⃗ · t = Δp⃗ = m v⃗₂ − m v⃗₁        "
             "[p] = kg·m/s = N·s",
             "Impulss ir vektors ar ātruma virzienu. Spēka impulss Ft "
             "maina ķermeņa impulsu - tas ir Ņūtona otrā likuma cita "
             "forma.", GOLD),
            ("divi",
             ("ENERĢIJA", BLUE,
              ["Ek = mv²/2 - skalārs.",
               "Vienmēr pozitīva.",
               "Atkarīga no v².",
               "Nesaglabājas neelastīgā triecienā."]),
             ("IMPULSS", GREEN,
              ["p = mv - vektors.",
               "Zīme rāda virzienu.",
               "Atkarīgs no v lineāri.",
               "Saglabājas VISOS triecienos."])),
        ]),
        ("Ft = Δp praksē", [
            ("panelis", "KĀPĒC DROŠĪBAS SPILVENS PALĪDZ",
             ["Sadursmē impulsa izmaiņa Δp ir fiksēta - tā atkarīga no "
              "masas un ātruma. Bet spēku nosaka sadursmes laiks:",
              "F = Δp/t",
              "Jo ILGĀKS sadursmes laiks, jo MAZĀKS spēks. Spilvens "
              "pagarina apstāšanās laiku no 0,01 s līdz 0,1 s - un "
              "spēks samazinās 10 reižu."], NAVY),
            ("tabula",
             ["Risinājums", "Kā darbojas", "Efekts"],
             [["Drošības spilvens", "Pagarina laiku", "F samazinās 10×"],
              ["Deformējamā zona", "Pagarina laiku", "F samazinās"],
              ["Ķivere", "Pagarina laiku", "Pasargā galvu"],
              ["Locīt kājas, lecot", "Pagarina laiku", "Mazāka slodze"]],
             [4.30, 3.60, 4.33]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Impulsa aprēķins",
             teksts="Aprēķini 1200 kg automašīnas impulsu, braucot\n"
                    "72 km/h!",
             dots=["m = 1200 kg", "v = 72 km/h = 20 m/s"],
             jaaprekina=["p = ?"],
             formulas=["p = mv"],
             aprekins=["1)  v = 72 : 3,6 = 20 m/s",
                       "2)  p = 1200 · 20",
                       "3)  p = 2,4·10⁴ kg·m/s"],
             atbilde="p = 2,4·10⁴ kg·m/s",
             piezime="Virziens - kustības virzienā."),
        dict(nr=2, virsraksts="Spēks no impulsa izmaiņas",
             teksts="Automašīna (1000 kg) no 20 m/s apstājas 0,10 s "
                    "laikā\n(bez spilvena). Aprēķini vidējo spēku!",
             dots=["m = 1000 kg", "v₁ = 20 m/s", "v₂ = 0",
                   "t = 0,10 s"],
             jaaprekina=["F = ?"],
             formulas=["Δp = m(v₂ − v₁)", "F = Δp/t"],
             aprekins=["1)  Δp = 1000 · (0 − 20) = −2,0·10⁴ kg·m/s",
                       "2)  F = −2,0·10⁴ : 0,10",
                       "3)  F = −2,0·10⁵ N"],
             atbilde="F = 2,0·10⁵ N, vērsts pretēji kustībai.",
             piezime="Tas ir 20 tonnu svars - letāls spēks."),
        dict(nr=3, virsraksts="Drošības spilvena efekts",
             teksts="Ar drošības spilvenu apstāšanās laiks pagarinās "
                    "līdz\n0,50 s. Aprēķini spēku un salīdzini ar "
                    "2. uzdevumu!",
             dots=["Δp = 2,0·10⁴ kg·m/s", "t = 0,50 s"],
             jaaprekina=["F = ?"],
             formulas=["F = Δp/t"],
             aprekins=["1)  F = 2,0·10⁴ : 0,50",
                       "2)  F = 4,0·10⁴ N",
                       "3)  Attiecība: 2,0·10⁵ : 4,0·10⁴ = 5"],
             atbilde="F = 4,0·10⁴ N - 5 reizes mazāks.",
             piezime="Tieši šajā atšķirībā slēpjas drošības spilvena "
                     "jēga."),
        dict(nr=4, virsraksts="Bumbas atsitiens",
             teksts="Bumba (m = 0,20 kg) trāpa sienā ar 15 m/s un "
                    "atlec\nar 12 m/s. Sadursme ilgst 0,020 s.\n"
                    "Aprēķini vidējo spēku!",
             dots=["m = 0,20 kg", "v₁ = 15 m/s", "v₂ = −12 m/s",
                   "t = 0,020 s"],
             jaaprekina=["F = ?"],
             formulas=["Δp = m(v₂ − v₁)", "F = Δp/t"],
             aprekins=["1)  Δp = 0,20 · (−12 − 15) = −5,4 kg·m/s",
                       "2)  F = −5,4 : 0,020",
                       "3)  F = −270 N"],
             atbilde="F = 2,7·10² N, vērsts pretēji sākotnējai kustībai.",
             piezime="Uzmanību ar zīmēm: atlecot ātrums maina virzienu."),
        dict(nr=5, virsraksts="Ātrums no impulsa",
             teksts="Ķermeņa (m = 4,0 kg) impulss ir 60 kg·m/s.\n"
                    "Aprēķini tā ātrumu!",
             dots=["m = 4,0 kg", "p = 60 kg·m/s"],
             jaaprekina=["v = ?"],
             formulas=["p = mv", "v = p/m"],
             aprekins=["1)  v = 60 : 4,0",
                       "2)  v = 15 m/s",
                       "3)  Pārbaude: 4,0 · 15 = 60 kg·m/s ✔"],
             atbilde="v = 15 m/s",
             piezime="Impulsa mērvienība kg·m/s ir tā pati, kas N·s."),
        dict(nr=6, virsraksts="Impulsa izmaiņa paātrinot",
             teksts="Automašīna (800 kg) 6,0 s laikā palielina ātrumu no\n"
                    "10 m/s līdz 25 m/s. Aprēķini impulsa izmaiņu un "
                    "spēku!",
             dots=["m = 800 kg", "v₁ = 10 m/s", "v₂ = 25 m/s",
                   "t = 6,0 s"],
             jaaprekina=["Δp = ?", "F = ?"],
             formulas=["Δp = m(v₂ − v₁)", "F = Δp/t"],
             aprekins=["1)  Δv = 25 − 10 = 15 m/s",
                       "2)  Δp = 800 · 15 = 1,2·10⁴ kg·m/s",
                       "3)  F = 1,2·10⁴ : 6,0 = 2,0·10³ N"],
             atbilde="Δp = 1,2·10⁴ kg·m/s ;   F = 2,0·10³ N",
             piezime="Pārbaude: a = 15 : 6,0 = 2,5 m/s²; "
                     "F = 800 · 2,5 = 2000 N ✔"),
        dict(nr=7, virsraksts="Kurš impulss lielāks",
             teksts="Kravas auto (8000 kg) brauc 10 m/s, vieglā "
                    "automašīna\n(1000 kg) - 30 m/s. Salīdzini to "
                    "impulsus!",
             dots=["m₁ = 8000 kg, v₁ = 10 m/s",
                   "m₂ = 1000 kg, v₂ = 30 m/s"],
             jaaprekina=["p₁ = ?", "p₂ = ?"],
             formulas=["p = mv"],
             aprekins=["1)  p₁ = 8000 · 10 = 8,0·10⁴ kg·m/s",
                       "2)  p₂ = 1000 · 30 = 3,0·10⁴ kg·m/s",
                       "3)  p₁ : p₂ ≈ 2,7"],
             atbilde="Kravas auto impulss ir 2,7 reizes lielāks.",
             piezime="Salīdzini ar kinētisko enerģiju: 4,0·10⁵ J pret "
                     "4,5·10⁵ J - tur uzvar vieglā automašīna."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "p = mv - vektors; [p] = kg·m/s.",
            "Ft = Δp - spēka impulss maina impulsu.",
            "Pagarinot sadursmes laiku, spēks samazinās.",
            "Impulss saglabājas visos triecienos, enerģija - ne.",
        ],
        majasdarbs=[
            "m = 80 kg, v = 6,0 m/s. Aprēķini p.",
            "m = 0,50 kg, no 20 m/s līdz 0 par 0,05 s. Aprēķini F.",
            "Bumba 0,15 kg trāpa 20 m/s, atlec 16 m/s, t = 0,01 s. "
            "Aprēķini F.",
        ],
        pasvertejums=["Protu rēķināt impulsu",
                      "Protu lietot Ft = Δp",
                      "Protu strādāt ar zīmēm",
                      "Protu izskaidrot drošības risinājumus"],
        nakama="Nākamā stunda: impulsa nezūdamība."),
),

dict(
    nr="5.9", virsraksts="Impulsa nezūdamība",
    jautajums="Kas notiek sadursmē?",
    apaksraksts="Σp pirms = Σp pēc · Slēgta sistēma · Reaktīvā kustība",
    merkis="Iemācīties lietot impulsa nezūdamības likumu sadursmju un "
           "reaktīvās kustības uzdevumos.",
    protu=["formulēt impulsa nezūdamības likumu;",
           "izvēlēties asi un pierakstīt impulsus ar zīmēm;",
           "risināt sadursmju uzdevumus;",
           "izskaidrot reaktīvo kustību ar impulsu."],
    atkartojums="5.8. stundā: Ft = Δp. Ja sistēma ir slēgta un ārēju "
                "spēku nav, kopējais impulss nemainās.",
    uzdevumu_apraksts="Impulsa nezūdamība sadursmēs",
    teorija=[
        ("Nezūdamības likums", [
            ("formula", "IMPULSA NEZŪDAMĪBA",
             "m₁v₁ + m₂v₂ = m₁u₁ + m₂u₂",
             "Slēgtā sistēmā (bez ārējiem spēkiem) kopējais impulss "
             "nemainās. Tā kā impulss ir vektors, visus ātrumus pieraksta "
             "ar ZĪMĒM pēc izvēlētās ass.", GOLD),
            ("kartitas", [
                ("SLĒGTA SISTĒMA", BLUE,
                 ["Ārējo spēku nav",
                  "vai tie ir daudz mazāki",
                  "par iekšējiem."]),
                ("ASS IZVĒLE", GREEN,
                 ["Parasti gar kustību.",
                  "Pa labi - plus.",
                  "Pa kreisi - mīnuss."]),
                ("PĀRBAUDE", GOLD,
                 ["Vai atbilde loģiska?",
                  "Vai ātrums nav pārāk liels?"]),
            ]),
        ]),
        ("Tipiskās situācijas", [
            ("tabula",
             ["Situācija", "Vienādojums", "Piezīme"],
             [["Saduras un saķeras", "m₁v₁ + m₂v₂ = (m₁+m₂)u",
               "Viens kopīgs ātrums"],
              ["Atgrūžas no miera", "0 = m₁u₁ + m₂u₂", "Pretēji virzieni"],
              ["Elastīgs trieciens", "Impulss un Ek saglabājas",
               "Divi vienādojumi"],
              ["Šaušana", "0 = m(lodes)v − M(ieroča)V", "Atsitiens"]],
             [4.30, 4.30, 3.63]),
            ("panelis", "KĀPĒC RAĶETE LIDO",
             ["Raķete izgrūž gāzes atpakaļ ar lielu ātrumu. Sistēmas "
              "kopējais impulss paliek nulle, tāpēc raķete iegūst "
              "impulsu uz priekšu. Tas darbojas arī vakuumā - nav "
              "vajadzīgs, no kā «atgrūsties»."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Neelastīga sadursme",
             teksts="Vagons (20 t) brauc 3,0 m/s un saduras ar "
                    "nekustīgu\nvagonu (10 t); tie saķeras.\n"
                    "Aprēķini kopējo ātrumu!",
             dots=["m₁ = 20 t, v₁ = 3,0 m/s", "m₂ = 10 t, v₂ = 0"],
             jaaprekina=["u = ?"],
             formulas=["m₁v₁ = (m₁ + m₂)u"],
             aprekins=["1)  Sākuma impulss: 20 000 · 3,0 = 6,0·10⁴ kg·m/s",
                       "2)  Kopējā masa: 30 000 kg",
                       "3)  u = 6,0·10⁴ : 3,0·10⁴ = 2,0 m/s"],
             atbilde="u = 2,0 m/s",
             piezime="Ātrums samazinājās, jo masa palielinājās 1,5 reizes."),
        dict(nr=2, virsraksts="Pretimbraucoša sadursme",
             teksts="Ķermenis (3,0 kg, 8,0 m/s) saduras ar pretimnākošu\n"
                    "(5,0 kg, 4,0 m/s); tie saķeras.\n"
                    "Aprēķini kopējo ātrumu un virzienu!",
             dots=["m₁ = 3,0 kg, v₁ = +8,0 m/s",
                   "m₂ = 5,0 kg, v₂ = −4,0 m/s"],
             jaaprekina=["u = ?"],
             formulas=["m₁v₁ + m₂v₂ = (m₁+m₂)u"],
             aprekins=["1)  p = 3,0·8,0 + 5,0·(−4,0) = 24 − 20 = "
                       "4,0 kg·m/s",
                       "2)  Σm = 8,0 kg",
                       "3)  u = 4,0 : 8,0 = 0,50 m/s"],
             atbilde="u = 0,50 m/s pirmā ķermeņa sākotnējā virzienā.",
             piezime="Pozitīvā atbilde nozīmē kustību ass virzienā."),
        dict(nr=3, virsraksts="Atsitiens šaujot",
             teksts="No 4,0 kg šautenes izšauj 10 g lodi ar 700 m/s.\n"
                    "Aprēķini šautenes atsitiena ātrumu!",
             dots=["M = 4,0 kg", "m = 0,010 kg", "v = 700 m/s"],
             jaaprekina=["V = ?"],
             formulas=["0 = mv + MV", "V = −mv/M"],
             aprekins=["1)  mv = 0,010 · 700 = 7,0 kg·m/s",
                       "2)  V = −7,0 : 4,0",
                       "3)  V = −1,75 m/s"],
             atbilde="V = 1,75 m/s pretējā virzienā.",
             piezime="Tāpēc šauteni cieši piespiež pie pleca - lai "
                     "pagarinātu sadursmes laiku."),
        dict(nr=4, virsraksts="Atgrūšanās uz slidām",
             teksts="Divi slidotāji (60 kg un 40 kg) atgrūžas viens no "
                    "otra.\nSmagākais sāk kustēties ar 2,0 m/s.\n"
                    "Aprēķini otrā ātrumu!",
             dots=["m₁ = 60 kg, u₁ = 2,0 m/s", "m₂ = 40 kg",
                   "sākumā mierā"],
             jaaprekina=["u₂ = ?"],
             formulas=["0 = m₁u₁ + m₂u₂"],
             aprekins=["1)  m₁u₁ = 60 · 2,0 = 120 kg·m/s",
                       "2)  u₂ = −120 : 40",
                       "3)  u₂ = −3,0 m/s"],
             atbilde="u₂ = 3,0 m/s pretējā virzienā.",
             piezime="Vieglākais kustas ātrāk - impulsi ir vienādi pēc "
                     "moduļa."),
        dict(nr=5, virsraksts="Izlēciens no laivas",
             teksts="Cilvēks (70 kg) izlec no mierā esošas 210 kg laivas\n"
                    "ar ātrumu 3,0 m/s. Aprēķini laivas ātrumu!",
             dots=["m = 70 kg, u₁ = 3,0 m/s", "M = 210 kg",
                   "sākumā mierā"],
             jaaprekina=["u₂ = ?"],
             formulas=["0 = mu₁ + Mu₂", "u₂ = −mu₁/M"],
             aprekins=["1)  mu₁ = 70 · 3,0 = 210 kg·m/s",
                       "2)  u₂ = −210 : 210",
                       "3)  u₂ = −1,0 m/s"],
             atbilde="u₂ = 1,0 m/s pretējā virzienā.",
             piezime="Tāpēc, izkāpjot no laivas, tā aizslīd - un cilvēks "
                     "iekrīt ūdenī."),
        dict(nr=6, virsraksts="Sadursme vienā virzienā",
             teksts="Ķermenis (2,0 kg, 5,0 m/s) panāk un saķeras ar\n"
                    "ķermeni (3,0 kg, 2,0 m/s), kas kustas tajā pašā\n"
                    "virzienā. Aprēķini kopējo ātrumu!",
             dots=["m₁ = 2,0 kg, v₁ = 5,0 m/s",
                   "m₂ = 3,0 kg, v₂ = 2,0 m/s"],
             jaaprekina=["u = ?"],
             formulas=["m₁v₁ + m₂v₂ = (m₁+m₂)u"],
             aprekins=["1)  p = 2,0·5,0 + 3,0·2,0 = 10 + 6,0 = "
                       "16 kg·m/s",
                       "2)  Σm = 5,0 kg",
                       "3)  u = 16 : 5,0 = 3,2 m/s"],
             atbilde="u = 3,2 m/s tajā pašā virzienā.",
             piezime="Kopējais ātrums vienmēr ir starp abiem sākuma "
                     "ātrumiem."),
        dict(nr=7, virsraksts="Raķetes princips",
             teksts="Raķete ar kopējo masu 500 kg izgrūž 10 kg gāzu ar\n"
                    "ātrumu 800 m/s. Cik lielu ātrumu iegūst raķete?",
             dots=["M = 490 kg (pēc izgrūšanas)", "m = 10 kg",
                   "u = 800 m/s"],
             jaaprekina=["V = ?"],
             formulas=["0 = mu + MV", "V = −mu/M"],
             aprekins=["1)  mu = 10 · 800 = 8000 kg·m/s",
                       "2)  V = −8000 : 490",
                       "3)  V ≈ −16,3 m/s"],
             atbilde="V ≈ 16 m/s pretēji gāzu plūsmai.",
             piezime="Raķetei nav vajadzīgs atbalsts - tā kustas, "
                     "atgrūžoties no pašas izmestās vielas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Slēgtā sistēmā Σp pirms = Σp pēc.",
            "Impulss ir vektors - ātrumus raksta ar zīmēm.",
            "Saķeroties ķermeņiem ir viens kopīgs ātrums.",
            "Reaktīvā kustība balstās uz impulsa nezūdamību.",
        ],
        majasdarbs=[
            "m₁ = 5,0 kg, v₁ = 6,0 m/s saduras ar mierā esošu 3,0 kg; "
            "saķeras. Aprēķini u.",
            "Laiva 200 kg, cilvēks 80 kg izlec ar 3,0 m/s. Aprēķini "
            "laivas ātrumu.",
            "m₁ = 2,0 kg, v₁ = 5,0 m/s pretim 4,0 kg ar 2,0 m/s; "
            "saķeras. Aprēķini u.",
        ],
        pasvertejums=["Protu formulēt nezūdamības likumu",
                      "Protu strādāt ar zīmēm",
                      "Protu risināt sadursmes",
                      "Protu izskaidrot reaktīvo kustību"],
        nakama="Nākamā stunda: elastīgs un neelastīgs trieciens."),
),

dict(
    nr="5.10", virsraksts="Elastīgs un neelastīgs trieciens",
    jautajums="Kad enerģija pazūd, bet impulss nē?",
    apaksraksts="Elastīgs · Neelastīgs · Enerģijas zudumi",
    merkis="Iemācīties atšķirt elastīgu un neelastīgu triecienu un "
           "aprēķināt enerģijas zudumus.",
    protu=["atšķirt elastīgu triecienu no neelastīga;",
           "aprēķināt enerģijas zudumus neelastīgā triecienā;",
           "pamatot, kāpēc impulss saglabājas vienmēr;",
           "nosaukt triecienu piemērus."],
    atkartojums="5.9. stundā: impulss saglabājas visos triecienos. Bet "
                "kā ar enerģiju? Atbilde ir atkarīga no trieciena veida.",
    uzdevumu_apraksts="Enerģijas zudumi triecienos",
    teorija=[
        ("Divi trieciena veidi", [
            ("divi",
             ("ELASTĪGS", GREEN,
              ["Impulss saglabājas.",
               "Kinētiskā enerģija saglabājas.",
               "Ķermeņi atlec.",
               "Piemērs: biljarda bumbas."]),
             ("NEELASTĪGS", RED,
              ["Impulss saglabājas.",
               "Ek daļēji pārvēršas siltumā.",
               "Ķermeņi saķeras vai deformējas.",
               "Piemērs: plastilīna pikas."])),
            ("formula", "ENERĢIJAS ZUDUMI",
             "ΔEk = Ek(pirms) − Ek(pēc)",
             "Pilnīgi neelastīgā triecienā (ķermeņi saķeras) zudumi ir "
             "vislielākie. Enerģija nepazūd - tā pārvēršas siltumā un "
             "deformācijā.", GOLD),
        ]),
        ("Kur to redz", [
            ("tabula",
             ["Trieciens", "Veids", "Ek zudumi"],
             [["Biljarda bumbas", "Gandrīz elastīgs", "< 5 %"],
              ["Tenisa bumba pret sienu", "Daļēji elastīgs", "20-40 %"],
              ["Auto sadursme", "Neelastīgs", "Liels"],
              ["Plastilīns pret sienu", "Pilnīgi neelastīgs", "100 %"],
              ["Šautenes lode kokā", "Pilnīgi neelastīgs", "Gandrīz viss"]],
             [4.60, 3.90, 3.73]),
            ("panelis", "KĀPĒC AUTO DEFORMĒJAS TĪŠI",
             ["Mūsdienu automašīnas ir projektētas tā, lai priekšgals "
              "deformētos - tā trieciena laiks pagarinās un daļa "
              "enerģijas aiziet metāla deformācijā, nevis pasažieru "
              "ķermeņos."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Enerģijas zudumi",
             teksts="Ķermenis (4,0 kg, 6,0 m/s) saduras ar mierā esošu\n"
                    "(2,0 kg) un saķeras. Aprēķini kopējo ātrumu un\n"
                    "enerģijas zudumus!",
             dots=["m₁ = 4,0 kg, v₁ = 6,0 m/s", "m₂ = 2,0 kg, v₂ = 0"],
             jaaprekina=["u = ?", "ΔEk = ?"],
             formulas=["m₁v₁ = (m₁+m₂)u", "Ek = mv²/2"],
             aprekins=["1)  u = 4,0 · 6,0 : 6,0 = 4,0 m/s",
                       "2)  Ek(pirms) = 4,0 · 36 : 2 = 72 J",
                       "3)  Ek(pēc) = 6,0 · 16 : 2 = 48 J;  ΔEk = 24 J"],
             atbilde="u = 4,0 m/s ;   ΔEk = 24 J (33 % zudumi)",
             piezime="Zaudētā enerģija pārvērtās siltumā un "
                     "deformācijā."),
        dict(nr=2, virsraksts="Pilnīgi neelastīgs trieciens",
             teksts="Lode (20 g, 400 m/s) iestrēgst 2,0 kg koka klucī,\n"
                    "kas karājas uz virves. Aprēķini kluča ātrumu un\n"
                    "enerģijas zudumus!",
             dots=["m = 0,020 kg, v = 400 m/s", "M = 2,0 kg"],
             jaaprekina=["u = ?", "ΔEk = ?"],
             formulas=["mv = (m+M)u", "Ek = mv²/2"],
             aprekins=["1)  u = 0,020·400 : 2,02 = 3,96 ≈ 4,0 m/s",
                       "2)  Ek(pirms) = 0,020 · 160 000 : 2 = 1600 J",
                       "3)  Ek(pēc) = 2,02 · 15,7 : 2 = 15,9 J;  "
                       "ΔEk ≈ 1584 J"],
             atbilde="u ≈ 4,0 m/s ;   ΔEk ≈ 1,6·10³ J (99 % zudumi)",
             piezime="Gandrīz visa enerģija pārvērtās siltumā - "
                     "tāpēc lode un koks uzsilst."),
        dict(nr=3, virsraksts="Elastīgs trieciens",
             teksts="Divas vienādas masas bumbas: viena ar 5,0 m/s "
                    "trāpa\nmierā esošu; trieciens elastīgs.\n"
                    "Kādi būs ātrumi pēc trieciena?",
             dots=["m₁ = m₂ = m", "v₁ = 5,0 m/s", "v₂ = 0"],
             jaaprekina=["u₁ = ?", "u₂ = ?"],
             formulas=["Impulss: mv₁ = mu₁ + mu₂",
                       "Enerģija: v₁² = u₁² + u₂²"],
             aprekins=["1)  5,0 = u₁ + u₂",
                       "2)  25 = u₁² + u₂²",
                       "3)  Risinājums: u₁ = 0;  u₂ = 5,0 m/s"],
             atbilde="Pirmā apstājas, otrā aizkustas ar 5,0 m/s.",
             piezime="Klasisks biljarda gadījums - ātrums «pāriet» "
                     "pilnībā."),
        dict(nr=4, virsraksts="Zudumu daļa",
             teksts="Divi vienādas masas ķermeņi ar pretējiem, bet "
                    "vienādiem\nātrumiem saduras un saķeras.\n"
                    "Cik liela Ek daļa pazūd?",
             dots=["m₁ = m₂ = m", "v₁ = +v", "v₂ = −v"],
             jaaprekina=["ΔEk/Ek = ?"],
             formulas=["Σp = 0 → u = 0", "Ek(pirms) = 2·mv²/2 = mv²"],
             aprekins=["1)  Kopējais impulss: mv − mv = 0",
                       "2)  Tātad u = 0 - abi apstājas",
                       "3)  Ek(pēc) = 0 → zaudēti 100 %"],
             atbilde="Pazūd visa kinētiskā enerģija (100 %).",
             piezime="Impulss saglabājas (bija nulle, palika nulle), bet "
                     "enerģija - nē."),
        dict(nr=5, virsraksts="Elastīgs trieciens ar nevienādām masām",
             teksts="Ķermenis (2,0 kg, 6,0 m/s) elastīgi saduras ar "
                    "mierā\nesošu 4,0 kg ķermeni. Aprēķini abu ātrumus "
                    "pēc trieciena!",
             dots=["m₁ = 2,0 kg, v₁ = 6,0 m/s", "m₂ = 4,0 kg, v₂ = 0"],
             jaaprekina=["u₁ = ?", "u₂ = ?"],
             formulas=["u₁ = (m₁−m₂)v₁/(m₁+m₂)",
                       "u₂ = 2m₁v₁/(m₁+m₂)"],
             aprekins=["1)  m₁ + m₂ = 6,0 kg",
                       "2)  u₁ = (2,0 − 4,0)·6,0 : 6,0 = −2,0 m/s",
                       "3)  u₂ = 2·2,0·6,0 : 6,0 = 4,0 m/s"],
             atbilde="u₁ = 2,0 m/s atpakaļ ;   u₂ = 4,0 m/s uz priekšu",
             piezime="Vieglākais ķermenis atlec atpakaļ, ja triecas pret "
                     "smagāku - kā bumba pret sienu."),
        dict(nr=6, virsraksts="Elastīgs atsitiens pret sienu",
             teksts="Bumba (0,40 kg, 10 m/s) elastīgi atlec no sienas.\n"
                    "Aprēķini impulsa izmaiņu un pārbaudi kinētisko "
                    "enerģiju!",
             dots=["m = 0,40 kg", "v₁ = +10 m/s", "v₂ = −10 m/s"],
             jaaprekina=["Δp = ?", "ΔEk = ?"],
             formulas=["Δp = m(v₂ − v₁)", "Ek = mv²/2"],
             aprekins=["1)  Δp = 0,40 · (−10 − 10) = −8,0 kg·m/s",
                       "2)  Ek(pirms) = 0,40 · 100 : 2 = 20 J",
                       "3)  Ek(pēc) = 20 J → ΔEk = 0"],
             atbilde="|Δp| = 8,0 kg·m/s ;   ΔEk = 0 (elastīgs "
                     "trieciens)",
             piezime="Impulss mainījās, kaut enerģija saglabājās - tie "
                     "ir divi dažādi lielumi."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Impulss saglabājas visos triecienos.",
            "Elastīgā triecienā saglabājas arī kinētiskā enerģija.",
            "Neelastīgā triecienā daļa Ek pārvēršas siltumā.",
            "Pilnīgi neelastīgā triecienā ķermeņi kustas kopā.",
        ],
        majasdarbs=[
            "m₁ = 3,0 kg, v₁ = 8,0 m/s trāpa mierā esošu 5,0 kg; "
            "saķeras. Aprēķini u un ΔEk.",
            "Lode 15 g, 500 m/s iestrēgst 3,0 kg klucī. Aprēķini u.",
            "Paskaidro, kāpēc auto priekšgals ir projektēts deformēties.",
        ],
        pasvertejums=["Protu atšķirt trieciena veidus",
                      "Protu rēķināt enerģijas zudumus",
                      "Protu risināt elastīgu triecienu",
                      "Protu pamatot drošības risinājumus"],
        nakama="Nākamā stunda: enerģija un impulss kopā."),
),

dict(
    nr="5.11", virsraksts="Enerģija un impulss kopā",
    jautajums="Kad lietot enerģiju, kad impulsu?",
    apaksraksts="Metodes izvēle · Kombinēti uzdevumi · Ballistiskais "
                "svārsts",
    merkis="Iemācīties izvēlēties starp enerģijas un impulsa metodi un "
           "risināt uzdevumus, kur vajadzīgas abas.",
    protu=["izvēlēties piemēroto nezūdamības likumu;",
           "kombinēt abus likumus vienā uzdevumā;",
           "risināt ballistiskā svārsta uzdevumu;",
           "pamatot metodes izvēli."],
    atkartojums="Mums ir divi nezūdamības likumi: enerģijas (5.6.) un "
                "impulsa (5.9.). Šodien mācāmies izvēlēties pareizo un "
                "tos apvienot.",
    uzdevumu_apraksts="Metodes izvēle un kombinēti uzdevumi",
    teorija=[
        ("Kuru likumu lietot", [
            ("tabula",
             ["Situācija", "Lieto", "Kāpēc"],
             [["Trieciens, saduršanās", "Impulsu", "Ek nesaglabājas"],
              ["Krišana, slīdēšana bez berzes", "Enerģiju",
               "Impulss mainās (ārējs spēks)"],
              ["Sprādziens, atgrūšanās", "Impulsu", "Iekšējie spēki"],
              ["Atspere, svārsts", "Enerģiju", "Nav zudumu"],
              ["Trieciens + pacelšanās", "Abus pēc kārtas",
               "Divas fāzes"]],
             [4.60, 2.90, 4.73]),
            ("panelis", "GALVENAIS NOTEIKUMS",
             ["Triecienā - VIENMĒR impulss (Ek var pazust). Kustībā bez "
              "berzes - enerģija. Ja uzdevumā ir gan trieciens, gan "
              "kustība, tos risina PA DAĻĀM: vispirms impulss triecienam, "
              "tad enerģija kustībai."], NAVY),
        ]),
        ("Ballistiskais svārsts", [
            ("formula", "DIVAS FĀZES",
             "1. fāze (trieciens):  m v = (m + M) u        "
             "2. fāze (pacelšanās):  (m+M)u²/2 = (m+M)g h",
             "Klasisks uzdevums, kurā jālieto abi likumi. No pacelšanās "
             "augstuma var atrast lodes ātrumu: v = (m+M)/m · √(2gh).",
             GOLD),
            ("kartitas", [
                ("1. FĀZE", RED,
                 ["Trieciens - ļoti ātrs.",
                  "Impulss saglabājas.",
                  "Ek pazūd."]),
                ("2. FĀZE", GREEN,
                 ["Pacelšanās - lēna.",
                  "Enerģija saglabājas.",
                  "Ek → Ep."]),
                ("KĻŪDA", GOLD,
                 ["Lietot enerģiju triecienā.",
                  "Tad atbilde iznāk par lielu."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ballistiskais svārsts",
             teksts="Lode (10 g) iestrēgst 990 g klucī, kas uzkaras "
                    "0,20 m\naugstumā. Aprēķini lodes ātrumu! "
                    "(g = 9,8 m/s²)",
             dots=["m = 0,010 kg", "M = 0,990 kg", "h = 0,20 m"],
             jaaprekina=["v = ?"],
             formulas=["u = √(2gh)", "mv = (m+M)u"],
             aprekins=["1)  u = √(2 · 9,8 · 0,20) = √3,92 = 1,98 m/s",
                       "2)  (m+M)u = 1,00 · 1,98 = 1,98 kg·m/s",
                       "3)  v = 1,98 : 0,010 = 198 ≈ 2,0·10² m/s"],
             atbilde="v ≈ 2,0·10² m/s",
             piezime="Vispirms enerģija (2. fāzei), tad impulss "
                     "(1. fāzei) - atpakaļejošā secībā."),
        dict(nr=2, virsraksts="Trieciens un slīdēšana",
             teksts="Ķermenis (2,0 kg, 6,0 m/s) saķeras ar mierā esošu\n"
                    "1,0 kg un tie slīd, līdz apstājas; µ = 0,20.\n"
                    "Aprēķini noslīdēto ceļu! (g = 9,8 m/s²)",
             dots=["m₁ = 2,0 kg, v₁ = 6,0 m/s", "m₂ = 1,0 kg",
                   "µ = 0,20"],
             jaaprekina=["u = ?", "s = ?"],
             formulas=["m₁v₁ = (m₁+m₂)u", "u²/2 = µgs"],
             aprekins=["1)  u = 2,0 · 6,0 : 3,0 = 4,0 m/s",
                       "2)  s = u² : (2µg) = 16 : (2 · 0,20 · 9,8)",
                       "3)  s = 16 : 3,92 = 4,08 ≈ 4,1 m"],
             atbilde="u = 4,0 m/s ;   s ≈ 4,1 m",
             piezime="Divas fāzes: impulss triecienam, enerģija "
                     "slīdēšanai."),
        dict(nr=3, virsraksts="Metodes izvēle",
             teksts="Kuru likumu lietosi: a) bumba krīt no 10 m;\n"
                    "b) divi vagoni saduras un saķeras;\n"
                    "c) raķete izgrūž gāzes? Pamato katru!",
             dots=["trīs situācijas"],
             jaaprekina=["metode = ?"],
             formulas=["Trieciens/sprādziens → impulss; kustība → "
                       "enerģija"],
             aprekins=["1)  a) Enerģija - ārējs spēks maina impulsu",
                       "2)  b) Impulss - triecienā Ek nesaglabājas",
                       "3)  c) Impulss - iekšēji spēki slēgtā sistēmā"],
             atbilde="a) enerģija;  b) impulss;  c) impulss.",
             piezime="Metodes izvēle ir puse no risinājuma."),
        dict(nr=4, virsraksts="Sprādziens",
             teksts="Mierā esošs 5,0 kg ķermenis sprāgst divās daļās:\n"
                    "2,0 kg aizlido ar 30 m/s. Aprēķini otrās daļas\n"
                    "ātrumu un atbrīvoto enerģiju!",
             dots=["M = 5,0 kg", "m₁ = 2,0 kg, u₁ = 30 m/s",
                   "m₂ = 3,0 kg"],
             jaaprekina=["u₂ = ?", "E = ?"],
             formulas=["0 = m₁u₁ + m₂u₂", "E = Ek₁ + Ek₂"],
             aprekins=["1)  u₂ = −2,0 · 30 : 3,0 = −20 m/s",
                       "2)  Ek₁ = 2,0 · 900 : 2 = 900 J",
                       "3)  Ek₂ = 3,0 · 400 : 2 = 600 J;  E = 1500 J"],
             atbilde="u₂ = 20 m/s pretējā virzienā;  E = 1,5·10³ J",
             piezime="Enerģija radās no sprāgstvielas - tā nav "
                     "mehāniskās enerģijas nezūdamības pārkāpums."),
        dict(nr=5, virsraksts="Lode izlido cauri",
             teksts="Lode (20 g, 500 m/s) izlido cauri mierā esošam "
                    "1,0 kg\nklucim un turpina lidot ar 200 m/s.\n"
                    "Aprēķini kluča ātrumu!",
             dots=["m = 0,020 kg", "v₁ = 500 m/s", "v₂ = 200 m/s",
                   "M = 1,0 kg"],
             jaaprekina=["u = ?"],
             formulas=["mv₁ = mv₂ + Mu", "u = m(v₁ − v₂)/M"],
             aprekins=["1)  v₁ − v₂ = 300 m/s",
                       "2)  m(v₁ − v₂) = 0,020 · 300 = 6,0 kg·m/s",
                       "3)  u = 6,0 : 1,0 = 6,0 m/s"],
             atbilde="u = 6,0 m/s",
             piezime="Klucis iegūst tieši to impulsu, ko lode zaudēja."),
        dict(nr=6, virsraksts="Sprādziens divās daļās",
             teksts="Mierā esošs 8,0 kg ķermenis sprāgst: 3,0 kg daļa\n"
                    "aizlido ar 40 m/s. Aprēķini otrās daļas ātrumu un\n"
                    "atbrīvoto enerģiju!",
             dots=["M = 8,0 kg", "m₁ = 3,0 kg, u₁ = 40 m/s",
                   "m₂ = 5,0 kg"],
             jaaprekina=["u₂ = ?", "E = ?"],
             formulas=["0 = m₁u₁ + m₂u₂", "E = Ek₁ + Ek₂"],
             aprekins=["1)  u₂ = −3,0 · 40 : 5,0 = −24 m/s",
                       "2)  Ek₁ = 3,0 · 1600 : 2 = 2400 J",
                       "3)  Ek₂ = 5,0 · 576 : 2 = 1440 J;  E = 3840 J"],
             atbilde="u₂ = 24 m/s pretējā virzienā ;   E ≈ 3,8·10³ J",
             piezime="Impulss palika nulle, bet enerģija radās no "
                     "sprāgstvielas ķīmiskās enerģijas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Triecienā vienmēr lieto impulsa nezūdamību.",
            "Kustībā bez berzes - enerģijas nezūdamību.",
            "Kombinētos uzdevumos fāzes risina atsevišķi.",
            "Sprādzienā enerģija rodas no iekšējiem avotiem.",
        ],
        majasdarbs=[
            "Lode 12 g, kluči 1,2 kg, h = 0,15 m. Aprēķini lodes "
            "ātrumu.",
            "m₁ = 4,0 kg, 5,0 m/s saķeras ar 2,0 kg; µ = 0,25. Aprēķini "
            "ceļu.",
            "M = 8,0 kg sprāgst: 3,0 kg ar 20 m/s. Aprēķini otras daļas "
            "ātrumu un E.",
        ],
        pasvertejums=["Protu izvēlēties metodi",
                      "Protu risināt divfāžu uzdevumus",
                      "Protu rēķināt ballistisko svārstu",
                      "Protu pamatot izvēli"],
        nakama="Nākamā stunda: temata nostiprināšana."),
),

dict(
    nr="5.12", virsraksts="Temata nostiprināšana",
    jautajums="Kā pamatot enerģijas pārvērtību ķēdi?",
    apaksraksts="Atgādne · Enerģijas ķēdes · PD6 formāts",
    merkis="Apkopot 5. temata saturu un nostiprināt enerģijas un impulsa "
           "uzdevumus pirms PD6.",
    protu=["izvēlēties pareizo sakarību;",
           "aprakstīt enerģijas pārvērtību ķēdi;",
           "risināt kombinētus uzdevumus;",
           "sagatavoties PD6."],
    atkartojums="Temats aptvēra darbu, jaudu, lietderību, kinētisko un "
                "potenciālo enerģiju, nezūdamības likumus, impulsu un "
                "triecienus.",
    uzdevumu_apraksts="Kombinēti uzdevumi PD6 formātā",
    teorija=[
        ("Temata atgādne", [
            ("formula", "DARBS, JAUDA UN ENERĢIJA",
             "A = F s cos α   ·   P = A/t = F v   ·   "
             "η = A(lietd)/A(patēr)·100 %   ·   Ek = mv²/2   ·   "
             "Ep = mgh   ·   Ep = kx²/2",
             "Enerģijas nezūdamība: Ek + Ep = const (bez berzes); "
             "ar berzi Ep = Ek + Q.", GOLD),
            ("formula", "IMPULSS UN TRIECIENI",
             "p = m v   ·   F t = Δp   ·   "
             "m₁v₁ + m₂v₂ = m₁u₁ + m₂u₂",
             "Impulss saglabājas visos triecienos; kinētiskā enerģija - "
             "tikai elastīgajos.", GOLD),
        ]),
        ("Enerģijas pārvērtību ķēdes", [
            ("tabula",
             ["Process", "Enerģijas ķēde", "Zudumi"],
             [["Ķermenis krīt", "Ep → Ek", "Gaisa pretestība"],
              ["Automašīna brauc", "Ķīmiskā → Ek + Q", "Dzinējs, berze"],
              ["Hidroelektrostacija", "Ep → Ek → Elektriskā", "Berze"],
              ["Vēja ģenerators", "Vēja Ek → Elektriskā", "Turbulence"],
              ["Trieciens", "Ek → Q + deformācija", "Neatgriezeniski"]],
             [4.30, 4.60, 3.33]),
            ("panelis", "PD6 FORMĀTS",
             ["Tests (10 p.) par darbu, enerģiju, jaudu un impulsu; "
              "lielumu un mērvienību tabula (5 p.); divi aprēķinu "
              "uzdevumi ar pilnu pierakstu (10 p.); uzdevums ar "
              "apakšjautājumiem par enerģijas bilanci vai triecienu "
              "(5 p.). Kopā 30 punkti, 40 minūtes."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Darbs un jauda",
             teksts="Celtnis paceļ 600 kg kravu 20 m augstumā 25 s laikā;\n"
                    "η = 80 %. Aprēķini patērēto jaudu! (g = 9,8 m/s²)",
             dots=["m = 600 kg", "h = 20 m", "t = 25 s", "η = 0,80"],
             jaaprekina=["P(patēr) = ?"],
             formulas=["A = mgh", "P(lietd) = A/t",
                       "P(pat) = P(lietd)/η"],
             aprekins=["1)  A = 600 · 9,8 · 20 = 1,176·10⁵ J",
                       "2)  P(lietd) = 1,176·10⁵ : 25 = 4704 W",
                       "3)  P(pat) = 4704 : 0,80 = 5880 W ≈ 5,9 kW"],
             atbilde="P(patēr) ≈ 5,9 kW",
             piezime="20 % jaudas aiziet berzē un trošu pretestībā."),
        dict(nr=2, virsraksts="Enerģijas nezūdamība",
             teksts="Ķermenis noslīd no 8,0 m augstas slidkalniņa;\n"
                    "apakšā v = 10 m/s. Cik liela enerģijas daļa\n"
                    "zaudēta berzē? (g = 9,8 m/s²)",
             dots=["h = 8,0 m", "v = 10 m/s"],
             jaaprekina=["daļa = ?"],
             formulas=["Ep = mgh", "Ek = mv²/2", "daļa = (Ep−Ek)/Ep"],
             aprekins=["1)  Ep = m · 9,8 · 8,0 = 78,4m",
                       "2)  Ek = m · 100 : 2 = 50m",
                       "3)  (78,4 − 50) : 78,4 = 0,362 = 36 %"],
             atbilde="Berzē zaudēti ≈ 36 % enerģijas.",
             piezime="Masa saīsinās - atbilde nav atkarīga no masas."),
        dict(nr=3, virsraksts="Trieciens",
             teksts="Vagons (15 t, 2,0 m/s) saduras ar mierā esošu\n"
                    "(10 t) un saķeras. Aprēķini kopējo ātrumu un\n"
                    "enerģijas zudumus!",
             dots=["m₁ = 15 000 kg, v₁ = 2,0 m/s", "m₂ = 10 000 kg"],
             jaaprekina=["u = ?", "ΔEk = ?"],
             formulas=["m₁v₁ = (m₁+m₂)u", "Ek = mv²/2"],
             aprekins=["1)  u = 15 000 · 2,0 : 25 000 = 1,2 m/s",
                       "2)  Ek(pirms) = 15 000 · 4,0 : 2 = 30 000 J",
                       "3)  Ek(pēc) = 25 000 · 1,44 : 2 = 18 000 J;  "
                       "ΔEk = 1,2·10⁴ J"],
             atbilde="u = 1,2 m/s ;   ΔEk = 1,2·10⁴ J (40 %)",
             piezime="Neelastīgā triecienā vienmēr ir zudumi."),
        dict(nr=4, virsraksts="Spēks no impulsa",
             teksts="Cilvēks (70 kg) nolec no 1,25 m augstuma un "
                    "apstājas\n0,20 s laikā. Aprēķini vidējo spēku! "
                    "(g = 9,8 m/s²)",
             dots=["m = 70 kg", "h = 1,25 m", "t = 0,20 s"],
             jaaprekina=["v = ?", "F = ?"],
             formulas=["v = √(2gh)", "F = mv/t"],
             aprekins=["1)  v = √(2 · 9,8 · 1,25) = √24,5 = 4,95 m/s",
                       "2)  Δp = 70 · 4,95 = 347 kg·m/s",
                       "3)  F = 347 : 0,20 = 1733 ≈ 1,7·10³ N"],
             atbilde="F ≈ 1,7·10³ N (2,5 reizes lielāks par svaru)",
             piezime="Locot kājas, laiks pagarinās un spēks samazinās - "
                     "tāpēc tā jādara."),
        dict(nr=5, virsraksts="Jauda kāpumā",
             teksts="Automašīna (1000 kg) brauc augšup pa 5 % kāpumu ar\n"
                    "20 m/s. Aprēķini jaudu, kas vajadzīga tikai "
                    "pacelšanai!\n(5 % kāpums nozīmē sin α ≈ 0,05; "
                    "g = 9,8 m/s²)",
             dots=["m = 1000 kg", "v = 20 m/s", "sin α = 0,05"],
             jaaprekina=["F = ?", "P = ?"],
             formulas=["F = mg sin α", "P = Fv"],
             aprekins=["1)  mg = 1000 · 9,8 = 9800 N",
                       "2)  F = 9800 · 0,05 = 490 N",
                       "3)  P = 490 · 20 = 9800 W ≈ 9,8 kW"],
             atbilde="P ≈ 9,8 kW tikai kāpuma pārvarēšanai",
             piezime="Šim vēl jāpieskaita jauda berzes un gaisa "
                     "pretestības pārvarēšanai."),
        dict(nr=6, virsraksts="Sadursme ar sienu",
             teksts="Automašīna (1200 kg, 15 m/s) atsitas pret sienu un\n"
                    "apstājas 0,15 s laikā. Aprēķini vidējo spēku un\n"
                    "izkliedēto enerģiju!",
             dots=["m = 1200 kg", "v = 15 m/s", "t = 0,15 s"],
             jaaprekina=["F = ?", "Ek = ?"],
             formulas=["F = mv/t", "Ek = mv²/2"],
             aprekins=["1)  Δp = 1200 · 15 = 1,8·10⁴ kg·m/s",
                       "2)  F = 1,8·10⁴ : 0,15 = 1,2·10⁵ N",
                       "3)  Ek = 1200 · 225 : 2 = 1,35·10⁵ J"],
             atbilde="F = 1,2·10⁵ N ;   Ek = 1,35·10⁵ J",
             piezime="Deformācijas zona pagarina laiku un tieši tāpēc "
                     "samazina spēku."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Triecienā - impulss; kustībā bez berzes - enerģija.",
            "η vienmēr < 100 %; zudumi pārvēršas siltumā.",
            "Enerģijas uzdevumos masa bieži saīsinās.",
            "Ft = Δp izskaidro visus drošības risinājumus.",
        ],
        majasdarbs=[
            "Atkārto abas atgādnes pirms PD6.",
            "Izpildi pa vienam uzdevumam no katra veida.",
            "Pārskati LD4 protokolu un enerģijas bilanci.",
        ],
        pasvertejums=["Protu izvēlēties sakarību",
                      "Protu aprakstīt enerģijas ķēdi",
                      "Protu risināt triecienus",
                      "Esmu gatavs PD6"],
        nakama="Nākamā stunda: PD6 - enerģija, darbs un impulss."),
),

dict(
    nr="5.13", virsraksts="Kļūdu analīze",
    jautajums="Ko paņemam līdzi uz 11. klasi?",
    apaksraksts="PD6 kļūdas · Gada kopsavilkums · Kas būs tālāk",
    merkis="Analizēt PD6 kļūdas un apkopot visu gadā apgūto pirms "
           "noslēguma stundām.",
    protu=["izlabot PD6 kļūdas;",
           "atpazīt, kuras metodes izmantoju biežāk;",
           "sastādīt gada kopsavilkuma atgādni;",
           "nosaukt, kas gaida 11. klasē."],
    atkartojums="PD6 bija pēdējais 10. klases pārbaudes darbs. Šodien "
                "kļūdas pārvēršam prasmēs un skatāmies uz priekšu.",
    uzdevumu_apraksts="Kļūdu labošana un gada kopsavilkums",
    teorija=[
        ("Biežākās PD6 kļūdas", [
            ("tabula",
             ["Kļūda", "Kā izskatās", "Pareizi"],
             [["Enerģija triecienā", "Ek saglabājas saķeroties",
               "Lieto impulsu"],
              ["Aizmirsts cos α", "A = Fs vienmēr", "A = Fs cos α"],
              ["η > 100 %", "Sajaukts lietd. un patēr.",
               "η = lietd/patēr"],
              ["Impulss bez zīmēm", "p₁ + p₂ vienmēr saskaita",
               "Zīme pēc virziena"],
              ["Ek ~ v", "Divreiz ātrāk - divreiz vairāk", "Ek ~ v²"]],
             [3.60, 4.30, 4.33]),
            ("panelis", "KĀ IZVAIRĪTIES",
             ["Pirms risināšanas atbildi uz diviem jautājumiem: "
              "1) Vai šeit ir trieciens? Ja jā - impulss.  2) Vai ir "
              "berze? Ja jā - mehāniskā enerģija nesaglabājas. Šie divi "
              "jautājumi novērš lielāko daļu kļūdu."], NAVY),
        ]),
        ("Gada kopsavilkums", [
            ("tabula",
             ["Temats", "Galvenā ideja", "Galvenās sakarības"],
             [["1. Kustības apraksts", "Kā ķermenis kustas",
               "v = s/t; x = x₀+vt"],
              ["2. Paātrināta kustība", "Ātrums mainās",
               "v = v₀+at; s = v₀t+at²/2"],
              ["3. Spēki", "Kāpēc ķermenis kustas",
               "F = ma; F(b) = µN"],
              ["4. Gravitācija", "Universāls spēks",
               "F = Gm₁m₂/r²; v = √(GM/r)"],
              ["5. Enerģija", "Nezūdamības likumi",
               "Ek+Ep = const; Σp = const"]],
             [3.60, 3.60, 5.03]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atrodi kļūdu I",
             teksts="«Divi ķermeņi saduras un saķeras. Kinētiskā "
                    "enerģija\nsaglabājas, tāpēc m₁v₁²/2 = (m₁+m₂)u²/2.»\n"
                    "Izlabo!",
             dots=["neelastīgs trieciens"],
             jaaprekina=["pareizais vienādojums = ?"],
             formulas=["Triecienā saglabājas IMPULSS"],
             aprekins=["1)  Saķeroties Ek NEsaglabājas",
                       "2)  Pareizi: m₁v₁ = (m₁+m₂)u",
                       "3)  Enerģijas zudumus var aprēķināt pēc tam"],
             atbilde="Jālieto impulsa nezūdamība, nevis enerģijas.",
             piezime="Šī ir visbiežākā PD6 kļūda."),
        dict(nr=2, virsraksts="Atrodi kļūdu II",
             teksts="«Spēks 100 N, ceļš 20 m, leņķis 60°.\n"
                    "A = 100 · 20 = 2000 J.»\nIzlabo!",
             dots=["F = 100 N", "s = 20 m", "α = 60°"],
             jaaprekina=["A = ?"],
             formulas=["A = Fs cos α", "cos 60° = 0,50"],
             aprekins=["1)  Kļūda: aizmirsts cos α",
                       "2)  cos 60° = 0,50",
                       "3)  A = 100 · 20 · 0,50 = 1000 J"],
             atbilde="A = 1000 J, nevis 2000 J.",
             piezime="Formula A = Fs der tikai tad, ja α = 0°."),
        dict(nr=3, virsraksts="Atrodi kļūdu III",
             teksts="«Automašīnas ātrumu palielina 2 reizes, tāpēc\n"
                    "kinētiskā enerģija palielinās 2 reizes.»\nIzlabo!",
             dots=["v₂ = 2v₁"],
             jaaprekina=["Ek₂/Ek₁ = ?"],
             formulas=["Ek = mv²/2", "Ek ~ v²"],
             aprekins=["1)  Kļūda: aizmirsts kvadrāts",
                       "2)  Ek₂/Ek₁ = (v₂/v₁)² = 4",
                       "3)  Enerģija palielinās 4 reizes"],
             atbilde="Ek palielinās 4 reizes, nevis 2.",
             piezime="Tieši šī kvadrātiskā atkarība padara ātrumu "
                     "bīstamu."),
        dict(nr=4, virsraksts="Atrodi kļūdu IV",
             teksts="«Ķermenis bija mierā un sprādzienā sadalījās divās\n"
                    "kustīgās daļās, tātad impulsa nezūdamības likums "
                    "šeit\nnedarbojas.» Izvērtē apgalvojumu!",
             dots=["sākumā p = 0", "divas daļas kustas"],
             jaaprekina=["Vai likums darbojas?"],
             formulas=["Σp(pirms) = Σp(pēc)"],
             aprekins=["1)  Sākumā kopējais impulss ir nulle",
                       "2)  Daļas aizlido pretējos virzienos",
                       "3)  m₁u₁ + m₂u₂ = 0 - summa joprojām nulle"],
             atbilde="Likums darbojas: atsevišķie impulsi nav nulle, bet "
                     "to VEKTORU summa ir.",
             piezime="Impulss ir vektors - vienmēr summē ar zīmēm, ne "
                     "moduļus."),
        dict(nr=5, virsraksts="Atrodi kļūdu V",
             teksts="«Dzinējs paveic 6,0·10⁴ J darbu 30 s laikā;\n"
                    "P = A · t = 6,0·10⁴ · 30 = 1,8·10⁶ W.»\nIzlabo!",
             dots=["A = 6,0·10⁴ J", "t = 30 s"],
             jaaprekina=["P = ?"],
             formulas=["P = A/t"],
             aprekins=["1)  Kļūda: darbs sareizināts ar laiku",
                       "2)  P = 6,0·10⁴ : 30",
                       "3)  P = 2,0·10³ W = 2,0 kW"],
             atbilde="P = 2,0 kW, nevis 1,8 MW.",
             piezime="Mērvienību pārbaude uzreiz atklāj kļūdu: J·s nav "
                     "vats."),
        dict(nr=6, virsraksts="Atrodi kļūdu VI",
             teksts="«Dzinējs patērē 3,0 kW un veic 3,6 kW lietderīgu\n"
                    "darbu, tātad η = 120 %.»\nIzvērtē rezultātu!",
             dots=["P(pat) = 3,0 kW", "P(lietd) = 3,6 kW"],
             jaaprekina=["Vai iespējams?"],
             formulas=["η = P(lietd)/P(pat) ≤ 1"],
             aprekins=["1)  Lietderīgā jauda nevar pārsniegt patērēto",
                       "2)  Tas nozīmētu enerģijas rašanos no nekā",
                       "3)  Kļūda ir mērījumos vai aprēķinā"],
             atbilde="η > 100 % nav iespējams - jāmeklē kļūda datos.",
             piezime="Ticamības pārbaude: η vienmēr ir robežās no 0 līdz "
                     "100 %."),
        dict(nr=7, virsraksts="Gada atgādne",
             teksts="Sastādi gada kopsavilkuma atgādni: pa vienai\n"
                    "galvenajai sakarībai no katra temata!",
             dots=["5 temati"],
             jaaprekina=["atgādne = ?"],
             formulas=["Viena sakarība no katra temata"],
             aprekins=["1)  1. temats: v = s/t;  2. temats: v = v₀ + at",
                       "2)  3. temats: F = ma;  "
                       "4. temats: F = Gm₁m₂/r²",
                       "3)  5. temats: Ek + Ep = const un Σp = const"],
             atbilde="Sešas pamatsakarības, kas aptver visu gadu.",
             piezime="Šo atgādni izmantosi arī 11. klasē un eksāmenā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Triecienā - impulss, ne enerģija.",
            "A = Fs cos α - cos α nedrīkst aizmirst.",
            "Ek ~ v² - kvadrātiska atkarība.",
            "Divi jautājumi pirms risināšanas novērš lielāko daļu kļūdu.",
        ],
        majasdarbs=[
            "Izlabo savas PD6 kļūdas pilnā pierakstā.",
            "Pabeidz gada kopsavilkuma atgādni.",
            "Padomā, kurš temats tev padevās vislabāk un kurš prasa "
            "atkārtošanu.",
        ],
        pasvertejums=["Protu atpazīt savu kļūdu",
                      "Protu izvēlēties pareizo metodi",
                      "Man ir gada atgādne",
                      "Zinu, kas jāatkārto"],
        nakama="Nākamā stunda: mehānika ap mums."),
),

dict(
    nr="5.14", virsraksts="Mehānika ap mums",
    jautajums="Kur mehānika parādās ikdienā?",
    apaksraksts="Transports · Sports · Celtniecība · Drošība",
    merkis="Saskatīt gadā apgūtās sakarības reālās situācijās un pamatot "
           "praktiskus risinājumus ar fiziku.",
    protu=["izskaidrot satiksmes drošības risinājumus;",
           "analizēt sporta kustības ar fizikas jēdzieniem;",
           "pamatot celtniecības risinājumus;",
           "atpazīt fiziku ikdienas ierīcēs."],
    atkartojums="Gads ir apgūts. Šodien skatāmies, kur šīs zināšanas "
                "reāli noder - un kāpēc tās mācījāmies.",
    uzdevumu_apraksts="Fizika reālās situācijās",
    teorija=[
        ("Mehānika transportā", [
            ("tabula",
             ["Risinājums", "Fizikas pamats", "Sakarība"],
             [["Ātruma ierobežojums", "Ek un bremzēšanas ceļš",
               "Ek ~ v²; s ~ v²"],
              ["Drošības josta", "Inerce un spēka impulss", "Ft = Δp"],
              ["Deformējamā zona", "Trieciena laika pagarināšana",
               "F = Δp/t"],
              ["Riepu protektors", "Berzes koeficients", "F(b) = µN"],
              ["ABS bremzes", "Miera berze > slīdes berze", "µ₀ > µ"]],
             [3.90, 4.30, 4.03]),
        ]),
        ("Sports un celtniecība", [
            ("divi",
             ("SPORTS", GREEN,
              ["Tāllēkšana - mešanas leņķis 45°.",
               "Šķēpmešana - Ek = mv²/2.",
               "Slēpošana - berze un slīpā plakne.",
               "Airēšana - Ņūtona trešais likums."]),
             ("CELTNIECĪBA", BLUE,
              ["Spriegums σ = F/S.",
               "Drošības koeficients.",
               "Momenti - sijas un balsti.",
               "Spiediens uz pamatiem p = F/S.",
               "Celtņi - svira un bloki."])),
            ("panelis", "KĀPĒC TO MĀCĀMIES",
             ["Fizikas kurss nav formulu krājums. Tas ir domāšanas veids: "
              "no situācijas nonākt līdz modelim, no modeļa - līdz "
              "skaitliskai atbildei, un pēc tam pārbaudīt, vai atbilde ir "
              "ticama. Tieši šo prasmi pārbauda eksāmens."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātruma ierobežojums",
             teksts="Pamato ar aprēķinu, kāpēc apdzīvotās vietās ātrums\n"
                    "ir ierobežots līdz 50 km/h, nevis 70 km/h!\n"
                    "(µ = 0,70; reakcijas laiks 1,0 s; g = 9,8 m/s²)",
             dots=["v₁ = 50 km/h = 13,9 m/s", "v₂ = 70 km/h = 19,4 m/s"],
             jaaprekina=["s₁ = ?", "s₂ = ?"],
             formulas=["s = v·t(r) + v²/(2µg)"],
             aprekins=["1)  s₁ = 13,9 + 193 : 13,7 = 13,9 + 14,1 = 28 m",
                       "2)  s₂ = 19,4 + 376 : 13,7 = 19,4 + 27,4 = 47 m",
                       "3)  Starpība 19 m"],
             atbilde="Pie 70 km/h apstāšanās ceļš ir 47 m pret 28 m - "
                     "par 19 m garāks.",
             piezime="19 m ir vairāk nekā gājēju pārejas platums - tā ir "
                     "atšķirība starp apstāšanos un sadursmi."),
        dict(nr=2, virsraksts="Tāllēkšana",
             teksts="Sportists atspērās ar 9,0 m/s 45° leņķī.\n"
                    "Aprēķini lēciena tālumu! (g = 9,8 m/s²;\n"
                    "sin 90° = 1)",
             dots=["v₀ = 9,0 m/s", "α = 45°"],
             jaaprekina=["L = ?"],
             formulas=["L = v₀² sin(2α) / g"],
             aprekins=["1)  sin(2 · 45°) = sin 90° = 1",
                       "2)  v₀² = 81 m²/s²",
                       "3)  L = 81 : 9,8 = 8,27 ≈ 8,3 m"],
             atbilde="L ≈ 8,3 m",
             piezime="Pasaules rekords ir 8,95 m - modelis ir tuvu "
                     "realitātei."),
        dict(nr=3, virsraksts="Sijas noslodze",
             teksts="Uz 5,0 m garas sijas ar balstiem galos 2,0 m no "
                    "kreisā\ngala novietota 800 kg krava. Aprēķini abu "
                    "balstu\nspēkus! (g = 9,8 m/s²)",
             dots=["L = 5,0 m", "m = 800 kg", "a = 2,0 m"],
             jaaprekina=["N₁ = ?", "N₂ = ?"],
             formulas=["N₁L = mg(L−a)", "N₁ + N₂ = mg"],
             aprekins=["1)  mg = 800 · 9,8 = 7840 N",
                       "2)  N₁ = 7840 · 3,0 : 5,0 = 4704 N",
                       "3)  N₂ = 7840 − 4704 = 3136 N"],
             atbilde="N₁ ≈ 4,7·10³ N ;   N₂ ≈ 3,1·10³ N",
             piezime="Tuvākais balsts nes lielāku daļu kravas."),
        dict(nr=4, virsraksts="Velosipēda pārnesums",
             teksts="Priekšējais zobrats 48 zobi, aizmugurējais 16 zobi,\n"
                    "riteņa rādiuss 0,35 m. Cik tālu velosipēds "
                    "aizbrauc\nvienā pedāļu apgriezienā? (π ≈ 3,14)",
             dots=["z₁ = 48", "z₂ = 16", "R = 0,35 m"],
             jaaprekina=["s = ?"],
             formulas=["n = z₁/z₂", "s = n · 2πR"],
             aprekins=["1)  n = 48 : 16 = 3 riteņa apgriezieni",
                       "2)  2πR = 2 · 3,14 · 0,35 = 2,20 m",
                       "3)  s = 3 · 2,20 = 6,6 m"],
             atbilde="s ≈ 6,6 m",
             piezime="Tas pats pārnesumu princips, ko mācījāmies "
                     "2.12. stundā."),
        dict(nr=5, virsraksts="Nolēciena spēks",
             teksts="Cilvēks (60 kg) nolec no 0,80 m augstuma.\n"
                    "Aprēķini spēku, ja apstāšanās laiks ir 0,10 s un ja "
                    "tas ir\n0,40 s (locot kājas)! (g = 9,8 m/s²)",
             dots=["m = 60 kg", "h = 0,80 m", "t₁ = 0,10 s",
                   "t₂ = 0,40 s"],
             jaaprekina=["v = ?", "F₁ = ?", "F₂ = ?"],
             formulas=["v = √(2gh)", "F = mv/t"],
             aprekins=["1)  v = √(2 · 9,8 · 0,80) = √15,7 = 3,96 m/s",
                       "2)  Δp = 60 · 3,96 = 238 kg·m/s",
                       "3)  F₁ = 2380 N ;  F₂ = 594 N"],
             atbilde="F₁ ≈ 2,4·10³ N ;   F₂ ≈ 5,9·10² N - 4 reizes "
                     "mazāks.",
             piezime="Locot kājas, laiks pagarinās 4 reizes un spēks "
                     "samazinās tikpat."),
        dict(nr=6, virsraksts="Vēja ģeneratora jauda",
             teksts="Cauri ģeneratora ripai katru sekundi izplūst "
                    "1,2·10⁴ kg\ngaisa ar ātrumu 8,0 m/s. Aprēķini "
                    "plūsmas kinētisko\nenerģiju sekundē!",
             dots=["m = 1,2·10⁴ kg katrā sekundē", "v = 8,0 m/s",
                   "t = 1,0 s"],
             jaaprekina=["Ek = ?", "P = ?"],
             formulas=["Ek = mv²/2", "P = Ek/t"],
             aprekins=["1)  v² = 64 m²/s²",
                       "2)  Ek = 1,2·10⁴ · 64 : 2 = 3,84·10⁵ J",
                       "3)  P = 3,84·10⁵ : 1,0 = 3,84·10⁵ W"],
             atbilde="P ≈ 3,8·10⁵ W = 380 kW",
             piezime="Reāli ģenerators izmanto ap 40 % no šīs jaudas - "
                     "gaiss nedrīkst apstāties pilnībā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Satiksmes drošības noteikumi balstās uz Ek ~ v² un Ft = Δp.",
            "Sportā darbojas tie paši mešanas un enerģijas likumi.",
            "Celtniecībā izmanto spriegumu, momentus un spiedienu.",
            "Fizika ir domāšanas veids, ne formulu krājums.",
        ],
        majasdarbs=[
            "Atrodi savā ikdienā trīs piemērus, kur darbojas gadā "
            "apgūtās sakarības.",
            "Aprēķini apstāšanās ceļu pie 90 km/h uz slapja asfalta "
            "(µ = 0,40).",
            "Sagatavo vienu jautājumu par fiziku, uz kuru vēlies "
            "atbildi.",
        ],
        pasvertejums=["Protu izskaidrot drošības risinājumus",
                      "Protu analizēt sporta kustības",
                      "Protu pamatot celtniecības risinājumus",
                      "Saskatu fiziku ikdienā"],
        nakama="Nākamā stunda: gada noslēgums."),
),

dict(
    nr="5.15", virsraksts="Gada noslēgums",
    jautajums="Ko protam, sākot 11. klasi?",
    apaksraksts="Gada kopsavilkums · Pašvērtējums · Kas gaida tālāk",
    merkis="Apkopot gada laikā apgūto, novērtēt savu sniegumu un "
           "saplānot, kas jāatkārto pirms 11. klases.",
    protu=["nosaukt visu piecu tematu galvenās idejas;",
           "novērtēt savas prasmes katrā tematā;",
           "saplānot atkārtošanu;",
           "nosaukt, kas tiks apgūts 11. klasē."],
    atkartojums="Gads sākās ar vektoriem un beidzas ar impulsa "
                "nezūdamību. Šodien to visu saliekam kopā.",
    uzdevumu_apraksts="Gada kopsavilkuma uzdevumi",
    teorija=[
        ("Gada saturs vienā lapā", [
            ("tabula",
             ["Temats", "Ko protam", "Eksāmenā"],
             [["1. Kustība", "Aprakstīt kustību, lasīt grafikus",
               "Vienmēr"],
              ["2. Paātrinājums", "Krišana, mešana, riņķa kustība",
               "Bieži"],
              ["3. Spēki", "Ņūtona likumi, berze, hidrostatika",
               "Vienmēr"],
              ["4. Gravitācija", "Orbītas, kosmiskie ātrumi", "Reizēm"],
              ["5. Enerģija", "Nezūdamības likumi, triecieni",
               "Vienmēr"]],
             [3.30, 5.30, 3.63]),
            ("panelis", "KAS GAIDA 11. KLASĒ",
             ["6.-14. temats: mehāniskās svārstības un viļņi, vielas "
              "uzbūve, siltums, elektrība, elektromagnētisms, "
              "elektromagnētiskie viļņi, optika, atoms un Visums. "
              "Mehānikas prasmes noderēs katrā no tiem - un 11. klases "
              "beigās gaida centralizētais eksāmens."], NAVY),
        ]),
        ("Kā gatavoties eksāmenam", [
            ("kartitas", [
                ("REGULĀRI", GREEN,
                 ["Pa vienam uzdevumam nedēļā.",
                  "Vasarā - atkārtošanas lapa.",
                  "Labāk nekā viss maijā."]),
                ("PĒC TEMATIEM", BLUE,
                 ["Vispirms - vājākie temati.",
                  "Tad - kombinētie uzdevumi.",
                  "Beigās - vecie eksāmeni."]),
                ("AR PIERAKSTU", GOLD,
                 ["Vienmēr pilns pieraksts.",
                  "Dots-Jāaprēķina-Formulas-",
                  "Aprēķins-Atbilde."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kombinēts uzdevums I",
             teksts="Automašīna (1200 kg) no miera 10 s laikā sasniedz\n"
                    "90 km/h. Aprēķini paātrinājumu, spēku, ceļu un "
                    "vidējo\njaudu!",
             dots=["m = 1200 kg", "v = 25 m/s", "t = 10 s", "v₀ = 0"],
             jaaprekina=["a, F, s, P = ?"],
             formulas=["a = v/t", "F = ma", "s = at²/2", "P = A/t"],
             aprekins=["1)  a = 25 : 10 = 2,5 m/s²;  "
                       "F = 1200 · 2,5 = 3000 N",
                       "2)  s = 2,5 · 100 : 2 = 125 m",
                       "3)  A = 3000 · 125 = 3,75·10⁵ J;  "
                       "P = 3,75·10⁴ W"],
             atbilde="a = 2,5 m/s² ;  F = 3,0 kN ;  s = 125 m ;  "
                     "P ≈ 38 kW",
             piezime="Viens uzdevums - četri temati kopā."),
        dict(nr=2, virsraksts="Kombinēts uzdevums II",
             teksts="Ķermenis (0,50 kg) noslīd no 3,0 m augsta "
                    "slidkalniņa\nbez berzes un saduras ar mierā esošu "
                    "1,0 kg ķermeni,\nsaķeroties. Aprēķini kopējo "
                    "ātrumu! (g = 9,8 m/s²)",
             dots=["m₁ = 0,50 kg", "h = 3,0 m", "m₂ = 1,0 kg"],
             jaaprekina=["v = ?", "u = ?"],
             formulas=["v = √(2gh)", "m₁v = (m₁+m₂)u"],
             aprekins=["1)  v = √(2 · 9,8 · 3,0) = √58,8 = 7,67 m/s",
                       "2)  m₁v = 0,50 · 7,67 = 3,83 kg·m/s",
                       "3)  u = 3,83 : 1,5 = 2,56 ≈ 2,6 m/s"],
             atbilde="v ≈ 7,7 m/s ;   u ≈ 2,6 m/s",
             piezime="Divas metodes: enerģija slīdēšanai, impulss "
                     "triecienam."),
        dict(nr=3, virsraksts="Kombinēts uzdevums III",
             teksts="Satelīts riņķo 400 km augstumā. Aprēķini ātrumu,\n"
                    "periodu un centrtieces paātrinājumu!\n"
                    "(R = 6,4·10⁶ m; GM = 4,0·10¹⁴ m³/s²; π ≈ 3,14)",
             dots=["h = 4,0·10⁵ m", "R = 6,4·10⁶ m"],
             jaaprekina=["v, T, a = ?"],
             formulas=["v = √(GM/r)", "T = 2πr/v", "a = v²/r"],
             aprekins=["1)  r = 6,8·10⁶ m;  "
                       "v = √(4,0·10¹⁴:6,8·10⁶) = 7,67·10³ m/s",
                       "2)  T = 2·3,14·6,8·10⁶ : 7,67·10³ = 5570 s ≈ "
                       "93 min",
                       "3)  a = (7,67·10³)² : 6,8·10⁶ = 8,65 m/s²"],
             atbilde="v ≈ 7,7 km/s ;  T ≈ 93 min ;  a ≈ 8,7 m/s²",
             piezime="Sakrīt ar KKS reālajiem parametriem."),
        dict(nr=4, virsraksts="Kombinēts uzdevums IV",
             teksts="Ķermenis (3,0 kg) noslīd no 6,0 m augstuma pa 12 m "
                    "garu\nplakni; apakšā v = 9,0 m/s. Aprēķini "
                    "enerģijas zudumus\nun vidējo berzes spēku! "
                    "(g = 9,8 m/s²)",
             dots=["m = 3,0 kg", "h = 6,0 m", "v = 9,0 m/s",
                   "s = 12 m"],
             jaaprekina=["Q = ?", "F(b) = ?"],
             formulas=["Ep = mgh", "Ek = mv²/2", "Q = Ep − Ek",
                       "F(b) = Q/s"],
             aprekins=["1)  Ep = 3,0 · 9,8 · 6,0 = 176,4 J",
                       "2)  Ek = 3,0 · 81 : 2 = 121,5 J",
                       "3)  Q = 54,9 J ;  F(b) = 54,9 : 12 = 4,6 N"],
             atbilde="Q ≈ 55 J (31 %) ;   F(b) ≈ 4,6 N",
             piezime="Enerģijas metode ļauj atrast berzes spēku, pat "
                     "nezinot plaknes leņķi."),
        dict(nr=5, virsraksts="Kombinēts uzdevums V",
             teksts="Uz planētas ar g = 8,0 m/s² ķermeni (m = 2,0 kg) "
                    "met\nvertikāli uz augšu ar 20 m/s. Aprēķini "
                    "maksimālo augstumu,\npacelšanās laiku un Ep "
                    "augšpunktā!",
             dots=["g = 8,0 m/s²", "m = 2,0 kg", "v₀ = 20 m/s"],
             jaaprekina=["h = ?", "t = ?", "Ep = ?"],
             formulas=["h = v₀²/(2g)", "t = v₀/g", "Ep = mgh"],
             aprekins=["1)  h = 400 : 16 = 25 m",
                       "2)  t = 20 : 8,0 = 2,5 s",
                       "3)  Ep = 2,0 · 8,0 · 25 = 400 J"],
             atbilde="h = 25 m ;   t = 2,5 s ;   Ep = 400 J",
             piezime="Pārbaude ar enerģiju: Ek(sākumā) = 2,0 · 400 : 2 = "
                     "400 J ✔"),
        dict(nr=6, virsraksts="Pašvērtējums un plāns",
             teksts="Novērtē savas prasmes katrā tematā skalā 1-4 un\n"
                    "izvēlies divus tematus, kurus atkārtosi vasarā!",
             dots=["5 temati"],
             jaaprekina=["pašvērtējums = ?", "plāns = ?"],
             formulas=["Godīgs pašvērtējums"],
             aprekins=["1)  Novērtē katru tematu: 1 - vājš, 4 - drošs",
                       "2)  Izvēlies divus ar zemāko vērtējumu",
                       "3)  Katram - 5 uzdevumi vasarā"],
             atbilde="Personīgs pašvērtējums un konkrēts atkārtošanas "
                     "plāns.",
             piezime="Divi temati pa 5 uzdevumiem vasarā ir reāls "
                     "plāns - un ar to pietiek."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Gads deva piecus tematus: kustība, paātrinājums, spēki, "
            "gravitācija, enerģija.",
            "Kombinētos uzdevumos vairāki temati savienojas.",
            "Eksāmenā vissvarīgākie ir 1., 3. un 5. temats.",
            "Regulāra atkārtošana ir efektīvāka par pēdējā brīža "
            "mācīšanos.",
        ],
        majasdarbs=[
            "Pabeidz pašvērtējumu un atkārtošanas plānu.",
            "Vasarā izpildi vismaz 10 uzdevumus no vājākajiem tematiem.",
            "Saglabā gada atgādni - 11. klasē tā būs vajadzīga.",
        ],
        pasvertejums=["Zinu visu tematu galvenās idejas",
                      "Protu risināt kombinētus uzdevumus",
                      "Esmu novērtējis savas prasmes",
                      "Man ir atkārtošanas plāns"],
        nakama="11. klase: mehāniskās svārstības un viļņi."),
),

]
