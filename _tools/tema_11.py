# -*- coding: utf-8 -*-
"""10.11. temats "Visuma uzbūve un pētniecība" — 8 stundas, pēc tam PD7."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN

TEMATS = "11. temats. Visuma uzbūve un pētniecība"
KICKER = "DABASZINĪBAS · 10. KLASE · 11. TEMATS: VISUMA UZBŪVE UN PĒTNIECĪBA"
MAPE = "C:/aphysics/Dabaszinibas/11. Visuma uzbūve un pētniecība"

STUNDAS = [

dict(
    nr="11.1", virsraksts="Debess sfēra un zvaigznāji",
    jautajums="Kāpēc zvaigznes pārvietojas pa debesīm?",
    apaksraksts="Zvaigznāji · Ekliptika · Zvaigžņlielums · Zvaigžņu karte",
    merkis="Iemācīties lietot zvaigžņu karti un skaidrot debess spīdekļu "
           "redzamo kustību ar Zemes rotāciju.",
    protu=["skaidrot zvaigžņu redzamo kustību;",
           "lietot jēdzienus zvaigznājs, ekliptika, zvaigžņlielums;",
           "atšķirt norietošos un nenorietošos spīdekļus;",
           "aprēķināt debess sfēras pagriešanās leņķi."],
    atkartojums="1.2. stundā sakārtojām Visuma objektus pēc izmēra. Tagad "
                "sāksim tos pētīt tā, kā to darīja pirmie astronomi — ar acīm.",
    uzdevumu_apraksts="Debess sfēras kustība un zvaigžņlielumi",
    teorija=[
        ("Debess sfēra un tās kustība", [
            ("panelis", "KĀPĒC ZVAIGZNES KUSTAS",
             ["Zvaigznes pie debesīm pārvietojas tāpēc, ka Zeme griežas ap "
              "savu asi. Pilnu apgriezienu (360°) tā veic 24 stundās, tātad "
              "debess sfēra pagriežas par 15° stundā.",
              "Ap Polārzvaigzni esošie spīdekļi Latvijā nenoriet — tos sauc "
              "par nenorietošajiem."], NAVY),
            ("kartitas", [
                ("ZVAIGZNĀJS", BLUE,
                 ["Debess apgabals ar nosacītu zvaigžņu grupu.",
                  "Kopā 88 zvaigznāji.",
                  "Lielais Greizais Rati, Orions, Kasiopeja."]),
                ("EKLIPTIKA", GOLD,
                 ["Saules redzamais ceļš pa debesīm gada laikā.",
                  "Iet caur 12 zodiaka zvaigznājiem.",
                  "Rodas Zemes riņķošanas dēļ."]),
                ("ZVAIGŽŅLIELUMS  m", GREEN,
                 ["Raksturo spožumu.",
                  "Jo MAZĀKS m, jo SPOŽĀKA zvaigzne.",
                  "Ar aci redz līdz m = 6."]),
            ]),
        ]),
        ("Kā orientēties pie debesīm", [
            ("formula", "DEBESS SFĒRAS PAGRIEŠANĀS",
             "360° = 24 h        1 h = 15°        α = 15° · t",
             "Zeme rotē no rietumiem uz austrumiem, tāpēc zvaigznes "
             "redzami pārvietojas pretējā virzienā.", GOLD),
            ("tabula",
             ["Objekts", "Zvaigžņlielums m", "Redzamība"],
             [["Saule", "−26,7", "žilbinoši spoža"],
              ["Pilns Mēness", "−12,7", "ļoti spožs"],
              ["Sīriuss (spožākā zvaigzne)", "−1,5", "ļoti labi redzama"],
              ["Polārzvaigzne", "+2,0", "labi redzama"],
              ["Vājākā ar aci redzamā", "+6,0", "tikai tumšās vietās"]],
             [4.63, 3.30, 4.30]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Debess sfēras pagriezies",
             teksts="Novērotājs vēro zvaigzni 3,0 stundas.\n"
                    "Par cik grādiem tā pārvietosies pa debess sfēru?",
             dots=["t = 3,0 h", "360° uz 24 h"],
             jaaprekina=["α = ?"],
             formulas=["α = 360° · t / 24 h = 15° · t"],
             aprekins=["1)  15° stundā",
                       "2)  α = 15° · 3,0",
                       "3)  α = 45°"],
             atbilde="α = 45°",
             piezime="Ceturtdaļa no taisnā leņķa katrā stundā — to var "
                     "pamanīt pat ar aci."),
        dict(nr=2, virsraksts="Cik ilgi novēro?",
             teksts="Zvaigzne pa debesīm pārvietojusies par 75°.\n"
                    "Cik ilgi ilga novērojums?",
             dots=["α = 75°", "15° stundā"],
             jaaprekina=["t = ?"],
             formulas=["t = α / 15°"],
             aprekins=["1)  t = 75° : 15°/h",
                       "2)  t = 5,0 h"],
             atbilde="t = 5,0 h",
             piezime="Šo metodi senatnē izmantoja laika noteikšanai naktī."),
        dict(nr=3, virsraksts="Spožuma salīdzinājums",
             teksts="Divu zvaigžņu zvaigžņlielumi ir m₁ = 1,0 un m₂ = 6,0. "
                    "Katra zvaigžņlieluma vienība nozīmē 2,5 reižu spožuma "
                    "starpību.\nCik reižu pirmā ir spožāka?",
             dots=["m₁ = 1,0", "m₂ = 6,0"],
             jaaprekina=["n = ?"],
             formulas=["Δm = m₂ − m₁", "n = 2,5^Δm"],
             aprekins=["1)  Δm = 6,0 − 1,0 = 5,0",
                       "2)  n = 2,5⁵",
                       "3)  n ≈ 100"],
             atbilde="n ≈ 100 reižu spožāka",
             piezime="Tieši tāpēc skalu izvēlējās tā: 5 zvaigžņlielumi = "
                     "100 reizes."),
        dict(nr=4, virsraksts="Gada kustība",
             teksts="Saule pa ekliptiku gada laikā (365 dienās) pārvietojas "
                    "par 360°.\nPar cik grādiem tā pārvietojas vienā "
                    "mēnesī (30 dienās)?",
             dots=["360° uz 365 dienām", "t = 30 dienas"],
             jaaprekina=["α = ?"],
             formulas=["α = 360° · t / 365"],
             aprekins=["1)  360° : 365 = 0,986°/dienā",
                       "2)  α = 0,986 · 30",
                       "3)  α = 29,6°"],
             atbilde="α ≈ 30°",
             piezime="Tieši tāpēc zodiaks ir sadalīts 12 zvaigznājos pa "
                     "30° katrs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Zvaigznes kustas, jo Zeme rotē: 15° stundā.",
            "Zvaigznājs — debess apgabals; ekliptika — Saules gada ceļš.",
            "Jo mazāks zvaigžņlielums m, jo spožāks objekts.",
            "5 zvaigžņlielumu starpība nozīmē 100 reižu spožuma atšķirību.",
        ],
        majasdarbs=[
            "Cik grādos zvaigzne pārvietosies 8 stundās?",
            "m₁ = 2, m₂ = 7. Cik reižu atšķiras spožums?",
            "Nosauc trīs zvaigznājus, kas Latvijā redzami ziemā.",
        ],
        pasvertejums=["Protu skaidrot zvaigžņu kustību",
                      "Protu lietot zvaigžņlielumu",
                      "Protu aprēķināt pagriešanās leņķi",
                      "Protu orientēties zvaigznājos"],
        nakama="Nākamā stunda: Zemes kustības un gadalaiki."),
),

dict(
    nr="11.2", virsraksts="Zemes kustības un gadalaiki",
    jautajums="Kāpēc ir gadalaiki?",
    apaksraksts="Rotācija · Riņķošana · Ass slīpums · Staru krišanas leņķis",
    merkis="Iemācīties saistīt Zemes rotāciju un riņķošanu ar diennakti, "
           "kalendāru un gadalaiku maiņu.",
    protu=["atšķirt Zemes rotāciju no riņķošanas;",
           "skaidrot gadalaikus ar ass slīpumu;",
           "pamatot, kāpēc svarīgs staru krišanas leņķis;",
           "aprēķināt Zemes kustības ātrumus."],
    atkartojums="11.1. stundā noskaidrojām, ka zvaigznes kustas Zemes "
                "rotācijas dēļ. Šodien — kā Zemes kustības nosaka mūsu "
                "kalendāru.",
    uzdevumu_apraksts="Zemes kustību ātrumi un staru leņķis",
    teorija=[
        ("Divas Zemes kustības", [
            ("divi",
             ("ROTĀCIJA ap asi", BLUE,
              ["Periods: 24 h (diennakts).",
               "Rada dienas un nakts maiņu.",
               "Rada zvaigžņu redzamo kustību.",
               "Ekvatora ātrums ~465 m/s."]),
             ("RIŅĶOŠANA ap Sauli", GREEN,
              ["Periods: 365,25 dienas (gads).",
               "Rada gadalaikus (kopā ar ass slīpumu).",
               "Orbītas rādiuss 1,50·10¹¹ m.",
               "Ātrums ~30 km/s."])),
            ("panelis", "KĀPĒC IR GADALAIKI",
             ["Gadalaiki NAV atkarīgi no attāluma līdz Saulei — janvārī Zeme "
              "ir pat tuvāk Saulei nekā jūlijā.",
              "Gadalaikus rada Zemes ass slīpums 23,5°. Vasarā Saules stari "
              "krīt stāvāk, tāpēc tā pati enerģija sadalās uz mazāka "
              "laukuma, un diena ir garāka."], NAVY),
        ]),
        ("Staru krišanas leņķis", [
            ("formula", "ENERĢIJAS BLĪVUMS UN LEŅĶIS",
             "E = E₀ · sin h",
             "h — Saules augstums virs horizonta. Jo stāvāk krīt stari, jo "
             "vairāk enerģijas uz laukuma vienību.", GOLD),
            ("tabula",
             ["Datums", "Saules augstums Rīgā", "Dienas garums"],
             [["21. jūnijs (vasaras saulgrieži)", "~56°", "~17,5 h"],
              ["21. marts / 23. septembris", "~33°", "12 h"],
              ["21. decembris (ziemas saulgrieži)", "~10°", "~6,5 h"]],
             [5.63, 3.30, 3.30]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Zemes rotācijas ātrums",
             teksts="Zemes rādiuss ir 6,37·10⁶ m, rotācijas periods 24 h.\n"
                    "Aprēķini punkta ātrumu uz ekvatora!",
             dots=["R = 6,37·10⁶ m", "T = 24 h"],
             jaaprekina=["υ = ?"],
             formulas=["s = 2πR", "υ = s / T"],
             aprekins=["1)  s = 2 · 3,14 · 6,37·10⁶ = 4,00·10⁷ m",
                       "2)  T = 24 · 3600 = 8,64·10⁴ s",
                       "3)  υ = 4,00·10⁷ : 8,64·10⁴ = 463 m/s"],
             atbilde="υ ≈ 4,6·10² m/s ≈ 1670 km/h",
             piezime="Mēs to nejūtam, jo kustamies vienmērīgi kopā ar visu "
                     "atmosfēru."),
        dict(nr=2, virsraksts="Zemes orbitālais ātrums",
             teksts="Zemes orbītas rādiuss ir 1,50·10¹¹ m, riņķošanas "
                    "periods 365 dienas.\nAprēķini Zemes orbitālo ātrumu "
                    "km/s!",
             dots=["R = 1,50·10¹¹ m", "T = 365 dienas"],
             jaaprekina=["υ = ?  (km/s)"],
             formulas=["s = 2πR", "υ = s / T"],
             aprekins=["1)  s = 2 · 3,14 · 1,50·10¹¹ = 9,42·10¹¹ m",
                       "2)  T = 365 · 24 · 3600 = 3,15·10⁷ s",
                       "3)  υ = 9,42·10¹¹ : 3,15·10⁷ = 2,99·10⁴ m/s"],
             atbilde="υ ≈ 3,0·10⁴ m/s = 30 km/s",
             piezime="Ap Sauli mēs traucamies 30 km katrā sekundē."),
        dict(nr=3, virsraksts="Staru enerģija vasarā un ziemā",
             teksts="Vasarā Saules augstums Rīgā ir 56°, ziemā 10°. "
                    "(sin 56° = 0,83; sin 10° = 0,17)\n"
                    "Cik reižu vasarā uz laukuma vienību krīt vairāk "
                    "enerģijas?",
             dots=["h₁ = 56° ;  sin h₁ = 0,83", "h₂ = 10° ;  sin h₂ = 0,17"],
             jaaprekina=["n = ?"],
             formulas=["E = E₀ · sin h", "n = sin h₁ / sin h₂"],
             aprekins=["1)  n = 0,83 : 0,17",
                       "2)  n = 4,9"],
             atbilde="n ≈ 4,9 reizes",
             piezime="Gandrīz piecas reizes — tāpēc vasarā ir siltāk, nevis "
                     "attāluma dēļ."),
        dict(nr=4, virsraksts="Diennakts garums uz Marsa",
             teksts="Marsa diennakts ilgst 24 h 37 min.\n"
                    "Par cik grādiem stundā pagriežas Marsa debess sfēra?",
             dots=["T = 24 h 37 min", "360° pilnam apgriezienam"],
             jaaprekina=["ω = ?  (°/h)"],
             formulas=["ω = 360° / T"],
             aprekins=["1)  T = 24 + 37/60 = 24,62 h",
                       "2)  ω = 360° : 24,62 h",
                       "3)  ω = 14,6°/h"],
             atbilde="ω ≈ 14,6° stundā",
             piezime="Gandrīz tāpat kā uz Zemes — tāpēc Marsa misijās lieto "
                     "īpašu “marsa diennakti”."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Rotācija ap asi (24 h) rada diennakti; riņķošana ap Sauli "
            "(365 d) — gadu.",
            "Gadalaikus rada Zemes ass slīpums 23,5°, nevis attālums līdz "
            "Saulei.",
            "Jo stāvāk krīt stari, jo vairāk enerģijas uz laukuma vienību.",
            "Ekvatora ātrums ~465 m/s; orbitālais ātrums ~30 km/s.",
        ],
        majasdarbs=[
            "Aprēķini Zemes rotācijas ātrumu 60° platuma grādos "
            "(R = 6,37·10⁶ · cos 60°).",
            "sin 45° = 0,71 un sin 20° = 0,34. Cik reižu atšķiras enerģija?",
            "Paskaidro, kāpēc janvārī Latvijā ir auksts, lai gan Zeme ir "
            "tuvāk Saulei.",
        ],
        pasvertejums=["Protu atšķirt Zemes kustības",
                      "Protu skaidrot gadalaikus",
                      "Protu aprēķināt kustības ātrumus",
                      "Protu pamatot staru leņķa nozīmi"],
        nakama="Nākamā stunda: Saules sistēma."),
),

dict(
    nr="11.3", virsraksts="Saules sistēma",
    jautajums="Kas ir Saules sistēmā?",
    apaksraksts="Planētas · Pavadoņi · Mazie ķermeņi · Fizikālie apstākļi",
    merkis="Iemācīties grupēt Saules sistēmas objektus un salīdzināt "
           "fizikālos apstākļus uz planētām.",
    protu=["grupēt Saules sistēmas objektus;",
           "salīdzināt Zemes un ārējās grupas planētas;",
           "aprēķināt svaru un attālumus Saules sistēmā;",
           "pamatot, kāpēc uz planētām ir dažādi apstākļi."],
    atkartojums="7.12. stundā mācījāmies gravitācijas likumu. Tas nosaka gan "
                "planētu orbītas, gan svaru uz to virsmas.",
    uzdevumu_apraksts="Saules sistēmas mērogi un fizikālie apstākļi",
    teorija=[
        ("Saules sistēmas sastāvs", [
            ("kartitas", [
                ("ZEMES GRUPA", BLUE,
                 ["Merkurs, Venera, Zeme, Marss.",
                  "Cietas, akmeņainas, mazas.",
                  "Liels blīvums, maz pavadoņu.",
                  "Tuvu Saulei."]),
                ("MILŽU PLANĒTAS", GOLD,
                 ["Jupiters, Saturns, Urāns, Neptūns.",
                  "Gāzu un ledus milži, ļoti lieli.",
                  "Mazs blīvums, daudz pavadoņu, gredzeni.",
                  "Tālu no Saules."]),
                ("MAZIE ĶERMEŅI", GREEN,
                 ["Asteroīdi, komētas, meteoroīdi.",
                  "Pundurplanētas (Plutons, Cerera).",
                  "Asteroīdu josla starp Marsu un Jupiteru.",
                  "Koipera josla aiz Neptūna."]),
            ]),
        ]),
        ("Fizikālie apstākļi", [
            ("tabula",
             ["Planēta", "Attālums, au", "g, m/s²", "Vidējā t°, °C",
              "Atmosfēra"],
             [["Merkurs", "0,39", "3,7", "−170…+430", "praktiski nav"],
              ["Venera", "0,72", "8,9", "+464", "blīva CO₂"],
              ["Zeme", "1,00", "9,8", "+15", "N₂ un O₂"],
              ["Marss", "1,52", "3,7", "−63", "reta CO₂"],
              ["Jupiters", "5,20", "24,8", "−145", "H₂ un He"]],
             [2.43, 2.60, 1.80, 2.90, 2.50]),
            ("panelis", "KAS NOSAKA APSTĀKĻUS",
             ["Attālums no Saules nosaka saņemto enerģiju; masa un rādiuss "
              "nosaka g un spēju noturēt atmosfēru; atmosfēras sastāvs "
              "nosaka siltumnīcas efektu.",
              "Tāpēc Venera ir karstāka par Merkuru, lai gan atrodas tālāk — "
              "vainīga blīvā CO₂ atmosfēra."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Svars uz Marsa",
             teksts="Astronauta masa ar aprīkojumu ir 130 kg. Uz Marsa "
                    "g = 3,7 m/s², uz Zemes 9,81 m/s².\n"
                    "Aprēķini svaru abās vietās un salīdzini!",
             dots=["m = 130 kg", "g(M) = 3,7 m/s²", "g(Z) = 9,81 m/s²"],
             jaaprekina=["F(M) = ?", "F(Z) = ?"],
             formulas=["F = m · g"],
             aprekins=["1)  F(M) = 130 · 3,7 = 481 N",
                       "2)  F(Z) = 130 · 9,81 = 1275 N",
                       "3)  n = 1275 : 481 = 2,7"],
             atbilde="F(M) ≈ 4,8·10² N ;  F(Z) ≈ 1,3 kN — 2,7 reizes vairāk",
             piezime="Uz Marsa pārvietoties ir vieglāk, bet skafandrs "
                     "joprojām ir smags."),
        dict(nr=2, virsraksts="Attālums līdz Jupiteram",
             teksts="Jupiters atrodas 5,20 au no Saules. 1 au = "
                    "1,50·10¹¹ m.\n"
                    "Izsaki attālumu metros un aprēķini, cik ilgi gaisma "
                    "ceļo no Saules līdz Jupiteram!",
             dots=["s = 5,20 au", "1 au = 1,50·10¹¹ m",
                   "c = 3,00·10⁸ m/s"],
             jaaprekina=["s = ?  (m)", "t = ?  (min)"],
             formulas=["s = N · au", "t = s / c"],
             aprekins=["1)  s = 5,20 · 1,50·10¹¹ = 7,80·10¹¹ m",
                       "2)  t = 7,80·10¹¹ : 3,00·10⁸ = 2600 s",
                       "3)  t = 2600 : 60 = 43 min"],
             atbilde="s = 7,80·10¹¹ m ;   t ≈ 43 min",
             piezime="Līdz Zemei gaisma ceļo 8,3 min, līdz Jupiteram — "
                     "5 reizes ilgāk."),
        dict(nr=3, virsraksts="Planētas blīvums",
             teksts="Merkura masa ir 3,3·10²³ kg, rādiuss 2,44·10⁶ m.\n"
                    "Aprēķini vidējo blīvumu! (V = 4/3·π·R³)",
             dots=["m = 3,3·10²³ kg", "R = 2,44·10⁶ m"],
             jaaprekina=["ρ = ?"],
             formulas=["V = 4/3·π·R³", "ρ = m / V"],
             aprekins=["1)  R³ = (2,44·10⁶)³ = 1,45·10¹⁹ m³",
                       "2)  V = 4/3 · 3,14 · 1,45·10¹⁹ = 6,08·10¹⁹ m³",
                       "3)  ρ = 3,3·10²³ : 6,08·10¹⁹ = 5,4·10³ kg/m³"],
             atbilde="ρ ≈ 5,4·10³ kg/m³",
             piezime="Gandrīz tikpat, cik Zemei — Merkuram ir liels dzelzs "
                     "kodols."),
        dict(nr=4, virsraksts="Saules enerģija uz planētām",
             teksts="Uz Zemes (1,00 au) Saules starojuma blīvums ir "
                    "1360 W/m². Enerģija samazinās kā 1/r².\n"
                    "Aprēķini starojuma blīvumu uz Marsa (1,52 au)!",
             dots=["E₁ = 1360 W/m² ;  r₁ = 1,00 au", "r₂ = 1,52 au"],
             jaaprekina=["E₂ = ?"],
             formulas=["E₁·r₁² = E₂·r₂²", "E₂ = E₁ · (r₁/r₂)²"],
             aprekins=["1)  r₂² = 1,52² = 2,31",
                       "2)  E₂ = 1360 : 2,31",
                       "3)  E₂ = 589 W/m²"],
             atbilde="E₂ ≈ 5,9·10² W/m² — 2,3 reizes mazāk",
             piezime="Tāpēc Marsa roveriem vajag lielus saules paneļus."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Zemes grupas planētas — cietas un mazas; milžu planētas — "
            "gāzveida un lielas.",
            "Apstākļus nosaka attālums no Saules, masa un atmosfēra.",
            "Svars uz planētas F = mg; g atkarīgs no planētas masas un "
            "rādiusa.",
            "Saules starojuma blīvums samazinās kā 1/r².",
        ],
        majasdarbs=[
            "m = 80 kg. Aprēķini svaru uz Veneras (g = 8,9) un Jupitera "
            "(g = 24,8).",
            "Saturns 9,54 au. Aprēķini attālumu metros un gaismas ceļošanas "
            "laiku.",
            "Kāpēc Venera ir karstāka par Merkuru? Paskaidro.",
        ],
        pasvertejums=["Protu grupēt objektus",
                      "Protu salīdzināt planētas",
                      "Protu aprēķināt svaru un attālumus",
                      "Protu pamatot apstākļu atšķirības"],
        nakama="Nākamā stunda: attālumi Visumā."),
),

dict(
    nr="11.4", virsraksts="Attālumi Visumā",
    jautajums="Kā izmērīt attālumu līdz zvaigznei?",
    apaksraksts="Astronomiskā vienība · Gaismas gads · Parseks · Paralakse",
    merkis="Iemācīties rēķināt ar astronomiskajām attālumu mērvienībām un "
           "pamatot to izvēli konkrētam objektam.",
    protu=["nosaukt au, gaismas gadu un parseku;",
           "pārvērst starp šīm mērvienībām;",
           "pamatot mērvienības izvēli objektam;",
           "aprēķināt gaismas ceļošanas laiku."],
    atkartojums="1.2. stundā jau rēķinājām attālumu līdz Proksimai Kentauram. "
                "Tagad iepazīsim visas astronomiskās mērvienības.",
    uzdevumu_apraksts="Astronomiskie attālumi un to pārveidošana",
    teorija=[
        ("Trīs mērvienības", [
            ("tabula",
             ["Mērvienība", "Vērtība metros", "Kam lieto"],
             [["Astronomiskā vienība (au)", "1,50·10¹¹ m",
               "attālumi Saules sistēmā"],
              ["Gaismas gads (ly)", "9,46·10¹⁵ m",
               "attālumi līdz zvaigznēm"],
              ["Parseks (pc)", "3,09·10¹⁶ m",
               "profesionālajā astronomijā"]],
             [4.63, 3.30, 4.30]),
            ("panelis", "KĀ IZVĒLAS MĒRVIENĪBU",
             ["Metros astronomiskie attālumi ir neērti — skaitļi ar 11–26 "
              "nullēm. Tāpēc katram mērogam ir sava vienība.",
              "1 gaismas gads = attālums, ko gaisma noiet gadā. "
              "1 pc = 3,26 ly. Visas vērtības ir datu bukletā."], NAVY),
        ]),
        ("Kā mēra attālumu līdz zvaigznei", [
            ("divi",
             ("PARALAKSES METODE", BLUE,
              ["Zvaigzni novēro ar pusgada starpību.",
               "Zeme pa to laiku pārvietojas par 2 au.",
               "Tuvā zvaigzne redzami nobīdās pret fonu.",
               "Pēc nobīdes leņķa aprēķina attālumu."]),
             ("KĀPĒC PARSEKS", GREEN,
              ["1 pc — attālums, no kura 1 au redzama 1 loka sekundes leņķī.",
               "Tuvākā zvaigzne — 1,30 pc.",
               "Metode der līdz ~1000 pc.",
               "Tālākiem objektiem lieto citas metodes."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="No gaismas gadiem uz metriem",
             teksts="Zvaigzne Vega atrodas 25 gaismas gadu attālumā.\n"
                    "Izsaki attālumu metros un parsekos!",
             dots=["s = 25 ly", "1 ly = 9,46·10¹⁵ m",
                   "1 pc = 3,09·10¹⁶ m"],
             jaaprekina=["s = ?  (m)", "s = ?  (pc)"],
             formulas=["s = N · ly", "s(pc) = s(m) / pc"],
             aprekins=["1)  s = 25 · 9,46·10¹⁵ = 2,37·10¹⁷ m",
                       "2)  s = 2,37·10¹⁷ : 3,09·10¹⁶",
                       "3)  s = 7,7 pc"],
             atbilde="s ≈ 2,4·10¹⁷ m ≈ 7,7 pc",
             piezime="Gaisma, ko šodien redzam no Vegas, izstarota pirms "
                     "25 gadiem."),
        dict(nr=2, virsraksts="Galaktikas centrs",
             teksts="Piena Ceļa centrs atrodas 8,0 kpc attālumā "
                    "(1 kpc = 1000 pc).\n"
                    "Izsaki attālumu gaismas gados! (1 pc = 3,26 ly)",
             dots=["s = 8,0 kpc", "1 pc = 3,26 ly"],
             jaaprekina=["s = ?  (ly)"],
             formulas=["s(ly) = s(pc) · 3,26"],
             aprekins=["1)  s = 8,0 kpc = 8,0·10³ pc",
                       "2)  s = 8,0·10³ · 3,26",
                       "3)  s = 2,6·10⁴ ly"],
             atbilde="s ≈ 2,6·10⁴ ly = 26 000 gaismas gadu",
             piezime="Gaismai no galaktikas centra līdz mums vajag "
                     "26 tūkstošus gadu."),
        dict(nr=3, virsraksts="Signāls uz Marsu",
             teksts="Marss atrodas 0,52 au no Zemes (tuvākajā punktā). "
                    "1 au = 1,50·10¹¹ m; c = 3,00·10⁸ m/s.\n"
                    "Cik ilgi radiosignāls ceļo turp un atpakaļ?",
             dots=["s = 0,52 au", "c = 3,00·10⁸ m/s"],
             jaaprekina=["t = ?  (min)"],
             formulas=["s = N · au", "t = 2s / c"],
             aprekins=["1)  s = 0,52 · 1,50·10¹¹ = 7,80·10¹⁰ m",
                       "2)  t = 2 · 7,80·10¹⁰ : 3,00·10⁸ = 520 s",
                       "3)  t = 520 : 60 = 8,7 min"],
             atbilde="t ≈ 8,7 min",
             piezime="Tāpēc Marsa roverus nevar vadīt reāllaikā — tie "
                     "darbojas daļēji patstāvīgi."),
        dict(nr=4, virsraksts="Visuma mērogs",
             teksts="Tālākās novērotās galaktikas atrodas 1,3·10¹⁰ gaismas "
                    "gadu attālumā.\nIzsaki attālumu metros!",
             dots=["s = 1,3·10¹⁰ ly", "1 ly = 9,46·10¹⁵ m"],
             jaaprekina=["s = ?  (m)"],
             formulas=["s = N · ly"],
             aprekins=["1)  s = 1,3·10¹⁰ · 9,46·10¹⁵",
                       "2)  s = 12,3·10²⁵ m",
                       "3)  s = 1,2·10²⁶ m"],
             atbilde="s ≈ 1,2·10²⁶ m",
             piezime="Šis skaitlis sakrīt ar 1.2. stundā minēto Visuma "
                     "izmēra kārtu 10²⁶ m."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "1 au = 1,50·10¹¹ m — Saules sistēmai.",
            "1 ly = 9,46·10¹⁵ m — attālumiem līdz zvaigznēm.",
            "1 pc = 3,09·10¹⁶ m = 3,26 ly — profesionālajā astronomijā.",
            "Attālumu līdz tuvām zvaigznēm mēra ar paralakses metodi.",
        ],
        majasdarbs=[
            "Zvaigzne 12 ly attālumā. Izsaki metros un parsekos.",
            "s = 4,0 kpc. Izsaki gaismas gados.",
            "Cik ilgi gaisma no Saules ceļo līdz Neptūnam (30 au)?",
        ],
        pasvertejums=["Protu nosaukt mērvienības",
                      "Protu tās pārvērst",
                      "Protu izvēlēties piemērotu mērvienību",
                      "Protu aprēķināt gaismas ceļošanas laiku"],
        nakama="Nākamā stunda: zvaigznes un to raksturlielumi."),
),

dict(
    nr="11.5", virsraksts="Zvaigznes un to raksturlielumi",
    jautajums="Kāpēc zvaigznes ir dažādās krāsās?",
    apaksraksts="Temperatūra un krāsa · H–R diagramma · Zvaigžņu evolūcija",
    merkis="Iemācīties saistīt zvaigznes krāsu ar tās virsmas temperatūru un "
           "noteikt Saules raksturlielumus Hercšprunga–Rasela diagrammā.",
    protu=["saistīt krāsu ar virsmas temperatūru;",
           "raksturot zvaigžņu tipus;",
           "lasīt H–R diagrammu;",
           "aprēķināt zvaigznes starjaudu un enerģiju."],
    atkartojums="3.3. stundā mācījāmies, ka spektra līnijas atkarīgas no "
                "atomiem. Tieši pēc spektra nosaka zvaigžņu sastāvu un "
                "temperatūru.",
    uzdevumu_apraksts="Zvaigžņu temperatūra un starjauda",
    teorija=[
        ("Krāsa un temperatūra", [
            ("tabula",
             ["Krāsa", "Virsmas t°, K", "Piemērs", "Tips"],
             [["Zilgana", "20 000–30 000", "Rigels", "karsts milzis"],
              ["Balta", "~10 000", "Sīriuss", "galvenā secība"],
              ["Dzeltena", "~5800", "Saule", "galvenā secība"],
              ["Oranža", "~4000", "Aldebarans", "milzis"],
              ["Sarkana", "~3000", "Betelgeise", "sarkanais pārmilzis"]],
             [2.63, 3.10, 3.30, 3.20]),
            ("panelis", "KRĀSA RĀDA TEMPERATŪRU",
             ["Jo karstāka zvaigzne, jo zilāka tās gaisma; jo vēsāka — jo "
              "sarkanāka. Tas ir tas pats, ko redzam, karsējot metālu: "
              "vispirms sarkans, tad balts.",
              "Tāpēc astronomi zvaigznes temperatūru nosaka, nemaz tur "
              "nelidojot — pietiek ar krāsu un spektru."], NAVY),
        ]),
        ("Hercšprunga–Rasela diagramma", [
            ("kartitas", [
                ("GALVENĀ SECĪBA", BLUE,
                 ["Josla no karstām zilām",
                  "līdz vēsām sarkanām zvaigznēm.",
                  "Tur atrodas ~90 % zvaigžņu,",
                  "arī Saule."]),
                ("MILŽI UN PĀRMILŽI", RED,
                 ["Vēsi, bet ļoti spoži,",
                  "jo ir ļoti lieli.",
                  "Betelgeise, Aldebarans.",
                  "Novecojušas zvaigznes."]),
                ("BALTIE PUNDURI", GREEN,
                 ["Karsti, bet vāji,",
                  "jo ļoti mazi.",
                  "Zvaigžņu atliekas.",
                  "Sīriusa pavadonis."]),
            ]),
            ("panelis", "SAULES RAKSTURLIELUMI",
             ["Virsmas temperatūra ~5800 K  ·  starjauda 3,8·10²⁶ W  ·  "
              "rādiuss 6,96·10⁸ m  ·  masa 1,99·10³⁰ kg  ·  atrodas galvenās "
              "secības vidusdaļā — dzeltena punduru zvaigzne."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Saules starojums uz Zemes",
             teksts="Saules starjauda ir 3,8·10²⁶ W, attālums līdz Zemei "
                    "1,50·10¹¹ m.\n"
                    "Aprēķini starojuma blīvumu pie Zemes! (S = 4πr²)",
             dots=["P = 3,8·10²⁶ W", "r = 1,50·10¹¹ m"],
             jaaprekina=["E = ?  (W/m²)"],
             formulas=["S = 4·π·r²", "E = P / S"],
             aprekins=["1)  r² = 2,25·10²² m²",
                       "2)  S = 4 · 3,14 · 2,25·10²² = 2,83·10²³ m²",
                       "3)  E = 3,8·10²⁶ : 2,83·10²³ = 1343 W/m²"],
             atbilde="E ≈ 1,3·10³ W/m²",
             piezime="Tabulas vērtība ir 1360 W/m² — aprēķins sakrīt."),
        dict(nr=2, virsraksts="Zvaigznes izmērs",
             teksts="Betelgeises rādiuss ir 8,0·10¹¹ m, Saules — "
                    "6,96·10⁸ m.\nCik reižu Betelgeise ir lielāka pēc "
                    "rādiusa un pēc tilpuma?",
             dots=["R₁ = 8,0·10¹¹ m", "R₂ = 6,96·10⁸ m"],
             jaaprekina=["n = ?", "N = ?"],
             formulas=["n = R₁ / R₂", "N = n³"],
             aprekins=["1)  n = 8,0·10¹¹ : 6,96·10⁸ = 1,15·10³",
                       "2)  n ≈ 1150",
                       "3)  N = 1150³ ≈ 1,5·10⁹"],
             atbilde="n ≈ 1,2·10³ ;   N ≈ 1,5·10⁹ reižu pēc tilpuma",
             piezime="Ja Betelgeisi novietotu Saules vietā, tā aizsniegtos "
                     "līdz Jupitera orbītai."),
        dict(nr=3, virsraksts="Temperatūra un krāsa",
             teksts="Zvaigznes A virsmas temperatūra ir 3000 K, zvaigznes B — "
                    "24 000 K.\nCik reižu B ir karstāka un kāda krāsa ir "
                    "katrai?",
             dots=["T₁ = 3000 K", "T₂ = 24 000 K"],
             jaaprekina=["n = ?", "Krāsas = ?"],
             formulas=["n = T₂ / T₁"],
             aprekins=["1)  n = 24 000 : 3000",
                       "2)  n = 8,0",
                       "3)  3000 K → sarkana ;  24 000 K → zilgana"],
             atbilde="n = 8,0 reizes ;  A sarkana, B zilgana",
             piezime="Zilās zvaigznes deg strauji un dzīvo īsi — tikai dažus "
                     "miljonus gadu."),
        dict(nr=4, virsraksts="Saules enerģija gadā",
             teksts="Saules starjauda ir 3,8·10²⁶ W.\n"
                    "Cik enerģijas Saule izstaro vienā gadā "
                    "(3,15·10⁷ s)?",
             dots=["P = 3,8·10²⁶ W", "t = 3,15·10⁷ s"],
             jaaprekina=["E = ?"],
             formulas=["E = P · t"],
             aprekins=["1)  E = 3,8·10²⁶ · 3,15·10⁷",
                       "2)  E = 12,0·10³³",
                       "3)  E = 1,2·10³⁴ J"],
             atbilde="E ≈ 1,2·10³⁴ J",
             piezime="Šo enerģiju rada kodolsintēze Saules kodolā "
                     "(3.4. stunda)."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Zvaigznes krāsa rāda tās virsmas temperatūru: zila — karsta, "
            "sarkana — vēsa.",
            "H–R diagrammā ~90 % zvaigžņu ir galvenajā secībā, arī Saule.",
            "Milži ir vēsi, bet spoži; baltie punduri — karsti, bet vāji.",
            "Saules starjauda 3,8·10²⁶ W, virsmas temperatūra ~5800 K.",
        ],
        majasdarbs=[
            "P = 3,8·10²⁶ W, r = 7,8·10¹¹ m (Jupiters). Aprēķini starojuma "
            "blīvumu.",
            "R₁ = 1,4·10⁹ m, R₂ = 6,96·10⁸ m. Cik reižu atšķiras tilpumi?",
            "Nosauc trīs zvaigznes un to krāsu un temperatūru.",
        ],
        pasvertejums=["Protu saistīt krāsu ar temperatūru",
                      "Protu lasīt H–R diagrammu",
                      "Protu aprēķināt starojuma blīvumu",
                      "Protu raksturot Sauli"],
        nakama="Nākamā stunda: galaktikas un Visuma struktūra."),
),

dict(
    nr="11.6", virsraksts="Galaktikas un Visuma struktūra",
    jautajums="Kā ir uzbūvēts Visums?",
    apaksraksts="Galaktiku tipi · Piena Ceļš · Visuma struktūra · Izplešanās",
    merkis="Iemācīties sakārtot Visuma struktūrelementus pēc izmēra un "
           "salīdzināt galaktiku tipus.",
    protu=["sakārtot Visuma struktūrelementus;",
           "salīdzināt galaktiku tipus;",
           "raksturot Piena Ceļu;",
           "skaidrot sarkano nobīdi un Visuma izplešanos."],
    atkartojums="1.2. stundā jau sakārtojām līmeņus no planētas līdz "
                "Visumam. Šodien katru no tiem aplūkosim tuvāk.",
    uzdevumu_apraksts="Galaktiku mērogi un Visuma izplešanās",
    teorija=[
        ("Visuma struktūra", [
            ("tabula",
             ["Struktūrelements", "Tipisks izmērs", "Piemērs"],
             [["Zvaigžņu sistēma", "10¹³ m", "Saules sistēma"],
              ["Zvaigžņu kopa", "10¹⁷ m", "Plejādes"],
              ["Galaktika", "10²¹ m", "Piena Ceļš (10⁵ ly)"],
              ["Galaktiku kopa", "10²³ m", "Vietējā kopa"],
              ["Galaktiku superkopa", "10²⁴ m", "Lanjakea"],
              ["Novērojamais Visums", "10²⁶ m", "~93 mljrd. ly"]],
             [4.13, 3.10, 5.00]),
        ]),
        ("Galaktikas un izplešanās", [
            ("kartitas", [
                ("SPIRĀLVEIDA", BLUE,
                 ["Disks ar spirāles zariem.",
                  "Daudz gāzes, jaunas zvaigznes.",
                  "Piena Ceļš, Andromeda."]),
                ("ELIPTISKĀS", GOLD,
                 ["Apaļas vai iegarenas.",
                  "Maz gāzes, vecas zvaigznes.",
                  "Lielākās galaktikas Visumā."]),
                ("NEREGULĀRĀS", GREEN,
                 ["Bez noteiktas formas.",
                  "Bieži mazas, ar aktīvu zvaigžņu veidošanos.",
                  "Magelāna mākoņi."]),
            ]),
            ("panelis", "SARKANĀ NOBĪDE UN IZPLEŠANĀS",
             ["Tālu galaktiku spektra līnijas ir nobīdītas uz sarkano pusi — "
              "tas nozīmē, ka tās attālinās no mums.",
              "Jo tālāka galaktika, jo ātrāk tā attālinās. Tas ir galvenais "
              "pierādījums, ka Visums izplešas, un no tā izriet Lielā Sprādziena "
              "modelis."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Piena Ceļa izmērs",
             teksts="Piena Ceļa diametrs ir 1,0·10⁵ gaismas gadu.\n"
                    "Izsaki to metros un parsekos! (1 ly = 9,46·10¹⁵ m; "
                    "1 pc = 3,09·10¹⁶ m)",
             dots=["D = 1,0·10⁵ ly"],
             jaaprekina=["D = ?  (m)", "D = ?  (pc)"],
             formulas=["D = N · ly", "D(pc) = D(m) / pc"],
             aprekins=["1)  D = 1,0·10⁵ · 9,46·10¹⁵ = 9,46·10²⁰ m",
                       "2)  D = 9,46·10²⁰ : 3,09·10¹⁶",
                       "3)  D = 3,1·10⁴ pc = 31 kpc"],
             atbilde="D ≈ 9,5·10²⁰ m ≈ 31 kpc",
             piezime="Gaismai, lai šķērsotu mūsu galaktiku, vajag "
                     "100 000 gadu."),
        dict(nr=2, virsraksts="Galaktiku attālināšanās",
             teksts="Galaktika atrodas 20 Mpc attālumā. Habla konstante "
                    "H = 70 km/s uz 1 Mpc.\n"
                    "Aprēķini, ar kādu ātrumu tā attālinās!",
             dots=["r = 20 Mpc", "H = 70 (km/s)/Mpc"],
             jaaprekina=["υ = ?"],
             formulas=["υ = H · r"],
             aprekins=["1)  υ = 70 · 20",
                       "2)  υ = 1400 km/s",
                       "3)  υ = 1,4·10⁶ m/s"],
             atbilde="υ = 1,4·10³ km/s",
             piezime="Jo tālāka galaktika, jo lielāks attālināšanās ātrums — "
                     "tas ir Habla likums."),
        dict(nr=3, virsraksts="Cik zvaigžņu Piena Ceļā?",
             teksts="Piena Ceļā ir aptuveni 2,0·10¹¹ zvaigžņu. Visumā ir "
                    "aptuveni 2,0·10¹² galaktiku.\n"
                    "Novērtē kopējo zvaigžņu skaitu Visumā!",
             dots=["N₁ = 2,0·10¹¹ zvaigznes", "N₂ = 2,0·10¹² galaktikas"],
             jaaprekina=["N = ?"],
             formulas=["N = N₁ · N₂"],
             aprekins=["1)  N = 2,0·10¹¹ · 2,0·10¹²",
                       "2)  N = 4,0·10²³"],
             atbilde="N ≈ 4·10²³ zvaigžņu",
             piezime="Tas ir aptuveni tikpat, cik atomu vienā molā vielas "
                     "(3.10. stunda)."),
        dict(nr=4, virsraksts="Attālums līdz Andromedai",
             teksts="Andromedas galaktika atrodas 2,5·10⁶ gaismas gadu "
                    "attālumā un tuvojas mums ar 110 km/s.\n"
                    "Pēc cik gadiem tā mūs sasniegtu? (1 ly = 9,46·10¹⁵ m)",
             dots=["s = 2,5·10⁶ ly", "υ = 110 km/s"],
             jaaprekina=["t = ?  (gadi)"],
             formulas=["s = N · ly", "t = s / υ"],
             aprekins=["1)  s = 2,5·10⁶ · 9,46·10¹⁵ = 2,37·10²² m",
                       "2)  υ = 1,10·10⁵ m/s",
                       "3)  t = 2,37·10²² : 1,10·10⁵ = 2,15·10¹⁷ s",
                       "4)  t = 2,15·10¹⁷ : 3,15·10⁷ = 6,8·10⁹ gadi"],
             atbilde="t ≈ 6,8·10⁹ gadi",
             piezime="Andromeda ir viena no retajām galaktikām, kas mums "
                     "tuvojas, nevis attālinās."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Visuma struktūra: zvaigžņu sistēma → kopa → galaktika → "
            "galaktiku kopa → superkopa → Visums.",
            "Galaktiku tipi: spirālveida, eliptiskās, neregulārās.",
            "Piena Ceļš ir spirālveida galaktika ar ~2·10¹¹ zvaigznēm.",
            "Sarkanā nobīde liecina, ka Visums izplešas (Habla likums).",
        ],
        majasdarbs=[
            "Galaktika 50 Mpc attālumā. Aprēķini attālināšanās ātrumu "
            "(H = 70).",
            "Sakārto pēc izmēra: galaktika, planēta, zvaigžņu kopa, Visums, "
            "Saules sistēma.",
            "Paskaidro, ko nozīmē sarkanā nobīde.",
        ],
        pasvertejums=["Protu sakārtot struktūrelementus",
                      "Protu salīdzināt galaktiku tipus",
                      "Protu lietot Habla likumu",
                      "Protu skaidrot izplešanos"],
        nakama="Nākamā stunda: Visuma pētniecība."),
),

dict(
    nr="11.7", virsraksts="Visuma pētniecība",
    jautajums="Kā pēta to, kurp nevar aizlidot?",
    apaksraksts="Teleskopi · Radioteleskopi · Zondes · Irbene",
    merkis="Iemācīties salīdzināt Visuma pētīšanas metodes un pamatot, kāpēc "
           "izpētīta ir tikai daļa no Visuma.",
    protu=["salīdzināt optiskos un radioteleskopus;",
           "raksturot kosmisko zondu un teleskopu iespējas;",
           "raksturot Irbenes radioteleskopa nozīmi;",
           "pamatot novērojumu ierobežojumus."],
    atkartojums="1.4.–1.5. stundā mācījāmies par mikroskopiem un "
                "izšķirtspēju. Teleskopiem darbojas tie paši principi.",
    uzdevumu_apraksts="Teleskopu iespējas un signālu ceļošanas laiks",
    teorija=[
        ("Pētīšanas metodes", [
            ("kartitas", [
                ("OPTISKIE TELESKOPI", BLUE,
                 ["Uztver redzamo gaismu.",
                  "Jo lielāks spoguļa diametrs,",
                  "jo vairāk gaismas un labāka izšķirtspēja.",
                  "Traucē atmosfēra un gaismas piesārņojums."]),
                ("RADIOTELESKOPI", GREEN,
                 ["Uztver radioviļņus.",
                  "Darbojas dienā, naktī un mākoņos.",
                  "Redz to, ko gaismā nevar (gāzes mākoņus).",
                  "Irbenes RT-32 — lielākais Ziemeļeiropā."]),
                ("KOSMISKIE APARĀTI", GOLD,
                 ["Teleskopi orbītā (Habls, Webb) — bez atmosfēras.",
                  "Zondes lido pie planētām.",
                  "Marsa roveri veic mērījumus uz vietas.",
                  "Dārgi un lēni."]),
            ]),
        ]),
        ("Kāpēc izpētīta tikai daļa", [
            ("panelis", "TRĪS IEROBEŽOJUMI",
             ["1. Gaismas ātrums ir galīgs — mēs redzam objektus tādus, kādi "
              "tie bija, kad gaisma tos pameta.",
               "2. Kosmisko aparātu ātrums ir mazs salīdzinājumā ar "
               "astronomiskajiem attālumiem.",
               "3. Instrumentu izšķirtspēja ir ierobežota."], NAVY),
            ("panelis", "IRBENES RADIOTELESKOPS",
             ["Ventspils novadā atrodas RT-32 — 32 m diametra "
              "radioteleskops, lielākais Ziemeļeiropā un astotais lielākais "
              "pasaulē. Tas piedalās starptautiskos novērojumu tīklos un "
              "ir nozīmīgs Latvijas zinātnes objekts."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Teleskopa gaismas savākšana",
             teksts="Teleskopa spoguļa diametrs ir 32 m, cilvēka acs zīlītes "
                    "diametrs 6,0 mm.\n"
                    "Cik reižu vairāk starojuma savāc teleskops? (S ~ d²)",
             dots=["d₁ = 32 m", "d₂ = 6,0 mm"],
             jaaprekina=["n = ?"],
             formulas=["S ~ d²", "n = (d₁/d₂)²"],
             aprekins=["1)  d₂ = 6,0 mm = 6,0·10⁻³ m",
                       "2)  d₁/d₂ = 32 : 6,0·10⁻³ = 5,3·10³",
                       "3)  n = (5,3·10³)² = 2,8·10⁷"],
             atbilde="n ≈ 2,8·10⁷ reižu",
             piezime="Tāpēc teleskops redz objektus, kas acij ir pilnīgi "
                     "neredzami."),
        dict(nr=2, virsraksts="Signāls no zondes",
             teksts="Zonde atrodas 30 au attālumā no Zemes. "
                    "1 au = 1,50·10¹¹ m; c = 3,00·10⁸ m/s.\n"
                    "Cik ilgi signāls ceļo līdz Zemei?",
             dots=["s = 30 au", "c = 3,00·10⁸ m/s"],
             jaaprekina=["t = ?  (h)"],
             formulas=["s = N · au", "t = s / c"],
             aprekins=["1)  s = 30 · 1,50·10¹¹ = 4,50·10¹² m",
                       "2)  t = 4,50·10¹² : 3,00·10⁸ = 1,5·10⁴ s",
                       "3)  t = 15 000 : 3600 = 4,2 h"],
             atbilde="t ≈ 4,2 h",
             piezime="Komandai no Zemes līdz zondei un atbildei atpakaļ "
                     "vajag vairāk nekā 8 stundas."),
        dict(nr=3, virsraksts="Cik sen izstarota gaisma?",
             teksts="Galaktika atrodas 5,0·10⁸ gaismas gadu attālumā.\n"
                    "Pirms cik gadiem tika izstarota gaisma, ko šodien "
                    "redzam? Ko tas nozīmē?",
             dots=["s = 5,0·10⁸ ly"],
             jaaprekina=["t = ?"],
             formulas=["1 ly = attālums, ko gaisma noiet 1 gadā",
                       "t = s / c → skaitliski vienāds ar ly skaitu"],
             aprekins=["1)  Gaisma 1 ly noiet 1 gadā",
                       "2)  t = 5,0·10⁸ gadi"],
             atbilde="t = 5,0·10⁸ gadi — redzam pagātni",
             piezime="Skatoties tālumā, mēs skatāmies atpakaļ laikā — tāpēc "
                     "teleskops ir arī “laika mašīna”."),
        dict(nr=4, virsraksts="Ceļojums līdz zvaigznei",
             teksts="Ātrākā kosmiskā zonde lido ar 20 km/s. Proksima "
                    "Kentaura atrodas 4,01·10¹⁶ m attālumā.\n"
                    "Cik gadu ilgtu ceļojums?",
             dots=["υ = 20 km/s", "s = 4,01·10¹⁶ m"],
             jaaprekina=["t = ?  (gadi)"],
             formulas=["t = s / υ", "1 gads = 3,15·10⁷ s"],
             aprekins=["1)  υ = 2,0·10⁴ m/s",
                       "2)  t = 4,01·10¹⁶ : 2,0·10⁴ = 2,0·10¹² s",
                       "3)  t = 2,0·10¹² : 3,15·10⁷ = 6,4·10⁴ gadi"],
             atbilde="t ≈ 6,4·10⁴ gadi",
             piezime="64 tūkstoši gadu līdz tuvākajai zvaigznei — tāpēc "
                     "Visumu pētām ar starojumu, nevis ceļojot."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Optiskie teleskopi uztver gaismu, radioteleskopi — radioviļņus.",
            "Jo lielāks teleskopa diametrs, jo vairāk starojuma tas savāc "
            "(S ~ d²).",
            "Irbenes RT-32 ir lielākais radioteleskops Ziemeļeiropā.",
            "Izpētīta ir tikai daļa Visuma: gaismas ātrums un tehnikas "
            "iespējas ir ierobežotas.",
        ],
        majasdarbs=[
            "d₁ = 8 m, d₂ = 2 m. Cik reižu vairāk gaismas savāc pirmais?",
            "Zonde 12 au attālumā. Cik ilgi ceļo signāls?",
            "Nosauc divas priekšrocības kosmiskajam teleskopam salīdzinājumā "
            "ar zemes teleskopu.",
        ],
        pasvertejums=["Protu salīdzināt teleskopu veidus",
                      "Protu aprēķināt signāla laiku",
                      "Protu pamatot ierobežojumus",
                      "Protu raksturot Irbenes teleskopu"],
        nakama="Nākamā stunda: citplanētas un dzīvība Visumā."),
),

dict(
    nr="11.8", virsraksts="Citplanētas un dzīvība Visumā",
    jautajums="Vai Visumā ir dzīvība?",
    apaksraksts="Citplanētas · Dzīvības apstākļi · Apdzīvojamā zona",
    merkis="Iemācīties nosaukt dzīvībai nepieciešamos faktorus un izvērtēt "
           "apgalvojumus par citplanētām un to pierādījumus; sagatavoties PD7.",
    protu=["nosaukt dzīvībai nepieciešamos faktorus;",
           "skaidrot, kā atklāj citplanētas;",
           "izvērtēt apgalvojuma pierādījumus;",
           "izvēlēties pareizo formulu temata uzdevumos."],
    atkartojums="Šī ir pēdējā stunda pirms PD7. Atkārtojam: debess sfēra, "
                "Zemes kustības, Saules sistēma, attālumi, zvaigznes, "
                "galaktikas, pētīšanas metodes.",
    uzdevumu_apraksts="Citplanētas un temata jauktie uzdevumi",
    teorija=[
        ("Dzīvība un citplanētas", [
            ("divi",
             ("DZĪVĪBAI VAJADZĪGS", GREEN,
              ["Zvaigznes starojums — enerģija.",
               "Šķidrs ūdens uz virsmas.",
               "Atmosfēra ar piemērotu sastāvu.",
               "Magnētiskais lauks — aizsardzība no starojuma.",
               "Pietiekama gravitācija atmosfēras noturēšanai."]),
             ("KĀ ATKLĀJ CITPLANĒTAS", BLUE,
              ["Tranzīta metode: planēta pārvietojas pār zvaigzni",
               "un tās spožums nedaudz samazinās.",
               "Radiālo ātrumu metode: zvaigzne mazliet šūpojas.",
               "Atklātas jau vairāk nekā 5000 citplanētu."])),
            ("panelis", "APDZĪVOJAMĀ ZONA",
             ["Josla ap zvaigzni, kur temperatūra ļauj ūdenim būt šķidrā "
              "stāvoklī. Zeme atrodas tieši tajā; Venera ir par karstu, "
              "Marss — par aukstu.",
               "Zonas attālums atkarīgs no zvaigznes starjaudas: jo spožāka "
               "zvaigzne, jo tālāk atrodas apdzīvojamā zona."], NAVY),
        ]),
        ("Temata formulas vienuviet", [
            ("tabula",
             ["Kas jāatrod", "Formula", "Kur lieto"],
             [["Debess sfēras leņķis", "α = 15° · t", "novērojumi"],
              ["Kustības ātrums", "υ = 2πR / T", "Zemes kustības"],
              ["Svars uz planētas", "F = m · g", "Saules sistēma"],
              ["Attālums", "s = N · au / ly / pc", "astronomija"],
              ["Gaismas laiks", "t = s / c", "signāli, novērojumi"],
              ["Starojuma blīvums", "E = P / (4πr²)", "zvaigznes"],
              ["Attālināšanās ātrums", "υ = H · r", "Habla likums"]],
             [3.63, 4.60, 4.00]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Tranzīta metode",
             teksts="Planētai šķērsojot zvaigzni, tās spožums samazinās par "
                    "1,0 %. Spožuma kritums atbilst laukumu attiecībai "
                    "(R(pl)/R(zv))².\n"
                    "Cik reižu planētas rādiuss mazāks par zvaigznes?",
             dots=["ΔL/L = 1,0 % = 0,010"],
             jaaprekina=["n = ?"],
             formulas=["ΔL/L = (R(pl)/R(zv))²", "n = R(zv)/R(pl)"],
             aprekins=["1)  (R(pl)/R(zv))² = 0,010",
                       "2)  R(pl)/R(zv) = √0,010 = 0,10",
                       "3)  n = 1 : 0,10 = 10"],
             atbilde="n = 10 reižu mazāks rādiuss",
             piezime="1 % spožuma kritums ir tipisks Jupitera izmēra planētai "
                     "pie Saulei līdzīgas zvaigznes."),
        dict(nr=2, virsraksts="Apdzīvojamā zona",
             teksts="Zvaigznes starjauda ir 4 reizes lielāka par Saules. "
                    "Apdzīvojamās zonas attālums r ~ √P.\n"
                    "Cik au attālumā tā atrodas, ja Saulei tā ir 1,0 au?",
             dots=["P₂ = 4 · P(Saules)", "r₁ = 1,0 au"],
             jaaprekina=["r₂ = ?"],
             formulas=["r ~ √P", "r₂ = r₁ · √(P₂/P₁)"],
             aprekins=["1)  P₂/P₁ = 4",
                       "2)  √4 = 2",
                       "3)  r₂ = 1,0 · 2 = 2,0 au"],
             atbilde="r₂ = 2,0 au",
             piezime="Spožākai zvaigznei apdzīvojamā zona ir tālāk — tur "
                     "arī jāmeklē planētas."),
        dict(nr=3, virsraksts="Jaukts: attālums un signāls",
             teksts="Citplanēta atrodas 12 gaismas gadu attālumā.\n"
                    "Izsaki attālumu metros un aprēķini, cik ilgi ceļo "
                    "radiosignāls turp un atpakaļ!",
             dots=["s = 12 ly", "1 ly = 9,46·10¹⁵ m"],
             jaaprekina=["s = ?  (m)", "t = ?  (gadi)"],
             formulas=["s = N · ly", "t = 2s / c"],
             aprekins=["1)  s = 12 · 9,46·10¹⁵ = 1,14·10¹⁷ m",
                       "2)  Turp gaisma ceļo 12 gadus",
                       "3)  t = 2 · 12 = 24 gadi"],
             atbilde="s ≈ 1,1·10¹⁷ m ;   t = 24 gadi",
             piezime="Saruna ar citplanētu ilgtu paaudzēm — tāpēc signālus "
                     "sūta nepārtraukti, negaidot atbildi."),
        dict(nr=4, virsraksts="Jaukts: svars un starojums",
             teksts="Citplanētas g = 12,5 m/s², astronauta masa 90 kg. "
                    "Planēta saņem 680 W/m² starojuma.\n"
                    "Aprēķini svaru un salīdzini starojumu ar Zemi "
                    "(1360 W/m²)!",
             dots=["m = 90 kg ;  g = 12,5 m/s²", "E₂ = 680 W/m² ;  "
                   "E₁ = 1360 W/m²"],
             jaaprekina=["F = ?", "n = ?"],
             formulas=["F = m · g", "n = E₁ / E₂"],
             aprekins=["1)  F = 90 · 12,5 = 1,13·10³ N",
                       "2)  n = 1360 : 680",
                       "3)  n = 2,0"],
             atbilde="F ≈ 1,1 kN ;   starojuma 2 reizes mazāk nekā uz Zemes",
             piezime="Smagāka gravitācija un vājāka gaisma — dzīvība tur "
                     "izskatītos citādi."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Dzīvībai vajag enerģiju, šķidru ūdeni, atmosfēru un "
            "aizsardzību no starojuma.",
            "Apdzīvojamā zona — attālums, kur ūdens var būt šķidrs.",
            "Citplanētas atklāj pēc zvaigznes spožuma krituma vai šūpošanās.",
            "Apgalvojumu izvērtē pēc pierādījumiem un mērījumiem, ne pēc "
            "iespaida.",
        ],
        majasdarbs=[
            "Atkārto 11.1.–11.7. stundas formulas un kopsavilkumus.",
            "Spožuma kritums 0,25 %. Cik reižu planēta mazāka par zvaigzni?",
            "Zvaigznes starjauda 9 reizes lielāka. Kur ir apdzīvojamā zona?",
        ],
        pasvertejums=["Protu nosaukt dzīvības faktorus",
                      "Protu skaidrot citplanētu atklāšanu",
                      "Protu izvēlēties formulu",
                      "Esmu gatavs pārbaudes darbam"],
        nakama="Nākamā stunda: PD7 — Visuma uzbūve un pētniecība."),
),
]


def build():
    return C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
