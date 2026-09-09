# -*- coding: utf-8 -*-
"""2. temats "Vienmērīgi paātrināta kustība". A daļa: 2.1.-2.7. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "2. temats. Vienmērīgi paātrināta kustība"
KICKER = "FIZIKA I · 10. KLASE · 2. TEMATS: VIENMĒRĪGI PAĀTRINĀTA KUSTĪBA"
KURSS = "FIZIKA I · 10. KLASE"
MAPE = "C:/aphysics/Fizika_1/2. Vienmērīga paātrināta kustība"

STUNDAS = [

dict(
    nr="2.1", virsraksts="Paātrinājums",
    jautajums="Ko nozīmē «no 0 līdz 100 sešās sekundēs»?",
    apaksraksts="a = Δv/Δt · [a] = m/s² · Paātrinājums un bremzēšana",
    merkis="Iemācīties definēt paātrinājumu, aprēķināt to no ātruma "
           "izmaiņas un pareizi interpretēt tā zīmi.",
    protu=["definēt paātrinājumu un nosaukt tā mērvienību;",
           "aprēķināt a = Δv/Δt;",
           "izskaidrot paātrinājuma zīmes nozīmi;",
           "atšķirt paātrināšanos no bremzēšanas."],
    atkartojums="1. tematā ātrums bija nemainīgs. Reālā kustībā tas "
                "mainās - un tieši ātruma izmaiņas ātrumu sauc par "
                "paātrinājumu.",
    uzdevumu_apraksts="Paātrinājuma aprēķins un zīmes noteikšana",
    teorija=[
        ("Kas ir paātrinājums", [
            ("formula", "PAĀTRINĀJUMA DEFINĪCIJA",
             "a = Δv / Δt = (v − v₀) / t        [a] = m/s²",
             "Paātrinājums rāda, par cik mainās ātrums KATRĀ sekundē. "
             "a = 3 m/s² nozīmē: katrā sekundē ātrums pieaug par 3 m/s.",
             GOLD),
            ("kartitas", [
                ("a > 0", GREEN,
                 ["Ātruma projekcija aug.",
                  "Ja v > 0 - kustība paātrinās.",
                  "Piemērs: starts no vietas."]),
                ("a < 0", RED,
                 ["Ātruma projekcija sarūk.",
                  "Ja v > 0 - bremzēšana.",
                  "Piemērs: apstāšanās pie luksofora."]),
                ("a = 0", GREY,
                 ["Ātrums nemainās.",
                  "Vienmērīga kustība.",
                  "1. temata gadījums."]),
            ]),
        ]),
        ("Tipiskas vērtības", [
            ("tabula",
             ["Situācija", "Paātrinājums", "Piezīme"],
             [["Brīvā krišana", "9,81 m/s²", "g - konstante"],
              ["Vieglā automašīna", "3-5 m/s²", "0-100 km/h 6-9 s"],
              ["Ārkārtas bremzēšana", "−7 m/s²", "uz sausa asfalta"],
              ["Lifts", "0,5-1,5 m/s²", "lai būtu ērti"],
              ["Sprinteris startā", "~4 m/s²", "pirmajās sekundēs"]],
             [4.60, 3.60, 4.03]),
            ("panelis", "UZMANĪBU AR ZĪMĒM",
             ["Negatīvs paātrinājums NE VIENMĒR nozīmē bremzēšanu. Ja "
              "ķermenis kustas pretēji asij (v < 0) un a < 0, tas "
              "paātrinās. Bremzēšana ir tad, kad a un v zīmes ir "
              "PRETĒJAS."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Paātrinājums no reklāmas",
             teksts="Automašīna no miera stāvokļa sasniedz 108 km/h "
                    "6,0 s laikā.\nAprēķini paātrinājumu!",
             dots=["v₀ = 0", "v = 108 km/h = 30 m/s", "t = 6,0 s"],
             jaaprekina=["a = ?"],
             formulas=["a = (v − v₀)/t"],
             aprekins=["1)  v = 108 : 3,6 = 30 m/s",
                       "2)  a = (30 − 0) : 6,0",
                       "3)  a = 5,0 m/s²"],
             atbilde="a = 5,0 m/s²",
             piezime="Katrā sekundē ātrums pieaug par 5 m/s = 18 km/h."),
        dict(nr=2, virsraksts="Bremzēšana",
             teksts="Automašīna no 72 km/h apstājas 4,0 s laikā.\n"
                    "Aprēķini paātrinājumu!",
             dots=["v₀ = 72 km/h = 20 m/s", "v = 0", "t = 4,0 s"],
             jaaprekina=["a = ?"],
             formulas=["a = (v − v₀)/t"],
             aprekins=["1)  v₀ = 72 : 3,6 = 20 m/s",
                       "2)  a = (0 − 20) : 4,0",
                       "3)  a = −5,0 m/s²"],
             atbilde="a = −5,0 m/s² (bremzēšana)",
             piezime="Mīnusa zīme kopā ar v > 0 nozīmē ātruma "
                     "samazināšanos."),
        dict(nr=3, virsraksts="Ātrums pēc dotā laika",
             teksts="Velosipēdists brauc 4,0 m/s un paātrinās ar "
                    "0,80 m/s².\nCik liels būs ātrums pēc 5,0 s?",
             dots=["v₀ = 4,0 m/s", "a = 0,80 m/s²", "t = 5,0 s"],
             jaaprekina=["v = ?"],
             formulas=["v = v₀ + at"],
             aprekins=["1)  at = 0,80 · 5,0 = 4,0 m/s",
                       "2)  v = 4,0 + 4,0",
                       "3)  v = 8,0 m/s"],
             atbilde="v = 8,0 m/s = 28,8 km/h",
             piezime="Ātrums dubultojās - loģiski, jo pieaugums vienāds "
                     "ar sākuma ātrumu."),
        dict(nr=4, virsraksts="Laiks līdz apstāšanās",
             teksts="Vilciens brauc 90 km/h un bremzē ar paātrinājumu\n"
                    "−0,50 m/s². Pēc cik ilga laika tas apstāsies?",
             dots=["v₀ = 90 km/h = 25 m/s", "v = 0", "a = −0,50 m/s²"],
             jaaprekina=["t = ?"],
             formulas=["v = v₀ + at", "t = (v − v₀)/a"],
             aprekins=["1)  v₀ = 90 : 3,6 = 25 m/s",
                       "2)  t = (0 − 25) : (−0,50)",
                       "3)  t = 50 s"],
             atbilde="t = 50 s",
             piezime="Vilcieniem bremzēšana ir lēna - tāpēc bremzēšanas "
                     "ceļš ir ļoti garš."),
        dict(nr=5, virsraksts="Sākuma ātrums",
             teksts="Ķermenis paātrinās ar 3,0 m/s² un pēc 5,0 s tā "
                    "ātrums\nir 25 m/s. Cik liels bija sākuma ātrums?",
             dots=["a = 3,0 m/s²", "t = 5,0 s", "v = 25 m/s"],
             jaaprekina=["v₀ = ?"],
             formulas=["v = v₀ + at", "v₀ = v − at"],
             aprekins=["1)  at = 3,0 · 5,0 = 15 m/s",
                       "2)  v₀ = 25 − 15",
                       "3)  v₀ = 10 m/s"],
             atbilde="v₀ = 10 m/s = 36 km/h",
             piezime="Formulu var izteikt attiecībā pret jebkuru "
                     "lielumu - pārkārtošana ir daļa no risinājuma."),
        dict(nr=6, virsraksts="Paātrinājums no tabulas",
             teksts="Mērījumi: t = 0 s → v = 2,0 m/s;  t = 2,0 s → "
                    "v = 8,0 m/s;\nt = 4,0 s → v = 14 m/s. Vai kustība "
                    "ir vienmērīgi\npaātrināta un cik liels ir a?",
             dots=["v(0) = 2,0 m/s", "v(2,0) = 8,0 m/s",
                   "v(4,0) = 14 m/s"],
             jaaprekina=["a = ?", "vai a = const?"],
             formulas=["a = Δv/Δt"],
             aprekins=["1)  a₁ = (8,0 − 2,0) : 2,0 = 3,0 m/s²",
                       "2)  a₂ = (14 − 8,0) : 2,0 = 3,0 m/s²",
                       "3)  a₁ = a₂ → kustība vienmērīgi paātrināta"],
             atbilde="a = 3,0 m/s²; kustība ir vienmērīgi paātrināta.",
             piezime="Vienādi ātruma pieaugumi vienādos laika sprīžos - "
                     "tā ir vienmērīgi paātrinātas kustības pazīme."),
        dict(nr=7, virsraksts="Divu automašīnu salīdzinājums",
             teksts="Pirmā automašīna paātrinās ar 2,5 m/s², otrā ar "
                    "4,0 m/s².\nAbas sāk no miera. Cik ilgā laikā katra "
                    "sasniedz 20 m/s?",
             dots=["a₁ = 2,5 m/s²", "a₂ = 4,0 m/s²", "v = 20 m/s"],
             jaaprekina=["t₁ = ?", "t₂ = ?"],
             formulas=["v = at", "t = v/a"],
             aprekins=["1)  t₁ = 20 : 2,5 = 8,0 s",
                       "2)  t₂ = 20 : 4,0 = 5,0 s",
                       "3)  Starpība: 3,0 s"],
             atbilde="t₁ = 8,0 s ;   t₂ = 5,0 s (par 3,0 s ātrāk)",
             piezime="Lielāks paātrinājums nozīmē īsāku laiku, nevis "
                     "lielāku gala ātrumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Paātrinājums a = Δv/Δt rāda ātruma izmaiņu vienā sekundē.",
            "[a] = m/s².",
            "Bremzēšana ir tad, kad a un v zīmes ir pretējas.",
            "v = v₀ + at.",
        ],
        majasdarbs=[
            "v₀ = 0, v = 54 km/h, t = 5,0 s. Aprēķini a.",
            "v₀ = 15 m/s, a = −3,0 m/s². Pēc cik ilga laika ķermenis "
            "apstāsies?",
            "v₀ = 2,0 m/s, a = 1,5 m/s², t = 8,0 s. Aprēķini v.",
        ],
        pasvertejums=["Protu definēt paātrinājumu",
                      "Protu aprēķināt a",
                      "Protu izskaidrot zīmi",
                      "Protu lietot v = v₀ + at"],
        nakama="Nākamā stunda: ātruma vienādojums un grafiks."),
),

dict(
    nr="2.2", virsraksts="Ātruma vienādojums un grafiks",
    jautajums="Kā mainās ātrums, ja paātrinājums ir nemainīgs?",
    apaksraksts="v = v₀ + at · Grafiks v(t) · Slīpums = a",
    merkis="Iemācīties lietot ātruma vienādojumu un lasīt v(t) grafiku "
           "vienmērīgi paātrinātā kustībā.",
    protu=["pierakstīt v = v₀ + at;",
           "no v(t) grafika noteikt v₀ un a;",
           "atpazīt paātrināšanos un bremzēšanu grafikā;",
           "uzzīmēt v(t) grafiku pēc vienādojuma."],
    atkartojums="2.1. stundā: a = Δv/Δt. No šīs definīcijas tieši izriet "
                "ātruma vienādojums v = v₀ + at.",
    uzdevumu_apraksts="Ātruma vienādojums un v(t) grafika lasīšana",
    teorija=[
        ("Ātruma vienādojums", [
            ("formula", "VIENMĒRĪGI PAĀTRINĀTA KUSTĪBA",
             "vₓ = v₀ₓ + aₓ · t",
             "Visi trīs lielumi ir projekcijas ar zīmi. Grafiks v(t) ir "
             "TAISNE: v₀ - krustpunkts ar v asi, a - taisnes slīpums.",
             GOLD),
            ("tabula",
             ["v(t) grafiks", "v₀", "a", "Kustība"],
             [["Augoša taisne no 0", "0", "> 0", "Starts no vietas"],
              ["Augoša taisne no v₀", "> 0", "> 0", "Paātrinās"],
              ["Dilstoša taisne", "> 0", "< 0", "Bremzē"],
              ["Horizontāla taisne", "> 0", "0", "Vienmērīga"]],
             [4.30, 2.20, 2.20, 3.53]),
        ]),
        ("Ko rāda grafika laukums", [
            ("panelis", "LAUKUMS ZEM v(t) GRAFIKA = CEĻŠ",
             ["Vienmērīgi paātrinātā kustībā laukums zem taisnes ir "
              "trapece vai trijstūris. Tieši no šī laukuma nākamajā "
              "stundā iegūsim pārvietojuma formulu."], NAVY),
            ("kartitas", [
                ("SLĪPUMS", BLUE,
                 ["a = (v₂ − v₁)/(t₂ − t₁)",
                  "Stāvāka taisne - lielāks a."]),
                ("KRUSTPUNKTS", GREEN,
                 ["v₀ pie t = 0.",
                  "Var būt arī nulle."]),
                ("SASKARE AR ASI", RED,
                 ["Vieta, kur v = 0.",
                  "Apstāšanās brīdis."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vienādojuma lasīšana",
             teksts="Dots v = 12 + 3t  (m/s; s).\n"
                    "Nosaki v₀, a un ātrumu pēc 6,0 s!",
             dots=["v = 12 + 3t"],
             jaaprekina=["v₀ = ?", "a = ?", "v(6 s) = ?"],
             formulas=["v = v₀ + at"],
             aprekins=["1)  v₀ = 12 m/s",
                       "2)  a = 3,0 m/s²",
                       "3)  v = 12 + 3·6 = 30 m/s"],
             atbilde="v₀ = 12 m/s ;  a = 3,0 m/s² ;  v(6 s) = 30 m/s",
             piezime="Vienādojums der jebkuram laikam, kamēr "
                     "paātrinājums nemainās."),
        dict(nr=2, virsraksts="Paātrinājums no grafika",
             teksts="v(t) taisne iet caur (0 s; 5,0 m/s) un\n"
                    "(8,0 s; 21 m/s). Aprēķini a un uzraksti "
                    "vienādojumu!",
             dots=["(0; 5,0)", "(8,0; 21)"],
             jaaprekina=["a = ?", "v(t) = ?"],
             formulas=["a = Δv/Δt", "v = v₀ + at"],
             aprekins=["1)  Δv = 21 − 5,0 = 16 m/s",
                       "2)  a = 16 : 8,0 = 2,0 m/s²",
                       "3)  v = 5,0 + 2,0t"],
             atbilde="a = 2,0 m/s² ;   v = 5,0 + 2,0t  (m/s; s)",
             piezime="Slīpums nolasāms tāpat kā x(t) grafikā - tikai "
                     "nozīme cita."),
        dict(nr=3, virsraksts="Bremzēšanas vienādojums",
             teksts="v = 24 − 4t  (m/s; s).\nKad ķermenis apstāsies un "
                    "kāds būs ātrums pēc 4,0 s?",
             dots=["v₀ = 24 m/s", "a = −4,0 m/s²"],
             jaaprekina=["t (v=0) = ?", "v(4 s) = ?"],
             formulas=["v = v₀ + at", "0 = v₀ + at"],
             aprekins=["1)  0 = 24 − 4t → t = 6,0 s",
                       "2)  v(4) = 24 − 16 = 8,0 m/s",
                       "3)  Pēc 6,0 s formula vairs neder"],
             atbilde="Apstājas pēc 6,0 s ;   v(4 s) = 8,0 m/s",
             piezime="Pēc apstāšanās ķermenis nesāk kustēties atpakaļ - "
                     "formulu tālāk nelieto."),
        dict(nr=4, virsraksts="Ceļš no grafika laukuma",
             teksts="v(t) taisne no 0 līdz 20 m/s 10 s laikā.\n"
                    "Aprēķini ceļu, izmantojot laukumu zem grafika!",
             dots=["v₀ = 0", "v = 20 m/s", "t = 10 s"],
             jaaprekina=["s = ?"],
             formulas=["s = laukums = ½ · pamats · augstums"],
             aprekins=["1)  Figūra - taisnleņķa trijstūris",
                       "2)  s = ½ · 10 · 20",
                       "3)  s = 100 m"],
             atbilde="s = 100 m",
             piezime="Tas pats, ko dotu formula s = (v₀+v)/2 · t = "
                     "10 · 10 = 100 m ✔"),
        dict(nr=5, virsraksts="Bremzēšana grafikā",
             teksts="v(t) taisne krīt no 30 m/s līdz 0 laikā 12 s.\n"
                    "Aprēķini paātrinājumu un bremzēšanas ceļu!",
             dots=["v₀ = 30 m/s", "v = 0", "t = 12 s"],
             jaaprekina=["a = ?", "s = ?"],
             formulas=["a = (v − v₀)/t", "s = ½ · t · v₀"],
             aprekins=["1)  a = (0 − 30) : 12 = −2,5 m/s²",
                       "2)  Laukums - taisnleņķa trijstūris",
                       "3)  s = ½ · 12 · 30 = 180 m"],
             atbilde="a = −2,5 m/s² ;   s = 180 m",
             piezime="Laukums zem v(t) grafika ir ceļš arī tad, ja "
                     "ātrums samazinās."),
        dict(nr=6, virsraksts="Divi posmi v(t) grafikā",
             teksts="v(t) grafikā ātrums aug no 0 līdz 10 m/s laikā "
                    "0-5,0 s,\ntad paliek nemainīgs līdz 15 s. Aprēķini "
                    "kopējo ceļu!",
             dots=["I: 0 → 10 m/s, t₁ = 5,0 s",
                   "II: v = 10 m/s, t₂ = 10 s"],
             jaaprekina=["s = ?"],
             formulas=["s₁ = ½ · t₁ · v", "s₂ = v · t₂"],
             aprekins=["1)  s₁ = ½ · 5,0 · 10 = 25 m",
                       "2)  s₂ = 10 · 10 = 100 m",
                       "3)  s = 25 + 100 = 125 m"],
             atbilde="s = 125 m",
             piezime="Grafiku sadala trijstūrī un taisnstūrī - tā ir "
                     "ātrākā metode."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "v = v₀ + at - ātruma vienādojums.",
            "v(t) grafiks ir taisne; tās slīpums ir paātrinājums.",
            "Krustpunkts ar v asi ir v₀.",
            "Laukums zem v(t) grafika ir ceļš.",
        ],
        majasdarbs=[
            "v = 6 + 2,5t. Nosaki v₀, a un v pēc 8 s.",
            "v = 30 − 6t. Kad ķermenis apstāsies?",
            "v(t) taisne no 4 m/s līdz 16 m/s 6 s laikā. Aprēķini a un "
            "ceļu.",
        ],
        pasvertejums=["Protu pierakstīt v = v₀ + at",
                      "Protu nolasīt a no grafika",
                      "Protu atpazīt bremzēšanu",
                      "Protu atrast ceļu no laukuma"],
        nakama="Nākamā stunda: pārvietojums paātrinātā kustībā."),
),

dict(
    nr="2.3", virsraksts="Pārvietojums paātrinātā kustībā",
    jautajums="Kāpēc laukums zem grafika ir ceļš?",
    apaksraksts="s = v₀t + at²/2 · s = (v₀+v)/2 · t · v² − v₀² = 2as",
    merkis="Iemācīties trīs pārvietojuma formulas un izvēlēties starp "
           "tām atbilstoši dotajiem lielumiem.",
    protu=["lietot s = v₀t + at²/2;",
           "lietot s = (v₀ + v)/2 · t;",
           "lietot v² − v₀² = 2as;",
           "izvēlēties formulu pēc dotajiem lielumiem."],
    atkartojums="2.2. stundā redzējām, ka ceļš ir laukums zem v(t) "
                "grafika. Tagad šo laukumu izteiksim ar formulu.",
    uzdevumu_apraksts="Trīs pārvietojuma formulas un to izvēle",
    teorija=[
        ("Trīs pamatformulas", [
            ("formula", "PĀRVIETOJUMS PAĀTRINĀTĀ KUSTĪBĀ",
             "s = v₀t + at²/2        s = (v₀ + v)/2 · t        "
             "v² − v₀² = 2as",
             "Visas trīs ir savstarpēji saistītas. Formulu izvēlas pēc "
             "tā, kurš lielums NAV dots un nav jāatrod.", GOLD),
            ("tabula",
             ["Ja nav dots...", "Lieto formulu", "Piemērs"],
             [["Gala ātrums v", "s = v₀t + at²/2", "Cik tālu 5 s laikā"],
              ["Paātrinājums a", "s = (v₀+v)/2 · t", "Vidējais ātrums"],
              ["Laiks t", "v² − v₀² = 2as", "Bremzēšanas ceļš"]],
             [3.80, 4.30, 4.13]),
        ]),
        ("Kā rodas formula", [
            ("panelis", "NO LAUKUMA UZ FORMULU",
             ["Laukums zem v(t) taisnes ir trapece: apakšējā mala v₀, "
              "augšējā v, augstums t.",
              "S = (v₀ + v)/2 · t",
              "Ievietojot v = v₀ + at, iegūst:",
              "s = v₀t + at²/2"], NAVY),
            ("kartitas", [
                ("NO MIERA", GREEN,
                 ["v₀ = 0",
                  "s = at²/2",
                  "v² = 2as"]),
                ("LĪDZ APSTĀŠANĀS", RED,
                 ["v = 0",
                  "s = v₀t − |a|t²/2",
                  "s = v₀² / (2|a|)"]),
                ("VISPĀRĪGI", BLUE,
                 ["Abi ātrumi ≠ 0",
                  "Lieto pilnās formulas.",
                  "Uzmani zīmes!"]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ceļš no miera stāvokļa",
             teksts="Automašīna sāk kustību ar paātrinājumu 2,5 m/s².\n"
                    "Cik lielu ceļu tā veiks 8,0 s laikā?",
             dots=["v₀ = 0", "a = 2,5 m/s²", "t = 8,0 s"],
             jaaprekina=["s = ?"],
             formulas=["s = v₀t + at²/2", "v₀ = 0 → s = at²/2"],
             aprekins=["1)  t² = 64 s²",
                       "2)  s = 2,5 · 64 : 2",
                       "3)  s = 80 m"],
             atbilde="s = 80 m",
             piezime="Pārbaude: v = 2,5·8 = 20 m/s; s = (0+20)/2 · 8 = "
                     "80 m ✔"),
        dict(nr=2, virsraksts="Bremzēšanas ceļš",
             teksts="Automašīna brauc 90 km/h un bremzē ar "
                    "−5,0 m/s².\nAprēķini bremzēšanas ceļu!",
             dots=["v₀ = 90 km/h = 25 m/s", "v = 0", "a = −5,0 m/s²"],
             jaaprekina=["s = ?"],
             formulas=["v² − v₀² = 2as", "s = (v² − v₀²)/(2a)"],
             aprekins=["1)  v₀ = 25 m/s ;  v₀² = 625 m²/s²",
                       "2)  s = (0 − 625) : (2·(−5,0))",
                       "3)  s = −625 : (−10) = 62,5 m"],
             atbilde="s = 62,5 m ≈ 63 m",
             piezime="Šeit laiks nav dots un nav jāatrod - tāpēc "
                     "trešā formula."),
        dict(nr=3, virsraksts="Ceļš caur vidējo ātrumu",
             teksts="Vilciens paātrinās no 36 km/h līdz 108 km/h "
                    "40 s laikā.\nAprēķini ceļu!",
             dots=["v₀ = 36 km/h = 10 m/s", "v = 108 km/h = 30 m/s",
                   "t = 40 s"],
             jaaprekina=["s = ?"],
             formulas=["s = (v₀ + v)/2 · t"],
             aprekins=["1)  v₀ = 10 m/s ;  v = 30 m/s",
                       "2)  (v₀+v)/2 = 20 m/s",
                       "3)  s = 20 · 40 = 800 m"],
             atbilde="s = 800 m",
             piezime="Paātrinājums nebija vajadzīgs - izvēlēta pareizā "
                     "formula."),
        dict(nr=4, virsraksts="Divkāršs ātrums",
             teksts="Kā mainīsies bremzēšanas ceļš, ja ātrumu palielina\n"
                    "2 reizes? Pamato ar formulu!",
             dots=["v₂ = 2v₁", "a nemainās"],
             jaaprekina=["s₂/s₁ = ?"],
             formulas=["s = v₀² / (2|a|)"],
             aprekins=["1)  s₁ = v₁² / (2|a|)",
                       "2)  s₂ = (2v₁)² / (2|a|) = 4v₁² / (2|a|)",
                       "3)  s₂ / s₁ = 4"],
             atbilde="Bremzēšanas ceļš palielinās 4 reizes.",
             piezime="Tāpēc pilsētā 50 km/h vietā 100 km/h nozīmē "
                     "četrreiz garāku bremzēšanas ceļu."),
        dict(nr=5, virsraksts="Ceļš piektajā sekundē",
             teksts="Ķermenis sāk kustību no miera ar paātrinājumu "
                    "2,0 m/s².\nCik lielu ceļu tas veic tieši piektajā "
                    "sekundē?",
             dots=["v₀ = 0", "a = 2,0 m/s²", "no t = 4,0 s līdz 5,0 s"],
             jaaprekina=["Δs = ?"],
             formulas=["s = at²/2", "Δs = s₅ − s₄"],
             aprekins=["1)  s₅ = 2,0 · 25 : 2 = 25 m",
                       "2)  s₄ = 2,0 · 16 : 2 = 16 m",
                       "3)  Δs = 25 − 16 = 9,0 m"],
             atbilde="Δs = 9,0 m",
             piezime="Ceļi secīgās sekundēs attiecas kā 1 : 3 : 5 : 7 : 9 "
                     "- to var izmantot pārbaudei."),
        dict(nr=6, virsraksts="Sākuma ātrums no ceļa",
             teksts="Ķermenis 5,0 s laikā veic 100 m, paātrinoties ar\n"
                    "2,0 m/s². Cik liels bija sākuma ātrums?",
             dots=["s = 100 m", "t = 5,0 s", "a = 2,0 m/s²"],
             jaaprekina=["v₀ = ?"],
             formulas=["s = v₀t + at²/2", "v₀ = (s − at²/2)/t"],
             aprekins=["1)  at²/2 = 2,0 · 25 : 2 = 25 m",
                       "2)  v₀t = 100 − 25 = 75 m",
                       "3)  v₀ = 75 : 5,0 = 15 m/s"],
             atbilde="v₀ = 15 m/s = 54 km/h",
             piezime="Pārbaude: v = 15 + 2·5 = 25 m/s; "
                     "s = (15+25)/2 · 5 = 100 m ✔"),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "s = v₀t + at²/2 - kad nav dots gala ātrums.",
            "s = (v₀ + v)/2 · t - kad nav dots paātrinājums.",
            "v² − v₀² = 2as - kad nav dots laiks.",
            "Bremzēšanas ceļš aug proporcionāli ātruma kvadrātam.",
        ],
        majasdarbs=[
            "v₀ = 0, a = 3,0 m/s², t = 6,0 s. Aprēķini s un v.",
            "v₀ = 20 m/s, v = 0, s = 50 m. Aprēķini a.",
            "v₀ = 5,0 m/s, v = 15 m/s, t = 4,0 s. Aprēķini s.",
        ],
        pasvertejums=["Protu lietot visas trīs formulas",
                      "Protu izvēlēties pareizo",
                      "Protu rēķināt bremzēšanas ceļu",
                      "Protu pamatot atkarību no v²"],
        nakama="Nākamā stunda: kustības vienādojums."),
),

dict(
    nr="2.4", virsraksts="Kustības vienādojums",
    jautajums="Kur ķermenis atradīsies pēc 5 sekundēm?",
    apaksraksts="x = x₀ + v₀t + at²/2 · Parabola · Koordināta",
    merkis="Iemācīties pierakstīt vienmērīgi paātrinātas kustības "
           "vienādojumu un no tā aprēķināt koordinātu jebkurā brīdī.",
    protu=["pierakstīt x = x₀ + v₀t + at²/2;",
           "no vienādojuma nolasīt x₀, v₀ un a;",
           "aprēķināt koordinātu dotā brīdī;",
           "atpazīt x(t) parabolas formu."],
    atkartojums="1.8. stundā vienmērīgai kustībai bija x = x₀ + vt. "
                "Tagad pievienojas loceklis ar t² - un grafiks kļūst par "
                "parabolu.",
    uzdevumu_apraksts="Kustības vienādojums un koordinātas aprēķins",
    teorija=[
        ("Pilnais kustības vienādojums", [
            ("formula", "VIENMĒRĪGI PAĀTRINĀTA KUSTĪBA",
             "x = x₀ + v₀ₓ · t + aₓ · t² / 2",
             "Trīs locekļi: sākuma vieta, vienmērīgā daļa un paātrinātā "
             "daļa. Visi lielumi - projekcijas ar zīmi.", GOLD),
            ("tabula",
             ["Loceklis", "Ko nozīmē", "Ja tā nav"],
             [["x₀", "Sākuma koordināta", "Sāk no nulles"],
              ["v₀t", "Vienmērīgā daļa", "Sāk no miera"],
              ["at²/2", "Paātrinājuma devums", "Vienmērīga kustība"]],
             [2.90, 4.60, 4.73]),
        ]),
        ("Grafiks x(t)", [
            ("divi",
             ("PARABOLA", BLUE,
              ["x(t) grafiks vairs nav taisne.",
               "a > 0 - zari uz augšu.",
               "a < 0 - zari uz leju.",
               "Slīpums katrā punktā = momentānais ātrums."]),
             ("KĀ LASĪT", GREEN,
              ["Krustpunkts ar x asi - x₀.",
               "Sākuma slīpums - v₀.",
               "Izliekums - paātrinājums.",
               "Virsotne - vieta, kur v = 0."])),
            ("panelis", "PĀRBAUDE AR MĒRVIENĪBĀM",
             ["at²/2 = m/s² · s² = m ✔",
              "Ja mērvienības nesaiet kopā, formula ir uzrakstīta "
              "nepareizi. To vienmēr vērts pārbaudīt pirms "
              "rēķināšanas."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vienādojuma lasīšana",
             teksts="x = 10 + 4t + 1,5t²  (m; s).\n"
                    "Nosaki x₀, v₀ un a; aprēķini x pēc 4,0 s!",
             dots=["x = 10 + 4t + 1,5t²"],
             jaaprekina=["x₀, v₀, a = ?", "x(4 s) = ?"],
             formulas=["x = x₀ + v₀t + at²/2"],
             aprekins=["1)  x₀ = 10 m ;  v₀ = 4,0 m/s",
                       "2)  a/2 = 1,5 → a = 3,0 m/s²",
                       "3)  x = 10 + 16 + 1,5·16 = 50 m"],
             atbilde="x₀ = 10 m ; v₀ = 4,0 m/s ; a = 3,0 m/s² ; "
                     "x(4 s) = 50 m",
             piezime="Uzmanību: koeficients pie t² ir a/2, nevis a!"),
        dict(nr=2, virsraksts="Vienādojuma sastādīšana",
             teksts="Ķermenis sāk kustību no punkta x₀ = −8,0 m ar "
                    "ātrumu\n6,0 m/s un paātrinājumu −2,0 m/s².\n"
                    "Uzraksti vienādojumu un atrodi x pēc 3,0 s!",
             dots=["x₀ = −8,0 m", "v₀ = 6,0 m/s", "a = −2,0 m/s²"],
             jaaprekina=["x(t) = ?", "x(3 s) = ?"],
             formulas=["x = x₀ + v₀t + at²/2"],
             aprekins=["1)  a/2 = −1,0 → x = −8 + 6t − t²",
                       "2)  x(3) = −8 + 18 − 9",
                       "3)  x(3) = 1,0 m"],
             atbilde="x = −8 + 6t − t²  (m; s) ;   x(3 s) = 1,0 m",
             piezime="Ķermenis paspēja pāriet no negatīvās uz pozitīvo "
                     "pusi."),
        dict(nr=3, virsraksts="Apstāšanās vieta",
             teksts="x = 5 + 20t − 2t²  (m; s).\n"
                    "Kad ķermenis apstāsies un kur tas būs?",
             dots=["v₀ = 20 m/s", "a = −4,0 m/s²", "x₀ = 5,0 m"],
             jaaprekina=["t = ?", "x = ?"],
             formulas=["v = v₀ + at = 0", "x = x₀ + v₀t + at²/2"],
             aprekins=["1)  0 = 20 − 4t → t = 5,0 s",
                       "2)  x = 5 + 20·5 − 2·25",
                       "3)  x = 5 + 100 − 50 = 55 m"],
             atbilde="Apstājas pēc 5,0 s punktā x = 55 m.",
             piezime="Tā ir parabolas virsotne - tālāk ķermenis sāktu "
                     "kustēties atpakaļ."),
        dict(nr=4, virsraksts="Divi ķermeņi",
             teksts="x₁ = 100 − 5t un x₂ = 2t²  (m; s).\n"
                    "Kad tie satiksies?",
             dots=["x₁ = 100 − 5t", "x₂ = 2t²"],
             jaaprekina=["t = ?"],
             formulas=["x₁ = x₂"],
             aprekins=["1)  100 − 5t = 2t²",
                       "2)  2t² + 5t − 100 = 0",
                       "3)  t = (−5 + √(25 + 800)) : 4 = "
                       "(−5 + 28,7) : 4 ≈ 5,9 s"],
             atbilde="t ≈ 5,9 s",
             piezime="Negatīvo sakni atmet - laiks nevar būt negatīvs."),
        dict(nr=5, virsraksts="No x(t) uz v(t)",
             teksts="x = 4 + 2t + 0,5t²  (m; s).\n"
                    "Uzraksti ātruma vienādojumu un aprēķini v un x "
                    "pēc 6,0 s!",
             dots=["x = 4 + 2t + 0,5t²"],
             jaaprekina=["v(t) = ?", "v(6 s) = ?", "x(6 s) = ?"],
             formulas=["x = x₀ + v₀t + at²/2", "v = v₀ + at"],
             aprekins=["1)  v₀ = 2,0 m/s ;  a/2 = 0,5 → a = 1,0 m/s²",
                       "2)  v = 2 + 1,0t → v(6) = 8,0 m/s",
                       "3)  x(6) = 4 + 12 + 0,5·36 = 34 m"],
             atbilde="v = 2 + t  (m/s; s) ;  v(6 s) = 8,0 m/s ;  "
                     "x(6 s) = 34 m",
             piezime="No viena vienādojuma var iegūt otru - koeficientus "
                     "salīdzina ar vispārīgo formu."),
        dict(nr=6, virsraksts="Satikšanās ar paātrinājumu",
             teksts="x₁ = 0,5t² un x₂ = 90 − 4t  (m; s).\n"
                    "Kad un kur ķermeņi satiksies?",
             dots=["x₁ = 0,5t²", "x₂ = 90 − 4t"],
             jaaprekina=["t = ?", "x = ?"],
             formulas=["x₁ = x₂"],
             aprekins=["1)  0,5t² = 90 − 4t  |·2",
                       "2)  t² + 8t − 180 = 0",
                       "3)  t = (−8 + √784) : 2 = (−8 + 28) : 2 = 10 s ;  "
                       "x = 50 m"],
             atbilde="t = 10 s ;   x = 50 m",
             piezime="Pārbaude: x₂ = 90 − 40 = 50 m ✔  Negatīvo sakni "
                     "atmet."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "x = x₀ + v₀t + at²/2.",
            "Koeficients pie t² ir a/2, nevis a.",
            "x(t) grafiks ir parabola.",
            "Parabolas virsotnē ātrums ir nulle.",
        ],
        majasdarbs=[
            "x = 4 + 3t + 2t². Nosaki x₀, v₀, a un x pēc 5 s.",
            "x₀ = 0, v₀ = 12 m/s, a = −3,0 m/s². Uzraksti vienādojumu un "
            "atrodi apstāšanās vietu.",
            "Sagatavojies: atkārto v = v₀ + at un visas s formulas.",
        ],
        pasvertejums=["Protu pierakstīt vienādojumu",
                      "Protu nolasīt x₀, v₀ un a",
                      "Protu aprēķināt koordinātu",
                      "Protu atrast apstāšanās vietu"],
        nakama="Nākamā stunda: uzdevumi par paātrinātu kustību."),
),

dict(
    nr="2.5", virsraksts="Uzdevumi par paātrinātu kustību",
    jautajums="Cik garš ir bremzēšanas ceļš?",
    apaksraksts="Formulas izvēle · Reakcijas ceļš · Drošība",
    merkis="Nostiprināt paātrinātas kustības uzdevumu risināšanu un "
           "saistīt to ar satiksmes drošību.",
    protu=["izvēlēties formulu pēc dotajiem lielumiem;",
           "aprēķināt apstāšanās ceļu ar reakcijas laiku;",
           "risināt divu posmu uzdevumus;",
           "pamatot ātruma ierobežojumus ar aprēķinu."],
    atkartojums="Mums ir četras formulas: v = v₀ + at un trīs "
                "pārvietojuma formulas. Šodien mācāmies izvēlēties "
                "pareizo un tās kombinēt.",
    uzdevumu_apraksts="Apstāšanās ceļš, reakcijas laiks un divi posmi",
    teorija=[
        ("Apstāšanās ceļš", [
            ("formula", "PILNAIS APSTĀŠANĀS CEĻŠ",
             "s = s(reakcijas) + s(bremzēšanas) = v₀·t(reakc.) + "
             "v₀² / (2|a|)",
             "Vidējais vadītāja reakcijas laiks ir 0,8-1,2 s. Šajā laikā "
             "automašīna brauc ar nemainīgu ātrumu.", GOLD),
            ("tabula",
             ["v₀", "Reakcijas ceļš (1 s)", "Bremzēšana (a=7 m/s²)",
              "Kopā"],
             [["50 km/h", "14 m", "14 m", "28 m"],
              ["70 km/h", "19 m", "27 m", "46 m"],
              ["90 km/h", "25 m", "45 m", "70 m"],
              ["110 km/h", "31 m", "67 m", "98 m"]],
             [2.40, 3.60, 3.90, 2.33]),
        ]),
        ("Formulas izvēle", [
            ("panelis", "TRĪS JAUTĀJUMI PIRMS RĒĶINĀŠANAS",
             ["1) Kas ir dots?  2) Kas jāatrod?  3) Kurš lielums NAV ne "
              "dots, ne meklēts?  Trešā atbilde uzreiz pasaka, kuru "
              "formulu lietot."], NAVY),
            ("kartitas", [
                ("NAV LAIKA", BLUE,
                 ["v² − v₀² = 2as",
                  "Tipiski: bremzēšanas ceļš."]),
                ("NAV GALA ĀTRUMA", GREEN,
                 ["s = v₀t + at²/2",
                  "Tipiski: ceļš dotā laikā."]),
                ("NAV PAĀTRINĀJUMA", GOLD,
                 ["s = (v₀+v)/2 · t",
                  "Tipiski: vidējais ātrums."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Pilnais apstāšanās ceļš",
             teksts="Automašīna brauc 72 km/h. Vadītāja reakcijas laiks "
                    "1,0 s,\nbremzēšanas paātrinājums −8,0 m/s².\n"
                    "Aprēķini pilno apstāšanās ceļu!",
             dots=["v₀ = 72 km/h = 20 m/s", "t(r) = 1,0 s",
                   "a = −8,0 m/s²"],
             jaaprekina=["s = ?"],
             formulas=["s(r) = v₀·t(r)", "s(b) = v₀²/(2|a|)",
                       "s = s(r) + s(b)"],
             aprekins=["1)  s(r) = 20 · 1,0 = 20 m",
                       "2)  s(b) = 400 : 16 = 25 m",
                       "3)  s = 20 + 25 = 45 m"],
             atbilde="s = 45 m",
             piezime="Gandrīz puse ceļa nobraukta, pirms bremzes vispār "
                     "sāk darboties."),
        dict(nr=2, virsraksts="Paātrinājums no ceļa",
             teksts="Lidmašīna paceļas no miera stāvokļa, veicot pa "
                    "skrejceļu\n1800 m un sasniedzot 270 km/h.\n"
                    "Aprēķini paātrinājumu un pacelšanās laiku!",
             dots=["v₀ = 0", "v = 270 km/h = 75 m/s", "s = 1800 m"],
             jaaprekina=["a = ?", "t = ?"],
             formulas=["v² = 2as", "t = v/a"],
             aprekins=["1)  v² = 5625 m²/s²",
                       "2)  a = 5625 : (2·1800) = 1,56 m/s²",
                       "3)  t = 75 : 1,56 ≈ 48 s"],
             atbilde="a ≈ 1,6 m/s² ;   t ≈ 48 s",
             piezime="Pārbaude: s = (0+75)/2 · 48 = 1800 m ✔"),
        dict(nr=3, virsraksts="Divi posmi",
             teksts="Ķermenis 4,0 s paātrinās no miera ar 3,0 m/s²,\n"
                    "tad 6,0 s kustas vienmērīgi.\n"
                    "Aprēķini kopējo ceļu!",
             dots=["v₀ = 0", "a = 3,0 m/s²", "t₁ = 4,0 s", "t₂ = 6,0 s"],
             jaaprekina=["s = ?"],
             formulas=["s₁ = at₁²/2", "v = at₁", "s₂ = vt₂"],
             aprekins=["1)  s₁ = 3,0 · 16 : 2 = 24 m",
                       "2)  v = 3,0 · 4,0 = 12 m/s",
                       "3)  s₂ = 12 · 6,0 = 72 m ;  s = 96 m"],
             atbilde="s = 96 m",
             piezime="Katram posmam - sava formula; ātrums pirmā posma "
                     "beigās ir otrā posma sākuma ātrums."),
        dict(nr=4, virsraksts="Drošības aprēķins",
             teksts="Cik reižu garāks ir bremzēšanas ceļš, braucot\n"
                    "100 km/h, salīdzinājumā ar 50 km/h?",
             dots=["v₁ = 50 km/h", "v₂ = 100 km/h", "a vienāds"],
             jaaprekina=["s₂/s₁ = ?"],
             formulas=["s = v₀²/(2|a|)"],
             aprekins=["1)  s ~ v₀²",
                       "2)  v₂ = 2v₁ → v₂² = 4v₁²",
                       "3)  s₂ / s₁ = 4"],
             atbilde="4 reizes garāks.",
             piezime="Tieši tāpēc apdzīvotās vietās ātrums ir "
                     "ierobežots līdz 50 km/h."),
        dict(nr=5, virsraksts="Bremzēšana līdz mazākam ātrumam",
             teksts="Automašīna samazina ātrumu no 30 m/s līdz 10 m/s ar\n"
                    "paātrinājumu −4,0 m/s². Aprēķini ceļu un laiku!",
             dots=["v₀ = 30 m/s", "v = 10 m/s", "a = −4,0 m/s²"],
             jaaprekina=["s = ?", "t = ?"],
             formulas=["v² − v₀² = 2as", "t = (v − v₀)/a"],
             aprekins=["1)  v² − v₀² = 100 − 900 = −800 m²/s²",
                       "2)  s = −800 : (2·(−4,0)) = 100 m",
                       "3)  t = (10 − 30) : (−4,0) = 5,0 s"],
             atbilde="s = 100 m ;   t = 5,0 s",
             piezime="Pārbaude ar vidējo ātrumu: s = (30+10)/2 · 5,0 = "
                     "100 m ✔"),
        dict(nr=6, virsraksts="Vilciena piestāšana",
             teksts="Vilciens, braucot ar 20 m/s, apstājas 400 m garā\n"
                    "bremzēšanas ceļā. Aprēķini paātrinājumu un laiku!",
             dots=["v₀ = 20 m/s", "v = 0", "s = 400 m"],
             jaaprekina=["a = ?", "t = ?"],
             formulas=["v² − v₀² = 2as", "t = (v − v₀)/a"],
             aprekins=["1)  0 − 400 = 2a · 400",
                       "2)  a = −400 : 800 = −0,50 m/s²",
                       "3)  t = (0 − 20) : (−0,50) = 40 s"],
             atbilde="a = −0,50 m/s² ;   t = 40 s",
             piezime="Tik mazs paātrinājums ir tāpēc, ka pasažieriem "
                     "bremzēšanai jābūt maigai."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Formulu izvēlas pēc lieluma, kas nav ne dots, ne meklēts.",
            "Pilnais apstāšanās ceļš = reakcijas ceļš + bremzēšanas ceļš.",
            "Bremzēšanas ceļš ir proporcionāls v₀².",
            "Divu posmu uzdevumā katram posmam - sava formula.",
        ],
        majasdarbs=[
            "v₀ = 90 km/h, t(r) = 1,2 s, a = −6,0 m/s². Aprēķini pilno "
            "apstāšanās ceļu.",
            "Vilciens no 0 līdz 20 m/s 400 m laikā. Aprēķini a un t.",
            "Ķermenis 5 s paātrinās ar 2 m/s², tad 10 s vienmērīgi. "
            "Aprēķini s.",
        ],
        pasvertejums=["Protu izvēlēties formulu",
                      "Protu rēķināt apstāšanās ceļu",
                      "Protu risināt divu posmu uzdevumus",
                      "Protu pamatot ātruma ierobežojumus"],
        nakama="Nākamā stunda: brīvā krišana."),
),

dict(
    nr="2.6", virsraksts="Brīvā krišana",
    jautajums="Vai smagāks ķermenis krīt ātrāk?",
    apaksraksts="g = 9,81 m/s² · h = gt²/2 · Gaisa pretestība",
    merkis="Saprast brīvo krišanu kā vienmērīgi paātrinātu kustību un "
           "lietot krišanas formulas.",
    protu=["nosaukt brīvās krišanas paātrinājumu;",
           "lietot h = gt²/2 un v = gt;",
           "izskaidrot, kāpēc vakuumā visi ķermeņi krīt vienādi;",
           "novērtēt gaisa pretestības nozīmi."],
    atkartojums="2.3. stundā izvedām s = v₀t + at²/2. Brīvā krišana ir "
                "tieši šī kustība ar a = g un v₀ = 0.",
    uzdevumu_apraksts="Krišanas augstums, laiks un ātrums",
    teorija=[
        ("Brīvā krišana", [
            ("formula", "KRIŠANAS FORMULAS",
             "h = g t² / 2        v = g t        v² = 2 g h        "
             "g = 9,81 m/s² ≈ 9,8 m/s²",
             "Brīvā krišana ir kustība tikai gravitācijas ietekmē - bez "
             "gaisa pretestības. Paātrinājums nav atkarīgs no masas.",
             GOLD),
            ("panelis", "KĀPĒC NEATKARĪGS NO MASAS",
             ["Uz smagāku ķermeni darbojas lielāks spēks, bet tam ir arī "
              "lielāka inerce. Abi efekti precīzi izlīdzinās, tāpēc "
              "paātrinājums ir vienāds. Galileja eksperiments Pizā un "
              "Apollo 15 pieredze uz Mēness (āmurs un spalva) to "
              "apstiprina."], NAVY),
        ]),
        ("Ar gaisu un bez tā", [
            ("divi",
             ("VAKUUMĀ", BLUE,
              ["Visi ķermeņi krīt vienādi.",
               "a = g vienmēr.",
               "Spalva un āmurs sasniedz zemi vienlaikus."]),
             ("GAISĀ", RED,
              ["Pretestība atkarīga no formas un ātruma.",
               "Vieglus, plašus ķermeņus bremzē vairāk.",
               "Sasniedz robežātrumu (izpletnis ~5 m/s)."])),
            ("tabula",
             ["Augstums h", "Krišanas laiks", "Ātrums pie zemes"],
             [["1,0 m", "0,45 s", "4,4 m/s"],
              ["5,0 m", "1,0 s", "9,9 m/s"],
              ["20 m", "2,0 s", "20 m/s"],
              ["45 m", "3,0 s", "30 m/s"]],
             [3.40, 4.10, 4.73]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Krišanas laiks",
             teksts="Ķermenis brīvi krīt no 20 m augstuma.\n"
                    "Aprēķini krišanas laiku un ātrumu pie zemes! "
                    "(g = 9,8 m/s²)",
             dots=["h = 20 m", "v₀ = 0", "g = 9,8 m/s²"],
             jaaprekina=["t = ?", "v = ?"],
             formulas=["h = gt²/2 → t = √(2h/g)", "v = gt"],
             aprekins=["1)  t² = 2·20 : 9,8 = 4,08 s²",
                       "2)  t = 2,0 s",
                       "3)  v = 9,8 · 2,0 = 19,6 ≈ 20 m/s"],
             atbilde="t = 2,0 s ;   v ≈ 20 m/s = 71 km/h",
             piezime="No 20 m (7. stāvs) ķermenis sasniedz automašīnas "
                     "ātrumu."),
        dict(nr=2, virsraksts="Krišanas augstums",
             teksts="Akmens krīt akā 3,0 s.\n"
                    "Cik dziļa ir aka? (g = 9,8 m/s²)",
             dots=["t = 3,0 s", "v₀ = 0", "g = 9,8 m/s²"],
             jaaprekina=["h = ?"],
             formulas=["h = gt²/2"],
             aprekins=["1)  t² = 9,0 s²",
                       "2)  h = 9,8 · 9,0 : 2",
                       "3)  h = 44,1 ≈ 44 m"],
             atbilde="h ≈ 44 m",
             piezime="Reālā mērījumā jāņem vērā arī skaņas atgriešanās "
                     "laiks."),
        dict(nr=3, virsraksts="Ātrums no augstuma",
             teksts="No kāda augstuma jākrīt ķermenim, lai tas sasniegtu\n"
                    "ātrumu 30 m/s? (g = 9,8 m/s²)",
             dots=["v = 30 m/s", "v₀ = 0", "g = 9,8 m/s²"],
             jaaprekina=["h = ?"],
             formulas=["v² = 2gh → h = v²/(2g)"],
             aprekins=["1)  v² = 900 m²/s²",
                       "2)  h = 900 : (2·9,8)",
                       "3)  h = 45,9 ≈ 46 m"],
             atbilde="h ≈ 46 m (aptuveni 15. stāvs)",
             piezime="Laiks šeit nebija dots - tāpēc formula ar v²."),
        dict(nr=4, virsraksts="Ceļš pēdējā sekundē",
             teksts="Ķermenis krīt 4,0 s. Cik lielu ceļu tas veic\n"
                    "pēdējā sekundē? (g = 9,8 m/s²)",
             dots=["t₁ = 3,0 s", "t₂ = 4,0 s", "g = 9,8 m/s²"],
             jaaprekina=["Δh = ?"],
             formulas=["h = gt²/2", "Δh = h₂ − h₁"],
             aprekins=["1)  h₁ = 9,8 · 9 : 2 = 44,1 m",
                       "2)  h₂ = 9,8 · 16 : 2 = 78,4 m",
                       "3)  Δh = 78,4 − 44,1 = 34,3 m"],
             atbilde="Δh ≈ 34 m",
             piezime="Pirmajā sekundē ķermenis veic tikai 4,9 m - "
                     "krišanā ceļš strauji pieaug."),
        dict(nr=5, virsraksts="Ceļš pirmajās sekundēs",
             teksts="Ķermenis brīvi krīt. Cik lielu ceļu tas veic "
                    "pirmajā\nun cik pirmajās divās sekundēs? "
                    "(g = 9,8 m/s²)",
             dots=["v₀ = 0", "t₁ = 1,0 s", "t₂ = 2,0 s"],
             jaaprekina=["h₁ = ?", "h₂ = ?", "h₂/h₁ = ?"],
             formulas=["h = gt²/2"],
             aprekins=["1)  h₁ = 9,8 · 1,0 : 2 = 4,9 m",
                       "2)  h₂ = 9,8 · 4,0 : 2 = 19,6 m",
                       "3)  h₂ : h₁ = 19,6 : 4,9 = 4"],
             atbilde="h₁ = 4,9 m ;  h₂ = 19,6 m ;  attiecība 1 : 4",
             piezime="Laiks divkāršojas - ceļš pieaug četrreiz, jo "
                     "h ~ t²."),
        dict(nr=6, virsraksts="Ātrums un augstums pēc 1,5 s",
             teksts="Ķermenis brīvi krīt no miera 1,5 s.\n"
                    "Aprēķini ātrumu un noieto ceļu! (g = 9,8 m/s²)",
             dots=["v₀ = 0", "t = 1,5 s", "g = 9,8 m/s²"],
             jaaprekina=["v = ?", "h = ?"],
             formulas=["v = gt", "h = gt²/2"],
             aprekins=["1)  v = 9,8 · 1,5 = 14,7 m/s",
                       "2)  t² = 2,25 s²",
                       "3)  h = 9,8 · 2,25 : 2 = 11,0 m"],
             atbilde="v ≈ 14,7 m/s ;   h ≈ 11 m",
             piezime="Pārbaude: h = (0 + 14,7)/2 · 1,5 = 11,0 m ✔"),
        dict(nr=7, virsraksts="Divi dažādi augstumi",
             teksts="Viens ķermenis krīt no 5,0 m, otrs no 20 m.\n"
                    "Salīdzini krišanas laikus! (g = 9,8 m/s²)",
             dots=["h₁ = 5,0 m", "h₂ = 20 m", "g = 9,8 m/s²"],
             jaaprekina=["t₁ = ?", "t₂ = ?", "t₂/t₁ = ?"],
             formulas=["t = √(2h/g)"],
             aprekins=["1)  t₁ = √(2·5,0 : 9,8) = √1,02 = 1,01 s",
                       "2)  t₂ = √(2·20 : 9,8) = √4,08 = 2,02 s",
                       "3)  t₂ : t₁ = 2"],
             atbilde="t₁ ≈ 1,0 s ;  t₂ ≈ 2,0 s ;  laiks ilgāks 2 reizes.",
             piezime="Augstums pieauga 4 reizes, laiks - tikai 2 reizes, "
                     "jo t ~ √h."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Brīvā krišana ir vienmērīgi paātrināta kustība ar "
            "a = g = 9,8 m/s².",
            "h = gt²/2;  v = gt;  v² = 2gh.",
            "Vakuumā krišanas paātrinājums nav atkarīgs no masas.",
            "Gaisa pretestība maina rezultātu viegliem un plašiem "
            "ķermeņiem.",
        ],
        majasdarbs=[
            "h = 45 m. Aprēķini t un v.",
            "t = 2,5 s. Aprēķini h un v.",
            "v = 25 m/s. Aprēķini h un t.",
        ],
        pasvertejums=["Protu lietot krišanas formulas",
                      "Protu izskaidrot neatkarību no masas",
                      "Protu novērtēt gaisa pretestību",
                      "Protu izvēlēties pareizo formulu"],
        nakama="Nākamā stunda: vertikāli mests ķermenis."),
),

dict(
    nr="2.7", virsraksts="Vertikāli mests ķermenis",
    jautajums="Cik augstu uzlido bumba?",
    apaksraksts="v₀ uz augšu · h(max) = v₀²/(2g) · Simetrija",
    merkis="Iemācīties risināt uzdevumus par vertikāli uz augšu mestu "
           "ķermeni un izmantot kustības simetriju.",
    protu=["aprēķināt maksimālo pacelšanās augstumu;",
           "aprēķināt pacelšanās un krišanas laiku;",
           "izmantot kustības simetriju;",
           "pareizi izvēlēties ass virzienu."],
    atkartojums="2.6. stundā ķermenis krita no miera. Tagad tam ir "
                "sākuma ātrums uz augšu - bet paātrinājums joprojām ir "
                "g uz leju.",
    uzdevumu_apraksts="Pacelšanās augstums, laiks un simetrija",
    teorija=[
        ("Kustība uz augšu", [
            ("formula", "VERTIKĀLI UZ AUGŠU",
             "h(max) = v₀² / (2g)        t(uz augšu) = v₀ / g        "
             "t(kopā) = 2v₀ / g",
             "Ass vērsta uz augšu: v₀ > 0, a = −g. Augstākajā punktā "
             "ātrums ir nulle, bet paātrinājums joprojām ir g.", GOLD),
            ("kartitas", [
                ("UZ AUGŠU", BLUE,
                 ["v samazinās par 9,8 m/s katrā sekundē.",
                  "Bremzēta kustība."]),
                ("AUGŠĀ", GOLD,
                 ["v = 0, bet a = g.",
                  "Tikai viens mirklis."]),
                ("LEJUP", GREEN,
                 ["v aug par 9,8 m/s katrā sekundē.",
                  "Brīvā krišana."]),
            ]),
        ]),
        ("Simetrija", [
            ("panelis", "TRĪS SIMETRIJAS ĪPAŠĪBAS",
             ["1) Pacelšanās laiks ir vienāds ar krišanas laiku.  "
              "2) Ātrums, atgriežoties sākuma punktā, ir vienāds ar "
              "sākuma ātrumu (pretēji vērsts).  3) Vienā augstumā ātruma "
              "modulis uz augšu un lejup ir vienāds."], NAVY),
            ("tabula",
             ["v₀", "h(max)", "t uz augšu", "t kopā"],
             [["10 m/s", "5,1 m", "1,0 s", "2,0 s"],
              ["20 m/s", "20 m", "2,0 s", "4,1 s"],
              ["30 m/s", "46 m", "3,1 s", "6,1 s"]],
             [2.90, 3.10, 3.10, 3.13]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Maksimālais augstums",
             teksts="Bumbu met vertikāli uz augšu ar ātrumu 15 m/s.\n"
                    "Cik augstu tā uzlido? (g = 9,8 m/s²)",
             dots=["v₀ = 15 m/s", "v = 0", "g = 9,8 m/s²"],
             jaaprekina=["h(max) = ?"],
             formulas=["v² − v₀² = −2gh", "h = v₀²/(2g)"],
             aprekins=["1)  v₀² = 225 m²/s²",
                       "2)  h = 225 : (2·9,8)",
                       "3)  h = 11,5 ≈ 11 m"],
             atbilde="h(max) ≈ 11 m",
             piezime="Aptuveni 4. stāva augstums."),
        dict(nr=2, virsraksts="Kopējais lidojuma laiks",
             teksts="Ķermeni met uz augšu ar 24,5 m/s.\n"
                    "Cik ilgi tas atrodas gaisā? (g = 9,8 m/s²)",
             dots=["v₀ = 24,5 m/s", "g = 9,8 m/s²"],
             jaaprekina=["t(kopā) = ?"],
             formulas=["t(uz augšu) = v₀/g", "t(kopā) = 2v₀/g"],
             aprekins=["1)  t(uz augšu) = 24,5 : 9,8 = 2,5 s",
                       "2)  Simetrija: krišana arī 2,5 s",
                       "3)  t = 5,0 s"],
             atbilde="t = 5,0 s",
             piezime="Simetrija ietaupa pusi darba."),
        dict(nr=3, virsraksts="Ātrums dotā augstumā",
             teksts="Ķermeni met uz augšu ar 20 m/s.\n"
                    "Cik liels ir ātrums 15 m augstumā? "
                    "(g = 9,8 m/s²)",
             dots=["v₀ = 20 m/s", "h = 15 m", "g = 9,8 m/s²"],
             jaaprekina=["v = ?"],
             formulas=["v² = v₀² − 2gh"],
             aprekins=["1)  v₀² = 400 ;  2gh = 2·9,8·15 = 294",
                       "2)  v² = 400 − 294 = 106 m²/s²",
                       "3)  v = 10,3 ≈ 10 m/s"],
             atbilde="v ≈ 10 m/s",
             piezime="Tādu pašu ātruma moduli ķermenim ir arī krītot "
                     "šajā augstumā."),
        dict(nr=4, virsraksts="Mešana no augstuma",
             teksts="No 25 m augsta torņa met akmeni vertikāli uz augšu\n"
                    "ar 10 m/s. Cik ilgi tas krīt līdz zemei? "
                    "(g = 9,8 m/s²)",
             dots=["h₀ = 25 m", "v₀ = 10 m/s (uz augšu)",
                   "g = 9,8 m/s²"],
             jaaprekina=["t = ?"],
             formulas=["y = h₀ + v₀t − gt²/2", "y = 0"],
             aprekins=["1)  0 = 25 + 10t − 4,9t²",
                       "2)  4,9t² − 10t − 25 = 0",
                       "3)  t = (10 + √(100 + 490)) : 9,8 ≈ 3,5 s"],
             atbilde="t ≈ 3,5 s",
             piezime="Negatīvo sakni atmet. Pārbaude: bez sākuma ātruma "
                     "krišana no 25 m prasītu 2,3 s - loģiski, ka ar "
                     "mešanu uz augšu ilgāk."),
        dict(nr=5, virsraksts="Augstums pēc dotā laika",
             teksts="Ķermeni met vertikāli uz augšu ar 20 m/s.\n"
                    "Kādā augstumā tas ir pēc 1,0 s un cik liels ir "
                    "ātrums?\n(g = 9,8 m/s²)",
             dots=["v₀ = 20 m/s", "t = 1,0 s", "g = 9,8 m/s²"],
             jaaprekina=["h = ?", "v = ?"],
             formulas=["h = v₀t − gt²/2", "v = v₀ − gt"],
             aprekins=["1)  gt²/2 = 9,8 · 1,0 : 2 = 4,9 m",
                       "2)  h = 20 − 4,9 = 15,1 m",
                       "3)  v = 20 − 9,8 = 10,2 m/s"],
             atbilde="h ≈ 15 m ;   v ≈ 10 m/s (vēl uz augšu)",
             piezime="Ātrums vēl ir pozitīvs, tātad ķermenis augstāko "
                     "punktu nav sasniedzis."),
        dict(nr=6, virsraksts="Sākuma ātrums no augstuma",
             teksts="Ķermenis uzlido 20 m augstumā.\n"
                    "Ar kādu ātrumu tas tika mests un cik ilgi lido "
                    "augšup?\n(g = 9,8 m/s²)",
             dots=["h(max) = 20 m", "v = 0", "g = 9,8 m/s²"],
             jaaprekina=["v₀ = ?", "t = ?"],
             formulas=["v₀² = 2gh", "t = v₀/g"],
             aprekins=["1)  v₀² = 2 · 9,8 · 20 = 392 m²/s²",
                       "2)  v₀ = 19,8 ≈ 20 m/s",
                       "3)  t = 19,8 : 9,8 ≈ 2,0 s"],
             atbilde="v₀ ≈ 20 m/s ;   t ≈ 2,0 s augšup",
             piezime="Kopējais lidojuma laiks būtu 4,0 s - augšup un "
                     "lejup vienādi."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "h(max) = v₀²/(2g);  t(uz augšu) = v₀/g;  t(kopā) = 2v₀/g.",
            "Augstākajā punktā v = 0, bet a = g.",
            "Pacelšanās un krišanas laiks ir vienādi.",
            "Vienā augstumā ātruma moduļi ir vienādi.",
        ],
        majasdarbs=[
            "v₀ = 12 m/s. Aprēķini h(max) un t(kopā).",
            "Ķermenis gaisā ir 6,0 s. Aprēķini v₀ un h(max).",
            "v₀ = 25 m/s. Aprēķini ātrumu 20 m augstumā.",
        ],
        pasvertejums=["Protu rēķināt h(max)",
                      "Protu rēķināt lidojuma laiku",
                      "Protu izmantot simetriju",
                      "Protu strādāt ar mešanu no augstuma"],
        nakama="Nākamā stunda: uzdevumi par krišanu un mešanu."),
),

]
