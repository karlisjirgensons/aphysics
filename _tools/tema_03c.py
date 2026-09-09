# -*- coding: utf-8 -*-
"""10.3. temata stundas 3.10.-3.12. (pēdējās pirms PD2)."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN
from tema_03 import TEMATS, KICKER, MAPE

STUNDAS = [

dict(
    nr="3.10", virsraksts="Vielas daudzums un daļiņu skaits",
    jautajums="Cik daļiņu ir vienā gramā vielas?",
    apaksraksts="Molmasa · Avogadro skaitlis · n = m/M = N/NA",
    merkis="Iemācīties lietot sakarību n = m/M = N/NA, lai aprēķinātu vielas "
           "daudzumu, masu un daļiņu skaitu.",
    protu=["skaidrot, kas ir viens mols un Avogadro skaitlis;",
           "noteikt molmasu pēc periodiskās tabulas;",
           "aprēķināt vielas daudzumu un daļiņu skaitu;",
           "aprēķināt vienas molekulas masu."],
    atkartojums="1.2. stundā rēķinājām, cik molekulu ietilpst 1 mm garā "
                "rindā. Tagad iemācīsimies to noteikt precīzi — ar formulu.",
    uzdevumu_apraksts="Vielas daudzums, masa un daļiņu skaits",
    teorija=[
        ("Mols un Avogadro skaitlis", [
            ("panelis", "VIELAS DAUDZUMS  n",
             ["Daļiņu ir tik daudz, ka tās skaitīt pa vienai nav iespējams. "
              "Tāpēc lieto īpašu vienību — MOLU.",
              "1 mols ir tāds vielas daudzums, kurā ir 6,02·10²³ daļiņas. "
              "Šo skaitli sauc par Avogadro skaitli NA."], NAVY),
            ("formula", "PAMATSAKARĪBA",
             "n = m / M = N / NA",
             "n — vielas daudzums [mol], m — masa [g], M — molmasa [g/mol], "
             "N — daļiņu skaits, NA = 6,02·10²³ mol⁻¹.", GOLD),
            ("panelis", "MOLMASA M",
             ["Molmasu skaitliski ņem no periodiskās tabulas relatīvās "
              "atommasas: Ar(H) = 1 → M(H) = 1 g/mol.",
              "Savienojumam molmasas saskaita: M(H₂O) = 2·1 + 16 = 18 g/mol; "
              "M(CO₂) = 12 + 2·16 = 44 g/mol."], BLUE),
        ]),
        ("Kā rēķina", [
            ("divi",
             ("NO MASAS UZ DAĻIŅĀM", BLUE,
              ["1. Nosaki M pēc periodiskās tabulas.",
               "2. n = m / M",
               "3. N = n · NA"]),
             ("VIENAS DAĻIŅAS MASA", GREEN,
              ["m₀ = M / NA",
               "Piemēram, ūdens molekulai:",
               "m₀ = 18·10⁻³ kg/mol : 6,02·10²³ mol⁻¹",
               "m₀ ≈ 3,0·10⁻²⁶ kg"])),
            ("panelis", "UZMANIES AR MĒRVIENĪBĀM",
             ["Molmasu parasti dod g/mol. SI vienībās M(H₂O) = 18·10⁻³ "
              "kg/mol. Ja masu ņem gramos, tad arī molmasu ņem g/mol — "
              "tad n iznāk molos pareizi."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vielas daudzums ūdenī",
             teksts="Glāzē ir 90 g ūdens. Ūdens molmasa ir 18 g/mol.\n"
                    "Aprēķini vielas daudzumu un ūdens molekulu skaitu!",
             dots=["m = 90 g", "M = 18 g/mol", "NA = 6,02·10²³ mol⁻¹"],
             jaaprekina=["n = ?", "N = ?"],
             formulas=["n = m / M", "N = n · NA"],
             aprekins=["1)  n = 90 g : 18 g/mol = 5,0 mol",
                       "2)  N = 5,0 mol · 6,02·10²³ mol⁻¹",
                       "3)  N = 3,0·10²⁴ molekulu"],
             atbilde="n = 5,0 mol ;   N = 3,0·10²⁴ molekulu",
             piezime="Glāzē ūdens ir vairāk molekulu nekā smilšu graudu uz "
                     "visas Zemes."),
        dict(nr=2, virsraksts="Daļiņu skaits gramā oglekļa",
             teksts="Oglekļa molmasa ir 12 g/mol.\n"
                    "Cik oglekļa atomu ir 1,0 g oglekļa?",
             dots=["m = 1,0 g", "M = 12 g/mol", "NA = 6,02·10²³ mol⁻¹"],
             jaaprekina=["N = ?"],
             formulas=["n = m / M", "N = n · NA"],
             aprekins=["1)  n = 1,0 g : 12 g/mol = 0,083 mol",
                       "2)  N = 0,083 · 6,02·10²³",
                       "3)  N = 5,0·10²² atomu"],
             atbilde="N ≈ 5,0·10²² atomu",
             piezime="Pat vienā gramā vielas ir vairāk atomu nekā zvaigžņu "
                     "novērojamajā Visumā."),
        dict(nr=3, virsraksts="Vienas molekulas masa",
             teksts="Oglekļa dioksīda CO₂ molmasa ir 44 g/mol.\n"
                    "Aprēķini vienas CO₂ molekulas masu kilogramos!",
             dots=["M = 44 g/mol = 44·10⁻³ kg/mol",
                   "NA = 6,02·10²³ mol⁻¹"],
             jaaprekina=["m₀ = ?"],
             formulas=["M = m₀ · NA", "m₀ = M / NA"],
             aprekins=["1)  m₀ = 44·10⁻³ kg/mol : 6,02·10²³ mol⁻¹",
                       "2)  m₀ = 7,3·10⁻²⁶ kg"],
             atbilde="m₀ ≈ 7,3·10⁻²⁶ kg",
             piezime="Salīdzini ar protona masu 1,67·10⁻²⁷ kg — molekula ir "
                     "~44 reizes smagāka."),
        dict(nr=4, virsraksts="Masa pēc daļiņu skaita",
             teksts="Paraugā ir 1,2·10²⁴ dzelzs atomu. Dzelzs molmasa ir "
                    "56 g/mol.\nAprēķini parauga masu!",
             dots=["N = 1,2·10²⁴", "M = 56 g/mol", "NA = 6,02·10²³ mol⁻¹"],
             jaaprekina=["m = ?"],
             formulas=["n = N / NA", "m = n · M"],
             aprekins=["1)  n = 1,2·10²⁴ : 6,02·10²³ = 2,0 mol",
                       "2)  m = 2,0 mol · 56 g/mol",
                       "3)  m = 112 g"],
             atbilde="m = 1,1·10² g ≈ 112 g",
             piezime="Formulu var lasīt abos virzienos: no masas uz daļiņām "
                     "un otrādi."),
        dict(nr=5, virsraksts="Alumīnija detaļa",
             teksts="Alumīnija detaļas tilpums ir 50 cm³, blīvums "
                    "2700 kg/m³, molmasa 27 g/mol.\n"
                    "Cik alumīnija atomu ir detaļā?",
             dots=["V = 50 cm³", "ρ = 2700 kg/m³", "M = 27 g/mol"],
             jaaprekina=["N = ?"],
             formulas=["m = ρ · V", "n = m / M", "N = n · NA"],
             aprekins=["1)  V = 50 cm³ = 5,0·10⁻⁵ m³",
                       "2)  m = 2700 · 5,0·10⁻⁵ = 0,135 kg = 135 g",
                       "3)  n = 135 : 27 = 5,0 mol",
                       "4)  N = 5,0 · 6,02·10²³ = 3,0·10²⁴"],
             atbilde="N = 3,0·10²⁴ atomu",
             piezime="Šis uzdevums saved kopā blīvumu no 1.3. stundas un "
                     "vielas daudzumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "1 mols satur NA = 6,02·10²³ daļiņas.",
            "n = m/M = N/NA — viena sakarība trim dažādiem aprēķiniem.",
            "Molmasu nosaka pēc periodiskās tabulas; savienojumam to "
            "saskaita.",
            "Vienas daļiņas masa m₀ = M / NA.",
        ],
        majasdarbs=[
            "Cik molekulu ir 36 g ūdens (M = 18 g/mol)?",
            "Aprēķini vienas skābekļa molekulas O₂ masu (M = 32 g/mol).",
            "Vara gabalā ir 3,01·10²³ atomu (M = 64 g/mol). Aprēķini masu.",
        ],
        pasvertejums=["Protu skaidrot molu un NA",
                      "Protu noteikt molmasu",
                      "Protu aprēķināt daļiņu skaitu",
                      "Protu aprēķināt vienas daļiņas masu"],
        nakama="Nākamā stunda: kristāliskas un amorfas vielas."),
),

dict(
    nr="3.11", virsraksts="Kristāliskas un amorfas vielas",
    jautajums="Kāpēc stikls nav kristāls?",
    apaksraksts="Kristālrežģis · Amorfa viela · Kušanas temperatūra",
    merkis="Iemācīties atšķirt kristālisku un amorfu uzbūvi un noteikt "
           "kristālrežģa veidu pēc vielas fizikālajām īpašībām.",
    protu=["atšķirt kristālisku vielu no amorfas;",
           "nosaukt četrus kristālrežģu veidus;",
           "noteikt režģa veidu pēc vielas īpašībām;",
           "skaidrot, kā uzbūve nosaka kušanas temperatūru."],
    atkartojums="3.10. stundā rēķinājām daļiņu skaitu vielā. Šodien "
                "noskaidrosim, kā šīs daļiņas vielā ir sakārtotas.",
    uzdevumu_apraksts="Kristālrežģi, blīvums un daļiņu izvietojums",
    teorija=[
        ("Kristāliska un amorfa uzbūve", [
            ("divi",
             ("KRISTĀLISKA VIELA", BLUE,
              ["Daļiņas sakārtotas regulārā kristālrežģī.",
               "Ir NOTEIKTA kušanas temperatūra.",
               "Kūstot temperatūra nemainās.",
               "Piemēri: sāls, metāli, dimants, ledus."]),
             ("AMORFA VIELA", RED,
              ["Daļiņas izvietotas haotiski — nav režģa.",
               "NAV noteiktas kušanas temperatūras.",
               "Sildot pakāpeniski mīkstinās.",
               "Piemēri: stikls, sveķi, plastmasa, vasks."])),
            ("panelis", "KĀPĒC STIKLS NAV KRISTĀLS",
             ["Stiklā daļiņas ir izvietotas tikpat nesakārtoti kā šķidrumā — "
              "tikai tās nespēj pārvietoties. Tāpēc stikls sildot nevis kūst "
              "noteiktā temperatūrā, bet pakāpeniski kļūst mīkstāks."],
             NAVY),
        ]),
        ("Kristālrežģu veidi", [
            ("tabula",
             ["Režģa veids", "Mezglos", "Kušanas t°", "Cietība",
              "Elektrovadītspēja", "Piemēri"],
             [["Jonu", "joni", "augsta", "cieta, trausla",
               "kausējumā un šķīdumā", "NaCl"],
              ["Atomu", "atomi", "ļoti augsta", "ļoti cieta", "nevada",
               "dimants, kvarcs"],
              ["Molekulu", "molekulas", "zema", "mīksta", "nevada",
               "ledus, joda, CO₂"],
              ["Metāliskais", "joni + brīvie e", "dažāda", "kaļama",
               "labi vada", "Fe, Cu, Al"]],
             [2.13, 2.10, 1.60, 2.10, 2.40, 1.90]),
            ("panelis", "KĀ NOTEIKT REŽĢA VEIDU PĒC ĪPAŠĪBĀM",
             ["Vada strāvu cietā veidā un ir kaļams → metāliskais režģis.  "
              "Cieta un trausla, vada tikai kausējumā → jonu režģis.",
               "Ļoti augsta kušanas temperatūra, ļoti cieta, nevada → atomu "
               "režģis.  Zema kušanas temperatūra, mīksta → molekulu režģis."],
             GREEN),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Režģa veida noteikšana",
             teksts="Viela kūst 801 °C temperatūrā, ir cieta un trausla, "
                    "cietā veidā strāvu nevada, bet kausējumā vada.\n"
                    "Kāds ir kristālrežģa veids? Pamato!",
             dots=["t(kuš) = 801 °C", "cieta, trausla",
                   "vada tikai kausējumā"],
             jaaprekina=["Režģa veids = ?"],
             formulas=["Vada kausējumā ⟹ ir brīvi joni",
                       "Trausla + augsta t(kuš) ⟹ jonu režģis"],
             aprekins=["1)  Cietā veidā nevada → nav brīvo elektronu",
                       "2)  Kausējumā vada → ir joni, kas kļūst kustīgi",
                       "3)  Trausla, augsta kušanas temperatūra"],
             atbilde="Jonu kristālrežģis (piemēram, NaCl)",
             piezime="Nātrija hlorīds kūst tieši 801 °C temperatūrā."),
        dict(nr=2, virsraksts="Daļiņu skaits kristālā",
             teksts="Sāls NaCl kristāla masa ir 11,7 g, molmasa "
                    "58,5 g/mol.\nCik NaCl formulvienību ir kristālā?",
             dots=["m = 11,7 g", "M = 58,5 g/mol", "NA = 6,02·10²³ mol⁻¹"],
             jaaprekina=["N = ?"],
             formulas=["n = m / M", "N = n · NA"],
             aprekins=["1)  n = 11,7 : 58,5 = 0,200 mol",
                       "2)  N = 0,200 · 6,02·10²³",
                       "3)  N = 1,2·10²³"],
             atbilde="N ≈ 1,2·10²³ formulvienību",
             piezime="Jonu kristālā nav atsevišķu molekulu — viss kristāls ir "
                     "viens milzīgs režģis."),
        dict(nr=3, virsraksts="Dimants un grafīts",
             teksts="Dimanta blīvums ir 3500 kg/m³, grafīta — 2200 kg/m³. "
                    "Abi sastāv tikai no oglekļa.\n"
                    "Cik reižu dimants ir blīvāks un kāpēc, ja abiem ir "
                    "vienādi atomi?",
             dots=["ρ₁ = 3500 kg/m³", "ρ₂ = 2200 kg/m³"],
             jaaprekina=["n = ?"],
             formulas=["n = ρ₁ / ρ₂"],
             aprekins=["1)  n = 3500 : 2200",
                       "2)  n = 1,6"],
             atbilde="n ≈ 1,6 — atšķiras kristālrežģa uzbūve, nevis atomi",
             piezime="Šo parādību sauc par alotropiju: viens elements, "
                     "dažādas kristāliskās formas."),
        dict(nr=4, virsraksts="Vienas šūniņas izmērs",
             teksts="1,0 cm³ vara ir 8,5·10²² atomu.\n"
                    "Aprēķini tilpumu, kas vidēji pienākas vienam atomam, un "
                    "novērtē atoma diametru! (d ≈ ∛V)",
             dots=["V = 1,0 cm³ = 1,0·10⁻⁶ m³", "N = 8,5·10²²"],
             jaaprekina=["V₀ = ?", "d = ?"],
             formulas=["V₀ = V / N", "d ≈ ∛V₀"],
             aprekins=["1)  V₀ = 1,0·10⁻⁶ : 8,5·10²² = 1,2·10⁻²⁹ m³",
                       "2)  d = ∛(1,2·10⁻²⁹) ≈ 2,3·10⁻¹⁰ m",
                       "3)  d ≈ 0,23 nm"],
             atbilde="V₀ ≈ 1,2·10⁻²⁹ m³ ;   d ≈ 2,3·10⁻¹⁰ m",
             piezime="Rezultāts sakrīt ar 1.2. stundā minēto atoma izmēru "
                     "~10⁻¹⁰ m."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Kristāliskā vielā daļiņas sakārtotas režģī; amorfā — haotiski.",
            "Kristāliskai vielai ir noteikta kušanas temperatūra, amorfai — "
            "nav.",
            "Četri režģu veidi: jonu, atomu, molekulu, metāliskais.",
            "Pēc cietības, kušanas temperatūras un vadītspējas var noteikt "
            "režģa veidu.",
        ],
        majasdarbs=[
            "Viela kūst 3550 °C, ļoti cieta, strāvu nevada. Kāds režģis?",
            "Viela kūst −57 °C, mīksta, nevada. Kāds režģis?",
            "Cik molekulu ir 18 g ledus (M = 18 g/mol)?",
        ],
        pasvertejums=["Protu atšķirt kristālisku un amorfu vielu",
                      "Protu nosaukt režģu veidus",
                      "Protu noteikt režģi pēc īpašībām",
                      "Protu aprēķināt daļiņu skaitu"],
        nakama="Nākamā stunda: uzbūve un fizikālās īpašības — temata "
               "nostiprināšana pirms PD2."),
),

dict(
    nr="3.12", virsraksts="Uzbūve un fizikālās īpašības",
    jautajums="Kā uzbūve nosaka vielas īpašības?",
    apaksraksts="Nostiprināšana · Prognozēšana · Gatavošanās PD2",
    merkis="Nostiprināt temata saturu: no atoma uzbūves un kristālrežģa veida "
           "prognozēt vielas fizikālās īpašības un sagatavoties pārbaudes "
           "darbam.",
    protu=["prognozēt īpašības pēc kristālrežģa veida;",
           "sasaistīt atoma uzbūvi, saites veidu un īpašības;",
           "izvēlēties pareizo formulu temata uzdevumos;",
           "atpazīt un labot biežākās kļūdas."],
    atkartojums="Šī ir pēdējā stunda pirms PD2. Atkārtojam visu tematu: "
                "atoma uzbūve → izotopi → radioaktivitāte → vielas daudzums "
                "→ kristālrežģi.",
    uzdevumu_apraksts="Jauktie temata uzdevumi — gatavošanās PD2",
    teorija=[
        ("Temata formulas vienuviet", [
            ("tabula",
             ["Kas jāatrod", "Formula", "Kur lieto"],
             [["Neitronu skaits", "N = A − Z", "atoma sastāvs"],
              ["Relatīvā atommasa", "Ar = (A₁w₁ + A₂w₂)/100", "izotopi"],
              ["Fotona enerģija", "E = hf ;  λ = c/f", "spektri"],
              ["Atlikums pēc sabrukšanas", "N = N₀/2ⁿ ;  n = t/T",
               "pussabrukšana"],
              ["Deva", "D = P·t ;  P₁r₁² = P₂r₂²", "drošība"],
              ["Vielas daudzums", "n = m/M = N/NA", "daļiņu skaits"],
              ["Blīvums", "ρ = m/V", "vielas raksturošana"]],
             [3.63, 4.60, 4.00]),
        ]),
        ("No uzbūves uz īpašībām", [
            ("kartitas", [
                ("1. SOLIS", BLUE,
                 ["Kādas daļiņas ir režģa mezglos?",
                  "Joni, atomi, molekulas vai",
                  "metāla joni ar brīviem elektroniem?"]),
                ("2. SOLIS", GREEN,
                 ["Cik stipra ir saite starp tām?",
                  "Stipra saite → augsta kušanas",
                  "temperatūra un liela cietība."]),
                ("3. SOLIS", GOLD,
                 ["Vai ir brīvi lādiņnesēji?",
                  "Brīvie elektroni → vada strāvu.",
                  "Kustīgi joni → vada kausējumā."]),
            ]),
            ("panelis", "BIEŽĀKĀS KĻŪDAS PĀRBAUDES DARBĀ",
             ["Sajauc A un Z  ·  aizmirst, ka bēta sabrukšanā A nemainās  ·  "
              "rēķina 1/2 no sākuma, nevis no atlikuma  ·  neizsaka cm³ "
              "kubmetros  ·  neraksta mērvienības atbildē."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Jaukts uzdevums: atoms",
             teksts="Izotopa ⁶⁵Zn kārtas skaitlis ir 30.\n"
                    "Nosaki protonu, neitronu un elektronu skaitu un "
                    "aprēķini, cik atomu ir 6,5 g šī izotopa "
                    "(M = 65 g/mol)!",
             dots=["A = 65 ;  Z = 30", "m = 6,5 g ;  M = 65 g/mol"],
             jaaprekina=["p, N, e = ?", "N(atomu) = ?"],
             formulas=["N = A − Z", "n = m / M", "N = n · NA"],
             aprekins=["1)  p = e = 30 ;  N = 65 − 30 = 35",
                       "2)  n = 6,5 : 65 = 0,10 mol",
                       "3)  N = 0,10 · 6,02·10²³ = 6,0·10²²"],
             atbilde="30 p, 35 n, 30 e ;   N = 6,0·10²² atomu",
             piezime="Uzdevums apvieno 3.1. un 3.10. stundas saturu — tieši "
                     "tā mēdz būt PD."),
        dict(nr=2, virsraksts="Jaukts uzdevums: sabrukšana",
             teksts="Izotopa (T = 15 h) sākuma aktivitāte ir 8,0·10⁵ Bq.\n"
                    "Cik liela tā būs pēc 60 h un cik procentu no sākuma tas "
                    "ir?",
             dots=["A₀ = 8,0·10⁵ Bq", "T = 15 h", "t = 60 h"],
             jaaprekina=["A = ?", "w = ?  (%)"],
             formulas=["n = t / T", "A = A₀ / 2ⁿ", "w = A/A₀ · 100 %"],
             aprekins=["1)  n = 60 : 15 = 4",
                       "2)  A = 8,0·10⁵ : 16 = 5,0·10⁴ Bq",
                       "3)  w = 1/16 · 100 % = 6,25 %"],
             atbilde="A = 5,0·10⁴ Bq ;   w = 6,25 %",
             piezime="Pēc četriem periodiem vienmēr paliek 1/16 = 6,25 %."),
        dict(nr=3, virsraksts="Jaukts uzdevums: īpašības",
             teksts="Vielas blīvums ir 8900 kg/m³, tā ir kaļama un labi vada "
                    "strāvu cietā veidā. Parauga tilpums 20 cm³, molmasa "
                    "64 g/mol.\nNosaki režģa veidu un aprēķini atomu "
                    "skaitu!",
             dots=["ρ = 8900 kg/m³", "V = 20 cm³", "M = 64 g/mol"],
             jaaprekina=["Režģis = ?", "N = ?"],
             formulas=["m = ρ·V", "n = m/M", "N = n·NA"],
             aprekins=["1)  Kaļama + vada cietā veidā → metāliskais režģis",
                       "2)  m = 8900 · 2,0·10⁻⁵ = 0,178 kg = 178 g",
                       "3)  n = 178 : 64 = 2,78 mol",
                       "4)  N = 2,78 · 6,02·10²³ = 1,7·10²⁴"],
             atbilde="Metāliskais režģis (varš); N ≈ 1,7·10²⁴ atomu",
             piezime="Blīvums 8900 kg/m³ un M = 64 g/mol norāda uz varu."),
        dict(nr=4, virsraksts="Jaukts uzdevums: drošība",
             teksts="2,0 m attālumā no avota devas jauda ir 36 µSv/h. "
                    "Strādnieks pārvietojas uz 6,0 m un strādā 4,0 h.\n"
                    "Aprēķini saņemto devu!",
             dots=["r₁ = 2,0 m ;  P₁ = 36 µSv/h", "r₂ = 6,0 m", "t = 4,0 h"],
             jaaprekina=["P₂ = ?", "D = ?"],
             formulas=["P₁r₁² = P₂r₂²", "D = P₂ · t"],
             aprekins=["1)  P₂ = 36 · 2,0² : 6,0² = 36 · 4 : 36 = 4,0 µSv/h",
                       "2)  D = 4,0 µSv/h · 4,0 h",
                       "3)  D = 16 µSv"],
             atbilde="P₂ = 4,0 µSv/h ;   D = 16 µSv",
             piezime="Vispirms pārrēķina devas jaudu jaunajā attālumā, tikai "
                     "tad reizina ar laiku."),
        dict(nr=5, virsraksts="Jaukts uzdevums: spektrs",
             teksts="Atoms izstaro fotonu ar viļņa garumu 620 nm.\n"
                    "Aprēķini frekvenci un fotona enerģiju! "
                    "(c = 3,00·10⁸ m/s; h = 6,63·10⁻³⁴ J·s)",
             dots=["λ = 620 nm", "c = 3,00·10⁸ m/s",
                   "h = 6,63·10⁻³⁴ J·s"],
             jaaprekina=["f = ?", "E = ?"],
             formulas=["λ = c/f  →  f = c/λ", "E = h·f"],
             aprekins=["1)  λ = 620 nm = 6,20·10⁻⁷ m",
                       "2)  f = 3,00·10⁸ : 6,20·10⁻⁷ = 4,84·10¹⁴ Hz",
                       "3)  E = 6,63·10⁻³⁴ · 4,84·10¹⁴ = 3,2·10⁻¹⁹ J"],
             atbilde="f ≈ 4,8·10¹⁴ Hz ;   E ≈ 3,2·10⁻¹⁹ J",
             piezime="620 nm ir sarkanā gaisma — tādu izstaro, piemēram, "
                     "neona lampas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Atoma uzbūve nosaka elementu; kristālrežģis nosaka vielas "
            "īpašības.",
            "Visas temata formulas ir datu bukletā — svarīgi izvēlēties "
            "pareizo.",
            "Sabrukšanas uzdevumos vispirms nosaka periodu skaitu n = t/T.",
            "Drošības uzdevumos vispirms pārrēķina devas jaudu, tad devu.",
        ],
        majasdarbs=[
            "Atkārto 3.1.–3.11. stundas kopsavilkumus un formulas.",
            "Izpildi vienu uzdevumu no katras stundas mājasdarba.",
            "Pārbaudi, vai katrā risinājumā ir Dots, Jāaprēķina, Formulas, "
            "Aprēķins un Atbilde ar mērvienībām.",
        ],
        pasvertejums=["Protu prognozēt īpašības pēc uzbūves",
                      "Protu izvēlēties pareizo formulu",
                      "Protu noformēt pilnu risinājumu",
                      "Esmu gatavs pārbaudes darbam"],
        nakama="Nākamā stunda: PD2 — Atoma uzbūve, radioaktivitāte un vielas "
               "uzbūve."),
),
]


def build():
    return C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
