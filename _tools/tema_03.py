# -*- coding: utf-8 -*-
"""
10.3. temats "Atoma uzbūve, vielas uzbūve, vielas stāvokļi" — fizikas daļa.
12 stundas (3.1.–3.12.), pēc tām PD2.
Stundu saraksts un jautājumi ņemti no plāna
"Dabaszinības ALL klase - 10.-12. klases saturs vienā gadā.docx".
"""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN

TEMATS = "3. temats. Atoma uzbūve, vielas uzbūve, vielas stāvokļi"
KICKER = ("DABASZINĪBAS · 10. KLASE · 3. TEMATS: ATOMA UZBŪVE, VIELAS "
          "UZBŪVE, VIELAS STĀVOKĻI")
MAPE = ("C:/aphysics/Dabaszinibas/"
        "3. Atoma uzbūve, vielas uzbūve, vielas stāvokļi")

PASV = ["Protu skaidrot", "Protu lietot formulu", "Protu veikt aprēķinu",
        "Protu pamatot atbildi"]

STUNDAS = [

# ---------------------------------------------------------------------- 3.1.
dict(
    nr="3.1", virsraksts="Atoma uzbūve",
    jautajums="No kā sastāv atoms?",
    apaksraksts="Kodols · Elektronapvalks · Protoni, neitroni, elektroni",
    merkis="Izprast atoma uzbūvi un iemācīties noteikt protonu, neitronu un "
           "elektronu skaitu, izmantojot ķīmisko elementu periodisko tabulu.",
    protu=["nosaukt atoma sastāvdaļas un to lādiņus;",
           "nolasīt kārtas skaitli un masas skaitli;",
           "aprēķināt protonu, neitronu un elektronu skaitu;",
           "pamatot, kāpēc atoms kopumā ir neitrāls."],
    atkartojums="1.2. stundā noskaidrojām: atoms ~10⁻¹⁰ m, kodols ~10⁻¹⁴ m — "
                "atoms ir par četrām kārtām lielāks nekā tā kodols.",
    uzdevumu_apraksts="Daļiņu skaits atomā",
    teorija=[
        ("Atoma sastāvdaļas", [
            ("kartitas", [
                ("PROTONS  p", RED,
                 ["Atrodas kodolā.", "Lādiņš: pozitīvs (+1)",
                  "Masa ≈ 1,67·10⁻²⁷ kg",
                  "Skaits = kārtas skaitlis Z"]),
                ("NEITRONS  n", BLUE,
                 ["Atrodas kodolā.", "Lādiņš: nav (0)",
                  "Masa ≈ protona masai", "Skaits N = A − Z"]),
                ("ELEKTRONS  e", GREEN,
                 ["Ap kodolu, elektronapvalkā.", "Lādiņš: negatīvs (−1)",
                  "Masa ≈ 9,1·10⁻³¹ kg",
                  "Neitrālā atomā skaits = Z"]),
            ]),
            ("panelis", "KODOLS UN ELEKTRONAPVALKS",
             ["Kodolā ir protoni un neitroni — tur ir gandrīz visa atoma "
              "masa, jo protons ir ~1800 reižu smagāks par elektronu.",
              "Elektronapvalks aizņem gandrīz visu atoma tilpumu, bet tā "
              "masa ir niecīga. Tāpēc atoms ir galvenokārt tukšums."], NAVY),
        ]),
        ("Kā nolasīt periodisko tabulu", [
            ("formula", "APZĪMĒJUMS", "Z — kārtas skaitlis     "
             "A — masas skaitlis     N = A − Z",
             "Z = protonu skaits = elektronu skaits neitrālā atomā; "
             "A = protonu un neitronu kopskaits kodolā.", GOLD),
            ("tabula",
             ["Elements", "Z", "A", "Protoni", "Neitroni", "Elektroni"],
             [["Ūdeņradis H", "1", "1", "1", "0", "1"],
              ["Ogleklis C", "6", "12", "6", "6", "6"],
              ["Skābeklis O", "8", "16", "8", "8", "8"],
              ["Dzelzs Fe", "26", "56", "26", "30", "26"],
              ["Urāns U", "92", "238", "92", "146", "92"]],
             [3.23, 1.50, 1.50, 2.00, 2.00, 2.00]),
            ("panelis", None,
             ["Atoms kopumā ir neitrāls, jo pozitīvo protonu skaits ir "
              "vienāds ar negatīvo elektronu skaitu: (+Z) + (−Z) = 0."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Alumīnija atoms",
             teksts="Alumīnija atoma kārtas skaitlis ir 13, masas skaitlis "
                    "27.\nCik alumīnija atomā ir protonu, neitronu un "
                    "elektronu?",
             dots=["Z = 13", "A = 27"],
             jaaprekina=["p = ?", "n = ?", "e = ?"],
             formulas=["p = Z", "N = A − Z", "e = Z"],
             aprekins=["1)  p = Z = 13",
                       "2)  N = A − Z = 27 − 13 = 14",
                       "3)  e = Z = 13"],
             atbilde="13 protoni, 14 neitroni, 13 elektroni",
             piezime="Neitrālā atomā elektronu skaits vienmēr sakrīt ar "
                     "protonu skaitu."),
        dict(nr=2, virsraksts="Nezināms elements",
             teksts="Atoma kodolā ir 17 protoni un 18 neitroni.\n"
                    "Nosaki masas skaitli un ar periodiskās tabulas "
                    "palīdzību — elementu!",
             dots=["p = 17", "N = 18"],
             jaaprekina=["A = ?", "Elements = ?"],
             formulas=["A = p + N", "Z = p"],
             aprekins=["1)  A = 17 + 18 = 35",
                       "2)  Z = 17 → hlors Cl"],
             atbilde="A = 35 ;  elements ir hlors (Cl)",
             piezime="Elementu nosaka TIKAI protonu skaits, nevis neitronu "
                     "skaits."),
        dict(nr=3, virsraksts="Atoma masas sadalījums",
             teksts="Oglekļa atomā ir 6 protoni, 6 neitroni un 6 elektroni. "
                    "Protona masa 1,67·10⁻²⁷ kg, elektrona 9,1·10⁻³¹ kg.\n"
                    "Cik procentu atoma masas ir elektronapvalkā?",
             dots=["p = n = 6 ;  e = 6", "m(p) = 1,67·10⁻²⁷ kg",
                   "m(e) = 9,1·10⁻³¹ kg"],
             jaaprekina=["w = ?  (%)"],
             formulas=["m(kod) = 12 · m(p)", "w = m(e·6) / m(kop) · 100 %"],
             aprekins=["1)  m(kod) = 12 · 1,67·10⁻²⁷ kg = 2,00·10⁻²⁶ kg",
                       "2)  m(e·6) = 6 · 9,1·10⁻³¹ kg = 5,5·10⁻³⁰ kg",
                       "3)  w = 5,5·10⁻³⁰ : 2,00·10⁻²⁶ · 100 % = 0,027 %"],
             atbilde="w ≈ 0,03 % — gandrīz visa masa ir kodolā",
             piezime="Tāpēc atoma masu praktiski nosaka masas skaitlis A."),
        dict(nr=4, virsraksts="Jons",
             teksts="Nātrija atoms (Z = 11, A = 23) atdod vienu elektronu un "
                    "kļūst par jonu Na⁺.\n"
                    "Cik jonā ir protonu, neitronu un elektronu? Kāds ir tā "
                    "lādiņš?",
             dots=["Z = 11", "A = 23", "atdots 1 elektrons"],
             jaaprekina=["p = ?", "N = ?", "e = ?"],
             formulas=["p = Z", "N = A − Z", "e = Z − 1"],
             aprekins=["1)  p = 11 ;  N = 23 − 11 = 12",
                       "2)  e = 11 − 1 = 10",
                       "3)  lādiņš = (+11) + (−10) = +1"],
             atbilde="11 protoni, 12 neitroni, 10 elektroni; lādiņš +1",
             piezime="Kodols nemainās — mainās tikai elektronu skaits, tāpēc "
                     "elements paliek nātrijs."),
        dict(nr=5, virsraksts="Kodola izmērs",
             teksts="Atoma diametrs ir 1,0·10⁻¹⁰ m, kodola — 1,0·10⁻¹⁴ m.\n"
                    "Cik reižu atoma TILPUMS ir lielāks par kodola tilpumu? "
                    "(V ~ d³)",
             dots=["d(at) = 1,0·10⁻¹⁰ m", "d(kod) = 1,0·10⁻¹⁴ m"],
             jaaprekina=["n = ?", "N = ?"],
             formulas=["n = d(at) / d(kod)", "N = n³"],
             aprekins=["1)  n = 10⁻¹⁰ : 10⁻¹⁴ = 10⁴",
                       "2)  N = (10⁴)³ = 10¹²"],
             atbilde="N = 10¹² — miljons miljonu reižu",
             piezime="Ja kodols būtu ķirsis, atoms sniegtos vairāk nekā "
                     "kilometra attālumā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Atomu veido kodols (protoni + neitroni) un elektronapvalks.",
            "Z — protonu skaits, nosaka elementu; A — protonu un neitronu "
            "kopskaits.",
            "N = A − Z; neitrālā atomā e = Z.",
            "Gandrīz visa atoma masa ir kodolā, gandrīz viss tilpums — "
            "elektronapvalkā.",
        ],
        majasdarbs=[
            "Nosaki p, N un e atomiem: ¹⁴N (Z = 7), ³⁵Cl (Z = 17), "
            "⁵⁶Fe (Z = 26).",
            "Kodolā ir 20 protoni un 20 neitroni. Kāds ir A un kāds "
            "elements?",
            "Jonam Cl⁻ (Z = 17, A = 35) nosaki p, N, e un lādiņu.",
        ],
        pasvertejums=["Protu nosaukt atoma daļiņas",
                      "Protu nolasīt Z un A", "Protu aprēķināt N un e",
                      "Protu skaidrot atoma neitralitāti"],
        nakama="Nākamā stunda: izotopi un relatīvā atommasa."),
),

# ---------------------------------------------------------------------- 3.2.
dict(
    nr="3.2", virsraksts="Izotopi un relatīvā atommasa",
    jautajums="Ar ko atšķiras viena elementa atomi?",
    apaksraksts="Izotopi · Relatīvā atommasa · Vidējā svērtā vērtība",
    merkis="Iemācīties salīdzināt izotopu kodola sastāvu un aprēķināt "
           "ķīmiskā elementa relatīvo atommasu pēc izotopu sastāva dabā.",
    protu=["skaidrot, kas ir izotopi, un tos pierakstīt;",
           "salīdzināt izotopu kodola sastāvu;",
           "aprēķināt relatīvo atommasu pēc izotopu īpatsvara;",
           "pamatot, kāpēc tabulā atommasas nav veseli skaitļi."],
    atkartojums="3.1. stundā noskaidrojām: elementu nosaka protonu skaits Z, "
                "bet neitronu skaits N = A − Z var atšķirties.",
    uzdevumu_apraksts="Izotopi un relatīvās atommasas aprēķini",
    teorija=[
        ("Kas ir izotopi", [
            ("panelis", "IZOTOPI",
             ["IZOTOPI ir viena ķīmiskā elementa atomi ar VIENĀDU protonu "
              "skaitu (Z), bet ATŠĶIRĪGU neitronu skaitu (N).",
              "Tāpēc tiem ir vienādas ķīmiskās īpašības, bet atšķirīga masa. "
              "Pieraksta: ¹²C un ¹⁴C jeb ogleklis-12 un ogleklis-14."], NAVY),
            ("tabula",
             ["Izotops", "Z (protoni)", "N (neitroni)", "A", "Īpatsvars dabā"],
             [["Ūdeņradis ¹H", "1", "0", "1", "99,98 %"],
              ["Deitērijs ²H", "1", "1", "2", "0,02 %"],
              ["Tritijs ³H", "1", "2", "3", "pēdas, radioaktīvs"],
              ["Ogleklis ¹²C", "6", "6", "12", "98,9 %"],
              ["Ogleklis ¹⁴C", "6", "8", "14", "pēdas, radioaktīvs"]],
             [3.03, 2.20, 2.30, 1.40, 3.30]),
        ]),
        ("Relatīvā atommasa", [
            ("formula", "VIDĒJĀ SVĒRTĀ VĒRTĪBA",
             "Ar = (A₁ · w₁ + A₂ · w₂ + …) / 100 %",
             "A — izotopa masas skaitlis, w — tā īpatsvars dabā procentos.",
             GOLD),
            ("divi",
             ("PIEMĒRS — hlors", BLUE,
              ["³⁵Cl — 75 %,  ³⁷Cl — 25 %",
               "Ar = (35 · 75 + 37 · 25) / 100",
               "Ar = (2625 + 925) / 100 = 35,5"]),
             ("KĀPĒC NE VESELS SKAITLIS", GREEN,
              ["Tabulā redzamā atommasa ir dabā sastopamo izotopu VIDĒJĀ "
               "vērtība.",
               "Tāpēc Ar(Cl) = 35,5, nevis 35 vai 37.",
               "Atsevišķa atoma A vienmēr ir vesels skaitlis."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Divi izotopi",
             teksts="Elementa izotopiem ⁶³Cu un ⁶⁵Cu kārtas skaitlis ir "
                    "29.\nCik neitronu ir katrā izotopā un ar cik neitroniem "
                    "tie atšķiras?",
             dots=["Z = 29", "A₁ = 63 ;  A₂ = 65"],
             jaaprekina=["N₁ = ?", "N₂ = ?", "ΔN = ?"],
             formulas=["N = A − Z"],
             aprekins=["1)  N₁ = 63 − 29 = 34",
                       "2)  N₂ = 65 − 29 = 36",
                       "3)  ΔN = 36 − 34 = 2"],
             atbilde="N₁ = 34 ;  N₂ = 36 ;  atšķiras par 2 neitroniem",
             piezime="Protonu skaits abiem vienāds — tāpēc abi ir varš."),
        dict(nr=2, virsraksts="Hlora relatīvā atommasa",
             teksts="Dabā hloru veido divi izotopi: ³⁵Cl (75 %) un ³⁷Cl "
                    "(25 %).\nAprēķini hlora relatīvo atommasu!",
             dots=["A₁ = 35 ;  w₁ = 75 %", "A₂ = 37 ;  w₂ = 25 %"],
             jaaprekina=["Ar = ?"],
             formulas=["Ar = (A₁·w₁ + A₂·w₂) / 100 %"],
             aprekins=["1)  A₁·w₁ = 35 · 75 = 2625",
                       "2)  A₂·w₂ = 37 · 25 = 925",
                       "3)  Ar = (2625 + 925) : 100 = 35,5"],
             atbilde="Ar(Cl) = 35,5",
             piezime="Vērtība tuvāka 35, jo vieglākā izotopa dabā ir vairāk."),
        dict(nr=3, virsraksts="Vara relatīvā atommasa",
             teksts="Dabā vara izotopu īpatsvars ir: ⁶³Cu — 69 %, ⁶⁵Cu — "
                    "31 %.\nAprēķini vara relatīvo atommasu!",
             dots=["A₁ = 63 ;  w₁ = 69 %", "A₂ = 65 ;  w₂ = 31 %"],
             jaaprekina=["Ar = ?"],
             formulas=["Ar = (A₁·w₁ + A₂·w₂) / 100 %"],
             aprekins=["1)  63 · 69 = 4347",
                       "2)  65 · 31 = 2015",
                       "3)  Ar = (4347 + 2015) : 100 = 63,6"],
             atbilde="Ar(Cu) ≈ 63,6",
             piezime="Salīdzini ar periodisko tabulu — tur norādīts 63,55."),
        dict(nr=4, virsraksts="Izotopa īpatsvara noteikšana",
             teksts="Litijam ir divi izotopi: ⁶Li un ⁷Li. Relatīvā atommasa "
                    "ir 6,94.\nAprēķini, cik procentu dabā ir izotopa ⁷Li!",
             dots=["A₁ = 6 ;  A₂ = 7", "Ar = 6,94"],
             jaaprekina=["w₂ = ?  (%)"],
             formulas=["Ar = (6·(100 − w₂) + 7·w₂) / 100"],
             aprekins=["1)  694 = 600 − 6w₂ + 7w₂",
                       "2)  694 = 600 + w₂",
                       "3)  w₂ = 94 %"],
             atbilde="⁷Li dabā ir 94 %,  ⁶Li — 6 %",
             piezime="Ja Ar ir tuvu lielākajam A, tad tā izotopa dabā ir "
                     "visvairāk."),
        dict(nr=5, virsraksts="Urāna izotopi",
             teksts="Urāna izotopiem ²³⁵U un ²³⁸U kārtas skaitlis ir 92.\n"
                    "Cik neitronu ir katrā? Cik reižu ²³⁸U dabā ir vairāk, "
                    "ja to īpatsvars ir 99,3 % un 0,7 %?",
             dots=["Z = 92", "A₁ = 235 ;  A₂ = 238",
                   "w₁ = 0,7 % ;  w₂ = 99,3 %"],
             jaaprekina=["N₁ = ?", "N₂ = ?", "n = ?"],
             formulas=["N = A − Z", "n = w₂ / w₁"],
             aprekins=["1)  N₁ = 235 − 92 = 143",
                       "2)  N₂ = 238 − 92 = 146",
                       "3)  n = 99,3 : 0,7 ≈ 142"],
             atbilde="N₁ = 143 ;  N₂ = 146 ;  ²³⁸U ir ~142 reižu vairāk",
             piezime="Tieši retais ²³⁵U ir kodoldegviela — tāpēc urānu "
                     "jābagātina."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Izotopiem ir vienāds Z, bet atšķirīgs N un tātad atšķirīgs A.",
            "Izotopu ķīmiskās īpašības ir vienādas, masa — atšķirīga.",
            "Ar = (A₁·w₁ + A₂·w₂ + …) / 100 % — vidējā svērtā vērtība.",
            "Tabulas atommasas nav veseli skaitļi, jo tās ir izotopu vidējās "
            "vērtības.",
        ],
        majasdarbs=[
            "Nosaki N izotopiem ¹⁶O, ¹⁸O (Z = 8) un ⁴⁰K, ⁴¹K (Z = 19).",
            "Bors: ¹⁰B — 20 %, ¹¹B — 80 %. Aprēķini Ar.",
            "Elementam ir izotopi ⁶⁹X (60 %) un ⁷¹X (40 %). Aprēķini Ar un "
            "atrodi elementu periodiskajā tabulā.",
        ],
        pasvertejums=["Protu izskaidrot izotopus",
                      "Protu aprēķināt N", "Protu aprēķināt Ar",
                      "Protu pamatot, kāpēc Ar nav vesels skaitlis"],
        nakama="Nākamā stunda: elektronu enerģijas līmeņi un atoma spektri."),
),

# ---------------------------------------------------------------------- 3.3.
dict(
    nr="3.3", virsraksts="Elektronu enerģijas līmeņi",
    jautajums="Kāpēc atoms izstaro noteiktas krāsas gaismu?",
    apaksraksts="Enerģijas līmeņi · Kvants · Spektra līnijas · E = hf",
    merkis="Izprast, ka elektrona enerģija atomā ir diskrēta, un iemācīties "
           "saistīt elektrona pāreju starp līmeņiem ar izstarotās gaismas "
           "frekvenci un krāsu.",
    protu=["skaidrot, kas ir enerģijas līmenis un kvants;",
           "saistīt elektrona pāreju ar spektra līniju;",
           "lietot E = hf un λ = c/f;",
           "atšķirt nepārtrauktu spektru no līniju spektra."],
    atkartojums="3.1. stundā noskaidrojām, ka elektroni atrodas "
                "elektronapvalkā ap kodolu. Šodien — kāpēc tie var atrasties "
                "tikai noteiktās vietās.",
    uzdevumu_apraksts="Fotona enerģija, frekvence un viļņa garums",
    teorija=[
        ("Enerģijas līmeņi un kvants", [
            ("panelis", "DISKRĒTI ENERĢIJAS LĪMEŅI",
             ["Elektrons atomā nevar atrasties jebkurā vietā — tam ir tikai "
              "noteiktas atļautās enerģijas vērtības jeb ENERĢIJAS LĪMEŅI.",
              "Elektrons var pārlēkt no viena līmeņa uz otru, bet nevar "
              "atrasties starp tiem — kā uz kāpņu pakāpieniem, nevis uz "
              "rampas."], NAVY),
            ("kartitas", [
                ("UZŅEM ENERĢIJU", BLUE,
                 ["Elektrons pārlec uz AUGSTĀKU līmeni.",
                  "Atoms ir ierosinātā stāvoklī.",
                  "Enerģija tiek absorbēta."]),
                ("ATDOD ENERĢIJU", RED,
                 ["Elektrons atgriežas ZEMĀKĀ līmenī.",
                  "Izstaro fotonu — gaismas kvantu.",
                  "Enerģija E = hf"]),
                ("KRĀSA", GREEN,
                 ["Fotona enerģija nosaka frekvenci,",
                  "frekvence nosaka krāsu.",
                  "Tāpēc katram elementam savs spektrs."]),
            ]),
        ]),
        ("Fotona enerģija un spektri", [
            ("formula", "FOTONA ENERĢIJA",
             "E = hf        λ = c / f        h = 6,63·10⁻³⁴ J·s",
             "E — fotona enerģija [J], f — frekvence [Hz], "
             "λ — viļņa garums [m], c = 3,00·10⁸ m/s.", GOLD),
            ("divi",
             ("NEPĀRTRAUKTS SPEKTRS", BLUE,
              ["Visas krāsas bez pārtraukuma — varavīksne.",
               "Rada karsti cieti ķermeņi un šķidrumi.",
               "Piemēram, kvēlspuldze vai Saules virsma."]),
             ("LĪNIJU SPEKTRS", GREEN,
              ["Tikai atsevišķas spilgtas līnijas.",
               "Rada atsevišķu atomu gāze.",
               "Katram elementam savs — kā pirkstu nospiedums.",
               "Pēc tā nosaka zvaigžņu sastāvu."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Sarkanās gaismas fotona enerģija",
             teksts="Sarkanās gaismas frekvence ir 4,3·10¹⁴ Hz, "
                    "h = 6,63·10⁻³⁴ J·s.\nAprēķini viena fotona enerģiju!",
             dots=["f = 4,3·10¹⁴ Hz", "h = 6,63·10⁻³⁴ J·s"],
             jaaprekina=["E = ?"],
             formulas=["E = h · f"],
             aprekins=["1)  E = 6,63·10⁻³⁴ J·s · 4,3·10¹⁴ Hz",
                       "2)  E = 28,5·10⁻²⁰ J = 2,9·10⁻¹⁹ J"],
             atbilde="E ≈ 2,9·10⁻¹⁹ J",
             piezime="Viena fotona enerģija ir ļoti maza — tāpēc gaismu "
                     "uztveram kā nepārtrauktu."),
        dict(nr=2, virsraksts="No viļņa garuma uz frekvenci",
             teksts="Nātrija tvaiku lampas dzeltenās līnijas viļņa garums ir "
                    "589 nm.\nAprēķini gaismas frekvenci un fotona enerģiju!",
             dots=["λ = 589 nm", "c = 3,00·10⁸ m/s", "h = 6,63·10⁻³⁴ J·s"],
             jaaprekina=["f = ?", "E = ?"],
             formulas=["λ = c / f  →  f = c / λ", "E = h · f"],
             aprekins=["1)  λ = 589 nm = 5,89·10⁻⁷ m",
                       "2)  f = 3,00·10⁸ : 5,89·10⁻⁷ = 5,09·10¹⁴ Hz",
                       "3)  E = 6,63·10⁻³⁴ · 5,09·10¹⁴ = 3,4·10⁻¹⁹ J"],
             atbilde="f ≈ 5,1·10¹⁴ Hz ;   E ≈ 3,4·10⁻¹⁹ J",
             piezime="Tieši šī līnija piešķir ielu lampām dzelteno krāsu."),
        dict(nr=3, virsraksts="Enerģijas pāreja",
             teksts="Elektrons pāriet no līmeņa ar enerģiju 5,4·10⁻¹⁹ J uz "
                    "līmeni ar enerģiju 2,2·10⁻¹⁹ J.\n"
                    "Aprēķini izstarotā fotona enerģiju un frekvenci!",
             dots=["E₁ = 5,4·10⁻¹⁹ J", "E₂ = 2,2·10⁻¹⁹ J",
                   "h = 6,63·10⁻³⁴ J·s"],
             jaaprekina=["E = ?", "f = ?"],
             formulas=["E = E₁ − E₂", "E = h·f  →  f = E / h"],
             aprekins=["1)  E = 5,4·10⁻¹⁹ − 2,2·10⁻¹⁹ = 3,2·10⁻¹⁹ J",
                       "2)  f = 3,2·10⁻¹⁹ : 6,63·10⁻³⁴",
                       "3)  f = 4,8·10¹⁴ Hz"],
             atbilde="E = 3,2·10⁻¹⁹ J ;   f ≈ 4,8·10¹⁴ Hz",
             piezime="4,8·10¹⁴ Hz atbilst oranžai gaismai."),
        dict(nr=4, virsraksts="Zaļās gaismas viļņa garums",
             teksts="Fotona enerģija ir 3,8·10⁻¹⁹ J.\n"
                    "Aprēķini gaismas viļņa garumu nanometros un nosaki "
                    "krāsu! (zaļa ≈ 500–560 nm)",
             dots=["E = 3,8·10⁻¹⁹ J", "h = 6,63·10⁻³⁴ J·s",
                   "c = 3,00·10⁸ m/s"],
             jaaprekina=["λ = ?  (nm)"],
             formulas=["E = h·f", "λ = c / f = h·c / E"],
             aprekins=["1)  f = 3,8·10⁻¹⁹ : 6,63·10⁻³⁴ = 5,73·10¹⁴ Hz",
                       "2)  λ = 3,00·10⁸ : 5,73·10¹⁴ = 5,2·10⁻⁷ m",
                       "3)  λ = 520 nm"],
             atbilde="λ ≈ 520 nm — zaļa gaisma",
             piezime="Jo lielāka fotona enerģija, jo mazāks viļņa garums."),
        dict(nr=5, virsraksts="Fotonu skaits",
             teksts="Lāzera stara jauda ir 2,0 mW, viena fotona enerģija "
                    "3,1·10⁻¹⁹ J.\nCik fotonu lāzers izstaro vienā "
                    "sekundē?",
             dots=["P = 2,0 mW", "E = 3,1·10⁻¹⁹ J", "t = 1,0 s"],
             jaaprekina=["N = ?"],
             formulas=["A = P · t", "N = A / E"],
             aprekins=["1)  P = 2,0 mW = 2,0·10⁻³ W",
                       "2)  A = 2,0·10⁻³ W · 1,0 s = 2,0·10⁻³ J",
                       "3)  N = 2,0·10⁻³ : 3,1·10⁻¹⁹ = 6,5·10¹⁵"],
             atbilde="N ≈ 6,5·10¹⁵ fotonu sekundē",
             piezime="Pat vājš lāzers izstaro tūkstošiem miljardu fotonu "
                     "sekundē."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Elektrona enerģija atomā ir diskrēta — tikai noteikti līmeņi.",
            "Pārejot uz zemāku līmeni, atoms izstaro fotonu ar enerģiju "
            "E = hf.",
            "λ = c/f: lielāka enerģija → augstāka frekvence → mazāks viļņa "
            "garums.",
            "Līniju spektrs ir katra elementa “pirkstu nospiedums” — pēc tā "
            "nosaka zvaigžņu sastāvu.",
        ],
        majasdarbs=[
            "f = 6,0·10¹⁴ Hz. Aprēķini fotona enerģiju.",
            "λ = 450 nm. Aprēķini frekvenci un fotona enerģiju.",
            "Elektrons pāriet no 8,0·10⁻¹⁹ J uz 3,0·10⁻¹⁹ J. Aprēķini "
            "izstarotā fotona frekvenci un viļņa garumu.",
        ],
        pasvertejums=["Protu skaidrot enerģijas līmeņus",
                      "Protu lietot E = hf", "Protu lietot λ = c/f",
                      "Protu atšķirt spektru veidus"],
        nakama="Nākamā stunda: kodolreakcijas — kā rodas jauns ķīmiskais "
               "elements."),
),
]


def build():
    return C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.split("/")[-1]))
