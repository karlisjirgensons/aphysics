# -*- coding: utf-8 -*-
"""10.8. Šķidrumi dabā un tehnikā (6 st.) un 10.9. Vides faktori (2 st.)."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN

T8 = "8. temats. Šķidrumi dabā un tehnikā"
K8 = "DABASZINĪBAS · 10. KLASE · 8. TEMATS: ŠĶIDRUMI DABĀ UN TEHNIKĀ"
M8 = "C:/aphysics/Dabaszinibas/8. Šķidrumi dabā un tehnikā"

T9 = "9. temats. Vides faktoru ietekme uz cilvēka organismu"
K9 = ("DABASZINĪBAS · 10. KLASE · 9. TEMATS: VIDES FAKTORU IETEKME UZ "
      "CILVĒKA ORGANISMU")
M9 = "C:/aphysics/Dabaszinibas/9. Vides faktoru ietekme uz cilvēka organismu"

ST8 = [

dict(
    nr="8.1", virsraksts="Blīvums un maisījumi",
    jautajums="Kāpēc eļļa peld virs ūdens?",
    apaksraksts="ρ = m/V · Šķidrumu slāņošanās · Maisījumu blīvums",
    merkis="Iemācīties salīdzināt šķidrumu blīvumus un skaidrot to "
           "slāņošanos, kā arī aprēķināt maisījuma blīvumu.",
    protu=["lietot ρ = m/V šķidrumiem;",
           "prognozēt šķidrumu slāņošanās secību;",
           "aprēķināt maisījuma vidējo blīvumu;",
           "pamatot, kāpēc naftas plankums peld uz jūras."],
    atkartojums="5.1. stundā rēķinājām cietvielu blīvumu. Tā pati formula "
                "der arī šķidrumiem — bet šķidrumi var slāņoties.",
    uzdevumu_apraksts="Blīvums, masa un maisījumi",
    teorija=[
        ("Šķidrumu blīvums", [
            ("formula", "BLĪVUMS", "ρ = m / V        m = ρ·V        V = m/ρ",
             "Šķidrumi ar mazāku blīvumu peld virs šķidrumiem ar lielāku "
             "blīvumu, ja tie nesajaucas.", GOLD),
            ("tabula",
             ["Šķidrums", "ρ, kg/m³", "Vieta traukā"],
             [["Dzīvsudrabs", "13 600", "apakšā"],
              ["Ūdens", "1000", "vidū"],
              ["Augu eļļa", "920", "virs ūdens"],
              ["Nafta", "800", "virs eļļas"],
              ["Spirts", "790", "virspusē"]],
             [4.13, 4.10, 4.00]),
        ]),
        ("Maisījumi un slāņošanās", [
            ("divi",
             ("KĀPĒC SLĀŅOJAS", BLUE,
              ["Uz katru slāni darbojas smaguma spēks.",
               "Blīvākais nogrimst zemāk.",
               "Slāņojas tikai nesajaucošies šķidrumi.",
               "Spirts un ūdens sajaucas — neslāņojas."]),
             ("MAISĪJUMA BLĪVUMS", GREEN,
              ["ρ = (m₁ + m₂) / (V₁ + V₂)",
               "Vienmēr starp abu komponentu blīvumiem.",
               "Nedrīkst vienkārši saskaitīt blīvumus",
               "un dalīt ar divi!"])),
            ("panelis", "KĀPĒC TAS SVARĪGI",
             ["Naftas noplūdes uz jūras peld virspusē, jo naftas blīvums "
              "(~800 kg/m³) ir mazāks par jūras ūdens blīvumu "
              "(~1025 kg/m³). Tāpēc noplūdi var savākt ar bonām no "
              "virspuses."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Šķidruma masa",
             teksts="Kannā ir 2,5 L augu eļļas, blīvums 920 kg/m³.\n"
                    "Aprēķini eļļas masu!",
             dots=["V = 2,5 L", "ρ = 920 kg/m³"],
             jaaprekina=["m = ?"],
             formulas=["ρ = m / V", "m = ρ · V", "1 L = 10⁻³ m³"],
             aprekins=["1)  V = 2,5 L = 2,5·10⁻³ m³",
                       "2)  m = 920 · 2,5·10⁻³",
                       "3)  m = 2,3 kg"],
             atbilde="m = 2,3 kg",
             piezime="1 litrs = 1 dm³ = 10⁻³ m³ — noderīgs pārveidojums."),
        dict(nr=2, virsraksts="Šķidruma atpazīšana",
             teksts="Mērcilindrā ielieti 250 mL šķidruma, tā masa 197,5 g.\n"
                    "Aprēķini blīvumu un nosaki šķidrumu pēc tabulas!",
             dots=["V = 250 mL", "m = 197,5 g"],
             jaaprekina=["ρ = ?"],
             formulas=["ρ = m / V"],
             aprekins=["1)  V = 250 mL = 2,50·10⁻⁴ m³",
                       "2)  m = 197,5 g = 0,1975 kg",
                       "3)  ρ = 0,1975 : 2,50·10⁻⁴ = 790 kg/m³"],
             atbilde="ρ = 790 kg/m³ — šķidrums ir spirts",
             piezime="1 mL = 1 cm³ = 10⁻⁶ m³."),
        dict(nr=3, virsraksts="Slāņošanās secība",
             teksts="Traukā ielej ūdeni (1000), eļļu (920) un dzīvsudrabu "
                    "(13 600 kg/m³).\n"
                    "Kādā secībā tie izvietosies no apakšas uz augšu? Cik "
                    "reižu dzīvsudrabs blīvāks par eļļu?",
             dots=["ρ₁ = 1000 ;  ρ₂ = 920 ;  ρ₃ = 13 600 kg/m³"],
             jaaprekina=["Secība = ?", "n = ?"],
             formulas=["Blīvākais — apakšā", "n = ρ₃ / ρ₂"],
             aprekins=["1)  13 600 > 1000 > 920",
                       "2)  Apakšā dzīvsudrabs, tad ūdens, virsū eļļa",
                       "3)  n = 13 600 : 920 = 14,8"],
             atbilde="Dzīvsudrabs — ūdens — eļļa; n ≈ 15 reižu",
             piezime="Tāpēc dzīvsudrabu izmanto barometros — mazam "
                     "spiedienam pietiek ar īsu stabiņu."),
        dict(nr=4, virsraksts="Maisījuma blīvums",
             teksts="Sajauc 2,0 kg ūdens (1000 kg/m³) un 1,0 kg spirta "
                    "(790 kg/m³).\nAprēķini maisījuma blīvumu, pieņemot, ka "
                    "tilpumi saskaitās!",
             dots=["m₁ = 2,0 kg ;  ρ₁ = 1000 kg/m³",
                   "m₂ = 1,0 kg ;  ρ₂ = 790 kg/m³"],
             jaaprekina=["ρ = ?"],
             formulas=["V = m/ρ", "ρ = (m₁+m₂)/(V₁+V₂)"],
             aprekins=["1)  V₁ = 2,0 : 1000 = 2,0·10⁻³ m³",
                       "2)  V₂ = 1,0 : 790 = 1,27·10⁻³ m³",
                       "3)  V = 3,27·10⁻³ m³ ;  m = 3,0 kg",
                       "4)  ρ = 3,0 : 3,27·10⁻³ = 918 kg/m³"],
             atbilde="ρ ≈ 9,2·10² kg/m³",
             piezime="Rezultāts ir starp 790 un 1000 — tā vienmēr ir "
                     "maisījumam."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "ρ = m/V der arī šķidrumiem; 1 L = 10⁻³ m³, 1 mL = 10⁻⁶ m³.",
            "Nesajaucošies šķidrumi slāņojas: blīvākais apakšā.",
            "Maisījuma blīvumu rēķina ρ = (m₁+m₂)/(V₁+V₂).",
            "Nafta peld uz ūdens, jo tās blīvums ir mazāks.",
        ],
        majasdarbs=[
            "V = 5,0 L ūdens. Aprēķini masu.",
            "m = 340 g, V = 400 mL. Aprēķini blīvumu un nosaki šķidrumu.",
            "Sajauc 1 kg ūdens un 1 kg eļļas (920). Aprēķini maisījuma "
            "blīvumu.",
        ],
        pasvertejums=["Protu lietot ρ = m/V", "Protu pārvērst L un mL",
                      "Protu prognozēt slāņošanos",
                      "Protu aprēķināt maisījuma blīvumu"],
        nakama="Nākamā stunda: spiediens šķidrumā."),
),

dict(
    nr="8.2", virsraksts="Spiediens šķidrumā",
    jautajums="Kāpēc dziļumā spiež stiprāk?",
    apaksraksts="p = ρgh · Hidrostatiskais spiediens · Atmosfēras spiediens",
    merkis="Iemācīties aprēķināt hidrostatisko spiedienu un skaidrot, kāpēc "
           "tas atkarīgs tikai no dziļuma un blīvuma.",
    protu=["lietot p = ρgh;",
           "skaidrot, no kā atkarīgs spiediens šķidrumā;",
           "aprēķināt kopējo spiedienu ar atmosfēras spiedienu;",
           "pamatot dambju un zemūdeņu konstrukciju."],
    atkartojums="7.14. stundā mācījāmies p = F/S. Šķidrumā spiedienu var "
                "izteikt arī caur dziļumu un blīvumu.",
    uzdevumu_apraksts="Hidrostatiskais spiediens",
    teorija=[
        ("Hidrostatiskais spiediens", [
            ("formula", "SPIEDIENS ŠĶIDRUMĀ",
             "p = ρ · g · h        p(kopā) = p₀ + ρgh",
             "ρ — šķidruma blīvums, h — dziļums, p₀ = 1,01·10⁵ Pa — "
             "atmosfēras spiediens. Spiediens NAV atkarīgs no trauka formas "
             "vai šķidruma daudzuma.", GOLD),
            ("kartitas", [
                ("NO KĀ ATKARĪGS", BLUE,
                 ["No dziļuma h.", "No blīvuma ρ.",
                  "No g (uz citas planētas — cits)."]),
                ("NO KĀ NAV ATKARĪGS", RED,
                 ["No trauka formas.", "No šķidruma daudzuma.",
                  "No trauka platuma."]),
                ("VIRZIENS", GREEN,
                 ["Šķidrumā spiediens darbojas",
                  "uz VISĀM pusēm vienādi:",
                  "lejup, augšup un uz sāniem."]),
            ]),
        ]),
        ("Kur to izmanto", [
            ("panelis", "DAMBJI UN ZEMŪDENES",
             ["Dambja siena apakšā vienmēr ir biezāka nekā augšā, jo dziļumā "
              "spiediens ir lielāks. Zemūdenes korpuss jāprojektē tā, lai "
              "izturētu spiedienu darba dziļumā.",
              "Katri 10 m ūdens dziļuma pievieno aptuveni vienu atmosfēras "
              "spiedienu."], NAVY),
            ("tabula",
             ["Dziļums ūdenī", "ρgh, kPa", "Kopā ar atmosfēru, kPa"],
             [["0 m (virspuse)", "0", "101"],
              ["10 m", "98", "199"],
              ["50 m", "491", "592"],
              ["100 m", "981", "1082"]],
             [4.63, 3.30, 4.30]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spiediens baseinā",
             teksts="Baseina dziļums ir 2,5 m, ūdens blīvums 1000 kg/m³, "
                    "g = 9,81 m/s².\nAprēķini hidrostatisko spiedienu pie "
                    "dibena!",
             dots=["h = 2,5 m", "ρ = 1000 kg/m³", "g = 9,81 m/s²"],
             jaaprekina=["p = ?"],
             formulas=["p = ρ · g · h"],
             aprekins=["1)  p = 1000 · 9,81 · 2,5",
                       "2)  p = 2,45·10⁴ Pa"],
             atbilde="p ≈ 2,5·10⁴ Pa = 25 kPa",
             piezime="Tas ir ceturtdaļa no atmosfēras spiediena."),
        dict(nr=2, virsraksts="Kopējais spiediens",
             teksts="Nirējs atrodas 30 m dziļumā jūrā (ρ = 1025 kg/m³). "
                    "p₀ = 1,01·10⁵ Pa.\n"
                    "Aprēķini kopējo spiedienu un cik reižu tas lielāks par "
                    "atmosfēras spiedienu!",
             dots=["h = 30 m", "ρ = 1025 kg/m³", "p₀ = 1,01·10⁵ Pa"],
             jaaprekina=["p = ?", "n = ?"],
             formulas=["p = p₀ + ρgh", "n = p / p₀"],
             aprekins=["1)  ρgh = 1025 · 9,81 · 30 = 3,02·10⁵ Pa",
                       "2)  p = 1,01·10⁵ + 3,02·10⁵ = 4,03·10⁵ Pa",
                       "3)  n = 4,03·10⁵ : 1,01·10⁵ = 4,0"],
             atbilde="p ≈ 4,0·10⁵ Pa ;   n = 4 atmosfēras",
             piezime="Tāpēc nirējiem jāievēro pacelšanās ātrums — citādi "
                     "draud dekompresijas slimība."),
        dict(nr=3, virsraksts="Dziļuma noteikšana",
             teksts="Zemūdenes sensors rāda hidrostatisko spiedienu "
                    "5,9·10⁵ Pa. Jūras ūdens blīvums 1025 kg/m³.\n"
                    "Aprēķini iegremdēšanās dziļumu!",
             dots=["p = 5,9·10⁵ Pa", "ρ = 1025 kg/m³", "g = 9,81 m/s²"],
             jaaprekina=["h = ?"],
             formulas=["p = ρgh", "h = p / (ρ·g)"],
             aprekins=["1)  ρ·g = 1025 · 9,81 = 1,01·10⁴",
                       "2)  h = 5,9·10⁵ : 1,01·10⁴",
                       "3)  h = 59 m"],
             atbilde="h ≈ 59 m",
             piezime="Tieši tā darbojas dziļummērs — tas mēra spiedienu."),
        dict(nr=4, virsraksts="Dzīvsudraba stabiņš",
             teksts="Barometrā dzīvsudraba (13 600 kg/m³) stabiņa augstums "
                    "ir 760 mm.\nAprēķini atmosfēras spiedienu!",
             dots=["h = 760 mm", "ρ = 13 600 kg/m³", "g = 9,81 m/s²"],
             jaaprekina=["p = ?"],
             formulas=["p = ρ · g · h"],
             aprekins=["1)  h = 760 mm = 0,760 m",
                       "2)  p = 13 600 · 9,81 · 0,760",
                       "3)  p = 1,01·10⁵ Pa"],
             atbilde="p ≈ 1,01·10⁵ Pa = 101 kPa",
             piezime="Tieši tā Toričelli pirmoreiz izmērīja atmosfēras "
                     "spiedienu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "p = ρgh — spiediens atkarīgs no dziļuma un blīvuma.",
            "Spiediens NAV atkarīgs no trauka formas vai ūdens daudzuma.",
            "Kopējais spiediens p = p₀ + ρgh; p₀ = 101 kPa.",
            "Katri 10 m ūdens pievieno aptuveni vienu atmosfēru.",
        ],
        majasdarbs=[
            "h = 4,0 m ūdenī. Aprēķini hidrostatisko spiedienu.",
            "p = 2,0·10⁵ Pa jūrā (1025 kg/m³). Aprēķini dziļumu.",
            "Paskaidro, kāpēc dambja siena apakšā ir biezāka.",
        ],
        pasvertejums=["Protu lietot p = ρgh",
                      "Protu skaidrot, no kā spiediens atkarīgs",
                      "Protu rēķināt kopējo spiedienu",
                      "Protu noteikt dziļumu pēc spiediena"],
        nakama="Nākamā stunda: Paskāla likums."),
),

dict(
    nr="8.3", virsraksts="Paskāla likums",
    jautajums="Kā darbojas hidrauliskā prese?",
    apaksraksts="Paskāla likums · Hidrauliskā sistēma · Spēka ieguvums",
    merkis="Iemācīties skaidrot spiediena pārnesi šķidrumā un aprēķināt spēka "
           "ieguvumu hidrauliskā sistēmā.",
    protu=["formulēt Paskāla likumu;",
           "lietot F₁/S₁ = F₂/S₂;",
           "aprēķināt spēka ieguvumu;",
           "nosaukt hidraulisko sistēmu lietojumus."],
    atkartojums="8.2. stundā: šķidrumā spiediens darbojas uz visām pusēm "
                "vienādi. Tieši uz tā balstās hidrauliskās iekārtas.",
    uzdevumu_apraksts="Hidrauliskā prese un spēka ieguvums",
    teorija=[
        ("Paskāla likums", [
            ("formula", "PASKĀLA LIKUMS",
             "p₁ = p₂        F₁ / S₁ = F₂ / S₂        F₂ = F₁ · S₂ / S₁",
             "Uz šķidrumu radītais spiediens tiek pārnests uz visām pusēm "
             "vienādi un nemazināts. Tāpēc mazs spēks uz maza virzuļa dod "
             "lielu spēku uz liela virzuļa.", GOLD),
            ("divi",
             ("SPĒKA IEGUVUMS", BLUE,
              ["n = S₂ / S₁",
               "Ja lielais virzulis ir 100 reižu platāks laukumā,",
               "spēks palielinās 100 reižu.",
               "Bet ceļš samazinās tikpat reižu."]),
             ("KUR IZMANTO", GREEN,
              ["Automašīnas bremzes.",
               "Hidrauliskā prese un domkrats.",
               "Ekskavatora un traktora hidraulika.",
               "Lidmašīnu vadības sistēmas."])),
        ]),
        ("Zelta likums arī šeit", [
            ("panelis", "ENERĢIJU NERADA",
             ["Hidrauliskā sistēma dod spēka ieguvumu, bet ne enerģijas "
              "ieguvumu — tāpat kā svira (7.15. stunda).",
              "Ja spēks palielinās 50 reižu, mazais virzulis jānospiež "
              "50 reižu tālāk: F₁·s₁ = F₂·s₂."], NAVY),
            ("tabula",
             ["Sistēma", "S₁", "S₂", "Ieguvums"],
             [["Domkrats", "2 cm²", "100 cm²", "50 reizes"],
              ["Automašīnas bremzes", "5 cm²", "20 cm²", "4 reizes"],
              ["Prese", "10 cm²", "1000 cm²", "100 reizes"]],
             [4.63, 2.60, 2.60, 2.40]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Hidrauliskais domkrats",
             teksts="Mazā virzuļa laukums ir 4,0 cm², lielā — 200 cm². Uz "
                    "mazo virzuli darbojas spēks 60 N.\n"
                    "Aprēķini spēku uz lielā virzuļa!",
             dots=["S₁ = 4,0 cm²", "S₂ = 200 cm²", "F₁ = 60 N"],
             jaaprekina=["F₂ = ?"],
             formulas=["F₁/S₁ = F₂/S₂", "F₂ = F₁ · S₂ / S₁"],
             aprekins=["1)  S₂ / S₁ = 200 : 4,0 = 50",
                       "2)  F₂ = 60 · 50",
                       "3)  F₂ = 3,0·10³ N"],
             atbilde="F₂ = 3,0 kN — spēka ieguvums 50 reizes",
             piezime="Laukumus var neizteikt m² — svarīga ir tikai to "
                     "attiecība."),
        dict(nr=2, virsraksts="Cik smagu auto var pacelt?",
             teksts="Hidrauliskajā presē S₁ = 5,0 cm², S₂ = 500 cm². Uz mazo "
                    "virzuli darbojas 200 N. g = 9,81 m/s².\n"
                    "Cik lielu masu var pacelt?",
             dots=["S₁ = 5,0 cm² ;  S₂ = 500 cm²", "F₁ = 200 N"],
             jaaprekina=["F₂ = ?", "m = ?"],
             formulas=["F₂ = F₁·S₂/S₁", "m = F₂ / g"],
             aprekins=["1)  S₂/S₁ = 500 : 5,0 = 100",
                       "2)  F₂ = 200 · 100 = 2,0·10⁴ N",
                       "3)  m = 2,0·10⁴ : 9,81 = 2,0·10³ kg"],
             atbilde="F₂ = 20 kN ;   m ≈ 2,0 t",
             piezime="Ar 200 N (kā ~20 kg) var pacelt divas tonnas."),
        dict(nr=3, virsraksts="Ceļa zaudējums",
             teksts="Domkratā spēka ieguvums ir 50 reizes. Lielais virzulis "
                    "jāpaceļ par 2,0 cm.\n"
                    "Cik tālu jānospiež mazais virzulis?",
             dots=["n = 50", "s₂ = 2,0 cm"],
             jaaprekina=["s₁ = ?"],
             formulas=["F₁·s₁ = F₂·s₂", "s₁ = n · s₂"],
             aprekins=["1)  s₁ = 50 · 2,0 cm",
                       "2)  s₁ = 100 cm = 1,0 m"],
             atbilde="s₁ = 1,0 m",
             piezime="Tāpēc domkratu sūknē daudzas reizes — katrs gājiens "
                     "paceļ tikai mazliet."),
        dict(nr=4, virsraksts="Bremžu sistēma",
             teksts="Bremžu pedāļa cilindra laukums ir 3,0 cm², bremžu "
                    "cilindra — 12 cm². Uz pedāli darbojas 150 N.\n"
                    "Aprēķini spēku, ar kādu bremžu kluči spiež uz disku!",
             dots=["S₁ = 3,0 cm² ;  S₂ = 12 cm²", "F₁ = 150 N"],
             jaaprekina=["F₂ = ?"],
             formulas=["F₂ = F₁ · S₂ / S₁"],
             aprekins=["1)  S₂/S₁ = 12 : 3,0 = 4,0",
                       "2)  F₂ = 150 · 4,0",
                       "3)  F₂ = 6,0·10² N"],
             atbilde="F₂ = 600 N",
             piezime="Reālās bremzēs ieguvumu vēl palielina pedāļa svira un "
                     "vakuuma pastiprinātājs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Paskāla likums: spiediens šķidrumā pārnesas uz visām pusēm "
            "vienādi.",
            "F₁/S₁ = F₂/S₂; spēka ieguvums n = S₂/S₁.",
            "Hidraulika dod spēka, bet ne enerģijas ieguvumu.",
            "Lietojumi: bremzes, domkrats, prese, ekskavatora hidraulika.",
        ],
        majasdarbs=[
            "S₁ = 2 cm², S₂ = 80 cm², F₁ = 40 N. Aprēķini F₂.",
            "Ieguvums 25 reizes, lielais virzulis paceļas 3 cm. Cik tālu "
            "jānospiež mazais?",
            "Nosauc trīs hidraulisko sistēmu lietojumus.",
        ],
        pasvertejums=["Protu formulēt Paskāla likumu",
                      "Protu lietot F₁/S₁ = F₂/S₂",
                      "Protu aprēķināt spēka ieguvumu",
                      "Protu pamatot ceļa zaudējumu"],
        nakama="Nākamā stunda: Arhimēda spēks."),
),

dict(
    nr="8.4", virsraksts="Arhimēda spēks",
    jautajums="Kāpēc kuģis peld?",
    apaksraksts="F(A) = ρgV · Peldēšana, grimšana, lidināšanās",
    merkis="Iemācīties aprēķināt cēlējspēku un pamatot peldēšanas, grimšanas "
           "un lidināšanās nosacījumus.",
    protu=["lietot Arhimēda likumu F = ρ·g·V;",
           "salīdzināt cēlējspēku ar smaguma spēku;",
           "pamatot peldēšanas nosacījumu;",
           "skaidrot, kāpēc tērauda kuģis peld."],
    atkartojums="8.2. stundā: dziļumā spiediens lielāks. Tieši spiedienu "
                "starpība uz ķermeņa apakšu un augšu rada cēlējspēku.",
    uzdevumu_apraksts="Cēlējspēks un peldēšanas nosacījumi",
    teorija=[
        ("Arhimēda likums", [
            ("formula", "ARHIMĒDA SPĒKS",
             "F(A) = ρ(šķidruma) · g · V(iegremdētā daļa)",
             "Cēlējspēks ir vienāds ar ķermeņa izspiestā šķidruma svaru. "
             "Uzmanies: formulā ir ŠĶIDRUMA blīvums, nevis ķermeņa!", GOLD),
            ("kartitas", [
                ("PELD", GREEN,
                 ["F(A) > F(smaguma) sākumā",
                  "ρ(ķermeņa) < ρ(šķidruma)",
                  "Ķermenis izpeld un daļēji iegrimst."]),
                ("LIDINĀS", BLUE,
                 ["F(A) = F(smaguma)",
                  "ρ(ķermeņa) = ρ(šķidruma)",
                  "Ķermenis paliek jebkurā dziļumā."]),
                ("GRIMST", RED,
                 ["F(A) < F(smaguma)",
                  "ρ(ķermeņa) > ρ(šķidruma)",
                  "Ķermenis nogrimst līdz dibenam."]),
            ]),
        ]),
        ("Kāpēc tērauda kuģis peld", [
            ("panelis", "VIDĒJAIS BLĪVUMS",
             ["Tērauda blīvums ir 7800 kg/m³ — daudz vairāk nekā ūdenim. Bet "
              "kuģis nav vienlaidus tērauda gabals: tā korpusā ir gaiss.",
              "Kuģa VIDĒJAIS blīvums (tērauds + gaiss) ir mazāks par ūdens "
              "blīvumu, tāpēc tas peld. Zemūdene maina savu vidējo blīvumu, "
              "piepildot vai iztukšojot balasta tvertnes."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Cēlējspēks",
             teksts="Ķermenis ar tilpumu 500 cm³ pilnīgi iegremdēts ūdenī "
                    "(1000 kg/m³). g = 9,81 m/s².\n"
                    "Aprēķini cēlējspēku!",
             dots=["V = 500 cm³", "ρ = 1000 kg/m³", "g = 9,81 m/s²"],
             jaaprekina=["F(A) = ?"],
             formulas=["F(A) = ρ · g · V"],
             aprekins=["1)  V = 500 cm³ = 5,00·10⁻⁴ m³",
                       "2)  F = 1000 · 9,81 · 5,00·10⁻⁴",
                       "3)  F = 4,9 N"],
             atbilde="F(A) ≈ 4,9 N",
             piezime="Tas ir tieši 0,5 kg ūdens svars — cik ķermenis "
                     "izspieda."),
        dict(nr=2, virsraksts="Vai peldēs?",
             teksts="Ķermeņa masa ir 0,40 kg, tilpums 500 cm³. Cēlējspēks "
                    "ūdenī ir 4,9 N.\n"
                    "Aprēķini smaguma spēku un nosaki, vai ķermenis peldēs!",
             dots=["m = 0,40 kg", "F(A) = 4,9 N", "g = 9,81 m/s²"],
             jaaprekina=["F(sm) = ?", "Peld vai grimst?"],
             formulas=["F(sm) = m · g", "Peld, ja F(A) > F(sm)"],
             aprekins=["1)  F(sm) = 0,40 · 9,81 = 3,9 N",
                       "2)  F(A) = 4,9 N > 3,9 N",
                       "3)  Cēlējspēks lielāks → ķermenis izpeld"],
             atbilde="Ķermenis peldēs (F(A) > F(sm))",
             piezime="Pārbaude ar blīvumu: ρ = 0,40 : 5,0·10⁻⁴ = 800 kg/m³ "
                     "< 1000 ✔"),
        dict(nr=3, virsraksts="Iegrimušā daļa",
             teksts="Koka bluķa masa ir 6,0 kg, tilpums 1,0·10⁻² m³. Tas "
                    "peld ūdenī (1000 kg/m³).\n"
                    "Aprēķini iegrimušās daļas tilpumu!",
             dots=["m = 6,0 kg", "V = 1,0·10⁻² m³", "ρ = 1000 kg/m³"],
             jaaprekina=["V(iegr.) = ?"],
             formulas=["Peldot F(A) = F(sm)", "ρ·g·V(iegr.) = m·g"],
             aprekins=["1)  ρ·V(iegr.) = m",
                       "2)  V(iegr.) = 6,0 : 1000",
                       "3)  V(iegr.) = 6,0·10⁻³ m³"],
             atbilde="V(iegr.) = 6,0·10⁻³ m³ — iegrimst 60 % tilpuma",
             piezime="Iegrimušā daļa vienmēr ir ρ(ķermeņa)/ρ(šķidruma) daļa "
                     "no tilpuma."),
        dict(nr=4, virsraksts="Kuģa kravnesība",
             teksts="Kuģis, uzņemot kravu, iegrimst papildus tā, ka izspiestā "
                    "ūdens tilpums palielinās par 2,0·10³ m³. Jūras ūdens "
                    "1025 kg/m³.\nAprēķini kravas masu!",
             dots=["ΔV = 2,0·10³ m³", "ρ = 1025 kg/m³", "g = 9,81 m/s²"],
             jaaprekina=["m = ?"],
             formulas=["F(A) = ρ·g·ΔV", "m = F(A) / g = ρ · ΔV"],
             aprekins=["1)  m = ρ · ΔV",
                       "2)  m = 1025 · 2,0·10³",
                       "3)  m = 2,05·10⁶ kg"],
             atbilde="m ≈ 2,1·10³ t",
             piezime="Tieši tāpēc uz kuģa korpusa ir iegrimes atzīmes — pēc "
                     "tām nosaka kravas daudzumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "F(A) = ρ(šķidruma)·g·V(iegremdētā daļa).",
            "Peld, ja ρ(ķermeņa) < ρ(šķidruma); grimst, ja lielāks.",
            "Peldot cēlējspēks ir vienāds ar smaguma spēku.",
            "Tērauda kuģis peld, jo tā vidējais blīvums ar gaisu ir mazs.",
        ],
        majasdarbs=[
            "V = 200 cm³ ūdenī. Aprēķini cēlējspēku.",
            "m = 1,2 kg, V = 1,0·10⁻³ m³. Vai peldēs ūdenī? Pamato.",
            "Paskaidro, kā zemūdene iegremdējas un uzpeld.",
        ],
        pasvertejums=["Protu lietot Arhimēda likumu",
                      "Protu salīdzināt spēkus",
                      "Protu noteikt peldēšanas nosacījumu",
                      "Protu aprēķināt iegrimušo daļu"],
        nakama="Nākamā stunda: virsmas spraigums un kapilaritāte."),
),

dict(
    nr="8.5", virsraksts="Virsmas spraigums un kapilaritāte",
    jautajums="Kāpēc ūdens veido pilienus?",
    apaksraksts="Virsmas spraigums · Slapināšana · Kapilaritāte",
    merkis="Iemācīties skaidrot virsmas spraigumu, slapināšanu un "
           "kapilaritāti un nosaukt to nozīmi dabā un tehnikā.",
    protu=["skaidrot virsmas spraiguma rašanos;",
           "atšķirt slapinošu un neslapinošu šķidrumu;",
           "skaidrot kapilaritāti un tās nozīmi;",
           "aprēķināt virsmas spraiguma spēku."],
    atkartojums="8.1.–8.4. stundā aplūkojām šķidrumu kā veselumu. Šodien "
                "skatīsim, kas notiek uz tā VIRSMAS.",
    uzdevumu_apraksts="Virsmas spraigums un kapilārā pacelšanās",
    teorija=[
        ("Virsmas spraigums", [
            ("panelis", "KĀPĒC RODAS VIRSMAS SPRAIGUMS",
             ["Molekulu šķidruma iekšienē no visām pusēm velk kaimiņu "
              "molekulas — spēki līdzsvarojas. Uz virsmas kaimiņu no augšas "
              "nav, tāpēc virsmas molekulas tiek vilktas uz iekšu.",
              "Rezultātā virsma uzvedas kā izstiepta plēvīte un tiecas "
              "kļūt pēc iespējas mazāka. Tāpēc piliens ir apaļš — lodei ir "
              "vismazākā virsma pie dotā tilpuma."], NAVY),
            ("formula", "VIRSMAS SPRAIGUMA SPĒKS",
             "F = σ · l        [σ] = N/m",
             "σ — virsmas spraiguma koeficients (ūdenim 0,073 N/m), "
             "l — kontūras garums. Sildot un pievienojot ziepes, σ "
             "samazinās.", GOLD),
        ]),
        ("Slapināšana un kapilaritāte", [
            ("divi",
             ("SLAPINA", BLUE,
              ["Šķidruma molekulas vairāk pievelk cietā viela.",
               "Ūdens uz stikla, spirts uz koka.",
               "Malas paceļas augšup, mensks ieliekts.",
               "Kapilārā šķidrums PACEĻAS."]),
             ("NESLAPINA", RED,
              ["Šķidruma molekulas vairāk pievelk citu citu.",
               "Dzīvsudrabs uz stikla, ūdens uz tauku.",
               "Malas nolaižas, mensks izliekts.",
               "Kapilārā šķidrums NOLAIŽAS."])),
            ("panelis", "KAPILARITĀTE DABĀ UN TEHNIKĀ",
             ["Augi ar kapilāriem paceļ ūdeni no saknēm līdz lapām  ·  "
              "augsne pa kapilāriem paceļ ūdeni uz virsmu  ·  dvielis un "
              "sūklis uzsūc ūdeni  ·  sveces daktī kūstošais vasks paceļas "
              "uz liesmu  ·  būvniecībā izmanto hidroizolāciju, lai "
              "kapilārais mitrums neceltos sienās."], GREEN),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Virsmas spraiguma spēks",
             teksts="Uz 5,0 cm gara stieplīša, kas atrodas uz ūdens virsmas, "
                    "darbojas virsmas spraigums. σ = 0,073 N/m.\n"
                    "Aprēķini spēku! (kontūra abās pusēs: l = 2 · 5,0 cm)",
             dots=["σ = 0,073 N/m", "l = 2 · 5,0 cm"],
             jaaprekina=["F = ?"],
             formulas=["F = σ · l"],
             aprekins=["1)  l = 2 · 0,050 m = 0,10 m",
                       "2)  F = 0,073 · 0,10",
                       "3)  F = 7,3·10⁻³ N"],
             atbilde="F = 7,3·10⁻³ N",
             piezime="Spēks niecīgs, bet ar to pietiek, lai uz ūdens noturētu "
                     "adatu vai ūdensmērītāju."),
        dict(nr=2, virsraksts="Piliena masa",
             teksts="No pipetes ar atveres apkārtmēru 6,0 mm atdalās ūdens "
                    "piliens. σ = 0,073 N/m; g = 9,81 m/s².\n"
                    "Aprēķini piliena masu!",
             dots=["l = 6,0 mm", "σ = 0,073 N/m"],
             jaaprekina=["m = ?"],
             formulas=["F = σ · l", "F = m · g  →  m = σ·l / g"],
             aprekins=["1)  l = 6,0 mm = 6,0·10⁻³ m",
                       "2)  F = 0,073 · 6,0·10⁻³ = 4,4·10⁻⁴ N",
                       "3)  m = 4,4·10⁻⁴ : 9,81 = 4,5·10⁻⁵ kg"],
             atbilde="m ≈ 4,5·10⁻⁵ kg = 45 mg",
             piezime="Piliens atdalās tieši tad, kad tā svars pārsniedz "
                     "virsmas spraiguma spēku."),
        dict(nr=3, virsraksts="Kapilārā pacelšanās",
             teksts="Ūdens kapilārā ar rādiusu 0,20 mm paceļas augstumā "
                    "h = 2σ/(ρgr). σ = 0,073 N/m; ρ = 1000 kg/m³.\n"
                    "Aprēķini pacelšanās augstumu!",
             dots=["r = 0,20 mm", "σ = 0,073 N/m", "ρ = 1000 kg/m³"],
             jaaprekina=["h = ?"],
             formulas=["h = 2σ / (ρ·g·r)"],
             aprekins=["1)  r = 2,0·10⁻⁴ m",
                       "2)  ρ·g·r = 1000 · 9,81 · 2,0·10⁻⁴ = 1,96",
                       "3)  h = 2 · 0,073 : 1,96 = 0,0745 m"],
             atbilde="h ≈ 7,5 cm",
             piezime="Jo šaurāks kapilārs, jo augstāk ūdens paceļas."),
        dict(nr=4, virsraksts="Divi kapilāri",
             teksts="Vienā kapilārā ūdens paceļas 8,0 cm augstu. Otrā "
                    "kapilārā rādiuss ir 4 reizes mazāks.\n"
                    "Cik augstu ūdens paceļas otrajā kapilārā?",
             dots=["h₁ = 8,0 cm", "r₂ = r₁ / 4"],
             jaaprekina=["h₂ = ?"],
             formulas=["h ~ 1/r", "h₂ = h₁ · r₁ / r₂"],
             aprekins=["1)  h ir apgriezti proporcionāls r",
                       "2)  h₂ = 8,0 · 4",
                       "3)  h₂ = 32 cm"],
             atbilde="h₂ = 32 cm",
             piezime="Tāpēc augsti koki spēj pacelt ūdeni — to kapilāri ir "
                     "ļoti šauri."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Virsmas spraigums rodas, jo virsmas molekulas velk uz iekšu.",
            "F = σ·l; ūdenim σ = 0,073 N/m.",
            "Slapinošs šķidrums kapilārā paceļas, neslapinošs — nolaižas.",
            "Jo šaurāks kapilārs, jo augstāk šķidrums paceļas (h ~ 1/r).",
        ],
        majasdarbs=[
            "σ = 0,073 N/m, l = 0,20 m. Aprēķini spēku.",
            "Kapilārā r = 0,50 mm. Aprēķini pacelšanās augstumu.",
            "Nosauc trīs kapilaritātes piemērus dabā un divus tehnikā.",
        ],
        pasvertejums=["Protu skaidrot virsmas spraigumu",
                      "Protu lietot F = σl",
                      "Protu atšķirt slapināšanu",
                      "Protu skaidrot kapilaritāti"],
        nakama="Nākamā stunda: kombinētie uzdevumi par šķidrumiem."),
),

dict(
    nr="8.6", virsraksts="Uzdevumi par šķidrumiem",
    jautajums="Kā apvienot blīvumu, spiedienu un cēlējspēku?",
    apaksraksts="Nostiprināšana · Kombinētie uzdevumi",
    merkis="Nostiprināt temata saturu, risinot uzdevumus, kuros jāapvieno "
           "blīvums, hidrostatiskais spiediens un Arhimēda spēks.",
    protu=["izvēlēties pareizo formulu situācijai;",
           "apvienot divas vai trīs sakarības vienā risinājumā;",
           "pārbaudīt mērvienības un rezultāta ticamību;",
           "pamatot atbildi ar fizikālu skaidrojumu."],
    atkartojums="Temata formulas: ρ = m/V, p = ρgh, F₁/S₁ = F₂/S₂, "
                "F(A) = ρgV, F = σl.",
    uzdevumu_apraksts="Kombinētie uzdevumi par šķidrumiem",
    teorija=[
        ("Temata formulas vienuviet", [
            ("tabula",
             ["Kas jāatrod", "Formula", "Kur lieto"],
             [["Blīvums, masa, tilpums", "ρ = m / V", "vielas atpazīšana"],
              ["Spiediens šķidrumā", "p = ρ · g · h", "dziļums, dambji"],
              ["Kopējais spiediens", "p = p₀ + ρgh", "nirēji, zemūdenes"],
              ["Hidraulika", "F₁/S₁ = F₂/S₂", "prese, bremzes"],
              ["Cēlējspēks", "F(A) = ρ · g · V", "peldēšana"],
              ["Virsmas spraigums", "F = σ · l", "pilieni, kapilāri"]],
             [3.63, 4.60, 4.00]),
        ]),
        ("Kā risina kombinētu uzdevumu", [
            ("kartitas", [
                ("1. IZLASI UN ZĪMĒ", BLUE,
                 ["Uzzīmē situāciju.",
                  "Atzīmē, kas dots un kas jāatrod.",
                  "Nosaki, kurš šķidrums un kurš ķermenis."]),
                ("2. IZVĒLIES CEĻU", GREEN,
                 ["Kura formula ved uz atbildi?",
                  "Vai vajag starprezultātu?",
                  "Piemēram, vispirms masu, tad spēku."]),
                ("3. PĀRBAUDI", GOLD,
                 ["Vai mērvienības sakrīt?",
                  "Vai atbilde ir saprātīga?",
                  "Vai ρ ir šķidruma vai ķermeņa?"]),
            ]),
            ("panelis", "BIEŽĀKĀS KĻŪDAS",
             ["Arhimēda formulā lieto ķermeņa blīvumu šķidruma vietā  ·  "
              "cm³ un mL nepārvērš m³  ·  aizmirst pieskaitīt atmosfēras "
              "spiedienu  ·  hidraulikā sajauc S₁ un S₂  ·  atbildē trūkst "
              "mērvienības."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Blīvums un cēlējspēks",
             teksts="Ķermeņa masa gaisā ir 2,7 kg, tilpums 1,0·10⁻³ m³.\n"
                    "Aprēķini blīvumu, cēlējspēku ūdenī un nosaki, vai "
                    "ķermenis grims!",
             dots=["m = 2,7 kg", "V = 1,0·10⁻³ m³", "ρ(ū) = 1000 kg/m³"],
             jaaprekina=["ρ = ?", "F(A) = ?", "Grims?"],
             formulas=["ρ = m/V", "F(A) = ρ(ū)·g·V", "F(sm) = m·g"],
             aprekins=["1)  ρ = 2,7 : 1,0·10⁻³ = 2700 kg/m³",
                       "2)  F(A) = 1000 · 9,81 · 1,0·10⁻³ = 9,8 N",
                       "3)  F(sm) = 2,7 · 9,81 = 26,5 N",
                       "4)  F(sm) > F(A) → grims"],
             atbilde="ρ = 2700 kg/m³ (alumīnijs); F(A) = 9,8 N; grims",
             piezime="Tas pats secinājums no blīvumiem: 2700 > 1000."),
        dict(nr=2, virsraksts="Spiediens un spēks uz lūku",
             teksts="Zemūdenes lūkas laukums ir 0,50 m², tā atrodas 40 m "
                    "dziļumā jūrā (1025 kg/m³).\n"
                    "Aprēķini hidrostatisko spiedienu un spēku uz lūku!",
             dots=["S = 0,50 m²", "h = 40 m", "ρ = 1025 kg/m³"],
             jaaprekina=["p = ?", "F = ?"],
             formulas=["p = ρ·g·h", "F = p · S"],
             aprekins=["1)  p = 1025 · 9,81 · 40 = 4,02·10⁵ Pa",
                       "2)  F = 4,02·10⁵ · 0,50",
                       "3)  F = 2,0·10⁵ N"],
             atbilde="p ≈ 4,0·10⁵ Pa ;   F = 2,0·10⁵ N = 200 kN",
             piezime="200 kN atbilst ~20 tonnu svaram — tāpēc lūkas ir tik "
                     "masīvas."),
        dict(nr=3, virsraksts="Plosts",
             teksts="Plosts no koka (600 kg/m³) ar tilpumu 1,5 m³ peld ūdenī "
                    "(1000 kg/m³).\n"
                    "Aprēķini plosta masu un maksimālo kravu, ko tas var "
                    "nest!",
             dots=["V = 1,5 m³", "ρ(k) = 600 kg/m³", "ρ(ū) = 1000 kg/m³"],
             jaaprekina=["m = ?", "m(kr) = ?"],
             formulas=["m = ρ(k)·V", "F(A,max) = ρ(ū)·g·V"],
             aprekins=["1)  m = 600 · 1,5 = 900 kg",
                       "2)  Maks. izspiestā masa = 1000 · 1,5 = 1500 kg",
                       "3)  m(kr) = 1500 − 900 = 600 kg"],
             atbilde="m = 9,0·10² kg ;   m(kr) = 6,0·10² kg",
             piezime="Ar pilnu kravu plosts iegrimtu tieši līdz malai."),
        dict(nr=4, virsraksts="Hidrauliskās bremzes un spiediens",
             teksts="Bremžu sistēmā S₁ = 4,0 cm², S₂ = 16 cm², F₁ = 200 N.\n"
                    "Aprēķini spiedienu šķidrumā un spēku uz lielā virzuļa!",
             dots=["S₁ = 4,0 cm² ;  S₂ = 16 cm²", "F₁ = 200 N"],
             jaaprekina=["p = ?", "F₂ = ?"],
             formulas=["p = F₁ / S₁", "F₂ = p · S₂"],
             aprekins=["1)  S₁ = 4,0·10⁻⁴ m²",
                       "2)  p = 200 : 4,0·10⁻⁴ = 5,0·10⁵ Pa",
                       "3)  S₂ = 1,6·10⁻³ m²",
                       "4)  F₂ = 5,0·10⁵ · 1,6·10⁻³ = 8,0·10² N"],
             atbilde="p = 5,0·10⁵ Pa ;   F₂ = 800 N",
             piezime="Caur spiedienu risinot, iznāk tas pats, kas ar "
                     "F₁/S₁ = F₂/S₂."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Šķidrumu uzdevumos gandrīz vienmēr sākas ar ρ = m/V.",
            "p = ρgh dod spiedienu, F = pS — spēku uz virsmu.",
            "Arhimēda formulā lieto ŠĶIDRUMA blīvumu.",
            "Kombinētos uzdevumos risina pa soļiem, ar starprezultātiem.",
        ],
        majasdarbs=[
            "Atkārto 8.1.–8.5. stundas formulas.",
            "m = 5,0 kg, V = 2,0·10⁻³ m³. Aprēķini ρ un noskaidro, vai "
            "peldēs.",
            "h = 25 m jūrā, S = 0,20 m². Aprēķini p un F.",
        ],
        pasvertejums=["Protu izvēlēties formulu",
                      "Protu apvienot vairākas sakarības",
                      "Protu pārbaudīt mērvienības",
                      "Protu pamatot atbildi"],
        nakama="Nākamā stunda: 9. temats — troksnis un apgaismojums."),
),
]

ST9 = [

dict(
    nr="9.1", virsraksts="Troksnis un apgaismojums",
    jautajums="Kad skaņa un gaisma kļūst kaitīgas?",
    apaksraksts="Skaņas skaļums dB · Apgaismojums · Darba vide",
    merkis="Iemācīties raksturot skaņas skaļumu decibelos un apgaismojuma "
           "atkarību no attāluma un izvērtēt darba vietas kvalitāti.",
    protu=["raksturot skaņas skaļumu decibelos;",
           "izvērtēt trokšņa ietekmi uz veselību;",
           "lietot apgaismojuma atkarību no attāluma;",
           "novērtēt darba vietas apgaismojumu."],
    atkartojums="3.8. stundā lietojām attāluma kvadrāta likumu starojumam. "
                "Tas pats likums der arī skaņai un gaismai.",
    uzdevumu_apraksts="Trokšņa līmenis un apgaismojums",
    teorija=[
        ("Skaņa un troksnis", [
            ("panelis", "SKAĻUMA LĪMENIS",
             ["Skaļumu mēra decibelos (dB). Skala ir logaritmiska: katri "
              "+10 dB nozīmē 10 reižu lielāku skaņas intensitāti, bet ausij "
              "— aptuveni divreiz skaļāku skaņu.",
              "Tāpēc 90 dB nav “nedaudz skaļāk” par 80 dB, bet 10 reižu "
              "intensīvāk."], NAVY),
            ("tabula",
             ["Skaņas avots", "Līmenis, dB", "Ietekme"],
             [["Čuksti", "30", "nekaitīgi"],
              ["Saruna", "60", "nekaitīgi"],
              ["Satiksme uz ielas", "80", "nogurdina"],
              ["Skaļa mūzika austiņās", "100", "bojā dzirdi pēc 15 min"],
              ["Lidmašīnas dzinējs 50 m", "120", "sāpju slieksnis"]],
             [4.63, 3.30, 4.30]),
        ]),
        ("Apgaismojums", [
            ("formula", "APGAISMOJUMS UN ATTĀLUMS",
             "E = I / r²        E₁ · r₁² = E₂ · r₂²",
             "E — apgaismojums [lx], I — gaismas stiprums [cd], r — "
             "attālums. Divreiz tālāk no lampas — četrreiz mazāks "
             "apgaismojums.", GOLD),
            ("divi",
             ("NORMAS DARBAM", BLUE,
              ["Gaitenis: 100 lx",
               "Klase, birojs: 300–500 lx",
               "Precīzs darbs, rasēšana: 750–1000 lx",
               "Par mazu apgaismojumu — nogurst acis."]),
             ("KĀ UZLABOT", GREEN,
              ["Novietot gaismas avotu tuvāk.",
               "Izmantot vairākus avotus.",
               "Izvairīties no ēnas un atspīduma.",
               "Gaisma no kreisās puses labročiem."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Apgaismojums pie galda",
             teksts="Lampas gaismas stiprums ir 120 cd, tā atrodas 1,5 m "
                    "virs galda.\nAprēķini apgaismojumu uz galda!",
             dots=["I = 120 cd", "r = 1,5 m"],
             jaaprekina=["E = ?"],
             formulas=["E = I / r²"],
             aprekins=["1)  r² = 1,5² = 2,25 m²",
                       "2)  E = 120 : 2,25",
                       "3)  E = 53 lx"],
             atbilde="E ≈ 53 lx — par maz mācību darbam",
             piezime="Klasē vajag 300–500 lx, tātad lampa jānolaiž zemāk vai "
                     "jāizvēlas spēcīgāka."),
        dict(nr=2, virsraksts="Lampu pietuvina",
             teksts="Lampu no 1,5 m nolaiž līdz 0,75 m virs galda.\n"
                    "Cik reižu palielinās apgaismojums?",
             dots=["r₁ = 1,5 m", "r₂ = 0,75 m"],
             jaaprekina=["n = ?"],
             formulas=["E ~ 1/r²", "n = (r₁/r₂)²"],
             aprekins=["1)  r₁ / r₂ = 1,5 : 0,75 = 2",
                       "2)  n = 2² = 4"],
             atbilde="n = 4 reizes",
             piezime="Attālumu samazinot divreiz, apgaismojums palielinās "
                     "četrreiz."),
        dict(nr=3, virsraksts="Vajadzīgais gaismas stiprums",
             teksts="Uz darba galda 1,2 m attālumā jānodrošina 400 lx.\n"
                    "Aprēķini nepieciešamo lampas gaismas stiprumu!",
             dots=["E = 400 lx", "r = 1,2 m"],
             jaaprekina=["I = ?"],
             formulas=["E = I / r²", "I = E · r²"],
             aprekins=["1)  r² = 1,2² = 1,44 m²",
                       "2)  I = 400 · 1,44",
                       "3)  I = 5,8·10² cd"],
             atbilde="I ≈ 5,8·10² cd",
             piezime="Praksē izvēlas lampu ar atbilstošu gaismas plūsmu "
                     "lūmenos."),
        dict(nr=4, virsraksts="Trokšņa intensitāte",
             teksts="Trokšņa līmenis pieaug no 60 dB līdz 90 dB.\n"
                    "Cik reižu palielinās skaņas intensitāte? (katri 10 dB → "
                    "10 reizes)",
             dots=["L₁ = 60 dB", "L₂ = 90 dB"],
             jaaprekina=["n = ?"],
             formulas=["ΔL = L₂ − L₁", "n = 10^(ΔL/10)"],
             aprekins=["1)  ΔL = 90 − 60 = 30 dB",
                       "2)  30 : 10 = 3",
                       "3)  n = 10³ = 1000"],
             atbilde="n = 1000 reižu",
             piezime="Tāpēc, strādājot 90 dB troksnī, obligāti jālieto "
                     "dzirdes aizsargi."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Skaļumu mēra decibelos; katri +10 dB ir 10 reižu lielāka "
            "intensitāte.",
            "Virs 85 dB ilgstošs troksnis bojā dzirdi.",
            "E = I/r²; divreiz tālāk — četrreiz mazāks apgaismojums.",
            "Mācību darbam vajag 300–500 lx.",
        ],
        majasdarbs=[
            "I = 200 cd, r = 2,0 m. Aprēķini apgaismojumu.",
            "Troksnis pieaug no 50 līdz 80 dB. Cik reižu aug intensitāte?",
            "Novērtē savu darba vietu mājās: kāds ir apgaismojums un kā to "
            "uzlabot?",
        ],
        pasvertejums=["Protu raksturot skaļumu dB",
                      "Protu lietot E = I/r²",
                      "Protu aprēķināt vajadzīgo gaismas stiprumu",
                      "Protu izvērtēt darba vietu"],
        nakama="Nākamā stunda: starojums vidē."),
),

dict(
    nr="9.2", virsraksts="Starojums vidē",
    jautajums="Kurš starojums ir bīstams?",
    apaksraksts="UV starojums · Elektromagnētiskais starojums · Avotu "
                "izvērtēšana",
    merkis="Iemācīties nošķirt jonizējošu starojumu no nejonizējoša, "
           "izvērtēt to ietekmi uz veselību un pārbaudīt informācijas avota "
           "ticamību.",
    protu=["nošķirt jonizējošu un nejonizējošu starojumu;",
           "salīdzināt UV, rentgena un radioviļņu ietekmi;",
           "pamatot aizsardzības līdzekļu izvēli;",
           "izvērtēt apgalvojuma ticamību un avotu."],
    atkartojums="3.7. stundā mācījāmies par jonizējošo starojumu un devām. "
                "Šodien salīdzināsim visu starojumu veidu ietekmi uz "
                "cilvēku.",
    uzdevumu_apraksts="Starojuma devas, UV indekss un aizsardzība",
    teorija=[
        ("Jonizējošs un nejonizējošs starojums", [
            ("tabula",
             ["Starojums", "Veids", "Ietekme", "Aizsardzība"],
             [["Radioviļņi, mikroviļņi", "nejonizējošs", "sasilda audus",
               "attālums, jaudas ierobežojumi"],
              ["Redzamā gaisma", "nejonizējošs", "nekaitīga",
               "spilgtumā — saulesbrilles"],
              ["UV-A un UV-B", "nejonizējošs", "apdegumi, ādas vēzis",
               "krēms, apģērbs, ēna"],
              ["Rentgens, gamma", "jonizējošs", "bojā DNS",
               "svins, attālums, laiks"]],
             [3.43, 2.60, 3.10, 3.10]),
            ("panelis", "GALVENĀ ATŠĶIRĪBA",
             ["Jonizējošs starojums spēj izsist elektronu no atoma un tieši "
              "bojāt DNS. Nejonizējošs starojums to nespēj — tas var tikai "
              "sasildīt audus.",
              "Tāpēc mobilā tālruņa radioviļņi un rentgena starojums NAV "
              "salīdzināmi pēc bīstamības."], NAVY),
        ]),
        ("UV starojums un avotu izvērtēšana", [
            ("divi",
             ("UV INDEKSS", GOLD,
              ["0–2 zems: aizsardzība nav vajadzīga.",
               "3–5 mērens: krēms SPF 30.",
               "6–7 augsts: krēms, cepure, ēna.",
               "8+ ļoti augsts: izvairīties 11–15."]),
             ("KĀ IZVĒRTĒT APGALVOJUMU", GREEN,
              ["Kas ir avots — zinātnieks vai reklāma?",
               "Vai ir mērījumi un skaitļi?",
               "Vai citi avoti apstiprina?",
               "Vai secinājums izriet no datiem?"])),
            ("panelis", "PIEMĒRS — KĀ PĀRBAUDĪT ZIŅU",
             ["Apgalvojums “5G tornis rada radiāciju un izraisa slimības”. "
              "Pārbaudi: 5G izmanto radioviļņus — nejonizējošu starojumu, "
              "kura enerģija ir miljoniem reižu mazāka nekā rentgenam.",
              "Tātad apgalvojums sajauc divus dažādus starojuma veidus. "
              "Uzticams avots būtu mērījumi ar norādītu jaudas blīvumu "
              "W/m² un salīdzinājums ar normu."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Fotona enerģijas salīdzinājums",
             teksts="Radioviļņa frekvence ir 1,0·10⁹ Hz, rentgenstarojuma — "
                    "1,0·10¹⁸ Hz. h = 6,63·10⁻³⁴ J·s.\n"
                    "Cik reižu rentgena fotona enerģija ir lielāka?",
             dots=["f₁ = 1,0·10⁹ Hz", "f₂ = 1,0·10¹⁸ Hz"],
             jaaprekina=["n = ?"],
             formulas=["E = h·f", "n = E₂/E₁ = f₂/f₁"],
             aprekins=["1)  E₁ = 6,63·10⁻³⁴ · 1,0·10⁹ = 6,6·10⁻²⁵ J",
                       "2)  E₂ = 6,63·10⁻³⁴ · 1,0·10¹⁸ = 6,6·10⁻¹⁶ J",
                       "3)  n = 10¹⁸ : 10⁹ = 10⁹"],
             atbilde="n = 10⁹ — miljardu reižu lielāka",
             piezime="Tieši tāpēc rentgens jonizē atomus, bet radioviļņi — "
                     "nespēj."),
        dict(nr=2, virsraksts="Saules aizsargkrēms",
             teksts="Bez aizsardzības āda apdeg 15 minūtēs. Krēms ar SPF 30 "
                    "pagarina šo laiku 30 reižu.\n"
                    "Cik ilgi var uzturēties saulē ar krēmu? Izsaki "
                    "stundās.",
             dots=["t₀ = 15 min", "SPF = 30"],
             jaaprekina=["t = ?  (h)"],
             formulas=["t = t₀ · SPF"],
             aprekins=["1)  t = 15 min · 30 = 450 min",
                       "2)  t = 450 : 60 = 7,5 h"],
             atbilde="t = 7,5 h",
             piezime="Praksē krēms jāatjauno ik pēc 2 h, jo tas nodilst un "
                     "noskalojas."),
        dict(nr=3, virsraksts="UV intensitāte kalnos",
             teksts="Katri 1000 m augstuma palielina UV intensitāti par "
                    "10 %.\nCik reižu tā ir lielāka 3000 m augstumā "
                    "salīdzinājumā ar jūras līmeni?",
             dots=["pieaugums 10 % uz 1000 m", "h = 3000 m"],
             jaaprekina=["n = ?"],
             formulas=["n = 1,10^(h/1000)"],
             aprekins=["1)  h / 1000 = 3",
                       "2)  n = 1,10³",
                       "3)  n = 1,33"],
             atbilde="n ≈ 1,3 reizes lielāka",
             piezime="Kalnos un uz sniega UV ir daudz stiprāks — tāpēc "
                     "slēpotāji lieto krēmu un brilles."),
        dict(nr=4, virsraksts="Mikroviļņu jaudas blīvums",
             teksts="Raidītāja jauda ir 20 W, tā izstaro vienmērīgi uz visām "
                    "pusēm. Norma ir 10 W/m².\n"
                    "Aprēķini jaudas blīvumu 2,0 m attālumā! "
                    "(S = 4πr²; vai norma pārsniegta?)",
             dots=["P = 20 W", "r = 2,0 m", "norma 10 W/m²"],
             jaaprekina=["I = ?"],
             formulas=["S = 4·π·r²", "I = P / S"],
             aprekins=["1)  S = 4 · 3,14 · 2,0² = 50,2 m²",
                       "2)  I = 20 : 50,2",
                       "3)  I = 0,40 W/m²"],
             atbilde="I ≈ 0,40 W/m² — 25 reizes zem normas",
             piezime="Šāds aprēķins ļauj pārbaudīt apgalvojumus par "
                     "raidītāju bīstamību."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Jonizējošs starojums izsit elektronus un bojā DNS; "
            "nejonizējošs — tikai sasilda.",
            "Fotona enerģija E = hf: jo lielāka frekvence, jo bīstamāks "
            "starojums.",
            "UV aizsardzība: krēms, apģērbs, ēna; SPF pagarina drošo laiku.",
            "Apgalvojumu izvērtē pēc avota, mērījumiem un salīdzinājuma ar "
            "normu.",
        ],
        majasdarbs=[
            "f = 5,0·10¹⁴ Hz. Aprēķini fotona enerģiju.",
            "t₀ = 20 min, SPF 15. Cik ilgi var būt saulē?",
            "P = 50 W, r = 5,0 m. Aprēķini jaudas blīvumu un salīdzini ar "
            "10 W/m².",
        ],
        pasvertejums=["Protu nošķirt starojuma veidus",
                      "Protu salīdzināt fotona enerģijas",
                      "Protu pamatot aizsardzību",
                      "Protu izvērtēt avota ticamību"],
        nakama="Nākamā stunda: PD6 — Šķidrumi un vides fizikālie faktori."),
),
]


def build():
    a = C.build_theme(T8, K8, M8, ST8)
    b = C.build_theme(T9, K9, M9, ST9)
    return a + b


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
