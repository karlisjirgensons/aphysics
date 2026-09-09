# -*- coding: utf-8 -*-
"""
Dabaszinības (fizikas daļa), 1. temats "Pasaule ap mums un tās pētīšana"
1.2. stunda: Pasaules organizācijas līmeņi — "Kā saistīts atoms ar Galaktiku?"

Stunda ņemta no plāna "Dabaszinības ALL klase - 10.-12. klases saturs vienā
gadā.docx" (10.1. temata 2. stunda).
Sasniedzamais rezultāts: sakārto objektus pēc izmēra no atoma līdz Visumam;
pamato līmeņu savstarpējo saistību ar piemēriem.

Izkārtojums un uzdevumu atklāšanas mehānika - no gen_dabaszinibas_1_1.py.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_dabaszinibas_1_1 as S              # noqa: E402
from gen_dabaszinibas_1_1 import (            # noqa: E402
    SW, SH, MX, CW, NAVY, BLUE, LIGHTBLUE, GOLD, LIGHTGOLD, GREY, LINEGREY,
    LIGHTGREY, DARK, RED, GREEN, LIGHTGREEN, WHITE, PP_ALIGN, MSO_ANCHOR,
    RGBColor, new_deck, blank, box, rule, put, panel, header, footer)

S.KICKER = ("DABASZINĪBAS · 10. KLASE · 1. TEMATS: PASAULE AP MUMS UN "
            "TĀS PĒTĪŠANA")
S.FOOT = "1.2. Pasaules organizācijas līmeņi — no atoma līdz Visumam"


# ============================================================ TEORIJAS SLAIDI
def slide_title(prs):
    s = blank(prs)
    box(s, 0, 0, SW, SH, fill=NAVY, rounded=False)
    box(s, 0, 6.10, SW, 1.40, fill=RGBColor(0x17, 0x2B, 0x4D), rounded=False)

    put(s, 1.05, 1.45, CW, 0.32,
        [{"t": "DABASZINĪBAS · 10. KLASE · FIZIKAS DAĻA", "size": 16,
          "bold": True, "color": RGBColor(0x9D, 0xC3, 0xE6)}], autofit=False)
    put(s, 1.05, 2.00, 11.0, 0.70,
        [{"t": "1. temats. Pasaule ap mums un tās pētīšana", "size": 36,
          "bold": True, "color": WHITE}])
    rule(s, 1.05, 3.05, 3.60, GOLD, 0.03)

    put(s, 1.05, 3.45, 11.0, 2.10, [
        {"t": "1.2. stunda", "size": 21, "bold": True, "color": GOLD},
        {"t": "Pasaules organizācijas līmeņi", "size": 33, "bold": True,
         "color": WHITE, "space": 12},
        {"t": "Kā saistīts atoms ar Galaktiku?", "size": 26,
         "color": RGBColor(0xBD, 0xD7, 0xEE), "space": 8},
    ])
    put(s, 1.05, 6.50, 11.0, 0.55,
        [{"t": "Izmēru kārtas · Standartforma · Mērogu salīdzināšana",
          "size": 15, "color": RGBColor(0xBD, 0xD7, 0xEE)}])
    return s


def slide_merkis(prs):
    s = blank(prs)
    header(s, "Stundas mērķis un sasniedzamais rezultāts")

    panel(s, MX, 1.20, CW, 1.15, [
        {"t": "MĒRĶIS", "size": 12, "bold": True, "color": GOLD},
        {"t": "Izprast, ka daba ir sakārtota līmeņos — no atoma līdz "
              "Visumam — un iemācīties salīdzināt šo līmeņu izmērus, "
              "lietojot standartformu.", "size": 20, "space": 6},
    ], accent=GOLD, fill=LIGHTGOLD)

    put(s, MX, 2.62, CW, 0.32,
        [{"t": "Stundas beigās es protu:", "size": 16, "bold": True,
          "color": NAVY}], autofit=False)

    items = [
        "nosaukt un sakārtot pasaules organizācijas līmeņus pēc izmēra;",
        "novērtēt katra līmeņa raksturīgo izmēru kārtu (10ⁿ);",
        "aprēķināt, cik reižu viens objekts ir lielāks par otru;",
        "pamatot ar piemēru, kā izmaiņas vienā līmenī ietekmē pārējos.",
    ]
    y = 3.10
    for i, it in enumerate(items, 1):
        box(s, MX, y, 0.44, 0.44, fill=BLUE, line=None)
        put(s, MX + 0.10, y + 0.09, 0.30, 0.28,
            [{"t": str(i), "size": 15, "bold": True, "color": WHITE,
              "align": PP_ALIGN.CENTER}], autofit=False)
        put(s, MX + 0.68, y + 0.05, CW - 0.80, 0.42, [{"t": it, "size": 19}])
        y += 0.70

    panel(s, MX, 6.02, CW, 0.90, [
        {"t": "ATKĀRTOJUMS no 1.1. stundas", "size": 12, "bold": True,
         "color": NAVY},
        {"t": "Matērija pastāv kā VIELA (masa) un kā LAUKS (stiprums). "
              "Pasauli nosacīti iedala mikro-, makro- un megapasaulē.",
         "size": 17, "space": 5},
    ], accent=NAVY)
    footer(s)
    return s


def _limenu_slaids(prs, title, ievads, steps, apaks, accent):
    s = blank(prs)
    header(s, title)
    put(s, MX, 1.16, CW, 0.30, [{"t": ievads, "size": 17, "color": GREY}],
        autofit=False)

    per_row, gapx = 5, 0.26
    w = (CW - (per_row - 1) * gapx) / per_row
    h = 1.10
    x, y = MX, 1.62
    for i, (n, sc, pm) in enumerate(steps):
        if i and i % per_row == 0:
            x = MX
            y += h + 0.34
        box(s, x, y, w, h, fill=WHITE, line=accent, lw=1.5)
        put(s, x + 0.10, y + 0.12, w - 0.20, h - 0.24, [
            {"t": n, "size": 15, "bold": True, "color": accent,
             "align": PP_ALIGN.CENTER},
            {"t": "≈ " + sc, "size": 15, "bold": True,
             "align": PP_ALIGN.CENTER, "space": 3},
            {"t": pm, "size": 12, "color": GREY, "align": PP_ALIGN.CENTER,
             "space": 3},
        ])
        if (i + 1) % per_row != 0 and i != len(steps) - 1:
            put(s, x + w, y + 0.34, gapx, 0.45,
                [{"t": "›", "size": 20, "bold": True, "color": LINEGREY,
                  "align": PP_ALIGN.CENTER}], autofit=False)
        x += w + gapx

    panel(s, MX, 5.86, CW, 0.94, apaks, accent=accent)
    footer(s)
    return s


def slide_dzivais(prs):
    return _limenu_slaids(
        prs, "Organizācijas līmeņi: no atoma līdz biosfērai",
        "Katrs nākamais līmenis veidojas no iepriekšējā — mazākais ir "
        "atoms:",
        [("atoms", "10⁻¹⁰ m", "ūdeņradis"),
         ("molekula", "10⁻⁹ m", "ūdens H₂O"),
         ("šūna", "10⁻⁵ m", "sarkanā asins šūna"),
         ("audi", "10⁻³ m", "muskuļaudi"),
         ("orgāns", "10⁻¹ m", "sirds"),
         ("organisms", "10⁰ m", "cilvēks 1,7 m"),
         ("populācija", "10² m", "stirnu bars"),
         ("ekosistēma", "10⁴ m", "mežs, ezers"),
         ("biosfēra", "10⁷ m", "visa dzīvā Zeme"),
         ("planēta", "10⁷ m", "Zeme R = 6,37·10⁶ m")],
        [{"t": "Katrā solī izmērs pieaug par vairākām KĀRTĀM — "
               "reizinājumu ar 10, 100, 1000 …", "size": 18, "bold": True,
          "color": NAVY},
         {"t": "Tāpēc izmērus pieraksta standartformā: 0,0000001 m = "
               "1 · 10⁻⁷ m.", "size": 16, "color": GREY, "space": 5}],
        BLUE)


def slide_mega(prs):
    return _limenu_slaids(
        prs, "Organizācijas līmeņi: no planētas līdz Visumam",
        "Megapasaulē attālumus vairs nemēra metros — lieto au, gaismas gadu "
        "un parseku:",
        [("planēta", "10⁷ m", "Zeme"),
         ("zvaigzne", "10⁹ m", "Saule R = 6,96·10⁸ m"),
         ("planētu sistēma", "10¹³ m", "Saules sistēma"),
         ("zvaigžņu kopa", "10¹⁷ m", "Plejādes"),
         ("galaktika", "10²¹ m", "Piena Ceļš"),
         ("galaktiku kopa", "10²³ m", "Vietējā kopa"),
         ("galaktiku superkopa", "10²⁴ m", "Lanjakea"),
         ("Visums", "10²⁶ m", "novērojamā daļa")],
        [{"t": "1 au = 1,50 · 10¹¹ m      ·      1 ly = 9,46 · 10¹⁵ m"
               "      ·      1 pc = 3,09 · 10¹⁶ m", "size": 19, "bold": True,
          "color": NAVY},
         {"t": "Vērtības atrodamas datu bukletā — tās nav jāiemācās no "
               "galvas.", "size": 16, "color": GREY, "space": 5}],
        GREEN)


def slide_merogs(prs):
    s = blank(prs)
    header(s, "Kā salīdzināt divus izmērus")

    colw = (CW - 0.38) / 2
    panel(s, MX, 1.20, colw, 2.60, [
        {"t": "1. SOLIS — abus izsaki SI vienībās un standartformā",
         "size": 14, "bold": True, "color": BLUE},
        {"t": "20 µm = 20 · 10⁻⁶ m = 2 · 10⁻⁵ m", "size": 19, "space": 10},
        {"t": "0,3 nm = 0,3 · 10⁻⁹ m = 3 · 10⁻¹⁰ m", "size": 19,
         "space": 6},
        {"t": "Standartformā skaitlis ir no 1 līdz 10, reizināts ar 10ⁿ.",
         "size": 15, "color": GREY, "space": 10},
    ], accent=BLUE)

    panel(s, MX + colw + 0.38, 1.20, colw, 2.60, [
        {"t": "2. SOLIS — dali lielāko ar mazāko", "size": 14, "bold": True,
         "color": BLUE},
        {"t": "n = 2 · 10⁻⁵ m : (3 · 10⁻¹⁰ m)", "size": 19, "space": 10},
        {"t": "n = (2 : 3) · 10⁻⁵⁻⁽⁻¹⁰⁾ = 0,67 · 10⁵", "size": 19,
         "space": 6},
        {"t": "n ≈ 6,7 · 10⁴", "size": 21, "bold": True, "color": RED,
         "space": 8},
    ], accent=BLUE)

    panel(s, MX, 3.98, CW, 1.34, [
        {"t": "PAKĀPJU LIKUMI, kas vajadzīgi katrā uzdevumā", "size": 12,
         "bold": True, "color": GOLD},
        {"t": "10ᵃ · 10ᵇ = 10ᵃ⁺ᵇ            10ᵃ : 10ᵇ = 10ᵃ⁻ᵇ            "
              "(10ᵃ)ᵇ = 10ᵃ·ᵇ", "size": 22, "bold": True, "space": 8,
         "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "Dalot atņem pakāpes rādītājus; uzmanies ar mīnusiem: "
              "−5 − (−10) = +5.", "size": 16, "color": GREY, "space": 8,
         "align": PP_ALIGN.CENTER},
    ], accent=GOLD, fill=LIGHTGOLD)

    panel(s, MX, 5.50, CW, 1.40, [
        {"t": "KĀRTA (lielumu secība)", "size": 12, "bold": True,
         "color": NAVY},
        {"t": "Ja n ≈ 10⁴, sakām: objekts ir par ČETRĀM kārtām lielāks — "
              "tātad 10 000 reižu.", "size": 19, "space": 7},
        {"t": "Atoms (10⁻¹⁰ m) ir par 4 kārtām lielāks nekā kodols "
              "(10⁻¹⁴ m), bet par 5 kārtām mazāks nekā šūna (10⁻⁵ m).",
         "size": 18, "space": 6, "color": GREY},
    ], accent=NAVY)
    return s


def slide_saistiba(prs):
    s = blank(prs)
    header(s, "Kāpēc līmeņi ir savstarpēji saistīti")

    put(s, MX, 1.16, CW, 0.32,
        [{"t": "Izmaiņas vienā līmenī ietekmē visus pārējos — gan uz augšu, "
               "gan uz leju:", "size": 18, "color": GREY}], autofit=False)

    piemeri = [
        ("MOLEKULA → ORGANISMS", BLUE,
         "Viena DNS molekulas kļūda šūnā var mainīt visa organisma pazīmi "
         "vai izraisīt slimību."),
        ("ATOMS → EKOSISTĒMA", GOLD,
         "Radioaktīva izotopa atomi nonāk augsnē, pēc tam augos un "
         "dzīvniekos — piesārņota tiek visa ekosistēma."),
        ("ZVAIGZNE → ATOMS", GREEN,
         "Zvaigznēs kodolsintēzē rodas smagie ķīmiskie elementi — arī tie, "
         "no kuriem sastāvam mēs paši."),
    ]
    y = 1.62
    for virsr, c, teksts in piemeri:
        panel(s, MX, y, CW, 1.16, [
            {"t": virsr, "size": 13, "bold": True, "color": c},
            {"t": teksts, "size": 20, "space": 7},
        ], accent=c)
        y += 1.28

    panel(s, MX, 5.50, CW, 1.34, [
        {"t": "SECINĀJUMS", "size": 12, "bold": True, "color": NAVY},
        {"t": "Dabu nevar izprast, pētot tikai vienu līmeni. Tāpēc "
              "dabaszinātnēs fizika, ķīmija un bioloģija pēta vienu un to "
              "pašu pasauli dažādos mērogos.", "size": 19, "space": 7},
        {"t": "Fizika: no elementārdaļiņām līdz Visumam.", "size": 17,
         "space": 6, "color": GREY},
    ], accent=NAVY)
    footer(s)
    return s


def slide_divider(prs):
    s = blank(prs)
    box(s, 0, 0, SW, SH, fill=NAVY, rounded=False)
    put(s, 1.05, 2.55, 11.0, 1.12,
        [{"t": "UZDEVUMI", "size": 56, "bold": True, "color": WHITE}])
    rule(s, 1.05, 3.90, 3.20, GOLD, 0.03)
    put(s, 1.05, 4.25, 11.0, 1.90, [
        {"t": "Cik reižu viens ir lielāks par otru?", "size": 24,
         "color": RGBColor(0xBD, 0xD7, 0xEE)},
        {"t": "Katrs jaunais solis vispirms parādās liels — pēc tam "
              "nostājas savā vietā risinājumā.", "size": 17, "space": 16,
         "color": RGBColor(0x9D, 0xC3, 0xE6)},
    ])
    return s


# ==================================================================== UZDEVUMI
UZDEVUMI = [
    dict(
        nr=1,
        virsraksts="Atoms un tā kodols · mikropasaule",
        teksts="Atoma diametrs ir aptuveni 10⁻¹⁰ m, bet atoma kodola "
               "diametrs — aptuveni 10⁻¹⁴ m.\n"
               "Cik reižu atoms ir lielāks par savu kodolu?",
        dots=["d(atoma) = 10⁻¹⁰ m", "d(kodola) = 10⁻¹⁴ m"],
        jaaprekina=["n = ?"],
        formulas=["n = d(atoma) / d(kodola)"],
        aprekins=[
            "1)  n = 10⁻¹⁰ m : 10⁻¹⁴ m",
            "2)  n = 10⁻¹⁰⁻⁽⁻¹⁴⁾ = 10⁴",
        ],
        atbilde="n = 10⁴ = 10 000 reižu",
        piezime="Ja atoms būtu futbola laukuma lielumā, kodols būtu "
                "zirnis laukuma vidū — atoms galvenokārt ir tukšums.",
    ),
    dict(
        nr=2,
        virsraksts="Šūna un molekula · mikropasaule",
        teksts="Cilvēka sarkanās asins šūnas diametrs ir 20 µm, bet ūdens "
               "molekulas diametrs — 0,3 nm.\n"
               "Cik reižu šūna ir lielāka par ūdens molekulu?",
        dots=["d(šūnas) = 20 µm", "d(molekulas) = 0,3 nm"],
        jaaprekina=["n = ?"],
        formulas=["n = d(šūnas) / d(molekulas)"],
        aprekins=[
            "1)  d(šūnas) = 20 µm = 20 · 10⁻⁶ m = 2 · 10⁻⁵ m",
            "2)  d(molekulas) = 0,3 nm = 0,3 · 10⁻⁹ m = 3 · 10⁻¹⁰ m",
            "3)  n = (2 · 10⁻⁵ m) : (3 · 10⁻¹⁰ m) = 0,67 · 10⁵",
        ],
        atbilde="n ≈ 6,7 · 10⁴ ≈ 67 000 reižu",
        piezime="Šūna ir par gandrīz piecām kārtām lielāka nekā molekula, "
                "no kurām tā sastāv.",
    ),
    dict(
        nr=3,
        virsraksts="Cilvēks un Zeme · makropasaule",
        teksts="Cilvēka augums ir 1,7 m, bet Zemes rādiuss — 6,37 · 10⁶ m "
               "(datu buklets).\n"
               "Cik reižu Zemes rādiuss ir lielāks par cilvēka augumu?",
        dots=["h = 1,7 m", "R = 6,37 · 10⁶ m"],
        jaaprekina=["n = ?"],
        formulas=["n = R / h"],
        aprekins=[
            "1)  n = (6,37 · 10⁶ m) : 1,7 m",
            "2)  n = 3,75 · 10⁶",
        ],
        atbilde="n ≈ 3,7 · 10⁶ ≈ 3,7 miljoni reižu",
        piezime="Cilvēks un Zeme abi ir makropasaules objekti, taču starp "
                "tiem ir vairāk nekā sešas kārtas.",
    ),
    dict(
        nr=4,
        virsraksts="Saule un Zeme · megapasaule",
        teksts="Saules rādiuss ir 6,96 · 10⁸ m, Zemes rādiuss — "
               "6,37 · 10⁶ m.\n"
               "a) Cik reižu Saules rādiuss ir lielāks?  b) Cik reižu "
               "lielāks ir Saules tilpums? (V ~ R³)",
        dots=["R(Saules) = 6,96 · 10⁸ m", "R(Zemes) = 6,37 · 10⁶ m"],
        jaaprekina=["n = ?", "N = ?"],
        formulas=["n = R(S) / R(Z)", "N = n³"],
        aprekins=[
            "1)  n = (6,96 · 10⁸ m) : (6,37 · 10⁶ m) = 1,09 · 10²",
            "2)  n ≈ 109",
            "3)  N = n³ = 109³ ≈ 1,3 · 10⁶",
        ],
        atbilde="n ≈ 109 reižu ;   N ≈ 1,3 · 10⁶ reižu",
        piezime="Saulē ietilptu vairāk nekā miljons Zemes — jo tilpums aug "
                "kā rādiusa kubs.",
    ),
    dict(
        nr=5,
        virsraksts="Piena Ceļš · galaktikas mērogs",
        teksts="Mūsu galaktikas Piena Ceļš diametrs ir aptuveni "
               "1,0 · 10⁵ gaismas gadu.\n"
               "Izsaki šo diametru metros! Izmanto datu bukletu.",
        dots=["D = 1,0 · 10⁵ ly", "1 ly = 9,46 · 10¹⁵ m"],
        jaaprekina=["D = ?  (m)"],
        formulas=["D = N · (1 ly)"],
        aprekins=[
            "1)  D = 1,0 · 10⁵ · 9,46 · 10¹⁵ m",
            "2)  D = 9,46 · 10⁵⁺¹⁵ m",
        ],
        atbilde="D ≈ 9,5 · 10²⁰ m",
        piezime="Gaismai, lai šķērsotu mūsu galaktiku, vajadzīgi "
                "100 000 gadu.",
    ),
    dict(
        nr=6,
        virsraksts="Saules sistēmas modelis · mērogs",
        teksts="Saules diametrs ir 1,39 · 10⁹ m, Zemes — 1,27 · 10⁷ m, "
               "attālums starp tām 1,50 · 10¹¹ m. Sauli attēlo kā 1,00 m "
               "lielu bumbu.\n"
               "Cik liela modelī ir Zeme un cik tālu tā jānovieto?",
        dots=["D(S) = 1,39 · 10⁹ m", "D(Z) = 1,27 · 10⁷ m",
              "s = 1,50 · 10¹¹ m"],
        jaaprekina=["d = ?  (m)", "l = ?  (m)"],
        formulas=["k = 1,00 m / D(S)", "d = k · D(Z)", "l = k · s"],
        aprekins=[
            "1)  k = 1,00 m : (1,39 · 10⁹ m) = 7,19 · 10⁻¹⁰",
            "2)  d = 7,19 · 10⁻¹⁰ · 1,27 · 10⁷ m = 9,1 · 10⁻³ m",
            "3)  l = 7,19 · 10⁻¹⁰ · 1,50 · 10¹¹ m = 1,08 · 10² m",
        ],
        atbilde="d ≈ 9 mm ;   l ≈ 108 m",
        piezime="Ja Saule ir pludmales bumba, Zeme ir zirnis vairāk nekā "
                "simt metru attālumā — Saules sistēma ir gandrīz tukša.",
    ),
]


def slide_kopsavilkums(prs):
    s = blank(prs)
    header(s, "Kopsavilkums un mājasdarbs")

    colw = (CW - 0.38) / 2
    panel(s, MX, 1.20, colw, 3.94, [
        {"t": "ŠODIEN IEMĀCĪJĀMIES", "size": 12, "bold": True,
         "color": BLUE},
        {"t": "•  Daba ir sakārtota līmeņos: atoms → molekula → šūna → "
              "organisms → ekosistēma → planēta → galaktika → Visums.",
         "size": 17, "space": 12},
        {"t": "•  Katram līmenim ir raksturīga izmēra kārta 10ⁿ.",
         "size": 17, "space": 9},
        {"t": "•  Lai salīdzinātu izmērus, abus izsaka SI vienībās un "
              "standartformā, tad dala.", "size": 17, "space": 9},
        {"t": "•  Dalot pakāpes atņem:  10ᵃ : 10ᵇ = 10ᵃ⁻ᵇ.", "size": 17,
         "space": 9},
        {"t": "•  Izmaiņas vienā līmenī ietekmē pārējos.", "size": 17,
         "space": 9},
    ], accent=BLUE)

    panel(s, MX + colw + 0.38, 1.20, colw, 3.94, [
        {"t": "MĀJASDARBS", "size": 12, "bold": True, "color": GOLD},
        {"t": "1.  Sakārto pēc izmēra, sākot ar mazāko: šūna, atoms, "
              "Galaktika, molekula, Zeme, vīruss, Saule.", "size": 17,
         "space": 12},
        {"t": "2.  Baktērijas garums 2 µm, vīrusa — 100 nm. Cik reižu "
              "baktērija ir lielāka?", "size": 17, "space": 12},
        {"t": "3.  Mēness rādiuss 1,74 · 10⁶ m, Zemes — 6,37 · 10⁶ m. "
              "Cik reižu Zeme ir lielāka pēc rādiusa un cik — pēc tilpuma?",
         "size": 17, "space": 12},
    ], accent=GOLD, fill=LIGHTGOLD)

    panel(s, MX, 5.30, CW, 1.62, [
        {"t": "PAŠVĒRTĒJUMS — atzīmē, cik droši jūties", "size": 12,
         "bold": True, "color": NAVY},
        {"t": "Protu nosaukt līmeņus pēc kārtas   ·   Protu novērtēt "
              "izmēra kārtu   ·   Protu izteikt skaitli standartformā   ·   "
              "Protu aprēķināt, cik reižu lielāks", "size": 17, "space": 9},
        {"t": "Nākamā stunda: fizikālie lielumi un SI mērvienības — kāpēc "
              "visā pasaulē mēra vienādi.", "size": 15, "space": 12,
         "color": GREY, "italic": True},
    ], accent=NAVY)
    return s


# ==================================================================== BŪVĒŠANA
def build(out_path):
    S.UZDEVUMI = UZDEVUMI
    prs = new_deck()
    slide_title(prs)
    slide_merkis(prs)
    slide_dzivais(prs)
    slide_mega(prs)
    slide_merogs(prs)
    slide_saistiba(prs)
    slide_divider(prs)
    for i in range(len(UZDEVUMI)):
        S.task_slides(prs, i)
    slide_kopsavilkums(prs)
    d = os.path.dirname(out_path)
    if d:
        os.makedirs(d, exist_ok=True)
    prs.save(out_path)
    return len(prs.slides._sldIdLst)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    out = ("C:/aphysics/Dabaszinibas/1. Pasaule ap mums un tās pētīšana/"
           "1.2. Pasaules organizācijas līmeņi.pptx")
    print("Izveidots: %s" % out)
    print("Slaidu skaits: %d" % build(out))
