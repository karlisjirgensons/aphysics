# -*- coding: utf-8 -*-
"""6. temats "Mehāniskās svārstības un viļņi". B daļa: padziļinātais līmenis.

Šīs divas stundas (6.5. un 6.6.) ir PAPILDU materiāls ārpus 100 stundu
plāna (fiz_plan_11.py) - optimālā līmeņa kurss beidzas ar 6.4. stundu un
PD1. Tās der padziļinātā līmeņa grupai un konsultācijām: te svārstības
apraksta ar vienādojumu x = x(m) · sin(ωt), nevis tikai ar T un f.

Formulas raksta tāpat kā visur - formulu lapas formā (Fizika_1_formulas.txt).
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "6. temats. Mehāniskās svārstības un viļņi"
KICKER = ("FIZIKA I · 11. KLASE · 6. TEMATS: SVĀRSTĪBAS UN VIĻŅI · "
          "PADZIĻINĀTAIS LĪMENIS")
KURSS = "FIZIKA I · 11. KLASE · PADZIĻINĀTAIS LĪMENIS"
MAPE = "C:/aphysics/Fizika_1/6. Mehāniskās svārstības un viļņi"

STUNDAS = [

dict(
    nr="6.5", virsraksts="Harmonisko svārstību vienādojums",
    jautajums="Kā ar vienu formulu pateikt, kur ķermenis ir katrā mirklī?",
    apaksraksts=("PADZIĻINĀTAIS LĪMENIS   ·   x = x(m) · sin(ωt)"
                 "   ·   ω = 2πf   ·   v(m) = ω · x(m)"),
    merkis="Lietot harmonisko svārstību vienādojumu x = x(m) · sin(ωt): "
           "nolasīt no tā amplitūdu un ciklisko frekvenci un aprēķināt "
           "novirzi, periodu un lielāko ātrumu.",
    protu=["pierakstīt svārstību vienādojumu x = x(m) · sin(ωt);",
           "no vienādojuma nolasīt amplitūdu un ciklisko frekvenci;",
           "no ω aprēķināt periodu un frekvenci;",
           "aprēķināt novirzi x jebkurā laika momentā."],
    atkartojums="6.1. stundā svārstības raksturojām ar amplitūdu, periodu "
                "un frekvenci. Tie visi ir vienā formulā - tikai tagad "
                "leņķi mēra radiānos, nevis grādos.",
    uzdevumu_apraksts="Svārstību vienādojums, ω un lielākais ātrums",
    teorija=[
        ("Svārstību vienādojums", [
            ("formula", "HARMONISKĀS SVĀRSTĪBAS",
             "x = x(m) · sin(ωt)        ω = 2πf = 2π/T        "
             "[ω] = rad/s",
             "Vienādojums dod novirzi x katrā laika momentā t. Amplitūda "
             "x(m) ir lielākā novirze, bet ω rāda, cik ātri griežas "
             "sinusa arguments.", GOLD),
            ("kartitas", [
                ("AMPLITŪDA x(m)", BLUE,
                 ["Reizinātājs sinusa priekšā.",
                  "Lielākā novirze metros.",
                  "Grafikā - līknes augstums."]),
                ("CIKLISKĀ FREKVENCE ω", GREEN,
                 ["Reizinātājs pie t.",
                  "ω = 2πf = 2π/T.",
                  "Mēra rad/s."]),
                ("FĀZE ωt", GOLD,
                 ["Sinusa arguments radiānos.",
                  "Pilna svārstība - 2π rad.",
                  "Rāda, kur ķermenis ir."]),
            ]),
        ]),
        ("Ātrums un paātrinājums", [
            ("divi",
             ("ĀTRUMS v", BLUE,
              ["Vienādojums: v = v(m) · cos(ωt).",
               "Lielākais ātrums v(m) = ω · x(m).",
               "Lielākais - līdzsvara stāvoklī.",
               "Galapunktos ātrums ir nulle."]),
             ("PAĀTRINĀJUMS a", GREEN,
              ["Vienādojums: a = −ω² · x.",
               "Lielākais a(m) = ω² · x(m).",
               "Lielākais - galapunktos.",
               "Vienmēr vērsts uz līdzsvaru."])),
            ("panelis", "KĀPĒC ZĪME IR MĪNUSS",
             ["Paātrinājums vienmēr ir vērsts pretēji novirzei - uz "
              "līdzsvara stāvokli. Tieši tāpēc kustība ir svārstības, "
              "nevis aizbēgšana prom.",
              "No a = −ω²x un F = ma seko F = −mω²x: atgriezējspēks aug "
              "proporcionāli novirzei. Tas pats redzams Huka likumā "
              "F = kx.",
              "Salīdzini ar 6.1. stundu: tur to pašu teicām vārdiem - "
              "«jo tālāk no līdzsvara, jo stiprāk velk atpakaļ»."], NAVY),
        ]),
        ("No grafika uz vienādojumu", [
            ("tabula",
             ["No grafika nolasa", "Aprēķina", "Ieliek vienādojumā"],
             [["Līknes augstums", "x(m) metros", "Reizinātājs priekšā"],
              ["Viena pilna svārstība", "T sekundēs", "ω = 2π/T"],
              ["Svārstību skaits 1 s", "f = 1/T", "ω = 2πf"],
              ["Sākuma novirze 0", "sin, ne cos", "x = x(m)·sin(ωt)"]],
             [3.60, 3.00, 5.63]),
            ("panelis", "DIVI SOĻI, KAS NEDRĪKST SAJUKT",
             ["1. ω NAV frekvence. Frekvenci mēra hercos, ω - radiānos "
              "sekundē, un tās atšķiras 2π ≈ 6,28 reizes.",
              "2. Kalkulatoram jābūt radiānu režīmā (RAD), citādi "
              "sin(0,785) tiks rēķināts grādos un atbilde būs nepareiza.",
              "Pārbaude: pēc laika t = T novirzei jābūt atkal nullei, jo "
              "ωT = 2π un sin 2π = 0."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Nolasa no vienādojuma",
             teksts="Svārstības apraksta vienādojums x = 0,05 · sin(4πt)\n"
                    "(SI vienībās). Nosaki amplitūdu, ciklisko frekvenci,\n"
                    "periodu un frekvenci!",
             dots=["x = 0,05 · sin(4πt)"],
             jaaprekina=["x(m) = ?", "ω = ?", "T = ?", "f = ?"],
             formulas=["x = x(m) · sin(ωt)", "ω = 2πf", "f = 1/T"],
             aprekins=["1)  x(m) = 0,05 m (reizinātājs sinusa priekšā)",
                       "2)  ω = 4π = 4 · 3,14 = 12,56 rad/s",
                       "3)  T = 2π/ω = 6,28 : 12,56 = 0,50 s",
                       "4)  f = 1/T = 1 : 0,50 = 2,0 Hz"],
             atbilde="x(m) = 0,05 m;  ω = 12,56 rad/s;  T = 0,50 s;  "
                     "f = 2,0 Hz",
             piezime="Vienādojumā viss jau ir - amplitūda stāv priekšā, "
                     "ciklisko frekvenci lasa pie t."),
        dict(nr=2, virsraksts="Uzraksta vienādojumu",
             teksts="Ķermenis svārstās ar amplitūdu 8,0 cm un periodu\n"
                    "0,40 s. Uzraksti svārstību vienādojumu!",
             dots=["x(m) = 8,0 cm = 0,08 m", "T = 0,40 s"],
             jaaprekina=["ω = ?", "x(t) = ?"],
             formulas=["ω = 2π/T", "x = x(m) · sin(ωt)"],
             aprekins=["1)  ω = 2π/T = 6,28 : 0,40 = 15,7 rad/s",
                       "2)  x = 0,08 · sin(15,7t)"],
             atbilde="x = 0,08 · sin(15,7t)  (metros un sekundēs)",
             piezime="Amplitūdu vienmēr vispirms pārrēķina metros - "
                     "citādi vienādojums nav SI vienībās."),
        dict(nr=3, virsraksts="Novirze noteiktā mirklī",
             teksts="Amplitūda ir 0,10 m, periods 2,0 s. Cik liela ir\n"
                    "novirze pēc 0,25 s no svārstību sākuma?",
             dots=["x(m) = 0,10 m", "T = 2,0 s", "t = 0,25 s"],
             jaaprekina=["x = ?"],
             formulas=["ω = 2π/T", "x = x(m) · sin(ωt)"],
             aprekins=["1)  ω = 2π/T = 6,28 : 2,0 = 3,14 rad/s",
                       "2)  ωt = 3,14 · 0,25 = 0,785 rad = 45°",
                       "3)  sin 45° ≈ 0,71",
                       "4)  x = 0,10 · 0,71 = 0,071 m"],
             atbilde="x ≈ 0,071 m",
             piezime="0,25 s ir ceturtdaļa no 1,0 s - tieši astotdaļa "
                     "perioda, tāpēc arī 45°."),
        dict(nr=4, virsraksts="Lielākais ātrums",
             teksts="Ķermenis svārstās ar amplitūdu 0,05 m un frekvenci\n"
                    "2,0 Hz. Cik liels ir lielākais ātrums?",
             dots=["x(m) = 0,05 m", "f = 2,0 Hz"],
             jaaprekina=["v(m) = ?"],
             formulas=["ω = 2πf", "v(m) = ω · x(m)"],
             aprekins=["1)  ω = 2πf = 2 · 3,14 · 2,0 = 12,56 rad/s",
                       "2)  v(m) = ω · x(m) = 12,56 · 0,05 ≈ 0,63 m/s"],
             atbilde="v(m) ≈ 0,63 m/s",
             piezime="Lielāko ātrumu ķermenis sasniedz līdzsvara "
                     "stāvoklī, kur novirze ir nulle."),
        dict(nr=5, virsraksts="Lielākais paātrinājums",
             teksts="Tā paša ķermeņa (x(m) = 0,05 m, f = 2,0 Hz)\n"
                    "lielākais paātrinājums?",
             dots=["x(m) = 0,05 m", "f = 2,0 Hz"],
             jaaprekina=["a(m) = ?"],
             formulas=["ω = 2πf", "a(m) = ω² · x(m)"],
             aprekins=["1)  ω = 2πf = 2 · 3,14 · 2,0 = 12,56 rad/s",
                       "2)  ω² = 12,56² ≈ 158 rad²/s²",
                       "3)  a(m) = ω² · x(m) = 158 · 0,05 ≈ 7,9 m/s²"],
             atbilde="a(m) ≈ 7,9 m/s²",
             piezime="Tas ir gandrīz kā brīvās krišanas paātrinājums - "
                     "un to rada tikai 5 cm liela novirze."),
        dict(nr=6, virsraksts="No grafika uz vienādojumu",
             teksts="Grafikā lielākā novirze ir 4,0 cm, un viena pilna\n"
                    "svārstība aizņem 0,80 s. Uzraksti vienādojumu un\n"
                    "aprēķini frekvenci!",
             dots=["x(m) = 4,0 cm = 0,04 m", "T = 0,80 s"],
             jaaprekina=["ω = ?", "f = ?", "x(t) = ?"],
             formulas=["ω = 2π/T", "f = 1/T", "x = x(m) · sin(ωt)"],
             aprekins=["1)  ω = 2π/T = 6,28 : 0,80 = 7,85 rad/s",
                       "2)  f = 1/T = 1 : 0,80 = 1,25 Hz",
                       "3)  x = 0,04 · sin(7,85t)"],
             atbilde="x = 0,04 · sin(7,85t);  f = 1,25 Hz",
             piezime="Grafiks dod tikai divus skaitļus - augstumu un "
                     "periodu; pārējais ir aprēķins."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Harmoniskās svārstības apraksta x = x(m) · sin(ωt).",
            "ω = 2πf = 2π/T un to mēra radiānos sekundē.",
            "Lielākais ātrums v(m) = ω · x(m) ir līdzsvara stāvoklī.",
            "Lielākais paātrinājums a(m) = ω² · x(m) ir galapunktos.",
        ],
        majasdarbs=[
            "x = 0,12 · sin(10t). Nosaki x(m), ω, T un f.",
            "x(m) = 6,0 cm, f = 5,0 Hz. Uzraksti vienādojumu.",
            "x(m) = 0,20 m, T = 4,0 s. Aprēķini x pēc t = 1,0 s.",
        ],
        pasvertejums=["Protu nolasīt x(m) un ω",
                      "Protu uzrakstīt vienādojumu",
                      "Protu aprēķināt x katrā mirklī",
                      "Zinu, kur ātrums ir lielākais"],
        nakama="Nākamā stunda: svārstību enerģija un svārsta periods."),
),

dict(
    nr="6.6", virsraksts="Svārstību enerģija un svārsti",
    jautajums="Kāpēc svārsta periods nav atkarīgs no masas?",
    apaksraksts=("PADZIĻINĀTAIS LĪMENIS   ·   T = 2π√(l/g)"
                 "   ·   T = 2π√(m/k)   ·   Ep = kx²/2"),
    merkis="Aprēķināt matemātiskā un atsperes svārsta periodu un "
           "svārstību enerģiju un izskaidrot enerģijas pārvērtības "
           "svārstību laikā.",
    protu=["aprēķināt matemātiskā svārsta periodu T = 2π√(l/g);",
           "aprēķināt atsperes svārsta periodu T = 2π√(m/k);",
           "aprēķināt svārstību enerģiju Ep = kx²/2;",
           "izskaidrot, kā enerģija pāriet no potenciālās kinētiskajā."],
    atkartojums="5. temata enerģijas nezūdamības likums te strādā "
                "pilnā spēkā: svārstībās kopējā enerģija paliek tā pati, "
                "tikai maina veidu.",
    uzdevumu_apraksts="Svārsta periods un svārstību enerģija",
    teorija=[
        ("Divi svārsti", [
            ("formula", "SVĀRSTA PERIODS",
             "T = 2π√(l/g)        T = 2π√(m/k)        [T] = s",
             "Matemātiskā svārsta periods atkarīgs tikai no garuma, "
             "atsperes svārsta - no masas un stinguma. Masa pirmajā "
             "formulā neparādās vispār.", GOLD),
            ("divi",
             ("MATEMĀTISKAIS SVĀRSTS", BLUE,
              ["Diegs un smaga lodīte.",
               "T = 2π√(l/g).",
               "Garāks diegs - lēnāks solis.",
               "Masa periodu nemaina.",
               "Der pulksteņiem."]),
             ("ATSPERES SVĀRSTS", GREEN,
              ["Atspere un atsvars.",
               "T = 2π√(m/k).",
               "Smagāks atsvars - lēnāk.",
               "Stingrāka atspere - ātrāk.",
               "Der amortizatoriem."])),
        ]),
        ("Enerģija svārstībās", [
            ("formula", "ENERĢIJAS PĀRVĒRTĪBAS",
             "Ep = kx²/2        Ek = mv²/2        E = Ep + Ek = const",
             "Galapunktos visa enerģija ir potenciālā, līdzsvara "
             "stāvoklī - kinētiskā. Kopējā enerģija bez berzes "
             "nemainās.", GOLD),
            ("tabula",
             ["Kur ķermenis ir", "Novirze x", "Ātrums v", "Enerģija"],
             [["Galapunktā", "x(m)", "0", "Visa potenciālā"],
              ["Pusceļā", "x(m)/2", "vidējs", "Abas kopā"],
              ["Līdzsvarā", "0", "v(m)", "Visa kinētiskā"],
              ["Otrā galapunktā", "−x(m)", "0", "Visa potenciālā"]],
             [3.40, 2.40, 2.60, 3.83]),
        ]),
        ("Slāpēšana un rezonanse", [
            ("divi",
             ("SLĀPĒTAS SVĀRSTĪBAS", RED,
              ["Berze pārvērš enerģiju siltumā.",
               "Amplitūda sarūk soli pa solim.",
               "Periods gandrīz nemainās.",
               "Piemērs: automašīnas atspere."]),
             ("REZONANSES LĪKNE", GREEN,
              ["Amplitūda pret ārējo frekvenci.",
               "Smaile pie f = f₀.",
               "Lielāka berze - zemāka smaile.",
               "Piemērs: tilta aprēķins."])),
            ("panelis", "KUR TO IZMANTO INŽENIERI",
             ["Ēkām seismiskajos rajonos pievieno slāpētājus - lielas "
              "masas, kas svārstās pretfāzē un «apēd» enerģiju.",
              "Pulksteņa svārstam garumu izvēlas tā, lai T = 2,0 s: tad "
              "katrs solis ir tieši viena sekunde.",
              "Mašīnu amortizatorus veido tā, lai svārstības izdzistu "
              "vienā vai divos gājienos - citādi brauciens kļūst "
              "nedrošs."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Matemātiskā svārsta periods",
             teksts="Svārsta diega garums ir 1,0 m.\n"
                    "Aprēķini svārstību periodu! (g = 9,8 m/s²)",
             dots=["l = 1,0 m", "g = 9,8 m/s²"],
             jaaprekina=["T = ?"],
             formulas=["T = 2π√(l/g)"],
             aprekins=["1)  l/g = 1,0 : 9,8 ≈ 0,102 s²",
                       "2)  √0,102 ≈ 0,32 s",
                       "3)  T = 6,28 · 0,32 ≈ 2,0 s"],
             atbilde="T ≈ 2,0 s",
             piezime="Tieši tāds ir pulksteņa svārsts: viens solis uz "
                     "vienu pusi ilgst sekundi."),
        dict(nr=2, virsraksts="Cik garš diegs vajadzīgs",
             teksts="Cik garam jābūt svārsta diegam, lai periods būtu\n"
                    "1,0 s? (g = 9,8 m/s²)",
             dots=["T = 1,0 s", "g = 9,8 m/s²"],
             jaaprekina=["l = ?"],
             formulas=["T = 2π√(l/g)", "l = gT²/(4π²)"],
             aprekins=["1)  4π² = 4 · 9,86 ≈ 39,4",
                       "2)  l = 9,8 · 1,0² : 39,4",
                       "3)  l ≈ 0,25 m"],
             atbilde="l ≈ 0,25 m",
             piezime="Periodu samazinot divas reizes, garums sarūk "
                     "četras - zem saknes taču ir l."),
        dict(nr=3, virsraksts="Atsperes svārsts",
             teksts="Pie atsperes ar stingumu 50 N/m iekārts 0,20 kg\n"
                    "smags atsvars. Aprēķini svārstību periodu!",
             dots=["k = 50 N/m", "m = 0,20 kg"],
             jaaprekina=["T = ?"],
             formulas=["T = 2π√(m/k)"],
             aprekins=["1)  m/k = 0,20 : 50 = 0,004 s²",
                       "2)  √0,004 ≈ 0,063 s",
                       "3)  T = 6,28 · 0,063 ≈ 0,40 s"],
             atbilde="T ≈ 0,40 s",
             piezime="Te masa periodu ietekmē - atšķirībā no "
                     "matemātiskā svārsta."),
        dict(nr=4, virsraksts="Svārstību enerģija",
             teksts="Atsperes stingums ir 50 N/m, svārstību amplitūda\n"
                    "0,10 m. Cik liela ir svārstību enerģija?",
             dots=["k = 50 N/m", "x(m) = 0,10 m"],
             jaaprekina=["E = ?"],
             formulas=["Ep = kx²/2"],
             aprekins=["1)  x(m)² = 0,10² = 0,01 m²",
                       "2)  E = 50 · 0,01 : 2",
                       "3)  E = 0,25 J"],
             atbilde="E = 0,25 J",
             piezime="Galapunktā visa enerģija ir potenciālā, tāpēc tā "
                     "arī ir svārstību kopējā enerģija."),
        dict(nr=5, virsraksts="Lielākais ātrums no enerģijas",
             teksts="Tā paša svārsta (E = 0,25 J) atsvara masa ir\n"
                    "0,20 kg. Cik liels ir lielākais ātrums?",
             dots=["E = 0,25 J", "m = 0,20 kg"],
             jaaprekina=["v(m) = ?"],
             formulas=["Ek = mv²/2", "v = √(2Ek/m)"],
             aprekins=["1)  2E/m = 2 · 0,25 : 0,20 = 2,5 m²/s²",
                       "2)  v(m) = √2,5 ≈ 1,6 m/s"],
             atbilde="v(m) ≈ 1,6 m/s",
             piezime="Līdzsvara stāvoklī visa potenciālā enerģija ir "
                     "kļuvusi par kinētisko."),
        dict(nr=6, virsraksts="Svārsts uz Mēness",
             teksts="Tāds pats 1,0 m garš svārsts nogādāts uz Mēness,\n"
                    "kur g = 1,6 m/s². Cik liels ir periods un cik\n"
                    "reižu tas atšķiras no Zemes perioda 2,0 s?",
             dots=["l = 1,0 m", "g = 1,6 m/s²", "T(Z) = 2,0 s"],
             jaaprekina=["T = ?", "T/T(Z) = ?"],
             formulas=["T = 2π√(l/g)"],
             aprekins=["1)  l/g = 1,0 : 1,6 = 0,625 s²",
                       "2)  √0,625 ≈ 0,79 s",
                       "3)  T = 6,28 · 0,79 ≈ 5,0 s",
                       "4)  T/T(Z) = 5,0 : 2,0 = 2,5"],
             atbilde="T ≈ 5,0 s;  tas ir 2,5 reizes ilgāk nekā uz Zemes",
             piezime="Vājāks lauks - lēnākas svārstības; tāpēc mehāniskais "
                     "pulkstenis uz Mēness atpaliktu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Matemātiskā svārsta periods T = 2π√(l/g) nav atkarīgs no "
            "masas.",
            "Atsperes svārsta periods T = 2π√(m/k) ir atkarīgs no masas.",
            "Svārstību enerģija Ep = kx²/2 tiek uzkrāta galapunktā.",
            "Bez berzes kopējā enerģija svārstībās nemainās.",
        ],
        majasdarbs=[
            "l = 0,64 m. Aprēķini svārsta periodu (g = 9,8 m/s²).",
            "k = 80 N/m, m = 0,50 kg. Aprēķini periodu un frekvenci.",
            "k = 200 N/m, amplitūda 0,05 m. Aprēķini svārstību enerģiju.",
        ],
        pasvertejums=["Protu aprēķināt svārsta periodu",
                      "Protu aprēķināt atsperes svārsta periodu",
                      "Protu aprēķināt svārstību enerģiju",
                      "Protu izskaidrot enerģijas pārvērtības"],
        nakama="Atgriežamies pie optimālā līmeņa: PD1 par svārstībām un "
               "viļņiem."),
),

]
