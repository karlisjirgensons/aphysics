# -*- coding: utf-8 -*-
"""
1.4. stunda: Mikropasaules pētīšana — "Ko un ar ko var saskatīt
mikropasaulē?"  Plāns: 10.1. temata 4. stunda.
SR: salīdzina optiskā, elektronu un atomspēku mikroskopa palielinājumu un
izšķirtspēju; izvēlas objektam piemērotu ierīci.
"""

import sys
import dz_common as C
from dz_common import (MX, CW, NAVY, BLUE, GOLD, LIGHTGOLD, GREY, RED,
                       GREEN, PP_ALIGN, MSO_ANCHOR, blank, put, panel,
                       header, footer, tabula)

META = dict(
    temats="1. temats. Pasaule ap mums un tās pētīšana",
    kicker=("DABASZINĪBAS · 10. KLASE · 1. TEMATS: PASAULE AP MUMS UN "
            "TĀS PĒTĪŠANA"),
    stunda="1.4. stunda",
    virsraksts="Mikropasaules pētīšana",
    jautajums="Ko un ar ko var saskatīt mikropasaulē?",
    apaksraksts="Palielinājums · Izšķirtspēja · Optiskais, elektronu un "
                "atomspēku mikroskops",
    foot="1.4. Mikropasaules pētīšana — mikroskopi un to iespējas",
    merkis="Izprast, kas ierobežo mikroskopa iespējas, un iemācīties "
           "izvēlēties pētāmajam objektam piemērotu mikroskopu, salīdzinot "
           "palielinājumu un izšķirtspēju.",
    protu=[
        "atšķirt palielinājumu no izšķirtspējas;",
        "aprēķināt mikroskopa palielinājumu un objekta patieso izmēru;",
        "salīdzināt optisko, elektronu un atomspēku mikroskopu;",
        "izvēlēties objektam piemērotu mikroskopu un pamatot izvēli.",
    ],
    atkartojums="1.2. stundā noskaidrojām mikropasaules izmēru kārtas: "
                "šūna ~10⁻⁵ m, molekula ~10⁻⁹ m, atoms ~10⁻¹⁰ m. Šodien "
                "noskaidrosim, ar ko tos var ieraudzīt.",
    uzdevumu_apraksts="Palielinājums, izšķirtspēja un attēla izmērs",
)


def s_acs(prs):
    s = blank(prs)
    header(s, "Kāpēc acs neredz mikropasauli")

    panel(s, MX, 1.20, CW, 1.10, [
        {"t": "Cilvēka acs izšķirtspēja ir aptuveni 0,1 mm = 10⁻⁴ m.",
         "size": 21, "bold": True, "color": NAVY},
        {"t": "Tas nozīmē: divus punktus, kas ir tuvāk par 0,1 mm, acs "
              "saredz kā vienu. Viss mazākais mums ir neredzams.",
         "size": 17, "space": 6, "color": GREY},
    ], accent=NAVY)

    C.kartitas(s, 2.46, 2.30, [
        ("PALIELINĀJUMS Γ", BLUE,
         ["Cik reižu attēls ir lielāks par objektu.",
          "Γ = attēla izmērs / objekta izmērs",
          "Palielinājumu var palielināt gandrīz bez robežas —",
          "bet no tā vien attēls nekļūst skaidrāks."]),
        ("IZŠĶIRTSPĒJA d", RED,
         ["Mazākais attālums starp diviem punktiem,",
          "kurus vēl var redzēt atsevišķi.",
          "Tā ir ierīces ĪSTĀ robeža.",
          "Jo mazāks d, jo labāka ierīce."]),
        ("TUKŠAIS PALIELINĀJUMS", GOLD,
         ["Ja palielina vairāk, nekā atļauj izšķirtspēja,",
          "attēls kļūst lielāks, bet izplūdis.",
          "Jaunu informāciju tas nedod.",
          "Tāpēc svarīga ir izšķirtspēja, ne tikai Γ."]),
    ])

    panel(s, MX, 5.00, CW, 1.90, [
        {"t": "KAS IEROBEŽO IZŠĶIRTSPĒJU", "size": 12, "bold": True,
         "color": NAVY},
        {"t": "Ar gaismu nevar saskatīt objektu, kas ir mazāks par gaismas "
              "viļņa garumu.", "size": 20, "bold": True, "space": 8},
        {"t": "Redzamās gaismas viļņa garums ir 400–700 nm, tāpēc optiskā "
              "mikroskopa izšķirtspēja nav labāka par ≈ 200 nm.",
         "size": 18, "space": 7},
        {"t": "Elektronu viļņa garums ir tūkstošiem reižu mazāks — tāpēc "
              "elektronmikroskops saskata daudz sīkākus objektus.",
         "size": 18, "space": 7, "color": GREY},
    ], accent=NAVY)
    return s


