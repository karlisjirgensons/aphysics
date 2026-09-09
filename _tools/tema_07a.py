# -*- coding: utf-8 -*-
"""10.7. temats, 1. daļa: kustības apraksts (7.1.-7.8.), pēc tam PD4."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN

TEMATS = "7. temats. Cietu ķermeņu kustība un mijiedarbība"
KICKER = ("DABASZINĪBAS · 10. KLASE · 7. TEMATS: CIETU ĶERMEŅU KUSTĪBA UN "
          "MIJIEDARBĪBA")
MAPE = "C:/aphysics/Dabaszinibas/7. Cietu ķermeņu kustība un mijiedarbība"

STUNDAS = [

dict(
    nr="7.1", virsraksts="Vektori un skalāri",
    jautajums="Ar ko ātrums atšķiras no ceļa?",
    apaksraksts="Skalāri · Vektori · Vektoru saskaitīšana",
    merkis="Iemācīties atšķirt vektoriālus lielumus no skalāriem un saskaitīt "
           "vektorus ģeometriski.",
    protu=["atšķirt vektoriālu lielumu no skalāra;",
           "attēlot vektoru ar bultu;",
           "saskaitīt vektorus, kas vērsti uz vienu un pretējām pusēm;",
           "aprēķināt divu perpendikulāru vektoru summu."],
    atkartojums="1.3. stundā mācījāmies, ka lielumam vajag skaitli un "
                "mērvienību. Dažiem lielumiem ar to nepietiek — vajag arī "
                "virzienu.",
    uzdevumu_apraksts="Vektoru saskaitīšana un rezultējošais lielums",
    teorija=[
        ("Divu veidu fizikālie lielumi", [
            ("divi",
             ("SKALĀRI", BLUE,
              ["Raksturo tikai skaitliskā vērtība un mērvienība.",
               "Ceļš s, laiks t, masa m, temperatūra T, enerģija E.",
               "Saskaita parasti: 3 m + 4 m = 7 m."]),
             ("VEKTORI", RED,
              ["Vajadzīga arī VIRZIENS.",
               "Pārvietojums, ātrums υ, spēks F, paātrinājums a.",
               "Attēlo ar bultu: garums = vērtība, bultas virziens = "
               "virziens.",
               "Saskaita ģeometriski."])),
            ("panelis", "KĀPĒC TAS SVARĪGI",
             ["Ja iet 3 km uz ziemeļiem un tad 4 km uz austrumiem, ceļš ir "
              "7 km, bet pārvietojums — tikai 5 km. Skaitļi atšķiras, jo "
              "ceļš ir skalārs, bet pārvietojums — vektors."], NAVY),
        ]),
        ("Kā saskaita vektorus", [
            ("kartitas", [
                ("VIENĀ VIRZIENĀ", BLUE,
                 ["Vērtības saskaita.",
                  "υ = υ₁ + υ₂",
                  "Piemērs: laiva pa straumi."]),
                ("PRETĒJOS VIRZIENOS", GOLD,
                 ["Vērtības atņem.",
                  "υ = υ₁ − υ₂",
                  "Piemērs: laiva pret straumi."]),
                ("PERPENDIKULĀRI", GREEN,
                 ["Lieto Pitagora teorēmu.",
                  "υ = √(υ₁² + υ₂²)",
                  "Piemērs: laiva šķērso upi."]),
            ]),
            ("formula", "REZULTĒJOŠAIS VEKTORS",
             "υ = υ₁ + υ₂   ·   υ = υ₁ − υ₂   ·   υ = √(υ₁² + υ₂²)",
             "Vienmēr vispirms uzzīmē situāciju un nosaki, kā vērsti "
             "vektori — tikai tad izvēlies formulu.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Laiva pa straumi un pret to",
             teksts="Laivas ātrums pret ūdeni ir 4,0 m/s, upes straumes "
                    "ātrums 1,5 m/s.\nAprēķini laivas ātrumu pret krastu, "
                    "braucot pa straumi un pret straumi!",
             dots=["υ₁ = 4,0 m/s", "υ₂ = 1,5 m/s"],
             jaaprekina=["υ(pa) = ?", "υ(pret) = ?"],
             formulas=["Pa straumi: υ = υ₁ + υ₂",
                       "Pret straumi: υ = υ₁ − υ₂"],
             aprekins=["1)  υ(pa) = 4,0 + 1,5 = 5,5 m/s",
                       "2)  υ(pret) = 4,0 − 1,5 = 2,5 m/s"],
             atbilde="υ(pa) = 5,5 m/s ;   υ(pret) = 2,5 m/s",
             piezime="Straume vienā virzienā palīdz, otrā — traucē. Tieši "
                     "tāpēc ātrums ir vektors."),
        dict(nr=2, virsraksts="Ceļš un pārvietojums",
             teksts="Skolēns nostaigā 30 m uz ziemeļiem, tad 40 m uz "
                    "austrumiem.\nAprēķini veikto ceļu un pārvietojumu!",
             dots=["s₁ = 30 m (Z)", "s₂ = 40 m (A)"],
             jaaprekina=["s = ?", "d = ?"],
             formulas=["s = s₁ + s₂", "d = √(s₁² + s₂²)"],
             aprekins=["1)  s = 30 + 40 = 70 m",
                       "2)  d = √(30² + 40²) = √(900 + 1600)",
                       "3)  d = √2500 = 50 m"],
             atbilde="s = 70 m ;   d = 50 m",
             piezime="Pārvietojums vienmēr ir mazāks vai vienāds ar ceļu."),
        dict(nr=3, virsraksts="Upes šķērsošana",
             teksts="Laiva peld perpendikulāri krastam ar ātrumu 3,0 m/s, "
                    "straume nes to ar 4,0 m/s.\n"
                    "Aprēķini laivas rezultējošo ātrumu pret krastu!",
             dots=["υ₁ = 3,0 m/s", "υ₂ = 4,0 m/s", "vektori ⊥"],
             jaaprekina=["υ = ?"],
             formulas=["υ = √(υ₁² + υ₂²)"],
             aprekins=["1)  υ₁² = 9,0 ;  υ₂² = 16,0",
                       "2)  υ² = 9,0 + 16,0 = 25,0",
                       "3)  υ = √25,0 = 5,0 m/s"],
             atbilde="υ = 5,0 m/s",
             piezime="Klasiskais 3–4–5 trijstūris. Laiva pārceļas šķērsām, "
                     "bet vienlaikus tiek aiznesta lejup pa straumi."),
        dict(nr=4, virsraksts="Divi spēki uz ķermeni",
             teksts="Uz ķermeni darbojas divi spēki: 60 N uz labo pusi un "
                    "25 N uz kreiso.\nAprēķini rezultējošo spēku un nosaki "
                    "tā virzienu!",
             dots=["F₁ = 60 N (pa labi)", "F₂ = 25 N (pa kreisi)"],
             jaaprekina=["F = ?"],
             formulas=["Pretēji vērsti: F = F₁ − F₂"],
             aprekins=["1)  F = 60 N − 25 N",
                       "2)  F = 35 N",
                       "3)  F₁ > F₂ → virziens pa labi"],
             atbilde="F = 35 N, vērsts pa labi",
             piezime="Rezultējošais spēks vienmēr vērsts uz lielākā spēka "
                     "pusi."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Skalāram vajag tikai vērtību, vektoram — arī virzienu.",
            "Ceļš ir skalārs, pārvietojums — vektors.",
            "Vienā virzienā vektorus saskaita, pretējos — atņem.",
            "Perpendikulāriem vektoriem υ = √(υ₁² + υ₂²).",
        ],
        majasdarbs=[
            "Kuri ir vektori: masa, ātrums, laiks, spēks, ceļš, "
            "paātrinājums?",
            "Lidmašīna 200 m/s, sānvējš 50 m/s perpendikulāri. Aprēķini "
            "rezultējošo ātrumu.",
            "Iet 60 m uz austrumiem, tad 80 m uz dienvidiem. Aprēķini ceļu "
            "un pārvietojumu.",
        ],
        pasvertejums=["Protu atšķirt vektoru no skalāra",
                      "Protu attēlot vektoru",
                      "Protu saskaitīt vektorus",
                      "Protu lietot Pitagora teorēmu"],
        nakama="Nākamā stunda: ceļš, pārvietojums un trajektorija."),
),

dict(
    nr="7.2", virsraksts="Ceļš, pārvietojums, trajektorija",
    jautajums="Cik tālu un cik daudz?",
    apaksraksts="Trajektorija · Ceļš · Pārvietojums · Atskaites sistēma",
    merkis="Iemācīties aprēķināt un salīdzināt ceļu un pārvietojumu kustībai "
           "pa dažādām trajektorijām.",
    protu=["skaidrot, kas ir trajektorija un atskaites sistēma;",
           "aprēķināt ceļu un pārvietojumu;",
           "salīdzināt tos dažādās kustībās;",
           "pamatot, kāpēc kustība ir relatīva."],
    atkartojums="7.1. stundā noskaidrojām: ceļš ir skalārs, pārvietojums — "
                "vektors. Šodien to izmantosim praksē.",
    uzdevumu_apraksts="Ceļa un pārvietojuma aprēķini",
    teorija=[
        ("Pamatjēdzieni", [
            ("kartitas", [
                ("TRAJEKTORIJA", BLUE,
                 ["Līnija, pa kuru ķermenis pārvietojas.",
                  "Taisnvirziena vai līklīnijas kustība.",
                  "Atkarīga no atskaites sistēmas."]),
                ("CEĻŠ  s", GREEN,
                 ["Trajektorijas garums.",
                  "Vienmēr pozitīvs, skalārs.",
                  "Mēra metros."]),
                ("PĀRVIETOJUMS", RED,
                 ["Vektors no sākuma uz beigu punktu.",
                  "Var būt arī nulle!",
                  "Vienmēr ≤ ceļš."]),
            ]),
            ("panelis", "ATSKAITES SISTĒMA — kustība ir relatīva",
             ["Pasažieris, kas sēž vilcienā, attiecībā pret vagonu ir miera "
              "stāvoklī, bet attiecībā pret sliedēm kustas ar 100 km/h.",
              "Tāpēc vienmēr jānorāda, attiecībā pret ko kustība tiek "
              "aplūkota."], NAVY),
        ]),
        ("Tipiskas situācijas", [
            ("tabula",
             ["Kustība", "Ceļš s", "Pārvietojums", "Attiecība"],
             [["Taisnvirziena, uz priekšu", "s", "s", "vienādi"],
              ["Turp un atpakaļ (l uz vienu pusi)", "2l", "0", "pārv. = 0"],
              ["Pa apļa loku (pusaplis, R)", "πR", "2R", "s > pārv."],
              ["Pilns aplis (R)", "2πR", "0", "pārv. = 0"]],
             [4.63, 2.60, 2.60, 2.40]),
            ("panelis", "IEVĒRO",
             ["Ja ķermenis atgriežas sākuma punktā, pārvietojums ir NULLE, "
              "lai cik garš būtu veiktais ceļš. Piemēram, skrējiens pa "
              "stadiona apli: ceļš 400 m, pārvietojums 0."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Turp un atpakaļ",
             teksts="Skolēns aiziet no mājām līdz skolai 800 m attālumā un "
                    "atgriežas mājās.\nAprēķini veikto ceļu un pārvietojumu!",
             dots=["l = 800 m", "turp un atpakaļ"],
             jaaprekina=["s = ?", "d = ?"],
             formulas=["s = 2 · l", "d = 0, ja atgriežas sākumā"],
             aprekins=["1)  s = 2 · 800 m = 1600 m",
                       "2)  Sākuma un beigu punkts sakrīt",
                       "3)  d = 0"],
             atbilde="s = 1,6·10³ m ;   d = 0",
             piezime="Ceļš 1,6 km, bet pārvietojums nulle — skolēns "
                     "atgriezies tur, kur sāka."),
        dict(nr=2, virsraksts="Pusaplis",
             teksts="Skrējējs noskrien pa pusapli, kura rādiuss ir 50 m.\n"
                    "Aprēķini ceļu un pārvietojumu! (π ≈ 3,14)",
             dots=["R = 50 m", "pusaplis"],
             jaaprekina=["s = ?", "d = ?"],
             formulas=["s = π · R", "d = 2 · R"],
             aprekins=["1)  s = 3,14 · 50 m = 157 m",
                       "2)  d = 2 · 50 m = 100 m",
                       "3)  s / d = 157 : 100 = 1,57"],
             atbilde="s = 157 m ;   d = 100 m",
             piezime="Ceļš ir π/2 ≈ 1,57 reizes garāks par pārvietojumu."),
        dict(nr=3, virsraksts="Kustība pa taisnstūri",
             teksts="Ķermenis pārvietojas 60 m uz austrumiem, tad 80 m uz "
                    "ziemeļiem.\nAprēķini ceļu un pārvietojumu!",
             dots=["s₁ = 60 m", "s₂ = 80 m", "vektori ⊥"],
             jaaprekina=["s = ?", "d = ?"],
             formulas=["s = s₁ + s₂", "d = √(s₁² + s₂²)"],
             aprekins=["1)  s = 60 + 80 = 140 m",
                       "2)  d = √(3600 + 6400) = √10 000",
                       "3)  d = 100 m"],
             atbilde="s = 140 m ;   d = 100 m",
             piezime="Pa taisno būtu par 40 m īsāk nekā pa abām malām."),
        dict(nr=4, virsraksts="Vidējais ātrums pa apli",
             teksts="Sportists 100 s laikā noskrien vienu pilnu apli, kura "
                    "rādiuss ir 40 m.\nAprēķini vidējo ātrumu pa ceļu un pēc "
                    "pārvietojuma!",
             dots=["R = 40 m", "t = 100 s", "pilns aplis"],
             jaaprekina=["υ(ceļš) = ?", "υ(pārv.) = ?"],
             formulas=["s = 2πR", "υ = s / t", "d = 0"],
             aprekins=["1)  s = 2 · 3,14 · 40 = 251 m",
                       "2)  υ(ceļš) = 251 : 100 = 2,5 m/s",
                       "3)  d = 0 → υ(pārv.) = 0 : 100 = 0"],
             atbilde="υ(ceļš) = 2,5 m/s ;   υ(pārv.) = 0",
             piezime="Ikdienā ar “ātrumu” domā ātrumu pa ceļu — to arī rāda "
                     "spidometrs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Trajektorija ir līnija, pa kuru ķermenis pārvietojas.",
            "Ceļš ir trajektorijas garums; pārvietojums — vektors no sākuma "
            "uz beigām.",
            "Pārvietojums vienmēr ir mazāks vai vienāds ar ceļu.",
            "Kustība ir relatīva — vienmēr jānorāda atskaites sistēma.",
        ],
        majasdarbs=[
            "Aplis R = 25 m. Aprēķini ceļu un pārvietojumu pusaplim.",
            "Iet 120 m uz ziemeļiem, tad 50 m atpakaļ uz dienvidiem. "
            "Aprēķini s un d.",
            "Paskaidro ar piemēru, kāpēc kustība ir relatīva.",
        ],
        pasvertejums=["Protu skaidrot trajektoriju",
                      "Protu aprēķināt ceļu",
                      "Protu aprēķināt pārvietojumu",
                      "Protu pamatot kustības relativitāti"],
        nakama="Nākamā stunda: vienmērīga kustība."),
),

dict(
    nr="7.3", virsraksts="Vienmērīga kustība",
    jautajums="Kā aprakstīt vienmērīgu kustību?",
    apaksraksts="υ = s/t · x = x₀ + υt · Kustības vienādojums",
    merkis="Iemācīties lietot vienmērīgas kustības sakarības un kustības "
           "vienādojumu, lai aprēķinātu ceļu, ātrumu, laiku un koordinātu.",
    protu=["lietot υ = s/t visos trīs virzienos;",
           "pārvērst km/h un m/s;",
           "lietot kustības vienādojumu x = x₀ + υt;",
           "aprēķināt divu ķermeņu satikšanās laiku."],
    atkartojums="1.3. stundā jau rēķinājām ar υ = s/t un pārvērtām km/h uz "
                "m/s. Šodien pievienosim koordinātu un kustības vienādojumu.",
    uzdevumu_apraksts="Ceļš, ātrums, laiks un satikšanās uzdevumi",
    teorija=[
        ("Vienmērīgas kustības sakarības", [
            ("formula", "PAMATSAKARĪBA",
             "υ = s / t        s = υ · t        t = s / υ",
             "Vienmērīgā kustībā ātrums nemainās: vienādos laika sprīžos "
             "ķermenis veic vienādus ceļus.", GOLD),
            ("divi",
             ("MĒRVIENĪBU PĀRVEIDE", BLUE,
              ["km/h → m/s:  dala ar 3,6",
               "m/s → km/h:  reizina ar 3,6",
               "72 km/h = 20 m/s",
               "10 m/s = 36 km/h"]),
             ("KUSTĪBAS VIENĀDOJUMS", GREEN,
              ["x = x₀ + υ · t",
               "x₀ — sākuma koordināta,",
               "υ — ātruma projekcija (var būt negatīva),",
               "x — koordināta laikā t."])),
        ]),
        ("Kustības vienādojums praksē", [
            ("panelis", "ĀTRUMA ZĪME",
             ["Ja ķermenis kustas ass POZITĪVAJĀ virzienā, υ > 0; ja pretējā "
              "— υ < 0.",
              "Piemēram, x = 100 − 20t nozīmē: sākuma koordināta 100 m, "
              "ķermenis kustas ar 20 m/s pretēji ass virzienam."], NAVY),
            ("panelis", "SATIKŠANĀS UZDEVUMI",
             ["Divi ķermeņi satiekas, kad to koordinātas sakrīt: x₁ = x₂.",
              "Uzraksti abus vienādojumus, pielīdzini tos un atrisini "
              "attiecībā pret t. Tad ievieto t vienā vienādojumā, lai "
              "atrastu satikšanās vietu."], GREEN),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vilciena ceļš",
             teksts="Vilciens brauc ar nemainīgu ātrumu 90 km/h.\n"
                    "Cik lielu ceļu tas veiks 40 minūtēs? Izsaki "
                    "kilometros!",
             dots=["υ = 90 km/h", "t = 40 min"],
             jaaprekina=["s = ?  (km)"],
             formulas=["υ = s / t", "s = υ · t"],
             aprekins=["1)  t = 40 min = 40/60 h = 0,667 h",
                       "2)  s = 90 km/h · 0,667 h",
                       "3)  s = 60 km"],
             atbilde="s = 60 km",
             piezime="Ja ātrums ir km/h, laiks jāizsaka stundās — tad ceļš "
                     "iznāk kilometros."),
        dict(nr=2, virsraksts="Skaņas ātrums",
             teksts="Zibens spēriens ieraudzīts, un pērkons dzirdams pēc "
                    "6,0 s. Skaņas ātrums gaisā 340 m/s.\n"
                    "Cik tālu atrodas zibens?",
             dots=["υ = 340 m/s", "t = 6,0 s"],
             jaaprekina=["s = ?  (km)"],
             formulas=["s = υ · t"],
             aprekins=["1)  s = 340 m/s · 6,0 s",
                       "2)  s = 2040 m",
                       "3)  s = 2,0 km"],
             atbilde="s ≈ 2,0·10³ m = 2,0 km",
             piezime="Gaismas ceļošanas laiku neņem vērā — tā ātrums ir "
                     "gandrīz miljons reižu lielāks."),
        dict(nr=3, virsraksts="Kustības vienādojums",
             teksts="Ķermeņa kustību apraksta vienādojums x = 20 + 15t "
                    "(metros un sekundēs).\n"
                    "Nosaki sākuma koordinātu, ātrumu un koordinātu pēc "
                    "8,0 s!",
             dots=["x = 20 + 15t", "t = 8,0 s"],
             jaaprekina=["x₀ = ?", "υ = ?", "x = ?"],
             formulas=["x = x₀ + υ · t"],
             aprekins=["1)  Salīdzinot: x₀ = 20 m ;  υ = 15 m/s",
                       "2)  x = 20 + 15 · 8,0",
                       "3)  x = 20 + 120 = 140 m"],
             atbilde="x₀ = 20 m ;  υ = 15 m/s ;  x = 140 m",
             piezime="Vienādojumā skaitlis pie t vienmēr ir ātrums."),
        dict(nr=4, virsraksts="Divu automašīnu satikšanās",
             teksts="Divas automašīnas brauc viena otrai pretī no punktiem, "
                    "kas atrodas 300 km attālumā. Ātrumi 80 km/h un "
                    "70 km/h.\nPēc cik ilga laika tās satiksies?",
             dots=["s = 300 km", "υ₁ = 80 km/h", "υ₂ = 70 km/h"],
             jaaprekina=["t = ?"],
             formulas=["υ(tuvošanās) = υ₁ + υ₂", "t = s / υ"],
             aprekins=["1)  υ = 80 + 70 = 150 km/h",
                       "2)  t = 300 km : 150 km/h",
                       "3)  t = 2,0 h"],
             atbilde="t = 2,0 h",
             piezime="Braucot pretī, ātrumus saskaita — attālums sarūk ar "
                     "abu ātrumu summu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vienmērīgā kustībā ātrums nemainās: υ = s/t.",
            "km/h → m/s dala ar 3,6; m/s → km/h reizina ar 3,6.",
            "Kustības vienādojums x = x₀ + υt; ātrums var būt negatīvs.",
            "Ķermeņi satiekas, kad x₁ = x₂; braucot pretī, ātrumus saskaita.",
        ],
        majasdarbs=[
            "υ = 54 km/h, t = 25 min. Aprēķini ceļu km.",
            "x = 80 − 12t. Nosaki x₀, υ un x pie t = 5 s.",
            "Divi riteņbraucēji 60 km attālumā brauc pretī ar 15 un 20 km/h. "
            "Kad satiksies?",
        ],
        pasvertejums=["Protu lietot υ = s/t",
                      "Protu pārvērst km/h un m/s",
                      "Protu lasīt kustības vienādojumu",
                      "Protu risināt satikšanās uzdevumu"],
        nakama="Nākamā stunda: kustības grafiki."),
),

dict(
    nr="7.4", virsraksts="Kustības grafiki",
    jautajums="Ko stāsta grafika slīpums?",
    apaksraksts="x(t) grafiks · υ(t) grafiks · Slīpums · Laukums",
    merkis="Iemācīties nolasīt x(t) un υ(t) grafikus, noteikt ātrumu pēc "
           "slīpuma un ceļu pēc laukuma zem grafika.",
    protu=["nolasīt vērtības no x(t) un υ(t) grafika;",
           "noteikt ātrumu pēc x(t) grafika slīpuma;",
           "noteikt ceļu pēc laukuma zem υ(t) grafika;",
           "atpazīt miera stāvokli un kustību pretējā virzienā."],
    atkartojums="1.6. stundā mācījāmies, ka grafika slīpums ir fizikāls "
                "lielums. Kustībā x(t) grafika slīpums ir ātrums.",
    uzdevumu_apraksts="Ātrums un ceļš no grafikiem",
    teorija=[
        ("Divi kustības grafiki", [
            ("divi",
             ("x(t) — KOORDINĀTA NO LAIKA", BLUE,
              ["Slīpums = ātrums:  υ = Δx / Δt",
               "Stāvāka līnija → lielāks ātrums.",
               "Horizontāla līnija → ķermenis stāv.",
               "Lejupejoša līnija → kustība atpakaļ."]),
             ("υ(t) — ĀTRUMS NO LAIKA", GREEN,
              ["Laukums zem grafika = ceļš.",
               "Horizontāla līnija → vienmērīga kustība.",
               "Augšupejoša līnija → paātrināta kustība.",
               "Slīpums = paātrinājums."])),
            ("formula", "DIVAS GALVENĀS SAKARĪBAS",
             "υ = Δx / Δt   (x(t) slīpums)        s = υ · t   (laukums zem "
             "υ(t))",
             "Vienmēr vispirms nosaki, KURŠ grafiks dots — x(t) vai υ(t). "
             "No tā atkarīgs viss risinājums.", GOLD),
        ]),
        ("Kā lasa grafiku", [
            ("tabula",
             ["Ko redz grafikā", "x(t) nozīme", "υ(t) nozīme"],
             [["Horizontāla līnija", "ķermenis stāv (υ = 0)",
               "vienmērīga kustība"],
              ["Augšupejoša taisne", "kustība uz priekšu",
               "vienmērīgi paātrināta"],
              ["Lejupejoša taisne", "kustība atpakaļ", "bremzēšana"],
              ["Stāvāka līnija", "lielāks ātrums", "lielāks paātrinājums"]],
             [3.83, 4.20, 4.20]),
            ("panelis", "BIEŽĀKĀ KĻŪDA",
             ["Horizontāla līnija x(t) grafikā nozīmē, ka ķermenis STĀV, bet "
              "horizontāla līnija υ(t) grafikā — ka tas brauc ar NEMAINĪGU "
              "ātrumu. Vienmēr pārbaudi asu apzīmējumus!"], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātrums no x(t) grafika",
             teksts="x(t) grafikā pie t = 2,0 s koordināta ir 10 m, bet pie "
                    "t = 8,0 s — 40 m.\n"
                    "Aprēķini ķermeņa ātrumu!",
             dots=["t₁ = 2,0 s ;  x₁ = 10 m", "t₂ = 8,0 s ;  x₂ = 40 m"],
             jaaprekina=["υ = ?"],
             formulas=["υ = Δx / Δt"],
             aprekins=["1)  Δx = 40 − 10 = 30 m",
                       "2)  Δt = 8,0 − 2,0 = 6,0 s",
                       "3)  υ = 30 : 6,0 = 5,0 m/s"],
             atbilde="υ = 5,0 m/s",
             piezime="Taisnes slīpums x(t) grafikā vienmēr ir ātrums."),
        dict(nr=2, virsraksts="Ceļš no υ(t) grafika",
             teksts="υ(t) grafikā ātrums ir nemainīgs 12 m/s no t = 0 līdz "
                    "t = 15 s.\nAprēķini veikto ceļu! Kāds lielums grafikā "
                    "tam atbilst?",
             dots=["υ = 12 m/s", "t = 15 s"],
             jaaprekina=["s = ?"],
             formulas=["s = υ · t  (laukums zem grafika)"],
             aprekins=["1)  s = 12 m/s · 15 s",
                       "2)  s = 180 m"],
             atbilde="s = 180 m — taisnstūra laukums zem υ(t) grafika",
             piezime="Zem υ(t) grafika esošais laukums vienmēr ir ceļš."),
        dict(nr=3, virsraksts="Kustība ar apstāšanos",
             teksts="Ķermenis 10 s brauc ar 6,0 m/s, tad 5,0 s stāv, tad "
                    "vēl 10 s brauc ar 4,0 m/s.\n"
                    "Aprēķini kopējo ceļu un vidējo ātrumu!",
             dots=["υ₁ = 6,0 m/s ;  t₁ = 10 s", "t₂ = 5,0 s (stāv)",
                   "υ₃ = 4,0 m/s ;  t₃ = 10 s"],
             jaaprekina=["s = ?", "υ(vid) = ?"],
             formulas=["s = υ·t", "υ(vid) = s(kop) / t(kop)"],
             aprekins=["1)  s₁ = 6,0 · 10 = 60 m ;  s₂ = 0 ;  "
                       "s₃ = 4,0 · 10 = 40 m",
                       "2)  s = 60 + 0 + 40 = 100 m",
                       "3)  t = 10 + 5,0 + 10 = 25 s",
                       "4)  υ(vid) = 100 : 25 = 4,0 m/s"],
             atbilde="s = 100 m ;   υ(vid) = 4,0 m/s",
             piezime="Vidējo ātrumu rēķina kā VISU ceļu dalītu ar VISU laiku "
                     "— arī apstāšanās laiks jāieskaita."),
        dict(nr=4, virsraksts="Divi ķermeņi vienā grafikā",
             teksts="Pirmā ķermeņa x(t) grafiks: x = 0 + 8t. Otrā: "
                    "x = 60 − 4t.\n"
                    "Aprēķini, kurā laika momentā un kurā koordinātā tie "
                    "satiksies!",
             dots=["x₁ = 8t", "x₂ = 60 − 4t"],
             jaaprekina=["t = ?", "x = ?"],
             formulas=["Satiekas, kad x₁ = x₂"],
             aprekins=["1)  8t = 60 − 4t",
                       "2)  12t = 60  →  t = 5,0 s",
                       "3)  x = 8 · 5,0 = 40 m"],
             atbilde="t = 5,0 s ;   x = 40 m",
             piezime="Grafikā tas ir punkts, kurā abas taisnes krustojas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "x(t) grafika slīpums ir ātrums: υ = Δx/Δt.",
            "Laukums zem υ(t) grafika ir veiktais ceļš.",
            "Horizontāla līnija x(t) grafikā — ķermenis stāv.",
            "Vidējais ātrums = viss ceļš dalīts ar visu laiku.",
        ],
        majasdarbs=[
            "x(t): pie t = 1 s x = 4 m, pie t = 6 s x = 24 m. Aprēķini υ.",
            "υ(t): υ = 9 m/s no 0 līdz 20 s. Aprēķini ceļu.",
            "x₁ = 10 + 5t un x₂ = 70 − 5t. Kad un kur satiksies?",
        ],
        pasvertejums=["Protu nolasīt grafikus",
                      "Protu aprēķināt ātrumu pēc slīpuma",
                      "Protu aprēķināt ceļu pēc laukuma",
                      "Protu atrast satikšanās punktu"],
        nakama="Nākamā stunda: paātrinājums."),
),

dict(
    nr="7.5", virsraksts="Paātrinājums",
    jautajums="Kā mainās ātrums?",
    apaksraksts="a = Δυ/Δt · υ = υ₀ + at · Paātrināšanās un bremzēšana",
    merkis="Iemācīties aprēķināt paātrinājumu un ātrumu vienmērīgi "
           "paātrinātā kustībā no datiem, tabulas vai grafika.",
    protu=["skaidrot, kas ir paātrinājums, un tā mērvienību;",
           "lietot a = Δυ/Δt un υ = υ₀ + at;",
           "atšķirt paātrināšanos no bremzēšanas pēc zīmes;",
           "noteikt paātrinājumu no υ(t) grafika slīpuma."],
    atkartojums="7.3.–7.4. stundā aplūkojām kustību ar NEMAINĪGU ātrumu. "
                "Reālā kustība parasti ir citāda — ātrums mainās.",
    uzdevumu_apraksts="Paātrinājums, ātrums un bremzēšana",
    teorija=[
        ("Kas ir paātrinājums", [
            ("formula", "PAĀTRINĀJUMS",
             "a = Δυ / Δt = (υ − υ₀) / t        υ = υ₀ + a · t",
             "a — paātrinājums [m/s²]; rāda, par cik mainās ātrums katrā "
             "sekundē. a = 3 m/s² nozīmē: katrā sekundē ātrums aug par "
             "3 m/s.", GOLD),
            ("kartitas", [
                ("PAĀTRINĀŠANĀS", GREEN,
                 ["Ātrums aug: υ > υ₀",
                  "a > 0 (ja υ vērsts pozitīvi)",
                  "a un υ vienā virzienā."]),
                ("BREMZĒŠANA", RED,
                 ["Ātrums samazinās: υ < υ₀",
                  "a < 0",
                  "a un υ pretējos virzienos."]),
                ("VIENMĒRĪGA KUSTĪBA", BLUE,
                 ["Ātrums nemainās.",
                  "a = 0",
                  "Tā ir 7.3. stundas kustība."]),
            ]),
        ]),
        ("Paātrinājums grafikā un praksē", [
            ("tabula",
             ["Situācija", "υ₀", "υ", "a"],
             [["Automašīna sāk braukt", "0", "20 m/s", "pozitīvs"],
              ["Automašīna bremzē līdz apstāšanās", "20 m/s", "0",
               "negatīvs"],
              ["Brīvi krītošs ķermenis", "0", "aug", "9,81 m/s²"],
              ["Vienmērīga kustība", "10 m/s", "10 m/s", "0"]],
             [5.03, 2.40, 2.40, 2.40]),
            ("panelis", "υ(t) GRAFIKS",
             ["Vienmērīgi paātrinātā kustībā υ(t) grafiks ir TAISNE. Tās "
              "slīpums ir paātrinājums: a = Δυ/Δt.",
              "Augšupejoša taisne — paātrināšanās; lejupejoša — bremzēšana; "
              "horizontāla — vienmērīga kustība."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Automašīnas paātrinājums",
             teksts="Automašīna 8,0 s laikā palielina ātrumu no 0 līdz "
                    "72 km/h.\nAprēķini paātrinājumu!",
             dots=["υ₀ = 0", "υ = 72 km/h", "t = 8,0 s"],
             jaaprekina=["a = ?"],
             formulas=["a = (υ − υ₀) / t"],
             aprekins=["1)  υ = 72 km/h = 72 : 3,6 = 20 m/s",
                       "2)  a = (20 − 0) : 8,0",
                       "3)  a = 2,5 m/s²"],
             atbilde="a = 2,5 m/s²",
             piezime="Katrā sekundē ātrums palielinās par 2,5 m/s."),
        dict(nr=2, virsraksts="Ātrums pēc dotā laika",
             teksts="Ķermenis sāk kustību ar ātrumu 4,0 m/s un paātrinās ar "
                    "a = 1,5 m/s².\nAprēķini ātrumu pēc 10 s!",
             dots=["υ₀ = 4,0 m/s", "a = 1,5 m/s²", "t = 10 s"],
             jaaprekina=["υ = ?"],
             formulas=["υ = υ₀ + a · t"],
             aprekins=["1)  υ = 4,0 + 1,5 · 10",
                       "2)  υ = 4,0 + 15",
                       "3)  υ = 19 m/s"],
             atbilde="υ = 19 m/s ≈ 68 km/h",
             piezime="Vienmēr vispirms reizina a ar t, tikai tad pieskaita "
                     "υ₀."),
        dict(nr=3, virsraksts="Bremzēšana",
             teksts="Automašīna, braucot ar 90 km/h, apstājas 5,0 s laikā.\n"
                    "Aprēķini paātrinājumu un paskaidro tā zīmi!",
             dots=["υ₀ = 90 km/h", "υ = 0", "t = 5,0 s"],
             jaaprekina=["a = ?"],
             formulas=["a = (υ − υ₀) / t"],
             aprekins=["1)  υ₀ = 90 : 3,6 = 25 m/s",
                       "2)  a = (0 − 25) : 5,0",
                       "3)  a = −5,0 m/s²"],
             atbilde="a = −5,0 m/s² — mīnuss norāda bremzēšanu",
             piezime="Paātrinājums vērsts pretēji kustībai, tāpēc tas ir "
                     "negatīvs."),
        dict(nr=4, virsraksts="Paātrinājums no grafika",
             teksts="υ(t) grafikā pie t = 2,0 s ātrums ir 6,0 m/s, bet pie "
                    "t = 10,0 s — 30,0 m/s.\n"
                    "Aprēķini paātrinājumu un ātrumu pie t = 15 s!",
             dots=["t₁ = 2,0 s ;  υ₁ = 6,0 m/s",
                   "t₂ = 10,0 s ;  υ₂ = 30,0 m/s"],
             jaaprekina=["a = ?", "υ(15 s) = ?"],
             formulas=["a = Δυ / Δt", "υ = υ₀ + a·t"],
             aprekins=["1)  Δυ = 30,0 − 6,0 = 24,0 m/s",
                       "2)  Δt = 10,0 − 2,0 = 8,0 s",
                       "3)  a = 24,0 : 8,0 = 3,0 m/s²",
                       "4)  υ = 6,0 + 3,0 · 13 = 45 m/s"],
             atbilde="a = 3,0 m/s² ;   υ(15 s) = 45 m/s",
             piezime="No t = 2 s līdz t = 15 s pagāja 13 s — tāpēc "
                     "reizinām ar 13, nevis ar 15."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Paātrinājums a = Δυ/Δt rāda, par cik mainās ātrums sekundē.",
            "υ = υ₀ + at — ātrums jebkurā laika momentā.",
            "Bremzējot a ir negatīvs; vienmērīgā kustībā a = 0.",
            "υ(t) grafika slīpums ir paātrinājums.",
        ],
        majasdarbs=[
            "Ātrums no 0 līdz 54 km/h 6,0 s laikā. Aprēķini a.",
            "υ₀ = 8 m/s, a = 2 m/s². Aprēķini υ pēc 12 s.",
            "Vilciens no 20 m/s apstājas 40 s laikā. Aprēķini a.",
        ],
        pasvertejums=["Protu skaidrot paātrinājumu",
                      "Protu lietot a = Δυ/Δt",
                      "Protu lietot υ = υ₀ + at",
                      "Protu atpazīt bremzēšanu"],
        nakama="Nākamā stunda: kustības vienādojums."),
),

dict(
    nr="7.6", virsraksts="Kustības vienādojums",
    jautajums="Kur ķermenis būs pēc piecām sekundēm?",
    apaksraksts="x = x₀ + υ₀t + at²/2 · Ceļš paātrinātā kustībā",
    merkis="Iemācīties lietot vienmērīgi paātrinātas kustības vienādojumu, "
           "lai prognozētu ķermeņa koordinātu un veikto ceļu.",
    protu=["lietot x = x₀ + υ₀t + at²/2;",
           "aprēķināt ceļu paātrinātā kustībā;",
           "nolasīt vienādojumā x₀, υ₀ un a;",
           "apvienot kustības vienādojumu ar υ = υ₀ + at."],
    atkartojums="7.5. stundā iemācījāmies aprēķināt ātrumu υ = υ₀ + at. "
                "Šodien noskaidrosim, kur ķermenis šajā laikā nonāks.",
    uzdevumu_apraksts="Koordināta un ceļš vienmērīgi paātrinātā kustībā",
    teorija=[
        ("Kustības vienādojums", [
            ("formula", "VIENMĒRĪGI PAĀTRINĀTA KUSTĪBA",
             "x = x₀ + υ₀ · t + a · t² / 2        υ = υ₀ + a · t",
             "x₀ — sākuma koordināta, υ₀ — sākuma ātrums, a — paātrinājums. "
             "Ja kustība sākas no miera un no koordinātu sākuma, "
             "s = at²/2.", GOLD),
            ("divi",
             ("KĀ LASA VIENĀDOJUMU", BLUE,
              ["x = 10 + 4t + 1,5t²",
               "x₀ = 10 m",
               "υ₀ = 4 m/s",
               "at²/2 = 1,5t²  →  a = 3 m/s²"]),
             ("UZMANIES", RED,
              ["Pie t² stāv a/2, nevis a!",
               "Ja vienādojumā ir 1,5t², tad a = 3 m/s².",
               "Bieža kļūda: uzskatīt, ka a = 1,5 m/s²."])),
        ]),
        ("Kā risina uzdevumus", [
            ("tabula",
             ["Kas dots", "Kas jāatrod", "Formula"],
             [["υ₀, a, t", "ātrums υ", "υ = υ₀ + at"],
              ["υ₀, a, t", "ceļš s", "s = υ₀t + at²/2"],
              ["υ₀ = 0, a, t", "ceļš s", "s = at²/2"],
              ["υ₀, υ, t", "vidējais ātrums", "υ(vid) = (υ₀ + υ)/2"],
              ["υ(vid), t", "ceļš s", "s = υ(vid) · t"]],
             [3.63, 3.60, 5.00]),
            ("panelis", "DIVI CEĻI UZ TO PAŠU ATBILDI",
             ["Ceļu var atrast divējādi: pēc formulas s = υ₀t + at²/2 vai "
              "caur vidējo ātrumu s = (υ₀ + υ)/2 · t.",
              "Abi dod vienādu rezultātu — otrais bieži ir ātrāks, ja "
              "gala ātrums jau ir zināms."], GREEN),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ceļš no miera stāvokļa",
             teksts="Automašīna sāk kustību no miera ar paātrinājumu "
                    "2,0 m/s².\nCik lielu ceļu tā veiks 10 s laikā?",
             dots=["υ₀ = 0", "a = 2,0 m/s²", "t = 10 s"],
             jaaprekina=["s = ?"],
             formulas=["s = υ₀t + at²/2", "ja υ₀ = 0:  s = at²/2"],
             aprekins=["1)  t² = 10² = 100 s²",
                       "2)  s = 2,0 · 100 : 2",
                       "3)  s = 100 m"],
             atbilde="s = 100 m",
             piezime="Ceļš aug ar laika kvadrātu — divreiz ilgāk nozīmē "
                     "četrreiz tālāk."),
        dict(nr=2, virsraksts="Kustība ar sākuma ātrumu",
             teksts="Ķermenis kustas ar sākuma ātrumu 5,0 m/s un "
                    "paātrinājumu 3,0 m/s².\n"
                    "Aprēķini ceļu un ātrumu pēc 6,0 s!",
             dots=["υ₀ = 5,0 m/s", "a = 3,0 m/s²", "t = 6,0 s"],
             jaaprekina=["s = ?", "υ = ?"],
             formulas=["s = υ₀t + at²/2", "υ = υ₀ + at"],
             aprekins=["1)  s = 5,0 · 6,0 + 3,0 · 36 : 2",
                       "2)  s = 30 + 54 = 84 m",
                       "3)  υ = 5,0 + 3,0 · 6,0 = 23 m/s"],
             atbilde="s = 84 m ;   υ = 23 m/s",
             piezime="Pārbaude: υ(vid) = (5+23)/2 = 14 m/s; "
                     "s = 14 · 6 = 84 m ✔"),
        dict(nr=3, virsraksts="Vienādojuma nolasīšana",
             teksts="Kustību apraksta x = 12 + 6t + 2t² (metros un "
                    "sekundēs).\n"
                    "Nosaki x₀, υ₀ un a un aprēķini koordinātu pie t = 4 s!",
             dots=["x = 12 + 6t + 2t²", "t = 4,0 s"],
             jaaprekina=["x₀, υ₀, a = ?", "x = ?"],
             formulas=["x = x₀ + υ₀t + at²/2", "a/2 = 2  →  a = 4"],
             aprekins=["1)  x₀ = 12 m ;  υ₀ = 6 m/s",
                       "2)  a/2 = 2  →  a = 4,0 m/s²",
                       "3)  x = 12 + 6·4 + 2·16 = 12 + 24 + 32",
                       "4)  x = 68 m"],
             atbilde="x₀ = 12 m ;  υ₀ = 6 m/s ;  a = 4,0 m/s² ;  x = 68 m",
             piezime="Koeficients pie t² ir a/2 — tāpēc a ir divreiz "
                     "lielāks."),
        dict(nr=4, virsraksts="Skrejceļa garums",
             teksts="Lidmašīna paceļas, sasniedzot 60 m/s. Tā sāk no miera "
                    "un paātrinās ar 3,0 m/s².\n"
                    "Aprēķini pacelšanās laiku un nepieciešamo skrejceļa "
                    "garumu!",
             dots=["υ₀ = 0", "υ = 60 m/s", "a = 3,0 m/s²"],
             jaaprekina=["t = ?", "s = ?"],
             formulas=["υ = υ₀ + at  →  t = υ/a", "s = at²/2"],
             aprekins=["1)  t = 60 : 3,0 = 20 s",
                       "2)  s = 3,0 · 20² : 2",
                       "3)  s = 3,0 · 400 : 2 = 600 m"],
             atbilde="t = 20 s ;   s = 6,0·10² m",
             piezime="Praksē skrejceļš ir garāks — vajadzīga rezerve "
                     "pārtrauktas pacelšanās gadījumam."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "x = x₀ + υ₀t + at²/2 — vienmērīgi paātrinātas kustības "
            "vienādojums.",
            "Ja υ₀ = 0, tad s = at²/2; ceļš aug ar laika kvadrātu.",
            "Vienādojumā pie t² stāv a/2, nevis a.",
            "Ceļu var atrast arī caur vidējo ātrumu: s = (υ₀ + υ)/2 · t.",
        ],
        majasdarbs=[
            "υ₀ = 0, a = 4 m/s², t = 5 s. Aprēķini s un υ.",
            "x = 5 + 2t + 3t². Nosaki x₀, υ₀ un a.",
            "Vilciens no miera sasniedz 30 m/s ar a = 0,5 m/s². Aprēķini t "
            "un s.",
        ],
        pasvertejums=["Protu lietot kustības vienādojumu",
                      "Protu aprēķināt ceļu un ātrumu",
                      "Protu nolasīt vienādojuma koeficientus",
                      "Protu apvienot divas formulas"],
        nakama="Nākamā stunda: brīvā krišana."),
),

dict(
    nr="7.7", virsraksts="Brīvā krišana",
    jautajums="Vai smagāks ķermenis krīt ātrāk?",
    apaksraksts="g = 9,81 m/s² · Krišanas laiks un ātrums · Gaisa pretestība",
    merkis="Iemācīties skaidrot brīvo krišanu un aprēķināt krišanas laiku, "
           "augstumu un ātrumu, lietojot g = 9,81 m/s².",
    protu=["skaidrot, kas ir brīvā krišana;",
           "pamatot, kāpēc vakuumā visi ķermeņi krīt vienādi;",
           "aprēķināt krišanas laiku, augstumu un ātrumu;",
           "izvērtēt gaisa pretestības ietekmi."],
    atkartojums="7.6. stundā mācījāmies s = at²/2. Brīvā krišana ir tieši "
                "šāda kustība, kur a = g = 9,81 m/s².",
    uzdevumu_apraksts="Krišanas augstums, laiks un ātrums",
    teorija=[
        ("Brīvā krišana", [
            ("panelis", "KAS IR BRĪVĀ KRIŠANA",
             ["Brīvā krišana ir kustība tikai gravitācijas spēka ietekmē, "
              "neņemot vērā gaisa pretestību.",
              "Vakuumā spalva un lodīte krīt VIENĀDI ātri — to pierādīja "
              "eksperimenti uz Mēness. Zemes tuvumā visiem ķermeņiem "
              "g = 9,81 m/s² (aprēķinos bieži 9,8 vai 10 m/s²)."], NAVY),
            ("formula", "BRĪVĀS KRIŠANAS FORMULAS",
             "h = g·t² / 2        υ = g·t        t = √(2h/g)",
             "Krītot no miera. Formulas ir tās pašas, kas 7.6. stundā, "
             "tikai a aizstāts ar g.", GOLD),
        ]),
        ("Kāpēc praksē krīt dažādi", [
            ("divi",
             ("VAKUUMĀ", BLUE,
              ["Darbojas tikai gravitācija.",
               "Visi ķermeņi krīt ar vienādu paātrinājumu.",
               "Masai nav nozīmes.",
               "Spalva un āmurs nokrīt vienlaikus."]),
             ("GAISĀ", RED,
              ["Papildus darbojas gaisa pretestība.",
               "Tā atkarīga no formas un ātruma, ne no masas.",
               "Viegli un plati ķermeņi bremzējas vairāk.",
               "Tāpēc papīra lapa krīt lēnāk par akmeni."])),
            ("panelis", "ROBEŽĀTRUMS",
             ["Krītot ātrums aug, un līdz ar to aug gaisa pretestība. Kad tā "
              "kļūst vienāda ar smaguma spēku, ātrums vairs nemainās — tas "
              "ir robežātrums.",
              "Izpletņlēcējam bez izpletņa tas ir ~55 m/s, ar izplestu "
              "izpletni — ~5 m/s."], GREEN),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Krišanas augstums",
             teksts="Ķermenis brīvi krīt 3,0 s. g = 9,81 m/s².\n"
                    "Aprēķini, no kāda augstuma tas krita!",
             dots=["t = 3,0 s", "g = 9,81 m/s²", "υ₀ = 0"],
             jaaprekina=["h = ?"],
             formulas=["h = g · t² / 2"],
             aprekins=["1)  t² = 3,0² = 9,0 s²",
                       "2)  h = 9,81 · 9,0 : 2",
                       "3)  h = 44,1 m"],
             atbilde="h ≈ 44 m",
             piezime="Tas ir apmēram 15 stāvu ēkas augstums."),
        dict(nr=2, virsraksts="Krišanas ātrums",
             teksts="Akmens brīvi krīt no 20 m augsta tilta. "
                    "g = 9,81 m/s².\nAprēķini krišanas laiku un ātrumu "
                    "nokrišanas brīdī!",
             dots=["h = 20 m", "g = 9,81 m/s²", "υ₀ = 0"],
             jaaprekina=["t = ?", "υ = ?"],
             formulas=["h = gt²/2  →  t = √(2h/g)", "υ = g · t"],
             aprekins=["1)  t = √(2 · 20 : 9,81) = √4,08",
                       "2)  t = 2,0 s",
                       "3)  υ = 9,81 · 2,0 = 19,6 m/s"],
             atbilde="t ≈ 2,0 s ;   υ ≈ 20 m/s = 71 km/h",
             piezime="Krītot tikai no 20 m, ātrums jau ir kā automašīnai "
                     "pilsētā."),
        dict(nr=3, virsraksts="Divi ķermeņi",
             teksts="No vienāda augstuma vienlaikus krīt 2,0 kg un 8,0 kg "
                    "smaga lodīte. Gaisa pretestību neņem vērā.\n"
                    "Kura nokritīs pirmā? Pamato ar aprēķinu, ja h = 45 m!",
             dots=["m₁ = 2,0 kg ;  m₂ = 8,0 kg", "h = 45 m",
                   "g = 9,81 m/s²"],
             jaaprekina=["t₁ = ?", "t₂ = ?"],
             formulas=["t = √(2h/g)  — masa formulā neietilpst"],
             aprekins=["1)  t = √(2 · 45 : 9,81) = √9,17",
                       "2)  t = 3,03 s",
                       "3)  Masa formulā neparādās → t₁ = t₂"],
             atbilde="Abas nokrīt vienlaikus: t ≈ 3,0 s",
             piezime="Brīvās krišanas laiks nav atkarīgs no masas — tikai no "
                     "augstuma."),
        dict(nr=4, virsraksts="Cik dziļa ir aka?",
             teksts="Akmenim, iemestam akā, līdz ūdenim krīt 1,6 s.\n"
                    "Aprēķini akas dziļumu! (g = 9,81 m/s²; skaņas "
                    "ceļošanas laiku neņem vērā)",
             dots=["t = 1,6 s", "g = 9,81 m/s²"],
             jaaprekina=["h = ?"],
             formulas=["h = g · t² / 2"],
             aprekins=["1)  t² = 1,6² = 2,56 s²",
                       "2)  h = 9,81 · 2,56 : 2",
                       "3)  h = 12,6 m"],
             atbilde="h ≈ 13 m",
             piezime="Šo metodi tiešām izmanto — tikai precīzos mērījumos "
                     "ņem vērā arī skaņas atgriešanās laiku."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Brīvā krišana notiek tikai gravitācijas ietekmē; "
            "g = 9,81 m/s².",
            "h = gt²/2 ;  υ = gt ;  t = √(2h/g).",
            "Vakuumā visi ķermeņi krīt vienādi — masai nav nozīmes.",
            "Gaisā krišanu ietekmē pretestība, kas atkarīga no formas un "
            "ātruma.",
        ],
        majasdarbs=[
            "t = 2,5 s. Aprēķini krišanas augstumu un gala ātrumu.",
            "h = 80 m. Aprēķini krišanas laiku.",
            "Paskaidro, kāpēc papīra lapa krīt lēnāk par saburzītu papīra "
            "bumbiņu.",
        ],
        pasvertejums=["Protu skaidrot brīvo krišanu",
                      "Protu aprēķināt h, t un υ",
                      "Protu pamatot masas nenozīmīgumu",
                      "Protu izvērtēt gaisa pretestību"],
        nakama="Nākamā stunda: kustības drošība."),
),

dict(
    nr="7.8", virsraksts="Kustības drošība",
    jautajums="Cik garš ir bremzēšanas ceļš?",
    apaksraksts="Reakcijas ceļš · Bremzēšanas ceļš · Apstāšanās ceļš",
    merkis="Iemācīties aprēķināt reakcijas un bremzēšanas ceļu un izvērtēt "
           "faktorus, kas palielina apstāšanās ceļu.",
    protu=["atšķirt reakcijas, bremzēšanas un apstāšanās ceļu;",
           "aprēķināt reakcijas ceļu;",
           "aprēķināt bremzēšanas ceļu;",
           "izvērtēt ātruma un reakcijas laika ietekmi uz drošību."],
    atkartojums="7.5.–7.7. stundā mācījāmies aprēķināt paātrinājumu un ceļu. "
                "Šodien to izmantosim visnopietnākajā situācijā — uz ceļa.",
    uzdevumu_apraksts="Reakcijas, bremzēšanas un apstāšanās ceļš",
    teorija=[
        ("Trīs ceļa daļas", [
            ("kartitas", [
                ("REAKCIJAS CEĻŠ", BLUE,
                 ["No briesmu pamanīšanas līdz",
                  "bremžu nospiešanai.",
                  "s₁ = υ · t(reakc.)",
                  "Vidēji t = 0,8–1,5 s."]),
                ("BREMZĒŠANAS CEĻŠ", RED,
                 ["No bremžu nospiešanas",
                  "līdz apstāšanās brīdim.",
                  "s₂ = υ² / (2a)",
                  "Aug ar ātruma KVADRĀTU!"]),
                ("APSTĀŠANĀS CEĻŠ", GOLD,
                 ["Abu summa.",
                  "s = s₁ + s₂",
                  "Tieši tas jāzina autovadītājam."]),
            ]),
            ("formula", "APSTĀŠANĀS CEĻŠ",
             "s = υ · t(reakc.) + υ² / (2a)",
             "Reakcijas ceļš aug lineāri ar ātrumu, bet bremzēšanas ceļš — "
             "ar ātruma kvadrātu. Tāpēc divreiz lielāks ātrums nozīmē "
             "četrreiz garāku bremzēšanas ceļu.", GOLD),
        ]),
        ("Kas palielina apstāšanās ceļu", [
            ("tabula",
             ["Faktors", "Ietekme", "Kāpēc"],
             [["Lielāks ātrums", "ļoti liela", "s₂ ~ υ²"],
              ["Nogurums, alkohols, telefons", "liela",
               "aug reakcijas laiks"],
              ["Slapjš vai apledojis ceļš", "liela",
               "samazinās bremzēšanas paātrinājums"],
              ["Nolietotas riepas vai bremzes", "vidēja",
               "samazinās berzes spēks"],
              ["Liela kravas masa", "vidēja", "grūtāk apturēt"]],
             [4.63, 2.60, 5.00]),
            ("panelis", "DIVREIZ ĀTRĀK — ČETRREIZ TĀLĀK",
             ["Pie 50 km/h bremzēšanas ceļš ir ~12 m, pie 100 km/h — jau "
              "~48 m. Tieši tāpēc apdzīvotās vietās ātrums ir ierobežots "
              "līdz 50 km/h."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Reakcijas ceļš",
             teksts="Automašīna brauc ar 72 km/h. Vadītāja reakcijas laiks "
                    "ir 1,0 s.\nAprēķini reakcijas ceļu!",
             dots=["υ = 72 km/h", "t = 1,0 s"],
             jaaprekina=["s₁ = ?"],
             formulas=["s₁ = υ · t"],
             aprekins=["1)  υ = 72 : 3,6 = 20 m/s",
                       "2)  s₁ = 20 m/s · 1,0 s",
                       "3)  s₁ = 20 m"],
             atbilde="s₁ = 20 m",
             piezime="20 m automašīna nobrauc, pirms vadītājs vispār "
                     "pieskaras bremzēm."),
        dict(nr=2, virsraksts="Bremzēšanas ceļš",
             teksts="Automašīna brauc ar 20 m/s. Bremzēšanas paātrinājums ir "
                    "5,0 m/s².\nAprēķini bremzēšanas ceļu!",
             dots=["υ = 20 m/s", "a = 5,0 m/s²"],
             jaaprekina=["s₂ = ?"],
             formulas=["s₂ = υ² / (2a)"],
             aprekins=["1)  υ² = 20² = 400 m²/s²",
                       "2)  2a = 2 · 5,0 = 10 m/s²",
                       "3)  s₂ = 400 : 10 = 40 m"],
             atbilde="s₂ = 40 m",
             piezime="Bremzēšanas ceļš ir divreiz garāks par reakcijas ceļu."),
        dict(nr=3, virsraksts="Pilnais apstāšanās ceļš",
             teksts="Automašīna brauc ar 90 km/h. Reakcijas laiks 1,2 s, "
                    "bremzēšanas paātrinājums 6,0 m/s².\n"
                    "Aprēķini pilno apstāšanās ceļu!",
             dots=["υ = 90 km/h", "t = 1,2 s", "a = 6,0 m/s²"],
             jaaprekina=["s = ?"],
             formulas=["s₁ = υt", "s₂ = υ²/(2a)", "s = s₁ + s₂"],
             aprekins=["1)  υ = 90 : 3,6 = 25 m/s",
                       "2)  s₁ = 25 · 1,2 = 30 m",
                       "3)  s₂ = 25² : (2 · 6,0) = 625 : 12 = 52 m",
                       "4)  s = 30 + 52 = 82 m"],
             atbilde="s ≈ 82 m",
             piezime="Vairāk nekā 80 m — tas ir gandrīz futbola laukuma "
                     "garums."),
        dict(nr=4, virsraksts="Ātruma dubultošana",
             teksts="Bremzēšanas paātrinājums ir 5,0 m/s². Salīdzini "
                    "bremzēšanas ceļu pie 50 km/h un 100 km/h!\n"
                    "Cik reižu tas atšķiras?",
             dots=["υ₁ = 50 km/h ;  υ₂ = 100 km/h", "a = 5,0 m/s²"],
             jaaprekina=["s₁ = ?", "s₂ = ?", "n = ?"],
             formulas=["s = υ² / (2a)"],
             aprekins=["1)  υ₁ = 13,9 m/s ;  υ₂ = 27,8 m/s",
                       "2)  s₁ = 13,9² : 10 = 19,3 m",
                       "3)  s₂ = 27,8² : 10 = 77,2 m",
                       "4)  n = 77,2 : 19,3 = 4,0"],
             atbilde="s₁ ≈ 19 m ;  s₂ ≈ 77 m ;  n = 4 reizes",
             piezime="Ātrums divkāršojas — bremzēšanas ceļš pieaug četras "
                     "reizes, jo s ~ υ²."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Apstāšanās ceļš = reakcijas ceļš + bremzēšanas ceļš.",
            "s₁ = υ·t(reakc.) aug lineāri; s₂ = υ²/(2a) aug ar kvadrātu.",
            "Divreiz lielāks ātrums — četrreiz garāks bremzēšanas ceļš.",
            "Reakcijas laiku palielina nogurums, alkohols un telefona "
            "lietošana.",
        ],
        majasdarbs=[
            "υ = 54 km/h, t(reakc.) = 1,0 s. Aprēķini reakcijas ceļu.",
            "υ = 15 m/s, a = 6 m/s². Aprēķini bremzēšanas ceļu.",
            "Aprēķini pilno apstāšanās ceļu pie 60 km/h, t = 1,5 s, "
            "a = 5 m/s².",
        ],
        pasvertejums=["Protu atšķirt ceļa daļas",
                      "Protu aprēķināt reakcijas ceļu",
                      "Protu aprēķināt bremzēšanas ceļu",
                      "Protu izvērtēt drošības faktorus"],
        nakama="Nākamā stunda: PD4 — Kustības apraksts (kinemātika). "
               "Atkārto 7.1.–7.8. stundu formulas un grafikus."),
),
]


def build():
    return C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
