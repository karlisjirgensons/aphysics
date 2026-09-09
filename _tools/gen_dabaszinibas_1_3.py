# -*- coding: utf-8 -*-
"""
1.3. stunda: Fizikālie lielumi un SI — "Kāpēc visā pasaulē mēra vienādi?"
Plāns: 10.1. temata 3. stunda.
SR: lieto SI pamatvienības, priedēkļus un standartformu; pārvērš mērvienības
un pārbauda rezultāta ticamību.
"""

import sys
import dz_common as C
from dz_common import (MX, CW, NAVY, BLUE, GOLD, LIGHTGOLD, GREY, RED,
                       GREEN, WHITE, PP_ALIGN, blank, box, put, panel,
                       header, footer, tabula)

META = dict(
    temats="1. temats. Pasaule ap mums un tās pētīšana",
    kicker=("DABASZINĪBAS · 10. KLASE · 1. TEMATS: PASAULE AP MUMS UN "
            "TĀS PĒTĪŠANA"),
    stunda="1.3. stunda",
    virsraksts="Fizikālie lielumi un SI mērvienības",
    jautajums="Kāpēc visā pasaulē mēra vienādi?",
    apaksraksts="SI pamatvienības · Atvasinātās vienības · Priedēkļi · "
                "Mērvienību pārveidošana",
    foot="1.3. Fizikālie lielumi un SI mērvienības",
    merkis="Iemācīties pierakstīt fizikālos lielumus SI mērvienībās, lietot "
           "priedēkļus un standartformu un pārbaudīt aprēķina rezultāta "
           "ticamību pēc mērvienībām.",
    protu=[
        "nosaukt SI pamatvienības un to apzīmējumus;",
        "izteikt atvasinātās vienības ar pamatvienībām;",
        "pārvērst mērvienības, lietojot priedēkļus un standartformu;",
        "pārbaudīt atbildi pēc mērvienībām un novērtēt tās ticamību.",
    ],
    atkartojums="1.2. stundā mācījāmies izmēru kārtas 10ⁿ un standartformu. "
                "Šodien to pašu pierakstu lietosim visiem fizikālajiem "
                "lielumiem.",
    uzdevumu_apraksts="Mērvienību pārveidošana un aprēķini",
)


def s_lielums(prs):
    s = blank(prs)
    header(s, "Kas ir fizikāls lielums?")

    panel(s, MX, 1.20, CW, 1.10, [
        {"t": "FIZIKĀLS LIELUMS — dabas objekta vai parādības īpašība, ko "
              "var izmērīt.", "size": 20, "bold": True, "color": NAVY},
        {"t": "Katru mērījuma rezultātu pieraksta kā SKAITLIS × MĒRVIENĪBA "
              "— skaitlis bez mērvienības fizikā nav atbilde.",
         "size": 17, "space": 6, "color": GREY},
    ], accent=NAVY)

    C.kartitas(s, 2.46, 1.90, [
        ("m = 540 g", BLUE,
         ["m — lieluma apzīmējums", "540 — skaitliskā vērtība",
          "g — mērvienība"]),
        ("Apzīmējumus raksta slīpi", GOLD,
         ["Lielums: m, V, t, s, υ", "Mērvienība: kg, m³, s, m, m/s",
          "Tā ir latviešu standarta prasība"]),
        ("Bez mērvienības nav atbildes", RED,
         ["“Blīvums ir 2700” — nepareizi", "ρ = 2700 kg/m³ — pareizi",
          "Mērvienība maina jēgu"]),
    ])

    put(s, MX, 4.56, CW, 0.30,
        [{"t": "SI SISTĒMAS 7 PAMATVIENĪBAS — visas pārējās veidojas no "
               "tām:", "size": 16, "bold": True, "color": NAVY}],
        autofit=False)
    tabula(s, MX, 4.92, CW,
           ["Lielums", "Apz.", "Vienība", "Simb.", "Lielums", "Apz.",
            "Vienība", "Simb."],
           [["garums", "l, s", "metrs", "m", "temperatūra", "T", "kelvins",
             "K"],
            ["masa", "m", "kilograms", "kg", "vielas daudzums", "n", "mols",
             "mol"],
            ["laiks", "t", "sekunde", "s", "gaismas stiprums", "Iᵥ",
             "kandela", "cd"],
            ["strāvas stiprums", "I", "ampērs", "A", "", "", "", ""]],
           [2.35, 0.85, 1.60, 0.78, 2.55, 0.80, 1.60, 1.70],
           rowh=0.46, size=15, hsize=12)
    footer(s)
    return s


