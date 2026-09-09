# -*- coding: utf-8 -*-
"""
1.5. stunda: Mērierīces un mērījumu precizitāte — "Vai digitāls mērījums
vienmēr ir precīzāks?"  Plāns: 10.1. temata 5. stunda.
SR: salīdzina analogās un digitālās mērierīces un sensorus; novērtē mērījuma
kļūdu un pieraksta rezultātu ar atbilstošu precizitāti.
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
    stunda="1.5. stunda",
    virsraksts="Mērierīces un mērījumu precizitāte",
    jautajums="Vai digitāls mērījums vienmēr ir precīzāks?",
    apaksraksts="Iedaļas vērtība · Absolūtā un relatīvā kļūda · Rezultāta "
                "pieraksts",
    foot="1.5. Mērierīces un mērījumu precizitāte",
    merkis="Iemācīties novērtēt mērījuma kļūdu, pierakstīt rezultātu formā "
           "x = (x ± Δx) un pamatot, kura mērierīce dotajā situācijā ir "
           "piemērotāka.",
    protu=[
        "noteikt mērierīces iedaļas vērtību un mērdiapazonu;",
        "novērtēt absolūto kļūdu un aprēķināt relatīvo kļūdu;",
        "pierakstīt rezultātu formā x = (x ± Δx) mērvienība;",
        "salīdzināt analogo un digitālo ierīci un pamatot izvēli.",
    ],
    atkartojums="1.3. stundā mācījāmies pārvērst mērvienības. Šodien "
                "noskaidrosim, cik ticams vispār ir mērījums, no kura "
                "sākas katrs aprēķins.",
    uzdevumu_apraksts="Iedaļas vērtība, kļūdas un rezultāta pieraksts",
)


def s_meriericies(prs):
    s = blank(prs)
    header(s, "Mērierīce, skala un iedaļas vērtība")

    colw = (CW - 0.38) / 2
    panel(s, MX, 1.20, colw, 2.34, [
        {"t": "IEDAĻAS VĒRTĪBA c", "size": 13, "bold": True, "color": BLUE},
        {"t": "Cik lielai lieluma izmaiņai atbilst viena skalas iedaļa.",
         "size": 17, "space": 8},
        {"t": "c = (b − a) / N", "size": 24, "bold": True, "space": 10,
         "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "a, b — divu apzīmētu svītriņu vērtības; N — iedaļu skaits "
              "starp tām.", "size": 15, "space": 8, "color": GREY},
    ], accent=BLUE)

    panel(s, MX + colw + 0.38, 1.20, colw, 2.34, [
        {"t": "MĒRDIAPAZONS", "size": 13, "bold": True, "color": GOLD},
        {"t": "No mazākās līdz lielākajai vērtībai, ko ierīce spēj izmērīt.",
         "size": 17, "space": 8},
        {"t": "Mēraparātu izvēlas tā, lai mērāmā vērtība būtu diapazona "
              "vidusdaļā.", "size": 17, "space": 8},
        {"t": "Pārsniedzot diapazonu, ierīci var sabojāt.", "size": 15,
         "space": 8, "color": RED},
    ], accent=GOLD)

    put(s, MX, 3.72, CW, 0.30,
        [{"t": "INSTRUMENTA KĻŪDA — cik daudz varam kļūdīties jau ierīces "
               "dēļ:", "size": 16, "bold": True, "color": NAVY}],
        autofit=False)

    tabula(s, MX, 4.08, CW,
           ["Ierīces veids", "Instrumenta kļūda Δx", "Piemērs"],
           [["Analogā (ar skalu)", "puse no iedaļas vērtības: Δx = c / 2",
             "lineāls c = 1 mm → Δx = 0,5 mm"],
            ["Digitālā (ar ekrānu)", "viena pēdējā cipara vienība: Δx = c",
             "svari 0,01 g → Δx = 0,01 g"],
            ["Sensors ar datu uzkrājēju", "norādīta ražotāja pasē",
             "temperatūras sensors ±0,2 °C"]],
           [3.30, 4.40, 4.53], rowh=0.56, size=16, hsize=13)

    panel(s, MX, 6.06, CW, 0.84, [
        {"t": "Neviens mērījums nav absolūti precīzs. Tāpēc fizikā vienmēr "
              "norāda ne tikai vērtību, bet arī tās kļūdu.", "size": 18,
         "bold": True, "color": NAVY},
    ], accent=NAVY, anchor=MSO_ANCHOR.MIDDLE)
    return s


def s_kludas(prs):
    s = blank(prs)
    header(s, "Absolūtā un relatīvā kļūda")

    colw = (CW - 0.38) / 2
    panel(s, MX, 1.20, colw, 2.60, [
        {"t": "ABSOLŪTĀ KĻŪDA  Δx", "size": 13, "bold": True, "color": BLUE},
        {"t": "Par cik vienībām rezultāts var atšķirties no patiesās "
              "vērtības.", "size": 17, "space": 8},
        {"t": "Izsaka tajās pašās mērvienībās, kas lielums.", "size": 17,
         "space": 6},
        {"t": "l = 25,0 cm ;  Δl = 0,05 cm", "size": 19, "bold": True,
         "space": 10, "color": NAVY},
    ], accent=BLUE)

    panel(s, MX + colw + 0.38, 1.20, colw, 2.60, [
        {"t": "RELATĪVĀ KĻŪDA  ε", "size": 13, "bold": True, "color": GREEN},
        {"t": "Cik liela ir kļūda salīdzinājumā ar pašu lielumu.",
         "size": 17, "space": 8},
        {"t": "ε = Δx / x · 100 %", "size": 24, "bold": True, "space": 8,
         "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "ε = 0,05 : 25,0 · 100 % = 0,2 %", "size": 19, "bold": True,
         "space": 8, "color": RED},
    ], accent=GREEN)

    panel(s, MX, 3.98, CW, 1.30, [
        {"t": "PRECIZITĀTI SALĪDZINA PĒC RELATĪVĀS KĻŪDAS", "size": 12,
         "bold": True, "color": GOLD},
        {"t": "Jo mazāka ε, jo precīzāks mērījums — arī tad, ja absolūtā "
              "kļūda ir lielāka.", "size": 20, "bold": True, "space": 8,
         "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "1 mm kļūda, mērot 10 mm, ir liela (10 %); tā pati 1 mm "
              "kļūda, mērot 10 m, ir niecīga (0,01 %).", "size": 17,
         "space": 8, "color": GREY, "align": PP_ALIGN.CENTER},
    ], accent=GOLD, fill=LIGHTGOLD)

    panel(s, MX, 5.46, CW, 1.44, [
        {"t": "REZULTĀTA PIERAKSTS", "size": 12, "bold": True,
         "color": NAVY},
        {"t": "l = (25,00 ± 0,05) cm            t = (23,0 ± 0,5) °C",
         "size": 22, "bold": True, "space": 8, "color": NAVY,
         "align": PP_ALIGN.CENTER},
        {"t": "Vērtību un kļūdu raksta ar vienādu ciparu skaitu aiz komata. "
              "Nerakstām vairāk ciparu, nekā ierīce spēj izmērīt.",
         "size": 17, "space": 8, "color": GREY, "align": PP_ALIGN.CENTER},
    ], accent=NAVY)
    return s


def s_analogs_digitals(prs):
    s = blank(prs)
    header(s, "Analogā, digitālā ierīce vai sensors?")

    C.kartitas(s, 1.20, 2.86, [
        ("ANALOGĀ", BLUE,
         ["Rādījumu nolasa no skalas.",
          "+ Redzama izmaiņu tendence.",
          "+ Nav vajadzīgs barošanas avots.",
          "− Nolasīšanas kļūda (skata leņķis).",
          "− Grūti fiksēt straujas izmaiņas."]),
        ("DIGITĀLĀ", GREEN,
         ["Rādījums parādās ciparos.",
          "+ Nav nolasīšanas kļūdas.",
          "+ Ātri un ērti.",
          "− Cipari NEnozīmē lielāku precizitāti.",
          "− Straujas izmaiņas grūti nolasīt."]),
        ("SENSORS + UZKRĀJĒJS", GOLD,
         ["Mēra automātiski un pieraksta datus.",
          "+ Daudz mērījumu sekundē.",
          "+ Uzreiz veido tabulu un grafiku.",
          "+ Var mērīt ilgstoši un attālināti.",
          "− Jākalibrē; dārgāks."]),
    ])

    panel(s, MX, 4.24, CW, 1.46, [
        {"t": "ATBILDE UZ STUNDAS JAUTĀJUMU", "size": 12, "bold": True,
         "color": RED},
        {"t": "Nē — digitāls mērījums NAV automātiski precīzāks.",
         "size": 22, "bold": True, "space": 8, "color": RED,
         "align": PP_ALIGN.CENTER},
        {"t": "Precizitāti nosaka ierīces kļūda, nevis tas, vai rādījums ir "
              "skalā vai ciparos. Ekrānā var būt daudz ciparu, bet ierīces "
              "kļūda — liela.", "size": 17, "space": 8, "color": GREY,
         "align": PP_ALIGN.CENTER},
    ], accent=RED)

    panel(s, MX, 5.88, CW, 1.02, [
        {"t": "KĀ SAMAZINĀT KĻŪDU", "size": 12, "bold": True,
         "color": NAVY},
        {"t": "Mēra vairākas reizes un rēķina vidējo vērtību  ·  izvēlas "
              "ierīci ar mazāku iedaļas vērtību  ·  mēra lielāku lielumu "
              "(mazāka relatīvā kļūda).", "size": 17, "space": 6},
    ], accent=NAVY)
    footer(s)
    return s


UZDEVUMI = [
    dict(
        nr=1,
        virsraksts="Iedaļas vērtība un instrumenta kļūda",
        teksts="Mērcilindra skalā starp atzīmēm 0 mL un 50 mL ir "
               "25 iedaļas.\n"
               "Aprēķini iedaļas vērtību un instrumenta kļūdu!",
        dots=["a = 0 mL ;  b = 50 mL", "N = 25"],
        jaaprekina=["c = ?", "ΔV = ?"],
        formulas=["c = (b − a) / N", "ΔV = c / 2"],
        aprekins=[
            "1)  c = (50 mL − 0 mL) : 25 = 2 mL",
            "2)  ΔV = c / 2 = 2 mL : 2 = 1 mL",
        ],
        atbilde="c = 2 mL ;   ΔV = 1 mL",
        piezime="Analogai ierīcei kļūdu pieņem kā pusi no iedaļas vērtības.",
    ),
    dict(
        nr=2,
        virsraksts="Relatīvā kļūda garuma mērījumā",
        teksts="Ar lineālu, kura iedaļas vērtība ir 1 mm, izmērīts galda "
               "garums 25,0 cm.\n"
               "Aprēķini relatīvo kļūdu un pieraksti rezultātu!",
        dots=["l = 25,0 cm", "c = 1 mm"],
        jaaprekina=["Δl = ?", "ε = ?"],
        formulas=["Δl = c / 2", "ε = Δl / l · 100 %"],
        aprekins=[
            "1)  Δl = 1 mm : 2 = 0,5 mm = 0,05 cm",
            "2)  ε = 0,05 cm : 25,0 cm · 100 %",
            "3)  ε = 0,002 · 100 % = 0,2 %",
        ],
        atbilde="l = (25,00 ± 0,05) cm ;   ε = 0,2 %",
        piezime="Kļūdu un vērtību raksta ar vienādu ciparu skaitu aiz "
                "komata.",
    ),
    dict(
        nr=3,
        virsraksts="Vidējā vērtība no atkārtotiem mērījumiem",
        teksts="Lodītes diametrs mērīts piecas reizes: 12,3 mm; 12,5 mm; "
               "12,4 mm; 12,6 mm; 12,2 mm.\n"
               "Aprēķini vidējo vērtību un absolūto kļūdu!",
        dots=["d₁…d₅ = 12,3; 12,5; 12,4; 12,6; 12,2 mm", "N = 5"],
        jaaprekina=["d(vid) = ?", "Δd = ?"],
        formulas=["d(vid) = (d₁ + … + d₅) / N",
                  "Δd = (d(max) − d(min)) / 2"],
        aprekins=[
            "1)  Σd = 12,3 + 12,5 + 12,4 + 12,6 + 12,2 = 62,0 mm",
            "2)  d(vid) = 62,0 mm : 5 = 12,4 mm",
            "3)  Δd = (12,6 − 12,2) : 2 = 0,2 mm",
        ],
        atbilde="d = (12,4 ± 0,2) mm",
        piezime="Atkārtoti mērījumi samazina nejaušo kļūdu — tāpēc fizikā "
                "vienmēr mēra vairākas reizes.",
    ),
    dict(
        nr=4,
        virsraksts="Kurš mērījums ir precīzāks?",
        teksts="Pirmais skolēns izmērīja 8,0 cm ar kļūdu 0,5 mm. Otrais "
               "izmērīja 250 cm ar kļūdu 5 mm.\n"
               "Kurš mērījums ir precīzāks? Pamato ar aprēķinu!",
        dots=["l₁ = 8,0 cm ;  Δl₁ = 0,5 mm", "l₂ = 250 cm ;  Δl₂ = 5 mm"],
        jaaprekina=["ε₁ = ?", "ε₂ = ?"],
        formulas=["ε = Δl / l · 100 %"],
        aprekins=[
            "1)  ε₁ = 0,05 cm : 8,0 cm · 100 % = 0,63 %",
            "2)  ε₂ = 0,5 cm : 250 cm · 100 % = 0,20 %",
            "3)  ε₂ < ε₁",
        ],
        atbilde="Precīzāks ir otrais mērījums (ε₂ = 0,20 %)",
        piezime="Otrā absolūtā kļūda ir 10 reižu lielāka, tomēr mērījums ir "
                "precīzāks — svarīga ir relatīvā kļūda.",
    ),
    dict(
        nr=5,
        virsraksts="Temperatūras mērījums",
        teksts="Šķidruma termometra iedaļas vērtība ir 2 °C, rādījums "
               "36 °C. Digitālais termometrs rāda 36,4 °C ar kļūdu "
               "0,1 °C.\n"
               "Salīdzini abu mērījumu relatīvās kļūdas!",
        dots=["t₁ = 36 °C ;  c = 2 °C", "t₂ = 36,4 °C ;  Δt₂ = 0,1 °C"],
        jaaprekina=["ε₁ = ?", "ε₂ = ?"],
        formulas=["Δt₁ = c / 2", "ε = Δt / t · 100 %"],
        aprekins=[
            "1)  Δt₁ = 2 °C : 2 = 1 °C",
            "2)  ε₁ = 1 : 36 · 100 % = 2,8 %",
            "3)  ε₂ = 0,1 : 36,4 · 100 % = 0,27 %",
        ],
        atbilde="ε₁ = 2,8 % ;   ε₂ = 0,27 % — digitālais ir precīzāks",
        piezime="Šeit digitālais tiešām ir precīzāks, bet tikai tāpēc, ka "
                "tā kļūda ir mazāka — nevis tāpēc, ka tas ir digitāls.",
    ),
    dict(
        nr=6,
        virsraksts="Blīvuma noteikšana ar kļūdu",
        teksts="Izmērīts: m = (50,0 ± 0,1) g un V = (20,0 ± 0,5) cm³.\n"
               "Aprēķini blīvumu un tā relatīvo kļūdu! (ε(ρ) = ε(m) + ε(V))",
        dots=["m = 50,0 g ;  Δm = 0,1 g", "V = 20,0 cm³ ;  ΔV = 0,5 cm³"],
        jaaprekina=["ρ = ?", "ε(ρ) = ?"],
        formulas=["ρ = m / V", "ε(ρ) = ε(m) + ε(V)"],
        aprekins=[
            "1)  ρ = 0,0500 kg : (2,00 · 10⁻⁵ m³) = 2500 kg/m³",
            "2)  ε(m) = 0,1 : 50,0 · 100 % = 0,2 %",
            "3)  ε(V) = 0,5 : 20,0 · 100 % = 2,5 %",
            "4)  ε(ρ) = 0,2 % + 2,5 % = 2,7 %",
        ],
        atbilde="ρ = 2500 kg/m³ ;   ε(ρ) ≈ 2,7 %",
        piezime="Lielāko kļūdu ienes tilpuma mērījums — tieši to būtu vērts "
                "mērīt precīzāk.",
    ),
]

KOPSAVILKUMS = dict(
    iemacijamies=[
        "Iedaļas vērtība c = (b − a) / N; analogai ierīcei Δx = c/2, "
        "digitālai Δx = pēdējā cipara vienība.",
        "Absolūtā kļūda Δx ir vienībās, relatīvā ε = Δx/x · 100 %.",
        "Precizitāti salīdzina pēc relatīvās kļūdas, nevis absolūtās.",
        "Rezultātu pieraksta formā x = (x ± Δx) mērvienība.",
        "Digitāla ierīce nav automātiski precīzāka — svarīga ir tās kļūda.",
    ],
    majasdarbs=[
        "Termometra skalā starp 0 °C un 100 °C ir 50 iedaļas. Nosaki "
        "iedaļas vērtību un instrumenta kļūdu.",
        "Izmērīts l = 1,50 m ar kļūdu 5 mm. Aprēķini relatīvo kļūdu un "
        "pieraksti rezultātu.",
        "Pieci laika mērījumi: 2,1; 2,3; 2,2; 2,4; 2,0 s. Aprēķini vidējo "
        "vērtību un absolūto kļūdu.",
    ],
    pasvertejums=["Protu noteikt iedaļas vērtību",
                  "Protu aprēķināt absolūto un relatīvo kļūdu",
                  "Protu pierakstīt rezultātu ar kļūdu",
                  "Protu pamatot mērierīces izvēli"],
    nakama="Nākamā stunda: pētījuma plānošana un dati — kā veikt godīgu "
           "pētījumu.",
)


def build(out_path):
    return C.build_lesson(META,
                          [s_meriericies, s_kludas, s_analogs_digitals],
                          UZDEVUMI, KOPSAVILKUMS, out_path)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    out = ("C:/aphysics/Dabaszinibas/1. Pasaule ap mums un tās pētīšana/"
           "1.5. Mērierīces un mērījumu precizitāte.pptx")
    print("Slaidu skaits: %d  ->  %s" % (build(out), out))
