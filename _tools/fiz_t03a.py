# -*- coding: utf-8 -*-
"""3. temats "Mijiedarbība un spēks". A daļa: 3.1.-3.7. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "3. temats. Mijiedarbība un spēks"
KICKER = "FIZIKA I · 10. KLASE · 3. TEMATS: MIJIEDARBĪBA UN SPĒKS"
KURSS = "FIZIKA I · 10. KLASE"
MAPE = "C:/aphysics/Fizika_1/3. Mijiedarbība un spēks"

STUNDAS = [

dict(
    nr="3.1", virsraksts="Mijiedarbība un spēks",
    jautajums="Kāpēc mainās ķermeņu ātrums?",
    apaksraksts="Mijiedarbība · Spēks · Dinamometrs · [F] = N",
    merkis="Saprast spēku kā mijiedarbības mēru un iemācīties raksturot "
           "spēku ar moduli, virzienu un pielikšanas punktu.",
    protu=["definēt spēku kā mijiedarbības mēru;",
           "nosaukt spēka mērvienību un mērierīci;",
           "nosaukt spēka trīs raksturlielumus;",
           "atpazīt mijiedarbības veidus."],
    atkartojums="2. tematā mācījāmies aprakstīt paātrinājumu. Tagad "
                "noskaidrosim, KĀPĒC tas rodas - jo uz ķermeni darbojas "
                "spēks.",
    uzdevumu_apraksts="Spēka raksturlielumi un mērīšana",
    teorija=[
        ("Spēks kā mijiedarbības mērs", [
            ("formula", "SPĒKS",
             "F⃗ - vektors;  [F] = ņūtons (N);  1 N = 1 kg · m/s²",
             "Spēks ir divu ķermeņu mijiedarbības mērs. Spēks nekad nav "
             "viena ķermeņa īpašība - vienmēr ir DIVI ķermeņi.", GOLD),
            ("kartitas", [
                ("MODULIS", BLUE,
                 ["Cik liels spēks.",
                  "Mēra ar dinamometru.",
                  "Piemērs: 25 N."]),
                ("VIRZIENS", RED,
                 ["Uz kuru pusi vērsts.",
                  "Zīmē ar bultu.",
                  "Piemērs: vertikāli lejup."]),
                ("PIELIKŠANAS PUNKTS", GREEN,
                 ["Kur spēks darbojas.",
                  "Svarīgs griešanās uzdevumos.",
                  "Piemērs: virves gals."]),
            ]),
        ]),
        ("Mijiedarbības veidi", [
            ("tabula",
             ["Mijiedarbība", "Vai vajadzīgs kontakts", "Piemērs"],
             [["Gravitācijas", "Nē", "Zeme velk ķermeni"],
              ["Elektromagnētiskā", "Nē", "Magnēts un dzelzs"],
              ["Elastības", "Jā", "Atspere, virve"],
              ["Berzes", "Jā", "Riepa un ceļš"],
              ["Balsta reakcija", "Jā", "Galds un grāmata"]],
             [4.10, 4.60, 3.53]),
            ("panelis", "SPĒKA IEDARBĪBAS SEKAS",
             ["Spēks maina ķermeņa ātrumu (rada paātrinājumu) VAI deformē "
              "ķermeni. Bieži - abus vienlaikus. Ja ātrums nemainās un "
              "deformācijas nav, kopspēks ir nulle."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēka raksturošana",
             teksts="Uz 4,0 kg smagu somu, kas karājas rokā, darbojas\n"
                    "smaguma spēks. Raksturo šo spēku! (g = 9,8 m/s²)",
             dots=["m = 4,0 kg", "g = 9,8 m/s²"],
             jaaprekina=["F = ?", "virziens = ?"],
             formulas=["F = mg"],
             aprekins=["1)  F = 4,0 · 9,8",
                       "2)  F = 39,2 ≈ 39 N",
                       "3)  Virziens - vertikāli lejup;",
                       "     pielikts somas smaguma centrā"],
             atbilde="F ≈ 39 N, vertikāli lejup, pielikts smaguma centrā.",
             piezime="Visi trīs raksturlielumi jānorāda vienmēr."),
        dict(nr=2, virsraksts="Dinamometra rādījums",
             teksts="Dinamometra skalā starp 0 N un 10 N ir 20 iedaļas.\n"
                    "Rādītājs stāv uz 13. iedaļas. Kāds ir spēks un "
                    "kļūda?",
             dots=["diapazons 0-10 N", "n = 20 iedaļas", "13. iedaļa"],
             jaaprekina=["C = ?", "F = ?", "ΔF = ?"],
             formulas=["C = diapazons/n", "F = C · iedaļu skaits",
                       "ΔF = C/2"],
             aprekins=["1)  C = 10 : 20 = 0,50 N",
                       "2)  F = 0,50 · 13 = 6,5 N",
                       "3)  ΔF = 0,25 N → F = (6,50 ± 0,25) N"],
             atbilde="F = (6,50 ± 0,25) N",
             piezime="Iedaļas vērtību rēķina tāpat kā 1.11. stundā."),
        dict(nr=3, virsraksts="Mijiedarbības atpazīšana",
             teksts="Grāmata guļ uz galda. Nosauc visus spēkus, kas uz "
                    "to\ndarbojas, un norādi otro ķermeni katrā "
                    "mijiedarbībā!",
             dots=["grāmata uz galda", "miera stāvoklī"],
             jaaprekina=["spēki = ?"],
             formulas=["Katram spēkam - divi ķermeņi"],
             aprekins=["1)  Smaguma spēks: Zeme un grāmata",
                       "2)  Balsta reakcija: galds un grāmata",
                       "3)  Kopspēks = 0, jo ātrums nemainās"],
             atbilde="Divi spēki: smaguma spēks (no Zemes) un balsta "
                     "reakcija (no galda); to summa ir nulle.",
             piezime="Ja kāds spēks nav «no kāda», tas ir izdomāts."),
        dict(nr=4, virsraksts="Spēka sekas",
             teksts="Futbolists sit pa bumbu. Nosauc, kas ar bumbu "
                    "notiek\nsitiena laikā, un paskaidro abas sekas!",
             dots=["sitiens pa bumbu"],
             jaaprekina=["sekas = ?"],
             formulas=["Spēks maina ātrumu vai deformē"],
             aprekins=["1)  Bumba deformējas (saspiežas)",
                       "2)  Bumbas ātrums strauji mainās",
                       "3)  Abas sekas notiek vienlaikus"],
             atbilde="Bumba deformējas un iegūst paātrinājumu - abas "
                     "spēka iedarbības sekas.",
             piezime="Ātrā fotogrāfijā redzams, cik stipri bumba "
                     "saspiežas."),
        dict(nr=5, virsraksts="Masa no smaguma spēka",
             teksts="Uz ķermeni darbojas smaguma spēks 245 N.\n"
                    "Aprēķini tā masu! (g = 9,8 m/s²)",
             dots=["F = 245 N", "g = 9,8 m/s²"],
             jaaprekina=["m = ?"],
             formulas=["F = mg", "m = F/g"],
             aprekins=["1)  m = 245 : 9,8",
                       "2)  m = 25 kg",
                       "3)  Pārbaude: 25 · 9,8 = 245 N ✔"],
             atbilde="m = 25 kg",
             piezime="Masa ir kilogramos, spēks - ņūtonos; tos sajaukt "
                     "nedrīkst."),
        dict(nr=6, virsraksts="Mijiedarbības pāri",
             teksts="Nosauc abus ķermeņus katrā mijiedarbībā:\n"
                    "a) magnēts pievelk naglu;  b) Zeme un Mēness;\n"
                    "c) roka atbalstās pret galdu.",
             dots=["trīs situācijas"],
             jaaprekina=["mijiedarbības ķermeņi = ?"],
             formulas=["Spēks vienmēr ir starp DIVIEM ķermeņiem"],
             aprekins=["1)  a) magnēts un nagla (magnētiska)",
                       "2)  b) Zeme un Mēness (gravitācijas)",
                       "3)  c) roka un galds (saskares)"],
             atbilde="Katrā gadījumā ir divi ķermeņi un abpusēja "
                     "iedarbība.",
             piezime="Ja nevar nosaukt otro ķermeni, tad tāda spēka nav."),
        dict(nr=7, virsraksts="Divi dinamometri",
             teksts="Divi dinamometri velk gredzenu ar 12 N un 9,0 N.\n"
                    "Aprēķini kopspēku, ja tie vērsti: a) vienā "
                    "virzienā;\nb) pretēji;  c) perpendikulāri.",
             dots=["F₁ = 12 N", "F₂ = 9,0 N"],
             jaaprekina=["F(a) = ?", "F(b) = ?", "F(c) = ?"],
             formulas=["a) F₁ + F₂", "b) |F₁ − F₂|",
                       "c) √(F₁² + F₂²)"],
             aprekins=["1)  a) F = 12 + 9,0 = 21 N",
                       "2)  b) F = |12 − 9,0| = 3,0 N",
                       "3)  c) F = √(144 + 81) = √225 = 15 N"],
             atbilde="a) 21 N ;   b) 3,0 N ;   c) 15 N",
             piezime="Tie paši vektoru likumi, ko mācījāmies "
                     "1.3. stundā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Spēks ir divu ķermeņu mijiedarbības mērs.",
            "Spēku raksturo modulis, virziens un pielikšanas punkts.",
            "[F] = ņūtons; 1 N = 1 kg·m/s².",
            "Spēks maina ātrumu vai deformē ķermeni.",
        ],
        majasdarbs=[
            "Nosauc visus spēkus, kas darbojas uz lampu, kas karājas "
            "griestos.",
            "Dinamometrā C = 0,2 N, rādītājs uz 17. iedaļas. Aprēķini F "
            "un ΔF.",
            "m = 12 kg. Aprēķini smaguma spēku.",
        ],
        pasvertejums=["Protu definēt spēku",
                      "Protu nosaukt raksturlielumus",
                      "Protu atpazīt mijiedarbības",
                      "Protu lietot dinamometru"],
        nakama="Nākamā stunda: Ņūtona pirmais likums."),
),

dict(
    nr="3.2", virsraksts="Ņūtona pirmais likums",
    jautajums="Kas notiek, ja spēku nav?",
    apaksraksts="Inerce · Inerciāla sistēma · Līdzsvars",
    merkis="Saprast inerces likumu un prast to lietot, izskaidrojot "
           "ikdienas situācijas.",
    protu=["formulēt Ņūtona pirmo likumu;",
           "izskaidrot inerci ar piemēriem;",
           "atpazīt inerciālu atskaites sistēmu;",
           "pamatot drošības jostu nepieciešamību."],
    atkartojums="3.1. stundā: spēks maina ātrumu. Loģisks jautājums - "
                "kas notiek, ja spēku nav vai to summa ir nulle?",
    uzdevumu_apraksts="Inerce, līdzsvars un drošība",
    teorija=[
        ("Inerces likums", [
            ("formula", "ŅŪTONA PIRMAIS LIKUMS",
             "Ja uz ķermeni darbojošos spēku summa ir nulle, tas saglabā "
             "miera stāvokli vai vienmērīgu taisnvirziena kustību.",
             "Citiem vārdiem: bez kopspēka ātrums NEMAINĀS. Lai kustētos "
             "vienmērīgi, spēks nav vajadzīgs - tas vajadzīgs tikai "
             "ātruma MAIŅAI.", GOLD),
            ("divi",
             ("SADZĪVES PRIEKŠSTATS", RED,
              ["«Lai kustētos, jāstumj.»",
               "Tas ir maldīgs - bez berzes",
               "ķermenis kustētos bezgalīgi."]),
             ("FIZIKĀLĀ PATIESĪBA", GREEN,
              ["Stumjot mēs kompensējam berzi.",
               "Kopspēks ir nulle,",
               "tāpēc ātrums nemainās."])),
        ]),
        ("Inerce ikdienā", [
            ("tabula",
             ["Situācija", "Kas notiek", "Kāpēc"],
             [["Autobuss strauji bremzē", "Pasažieris paliecas uz priekšu",
               "Ķermenis saglabā ātrumu"],
              ["Autobuss sāk braukt", "Pasažieris paliecas atpakaļ",
               "Ķermenis saglabā mieru"],
              ["Āmura kāta sišana", "Uzgalis uzsēžas ciešāk",
               "Uzgalis saglabā kustību"],
              ["Galdauta izraušana", "Trauki paliek vietā",
               "Trauki saglabā mieru"]],
             [4.30, 4.30, 3.63]),
            ("panelis", "INERCIĀLA ATSKAITES SISTĒMA",
             ["Ņūtona likumi der tikai sistēmās, kas pašas nekustas "
              "paātrināti. Bremzējošā autobusā šķiet, ka uz pasažieri "
              "darbojas spēks uz priekšu - patiesībā vienkārši autobuss "
              "palēninās, bet pasažieris saglabā ātrumu."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kopspēks un ātrums",
             teksts="Uz kasti darbojas vilkšanas spēks 80 N un berzes "
                    "spēks\n80 N pretējā virzienā. Kaste kustas 2,0 m/s.\n"
                    "Kas notiks ar tās ātrumu?",
             dots=["F₁ = 80 N", "F₂ = 80 N (pretēji)", "v = 2,0 m/s"],
             jaaprekina=["F(kop) = ?", "v pēc laika = ?"],
             formulas=["F(kop) = F₁ − F₂", "Ja F = 0, tad v = const"],
             aprekins=["1)  F(kop) = 80 − 80 = 0",
                       "2)  Pēc 1. likuma ātrums nemainās",
                       "3)  v = 2,0 m/s arī turpmāk"],
             atbilde="Kaste turpinās kustēties vienmērīgi ar 2,0 m/s.",
             piezime="Vienmērīgai kustībai kopspēks ir nulle - ne otrādi."),
        dict(nr=2, virsraksts="Drošības josta",
             teksts="Automašīna brauc 54 km/h un strauji apstājas.\n"
                    "Paskaidro ar 1. likumu, kāpēc vajadzīga drošības "
                    "josta!",
             dots=["v = 54 km/h = 15 m/s"],
             jaaprekina=["paskaidrojums = ?"],
             formulas=["Bez spēka ķermenis saglabā ātrumu"],
             aprekins=["1)  Automašīna apstājas, jo uz to darbojas "
                       "bremzēšanas spēks",
                       "2)  Uz pasažieri šāds spēks nedarbojas",
                       "3)  Pasažieris saglabā 15 m/s un turpina kustību "
                       "uz priekšu"],
             atbilde="Josta rada spēku, kas aptur pasažieri kopā ar "
                     "automašīnu; bez tās viņš saglabātu 15 m/s.",
             piezime="15 m/s ≈ krišana no 11 m augstuma."),
        dict(nr=3, virsraksts="Trīs spēki līdzsvarā",
             teksts="Uz ķermeni darbojas F₁ = 30 N pa labi, F₂ = 40 N\n"
                    "uz augšu un F₃. Kāds ir F₃, ja ķermenis ir mierā?",
             dots=["F₁ = 30 N (pa labi)", "F₂ = 40 N (uz augšu)",
                   "miers"],
             jaaprekina=["F₃ = ?"],
             formulas=["ΣF = 0", "F₃ = −(F₁ + F₂)"],
             aprekins=["1)  F₁ un F₂ ir perpendikulāri",
                       "2)  |F₁ + F₂| = √(900 + 1600) = 50 N",
                       "3)  F₃ = 50 N pretēji šai summai"],
             atbilde="F₃ = 50 N, vērsts pretēji pirmo divu summai.",
             piezime="Miera stāvoklī visu spēku vektoru summa ir nulle."),
        dict(nr=4, virsraksts="Kosmosā",
             teksts="Kosmosa kuģis izslēdz dzinējus 20 km/s ātrumā tālu "
                    "no\nzvaigznēm. Kas notiks ar tā ātrumu? Pamato!",
             dots=["v = 20 km/s", "dzinēji izslēgti", "spēku praktiski nav"],
             jaaprekina=["v pēc laika = ?"],
             formulas=["ΣF = 0 → v = const"],
             aprekins=["1)  Vakuumā nav gaisa pretestības",
                       "2)  Tālu no masām gravitācija ir niecīga",
                       "3)  ΣF ≈ 0 → v paliek 20 km/s"],
             atbilde="Kuģis turpinās kustēties ar 20 km/s bezgalīgi.",
             piezime="Tieši tāpēc Voyager zondes joprojām lido bez "
                     "degvielas."),
        dict(nr=5, virsraksts="Inerce autobusā",
             teksts="Autobuss strauji sāk kustību. Kāpēc stāvošs "
                    "pasažieris\nkrīt atpakaļ? Paskaidro ar pirmo "
                    "likumu!",
             dots=["autobuss sāk kustību", "pasažieris stāv"],
             jaaprekina=["paskaidrojums = ?"],
             formulas=["Bez kopspēka ķermenis saglabā ātrumu"],
             aprekins=["1)  Autobusa grīda sāk kustēties uz priekšu",
                       "2)  Uz pasažiera ķermeni horizontāls spēks "
                       "gandrīz nedarbojas",
                       "3)  Ķermenis saglabā mieru, tāpēc atpaliek"],
             atbilde="Pasažieris nekrīt atpakaļ - viņš paliek uz vietas, "
                     "kamēr autobuss aizbrauc uz priekšu.",
             piezime="Bremzējot notiek pretēji: ķermenis saglabā ātrumu "
                     "un slīd uz priekšu."),
        dict(nr=6, virsraksts="Trīs spēki uz taisnes",
             teksts="Uz ķermeni darbojas 25 N pa labi un 40 N pa kreisi.\n"
                    "Cik lielam un kā vērstam jābūt trešajam spēkam,\n"
                    "lai ķermenis būtu mierā?",
             dots=["F₁ = 25 N (pa labi)", "F₂ = 40 N (pa kreisi)"],
             jaaprekina=["F₃ = ?"],
             formulas=["ΣF = 0", "F₃ = F₂ − F₁"],
             aprekins=["1)  Pagaidu kopspēks: 40 − 25 = 15 N pa kreisi",
                       "2)  Lai summa būtu nulle, vajag 15 N pa labi",
                       "3)  F₃ = 15 N pa labi"],
             atbilde="F₃ = 15 N, vērsts pa labi.",
             piezime="Līdzsvarā katras ass projekciju summa ir nulle."),
        dict(nr=7, virsraksts="Lidmašīna vienmērīgā lidojumā",
             teksts="Lidmašīna lido horizontāli ar nemainīgu 900 km/h "
                    "ātrumu.\nDzinēju vilces spēks ir 60 kN. Cik liels "
                    "ir gaisa\npretestības spēks?",
             dots=["v = const", "F(vilces) = 60 kN"],
             jaaprekina=["F(pret) = ?"],
             formulas=["v = const → ΣF = 0"],
             aprekins=["1)  Ātrums nemainās → kopspēks ir nulle",
                       "2)  Horizontāli: F(vilces) − F(pret) = 0",
                       "3)  F(pret) = 60 kN = 6,0·10⁴ N"],
             atbilde="F(pret) = 6,0·10⁴ N, vērsts pretēji kustībai.",
             piezime="Vienmērīga kustība nenozīmē, ka spēku nav - "
                     "tie ir līdzsvarā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ja ΣF = 0, ātrums nemainās (miers vai vienmērīga kustība).",
            "Spēks vajadzīgs ātruma MAIŅAI, ne uzturēšanai.",
            "Inerce ir ķermeņa īpašība saglabāt ātrumu.",
            "Ņūtona likumi der tikai inerciālās sistēmās.",
        ],
        majasdarbs=[
            "Paskaidro ar 1. likumu, kāpēc automašīnā jāstiprina bagāža.",
            "F₁ = 60 N pa labi, F₂ = 25 N pa kreisi. Kāds spēks vajadzīgs "
            "līdzsvaram?",
            "Nosauc trīs inerces izpausmes ikdienā.",
        ],
        pasvertejums=["Protu formulēt 1. likumu",
                      "Protu izskaidrot inerci",
                      "Protu atrast līdzsvara nosacījumu",
                      "Protu pamatot drošības prasības"],
        nakama="Nākamā stunda: Ņūtona otrais likums."),
),

dict(
    nr="3.3", virsraksts="Ņūtona otrais likums",
    jautajums="Cik liels paātrinājums rodas no dotā spēka?",
    apaksraksts="F = ma · a = F/m · Masa kā inerces mērs",
    merkis="Iemācīties lietot Ņūtona otro likumu un saprast masu kā "
           "inerces mēru.",
    protu=["formulēt un pierakstīt F = ma;",
           "aprēķināt jebkuru no trim lielumiem;",
           "izskaidrot masu kā inerces mēru;",
           "saistīt dinamiku ar kinemātiku."],
    atkartojums="3.2. stundā: ja ΣF = 0, ātrums nemainās. Bet kas notiek, "
                "ja ΣF ≠ 0? Atbildi dod Ņūtona otrais likums.",
    uzdevumu_apraksts="F = ma kombinācijā ar kinemātikas formulām",
    teorija=[
        ("Otrais likums", [
            ("formula", "ŅŪTONA OTRAIS LIKUMS",
             "F⃗ = m · a⃗        a⃗ = F⃗ / m        [F] = N = kg·m/s²",
             "Paātrinājums ir TIEŠI proporcionāls kopspēkam un APGRIEZTI "
             "proporcionāls masai. Paātrinājuma virziens sakrīt ar "
             "kopspēka virzienu.", GOLD),
            ("kartitas", [
                ("LIELĀKS SPĒKS", GREEN,
                 ["a aug proporcionāli.",
                  "2× spēks → 2× paātrinājums."]),
                ("LIELĀKA MASA", RED,
                 ["a samazinās.",
                  "2× masa → 2× mazāks a."]),
                ("MASA", BLUE,
                 ["Inerces mērs.",
                  "Jo lielāka, jo grūtāk mainīt ātrumu."]),
            ]),
        ]),
        ("Dinamika + kinemātika", [
            ("panelis", "DIVU SOĻU RISINĀJUMS",
             ["Lielākā daļa uzdevumu risināma divos soļos.",
              "1. solis - no spēkiem aprēķina paātrinājumu:",
              "a = ΣF/m",
              "2. solis - ar kinemātikas formulām atrod ātrumu, ceļu "
              "vai laiku. Vai otrādi."], NAVY),
            ("tabula",
             ["Ja dots", "1. solis", "2. solis"],
             [["F, m, t", "a = F/m", "v = at; s = at²/2"],
              ["m, v₀, v, t", "a = (v−v₀)/t", "F = ma"],
              ["m, v₀, s (apstājas)", "a = −v₀²/(2s)", "F = ma"],
              ["F, m, s", "a = F/m", "v = √(2as)"]],
             [4.10, 3.90, 4.23]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Paātrinājums no spēka",
             teksts="Uz 1400 kg smagu automašīnu darbojas kopspēks "
                    "4200 N.\nAprēķini paātrinājumu un ātrumu pēc 8,0 s "
                    "no miera!",
             dots=["m = 1400 kg", "F = 4200 N", "t = 8,0 s", "v₀ = 0"],
             jaaprekina=["a = ?", "v = ?"],
             formulas=["a = F/m", "v = at"],
             aprekins=["1)  a = 4200 : 1400 = 3,0 m/s²",
                       "2)  v = 3,0 · 8,0",
                       "3)  v = 24 m/s = 86 km/h"],
             atbilde="a = 3,0 m/s² ;   v = 24 m/s",
             piezime="Reāla vieglās automašīnas dinamika."),
        dict(nr=2, virsraksts="Spēks no bremzēšanas",
             teksts="1200 kg automašīna no 20 m/s apstājas 50 m ceļā.\n"
                    "Aprēķini bremzēšanas spēku!",
             dots=["m = 1200 kg", "v₀ = 20 m/s", "v = 0", "s = 50 m"],
             jaaprekina=["a = ?", "F = ?"],
             formulas=["v² − v₀² = 2as", "F = ma"],
             aprekins=["1)  a = (0 − 400) : (2·50) = −4,0 m/s²",
                       "2)  F = 1200 · (−4,0)",
                       "3)  F = −4800 N"],
             atbilde="F = 4,8·10³ N, vērsts pretēji kustībai.",
             piezime="Mīnusa zīme norāda virzienu; modulī spēks ir "
                     "4800 N."),
        dict(nr=3, virsraksts="Masas ietekme",
             teksts="Uz diviem ķermeņiem ar masām 2,0 kg un 8,0 kg "
                    "darbojas\nvienāds spēks 12 N. Salīdzini "
                    "paātrinājumus!",
             dots=["F = 12 N", "m₁ = 2,0 kg", "m₂ = 8,0 kg"],
             jaaprekina=["a₁ = ?", "a₂ = ?"],
             formulas=["a = F/m"],
             aprekins=["1)  a₁ = 12 : 2,0 = 6,0 m/s²",
                       "2)  a₂ = 12 : 8,0 = 1,5 m/s²",
                       "3)  a₁ : a₂ = 4 = m₂ : m₁"],
             atbilde="a₁ = 6,0 m/s² ;  a₂ = 1,5 m/s²; attiecība 4 : 1.",
             piezime="Paātrinājums ir apgriezti proporcionāls masai."),
        dict(nr=4, virsraksts="Divi spēki",
             teksts="Uz 5,0 kg kasti darbojas vilkšanas spēks 30 N un "
                    "berze\n12 N pretējā virzienā. Aprēķini paātrinājumu\n"
                    "un ceļu 4,0 s laikā no miera!",
             dots=["m = 5,0 kg", "F₁ = 30 N", "F₂ = 12 N", "t = 4,0 s"],
             jaaprekina=["a = ?", "s = ?"],
             formulas=["ΣF = F₁ − F₂", "a = ΣF/m", "s = at²/2"],
             aprekins=["1)  ΣF = 30 − 12 = 18 N",
                       "2)  a = 18 : 5,0 = 3,6 m/s²",
                       "3)  s = 3,6 · 16 : 2 = 28,8 ≈ 29 m"],
             atbilde="a = 3,6 m/s² ;   s ≈ 29 m",
             piezime="F = ma vienmēr lieto ar KOPSPĒKU, nevis atsevišķu "
                     "spēku."),
        dict(nr=5, virsraksts="Masa no spēka",
             teksts="Uz ķermeni darbojas kopspēks 250 N, un tas iegūst\n"
                    "paātrinājumu 0,50 m/s². Aprēķini masu!",
             dots=["F = 250 N", "a = 0,50 m/s²"],
             jaaprekina=["m = ?"],
             formulas=["F = ma", "m = F/a"],
             aprekins=["1)  m = 250 : 0,50",
                       "2)  m = 500 kg",
                       "3)  Pārbaude: 500 · 0,50 = 250 N ✔"],
             atbilde="m = 500 kg",
             piezime="Otro likumu var izteikt pret jebkuru no trim "
                     "lielumiem."),
        dict(nr=6, virsraksts="Lidmašīnas pacelšanās",
             teksts="Lidmašīna (m = 60 t) no miera sasniedz 75 m/s "
                    "1800 m\nskrejceļā. Aprēķini paātrinājumu un dzinēju "
                    "spēku!",
             dots=["m = 6,0·10⁴ kg", "v₀ = 0", "v = 75 m/s",
                   "s = 1800 m"],
             jaaprekina=["a = ?", "F = ?"],
             formulas=["v² = 2as", "F = ma"],
             aprekins=["1)  v² = 5625 m²/s²",
                       "2)  a = 5625 : 3600 = 1,56 m/s²",
                       "3)  F = 6,0·10⁴ · 1,56 ≈ 9,4·10⁴ N"],
             atbilde="a ≈ 1,6 m/s² ;   F ≈ 9,4·10⁴ N",
             piezime="Kinemātika un dinamika viena uzdevuma iekšienē - "
                     "tipisks eksāmena uzdevums."),
        dict(nr=7, virsraksts="Perpendikulāri spēki",
             teksts="Uz 10 kg ķermeni darbojas divi perpendikulāri "
                    "spēki\n30 N un 40 N. Aprēķini paātrinājumu!",
             dots=["m = 10 kg", "F₁ = 30 N", "F₂ = 40 N", "α = 90°"],
             jaaprekina=["F = ?", "a = ?"],
             formulas=["F = √(F₁² + F₂²)", "a = F/m"],
             aprekins=["1)  F² = 900 + 1600 = 2500 N²",
                       "2)  F = 50 N",
                       "3)  a = 50 : 10 = 5,0 m/s²"],
             atbilde="F = 50 N ;   a = 5,0 m/s² kopspēka virzienā",
             piezime="Paātrinājums vienmēr ir vērsts tāpat kā KOPSPĒKS."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "F = ma; a = F/m - paātrinājums proporcionāls kopspēkam.",
            "Masa ir inerces mērs.",
            "F = ma lieto ar spēku SUMMU.",
            "Uzdevumus risina divos soļos: spēki → a → kinemātika.",
        ],
        majasdarbs=[
            "m = 800 kg, F = 2400 N. Aprēķini a un v pēc 10 s.",
            "m = 0,50 kg, v₀ = 0, v = 12 m/s, t = 0,20 s. Aprēķini F.",
            "F₁ = 50 N, F₂ = 20 N pretēji, m = 6,0 kg. Aprēķini a.",
        ],
        pasvertejums=["Protu lietot F = ma",
                      "Protu rēķināt jebkuru lielumu",
                      "Protu apvienot ar kinemātiku",
                      "Protu strādāt ar kopspēku"],
        nakama="Nākamā stunda: Ņūtona trešais likums."),
),

dict(
    nr="3.4", virsraksts="Ņūtona trešais likums",
    jautajums="Vai zirgs velk ratus vai rati zirgu?",
    apaksraksts="F₁₂ = −F₂₁ · Divi ķermeņi · Reaktīvā kustība",
    merkis="Saprast, ka spēki vienmēr rodas pāros, un prast atšķirt "
           "trešā likuma pāri no līdzsvarā esošiem spēkiem.",
    protu=["formulēt trešo likumu;",
           "atrast spēka pāri konkrētā situācijā;",
           "atšķirt trešā likuma pāri no līdzsvara spēkiem;",
           "izskaidrot reaktīvo kustību."],
    atkartojums="3.1. stundā: spēks ir DIVU ķermeņu mijiedarbība. Trešais "
                "likums pasaka, kā šie divi spēki ir saistīti.",
    uzdevumu_apraksts="Spēku pāri un reaktīvā kustība",
    teorija=[
        ("Trešais likums", [
            ("formula", "ŅŪTONA TREŠAIS LIKUMS",
             "F⃗₁₂ = − F⃗₂₁",
             "Divi ķermeņi mijiedarbojas ar vienāda moduļa, pretēji "
             "vērstiem spēkiem, kas darbojas pa vienu taisni. Šie spēki "
             "vienmēr ir vienāda VEIDA un pielikti DAŽĀDIEM ķermeņiem.",
             GOLD),
            ("divi",
             ("TREŠĀ LIKUMA PĀRIS", GREEN,
              ["Pielikti DIVIEM dažādiem ķermeņiem.",
               "Nekad neizlīdzinās.",
               "Piemērs: Zeme velk grāmatu,",
               "bet grāmata velk Zemi."]),
             ("LĪDZSVARA SPĒKI", BLUE,
              ["Pielikti VIENAM ķermenim.",
               "To summa var būt nulle.",
               "Piemērs: smaguma spēks un",
               "balsta reakcija uz grāmatu."])),
        ]),
        ("Kāpēc kustība vispār notiek", [
            ("panelis", "ATBILDE UZ ZIRGA JAUTĀJUMU",
             ["Zirgs velk ratus tikpat stipri, cik rati velk zirgu - "
              "bet šie spēki pielikti DAŽĀDIEM ķermeņiem, tāpēc "
              "neizlīdzinās. Sistēma kustas tāpēc, ka zirgs atgrūžas no "
              "ZEMES: berzes spēks no zemes uz zirgu ir lielāks nekā "
              "ratu pretestība."], NAVY),
            ("tabula",
             ["Situācija", "1. spēks", "2. spēks (pāris)"],
             [["Cilvēks iet", "Kāja spiež zemi atpakaļ",
               "Zeme spiež kāju uz priekšu"],
              ["Raķete", "Dzinējs izgrūž gāzes lejup",
               "Gāzes stumj raķeti augšup"],
              ["Peldēšana", "Roka stumj ūdeni atpakaļ",
               "Ūdens stumj peldētāju uz priekšu"],
              ["Šaušana", "Ierocis stumj lodi",
               "Lode stumj ieroci (atsitiens)"]],
             [2.90, 4.60, 4.73]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēka pāra atrašana",
             teksts="Grāmata (m = 0,80 kg) guļ uz galda.\n"
                    "Nosauc trešā likuma pāri smaguma spēkam un aprēķini "
                    "tā moduli! (g = 9,8 m/s²)",
             dots=["m = 0,80 kg", "g = 9,8 m/s²"],
             jaaprekina=["F = ?", "pāris = ?"],
             formulas=["F = mg", "F₁₂ = −F₂₁"],
             aprekins=["1)  Zeme velk grāmatu: F = 0,80 · 9,8 = 7,8 N",
                       "2)  Pāris: grāmata velk Zemi ar 7,8 N uz augšu",
                       "3)  Balsta reakcija NAV šis pāris - tā pielikta "
                       "tam pašam ķermenim"],
             atbilde="Pāris ir grāmatas pievilkšanas spēks uz Zemi, "
                     "7,8 N vertikāli uz augšu.",
             piezime="Biežākā kļūda - saukt balsta reakciju par trešā "
                     "likuma pāri."),
        dict(nr=2, virsraksts="Divu ķermeņu sadursme",
             teksts="Kravas auto (8000 kg) saduras ar vieglo (1200 kg).\n"
                    "Salīdzini spēkus un paātrinājumus!",
             dots=["m₁ = 8000 kg", "m₂ = 1200 kg"],
             jaaprekina=["F₁ pret F₂ = ?", "a₁ pret a₂ = ?"],
             formulas=["F₁₂ = −F₂₁", "a = F/m"],
             aprekins=["1)  Spēku moduļi VIENĀDI: F₁ = F₂",
                       "2)  a₁ = F/8000 ;  a₂ = F/1200",
                       "3)  a₂ / a₁ = 8000 : 1200 ≈ 6,7"],
             atbilde="Spēki vienādi, bet vieglās automašīnas "
                     "paātrinājums ir 6,7 reizes lielāks.",
             piezime="Tāpēc sadursmē vairāk cieš vieglākā automašīna, "
                     "lai gan spēki ir vienādi."),
        dict(nr=3, virsraksts="Reaktīvā kustība",
             teksts="Cilvēks (70 kg) uz slidām atgrūž 5,0 kg bumbu ar\n"
                    "paātrinājumu 12 m/s². Kāds ir cilvēka paātrinājums?",
             dots=["m₁ = 70 kg", "m₂ = 5,0 kg", "a₂ = 12 m/s²"],
             jaaprekina=["F = ?", "a₁ = ?"],
             formulas=["F = m₂a₂", "a₁ = F/m₁"],
             aprekins=["1)  F = 5,0 · 12 = 60 N",
                       "2)  Uz cilvēku darbojas tāds pats 60 N pretēji",
                       "3)  a₁ = 60 : 70 ≈ 0,86 m/s²"],
             atbilde="a₁ ≈ 0,86 m/s², vērsts pretēji bumbas kustībai.",
             piezime="Cilvēks sāk slīdēt atpakaļ - reaktīvā kustība."),
        dict(nr=4, virsraksts="Pāris vai līdzsvars",
             teksts="Lampa karājas griestos. Nosauc: a) spēkus, kas "
                    "darbojas\nuz lampu; b) trešā likuma pāri virves "
                    "vilkšanas spēkam!",
             dots=["lampa karājas mierā"],
             jaaprekina=["a) spēki = ?", "b) pāris = ?"],
             formulas=["Līdzsvars - viens ķermenis; pāris - divi"],
             aprekins=["1)  Uz lampu: smaguma spēks lejup un virves "
                       "vilkšana augšup (līdzsvars)",
                       "2)  Virve velk lampu augšup",
                       "3)  Pāris: lampa velk virvi lejup"],
             atbilde="a) smaguma spēks un virves spēks; b) lampas "
                     "vilkšanas spēks uz virvi, vērsts lejup.",
             piezime="Pārbaudes jautājums: vai abi spēki pielikti "
                     "vienam ķermenim? Ja jā - tas nav trešā likuma "
                     "pāris."),
        dict(nr=5, virsraksts="Cilvēks un laiva",
             teksts="Cilvēks (60 kg) atgrūžas no laivas (120 kg) ar "
                    "spēku\n180 N. Aprēķini abu paātrinājumus!",
             dots=["m₁ = 60 kg", "m₂ = 120 kg", "F = 180 N"],
             jaaprekina=["a₁ = ?", "a₂ = ?"],
             formulas=["F₁₂ = −F₂₁", "a = F/m"],
             aprekins=["1)  Uz abiem darbojas 180 N pretējos virzienos",
                       "2)  a₁ = 180 : 60 = 3,0 m/s²",
                       "3)  a₂ = 180 : 120 = 1,5 m/s²"],
             atbilde="a₁ = 3,0 m/s² ;   a₂ = 1,5 m/s² pretējā virzienā",
             piezime="Spēki vienādi, paātrinājumi - nē; tos nosaka "
                     "masas."),
        dict(nr=6, virsraksts="Zirgs un rati",
             teksts="«Zirgs velk ratus ar tādu pašu spēku, ar kādu rati\n"
                    "velk zirgu, tātad tie nevar sākt kustēties.»\n"
                    "Atrodi kļūdu spriedumā!",
             dots=["F(zirgs→rati) = F(rati→zirgs)"],
             jaaprekina=["kļūda = ?"],
             formulas=["F = ma katram ķermenim atsevišķi"],
             aprekins=["1)  Abi spēki pielikti DAŽĀDIEM ķermeņiem",
                       "2)  Ratu paātrinājumu nosaka spēki, kas "
                       "pielikti ratiem",
                       "3)  Zirga vilkme pārsniedz ratu berzi → rati "
                       "kustas"],
             atbilde="Trešā likuma spēkus nedrīkst saskaitīt - tie "
                     "pielikti dažādiem ķermeņiem.",
             piezime="Vienmēr izvēlies VIENU ķermeni un saskaiti tikai "
                     "tam pieliktos spēkus."),
        dict(nr=7, virsraksts="Ābols un Zeme",
             teksts="Ābols (m = 0,20 kg) krīt uz Zemi (M = 6,0·10²⁴ kg).\n"
                    "Aprēķini spēku uz Zemi un Zemes paātrinājumu! "
                    "(g = 9,8 m/s²)",
             dots=["m = 0,20 kg", "M = 6,0·10²⁴ kg", "g = 9,8 m/s²"],
             jaaprekina=["F = ?", "a(Zemes) = ?"],
             formulas=["F = mg", "a = F/M"],
             aprekins=["1)  F = 0,20 · 9,8 = 1,96 N",
                       "2)  Tāds pats spēks darbojas uz Zemi",
                       "3)  a = 1,96 : 6,0·10²⁴ ≈ 3,3·10⁻²⁵ m/s²"],
             atbilde="F = 1,96 N ;   a(Zemes) ≈ 3,3·10⁻²⁵ m/s²",
             piezime="Zeme arī tuvojas ābolam, tikai nesalīdzināmi "
                     "lēnāk - tāpēc to nepamana."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "F₁₂ = −F₂₁: spēki rodas pāros, vienādi pēc moduļa.",
            "Trešā likuma pāris vienmēr pielikts DIVIEM dažādiem "
            "ķermeņiem.",
            "Līdzsvara spēki pielikti VIENAM ķermenim.",
            "Reaktīvā kustība balstās uz trešo likumu.",
        ],
        majasdarbs=[
            "Nosauc trešā likuma pāri spēkam, ar kuru tu spied uz "
            "grīdu.",
            "m₁ = 60 kg, m₂ = 3,0 kg, a₂ = 8,0 m/s². Aprēķini a₁.",
            "Paskaidro, kāpēc raķete lido arī vakuumā.",
        ],
        pasvertejums=["Protu formulēt 3. likumu",
                      "Protu atrast spēka pāri",
                      "Protu atšķirt pāri no līdzsvara",
                      "Protu izskaidrot reaktīvo kustību"],
        nakama="Nākamā stunda: spēku shēmas un kopspēks."),
),

dict(
    nr="3.5", virsraksts="Spēku shēmas un kopspēks",
    jautajums="Kā uzzīmēt visus spēkus?",
    apaksraksts="Spēku shēma · Projekcijas · ΣF = ma",
    merkis="Iemācīties zīmēt pareizu spēku shēmu un no tās uzrakstīt "
           "Ņūtona otro likumu projekcijās.",
    protu=["uzzīmēt pilnu spēku shēmu;",
           "izvēlēties koordinātu asis;",
           "uzrakstīt ΣF = ma projekcijās;",
           "pārbaudīt, vai nav lieku vai trūkstošu spēku."],
    atkartojums="1.4. stundā mācījāmies projekcijas, 3.3. stundā - "
                "F = ma. Tagad tos savienojam: spēku shēma ir katra "
                "dinamikas uzdevuma pirmais solis.",
    uzdevumu_apraksts="Spēku shēmas un vienādojumi projekcijās",
    teorija=[
        ("Kā zīmē spēku shēmu", [
            ("panelis", "PIECI SOĻI",
             ["1) Uzzīmē ķermeni kā punktu vai vienkāršu figūru.  "
              "2) Uzzīmē KATRU spēku ar bultu no ķermeņa.  3) Katrai "
              "bultai pieraksti apzīmējumu (F(sm), N, F(b), T).  "
              "4) Izvēlies asis - vienu gar kustību.  5) Uzraksti "
              "ΣF = ma katrai asij atsevišķi."], NAVY),
            ("kartitas", [
                ("VIENMĒR PĀRBAUDI", BLUE,
                 ["Katram spēkam ir «no kā»?",
                  "Vai neesmu aizmirsis berzi?",
                  "Vai nav divkārši uzzīmēts?"]),
                ("BIEŽĀK AIZMIRST", RED,
                 ["Balsta reakciju N.",
                  "Berzes spēku.",
                  "Virves spraigumu T."]),
                ("BIEŽĀK LIEKI", GOLD,
                 ["«Kustības spēks» - nav tāda.",
                  "«Centrbēdzes spēks» inerciālā sistēmā.",
                  "Divreiz uzzīmēts svars."]),
            ]),
        ]),
        ("Vienādojumi projekcijās", [
            ("formula", "OTRAIS LIKUMS PROJEKCIJĀS",
             "x ass:  ΣFₓ = m · aₓ        y ass:  ΣF_y = m · a_y",
             "Ja pa kādu asi kustības nav (piemēram, vertikāli uz "
             "horizontālas virsmas), tad tai asij ΣF = 0.", GOLD),
            ("tabula",
             ["Situācija", "x ass vienādojums", "y ass vienādojums"],
             [["Kaste velkas horizontāli", "F − F(b) = ma", "N − mg = 0"],
              ["Lifts kustas uz augšu", "—", "T − mg = ma"],
              ["Ķermenis brīvi krīt", "—", "mg = ma → a = g"],
              ["Ķermenis mierā", "ΣFₓ = 0", "ΣF_y = 0"]],
             [3.90, 4.30, 4.03]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Shēma un vienādojums",
             teksts="Kasti (m = 20 kg) velk horizontāli ar spēku 80 N;\n"
                    "berzes spēks 30 N. Uzzīmē shēmu un aprēķini "
                    "paātrinājumu!",
             dots=["m = 20 kg", "F = 80 N", "F(b) = 30 N"],
             jaaprekina=["a = ?", "N = ?"],
             formulas=["x: F − F(b) = ma", "y: N − mg = 0"],
             aprekins=["1)  Spēki: F, F(b), mg, N",
                       "2)  x: 80 − 30 = 20a → a = 2,5 m/s²",
                       "3)  y: N = mg = 20 · 9,8 = 196 N"],
             atbilde="a = 2,5 m/s² ;   N = 196 N ≈ 2,0·10² N",
             piezime="Vertikāli kustības nav, tāpēc ΣF_y = 0."),
        dict(nr=2, virsraksts="Lifts uz augšu",
             teksts="Lifta kabīne (m = 500 kg) sāk kustību uz augšu ar\n"
                    "paātrinājumu 1,2 m/s². Aprēķini troses spraigumu!\n"
                    "(g = 9,8 m/s²)",
             dots=["m = 500 kg", "a = 1,2 m/s² (uz augšu)",
                   "g = 9,8 m/s²"],
             jaaprekina=["T = ?"],
             formulas=["y: T − mg = ma", "T = m(g + a)"],
             aprekins=["1)  g + a = 9,8 + 1,2 = 11,0 m/s²",
                       "2)  T = 500 · 11,0",
                       "3)  T = 5500 N"],
             atbilde="T = 5,5·10³ N",
             piezime="Mierā trose turētu tikai 4900 N - paātrinājums "
                     "palielina slodzi."),
        dict(nr=3, virsraksts="Lifts uz leju",
             teksts="Tā pati kabīne bremzē, kustoties lejup, ar\n"
                    "paātrinājumu 1,2 m/s² uz augšu. Kāds ir spraigums?\n"
                    "Un ja lifts brīvi krīt?",
             dots=["m = 500 kg", "a = 1,2 m/s² (uz augšu)"],
             jaaprekina=["T = ?", "T (brīvā krišanā) = ?"],
             formulas=["T = m(g + a)", "brīvā krišanā a = −g"],
             aprekins=["1)  Paātrinājums uz augšu → T = 500 · 11,0 = "
                       "5500 N",
                       "2)  Brīvā krišanā a = −g",
                       "3)  T = 500 · (9,8 − 9,8) = 0"],
             atbilde="T = 5,5·10³ N; brīvā krišanā T = 0 (bezsvara "
                     "stāvoklis).",
             piezime="Bezsvara stāvoklis nozīmē, ka balsts nespiež - "
                     "nevis ka gravitācijas nav."),
        dict(nr=4, virsraksts="Kļūdaina shēma",
             teksts="Skolēns kastei, ko velk horizontāli, uzzīmēja "
                    "spēkus:\nmg, N, F(vilkšanas), F(berzes) un "
                    "«kustības spēku».\nAtrodi kļūdu!",
             dots=["5 uzzīmēti spēki"],
             jaaprekina=["kļūda = ?"],
             formulas=["Katram spēkam - otrs ķermenis"],
             aprekins=["1)  mg - no Zemes ✔",
                       "2)  N, F(vilk), F(berz) - no galda, rokas, "
                       "galda ✔",
                       "3)  «Kustības spēks» - nav otrā ķermeņa → "
                       "tāda spēka nav"],
             atbilde="«Kustības spēks» ir lieks - kustība nav spēks.",
             piezime="Šī ir viena no biežākajām kļūdām spēku shēmās."),
        dict(nr=5, virsraksts="Lifts vienmērīgi",
             teksts="Lifta kabīne (m = 500 kg) kustas uz augšu ar "
                    "nemainīgu\nātrumu. Aprēķini troses spraigumu! "
                    "(g = 9,8 m/s²)",
             dots=["m = 500 kg", "v = const → a = 0", "g = 9,8 m/s²"],
             jaaprekina=["T = ?"],
             formulas=["y: T − mg = ma", "a = 0 → T = mg"],
             aprekins=["1)  Ātrums nemainās → a = 0",
                       "2)  T = mg = 500 · 9,8",
                       "3)  T = 4900 N"],
             atbilde="T = 4,9·10³ N",
             piezime="Vienmērīgā kustībā spraigums ir tāds pats kā "
                     "mierā - virziens nozīmes nav."),
        dict(nr=6, virsraksts="Kopspēks un paātrinājums",
             teksts="Uz 20 kg ķermeni darbojas F₁ = 60 N gar x asi un\n"
                    "F₂ = 80 N gar y asi. Aprēķini kopspēku un "
                    "paātrinājumu!",
             dots=["m = 20 kg", "F₁ = 60 N", "F₂ = 80 N"],
             jaaprekina=["R = ?", "a = ?"],
             formulas=["R = √(F₁² + F₂²)", "a = R/m"],
             aprekins=["1)  R² = 3600 + 6400 = 10 000 N²",
                       "2)  R = 100 N",
                       "3)  a = 100 : 20 = 5,0 m/s²"],
             atbilde="R = 100 N ;   a = 5,0 m/s² kopspēka virzienā",
             piezime="Vispirms kopspēks projekcijās, tikai pēc tam "
                     "F = ma."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Spēku shēma ir katra dinamikas uzdevuma pirmais solis.",
            "Katram spēkam jāzina, no kura ķermeņa tas nāk.",
            "ΣF = ma raksta katrai asij atsevišķi.",
            "Ja pa asi kustības nav, tai asij ΣF = 0.",
        ],
        majasdarbs=[
            "m = 15 kg, F = 60 N, F(b) = 24 N. Uzzīmē shēmu un aprēķini "
            "a un N.",
            "Lifts m = 800 kg, a = 2,0 m/s² uz augšu. Aprēķini T.",
            "Nosauc trīs spēkus, kurus visbiežāk aizmirst shēmā.",
        ],
        pasvertejums=["Protu uzzīmēt spēku shēmu",
                      "Protu izvēlēties asis",
                      "Protu uzrakstīt vienādojumus",
                      "Protu pamanīt lieku spēku"],
        nakama="Nākamā stunda: smaguma spēks un svars."),
),

dict(
    nr="3.6", virsraksts="Smaguma spēks un svars",
    jautajums="Ar ko svars atšķiras no smaguma spēka?",
    apaksraksts="F(sm) = mg · Svars P · Pārslodze · Bezsvara stāvoklis",
    merkis="Iemācīties atšķirt smaguma spēku no svara un aprēķināt svaru "
           "paātrinātā kustībā.",
    protu=["definēt smaguma spēku un svaru;",
           "nosaukt, uz kuru ķermeni katrs no tiem darbojas;",
           "aprēķināt svaru liftā;",
           "izskaidrot pārslodzi un bezsvara stāvokli."],
    atkartojums="3.5. stundā rēķinājām troses spraigumu liftā. Tas ir "
                "cieši saistīts ar svaru - lielumu, ko sadzīvē bieži "
                "sajauc ar masu.",
    uzdevumu_apraksts="Svars liftā, pārslodze un bezsvara stāvoklis",
    teorija=[
        ("Divi dažādi lielumi", [
            ("divi",
             ("SMAGUMA SPĒKS  F(sm)", BLUE,
              ["Zeme velk ķermeni.",
               "Pielikts ĶERMENIM.",
               "F(sm) = mg - vienmēr.",
               "Nav atkarīgs no kustības."]),
             ("SVARS  P", GOLD,
              ["Ķermenis spiež uz balstu vai velk pakari.",
               "Pielikts BALSTAM vai PAKAREI.",
               "P = m(g ± a).",
               "Atkarīgs no kustības."])),
            ("formula", "SVARS PAĀTRINĀTĀ KUSTĪBĀ",
             "P = m(g + a)  - paātrinājums uz augšu (pārslodze)        "
             "P = m(g − a)  - paātrinājums uz leju",
             "Ja a = g (brīva krišana), P = 0 - bezsvara stāvoklis. "
             "Smaguma spēks pie tam nekur nepazūd.", GOLD),
        ]),
        ("Kur to jūt", [
            ("tabula",
             ["Situācija", "Paātrinājums", "Svars"],
             [["Mierā vai vienmērīgi", "a = 0", "P = mg"],
              ["Lifts sāk kāpt", "a uz augšu", "P > mg (smagāk)"],
              ["Lifts sāk laisties", "a uz leju", "P < mg (vieglāk)"],
              ["Brīvā krišana", "a = g", "P = 0"],
              ["Raķetes starts", "a ≈ 3g", "P ≈ 4mg"]],
             [4.30, 3.60, 4.33]),
            ("panelis", "MASA UN SVARS SADZĪVĒ",
             ["Veikalā «sver 2 kg» patiesībā nozīmē MASU 2 kg. Masa ir "
              "kilogramos un nemainās; svars ir ņūtonos un mainās. Uz "
              "Mēness masa būtu tā pati, bet svars - 6 reizes mazāks."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Svars liftā",
             teksts="Cilvēks (m = 70 kg) atrodas liftā, kas kustas uz "
                    "augšu\nar paātrinājumu 2,0 m/s². Aprēķini viņa "
                    "svaru! (g = 9,8 m/s²)",
             dots=["m = 70 kg", "a = 2,0 m/s² (uz augšu)",
                   "g = 9,8 m/s²"],
             jaaprekina=["P = ?"],
             formulas=["P = m(g + a)"],
             aprekins=["1)  g + a = 9,8 + 2,0 = 11,8 m/s²",
                       "2)  P = 70 · 11,8",
                       "3)  P = 826 ≈ 8,3·10² N"],
             atbilde="P ≈ 8,3·10² N  (mierā būtu 686 N)",
             piezime="Svars pieaudzis par 20 % - to sajūt kā «piespiešanu "
                     "pie grīdas»."),
        dict(nr=2, virsraksts="Pārslodzes koeficients",
             teksts="Lidotājs izpilda manevru ar paātrinājumu 29,4 m/s²\n"
                    "uz augšu. Cik reižu viņa svars pārsniedz parasto? "
                    "(g = 9,8 m/s²)",
             dots=["a = 29,4 m/s²", "g = 9,8 m/s²"],
             jaaprekina=["P/mg = ?"],
             formulas=["P = m(g + a)", "k = P/(mg) = (g+a)/g"],
             aprekins=["1)  g + a = 9,8 + 29,4 = 39,2 m/s²",
                       "2)  k = 39,2 : 9,8",
                       "3)  k = 4,0"],
             atbilde="Svars 4 reizes lielāks - pārslodze 4 g.",
             piezime="Pie 5-6 g bez īpaša tērpa cilvēks zaudē samaņu."),
        dict(nr=3, virsraksts="Bezsvara stāvoklis",
             teksts="Lifts, kura trose pārtrūkusi, brīvi krīt.\n"
                    "Aprēķini 60 kg cilvēka svaru un smaguma spēku!\n"
                    "(g = 9,8 m/s²)",
             dots=["m = 60 kg", "a = g = 9,8 m/s² (lejup)"],
             jaaprekina=["P = ?", "F(sm) = ?"],
             formulas=["P = m(g − a)", "F(sm) = mg"],
             aprekins=["1)  P = 60 · (9,8 − 9,8) = 0",
                       "2)  F(sm) = 60 · 9,8 = 588 N",
                       "3)  Smaguma spēks paliek, svars kļūst nulle"],
             atbilde="P = 0 N ;   F(sm) = 588 N ≈ 5,9·10² N",
             piezime="Kosmosa stacijā ir tieši tāpat - tā nepārtraukti "
                     "«krīt» ap Zemi."),
        dict(nr=4, virsraksts="Svars uz Mēness",
             teksts="Uz Mēness g = 1,6 m/s². Aprēķini 80 kg astronauta\n"
                    "masu un svaru uz Zemes un uz Mēness!",
             dots=["m = 80 kg", "g(Z) = 9,8 m/s²", "g(M) = 1,6 m/s²"],
             jaaprekina=["P(Z) = ?", "P(M) = ?"],
             formulas=["P = mg"],
             aprekins=["1)  Masa abās vietās 80 kg",
                       "2)  P(Z) = 80 · 9,8 = 784 N",
                       "3)  P(M) = 80 · 1,6 = 128 N"],
             atbilde="m = 80 kg abur; P(Z) ≈ 7,8·10² N; P(M) = "
                     "1,3·10² N.",
             piezime="Svars 6 reizes mazāks - tāpēc astronauti uz Mēness "
                     "lēkā."),
        dict(nr=5, virsraksts="Svars, liftam bremzējot",
             teksts="Lifts kustas uz augšu un bremzē ar paātrinājumu\n"
                    "2,0 m/s² (vērsts lejup). Aprēķini 70 kg cilvēka "
                    "svaru!\n(g = 9,8 m/s²)",
             dots=["m = 70 kg", "a = 2,0 m/s² (lejup)",
                   "g = 9,8 m/s²"],
             jaaprekina=["P = ?"],
             formulas=["P = m(g − a)"],
             aprekins=["1)  g − a = 9,8 − 2,0 = 7,8 m/s²",
                       "2)  P = 70 · 7,8",
                       "3)  P = 546 ≈ 5,5·10² N"],
             atbilde="P ≈ 5,5·10² N  (mierā būtu 686 N)",
             piezime="Bremzējot augšupceļā rodas «viegluma» sajūta - "
                     "svars samazinās par 20 %."),
        dict(nr=6, virsraksts="Masa no svara",
             teksts="Cilvēka svars uz Zemes ir 588 N.\n"
                    "Aprēķini masu un svaru uz Marsa! "
                    "(g(Z) = 9,8 m/s²; g(M) = 3,7 m/s²)",
             dots=["P(Z) = 588 N", "g(Z) = 9,8 m/s²",
                   "g(M) = 3,7 m/s²"],
             jaaprekina=["m = ?", "P(M) = ?"],
             formulas=["P = mg", "m = P/g"],
             aprekins=["1)  m = 588 : 9,8 = 60 kg",
                       "2)  P(M) = 60 · 3,7",
                       "3)  P(M) = 222 N"],
             atbilde="m = 60 kg ;   P(M) ≈ 2,2·10² N",
             piezime="Masa nemainās nekur - mainās tikai svars."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Smaguma spēks pielikts ķermenim; svars - balstam vai "
            "pakarei.",
            "F(sm) = mg vienmēr; P = m(g ± a).",
            "Brīvā krišanā P = 0, bet smaguma spēks paliek.",
            "Masa nemainās, svars ir atkarīgs no g un paātrinājuma.",
        ],
        majasdarbs=[
            "m = 55 kg, lifts kustas lejup ar a = 1,5 m/s². Aprēķini P.",
            "Pārslodze 3 g. Aprēķini paātrinājumu.",
            "Uz Marsa g = 3,7 m/s². Aprēķini 65 kg cilvēka svaru.",
        ],
        pasvertejums=["Protu atšķirt smaguma spēku no svara",
                      "Protu rēķināt svaru liftā",
                      "Protu izskaidrot pārslodzi",
                      "Protu izskaidrot bezsvara stāvokli"],
        nakama="Nākamā stunda: balsta reakcija."),
),

dict(
    nr="3.7", virsraksts="Balsta reakcija",
    jautajums="Kāpēc grīda «spiež pretī»?",
    apaksraksts="N · Perpendikulāri virsmai · N ≠ mg vienmēr",
    merkis="Saprast balsta reakcijas dabu un iemācīties to aprēķināt "
           "dažādās situācijās.",
    protu=["definēt balsta reakciju un tās virzienu;",
           "aprēķināt N horizontālā un slīpā virsmā;",
           "pamatot, kad N ≠ mg;",
           "saistīt N ar berzes spēku."],
    atkartojums="3.5. stundā N parādījās spēku shēmās. Tagad "
                "noskaidrosim, no kurienes tā rodas un kā to aprēķināt.",
    uzdevumu_apraksts="Balsta reakcija dažādās situācijās",
    teorija=[
        ("Kas ir balsta reakcija", [
            ("formula", "BALSTA REAKCIJA  N",
             "Vērsta VIENMĒR perpendikulāri balsta virsmai, prom no tās.",
             "Tā ir elastības spēks: balsts nedaudz deformējas un "
             "atgrūžas. Uz horizontālas virsmas bez vertikāla "
             "paātrinājuma N = mg, bet tā NAV vispārīga formula.", GOLD),
            ("tabula",
             ["Situācija", "Balsta reakcija N", "Piezīme"],
             [["Horizontāla virsma, miers", "N = mg", "Vienkāršākais "
               "gadījums"],
              ["Slīpa plakne, leņķis α", "N = mg·cos α", "Mazāka par mg"],
              ["Lifts kustas augšup ar a", "N = m(g + a)", "Lielāka par "
               "mg"],
              ["Ar spiedienu F lejup", "N = mg + F", "Piemēram, "
               "spiežot"],
              ["Brīvā krišana", "N = 0", "Balsts nespiež"]],
             [4.30, 3.90, 4.03]),
        ]),
        ("Kāpēc tas svarīgi", [
            ("panelis", "N NOSAKA BERZI",
             ["Berzes spēks F(b) = µN. Tāpēc katrā berzes uzdevumā "
              "vispirms jāatrod N. Slīpā plaknē N = mg·cos α, tāpēc "
              "berze tur ir MAZĀKA nekā uz horizontālas virsmas - to "
              "bieži aizmirst."], NAVY),
            ("kartitas", [
                ("VIRZIENS", BLUE,
                 ["Perpendikulāri virsmai.",
                  "Nekad ne pa virsmu."]),
                ("AVOTS", GREEN,
                 ["Balsta deformācija.",
                  "Elastības spēks."]),
                ("VĒRTĪBA", GOLD,
                 ["Atkarīga no situācijas.",
                  "N = mg tikai dažreiz."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="N ar papildu spiedienu",
             teksts="Uz 10 kg kasti, kas stāv uz grīdas, vertikāli lejup\n"
                    "spiež ar spēku 40 N. Aprēķini balsta reakciju! "
                    "(g = 9,8 m/s²)",
             dots=["m = 10 kg", "F = 40 N (lejup)", "g = 9,8 m/s²"],
             jaaprekina=["N = ?"],
             formulas=["y: N − mg − F = 0", "N = mg + F"],
             aprekins=["1)  mg = 10 · 9,8 = 98 N",
                       "2)  N = 98 + 40",
                       "3)  N = 138 N"],
             atbilde="N = 138 N ≈ 1,4·10² N",
             piezime="Šeit N ≠ mg - papildu spiediens palielina reakciju."),
        dict(nr=2, virsraksts="N slīpā plaknē",
             teksts="Kaste (m = 25 kg) stāv uz slīpas plaknes ar leņķi "
                    "30°.\nAprēķini balsta reakciju! (g = 9,8 m/s²; "
                    "cos 30° = 0,87)",
             dots=["m = 25 kg", "α = 30°", "cos 30° = 0,87"],
             jaaprekina=["N = ?"],
             formulas=["N = mg · cos α"],
             aprekins=["1)  mg = 25 · 9,8 = 245 N",
                       "2)  N = 245 · 0,87",
                       "3)  N = 213 ≈ 2,1·10² N"],
             atbilde="N ≈ 2,1·10² N  (mazāka par mg = 245 N)",
             piezime="Jo stāvāka plakne, jo mazāka N un mazāka berze."),
        dict(nr=3, virsraksts="N ar velkošu spēku leņķī",
             teksts="Kasti (m = 20 kg) velk ar spēku 60 N, kas vērsts "
                    "30°\nleņķī uz augšu. Aprēķini balsta reakciju!\n"
                    "(g = 9,8 m/s²; sin 30° = 0,50)",
             dots=["m = 20 kg", "F = 60 N", "α = 30°"],
             jaaprekina=["N = ?"],
             formulas=["F_y = F·sin α", "N = mg − F_y"],
             aprekins=["1)  mg = 20 · 9,8 = 196 N",
                       "2)  F_y = 60 · 0,50 = 30 N",
                       "3)  N = 196 − 30 = 166 N"],
             atbilde="N = 166 N ≈ 1,7·10² N",
             piezime="Velkot slīpi uz augšu, N samazinās - tāpēc kasti "
                     "vieglāk vilkt nekā stumt."),
        dict(nr=4, virsraksts="N un berze",
             teksts="Izmantojot 3. uzdevuma datus un µ = 0,30, aprēķini\n"
                    "berzes spēku un salīdzini to ar gadījumu, kad velk\n"
                    "horizontāli!",
             dots=["N₁ = 166 N", "N₂ = 196 N", "µ = 0,30"],
             jaaprekina=["F(b1) = ?", "F(b2) = ?"],
             formulas=["F(b) = µN"],
             aprekins=["1)  Slīpi: F(b) = 0,30 · 166 = 49,8 N",
                       "2)  Horizontāli: F(b) = 0,30 · 196 = 58,8 N",
                       "3)  Starpība ≈ 9 N (15 %)"],
             atbilde="Velkot slīpi, berze ir par ~9 N mazāka.",
             piezime="Praktisks secinājums: smagu somu labāk vilkt aiz "
                     "roktura uz augšu, nevis stumt."),
        dict(nr=5, virsraksts="N liftā",
             teksts="Kaste (m = 15 kg) stāv uz lifta grīdas. Lifts kustas "
                    "uz\naugšu ar paātrinājumu 1,5 m/s². Aprēķini balsta "
                    "reakciju!\n(g = 9,8 m/s²)",
             dots=["m = 15 kg", "a = 1,5 m/s² (uz augšu)",
                   "g = 9,8 m/s²"],
             jaaprekina=["N = ?"],
             formulas=["y: N − mg = ma", "N = m(g + a)"],
             aprekins=["1)  g + a = 9,8 + 1,5 = 11,3 m/s²",
                       "2)  N = 15 · 11,3",
                       "3)  N = 169,5 ≈ 1,7·10² N"],
             atbilde="N ≈ 1,7·10² N  (mierā būtu 147 N)",
             piezime="Balsta reakcija skaitliski sakrīt ar kastes svaru - "
                     "tie ir trešā likuma pāris."),
        dict(nr=6, virsraksts="Stumšana slīpi uz leju",
             teksts="Kasti (m = 20 kg) stumj ar spēku 50 N, kas vērsts "
                    "30°\nleņķī uz leju. Aprēķini balsta reakciju!\n"
                    "(g = 9,8 m/s²; sin 30° = 0,50)",
             dots=["m = 20 kg", "F = 50 N", "α = 30° uz leju"],
             jaaprekina=["N = ?"],
             formulas=["F_y = F·sin α", "N = mg + F_y"],
             aprekins=["1)  mg = 20 · 9,8 = 196 N",
                       "2)  F_y = 50 · 0,50 = 25 N (lejup)",
                       "3)  N = 196 + 25 = 221 N"],
             atbilde="N = 221 N ≈ 2,2·10² N",
             piezime="Stumjot slīpi uz leju, N un līdz ar to berze "
                     "PALIELINĀS - tāpēc stumt ir grūtāk nekā vilkt."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Balsta reakcija vērsta perpendikulāri virsmai.",
            "N = mg tikai horizontālā virsmā bez papildu spēkiem.",
            "Slīpā plaknē N = mg·cos α.",
            "N nosaka berzes spēku: F(b) = µN.",
        ],
        majasdarbs=[
            "m = 30 kg, uz kasti spiež 50 N lejup. Aprēķini N.",
            "m = 12 kg, α = 45° (cos 45° = 0,71). Aprēķini N.",
            "m = 18 kg, velk ar 70 N 20° leņķī uz augšu (sin 20° = "
            "0,34). Aprēķini N.",
        ],
        pasvertejums=["Protu noteikt N virzienu",
                      "Protu rēķināt N dažādās situācijās",
                      "Protu pamatot, kad N ≠ mg",
                      "Protu saistīt N ar berzi"],
        nakama="Nākamā stunda: elastības spēks un Huka likums."),
),

]
