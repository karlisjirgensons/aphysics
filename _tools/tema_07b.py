# -*- coding: utf-8 -*-
"""10.7. temats, 2. daļa: spēki un mijiedarbība (7.9.-7.16.), pēc tam PD5."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN
from tema_07a import TEMATS, KICKER, MAPE

STUNDAS = [

dict(
    nr="7.9", virsraksts="Inerce un Ņūtona I likums",
    jautajums="Kāpēc pasažieri paliecas uz priekšu?",
    apaksraksts="Inerce · Masa · Ņūtona I likums · Drošības josta",
    merkis="Iemācīties skaidrot inerci un masu kā inerces mēru un ar "
           "piemēriem pamatot pirmo Ņūtona likumu.",
    protu=["formulēt Ņūtona I likumu;",
           "skaidrot inerci ikdienas piemēros;",
           "pamatot masu kā inerces mēru;",
           "aprēķināt rezultējošo spēku un noteikt kustības raksturu."],
    atkartojums="7.1.–7.8. stundā aprakstījām, KĀ ķermeņi kustas. Tagad "
                "noskaidrosim, KĀPĒC tie kustas tieši tā.",
    uzdevumu_apraksts="Rezultējošais spēks un inerce",
    teorija=[
        ("Ņūtona pirmais likums", [
            ("formula", "ŅŪTONA I LIKUMS (inerces likums)",
             "Ja rezultējošais spēks ir nulle, ķermenis paliek miera "
             "stāvoklī vai kustas vienmērīgi taisnvirzienā.",
             "Citiem vārdiem: lai ķermenis kustētos vienmērīgi, spēks NAV "
             "vajadzīgs. Spēks vajadzīgs, lai kustību MAINĪTU.", GOLD),
            ("divi",
             ("INERCE", BLUE,
              ["Ķermeņa īpašība saglabāt savu ātrumu.",
               "Tāpēc, auto strauji bremzējot,",
               "pasažieris turpina kustēties uz priekšu.",
               "Drošības josta iedarbojas ar spēku un aptur."]),
             ("MASA — INERCES MĒRS", GREEN,
              ["Jo lielāka masa, jo grūtāk mainīt ātrumu.",
               "Tukšu ratiņu var apturēt ar roku,",
               "pilnu kravas auto — nē.",
               "Masu mēra kilogramos."])),
        ]),
        ("Kur to redzam ikdienā", [
            ("kartitas", [
                ("BREMZĒJOT", RED,
                 ["Ķermenis turpina kustēties uz priekšu.",
                  "Tāpēc vajadzīga drošības josta",
                  "un galvas balsts."]),
                ("SĀKOT BRAUKT", BLUE,
                 ["Ķermenis “paliek atpakaļ”.",
                  "Autobusā jāturas pie roktura.",
                  "Krava jānostiprina."]),
                ("PAGRIEZIENĀ", GOLD,
                 ["Ķermenis tiecas turpināt taisni.",
                  "Tāpēc pagriezienā met uz sāniem.",
                  "Ātrums pagriezienā jāsamazina."]),
            ]),
            ("panelis", "SVARĪGI SAPRAST",
             ["Ja uz ķermeni darbojas vairāki spēki, kas viens otru "
              "līdzsvaro (rezultējošais spēks = 0), ķermenis kustas "
              "vienmērīgi — tieši tāpat kā tad, ja spēku vispār nebūtu.",
              "Piemēram, automašīna, kas brauc ar nemainīgu ātrumu: dzinēja "
              "vilces spēks ir vienāds ar pretestības spēku."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Rezultējošais spēks",
             teksts="Uz kasti darbojas vilces spēks 250 N un berzes spēks "
                    "250 N pretējā virzienā.\n"
                    "Aprēķini rezultējošo spēku un nosaki, kā kaste kustas!",
             dots=["F₁ = 250 N", "F₂ = 250 N (pretēji)"],
             jaaprekina=["F = ?", "Kustības raksturs = ?"],
             formulas=["F = F₁ − F₂", "Ja F = 0 → Ņūtona I likums"],
             aprekins=["1)  F = 250 − 250 = 0",
                       "2)  Rezultējošais spēks ir nulle",
                       "3)  Pēc I likuma — kustas vienmērīgi vai stāv"],
             atbilde="F = 0 — kaste kustas vienmērīgi vai paliek mierā",
             piezime="Vienmērīgai kustībai spēks nav vajadzīgs — vajadzīgs "
                     "tikai berzes kompensēšanai."),
        dict(nr=2, virsraksts="Bremzēšanas spēks uz pasažieri",
             teksts="Automašīna ar 54 km/h bremzē un apstājas 3,0 s laikā. "
                    "Pasažiera masa 60 kg.\n"
                    "Aprēķini paātrinājumu un spēku, ar kādu jāiedarbojas "
                    "drošības jostai!",
             dots=["υ₀ = 54 km/h ;  υ = 0", "t = 3,0 s", "m = 60 kg"],
             jaaprekina=["a = ?", "F = ?"],
             formulas=["a = (υ − υ₀)/t", "F = m · a"],
             aprekins=["1)  υ₀ = 54 : 3,6 = 15 m/s",
                       "2)  a = (0 − 15) : 3,0 = −5,0 m/s²",
                       "3)  F = 60 · 5,0 = 3,0·10² N"],
             atbilde="a = −5,0 m/s² ;   F = 300 N",
             piezime="Bez jostas šo spēku uzņemtu stūre vai priekšējais "
                     "stikls."),
        dict(nr=3, virsraksts="Divu ķermeņu inerce",
             teksts="Uz diviem ratiņiem (2,0 kg un 8,0 kg) darbojas vienāds "
                    "spēks 12 N.\n"
                    "Aprēķini abu paātrinājumu un salīdzini!",
             dots=["m₁ = 2,0 kg ;  m₂ = 8,0 kg", "F = 12 N"],
             jaaprekina=["a₁ = ?", "a₂ = ?"],
             formulas=["a = F / m"],
             aprekins=["1)  a₁ = 12 : 2,0 = 6,0 m/s²",
                       "2)  a₂ = 12 : 8,0 = 1,5 m/s²",
                       "3)  a₁ / a₂ = 4,0"],
             atbilde="a₁ = 6,0 m/s² ;  a₂ = 1,5 m/s² — vieglākais paātrinās "
                     "4× vairāk",
             piezime="Jo lielāka masa, jo lielāka inerce un mazāks "
                     "paātrinājums."),
        dict(nr=4, virsraksts="Kravas nostiprināšana",
             teksts="Kravas auto ar 36 km/h strauji bremzē un apstājas "
                    "2,0 s laikā. Krava sver 500 kg.\n"
                    "Aprēķini spēku, ar kādu krava spiež uz stiprinājumiem!",
             dots=["υ₀ = 36 km/h ;  υ = 0", "t = 2,0 s", "m = 500 kg"],
             jaaprekina=["a = ?", "F = ?"],
             formulas=["a = (υ − υ₀)/t", "F = m · a"],
             aprekins=["1)  υ₀ = 36 : 3,6 = 10 m/s",
                       "2)  a = 10 : 2,0 = 5,0 m/s²",
                       "3)  F = 500 · 5,0 = 2,5·10³ N"],
             atbilde="F = 2,5·10³ N = 2,5 kN",
             piezime="Pusotras tonnas smaga krava inerces dēļ spiež ar "
                     "spēku, kas atbilst ~250 kg svaram."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ņūtona I likums: ja F = 0, ķermenis stāv vai kustas vienmērīgi.",
            "Inerce ir ķermeņa īpašība saglabāt savu ātrumu.",
            "Masa ir inerces mērs: lielāka masa — grūtāk mainīt ātrumu.",
            "Vienmērīgai kustībai spēks nav vajadzīgs — tikai berzes "
            "kompensēšanai.",
        ],
        majasdarbs=[
            "F₁ = 400 N uz priekšu, F₂ = 150 N atpakaļ. Aprēķini "
            "rezultējošo spēku.",
            "m = 70 kg, a = 4 m/s². Aprēķini spēku.",
            "Paskaidro ar inerci, kāpēc autobusā jāturas pie roktura.",
        ],
        pasvertejums=["Protu formulēt I likumu",
                      "Protu skaidrot inerci",
                      "Protu aprēķināt rezultējošo spēku",
                      "Protu pamatot masu kā inerces mēru"],
        nakama="Nākamā stunda: Ņūtona II likums."),
),

dict(
    nr="7.10", virsraksts="Ņūtona II likums",
    jautajums="Kā spēks maina kustību?",
    apaksraksts="a = F/m · F = ma · Spēku shēma",
    merkis="Iemācīties lietot Ņūtona otro likumu, lai aprēķinātu spēku, masu "
           "vai paātrinājumu, un zīmēt spēku shēmu.",
    protu=["formulēt un lietot Ņūtona II likumu;",
           "aprēķināt F, m vai a;",
           "zīmēt uz ķermeni darbojošos spēku shēmu;",
           "apvienot II likumu ar kinemātikas formulām."],
    atkartojums="7.9. stundā: ja F = 0, ātrums nemainās. Šodien — kas notiek, "
                "ja rezultējošais spēks NAV nulle.",
    uzdevumu_apraksts="Spēks, masa un paātrinājums",
    teorija=[
        ("Ņūtona otrais likums", [
            ("formula", "ŅŪTONA II LIKUMS",
             "a = F / m        F = m · a        m = F / a",
             "Paātrinājums ir tieši proporcionāls rezultējošajam spēkam un "
             "apgriezti proporcionāls masai. Paātrinājums vērsts tajā pašā "
             "virzienā, kur spēks. [F] = N = kg·m/s².", GOLD),
            ("kartitas", [
                ("LIELĀKS SPĒKS", BLUE,
                 ["Ta pati masa, divreiz lielāks spēks",
                  "→ divreiz lielāks paātrinājums.",
                  "a ~ F"]),
                ("LIELĀKA MASA", GREEN,
                 ["Tas pats spēks, divreiz lielāka masa",
                  "→ divreiz mazāks paātrinājums.",
                  "a ~ 1/m"]),
                ("VIRZIENS", RED,
                 ["Paātrinājums vienmēr vērsts",
                  "tāpat kā rezultējošais spēks.",
                  "Bremzējot — pretēji kustībai."]),
            ]),
        ]),
        ("Kā risina uzdevumus ar spēkiem", [
            ("panelis", "SPĒKU SHĒMA — pirmais solis vienmēr",
             ["1. Uzzīmē ķermeni.  2. Attēlo visus spēkus ar bultām: "
              "smaguma spēks lejup, balsta reakcija augšup, vilce, berze.",
              "3. Atrodi rezultējošo spēku (saskaiti vai atņem).  "
              "4. Lieto a = F/m."], NAVY),
            ("tabula",
             ["Situācija", "Rezultējošais spēks", "Rezultāts"],
             [["Vilce > berze", "F = F(vilce) − F(berze)", "paātrinās"],
              ["Vilce = berze", "F = 0", "vienmērīga kustība"],
              ["Vilce < berze", "F < 0", "bremzējas"],
              ["Brīva krišana", "F = mg", "a = g = 9,81 m/s²"]],
             [3.83, 4.60, 3.80]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Paātrinājums no spēka",
             teksts="Uz 1200 kg smagu automašīnu darbojas rezultējošais "
                    "spēks 3,6 kN.\nAprēķini paātrinājumu!",
             dots=["m = 1200 kg", "F = 3,6 kN"],
             jaaprekina=["a = ?"],
             formulas=["a = F / m"],
             aprekins=["1)  F = 3,6 kN = 3,6·10³ N",
                       "2)  a = 3,6·10³ : 1200",
                       "3)  a = 3,0 m/s²"],
             atbilde="a = 3,0 m/s²",
             piezime="Pārbaude: N/kg = kg·m/s² : kg = m/s² ✔"),
        dict(nr=2, virsraksts="Spēks ar berzi",
             teksts="Uz 40 kg smagu kasti darbojas vilces spēks 180 N, "
                    "berzes spēks 60 N.\n"
                    "Aprēķini kastes paātrinājumu!",
             dots=["m = 40 kg", "F₁ = 180 N", "F₂ = 60 N"],
             jaaprekina=["F = ?", "a = ?"],
             formulas=["F = F₁ − F₂", "a = F / m"],
             aprekins=["1)  F = 180 − 60 = 120 N",
                       "2)  a = 120 : 40",
                       "3)  a = 3,0 m/s²"],
             atbilde="F = 120 N ;   a = 3,0 m/s²",
             piezime="Vienmēr vispirms atrodi REZULTĒJOŠO spēku, tikai tad "
                     "lieto a = F/m."),
        dict(nr=3, virsraksts="Spēks no kinemātikas",
             teksts="Ķermenis ar masu 2,5 kg no miera 4,0 s laikā sasniedz "
                    "ātrumu 12 m/s.\n"
                    "Aprēķini paātrinājumu un spēku!",
             dots=["m = 2,5 kg", "υ₀ = 0 ;  υ = 12 m/s", "t = 4,0 s"],
             jaaprekina=["a = ?", "F = ?"],
             formulas=["a = (υ − υ₀)/t", "F = m · a"],
             aprekins=["1)  a = 12 : 4,0 = 3,0 m/s²",
                       "2)  F = 2,5 · 3,0",
                       "3)  F = 7,5 N"],
             atbilde="a = 3,0 m/s² ;   F = 7,5 N",
             piezime="Tipisks divu soļu uzdevums: vispirms kinemātika, tad "
                     "dinamika."),
        dict(nr=4, virsraksts="Bremzēšanas spēks",
             teksts="Automašīna (1000 kg) no 20 m/s apstājas 40 m ceļā.\n"
                    "Aprēķini paātrinājumu un bremzēšanas spēku! "
                    "(υ² = 2as)",
             dots=["m = 1000 kg", "υ₀ = 20 m/s ;  υ = 0", "s = 40 m"],
             jaaprekina=["a = ?", "F = ?"],
             formulas=["υ₀² = 2·a·s  →  a = υ₀²/(2s)", "F = m · a"],
             aprekins=["1)  a = 20² : (2 · 40) = 400 : 80",
                       "2)  a = 5,0 m/s²",
                       "3)  F = 1000 · 5,0 = 5,0·10³ N"],
             atbilde="a = 5,0 m/s² ;   F = 5,0 kN",
             piezime="Šo spēku rada riepu berze pret ceļu — uz slidena ceļa "
                     "tas ir daudz mazāks."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ņūtona II likums: a = F/m jeb F = ma.",
            "Paātrinājums vērsts tāpat kā rezultējošais spēks.",
            "Vienmēr vispirms atrodi rezultējošo spēku.",
            "1 N = 1 kg·m/s² — spēks, kas 1 kg piešķir 1 m/s².",
        ],
        majasdarbs=[
            "m = 800 kg, F = 2,4 kN. Aprēķini a.",
            "Vilce 300 N, berze 120 N, m = 60 kg. Aprēķini a.",
            "m = 3 kg no miera 5 s sasniedz 15 m/s. Aprēķini F.",
        ],
        pasvertejums=["Protu formulēt II likumu",
                      "Protu aprēķināt F, m un a",
                      "Protu zīmēt spēku shēmu",
                      "Protu apvienot ar kinemātiku"],
        nakama="Nākamā stunda: Ņūtona III likums un reaktīvā kustība."),
),

dict(
    nr="7.11", virsraksts="Ņūtona III likums un reaktīvā kustība",
    jautajums="Kāpēc raķete lido?",
    apaksraksts="Spēku pāri · Impulss p = mυ · Impulsa nezūdamība",
    merkis="Iemācīties skaidrot spēku pārus un ar impulsa nezūdamību pamatot "
           "reaktīvo kustību.",
    protu=["formulēt Ņūtona III likumu;",
           "atpazīt spēku pārus situācijās;",
           "aprēķināt impulsu p = mυ;",
           "lietot impulsa nezūdamību reaktīvā kustībā."],
    atkartojums="7.10. stundā: spēks maina kustību. Šodien — spēki vienmēr "
                "rodas PĀROS, un tas ļauj lidot raķetēm.",
    uzdevumu_apraksts="Impulss un impulsa nezūdamība",
    teorija=[
        ("Ņūtona trešais likums", [
            ("formula", "ŅŪTONA III LIKUMS",
             "F₁ = −F₂",
             "Divi ķermeņi iedarbojas viens uz otru ar vienāda lieluma, bet "
             "pretēji vērstiem spēkiem. Spēki darbojas uz DAŽĀDIEM "
             "ķermeņiem, tāpēc tie viens otru neizlīdzina.", GOLD),
            ("kartitas", [
                ("SPĒKU PĀRI", BLUE,
                 ["Zeme velk cilvēku — cilvēks velk Zemi.",
                  "Kāja spiež uz zemi — zeme spiež uz kāju.",
                  "Airis spiež ūdeni — ūdens spiež airi."]),
                ("KĀPĒC NEIZLĪDZINĀS", GREEN,
                 ["Spēki darbojas uz DAŽĀDIEM ķermeņiem.",
                  "Izlīdzināties var tikai spēki,",
                  "kas darbojas uz VIENU ķermeni."]),
                ("REZULTĀTS ATŠĶIRAS", RED,
                 ["Spēki vienādi, bet masas atšķiras.",
                  "a = F/m → vieglākais paātrinās vairāk.",
                  "Tāpēc Zeme praktiski nekustas."]),
            ]),
        ]),
        ("Impulss un reaktīvā kustība", [
            ("formula", "IMPULSS UN TĀ NEZŪDAMĪBA",
             "p = m · υ        m₁υ₁ = m₂υ₂",
             "Slēgtā sistēmā kopējais impulss saglabājas. Ja sistēma sākumā "
             "bija mierā, tad pēc atgrūšanās impulsu summa joprojām ir "
             "nulle.", GOLD),
            ("panelis", "KĀ LIDO RAĶETE",
             ["Raķete izmet degvielas gāzes atpakaļ ar lielu ātrumu. Gāzes "
              "iegūst impulsu vienā virzienā, tāpēc raķete iegūst tikpat "
              "lielu impulsu pretējā virzienā.",
              "Raķetei nav vajadzīgs gaiss, no kā atgrūsties — tāpēc tā "
              "darbojas arī kosmosā."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ķermeņa impulss",
             teksts="Automašīnas masa ir 1500 kg, ātrums 72 km/h.\n"
                    "Aprēķini automašīnas impulsu!",
             dots=["m = 1500 kg", "υ = 72 km/h"],
             jaaprekina=["p = ?"],
             formulas=["p = m · υ"],
             aprekins=["1)  υ = 72 : 3,6 = 20 m/s",
                       "2)  p = 1500 · 20",
                       "3)  p = 3,0·10⁴ kg·m/s"],
             atbilde="p = 3,0·10⁴ kg·m/s",
             piezime="Impulss ir vektors — tam ir arī virziens."),
        dict(nr=2, virsraksts="Laiva un cilvēks",
             teksts="Cilvēks (70 kg) izlec no mierā stāvošas laivas "
                    "(210 kg) ar ātrumu 3,0 m/s.\n"
                    "Aprēķini laivas ātrumu pēc izlēkšanas!",
             dots=["m₁ = 70 kg ;  υ₁ = 3,0 m/s", "m₂ = 210 kg"],
             jaaprekina=["υ₂ = ?"],
             formulas=["m₁υ₁ = m₂υ₂", "υ₂ = m₁υ₁ / m₂"],
             aprekins=["1)  m₁υ₁ = 70 · 3,0 = 210 kg·m/s",
                       "2)  υ₂ = 210 : 210",
                       "3)  υ₂ = 1,0 m/s"],
             atbilde="υ₂ = 1,0 m/s pretējā virzienā",
             piezime="Sākumā kopējais impulss bija nulle — tāds tas paliek "
                     "arī pēc izlēkšanas."),
        dict(nr=3, virsraksts="Raķetes ātrums",
             teksts="Raķete (masa 800 kg) izmet 20 kg gāzu ar ātrumu "
                    "1200 m/s.\nAprēķini raķetes iegūto ātrumu!",
             dots=["m₁ = 20 kg ;  υ₁ = 1200 m/s", "m₂ = 800 kg"],
             jaaprekina=["υ₂ = ?"],
             formulas=["m₁υ₁ = m₂υ₂", "υ₂ = m₁υ₁ / m₂"],
             aprekins=["1)  m₁υ₁ = 20 · 1200 = 2,4·10⁴ kg·m/s",
                       "2)  υ₂ = 2,4·10⁴ : 800",
                       "3)  υ₂ = 30 m/s"],
             atbilde="υ₂ = 30 m/s",
             piezime="Jo lielāks izmesto gāzu ātrums, jo lielāku ātrumu "
                     "iegūst raķete."),
        dict(nr=4, virsraksts="Spēku pāris",
             teksts="Cilvēks (60 kg) atgrūžas no sienas ar spēku 120 N.\n"
                    "Ar kādu spēku siena darbojas uz cilvēku un kāds ir "
                    "cilvēka paātrinājums?",
             dots=["m = 60 kg", "F = 120 N"],
             jaaprekina=["F(sienas) = ?", "a = ?"],
             formulas=["F₁ = −F₂  (III likums)", "a = F / m"],
             aprekins=["1)  Pēc III likuma F(sienas) = 120 N",
                       "2)  Virziens — pretējs, prom no sienas",
                       "3)  a = 120 : 60 = 2,0 m/s²"],
             atbilde="F = 120 N pretējā virzienā ;   a = 2,0 m/s²",
             piezime="Siena arī iegūst impulsu, bet kopā ar visu Zemi — "
                     "tāpēc tās paātrinājums ir nemanāms."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ņūtona III likums: F₁ = −F₂; spēki rodas pāros.",
            "Spēku pāra locekļi darbojas uz dažādiem ķermeņiem.",
            "Impulss p = mυ; slēgtā sistēmā tas saglabājas.",
            "Reaktīvā kustība: m₁υ₁ = m₂υ₂ — tā lido raķete.",
        ],
        majasdarbs=[
            "m = 2000 kg, υ = 15 m/s. Aprēķini impulsu.",
            "Cilvēks 80 kg izlec ar 2 m/s no 160 kg laivas. Aprēķini laivas "
            "ātrumu.",
            "Nosauc trīs spēku pārus no ikdienas un paskaidro tos.",
        ],
        pasvertejums=["Protu formulēt III likumu",
                      "Protu atpazīt spēku pārus",
                      "Protu aprēķināt impulsu",
                      "Protu lietot impulsa nezūdamību"],
        nakama="Nākamā stunda: gravitācijas spēks."),
),

dict(
    nr="7.12", virsraksts="Gravitācijas spēks",
    jautajums="Kas notur planētas orbītā?",
    apaksraksts="F = Gm₁m₂/R² · F = mg · Svars uz citām planētām",
    merkis="Iemācīties lietot vispasaules gravitācijas likumu un aprēķināt "
           "smaguma spēku uz Zemes un citām planētām.",
    protu=["formulēt vispasaules gravitācijas likumu;",
           "lietot F = Gm₁m₂/R²;",
           "aprēķināt smaguma spēku F = mg;",
           "salīdzināt svaru uz dažādām planētām."],
    atkartojums="7.7. stundā mācījāmies brīvo krišanu ar g = 9,81 m/s². "
                "Šodien noskaidrosim, no kā šis g rodas.",
    uzdevumu_apraksts="Gravitācijas spēks un svars",
    teorija=[
        ("Vispasaules gravitācijas likums", [
            ("formula", "GRAVITĀCIJAS LIKUMS",
             "F = G · m₁ · m₂ / R²        G = 6,67·10⁻¹¹ m³/(kg·s²)",
             "Jebkuri divi ķermeņi pievelk viens otru. Spēks aug ar masām un "
             "strauji samazinās, attālumam augot — jo R ir kvadrātā.", GOLD),
            ("divi",
             ("SMAGUMA SPĒKS", BLUE,
              ["Zemes tuvumā: F = m · g",
               "g = 9,81 m/s² Zemes virsmas tuvumā.",
               "Tā ir gravitācijas likuma vienkāršotā forma.",
               "Svars — spēks, ar kādu ķermenis spiež uz balstu."]),
             ("ATTĀLUMA IETEKME", RED,
              ["Divreiz tālāk → četrreiz mazāks spēks.",
               "Trīsreiz tālāk → deviņas reizes mazāks.",
               "F ~ 1/R²",
               "Tāpat kā starojuma devas jauda (3.8. stunda)."])),
        ]),
        ("Gravitācija Saules sistēmā", [
            ("tabula",
             ["Debess ķermenis", "g, m/s²", "Svars 60 kg cilvēkam, N"],
             [["Zeme", "9,81", "589"],
              ["Mēness", "1,62", "97"],
              ["Marss", "3,71", "223"],
              ["Jupiters", "24,8", "1488"]],
             [4.63, 3.30, 4.30]),
            ("panelis", "KĀPĒC PLANĒTAS NEAIZLIDO",
             ["Gravitācijas spēks nemitīgi novirza planētu no taisnvirziena "
              "kustības uz Sauli. Rezultātā planēta “krīt” ap Sauli pa "
              "riņķveida orbītu.",
              "Tas pats notiek ar mākslīgajiem pavadoņiem ap Zemi — tie "
              "nepārtraukti krīt, bet Zeme zem tiem “aizlokās”."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Smaguma spēks uz Zemes",
             teksts="Skolēna masa ir 55 kg. g = 9,81 m/s².\n"
                    "Aprēķini smaguma spēku, kas uz viņu darbojas!",
             dots=["m = 55 kg", "g = 9,81 m/s²"],
             jaaprekina=["F = ?"],
             formulas=["F = m · g"],
             aprekins=["1)  F = 55 kg · 9,81 m/s²",
                       "2)  F = 540 N"],
             atbilde="F ≈ 5,4·10² N",
             piezime="Masa 55 kg, bet svars 540 N — tie ir DAŽĀDI lielumi ar "
                     "dažādām mērvienībām."),
        dict(nr=2, virsraksts="Svars uz Mēness",
             teksts="Uz Mēness g = 1,62 m/s². Astronauta masa ar skafandru "
                    "ir 120 kg.\nAprēķini svaru uz Mēness un uz Zemes un "
                    "salīdzini!",
             dots=["m = 120 kg", "g(M) = 1,62 m/s²", "g(Z) = 9,81 m/s²"],
             jaaprekina=["F(M) = ?", "F(Z) = ?", "n = ?"],
             formulas=["F = m · g"],
             aprekins=["1)  F(M) = 120 · 1,62 = 194 N",
                       "2)  F(Z) = 120 · 9,81 = 1177 N",
                       "3)  n = 1177 : 194 = 6,1"],
             atbilde="F(M) ≈ 194 N ;  F(Z) ≈ 1,2 kN — uz Zemes 6× smagāk",
             piezime="Masa abās vietās ir vienāda — mainās tikai svars."),
        dict(nr=3, virsraksts="Divu ķermeņu pievilkšanās",
             teksts="Divas 1,0·10⁵ kg smagas kravas atrodas 10 m attālumā. "
                    "G = 6,67·10⁻¹¹ m³/(kg·s²).\n"
                    "Aprēķini gravitācijas spēku starp tām!",
             dots=["m₁ = m₂ = 1,0·10⁵ kg", "R = 10 m",
                   "G = 6,67·10⁻¹¹"],
             jaaprekina=["F = ?"],
             formulas=["F = G·m₁·m₂ / R²"],
             aprekins=["1)  m₁·m₂ = 1,0·10¹⁰ kg²",
                       "2)  R² = 100 m²",
                       "3)  F = 6,67·10⁻¹¹ · 1,0·10¹⁰ : 100",
                       "4)  F = 6,7·10⁻³ N"],
             atbilde="F ≈ 6,7·10⁻³ N — mazāk nekā gramu svars",
             piezime="Gravitācija ir vājākā mijiedarbība — to jūtam tikai "
                     "tāpēc, ka Zeme ir ļoti masīva."),
        dict(nr=4, virsraksts="Attāluma ietekme",
             teksts="Pavadonis atrodas Zemes virsmas tuvumā, kur "
                    "F = 8000 N. To paceļ augstumā, kur attālums no Zemes "
                    "centra ir divreiz lielāks.\n"
                    "Aprēķini jauno gravitācijas spēku!",
             dots=["F₁ = 8000 N", "R₂ = 2·R₁"],
             jaaprekina=["F₂ = ?"],
             formulas=["F ~ 1/R²", "F₂ = F₁ / 4"],
             aprekins=["1)  R₂ = 2R₁  →  R₂² = 4R₁²",
                       "2)  F₂ = F₁ : 4",
                       "3)  F₂ = 8000 : 4 = 2,0·10³ N"],
             atbilde="F₂ = 2,0 kN — četras reizes mazāk",
             piezime="Attālumu mēra no planētas CENTRA, nevis no virsmas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "F = Gm₁m₂/R² — jebkuri divi ķermeņi pievelk viens otru.",
            "Zemes tuvumā smaguma spēku rēķina vienkāršāk: F = mg.",
            "Masa ir vienāda visur, bet svars atkarīgs no g.",
            "F ~ 1/R²: divreiz tālāk nozīmē četrreiz mazāku spēku.",
        ],
        majasdarbs=[
            "m = 75 kg. Aprēķini smaguma spēku uz Zemes un uz Marsa "
            "(g = 3,71).",
            "Divi 500 kg ķermeņi 2,0 m attālumā. Aprēķini F.",
            "Attālums palielināts 3 reizes. Cik reižu mainās F?",
        ],
        pasvertejums=["Protu formulēt gravitācijas likumu",
                      "Protu lietot F = Gm₁m₂/R²",
                      "Protu aprēķināt smaguma spēku",
                      "Protu salīdzināt svaru uz planētām"],
        nakama="Nākamā stunda: elastības un berzes spēks."),
),

dict(
    nr="7.13", virsraksts="Elastības un berzes spēks",
    jautajums="Kāpēc kāpnes neslīd?",
    apaksraksts="Fe = −kΔx · Berzes veidi · Berze dabā un tehnikā",
    merkis="Iemācīties lietot Huka likumu un salīdzināt berzes veidus, "
           "pamatojot berzes nozīmi tehnikā un ikdienā.",
    protu=["lietot Fe = −kΔx;",
           "atšķirt miera, slīdes un rites berzi;",
           "aprēķināt berzes spēku;",
           "pamatot, kad berze ir noderīga un kad kaitīga."],
    atkartojums="5.3. stundā jau iepazināmies ar Huka likumu materiālu "
                "kontekstā. Šodien to skatīsim kā spēku starp ķermeņiem.",
    uzdevumu_apraksts="Elastības un berzes spēka aprēķini",
    teorija=[
        ("Elastības spēks", [
            ("formula", "HUKA LIKUMS",
             "Fe = −k · Δx        k = F / Δx",
             "Elastības spēks ir proporcionāls deformācijai un vērsts pretēji "
             "tai. Darbojas tikai līdz elastības robežai.", GOLD),
            ("panelis", "KUR TO IZMANTO",
             ["Dinamometrs mēra spēku pēc atsperes pagarinājuma. Amortizatori "
              "automašīnās, atsperes matračos, batuts, lokšaušanas loks — "
              "visur darbojas elastības spēks."], BLUE),
        ]),
        ("Berzes spēks", [
            ("kartitas", [
                ("MIERA BERZE", BLUE,
                 ["Neļauj ķermenim sākt kustēties.",
                  "Pielāgojas ārējam spēkam.",
                  "Vislielākā no trim veidiem.",
                  "Tāpēc kāpnes un mēbeles neslīd."]),
                ("SLĪDES BERZE", GOLD,
                 ["Rodas, ķermenim slīdot.",
                  "F = µ · N",
                  "µ — berzes koeficients.",
                  "Piemērs: slēpes uz sniega."]),
                ("RITES BERZE", GREEN,
                 ["Rodas, ķermenim ripojot.",
                  "Daudz mazāka par slīdes berzi.",
                  "Tāpēc izgudroja riteni un gultņus."]),
            ]),
            ("divi",
             ("BERZE IR NODERĪGA", GREEN,
              ["Ļauj staigāt un braukt.",
               "Ļauj bremzēt.",
               "Notur naglas, skrūves un mezglus.",
               "Bez tās viss slīdētu."]),
             ("BERZE IR KAITĪGA", RED,
              ["Nolieto detaļas.",
               "Rada lieku siltumu.",
               "Patērē enerģiju.",
               "Samazina ar eļļošanu un gultņiem."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Dinamometra atspere",
             teksts="Dinamometra atspere ar k = 400 N/m pagarinās par "
                    "3,5 cm.\nAprēķini spēku, ko rāda dinamometrs!",
             dots=["k = 400 N/m", "Δx = 3,5 cm"],
             jaaprekina=["F = ?"],
             formulas=["Fe = k · Δx"],
             aprekins=["1)  Δx = 3,5 cm = 0,035 m",
                       "2)  F = 400 · 0,035",
                       "3)  F = 14 N"],
             atbilde="F = 14 N",
             piezime="Tieši tā darbojas atsperu svari veikalā."),
        dict(nr=2, virsraksts="Berzes spēks",
             teksts="Kaste ar masu 50 kg slīd pa horizontālu grīdu. Berzes "
                    "koeficients µ = 0,30. g = 9,81 m/s².\n"
                    "Aprēķini berzes spēku!",
             dots=["m = 50 kg", "µ = 0,30", "g = 9,81 m/s²"],
             jaaprekina=["F(berze) = ?"],
             formulas=["N = m · g", "F = µ · N"],
             aprekins=["1)  N = 50 · 9,81 = 491 N",
                       "2)  F = 0,30 · 491",
                       "3)  F = 147 N"],
             atbilde="F ≈ 1,5·10² N",
             piezime="Uz horizontālas virsmas balsta reakcija N ir vienāda ar "
                     "smaguma spēku."),
        dict(nr=3, virsraksts="Paātrinājums ar berzi",
             teksts="Uz 50 kg kasti darbojas vilces spēks 250 N, berzes "
                    "spēks 147 N.\nAprēķini kastes paātrinājumu!",
             dots=["m = 50 kg", "F₁ = 250 N", "F₂ = 147 N"],
             jaaprekina=["a = ?"],
             formulas=["F = F₁ − F₂", "a = F / m"],
             aprekins=["1)  F = 250 − 147 = 103 N",
                       "2)  a = 103 : 50",
                       "3)  a = 2,1 m/s²"],
             atbilde="a ≈ 2,1 m/s²",
             piezime="Ja vilces spēks būtu mazāks par 147 N, kaste vispār "
                     "nesāktu kustēties."),
        dict(nr=4, virsraksts="Berzes koeficienta noteikšana",
             teksts="Lai 80 kg smagu kasti vilktu vienmērīgi, vajadzīgs "
                    "196 N liels spēks. g = 9,81 m/s².\n"
                    "Aprēķini berzes koeficientu!",
             dots=["m = 80 kg", "F = 196 N", "g = 9,81 m/s²"],
             jaaprekina=["µ = ?"],
             formulas=["Vienmērīgi → F = F(berze)", "µ = F / (m·g)"],
             aprekins=["1)  N = 80 · 9,81 = 785 N",
                       "2)  µ = 196 : 785",
                       "3)  µ = 0,25"],
             atbilde="µ = 0,25",
             piezime="Vienmērīgā kustībā vilces spēks tieši līdzsvaro berzi "
                     "— tas ir Ņūtona I likums."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Fe = −kΔx — elastības spēks proporcionāls deformācijai.",
            "Trīs berzes veidi: miera, slīdes, rites; rites ir vismazākā.",
            "Slīdes berzi rēķina F = µN, uz horizontālas virsmas N = mg.",
            "Berze ir gan noderīga (staigāšana, bremzēšana), gan kaitīga "
            "(nolietojums).",
        ],
        majasdarbs=[
            "k = 250 N/m, Δx = 8 cm. Aprēķini spēku.",
            "m = 30 kg, µ = 0,4. Aprēķini berzes spēku.",
            "Nosauc divus gadījumus, kad berzi palielina, un divus, kad "
            "samazina.",
        ],
        pasvertejums=["Protu lietot Huka likumu",
                      "Protu atšķirt berzes veidus",
                      "Protu aprēķināt berzes spēku",
                      "Protu pamatot berzes nozīmi"],
        nakama="Nākamā stunda: spiediens."),
),

dict(
    nr="7.14", virsraksts="Spiediens",
    jautajums="Kāpēc slēpes nesagrimst sniegā?",
    apaksraksts="p = F/S · Laukuma nozīme · Spiediens tehnikā",
    merkis="Iemācīties lietot p = F/S un pamatot balsta laukuma nozīmi "
           "sadzīves un tehnikas situācijās.",
    protu=["skaidrot, kas ir spiediens, un tā mērvienību;",
           "lietot p = F/S un F = mg;",
           "pamatot, kad laukumu palielina un kad samazina;",
           "aprēķināt spiedienu sadzīves situācijās."],
    atkartojums="5.2. stundā rēķinājām mehānisko spriegumu σ = F/S. "
                "Spiedienu p = F/S rēķina tāpat, bet tas raksturo iedarbību "
                "uz virsmu.",
    uzdevumu_apraksts="Spiediens un balsta laukums",
    teorija=[
        ("Kas ir spiediens", [
            ("formula", "SPIEDIENS",
             "p = F / S        [p] = Pa = N/m²        F = m · g",
             "Spiediens rāda, cik liels spēks darbojas uz laukuma vienību. "
             "Tas pats spēks uz maza laukuma dod lielu spiedienu, uz liela "
             "laukuma — mazu.", GOLD),
            ("divi",
             ("PALIELINA LAUKUMU → MAZĀKS SPIEDIENS", BLUE,
              ["Slēpes un sniega kurpes.",
               "Platas riepas traktoram.",
               "Kāpurķēdes tankam un ekskavatoram.",
               "Plati pamati ēkām."]),
             ("SAMAZINA LAUKUMU → LIELĀKS SPIEDIENS", RED,
              ["Naža asmens, adata, nagla.",
               "Slidas ledū.",
               "Zobi un dzīvnieku nagi.",
               "Urbja gals."])),
        ]),
        ("Spiediens praksē", [
            ("tabula",
             ["Situācija", "Spēks", "Laukums", "Spiediens"],
             [["Cilvēks uz abām kājām", "~700 N", "~0,04 m²", "~18 kPa"],
              ["Cilvēks uz slēpēm", "~700 N", "~0,4 m²", "~1,8 kPa"],
              ["Cilvēks uz slidām", "~700 N", "~0,0004 m²", "~1,8 MPa"],
              ["Atmosfēras spiediens", "—", "—", "101 kPa"]],
             [4.63, 2.60, 2.60, 2.40]),
            ("panelis", "KĀPĒC SLĒPES PALĪDZ",
             ["Cilvēka svars nemainās, bet slēpes palielina balsta laukumu "
              "~10 reižu. Tāpēc spiediens uz sniegu samazinās 10 reižu, un "
              "sniegs to iztur.",
              "Slidas darbojas pretēji: mazs laukums dod lielu spiedienu, kas "
              "izkausē plānu ūdens kārtiņu, un slida slīd."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Cilvēks uz grīdas",
             teksts="Cilvēka masa ir 70 kg, abu pēdu kopējais laukums "
                    "0,035 m². g = 9,81 m/s².\n"
                    "Aprēķini spiedienu uz grīdu!",
             dots=["m = 70 kg", "S = 0,035 m²", "g = 9,81 m/s²"],
             jaaprekina=["p = ?"],
             formulas=["F = m · g", "p = F / S"],
             aprekins=["1)  F = 70 · 9,81 = 687 N",
                       "2)  p = 687 : 0,035",
                       "3)  p = 1,96·10⁴ Pa"],
             atbilde="p ≈ 2,0·10⁴ Pa = 20 kPa",
             piezime="Tas ir ~5 reizes mazāk par atmosfēras spiedienu."),
        dict(nr=2, virsraksts="Slēpes",
             teksts="Tas pats 70 kg smagais cilvēks uzkāpj uz slēpēm, kuru "
                    "kopējais laukums ir 0,35 m².\n"
                    "Aprēķini spiedienu un salīdzini ar iepriekšējo!",
             dots=["F = 687 N", "S = 0,35 m²", "p₁ = 20 kPa"],
             jaaprekina=["p₂ = ?", "n = ?"],
             formulas=["p = F / S", "n = p₁ / p₂"],
             aprekins=["1)  p₂ = 687 : 0,35 = 1,96·10³ Pa",
                       "2)  p₂ = 2,0 kPa",
                       "3)  n = 20 : 2,0 = 10"],
             atbilde="p₂ ≈ 2,0 kPa — 10 reižu mazāks spiediens",
             piezime="Laukums palielinājās 10 reižu, tāpēc spiediens "
                     "samazinājās tikpat reižu."),
        dict(nr=3, virsraksts="Naglas gals",
             teksts="Uz naglu darbojas spēks 150 N. Naglas gala laukums ir "
                    "0,10 mm².\nAprēķini spiedienu naglas galā!",
             dots=["F = 150 N", "S = 0,10 mm²"],
             jaaprekina=["p = ?"],
             formulas=["p = F / S"],
             aprekins=["1)  S = 0,10 mm² = 1,0·10⁻⁷ m²",
                       "2)  p = 150 : 1,0·10⁻⁷",
                       "3)  p = 1,5·10⁹ Pa"],
             atbilde="p = 1,5·10⁹ Pa = 1,5 GPa",
             piezime="Tas ir ~15 000 reižu vairāk par atmosfēras spiedienu — "
                     "tāpēc nagla iespiežas kokā."),
        dict(nr=4, virsraksts="Traktora riepas",
             teksts="Traktora masa ir 4,0 t. Lai spiediens uz augsni "
                    "nepārsniegtu 50 kPa, jāizvēlas riepu platums.\n"
                    "Aprēķini nepieciešamo kopējo saskares laukumu!",
             dots=["m = 4,0·10³ kg", "p = 50 kPa", "g = 9,81 m/s²"],
             jaaprekina=["S = ?"],
             formulas=["F = m · g", "p = F/S  →  S = F / p"],
             aprekins=["1)  F = 4,0·10³ · 9,81 = 3,92·10⁴ N",
                       "2)  p = 50 kPa = 5,0·10⁴ Pa",
                       "3)  S = 3,92·10⁴ : 5,0·10⁴ = 0,78 m²"],
             atbilde="S ≈ 0,78 m²",
             piezime="Tāpēc lauksaimniecības tehnikai ir platas riepas — lai "
                     "nesablīvētu augsni."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "p = F/S; spiedienu mēra paskālos (1 Pa = 1 N/m²).",
            "Tas pats spēks uz maza laukuma dod lielu spiedienu.",
            "Laukumu palielina, lai nesagrimtu; samazina, lai iegrieztu.",
            "Atmosfēras spiediens ir 101 kPa.",
        ],
        majasdarbs=[
            "m = 60 kg, S = 0,03 m². Aprēķini spiedienu.",
            "F = 200 N, S = 0,05 mm². Aprēķini spiedienu naža asmenī.",
            "Nosauc trīs gadījumus, kad laukumu palielina, un trīs, kad "
            "samazina.",
        ],
        pasvertejums=["Protu skaidrot spiedienu",
                      "Protu lietot p = F/S",
                      "Protu pārvērst mm² un cm² uz m²",
                      "Protu pamatot laukuma izvēli"],
        nakama="Nākamā stunda: spēka moments."),
),

dict(
    nr="7.15", virsraksts="Spēka moments",
    jautajums="Kā ietaupīt spēku?",
    apaksraksts="M = F·l · Sviras līdzsvars · Spēka plecs",
    merkis="Iemācīties lietot spēka momentu un sviras līdzsvara nosacījumu, "
           "lai aprēķinātu spēkus un plecus.",
    protu=["skaidrot spēka momentu un spēka plecu;",
           "lietot M = F·l;",
           "pierakstīt sviras līdzsvara nosacījumu;",
           "aprēķināt nezināmu spēku vai plecu."],
    atkartojums="7.10. stundā spēks izraisīja kustību pa taisni. Šodien "
                "skatīsim spēkus, kas izraisa GRIEŠANOS.",
    uzdevumu_apraksts="Spēka moments un sviras līdzsvars",
    teorija=[
        ("Spēka moments", [
            ("formula", "SPĒKA MOMENTS UN LĪDZSVARS",
             "M = F · l        F₁ · l₁ = F₂ · l₂",
             "l — spēka plecs: īsākais attālums no griešanās ass līdz spēka "
             "darbības līnijai. [M] = N·m. Svira ir līdzsvarā, ja momenti "
             "abās pusēs ir vienādi.", GOLD),
            ("kartitas", [
                ("SPĒKA PLECS  l", BLUE,
                 ["Attālums no ass līdz spēkam.",
                  "Jo garāks plecs, jo lielāks moments",
                  "pie tā paša spēka."]),
                ("KĀ IETAUPA SPĒKU", GREEN,
                 ["Garāks plecs → mazāks spēks.",
                  "F₁ = F₂ · l₂ / l₁",
                  "Bet ceļš, ko jāveic, ir garāks."]),
                ("PIEMĒRI", GOLD,
                 ["Knaibles, šķēres, atslēgas kāts.",
                  "Durvju rokturis tālāk no eņģēm.",
                  "Ķerra, airis, lauznis."]),
            ]),
        ]),
        ("Svira praksē", [
            ("tabula",
             ["Ierīce", "Kur ass", "Ko iegūst"],
             [["Knaibles, šķēres", "starp spēkiem", "spēka ieguvumu"],
              ["Ķerra", "ritenis, malā", "spēka ieguvumu"],
              ["Pincete, makšķere", "vienā galā", "ceļa un ātruma ieguvumu"],
              ["Durvis", "eņģes", "spēka ieguvumu"]],
             [4.13, 4.10, 4.00]),
            ("panelis", "ZELTA LIKUMS MEHĀNIKĀ",
             ["Neviens mehānisms nedod enerģijas ieguvumu. Cik reižu iegūst "
              "spēkā, tik reižu zaudē ceļā.",
              "Ja ar sviru spēku samazina 4 reizes, roka jāpārvieto 4 reizes "
              "tālāk. Padarītais darbs paliek tāds pats."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēka moments",
             teksts="Uz sviras galu darbojas spēks 25 N, spēka plecs ir "
                    "0,80 m.\nAprēķini spēka momentu!",
             dots=["F = 25 N", "l = 0,80 m"],
             jaaprekina=["M = ?"],
             formulas=["M = F · l"],
             aprekins=["1)  M = 25 N · 0,80 m",
                       "2)  M = 20 N·m"],
             atbilde="M = 20 N·m",
             piezime="Momentu mēra ņūtonmetros, nevis džoulos, lai gan "
                     "mērvienības izskatās līdzīgi."),
        dict(nr=2, virsraksts="Sviras līdzsvars",
             teksts="Sviras vienā pusē 0,20 m attālumā no ass darbojas spēks "
                    "300 N. Otrā pusē plecs ir 1,20 m.\n"
                    "Aprēķini spēku, kas nepieciešams līdzsvaram!",
             dots=["F₁ = 300 N ;  l₁ = 0,20 m", "l₂ = 1,20 m"],
             jaaprekina=["F₂ = ?"],
             formulas=["F₁·l₁ = F₂·l₂", "F₂ = F₁·l₁ / l₂"],
             aprekins=["1)  F₁·l₁ = 300 · 0,20 = 60 N·m",
                       "2)  F₂ = 60 : 1,20",
                       "3)  F₂ = 50 N"],
             atbilde="F₂ = 50 N — spēka ieguvums 6 reizes",
             piezime="Plecs 6 reizes garāks, tāpēc spēks 6 reizes mazāks."),
        dict(nr=3, virsraksts="Masas noteikšana ar sviru",
             teksts="Uz sviras 0,15 m attālumā no ass novietots nezināms "
                    "ķermenis. Līdzsvaram 0,60 m attālumā vajag 2,0 kg "
                    "atsvaru.\nAprēķini ķermeņa masu!",
             dots=["l₁ = 0,15 m", "m₂ = 2,0 kg ;  l₂ = 0,60 m"],
             jaaprekina=["m₁ = ?"],
             formulas=["F₁·l₁ = F₂·l₂", "F = m·g  →  m₁·l₁ = m₂·l₂"],
             aprekins=["1)  m₁ · 0,15 = 2,0 · 0,60",
                       "2)  m₁ · 0,15 = 1,20",
                       "3)  m₁ = 1,20 : 0,15 = 8,0 kg"],
             atbilde="m₁ = 8,0 kg",
             piezime="g abās pusēs saīsinās — tāpēc var rēķināt tieši ar "
                     "masām."),
        dict(nr=4, virsraksts="Ķerra",
             teksts="Ķerrā ir 60 kg krava, kuras plecs no riteņa ass ir "
                    "0,40 m. Roku plecs ir 1,20 m. g = 9,81 m/s².\n"
                    "Aprēķini spēku, kas jāpieliek rokām!",
             dots=["m = 60 kg", "l₁ = 0,40 m", "l₂ = 1,20 m"],
             jaaprekina=["F₂ = ?"],
             formulas=["F₁ = m·g", "F₁·l₁ = F₂·l₂"],
             aprekins=["1)  F₁ = 60 · 9,81 = 589 N",
                       "2)  F₁·l₁ = 589 · 0,40 = 236 N·m",
                       "3)  F₂ = 236 : 1,20 = 196 N"],
             atbilde="F₂ ≈ 2,0·10² N",
             piezime="Rokām jāceļ tikai ~20 kg vietā 60 kg — trīskāršs spēka "
                     "ieguvums."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "M = F·l; spēka plecs ir attālums no ass līdz spēka līnijai.",
            "Svira līdzsvarā: F₁·l₁ = F₂·l₂.",
            "Garāks plecs nozīmē mazāku vajadzīgo spēku.",
            "Mehānisms dod spēka ieguvumu, bet ne enerģijas ieguvumu.",
        ],
        majasdarbs=[
            "F = 40 N, l = 0,25 m. Aprēķini momentu.",
            "F₁ = 500 N, l₁ = 0,30 m, l₂ = 1,50 m. Aprēķini F₂.",
            "Nosauc trīs sviras no ikdienas un norādi, kur ir to ass.",
        ],
        pasvertejums=["Protu skaidrot spēka momentu",
                      "Protu noteikt spēka plecu",
                      "Protu lietot līdzsvara nosacījumu",
                      "Protu aprēķināt spēka ieguvumu"],
        nakama="Nākamā stunda: vienkāršie mehānismi."),
),

dict(
    nr="7.16", virsraksts="Vienkāršie mehānismi",
    jautajums="Vai mehānisms dod enerģijas ieguvumu?",
    apaksraksts="Svira · Bloks · Slīpā plakne · Zelta likums mehānikā",
    merkis="Salīdzināt vienkāršos mehānismus un pamatot, ka mehānisms ietaupa "
           "spēku, bet ne darbu; sagatavoties PD5.",
    protu=["salīdzināt sviru, bloku un slīpo plakni;",
           "aprēķināt spēka ieguvumu;",
           "pamatot zelta likumu mehānikā;",
           "izvēlēties pareizo formulu temata uzdevumos."],
    atkartojums="Šī ir pēdējā stunda pirms PD5. Atkārtojam visus spēkus: "
                "Ņūtona likumi, gravitācija, berze, spiediens, moments.",
    uzdevumu_apraksts="Mehānismi un jauktie temata uzdevumi",
    teorija=[
        ("Trīs vienkāršie mehānismi", [
            ("kartitas", [
                ("SVIRA", BLUE,
                 ["F₁·l₁ = F₂·l₂",
                  "Ieguvums = l₂ / l₁",
                  "Knaibles, ķerra, airis."]),
                ("BLOKS", GREEN,
                 ["Nekustīgs: maina virzienu, ieguvums 1.",
                  "Kustīgs: ieguvums 2.",
                  "Celtņi, liftu sistēmas."]),
                ("SLĪPĀ PLAKNE", GOLD,
                 ["Ieguvums = garums / augstums",
                  "Jo lēzenāka, jo mazāks spēks.",
                  "Uzbrauktuves, skrūve, ķīlis."]),
            ]),
            ("formula", "ZELTA LIKUMS MEHĀNIKĀ",
             "A = F₁ · s₁ = F₂ · s₂",
             "Cik reižu iegūst spēkā, tik reižu zaudē ceļā. Darbs paliek "
             "nemainīgs — mehānisms enerģiju nerada.", GOLD),
        ]),
        ("Temata formulas vienuviet", [
            ("tabula",
             ["Kas jāatrod", "Formula", "Kur lieto"],
             [["Ātrums, ceļš, laiks", "υ = s/t", "vienmērīga kustība"],
              ["Paātrinājums", "a = Δυ/Δt ;  υ = υ₀ + at", "kinemātika"],
              ["Koordināta, ceļš", "x = x₀ + υ₀t + at²/2", "kinemātika"],
              ["Spēks", "F = m·a", "Ņūtona II likums"],
              ["Smaguma spēks", "F = m·g ;  F = Gm₁m₂/R²", "gravitācija"],
              ["Elastības spēks", "Fe = k·Δx", "atsperes"],
              ["Spiediens", "p = F/S", "balsta laukums"],
              ["Spēka moments", "M = F·l ;  F₁l₁ = F₂l₂", "sviras"]],
             [3.63, 4.60, 4.00]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Slīpā plakne",
             teksts="Mucu (100 kg) uzripina 3,0 m garā uzbrauktuvē 1,0 m "
                    "augstumā. g = 9,81 m/s²; berzi neņem vērā.\n"
                    "Aprēķini vajadzīgo spēku un spēka ieguvumu!",
             dots=["m = 100 kg", "l = 3,0 m", "h = 1,0 m"],
             jaaprekina=["F = ?", "n = ?"],
             formulas=["A = m·g·h = F·l", "F = m·g·h / l"],
             aprekins=["1)  m·g·h = 100 · 9,81 · 1,0 = 981 J",
                       "2)  F = 981 : 3,0 = 327 N",
                       "3)  n = 981 N : 327 N = 3,0"],
             atbilde="F ≈ 3,3·10² N ;   spēka ieguvums 3 reizes",
             piezime="Ieguvums vienāds ar l/h = 3,0/1,0 = 3 — bet ceļš arī "
                     "3 reizes garāks."),
        dict(nr=2, virsraksts="Kustīgais bloks",
             teksts="Ar kustīgo bloku paceļ 40 kg smagu kravu. "
                    "g = 9,81 m/s².\nAprēķini vajadzīgo spēku un ceļu, kas "
                    "jāizvelk, paceļot kravu par 2,0 m!",
             dots=["m = 40 kg", "h = 2,0 m", "kustīgais bloks"],
             jaaprekina=["F = ?", "s = ?"],
             formulas=["F = m·g / 2", "s = 2 · h"],
             aprekins=["1)  F(kravas) = 40 · 9,81 = 392 N",
                       "2)  F = 392 : 2 = 196 N",
                       "3)  s = 2 · 2,0 = 4,0 m"],
             atbilde="F ≈ 2,0·10² N ;   s = 4,0 m",
             piezime="Spēks divreiz mazāks, bet virve jāizvelk divreiz "
                     "garāka — darbs tas pats."),
        dict(nr=3, virsraksts="Jaukts: kustība un spēks",
             teksts="Automašīna (1200 kg) no miera 10 s laikā sasniedz "
                    "20 m/s.\nAprēķini paātrinājumu, spēku un veikto ceļu!",
             dots=["m = 1200 kg", "υ₀ = 0 ;  υ = 20 m/s", "t = 10 s"],
             jaaprekina=["a = ?", "F = ?", "s = ?"],
             formulas=["a = (υ − υ₀)/t", "F = m·a", "s = at²/2"],
             aprekins=["1)  a = 20 : 10 = 2,0 m/s²",
                       "2)  F = 1200 · 2,0 = 2,4·10³ N",
                       "3)  s = 2,0 · 100 : 2 = 100 m"],
             atbilde="a = 2,0 m/s² ;  F = 2,4 kN ;  s = 1,0·10² m",
             piezime="Trīs soļi, trīs formulas — tipisks PD uzdevums."),
        dict(nr=4, virsraksts="Jaukts: svars un spiediens",
             teksts="Skapja masa 120 kg, četru kāju kopējais laukums "
                    "80 cm². g = 9,81 m/s².\n"
                    "Aprēķini svaru un spiedienu uz grīdu!",
             dots=["m = 120 kg", "S = 80 cm²", "g = 9,81 m/s²"],
             jaaprekina=["F = ?", "p = ?"],
             formulas=["F = m·g", "p = F/S"],
             aprekins=["1)  F = 120 · 9,81 = 1,18·10³ N",
                       "2)  S = 80 cm² = 8,0·10⁻³ m²",
                       "3)  p = 1177 : 8,0·10⁻³ = 1,5·10⁵ Pa"],
             atbilde="F ≈ 1,2 kN ;   p ≈ 1,5·10⁵ Pa = 150 kPa",
             piezime="Zem skapja kājām spiediens ir lielāks nekā atmosfēras "
                     "spiediens."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Svira, bloks un slīpā plakne dod spēka ieguvumu.",
            "Kustīgais bloks dod ieguvumu 2; slīpā plakne — l/h.",
            "Zelta likums: cik reižu iegūst spēkā, tik reižu zaudē ceļā.",
            "Neviens mehānisms nerada enerģiju — darbs paliek tas pats.",
        ],
        majasdarbs=[
            "Atkārto 7.9.–7.15. stundas formulas un kopsavilkumus.",
            "Uzbrauktuve 4,0 m gara, 1,0 m augsta, krava 80 kg. Aprēķini F.",
            "Izpildi vienu uzdevumu no katras stundas mājasdarba.",
        ],
        pasvertejums=["Protu salīdzināt mehānismus",
                      "Protu aprēķināt spēka ieguvumu",
                      "Protu pamatot zelta likumu",
                      "Esmu gatavs pārbaudes darbam"],
        nakama="Nākamā stunda: PD5 — Spēki un ķermeņu mijiedarbība "
               "(dinamika)."),
),
]


def build():
    return C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
