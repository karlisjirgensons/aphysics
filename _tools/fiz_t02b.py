# -*- coding: utf-8 -*-
"""2. temats. B daļa: 2.8.-2.14. stunda (mešana, riņķa kustība, PD3)."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t02a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="2.8", virsraksts="Uzdevumi: krišana un mešana",
    jautajums="Cik ilgi ķermenis atrodas gaisā?",
    apaksraksts="Krišana · Mešana uz augšu · LD2 sagatavošana",
    merkis="Nostiprināt krišanas un mešanas uzdevumus un sagatavoties "
           "LD2 - brīvās krišanas paātrinājuma noteikšanai.",
    protu=["risināt kombinētus krišanas uzdevumus;",
           "izvēlēties ass virzienu un zīmes;",
           "novērtēt rezultāta ticamību;",
           "sagatavot LD2 mērījumu plānu."],
    atkartojums="2.6. un 2.7. stunda: h = gt²/2, v = gt, h(max) = "
                "v₀²/(2g). Šodien tās lietosim kopā un sagatavosim "
                "laboratorijas darbu.",
    uzdevumu_apraksts="Kombinēti krišanas uzdevumi un svārsta metode",
    teorija=[
        ("Ass izvēle un zīmes", [
            ("divi",
             ("ASS UZ AUGŠU", BLUE,
              ["v₀ > 0 (metot uz augšu).",
               "a = −g = −9,8 m/s².",
               "h > 0 virs sākuma punkta.",
               "Ērti mešanas uzdevumos."]),
             ("ASS UZ LEJU", GREEN,
              ["v₀ = 0 vai > 0 (metot lejup).",
               "a = +g = 9,8 m/s².",
               "h > 0 zem sākuma punkta.",
               "Ērti tīras krišanas uzdevumos."])),
            ("panelis", "GALVENAIS NOTEIKUMS",
             ["Ass virzienu izvēlas brīvi, bet TAD tas jāievēro visos "
              "lielumos. Lielākā daļa kļūdu rodas tāpēc, ka ass izvēlēta "
              "uz augšu, bet g ierakstīts ar plusu."], NAVY),
        ]),
        ("Gatavošanās LD2", [
            ("formula", "SVĀRSTA METODE",
             "T = 2π · √(l / g)        ⟹        g = 4π² l / T²",
             "Periodu nosaka precīzi, mērot laiku N svārstībām: T = t/N. "
             "Ar N = 20 hronometra kļūda samazinās 20 reižu.", GOLD),
            ("tabula",
             ["LD2 solis", "Ko dara", "Ko pieraksta"],
             [["Sagatavošana", "Iekar svārstu statīvā", "Garumu l"],
              ["Ierosināšana", "Novirze līdz 10°", "Leņķa kontrole"],
              ["Mērījums", "Laiks 20 svārstībām", "t₁ un t₂"],
              ["Atkārtojums", "5 dažādi garumi", "Tabulas rindas"],
              ["Aprēķins", "T = t/20; g = 4π²l/T²", "g katrai rindai"]],
             [3.40, 4.60, 4.23]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Mešana lejup",
             teksts="No 40 m augstuma akmeni met lejup ar sākuma ātrumu\n"
                    "5,0 m/s. Cik ilgi tas krīt? (g = 9,8 m/s²)",
             dots=["h = 40 m", "v₀ = 5,0 m/s (lejup)", "g = 9,8 m/s²"],
             jaaprekina=["t = ?"],
             formulas=["h = v₀t + gt²/2", "4,9t² + 5t − 40 = 0"],
             aprekins=["1)  40 = 5t + 4,9t²",
                       "2)  4,9t² + 5t − 40 = 0",
                       "3)  t = (−5 + √(25 + 784)) : 9,8 = "
                       "(−5 + 28,4) : 9,8 ≈ 2,4 s"],
             atbilde="t ≈ 2,4 s",
             piezime="Bez sākuma ātruma krišana prasītu 2,9 s - "
                     "salīdzinājums apstiprina rezultātu."),
        dict(nr=2, virsraksts="Divi ķermeņi",
             teksts="Viens ķermenis krīt no 45 m, otru vienlaikus met "
                    "no zemes\nuz augšu ar 30 m/s. Kad tie satiksies? "
                    "(g = 9,8 m/s²)",
             dots=["h = 45 m", "v₀ = 30 m/s", "g = 9,8 m/s²"],
             jaaprekina=["t = ?"],
             formulas=["y₁ = 45 − gt²/2", "y₂ = 30t − gt²/2",
                       "y₁ = y₂"],
             aprekins=["1)  45 − 4,9t² = 30t − 4,9t²",
                       "2)  45 = 30t",
                       "3)  t = 1,5 s"],
             atbilde="t = 1,5 s",
             piezime="Locekļi ar t² saīsinās - abiem ķermeņiem ir tāds "
                     "pats paātrinājums."),
        dict(nr=3, virsraksts="Svārsta periods",
             teksts="Svārsta garums ir 0,80 m. Aprēķini periodu!\n"
                    "(g = 9,8 m/s²;  π² ≈ 9,87)",
             dots=["l = 0,80 m", "g = 9,8 m/s²"],
             jaaprekina=["T = ?"],
             formulas=["T = 2π√(l/g)"],
             aprekins=["1)  l/g = 0,80 : 9,8 = 0,0816 s²",
                       "2)  √0,0816 = 0,286 s",
                       "3)  T = 2 · 3,14 · 0,286 = 1,80 s"],
             atbilde="T ≈ 1,8 s",
             piezime="20 svārstības aizņemtu 36 s - ērts mērījums."),
        dict(nr=4, virsraksts="g no svārsta mērījuma",
             teksts="Svārsts ar garumu 1,00 m veic 20 svārstības 40,2 s "
                    "laikā.\nAprēķini brīvās krišanas paātrinājumu!",
             dots=["l = 1,00 m", "N = 20", "t = 40,2 s"],
             jaaprekina=["g = ?"],
             formulas=["T = t/N", "g = 4π²l/T²"],
             aprekins=["1)  T = 40,2 : 20 = 2,01 s",
                       "2)  T² = 4,04 s²",
                       "3)  g = 4 · 9,87 · 1,00 : 4,04 ≈ 9,77 m/s²"],
             atbilde="g ≈ 9,8 m/s²  (novirze no 9,81 ir 0,4 %)",
             piezime="Tieši šo aprēķinu veiksi LD2 laboratorijas darbā."),
        dict(nr=5, virsraksts="Svārsta garums no perioda",
             teksts="Svārsta periods ir 2,00 s.\n"
                    "Aprēķini svārsta garumu! (g = 9,8 m/s²; π² ≈ 9,87)",
             dots=["T = 2,00 s", "g = 9,8 m/s²"],
             jaaprekina=["l = ?"],
             formulas=["T = 2π√(l/g)", "l = gT²/(4π²)"],
             aprekins=["1)  T² = 4,00 s²",
                       "2)  4π² = 39,5",
                       "3)  l = 9,8 · 4,00 : 39,5 = 0,99 m"],
             atbilde="l ≈ 0,99 m ≈ 1,0 m",
             piezime="Metru garam svārstam periods ir gandrīz tieši 2 s - "
                     "to izmantoja pirmajos pulksteņos."),
        dict(nr=6, virsraksts="Ātrums pie zemes, metot lejup",
             teksts="No 30 m augstuma ķermeni met lejup ar 4,0 m/s.\n"
                    "Cik liels ir ātrums pie zemes? (g = 9,8 m/s²)",
             dots=["h = 30 m", "v₀ = 4,0 m/s (lejup)", "g = 9,8 m/s²"],
             jaaprekina=["v = ?"],
             formulas=["v² = v₀² + 2gh"],
             aprekins=["1)  v₀² = 16 m²/s²",
                       "2)  2gh = 2 · 9,8 · 30 = 588 m²/s²",
                       "3)  v = √604 ≈ 24,6 m/s"],
             atbilde="v ≈ 25 m/s",
             piezime="Bez sākuma ātruma iznāktu 24,2 m/s - starpība maza, "
                     "jo krišanas ceļš ir garš."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ass virzienu izvēlas brīvi, bet zīmes jāievēro visur.",
            "Diviem ķermeņiem ar vienādu g locekļi ar t² saīsinās.",
            "T = 2π√(l/g);  g = 4π²l/T².",
            "Mērot 20 svārstības, hronometra kļūda samazinās 20 reižu.",
        ],
        majasdarbs=[
            "Sagatavo LD2 protokola hipotēzi un piederumu sarakstu.",
            "l = 0,50 m. Aprēķini T un laiku 20 svārstībām.",
            "No 60 m met lejup ar 8,0 m/s. Aprēķini krišanas laiku.",
        ],
        pasvertejums=["Protu izvēlēties asi un zīmes",
                      "Protu risināt divu ķermeņu uzdevumus",
                      "Protu lietot svārsta formulu",
                      "Esmu gatavs LD2"],
        nakama="Nākamā stunda: LD2 - brīvās krišanas paātrinājuma "
               "noteikšana."),
),

dict(
    nr="2.9", virsraksts="Horizontāli mests ķermenis",
    jautajums="Kāpēc lodes trajektorija ir parabola?",
    apaksraksts="Kustību neatkarība · x = v₀t · y = gt²/2",
    merkis="Iemācīties sadalīt horizontālu mešanu divās neatkarīgās "
           "kustībās un aprēķināt lidojuma laiku, attālumu un ātrumu.",
    protu=["sadalīt kustību horizontālā un vertikālā komponentē;",
           "aprēķināt lidojuma laiku un attālumu;",
           "aprēķināt ātrumu nokrišanas brīdī;",
           "pamatot kustību neatkarības principu."],
    atkartojums="1.4. stundā mācījāmies projekcijas. Tagad tās lietosim "
                "kustībai: horizontāli - vienmērīga, vertikāli - brīvā "
                "krišana.",
    uzdevumu_apraksts="Lidojuma laiks, attālums un ātrums",
    teorija=[
        ("Kustību neatkarības princips", [
            ("formula", "HORIZONTĀLI MESTS ĶERMENIS",
             "x = v₀ · t        y = g t² / 2        t = √(2h / g)        "
             "L = v₀ · √(2h / g)",
             "Horizontālā un vertikālā kustība notiek NEATKARĪGI. "
             "Krišanas laiks ir tāds pats kā ķermenim, kas vienkārši "
             "nomests no tā paša augstuma.", GOLD),
            ("divi",
             ("HORIZONTĀLI  x", BLUE,
              ["Vienmērīga kustība.",
               "vₓ = v₀ = const.",
               "Nav paātrinājuma.",
               "x = v₀t."]),
             ("VERTIKĀLI  y", GREEN,
              ["Brīvā krišana.",
               "v_y = gt (aug).",
               "a = g.",
               "y = gt²/2."])),
        ]),
        ("Trajektorija un ātrums", [
            ("panelis", "KLASISKAIS DEMONSTRĒJUMS",
             ["Divas lodītes: vienu nomet, otru vienlaikus izšauj "
              "horizontāli. Abas sasniedz grīdu VIENLAIKUS, lai gan otrā "
              "aizlido daudz tālāk. Tas pierāda kustību neatkarību."],
             NAVY),
            ("tabula",
             ["Lielums", "Formula", "Piezīme"],
             [["Lidojuma laiks", "t = √(2h/g)", "Nav atkarīgs no v₀"],
              ["Lidojuma attālums", "L = v₀t", "Proporcionāls v₀"],
              ["Ātruma vertikālā daļa", "v_y = gt", "Aug ar laiku"],
              ["Pilnais ātrums", "v = √(v₀² + v_y²)", "Pitagora teorēma"]],
             [4.30, 3.90, 4.03]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Lidojuma laiks un attālums",
             teksts="No 20 m augsta torņa horizontāli izmet akmeni ar "
                    "ātrumu\n15 m/s. Aprēķini lidojuma laiku un "
                    "attālumu! (g = 9,8 m/s²)",
             dots=["h = 20 m", "v₀ = 15 m/s", "g = 9,8 m/s²"],
             jaaprekina=["t = ?", "L = ?"],
             formulas=["t = √(2h/g)", "L = v₀t"],
             aprekins=["1)  2h/g = 40 : 9,8 = 4,08 s²",
                       "2)  t = 2,02 ≈ 2,0 s",
                       "3)  L = 15 · 2,0 = 30 m"],
             atbilde="t ≈ 2,0 s ;   L ≈ 30 m",
             piezime="Ja v₀ būtu divreiz lielāks, laiks nemainītos, bet "
                     "attālums dubultotos."),
        dict(nr=2, virsraksts="Ātrums nokrišanas brīdī",
             teksts="Izmantojot 1. uzdevuma datus, aprēķini ātrumu\n"
                    "nokrišanas brīdī!",
             dots=["v₀ = 15 m/s", "t = 2,0 s", "g = 9,8 m/s²"],
             jaaprekina=["v = ?"],
             formulas=["v_y = gt", "v = √(v₀² + v_y²)"],
             aprekins=["1)  v_y = 9,8 · 2,0 = 19,6 m/s",
                       "2)  v² = 225 + 384 = 609 m²/s²",
                       "3)  v = 24,7 ≈ 25 m/s"],
             atbilde="v ≈ 25 m/s",
             piezime="Ātrums pie zemes vienmēr ir lielāks par sākuma "
                     "ātrumu."),
        dict(nr=3, virsraksts="Augstuma noteikšana",
             teksts="Bumba, izmesta horizontāli ar 12 m/s, nokrīt 36 m\n"
                    "attālumā. No kāda augstuma tā izmesta? "
                    "(g = 9,8 m/s²)",
             dots=["v₀ = 12 m/s", "L = 36 m", "g = 9,8 m/s²"],
             jaaprekina=["h = ?"],
             formulas=["t = L/v₀", "h = gt²/2"],
             aprekins=["1)  t = 36 : 12 = 3,0 s",
                       "2)  t² = 9,0 s²",
                       "3)  h = 9,8 · 9,0 : 2 = 44,1 ≈ 44 m"],
             atbilde="h ≈ 44 m",
             piezime="Vispirms no horizontālās kustības atrod laiku, tad "
                     "no vertikālās - augstumu."),
        dict(nr=4, virsraksts="Divas lodītes",
             teksts="Vienu lodīti nomet no 5,0 m, otru vienlaikus izšauj\n"
                    "horizontāli ar 20 m/s no tā paša augstuma.\n"
                    "Kura sasniegs grīdu pirmā? Pamato ar aprēķinu!",
             dots=["h = 5,0 m", "v₀₁ = 0", "v₀₂ = 20 m/s"],
             jaaprekina=["t₁ = ?", "t₂ = ?"],
             formulas=["t = √(2h/g) - abām vienāds"],
             aprekins=["1)  t₁ = √(10 : 9,8) = 1,01 s",
                       "2)  Otrai vertikālā kustība ir tāda pati",
                       "3)  t₂ = 1,01 s - vienādi"],
             atbilde="Abas sasniedz grīdu vienlaikus (t ≈ 1,0 s).",
             piezime="Otrā aizlido 20 m tālāk, bet krīt tikpat ilgi - "
                     "kustību neatkarība."),
        dict(nr=5, virsraksts="Sākuma ātrums no attāluma",
             teksts="No 80 m augstuma horizontāli izmests ķermenis "
                    "nokrīt\n60 m attālumā. Ar kādu ātrumu tas tika "
                    "izmests? (g = 9,8 m/s²)",
             dots=["h = 80 m", "L = 60 m", "g = 9,8 m/s²"],
             jaaprekina=["t = ?", "v₀ = ?"],
             formulas=["t = √(2h/g)", "v₀ = L/t"],
             aprekins=["1)  2h/g = 160 : 9,8 = 16,3 s²",
                       "2)  t = 4,04 s",
                       "3)  v₀ = 60 : 4,04 ≈ 14,9 m/s"],
             atbilde="v₀ ≈ 15 m/s",
             piezime="Laiku vienmēr nosaka tikai augstums - tikai pēc tam "
                     "var izteikt horizontālo ātrumu."),
        dict(nr=6, virsraksts="Ātruma virziens pie zemes",
             teksts="Ķermeni met horizontāli ar 10 m/s no 5,0 m "
                    "augstuma.\nKādā leņķī pret horizontu tas nokrīt? "
                    "(g = 9,8 m/s²)",
             dots=["v₀ = 10 m/s", "h = 5,0 m", "g = 9,8 m/s²"],
             jaaprekina=["t = ?", "v_y = ?", "α = ?"],
             formulas=["t = √(2h/g)", "v_y = gt", "tg α = v_y/v₀"],
             aprekins=["1)  t = √(10 : 9,8) = 1,01 s",
                       "2)  v_y = 9,8 · 1,01 = 9,9 m/s",
                       "3)  tg α = 9,9 : 10 = 0,99 → α ≈ 45°"],
             atbilde="α ≈ 45° pret horizontu",
             piezime="Leņķis 45° iznāk tad, kad abas ātruma projekcijas "
                     "ir vienādas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Horizontālā un vertikālā kustība ir neatkarīgas.",
            "t = √(2h/g) - nav atkarīgs no sākuma ātruma.",
            "L = v₀t - proporcionāls sākuma ātrumam.",
            "v = √(v₀² + v_y²) nokrišanas brīdī.",
        ],
        majasdarbs=[
            "h = 45 m, v₀ = 10 m/s. Aprēķini t, L un v.",
            "L = 24 m, v₀ = 8,0 m/s. Aprēķini h.",
            "Paskaidro, kāpēc lidojuma laiks nav atkarīgs no v₀.",
        ],
        pasvertejums=["Protu sadalīt kustību komponentēs",
                      "Protu rēķināt lidojuma laiku",
                      "Protu rēķināt attālumu un ātrumu",
                      "Protu pamatot kustību neatkarību"],
        nakama="Nākamā stunda: kustība pa riņķa līniju."),
),

dict(
    nr="2.10", virsraksts="Kustība pa riņķa līniju",
    jautajums="Ar ko riņķa kustība atšķiras no taisnvirziena?",
    apaksraksts="Periods · Frekvence · v = 2πR/T · ω",
    merkis="Iemācīties raksturot kustību pa riņķa līniju ar periodu, "
           "frekvenci, lineāro un leņķisko ātrumu.",
    protu=["definēt periodu un frekvenci;",
           "aprēķināt lineāro ātrumu v = 2πR/T;",
           "lietot leņķisko ātrumu ω = 2π/T;",
           "saistīt v un ω ar sakarību v = ωR."],
    atkartojums="Līdz šim kustība bija pa taisni. Kustībā pa riņķa "
                "līniju ātruma MODULIS var būt nemainīgs, bet VIRZIENS "
                "mainās nepārtraukti.",
    uzdevumu_apraksts="Periods, frekvence, lineārais un leņķiskais ātrums",
    teorija=[
        ("Riņķa kustības raksturlielumi", [
            ("kartitas", [
                ("PERIODS  T", BLUE,
                 ["Laiks vienam pilnam apgriezienam.",
                  "T = t / N",
                  "[T] = s"]),
                ("FREKVENCE  n", GREEN,
                 ["Apgriezienu skaits sekundē.",
                  "n = N / t = 1/T",
                  "[n] = Hz jeb s⁻¹"]),
                ("LEŅĶISKAIS  ω", GOLD,
                 ["Leņķis sekundē.",
                  "ω = 2π/T = 2πn",
                  "[ω] = rad/s"]),
            ]),
            ("formula", "LINEĀRAIS ĀTRUMS",
             "v = 2πR / T = 2πRn = ωR",
             "Lineārais ātrums vērsts pa pieskari riņķa līnijai. Jo tālāk "
             "no centra, jo lielāks v pie tā paša ω.", GOLD),
        ]),
        ("Kur tas sastopams", [
            ("tabula",
             ["Objekts", "Periods T", "Piezīme"],
             [["Pulksteņa sekunžu rādītājs", "60 s", "n = 1/60 Hz"],
              ["Zeme ap savu asi", "24 h", "v uz ekvatora 465 m/s"],
              ["Zeme ap Sauli", "365 dienas", "v ≈ 30 km/s"],
              ["Velosipēda ritenis 20 km/h", "~0,7 s", "R = 0,35 m"],
              ["Veļasmašīnas centrifūga", "~0,05 s", "1200 apgr./min"]],
             [5.10, 3.20, 3.93]),
            ("panelis", "SVARĪGA ATŠĶIRĪBA",
             ["Karuselī visiem punktiem ir VIENĀDS leņķiskais ātrums ω, "
              "bet DAŽĀDS lineārais ātrums v = ωR. Tāpēc malā griežas "
              "«ātrāk» nekā centrā."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Periods un frekvence",
             teksts="Ritenis veic 300 apgriezienus 2,0 minūtēs.\n"
                    "Aprēķini periodu un frekvenci!",
             dots=["N = 300", "t = 2,0 min = 120 s"],
             jaaprekina=["T = ?", "n = ?"],
             formulas=["T = t/N", "n = N/t = 1/T"],
             aprekins=["1)  T = 120 : 300 = 0,40 s",
                       "2)  n = 300 : 120 = 2,5 Hz",
                       "3)  Pārbaude: 1 : 0,40 = 2,5 ✔"],
             atbilde="T = 0,40 s ;   n = 2,5 Hz",
             piezime="T un n vienmēr ir savstarpēji apgriezti lielumi."),
        dict(nr=2, virsraksts="Lineārais ātrums",
             teksts="Karuseļa rādiuss ir 4,0 m, apgrieziena periods "
                    "8,0 s.\nAprēķini lineāro un leņķisko ātrumu! "
                    "(π ≈ 3,14)",
             dots=["R = 4,0 m", "T = 8,0 s"],
             jaaprekina=["v = ?", "ω = ?"],
             formulas=["v = 2πR/T", "ω = 2π/T"],
             aprekins=["1)  2πR = 2 · 3,14 · 4,0 = 25,1 m",
                       "2)  v = 25,1 : 8,0 = 3,1 m/s",
                       "3)  ω = 6,28 : 8,0 = 0,79 rad/s"],
             atbilde="v ≈ 3,1 m/s ;   ω ≈ 0,79 rad/s",
             piezime="Pārbaude: v = ωR = 0,79 · 4,0 = 3,1 m/s ✔"),
        dict(nr=3, virsraksts="Velosipēda ritenis",
             teksts="Velosipēds brauc 18 km/h, riteņa rādiuss 0,35 m.\n"
                    "Aprēķini riteņa apgriezienu frekvenci! (π ≈ 3,14)",
             dots=["v = 18 km/h = 5,0 m/s", "R = 0,35 m"],
             jaaprekina=["n = ?"],
             formulas=["v = 2πRn", "n = v/(2πR)"],
             aprekins=["1)  v = 18 : 3,6 = 5,0 m/s",
                       "2)  2πR = 2 · 3,14 · 0,35 = 2,20 m",
                       "3)  n = 5,0 : 2,20 ≈ 2,3 Hz"],
             atbilde="n ≈ 2,3 apgriezieni sekundē",
             piezime="Tas ir aptuveni 136 apgriezieni minūtē."),
        dict(nr=4, virsraksts="Divi punkti uz diska",
             teksts="Disks griežas ar periodu 0,50 s. Punkts A ir 10 cm,\n"
                    "punkts B - 25 cm no centra. Salīdzini to ātrumus!",
             dots=["T = 0,50 s", "R(A) = 0,10 m", "R(B) = 0,25 m"],
             jaaprekina=["v(A) = ?", "v(B) = ?", "ω = ?"],
             formulas=["ω = 2π/T", "v = ωR"],
             aprekins=["1)  ω = 6,28 : 0,50 = 12,6 rad/s (abiem vienāds)",
                       "2)  v(A) = 12,6 · 0,10 = 1,26 m/s",
                       "3)  v(B) = 12,6 · 0,25 = 3,14 m/s"],
             atbilde="ω vienāds; v(B) : v(A) = 2,5 - tāpat kā rādiusu "
                     "attiecība.",
             piezime="Leņķiskais ātrums ir visa diska īpašība, lineārais - "
                     "konkrētā punkta."),
        dict(nr=5, virsraksts="Leņķiskais ātrums no frekvences",
             teksts="Elektromotora rotors griežas ar frekvenci 50 Hz.\n"
                    "Aprēķini periodu un leņķisko ātrumu! (π ≈ 3,14)",
             dots=["n = 50 Hz"],
             jaaprekina=["T = ?", "ω = ?"],
             formulas=["T = 1/n", "ω = 2πn"],
             aprekins=["1)  T = 1 : 50 = 0,020 s",
                       "2)  ω = 2 · 3,14 · 50",
                       "3)  ω = 314 rad/s"],
             atbilde="T = 0,020 s ;   ω ≈ 3,1·10² rad/s",
             piezime="50 Hz ir Latvijas elektrotīkla frekvence - "
                     "tāpēc tieši tik griežas daudzi motori."),
        dict(nr=6, virsraksts="Pulksteņa minūšu rādītājs",
             teksts="Minūšu rādītāja garums ir 12 cm.\n"
                    "Aprēķini tā leņķisko un lineāro ātrumu gala punktā! "
                    "(π ≈ 3,14)",
             dots=["R = 0,12 m", "T = 1 h = 3600 s"],
             jaaprekina=["ω = ?", "v = ?"],
             formulas=["ω = 2π/T", "v = ωR"],
             aprekins=["1)  ω = 6,28 : 3600 = 1,74·10⁻³ rad/s",
                       "2)  v = 1,74·10⁻³ · 0,12",
                       "3)  v ≈ 2,1·10⁻⁴ m/s"],
             atbilde="ω ≈ 1,7·10⁻³ rad/s ;   v ≈ 2,1·10⁻⁴ m/s",
             piezime="Tas ir aptuveni 0,75 m stundā - lēni, bet "
                     "nepārtraukti."),
        dict(nr=7, virsraksts="Ceļš un pārvietojums pa riņķi",
             teksts="Ķermenis veic 15 pilnus apgriezienus pa riņķa "
                    "līniju\nar rādiusu 2,0 m. Aprēķini ceļu un "
                    "pārvietojumu! (π ≈ 3,14)",
             dots=["R = 2,0 m", "N = 15"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = N · 2πR", "d⃗ - no sākuma uz beigām"],
             aprekins=["1)  2πR = 6,28 · 2,0 = 12,6 m",
                       "2)  s = 15 · 12,6 = 188 m",
                       "3)  Sākums un beigas sakrīt → |d⃗| = 0"],
             atbilde="s ≈ 1,9·10² m ;   |d⃗| = 0 m",
             piezime="Riņķa kustībā pēc pilna apgrieziena pārvietojums "
                     "vienmēr ir nulle."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "T = t/N;  n = 1/T;  ω = 2π/T.",
            "v = 2πR/T = ωR.",
            "Uz viena diska ω ir vienāds, bet v atkarīgs no rādiusa.",
            "Riņķa kustībā ātruma virziens mainās nepārtraukti.",
        ],
        majasdarbs=[
            "N = 120 apgriezieni 30 s laikā. Aprēķini T, n un ω.",
            "R = 0,60 m, T = 1,5 s. Aprēķini v un ω.",
            "v = 12 m/s, R = 3,0 m. Aprēķini T un n.",
        ],
        pasvertejums=["Protu rēķināt periodu un frekvenci",
                      "Protu rēķināt lineāro ātrumu",
                      "Protu lietot leņķisko ātrumu",
                      "Protu salīdzināt punktus uz diska"],
        nakama="Nākamā stunda: centrtieces paātrinājums."),
),

dict(
    nr="2.11", virsraksts="Centrtieces paātrinājums",
    jautajums="Kāpēc kustība pa riņķi ir paātrināta?",
    apaksraksts="a = v²/R = ω²R · Virziens uz centru",
    merkis="Saprast, kāpēc kustībā pa riņķa līniju ar nemainīgu ātruma "
           "moduli tomēr ir paātrinājums, un iemācīties to aprēķināt.",
    protu=["paskaidrot, kāpēc riņķa kustība ir paātrināta;",
           "lietot a = v²/R un a = ω²R;",
           "noteikt paātrinājuma virzienu;",
           "novērtēt pārslodzi ar g vienībām."],
    atkartojums="2.10. stundā: v = ωR. Ātruma MODULIS var būt nemainīgs, "
                "bet VIRZIENS mainās - tātad ātruma vektors mainās, un "
                "paātrinājums nav nulle.",
    uzdevumu_apraksts="Centrtieces paātrinājums un pārslodze",
    teorija=[
        ("Kāpēc paātrinājums nav nulle", [
            ("formula", "CENTRTIECES PAĀTRINĀJUMS",
             "a = v² / R = ω² R = 4π² R / T²",
             "Vērsts VIENMĒR uz riņķa centru, perpendikulāri ātrumam. "
             "Tas maina tikai ātruma virzienu, nevis moduli.", GOLD),
            ("panelis", "PAĀTRINĀJUMS BEZ ĀTRUMA MAIŅAS",
             ["Paātrinājums ir ātruma VEKTORA izmaiņa. Riņķa kustībā "
              "vektora garums paliek tas pats, bet virziens mainās "
              "nepārtraukti - tāpēc a ≠ 0. Ja paātrinājuma nebūtu, "
              "ķermenis lidotu pa pieskari taisni prom."], NAVY),
        ]),
        ("Kur tas jūtams", [
            ("tabula",
             ["Situācija", "Aptuvenais a", "Cik g"],
             [["Automašīna līkumā 50 km/h, R = 50 m", "3,9 m/s²",
               "0,4 g"],
              ["Karuselis parkā", "5-10 m/s²", "0,5-1 g"],
              ["Lidmašīnas akrobātika", "60 m/s²", "6 g"],
              ["Veļasmašīnas centrifūga", "~4000 m/s²", "400 g"]],
             [5.60, 3.20, 3.43]),
            ("kartitas", [
                ("MAZĀKS R", RED,
                 ["a = v²/R aug.",
                  "Ass līkums - bīstamāks."]),
                ("LIELĀKS v", RED,
                 ["a ~ v² - aug kvadrātā.",
                  "Divreiz ātrāk - četrreiz lielāks a."]),
                ("VIRZIENS", BLUE,
                 ["Vienmēr uz centru.",
                  "Perpendikulāri ātrumam."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Paātrinājums līkumā",
             teksts="Automašīna brauc 72 km/h pa līkumu ar rādiusu "
                    "100 m.\nAprēķini centrtieces paātrinājumu!",
             dots=["v = 72 km/h = 20 m/s", "R = 100 m"],
             jaaprekina=["a = ?"],
             formulas=["a = v²/R"],
             aprekins=["1)  v = 72 : 3,6 = 20 m/s",
                       "2)  v² = 400 m²/s²",
                       "3)  a = 400 : 100 = 4,0 m/s²"],
             atbilde="a = 4,0 m/s², vērsts uz līkuma centru.",
             piezime="Tas ir 0,41 g - jau labi jūtams sānu spiediens."),
        dict(nr=2, virsraksts="Ātruma ietekme",
             teksts="Kā mainīsies centrtieces paātrinājums, ja ātrumu\n"
                    "palielinās 3 reizes? Pamato ar formulu!",
             dots=["v₂ = 3v₁", "R nemainās"],
             jaaprekina=["a₂/a₁ = ?"],
             formulas=["a = v²/R"],
             aprekins=["1)  a₁ = v₁²/R",
                       "2)  a₂ = (3v₁)²/R = 9v₁²/R",
                       "3)  a₂ / a₁ = 9"],
             atbilde="Palielināsies 9 reizes.",
             piezime="Tāpēc pirms līkuma vienmēr samazina ātrumu, nevis "
                     "tikai «brauc uzmanīgi»."),
        dict(nr=3, virsraksts="Paātrinājums no perioda",
             teksts="Karuseļa rādiuss 5,0 m, apgrieziena periods 4,0 s.\n"
                    "Aprēķini centrtieces paātrinājumu! (π² ≈ 9,87)",
             dots=["R = 5,0 m", "T = 4,0 s"],
             jaaprekina=["a = ?"],
             formulas=["a = 4π²R/T²"],
             aprekins=["1)  4π² = 39,5",
                       "2)  T² = 16 s²",
                       "3)  a = 39,5 · 5,0 : 16 = 12,3 m/s²"],
             atbilde="a ≈ 12 m/s² ≈ 1,3 g",
             piezime="Vairāk nekā brīvās krišanas paātrinājums - tāpēc "
                     "sajūta ir spēcīga."),
        dict(nr=4, virsraksts="Zemes rotācija",
             teksts="Aprēķini centrtieces paātrinājumu uz ekvatora!\n"
                    "(R = 6,4·10⁶ m; T = 24 h = 86 400 s; π² ≈ 9,87)",
             dots=["R = 6,4·10⁶ m", "T = 86 400 s"],
             jaaprekina=["a = ?"],
             formulas=["a = 4π²R/T²"],
             aprekins=["1)  4π²R = 39,5 · 6,4·10⁶ = 2,53·10⁸ m",
                       "2)  T² = 7,46·10⁹ s²",
                       "3)  a = 2,53·10⁸ : 7,46·10⁹ ≈ 0,034 m/s²"],
             atbilde="a ≈ 0,034 m/s² - tikai 0,35 % no g.",
             piezime="Tāpēc uz ekvatora ķermeņi sver nedaudz mazāk nekā "
                     "polos."),
        dict(nr=5, virsraksts="Līkuma rādiuss",
             teksts="Automašīna brauc ar 15 m/s. Cik liels jābūt līkuma\n"
                    "rādiusam, lai centrtieces paātrinājums būtu "
                    "2,5 m/s²?",
             dots=["v = 15 m/s", "a = 2,5 m/s²"],
             jaaprekina=["R = ?"],
             formulas=["a = v²/R", "R = v²/a"],
             aprekins=["1)  v² = 225 m²/s²",
                       "2)  R = 225 : 2,5",
                       "3)  R = 90 m"],
             atbilde="R = 90 m",
             piezime="Jo lielāks rādiuss, jo mazāks paātrinājums - "
                     "tāpēc ātrgaitas ceļiem līkumi ir loti plūdeni."),
        dict(nr=6, virsraksts="Paātrinājums no frekvences",
             teksts="Slīpripa ar rādiusu 0,20 m griežas ar frekvenci "
                    "5,0 Hz.\nAprēķini centrtieces paātrinājumu malas "
                    "punktam! (π ≈ 3,14)",
             dots=["R = 0,20 m", "n = 5,0 Hz"],
             jaaprekina=["ω = ?", "a = ?"],
             formulas=["ω = 2πn", "a = ω²R"],
             aprekins=["1)  ω = 2 · 3,14 · 5,0 = 31,4 rad/s",
                       "2)  ω² = 986 rad²/s²",
                       "3)  a = 986 · 0,20 ≈ 197 m/s²"],
             atbilde="a ≈ 2,0·10² m/s² ≈ 20 g",
             piezime="Tāpēc bojāta slīpripa pie lieliem apgriezieniem "
                     "var saplīst - materiāls neiztur."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "a = v²/R = ω²R = 4π²R/T².",
            "Centrtieces paātrinājums vērsts uz riņķa centru.",
            "Tas maina ātruma virzienu, nevis moduli.",
            "a ir proporcionāls v² - ātrums ir izšķirošs.",
        ],
        majasdarbs=[
            "v = 15 m/s, R = 45 m. Aprēķini a un salīdzini ar g.",
            "R = 2,0 m, T = 1,0 s. Aprēķini a.",
            "Kā mainīsies a, ja rādiusu samazinās 2 reizes?",
        ],
        pasvertejums=["Protu paskaidrot, kāpēc a ≠ 0",
                      "Protu rēķināt a pēc v un R",
                      "Protu rēķināt a pēc T",
                      "Protu novērtēt pārslodzi"],
        nakama="Nākamā stunda: uzdevumi par riņķa kustību."),
),

dict(
    nr="2.12", virsraksts="Uzdevumi par riņķa kustību",
    jautajums="Cik ātri jāgriežas karuselim?",
    apaksraksts="Kombinēti uzdevumi · Pārnesumi · Drošība",
    merkis="Nostiprināt riņķa kustības uzdevumus, tostarp uzdevumus par "
           "pārnesumiem un drošu ātrumu līkumā.",
    protu=["kombinēt riņķa kustības formulas;",
           "risināt uzdevumus par saistītiem riteņiem;",
           "aprēķināt drošu ātrumu līkumā;",
           "pārbaudīt rezultāta ticamību."],
    atkartojums="Mums ir formulas: T = t/N, n = 1/T, ω = 2π/T, v = ωR, "
                "a = v²/R. Šodien mācāmies tās kombinēt.",
    uzdevumu_apraksts="Pārnesumi, saistīti riteņi un drošs ātrums",
    teorija=[
        ("Saistīti riteņi", [
            ("divi",
             ("UZ VIENAS ASS", BLUE,
              ["Vienāds leņķiskais ātrums: ω₁ = ω₂.",
               "Lineārie ātrumi atšķiras: v = ωR.",
               "Piemērs: divi diski uz viena vārpstas."]),
             ("SAVIENOTI AR SIKSNU", GREEN,
              ["Vienāds lineārais ātrums: v₁ = v₂.",
               "Leņķiskie atšķiras: ω = v/R.",
               "Piemērs: velosipēda ķēde, siksnas pārvads."])),
            ("formula", "PĀRNESUMA ATTIECĪBA",
             "Ar siksnu:  ω₁R₁ = ω₂R₂        ⟹        "
             "ω₁ / ω₂ = R₂ / R₁",
             "Mazāks skriemelis griežas ātrāk. Tieši tā velosipēdā maza "
             "aizmugurējā zvaigznīte dod lielu ātrumu.", GOLD),
        ]),
        ("Drošība līkumā", [
            ("panelis", "KĀPĒC ĀTRUMS IZŠĶIR",
             ["Centrtieces paātrinājumu nodrošina berzes spēks.",
              "a = v²/R",
              "Ja vajadzīgais paātrinājums pārsniedz to, ko var dot "
              "berze, automašīna izslīd. Tā kā a ~ v², ātruma "
              "palielināšana par 40 % divkāršo vajadzīgo berzi."], NAVY),
            ("tabula",
             ["R", "Drošs v (a ≤ 5 m/s²)", "Piezīme"],
             [["30 m", "12 m/s = 43 km/h", "Ass pilsētas līkums"],
              ["100 m", "22 m/s = 80 km/h", "Šosejas līkums"],
              ["300 m", "39 m/s = 139 km/h", "Lēzens līkums"]],
             [2.90, 5.10, 4.23]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Siksnas pārvads",
             teksts="Divus skriemeļus ar rādiusiem 6,0 cm un 18 cm "
                    "savieno\nsiksna. Mazais griežas ar 900 apgr./min.\n"
                    "Aprēķini lielā skriemeļa frekvenci!",
             dots=["R₁ = 6,0 cm", "R₂ = 18 cm", "n₁ = 900 apgr./min"],
             jaaprekina=["n₂ = ?"],
             formulas=["v₁ = v₂", "2πR₁n₁ = 2πR₂n₂", "n₂ = n₁R₁/R₂"],
             aprekins=["1)  n₁ = 900 : 60 = 15 Hz",
                       "2)  n₂ = 15 · 6,0 : 18",
                       "3)  n₂ = 5,0 Hz = 300 apgr./min"],
             atbilde="n₂ = 5,0 Hz = 300 apgriezieni minūtē",
             piezime="Lielāks skriemelis griežas lēnāk - tieši "
                     "proporcionāli rādiusu attiecībai."),
        dict(nr=2, virsraksts="Drošs ātrums līkumā",
             teksts="Līkuma rādiuss ir 80 m. Cik liels drīkst būt "
                    "ātrums,\nlai centrtieces paātrinājums nepārsniegtu "
                    "4,0 m/s²?",
             dots=["R = 80 m", "a = 4,0 m/s²"],
             jaaprekina=["v = ?"],
             formulas=["a = v²/R", "v = √(aR)"],
             aprekins=["1)  aR = 4,0 · 80 = 320 m²/s²",
                       "2)  v = √320",
                       "3)  v = 17,9 ≈ 18 m/s = 64 km/h"],
             atbilde="v ≈ 18 m/s ≈ 64 km/h",
             piezime="Uz slidena ceļa pieļaujamais a ir 2-3 reizes "
                     "mazāks - tad drošs ātrums ir tikai ~40 km/h."),
        dict(nr=3, virsraksts="Zemes pavadonis",
             teksts="Pavadonis riņķo ap Zemi 300 km augstumā ar periodu\n"
                    "90 min. Aprēķini ātrumu! (R(Zemes) = 6400 km; "
                    "π ≈ 3,14)",
             dots=["h = 300 km", "R(Z) = 6400 km", "T = 90 min = 5400 s"],
             jaaprekina=["v = ?"],
             formulas=["R = R(Z) + h", "v = 2πR/T"],
             aprekins=["1)  R = 6400 + 300 = 6700 km = 6,7·10⁶ m",
                       "2)  2πR = 6,28 · 6,7·10⁶ = 4,21·10⁷ m",
                       "3)  v = 4,21·10⁷ : 5400 ≈ 7,8·10³ m/s"],
             atbilde="v ≈ 7,8 km/s",
             piezime="Tas ir pirmais kosmiskais ātrums - to pētīsim "
                     "4. tematā."),
        dict(nr=4, virsraksts="Centrifūga",
             teksts="Veļasmašīnas cilindra rādiuss ir 0,25 m, "
                    "izgriešanas\nfrekvence 1200 apgr./min. Aprēķini "
                    "centrtieces paātrinājumu\nun izsaki to g vienībās!",
             dots=["R = 0,25 m", "n = 1200 apgr./min = 20 Hz"],
             jaaprekina=["a = ?", "a/g = ?"],
             formulas=["ω = 2πn", "a = ω²R"],
             aprekins=["1)  ω = 2 · 3,14 · 20 = 126 rad/s",
                       "2)  ω² = 1,58·10⁴ rad²/s²",
                       "3)  a = 1,58·10⁴ · 0,25 ≈ 3,9·10³ m/s² ≈ 400 g"],
             atbilde="a ≈ 3,9·10³ m/s² ≈ 400 g",
             piezime="Tāpēc ūdens tik efektīvi tiek izspiests no veļas."),
        dict(nr=5, virsraksts="Zobratu pārvads",
             teksts="Zobrats ar 20 zobiem griežas ar 600 apgr./min un\n"
                    "saķeras ar zobratu, kam ir 50 zobi.\n"
                    "Aprēķini otrā zobrata frekvenci!",
             dots=["z₁ = 20", "n₁ = 600 apgr./min", "z₂ = 50"],
             jaaprekina=["n₂ = ?"],
             formulas=["n₁z₁ = n₂z₂", "n₂ = n₁z₁/z₂"],
             aprekins=["1)  n₁z₁ = 600 · 20 = 12 000",
                       "2)  n₂ = 12 000 : 50",
                       "3)  n₂ = 240 apgr./min = 4,0 Hz"],
             atbilde="n₂ = 240 apgr./min = 4,0 Hz",
             piezime="Saķērušos zobratu saskares punktā lineārais ātrums "
                     "ir vienāds - tāpat kā siksnas pārvadā."),
        dict(nr=6, virsraksts="Centrifūga astronautiem",
             teksts="Centrifūgas rādiuss ir 8,0 m. Cik lielam jābūt "
                    "ātrumam,\nlai paātrinājums būtu 8g, un cik liels "
                    "tad ir periods?\n(g = 9,8 m/s²; π ≈ 3,14)",
             dots=["R = 8,0 m", "a = 8g = 78,4 m/s²"],
             jaaprekina=["v = ?", "T = ?"],
             formulas=["v = √(aR)", "T = 2πR/v"],
             aprekins=["1)  aR = 78,4 · 8,0 = 627 m²/s²",
                       "2)  v = √627 ≈ 25 m/s",
                       "3)  T = 6,28 · 8,0 : 25 ≈ 2,0 s"],
             atbilde="v ≈ 25 m/s ;   T ≈ 2,0 s",
             piezime="Viens apgrieziens divās sekundēs - un cilvēks jūtas "
                     "astoņas reizes smagāks."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Uz vienas ass ω vienāds; ar siksnu v vienāds.",
            "Pārnesumā ω₁R₁ = ω₂R₂.",
            "Drošs ātrums līkumā: v = √(aR).",
            "Centrifūgā paātrinājums var sasniegt simtiem g.",
        ],
        majasdarbs=[
            "R₁ = 10 cm, R₂ = 40 cm, n₁ = 600 apgr./min. Aprēķini n₂.",
            "R = 120 m, a = 3,0 m/s². Aprēķini drošu ātrumu.",
            "n = 3000 apgr./min, R = 0,10 m. Aprēķini a un a/g.",
        ],
        pasvertejums=["Protu risināt pārnesumu uzdevumus",
                      "Protu rēķināt drošu ātrumu",
                      "Protu kombinēt formulas",
                      "Protu pārbaudīt ticamību"],
        nakama="Nākamā stunda: temata nostiprināšana."),
),

dict(
    nr="2.13", virsraksts="Temata nostiprināšana",
    jautajums="Kuru vienādojumu izvēlēties?",
    apaksraksts="Atgādne · Formulu izvēle · PD3 formāts",
    merkis="Apkopot visu 2. temata saturu vienā atgādnē un nostiprināt "
           "formulu izvēli pirms PD3.",
    protu=["izvēlēties formulu pēc dotajiem lielumiem;",
           "risināt kombinētus kinemātikas uzdevumus;",
           "atpazīt kustības veidu pēc uzdevuma teksta;",
           "sagatavoties PD3."],
    atkartojums="Temats aptvēra: paātrinājumu, ātruma un kustības "
                "vienādojumus, brīvo krišanu, mešanu un kustību pa "
                "riņķa līniju.",
    uzdevumu_apraksts="Kombinēti uzdevumi PD3 formātā",
    teorija=[
        ("Temata atgādne", [
            ("formula", "VIENMĒRĪGI PAĀTRINĀTA KUSTĪBA",
             "v = v₀ + at   ·   s = v₀t + at²/2   ·   "
             "s = (v₀+v)/2 · t   ·   v² − v₀² = 2as",
             "Brīvā krišana: a = g = 9,8 m/s², v₀ = 0.  "
             "Mešana uz augšu: a = −g.", GOLD),
            ("formula", "KUSTĪBA PA RIŅĶA LĪNIJU",
             "T = t/N   ·   n = 1/T   ·   ω = 2π/T   ·   v = ωR   ·   "
             "a = v²/R = ω²R",
             "Riņķa kustībā paātrinājums vērsts uz centru un maina tikai "
             "ātruma virzienu.", GOLD),
        ]),
        ("Kā atpazīt uzdevuma veidu", [
            ("tabula",
             ["Uzdevuma pazīme", "Kustības veids", "Sākuma formula"],
             [["«no 0 līdz ... sekundēs»", "Paātrināta taisnvirziena",
               "a = Δv/t"],
              ["«bremzēšanas ceļš»", "Bremzēšana", "v² − v₀² = 2as"],
              ["«krīt no augstuma»", "Brīvā krišana", "h = gt²/2"],
              ["«met horizontāli»", "Horizontāla mešana", "t = √(2h/g)"],
              ["«apgriezieni minūtē»", "Riņķa kustība", "T = t/N"]],
             [4.60, 4.30, 3.33]),
            ("panelis", "PD3 FORMĀTS",
             ["Tests (10 p.); mērvienību un lielumu tabula (5 p.); divi "
              "aprēķinu uzdevumi ar pilnu pierakstu (10 p.); uzdevums ar "
              "apakšjautājumiem par grafiku vai riņķa kustību (5 p.). "
              "Kopā 30 punkti, 40 minūtes."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Formulas izvēle",
             teksts="Automašīna no 25 m/s apstājas 40 m ceļā.\n"
                    "Kuru formulu izvēlēsies un kāds ir paātrinājums?",
             dots=["v₀ = 25 m/s", "v = 0", "s = 40 m"],
             jaaprekina=["a = ?"],
             formulas=["Nav dots laiks → v² − v₀² = 2as"],
             aprekins=["1)  0 − 625 = 2 · a · 40",
                       "2)  −625 = 80a",
                       "3)  a = −7,8 m/s²"],
             atbilde="a ≈ −7,8 m/s² (bremzēšana)",
             piezime="Reāla ārkārtas bremzēšana uz sausa asfalta."),
        dict(nr=2, virsraksts="Kombinēts krišanas uzdevums",
             teksts="Ķermeni met vertikāli uz augšu ar 20 m/s no 15 m\n"
                    "augsta jumta. Aprēķini maksimālo augstumu virs "
                    "zemes! (g = 9,8 m/s²)",
             dots=["v₀ = 20 m/s", "h₀ = 15 m", "g = 9,8 m/s²"],
             jaaprekina=["H = ?"],
             formulas=["h(max) = v₀²/(2g)", "H = h₀ + h(max)"],
             aprekins=["1)  v₀² = 400 m²/s²",
                       "2)  h(max) = 400 : 19,6 = 20,4 m",
                       "3)  H = 15 + 20,4 = 35,4 ≈ 35 m"],
             atbilde="H ≈ 35 m virs zemes",
             piezime="Uzmanīgi: h(max) mēra no mešanas vietas, ne no "
                     "zemes."),
        dict(nr=3, virsraksts="Horizontāla mešana",
             teksts="No 45 m augstuma horizontāli izmet ķermeni ar "
                    "20 m/s.\nAprēķini lidojuma attālumu un ātrumu pie "
                    "zemes! (g = 9,8 m/s²)",
             dots=["h = 45 m", "v₀ = 20 m/s", "g = 9,8 m/s²"],
             jaaprekina=["L = ?", "v = ?"],
             formulas=["t = √(2h/g)", "L = v₀t", "v = √(v₀² + (gt)²)"],
             aprekins=["1)  t = √(90 : 9,8) = 3,03 s",
                       "2)  L = 20 · 3,03 ≈ 61 m",
                       "3)  v_y = 29,7 ;  v = √(400 + 882) ≈ 36 m/s"],
             atbilde="L ≈ 61 m ;   v ≈ 36 m/s",
             piezime="Vispirms laiks, tad attālums, tad ātrums - "
                     "vienmēr šādā secībā."),
        dict(nr=4, virsraksts="Riņķa kustība",
             teksts="Ritenis ar rādiusu 0,30 m griežas ar 240 apgr./min.\n"
                    "Aprēķini lineāro ātrumu un centrtieces "
                    "paātrinājumu! (π ≈ 3,14)",
             dots=["R = 0,30 m", "n = 240 apgr./min = 4,0 Hz"],
             jaaprekina=["v = ?", "a = ?"],
             formulas=["v = 2πRn", "a = v²/R"],
             aprekins=["1)  n = 240 : 60 = 4,0 Hz",
                       "2)  v = 2 · 3,14 · 0,30 · 4,0 = 7,5 m/s",
                       "3)  a = 56,7 : 0,30 ≈ 189 m/s² ≈ 19 g"],
             atbilde="v ≈ 7,5 m/s ;   a ≈ 1,9·10² m/s²",
             piezime="Pārbaude ar ω: ω = 2πn = 25,1 rad/s; "
                     "a = ω²R = 189 m/s² ✔"),
        dict(nr=5, virsraksts="Ceļš caur vidējo ātrumu",
             teksts="Ķermenis sāk kustību ar 10 m/s un paātrinās ar\n"
                    "2,0 m/s² 8,0 s. Aprēķini gala ātrumu un ceļu!",
             dots=["v₀ = 10 m/s", "a = 2,0 m/s²", "t = 8,0 s"],
             jaaprekina=["v = ?", "s = ?"],
             formulas=["v = v₀ + at", "s = (v₀ + v)/2 · t"],
             aprekins=["1)  v = 10 + 2,0 · 8,0 = 26 m/s",
                       "2)  (v₀ + v)/2 = 18 m/s",
                       "3)  s = 18 · 8,0 = 144 m"],
             atbilde="v = 26 m/s ;   s = 144 m",
             piezime="Pārbaude: s = 10·8 + 2·64:2 = 80 + 64 = 144 m ✔"),
        dict(nr=6, virsraksts="Divi reizes vienā augstumā",
             teksts="Ķermeni met vertikāli uz augšu ar 25 m/s.\n"
                    "Kuros brīžos tas atrodas 20 m augstumā? "
                    "(g = 9,8 m/s²)",
             dots=["v₀ = 25 m/s", "h = 20 m", "g = 9,8 m/s²"],
             jaaprekina=["t₁ = ?", "t₂ = ?"],
             formulas=["h = v₀t − gt²/2", "4,9t² − 25t + 20 = 0"],
             aprekins=["1)  D = 625 − 4·4,9·20 = 233",
                       "2)  √D = 15,3",
                       "3)  t = (25 ± 15,3) : 9,8 → t₁ ≈ 1,0 s ;  "
                       "t₂ ≈ 4,1 s"],
             atbilde="t₁ ≈ 1,0 s (augšup) ;   t₂ ≈ 4,1 s (lejup)",
             piezime="Divas saknes ir fizikāli pamatotas: augstumu ķermenis "
                     "šķērso divreiz."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Formulu izvēlas pēc lieluma, kas nav ne dots, ne meklēts.",
            "Brīvā krišana un mešana ir tā pati paātrinātā kustība ar "
            "a = g.",
            "Horizontālā mešanā vispirms atrod laiku.",
            "Riņķa kustībā a = v²/R vienmēr vērsts uz centru.",
        ],
        majasdarbs=[
            "Atkārto abas atgādnes pirms PD3.",
            "Izpildi pa vienam uzdevumam no katra veida.",
            "Pārskati LD2 protokolu un g aprēķinu.",
        ],
        pasvertejums=["Protu izvēlēties formulu",
                      "Protu risināt krišanas uzdevumus",
                      "Protu risināt riņķa kustības uzdevumus",
                      "Esmu gatavs PD3"],
        nakama="Nākamā stunda: PD3 - vienmērīgi paātrināta kustība."),
),

dict(
    nr="2.14", virsraksts="Kļūdu analīze un treniņš",
    jautajums="Kā izvairīties no tipiskajām kļūdām?",
    apaksraksts="PD3 kļūdas · Labošana · Pāreja uz dinamiku",
    merkis="Analizēt PD3 kļūdas, izlabot tipiskākās un sagatavoties "
           "3. tematam par spēkiem.",
    protu=["atpazīt savu kļūdas veidu;",
           "izlabot risinājumu ar pilnu pierakstu;",
           "papildināt personīgo atgādni;",
           "saistīt kinemātiku ar nākamo tematu."],
    atkartojums="PD3 ir uzrakstīts. Šī stunda pārvērš kļūdas prasmēs un "
                "pārmet tiltu uz 3. tematu - spēkiem.",
    uzdevumu_apraksts="Kļūdainu risinājumu labošana",
    teorija=[
        ("Biežākās PD3 kļūdas", [
            ("tabula",
             ["Kļūda", "Kā izskatās", "Pareizi"],
             [["a/2 vietā a", "x = x₀ + v₀t + at²",
               "x = x₀ + v₀t + at²/2"],
              ["Sajaukta g zīme", "h = v₀t + gt²/2 uz augšu",
               "y = v₀t − gt²/2"],
              ["Mešanas laiks no v₀", "t = √(2h/g) atkarīgs no v₀",
               "t nav atkarīgs no v₀"],
              ["a = 0 riņķa kustībā", "«v nemainās, tātad a = 0»",
               "a = v²/R ≠ 0"]],
             [3.60, 4.60, 4.03]),
            ("panelis", "PĀRBAUDES PAŅĒMIENS",
             ["Katru atbildi pārbaudi ar mērvienībām un ar otru formulu.",
              "s = v₀t + at²/2",
              "s = (v₀ + v)/2 · t",
              "Ja abas formulas dod vienu rezultātu, risinājums "
              "visdrīzāk ir pareizs."], NAVY),
        ]),
        ("Tilts uz 3. tematu", [
            ("divi",
             ("KINEMĀTIKA (2. temats)", BLUE,
              ["Apraksta, KĀ ķermenis kustas.",
               "Lielumi: s, v, a, t.",
               "Neinteresē, kāpēc."]),
             ("DINAMIKA (3. temats)", GREEN,
              ["Skaidro, KĀPĒC ķermenis kustas.",
               "Pievienojas: F, m.",
               "Galvenā sakarība: F = ma."])),
            ("formula", "SAVIENOJOŠĀ SAKARĪBA",
             "F = m · a",
             "Viss, ko iemācījāmies par paātrinājumu, tagad savienosies "
             "ar spēku. Paātrinājums vairs nebūs dots - to rēķināsim no "
             "spēkiem.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atrodi kļūdu I",
             teksts="«x = 5 + 4t + 3t²; tātad a = 3 m/s².»\n"
                    "Atrodi un izlabo kļūdu!",
             dots=["x = 5 + 4t + 3t²"],
             jaaprekina=["a = ?"],
             formulas=["x = x₀ + v₀t + at²/2"],
             aprekins=["1)  Koeficients pie t² ir a/2, nevis a",
                       "2)  a/2 = 3",
                       "3)  a = 6,0 m/s²"],
             atbilde="a = 6,0 m/s², nevis 3 m/s².",
             piezime="Šī kļūda PD darbos ir visbiežākā - vienmēr "
                     "pārbaudi koeficientu."),
        dict(nr=2, virsraksts="Atrodi kļūdu II",
             teksts="«Ķermeni met horizontāli ar 30 m/s no 20 m. Tā kā\n"
                    "ātrums ir liels, tas krīt ilgāk nekā vienkārši "
                    "nomests.»\nIzvērtē apgalvojumu!",
             dots=["h = 20 m", "v₀ = 30 m/s"],
             jaaprekina=["Vai apgalvojums pareizs?"],
             formulas=["t = √(2h/g) - nav atkarīgs no v₀"],
             aprekins=["1)  Vertikālā kustība ir brīvā krišana",
                       "2)  t = √(40 : 9,8) = 2,0 s",
                       "3)  Tāds pats laiks arī nomestam ķermenim"],
             atbilde="Apgalvojums nepareizs: krišanas laiks nav atkarīgs "
                     "no horizontālā ātruma.",
             piezime="Kustību neatkarības princips - pamatideja visā "
                     "mešanas tēmā."),
        dict(nr=3, virsraksts="Atrodi kļūdu III",
             teksts="«Karuselis griežas ar nemainīgu ātrumu, tātad\n"
                    "paātrinājums ir nulle.»\nIzlabo un pamato!",
             dots=["v = const", "kustība pa riņķi"],
             jaaprekina=["a = ?"],
             formulas=["a = v²/R"],
             aprekins=["1)  Nemainīgs ir tikai ātruma MODULIS",
                       "2)  Virziens mainās nepārtraukti",
                       "3)  a = v²/R ≠ 0, vērsts uz centru"],
             atbilde="Paātrinājums nav nulle: a = v²/R, vērsts uz centru.",
             piezime="Paātrinājums ir ātruma VEKTORA, nevis moduļa "
                     "izmaiņa."),
        dict(nr=4, virsraksts="Atrodi kļūdu IV",
             teksts="«v₀ = 20 m/s, a = −5,0 m/s², t = 6,0 s;\n"
                    "v = 20 − 30 = −10 m/s, tātad automašīna brauc "
                    "atpakaļ.»\nIzvērtē risinājumu!",
             dots=["v₀ = 20 m/s", "a = −5,0 m/s²", "t = 6,0 s"],
             jaaprekina=["t(apstāšanās) = ?", "kļūda = ?"],
             formulas=["v = v₀ + at", "0 = v₀ + at"],
             aprekins=["1)  0 = 20 − 5t → t = 4,0 s",
                       "2)  Pēc 4,0 s automašīna apstājas",
                       "3)  Formulu 6 sekundēm lietot nedrīkst"],
             atbilde="Automašīna apstājas pēc 4,0 s; atpakaļ tā "
                     "nebrauc.",
             piezime="Vienmēr pārbaudi, vai laiks nepārsniedz apstāšanās "
                     "brīdi."),
        dict(nr=5, virsraksts="Atrodi kļūdu V",
             teksts="«Ķermenis krīt 3,0 s: h = 9,8 · 9 : 2 = 44 m,\n"
                    "tātad ātrums pie zemes v = 44 : 3,0 = 14,7 m/s.»\n"
                    "Izlabo risinājumu!",
             dots=["t = 3,0 s", "h = 44 m", "g = 9,8 m/s²"],
             jaaprekina=["v = ?"],
             formulas=["v = gt", "v(vid) = h/t"],
             aprekins=["1)  h/t dod VIDĒJO ātrumu, ne gala ātrumu",
                       "2)  v(vid) = 14,7 m/s - tas ir pareizi",
                       "3)  Gala ātrums v = 9,8 · 3,0 = 29,4 m/s"],
             atbilde="v = 29,4 m/s; 14,7 m/s ir vidējais ātrums.",
             piezime="Paātrinātā kustībā gala ātrums ir tieši divreiz "
                     "lielāks par vidējo, ja v₀ = 0."),
        dict(nr=6, virsraksts="Atrodi kļūdu VI",
             teksts="«a = v²/R; ja rādiusu palielina 2 reizes,\n"
                    "centrtieces paātrinājums arī palielinās 2 reizes.»\n"
                    "Izlabo un pamato!",
             dots=["R₂ = 2R₁", "v nemainās"],
             jaaprekina=["a₂/a₁ = ?"],
             formulas=["a = v²/R"],
             aprekins=["1)  R ir SAUCĒJĀ",
                       "2)  a₂ = v²/(2R₁) = ½ · v²/R₁",
                       "3)  a₂ / a₁ = 0,5"],
             atbilde="Paātrinājums SAMAZINĀS 2 reizes, nevis palielinās.",
             piezime="Pirms secinājuma vienmēr paskaties, vai lielums ir "
                     "skaitītājā vai saucējā."),
        dict(nr=7, virsraksts="Atgādnes papildināšana",
             teksts="Papildini personīgo atgādni ar 2. temata "
                    "sakarībām\nun divām kļūdām, no kurām jāizvairās!",
             dots=["PD3 rezultāti"],
             jaaprekina=["atgādne = ?"],
             formulas=["Personīgs saraksts"],
             aprekins=["1)  Sakarības: v = v₀ + at; s = v₀t + at²/2;",
                       "     v² − v₀² = 2as; a = v²/R",
                       "2)  Kļūdas: a/2 pie t²; a = 0 riņķa kustībā"],
             atbilde="Atgādne papildināta ar 4 sakarībām un 2 kļūdām.",
             piezime="Nākamajā tematā atgādne kļūs vēl garāka - tāpēc "
                     "raksti kompakti."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Koeficients pie t² kustības vienādojumā ir a/2.",
            "Krišanas laiks nav atkarīgs no horizontālā ātruma.",
            "Riņķa kustībā paātrinājums nav nulle.",
            "Katru atbildi vērts pārbaudīt ar otru formulu.",
        ],
        majasdarbs=[
            "Izlabo savas PD3 kļūdas pilnā pierakstā.",
            "Papildini personīgo atgādni.",
            "Atkārto vektoru saskaitīšanu - 3. tematā tā būs vajadzīga "
            "katrā stundā.",
        ],
        pasvertejums=["Protu atpazīt savu kļūdu",
                      "Protu izlabot risinājumu",
                      "Protu pārbaudīt ar otru formulu",
                      "Esmu gatavs 3. tematam"],
        nakama="Nākamais temats: mijiedarbība un spēks."),
),

]
