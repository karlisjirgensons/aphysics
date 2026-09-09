# -*- coding: utf-8 -*-
"""10.3. temata stundas 3.4.-3.9. (turpinājums failam tema_03.py)."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN
from tema_03 import TEMATS, KICKER, MAPE

STUNDAS = [

dict(
    nr="3.4", virsraksts="Kodolreakcijas",
    jautajums="Kā rodas jauns ķīmiskais elements?",
    apaksraksts="Kodolu dalīšanās · Kodolsintēze · Vienādojumu pieraksts",
    merkis="Iemācīties atšķirt kodolu dalīšanos no kodolsintēzes un "
           "papildināt vienkāršu kodolreakcijas vienādojumu, lietojot "
           "lādiņa un masas skaitļa nezūdamību.",
    protu=["atšķirt kodolreakciju no ķīmiskas reakcijas;",
           "salīdzināt kodolu dalīšanos un kodolsintēzi;",
           "papildināt kodolreakcijas vienādojumu;",
           "nosaukt, kur kodolreakcijas notiek dabā un tehnikā."],
    atkartojums="3.1. stundā: kodolā ir protoni un neitroni; elementu nosaka "
                "protonu skaits Z. Ja mainās Z, rodas cits elements.",
    uzdevumu_apraksts="Kodolreakciju vienādojumi un enerģija",
    teorija=[
        ("Divi kodolreakciju veidi", [
            ("panelis", "KODOLREAKCIJA",
             ["Kodolreakcijā mainās kodola sastāvs, tāpēc rodas CITA "
              "elementa atoms. Ķīmiskā reakcijā kodols nemainās — mainās "
              "tikai elektronapvalks.",
              "Kodolreakcijās atbrīvojas miljoniem reižu vairāk enerģijas "
              "nekā ķīmiskajās reakcijās."], NAVY),
            ("divi",
             ("DALĪŠANĀS (fisija)", BLUE,
              ["Smags kodols sadalās divos vieglākos.",
               "²³⁵U + n → ¹⁴¹Ba + ⁹²Kr + 3n",
               "Notiek atomelektrostacijās.",
               "Rodas radioaktīvi atkritumi."]),
             ("SINTĒZE (fūzija)", RED,
              ["Divi viegli kodoli saplūst vienā smagākā.",
               "²H + ³H → ⁴He + n",
               "Notiek Saulē un zvaigznēs.",
               "Vajadzīga ļoti augsta temperatūra."])),
        ]),
        ("Kā papildina vienādojumu", [
            ("formula", "DIVI NEZŪDAMĪBAS LIKUMI",
             "Masas skaitļu summa nemainās  ·  Lādiņu summa nemainās",
             "Augšā raksta masas skaitli A, apakšā — kārtas skaitli Z. "
             "Abām vienādojuma pusēm summas jāsakrīt.", GOLD),
            ("tabula",
             ["Daļiņa", "Apzīmējums", "A", "Z"],
             [["protons", "p", "1", "+1"],
              ["neitrons", "n", "1", "0"],
              ["elektrons (bēta)", "e", "0", "−1"],
              ["alfa daļiņa (He kodols)", "α", "4", "+2"]],
             [4.23, 2.80, 2.60, 2.60]),
            ("panelis", "PIEMĒRS",
             ["²³⁸U → ⁴He + ?      A: 238 = 4 + 234      Z: 92 = 2 + 90",
              "Tātad rodas elements ar Z = 90 un A = 234 — torijs ²³⁴Th."],
             GREEN),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Alfa sabrukšana",
             teksts="Rādija kodols ²²⁶Ra (Z = 88) izstaro alfa daļiņu.\n"
                    "Nosaki radušos kodola masas un kārtas skaitli!",
             dots=["A = 226 ;  Z = 88", "α: A = 4 ;  Z = 2"],
             jaaprekina=["A₁ = ?", "Z₁ = ?"],
             formulas=["A₁ = A − 4", "Z₁ = Z − 2"],
             aprekins=["1)  A₁ = 226 − 4 = 222",
                       "2)  Z₁ = 88 − 2 = 86",
                       "3)  Z = 86 → radons Rn"],
             atbilde="Rodas ²²²Rn (radons)",
             piezime="Alfa sabrukšanā Z samazinās par 2, A — par 4."),
        dict(nr=2, virsraksts="Bēta sabrukšana",
             teksts="Oglekļa izotops ¹⁴C (Z = 6) izstaro bēta daļiņu "
                    "(elektronu).\nKāds elements rodas?",
             dots=["A = 14 ;  Z = 6", "e: A = 0 ;  Z = −1"],
             jaaprekina=["A₁ = ?", "Z₁ = ?"],
             formulas=["A₁ = A", "Z₁ = Z − (−1) = Z + 1"],
             aprekins=["1)  A₁ = 14",
                       "2)  Z₁ = 6 + 1 = 7",
                       "3)  Z = 7 → slāpeklis N"],
             atbilde="Rodas ¹⁴N (slāpeklis)",
             piezime="Bēta sabrukšanā neitrons pārvēršas protonā: Z aug par "
                     "1, bet A nemainās."),
        dict(nr=3, virsraksts="Urāna dalīšanās",
             teksts="Reakcijā ²³⁵U + n → ¹⁴¹Ba + ? + 3n. Urānam Z = 92, "
                    "bārijam Z = 56.\nNosaki trūkstošā kodola A un Z!",
             dots=["A: 235 + 1 = 141 + A₂ + 3", "Z: 92 + 0 = 56 + Z₂"],
             jaaprekina=["A₂ = ?", "Z₂ = ?"],
             formulas=["ΣA kreisajā = ΣA labajā pusē",
                       "ΣZ kreisajā = ΣZ labajā pusē"],
             aprekins=["1)  236 = 141 + A₂ + 3",
                       "2)  A₂ = 236 − 144 = 92",
                       "3)  Z₂ = 92 − 56 = 36 → kriptons Kr"],
             atbilde="Rodas ⁹²Kr (kriptons)",
             piezime="Trīs brīvie neitroni var izraisīt nākamās dalīšanās — "
                     "tā rodas ķēdes reakcija."),
        dict(nr=4, virsraksts="Enerģija kodolsintēzē",
             teksts="Vienā sintēzes reakcijā ²H + ³H → ⁴He + n atbrīvojas "
                    "2,8·10⁻¹² J.\nCik enerģijas atbrīvotos 1,0·10²⁰ šādās "
                    "reakcijās?",
             dots=["E₁ = 2,8·10⁻¹² J", "N = 1,0·10²⁰"],
             jaaprekina=["E = ?"],
             formulas=["E = N · E₁"],
             aprekins=["1)  E = 1,0·10²⁰ · 2,8·10⁻¹² J",
                       "2)  E = 2,8·10⁸ J"],
             atbilde="E = 2,8·10⁸ J = 280 MJ",
             piezime="Salīdzinājumam: sadegot 1 kg benzīna, rodas ~46 MJ."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Kodolreakcijā mainās kodola sastāvs un rodas cits elements.",
            "Dalīšanās — smags kodols sadalās; sintēze — divi vieglie "
            "saplūst.",
            "Vienādojumā masas skaitļu un lādiņu summas abās pusēs ir "
            "vienādas.",
            "Alfa: Z −2, A −4. Bēta: Z +1, A nemainās.",
        ],
        majasdarbs=[
            "²¹⁰Po (Z = 84) izstaro alfa daļiņu. Kāds elements rodas?",
            "⁹⁰Sr (Z = 38) izstaro bēta daļiņu. Nosaki jauno A un Z.",
            "Papildini: ²³⁹Pu → ⁴He + ?   (Pu: Z = 94).",
        ],
        pasvertejums=["Protu atšķirt dalīšanos no sintēzes",
                      "Protu lietot nezūdamības likumus",
                      "Protu papildināt vienādojumu",
                      "Protu nosaukt lietojumus"],
        nakama="Nākamā stunda: radioaktivitāte un starojuma veidi."),
),

dict(
    nr="3.5", virsraksts="Radioaktivitāte",
    jautajums="Kāpēc daži atomi sabrūk paši no sevis?",
    apaksraksts="Alfa · Bēta · Gamma · Caurspiešanās spēja",
    merkis="Iemācīties salīdzināt alfa, bēta un gamma starojumu pēc dabas, "
           "caurspiešanās spējas un bīstamības un atšķirt dabisko "
           "radioaktivitāti no mākslīgās.",
    protu=["skaidrot, kas ir radioaktivitāte;",
           "salīdzināt alfa, bēta un gamma starojumu;",
           "sakārtot starojumus pēc caurspiešanās spējas;",
           "atšķirt dabisko un mākslīgo radioaktivitāti."],
    atkartojums="3.4. stundā mācījāmies pierakstīt alfa un bēta sabrukšanu. "
                "Šodien noskaidrosim, kas šie starojumi patiesībā ir.",
    uzdevumu_apraksts="Starojuma veidi un aizsardzība",
    teorija=[
        ("Trīs starojuma veidi", [
            ("panelis", "RADIOAKTIVITĀTE",
             ["Nestabils kodols patvaļīgi sabrūk un izstaro starojumu. To "
              "nevar apturēt, paātrināt vai palēnināt — ne ar temperatūru, "
              "ne ar spiedienu, ne ar ķīmiskām reakcijām."], NAVY),
            ("tabula",
             ["Starojums", "Kas tas ir", "Lādiņš", "Aptur", "Bīstamība"],
             [["Alfa  α", "hēlija kodols (2p + 2n)", "+2", "papīra lapa",
               "ļoti bīstams organismā"],
              ["Bēta  β", "ātrs elektrons", "−1", "alumīnija plāksne",
               "vidēji bīstams"],
              ["Gamma  γ", "elektromagnētiskais starojums", "0",
               "biezs svins vai betons", "bīstams no attāluma"]],
             [2.03, 3.60, 1.40, 2.70, 2.50]),
        ]),
        ("Caurspiešanās un izcelsme", [
            ("kartitas", [
                ("CAURSPIEŠANĀS SPĒJA", BLUE,
                 ["α — vismazākā, bet vislielākā jonizācija.",
                  "β — vidēja.",
                  "γ — vislielākā, bet vismazākā jonizācija.",
                  "Jo lielāka caurspiešanās, jo grūtāk aizsargāties."]),
                ("DABISKĀ", GREEN,
                 ["Notiek pati no sevis dabā.",
                  "Urāns, torijs, kālijs-40, radons.",
                  "Veido dabisko radioaktīvo fonu."]),
                ("MĀKSLĪGĀ", GOLD,
                 ["Iegūta cilvēka darbības rezultātā.",
                  "Reaktoros un paātrinātājos.",
                  "Medicīnas un rūpniecības izotopi."]),
            ]),
            ("panelis", "KĀPĒC ALFA IR BĪSTAMĀKĀ ORGANISMĀ",
             ["Alfa daļiņu aptur pat āda, tāpēc no ārpuses tā nav bīstama. "
              "Bet, ja alfa avots nokļūst organismā (ieelpojot vai ar "
              "pārtiku), visa enerģija tiek atdota nelielā audu tilpumā — "
              "tas rada vislielāko kaitējumu."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Starojuma atpazīšana",
             teksts="Starojums nenoliecās magnētiskajā laukā un tika "
                    "apturēts tikai ar 5 cm biezu svina plāksni.\n"
                    "Kāds tas ir starojums? Pamato ar diviem argumentiem!",
             dots=["Magnētiskajā laukā nenoliecas", "Aptur biezs svins"],
             jaaprekina=["Starojuma veids = ?"],
             formulas=["Noliecas laukā ⟹ ir lādiņš",
                       "Liela caurspiešanās ⟹ γ"],
             aprekins=["1)  Nenoliecas → lādiņš 0 → nav α un nav β",
                       "2)  Aptur tikai biezs svins → liela caurspiešanās",
                       "3)  Abas pazīmes atbilst gamma starojumam"],
             atbilde="Tas ir gamma starojums",
             piezime="Alfa noliektos uz vienu pusi, bēta — uz pretējo, jo to "
                     "lādiņi ir pretēji."),
        dict(nr=2, virsraksts="Sabrukšanu virkne",
             teksts="Kodols ²³⁸U (Z = 92) izstaro vienu alfa un pēc tam "
                    "divas bēta daļiņas.\nNosaki galarezultātā radušos "
                    "kodola A un Z!",
             dots=["Sākums: A = 238 ;  Z = 92", "1 α, pēc tam 2 β"],
             jaaprekina=["A = ?", "Z = ?"],
             formulas=["α: A −4, Z −2", "β: A nemainās, Z +1"],
             aprekins=["1)  Pēc α:  A = 234 ;  Z = 90",
                       "2)  Pēc 1. β:  A = 234 ;  Z = 91",
                       "3)  Pēc 2. β:  A = 234 ;  Z = 92"],
             atbilde="A = 234 ;  Z = 92 — atkal urāns, izotops ²³⁴U",
             piezime="Elements atgriezās, bet izotops ir cits — kodolā par "
                     "četrām daļiņām mazāk."),
        dict(nr=3, virsraksts="Aizsardzības biezums",
             teksts="Gamma starojuma intensitāte katros 2,0 cm svina "
                    "samazinās uz pusi. Sākumā tā ir 800 vienības.\n"
                    "Cik liela tā būs aiz 8,0 cm bieza svina?",
             dots=["I₀ = 800 vien.", "d = 8,0 cm", "d(1/2) = 2,0 cm"],
             jaaprekina=["I = ?"],
             formulas=["n = d / d(1/2)", "I = I₀ / 2ⁿ"],
             aprekins=["1)  n = 8,0 : 2,0 = 4",
                       "2)  2ⁿ = 2⁴ = 16",
                       "3)  I = 800 : 16 = 50 vienības"],
             atbilde="I = 50 vienības",
             piezime="Gamma starojumu nevar apturēt pilnībā — to var tikai "
                     "vājināt."),
        dict(nr=4, virsraksts="Jonizācija un enerģija",
             teksts="Alfa daļiņas enerģija ir 8,0·10⁻¹³ J. Vienas molekulas "
                    "jonizācijai vajadzīgi 5,0·10⁻¹⁸ J.\n"
                    "Cik molekulu daļiņa var jonizēt, atdodot visu "
                    "enerģiju?",
             dots=["E = 8,0·10⁻¹³ J", "E₁ = 5,0·10⁻¹⁸ J"],
             jaaprekina=["N = ?"],
             formulas=["N = E / E₁"],
             aprekins=["1)  N = 8,0·10⁻¹³ : 5,0·10⁻¹⁸",
                       "2)  N = 1,6·10⁵"],
             atbilde="N = 1,6·10⁵ molekulu",
             piezime="Viena alfa daļiņa var sabojāt simtiem tūkstošu "
                     "molekulu — tāpēc tā organismā ir tik bīstama."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Radioaktivitāte ir patvaļīga nestabila kodola sabrukšana; to "
            "nevar ietekmēt.",
            "α — hēlija kodols (+2), β — elektrons (−1), γ — "
            "elektromagnētiskais starojums (0).",
            "Caurspiešanās: α < β < γ; jonizācija otrādi: α > β > γ.",
            "Dabiskā radioaktivitāte veido fonu; mākslīgo iegūst reaktoros.",
        ],
        majasdarbs=[
            "Sakārto α, β, γ pēc caurspiešanās spējas un paskaidro, kas "
            "katru aptur.",
            "²²⁶Ra (Z = 88) izstaro 2 alfa un 1 bēta daļiņu. Nosaki A un Z.",
            "Gamma intensitāte uz pusi samazinās katros 3 cm. Cik paliek aiz "
            "12 cm?",
        ],
        pasvertejums=["Protu raksturot α, β un γ",
                      "Protu salīdzināt caurspiešanās spēju",
                      "Protu izsekot sabrukšanu virknei",
                      "Protu pamatot bīstamību"],
        nakama="Nākamā stunda: pussabrukšanas periods."),
),

dict(
    nr="3.6", virsraksts="Pussabrukšanas periods",
    jautajums="Cik ilgi viela paliek radioaktīva?",
    apaksraksts="Pussabrukšanas periods · Sabrukšanas grafiks · Aktivitāte",
    merkis="Iemācīties nolasīt sabrukšanas grafiku un aprēķināt atlikušo "
           "vielas daudzumu vai aktivitāti pēc vesela pussabrukšanas periodu "
           "skaita.",
    protu=["skaidrot, kas ir pussabrukšanas periods;",
           "nolasīt sabrukšanas grafiku;",
           "aprēķināt atlikumu pēc n periodiem;",
           "noteikt pagājušo laiku pēc atlikuma."],
    atkartojums="3.5. stundā noskaidrojām, ka sabrukšana notiek patvaļīgi. "
                "Viena kodola likteni paredzēt nevar — bet lielam kodolu "
                "skaitam sabrukšana notiek pēc precīzas likumsakarības.",
    uzdevumu_apraksts="Atlikums un laiks pēc pussabrukšanas periodiem",
    teorija=[
        ("Kā notiek sabrukšana", [
            ("formula", "PUSSABRUKŠANAS PERIODS  T",
             "N = N₀ / 2ⁿ          n = t / T",
             "T — laiks, kurā sabrūk puse kodolu; n — periodu skaits; "
             "N₀ — sākuma daudzums; N — atlikums.", GOLD),
            ("tabula",
             ["Periodu skaits n", "0", "1", "2", "3", "4", "5"],
             [["Pagājušais laiks", "0", "T", "2T", "3T", "4T", "5T"],
              ["Palicis (daļa)", "1", "1/2", "1/4", "1/8", "1/16", "1/32"],
              ["Palicis (%)", "100", "50", "25", "12,5", "6,25", "3,1"]],
             [3.23, 1.50, 1.50, 1.50, 1.50, 1.50, 1.50]),
            ("panelis", None,
             ["Ik pēc viena perioda paliek PUSE no tā, kas bija — nevis puse "
              "no sākuma. Tāpēc pēc diviem periodiem paliek 1/4, nevis "
              "nulle."], RED),
        ]),
        ("Pussabrukšanas periodi un aktivitāte", [
            ("divi",
             ("DAŽU IZOTOPU PERIODI", BLUE,
              ["Ogleklis-14:  5700 gadi",
               "Jods-131:  8 dienas",
               "Cēzijs-137:  30 gadi",
               "Urāns-238:  4,5 miljardi gadu"]),
             ("AKTIVITĀTE", GREEN,
              ["Sabrukumu skaits sekundē.",
               "Mērvienība: bekerels (Bq); 1 Bq = 1 sabrukums sekundē.",
               "Samazinās tāpat kā kodolu skaits:  A = A₀ / 2ⁿ"])),
            ("panelis", "KUR TO IZMANTO",
             ["Pēc ¹⁴C atlikuma nosaka organiskas izcelsmes atradumu vecumu "
              "(radiooglekļa datēšana). Pēc ²³⁸U atlikuma — iežu un pat "
              "Zemes vecumu."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atlikums pēc trim periodiem",
             teksts="Radioaktīva parauga sākuma masa ir 80 g, pussabrukšanas "
                    "periods 6 dienas.\nCik daudz nesabrukušas vielas paliks "
                    "pēc 18 dienām?",
             dots=["m₀ = 80 g", "T = 6 dienas", "t = 18 dienas"],
             jaaprekina=["m = ?"],
             formulas=["n = t / T", "m = m₀ / 2ⁿ"],
             aprekins=["1)  n = 18 : 6 = 3",
                       "2)  2ⁿ = 2³ = 8",
                       "3)  m = 80 g : 8 = 10 g"],
             atbilde="m = 10 g",
             piezime="Pārējie 70 g nav pazuduši — tie pārvērtušies citos "
                     "elementos."),
        dict(nr=2, virsraksts="Joda-131 aktivitāte",
             teksts="Joda-131 pussabrukšanas periods ir 8 dienas, sākuma "
                    "aktivitāte 4,8·10⁶ Bq.\nCik liela būs aktivitāte pēc "
                    "32 dienām?",
             dots=["A₀ = 4,8·10⁶ Bq", "T = 8 dienas", "t = 32 dienas"],
             jaaprekina=["A = ?"],
             formulas=["n = t / T", "A = A₀ / 2ⁿ"],
             aprekins=["1)  n = 32 : 8 = 4",
                       "2)  2⁴ = 16",
                       "3)  A = 4,8·10⁶ : 16 = 3,0·10⁵ Bq"],
             atbilde="A = 3,0·10⁵ Bq",
             piezime="Tāpēc pēc avārijām jods-131 ir bīstams dažas nedēļas, "
                     "bet cēzijs-137 — gadu desmitiem."),
        dict(nr=3, virsraksts="Cik laika pagājis?",
             teksts="Paraugā palikuši 12,5 % sākotnējo radioaktīvo kodolu. "
                    "Pussabrukšanas periods ir 20 minūtes.\n"
                    "Cik ilgs laiks pagājis?",
             dots=["N / N₀ = 12,5 % = 1/8", "T = 20 min"],
             jaaprekina=["t = ?"],
             formulas=["N = N₀ / 2ⁿ", "t = n · T"],
             aprekins=["1)  1/8 = 1/2³  →  n = 3",
                       "2)  t = 3 · 20 min = 60 min"],
             atbilde="t = 60 min = 1 stunda",
             piezime="12,5 % ir 1/8 — tas atbilst tieši trim periodiem."),
        dict(nr=4, virsraksts="Radiooglekļa datēšana",
             teksts="Koka atradumā ¹⁴C daudzums ir 25 % no dzīvā koka "
                    "daudzuma. ¹⁴C pussabrukšanas periods ir 5700 gadi.\n"
                    "Cik vecs ir atradums?",
             dots=["N / N₀ = 25 % = 1/4", "T = 5700 gadi"],
             jaaprekina=["t = ?"],
             formulas=["N = N₀ / 2ⁿ", "t = n · T"],
             aprekins=["1)  1/4 = 1/2²  →  n = 2",
                       "2)  t = 2 · 5700 gadi",
                       "3)  t = 11 400 gadi"],
             atbilde="t = 1,14·10⁴ gadi",
             piezime="Dzīvs organisms ¹⁴C papildina; pēc nāves papildināšana "
                     "beidzas un pulkstenis sāk tikšķēt."),
        dict(nr=5, virsraksts="Perioda noteikšana no datiem",
             teksts="Parauga aktivitāte 40 minūtēs samazinājās no "
                    "6,4·10⁵ Bq līdz 4,0·10⁴ Bq.\n"
                    "Aprēķini pussabrukšanas periodu!",
             dots=["A₀ = 6,4·10⁵ Bq", "A = 4,0·10⁴ Bq", "t = 40 min"],
             jaaprekina=["T = ?"],
             formulas=["A₀ / A = 2ⁿ", "T = t / n"],
             aprekins=["1)  A₀ / A = 6,4·10⁵ : 4,0·10⁴ = 16",
                       "2)  16 = 2⁴  →  n = 4",
                       "3)  T = 40 min : 4 = 10 min"],
             atbilde="T = 10 minūtes",
             piezime="Vispirms nosaka, cik reižu samazinājies, tad — cik tas "
                     "ir periodu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Pussabrukšanas periods T — laiks, kurā sabrūk puse kodolu.",
            "n = t/T  un  N = N₀/2ⁿ; tāpat samazinās arī aktivitāte.",
            "Pēc 1 perioda paliek 1/2, pēc 2 — 1/4, pēc 3 — 1/8.",
            "Pēc atlikuma var noteikt pagājušo laiku — tā datē atradumus.",
        ],
        majasdarbs=[
            "m₀ = 120 g, T = 4 gadi. Cik paliks pēc 12 gadiem?",
            "Aktivitāte samazinājusies 32 reizes, T = 5 dienas. Cik laika "
            "pagājis?",
            "Atradumā palikuši 6,25 % ¹⁴C (T = 5700 gadi). Cik tas vecs?",
        ],
        pasvertejums=["Protu skaidrot pussabrukšanas periodu",
                      "Protu aprēķināt atlikumu",
                      "Protu noteikt pagājušo laiku",
                      "Protu nolasīt sabrukšanas grafiku"],
        nakama="Nākamā stunda: jonizējošais starojums un dabiskais fons."),
),

dict(
    nr="3.7", virsraksts="Jonizējošais starojums un fons",
    jautajums="Cik daudz starojuma saņemam ikdienā?",
    apaksraksts="Dabiskais fons · Devas · Sīverts · Starojuma avoti",
    merkis="Iemācīties nosaukt dabiskos un mākslīgos jonizējošā starojuma "
           "avotus un salīdzināt saņemtās devas ar dabisko radioaktīvo fonu.",
    protu=["skaidrot, kas ir jonizējošais starojums;",
           "nosaukt dabiskos un mākslīgos avotus;",
           "lietot devas mērvienību sīvertu;",
           "salīdzināt devu ar gada dabisko fonu."],
    atkartojums="3.5. stundā noskaidrojām starojuma veidus. Šodien — cik "
                "daudz starojuma cilvēks saņem un kad tas kļūst bīstams.",
    uzdevumu_apraksts="Devu aprēķini un salīdzināšana ar fonu",
    teorija=[
        ("Starojuma avoti ap mums", [
            ("panelis", "JONIZĒJOŠAIS STAROJUMS",
             ["Starojums, kura enerģija pietiek, lai no atoma izsistu "
              "elektronu — atoms kļūst par jonu. Tieši tas var bojāt šūnu "
              "un DNS.",
              "Jonizējošs: α, β, γ, rentgenstarojums, neitroni. "
              "Nejonizējošs: radioviļņi, mikroviļņi, redzamā gaisma."],
             NAVY),
            ("tabula",
             ["Avots", "Veids", "Deva gadā", "Daļa no fona"],
             [["Radons telpās", "dabiskais", "1,2 mSv", "~50 %"],
              ["Kosmiskais starojums", "dabiskais", "0,4 mSv", "~16 %"],
              ["Zeme un ēku materiāli", "dabiskais", "0,5 mSv", "~20 %"],
              ["Pārtika un ūdens (⁴⁰K)", "dabiskais", "0,3 mSv", "~12 %"],
              ["Medicīna (rentgens u. c.)", "mākslīgais", "0,6 mSv",
               "papildus fonam"]],
             [3.63, 2.20, 2.20, 4.20]),
        ]),
        ("Devas un to nozīme", [
            ("formula", "DEVA UN LAIKS",
             "D = P · t          [D] = Sv (sīverts);  1 mSv = 10⁻³ Sv",
             "P — devas jauda (Sv/h vai µSv/h), t — laiks starojuma laukā. "
             "Jo ilgāk atrodas, jo lielāka deva.", GOLD),
            ("kartitas", [
                ("VIDĒJAIS FONS", GREEN,
                 ["Latvijā ~2,4 mSv gadā.",
                  "Tas ir normāls un nenovēršams.",
                  "Lielākā daļa — radons no augsnes."]),
                ("PIEMĒRI", BLUE,
                 ["Krūškurvja rentgens: 0,1 mSv",
                  "Datortomogrāfija: 10 mSv",
                  "Lidojums Rīga–Ņujorka: 0,05 mSv"]),
                ("ROBEŽAS", RED,
                 ["Iedzīvotājiem papildus fonam: 1 mSv gadā.",
                  "Strādājošiem ar starojumu: 20 mSv gadā.",
                  "Virs 1000 mSv — akūta staru slimība."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Deva laboratorijā",
             teksts="Laboratorijā devas jauda ir 25 µSv/h. Skolēns tur "
                    "uzturas 3,0 stundas.\nAprēķini saņemto devu "
                    "mikrosīvertos un milisīvertos!",
             dots=["P = 25 µSv/h", "t = 3,0 h"],
             jaaprekina=["D = ?"],
             formulas=["D = P · t"],
             aprekins=["1)  D = 25 µSv/h · 3,0 h = 75 µSv",
                       "2)  D = 75·10⁻⁶ Sv = 0,075 mSv"],
             atbilde="D = 75 µSv = 0,075 mSv",
             piezime="Tas ir mazāk nekā viens krūškurvja rentgens."),
        dict(nr=2, virsraksts="Salīdzinājums ar gada fonu",
             teksts="Datortomogrāfijas izmeklējuma deva ir 10 mSv. Vidējais "
                    "dabiskais fons Latvijā ir 2,4 mSv gadā.\n"
                    "Cik gadu dabiskajam fonam tas atbilst?",
             dots=["D = 10 mSv", "D(gadā) = 2,4 mSv"],
             jaaprekina=["n = ?"],
             formulas=["n = D / D(gadā)"],
             aprekins=["1)  n = 10 mSv : 2,4 mSv",
                       "2)  n = 4,2"],
             atbilde="n ≈ 4,2 gadu dabiskajam fonam",
             piezime="Tāpēc tomogrāfiju nozīmē tikai tad, ja ieguvums "
                     "diagnostikā pārsniedz risku."),
        dict(nr=3, virsraksts="Cik ilgi drīkst strādāt?",
             teksts="Darbinieka gada robeža ir 20 mSv. Darba vietā devas "
                    "jauda ir 8,0 µSv/h.\nCik stundas gadā viņš drīkst tur "
                    "strādāt?",
             dots=["D = 20 mSv", "P = 8,0 µSv/h"],
             jaaprekina=["t = ?  (h)"],
             formulas=["D = P · t", "t = D / P"],
             aprekins=["1)  D = 20 mSv = 20 000 µSv",
                       "2)  t = 20 000 µSv : 8,0 µSv/h",
                       "3)  t = 2,5·10³ h"],
             atbilde="t = 2500 stundas gadā",
             piezime="Tas ir vairāk nekā gada darba laiks (~1800 h), tātad "
                     "šāda darba vieta ir droša."),
        dict(nr=4, virsraksts="Lidojuma deva",
             teksts="Lidojot 10 km augstumā, devas jauda ir 5,0 µSv/h. "
                    "Lidojums ilgst 9,0 h.\n"
                    "Aprēķini devu un salīdzini to ar krūškurvja rentgenu "
                    "(0,10 mSv)!",
             dots=["P = 5,0 µSv/h", "t = 9,0 h", "D(rtg) = 0,10 mSv"],
             jaaprekina=["D = ?", "n = ?"],
             formulas=["D = P · t", "n = D / D(rtg)"],
             aprekins=["1)  D = 5,0 · 9,0 = 45 µSv = 0,045 mSv",
                       "2)  n = 0,045 : 0,10 = 0,45"],
             atbilde="D = 0,045 mSv ≈ 0,45 no rentgena devas",
             piezime="Augstumā kosmiskais starojums ir stiprāks, jo "
                     "atmosfēras slānis virs mums ir plānāks."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Jonizējošais starojums spēj izsist elektronu no atoma un bojāt "
            "šūnu.",
            "Devu mēra sīvertos; D = P · t — jo ilgāk, jo lielāka deva.",
            "Dabiskais fons Latvijā ~2,4 mSv gadā; lielākā daļa — radons.",
            "Devu vienmēr salīdzina ar gada fonu, lai novērtētu risku.",
        ],
        majasdarbs=[
            "P = 12 µSv/h, t = 5 h. Aprēķini devu mSv.",
            "Izmeklējuma deva 3,6 mSv. Cik gadu dabiskajam fonam "
            "(2,4 mSv gadā) tas atbilst?",
            "Gada robeža 1 mSv. Cik stundas drīkst uzturēties vietā, kur "
            "P = 0,5 µSv/h?",
        ],
        pasvertejums=["Protu atšķirt jonizējošu starojumu",
                      "Protu nosaukt avotus", "Protu aprēķināt devu",
                      "Protu salīdzināt devu ar fonu"],
        nakama="Nākamā stunda: radiācijas drošība."),
),

dict(
    nr="3.8", virsraksts="Radiācijas drošība",
    jautajums="Kā pasargāties no jonizējošā starojuma?",
    apaksraksts="Laiks · Attālums · Ekranēšana · Apstarošana un piesārņojums",
    merkis="Iemācīties pamatot aizsardzību ar laiku, attālumu un ekranēšanu "
           "un nošķirt apstarošanu no radioaktīva piesārņojuma.",
    protu=["nosaukt trīs aizsardzības principus;",
           "lietot attāluma kvadrāta likumu;",
           "aprēķināt devu pie mainīta laika vai attāluma;",
           "atšķirt apstarošanu no piesārņojuma."],
    atkartojums="3.7. stundā mācījāmies aprēķināt devu D = P·t. Šodien "
                "noskaidrosim, kā šo devu samazināt.",
    uzdevumu_apraksts="Aizsardzība ar laiku, attālumu un ekranēšanu",
    teorija=[
        ("Trīs aizsardzības principi", [
            ("kartitas", [
                ("LAIKS", BLUE,
                 ["Jo mazāk laika starojuma laukā, jo mazāka deva.",
                  "D = P · t",
                  "Divreiz īsāks laiks — divreiz mazāka deva."]),
                ("ATTĀLUMS", GREEN,
                 ["Attālinoties deva strauji samazinās.",
                  "P ~ 1 / r²",
                  "Divreiz tālāk — četrreiz mazāka deva.",
                  "Vienkāršākā un lētākā aizsardzība."]),
                ("EKRANĒŠANA", GOLD,
                 ["Starp avotu un cilvēku liek šķērsli.",
                  "α — papīrs;  β — alumīnijs;  γ — svins vai betons.",
                  "Jo blīvāks materiāls, jo labāk."]),
            ]),
            ("formula", "ATTĀLUMA KVADRĀTA LIKUMS",
             "P₁ · r₁² = P₂ · r₂²",
             "Attālinoties divas reizes, devas jauda samazinās četras "
             "reizes; trīs reizes tālāk — deviņas reizes mazāk.", GOLD),
        ]),
        ("Apstarošana un piesārņojums", [
            ("divi",
             ("APSTAROŠANA", BLUE,
              ["Cilvēks atrodas starojuma laukā.",
               "Aizejot no avota, apstarošana beidzas.",
               "Cilvēks NEKĻŪST radioaktīvs.",
               "Piemērs: rentgena izmeklējums."]),
             ("PIESĀRŅOJUMS", RED,
              ["Radioaktīva viela nokļūst uz ķermeņa vai iekšā.",
               "Starojums turpinās arī pēc aiziešanas.",
               "Viela jānomazgā vai jāgaida sabrukšana.",
               "Piemērs: radioaktīvi putekļi."])),
            ("panelis", "RĪCĪBA AVĀRIJAS GADĪJUMĀ",
             ["Palielini attālumu no avota  ·  samazini uzturēšanās laiku  ·  "
              "izmanto ekrānu vai telpu ar biezām sienām  ·  neēd un nedzer "
              "piesārņotā vietā  ·  novelc ārējo apģērbu un nomazgājies."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Attālinoties divas reizes",
             teksts="1,0 m attālumā no avota devas jauda ir 64 µSv/h.\n"
                    "Cik liela tā būs 2,0 m un 4,0 m attālumā?",
             dots=["r₁ = 1,0 m ;  P₁ = 64 µSv/h",
                   "r₂ = 2,0 m ;  r₃ = 4,0 m"],
             jaaprekina=["P₂ = ?", "P₃ = ?"],
             formulas=["P₁·r₁² = P₂·r₂²"],
             aprekins=["1)  P₂ = 64 · 1,0² : 2,0² = 64 : 4 = 16 µSv/h",
                       "2)  P₃ = 64 · 1,0² : 4,0² = 64 : 16 = 4 µSv/h"],
             atbilde="P₂ = 16 µSv/h ;   P₃ = 4 µSv/h",
             piezime="Attālums ir efektīvākā aizsardzība — un tā neko "
                     "nemaksā."),
        dict(nr=2, virsraksts="Drošs attālums",
             teksts="0,50 m attālumā devas jauda ir 200 µSv/h. Drošs "
                    "līmenis ir 8,0 µSv/h.\nCik tālu jāatkāpjas?",
             dots=["r₁ = 0,50 m ;  P₁ = 200 µSv/h", "P₂ = 8,0 µSv/h"],
             jaaprekina=["r₂ = ?"],
             formulas=["P₁·r₁² = P₂·r₂²", "r₂ = r₁·√(P₁/P₂)"],
             aprekins=["1)  P₁ / P₂ = 200 : 8,0 = 25",
                       "2)  √25 = 5",
                       "3)  r₂ = 0,50 m · 5 = 2,5 m"],
             atbilde="r₂ = 2,5 m",
             piezime="Devas jauda samazinājās 25 reizes, bet attālums "
                     "palielinājās tikai 5 reizes."),
        dict(nr=3, virsraksts="Laika ierobežošana",
             teksts="Pieļaujamā deva ir 50 µSv. Devas jauda darba vietā ir "
                    "120 µSv/h.\nCik ilgi tur drīkst strādāt? Izsaki "
                    "minūtēs.",
             dots=["D = 50 µSv", "P = 120 µSv/h"],
             jaaprekina=["t = ?  (min)"],
             formulas=["D = P · t", "t = D / P"],
             aprekins=["1)  t = 50 µSv : 120 µSv/h = 0,417 h",
                       "2)  t = 0,417 · 60 min = 25 min"],
             atbilde="t = 25 minūtes",
             piezime="Tāpēc šādos darbos strādā maiņās — katrs pa īsu laiku."),
        dict(nr=4, virsraksts="Ekrāns un attālums kopā",
             teksts="Devas jauda 1,0 m attālumā ir 320 µSv/h. Strādnieks "
                    "atkāpjas uz 4,0 m un uzstāda svina ekrānu, kas "
                    "samazina starojumu 5 reizes.\n"
                    "Aprēķini gala devas jaudu!",
             dots=["r₁ = 1,0 m ;  P₁ = 320 µSv/h", "r₂ = 4,0 m", "k = 5"],
             jaaprekina=["P = ?"],
             formulas=["P₂ = P₁·r₁² / r₂²", "P = P₂ / k"],
             aprekins=["1)  P₂ = 320 · 1,0² : 4,0² = 320 : 16 = 20 µSv/h",
                       "2)  P = 20 : 5 = 4,0 µSv/h"],
             atbilde="P = 4,0 µSv/h — 80 reižu mazāk nekā sākumā",
             piezime="Attālums un ekrāns darbojas kopā: 16 · 5 = 80 reizes."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Trīs aizsardzības principi: laiks, attālums, ekranēšana.",
            "P₁·r₁² = P₂·r₂² — divreiz tālāk nozīmē četrreiz mazāku devas "
            "jaudu.",
            "Ekrānu izvēlas pēc starojuma veida: α — papīrs, β — alumīnijs, "
            "γ — svins.",
            "Apstarošana beidzas, aizejot no avota; piesārņojums ceļo līdzi.",
        ],
        majasdarbs=[
            "2,0 m attālumā P = 45 µSv/h. Cik būs 6,0 m attālumā?",
            "Pieļaujamā deva 120 µSv, P = 90 µSv/h. Cik ilgi drīkst "
            "strādāt?",
            "Paskaidro ar piemēru atšķirību starp apstarošanu un "
            "piesārņojumu.",
        ],
        pasvertejums=["Protu nosaukt aizsardzības principus",
                      "Protu lietot attāluma kvadrāta likumu",
                      "Protu aprēķināt drošu laiku",
                      "Protu atšķirt apstarošanu no piesārņojuma"],
        nakama="Nākamā stunda: radioaktivitātes lietojumi."),
),

dict(
    nr="3.9", virsraksts="Radioaktivitātes lietojumi",
    jautajums="Kur izmanto radioaktīvos izotopus?",
    apaksraksts="Medicīna · Datēšana · Enerģētika · Rūpniecība",
    merkis="Ar piemēriem pamatot radioaktīvo izotopu lietojumu medicīnā, "
           "datēšanā un enerģētikā un izvērtēt ieguvumus un riskus.",
    protu=["nosaukt izotopu lietojumus dažādās nozarēs;",
           "pamatot izotopa izvēli pēc pussabrukšanas perioda;",
           "aprēķināt ar enerģijas iegūšanu saistītus lielumus;",
           "izvērtēt ieguvumus un riskus."],
    atkartojums="3.6. stundā mācījāmies pussabrukšanas periodu. Tieši tas "
                "nosaka, kuram uzdevumam izotops ir derīgs.",
    uzdevumu_apraksts="Izotopu izvēle un enerģijas aprēķini",
    teorija=[
        ("Kur izmanto radioaktīvos izotopus", [
            ("kartitas", [
                ("MEDICĪNA", BLUE,
                 ["Diagnostika: jods-131 vairogdziedzerim.",
                  "Terapija: kobalts-60 audzēju apstarošanai.",
                  "Instrumentu sterilizācija ar gamma starojumu.",
                  "Vajadzīgs ĪSS periods — lai ātri izvadītos."]),
                ("DATĒŠANA", GREEN,
                 ["Ogleklis-14 — organiskas izcelsmes atradumi.",
                  "Urāns-238 — ieži un Zemes vecums.",
                  "Vajadzīgs GARŠ periods — salīdzināms ar pētāmo vecumu."]),
                ("ENERĢĒTIKA UN RŪPNIECĪBA", GOLD,
                 ["Urāns-235 — kodoldegviela AES.",
                  "Biezuma un līmeņa mērīšana ražošanā.",
                  "Metinājumu defektoskopija.",
                  "Dūmu detektori (americijs-241)."]),
            ]),
            ("panelis", "KĀ IZVĒLAS IZOTOPU",
             ["Pēc pussabrukšanas perioda: medicīnā — stundas vai dienas, lai "
              "pacients ilgi netiktu apstarots; datēšanā — tūkstoši vai "
              "miljoni gadu.",
              "Pēc starojuma veida: diagnostikā gamma (iznāk no organisma un "
              "to var reģistrēt), terapijā — vietēji spēcīgi jonizējošs."],
             NAVY),
        ]),
        ("Ieguvumi un riski", [
            ("divi",
             ("IEGUVUMI", GREEN,
              ["Diagnoze bez operācijas.",
               "Audzēju ārstēšana.",
               "Elektroenerģija bez CO₂ izmešiem.",
               "Precīza vecuma noteikšana arheoloģijā."]),
             ("RISKI", RED,
              ["Radioaktīvi atkritumi ar ilgu periodu.",
               "Avāriju sekas (Černobiļa, Fukušima).",
               "Nepieciešama stingra kontrole un glabāšana.",
               "Pārmērīga apstarošana kaitē veselībai."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Izotopa izvēle diagnostikai",
             teksts="Diagnostikai vajadzīgs izotops, kas organismā "
                    "samazinās līdz 1/16 aptuveni divās dienās.\n"
                    "Aprēķini nepieciešamo pussabrukšanas periodu stundās!",
             dots=["N/N₀ = 1/16", "t = 2 dienas = 48 h"],
             jaaprekina=["T = ?"],
             formulas=["N = N₀ / 2ⁿ", "T = t / n"],
             aprekins=["1)  1/16 = 1/2⁴  →  n = 4",
                       "2)  T = 48 h : 4 = 12 h"],
             atbilde="T = 12 stundas",
             piezime="Īss periods nozīmē, ka pacients netiek apstarots ilgi."),
        dict(nr=2, virsraksts="Kodoldegvielas enerģija",
             teksts="Sadaloties vienam ²³⁵U kodolam, atbrīvojas "
                    "3,2·10⁻¹¹ J. 1,0 g urāna ir 2,6·10²¹ kodolu.\n"
                    "Cik enerģijas atbrīvojas, sadaloties 1,0 g urāna?",
             dots=["E₁ = 3,2·10⁻¹¹ J", "N = 2,6·10²¹"],
             jaaprekina=["E = ?"],
             formulas=["E = N · E₁"],
             aprekins=["1)  E = 2,6·10²¹ · 3,2·10⁻¹¹ J",
                       "2)  E = 8,3·10¹⁰ J"],
             atbilde="E ≈ 8,3·10¹⁰ J",
             piezime="Tikpat enerģijas dod ~2 tonnas naftas — tāpēc "
                     "kodoldegvielas vajag tik maz."),
        dict(nr=3, virsraksts="Kobalta avota novecošana",
             teksts="Kobalta-60 (T = 5,3 gadi) avota sākuma aktivitāte ir "
                    "1,6·10¹⁴ Bq.\nCik liela tā būs pēc 21,2 gadiem?",
             dots=["A₀ = 1,6·10¹⁴ Bq", "T = 5,3 gadi", "t = 21,2 gadi"],
             jaaprekina=["A = ?"],
             formulas=["n = t / T", "A = A₀ / 2ⁿ"],
             aprekins=["1)  n = 21,2 : 5,3 = 4",
                       "2)  2⁴ = 16",
                       "3)  A = 1,6·10¹⁴ : 16 = 1,0·10¹³ Bq"],
             atbilde="A = 1,0·10¹³ Bq",
             piezime="Tāpēc medicīnas avoti periodiski jānomaina."),
        dict(nr=4, virsraksts="Atomelektrostacijas jauda",
             teksts="Reaktorā vienā sekundē sadalās 2,5·10¹⁹ kodolu, katrā "
                    "atbrīvojot 3,2·10⁻¹¹ J. Lietderības koeficients ir "
                    "33 %.\nAprēķini elektrisko jaudu!",
             dots=["N = 2,5·10¹⁹ 1/s", "E₁ = 3,2·10⁻¹¹ J", "η = 33 %"],
             jaaprekina=["P = ?"],
             formulas=["P(kop) = N · E₁", "P = η · P(kop)"],
             aprekins=["1)  P(kop) = 2,5·10¹⁹ · 3,2·10⁻¹¹ = 8,0·10⁸ W",
                       "2)  P = 0,33 · 8,0·10⁸ W",
                       "3)  P = 2,6·10⁸ W = 260 MW"],
             atbilde="P ≈ 2,6·10⁸ W = 260 MW",
             piezime="Divas trešdaļas enerģijas aiziet siltumā — tāpēc AES "
                     "vajadzīga dzesēšana."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Izotopus izmanto medicīnā, datēšanā, enerģētikā un rūpniecībā.",
            "Izotopu izvēlas pēc pussabrukšanas perioda un starojuma veida.",
            "Kodoldegviela dod miljoniem reižu vairāk enerģijas nekā ķīmiskā "
            "degviela.",
            "Ieguvumi jāsver kopā ar riskiem: atkritumi, avārijas, kontrole.",
        ],
        majasdarbs=[
            "Izotopa aktivitāte 3 dienās samazinās 8 reizes. Aprēķini T.",
            "Viena kodola sadalīšanās dod 3,2·10⁻¹¹ J. Cik kodolu vajag "
            "1,0 MJ?",
            "Nosauc divus ieguvumus un divus riskus kodolenerģijai.",
        ],
        pasvertejums=["Protu nosaukt lietojumus",
                      "Protu pamatot izotopa izvēli",
                      "Protu aprēķināt enerģiju un aktivitāti",
                      "Protu izvērtēt riskus"],
        nakama="Nākamā stunda: vielas daudzums un daļiņu skaits."),
),
]


def build():
    return C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
