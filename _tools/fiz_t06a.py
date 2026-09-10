# -*- coding: utf-8 -*-
"""6. temats "Mehāniskās svārstības un viļņi". A daļa: 6.1.-6.4. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "6. temats. Mehāniskās svārstības un viļņi"
KICKER = "FIZIKA I · 11. KLASE · 6. TEMATS: SVĀRSTĪBAS UN VIĻŅI"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/6. Mehāniskās svārstības un viļņi"

STUNDAS = [

dict(
    nr="6.1", virsraksts="Svārstības un rezonanse",
    jautajums="Kāpēc šūpoles var iešūpot arvien augstāk?",
    apaksraksts="Amplitūda · T = t/N · f = 1/T · Rezonanse",
    merkis="Atpazīt svārstību raksturlielumus un ar piemēru izskaidrot "
           "rezonansi.",
    protu=["nosaukt amplitūdu, periodu un frekvenci;",
           "aprēķināt T = t/N un f = 1/T;",
           "nolasīt amplitūdu un periodu no grafika;",
           "izskaidrot rezonansi ar piemēru."],
    atkartojums="10. klasē riņķa kustībā jau lietojām periodu un "
                "frekvenci. Svārstībās tie ir tie paši lielumi - tikai "
                "kustība notiek turp un atpakaļ.",
    uzdevumu_apraksts="Periods, frekvence un rezonanse",
    teorija=[
        ("Svārstību raksturlielumi", [
            ("formula", "PERIODS UN FREKVENCE",
             "T = t/N        f = 1/T        [T] = s,  [f] = herci (Hz)",
             "N ir svārstību skaits laikā t. Periods un frekvence ir "
             "apgriezti lielumi: jo biežākas svārstības, jo īsāks "
             "periods.", GOLD),
            ("kartitas", [
                ("AMPLITŪDA A", BLUE,
                 ["Lielākā novirze no",
                  "līdzsvara stāvokļa.",
                  "Mēra metros."]),
                ("PERIODS T", GREEN,
                 ["Viena pilna svārstība.",
                  "Mēra sekundēs.",
                  "T = t/N."]),
                ("FREKVENCE f", GOLD,
                 ["Svārstības sekundē.",
                  "Mēra hercos.",
                  "f = 1/T."]),
            ]),
        ]),
        ("Rezonanse", [
            ("divi",
             ("BRĪVĀS SVĀRSTĪBAS", BLUE,
              ["Notiek pēc viena grūdiena.",
               "Frekvenci nosaka pati sistēma.",
               "Berze amplitūdu samazina.",
               "Piemērs: atlaistas šūpoles."]),
             ("UZSPIESTĀS SVĀRSTĪBAS", GREEN,
              ["Uztur ārējs periodisks spēks.",
               "Frekvenci nosaka spēks.",
               "Amplitūda nesarūk.",
               "Piemērs: stumtas šūpoles."])),
            ("panelis", "REZONANSE - KAD FREKVENCES SAKRĪT",
             ["Ja ārējā spēka frekvence sakrīt ar sistēmas brīvo "
              "svārstību frekvenci, amplitūda strauji pieaug. Tā šūpoles "
              "iešūpo, stumjot tieši īstajā brīdī.",
              "Noderīgi: mūzikas instrumenti, mikroviļņu krāsns, radio "
              "uztvērēja noskaņošana.",
              "Bīstami: tilta šūpošanās soļu ritmā, ēku svārstības "
              "zemestrīcē - tāpēc pa tiltu kareivji iet bez soļa."], NAVY),
        ]),
        ("Svārstības ap mums", [
            ("tabula",
             ["Kas svārstās", "Periods T", "Frekvence f"],
             [["Šūpoles", "2,0 s", "0,50 Hz"],
              ["Pulksteņa svārsts", "2,0 s", "0,50 Hz"],
              ["Ģitāras stīga (la)", "0,0023 s", "440 Hz"],
              ["Cilvēka sirds mierā", "0,80 s", "1,25 Hz"]],
             [4.60, 3.80, 3.83]),
            ("panelis", "KO JAU ZINI NO PAMATSKOLAS - PĀRBAUDI SEVI",
             ["1. Kurš lielums rāda svārstību skaitu sekundē?",
              "2. Ja periods ir 0,50 s, cik liela ir frekvence?",
              "3. Kas notiek ar amplitūdu, ja šūpoles vairs nestumj?",
              "4. Nosauc vienu rezonanses piemēru no ikdienas."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Periods no svārstību skaita",
             teksts="Svārsts 60 s laikā veic 30 pilnas svārstības.\n"
                    "Aprēķini periodu un frekvenci!",
             dots=["t = 60 s", "N = 30"],
             jaaprekina=["T = ?", "f = ?"],
             formulas=["T = t/N", "f = 1/T"],
             aprekins=["1)  T = 60 : 30 = 2,0 s",
                       "2)  f = 1 : 2,0 = 0,50 Hz"],
             atbilde="T = 2,0 s;  f = 0,50 Hz",
             piezime="Pārbaudi: 0,50 svārstības sekundē · 60 s = 30 "
                     "svārstības."),
        dict(nr=2, virsraksts="Periods no frekvences",
             teksts="Elektrotīkla maiņstrāvas frekvence ir 50 Hz.\n"
                    "Cik ilgs ir viens periods?",
             dots=["f = 50 Hz"],
             jaaprekina=["T = ?"],
             formulas=["f = 1/T", "T = 1/f"],
             aprekins=["1)  T = 1 : 50",
                       "2)  T = 0,02 s = 20 ms"],
             atbilde="T = 0,02 s",
             piezime="20 milisekundes - tik ātri acs izmaiņas vairs "
                     "nepamana."),
        dict(nr=3, virsraksts="Grafika nolasīšana",
             teksts="Svārstību grafikā lielākā novirze ir 4,0 cm, un\n"
                    "viena pilna svārstība aizņem 0,8 s. Nosaki\n"
                    "amplitūdu, frekvenci un svārstību skaitu 1 min!",
             dots=["A = 4,0 cm = 0,04 m", "T = 0,8 s", "t = 1 min = 60 s"],
             jaaprekina=["f = ?", "N = ?"],
             formulas=["f = 1/T", "N = t/T"],
             aprekins=["1)  A = 0,04 m (lielākā novirze)",
                       "2)  f = 1 : 0,8 = 1,25 Hz",
                       "3)  N = 60 : 0,8 = 75 svārstības"],
             atbilde="A = 0,04 m;  f = 1,25 Hz;  N = 75",
             piezime="Amplitūdu nolasa no grafika augstuma, periodu - no "
                     "attāluma starp diviem vienādiem punktiem."),
        dict(nr=4, virsraksts="Rezonanse uz tilta",
             teksts="Gājēju tilta brīvo svārstību frekvence ir 1,5 Hz.\n"
                    "Ar kādu soļu periodu kareivju grupa izraisītu\n"
                    "rezonansi?",
             dots=["f₀ = 1,5 Hz", "Rezonanse: f = f₀"],
             jaaprekina=["T = ?"],
             formulas=["Rezonansē: f = f₀", "T = 1/f"],
             aprekins=["1)  Rezonansē soļu frekvence f = 1,5 Hz",
                       "2)  T = 1 : 1,5 ≈ 0,67 s",
                       "3)  Solis ik pēc 0,67 s tiltu iešūpotu"],
             atbilde="T ≈ 0,67 s",
             piezime="Tieši tāpēc pa tiltu kareivji iet bez soļa - lai "
                     "frekvences nesakristu."),
        dict(nr=5, virsraksts="Svārsta periods no garuma",
             teksts="Matemātiskā svārsta garums ir 0,25 m.\n"
                    "Aprēķini periodu un frekvenci! (g = 9,8 m/s²; "
                    "π = 3,14)",
             dots=["l = 0,25 m", "g = 9,8 m/s²"],
             jaaprekina=["T = ?", "f = ?"],
             formulas=["T = 2π√(l/g)", "f = 1/T"],
             aprekins=["1)  T = 2π√(l/g)",
                       "2)  T = 2 · 3,14 · √(0,25 / 9,8)",
                       "3)  T ≈ 1,0 s",
                       "4)  f = 1 : 1,0 ≈ 1,0 Hz"],
             atbilde="T ≈ 1,0 s;  f ≈ 1,0 Hz",
             piezime="Periodu nosaka tikai garums un g - svārsta masa "
                     "to neietekmē."),
        dict(nr=6, virsraksts="Svārstību skaits",
             teksts="Kamertonis skan ar frekvenci 440 Hz.\n"
                    "Cik pilnas svārstības tas veic 0,50 s laikā?",
             dots=["f = 440 Hz", "t = 0,50 s"],
             jaaprekina=["N = ?"],
             formulas=["T = t/N", "N = f · t"],
             aprekins=["1)  N = f · t",
                       "2)  N = 440 · 0,50",
                       "3)  N = 220"],
             atbilde="N = 220 svārstības",
             piezime="Frekvence jau ir svārstību skaits vienā "
                     "sekundē - tāpēc pietiek to reizināt ar laiku."),
        dict(nr=7, virsraksts="Atsperes svārstības",
             teksts="Pie atsperes (k = 80 N/m) piekārts 0,20 kg "
                    "atsvars.\nAprēķini svārstību periodu un frekvenci! "
                    "(π = 3,14)",
             dots=["k = 80 N/m", "m = 0,20 kg"],
             jaaprekina=["T = ?", "f = ?"],
             formulas=["T = 2π√(m/k)", "f = 1/T"],
             aprekins=["1)  T = 2π√(m/k)",
                       "2)  T = 2 · 3,14 · √(0,20 / 80)",
                       "3)  T ≈ 0,31 s",
                       "4)  f = 1 : 0,31 ≈ 3,2 Hz"],
             atbilde="T ≈ 0,31 s;  f ≈ 3,2 Hz",
             piezime="Atsperes svārstam masa ir svarīga - atšķirībā no "
                     "matemātiskā svārsta."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Amplitūda ir lielākā novirze no līdzsvara stāvokļa.",
            "T = t/N;  f = 1/T;  frekvenci mēra hercos.",
            "Brīvās svārstības uztur pati sistēma, uzspiestās - ārējs "
            "spēks.",
            "Rezonansē frekvences sakrīt un amplitūda strauji pieaug.",
        ],
        majasdarbs=[
            "t = 45 s, N = 15. Aprēķini T un f.",
            "f = 25 Hz. Aprēķini periodu.",
            "Uzraksti divus rezonanses piemērus: vienu noderīgu, vienu "
            "bīstamu.",
        ],
        pasvertejums=["Protu nosaukt A, T un f",
                      "Protu rēķināt T un f",
                      "Protu lasīt svārstību grafiku",
                      "Protu izskaidrot rezonansi"],
        nakama="Nākamā stunda: mehāniskie viļņi un skaņa."),
),

dict(
    nr="6.2", virsraksts="Mehāniskie viļņi un skaņa",
    jautajums="Kas pārvietojas vilnī?",
    apaksraksts="Šķērsviļņi · Garenviļņi · Augstums un skaļums",
    merkis="Atšķirt šķērsviļņus un garenviļņus un saistīt skaņas augstumu "
           "ar frekvenci, bet skaļumu ar amplitūdu.",
    protu=["izskaidrot, ka vilnis pārnes enerģiju, nevis vielu;",
           "atšķirt šķērsviļņus un garenviļņus;",
           "saistīt skaņas augstumu ar frekvenci;",
           "saistīt skaļumu ar amplitūdu."],
    atkartojums="Iepriekšējā stundā viena daļiņa svārstījās ap līdzsvara "
                "stāvokli. Ja daļiņas ir saistītas, svārstības pārnesas "
                "tālāk - tā rodas vilnis.",
    uzdevumu_apraksts="Skaņas izplatīšanās un raksturlielumi",
    teorija=[
        ("Vilnis pārnes enerģiju", [
            ("panelis", "KAS VILNĪ PĀRVIETOJAS",
             ["Vilnī pārvietojas svārstības un enerģija, nevis pati "
              "viela. Ūdenī peldošs korķis vilnī paceļas un nolaižas, "
              "bet uz krastu neaizpeld.",
              "Mehāniskajiem viļņiem vajadzīga vide: gaiss, ūdens vai "
              "cietviela. Vakuumā skaņa neizplatās."], NAVY),
            ("divi",
             ("ŠĶĒRSVILNIS", BLUE,
              ["Daļiņas svārstās PERPENDIKULĀRI",
               "izplatīšanās virzienam.",
               "Redz kalnus un ielejas.",
               "Piemēri: vilnis virvē, ūdens",
               "virsmas vilnis."]),
             ("GARENVILNIS", GREEN,
              ["Daļiņas svārstās PA",
               "izplatīšanās virzienu.",
               "Veido sabiezinājumus un",
               "retinājumus.",
               "Piemērs: skaņa gaisā."])),
        ]),
        ("Skaņa", [
            ("tabula",
             ["Vide", "Skaņas ātrums", "Kāpēc tā"],
             [["Gaiss (20 °C)", "340 m/s", "Daļiņas tālu viena no otras"],
              ["Ūdens", "1500 m/s", "Daļiņas izvietotas blīvāk"],
              ["Tērauds", "5000 m/s", "Stingras saites starp daļiņām"],
              ["Vakuums", "neizplatās", "Nav daļiņu, kas nodotu tālāk"]],
             [3.60, 3.00, 5.63]),
            ("panelis", "AUGSTUMS, SKAĻUMS UN DZIRDAMĪBA",
             ["Skaņas augstumu nosaka FREKVENCE: lielāka frekvence - "
              "augstāka skaņa.",
              "Skaļumu nosaka AMPLITŪDA: lielāka amplitūda - skaļāka "
              "skaņa.",
              "Cilvēks dzird no 20 Hz līdz 20 000 Hz. Zemāk ir "
              "infraskaņa, augstāk - ultraskaņa, ko izmanto sonāros un "
              "medicīnas izmeklējumos."], BLUE),
        ]),
        ("Infraskaņa, dzirdamā skaņa un ultraskaņa", [
            ("kartitas", [
                ("INFRASKAŅA", BLUE,
                 ["Zem 20 Hz.",
                  "Cilvēks nedzird.",
                  "Zemestrīces, vulkāni,",
                  "vaļi un ziloņi."]),
                ("DZIRDAMĀ SKAŅA", GREEN,
                 ["20 Hz - 20 000 Hz.",
                  "Runa: 100-3000 Hz.",
                  "Ar gadiem augšējā",
                  "robeža pazeminās."]),
                ("ULTRASKAŅA", GOLD,
                 ["Virs 20 000 Hz.",
                  "Sikspārņi, delfīni.",
                  "Sonārs, medicīna,",
                  "materiālu pārbaude."]),
            ]),
            ("panelis", "KĀPĒC ULTRASKAŅA NODER TIEŠI IZMEKLĒJUMOS",
             ["Jo augstāka frekvence, jo īsāks viļņa garums - un jo "
              "sīkākas detaļas vilnis spēj atšķirt.",
              "Ultraskaņa nav jonizējošs starojums, tāpēc izmeklējums ir "
              "drošs arī grūtniecības laikā.",
              "To pašu principu izmanto sonāros un metināto šuvju "
              "pārbaudē - vilnis atstarojas no defekta."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Cik tālu ir negaiss",
             teksts="Zibens tiek ieraudzīts, un pēc 6,0 s atskan pērkons.\n"
                    "Cik tālu ir negaiss? (v = 340 m/s)",
             dots=["t = 6,0 s", "v = 340 m/s"],
             jaaprekina=["s = ?"],
             formulas=["s = vt"],
             aprekins=["1)  s = 340 · 6,0",
                       "2)  s = 2040 m ≈ 2,0 km"],
             atbilde="s ≈ 2,0 km",
             piezime="Gaismas ceļa laiku neņem vērā - gaisma šo attālumu "
                     "veic gandrīz acumirklī."),
        dict(nr=2, virsraksts="Atbalss",
             teksts="Kliedziens atstarojas no klints, un atbalsi dzird\n"
                    "pēc 1,2 s. Cik tālu ir klints? (v = 340 m/s)",
             dots=["t = 1,2 s", "v = 340 m/s"],
             jaaprekina=["s = ?"],
             formulas=["Skaņa iet turp un atpakaļ", "s = vt/2"],
             aprekins=["1)  Viss ceļš: 340 · 1,2 = 408 m",
                       "2)  Līdz klintij: 408 : 2",
                       "3)  s = 204 m"],
             atbilde="s = 204 m",
             piezime="Tipiskā kļūda - aizmirst dalīt ar 2. Skaņa šo "
                     "attālumu noiet divreiz."),
        dict(nr=3, virsraksts="Sonārs",
             teksts="Kuģa sonāra signāls atgriežas no jūras dibena pēc\n"
                    "0,80 s. Cik dziļa ir jūra? (v = 1500 m/s)",
             dots=["t = 0,80 s", "v = 1500 m/s"],
             jaaprekina=["h = ?"],
             formulas=["h = vt/2"],
             aprekins=["1)  Viss ceļš: 1500 · 0,80 = 1200 m",
                       "2)  Dziļums: 1200 : 2",
                       "3)  h = 600 m"],
             atbilde="h = 600 m",
             piezime="Ūdenī skaņa iet gandrīz 4,5 reizes ātrāk nekā "
                     "gaisā."),
        dict(nr=4, virsraksts="Dzirdamības robežas",
             teksts="Sikspārnis izstaro signālu ar frekvenci 45 kHz,\n"
                    "vaļa sauciens ir 15 Hz. Vai cilvēks tos dzird un\n"
                    "kā šīs skaņas sauc?",
             dots=["f₁ = 45 kHz = 45 000 Hz", "f₂ = 15 Hz",
                   "Dzirde: 20 Hz - 20 000 Hz"],
             jaaprekina=["Dzirdamība = ?"],
             formulas=["Dzirdams, ja 20 Hz ≤ f ≤ 20 000 Hz"],
             aprekins=["1)  45 000 Hz > 20 000 Hz - ultraskaņa",
                       "2)  15 Hz < 20 Hz - infraskaņa",
                       "3)  Nevienu no tiem cilvēks nedzird"],
             atbilde="Abas ir ārpus dzirdes robežām",
             piezime="Ultraskaņu izmanto sonāros un medicīnā, infraskaņu "
                     "izstaro zemestrīces un lieli dzīvnieki."),
        dict(nr=5, virsraksts="Skaņas ātruma noteikšana",
             teksts="Skaņa 680 m attālumu veic 2,0 s laikā.\n"
                    "Aprēķini skaņas ātrumu!",
             dots=["s = 680 m", "t = 2,0 s"],
             jaaprekina=["v = ?"],
             formulas=["v = s/t"],
             aprekins=["1)  v = 680 : 2,0",
                       "2)  v = 340 m/s",
                       "3)  Tas atbilst tabulas vērtībai gaisā"],
             atbilde="v = 340 m/s",
             piezime="Skaņas ātrums gaisā mainās ar temperatūru - "
                     "0 °C tas ir 331 m/s."),
        dict(nr=6, virsraksts="Signāls pa sliedēm un pa gaisu",
             teksts="Pa sliedēm (v = 5000 m/s) un pa gaisu "
                    "(v = 340 m/s)\nskaņa veic 850 m. Aprēķini abus "
                    "laikus un to starpību!",
             dots=["s = 850 m", "v₁ = 5000 m/s", "v₂ = 340 m/s"],
             jaaprekina=["t₁ = ?", "t₂ = ?", "Δt = ?"],
             formulas=["t = s/v"],
             aprekins=["1)  t₁ = 850 : 5000 = 0,17 s",
                       "2)  t₂ = 850 : 340 = 2,5 s",
                       "3)  Δt = 2,5 − 0,17 ≈ 2,3 s"],
             atbilde="t₁ = 0,17 s;  t₂ = 2,5 s;  Δt ≈ 2,3 s",
             piezime="Tāpēc, pieliekot ausi pie sliedēm, vilcienu dzird "
                     "daudz agrāk."),
        dict(nr=7, virsraksts="Ultraskaņas defektoskops",
             teksts="Ultraskaņas signāls tērauda detaļā (v = 5000 m/s)\n"
                    "atgriežas no plaisas pēc 2,0·10⁻⁵ s.\n"
                    "Cik dziļi ir plaisa?",
             dots=["t = 2,0·10⁻⁵ s", "v = 5000 m/s"],
             jaaprekina=["h = ?"],
             formulas=["h = vt/2"],
             aprekins=["1)  Viss ceļš: 5000 · 2,0·10⁻⁵ = 0,10 m",
                       "2)  Līdz plaisai: 0,10 : 2",
                       "3)  h = 0,05 m = 5,0 cm"],
             atbilde="h = 5,0 cm",
             piezime="Tā pati atbalss ideja, tikai metālā un ar "
                     "mikrosekundēm."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vilnis pārnes enerģiju, nevis vielu.",
            "Šķērsvilnī daļiņas svārstās perpendikulāri, garenvilnī - pa "
            "izplatīšanās virzienu.",
            "Skaņa gaisā ir garenvilnis; vakuumā tā neizplatās.",
            "Augstumu nosaka frekvence, skaļumu - amplitūda.",
        ],
        majasdarbs=[
            "Pērkons dzirdams pēc 4,5 s. Cik tālu ir negaiss?",
            "Atbalss atgriežas pēc 2,0 s. Cik tālu ir siena?",
            "Uzraksti pa vienam šķērsviļņa un garenviļņa piemēram.",
        ],
        pasvertejums=["Zinu, ka vilnis pārnes enerģiju",
                      "Protu atšķirt viļņu veidus",
                      "Protu rēķināt skaņas ceļu",
                      "Zinu dzirdes robežas"],
        nakama="Nākamā stunda: viļņu raksturlielumi un sakarība v = λf."),
),

dict(
    nr="6.3", virsraksts="Viļņu raksturlielumi",
    jautajums="Kā saistīti viļņa garums, frekvence un ātrums?",
    apaksraksts="v = λf · λ = v/f · λ = vT",
    merkis="Iemācīties lietot sakarību v = λf viena un divu soļu "
           "uzdevumos.",
    protu=["nosaukt viļņa garumu un tā mērvienību;",
           "lietot v = λf un λ = v/f;",
           "saistīt viļņa garumu ar periodu: λ = vT;",
           "izskaidrot, kas mainās, vilnim pārejot citā vidē."],
    atkartojums="Iepriekš mācījāmies periodu un frekvenci. Tagad "
                "pievienojam viļņa garumu - attālumu, ko vilnis noiet "
                "viena perioda laikā.",
    uzdevumu_apraksts="Viļņa garums, frekvence un ātrums",
    teorija=[
        ("Viļņa pamatsakarība", [
            ("formula", "VIĻŅA GARUMS",
             "v = λ · f        λ = v/f        λ = vT        [λ] = m",
             "Viļņa garums λ ir attālums starp diviem tuvākajiem vienādi "
             "svārstošiem punktiem - to vilnis noiet viena perioda "
             "laikā.", GOLD),
            ("kartitas", [
                ("λ - VIĻŅA GARUMS", BLUE,
                 ["Attālums starp diviem",
                  "kalniem vai ielejām.",
                  "Mēra metros."]),
                ("f - FREKVENCE", GREEN,
                 ["To nosaka avots.",
                  "Citā vidē nemainās.",
                  "Mēra hercos."]),
                ("v - ĀTRUMS", GOLD,
                 ["To nosaka vide.",
                  "Gaisā 340 m/s.",
                  "Mēra metros sekundē."]),
            ]),
        ]),
        ("Vilnis citā vidē", [
            ("tabula",
             ["Vilnis", "Ātrums", "Frekvence", "Viļņa garums"],
             [["Skaņa gaisā", "340 m/s", "340 Hz", "1,0 m"],
              ["Skaņa ūdenī", "1500 m/s", "340 Hz", "4,4 m"],
              ["Radiovilnis", "3·10⁸ m/s", "100 MHz", "3,0 m"],
              ["Ūdens vilnis", "2,0 m/s", "0,50 Hz", "4,0 m"]],
             [3.20, 2.60, 2.60, 3.83]),
            ("panelis", "KAS MAINĀS, PĀREJOT CITĀ VIDĒ",
             ["Frekvenci nosaka avots, tāpēc, pārejot citā vidē, tā "
              "NEMAINĀS.",
              "Ātrumu nosaka vide, tāpēc tas mainās - un līdz ar to "
              "mainās arī viļņa garums.",
              "Tabulas otrā rinda to parāda: tā pati 340 Hz skaņa ūdenī "
              "iegūst 4,4 reizes garāku vilni."], NAVY),
        ]),
        ("Mērvienības pirms aprēķina", [
            ("tabula",
             ["Dots uzdevumā", "SI vienībās", "Kur sastopas"],
             [["1 kHz", "1000 Hz", "Skaņas frekvences"],
              ["1 MHz", "10⁶ Hz", "Radio un ultraskaņa"],
              ["1 cm", "0,01 m", "Viļņa garums ūdenī"],
              ["1 mm", "0,001 m", "Ultraskaņas viļņa garums"]],
             [3.40, 3.20, 5.63]),
            ("panelis", "DIVI SOĻI, KAS PASARGĀ NO KĻŪDAS",
             ["1. Vispirms pārrēķini visu SI vienībās - hercos un "
              "metros; tikai tad ievieto formulā.",
              "2. Pēc aprēķina pārbaudi kārtu: skaņas viļņa garums gaisā "
              "ir metru desmitdaļas, ultraskaņai - milimetri.",
              "Ja atbilde iznāk kilometros vai mikrometros, meklē kļūdu "
              "pārrēķinā, nevis formulā."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Viļņa garums gaisā",
             teksts="Skaņas frekvence ir 500 Hz, ātrums gaisā 340 m/s.\n"
                    "Aprēķini viļņa garumu!",
             dots=["f = 500 Hz", "v = 340 m/s"],
             jaaprekina=["λ = ?"],
             formulas=["v = λf", "λ = v/f"],
             aprekins=["1)  λ = 340 : 500",
                       "2)  λ = 0,68 m"],
             atbilde="λ = 0,68 m",
             piezime="Jo augstāka skaņa, jo īsāks vilnis - ātrums taču "
                     "paliek tas pats."),
        dict(nr=2, virsraksts="Frekvence no viļņa garuma",
             teksts="Ūdens virsmas viļņa garums ir 2,5 m, ātrums 2,0 m/s.\n"
                    "Aprēķini frekvenci un periodu!",
             dots=["λ = 2,5 m", "v = 2,0 m/s"],
             jaaprekina=["f = ?", "T = ?"],
             formulas=["v = λf", "f = v/λ", "T = 1/f"],
             aprekins=["1)  f = 2,0 : 2,5 = 0,80 Hz",
                       "2)  T = 1 : 0,80 = 1,25 s"],
             atbilde="f = 0,80 Hz;  T = 1,25 s",
             piezime="Divi soļi: vispirms frekvence, tad periods kā tās "
                     "apgrieztais lielums."),
        dict(nr=3, virsraksts="Ātrums no perioda",
             teksts="Viļņa garums ir 6,0 m, periods 1,5 s.\n"
                    "Aprēķini viļņa izplatīšanās ātrumu!",
             dots=["λ = 6,0 m", "T = 1,5 s"],
             jaaprekina=["v = ?"],
             formulas=["λ = vT", "v = λ/T"],
             aprekins=["1)  v = 6,0 : 1,5",
                       "2)  v = 4,0 m/s"],
             atbilde="v = 4,0 m/s",
             piezime="Var arī vispirms atrast f = 1 : 1,5 ≈ 0,67 Hz un "
                     "tad v = λf - rezultāts ir tas pats."),
        dict(nr=4, virsraksts="Skaņa pāriet ūdenī",
             teksts="Skaņa ar frekvenci 340 Hz no gaisa (340 m/s) pāriet\n"
                    "ūdenī (1500 m/s). Aprēķini viļņa garumu abās vidēs!",
             dots=["f = 340 Hz", "v₁ = 340 m/s", "v₂ = 1500 m/s"],
             jaaprekina=["λ₁ = ?", "λ₂ = ?"],
             formulas=["λ = v/f", "Frekvence nemainās"],
             aprekins=["1)  λ₁ = 340 : 340 = 1,0 m",
                       "2)  λ₂ = 1500 : 340 ≈ 4,4 m",
                       "3)  Frekvence abās vidēs ir 340 Hz"],
             atbilde="λ₁ = 1,0 m;  λ₂ ≈ 4,4 m",
             piezime="Vidē mainās ātrums un viļņa garums, bet frekvenci "
                     "nosaka avots."),
        dict(nr=5, virsraksts="Radioviļņa garums",
             teksts="Radiostacija raida ar frekvenci 100 MHz.\n"
                    "Aprēķini viļņa garumu! (c = 3,0·10⁸ m/s)",
             dots=["f = 100 MHz = 1,0·10⁸ Hz", "c = 3,0·10⁸ m/s"],
             jaaprekina=["λ = ?"],
             formulas=["λ = c/f"],
             aprekins=["1)  f = 1,0·10⁸ Hz",
                       "2)  λ = 3,0·10⁸ : 1,0·10⁸",
                       "3)  λ = 3,0 m"],
             atbilde="λ = 3,0 m",
             piezime="Tāpēc FM antenas garums ir ap 0,75 m - ceturtdaļa "
                     "viļņa garuma."),
        dict(nr=6, virsraksts="Frekvence no viļņa garuma",
             teksts="Skaņas viļņa garums gaisā ir 0,50 m.\n"
                    "Aprēķini frekvenci un periodu! (v = 340 m/s)",
             dots=["λ = 0,50 m", "v = 340 m/s"],
             jaaprekina=["f = ?", "T = ?"],
             formulas=["f = v/λ", "T = 1/f"],
             aprekins=["1)  f = 340 : 0,50 = 680 Hz",
                       "2)  T = 1 : 680",
                       "3)  T ≈ 1,5·10⁻³ s = 1,5 ms"],
             atbilde="f = 680 Hz;  T ≈ 1,5 ms",
             piezime="680 Hz ir cilvēka balsij tuva frekvence - to auss "
                     "uztver ļoti labi."),
        dict(nr=7, virsraksts="Frekvences maiņa",
             teksts="Kā mainīsies viļņa garums, ja frekvenci palielinās\n"
                    "4 reizes, bet vide paliek tā pati?",
             dots=["f₂ = 4f₁", "v nemainās"],
             jaaprekina=["λ₂/λ₁ = ?"],
             formulas=["λ = v/f", "λ ~ 1/f"],
             aprekins=["1)  λ₁ = v/f₁",
                       "2)  λ₂ = v/(4f₁) = λ₁/4",
                       "3)  λ₂/λ₁ = 1/4"],
             atbilde="Viļņa garums samazināsies 4 reizes.",
             piezime="Vidē ātrumu nosaka pati vide, tāpēc f un λ vienmēr "
                     "mainās pretēji."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Viļņa garums ir attālums, ko vilnis noiet viena perioda "
            "laikā.",
            "v = λf;  λ = v/f;  λ = vT.",
            "Frekvenci nosaka avots, ātrumu - vide.",
            "Pārejot citā vidē, frekvence nemainās, bet λ un v mainās.",
        ],
        majasdarbs=[
            "f = 200 Hz, v = 340 m/s. Aprēķini λ.",
            "λ = 5,0 m, v = 2,5 m/s. Aprēķini f un T.",
            "λ = 3,0 m, T = 0,50 s. Aprēķini v.",
        ],
        pasvertejums=["Zinu, kas ir viļņa garums",
                      "Protu lietot v = λf",
                      "Protu izteikt λ un f",
                      "Zinu, kas mainās citā vidē"],
        nakama="Nākamā stunda: uzdevumi par viļņiem un gatavošanās PD1."),
),

dict(
    nr="6.4", virsraksts="Uzdevumi par viļņiem",
    jautajums="Kā no grafika nolasīt periodu un amplitūdu?",
    apaksraksts="Grafiks → T un A · f = 1/T · v = λf · Gatavošanās PD1",
    merkis="Nolasīt svārstību un viļņa grafiku, aprēķināt periodu, "
           "frekvenci un viļņa garumu un pārbaudīt mērvienības.",
    protu=["atšķirt svārstību grafiku no viļņa grafika;",
           "nolasīt amplitūdu, periodu un viļņa garumu;",
           "risināt divu un triju soļu uzdevumus ar v = λf;",
           "pārbaudīt atbildes mērvienības."],
    atkartojums="Šī ir temata pēdējā mācību stunda. Nākamajā stundā ir "
                "PD1 - tāpēc šodien atkārtojam visu, kas tajā būs.",
    uzdevumu_apraksts="Kombinēti uzdevumi pirms PD1",
    teorija=[
        ("Divi dažādi grafiki", [
            ("divi",
             ("SVĀRSTĪBU GRAFIKS  x(t)", BLUE,
              ["Uz horizontālās ass - LAIKS.",
               "Rāda vienu daļiņu.",
               "Nolasa amplitūdu A.",
               "Nolasa periodu T sekundēs.",
               "Tad f = 1/T."]),
             ("VIĻŅA GRAFIKS  x(l)", GREEN,
              ["Uz horizontālās ass - ATTĀLUMS.",
               "Rāda vilni vienā mirklī.",
               "Nolasa amplitūdu A.",
               "Nolasa viļņa garumu λ metros.",
               "Tad v = λf."])),
            ("panelis", "BIEŽĀKĀS KĻŪDAS",
             ["Amplitūda ir novirze no līdzsvara stāvokļa, nevis "
              "attālums no kalna līdz ielejai - tas ir divas amplitūdas.",
              "Periodu nolasa starp diviem vienādiem punktiem, nevis "
              "starp kalnu un ieleju - tur ir tikai pusperiods.",
              "Pirms atbildes vienmēr pārbauda asu mērvienību: sekundes "
              "dod periodu, metri - viļņa garumu."], RED),
        ]),
        ("Gatavošanās PD1", [
            ("tabula",
             ["PD1 daļa", "Ko prasa", "Ko atkārtot"],
             [["Jēdzieni", "A, T, f un λ nozīme", "6.1. un 6.3. stunda"],
              ["Skaidrojums", "Rezonanse ar piemēru", "6.1. stunda"],
              ["Viļņu veidi", "Šķērs- un garenviļņi", "6.2. stunda"],
              ["Aprēķins", "T = t/N, f = 1/T, v = λf", "Visas stundas"]],
             [2.90, 4.10, 3.23]),
            ("panelis", "KĀ NOFORMĒT PD1 UZDEVUMU",
             ["Dots → Jāaprēķina → Formulas → Aprēķins → Atbilde. Katrs "
              "solis dod punktus arī tad, ja gala skaitlis ir kļūdains.",
              "Mērvienības pārrēķina uzreiz: centimetrus metros, minūtes "
              "sekundēs, kilohercus hercos.",
              "Atbildi pieraksta ar mērvienību un novērtē, vai skaitlis "
              "ir saprātīgs."], NAVY),
        ]),
        ("PD1 vērtēšana", [
            ("tabula",
             ["Solis risinājumā", "Ko vērtē", "Punkti"],
             [["Dots un jāaprēķina", "Pārrēķins SI vienībās", "1"],
              ["Formulas", "Pareiza sakarība", "1"],
              ["Aprēķins", "Pareizas darbības", "1"],
              ["Atbilde", "Skaitlis ar mērvienību", "1"]],
             [4.00, 4.40, 3.83]),
            ("divi",
             ("KĀ IEGŪT VISUS PUNKTUS", GREEN,
              ["Pieraksti doto arī tad, ja",
               "uzdevumu nepabeidz.",
               "Formulu vispirms raksti",
               "vispārīgā formā.",
               "Atbildi izcel un pieraksti",
               "ar mērvienību."]),
             ("KUR PUNKTUS ZAUDĒ", RED,
              ["Tikai skaitļu virkne bez",
               "formulām.",
               "Nepārrēķinātas vienības.",
               "Atbilde bez mērvienības.",
               "Tukša lapa - tur punktu",
               "nav vispār."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="No svārstību grafika",
             teksts="Svārstību grafikā amplitūda ir 5,0 cm un periods\n"
                    "0,40 s. Aprēķini frekvenci un svārstību skaitu 10 s!",
             dots=["A = 5,0 cm = 0,05 m", "T = 0,40 s", "t = 10 s"],
             jaaprekina=["f = ?", "N = ?"],
             formulas=["f = 1/T", "N = t/T"],
             aprekins=["1)  f = 1 : 0,40 = 2,5 Hz",
                       "2)  N = 10 : 0,40 = 25 svārstības"],
             atbilde="f = 2,5 Hz;  N = 25",
             piezime="Amplitūdu uzreiz pārrēķina metros - PD1 to prasa."),
        dict(nr=2, virsraksts="No viļņa grafika",
             teksts="Attālums starp diviem kalniem ir 3,0 m, un vilnis\n"
                    "4,0 s laikā veic 8 svārstības.\n"
                    "Aprēķini viļņa ātrumu!",
             dots=["λ = 3,0 m", "t = 4,0 s", "N = 8"],
             jaaprekina=["v = ?"],
             formulas=["T = t/N", "f = 1/T", "v = λf"],
             aprekins=["1)  T = 4,0 : 8 = 0,50 s",
                       "2)  f = 1 : 0,50 = 2,0 Hz",
                       "3)  v = 3,0 · 2,0 = 6,0 m/s"],
             atbilde="v = 6,0 m/s",
             piezime="Trīs soļi pēc kārtas - tieši tāds būs grūtākais "
                     "PD1 uzdevums."),
        dict(nr=3, virsraksts="Mērvienību pārrēķins",
             teksts="Ultraskaņas signāla frekvence ir 40 kHz, ātrums\n"
                    "ūdenī 1500 m/s. Aprēķini viļņa garumu milimetros!",
             dots=["f = 40 kHz = 40 000 Hz", "v = 1500 m/s"],
             jaaprekina=["λ = ?"],
             formulas=["λ = v/f"],
             aprekins=["1)  λ = 1500 : 40 000",
                       "2)  λ = 0,0375 m",
                       "3)  λ ≈ 37,5 mm"],
             atbilde="λ ≈ 37,5 mm",
             piezime="Īss vilnis ļauj ultraskaņai «saskatīt» sīkas "
                     "detaļas medicīnas izmeklējumos."),
        dict(nr=4, virsraksts="Stīga un skaņa",
             teksts="Stīga svārstās ar frekvenci 256 Hz. Skaņas ātrums\n"
                    "gaisā ir 340 m/s. Aprēķini skaņas viļņa garumu un\n"
                    "periodu!",
             dots=["f = 256 Hz", "v = 340 m/s"],
             jaaprekina=["λ = ?", "T = ?"],
             formulas=["λ = v/f", "T = 1/f"],
             aprekins=["1)  λ = 340 : 256 ≈ 1,33 m",
                       "2)  T = 1 : 256 ≈ 0,0039 s",
                       "3)  T ≈ 3,9 ms"],
             atbilde="λ ≈ 1,33 m;  T ≈ 3,9 ms",
             piezime="256 Hz ir nots «do» - stīga iešūpo gaisu ar to "
                     "pašu frekvenci."),
        dict(nr=5, virsraksts="No svārstībām uz vilni",
             teksts="Avots 20 s laikā veic 40 svārstības; radītā viļņa\n"
                    "garums ir 1,5 m. Aprēķini periodu, frekvenci un "
                    "ātrumu!",
             dots=["t = 20 s", "N = 40", "λ = 1,5 m"],
             jaaprekina=["T = ?", "f = ?", "v = ?"],
             formulas=["T = t/N", "f = 1/T", "v = λf"],
             aprekins=["1)  T = 20 : 40 = 0,50 s",
                       "2)  f = 1 : 0,50 = 2,0 Hz",
                       "3)  v = 1,5 · 2,0 = 3,0 m/s"],
             atbilde="T = 0,50 s;  f = 2,0 Hz;  v = 3,0 m/s",
             piezime="Viļņa frekvenci vienmēr nosaka avota svārstību "
                     "frekvence."),
        dict(nr=6, virsraksts="Vilnis un atbalss kopā",
             teksts="Skaņas viļņa garums ir 0,20 m, frekvence 1700 Hz.\n"
                    "Aprēķini ātrumu un attālumu līdz sienai, ja atbalsi\n"
                    "dzird pēc 0,50 s!",
             dots=["λ = 0,20 m", "f = 1700 Hz", "t = 0,50 s"],
             jaaprekina=["v = ?", "s = ?"],
             formulas=["v = λf", "s = vt/2"],
             aprekins=["1)  v = 0,20 · 1700 = 340 m/s",
                       "2)  Viss ceļš: 340 · 0,50 = 170 m",
                       "3)  s = 170 : 2 = 85 m"],
             atbilde="v = 340 m/s;  s = 85 m",
             piezime="Divi temati vienā uzdevumā: viļņa vienādojums un "
                     "atbalss - tieši tā mēdz būt pārbaudes darbā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Svārstību grafikā nolasa periodu, viļņa grafikā - viļņa "
            "garumu.",
            "Amplitūda ir novirze no līdzsvara, nevis kalna un ielejas "
            "starpība.",
            "Kombinētos uzdevumus risina pa soļiem: T → f → v.",
            "Mērvienības pārrēķina pirms aprēķina, ne pēc tā.",
        ],
        majasdarbs=[
            "Atkārto 6.1.-6.3. stundas kopsavilkumus.",
            "λ = 2,0 m; 10 svārstības 5,0 s laikā. Aprēķini v.",
            "Sagatavo formulu sarakstu PD1: T = t/N, f = 1/T, v = λf.",
        ],
        pasvertejums=["Protu lasīt abu veidu grafikus",
                      "Protu risināt vairāku soļu uzdevumus",
                      "Protu pārrēķināt mērvienības",
                      "Esmu gatavs PD1"],
        nakama="Nākamā stunda: PD1 - mehāniskās svārstības un viļņi."),
),

]