def s_atvasinatas(prs):
    s = blank(prs)
    header(s, "Atvasinātās vienības — no kā tās sastāv")

    put(s, MX, 1.16, CW, 0.30,
        [{"t": "Katru atvasināto vienību var izteikt ar pamatvienībām. Tas "
               "ļauj pārbaudīt, vai aprēķins ir pareizs:", "size": 17,
          "color": GREY}], autofit=False)

    tabula(s, MX, 1.56, CW,
           ["Lielums", "Formula", "Vienība", "Izteikts pamatvienībās"],
           [["ātrums υ", "υ = s / t", "m/s", "m · s⁻¹"],
            ["paātrinājums a", "a = Δυ / Δt", "m/s²", "m · s⁻²"],
            ["blīvums ρ", "ρ = m / V", "kg/m³", "kg · m⁻³"],
            ["spēks F", "F = m · a", "ņūtons (N)", "kg · m · s⁻²"],
            ["spiediens p", "p = F / S", "paskāls (Pa)", "kg · m⁻¹ · s⁻²"],
            ["darbs A, enerģija E", "A = F · s", "džouls (J)",
             "kg · m² · s⁻²"],
            ["jauda P", "P = A / t", "vats (W)", "kg · m² · s⁻³"]],
           [3.30, 2.60, 2.60, 3.73], rowh=0.50, size=16, hsize=13)

    panel(s, MX, 5.42, CW, 1.48, [
        {"t": "MĒRVIENĪBU PĀRBAUDE — kā pārliecināties, ka formula lietota "
              "pareizi", "size": 12, "bold": True, "color": GOLD},
        {"t": "ρ = m / V  →  kg : m³ = kg/m³  ✔      "
              "p = F / S  →  N : m² = N/m² = Pa  ✔", "size": 20,
         "bold": True, "space": 8, "color": NAVY,
         "align": PP_ALIGN.CENTER},
        {"t": "Ja, ievietojot mērvienības, iznāk cita vienība, nekā "
              "vajadzīgs, — formula vai pārveidojums ir kļūdains.",
         "size": 16, "space": 8, "color": GREY, "align": PP_ALIGN.CENTER},
    ], accent=GOLD, fill=LIGHTGOLD)
    return s


def s_parveide(prs):
    s = blank(prs)
    header(s, "Kā pārvērš mērvienības")

    colw = (CW - 0.38) / 2
    panel(s, MX, 1.20, colw, 2.66, [
        {"t": "PRIEDĒKĻI — biežāk lietotie", "size": 13, "bold": True,
         "color": BLUE},
        {"t": "k (kilo) = 10³        M (mega) = 10⁶", "size": 19,
         "space": 10},
        {"t": "c (centi) = 10⁻²      m (mili) = 10⁻³", "size": 19,
         "space": 6},
        {"t": "µ (mikro) = 10⁻⁶      n (nano) = 10⁻⁹", "size": 19,
         "space": 6},
        {"t": "Priedēkli aizstāj ar pakāpi un rēķina tālāk.", "size": 15,
         "space": 10, "color": GREY},
    ], accent=BLUE)

    panel(s, MX + colw + 0.38, 1.20, colw, 2.66, [
        {"t": "LAUKUMS UN TILPUMS — uzmanies!", "size": 13, "bold": True,
         "color": RED},
        {"t": "1 cm = 10⁻² m", "size": 19, "space": 10},
        {"t": "1 cm² = (10⁻²)² m² = 10⁻⁴ m²", "size": 19, "space": 6},
        {"t": "1 cm³ = (10⁻²)³ m³ = 10⁻⁶ m³", "size": 19, "space": 6},
        {"t": "Pakāpi kāpina tikpat reižu, cik mērvienību!", "size": 15,
         "space": 10, "color": GREY},
    ], accent=RED)

    put(s, MX, 4.04, CW, 0.30,
        [{"t": "TRĪS BIEŽĀKIE PĀRVEIDOJUMI — iemācies tos no galvas:",
          "size": 16, "bold": True, "color": NAVY}], autofit=False)

    C.kartitas(s, 4.42, 1.36, [
        ("g → kg", BLUE, ["540 g = 540 · 10⁻³ kg", "= 0,54 kg"]),
        ("cm³ → m³", BLUE, ["200 cm³ = 200 · 10⁻⁶ m³", "= 2 · 10⁻⁴ m³"]),
        ("km/h → m/s", BLUE, ["72 km/h = 72 : 3,6", "= 20 m/s"]),
    ])

    panel(s, MX, 5.98, CW, 0.92, [
        {"t": "Kāpēc dala ar 3,6:  1 km/h = 1000 m : 3600 s = 1/3,6 m/s. "
              "Pretēji — no m/s uz km/h reizina ar 3,6.", "size": 18,
         "bold": True, "color": NAVY},
    ], accent=NAVY, anchor=C.MSO_ANCHOR.MIDDLE)
    return s