def s_mikroskopi(prs):
    s = blank(prs)
    header(s, "Trīs mikroskopu veidi")

    put(s, MX, 1.16, CW, 0.30,
        [{"t": "Katram mikroskopam ir sava izšķirtspēja un savs pielietojums:",
          "size": 17, "color": GREY}], autofit=False)

    tabula(s, MX, 1.56, CW,
           ["Mikroskops", "Palielinājums", "Izšķirtspēja", "Ko var saskatīt",
            "Trūkumi"],
           [["Optiskais", "līdz ~1500×", "~200 nm",
             "šūnas, audi, baktērijas", "neredz vīrusus un molekulas"],
            ["Elektronu (SEM/TEM)", "līdz ~10⁶×", "~0,1 nm",
             "vīrusi, šūnas sīkbūves", "tikai vakuumā, paraugs nedzīvs"],
            ["Atomspēku (AFM)", "līdz ~10⁷×", "~0,1 nm",
             "atsevišķi atomi un molekulas", "lēns, mazs skata laukums"]],
           [3.10, 2.20, 1.90, 3.10, 1.93], rowh=0.72, size=15, hsize=13)

    C.kartitas(s, 4.10, 1.80, [
        ("OPTISKAIS", BLUE,
         ["Objekts apgaismots ar redzamo gaismu.",
          "Divas lēcas: objektīvs un okulārs.",
          "Γ = Γ(objektīva) · Γ(okulāra)"]),
        ("ELEKTRONU", GREEN,
         ["Objektu “apgaismo” ar elektronu kūli.",
          "Attēlu veido ekrānā vai datorā.",
          "Ar to atklāja vīrusu uzbūvi."]),
        ("ATOMSPĒKU", GOLD,
         ["Ļoti asa adata “taustās” pa virsmu.",
          "Mēra spēku starp adatu un atomiem.",
          "Ļauj redzēt atsevišķus atomus."]),
    ])

    panel(s, MX, 6.06, CW, 0.84, [
        {"t": "DROŠĪBA:  mikroskopu nes ar abām rokām (statni un pamatni); "
              "elektroiekārtu neieslēdz ar slapjām rokām; lāzera un UV "
              "gaismā neskatās.", "size": 17, "bold": True, "color": RED},
    ], accent=RED, anchor=MSO_ANCHOR.MIDDLE)
    return s


def s_aprekini(prs):
    s = blank(prs)
    header(s, "Kā rēķina ar mikroskopu")

    colw = (CW - 0.38) / 2
    panel(s, MX, 1.20, colw, 2.50, [
        {"t": "OPTISKĀ MIKROSKOPA PALIELINĀJUMS", "size": 13, "bold": True,
         "color": BLUE},
        {"t": "Γ = Γ(ob) · Γ(ok)", "size": 26, "bold": True, "space": 12,
         "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "Piemērs: objektīvs 40×, okulārs 10×", "size": 17,
         "space": 12},
        {"t": "Γ = 40 · 10 = 400×", "size": 19, "bold": True, "space": 6,
         "color": RED},
    ], accent=BLUE)

    panel(s, MX + colw + 0.38, 1.20, colw, 2.50, [
        {"t": "OBJEKTA PATIESAIS IZMĒRS", "size": 13, "bold": True,
         "color": BLUE},
        {"t": "d = D / Γ", "size": 26, "bold": True, "space": 12,
         "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "D — attēla izmērs, d — objekta izmērs", "size": 17,
         "space": 12},
        {"t": "Piemērs: D = 8 mm, Γ = 400× → d = 20 µm", "size": 19,
         "bold": True, "space": 6, "color": RED},
    ], accent=BLUE)

    panel(s, MX, 3.88, CW, 1.36, [
        {"t": "VAI OBJEKTS BŪS SASKATĀMS?", "size": 12, "bold": True,
         "color": GOLD},
        {"t": "Objektu var saskatīt tikai tad, ja tā izmērs ir LIELĀKS par "
              "mikroskopa izšķirtspēju.", "size": 20, "bold": True,
         "space": 8, "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "Vīruss (100 nm) < optiskā mikroskopa izšķirtspēja (200 nm) "
              "→ ar optisko mikroskopu to neredzēs.", "size": 17,
         "space": 8, "color": GREY, "align": PP_ALIGN.CENTER},
    ], accent=GOLD, fill=LIGHTGOLD)

    panel(s, MX, 5.42, CW, 1.48, [
        {"t": "IZMĒRU ATGĀDNE — ko ar ko salīdzināt", "size": 12,
         "bold": True, "color": NAVY},
        {"t": "mati ~70 µm   ·   šūna ~10–100 µm   ·   baktērija ~1–5 µm   "
              "·   vīruss ~20–300 nm   ·   molekula ~1 nm   ·   "
              "atoms ~0,1 nm", "size": 18, "space": 8},
        {"t": "1 mm = 10⁻³ m   ·   1 µm = 10⁻⁶ m   ·   1 nm = 10⁻⁹ m",
         "size": 17, "space": 8, "color": GREY},
    ], accent=NAVY)
    footer(s)
    return s


