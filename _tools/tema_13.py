# -*- coding: utf-8 -*-
"""10.13. temats "Viļņi dabā un tehnikā" — 8 stundas, pēc tam PD8."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN

TEMATS = "13. temats. Viļņi dabā un tehnikā"
KICKER = "DABASZINĪBAS · 10. KLASE · 13. TEMATS: VIĻŅI DABĀ UN TEHNIKĀ"
MAPE = "C:/aphysics/Dabaszinibas/13. Viļņi dabā un tehnikā"

STUNDAS = [

dict(
    nr="13.1", virsraksts="Svārstības",
    jautajums="Kas ir periods, frekvence un amplitūda?",
    apaksraksts="Amplitūda · Periods · Frekvence · f = 1/T",
    merkis="Iemācīties raksturot svārstības ar amplitūdu, periodu un "
           "frekvenci un lietot sakarību f = 1/T.",
    protu=["nosaukt svārstību raksturlielumus;",
           "lietot f = 1/T un T = 1/f;",
           "aprēķināt svārstību skaitu dotā laikā;",
           "atpazīt svārstības dabā un tehnikā."],
    atkartojums="Svārstības ir kustība, kas atkārtojas. No tām rodas viļņi, "
                "kurus pētīsim visā šajā tematā.",
    uzdevumu_apraksts="Periods, frekvence un svārstību skaits",
    teorija=[
        ("Svārstību raksturlielumi", [
            ("kartitas", [
                ("AMPLITŪDA  A", BLUE,
                 ["Lielākā novirze no līdzsvara stāvokļa.",
                  "Mēra metros.",
                  "Skaņā nosaka skaļumu."]),
                ("PERIODS  T", GREEN,
                 ["Laiks vienai pilnai svārstībai.",
                  "Mēra sekundēs.",
                  "T = t / N"]),
                ("FREKVENCE  f", GOLD,
                 ["Svārstību skaits sekundē.",
                  "Mēra hercos (Hz).",
                  "f = N / t"]),
            ]),
            ("formula", "PERIODA UN FREKVENCES SAISTĪBA",
             "f = 1 / T        T = 1 / f        [f] = Hz = 1/s",
             "Jo īsāks periods, jo lielāka frekvence. 50 Hz nozīmē 50 "
             "svārstības sekundē, tātad T = 0,02 s.", GOLD),
        ]),
        ("Svārstības ap mums", [
            ("tabula",
             ["Svārstības", "Frekvence", "Periods"],
             [["Sirdspuksti miera stāvoklī", "~1,2 Hz", "~0,8 s"],
              ["Maiņstrāva tīklā", "50 Hz", "0,02 s"],
              ["Kamertonis (nots la)", "440 Hz", "2,3 ms"],
              ["Radio FM raidītājs", "100 MHz", "10 ns"]],
             [5.13, 3.60, 3.50]),
            ("panelis", "KUR SVĀRSTĪBAS NODER",
             ["Pulkstenis mēra laiku ar svārstībām  ·  mūzikas instrumenti "
              "rada skaņu ar stīgu vai gaisa svārstībām  ·  šūpoles, "
              "atsperes, amortizatori  ·  elektriskās svārstības rada "
              "radioviļņus."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Periods un frekvence",
             teksts="Svārsts 60 s laikā veic 150 pilnas svārstības.\n"
                    "Aprēķini periodu un frekvenci!",
             dots=["t = 60 s", "N = 150"],
             jaaprekina=["T = ?", "f = ?"],
             formulas=["T = t / N", "f = N / t = 1/T"],
             aprekins=["1)  T = 60 : 150 = 0,40 s",
                       "2)  f = 150 : 60 = 2,5 Hz",
                       "3)  Pārbaude: 1 : 0,40 = 2,5 ✔"],
             atbilde="T = 0,40 s ;   f = 2,5 Hz",
             piezime="T un f vienmēr ir savstarpēji apgriezti lielumi."),
        dict(nr=2, virsraksts="Maiņstrāvas periods",
             teksts="Latvijas elektrotīklā maiņstrāvas frekvence ir 50 Hz.\n"
                    "Aprēķini periodu un svārstību skaitu vienā minūtē!",
             dots=["f = 50 Hz", "t = 1 min"],
             jaaprekina=["T = ?", "N = ?"],
             formulas=["T = 1 / f", "N = f · t"],
             aprekins=["1)  T = 1 : 50 = 0,020 s",
                       "2)  t = 60 s",
                       "3)  N = 50 · 60 = 3,0·10³"],
             atbilde="T = 0,020 s ;   N = 3000 svārstības",
             piezime="Tāpēc vecās kvēlspuldzes nemanāmi mirgo 100 reižu "
                     "sekundē."),
        dict(nr=3, virsraksts="Sirdsdarbība",
             teksts="Sportista sirds miera stāvoklī veic 48 sitienus "
                    "minūtē.\nAprēķini frekvenci hercos un periodu!",
             dots=["N = 48", "t = 1 min = 60 s"],
             jaaprekina=["f = ?", "T = ?"],
             formulas=["f = N / t", "T = 1 / f"],
             aprekins=["1)  f = 48 : 60 = 0,80 Hz",
                       "2)  T = 1 : 0,80",
                       "3)  T = 1,25 s"],
             atbilde="f = 0,80 Hz ;   T = 1,25 s",
             piezime="Trenētam sportistam sirds pukst retāk, jo katrs "
                     "sitiens ir spēcīgāks."),
        dict(nr=4, virsraksts="Kamertoņa svārstības",
             teksts="Kamertonis skan ar frekvenci 440 Hz un skan 3,0 s.\n"
                    "Aprēķini periodu un kopējo svārstību skaitu!",
             dots=["f = 440 Hz", "t = 3,0 s"],
             jaaprekina=["T = ?", "N = ?"],
             formulas=["T = 1 / f", "N = f · t"],
             aprekins=["1)  T = 1 : 440 = 2,27·10⁻³ s",
                       "2)  N = 440 · 3,0",
                       "3)  N = 1,32·10³"],
             atbilde="T ≈ 2,3 ms ;   N = 1320 svārstības",
             piezime="440 Hz ir nots “la” — pēc tās skaņo visus mūzikas "
                     "instrumentus."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Svārstības raksturo amplitūda, periods un frekvence.",
            "f = 1/T; frekvenci mēra hercos (1 Hz = 1 svārstība sekundē).",
            "T = t/N un f = N/t.",
            "Amplitūda nosaka skaņas skaļumu, frekvence — augstumu.",
        ],
        majasdarbs=[
            "N = 240 svārstības 40 s laikā. Aprēķini T un f.",
            "f = 25 Hz. Aprēķini T un svārstību skaitu 2 minūtēs.",
            "Nosauc trīs svārstību piemērus dabā un trīs tehnikā.",
        ],
        pasvertejums=["Protu nosaukt raksturlielumus",
                      "Protu lietot f = 1/T",
                      "Protu aprēķināt svārstību skaitu",
                      "Protu atpazīt svārstības"],
        nakama="Nākamā stunda: mehāniskie viļņi."),
),

dict(
    nr="13.2", virsraksts="Mehāniskie viļņi",
    jautajums="Kas pārvietojas vilnī?",
    apaksraksts="Garenviļņi · Šķērsviļņi · λ = υT · Enerģijas pārnese",
    merkis="Iemācīties atšķirt garenviļņus no šķērsviļņiem un lietot "
           "sakarību λ = υT starp viļņa garumu, ātrumu un periodu.",
    protu=["atšķirt garenviļni no šķērsviļņa;",
           "skaidrot, ka vilnī pārvietojas enerģija, nevis viela;",
           "lietot λ = υT un λ = υ/f;",
           "aprēķināt viļņa garumu, ātrumu vai frekvenci."],
    atkartojums="13.1. stundā: svārstības atkārtojas laikā. Ja svārstības "
                "izplatās telpā, rodas VILNIS.",
    uzdevumu_apraksts="Viļņa garums, ātrums un frekvence",
    teorija=[
        ("Divi viļņu veidi", [
            ("divi",
             ("GARENVILNIS", BLUE,
              ["Daļiņas svārstās TAJĀ PAŠĀ virzienā,",
               "kurā vilnis izplatās.",
               "Veidojas sabiezinājumi un retinājumi.",
               "Piemērs: skaņa gaisā, atsperē."]),
             ("ŠĶĒRSVILNIS", GREEN,
              ["Daļiņas svārstās PERPENDIKULĀRI",
               "viļņa izplatīšanās virzienam.",
               "Veidojas kalni un ielejas.",
               "Piemērs: viļņi uz ūdens, uz virves."])),
            ("panelis", "SVARĪGI SAPRAST",
             ["Vilnī pārvietojas ENERĢIJA, nevis viela. Pludiņš uz ūdens "
              "viļņa tikai šūpojas augšup un lejup — tas neaizpeld kopā ar "
              "vilni.",
              "Tāpat gaisa daļiņas skaņas vilnī tikai svārstās ap savu vietu "
              "— tās neaizceļo no runātāja līdz klausītājam."], NAVY),
        ]),
        ("Viļņa raksturlielumi", [
            ("formula", "VIĻŅA PAMATSAKARĪBA",
             "λ = υ · T        λ = υ / f        υ = λ · f",
             "λ — viļņa garums [m] (attālums starp diviem kaimiņu kalniem), "
             "υ — izplatīšanās ātrums [m/s], T — periods, f — frekvence.",
             GOLD),
            ("tabula",
             ["Vide", "Skaņas ātrums, m/s", "Piezīme"],
             [["Gaiss (20 °C)", "343", "vidē blīvumam augot, ātrums aug"],
              ["Ūdens", "1480", "~4 reizes ātrāk nekā gaisā"],
              ["Tērauds", "5100", "~15 reizes ātrāk nekā gaisā"]],
             [3.63, 3.60, 5.00]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Viļņa garums uz ūdens",
             teksts="Viļņi uz ūdens izplatās ar ātrumu 2,4 m/s, to periods "
                    "ir 1,5 s.\nAprēķini viļņa garumu!",
             dots=["υ = 2,4 m/s", "T = 1,5 s"],
             jaaprekina=["λ = ?"],
             formulas=["λ = υ · T"],
             aprekins=["1)  λ = 2,4 m/s · 1,5 s",
                       "2)  λ = 3,6 m"],
             atbilde="λ = 3,6 m",
             piezime="Viļņa garums ir attālums starp diviem kaimiņu viļņu "
                     "kalniem."),
        dict(nr=2, virsraksts="Skaņas viļņa garums",
             teksts="Skaņas frekvence ir 680 Hz, ātrums gaisā 340 m/s.\n"
                    "Aprēķini viļņa garumu!",
             dots=["f = 680 Hz", "υ = 340 m/s"],
             jaaprekina=["λ = ?"],
             formulas=["λ = υ / f"],
             aprekins=["1)  λ = 340 : 680",
                       "2)  λ = 0,50 m"],
             atbilde="λ = 0,50 m = 50 cm",
             piezime="Jo augstāka frekvence, jo īsāks viļņa garums."),
        dict(nr=3, virsraksts="Skaņa ūdenī",
             teksts="Skaņas viļņa garums ūdenī ir 2,0 m, ātrums ūdenī "
                    "1480 m/s.\nAprēķini frekvenci un salīdzini viļņa garumu "
                    "gaisā pie tās pašas frekvences (υ = 340 m/s)!",
             dots=["λ₁ = 2,0 m ;  υ₁ = 1480 m/s", "υ₂ = 340 m/s"],
             jaaprekina=["f = ?", "λ₂ = ?"],
             formulas=["f = υ / λ", "λ = υ / f"],
             aprekins=["1)  f = 1480 : 2,0 = 740 Hz",
                       "2)  λ₂ = 340 : 740",
                       "3)  λ₂ = 0,46 m"],
             atbilde="f = 740 Hz ;   λ₂ ≈ 0,46 m",
             piezime="Pārejot citā vidē, frekvence NEMAINĀS, bet mainās "
                     "ātrums un viļņa garums."),
        dict(nr=4, virsraksts="Viļņu skaits",
             teksts="Uz ezera 30 s laikā piestātni sasniedz 20 viļņu kalni. "
                    "Attālums starp kalniem ir 1,8 m.\n"
                    "Aprēķini periodu, frekvenci un viļņu ātrumu!",
             dots=["N = 20 ;  t = 30 s", "λ = 1,8 m"],
             jaaprekina=["T = ?", "f = ?", "υ = ?"],
             formulas=["T = t/N", "f = 1/T", "υ = λ · f"],
             aprekins=["1)  T = 30 : 20 = 1,5 s",
                       "2)  f = 1 : 1,5 = 0,67 Hz",
                       "3)  υ = 1,8 · 0,67 = 1,2 m/s"],
             atbilde="T = 1,5 s ;  f = 0,67 Hz ;  υ = 1,2 m/s",
             piezime="Trīs soļi: vispirms periods, tad frekvence, tad "
                     "ātrums."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Garenvilnī daļiņas svārstās gar izplatīšanās virzienu, "
            "šķērsvilnī — perpendikulāri.",
            "Vilnī pārvietojas enerģija, nevis viela.",
            "λ = υT = υ/f — galvenā viļņu sakarība.",
            "Pārejot citā vidē, frekvence nemainās, bet ātrums un λ mainās.",
        ],
        majasdarbs=[
            "υ = 340 m/s, f = 170 Hz. Aprēķini λ.",
            "λ = 0,25 m, f = 1360 Hz. Aprēķini ātrumu.",
            "Nosauc divus garenviļņu un divus šķērsviļņu piemērus.",
        ],
        pasvertejums=["Protu atšķirt viļņu veidus",
                      "Protu skaidrot enerģijas pārnesi",
                      "Protu lietot λ = υT",
                      "Protu aprēķināt λ, υ un f"],
        nakama="Nākamā stunda: skaņa."),
),

dict(
    nr="13.3", virsraksts="Skaņa",
    jautajums="No kā atkarīgs skaņas augstums un skaļums?",
    apaksraksts="Frekvence un augstums · Amplitūda un skaļums · Dzirdamības "
                "diapazons",
    merkis="Iemācīties saistīt skaņas frekvenci ar augstumu un amplitūdu ar "
           "skaļumu un aprēķināt skaņas viļņa raksturlielumus.",
    protu=["saistīt frekvenci ar skaņas augstumu;",
           "saistīt amplitūdu ar skaļumu;",
           "nosaukt dzirdamības diapazonu;",
           "aprēķināt skaņas viļņa garumu un frekvenci."],
    atkartojums="13.2. stundā: skaņa ir garenvilnis. Šodien noskaidrosim, kas "
                "nosaka, kā mēs to dzirdam.",
    uzdevumu_apraksts="Skaņas frekvence, viļņa garums un ātrums",
    teorija=[
        ("Skaņas raksturlielumi", [
            ("divi",
             ("AUGSTUMS ← FREKVENCE", BLUE,
              ["Liela frekvence → augsta skaņa.",
               "Maza frekvence → zema skaņa.",
               "Sievietes balss ~200 Hz,",
               "vīrieša balss ~120 Hz."]),
             ("SKAĻUMS ← AMPLITŪDA", GREEN,
              ["Liela amplitūda → skaļa skaņa.",
               "Maza amplitūda → klusa skaņa.",
               "Skaļumu mēra decibelos (9.1. stunda).",
               "Amplitūda nosaka enerģiju."])),
            ("tabula",
             ["Diapazons", "Frekvence", "Piemērs"],
             [["Infraskaņa", "zem 20 Hz", "zemestrīces, vulkāni"],
              ["Dzirdamā skaņa", "20 Hz – 20 kHz", "runa, mūzika"],
              ["Ultraskaņa", "virs 20 kHz", "sikspārņi, sonogrāfija"]],
             [3.63, 3.60, 5.00]),
        ]),
        ("Skaņa dažādās vidēs", [
            ("panelis", "SKAŅAI VAJADZĪGA VIDE",
             ["Skaņa ir mehānisks vilnis — tai vajag vielu, kurā izplatīties. "
              "Vakuumā skaņa neizplatās, tāpēc kosmosā ir klusums.",
              "Jo blīvāka un elastīgāka vide, jo ātrāk izplatās skaņa: gaisā "
              "343 m/s, ūdenī 1480 m/s, tēraudā 5100 m/s."], NAVY),
            ("formula", "SKAŅAS SAKARĪBAS",
             "λ = υ / f        υ = 343 m/s (gaisā, 20 °C)",
             "Dzirdamās skaņas viļņa garums gaisā ir no ~17 m (20 Hz) līdz "
             "~17 mm (20 kHz).", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Dzirdamības robežas",
             teksts="Dzirdamās skaņas frekvence ir no 20 Hz līdz 20 000 Hz. "
                    "Skaņas ātrums gaisā 340 m/s.\n"
                    "Aprēķini abu robežu viļņu garumus!",
             dots=["f₁ = 20 Hz ;  f₂ = 20 000 Hz", "υ = 340 m/s"],
             jaaprekina=["λ₁ = ?", "λ₂ = ?"],
             formulas=["λ = υ / f"],
             aprekins=["1)  λ₁ = 340 : 20 = 17 m",
                       "2)  λ₂ = 340 : 20 000 = 0,017 m",
                       "3)  λ₂ = 17 mm"],
             atbilde="λ₁ = 17 m ;   λ₂ = 17 mm",
             piezime="Zemas skaņas viļņi ir gari — tāpēc tie labāk apiet "
                     "šķēršļus un dzirdami tālāk."),
        dict(nr=2, virsraksts="Nots frekvence",
             teksts="Nots “la” viļņa garums gaisā ir 0,78 m, skaņas ātrums "
                    "343 m/s.\nAprēķini frekvenci!",
             dots=["λ = 0,78 m", "υ = 343 m/s"],
             jaaprekina=["f = ?"],
             formulas=["f = υ / λ"],
             aprekins=["1)  f = 343 : 0,78",
                       "2)  f = 440 Hz"],
             atbilde="f = 440 Hz",
             piezime="Tā ir standarta skaņošanas nots visos orķestros."),
        dict(nr=3, virsraksts="Skaņa tēraudā un gaisā",
             teksts="Skaņas frekvence ir 500 Hz. Ātrums gaisā 343 m/s, "
                    "tēraudā 5100 m/s.\n"
                    "Aprēķini viļņa garumu abās vidēs un cik reižu tie "
                    "atšķiras!",
             dots=["f = 500 Hz", "υ₁ = 343 m/s ;  υ₂ = 5100 m/s"],
             jaaprekina=["λ₁ = ?", "λ₂ = ?", "n = ?"],
             formulas=["λ = υ / f"],
             aprekins=["1)  λ₁ = 343 : 500 = 0,686 m",
                       "2)  λ₂ = 5100 : 500 = 10,2 m",
                       "3)  n = 10,2 : 0,686 = 14,9"],
             atbilde="λ₁ ≈ 0,69 m ;  λ₂ = 10,2 m ;  n ≈ 15 reižu",
             piezime="Frekvence abās vidēs vienāda — mainās tikai ātrums un "
                     "viļņa garums."),
        dict(nr=4, virsraksts="Zibens attālums",
             teksts="Starp zibeni un pērkonu pagāja 4,5 s. Skaņas ātrums "
                    "343 m/s.\n"
                    "Cik tālu bija zibens? Kāpēc gaismas laiku neņem vērā?",
             dots=["t = 4,5 s", "υ = 343 m/s"],
             jaaprekina=["s = ?"],
             formulas=["s = υ · t"],
             aprekins=["1)  s = 343 · 4,5",
                       "2)  s = 1544 m",
                       "3)  s ≈ 1,5 km"],
             atbilde="s ≈ 1,5·10³ m = 1,5 km",
             piezime="Gaisma 1,5 km noiet 5 µs — tas ir miljons reižu ātrāk "
                     "nekā skaņa."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Skaņas augstumu nosaka frekvence, skaļumu — amplitūda.",
            "Dzirdamā skaņa: 20 Hz – 20 kHz; zem tās infraskaņa, virs — "
            "ultraskaņa.",
            "Skaņai vajadzīga vide — vakuumā tā neizplatās.",
            "Blīvākā vidē skaņa izplatās ātrāk: gaiss < ūdens < tērauds.",
        ],
        majasdarbs=[
            "f = 1000 Hz, υ = 343 m/s. Aprēķini λ.",
            "λ = 1,7 m gaisā. Aprēķini frekvenci.",
            "Pērkons dzirdams pēc 7 s. Cik tālu ir zibens?",
        ],
        pasvertejums=["Protu saistīt frekvenci ar augstumu",
                      "Protu saistīt amplitūdu ar skaļumu",
                      "Protu aprēķināt λ un f",
                      "Protu salīdzināt skaņu dažādās vidēs"],
        nakama="Nākamā stunda: atbalss, eholokācija un ultraskaņa."),
),

dict(
    nr="13.4", virsraksts="Atbalss, eholokācija, ultraskaņa un infraskaņa",
    jautajums="Kā ar skaņu izmērīt attālumu un ieraudzīt neredzamo?",
    apaksraksts="Atbalss · Eholokācija · Ultrasonogrāfija · Infraskaņa",
    merkis="Iemācīties aprēķināt attālumu pēc atbalss vai atstarotā "
           "ultraskaņas signāla un skaidrot eholokācijas lietojumus.",
    protu=["aprēķināt attālumu pēc atbalss laika;",
           "skaidrot eholokācijas principu;",
           "nosaukt ultraskaņas lietojumus;",
           "raksturot infraskaņas nozīmi."],
    atkartojums="13.3. stundā mācījāmies par skaņas ātrumu. Ja skaņa "
                "atstarojas un atgriežas, pēc laika var aprēķināt attālumu.",
    uzdevumu_apraksts="Attālums pēc atbalss un ultraskaņas signāla",
    teorija=[
        ("Atbalss un eholokācija", [
            ("formula", "ATTĀLUMS PĒC ATBALSS",
             "s = υ · t / 2",
             "Signāls noiet ceļu TURP UN ATPAKAĻ, tāpēc kopējo ceļu dala ar "
             "divi. Tā rēķina sonārs, eholots un ultrasonogrāfs.", GOLD),
            ("kartitas", [
                ("SIKSPĀRŅI UN DELFĪNI", BLUE,
                 ["Izstaro ultraskaņu un klausās atbalsi.",
                  "Nosaka attālumu, izmēru un formu.",
                  "Orientējas pilnīgā tumsā."]),
                ("SONĀRS UN EHOLOTS", GREEN,
                 ["Kuģi mēra dziļumu un meklē zivju barus.",
                  "Zemūdenes atklāj objektus.",
                  "Ūdenī skaņa izplatās tālu."]),
                ("ULTRASONOGRĀFIJA", GOLD,
                 ["Medicīnā apskata iekšējos orgānus.",
                  "Nav jonizējoša — droša grūtniecēm.",
                  "Attēls veidojas no atstarotiem signāliem."]),
            ]),
        ]),
        ("Ultraskaņa un infraskaņa", [
            ("divi",
             ("ULTRASKAŅA (virs 20 kHz)", BLUE,
              ["Īss viļņa garums → labāka izšķirtspēja.",
               "Medicīna, defektoskopija, tīrīšana.",
               "Metinājumu un detaļu pārbaude.",
               "Trūkums: slikti izplatās gaisā."]),
             ("INFRASKAŅA (zem 20 Hz)", RED,
              ["Ļoti garš viļņa garums → izplatās tālu.",
               "Zemestrīces, vulkāni, vētras.",
               "Seismoloģiskais monitorings.",
               "Dzīvnieki to sajūt pirms katastrofām."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Attālums līdz klintij",
             teksts="Atbalss no klints dzirdama pēc 2,4 s. Skaņas ātrums "
                    "343 m/s.\nAprēķini attālumu līdz klintij!",
             dots=["t = 2,4 s", "υ = 343 m/s"],
             jaaprekina=["s = ?"],
             formulas=["s = υ · t / 2"],
             aprekins=["1)  Kopējais ceļš = 343 · 2,4 = 823 m",
                       "2)  s = 823 : 2",
                       "3)  s = 412 m"],
             atbilde="s ≈ 4,1·10² m",
             piezime="Neaizmirsti dalīt ar 2 — skaņa noiet turp un atpakaļ."),
        dict(nr=2, virsraksts="Jūras dziļums",
             teksts="Eholota signāls atgriežas pēc 0,80 s. Skaņas ātrums "
                    "ūdenī 1480 m/s.\nAprēķini jūras dziļumu!",
             dots=["t = 0,80 s", "υ = 1480 m/s"],
             jaaprekina=["h = ?"],
             formulas=["h = υ · t / 2"],
             aprekins=["1)  Kopējais ceļš = 1480 · 0,80 = 1184 m",
                       "2)  h = 1184 : 2",
                       "3)  h = 592 m"],
             atbilde="h ≈ 5,9·10² m",
             piezime="Tā kuģi kartē jūras dibenu."),
        dict(nr=3, virsraksts="Sikspārņa medības",
             teksts="Sikspārnis izstaro ultraskaņu un saņem atbalsi no kukaiņa "
                    "pēc 0,012 s. Skaņas ātrums gaisā 343 m/s.\n"
                    "Cik tālu ir kukainis?",
             dots=["t = 0,012 s", "υ = 343 m/s"],
             jaaprekina=["s = ?"],
             formulas=["s = υ · t / 2"],
             aprekins=["1)  Kopējais ceļš = 343 · 0,012 = 4,12 m",
                       "2)  s = 4,12 : 2",
                       "3)  s = 2,1 m"],
             atbilde="s ≈ 2,1 m",
             piezime="Sikspārnis šo aprēķinu veic dabiski, daudzas reizes "
                     "sekundē."),
        dict(nr=4, virsraksts="Ultraskaņas izšķirtspēja",
             teksts="Ultrasonogrāfā izmanto 5,0 MHz frekvenci. Skaņas ātrums "
                    "audos 1540 m/s.\n"
                    "Aprēķini viļņa garumu un paskaidro, kāpēc lieto tik "
                    "augstu frekvenci!",
             dots=["f = 5,0 MHz", "υ = 1540 m/s"],
             jaaprekina=["λ = ?"],
             formulas=["λ = υ / f"],
             aprekins=["1)  f = 5,0·10⁶ Hz",
                       "2)  λ = 1540 : 5,0·10⁶",
                       "3)  λ = 3,1·10⁻⁴ m = 0,31 mm"],
             atbilde="λ ≈ 0,31 mm",
             piezime="Var saskatīt detaļas, kas nav mazākas par viļņa garumu "
                     "— tāpat kā mikroskopā (1.4. stunda)."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "s = υt/2 — attālumu pēc atbalss rēķina, dalot ar divi.",
            "Eholokāciju izmanto sikspārņi, delfīni, sonāri un eholoti.",
            "Ultraskaņa (virs 20 kHz) dod labu izšķirtspēju medicīnā.",
            "Infraskaņa (zem 20 Hz) izplatās tālu — zemestrīces, vētras.",
        ],
        majasdarbs=[
            "Atbalss pēc 1,6 s gaisā. Aprēķini attālumu.",
            "Eholots: t = 0,50 s ūdenī. Aprēķini dziļumu.",
            "f = 2,0 MHz, υ = 1540 m/s. Aprēķini λ.",
        ],
        pasvertejums=["Protu lietot s = υt/2",
                      "Protu skaidrot eholokāciju",
                      "Protu nosaukt ultraskaņas lietojumus",
                      "Protu raksturot infraskaņu"],
        nakama="Nākamā stunda: elektromagnētiskie viļņi."),
),

dict(
    nr="13.5", virsraksts="Elektromagnētiskie viļņi",
    jautajums="Kā signāls ceļo bez vada?",
    apaksraksts="EM viļņu rašanās · c = 3,00·10⁸ m/s · λ = c/f",
    merkis="Iemācīties skaidrot elektromagnētiskā viļņa rašanos un lietot "
           "λ = c/f ar gaismas ātrumu vakuumā.",
    protu=["skaidrot EM viļņa rašanos;",
           "salīdzināt EM viļņus ar mehāniskajiem;",
           "lietot λ = c/f;",
           "aprēķināt signāla ceļošanas laiku."],
    atkartojums="13.2. stundā: mehāniskajam vilnim vajadzīga vide. "
                "Elektromagnētiskajam vilnim vide NAV vajadzīga — tas "
                "izplatās arī vakuumā.",
    uzdevumu_apraksts="EM viļņu garums, frekvence un ceļošanas laiks",
    teorija=[
        ("Kā rodas elektromagnētiskais vilnis", [
            ("panelis", "MAINĪGS LAUKS RADA VILNI",
             ["Mainīgs elektriskais lauks rada mainīgu magnētisko lauku, un "
              "mainīgs magnētiskais lauks — atkal elektrisko. Tā abi lauki "
              "uztur viens otru un izplatās telpā kā vilnis.",
              "Tāpēc EM vilnim NAV vajadzīga vide — tas izplatās arī "
              "vakuumā. Tieši tāpēc mēs redzam Sauli un zvaigznes."], NAVY),
            ("divi",
             ("MEHĀNISKAIS VILNIS", BLUE,
              ["Vajadzīga vide (gaiss, ūdens, cietviela).",
               "Vakuumā neizplatās.",
               "Ātrums: 343 m/s gaisā.",
               "Skaņa, viļņi uz ūdens."]),
             ("ELEKTROMAGNĒTISKAIS VILNIS", GREEN,
              ["Vide nav vajadzīga.",
               "Izplatās arī vakuumā.",
               "Ātrums vakuumā c = 3,00·10⁸ m/s.",
               "Radioviļņi, gaisma, rentgens."])),
        ]),
        ("Aprēķini ar EM viļņiem", [
            ("formula", "EM VIĻŅU SAKARĪBAS",
             "λ = c / f        f = c / λ        c = 3,00·10⁸ m/s",
             "Vakuumā VISI elektromagnētiskie viļņi izplatās ar vienādu "
             "ātrumu c — atšķiras tikai frekvence un viļņa garums.", GOLD),
            ("tabula",
             ["Signāls", "Frekvence", "Viļņa garums"],
             [["Radio AM", "1,0 MHz", "300 m"],
              ["Radio FM", "100 MHz", "3,0 m"],
              ["Mobilais tālrunis", "1,8 GHz", "17 cm"],
              ["Wi-Fi", "2,4 GHz", "12,5 cm"],
              ["Redzamā gaisma", "5,0·10¹⁴ Hz", "600 nm"]],
             [4.13, 3.60, 4.50]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="FM radio viļņa garums",
             teksts="Radiostacija raida ar frekvenci 101,7 MHz. "
                    "c = 3,00·10⁸ m/s.\nAprēķini viļņa garumu!",
             dots=["f = 101,7 MHz", "c = 3,00·10⁸ m/s"],
             jaaprekina=["λ = ?"],
             formulas=["λ = c / f"],
             aprekins=["1)  f = 101,7·10⁶ Hz = 1,017·10⁸ Hz",
                       "2)  λ = 3,00·10⁸ : 1,017·10⁸",
                       "3)  λ = 2,95 m"],
             atbilde="λ ≈ 2,95 m",
             piezime="Tāpēc FM radio antenas garums ir ~1,5 m — puse no "
                     "viļņa garuma."),
        dict(nr=2, virsraksts="Wi-Fi frekvence",
             teksts="Wi-Fi viļņa garums ir 12,5 cm.\n"
                    "Aprēķini frekvenci gigahercos!",
             dots=["λ = 12,5 cm", "c = 3,00·10⁸ m/s"],
             jaaprekina=["f = ?  (GHz)"],
             formulas=["f = c / λ"],
             aprekins=["1)  λ = 0,125 m",
                       "2)  f = 3,00·10⁸ : 0,125 = 2,4·10⁹ Hz",
                       "3)  f = 2,4 GHz"],
             atbilde="f = 2,4 GHz",
             piezime="Tā ir standarta Wi-Fi frekvence, ko lieto arī "
                     "mikroviļņu krāsnis."),
        dict(nr=3, virsraksts="Signāls uz satelītu",
             teksts="Ģeostacionārais satelīts atrodas 3,6·10⁷ m augstumā.\n"
                    "Cik ilgi signāls ceļo no Zemes līdz satelītam un "
                    "atpakaļ?",
             dots=["h = 3,6·10⁷ m", "c = 3,00·10⁸ m/s"],
             jaaprekina=["t = ?"],
             formulas=["t = 2h / c"],
             aprekins=["1)  Kopējais ceļš = 2 · 3,6·10⁷ = 7,2·10⁷ m",
                       "2)  t = 7,2·10⁷ : 3,00·10⁸",
                       "3)  t = 0,24 s"],
             atbilde="t = 0,24 s",
             piezime="Tāpēc satelīta telefonsarunā ir manāma aizture."),
        dict(nr=4, virsraksts="Radars",
             teksts="Radara signāls atgriežas pēc 6,0·10⁻⁵ s.\n"
                    "Aprēķini attālumu līdz objektam!",
             dots=["t = 6,0·10⁻⁵ s", "c = 3,00·10⁸ m/s"],
             jaaprekina=["s = ?"],
             formulas=["s = c · t / 2"],
             aprekins=["1)  Kopējais ceļš = 3,00·10⁸ · 6,0·10⁻⁵ = 1,8·10⁴ m",
                       "2)  s = 1,8·10⁴ : 2",
                       "3)  s = 9,0·10³ m = 9,0 km"],
             atbilde="s = 9,0 km",
             piezime="Radars darbojas kā eholokācija, tikai ar EM viļņiem — "
                     "tāpēc arī dala ar 2."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "EM vilni rada savstarpēji mainīgs elektriskais un magnētiskais "
            "lauks.",
            "EM vilnim nav vajadzīga vide — tas izplatās arī vakuumā.",
            "Vakuumā visi EM viļņi izplatās ar c = 3,00·10⁸ m/s.",
            "λ = c/f; radaram un satelītam s = ct/2.",
        ],
        majasdarbs=[
            "f = 88,0 MHz. Aprēķini λ.",
            "λ = 0,17 m. Aprēķini frekvenci GHz.",
            "Radara signāls atgriežas pēc 2,0·10⁻⁴ s. Aprēķini attālumu.",
        ],
        pasvertejums=["Protu skaidrot EM viļņa rašanos",
                      "Protu salīdzināt ar mehānisko vilni",
                      "Protu lietot λ = c/f",
                      "Protu aprēķināt signāla laiku"],
        nakama="Nākamā stunda: elektromagnētisko viļņu skala."),
),

dict(
    nr="13.6", virsraksts="Elektromagnētisko viļņu skala",
    jautajums="Kas kopīgs radioviļņiem un rentgenam?",
    apaksraksts="EM skala · Jonizējošs un nejonizējošs starojums",
    merkis="Iemācīties sakārtot elektromagnētisko viļņu skalu un nošķirt "
           "jonizējošu starojumu no nejonizējoša.",
    protu=["sakārtot EM skalu pēc frekvences un viļņa garuma;",
           "nosaukt katra diapazona lietojumus;",
           "nošķirt jonizējošu un nejonizējošu starojumu;",
           "aprēķināt fotona enerģiju E = hf."],
    atkartojums="3.3. stundā mācījāmies E = hf, 9.2. stundā — jonizējošo "
                "starojumu. Šodien saliksim visu vienā skalā.",
    uzdevumu_apraksts="EM skala un fotona enerģija",
    teorija=[
        ("Elektromagnētisko viļņu skala", [
            ("tabula",
             ["Diapazons", "Viļņa garums", "Frekvence", "Lietojums"],
             [["Radioviļņi", "> 1 m", "< 300 MHz", "radio, TV, sakari"],
              ["Mikroviļņi", "1 m – 1 mm", "0,3–300 GHz",
               "Wi-Fi, krāsnis, radars"],
              ["Infrasarkanais", "1 mm – 700 nm", "10¹²–10¹⁴ Hz",
               "termogrāfija, pults"],
              ["Redzamā gaisma", "700–400 nm", "~10¹⁵ Hz", "redze, optika"],
              ["Ultravioletais", "400–10 nm", "10¹⁵–10¹⁶ Hz",
               "sterilizācija, D vitamīns"],
              ["Rentgens", "10 nm – 1 pm", "10¹⁶–10²⁰ Hz",
               "medicīna, drošība"],
              ["Gamma", "< 1 pm", "> 10²⁰ Hz", "terapija, sterilizācija"]],
             [2.63, 2.80, 2.60, 4.20]),
        ]),
        ("Kur ir bīstamības robeža", [
            ("formula", "FOTONA ENERĢIJA",
             "E = h · f        h = 6,63·10⁻³⁴ J·s",
             "Jo augstāka frekvence, jo lielāka fotona enerģija. Robeža starp "
             "nejonizējošu un jonizējošu starojumu ir ultravioletā "
             "diapazonā.", GOLD),
            ("divi",
             ("NEJONIZĒJOŠS", GREEN,
              ["Radioviļņi, mikroviļņi, IS, redzamā gaisma.",
               "Fotona enerģija par mazu, lai izsistu elektronu.",
               "Var tikai sasildīt audus.",
               "Aizsardzība: attālums un jaudas ierobežojumi."]),
             ("JONIZĒJOŠS", RED,
              ["UV (daļēji), rentgens, gamma.",
               "Izsit elektronus, bojā DNS.",
               "Var izraisīt vēzi.",
               "Aizsardzība: laiks, attālums, ekrāns."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Fotona enerģija dažādos diapazonos",
             teksts="Radioviļņa frekvence 1,0·10⁸ Hz, rentgena — "
                    "1,0·10¹⁸ Hz. h = 6,63·10⁻³⁴ J·s.\n"
                    "Aprēķini abu fotonu enerģijas!",
             dots=["f₁ = 1,0·10⁸ Hz", "f₂ = 1,0·10¹⁸ Hz"],
             jaaprekina=["E₁ = ?", "E₂ = ?"],
             formulas=["E = h · f"],
             aprekins=["1)  E₁ = 6,63·10⁻³⁴ · 1,0·10⁸ = 6,6·10⁻²⁶ J",
                       "2)  E₂ = 6,63·10⁻³⁴ · 1,0·10¹⁸ = 6,6·10⁻¹⁶ J",
                       "3)  n = 10¹⁰"],
             atbilde="E₁ = 6,6·10⁻²⁶ J ;  E₂ = 6,6·10⁻¹⁶ J ;  n = 10¹⁰",
             piezime="Desmit miljardu reižu starpība — tāpēc viens ir "
                     "nekaitīgs, otrs bīstams."),
        dict(nr=2, virsraksts="Infrasarkanā starojuma viļņa garums",
             teksts="Termokameras uztvertais infrasarkanais starojums ir ar "
                    "frekvenci 3,0·10¹³ Hz.\n"
                    "Aprēķini viļņa garumu mikrometros!",
             dots=["f = 3,0·10¹³ Hz", "c = 3,00·10⁸ m/s"],
             jaaprekina=["λ = ?  (µm)"],
             formulas=["λ = c / f"],
             aprekins=["1)  λ = 3,00·10⁸ : 3,0·10¹³",
                       "2)  λ = 1,0·10⁻⁵ m",
                       "3)  λ = 10 µm"],
             atbilde="λ = 10 µm",
             piezime="Cilvēka ķermenis izstaro tieši šajā diapazonā — tāpēc "
                     "termokamera mūs “redz” tumsā."),
        dict(nr=3, virsraksts="UV robeža",
             teksts="Jonizācijai vajadzīga fotona enerģija vismaz "
                    "5,0·10⁻¹⁹ J. h = 6,63·10⁻³⁴ J·s; c = 3,00·10⁸ m/s.\n"
                    "Aprēķini atbilstošo frekvenci un viļņa garumu!",
             dots=["E = 5,0·10⁻¹⁹ J", "h = 6,63·10⁻³⁴ J·s"],
             jaaprekina=["f = ?", "λ = ?"],
             formulas=["f = E / h", "λ = c / f"],
             aprekins=["1)  f = 5,0·10⁻¹⁹ : 6,63·10⁻³⁴ = 7,5·10¹⁴ Hz",
                       "2)  λ = 3,00·10⁸ : 7,5·10¹⁴",
                       "3)  λ = 4,0·10⁻⁷ m = 400 nm"],
             atbilde="f ≈ 7,5·10¹⁴ Hz ;   λ = 400 nm",
             piezime="400 nm ir tieši redzamās gaismas un UV robeža — tur "
                     "sākas jonizējošais starojums."),
        dict(nr=4, virsraksts="Mikroviļņu krāsns",
             teksts="Mikroviļņu krāsns darbojas ar frekvenci 2,45 GHz.\n"
                    "Aprēķini viļņa garumu un fotona enerģiju! Vai tas ir "
                    "jonizējošs starojums?",
             dots=["f = 2,45 GHz", "h = 6,63·10⁻³⁴ J·s",
                   "c = 3,00·10⁸ m/s"],
             jaaprekina=["λ = ?", "E = ?"],
             formulas=["λ = c/f", "E = h·f"],
             aprekins=["1)  f = 2,45·10⁹ Hz",
                       "2)  λ = 3,00·10⁸ : 2,45·10⁹ = 0,122 m",
                       "3)  E = 6,63·10⁻³⁴ · 2,45·10⁹ = 1,6·10⁻²⁴ J"],
             atbilde="λ ≈ 12 cm ;  E ≈ 1,6·10⁻²⁴ J — NAV jonizējošs",
             piezime="Enerģija ~300 000 reižu mazāka par jonizācijas slieksni "
                     "— krāsns tikai sasilda ūdens molekulas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "EM skala: radioviļņi → mikroviļņi → IS → redzamā → UV → "
            "rentgens → gamma.",
            "Skalā pa labi frekvence aug, viļņa garums sarūk, enerģija aug.",
            "E = hf; jonizējošais starojums sākas ultravioletajā diapazonā.",
            "Visi EM viļņi vakuumā izplatās ar vienādu ātrumu c.",
        ],
        majasdarbs=[
            "f = 6,0·10¹⁴ Hz. Aprēķini λ un E.",
            "λ = 500 nm. Aprēķini frekvenci un fotona enerģiju.",
            "Sakārto pēc augošas enerģijas: mikroviļņi, gamma, UV, radio.",
        ],
        pasvertejums=["Protu sakārtot EM skalu",
                      "Protu nosaukt lietojumus",
                      "Protu lietot E = hf",
                      "Protu nošķirt jonizējošu starojumu"],
        nakama="Nākamā stunda: viļņu īpašības."),
),

dict(
    nr="13.7", virsraksts="Viļņu īpašības",
    jautajums="Kāpēc viļņi liecas ap šķērsli?",
    apaksraksts="Atstarošanās · Laušana · Interference · Difrakcija",
    merkis="Iemācīties salīdzināt viļņu atstarošanos, laušanu, interferenci "
           "un difrakciju un nosaukt to izpausmes dabā.",
    protu=["nosaukt četras viļņu īpašības;",
           "skaidrot atstarošanos un laušanu;",
           "skaidrot interferenci un difrakciju;",
           "aprēķināt uzdevumus par atstarošanos un laušanu."],
    atkartojums="13.2.–13.6. stundā aplūkojām dažādus viļņus. Šodien "
                "noskaidrosim, kas VISIEM viļņiem ir kopīgs.",
    uzdevumu_apraksts="Atstarošanās, laušana un difrakcija",
    teorija=[
        ("Četras viļņu īpašības", [
            ("kartitas", [
                ("ATSTAROŠANĀS", BLUE,
                 ["Vilnis atlec no šķēršļa.",
                  "Krišanas leņķis = atstarošanās leņķis.",
                  "Atbalss, spogulis, radars."]),
                ("LAUŠANA", GREEN,
                 ["Vilnis maina virzienu, pārejot citā vidē.",
                  "Mainās ātrums un viļņa garums,",
                  "frekvence paliek tā pati.",
                  "Salmiņš ūdenī izskatās saliekts."]),
                ("INTERFERENCE", GOLD,
                 ["Divi viļņi pārklājas.",
                  "Kalns + kalns → pastiprinās.",
                  "Kalns + ieleja → dzēš viens otru.",
                  "Ziepju burbuļa krāsas."]),
            ]),
            ("panelis", "DIFRAKCIJA — viļņu apliekšanās",
             ["Vilnis liecas ap šķērsli vai izplatās aiz šauras spraugas. Jo "
              "lielāks viļņa garums salīdzinājumā ar šķērsli, jo vairāk "
              "vilnis liecas.",
              "Tāpēc skaņu (λ ~ 1 m) dzirdam aiz stūra, bet gaismu "
              "(λ ~ 500 nm) — neredzam."], NAVY),
        ]),
        ("Kā tas izpaužas", [
            ("tabula",
             ["Parādība", "Skaņā", "Gaismā"],
             [["Atstarošanās", "atbalss klintī", "attēls spogulī"],
              ["Laušana", "skaņa liecas siltā gaisā", "salmiņš ūdenī"],
              ["Interference", "skaņas “klusie punkti” zālē",
               "ziepju burbuļa krāsas"],
              ["Difrakcija", "dzirdam aiz stūra", "difrakcijas režģis"]],
             [3.63, 4.30, 4.30]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atstarošanās leņķis",
             teksts="Gaismas stars krīt uz spoguli 35° leņķī pret spoguļa "
                    "virsmu.\n"
                    "Aprēķini krišanas un atstarošanās leņķi, mērot no "
                    "perpendikula!",
             dots=["leņķis pret virsmu = 35°"],
             jaaprekina=["α = ?", "β = ?"],
             formulas=["Leņķi mēra no perpendikula: α = 90° − 35°",
                       "β = α"],
             aprekins=["1)  α = 90° − 35° = 55°",
                       "2)  β = α = 55°"],
             atbilde="α = β = 55°",
             piezime="Optikā leņķus vienmēr mēra no perpendikula, nevis no "
                     "virsmas."),
        dict(nr=2, virsraksts="Viļņa garums citā vidē",
             teksts="Gaismas viļņa garums vakuumā ir 600 nm. Ūdenī gaismas "
                    "ātrums ir 2,25·10⁸ m/s.\n"
                    "Aprēķini frekvenci un viļņa garumu ūdenī!",
             dots=["λ₁ = 600 nm ;  c = 3,00·10⁸ m/s",
                   "υ₂ = 2,25·10⁸ m/s"],
             jaaprekina=["f = ?", "λ₂ = ?"],
             formulas=["f = c / λ₁", "λ₂ = υ₂ / f"],
             aprekins=["1)  f = 3,00·10⁸ : 6,00·10⁻⁷ = 5,00·10¹⁴ Hz",
                       "2)  λ₂ = 2,25·10⁸ : 5,00·10¹⁴",
                       "3)  λ₂ = 4,50·10⁻⁷ m = 450 nm"],
             atbilde="f = 5,00·10¹⁴ Hz ;   λ₂ = 450 nm",
             piezime="Frekvence nemainās — mainās ātrums un viļņa garums. "
                     "Tāpēc krāsa paliek tā pati."),
        dict(nr=3, virsraksts="Difrakcija uz spraugas",
             teksts="Skaņas viļņa garums ir 1,7 m, durvju platums 0,80 m. "
                    "Gaismas viļņa garums 5,0·10⁻⁷ m.\n"
                    "Salīdzini λ ar spraugas platumu abos gadījumos!",
             dots=["λ₁ = 1,7 m ;  λ₂ = 5,0·10⁻⁷ m", "d = 0,80 m"],
             jaaprekina=["λ₁/d = ?", "λ₂/d = ?"],
             formulas=["Difrakcija manāma, ja λ ≥ d"],
             aprekins=["1)  λ₁ / d = 1,7 : 0,80 = 2,1",
                       "2)  λ₂ / d = 5,0·10⁻⁷ : 0,80 = 6,3·10⁻⁷",
                       "3)  Skaņai λ > d, gaismai λ ≪ d"],
             atbilde="Skaņa stipri liecas, gaisma praktiski neliecas",
             piezime="Tāpēc runu dzirdam aiz durvīm, bet cilvēku neredzam."),
        dict(nr=4, virsraksts="Interference",
             teksts="Divi skaļruņi izstaro skaņu ar viļņa garumu 0,50 m. "
                    "Klausītājs atrodas tā, ka ceļu starpība ir 0,25 m.\n"
                    "Vai skaņa pastiprināsies vai dzēsīsies?",
             dots=["λ = 0,50 m", "Δs = 0,25 m"],
             jaaprekina=["Δs / λ = ?"],
             formulas=["Pastiprinās, ja Δs = kλ",
                       "Dzēšas, ja Δs = (k + 0,5)λ"],
             aprekins=["1)  Δs / λ = 0,25 : 0,50 = 0,5",
                       "2)  Δs = 0,5λ — puse viļņa garuma",
                       "3)  Viļņi nāk pretfāzē"],
             atbilde="Skaņa dzēsīsies (klusais punkts)",
             piezime="Uz šī principa darbojas trokšņu slāpējošās austiņas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Visiem viļņiem piemīt atstarošanās, laušana, interference un "
            "difrakcija.",
            "Atstarojoties krišanas leņķis vienāds ar atstarošanās leņķi.",
            "Laužoties mainās ātrums un λ, bet frekvence paliek tā pati.",
            "Difrakcija manāma, kad λ ir salīdzināms ar šķēršļa izmēru.",
        ],
        majasdarbs=[
            "Stars krīt 20° leņķī pret virsmu. Aprēķini leņķi no "
            "perpendikula.",
            "λ = 500 nm vakuumā, stiklā υ = 2,0·10⁸ m/s. Aprēķini λ stiklā.",
            "Nosauc katrai viļņu īpašībai vienu piemēru skaņā un gaismā.",
        ],
        pasvertejums=["Protu nosaukt viļņu īpašības",
                      "Protu skaidrot laušanu",
                      "Protu skaidrot difrakciju",
                      "Protu risināt interferences uzdevumu"],
        nakama="Nākamā stunda: viļņi tehnoloģijās un veselībā."),
),

dict(
    nr="13.8", virsraksts="Viļņi tehnoloģijās un veselībā",
    jautajums="Kur viļņi noder un kuri viļņi ir bīstami?",
    apaksraksts="GPS · Lāzers · Rentgens · Aizsardzība · Gatavošanās PD8",
    merkis="Raksturot elektromagnētisko viļņu lietojumus, salīdzināt to "
           "ietekmi uz veselību un sagatavoties PD8.",
    protu=["raksturot EM viļņu lietojumus tehnoloģijās;",
           "salīdzināt UV, rentgena un gamma ietekmi;",
           "pamatot aizsardzības pasākumus;",
           "izvēlēties pareizo formulu temata uzdevumos."],
    atkartojums="Šī ir pēdējā stunda pirms PD8. Atkārtojam: f = 1/T, "
                "λ = υT, λ = c/f, s = υt/2, E = hf.",
    uzdevumu_apraksts="Viļņu lietojumi un temata jauktie uzdevumi",
    teorija=[
        ("Viļņi tehnoloģijās", [
            ("kartitas", [
                ("GPS", BLUE,
                 ["Satelīti raida signālus ar precīzu laiku.",
                  "Uztvērējs mēra signāla ceļošanas laiku.",
                  "No trim satelītiem nosaka vietu.",
                  "Precizitāte prasa relativitātes korekcijas."]),
                ("LĀZERS", GREEN,
                 ["Šaurs, vienas frekvences stars.",
                  "Optiskā šķiedra, skeneri, medicīna.",
                  "Griež metālu, veic acu operācijas.",
                  "Nedrīkst skatīties starā!"]),
                ("RENTGENS UN TERMOGRĀFIJA", GOLD,
                 ["Rentgens — kauli, drošības kontrole.",
                  "Infrasarkanais — siltuma noplūdes ēkās.",
                  "Termokamera redz temperatūras atšķirības.",
                  "Rentgenam vajadzīga aizsardzība."]),
            ]),
        ]),
        ("Temata formulas vienuviet", [
            ("tabula",
             ["Kas jāatrod", "Formula", "Kur lieto"],
             [["Periods, frekvence", "f = 1/T ;  T = t/N", "svārstības"],
              ["Viļņa garums", "λ = υ·T = υ/f", "mehāniskie viļņi"],
              ["EM viļņa garums", "λ = c/f ;  c = 3,00·10⁸ m/s", "EM viļņi"],
              ["Attālums pēc atbalss", "s = υ·t/2", "eholots, radars"],
              ["Fotona enerģija", "E = h·f", "EM skala, bīstamība"]],
             [3.63, 4.60, 4.00]),
            ("panelis", "BIEŽĀKĀS KĻŪDAS PD",
             ["aizmirst dalīt ar 2 atbalss uzdevumos  ·  MHz un GHz "
              "nepārvērš hercos  ·  nm nepārvērš metros  ·  skaņai lieto c "
              "gaismas ātruma vietā  ·  atbildē trūkst mērvienības."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="GPS satelīta signāls",
             teksts="GPS satelīts atrodas 2,0·10⁷ m attālumā.\n"
                    "Cik ilgi signāls ceļo līdz uztvērējam? "
                    "(c = 3,00·10⁸ m/s)",
             dots=["s = 2,0·10⁷ m", "c = 3,00·10⁸ m/s"],
             jaaprekina=["t = ?"],
             formulas=["t = s / c"],
             aprekins=["1)  t = 2,0·10⁷ : 3,00·10⁸",
                       "2)  t = 6,7·10⁻² s"],
             atbilde="t ≈ 0,067 s = 67 ms",
             piezime="GPS precizitātei laiks jāmēra ar nanosekunžu "
                     "precizitāti."),
        dict(nr=2, virsraksts="Lāzera fotoni",
             teksts="Lāzera viļņa garums ir 650 nm, jauda 5,0 mW.\n"
                    "Aprēķini fotona enerģiju un fotonu skaitu sekundē!",
             dots=["λ = 650 nm ;  P = 5,0 mW",
                   "h = 6,63·10⁻³⁴ ;  c = 3,00·10⁸"],
             jaaprekina=["E = ?", "N = ?"],
             formulas=["f = c/λ", "E = h·f", "N = P·t / E"],
             aprekins=["1)  f = 3,00·10⁸ : 6,50·10⁻⁷ = 4,62·10¹⁴ Hz",
                       "2)  E = 6,63·10⁻³⁴ · 4,62·10¹⁴ = 3,06·10⁻¹⁹ J",
                       "3)  N = 5,0·10⁻³ : 3,06·10⁻¹⁹ = 1,6·10¹⁶"],
             atbilde="E ≈ 3,1·10⁻¹⁹ J ;   N ≈ 1,6·10¹⁶ fotonu sekundē",
             piezime="650 nm ir sarkanā lāzera rādītāja krāsa."),
        dict(nr=3, virsraksts="Jaukts: skaņa un radars",
             teksts="a) Atbalss no sienas pēc 1,2 s (υ = 343 m/s). "
                    "b) Radara signāls atgriežas pēc 4,0·10⁻⁵ s.\n"
                    "Aprēķini abus attālumus!",
             dots=["t₁ = 1,2 s ;  υ = 343 m/s",
                   "t₂ = 4,0·10⁻⁵ s ;  c = 3,00·10⁸ m/s"],
             jaaprekina=["s₁ = ?", "s₂ = ?"],
             formulas=["s = υ · t / 2"],
             aprekins=["1)  s₁ = 343 · 1,2 : 2 = 206 m",
                       "2)  s₂ = 3,00·10⁸ · 4,0·10⁻⁵ : 2",
                       "3)  s₂ = 6,0·10³ m = 6,0 km"],
             atbilde="s₁ ≈ 2,1·10² m ;   s₂ = 6,0 km",
             piezime="Viena formula, divi dažādi ātrumi — svarīgi izvēlēties "
                     "pareizo."),
        dict(nr=4, virsraksts="Jaukts: svārstības un vilnis",
             teksts="Vilnis 20 s laikā veic 50 svārstības, viļņa garums "
                    "3,2 m.\n"
                    "Aprēķini periodu, frekvenci un izplatīšanās ātrumu!",
             dots=["N = 50 ;  t = 20 s", "λ = 3,2 m"],
             jaaprekina=["T = ?", "f = ?", "υ = ?"],
             formulas=["T = t/N", "f = 1/T", "υ = λ · f"],
             aprekins=["1)  T = 20 : 50 = 0,40 s",
                       "2)  f = 1 : 0,40 = 2,5 Hz",
                       "3)  υ = 3,2 · 2,5 = 8,0 m/s"],
             atbilde="T = 0,40 s ;  f = 2,5 Hz ;  υ = 8,0 m/s",
             piezime="Trīs soļi pēc kārtas — tipisks PD uzdevums par viļņiem."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "GPS, lāzers, radars, termogrāfija un rentgens — visi izmanto EM "
            "viļņus.",
            "Bīstamību nosaka fotona enerģija E = hf, nevis jauda vien.",
            "Atbalss un radara uzdevumos vienmēr dala ar 2.",
            "Frekvenci vienmēr izsaka hercos, viļņa garumu — metros.",
        ],
        majasdarbs=[
            "Atkārto 13.1.–13.7. stundas formulas un kopsavilkumus.",
            "λ = 780 nm lāzeram. Aprēķini frekvenci un fotona enerģiju.",
            "Eholots ūdenī: t = 0,60 s. Aprēķini dziļumu.",
        ],
        pasvertejums=["Protu raksturot lietojumus",
                      "Protu salīdzināt starojuma bīstamību",
                      "Protu izvēlēties pareizo formulu",
                      "Esmu gatavs pārbaudes darbam"],
        nakama="Nākamā stunda: PD8 — Viļņi dabā un tehnikā."),
),
]


def build():
    return C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