UZDEVUMI = [
    dict(
        nr=1,
        virsraksts="Automašīnas ātrums · mērvienību pārveide",
        teksts="Automašīna brauc ar ātrumu 72 km/h.\n"
               "a) Izsaki ātrumu SI vienībās.  b) Cik lielu ceļu tā veiks "
               "5 minūtēs?",
        dots=["υ = 72 km/h", "t = 5 min"],
        jaaprekina=["υ = ?  (m/s)", "s = ?  (m)"],
        formulas=["υ = s / t", "s = υ · t"],
        aprekins=[
            "1)  υ = 72 km/h = 72 : 3,6 = 20 m/s",
            "2)  t = 5 min = 5 · 60 s = 300 s",
            "3)  s = υ · t = 20 m/s · 300 s = 6000 m = 6 km",
        ],
        atbilde="υ = 20 m/s ;   s = 6000 m = 6,0 km",
        piezime="Pārbaude pēc mērvienībām: m/s · s = m — iznāk garums, "
                "tātad formula lietota pareizi.",
    ),
    dict(
        nr=2,
        virsraksts="Ķermeņa blīvums · SI vienības",
        teksts="Ķermeņa masa ir 200 g, bet tilpums 250 cm³.\n"
               "Aprēķini ķermeņa blīvumu SI vienībās un nosaki, vai tas "
               "peldēs ūdenī (ρ(ūdens) = 1000 kg/m³).",
        dots=["m = 200 g", "V = 250 cm³", "ρ(ūdens) = 1000 kg/m³"],
        jaaprekina=["ρ = ?"],
        formulas=["ρ = m / V"],
        aprekins=[
            "1)  m = 200 g = 200 · 10⁻³ kg = 0,20 kg",
            "2)  V = 250 cm³ = 250 · 10⁻⁶ m³ = 2,5 · 10⁻⁴ m³",
            "3)  ρ = m / V = 0,20 kg : (2,5 · 10⁻⁴ m³) = 800 kg/m³",
        ],
        atbilde="ρ = 800 kg/m³ — ķermenis peldēs, jo ρ < ρ(ūdens)",
        piezime="Blīvums mazāks par ūdens blīvumu — ķermenis peld. "
                "Piemēram, koks.",
    ),
    dict(
        nr=3,
        virsraksts="Garumu saskaitīšana · standartforma",
        teksts="Trases posmu garumi ir 0,45 km, 320 m un 15 cm.\n"
               "Aprēķini trases kopgarumu un izsaki to metros "
               "standartformā!",
        dots=["l₁ = 0,45 km", "l₂ = 320 m", "l₃ = 15 cm"],
        jaaprekina=["l = ?  (m)"],
        formulas=["l = l₁ + l₂ + l₃"],
        aprekins=[
            "1)  l₁ = 0,45 km = 0,45 · 10³ m = 450 m",
            "2)  l₃ = 15 cm = 15 · 10⁻² m = 0,15 m",
            "3)  l = 450 m + 320 m + 0,15 m = 770,15 m",
        ],
        atbilde="l = 770,15 m ≈ 7,70 · 10² m",
        piezime="Saskaitīt drīkst tikai vienādās mērvienībās izteiktus "
                "lielumus.",
    ),
    dict(
        nr=4,
        virsraksts="Spiediens uz grīdu · atvasinātā vienība",
        teksts="Skapja svars ir 600 N, un tas balstās uz kājām, kuru kopējais "
               "laukums ir 300 cm².\n"
               "Aprēķini spiedienu uz grīdu paskālos!",
        dots=["F = 600 N", "S = 300 cm²"],
        jaaprekina=["p = ?  (Pa)"],
        formulas=["p = F / S"],
        aprekins=[
            "1)  S = 300 cm² = 300 · 10⁻⁴ m² = 3,0 · 10⁻² m²",
            "2)  p = F / S = 600 N : (3,0 · 10⁻² m²)",
            "3)  p = 2,0 · 10⁴ Pa = 20 kPa",
        ],
        atbilde="p = 2,0 · 10⁴ Pa = 20 kPa",
        piezime="1 cm² = 10⁻⁴ m², nevis 10⁻² m² — laukumā pakāpi kāpina "
                "kvadrātā.",
    ),
    dict(
        nr=5,
        virsraksts="Elektriskā tējkanna · enerģija un jauda",
        teksts="Tējkannas jauda ir 2,2 kW, un tā darbojas 15 minūtes.\n"
               "Cik daudz enerģijas tā patērē? Izsaki džoulos un "
               "kilovatstundās.",
        dots=["P = 2,2 kW", "t = 15 min"],
        jaaprekina=["A = ?  (J)", "A = ?  (kWh)"],
        formulas=["P = A / t", "A = P · t"],
        aprekins=[
            "1)  P = 2,2 kW = 2,2 · 10³ W ;   t = 15 min = 900 s",
            "2)  A = P · t = 2,2 · 10³ W · 900 s = 1,98 · 10⁶ J",
            "3)  A = 2,2 kW · 0,25 h = 0,55 kWh",
        ],
        atbilde="A ≈ 1,98 · 10⁶ J = 0,55 kWh",
        piezime="Rēķinos lieto džoulus, bet elektrības rēķinā — "
                "kilovatstundas: 1 kWh = 3,6 · 10⁶ J.",
    ),
    dict(
        nr=6,
        virsraksts="Ticamības pārbaude · vai atbilde ir saprātīga?",
        teksts="Skolēns aprēķināja, ka gājēja ātrums ir 5,0 · 10³ m/s.\n"
               "Pārbaudi, cik tālu gājējs tā aizietu 1 stundā, un novērtē, "
               "vai atbilde ir ticama.",
        dots=["υ = 5,0 · 10³ m/s", "t = 1 h"],
        jaaprekina=["s = ?  (km)"],
        formulas=["s = υ · t"],
        aprekins=[
            "1)  t = 1 h = 3600 s",
            "2)  s = 5,0 · 10³ m/s · 3600 s = 1,8 · 10⁷ m",
            "3)  s = 1,8 · 10⁴ km",
        ],
        atbilde="s = 1,8 · 10⁴ km — atbilde NAV ticama",
        piezime="Gājējs ietu 18 000 km stundā — gandrīz apkārt Zemei. "
                "Ticams gājēja ātrums ir ~1,4 m/s.",
    ),
]