UZDEVUMI = [
    dict(
        nr=1,
        virsraksts="Mikroskopa palielinājums",
        teksts="Mikroskopa objektīva palielinājums ir 40×, bet okulāra — "
               "15×.\n"
               "Aprēķini mikroskopa kopējo palielinājumu!",
        dots=["Γ(ob) = 40×", "Γ(ok) = 15×"],
        jaaprekina=["Γ = ?"],
        formulas=["Γ = Γ(ob) · Γ(ok)"],
        aprekins=[
            "1)  Γ = 40 · 15",
            "2)  Γ = 600",
        ],
        atbilde="Γ = 600× ",
        piezime="Palielinājumus reizina, nevis saskaita.",
    ),
    dict(
        nr=2,
        virsraksts="Šūnas patiesais izmērs",
        teksts="Ar mikroskopu, kura palielinājums ir 600×, šūnas attēla "
               "diametrs ir 12 mm.\n"
               "Aprēķini šūnas patieso diametru un izsaki to mikrometros!",
        dots=["Γ = 600×", "D = 12 mm"],
        jaaprekina=["d = ?  (µm)"],
        formulas=["Γ = D / d", "d = D / Γ"],
        aprekins=[
            "1)  D = 12 mm = 12 · 10⁻³ m",
            "2)  d = D / Γ = (12 · 10⁻³ m) : 600 = 2,0 · 10⁻⁵ m",
            "3)  d = 2,0 · 10⁻⁵ m = 20 µm",
        ],
        atbilde="d = 2,0 · 10⁻⁵ m = 20 µm",
        piezime="20 µm ir tipisks dzīvnieka šūnas izmērs.",
    ),
    dict(
        nr=3,
        virsraksts="Izšķirtspēju salīdzinājums",
        teksts="Optiskā mikroskopa izšķirtspēja ir 200 nm, bet "
               "elektronmikroskopa — 0,10 nm.\n"
               "Cik reižu elektronmikroskopa izšķirtspēja ir labāka?",
        dots=["d(opt) = 200 nm", "d(el) = 0,10 nm"],
        jaaprekina=["n = ?"],
        formulas=["n = d(opt) / d(el)"],
        aprekins=[
            "1)  n = 200 nm : 0,10 nm",
            "2)  n = 2,0 · 10³",
        ],
        atbilde="n = 2,0 · 10³ = 2000 reižu",
        piezime="Mērvienības var nepārvērst — tās vienādas un saīsinās.",
    ),
    dict(
        nr=4,
        virsraksts="Vai vīrusu var saskatīt?",
        teksts="Gripas vīrusa diametrs ir 100 nm. Skolēnam ir optiskais "
               "mikroskops ar izšķirtspēju 200 nm un palielinājumu 1500×.\n"
               "Vai ar to var saskatīt vīrusu? Pamato ar aprēķinu!",
        dots=["d(vīrusa) = 100 nm", "d(izšķ.) = 200 nm", "Γ = 1500×"],
        jaaprekina=["Vai d(vīrusa) > d(izšķ.)?"],
        formulas=["Saskata, ja  d(objekta) > d(izšķirtspējas)"],
        aprekins=[
            "1)  100 nm < 200 nm",
            "2)  Objekts ir mazāks par izšķirtspēju",
            "3)  D = d · Γ = 100 nm · 1500 = 1,5 · 10⁻⁴ m = 0,15 mm",
        ],
        atbilde="Nevar saskatīt — vīruss ir mazāks par izšķirtspēju",
        piezime="Attēls būtu 0,15 mm liels, bet pilnīgi izplūdis — tas ir "
                "tukšais palielinājums. Vajadzīgs elektronmikroskops.",
    ),
    dict(
        nr=5,
        virsraksts="Cik liels palielinājums vajadzīgs?",
        teksts="Cilvēka acs izšķirtspēja ir 0,10 mm. Skolēns vēlas saskatīt "
               "baktēriju, kuras garums ir 5,0 µm.\n"
               "Cik liels palielinājums vajadzīgs vismaz?",
        dots=["D = 0,10 mm", "d = 5,0 µm"],
        jaaprekina=["Γ = ?"],
        formulas=["Γ = D / d"],
        aprekins=[
            "1)  D = 0,10 mm = 1,0 · 10⁻⁴ m",
            "2)  d = 5,0 µm = 5,0 · 10⁻⁶ m",
            "3)  Γ = (1,0 · 10⁻⁴ m) : (5,0 · 10⁻⁶ m) = 20",
        ],
        atbilde="Γ ≥ 20× ",
        piezime="Praksē izvēlas lielāku palielinājumu, lai attēls būtu ērti "
                "aplūkojams, piemēram, 400×.",
    ),
    dict(
        nr=6,
        virsraksts="Palielinājums pēc attēla",
        teksts="Mācību grāmatā baktērija, kuras patiesais garums ir 2,0 µm, "
               "attēlota 4,0 cm gara.\n"
               "Cik liels ir attēla palielinājums?",
        dots=["d = 2,0 µm", "D = 4,0 cm"],
        jaaprekina=["Γ = ?"],
        formulas=["Γ = D / d"],
        aprekins=[
            "1)  D = 4,0 cm = 4,0 · 10⁻² m",
            "2)  d = 2,0 µm = 2,0 · 10⁻⁶ m",
            "3)  Γ = (4,0 · 10⁻² m) : (2,0 · 10⁻⁶ m) = 2,0 · 10⁴",
        ],
        atbilde="Γ = 2,0 · 10⁴ = 20 000×",
        piezime="Šāds palielinājums iegūstams tikai ar elektronmikroskopu.",
    ),
]

