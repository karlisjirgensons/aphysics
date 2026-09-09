# -*- coding: utf-8 -*-
"""10.14./10.15. Enerģija dabā un tehnikā (8 st., pēc tam PD9)
un gatavošanās eksāmenam (3 st.)."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN

T15 = "14.–15. temats. Enerģija dabā un tehnikā"
K15 = ("DABASZINĪBAS · 10. KLASE · 14.–15. TEMATS: ENERĢIJA DABĀ UN "
       "TEHNIKĀ")
M15 = "C:/aphysics/Dabaszinibas/14.-15. Enerģija dabā un tehnikā"

T16 = "Gatavošanās centralizētajam eksāmenam"
K16 = "DABASZINĪBAS · 10. KLASE · GATAVOŠANĀS EKSĀMENAM"
M16 = "C:/aphysics/Dabaszinibas/16. Gatavošanās eksāmenam"

ST15 = [

dict(
    nr="15.1", virsraksts="Darbs, enerģija, jauda",
    jautajums="Kas fizikā ir darbs?",
    apaksraksts="A = F·s · P = A/t · Vats un džouls",
    merkis="Iemācīties aprēķināt mehānisko darbu un jaudu un atšķirt "
           "sadzīves “darbu” no fizikālā darba.",
    protu=["skaidrot, kad tiek veikts mehānisks darbs;",
           "lietot A = F·s;",
           "lietot P = A/t;",
           "pārvērst enerģijas un jaudas mērvienības."],
    atkartojums="7.10. stundā mācījāmies par spēku. Ja spēks pārvieto "
                "ķermeni, tiek veikts DARBS.",
    uzdevumu_apraksts="Darbs, jauda un enerģijas mērvienības",
    teorija=[
        ("Darbs un jauda", [
            ("formula", "DARBS UN JAUDA",
             "A = F · s        P = A / t        [A] = J ;  [P] = W",
             "Darbs tiek veikts tikai tad, ja spēks pārvieto ķermeni spēka "
             "virzienā. 1 J = 1 N·m; 1 W = 1 J/s.", GOLD),
            ("divi",
             ("DARBS TIEK VEIKTS", GREEN,
              ["Ceļ somu augšup.",
               "Stumj ratiņus uz priekšu.",
               "Vilcējs velk vagonu.",
               "Spēks un pārvietojums vienā virzienā."]),
             ("DARBS NETIEK VEIKTS", RED,
              ["Tur somu rokā nekustīgi (s = 0).",
               "Stumj sienu, kas nekustas.",
               "Nes somu horizontāli — smaguma spēks",
               "perpendikulārs pārvietojumam."])),
        ]),
        ("Mērvienības", [
            ("tabula",
             ["Lielums", "Mērvienība", "Sakarība", "Piemērs"],
             [["Darbs, enerģija", "džouls (J)", "1 J = 1 N·m",
               "pacelt 1 kg par 10 cm"],
              ["Jauda", "vats (W)", "1 W = 1 J/s", "LED spuldze 8 W"],
              ["Enerģija sadzīvē", "kilovatstunda", "1 kWh = 3,6·10⁶ J",
               "elektrības rēķins"],
              ["Liela jauda", "kilovats (kW)", "1 kW = 10³ W",
               "tējkanna 2 kW"]],
             [3.13, 2.80, 3.10, 3.20]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kastes pārvietošana",
             teksts="Kasti stumj ar spēku 250 N par 12 m.\n"
                    "Aprēķini veikto darbu!",
             dots=["F = 250 N", "s = 12 m"],
             jaaprekina=["A = ?"],
             formulas=["A = F · s"],
             aprekins=["1)  A = 250 N · 12 m",
                       "2)  A = 3,0·10³ J = 3,0 kJ"],
             atbilde="A = 3,0 kJ",
             piezime="1 J ir mazs — tāpēc praksē bieži lieto kilodžoulus."),
        dict(nr=2, virsraksts="Celtņa jauda",
             teksts="Celtnis paceļ 500 kg kravu 12 m augstumā 20 s laikā. "
                    "g = 9,81 m/s².\nAprēķini darbu un jaudu!",
             dots=["m = 500 kg", "h = 12 m", "t = 20 s"],
             jaaprekina=["A = ?", "P = ?"],
             formulas=["F = m·g", "A = F·h", "P = A/t"],
             aprekins=["1)  F = 500 · 9,81 = 4905 N",
                       "2)  A = 4905 · 12 = 5,9·10⁴ J",
                       "3)  P = 5,9·10⁴ : 20 = 2,9·10³ W"],
             atbilde="A ≈ 5,9·10⁴ J ;   P ≈ 2,9 kW",
             piezime="Ceļot vertikāli, spēks ir vienāds ar smaguma spēku."),
        dict(nr=3, virsraksts="Cilvēka jauda",
             teksts="Skolēns (55 kg) uzskrien pa kāpnēm 6,0 m augstumā "
                    "8,0 s laikā. g = 9,81 m/s².\n"
                    "Aprēķini viņa attīstīto jaudu!",
             dots=["m = 55 kg", "h = 6,0 m", "t = 8,0 s"],
             jaaprekina=["P = ?"],
             formulas=["A = m·g·h", "P = A / t"],
             aprekins=["1)  A = 55 · 9,81 · 6,0 = 3237 J",
                       "2)  P = 3237 : 8,0",
                       "3)  P = 4,0·10² W"],
             atbilde="P ≈ 4,0·10² W",
             piezime="Cilvēks īslaicīgi var attīstīt ~400 W, ilgstoši — "
                     "tikai ~100 W."),
        dict(nr=4, virsraksts="Enerģija kilovatstundās",
             teksts="Sildītāja jauda ir 1,8 kW, tas strādā 3,0 h.\n"
                    "Aprēķini patērēto enerģiju kilovatstundās un džoulos!",
             dots=["P = 1,8 kW", "t = 3,0 h"],
             jaaprekina=["A = ?  (kWh)", "A = ?  (J)"],
             formulas=["A = P · t", "1 kWh = 3,6·10⁶ J"],
             aprekins=["1)  A = 1,8 kW · 3,0 h = 5,4 kWh",
                       "2)  A = 5,4 · 3,6·10⁶",
                       "3)  A = 1,9·10⁷ J"],
             atbilde="A = 5,4 kWh = 1,9·10⁷ J",
             piezime="Elektrības rēķinā maksā par kilovatstundām, nevis "
                     "džouliem."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "A = F·s; darbs tiek veikts tikai tad, ja ķermenis pārvietojas.",
            "P = A/t; jauda rāda, cik ātri darbs tiek veikts.",
            "1 J = 1 N·m; 1 W = 1 J/s; 1 kWh = 3,6·10⁶ J.",
            "Ceļot ķermeni, A = m·g·h.",
        ],
        majasdarbs=[
            "F = 400 N, s = 25 m. Aprēķini darbu.",
            "m = 80 kg paceļ 4 m 5 s laikā. Aprēķini P.",
            "P = 2,2 kW, t = 45 min. Aprēķini enerģiju kWh un J.",
        ],
        pasvertejums=["Protu skaidrot darbu", "Protu lietot A = F·s",
                      "Protu lietot P = A/t",
                      "Protu pārvērst kWh un J"],
        nakama="Nākamā stunda: kinētiskā un potenciālā enerģija."),
),

dict(
    nr="15.2", virsraksts="Kinētiskā un potenciālā enerģija",
    jautajums="Kur enerģija “uzkrājas”?",
    apaksraksts="Ek = mυ²/2 · Ep = mgh · Enerģijas veidi",
    merkis="Iemācīties aprēķināt kinētisko un potenciālo enerģiju un "
           "salīdzināt tās konkrētās situācijās.",
    protu=["atšķirt kinētisko un potenciālo enerģiju;",
           "lietot Ek = mυ²/2;",
           "lietot Ep = mgh;",
           "salīdzināt enerģijas veidus situācijā."],
    atkartojums="15.1. stundā: darbs maina enerģiju. Šodien noskaidrosim, "
                "kādos veidos enerģija ķermenī uzkrājas.",
    uzdevumu_apraksts="Kinētiskā un potenciālā enerģija",
    teorija=[
        ("Divi mehāniskās enerģijas veidi", [
            ("divi",
             ("KINĒTISKĀ ENERĢIJA", BLUE,
              ["Kustības enerģija.",
               "Ek = m·υ² / 2",
               "Aug ar ātruma KVADRĀTU!",
               "Divreiz ātrāk → četrreiz vairāk enerģijas."]),
             ("POTENCIĀLĀ ENERĢIJA", GREEN,
              ["Stāvokļa enerģija (augstumā).",
               "Ep = m·g·h",
               "Aug lineāri ar augstumu.",
               "Atkarīga no izvēlētā nulles līmeņa."])),
            ("panelis", "KĀPĒC ĀTRUMS IR TIK SVARĪGS",
             ["Ek ~ υ²: pie 100 km/h automašīnai ir četras reizes vairāk "
              "kinētiskās enerģijas nekā pie 50 km/h. Tieši šī enerģija "
              "sadursmē pārvēršas deformācijā.",
              "Tas ir tas pats iemesls, kāpēc bremzēšanas ceļš aug ar ātruma "
              "kvadrātu (7.8. stunda)."], RED),
        ]),
        ("Enerģijas veidi dabā un tehnikā", [
            ("tabula",
             ["Enerģijas veids", "Piemērs", "Kur pārvēršas"],
             [["Mehāniskā (Ek, Ep)", "krītošs ūdens", "HES turbīnā"],
              ["Iekšējā (siltuma)", "sadedzināta malka", "apkurē"],
              ["Ķīmiskā", "degviela, pārtika", "dzinējā, organismā"],
              ["Elektriskā", "strāva vados", "ierīcēs"],
              ["Kodolenerģija", "urāns reaktorā", "AES"],
              ["Starojuma", "Saules gaisma", "saules panelī"]],
             [3.63, 4.10, 4.50]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Automašīnas kinētiskā enerģija",
             teksts="Automašīnas masa ir 1200 kg, ātrums 72 km/h.\n"
                    "Aprēķini kinētisko enerģiju!",
             dots=["m = 1200 kg", "υ = 72 km/h"],
             jaaprekina=["Ek = ?"],
             formulas=["Ek = m·υ² / 2"],
             aprekins=["1)  υ = 72 : 3,6 = 20 m/s",
                       "2)  υ² = 400 m²/s²",
                       "3)  Ek = 1200 · 400 : 2 = 2,4·10⁵ J"],
             atbilde="Ek = 2,4·10⁵ J = 240 kJ",
             piezime="Vienmēr vispirms pārvērs km/h uz m/s, tikai tad kāp "
                     "kvadrātā."),
        dict(nr=2, virsraksts="Ātruma dubultošana",
             teksts="Tā pati automašīna brauc ar 144 km/h.\n"
                    "Cik reižu palielinās kinētiskā enerģija salīdzinājumā ar "
                    "72 km/h?",
             dots=["υ₁ = 72 km/h", "υ₂ = 144 km/h"],
             jaaprekina=["n = ?"],
             formulas=["Ek ~ υ²", "n = (υ₂/υ₁)²"],
             aprekins=["1)  υ₂ / υ₁ = 144 : 72 = 2",
                       "2)  n = 2² = 4"],
             atbilde="n = 4 reizes",
             piezime="Tāpēc sadursme pie 144 km/h ir četras reizes "
                     "postošāka."),
        dict(nr=3, virsraksts="Potenciālā enerģija",
             teksts="Ūdens tvertne (2,0 t) atrodas 15 m augstumā. "
                    "g = 9,81 m/s².\nAprēķini potenciālo enerģiju!",
             dots=["m = 2,0·10³ kg", "h = 15 m", "g = 9,81 m/s²"],
             jaaprekina=["Ep = ?"],
             formulas=["Ep = m · g · h"],
             aprekins=["1)  Ep = 2,0·10³ · 9,81 · 15",
                       "2)  Ep = 2,9·10⁵ J"],
             atbilde="Ep ≈ 2,9·10⁵ J = 294 kJ",
             piezime="Tieši šo enerģiju izmanto ūdenstorņi un HES."),
        dict(nr=4, virsraksts="Enerģija krītot",
             teksts="Ķermenis (5,0 kg) nokrīt no 20 m augstuma. "
                    "g = 9,81 m/s²; gaisa pretestību neņem vērā.\n"
                    "Aprēķini Ep sākumā un ātrumu tieši pirms zemes!",
             dots=["m = 5,0 kg", "h = 20 m"],
             jaaprekina=["Ep = ?", "υ = ?"],
             formulas=["Ep = mgh", "Ep = Ek = mυ²/2", "υ = √(2gh)"],
             aprekins=["1)  Ep = 5,0 · 9,81 · 20 = 981 J",
                       "2)  υ = √(2 · 9,81 · 20) = √392",
                       "3)  υ = 19,8 m/s"],
             atbilde="Ep ≈ 9,8·10² J ;   υ ≈ 20 m/s",
             piezime="Visa potenciālā enerģija pārvērtusies kinētiskajā — "
                     "par to nākamajā stundā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ek = mυ²/2 — kustības enerģija, aug ar ātruma kvadrātu.",
            "Ep = mgh — stāvokļa enerģija, aug lineāri ar augstumu.",
            "Divreiz lielāks ātrums nozīmē četrreiz lielāku Ek.",
            "Enerģijas veidi: mehāniskā, iekšējā, ķīmiskā, elektriskā, "
            "kodolenerģija, starojuma.",
        ],
        majasdarbs=[
            "m = 800 kg, υ = 54 km/h. Aprēķini Ek.",
            "m = 60 kg, h = 8 m. Aprēķini Ep.",
            "Cik reižu Ek atšķiras pie 30 km/h un 90 km/h?",
        ],
        pasvertejums=["Protu atšķirt Ek un Ep",
                      "Protu lietot Ek = mυ²/2",
                      "Protu lietot Ep = mgh",
                      "Protu pamatot ātruma nozīmi"],
        nakama="Nākamā stunda: enerģijas nezūdamība."),
),

dict(
    nr="15.3", virsraksts="Enerģijas nezūdamība",
    jautajums="Kur enerģija pazūd?",
    apaksraksts="Nezūdamības likums · Pārvērtību virknes · Enerģijas zudumi",
    merkis="Iemācīties ar enerģijas nezūdamības likumu skaidrot pārvērtību "
           "virknes un analizēt enerģijas zudumus.",
    protu=["formulēt enerģijas nezūdamības likumu;",
           "veidot enerģijas pārvērtību virknes;",
           "aprēķināt ātrumu vai augstumu ar nezūdamības likumu;",
           "skaidrot, kur enerģija “pazūd”."],
    atkartojums="15.2. stundā rēķinājām Ek un Ep atsevišķi. Šodien "
                "noskaidrosim, kā tās pārvēršas viena otrā.",
    uzdevumu_apraksts="Enerģijas pārvērtības un nezūdamība",
    teorija=[
        ("Nezūdamības likums", [
            ("formula", "ENERĢIJAS NEZŪDAMĪBAS LIKUMS",
             "Ep + Ek = const        m·g·h = m·υ² / 2",
             "Enerģija nerodas no nekā un nepazūd — tā tikai pārvēršas no "
             "viena veida citā. Slēgtā sistēmā kopējā enerģija nemainās.",
             GOLD),
            ("panelis", "PĀRVĒRTĪBU VIRKNES",
             ["Saule → fotosintēze → augi → pārtika → muskuļu darbs.",
              "Ūdens augstumā (Ep) → krišana (Ek) → turbīna → ģenerators → "
              "elektrība → gaisma spuldzē → siltums.",
              "Katrā pārejā daļa enerģijas pārvēršas siltumā — tā nepazūd, "
              "bet vairs nav izmantojama."], NAVY),
        ]),
        ("Kur enerģija “pazūd”", [
            ("kartitas", [
                ("BERZE", RED,
                 ["Mehāniskā enerģija → siltums.",
                  "Bremzes sakarst.",
                  "Detaļas nolietojas."]),
                ("GAISA PRETESTĪBA", GOLD,
                 ["Enerģija → gaisa kustība un siltums.",
                  "Jo lielāks ātrums, jo lielāki zudumi.",
                  "Tāpēc auto formu veido aerodinamisku."]),
                ("SILTUMA IZKLIEDE", BLUE,
                 ["Vadi sakarst, dzinējs sakarst.",
                  "Siltums izkliedējas apkārtējā vidē.",
                  "To vairs nevar savākt un izmantot."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātrums pēc krišanas",
             teksts="Ķermenis nokrīt no 45 m augstuma. g = 9,81 m/s²; gaisa "
                    "pretestību neņem vērā.\n"
                    "Aprēķini ātrumu pie zemes, izmantojot enerģijas "
                    "nezūdamību!",
             dots=["h = 45 m", "g = 9,81 m/s²", "υ₀ = 0"],
             jaaprekina=["υ = ?"],
             formulas=["m·g·h = m·υ²/2", "υ = √(2·g·h)"],
             aprekins=["1)  Masa saīsinās: g·h = υ²/2",
                       "2)  υ² = 2 · 9,81 · 45 = 883",
                       "3)  υ = √883 = 29,7 m/s"],
             atbilde="υ ≈ 30 m/s",
             piezime="Masa neietekmē rezultātu — tā saīsinās, tāpat kā brīvās "
                     "krišanas uzdevumos."),
        dict(nr=2, virsraksts="Augstums pēc uzmešanas",
             teksts="Bumbu met vertikāli augšup ar ātrumu 15 m/s.\n"
                    "Cik augstu tā pacelsies? (g = 9,81 m/s²)",
             dots=["υ = 15 m/s", "g = 9,81 m/s²"],
             jaaprekina=["h = ?"],
             formulas=["m·υ²/2 = m·g·h", "h = υ² / (2g)"],
             aprekins=["1)  υ² = 225 m²/s²",
                       "2)  2g = 19,62 m/s²",
                       "3)  h = 225 : 19,62 = 11,5 m"],
             atbilde="h ≈ 11 m",
             piezime="Augstākajā punktā visa kinētiskā enerģija ir "
                     "pārvērtusies potenciālajā."),
        dict(nr=3, virsraksts="Enerģija ragaviņām",
             teksts="Ragaviņas ar bērnu (40 kg) noslīd no 8,0 m augsta kalna. "
                    "Pie pakājes to ātrums ir 10 m/s.\n"
                    "Aprēķini Ep sākumā, Ek beigās un enerģijas zudumus!",
             dots=["m = 40 kg ;  h = 8,0 m", "υ = 10 m/s"],
             jaaprekina=["Ep = ?", "Ek = ?", "ΔE = ?"],
             formulas=["Ep = mgh", "Ek = mυ²/2", "ΔE = Ep − Ek"],
             aprekins=["1)  Ep = 40 · 9,81 · 8,0 = 3139 J",
                       "2)  Ek = 40 · 100 : 2 = 2000 J",
                       "3)  ΔE = 3139 − 2000 = 1139 J"],
             atbilde="Ep ≈ 3,1 kJ ;  Ek = 2,0 kJ ;  zudumi ≈ 1,1 kJ",
             piezime="Zudumi aizgāja berzē un gaisa pretestībā — pārvērtās "
                     "siltumā."),
        dict(nr=4, virsraksts="Hidroelektrostacija",
             teksts="HES katru sekundi caur turbīnu izlaiž 500 m³ ūdens no "
                    "20 m augstuma. Ūdens blīvums 1000 kg/m³.\n"
                    "Aprēķini teorētisko jaudu!",
             dots=["V = 500 m³/s ;  h = 20 m", "ρ = 1000 kg/m³"],
             jaaprekina=["P = ?"],
             formulas=["m = ρ·V", "Ep = m·g·h", "P = Ep / t"],
             aprekins=["1)  m = 1000 · 500 = 5,0·10⁵ kg sekundē",
                       "2)  Ep = 5,0·10⁵ · 9,81 · 20 = 9,81·10⁷ J",
                       "3)  P = 9,81·10⁷ W ≈ 98 MW"],
             atbilde="P ≈ 9,8·10⁷ W = 98 MW",
             piezime="Reālā jauda ir mazāka — par lietderības koeficientu "
                     "nākamajā stundā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Enerģija nerodas un nepazūd — tā tikai pārvēršas.",
            "mgh = mυ²/2; masa šajās sakarībās bieži saīsinās.",
            "υ = √(2gh) un h = υ²/(2g).",
            "Zudumi aiziet berzē, gaisa pretestībā un siltumā.",
        ],
        majasdarbs=[
            "h = 20 m. Aprēķini ātrumu pie zemes.",
            "υ = 20 m/s augšup. Cik augstu pacelsies?",
            "Uzraksti enerģijas pārvērtību virkni velosipēdistam, kas "
            "nobrauc no kalna.",
        ],
        pasvertejums=["Protu formulēt nezūdamības likumu",
                      "Protu veidot pārvērtību virknes",
                      "Protu aprēķināt υ un h",
                      "Protu skaidrot zudumus"],
        nakama="Nākamā stunda: lietderības koeficients."),
),

dict(
    nr="15.4", virsraksts="Lietderības koeficients",
    jautajums="Cik efektīva ir ierīce?",
    apaksraksts="η = Al/Ap · Enerģijas zudumi · Ierīču salīdzināšana",
    merkis="Iemācīties aprēķināt lietderības koeficientu un salīdzināt ierīču "
           "efektivitāti.",
    protu=["skaidrot, kas ir lietderības koeficients;",
           "lietot η = Al/Ap · 100 %;",
           "aprēķināt lietderīgo vai patērēto enerģiju;",
           "salīdzināt ierīces un pamatot izvēli."],
    atkartojums="15.3. stundā redzējām, ka daļa enerģijas pārvēršas siltumā. "
                "Lietderības koeficients rāda, cik liela daļa tomēr paliek "
                "noderīga.",
    uzdevumu_apraksts="Lietderības koeficients un enerģijas zudumi",
    teorija=[
        ("Lietderības koeficients", [
            ("formula", "LIETDERĪBAS KOEFICIENTS",
             "η = A(lietderīgais) / A(patērētais) · 100 %",
             "η vienmēr ir mazāks par 100 % — daļa enerģijas neizbēgami "
             "pārvēršas siltumā. Ja kāds sola η > 100 %, tas ir "
             "neiespējami.", GOLD),
            ("tabula",
             ["Ierīce", "η", "Kur aiziet zudumi"],
             [["Elektromotors", "85–95 %", "siltums vados un gultņos"],
              ["LED spuldze", "~40 %", "siltums"],
              ["Kvēlspuldze", "~5 %", "siltums (95 %!)"],
              ["Iekšdedzes dzinējs", "25–35 %", "izplūdes gāzes, dzesēšana"],
              ["Saules panelis", "15–22 %", "atstarošana, siltums"],
              ["HES turbīna", "~90 %", "berze, ūdens plūsma"]],
             [3.63, 2.60, 6.00]),
        ]),
        ("Kā to izmanto", [
            ("panelis", "KĀPĒC KVĒLSPULDZES AIZSTĀJ AR LED",
             ["Kvēlspuldze 95 % enerģijas pārvērš siltumā un tikai 5 % — "
              "gaismā. LED spuldze dod tikpat daudz gaismas, patērējot "
              "~8 reizes mazāk enerģijas.",
              "60 W kvēlspuldzi aizstāj 8 W LED spuldze — gaisma tāda pati, "
              "rēķins mazāks."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Celtņa lietderība",
             teksts="Celtnis patērē 8,0·10⁴ J enerģijas, lai paceltu kravu, "
                    "kuras potenciālā enerģija palielinās par 6,0·10⁴ J.\n"
                    "Aprēķini lietderības koeficientu!",
             dots=["A(p) = 8,0·10⁴ J", "A(l) = 6,0·10⁴ J"],
             jaaprekina=["η = ?"],
             formulas=["η = A(l) / A(p) · 100 %"],
             aprekins=["1)  η = 6,0·10⁴ : 8,0·10⁴",
                       "2)  η = 0,75",
                       "3)  η = 75 %"],
             atbilde="η = 75 %",
             piezime="Ceturtdaļa enerģijas aizgāja berzē un siltumā."),
        dict(nr=2, virsraksts="Patērētā enerģija",
             teksts="Ierīces lietderības koeficients ir 40 %, lietderīgais "
                    "darbs 1,2·10⁵ J.\nAprēķini patērēto enerģiju!",
             dots=["η = 40 %", "A(l) = 1,2·10⁵ J"],
             jaaprekina=["A(p) = ?"],
             formulas=["η = A(l)/A(p)", "A(p) = A(l) / η"],
             aprekins=["1)  η = 0,40",
                       "2)  A(p) = 1,2·10⁵ : 0,40",
                       "3)  A(p) = 3,0·10⁵ J"],
             atbilde="A(p) = 3,0·10⁵ J",
             piezime="Patērētā enerģija vienmēr lielāka par lietderīgo."),
        dict(nr=3, virsraksts="Spuldžu salīdzinājums",
             teksts="Kvēlspuldze (60 W, η = 5 %) un LED spuldze (8 W, "
                    "η = 40 %).\n"
                    "Aprēķini abu gaismas jaudu un salīdzini!",
             dots=["P₁ = 60 W ;  η₁ = 5 %", "P₂ = 8 W ;  η₂ = 40 %"],
             jaaprekina=["P(g₁) = ?", "P(g₂) = ?"],
             formulas=["P(gaismas) = η · P"],
             aprekins=["1)  P(g₁) = 0,05 · 60 = 3,0 W",
                       "2)  P(g₂) = 0,40 · 8 = 3,2 W",
                       "3)  Gaisma līdzīga, patēriņš 7,5× atšķirīgs"],
             atbilde="P(g₁) = 3,0 W ;  P(g₂) = 3,2 W — LED labāka",
             piezime="LED dod pat nedaudz vairāk gaismas, patērējot "
                     "7,5 reizes mazāk."),
        dict(nr=4, virsraksts="Automašīnas dzinējs",
             teksts="Automašīna patērē degvielu ar enerģiju 4,0·10⁷ J. "
                    "Dzinēja lietderības koeficients 30 %.\n"
                    "Cik enerģijas pārvēršas noderīgā darbā un cik — "
                    "siltumā?",
             dots=["A(p) = 4,0·10⁷ J", "η = 30 %"],
             jaaprekina=["A(l) = ?", "A(zud) = ?"],
             formulas=["A(l) = η · A(p)", "A(zud) = A(p) − A(l)"],
             aprekins=["1)  A(l) = 0,30 · 4,0·10⁷ = 1,2·10⁷ J",
                       "2)  A(zud) = 4,0·10⁷ − 1,2·10⁷",
                       "3)  A(zud) = 2,8·10⁷ J"],
             atbilde="A(l) = 1,2·10⁷ J ;   zudumi 2,8·10⁷ J (70 %)",
             piezime="Tāpēc elektroauto ir efektīvāki — to motoru η ir "
                     "~90 %."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "η = A(l)/A(p) · 100 %; vienmēr mazāks par 100 %.",
            "Zudumi galvenokārt aiziet siltumā.",
            "LED spuldze ~8 reizes efektīvāka par kvēlspuldzi.",
            "Iekšdedzes dzinēja η ~30 %, elektromotora ~90 %.",
        ],
        majasdarbs=[
            "A(p) = 5,0·10⁴ J, A(l) = 3,5·10⁴ J. Aprēķini η.",
            "η = 25 %, A(l) = 8,0·10⁴ J. Aprēķini A(p).",
            "Salīdzini 100 W kvēlspuldzi (η = 5 %) un 12 W LED (η = 40 %).",
        ],
        pasvertejums=["Protu skaidrot lietderību",
                      "Protu lietot η = Al/Ap",
                      "Protu aprēķināt zudumus",
                      "Protu salīdzināt ierīces"],
        nakama="Nākamā stunda: kurināmais un siltums."),
),

dict(
    nr="15.5", virsraksts="Kurināmais un siltums",
    jautajums="Cik enerģijas dod malka un gāze?",
    apaksraksts="Īpatnējais sadegšanas siltums · Q = q·m · Kurināmā "
                "salīdzināšana",
    merkis="Iemācīties aprēķināt degšanā iegūto siltuma daudzumu un salīdzināt "
           "kurināmā veidus.",
    protu=["lietot Q = q·m;",
           "salīdzināt kurināmā veidus pēc q;",
           "aprēķināt nepieciešamo kurināmā daudzumu;",
           "izvērtēt kurināmā izvēli apkurei."],
    atkartojums="15.4. stundā aprēķinājām lietderību. Tagad noskaidrosim, cik "
                "enerģijas vispār ir kurināmajā.",
    uzdevumu_apraksts="Sadegšanas siltums un kurināmā daudzums",
    teorija=[
        ("Īpatnējais sadegšanas siltums", [
            ("formula", "SILTUMA DAUDZUMS DEGŠANĀ",
             "Q = q · m        [q] = J/kg",
             "q — īpatnējais sadegšanas siltums: cik enerģijas atbrīvojas, "
             "pilnībā sadegot 1 kg kurināmā.", GOLD),
            ("tabula",
             ["Kurināmais", "q, MJ/kg", "Piezīmes"],
             [["Malka (sausa)", "10–15", "atjaunojams, CO₂ neitrāls"],
              ["Kūdra", "~15", "vietējais resurss"],
              ["Akmeņogles", "~29", "daudz izmešu"],
              ["Dabasgāze", "~50", "mazāk CO₂ nekā oglēm"],
              ["Benzīns", "~46", "transportam"],
              ["Ūdeņradis", "~120", "nav CO₂, bet grūti uzglabāt"]],
             [3.63, 2.60, 6.00]),
        ]),
        ("Kurināmā izvēle", [
            ("divi",
             ("KO VĒRTĒ", BLUE,
              ["Enerģijas daudzums uz kg (q).",
               "Cena par kWh.",
               "Izmeši un ietekme uz vidi.",
               "Pieejamība un uzglabāšana."]),
             ("LATVIJAS KONTEKSTS", GREEN,
              ["Malka un šķelda — vietējais resurss.",
               "Dabasgāze — importēta.",
               "Siltumsūkņi izmanto vides siltumu.",
               "Biomasa uzskatāma par CO₂ neitrālu."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Malkas sadegšana",
             teksts="Sadedzina 15 kg sausas malkas, q = 1,2·10⁷ J/kg.\n"
                    "Aprēķini atbrīvoto siltuma daudzumu!",
             dots=["m = 15 kg", "q = 1,2·10⁷ J/kg"],
             jaaprekina=["Q = ?"],
             formulas=["Q = q · m"],
             aprekins=["1)  Q = 1,2·10⁷ · 15",
                       "2)  Q = 1,8·10⁸ J"],
             atbilde="Q = 1,8·10⁸ J = 180 MJ",
             piezime="180 MJ = 50 kWh — tas ir aptuveni divu dienu "
                     "elektrības patēriņš mājsaimniecībā."),
        dict(nr=2, virsraksts="Cik gāzes vajag?",
             teksts="Jāiegūst 4,0·10⁸ J siltuma. Dabasgāzes "
                    "q = 5,0·10⁷ J/kg, katla lietderība 90 %.\n"
                    "Cik kilogramu gāzes vajag?",
             dots=["Q = 4,0·10⁸ J", "q = 5,0·10⁷ J/kg", "η = 90 %"],
             jaaprekina=["m = ?"],
             formulas=["Q = η · q · m", "m = Q / (η·q)"],
             aprekins=["1)  η·q = 0,90 · 5,0·10⁷ = 4,5·10⁷ J/kg",
                       "2)  m = 4,0·10⁸ : 4,5·10⁷",
                       "3)  m = 8,9 kg"],
             atbilde="m ≈ 8,9 kg",
             piezime="Bez lietderības ievērošanas iznāktu 8,0 kg — par maz."),
        dict(nr=3, virsraksts="Kurināmā salīdzinājums",
             teksts="Malkas q = 1,2·10⁷ J/kg, dabasgāzes q = 5,0·10⁷ J/kg.\n"
                    "Cik reižu vairāk malkas vajag, lai iegūtu tikpat "
                    "enerģijas?",
             dots=["q₁ = 1,2·10⁷ J/kg", "q₂ = 5,0·10⁷ J/kg"],
             jaaprekina=["n = ?"],
             formulas=["m = Q / q", "n = q₂ / q₁"],
             aprekins=["1)  n = 5,0·10⁷ : 1,2·10⁷",
                       "2)  n = 4,2"],
             atbilde="n ≈ 4,2 reizes vairāk malkas pēc masas",
             piezime="Malka arī aizņem daudz vairāk vietas — tāpēc vajag "
                     "malkas šķūni."),
        dict(nr=4, virsraksts="Mājas apkure",
             teksts="Mājas apkurei ziemā vajag 3,6·10¹⁰ J. Šķeldas "
                    "q = 1,0·10⁷ J/kg, katla η = 85 %.\n"
                    "Cik tonnu šķeldas vajag?",
             dots=["Q = 3,6·10¹⁰ J", "q = 1,0·10⁷ J/kg", "η = 85 %"],
             jaaprekina=["m = ?  (t)"],
             formulas=["m = Q / (η · q)"],
             aprekins=["1)  η·q = 0,85 · 1,0·10⁷ = 8,5·10⁶ J/kg",
                       "2)  m = 3,6·10¹⁰ : 8,5·10⁶",
                       "3)  m = 4,2·10³ kg = 4,2 t"],
             atbilde="m ≈ 4,2 t",
             piezime="Tāpēc siltumizolācija ir izdevīga — tā tieši samazina "
                     "vajadzīgo kurināmā daudzumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Q = q·m; q — īpatnējais sadegšanas siltums J/kg.",
            "Dabasgāzei q ~50 MJ/kg, malkai ~12 MJ/kg.",
            "Ar lietderību: Q(noderīgais) = η·q·m.",
            "Kurināmo izvēlas pēc q, cenas, izmešiem un pieejamības.",
        ],
        majasdarbs=[
            "m = 25 kg malkas (q = 1,2·10⁷). Aprēķini Q.",
            "Vajag 2,0·10⁸ J, q = 4,6·10⁷ J/kg, η = 80 %. Cik kg?",
            "Salīdzini akmeņogles (29 MJ/kg) un malku (12 MJ/kg).",
        ],
        pasvertejums=["Protu lietot Q = q·m",
                      "Protu ievērot lietderību",
                      "Protu salīdzināt kurināmo",
                      "Protu aprēķināt vajadzīgo daudzumu"],
        nakama="Nākamā stunda: elektroenerģija mājsaimniecībā."),
),

dict(
    nr="15.6", virsraksts="Elektroenerģija mājsaimniecībā",
    jautajums="Cik maksā elektrība?",
    apaksraksts="P = IU · E = Pt · Patēriņš un izmaksas",
    merkis="Iemācīties aprēķināt elektroierīču patērēto enerģiju un izmaksas "
           "un salīdzināt energoefektivitāti.",
    protu=["lietot P = IU un E = Pt;",
           "aprēķināt patēriņu kilovatstundās;",
           "aprēķināt izmaksas pēc tarifa;",
           "salīdzināt ierīču energoefektivitāti."],
    atkartojums="5.5. stundā mācījāmies par vadītājiem un R = ρl/S. Šodien "
                "rēķināsim, cik elektroenerģijas patērē mājas ierīces.",
    uzdevumu_apraksts="Jauda, patēriņš un izmaksas",
    teorija=[
        ("Elektriskā jauda un patēriņš", [
            ("formula", "JAUDA UN ENERĢIJA",
             "P = I · U        E = P · t        I = U / R",
             "P — jauda [W], I — strāvas stiprums [A], U — spriegums [V]. "
             "Latvijā tīkla spriegums ir 230 V.", GOLD),
            ("tabula",
             ["Ierīce", "Jauda", "Patēriņš dienā", "Piezīme"],
             [["LED spuldze", "8 W", "0,04 kWh (5 h)", "ļoti ekonomiska"],
              ["Ledusskapis", "100 W", "~0,8 kWh", "strādā ar pārtraukumiem"],
              ["Televizors", "120 W", "0,48 kWh (4 h)", "vidēji"],
              ["Tējkanna", "2000 W", "0,17 kWh (5 min)", "liela jauda, īss "
               "laiks"],
              ["Elektriskā plīts", "3000 W", "1,5 kWh (30 min)", "lielākais "
               "patērētājs"]],
             [3.13, 2.10, 3.30, 3.70]),
        ]),
        ("Izmaksas", [
            ("formula", "IZMAKSU APRĒĶINS",
             "E(kWh) = P(kW) · t(h)        Cena = E · tarifs",
             "Tarifs Latvijā ~0,20 EUR/kWh (ar piegādi). Rēķinā maksā par "
             "kilovatstundām.", GOLD),
            ("panelis", "KĀ SAMAZINĀT RĒĶINU",
             ["Nomainīt kvēlspuldzes pret LED  ·  izslēgt ierīces no gaidīšanas "
              "režīma  ·  izvēlēties A klases ierīces  ·  vārīt ūdeni tieši "
              "tik, cik vajag  ·  neatstāt ledusskapja durvis vaļā."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ierīces jauda",
             teksts="Caur ierīci plūst 4,5 A strāva pie 230 V sprieguma.\n"
                    "Aprēķini ierīces jaudu!",
             dots=["I = 4,5 A", "U = 230 V"],
             jaaprekina=["P = ?"],
             formulas=["P = I · U"],
             aprekins=["1)  P = 4,5 A · 230 V",
                       "2)  P = 1035 W ≈ 1,0 kW"],
             atbilde="P ≈ 1,0·10³ W = 1,0 kW",
             piezime="Tāda jauda ir, piemēram, matu fēnam."),
        dict(nr=2, virsraksts="Tējkannas izmaksas",
             teksts="Tējkanna (2,0 kW) darbojas 8 minūtes dienā. Tarifs "
                    "0,20 EUR/kWh.\n"
                    "Aprēķini enerģijas patēriņu un izmaksas mēnesī "
                    "(30 dienas)!",
             dots=["P = 2,0 kW", "t = 8 min dienā", "tarifs 0,20 EUR/kWh"],
             jaaprekina=["E = ?", "Cena = ?"],
             formulas=["E = P · t", "Cena = E · tarifs"],
             aprekins=["1)  t = 8 : 60 = 0,133 h dienā",
                       "2)  E(diena) = 2,0 · 0,133 = 0,267 kWh",
                       "3)  E(mēnesis) = 0,267 · 30 = 8,0 kWh",
                       "4)  Cena = 8,0 · 0,20 = 1,60 EUR"],
             atbilde="E = 8,0 kWh ;   izmaksas 1,60 EUR mēnesī",
             piezime="Liela jauda, bet īss laiks — tāpēc patēriņš nav "
                     "milzīgs."),
        dict(nr=3, virsraksts="Spuldžu nomaiņa",
             teksts="Mājā ir 10 kvēlspuldzes pa 60 W, tās deg 5 h dienā. Tās "
                    "nomaina pret 8 W LED. Tarifs 0,20 EUR/kWh.\n"
                    "Cik ietaupa gadā?",
             dots=["N = 10 ;  P₁ = 60 W ;  P₂ = 8 W", "t = 5 h dienā"],
             jaaprekina=["ΔE = ?", "Ietaupījums = ?"],
             formulas=["E = N · P · t", "Cena = E · tarifs"],
             aprekins=["1)  ΔP = 10 · (60 − 8) = 520 W = 0,52 kW",
                       "2)  ΔE = 0,52 · 5 · 365 = 949 kWh",
                       "3)  Cena = 949 · 0,20 = 190 EUR"],
             atbilde="ΔE ≈ 9,5·10² kWh ;   ietaupījums ~190 EUR gadā",
             piezime="Spuldzes atmaksājas dažos mēnešos."),
        dict(nr=4, virsraksts="Drošinātāja pārbaude",
             teksts="Vienā līnijā (230 V, drošinātājs 16 A) vienlaikus "
                    "ieslēdz plīti (3000 W) un tējkannu (2000 W).\n"
                    "Aprēķini kopējo strāvu un nosaki, vai drošinātājs "
                    "izslēgsies!",
             dots=["P₁ = 3000 W ;  P₂ = 2000 W", "U = 230 V ;  I(max) = 16 A"],
             jaaprekina=["I = ?"],
             formulas=["P = I·U", "I = P / U"],
             aprekins=["1)  P = 3000 + 2000 = 5000 W",
                       "2)  I = 5000 : 230",
                       "3)  I = 21,7 A > 16 A"],
             atbilde="I ≈ 22 A — drošinātājs izslēgsies",
             piezime="Tāpēc lielas jaudas ierīces nedrīkst slēgt vienā "
                     "līnijā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "P = I·U; Latvijā U = 230 V.",
            "E = P·t; sadzīvē enerģiju mēra kilovatstundās.",
            "Izmaksas = E(kWh) · tarifs.",
            "Drošinātājs izslēdzas, ja kopējā strāva pārsniedz tā vērtību.",
        ],
        majasdarbs=[
            "I = 6 A, U = 230 V. Aprēķini jaudu.",
            "P = 1,5 kW, t = 2 h dienā. Aprēķini patēriņu un cenu mēnesī.",
            "Vai 16 A drošinātājs iztur 2500 W un 1500 W ierīces kopā?",
        ],
        pasvertejums=["Protu lietot P = IU", "Protu aprēķināt kWh",
                      "Protu aprēķināt izmaksas",
                      "Protu pārbaudīt drošinātāju"],
        nakama="Nākamā stunda: elektrodrošība."),
),

dict(
    nr="15.7", virsraksts="Elektrodrošība",
    jautajums="Kā pasargā drošinātājs un zemējums?",
    apaksraksts="Pārslodze · Īsslēgums · Zemējums · Pirmā palīdzība",
    merkis="Iemācīties skaidrot pārslodzi un īsslēgumu un pamatot rīcības "
           "soļus elektrotraumas gadījumā.",
    protu=["skaidrot pārslodzi un īsslēgumu;",
           "pamatot drošinātāja un zemējuma nozīmi;",
           "aprēķināt strāvu un pārbaudīt drošību;",
           "nosaukt rīcību elektrotraumas gadījumā."],
    atkartojums="15.6. stundā rēķinājām strāvu I = P/U. Šodien noskaidrosim, "
                "kas notiek, ja strāva kļūst par lielu.",
    uzdevumu_apraksts="Strāvas stiprums un drošība",
    teorija=[
        ("Kas apdraud", [
            ("divi",
             ("PĀRSLODZE", GOLD,
              ["Vienā līnijā ieslēgts par daudz ierīču.",
               "Strāva pārsniedz vada izturību.",
               "Vadi sakarst — var izcelties ugunsgrēks.",
               "Drošinātājs pārtrauc ķēdi."]),
             ("ĪSSLĒGUMS", RED,
              ["Fāzes un nulles vadi saskaras.",
               "Pretestība gandrīz nulle → milzīga strāva.",
               "Momentāns sakaršanas un dzirksteļu risks.",
               "Automātslēdzis nostrādā tūlītēji."])),
            ("panelis", "AIZSARDZĪBAS IERĪCES",
             ["Drošinātājs / automātslēdzis pārtrauc ķēdi, ja strāva "
              "pārsniedz nominālo  ·  zemējums novada bīstamo spriegumu "
              "zemē  ·  noplūdes strāvas relejs (RCD) atslēdz ķēdi, ja "
              "strāva noplūst caur cilvēku."], NAVY),
        ]),
        ("Strāvas ietekme un pirmā palīdzība", [
            ("tabula",
             ["Strāva caur cilvēku", "Ietekme"],
             [["līdz 1 mA", "gandrīz nejūt"],
              ["10–20 mA", "muskuļu krampji, grūti atrauties"],
              ["50 mA", "bīstami elpošanai"],
              ["virs 100 mA", "sirds fibrilācija, dzīvībai bīstami"]],
             [5.13, 7.10]),
            ("panelis", "RĪCĪBA ELEKTROTRAUMAS GADĪJUMĀ",
             ["1. Atslēdz strāvu (slēdzis, drošinātājs) — NEPIESKARIES "
              "cietušajam, kamēr strāva ieslēgta.",
              "2. Ja nevar atslēgt, atbīdi cietušo ar sausu koka vai "
              "plastmasas priekšmetu.  3. Zvani 113.  4. Pārbaudi elpošanu "
              "un sāc atdzīvināšanu (ABC), ja nepieciešams."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vai drošinātājs iztur?",
             teksts="Līnijā (230 V, 10 A drošinātājs) ieslēgtas ierīces ar "
                    "kopējo jaudu 2100 W.\n"
                    "Aprēķini strāvu un nosaki, vai drošinātājs iztur!",
             dots=["P = 2100 W", "U = 230 V", "I(max) = 10 A"],
             jaaprekina=["I = ?"],
             formulas=["I = P / U"],
             aprekins=["1)  I = 2100 : 230",
                       "2)  I = 9,1 A",
                       "3)  9,1 A < 10 A"],
             atbilde="I ≈ 9,1 A — drošinātājs iztur",
             piezime="Rezerve maza — vēl viena ierīce jau pārslogotu līniju."),
        dict(nr=2, virsraksts="Maksimālā jauda",
             teksts="Līnijas drošinātājs ir 16 A, spriegums 230 V.\n"
                    "Aprēķini maksimālo pieļaujamo jaudu!",
             dots=["I = 16 A", "U = 230 V"],
             jaaprekina=["P = ?"],
             formulas=["P = I · U"],
             aprekins=["1)  P = 16 · 230",
                       "2)  P = 3680 W ≈ 3,7 kW"],
             atbilde="P ≈ 3,7 kW",
             piezime="Tāpēc elektriskajai plītij (3 kW) parasti ir atsevišķa "
                     "līnija."),
        dict(nr=3, virsraksts="Strāva caur cilvēku",
             teksts="Cilvēks pieskaras 230 V spriegumam. Sausas ādas "
                    "pretestība ~10 kΩ, slapjas ~1,0 kΩ.\n"
                    "Aprēķini strāvu abos gadījumos un novērtē bīstamību!",
             dots=["U = 230 V", "R₁ = 10 kΩ ;  R₂ = 1,0 kΩ"],
             jaaprekina=["I₁ = ?", "I₂ = ?"],
             formulas=["I = U / R"],
             aprekins=["1)  I₁ = 230 : 1,0·10⁴ = 0,023 A = 23 mA",
                       "2)  I₂ = 230 : 1,0·10³ = 0,23 A = 230 mA",
                       "3)  23 mA — krampji ;  230 mA — dzīvībai bīstami"],
             atbilde="I₁ = 23 mA ;   I₂ = 230 mA — slapjumā ļoti bīstami",
             piezime="Tāpēc ar elektroierīcēm nedrīkst rīkoties ar slapjām "
                     "rokām vai vannasistabā."),
        dict(nr=4, virsraksts="Īsslēguma strāva",
             teksts="Īsslēgumā ķēdes pretestība samazinās līdz 0,50 Ω, "
                    "spriegums 230 V.\n"
                    "Aprēķini strāvu un salīdzini ar 16 A drošinātāju!",
             dots=["U = 230 V", "R = 0,50 Ω", "I(max) = 16 A"],
             jaaprekina=["I = ?", "n = ?"],
             formulas=["I = U / R", "n = I / I(max)"],
             aprekins=["1)  I = 230 : 0,50 = 460 A",
                       "2)  n = 460 : 16",
                       "3)  n = 29"],
             atbilde="I = 4,6·10² A — 29 reizes virs nominālā",
             piezime="Šāda strāva vadu sakarsētu momentāni — tāpēc "
                     "automātslēdzim jānostrādā milisekundēs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Pārslodze — par daudz ierīču; īsslēgums — pretestība tuvu nullei.",
            "Drošinātājs pārtrauc ķēdi, zemējums novada spriegumu zemē.",
            "I = U/R; slapja āda samazina pretestību ~10 reižu.",
            "Elektrotraumā vispirms atslēdz strāvu, tikai tad palīdz.",
        ],
        majasdarbs=[
            "P = 2760 W, U = 230 V. Aprēķini I un salīdzini ar 10 A.",
            "I(max) = 20 A, U = 230 V. Aprēķini maksimālo jaudu.",
            "Uzraksti četrus rīcības soļus elektrotraumas gadījumā.",
        ],
        pasvertejums=["Protu skaidrot pārslodzi un īsslēgumu",
                      "Protu pamatot drošinātāja nozīmi",
                      "Protu aprēķināt strāvu",
                      "Protu nosaukt pirmās palīdzības soļus"],
        nakama="Nākamā stunda: ģenerators, elektrodzinējs, transformators."),
),

dict(
    nr="15.8", virsraksts="Ģenerators, elektrodzinējs, transformators",
    jautajums="Kā elektrība nonāk no elektrostacijas mājā?",
    apaksraksts="Ģenerators · Elektrodzinējs · k = N₁/N₂ = U₁/U₂ · Pārvade",
    merkis="Iemācīties skaidrot ģeneratora, elektrodzinēja un transformatora "
           "darbību un pamatot augsta sprieguma izmantošanu pārvadē; "
           "sagatavoties PD9.",
    protu=["skaidrot ģeneratora un elektrodzinēja darbību;",
           "lietot k = N₁/N₂ = U₁/U₂;",
           "pamatot augsta sprieguma pārvadi;",
           "izvēlēties pareizo formulu temata uzdevumos."],
    atkartojums="Šī ir pēdējā stunda pirms PD9. Atkārtojam: A = F·s, P = A/t, "
                "Ek, Ep, η, Q = q·m, P = I·U.",
    uzdevumu_apraksts="Transformators un elektroenerģijas pārvade",
    teorija=[
        ("Trīs ierīces", [
            ("kartitas", [
                ("ĢENERATORS", BLUE,
                 ["Mehāniskā enerģija → elektriskā.",
                  "Spole griežas magnētiskajā laukā.",
                  "Elektrostacijās, dinamo, vēja turbīnās."]),
                ("ELEKTRODZINĒJS", GREEN,
                 ["Elektriskā enerģija → mehāniskā.",
                  "Strāva vadā magnētiskajā laukā rada spēku.",
                  "Ventilatori, elektroauto, sūkņi."]),
                ("TRANSFORMATORS", GOLD,
                 ["Maina maiņstrāvas spriegumu.",
                  "Divas spoles uz kopēja serdeņa.",
                  "Darbojas TIKAI ar maiņstrāvu."]),
            ]),
            ("formula", "TRANSFORMĀCIJAS KOEFICIENTS",
             "k = N₁ / N₂ = U₁ / U₂",
             "N — vijumu skaits. Ja N₂ > N₁, spriegums paaugstinās; ja "
             "N₂ < N₁ — pazeminās. Jauda (bez zudumiem) nemainās.", GOLD),
        ]),
        ("Kāpēc pārvadē augsts spriegums", [
            ("panelis", "ZUDUMI LĪNIJĀ",
             ["Pie tās pašas jaudas augstāks spriegums nozīmē mazāku strāvu "
              "(P = UI). Zudumi vados ir proporcionāli strāvas kvadrātam, "
              "tāpēc mazāka strāva nozīmē krietni mazākus zudumus.",
              "Tāpēc no elektrostacijas spriegumu paaugstina līdz 110–330 kV, "
              "bet pie mājas atkal pazemina līdz 230 V."], NAVY),
            ("tabula",
             ["Posms", "Spriegums", "Iekārta"],
             [["Ģenerators stacijā", "10–20 kV", "ģenerators"],
              ["Pārvades līnija", "110–330 kV", "paaugstinošs transformators"],
              ["Apakšstacija", "10–20 kV", "pazeminošs transformators"],
              ["Mājas tīkls", "230 V", "sadales transformators"]],
             [4.63, 3.30, 4.30]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Pazeminošs transformators",
             teksts="Transformatora primārajā spolē ir 2000 vijumu, "
                    "sekundārajā 100. Ieejas spriegums 4600 V.\n"
                    "Aprēķini izejas spriegumu!",
             dots=["N₁ = 2000 ;  N₂ = 100", "U₁ = 4600 V"],
             jaaprekina=["U₂ = ?"],
             formulas=["N₁/N₂ = U₁/U₂", "U₂ = U₁ · N₂ / N₁"],
             aprekins=["1)  k = 2000 : 100 = 20",
                       "2)  U₂ = 4600 : 20",
                       "3)  U₂ = 230 V"],
             atbilde="U₂ = 230 V",
             piezime="Tieši tāds transformators stāv pie katras "
                     "daudzdzīvokļu mājas."),
        dict(nr=2, virsraksts="Vijumu skaits",
             teksts="Jāizgatavo transformators, kas 230 V pazemina līdz "
                    "12 V. Primārajā spolē ir 1150 vijumu.\n"
                    "Cik vijumu vajag sekundārajā spolē?",
             dots=["U₁ = 230 V ;  U₂ = 12 V", "N₁ = 1150"],
             jaaprekina=["N₂ = ?"],
             formulas=["U₁/U₂ = N₁/N₂", "N₂ = N₁ · U₂ / U₁"],
             aprekins=["1)  k = 230 : 12 = 19,2",
                       "2)  N₂ = 1150 : 19,2",
                       "3)  N₂ = 60 vijumi"],
             atbilde="N₂ = 60 vijumu",
             piezime="Tādi transformatori ir lādētājos un halogēnu "
                     "apgaismojumā."),
        dict(nr=3, virsraksts="Strāva pārvades līnijā",
             teksts="Pārvades līnijā jāpārraida 10 MW jauda. Salīdzini "
                    "strāvu pie 10 kV un pie 330 kV sprieguma!",
             dots=["P = 10 MW", "U₁ = 10 kV ;  U₂ = 330 kV"],
             jaaprekina=["I₁ = ?", "I₂ = ?"],
             formulas=["P = U · I", "I = P / U"],
             aprekins=["1)  I₁ = 1,0·10⁷ : 1,0·10⁴ = 1,0·10³ A",
                       "2)  I₂ = 1,0·10⁷ : 3,3·10⁵ = 30 A",
                       "3)  n = 1000 : 30 = 33"],
             atbilde="I₁ = 1000 A ;  I₂ = 30 A — 33 reizes mazāk",
             piezime="Zudumi ~I², tātad tie samazinās ~1100 reižu."),
        dict(nr=4, virsraksts="Jaukts: enerģija un lietderība",
             teksts="Vēja ģenerators (P = 2,0 MW, η = 40 %) strādā 6,0 h.\n"
                    "Aprēķini saražoto elektroenerģiju kWh un cik mājām ar "
                    "patēriņu 10 kWh dienā tas pietiktu!",
             dots=["P = 2,0 MW ;  t = 6,0 h", "patēriņš 10 kWh dienā"],
             jaaprekina=["E = ?", "N = ?"],
             formulas=["E = P · t", "N = E / 10 kWh"],
             aprekins=["1)  P = 2,0·10³ kW",
                       "2)  E = 2,0·10³ · 6,0 = 1,2·10⁴ kWh",
                       "3)  N = 1,2·10⁴ : 10 = 1,2·10³"],
             atbilde="E = 1,2·10⁴ kWh ;   pietiktu ~1200 mājām",
             piezime="Jauda 2 MW jau ir izejas jauda, tāpēc η šeit vairs "
                     "nav jāpiemēro."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ģenerators pārvērš mehānisko enerģiju elektriskajā, dzinējs — "
            "otrādi.",
            "Transformators maina maiņstrāvas spriegumu: k = N₁/N₂ = U₁/U₂.",
            "Augsts spriegums pārvadē nozīmē mazu strāvu un mazus zudumus.",
            "Pārvades ķēde: 10–20 kV → 110–330 kV → 10–20 kV → 230 V.",
        ],
        majasdarbs=[
            "Atkārto 15.1.–15.7. stundas formulas un kopsavilkumus.",
            "N₁ = 800, N₂ = 40, U₁ = 4600 V. Aprēķini U₂.",
            "P = 5 MW. Aprēķini strāvu pie 20 kV un pie 110 kV.",
        ],
        pasvertejums=["Protu skaidrot ierīču darbību",
                      "Protu lietot k = N₁/N₂ = U₁/U₂",
                      "Protu pamatot augstu spriegumu pārvadē",
                      "Esmu gatavs pārbaudes darbam"],
        nakama="Nākamā stunda: PD9 — Enerģija dabā un tehnikā."),
),
]

ST16 = [

dict(
    nr="16.1", virsraksts="Datu buklets un risinājuma pieraksts",
    jautajums="Kā ātri atrast un pareizi lietot vajadzīgo formulu?",
    apaksraksts="Datu buklets · Risinājuma noformēšana · Mērvienības",
    merkis="Iemācīties ātri atrast datu bukletā vajadzīgo formulu un noformēt "
           "risinājumu tā, lai par katru soli varētu saņemt punktus.",
    protu=["orientēties datu bukleta sadaļās;",
           "izvēlēties formulu pēc dotajiem lielumiem;",
           "noformēt pilnu risinājumu;",
           "pārbaudīt mērvienības un atbildes ticamību."],
    atkartojums="Eksāmenā datu buklets ir atļauts. Uzvar tas, kurš prot to "
                "ātri lietot — nevis tas, kurš formulas iemācījies no "
                "galvas.",
    uzdevumu_apraksts="Formulas izvēle un pilna risinājuma noformēšana",
    teorija=[
        ("Datu bukleta uzbūve", [
            ("tabula",
             ["Sadaļa", "Kas tur atrodams", "Kad noder"],
             [["Mehānika", "υ, a, x, f, ω", "kustības uzdevumi"],
              ["Dinamika", "F = ma, F = Gm₁m₂/R², p = F/S, M = Fl",
               "spēki, spiediens, sviras"],
              ["Enerģija, darbs", "Ek, Ep, η, p = mυ", "enerģijas uzdevumi"],
              ["Svārstības, viļņi", "λ = υT, λ = c/f, c", "viļņu uzdevumi"],
              ["Vielas uzbūve", "n = m/M = N/NA, ρ = m/V", "daļiņu skaits"],
              ["Līdzstrāva", "R = ρl/S, I = U/R, P = IU", "elektrība"],
              ["Konstantes", "g, c, G, NA, p₀", "visos aprēķinos"]],
             [3.13, 5.10, 4.00]),
        ]),
        ("Kā noformē risinājumu", [
            ("panelis", "PIECI SOĻI — PAR KATRU DOD PUNKTUS",
             ["1. Dots: visi doti lielumi ar apzīmējumiem un mērvienībām.  "
              "2. Jāaprēķina: kas jāatrod.  3. Formulas: no datu bukleta.",
              "4. Aprēķins: pa soļiem, ar mērvienībām, vispirms pārveidojot "
              "SI vienībās.  5. Atbilde: ar mērvienību un saprātīgu "
              "precizitāti."], GOLD),
            ("panelis", "PĀRBAUDES JAUTĀJUMI PIRMS NODOŠANAS",
             ["Vai visi lielumi pārvērsti SI?  ·  Vai mērvienības aprēķinā "
              "sakrīt?  ·  Vai atbilde ir saprātīga pēc lieluma?  ·  Vai "
              "atbildē ir mērvienība?  ·  Vai atbildēts uz visiem "
              "jautājumiem?"], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Formulas izvēle: kustība",
             teksts="Dots: υ₀ = 0, a = 2,5 m/s², t = 8,0 s. Jāatrod ceļš.\n"
                    "Izvēlies formulu no datu bukleta un aprēķini!",
             dots=["υ₀ = 0", "a = 2,5 m/s²", "t = 8,0 s"],
             jaaprekina=["s = ?"],
             formulas=["x = x₀ + υ₀t + at²/2", "ja υ₀ = 0:  s = at²/2"],
             aprekins=["1)  t² = 64 s²",
                       "2)  s = 2,5 · 64 : 2",
                       "3)  s = 80 m"],
             atbilde="s = 80 m",
             piezime="Formulu izvēlas pēc tā, KAS dots — šeit doti a un t, "
                     "tātad der kustības vienādojums."),
        dict(nr=2, virsraksts="Formulas izvēle: enerģija",
             teksts="Dots: m = 1500 kg, υ = 90 km/h. Jāatrod kinētiskā "
                    "enerģija.\nIzvēlies formulu un aprēķini!",
             dots=["m = 1500 kg", "υ = 90 km/h"],
             jaaprekina=["Ek = ?"],
             formulas=["Ek = m·υ² / 2"],
             aprekins=["1)  υ = 90 : 3,6 = 25 m/s",
                       "2)  υ² = 625 m²/s²",
                       "3)  Ek = 1500 · 625 : 2 = 4,7·10⁵ J"],
             atbilde="Ek ≈ 4,7·10⁵ J",
             piezime="Tipiska kļūda — ievietot 90 m/s vietā km/h."),
        dict(nr=3, virsraksts="Formulas izvēle: viļņi",
             teksts="Dots: f = 150 MHz radio raidītājam. Jāatrod viļņa "
                    "garums.\nIzvēlies formulu un aprēķini!",
             dots=["f = 150 MHz", "c = 3,00·10⁸ m/s"],
             jaaprekina=["λ = ?"],
             formulas=["λ = c / f"],
             aprekins=["1)  f = 150·10⁶ = 1,5·10⁸ Hz",
                       "2)  λ = 3,00·10⁸ : 1,5·10⁸",
                       "3)  λ = 2,0 m"],
             atbilde="λ = 2,0 m",
             piezime="EM viļņiem lieto c, mehāniskajiem — vides ātrumu."),
        dict(nr=4, virsraksts="Mērvienību pārbaude",
             teksts="Skolēns aprēķināja spiedienu: p = 500 N : 20 cm² = "
                    "25 Pa.\nAtrodi kļūdu un aprēķini pareizi!",
             dots=["F = 500 N", "S = 20 cm²"],
             jaaprekina=["p = ?"],
             formulas=["p = F / S", "1 cm² = 10⁻⁴ m²"],
             aprekins=["1)  Kļūda: cm² nav pārvērsti m²",
                       "2)  S = 20 cm² = 2,0·10⁻³ m²",
                       "3)  p = 500 : 2,0·10⁻³ = 2,5·10⁵ Pa"],
             atbilde="p = 2,5·10⁵ Pa (nevis 25 Pa)",
             piezime="Kļūda 10 000 reižu. Vienmēr pārvērs laukumus un "
                     "tilpumus!"),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Datu buklets ir sadalīts pa tēmām — iemācies, kur ko meklēt.",
            "Formulu izvēlas pēc tā, kas dots un kas jāatrod.",
            "Risinājumā par katru soli var saņemt punktus.",
            "Biežākā kļūda — nepārvērstas mērvienības (cm², cm³, km/h).",
        ],
        majasdarbs=[
            "Atrodi datu bukletā piecas formulas un pieraksti, kad tās lieto.",
            "υ₀ = 5 m/s, a = 3 m/s², t = 4 s. Aprēķini s un υ.",
            "F = 800 N, S = 40 cm². Aprēķini spiedienu.",
        ],
        pasvertejums=["Protu orientēties datu bukletā",
                      "Protu izvēlēties formulu",
                      "Protu noformēt risinājumu",
                      "Protu pārbaudīt mērvienības"],
        nakama="Nākamā stunda: eksāmena 1. daļa — zināšanas un izpratne."),
),

dict(
    nr="16.2", virsraksts="Eksāmena 1. daļa — zināšanas un izpratne",
    jautajums="Kā ātri izvēlēties pareizo atbildi?",
    apaksraksts="Izvēles uzdevumi · Laika plānošana · Izslēgšanas metode",
    merkis="Iemācīties efektīvi risināt eksāmena 1. daļas izvēles uzdevumus "
           "un plānot laiku.",
    protu=["plānot laiku 1. daļas uzdevumiem;",
           "lietot izslēgšanas metodi;",
           "atpazīt jautājuma tipu;",
           "pārbaudīt atbildi ar novērtējumu."],
    atkartojums="Eksāmena 1. daļā ir 24 uzdevumi un 40 minūtes — vidēji "
                "100 sekundes katram. Tāpēc svarīgs ir ātrums.",
    uzdevumu_apraksts="1. daļas tipa uzdevumi ar aprēķinu",
    teorija=[
        ("Kā strādāt ar 1. daļu", [
            ("kartitas", [
                ("LAIKS", BLUE,
                 ["24 uzdevumi, 40 minūtes.",
                  "~100 s katram.",
                  "Neiestrēgsti — atzīmē un ej tālāk.",
                  "Beigās atgriezies pie atlikušajiem."]),
                ("IZSLĒGŠANA", GREEN,
                 ["Vispirms izsvītro acīmredzami nepareizās.",
                  "Bieži divas atbildes var izslēgt uzreiz.",
                  "Tad izvēlies no atlikušajām divām.",
                  "Neatstāj neatbildētu — nav soda punktu."]),
                ("NOVĒRTĒŠANA", GOLD,
                 ["Bieži pietiek ar aptuvenu aprēķinu.",
                  "Pārbaudi kārtu: vai atbilde 10² vai 10⁵?",
                  "Pārbaudi mērvienību.",
                  "Nepareiza mērvienība = nepareiza atbilde."]),
            ]),
            ("panelis", "TIPISKI 1. DAĻAS JAUTĀJUMU VEIDI",
             ["Jēdziena atpazīšana (kas ir izotops?)  ·  grafika nolasīšana  "
              "·  vienkāršs viena soļa aprēķins  ·  sakarības atpazīšana "
              "(kas notiks, ja...)  ·  mērvienības izvēle  ·  datu bukleta "
              "lietošana."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātrs aprēķins: ātrums",
             teksts="Grafikā ķermeņa koordināta 4 s laikā mainās no 2 m līdz "
                    "12 m.\nKāds ir ātrums? (A 2,5 m/s  B 3,0 m/s  "
                    "C 5,0 m/s  D 10 m/s)",
             dots=["t = 4 s", "Δx = 12 − 2 = 10 m"],
             jaaprekina=["υ = ?"],
             formulas=["υ = Δx / Δt"],
             aprekins=["1)  Δx = 10 m",
                       "2)  υ = 10 : 4",
                       "3)  υ = 2,5 m/s"],
             atbilde="A — υ = 2,5 m/s",
             piezime="Biežā kļūda — dalīt 12 ar 4 un iegūt 3,0 (atbilde B). "
                     "Vienmēr rēķini STARPĪBU."),
        dict(nr=2, virsraksts="Ātrs aprēķins: enerģija",
             teksts="Cik lielu potenciālo enerģiju iegūst 2,0 kg ķermenis, "
                    "pacelts par 5,0 m? (g = 10 m/s²)\n"
                    "(A 10 J  B 25 J  C 100 J  D 1000 J)",
             dots=["m = 2,0 kg ;  h = 5,0 m", "g = 10 m/s²"],
             jaaprekina=["Ep = ?"],
             formulas=["Ep = m · g · h"],
             aprekins=["1)  Ep = 2,0 · 10 · 5,0",
                       "2)  Ep = 100 J"],
             atbilde="C — Ep = 100 J",
             piezime="Vienkāršos aprēķinos g bieži ņem 10 m/s², lai rēķinātu "
                     "no galvas."),
        dict(nr=3, virsraksts="Kārtas novērtēšana",
             teksts="Atoma diametrs ir aptuveni:\n"
                    "(A 10⁻³ m  B 10⁻⁶ m  C 10⁻¹⁰ m  D 10⁻¹⁵ m)",
             dots=["Jāatceras izmēru kārtas"],
             jaaprekina=["d = ?"],
             formulas=["Atoms ~10⁻¹⁰ m ;  kodols ~10⁻¹⁴ m"],
             aprekins=["1)  10⁻³ m = 1 mm — par lielu",
                       "2)  10⁻⁶ m = 1 µm — šūnas izmērs",
                       "3)  10⁻¹⁵ m — elementārdaļiņa"],
             atbilde="C — 10⁻¹⁰ m",
             piezime="Izmēru kārtas no 1.2. stundas jāzina no galvas — tās "
                     "bukletā nav."),
        dict(nr=4, virsraksts="Sakarības atpazīšana",
             teksts="Automašīnas ātrums palielinās divas reizes. Kā mainās "
                    "kinētiskā enerģija?\n"
                    "(A nemainās  B 2×  C 4×  D 8×)",
             dots=["υ₂ = 2·υ₁"],
             jaaprekina=["Ek₂ / Ek₁ = ?"],
             formulas=["Ek = mυ²/2  →  Ek ~ υ²"],
             aprekins=["1)  Ek ~ υ²",
                       "2)  (2υ)² = 4υ²",
                       "3)  Ek palielinās 4 reizes"],
             atbilde="C — 4 reizes",
             piezime="Šis jautājums atkārtojas gandrīz katrā eksāmenā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "1. daļā ~100 s katram uzdevumam — neiestrēgsti.",
            "Izslēgšanas metode: vispirms izsvītro acīmredzami nepareizās.",
            "Pārbaudi lieluma kārtu un mērvienību.",
            "Nekad neatstāj neatbildētu jautājumu.",
        ],
        majasdarbs=[
            "Izpildi vienu iepriekšējā gada eksāmena 1. daļu, mērot laiku.",
            "Pieraksti, kuri uzdevumi bija grūtākie, un atkārto to tēmas.",
            "Atkārto izmēru kārtas no 1.2. stundas.",
        ],
        pasvertejums=["Protu plānot laiku",
                      "Protu lietot izslēgšanas metodi",
                      "Protu novērtēt lieluma kārtu",
                      "Protu atpazīt jautājuma tipu"],
        nakama="Nākamā stunda: eksāmena 2. daļa — prasmes."),
),

dict(
    nr="16.3", virsraksts="Eksāmena 2. daļa un gala atkārtošana",
    jautajums="Kā rīkoties ar grafikiem, datiem un aprēķiniem?",
    apaksraksts="2. daļas uzdevumi · Grafiki un tabulas · Gala atkārtošana",
    merkis="Iemācīties risināt eksāmena 2. daļas vairāku soļu uzdevumus un "
           "izvērtēt savu gatavību eksāmenam.",
    protu=["nolasīt grafikus un tabulas;",
           "risināt vairāku soļu uzdevumu;",
           "pamatot secinājumu ar datiem;",
           "izvērtēt savu gatavību un plānot atkārtošanu."],
    atkartojums="2. daļā ir 7 uzdevumi un 95 minūtes — vidēji 13 minūtes "
                "katram. Šeit vērtē arī risinājuma gaitu, ne tikai atbildi.",
    uzdevumu_apraksts="2. daļas tipa vairāku soļu uzdevumi",
    teorija=[
        ("Kā strādāt ar 2. daļu", [
            ("panelis", "PUNKTUS DOD PAR SOĻIEM",
             ["2. daļā par pareizu formulu, pareizu pārveidojumu un pareizu "
              "starprezultātu dod punktus arī tad, ja galaatbilde ir "
              "kļūdaina.",
              "Tāpēc VIENMĒR raksti visu risinājuma gaitu — Dots, "
              "Jāaprēķina, Formulas, Aprēķins, Atbilde. Nekad neraksti "
              "tikai atbildi."], GOLD),
            ("kartitas", [
                ("GRAFIKI", BLUE,
                 ["Vispirms izlasi asu apzīmējumus.",
                  "Nosaki mērogu (cik vienā rūtiņā).",
                  "Slīpums un laukums ir fizikāli lielumi."]),
                ("TABULAS", GREEN,
                 ["Meklē likumsakarību starp slejām.",
                  "Vai attiecība ir nemainīga?",
                  "Vai lielums aug proporcionāli?"]),
                ("SECINĀJUMI", RED,
                 ["Vienmēr pamato ar SKAITĻIEM.",
                  "“Lielāks” nepietiek — cik reižu?",
                  "Nosauc arī kļūdu avotus."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vairāku soļu uzdevums: kustība un spēks",
             teksts="Automašīna (1000 kg) no 25 m/s apstājas 50 m ceļā.\n"
                    "Aprēķini paātrinājumu, bremzēšanas spēku un laiku!",
             dots=["m = 1000 kg", "υ₀ = 25 m/s ;  υ = 0", "s = 50 m"],
             jaaprekina=["a = ?", "F = ?", "t = ?"],
             formulas=["υ₀² = 2as", "F = m·a", "t = υ₀ / a"],
             aprekins=["1)  a = υ₀² : (2s) = 625 : 100 = 6,25 m/s²",
                       "2)  F = 1000 · 6,25 = 6,25·10³ N",
                       "3)  t = 25 : 6,25 = 4,0 s"],
             atbilde="a = 6,25 m/s² ;  F ≈ 6,3 kN ;  t = 4,0 s",
             piezime="Trīs soļi, trīs punktu grupas — pat ja kļūdies trešajā, "
                     "par pirmajiem diviem punktus saņem."),
        dict(nr=2, virsraksts="Datu analīze no tabulas",
             teksts="Mērījumi: V = 10, 20, 30 cm³; m = 27, 54, 81 g.\n"
                    "Nosaki likumsakarību, aprēķini blīvumu un nosaki "
                    "vielu!",
             dots=["V: 10 ; 20 ; 30 cm³", "m: 27 ; 54 ; 81 g"],
             jaaprekina=["ρ = ?", "Viela = ?"],
             formulas=["ρ = m / V"],
             aprekins=["1)  27:10 = 2,7 ;  54:20 = 2,7 ;  81:30 = 2,7",
                       "2)  Attiecība nemainīga → m ~ V",
                       "3)  ρ = 2,7 g/cm³ = 2700 kg/m³"],
             atbilde="ρ = 2700 kg/m³ — alumīnijs",
             piezime="Vienāda attiecība visās rindās pierāda tiešu "
                     "proporcionalitāti."),
        dict(nr=3, virsraksts="Grafika analīze",
             teksts="υ(t) grafikā ātrums vienmērīgi aug no 0 līdz 20 m/s "
                    "10 s laikā.\n"
                    "Aprēķini paātrinājumu un veikto ceļu (laukums zem "
                    "grafika)!",
             dots=["υ₀ = 0 ;  υ = 20 m/s", "t = 10 s"],
             jaaprekina=["a = ?", "s = ?"],
             formulas=["a = Δυ/Δt", "s = laukums = υ·t/2"],
             aprekins=["1)  a = 20 : 10 = 2,0 m/s²",
                       "2)  Laukums = trijstūris = 20 · 10 : 2",
                       "3)  s = 100 m"],
             atbilde="a = 2,0 m/s² ;   s = 1,0·10² m",
             piezime="Zem taisnes, kas sākas no nulles, laukums ir "
                     "trijstūris."),
        dict(nr=4, virsraksts="Enerģija un lietderība",
             teksts="Sūknis paceļ 300 kg ūdens 12 m augstumā 40 s laikā. "
                    "Sūkņa patērētā jauda 1,5 kW. g = 9,81 m/s².\n"
                    "Aprēķini lietderīgo darbu, jaudu un lietderības "
                    "koeficientu!",
             dots=["m = 300 kg ;  h = 12 m", "t = 40 s ;  P(p) = 1,5 kW"],
             jaaprekina=["A(l) = ?", "P(l) = ?", "η = ?"],
             formulas=["A(l) = m·g·h", "P = A/t", "η = P(l)/P(p)"],
             aprekins=["1)  A(l) = 300 · 9,81 · 12 = 3,53·10⁴ J",
                       "2)  P(l) = 3,53·10⁴ : 40 = 883 W",
                       "3)  η = 883 : 1500 = 0,59 = 59 %"],
             atbilde="A(l) ≈ 3,5·10⁴ J ;  P(l) ≈ 8,8·10² W ;  η ≈ 59 %",
             piezime="Klasisks 2. daļas uzdevums: trīs soļi no trim dažādām "
                     "tēmām."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "2. daļā punktus dod par katru pareizu soli — raksti visu gaitu.",
            "Grafikā slīpums un laukums ir fizikāli lielumi.",
            "Tabulā meklē nemainīgu attiecību — tā liecina par "
            "proporcionalitāti.",
            "Secinājumu vienmēr pamato ar skaitļiem.",
        ],
        majasdarbs=[
            "Izpildi vienu pilnu iepriekšējā gada eksāmenu, ievērojot laiku.",
            "Atzīmē tēmas, kurās kļūdījies, un atkārto to stundu "
            "kopsavilkumus.",
            "Pārliecinies, ka proti lietot datu bukletu bez meklēšanas.",
        ],
        pasvertejums=["Protu nolasīt grafikus un tabulas",
                      "Protu risināt vairāku soļu uzdevumu",
                      "Protu pamatot secinājumu ar datiem",
                      "Jūtos gatavs eksāmenam"],
        nakama="Veiksmi eksāmenā! Atceries: Dots — Jāaprēķina — Formulas — "
               "Aprēķins — Atbilde."),
),
]


def build():
    return (C.build_theme(T15, K15, M15, ST15)
            + C.build_theme(T16, K16, M16, ST16))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