KOPSAVILKUMS = dict(
    iemacijamies=[
        "Fizikāls lielums = skaitlis × mērvienība; bez mērvienības nav "
        "atbildes.",
        "SI ir 7 pamatvienības; visas pārējās ir atvasinātas no tām.",
        "Priedēkli aizstāj ar pakāpi: k = 10³, c = 10⁻², m = 10⁻³, "
        "µ = 10⁻⁶, n = 10⁻⁹.",
        "Laukumam un tilpumam pakāpi kāpina: 1 cm² = 10⁻⁴ m², "
        "1 cm³ = 10⁻⁶ m³.",
        "Atbildi pārbauda pēc mērvienībām un pēc tā, vai tā ir saprātīga.",
    ],
    majasdarbs=[
        "Izsaki SI vienībās: a) 36 km/h   b) 750 g   c) 4,5 cm³   "
        "d) 120 kPa   e) 25 min.",
        "Alumīnija plāksnes masa 810 g, tilpums 300 cm³. Aprēķini blīvumu "
        "un salīdzini ar tabulas vērtību 2700 kg/m³.",
        "Sildītāja jauda 1,5 kW. Cik enerģijas (J un kWh) tas patērē "
        "40 minūtēs?",
    ],
    pasvertejums=["Protu nosaukt SI pamatvienības",
                  "Protu pārvērst mērvienības",
                  "Protu lietot standartformu",
                  "Protu pārbaudīt atbildi pēc mērvienībām"],
    nakama="Nākamā stunda: mikropasaules pētīšana — ko un ar ko var "
           "saskatīt mikropasaulē.",
)


def build(out_path):
    return C.build_lesson(META, [s_lielums, s_atvasinatas, s_parveide],
                          UZDEVUMI, KOPSAVILKUMS, out_path)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    out = ("C:/aphysics/Dabaszinibas/1. Pasaule ap mums un tās pētīšana/"
           "1.3. Fizikālie lielumi un SI mērvienības.pptx")
    print("Slaidu skaits: %d  ->  %s" % (build(out), out))