KOPSAVILKUMS = dict(
    iemacijamies=[
        "Palielinājums rāda, cik reižu attēls lielāks; izšķirtspēja — cik "
        "sīkas detaļas vēl var atšķirt.",
        "Ar gaismu nevar saskatīt objektu, mazāku par gaismas viļņa garumu "
        "→ optiskā mikroskopa robeža ~200 nm.",
        "Γ = Γ(ob) · Γ(ok)  un  d = D / Γ.",
        "Objektu saskata tikai tad, ja tas ir lielāks par izšķirtspēju.",
        "Vīrusus un atomus pēta ar elektronu un atomspēku mikroskopu.",
    ],
    majasdarbs=[
        "Objektīvs 100×, okulārs 12,5×. Aprēķini palielinājumu.",
        "Ar 400× mikroskopu šūnas attēls ir 10 mm. Cik liela ir šūna "
        "mikrometros?",
        "Vai ar optisko mikroskopu (izšķirtspēja 200 nm) var saskatīt "
        "molekulu (1 nm)? Pamato ar salīdzinājumu.",
    ],
    pasvertejums=["Protu atšķirt palielinājumu no izšķirtspējas",
                  "Protu aprēķināt Γ un objekta izmēru",
                  "Protu salīdzināt mikroskopu veidus",
                  "Protu pamatot mikroskopa izvēli"],
    nakama="Nākamā stunda: mērierīces un mērījumu precizitāte — vai "
           "digitāls mērījums vienmēr ir precīzāks.",
)


def build(out_path):
    return C.build_lesson(META, [s_acs, s_mikroskopi, s_aprekini],
                          UZDEVUMI, KOPSAVILKUMS, out_path)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    out = ("C:/aphysics/Dabaszinibas/1. Pasaule ap mums un tās pētīšana/"
           "1.4. Mikropasaules pētīšana.pptx")
    print("Slaidu skaits: %d  ->  %s" % (build(out), out))
