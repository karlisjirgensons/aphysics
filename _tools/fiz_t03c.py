# -*- coding: utf-8 -*-
"""3. temats. C daļa: 3.15.-3.22. stunda (spiediens, hidrostatika, PD4)."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t03a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="3.15", virsraksts="Spiediens cietās vielās",
    jautajums="Kāpēc naglai ir smails gals?",
    apaksraksts="p = F/S · [p] = Pa · Laukuma nozīme",
    merkis="Iemācīties aprēķināt spiedienu cietās vielās un izskaidrot, "
           "kā laukums maina spiediena iedarbību.",
    protu=["definēt spiedienu un nosaukt mērvienību;",
           "aprēķināt p, F vai S;",
           "izskaidrot, kad spiedienu palielina un kad samazina;",
           "novērtēt spiedienu ikdienas situācijās."],
    atkartojums="Līdz šim runājām par spēku. Tagad svarīgs kļūst arī "
                "LAUKUMS, uz kuru spēks darbojas.",
    uzdevumu_apraksts="Spiediena aprēķins un laukuma nozīme",
    teorija=[
        ("Spiediens", [
            ("formula", "SPIEDIENS",
             "p = F / S        [p] = paskāls (Pa) = N/m²        "
             "1 kPa = 10³ Pa;  1 MPa = 10⁶ Pa",
             "F ir spēks, kas darbojas PERPENDIKULĀRI virsmai; S ir "
             "saskares laukums. Viens un tas pats spēks uz maza laukuma "
             "rada lielu spiedienu.", GOLD),
            ("divi",
             ("PALIELINA SPIEDIENU", RED,
              ["Samazina laukumu.",
               "Naga smailums, naža asmens,",
               "slidas asmens, adata.",
               "Mērķis - iespiesties."]),
             ("SAMAZINA SPIEDIENU", GREEN,
              ["Palielina laukumu.",
               "Kāpurķēdes, slēpes, plati riteņi,",
               "pamatu plātne.",
               "Mērķis - neiegrimt."])),
        ]),
        ("Tipiskas vērtības", [
            ("tabula",
             ["Situācija", "Spiediens", "Piezīme"],
             [["Cilvēks stāv uz abām kājām", "~15 kPa", "S ≈ 0,05 m²"],
              ["Cilvēks uz slēpēm", "~2 kPa", "S ≈ 0,4 m²"],
              ["Automašīnas riepa", "200-250 kPa", "Manometra rādījums"],
              ["Atmosfēras spiediens", "101 kPa", "Jūras līmenī"],
              ["Naga gals", "~10⁸ Pa", "S ≈ 10⁻⁸ m²"]],
             [5.10, 3.40, 3.73]),
            ("panelis", "KĀPĒC NAGLA IESPIEŽAS",
             ["Uz naglas galvas un uz gala darbojas viens un tas pats "
              "spēks, bet gala laukums ir tūkstošiem reižu mazāks - "
              "tāpēc spiediens tur ir tūkstošiem reižu lielāks un koks "
              "padodas."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Cilvēka spiediens uz grīdu",
             teksts="Cilvēka masa 70 kg, abu pēdu laukums 0,048 m².\n"
                    "Aprēķini spiedienu uz grīdu! (g = 9,8 m/s²)",
             dots=["m = 70 kg", "S = 0,048 m²", "g = 9,8 m/s²"],
             jaaprekina=["p = ?"],
             formulas=["F = mg", "p = F/S"],
             aprekins=["1)  F = 70 · 9,8 = 686 N",
                       "2)  p = 686 : 0,048",
                       "3)  p = 14 292 ≈ 1,4·10⁴ Pa = 14 kPa"],
             atbilde="p ≈ 14 kPa",
             piezime="Stāvot uz vienas kājas, spiediens dubultotos."),
        dict(nr=2, virsraksts="Slēpes un iegrimšana",
             teksts="Tas pats cilvēks uzvelk slēpes ar kopējo laukumu\n"
                    "0,60 m². Cik reižu samazinās spiediens?",
             dots=["F = 686 N", "S₁ = 0,048 m²", "S₂ = 0,60 m²"],
             jaaprekina=["p₂ = ?", "p₁/p₂ = ?"],
             formulas=["p = F/S"],
             aprekins=["1)  p₂ = 686 : 0,60 = 1143 Pa ≈ 1,1 kPa",
                       "2)  p₁ / p₂ = 14 292 : 1143",
                       "3)  ≈ 12,5 reizes"],
             atbilde="p₂ ≈ 1,1 kPa - spiediens samazinās 12,5 reizes.",
             piezime="Tieši tāpēc uz slēpēm sniegā neiegrimst."),
        dict(nr=3, virsraksts="Laukums no spiediena",
             teksts="Traktors ar masu 6000 kg drīkst radīt spiedienu\n"
                    "ne vairāk par 40 kPa. Cik lielam jābūt kāpurķēžu\n"
                    "kopējam laukumam? (g = 9,8 m/s²)",
             dots=["m = 6000 kg", "p = 40 kPa = 4,0·10⁴ Pa"],
             jaaprekina=["S = ?"],
             formulas=["F = mg", "S = F/p"],
             aprekins=["1)  F = 6000 · 9,8 = 58 800 N",
                       "2)  S = 58 800 : 4,0·10⁴",
                       "3)  S = 1,47 ≈ 1,5 m²"],
             atbilde="S ≈ 1,5 m²",
             piezime="Uz riteņiem laukums būtu daudz mazāks - traktors "
                     "iegrimtu."),
        dict(nr=4, virsraksts="Naga gals",
             teksts="Ar āmuru uz naglu iedarbojas 400 N; gala laukums\n"
                    "0,20 mm². Aprēķini spiedienu!",
             dots=["F = 400 N", "S = 0,20 mm² = 2,0·10⁻⁷ m²"],
             jaaprekina=["p = ?"],
             formulas=["1 mm² = 10⁻⁶ m²", "p = F/S"],
             aprekins=["1)  S = 0,20 · 10⁻⁶ = 2,0·10⁻⁷ m²",
                       "2)  p = 400 : 2,0·10⁻⁷",
                       "3)  p = 2,0·10⁹ Pa = 2,0 GPa"],
             atbilde="p = 2,0·10⁹ Pa",
             piezime="Tas ir 20 000 reižu lielāks par atmosfēras "
                     "spiedienu."),
        dict(nr=5, virsraksts="Ķieģelis divās pozīcijās",
             teksts="Ķieģeļa (m = 4,0 kg) skaldnes ir 0,25 × 0,12 m un\n"
                    "0,12 × 0,065 m. Aprēķini lielāko un mazāko "
                    "spiedienu!\n(g = 9,8 m/s²)",
             dots=["m = 4,0 kg", "S₁ = 0,030 m²", "S₂ = 0,0078 m²"],
             jaaprekina=["p(min) = ?", "p(max) = ?"],
             formulas=["F = mg", "p = F/S"],
             aprekins=["1)  F = 4,0 · 9,8 = 39,2 N",
                       "2)  p(min) = 39,2 : 0,030 = 1307 Pa ≈ 1,3 kPa",
                       "3)  p(max) = 39,2 : 0,0078 = 5026 Pa ≈ 5,0 kPa"],
             atbilde="p(min) ≈ 1,3 kPa ;   p(max) ≈ 5,0 kPa",
             piezime="Spēks abos gadījumos vienāds - atšķiras tikai "
                     "laukums."),
        dict(nr=6, virsraksts="Galda kājas",
             teksts="Galda masa ir 20 kg, tam ir 4 kājas ar laukumu\n"
                    "25 cm² katra. Aprēķini spiedienu uz grīdu! "
                    "(g = 9,8 m/s²)",
             dots=["m = 20 kg", "4 kājas pa 25 cm²"],
             jaaprekina=["S = ?", "p = ?"],
             formulas=["S = 4 · 25 cm²", "F = mg", "p = F/S"],
             aprekins=["1)  S = 100 cm² = 0,010 m²",
                       "2)  F = 20 · 9,8 = 196 N",
                       "3)  p = 196 : 0,010 = 19 600 Pa ≈ 20 kPa"],
             atbilde="p ≈ 2,0·10⁴ Pa = 20 kPa",
             piezime="Laukumu saskaita par visām atbalsta vietām, "
                     "nevis vienu."),
        dict(nr=7, virsraksts="Ass un truls nazis",
             teksts="Ar 50 N spiež nazi, kura asmens laukums ir "
                    "0,50 mm².\nCik liels ir spiediens un cik tas "
                    "mainītos, ja asmens\nnotrulotos līdz 5,0 mm²?",
             dots=["F = 50 N", "S₁ = 0,50 mm²", "S₂ = 5,0 mm²"],
             jaaprekina=["p₁ = ?", "p₂ = ?"],
             formulas=["1 mm² = 10⁻⁶ m²", "p = F/S"],
             aprekins=["1)  S₁ = 5,0·10⁻⁷ m² → p₁ = 50 : 5,0·10⁻⁷ = "
                       "1,0·10⁸ Pa",
                       "2)  S₂ = 5,0·10⁻⁶ m² → p₂ = 1,0·10⁷ Pa",
                       "3)  p₁ : p₂ = 10"],
             atbilde="p₁ = 1,0·10⁸ Pa ;   p₂ = 1,0·10⁷ Pa - 10 reižu "
                     "mazāk.",
             piezime="Tāpēc ass nazis griež viegli, bet truls - "
                     "gandrīz nemaz."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "p = F/S;  [p] = paskāls = N/m².",
            "Mazāks laukums - lielāks spiediens.",
            "Spiedienu palielina ar smailumu, samazina ar platumu.",
            "Vienmēr jāpārveido mm² un cm² uz m².",
        ],
        majasdarbs=[
            "m = 85 kg, S = 0,055 m². Aprēķini p.",
            "F = 250 N, S = 0,50 cm². Aprēķini p.",
            "p = 30 kPa, m = 1500 kg. Aprēķini vajadzīgo laukumu.",
        ],
        pasvertejums=["Protu definēt spiedienu",
                      "Protu rēķināt p, F un S",
                      "Protu pārveidot laukuma vienības",
                      "Protu izskaidrot laukuma nozīmi"],
        nakama="Nākamā stunda: spiediens šķidrumos."),
),

dict(
    nr="3.16", virsraksts="Spiediens šķidrumos",
    jautajums="Kāpēc dziļumā spiediens ir lielāks?",
    apaksraksts="p = ρgh · Paskāla likums · Hidrauliskā prese",
    merkis="Iemācīties aprēķināt hidrostatisko spiedienu un lietot "
           "Paskāla likumu.",
    protu=["lietot p = ρgh;",
           "formulēt Paskāla likumu;",
           "aprēķināt spēku hidrauliskajā presē;",
           "pamatot, kāpēc spiediens nav atkarīgs no trauka formas."],
    atkartojums="3.15. stundā: p = F/S. Šķidrumā spiedienu rada paša "
                "šķidruma svars, un tas ir vienāds visos virzienos.",
    uzdevumu_apraksts="Hidrostatiskais spiediens un hidrauliskā prese",
    teorija=[
        ("Hidrostatiskais spiediens", [
            ("formula", "SPIEDIENS DZIĻUMĀ",
             "p = ρ · g · h        p(pilnais) = p₀ + ρgh",
             "ρ - šķidruma blīvums, h - dziļums no virsmas. Spiediens "
             "NAV atkarīgs no trauka formas vai šķidruma daudzuma - "
             "tikai no dziļuma un blīvuma.", GOLD),
            ("kartitas", [
                ("VISOS VIRZIENOS", BLUE,
                 ["Šķidrumā spiediens vienāds",
                  "uz augšu, uz leju un uz sāniem.",
                  "Tāpēc ķermenis tiek spiests no visām pusēm."]),
                ("NEATKARĪGS NO FORMAS", GREEN,
                 ["Šaurā un platā traukā",
                  "vienā dziļumā spiediens vienāds.",
                  "Hidrostatikas paradokss."]),
                ("SAVIENOTIE TRAUKI", GOLD,
                 ["Viendabīgs šķidrums nostājas",
                  "vienā līmenī.",
                  "Ūdenslīmeņrādis, akvedukti."]),
            ]),
        ]),
        ("Paskāla likums", [
            ("formula", "PASKĀLA LIKUMS UN HIDRAULISKĀ PRESE",
             "Šķidrumam pieliktais spiediens pārnesas visos virzienos "
             "vienādi:        p₁ = p₂   ⟹   F₁ / S₁ = F₂ / S₂",
             "Spēku ieguvums: F₂ = F₁ · S₂/S₁. Tā darbojas hidrauliskās "
             "bremzes, domkrats un prese.", GOLD),
            ("tabula",
             ["Dziļums ūdenī", "ρgh", "Kopā ar atmosfēru"],
             [["1 m", "9,8 kPa", "111 kPa"],
              ["10 m", "98 kPa", "199 kPa (≈ 2 atm)"],
              ["100 m", "980 kPa", "1081 kPa"],
              ["11 000 m (Marianas)", "108 MPa", "108 MPa"]],
             [4.30, 3.40, 4.53]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spiediens dziļumā",
             teksts="Aprēķini ūdens spiedienu 25 m dziļumā!\n"
                    "(ρ = 1000 kg/m³; g = 9,8 m/s²)",
             dots=["h = 25 m", "ρ = 1000 kg/m³", "g = 9,8 m/s²"],
             jaaprekina=["p = ?"],
             formulas=["p = ρgh"],
             aprekins=["1)  ρg = 1000 · 9,8 = 9800 N/m³",
                       "2)  p = 9800 · 25",
                       "3)  p = 2,45·10⁵ Pa = 245 kPa"],
             atbilde="p = 2,45·10⁵ Pa ≈ 2,5·10² kPa",
             piezime="Kopā ar atmosfēru niršanas dziļumā spiediens ir "
                     "~3,5 atmosfēras."),
        dict(nr=2, virsraksts="Dziļums no spiediena",
             teksts="Zemūdenes korpuss iztur spiedienu 4,0 MPa.\n"
                    "Cik dziļi tā drīkst nirt jūrā? "
                    "(ρ = 1030 kg/m³; g = 9,8 m/s²)",
             dots=["p = 4,0 MPa = 4,0·10⁶ Pa", "ρ = 1030 kg/m³"],
             jaaprekina=["h = ?"],
             formulas=["p = ρgh", "h = p/(ρg)"],
             aprekins=["1)  ρg = 1030 · 9,8 = 10 094 N/m³",
                       "2)  h = 4,0·10⁶ : 10 094",
                       "3)  h ≈ 396 ≈ 4,0·10² m"],
             atbilde="h ≈ 4,0·10² m",
             piezime="Jūras ūdens blīvums ir nedaudz lielāks nekā saldam "
                     "ūdenim."),
        dict(nr=3, virsraksts="Hidrauliskā prese",
             teksts="Hidrauliskās preses mazā virzuļa laukums 5,0 cm²,\n"
                    "lielā - 400 cm². Uz mazo darbojas 120 N.\n"
                    "Aprēķini spēku uz lielo virzuli!",
             dots=["S₁ = 5,0 cm²", "S₂ = 400 cm²", "F₁ = 120 N"],
             jaaprekina=["F₂ = ?"],
             formulas=["F₁/S₁ = F₂/S₂", "F₂ = F₁ · S₂/S₁"],
             aprekins=["1)  S₂/S₁ = 400 : 5,0 = 80",
                       "2)  F₂ = 120 · 80",
                       "3)  F₂ = 9600 N"],
             atbilde="F₂ = 9,6·10³ N - ieguvums 80 reižu.",
             piezime="Spēka ieguvums; ceļa zaudējums ir tikpat liels - "
                     "enerģija nerodas no nekā."),
        dict(nr=4, virsraksts="Divi šķidrumi",
             teksts="Traukā ir 20 cm ūdens (ρ = 1000 kg/m³) un virs tā\n"
                    "10 cm eļļas (ρ = 900 kg/m³). Aprēķini spiedienu\n"
                    "trauka dibenā! (g = 9,8 m/s²)",
             dots=["h₁ = 0,10 m (eļļa)", "h₂ = 0,20 m (ūdens)"],
             jaaprekina=["p = ?"],
             formulas=["p = ρ₁gh₁ + ρ₂gh₂"],
             aprekins=["1)  p₁ = 900 · 9,8 · 0,10 = 882 Pa",
                       "2)  p₂ = 1000 · 9,8 · 0,20 = 1960 Pa",
                       "3)  p = 882 + 1960 = 2842 ≈ 2,8 kPa"],
             atbilde="p ≈ 2,8 kPa (bez atmosfēras spiediena)",
             piezime="Slāņu spiedienus vienkārši saskaita - katrs dod "
                     "savu daļu."),
        dict(nr=5, virsraksts="Dzīvsudraba stabs",
             teksts="Aprēķini spiedienu, ko rada 760 mm augsts "
                    "dzīvsudraba\nstabs! (ρ = 13 600 kg/m³; "
                    "g = 9,8 m/s²)",
             dots=["h = 0,760 m", "ρ = 13 600 kg/m³"],
             jaaprekina=["p = ?"],
             formulas=["p = ρgh"],
             aprekins=["1)  ρg = 13 600 · 9,8 = 133 280 N/m³",
                       "2)  p = 133 280 · 0,760",
                       "3)  p ≈ 1,013·10⁵ Pa"],
             atbilde="p ≈ 1,0·10⁵ Pa - tas ir normālais atmosfēras "
                     "spiediens.",
             piezime="Tieši tāpēc barometros lieto dzīvsudrabu: ūdens "
                     "stabam vajadzētu 10 m."),
        dict(nr=6, virsraksts="Domkrata ceļa zaudējums",
             teksts="Domkratā S₁ = 2,0 cm², S₂ = 100 cm², F₁ = 200 N.\n"
                    "Aprēķini spēku uz lielo virzuli un tā pacēlumu,\n"
                    "ja mazo nospiež par 25 cm!",
             dots=["S₁ = 2,0 cm²", "S₂ = 100 cm²", "F₁ = 200 N",
                   "h₁ = 25 cm"],
             jaaprekina=["F₂ = ?", "h₂ = ?"],
             formulas=["F₂ = F₁S₂/S₁", "S₁h₁ = S₂h₂"],
             aprekins=["1)  S₂/S₁ = 50 → F₂ = 200 · 50 = 10 000 N",
                       "2)  h₂ = h₁ · S₁/S₂ = 25 : 50",
                       "3)  h₂ = 0,50 cm"],
             atbilde="F₂ = 1,0·10⁴ N ;   h₂ = 0,50 cm",
             piezime="Spēks 50 reižu lielāks, ceļš 50 reižu mazāks - "
                     "darbs paliek tāds pats."),
        dict(nr=7, virsraksts="Ūdenstornis",
             teksts="Ūdenstorņa ūdens līmenis ir 30 m virs krāna.\n"
                    "Aprēķini spiedienu pie krāna! (ρ = 1000 kg/m³; "
                    "g = 9,8 m/s²)",
             dots=["h = 30 m", "ρ = 1000 kg/m³"],
             jaaprekina=["p = ?"],
             formulas=["p = ρgh"],
             aprekins=["1)  ρg = 9800 N/m³",
                       "2)  p = 9800 · 30",
                       "3)  p = 2,94·10⁵ Pa ≈ 294 kPa"],
             atbilde="p ≈ 2,9·10⁵ Pa ≈ 3 atmosfēras",
             piezime="Spiedienu nosaka tikai augstums - torņa platums "
                     "nozīmes nav."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "p = ρgh - nav atkarīgs no trauka formas.",
            "Šķidrumā spiediens ir vienāds visos virzienos.",
            "Paskāla likums: F₁/S₁ = F₂/S₂.",
            "Hidrauliskā prese dod spēka ieguvumu S₂/S₁.",
        ],
        majasdarbs=[
            "h = 8,0 m ūdenī. Aprēķini p.",
            "S₁ = 4,0 cm², S₂ = 200 cm², F₁ = 80 N. Aprēķini F₂.",
            "p = 1,5 MPa. Aprēķini dziļumu saldūdenī.",
        ],
        pasvertejums=["Protu lietot p = ρgh",
                      "Protu formulēt Paskāla likumu",
                      "Protu rēķināt hidraulisko presi",
                      "Protu strādāt ar vairākiem slāņiem"],
        nakama="Nākamā stunda: Arhimēda spēks."),
),

dict(
    nr="3.17", virsraksts="Arhimēda spēks",
    jautajums="Kāpēc kuģis peld?",
    apaksraksts="F(A) = ρgV · Peldēšanas nosacījumi",
    merkis="Iemācīties aprēķināt Arhimēda spēku un noteikt, vai ķermenis "
           "peldēs, grims vai peldēs iegremdēts.",
    protu=["lietot F(A) = ρgV;",
           "nosaukt peldēšanas nosacījumus;",
           "aprēķināt iegrimušo tilpumu;",
           "izskaidrot, kāpēc tērauda kuģis peld."],
    atkartojums="3.16. stundā: dziļumā spiediens lielāks. Tieši šī "
                "spiediena starpība uz ķermeņa apakšu un augšu rada "
                "cēlējspēku.",
    uzdevumu_apraksts="Arhimēda spēks un peldēšanas nosacījumi",
    teorija=[
        ("Arhimēda likums", [
            ("formula", "CĒLĒJSPĒKS",
             "F(A) = ρ(šķidruma) · g · V(iegremdētā daļa)",
             "Cēlējspēks ir vienāds ar ķermeņa izspiestā šķidruma svaru. "
             "Uzmanību: ρ ir ŠĶIDRUMA blīvums, V - IEGREMDĒTĀ tilpuma "
             "daļa.", GOLD),
            ("kartitas", [
                ("GRIMST", RED,
                 ["ρ(ķerm) > ρ(šķidr)",
                  "F(A) < mg",
                  "Piemērs: akmens ūdenī."]),
                ("PELD IEGREMDĒTS", GOLD,
                 ["ρ(ķerm) = ρ(šķidr)",
                  "F(A) = mg",
                  "Piemērs: zivs ar peldpūsli."]),
                ("PELD UZ VIRSMAS", GREEN,
                 ["ρ(ķerm) < ρ(šķidr)",
                  "Iegrimst tikai daļēji.",
                  "Piemērs: koks, kuģis."]),
            ]),
        ]),
        ("Kāpēc tērauda kuģis peld", [
            ("panelis", "VIDĒJAIS BLĪVUMS",
             ["Tērauda blīvums ir 7800 kg/m³ - tas grimtu. Bet kuģis nav "
              "no cieta tērauda: korpusā ir gaiss, tāpēc VIDĒJAIS "
              "blīvums (kopējā masa dalīta ar kopējo tilpumu) ir mazāks "
              "par 1000 kg/m³. Tāpēc kuģis peld."], NAVY),
            ("tabula",
             ["Ķermenis", "ρ, kg/m³", "Ūdenī"],
             [["Korķis", "240", "Peld, iegrimst 24 %"],
              ["Priede", "500", "Peld, iegrimst 50 %"],
              ["Ledus", "920", "Peld, iegrimst 92 %"],
              ["Alumīnijs", "2700", "Grimst"],
              ["Tērauda kuģis (vidēji)", "~300", "Peld"]],
             [4.60, 3.10, 4.53]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Cēlējspēks",
             teksts="Ķermenis ar tilpumu 0,020 m³ pilnībā iegremdēts "
                    "ūdenī.\nAprēķini Arhimēda spēku! (ρ = 1000 kg/m³; "
                    "g = 9,8 m/s²)",
             dots=["V = 0,020 m³", "ρ = 1000 kg/m³"],
             jaaprekina=["F(A) = ?"],
             formulas=["F(A) = ρgV"],
             aprekins=["1)  ρg = 9800 N/m³",
                       "2)  F(A) = 9800 · 0,020",
                       "3)  F(A) = 196 N"],
             atbilde="F(A) = 196 N ≈ 2,0·10² N",
             piezime="Tas ir izspiestā ūdens (20 kg) svars."),
        dict(nr=2, virsraksts="Vai grims",
             teksts="Ķermeņa masa 15 kg, tilpums 0,012 m³.\n"
                    "Vai tas peldēs ūdenī? (ρ = 1000 kg/m³; "
                    "g = 9,8 m/s²)",
             dots=["m = 15 kg", "V = 0,012 m³"],
             jaaprekina=["ρ(ķerm) = ?", "vai peldēs?"],
             formulas=["ρ = m/V", "Peld, ja ρ(ķerm) < ρ(šķidr)"],
             aprekins=["1)  ρ = 15 : 0,012 = 1250 kg/m³",
                       "2)  1250 > 1000",
                       "3)  Ķermenis grims"],
             atbilde="Grims, jo ρ(ķerm) = 1250 kg/m³ > 1000 kg/m³.",
             piezime="Pārbaude: mg = 147 N, F(A) = 118 N - svars "
                     "lielāks."),
        dict(nr=3, virsraksts="Iegrimušais tilpums",
             teksts="Koka klucis (ρ = 600 kg/m³) ar tilpumu 0,050 m³\n"
                    "peld ūdenī. Cik liela tilpuma daļa ir zem ūdens?",
             dots=["ρ(k) = 600 kg/m³", "V = 0,050 m³",
                   "ρ(ū) = 1000 kg/m³"],
             jaaprekina=["V(iegr) = ?"],
             formulas=["Peldot F(A) = mg",
                       "ρ(ū)·g·V(iegr) = ρ(k)·g·V"],
             aprekins=["1)  V(iegr)/V = ρ(k)/ρ(ū) = 600 : 1000 = 0,60",
                       "2)  V(iegr) = 0,60 · 0,050",
                       "3)  V(iegr) = 0,030 m³"],
             atbilde="V(iegr) = 0,030 m³ - 60 % no tilpuma.",
             piezime="Iegrimušā daļa vienmēr ir ρ(ķerm)/ρ(šķidr)."),
        dict(nr=4, virsraksts="Svars ūdenī",
             teksts="Ķermeņa masa 8,0 kg, tilpums 0,0030 m³.\n"
                    "Cik lielu spēku rāda dinamometrs, kad ķermenis\n"
                    "iegremdēts ūdenī? (g = 9,8 m/s²)",
             dots=["m = 8,0 kg", "V = 0,0030 m³", "ρ = 1000 kg/m³"],
             jaaprekina=["F = ?"],
             formulas=["F = mg − F(A)", "F(A) = ρgV"],
             aprekins=["1)  mg = 8,0 · 9,8 = 78,4 N",
                       "2)  F(A) = 1000 · 9,8 · 0,0030 = 29,4 N",
                       "3)  F = 78,4 − 29,4 = 49 N"],
             atbilde="F = 49 N (gaisā būtu 78,4 N)",
             piezime="Šī spēku starpība ir tieši Arhimēda spēks - tā to "
                     "arī mēra."),
        dict(nr=5, virsraksts="Arhimēda spēks eļļā",
             teksts="Ķermeni ar tilpumu 0,010 m³ iegremdē eļļā\n"
                    "(ρ = 900 kg/m³). Aprēķini Arhimēda spēku un "
                    "salīdzini\nar ūdeni! (g = 9,8 m/s²)",
             dots=["V = 0,010 m³", "ρ(e) = 900 kg/m³",
                   "ρ(ū) = 1000 kg/m³"],
             jaaprekina=["F(A,eļļā) = ?", "F(A,ūdenī) = ?"],
             formulas=["F(A) = ρgV"],
             aprekins=["1)  F(A,e) = 900 · 9,8 · 0,010 = 88,2 N",
                       "2)  F(A,ū) = 1000 · 9,8 · 0,010 = 98 N",
                       "3)  Starpība 9,8 N (10 %)"],
             atbilde="F(A,eļļā) = 88,2 N ;   F(A,ūdenī) = 98 N",
             piezime="Jo blīvāks šķidrums, jo lielāks cēlējspēks - "
                     "tāpēc jūrā peld vieglāk nekā ezerā."),
        dict(nr=6, virsraksts="Ledus gabals ūdenī",
             teksts="Ledus blīvums ir 920 kg/m³.\n"
                    "Cik liela daļa ledus gabala ir zem ūdens? "
                    "(ρ(ū) = 1000 kg/m³)",
             dots=["ρ(l) = 920 kg/m³", "ρ(ū) = 1000 kg/m³"],
             jaaprekina=["V(iegr)/V = ?"],
             formulas=["V(iegr)/V = ρ(l)/ρ(ū)"],
             aprekins=["1)  V(iegr)/V = 920 : 1000",
                       "2)  = 0,92",
                       "3)  Virs ūdens paliek 8 %"],
             atbilde="Zem ūdens ir 92 % tilpuma.",
             piezime="Saldūdenī ledus iegrimst vairāk nekā jūrā - "
                     "salīdzini ar aisberga uzdevumu 3.18. stundā."),
        dict(nr=7, virsraksts="Cik jāpieliek, lai grimtu",
             teksts="Doba bumba (V = 0,0050 m³, m = 2,0 kg) peld ūdenī.\n"
                    "Cik lielu papildu masu jāieliek, lai tā tikko "
                    "grimtu?\n(ρ = 1000 kg/m³; g = 9,8 m/s²)",
             dots=["V = 0,0050 m³", "m = 2,0 kg", "ρ = 1000 kg/m³"],
             jaaprekina=["F(A) = ?", "Δm = ?"],
             formulas=["F(A) = ρgV", "Grimst, ja mg ≥ F(A)"],
             aprekins=["1)  F(A) = 1000 · 9,8 · 0,0050 = 49 N",
                       "2)  Vajadzīgā kopējā masa: 49 : 9,8 = 5,0 kg",
                       "3)  Δm = 5,0 − 2,0 = 3,0 kg"],
             atbilde="Δm = 3,0 kg",
             piezime="Ķermenis «karājas» ūdenī, kad tā vidējais blīvums "
                     "tieši sakrīt ar ūdens blīvumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "F(A) = ρ(šķidruma)·g·V(iegremdētā daļa).",
            "Peld, ja ρ(ķerm) < ρ(šķidr); grimst, ja lielāks.",
            "Iegrimušā daļa = ρ(ķerm)/ρ(šķidr).",
            "Kuģis peld, jo tā VIDĒJAIS blīvums ir mazs.",
        ],
        majasdarbs=[
            "V = 0,015 m³ ūdenī. Aprēķini F(A).",
            "ρ(ledus) = 920 kg/m³. Cik % aisberga ir zem ūdens?",
            "m = 5,0 kg, V = 0,0020 m³. Aprēķini svaru ūdenī.",
        ],
        pasvertejums=["Protu lietot F(A) = ρgV",
                      "Protu noteikt, vai peldēs",
                      "Protu rēķināt iegrimušo daļu",
                      "Protu izskaidrot kuģa peldēšanu"],
        nakama="Nākamā stunda: uzdevumi par hidrostatiku."),
),

dict(
    nr="3.18", virsraksts="Uzdevumi: hidrostatika",
    jautajums="Cik daudz ledus ir zem ūdens?",
    apaksraksts="Kombinēti uzdevumi · Kravnesība · Blīvuma noteikšana",
    merkis="Nostiprināt hidrostatikas uzdevumus: spiediens, cēlējspēks "
           "un peldēšana kopā.",
    protu=["kombinēt p = ρgh un F(A) = ρgV;",
           "aprēķināt kravnesību;",
           "noteikt blīvumu ar Arhimēda metodi;",
           "risināt uzdevumus par peldēšanu dažādos šķidrumos."],
    atkartojums="3.16. un 3.17. stunda: p = ρgh un F(A) = ρgV. Šodien "
                "tās kombinēsim praktiskos uzdevumos.",
    uzdevumu_apraksts="Kravnesība, blīvums un peldēšana",
    teorija=[
        ("Risinājuma paņēmieni", [
            ("tabula",
             ["Jautājums", "Pieeja", "Formula"],
             [["Cik dziļi iegrimst", "F(A) = mg", "V(iegr) = m/ρ(šķ)"],
              ["Kravnesība", "F(A,max) − mg", "m(kr) = ρV − m"],
              ["Blīvums ar svēršanu", "F(A) = mg − F(ūdenī)",
               "ρ = m·ρ(ū)/(m − m(ū))"],
              ["Spiediens uz dibenu", "p = ρgh", "F = pS"]],
             [3.90, 4.30, 4.03]),
            ("panelis", "SVARĪGI ATCERĒTIES",
             ["F(A) formulā ρ vienmēr ir ŠĶIDRUMA blīvums, nevis ķermeņa. "
              "V ir tikai IEGREMDĒTĀ daļa. Šīs divas kļūdas ir "
              "visbiežākās hidrostatikas uzdevumos."], NAVY),
        ]),
        ("Blīvumi, kas jāzina", [
            ("kartitas", [
                ("ŠĶIDRUMI", BLUE,
                 ["Ūdens 1000 kg/m³",
                  "Jūras ūdens 1030 kg/m³",
                  "Spirts 800 kg/m³",
                  "Dzīvsudrabs 13 600 kg/m³"]),
                ("CIETVIELAS", GREEN,
                 ["Ledus 920 kg/m³",
                  "Alumīnijs 2700 kg/m³",
                  "Tērauds 7800 kg/m³",
                  "Svins 11 300 kg/m³"]),
                ("GĀZES", GOLD,
                 ["Gaiss 1,29 kg/m³",
                  "Hēlijs 0,18 kg/m³",
                  "Arī gāzēs ir cēlējspēks!"]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Aisberga daļa",
             teksts="Ledus blīvums 920 kg/m³, jūras ūdens 1030 kg/m³.\n"
                    "Cik liela aisberga daļa ir zem ūdens?",
             dots=["ρ(l) = 920 kg/m³", "ρ(ū) = 1030 kg/m³"],
             jaaprekina=["V(iegr)/V = ?"],
             formulas=["V(iegr)/V = ρ(l)/ρ(ū)"],
             aprekins=["1)  V(iegr)/V = 920 : 1030",
                       "2)  = 0,893",
                       "3)  ≈ 89 %"],
             atbilde="Zem ūdens ir ≈ 89 % aisberga; virs ūdens tikai "
                     "11 %.",
             piezime="No tā radies izteiciens «aisberga redzamā daļa»."),
        dict(nr=2, virsraksts="Plosta kravnesība",
             teksts="Plosts no koka (ρ = 500 kg/m³) ar tilpumu 2,0 m³.\n"
                    "Cik lielu kravu tas var nest ūdenī? "
                    "(ρ(ū) = 1000 kg/m³)",
             dots=["V = 2,0 m³", "ρ(k) = 500 kg/m³",
                   "ρ(ū) = 1000 kg/m³"],
             jaaprekina=["m(kravas) = ?"],
             formulas=["F(A,max) = ρ(ū)gV", "m(kr) = ρ(ū)V − ρ(k)V"],
             aprekins=["1)  Maksimālā kopējā masa = 1000 · 2,0 = 2000 kg",
                       "2)  Plosta masa = 500 · 2,0 = 1000 kg",
                       "3)  m(kr) = 2000 − 1000 = 1000 kg"],
             atbilde="m(kravas) = 1000 kg = 1,0 t",
             piezime="Pie šīs kravas plosts iegrimtu tieši līdz augšējai "
                     "malai."),
        dict(nr=3, virsraksts="Blīvuma noteikšana",
             teksts="Ķermeņa masa gaisā 2,7 kg, ūdenī dinamometrs rāda\n"
                    "16,7 N. Aprēķini ķermeņa blīvumu! (g = 9,8 m/s²)",
             dots=["m = 2,7 kg", "F(ū) = 16,7 N", "ρ(ū) = 1000 kg/m³"],
             jaaprekina=["ρ = ?"],
             formulas=["F(A) = mg − F(ū)", "V = F(A)/(ρ(ū)g)",
                       "ρ = m/V"],
             aprekins=["1)  mg = 26,5 N ;  F(A) = 26,5 − 16,7 = 9,8 N",
                       "2)  V = 9,8 : 9800 = 1,0·10⁻³ m³",
                       "3)  ρ = 2,7 : 1,0·10⁻³ = 2700 kg/m³"],
             atbilde="ρ = 2,7·10³ kg/m³ - tas ir alumīnijs.",
             piezime="Tā Arhimēds noteica, vai kronis ir no tīra zelta."),
        dict(nr=4, virsraksts="Spiediens un spēks uz dibenu",
             teksts="Baseinā ūdens dziļums 2,5 m, dibena laukums 40 m².\n"
                    "Aprēķini spiedienu un spēku uz dibenu!\n"
                    "(ρ = 1000 kg/m³; g = 9,8 m/s²)",
             dots=["h = 2,5 m", "S = 40 m²", "ρ = 1000 kg/m³"],
             jaaprekina=["p = ?", "F = ?"],
             formulas=["p = ρgh", "F = pS"],
             aprekins=["1)  p = 1000 · 9,8 · 2,5 = 24 500 Pa",
                       "2)  F = 24 500 · 40",
                       "3)  F = 9,8·10⁵ N"],
             atbilde="p = 24,5 kPa ;   F = 9,8·10⁵ N",
             piezime="Tas atbilst 100 tonnu ūdens svaram - tieši tik "
                     "baseinā arī ir."),
        dict(nr=5, virsraksts="Kuģa iegrime",
             teksts="Kuģa ūdenslīnijas laukums ir 500 m². Uz kuģa "
                    "uzkrauj\n50 t kravas. Par cik palielinās iegrime? "
                    "(ρ = 1000 kg/m³)",
             dots=["S = 500 m²", "m = 5,0·10⁴ kg", "ρ = 1000 kg/m³"],
             jaaprekina=["Δh = ?"],
             formulas=["Papildu izspiestais tilpums V = m/ρ",
                       "Δh = V/S"],
             aprekins=["1)  V = 5,0·10⁴ : 1000 = 50 m³",
                       "2)  Δh = 50 : 500",
                       "3)  Δh = 0,10 m = 10 cm"],
             atbilde="Δh = 0,10 m",
             piezime="Pēc iegrimes atzīmēm uz borta ostā nosaka kuģa "
                     "kravas masu."),
        dict(nr=6, virsraksts="Spiediens uz zemūdenes lūku",
             teksts="Zemūdene atrodas 200 m dziļumā; lūkas laukums "
                    "0,50 m².\nAprēķini spiedienu un spēku uz lūku! "
                    "(ρ = 1030 kg/m³; g = 9,8 m/s²)",
             dots=["h = 200 m", "S = 0,50 m²", "ρ = 1030 kg/m³"],
             jaaprekina=["p = ?", "F = ?"],
             formulas=["p = ρgh", "F = pS"],
             aprekins=["1)  ρg = 1030 · 9,8 = 10 094 N/m³",
                       "2)  p = 10 094 · 200 ≈ 2,02·10⁶ Pa",
                       "3)  F = 2,02·10⁶ · 0,50 ≈ 1,0·10⁶ N"],
             atbilde="p ≈ 2,0 MPa ;   F ≈ 1,0·10⁶ N",
             piezime="Miljons ņūtonu ir aptuveni 100 tonnu svars - "
                     "tāpēc lūkas ir tik masīvas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Iegrimušā daļa = ρ(ķerm)/ρ(šķidr).",
            "Kravnesība = ρ(šķidr)V − m(peldlīdzekļa).",
            "Blīvumu var noteikt, sverot gaisā un ūdenī.",
            "Spēks uz dibenu F = ρghS.",
        ],
        majasdarbs=[
            "Koks ρ = 700 kg/m³. Cik % iegrimst ūdenī?",
            "V = 5,0 m³ plosts, ρ(k) = 400 kg/m³. Aprēķini kravnesību.",
            "m = 1,5 kg gaisā, 11,3 N ūdenī. Aprēķini ρ.",
        ],
        pasvertejums=["Protu kombinēt hidrostatikas formulas",
                      "Protu rēķināt kravnesību",
                      "Protu noteikt blīvumu",
                      "Protu rēķināt spēku uz dibenu"],
        nakama="Nākamā stunda: deformācijas un spriegums."),
),

dict(
    nr="3.19", virsraksts="Deformācijas un spriegums",
    jautajums="Kad trose pārtrūks?",
    apaksraksts="σ = F/S · Elastīga un plastiska · Drošības koeficients",
    merkis="Iemācīties aprēķināt mehānisko spriegumu un novērtēt "
           "konstrukcijas drošību.",
    protu=["definēt mehānisko spriegumu;",
           "aprēķināt σ = F/S;",
           "atšķirt elastīgu un plastisku deformāciju;",
           "lietot drošības koeficientu."],
    atkartojums="3.8. stundā: F = kx apraksta atsperi. Tagad skatīsimies "
                "uz materiālu pašu - cik lielu slodzi tas iztur.",
    uzdevumu_apraksts="Spriegums, izturība un drošības koeficients",
    teorija=[
        ("Mehāniskais spriegums", [
            ("formula", "SPRIEGUMS",
             "σ = F / S        [σ] = Pa;  praksē MPa vai GPa",
             "Spriegums rāda spēku uz šķērsgriezuma laukuma vienību. "
             "Materiāls pārtrūkst, kad σ sasniedz stiepes izturību.",
             GOLD),
            ("tabula",
             ["Materiāls", "Stiepes izturība", "Piezīme"],
             [["Tērauds (būvniecības)", "400-550 MPa", "Trošu, siju "
               "materiāls"],
              ["Alumīnijs", "90-300 MPa", "Vieglās konstrukcijas"],
              ["Koks (gar šķiedrām)", "40-100 MPa", "Anizotrops"],
              ["Betons (spiedē)", "20-40 MPa", "Stiepē ļoti vājš"],
              ["Neilona virve", "60-80 MPa", "Elastīga"]],
             [4.60, 3.60, 4.03]),
        ]),
        ("Deformāciju veidi un drošība", [
            ("divi",
             ("ELASTĪGA", GREEN,
              ["Pēc slodzes noņemšanas",
               "ķermenis atgriežas sākuma formā.",
               "Der Huka likums.",
               "σ < elastības robeža."]),
             ("PLASTISKA", RED,
              ["Forma paliek izmainīta.",
               "Huka likums neder.",
               "Metāla locīšana, štancēšana.",
               "σ > elastības robeža."])),
            ("formula", "DROŠĪBAS KOEFICIENTS",
             "n = σ(izturības) / σ(darba)        "
             "σ(pieļaujamais) = σ(izturības) / n",
             "Celtniecībā n = 2-3; cilvēku pacelšanas iekārtām n = 5-10; "
             "lidmašīnu detaļām n = 1,5-2 (ar ļoti stingru kontroli).",
             GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spriegums trosē",
             teksts="Tērauda trose ar šķērsgriezuma laukumu 50 mm² tur\n"
                    "1200 kg kravu. Aprēķini spriegumu! (g = 9,8 m/s²)",
             dots=["m = 1200 kg", "S = 50 mm² = 5,0·10⁻⁵ m²"],
             jaaprekina=["σ = ?"],
             formulas=["F = mg", "σ = F/S"],
             aprekins=["1)  F = 1200 · 9,8 = 11 760 N",
                       "2)  S = 50 · 10⁻⁶ = 5,0·10⁻⁵ m²",
                       "3)  σ = 11 760 : 5,0·10⁻⁵ = 2,35·10⁸ Pa = "
                       "235 MPa"],
             atbilde="σ ≈ 2,4·10² MPa",
             piezime="Ja izturība ir 500 MPa, drošības koeficients ir "
                     "tikai 2,1."),
        dict(nr=2, virsraksts="Pieļaujamā krava",
             teksts="Trosei izturība 480 MPa, laukums 80 mm²,\n"
                    "drošības koeficients 6. Cik lielu masu tā drīkst "
                    "celt? (g = 9,8 m/s²)",
             dots=["σ(izt) = 480 MPa", "S = 80 mm²", "n = 6"],
             jaaprekina=["m = ?"],
             formulas=["σ(piel) = σ(izt)/n", "F = σ(piel)·S",
                       "m = F/g"],
             aprekins=["1)  σ(piel) = 480 : 6 = 80 MPa = 8,0·10⁷ Pa",
                       "2)  F = 8,0·10⁷ · 8,0·10⁻⁵ = 6400 N",
                       "3)  m = 6400 : 9,8 ≈ 653 kg"],
             atbilde="m ≈ 6,5·10² kg",
             piezime="Cilvēku celšanai koeficients 6 ir minimums."),
        dict(nr=3, virsraksts="Vajadzīgais laukums",
             teksts="Jāpiekar 5,0 t krava. Tērauda pieļaujamais "
                    "spriegums\n120 MPa. Cik lielam jābūt troses "
                    "laukumam? (g = 9,8 m/s²)",
             dots=["m = 5000 kg", "σ = 120 MPa = 1,2·10⁸ Pa"],
             jaaprekina=["S = ?"],
             formulas=["F = mg", "S = F/σ"],
             aprekins=["1)  F = 5000 · 9,8 = 49 000 N",
                       "2)  S = 49 000 : 1,2·10⁸",
                       "3)  S = 4,08·10⁻⁴ m² ≈ 4,1 cm²"],
             atbilde="S ≈ 4,1 cm² (diametrs aptuveni 23 mm)",
             piezime="Reālā trose sastāv no daudzām plānām stieplēm - "
                     "tā ir elastīgāka."),
        dict(nr=4, virsraksts="Divas troses",
             teksts="Kravu 800 kg tur divas vienādas troses ar laukumu\n"
                    "30 mm² katra. Aprēķini spriegumu katrā trosē! "
                    "(g = 9,8 m/s²)",
             dots=["m = 800 kg", "S = 30 mm² katrai", "2 troses"],
             jaaprekina=["σ = ?"],
             formulas=["F(katrai) = mg/2", "σ = F/S"],
             aprekins=["1)  mg = 800 · 9,8 = 7840 N",
                       "2)  F(katrai) = 3920 N",
                       "3)  σ = 3920 : 3,0·10⁻⁵ = 1,31·10⁸ Pa ≈ "
                       "1,3·10² MPa"],
             atbilde="σ ≈ 1,3·10² MPa katrā trosē",
             piezime="Divas troses uz pusi samazina spriegumu - tāpēc "
                     "kritiskās vietās vienmēr ir dublējums."),
        dict(nr=5, virsraksts="Relatīvais pagarinājums",
             teksts="Trose ar sākotnējo garumu 2,0 m slodzes ietekmē\n"
                    "pagarinās par 4,0 mm. Aprēķini relatīvo "
                    "pagarinājumu!",
             dots=["l₀ = 2,0 m", "Δl = 4,0 mm = 0,0040 m"],
             jaaprekina=["ε = ?"],
             formulas=["ε = Δl/l₀"],
             aprekins=["1)  Δl = 4,0 mm = 0,0040 m",
                       "2)  ε = 0,0040 : 2,0",
                       "3)  ε = 0,0020 = 0,20 %"],
             atbilde="ε = 2,0·10⁻³ = 0,20 %",
             piezime="Relatīvais pagarinājums ir bezdimensiju lielums - "
                     "to bieži izsaka procentos."),
        dict(nr=6, virsraksts="Drošības koeficients",
             teksts="Materiāla izturība ir 400 MPa, bet konstrukcijā "
                    "darba\nspriegums ir 80 MPa. Cik liels ir drošības "
                    "koeficients?",
             dots=["σ(izt) = 400 MPa", "σ(darba) = 80 MPa"],
             jaaprekina=["n = ?"],
             formulas=["n = σ(izt)/σ(darba)"],
             aprekins=["1)  n = 400 : 80",
                       "2)  n = 5",
                       "3)  Konstrukcija iztur 5 reizes lielāku slodzi"],
             atbilde="n = 5",
             piezime="Būvniecībā parasti prasa n = 2...4, cilvēku "
                     "celšanai - vismaz 6."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "σ = F/S; mēra paskālos, praksē megapaskālos.",
            "Elastīga deformācija ir atgriezeniska, plastiska - nav.",
            "Drošības koeficients n = σ(izturības)/σ(darba).",
            "Vairākas troses proporcionāli samazina spriegumu.",
        ],
        majasdarbs=[
            "m = 500 kg, S = 25 mm². Aprēķini σ.",
            "σ(izt) = 400 MPa, n = 5, S = 60 mm². Aprēķini pieļaujamo "
            "masu.",
            "m = 2,0 t, σ(piel) = 100 MPa. Aprēķini vajadzīgo laukumu.",
        ],
        pasvertejums=["Protu rēķināt spriegumu",
                      "Protu atšķirt deformāciju veidus",
                      "Protu lietot drošības koeficientu",
                      "Protu rēķināt vajadzīgo laukumu"],
        nakama="Nākamā stunda: spēka moments."),
),

dict(
    nr="3.20", virsraksts="Spēka moments",
    jautajums="Kā ar mazu spēku pacelt smagu kravu?",
    apaksraksts="M = F·d · Sviras nosacījums · Griešanās līdzsvars",
    merkis="Iemācīties aprēķināt spēka momentu un lietot sviras "
           "līdzsvara nosacījumu.",
    protu=["definēt spēka momentu un plecu;",
           "aprēķināt M = Fd;",
           "lietot līdzsvara nosacījumu ΣM = 0;",
           "izskaidrot vienkāršos mehānismus."],
    atkartojums="Līdz šim spēki tikai pārvietoja ķermeni. Tagad "
                "skatīsimies uz GRIEŠANOS - un tur svarīgs kļūst arī "
                "pielikšanas punkts.",
    uzdevumu_apraksts="Sviras līdzsvars un spēka moments",
    teorija=[
        ("Spēka moments", [
            ("formula", "SPĒKA MOMENTS",
             "M = F · d        [M] = N·m",
             "d ir PLECS - īsākais attālums no griešanās ass līdz spēka "
             "darbības līnijai (perpendikuls!). Ja spēka līnija iet caur "
             "asi, moments ir nulle.", GOLD),
            ("kartitas", [
                ("PLECS", BLUE,
                 ["Perpendikuls no ass",
                  "līdz spēka līnijai.",
                  "Nevis attālums līdz punktam!"]),
                ("VIRZIENS", GREEN,
                 ["Pulksteņa rādītāja virzienā",
                  "vai pretēji.",
                  "Zīmes izvēlas pats."]),
                ("LĪDZSVARS", GOLD,
                 ["ΣM = 0",
                  "M(pa) = M(pretī)",
                  "F₁d₁ = F₂d₂"]),
            ]),
        ]),
        ("Vienkāršie mehānismi", [
            ("panelis", "SVIRAS LIKUMS",
             ["F₁d₁ = F₂d₂. Spēka ieguvums ir tikpat liels, cik ceļa "
              "zaudējums - darbs paliek tas pats. Neviens mehānisms "
              "nedod enerģijas ieguvumu; tas tikai maina spēka un ceļa "
              "attiecību."], NAVY),
            ("tabula",
             ["Mehānisms", "Kā darbojas", "Piemērs"],
             [["Svira", "F₁d₁ = F₂d₂", "Lauznis, šķēres"],
              ["Nekustīgs bloks", "Maina virzienu, F nemainās", "Karogs"],
              ["Kustīgs bloks", "Ieguvums 2 reizes", "Celtnis"],
              ["Slīpā plakne", "F = mg sin α", "Uzbrauktuve"],
              ["Hidrauliskā prese", "F₂ = F₁S₂/S₁", "Domkrats"]],
             [3.90, 4.60, 3.73]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēka moments",
             teksts="Uz sviru 0,80 m attālumā no ass darbojas spēks 25 N\n"
                    "perpendikulāri svirai. Aprēķini momentu!",
             dots=["F = 25 N", "d = 0,80 m"],
             jaaprekina=["M = ?"],
             formulas=["M = Fd"],
             aprekins=["1)  Spēks perpendikulārs → plecs = 0,80 m",
                       "2)  M = 25 · 0,80",
                       "3)  M = 20 N·m"],
             atbilde="M = 20 N·m",
             piezime="Ja spēks būtu vērsts gar sviru, moments būtu nulle."),
        dict(nr=2, virsraksts="Sviras līdzsvars",
             teksts="Uz sviras vienā pusē 0,30 m no ass ir 60 N.\n"
                    "Cik lielam jābūt spēkam otrā pusē 0,90 m no ass,\n"
                    "lai svira būtu līdzsvarā?",
             dots=["F₁ = 60 N", "d₁ = 0,30 m", "d₂ = 0,90 m"],
             jaaprekina=["F₂ = ?"],
             formulas=["F₁d₁ = F₂d₂", "F₂ = F₁d₁/d₂"],
             aprekins=["1)  M₁ = 60 · 0,30 = 18 N·m",
                       "2)  F₂ = 18 : 0,90",
                       "3)  F₂ = 20 N"],
             atbilde="F₂ = 20 N - trīs reizes mazāks spēks.",
             piezime="Spēka ieguvums 3 reizes, bet ceļš 3 reizes garāks."),
        dict(nr=3, virsraksts="Lauznis",
             teksts="Ar lauzni (garums 1,2 m, atbalsts 0,15 m no gala)\n"
                    "ceļ 200 kg akmeni. Cik liels spēks vajadzīgs?\n"
                    "(g = 9,8 m/s²)",
             dots=["m = 200 kg", "d₁ = 0,15 m",
                   "d₂ = 1,2 − 0,15 = 1,05 m"],
             jaaprekina=["F = ?"],
             formulas=["F₁d₁ = F₂d₂"],
             aprekins=["1)  F₁ = 200 · 9,8 = 1960 N",
                       "2)  M = 1960 · 0,15 = 294 N·m",
                       "3)  F₂ = 294 : 1,05 = 280 N"],
             atbilde="F ≈ 2,8·10² N - septiņas reizes mazāk par kravas "
                     "svaru.",
             piezime="Ieguvums = 1,05 : 0,15 = 7 reizes."),
        dict(nr=4, virsraksts="Sija ar diviem balstiem",
             teksts="Uz 4,0 m garas sijas, kas balstās uz abiem galiem,\n"
                    "1,0 m no kreisā gala novietota 300 kg krava.\n"
                    "Aprēķini spēku uz kreiso balstu! (g = 9,8 m/s²)",
             dots=["L = 4,0 m", "m = 300 kg", "a = 1,0 m no kreisā"],
             jaaprekina=["N₁ = ?"],
             formulas=["Momenti pret labo balstu: N₁·L = mg·(L − a)"],
             aprekins=["1)  mg = 300 · 9,8 = 2940 N",
                       "2)  N₁ · 4,0 = 2940 · 3,0",
                       "3)  N₁ = 8820 : 4,0 = 2205 ≈ 2,2·10³ N"],
             atbilde="N₁ ≈ 2,2·10³ N  (labajam paliek 735 N)",
             piezime="Pārbaude: 2205 + 735 = 2940 N = mg ✔"),
        dict(nr=5, virsraksts="Moments, ja spēks vērsts leņķī",
             teksts="Uz sviru 0,60 m attālumā no ass darbojas 40 N "
                    "spēks,\nkas vērsts 30° leņķī pret sviru. Aprēķini "
                    "momentu!\n(sin 30° = 0,50)",
             dots=["F = 40 N", "r = 0,60 m", "α = 30°"],
             jaaprekina=["d = ?", "M = ?"],
             formulas=["d = r · sin α", "M = Fd"],
             aprekins=["1)  d = 0,60 · 0,50 = 0,30 m",
                       "2)  M = 40 · 0,30",
                       "3)  M = 12 N·m"],
             atbilde="M = 12 N·m",
             piezime="Plecs ir attālums no ass līdz spēka darbības "
                     "līnijai, nevis līdz spēka pielikšanas punktam."),
        dict(nr=6, virsraksts="Durvju rokturis",
             teksts="Durvis stumj ar 15 N spēku 0,70 m no eņģēm un pēc "
                    "tam\n0,10 m no eņģēm. Salīdzini momentus!",
             dots=["F = 15 N", "d₁ = 0,70 m", "d₂ = 0,10 m"],
             jaaprekina=["M₁ = ?", "M₂ = ?"],
             formulas=["M = Fd"],
             aprekins=["1)  M₁ = 15 · 0,70 = 10,5 N·m",
                       "2)  M₂ = 15 · 0,10 = 1,5 N·m",
                       "3)  M₁ : M₂ = 7"],
             atbilde="M₁ = 10,5 N·m ;   M₂ = 1,5 N·m - septiņas reizes "
                     "mazāk.",
             piezime="Tāpēc rokturi vienmēr liek pēc iespējas tālāk no "
                     "eņģēm."),
        dict(nr=7, virsraksts="Divi bērni uz šūpolēm",
             teksts="Bērns (30 kg) sēž 1,8 m no šūpoļu ass.\n"
                    "Cik tālu no ass jāsēž otram bērnam (45 kg),\n"
                    "lai šūpoles būtu līdzsvarā?",
             dots=["m₁ = 30 kg", "d₁ = 1,8 m", "m₂ = 45 kg"],
             jaaprekina=["d₂ = ?"],
             formulas=["m₁gd₁ = m₂gd₂", "d₂ = m₁d₁/m₂"],
             aprekins=["1)  g saīsinās abās pusēs",
                       "2)  d₂ = 30 · 1,8 : 45",
                       "3)  d₂ = 1,2 m"],
             atbilde="d₂ = 1,2 m",
             piezime="Smagākajam vienmēr jāsēž tuvāk asij - attālumi "
                     "apgriezti proporcionāli masām."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "M = Fd, kur d ir perpendikulārais plecs.",
            "Līdzsvarā ΣM = 0, tātad F₁d₁ = F₂d₂.",
            "Spēka ieguvums = ceļa zaudējums.",
            "Neviens mehānisms nedod enerģijas ieguvumu.",
        ],
        majasdarbs=[
            "F = 40 N, d = 0,60 m. Aprēķini M.",
            "F₁ = 120 N, d₁ = 0,20 m, d₂ = 0,80 m. Aprēķini F₂.",
            "Sija 6,0 m, krava 400 kg 2,0 m no kreisā gala. Aprēķini "
            "abus balsta spēkus.",
        ],
        pasvertejums=["Protu definēt momentu un plecu",
                      "Protu rēķināt M",
                      "Protu lietot sviras likumu",
                      "Protu rēķināt balsta spēkus"],
        nakama="Nākamā stunda: temata nostiprināšana."),
),

dict(
    nr="3.21", virsraksts="Temata nostiprināšana",
    jautajums="Kā no situācijas nonākt līdz vienādojumam?",
    apaksraksts="Atgādne · Spēku shēma · PD4 formāts",
    merkis="Apkopot 3. temata saturu un nostiprināt ceļu no situācijas "
           "apraksta līdz atrisinātam vienādojumam.",
    protu=["izvēlēties pareizo pieeju pēc uzdevuma veida;",
           "uzzīmēt spēku shēmu jebkurā situācijā;",
           "kombinēt dinamiku, hidrostatiku un momentus;",
           "sagatavoties PD4."],
    atkartojums="Temats aptvēra Ņūtona likumus, spēku veidus, berzi, "
                "slīpo plakni, ķermeņu sistēmas, spiedienu, "
                "hidrostatiku, deformācijas un momentus.",
    uzdevumu_apraksts="Kombinēti uzdevumi PD4 formātā",
    teorija=[
        ("Temata atgādne", [
            ("formula", "DINAMIKA",
             "F = ma   ·   F(sm) = mg   ·   P = m(g ± a)   ·   "
             "F(b) = µN   ·   F = kx   ·   N = mg cos α",
             "Slīpā plakne: a = g(sin α − µ cos α).  "
             "Sistēmas: a = ΣF/Σm.", GOLD),
            ("formula", "SPIEDIENS, HIDROSTATIKA UN MOMENTI",
             "p = F/S   ·   p = ρgh   ·   F₁/S₁ = F₂/S₂   ·   "
             "F(A) = ρgV   ·   σ = F/S   ·   M = Fd",
             "Peldēšanas nosacījums: ρ(ķerm) < ρ(šķidr).  "
             "Līdzsvars: ΣF = 0 un ΣM = 0.", GOLD),
        ]),
        ("Kā atpazīt uzdevuma veidu", [
            ("tabula",
             ["Pazīme tekstā", "Pieeja", "Sākuma solis"],
             [["«paātrinājums», «bremzē»", "Dinamika", "Spēku shēma"],
              ["«slīp», «leņķī α»", "Slīpā plakne", "Asis gar plakni"],
              ["«peld», «iegremdē»", "Hidrostatika", "F(A) = ρgV"],
              ["«dziļumā», «spiediens»", "p = ρgh", "Blīvums un h"],
              ["«svira», «līdzsvarā»", "Momenti", "ΣM = 0"]],
             [4.30, 3.60, 4.33]),
            ("panelis", "PD4 FORMĀTS",
             ["Tests (10 p.) par spēkiem, likumiem un shēmām; lielumu un "
              "mērvienību tabula (5 p.); divi aprēķinu uzdevumi ar pilnu "
              "pierakstu (10 p.); uzdevums ar apakšjautājumiem par spēku "
              "shēmu vai hidrostatiku (5 p.). Kopā 30 punkti, "
              "40 minūtes."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Dinamika ar berzi",
             teksts="Kasti (m = 40 kg) velk horizontāli ar 200 N;\n"
                    "µ = 0,30. Aprēķini paātrinājumu un ātrumu pēc "
                    "5,0 s! (g = 9,8 m/s²)",
             dots=["m = 40 kg", "F = 200 N", "µ = 0,30", "t = 5,0 s"],
             jaaprekina=["a = ?", "v = ?"],
             formulas=["N = mg", "F(b) = µN", "a = (F − F(b))/m",
                       "v = at"],
             aprekins=["1)  N = 392 N ;  F(b) = 0,30 · 392 = 118 N",
                       "2)  a = (200 − 118) : 40 = 2,05 m/s²",
                       "3)  v = 2,05 · 5,0 ≈ 10 m/s"],
             atbilde="a ≈ 2,1 m/s² ;   v ≈ 10 m/s",
             piezime="Klasisks divu soļu uzdevums: dinamika, tad "
                     "kinemātika."),
        dict(nr=2, virsraksts="Slīpā plakne",
             teksts="Ķermenis slīd no miera 6,0 m pa plakni ar 30°;\n"
                    "µ = 0,25. Aprēķini ātrumu plaknes galā!\n"
                    "(sin 30° = 0,50; cos 30° = 0,87)",
             dots=["s = 6,0 m", "α = 30°", "µ = 0,25"],
             jaaprekina=["a = ?", "v = ?"],
             formulas=["a = g(sin α − µ cos α)", "v = √(2as)"],
             aprekins=["1)  µ cos α = 0,25 · 0,87 = 0,218",
                       "2)  a = 9,8(0,50 − 0,218) = 2,76 m/s²",
                       "3)  v = √(2 · 2,76 · 6,0) = √33,2 ≈ 5,8 m/s"],
             atbilde="v ≈ 5,8 m/s",
             piezime="Bez berzes būtu 7,7 m/s."),
        dict(nr=3, virsraksts="Hidrostatika",
             teksts="Ķermenis (m = 4,0 kg, V = 0,0025 m³) iegremdēts "
                    "ūdenī.\nAprēķini Arhimēda spēku un noskaidro, vai "
                    "tas grims!\n(ρ = 1000 kg/m³; g = 9,8 m/s²)",
             dots=["m = 4,0 kg", "V = 0,0025 m³", "ρ = 1000 kg/m³"],
             jaaprekina=["F(A) = ?", "vai grims?"],
             formulas=["F(A) = ρgV", "Salīdzina ar mg"],
             aprekins=["1)  F(A) = 1000 · 9,8 · 0,0025 = 24,5 N",
                       "2)  mg = 4,0 · 9,8 = 39,2 N",
                       "3)  39,2 > 24,5 → grims"],
             atbilde="F(A) = 24,5 N; ķermenis grims, jo mg > F(A).",
             piezime="Pārbaude: ρ(ķerm) = 4,0 : 0,0025 = 1600 kg/m³ > "
                     "1000 ✔"),
        dict(nr=4, virsraksts="Svira",
             teksts="Uz 3,0 m garas sviras ar atbalstu vidū vienā pusē\n"
                    "0,50 m no atbalsta ir 80 kg. Kāda masa jāliek otrā\n"
                    "pusē 1,5 m no atbalsta?",
             dots=["m₁ = 80 kg", "d₁ = 0,50 m", "d₂ = 1,5 m"],
             jaaprekina=["m₂ = ?"],
             formulas=["m₁gd₁ = m₂gd₂", "m₂ = m₁d₁/d₂"],
             aprekins=["1)  Masas g saīsinās",
                       "2)  m₂ = 80 · 0,50 : 1,5",
                       "3)  m₂ = 26,7 ≈ 27 kg"],
             atbilde="m₂ ≈ 27 kg",
             piezime="Trīs reizes lielāks plecs - trīs reizes mazāka "
                     "masa."),
        dict(nr=5, virsraksts="Sistēma ar bloku un berzi",
             teksts="Uz galda ir 4,0 kg kaste (µ = 0,25), savienota pār\n"
                    "bloku ar 2,0 kg atsvaru. Aprēķini paātrinājumu! "
                    "(g = 9,8 m/s²)",
             dots=["m₁ = 4,0 kg", "m₂ = 2,0 kg", "µ = 0,25"],
             jaaprekina=["F(b) = ?", "a = ?"],
             formulas=["F(b) = µm₁g", "a = (m₂g − F(b))/(m₁+m₂)"],
             aprekins=["1)  m₂g = 2,0 · 9,8 = 19,6 N",
                       "2)  F(b) = 0,25 · 4,0 · 9,8 = 9,8 N",
                       "3)  a = (19,6 − 9,8) : 6,0 = 1,63 ≈ 1,6 m/s²"],
             atbilde="a ≈ 1,6 m/s²",
             piezime="Bez berzes paātrinājums būtu 3,3 m/s² - berze to "
                     "samazina uz pusi."),
        dict(nr=6, virsraksts="Spiediens liftā",
             teksts="Kaste (m = 25 kg, pamatnes laukums 0,25 m²) stāv "
                    "liftā,\nkas kustas augšup ar 1,8 m/s² "
                    "paātrinājumu.\nAprēķini balsta reakciju un "
                    "spiedienu uz grīdu! (g = 9,8 m/s²)",
             dots=["m = 25 kg", "S = 0,25 m²", "a = 1,8 m/s²"],
             jaaprekina=["N = ?", "p = ?"],
             formulas=["N = m(g + a)", "p = N/S"],
             aprekins=["1)  g + a = 11,6 m/s²",
                       "2)  N = 25 · 11,6 = 290 N",
                       "3)  p = 290 : 0,25 = 1160 Pa ≈ 1,2 kPa"],
             atbilde="N = 290 N ;   p ≈ 1,2 kPa",
             piezime="Mierā spiediens būtu 980 Pa - paātrinājums to "
                     "palielina par 18 %."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Katrs dinamikas uzdevums sākas ar spēku shēmu.",
            "Slīpajā plaknē asis izvēlas gar plakni.",
            "Hidrostatikā salīdzina F(A) ar mg vai blīvumus.",
            "Momentu uzdevumos g bieži saīsinās.",
        ],
        majasdarbs=[
            "Atkārto abas atgādnes pirms PD4.",
            "Izpildi pa vienam uzdevumam no katra veida.",
            "Pārskati LD3 protokolu un Huka likumu.",
        ],
        pasvertejums=["Protu atpazīt uzdevuma veidu",
                      "Protu uzzīmēt spēku shēmu",
                      "Protu risināt hidrostatikas uzdevumus",
                      "Esmu gatavs PD4"],
        nakama="Nākamā stunda: PD4 - mijiedarbība un spēks."),
),

dict(
    nr="3.22", virsraksts="Kļūdu analīze",
    jautajums="Kuras spēku shēmas bija kļūdainas?",
    apaksraksts="PD4 kļūdas · Shēmu labošana · Pāreja uz gravitāciju",
    merkis="Analizēt PD4 kļūdas, izlabot spēku shēmas un sagatavoties "
           "4. tematam par gravitāciju.",
    protu=["atrast kļūdas spēku shēmās;",
           "izlabot risinājumu ar pamatojumu;",
           "papildināt personīgo atgādni;",
           "saistīt spēkus ar gravitācijas tematu."],
    atkartojums="PD4 ir uzrakstīts - tas bija apjomīgākais darbs "
                "10. klasē. Šodien kļūdas pārvēršam prasmēs.",
    uzdevumu_apraksts="Kļūdainu shēmu un risinājumu labošana",
    teorija=[
        ("Biežākās PD4 kļūdas", [
            ("tabula",
             ["Kļūda", "Kā izskatās", "Pareizi"],
             [["N = mg slīpā plaknē", "N = mg", "N = mg cos α"],
              ["Berze no mg", "F(b) = µmg slīpumā", "F(b) = µmg cos α"],
              ["F(A) ar ķermeņa ρ", "F(A) = ρ(ķerm)gV",
               "F(A) = ρ(šķidr)gV"],
              ["Plecs = attālums", "d līdz spēka punktam",
               "d = perpendikuls"],
              ["Trešā likuma pāris", "N un mg uz vienu ķermeni",
               "Divi dažādi ķermeņi"]],
             [3.60, 4.30, 4.33]),
            ("panelis", "SHĒMAS PAŠPĀRBAUDE",
             ["1) Vai katram spēkam ir «no kā»?  2) Vai N vērsta "
              "perpendikulāri virsmai?  3) Vai berze vērsta pretēji "
              "kustībai?  4) Vai nav lieku «kustības spēku»?  "
              "5) Vai asis izvēlētas ērti?"], NAVY),
        ]),
        ("Tilts uz 4. tematu", [
            ("divi",
             ("3. TEMATS", BLUE,
              ["Spēks tuvumā uz Zemes.",
               "F(sm) = mg ar g = const.",
               "Der tikai pie Zemes virsmas."]),
             ("4. TEMATS", GREEN,
              ["Gravitācija kā universāls spēks.",
               "F = G·m₁m₂/r².",
               "Der visur - arī kosmosā."])),
            ("formula", "SAVIENOJOŠĀ IDEJA",
             "mg = G · M(Zemes) · m / R²        ⟹        "
             "g = G · M / R²",
             "Formula F = mg ir tikai īpašs gadījums no vispārīgā "
             "gravitācijas likuma. Nākamajā tematā to pierādīsim.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atrodi kļūdu I",
             teksts="«Kaste uz plaknes ar 30°; m = 20 kg; µ = 0,20.\n"
                    "F(b) = µmg = 0,20 · 196 = 39,2 N.»\nIzlabo!",
             dots=["m = 20 kg", "α = 30°", "µ = 0,20"],
             jaaprekina=["F(b) = ?"],
             formulas=["N = mg cos α", "F(b) = µN"],
             aprekins=["1)  Kļūda: N slīpā plaknē nav mg",
                       "2)  N = 196 · 0,87 = 171 N",
                       "3)  F(b) = 0,20 · 171 = 34,1 N"],
             atbilde="F(b) ≈ 34 N, nevis 39,2 N.",
             piezime="Slīpā plaknē berze VIENMĒR mazāka nekā uz "
                     "horizontālas virsmas."),
        dict(nr=2, virsraksts="Atrodi kļūdu II",
             teksts="«Ķermenis ρ = 2000 kg/m³, V = 0,0010 m³ ūdenī.\n"
                    "F(A) = 2000 · 9,8 · 0,0010 = 19,6 N.»\nIzlabo!",
             dots=["ρ(ķerm) = 2000 kg/m³", "V = 0,0010 m³"],
             jaaprekina=["F(A) = ?"],
             formulas=["F(A) = ρ(šķidruma)gV"],
             aprekins=["1)  Kļūda: lietots ķermeņa, nevis šķidruma "
                       "blīvums",
                       "2)  ρ(ūdens) = 1000 kg/m³",
                       "3)  F(A) = 1000 · 9,8 · 0,0010 = 9,8 N"],
             atbilde="F(A) = 9,8 N, nevis 19,6 N.",
             piezime="Arhimēda spēku nosaka IZSPIESTAIS šķidrums."),
        dict(nr=3, virsraksts="Atrodi kļūdu III",
             teksts="«Uz grāmatu uz galda darbojas mg un N. Tie ir\n"
                    "Ņūtona trešā likuma pāris.»\nIzlabo un pamato!",
             dots=["grāmata uz galda"],
             jaaprekina=["Vai tas ir pāris?"],
             formulas=["Pāris - divi DAŽĀDI ķermeņi"],
             aprekins=["1)  mg un N pieliktas VIENAI grāmatai",
                       "2)  Tātad tas ir līdzsvars, ne pāris",
                       "3)  mg pāris: grāmata velk Zemi; "
                       "N pāris: grāmata spiež galdu"],
             atbilde="Tie ir līdzsvara spēki, nevis trešā likuma pāris.",
             piezime="Vienam ķermenim pielikti spēki NEKAD nav trešā "
                     "likuma pāris."),
        dict(nr=4, virsraksts="Atrodi kļūdu IV",
             teksts="«Svirai F₁ = 40 N, d₁ = 20 cm, d₂ = 50 cm;\n"
                    "F₂ = 40 · 50 : 20 = 100 N.»\nIzlabo risinājumu!",
             dots=["F₁ = 40 N", "d₁ = 0,20 m", "d₂ = 0,50 m"],
             jaaprekina=["F₂ = ?"],
             formulas=["F₁d₁ = F₂d₂", "F₂ = F₁d₁/d₂"],
             aprekins=["1)  Kļūda: pleci sareizināti nepareizā secībā",
                       "2)  F₂ = 40 · 0,20 : 0,50",
                       "3)  F₂ = 16 N"],
             atbilde="F₂ = 16 N, nevis 100 N.",
             piezime="Garākam plecam atbilst MAZĀKS spēks - to var "
                     "pārbaudīt ar veselo saprātu."),
        dict(nr=5, virsraksts="Atrodi kļūdu V",
             teksts="«Trose ar laukumu 20 mm² tur 1000 N;\n"
                    "S = 20 mm² = 0,020 m², tātad σ = 1000 : 0,020 = "
                    "50 kPa.»\nIzlabo!",
             dots=["F = 1000 N", "S = 20 mm²"],
             jaaprekina=["σ = ?"],
             formulas=["1 mm² = 10⁻⁶ m²", "σ = F/S"],
             aprekins=["1)  Kļūda mērvienībās: 20 mm² = 2,0·10⁻⁵ m²",
                       "2)  σ = 1000 : 2,0·10⁻⁵",
                       "3)  σ = 5,0·10⁷ Pa = 50 MPa"],
             atbilde="σ = 50 MPa, nevis 50 kPa - kļūda 1000 reižu.",
             piezime="Laukuma vienībās priedēklis kāpjams kvadrātā: "
                     "1 mm² = 10⁻⁶ m²."),
        dict(nr=6, virsraksts="Atrodi kļūdu VI",
             teksts="«Ķermenis peld uz ūdens virsmas, tātad Arhimēda "
                    "spēks\nir lielāks par smaguma spēku.»\n"
                    "Izlabo un pamato!",
             dots=["ķermenis peld", "v = 0"],
             jaaprekina=["F(A) pret mg = ?"],
             formulas=["Miera stāvoklī ΣF = 0"],
             aprekins=["1)  Peldošs ķermenis ir mierā",
                       "2)  Tātad kopspēks ir nulle",
                       "3)  F(A) = mg - spēki ir VIENĀDI"],
             atbilde="Peldot F(A) = mg; lielāks tas ir tikai tad, kad "
                     "ķermenis ceļas uz augšu.",
             piezime="Nosacījums ρ(ķerm) < ρ(šķidr) nosaka, VAI ķermenis "
                     "peld, bet peldot spēki vienmēr ir līdzsvarā."),
        dict(nr=7, virsraksts="Atgādnes papildināšana",
             teksts="Papildini personīgo atgādni ar 3. temata "
                    "sakarībām\nun divām kļūdām, kuras tev bija PD4!",
             dots=["PD4 rezultāti"],
             jaaprekina=["atgādne = ?"],
             formulas=["Personīgs saraksts"],
             aprekins=["1)  Sakarības: F = ma; F(b) = µN; N = mg cos α;",
                       "     F(A) = ρ(šķidr)gV; M = Fd",
                       "2)  Kļūdas: N slīpumā; ρ Arhimēda formulā"],
             atbilde="Atgādne papildināta ar 5 sakarībām un personīgām "
                     "kļūdām.",
             piezime="Šī atgādne noderēs arī 11. klasē un eksāmenā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Slīpā plaknē N = mg cos α, tāpēc arī berze ir mazāka.",
            "Arhimēda formulā lieto ŠĶIDRUMA blīvumu.",
            "Vienam ķermenim pielikti spēki nav trešā likuma pāris.",
            "Spēku shēmu vienmēr pārbauda pēc pieciem jautājumiem.",
        ],
        majasdarbs=[
            "Izlabo savas PD4 kļūdas pilnā pierakstā.",
            "Papildini personīgo atgādni.",
            "Atkārto F = ma un mg - 4. tematā tos savienosim ar "
            "gravitācijas likumu.",
        ],
        pasvertejums=["Protu atrast kļūdu shēmā",
                      "Protu izlabot risinājumu",
                      "Protu pamatot labojumu",
                      "Esmu gatavs 4. tematam"],
        nakama="Nākamais temats: gravitācijas lauks un kustība."),
),

]
