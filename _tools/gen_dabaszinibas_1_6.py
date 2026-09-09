# -*- coding: utf-8 -*-
"""
1.6. stunda: Pētījuma plānošana un dati — "Kā veikt godīgu pētījumu?"
Plāns: 10.1. temata 6. stunda (pēdējā pirms PD1).
SR: formulē pētāmo jautājumu, nosaka atkarīgo, neatkarīgo un nemainīgos
lielumus; attēlo datus grafikā un formulē secinājumu.
"""

import sys
import dz_common as C
from dz_common import (MX, CW, NAVY, BLUE, GOLD, LIGHTGOLD, GREY, RED,
                       GREEN, WHITE, LINEGREY, PP_ALIGN, MSO_ANCHOR,
                       blank, box, rule, put, panel, header, footer, tabula)

META = dict(
    temats="1. temats. Pasaule ap mums un tās pētīšana",
    kicker=("DABASZINĪBAS · 10. KLASE · 1. TEMATS: PASAULE AP MUMS UN "
            "TĀS PĒTĪŠANA"),
    stunda="1.6. stunda",
    virsraksts="Pētījuma plānošana un dati",
    jautajums="Kā veikt godīgu pētījumu?",
    apaksraksts="Mainīgie lielumi · Datu tabula · Grafiks · Secinājums",
    foot="1.6. Pētījuma plānošana un dati",
    merkis="Iemācīties saplānot godīgu pētījumu — noteikt mainīgos lielumus, "
           "sakārtot datus tabulā un grafikā un formulēt ar datiem pamatotu "
           "secinājumu.",
    protu=[
        "atšķirt neatkarīgo, atkarīgo un nemainīgos lielumus;",
        "noformēt datu tabulu un uzzīmēt grafiku ar pareizām asīm;",
        "nolasīt no grafika vērtību un noteikt tā slīpumu;",
        "formulēt secinājumu, pamatotu ar datiem, un nosaukt kļūdu avotus.",
    ],
    atkartojums="1.5. stundā mācījāmies novērtēt viena mērījuma kļūdu. "
                "Šodien no atsevišķiem mērījumiem veidosim pētījumu ar "
                "secinājumu. Nākamajā stundā — PD1.",
    uzdevumu_apraksts="Datu tabulas, grafiki un secinājumi",
)


def s_soli(prs):
    s = blank(prs)
    header(s, "Pētījuma soļi")

    soli = [("1", "JAUTĀJUMS", "Kā viens lielums\nietekmē otru?", BLUE),
            ("2", "HIPOTĒZE", "Pieņēmums, ko var\npārbaudīt ar mērījumiem",
             BLUE),
            ("3", "MAINĪGIE", "Ko mainu, ko mēru,\nko turu nemainīgu", GOLD),
            ("4", "MĒRĪJUMI", "Vairākas reizes,\nvienādos apstākļos", GOLD),
            ("5", "DATI", "Tabula un\ngrafiks", GREEN),
            ("6", "SECINĀJUMS", "Atbilde uz jautājumu,\npamatota ar datiem",
             GREEN)]

    gapx = 0.24
    w = (CW - 5 * gapx) / 6
    x = MX
    for nr, virsr, teksts, c in soli:
        box(s, x, 1.34, w, 1.90, fill=WHITE, line=c, lw=1.5)
        box(s, x + w / 2 - 0.22, 1.16, 0.44, 0.44, fill=c, line=None)
        put(s, x + w / 2 - 0.22, 1.25, 0.44, 0.28,
            [{"t": nr, "size": 15, "bold": True, "color": WHITE,
              "align": PP_ALIGN.CENTER}], autofit=False)
        lines = [{"t": virsr, "size": 14, "bold": True, "color": c,
                  "align": PP_ALIGN.CENTER}]
        for i, t in enumerate(teksts.split("\n")):
            lines.append({"t": t, "size": 13, "align": PP_ALIGN.CENTER,
                          "space": 8 if i == 0 else 2, "color": GREY})
        put(s, x + 0.10, 1.72, w - 0.20, 1.42, lines)
        x += w + gapx

    panel(s, MX, 3.52, CW, 1.60, [
        {"t": "GODĪGS PĒTĪJUMS", "size": 12, "bold": True, "color": RED},
        {"t": "Vienlaikus maina TIKAI VIENU lielumu. Visu pārējo tur "
              "nemainīgu.", "size": 22, "bold": True, "space": 8,
         "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "Ja reizē maina divus lielumus, nevar zināt, kurš no tiem "
              "izraisīja izmaiņu — pētījums nav godīgs un secinājums nav "
              "pamatots.", "size": 17, "space": 8, "color": GREY,
         "align": PP_ALIGN.CENTER},
    ], accent=RED)

    panel(s, MX, 5.30, CW, 1.60, [
        {"t": "PIEMĒRS — kā slīpums ietekmē lodītes ātrumu", "size": 12,
         "bold": True, "color": NAVY},
        {"t": "Neatkarīgais (maina): rēnītes slīpuma leņķis.       "
              "Atkarīgais (mēra): lodītes ātrums.", "size": 18, "space": 8},
        {"t": "Nemainīgie: tā pati lodīte, tas pats ceļš, tā pati rēnīte, "
              "tas pats mērīšanas veids.", "size": 18, "space": 6,
         "color": GREY},
    ], accent=NAVY)
    return s


def s_mainigie(prs):
    s = blank(prs)
    header(s, "Mainīgie lielumi un datu tabula")

    C.kartitas(s, 1.20, 1.94, [
        ("NEATKARĪGAIS", BLUE,
         ["To es pats MAINU.", "Tabulā — pirmā sleja.",
          "Grafikā — uz x ass."]),
        ("ATKARĪGAIS", GREEN,
         ["To es MĒRU.", "Tabulā — nākamās slejas.",
          "Grafikā — uz y ass."]),
        ("NEMAINĪGIE", GOLD,
         ["Tos es TURU VIENĀDUS.", "Tabulā neparādās,",
          "bet jāapraksta darba gaitā."]),
    ])

    put(s, MX, 3.34, CW, 0.30,
        [{"t": "DATU TABULA — katrā ailē lielums, apzīmējums un mērvienība:",
          "size": 16, "bold": True, "color": NAVY}], autofit=False)

    tabula(s, MX, 3.70, 8.60,
           ["Mērījuma nr.", "Tilpums V, cm³", "Masa m, g", "Blīvums ρ, g/cm³"],
           [["1", "10,0", "79,0", "7,90"],
            ["2", "20,0", "158,0", "7,90"],
            ["3", "30,0", "237,0", "7,90"],
            ["4", "40,0", "316,0", "7,90"]],
           [1.90, 2.30, 2.10, 2.30], rowh=0.46, size=16, hsize=13)

    panel(s, 9.36, 3.70, CW - 8.81, 2.60, [
        {"t": "TABULAS NOTEIKUMI", "size": 12, "bold": True, "color": BLUE},
        {"t": "•  Mērvienību raksta galvā, nevis pie katra skaitļa.",
         "size": 16, "space": 9},
        {"t": "•  Visos skaitļos vienāds ciparu skaits aiz komata.",
         "size": 16, "space": 7},
        {"t": "•  Neatkarīgo lielumu sakārto augošā secībā.", "size": 16,
         "space": 7},
        {"t": "•  Aprēķinātās vērtības — atsevišķā slejā.", "size": 16,
         "space": 7},
    ], accent=BLUE)

    panel(s, MX, 6.44, CW, 0.72, [
        {"t": "Šajā tabulā ρ visos mērījumos ir vienāds — tas liecina, ka "
              "masa ir tieši proporcionāla tilpumam.", "size": 18,
         "bold": True, "color": NAVY},
    ], accent=NAVY, anchor=MSO_ANCHOR.MIDDLE)
    return s


def s_grafiks(prs):
    s = blank(prs)
    header(s, "Grafiks un secinājums")

    # --- shematisks grafiks ------------------------------------------------
    gx, gy, gw, gh = MX, 1.30, 5.30, 3.60
    box(s, gx, gy, gw, gh, fill=WHITE, line=LINEGREY, lw=1.0)
    ox, oy = gx + 0.85, gy + gh - 0.70          # koordinātu sākums
    ax_w, ax_h = 3.90, 2.55
    box(s, ox, oy - ax_h, 0.02, ax_h, fill=NAVY, rounded=False)   # y ass
    box(s, ox, oy, ax_w, 0.02, fill=NAVY, rounded=False)          # x ass
    put(s, gx + 0.12, gy + 0.18, 1.90, 0.26,
        [{"t": "m, g", "size": 13, "bold": True, "color": NAVY}],
        autofit=False)
    put(s, ox + ax_w - 1.10, oy + 0.16, 1.10, 0.26,
        [{"t": "V, cm³", "size": 13, "bold": True, "color": NAVY,
          "align": PP_ALIGN.RIGHT}], autofit=False)
    # punkti un taisne
    for i in range(1, 5):
        px = ox + ax_w * (i / 5.0)
        py = oy - ax_h * (i / 5.0)
        box(s, px - 0.055, py - 0.055, 0.11, 0.11, fill=BLUE, line=None)
    put(s, ox + 0.35, oy - ax_h - 0.02, 3.20, 0.30,
        [{"t": "punkti izvietojas uz taisnes", "size": 12, "italic": True,
          "color": GREY}], autofit=False)
    put(s, ox + 0.10, oy + 0.34, 3.90, 0.28,
        [{"t": "0", "size": 12, "color": GREY}], autofit=False)

    panel(s, 6.20, 1.30, CW - 5.65, 1.72, [
        {"t": "GRAFIKA NOTEIKUMI", "size": 12, "bold": True, "color": BLUE},
        {"t": "•  Neatkarīgais lielums — uz x ass, atkarīgais — uz y ass.",
         "size": 16, "space": 8},
        {"t": "•  Uz katras ass raksta lielumu un mērvienību.", "size": 16,
         "space": 6},
        {"t": "•  Mērogu izvēlas tā, lai punkti aizņemtu visu laukumu.",
         "size": 16, "space": 6},
        {"t": "•  Punktus nesavieno ar lauzītu līniju — velk izlīdzinošu "
              "līkni.", "size": 16, "space": 6},
    ], accent=BLUE)

    panel(s, 6.20, 3.18, CW - 5.65, 1.72, [
        {"t": "SLĪPUMS — ko tas nozīmē", "size": 12, "bold": True,
         "color": GREEN},
        {"t": "k = Δy / Δx", "size": 22, "bold": True, "space": 8,
         "color": NAVY, "align": PP_ALIGN.CENTER},
        {"t": "m(V) grafikā slīpums ir blīvums:  k = Δm / ΔV = ρ.",
         "size": 17, "space": 8},
        {"t": "υ(t) grafikā slīpums ir paātrinājums, s(t) grafikā — ātrums.",
         "size": 16, "space": 6, "color": GREY},
    ], accent=GREEN)

    panel(s, MX, 5.08, CW, 1.82, [
        {"t": "SECINĀJUMS NAV NOVĒROJUMS", "size": 12, "bold": True,
         "color": GOLD},
        {"t": "Novērojums: “Punkti izvietojas uz taisnes caur koordinātu "
              "sākumu.”", "size": 18, "space": 8},
        {"t": "Secinājums: “Masa ir tieši proporcionāla tilpumam; taisnes "
              "slīpums ρ = 7,9 g/cm³ atbilst dzelzij.”", "size": 18,
         "space": 6, "bold": True, "color": NAVY},
        {"t": "Kļūdu avoti: svaru un mērcilindra kļūda, gaisa burbuļi, "
              "nepilnīgi nosusināts paraugs.", "size": 16, "space": 8,
         "color": GREY},
    ], accent=GOLD, fill=LIGHTGOLD)
    return s


UZDEVUMI = [
    dict(
        nr=1,
        virsraksts="Vidējais ātrums no datu tabulas",
        teksts="Pētījumā izmērīts, ka ratiņi 30 s laikā veic 120 m garu "
               "ceļu.\n"
               "Aprēķini ratiņu vidējo ātrumu un izsaki to km/h!",
        dots=["s = 120 m", "t = 30 s"],
        jaaprekina=["υ = ?  (m/s)", "υ = ?  (km/h)"],
        formulas=["υ(vid) = s / t"],
        aprekins=[
            "1)  υ = s / t = 120 m : 30 s = 4,0 m/s",
            "2)  υ = 4,0 · 3,6 = 14,4 km/h",
        ],
        atbilde="υ = 4,0 m/s = 14,4 km/h",
        piezime="No m/s uz km/h reizina ar 3,6.",
    ),
    dict(
        nr=2,
        virsraksts="Ceļš no ātruma grafika",
        teksts="Grafikā redzams, ka ķermeņa ātrums 8,0 s laikā nemainīgi ir "
               "2,5 m/s.\n"
               "Aprēķini veikto ceļu! Kāds lielums grafikā atbilst šim "
               "ceļam?",
        dots=["υ = 2,5 m/s", "t = 8,0 s"],
        jaaprekina=["s = ?"],
        formulas=["υ = s / t", "s = υ · t"],
        aprekins=[
            "1)  s = υ · t = 2,5 m/s · 8,0 s",
            "2)  s = 20 m",
        ],
        atbilde="s = 20 m — tas ir laukums zem υ(t) grafika",
        piezime="Vienmērīgas kustības υ(t) grafikā ceļš ir taisnstūra "
                "laukums zem līnijas.",
    ),
    dict(
        nr=3,
        virsraksts="Blīvums no grafika slīpuma",
        teksts="Pētījumā ieguva m(V) grafiku: pie V = 40,0 cm³ masa ir "
               "316 g, pie V = 10,0 cm³ masa ir 79 g.\n"
               "Aprēķini grafika slīpumu un nosaki, kāda viela tā ir!",
        dots=["V₁ = 10,0 cm³ ;  m₁ = 79 g", "V₂ = 40,0 cm³ ;  m₂ = 316 g"],
        jaaprekina=["k = ρ = ?"],
        formulas=["k = Δm / ΔV", "ρ = m / V"],
        aprekins=[
            "1)  Δm = 316 g − 79 g = 237 g",
            "2)  ΔV = 40,0 cm³ − 10,0 cm³ = 30,0 cm³",
            "3)  ρ = 237 g : 30,0 cm³ = 7,9 g/cm³ = 7900 kg/m³",
        ],
        atbilde="ρ = 7,9 · 10³ kg/m³ — viela ir dzelzs",
        piezime="Grafika slīpums dod blīvumu neatkarīgi no tā, kurus divus "
                "punktus izvēlas.",
    ),
    dict(
        nr=4,
        virsraksts="Transpirācijas pētījums",
        teksts="Pētot transpirāciju, augs 4,0 stundās zaudēja 12 g ūdens.\n"
               "Aprēķini ūdens zuduma ātrumu gramos stundā un miligramos "
               "sekundē!",
        dots=["m = 12 g", "t = 4,0 h"],
        jaaprekina=["υ = ?  (g/h)", "υ = ?  (mg/s)"],
        formulas=["υ = m / t"],
        aprekins=[
            "1)  υ = 12 g : 4,0 h = 3,0 g/h",
            "2)  t = 4,0 h = 4,0 · 3600 s = 1,44 · 10⁴ s",
            "3)  υ = 12 000 mg : (1,44 · 10⁴ s) = 0,83 mg/s",
        ],
        atbilde="υ = 3,0 g/h ≈ 0,83 mg/s",
        piezime="Neatkarīgais lielums šeit ir laiks, atkarīgais — zaudētā "
                "ūdens masa.",
    ),
    dict(
        nr=5,
        virsraksts="Atkārtoti mērījumi pētījumā",
        teksts="Lodītes noripošanas laiks mērīts piecas reizes: 1,8 s; "
               "2,0 s; 1,9 s; 2,1 s; 1,7 s. Ceļa garums ir 1,90 m.\n"
               "Aprēķini vidējo laiku un vidējo ātrumu!",
        dots=["t₁…t₅ = 1,8; 2,0; 1,9; 2,1; 1,7 s", "s = 1,90 m"],
        jaaprekina=["t(vid) = ?", "υ = ?"],
        formulas=["t(vid) = (t₁ + … + t₅) / N", "υ = s / t(vid)"],
        aprekins=[
            "1)  Σt = 1,8 + 2,0 + 1,9 + 2,1 + 1,7 = 9,5 s",
            "2)  t(vid) = 9,5 s : 5 = 1,9 s",
            "3)  υ = 1,90 m : 1,9 s = 1,0 m/s",
        ],
        atbilde="t(vid) = 1,9 s ;   υ = 1,0 m/s",
        piezime="Ātrumu rēķina no VIDĒJĀ laika, nevis no viena mērījuma.",
    ),
    dict(
        nr=6,
        virsraksts="Divu materiālu salīdzinājums",
        teksts="Pētot siltumizolāciju, pirmā trauka temperatūra 10 minūtēs "
               "krita no 80 °C līdz 62 °C, otrā — no 80 °C līdz 71 °C.\n"
               "Aprēķini atdzišanas ātrumu abiem un secini, kurš materiāls "
               "izolē labāk!",
        dots=["Δt₁: 80 → 62 °C", "Δt₂: 80 → 71 °C", "τ = 10 min"],
        jaaprekina=["υ₁ = ?", "υ₂ = ?"],
        formulas=["υ = Δt / τ"],
        aprekins=[
            "1)  υ₁ = (80 − 62) °C : 10 min = 1,8 °C/min",
            "2)  υ₂ = (80 − 71) °C : 10 min = 0,9 °C/min",
            "3)  υ₂ < υ₁ — otrais atdziest divreiz lēnāk",
        ],
        atbilde="υ₁ = 1,8 °C/min ;  υ₂ = 0,9 °C/min — labāk izolē otrais",
        piezime="Secinājums ir pamatots ar skaitļiem. Godīgs salīdzinājums "
                "prasa vienādu sākuma temperatūru un vienādu laiku.",
    ),
]

KOPSAVILKUMS = dict(
    iemacijamies=[
        "Godīgā pētījumā maina tikai vienu lielumu, pārējos tur nemainīgus.",
        "Neatkarīgais lielums — uz x ass, atkarīgais — uz y ass.",
        "Tabulā mērvienību raksta galvā; dati sakārtoti augošā secībā.",
        "Grafika slīpums k = Δy/Δx ir fizikāls lielums: m(V) grafikā tas ir "
        "blīvums.",
        "Secinājums atbild uz pētāmo jautājumu un ir pamatots ar datiem.",
    ],
    majasdarbs=[
        "Pētījumā maina atsperes slodzi un mēra pagarinājumu. Nosaki "
        "neatkarīgo, atkarīgo un divus nemainīgos lielumus.",
        "Ķermenis 25 s laikā veic 150 m. Aprēķini vidējo ātrumu m/s un "
        "km/h.",
        "m(V) grafikā pie V = 50 cm³ masa ir 135 g. Aprēķini blīvumu "
        "kg/m³ un nosaki vielu.",
    ],
    pasvertejums=["Protu noteikt mainīgos lielumus",
                  "Protu noformēt tabulu un grafiku",
                  "Protu aprēķināt grafika slīpumu",
                  "Protu formulēt ar datiem pamatotu secinājumu"],
    nakama="Nākamā stunda: PD1 — Pasaule ap mums un tās pētīšana. "
           "Atkārto 1.1.–1.6. stundu saturu un datu bukleta lietošanu.",
)


def build(out_path):
    return C.build_lesson(META, [s_soli, s_mainigie, s_grafiks],
                          UZDEVUMI, KOPSAVILKUMS, out_path)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    out = ("C:/aphysics/Dabaszinibas/1. Pasaule ap mums un tās pētīšana/"
           "1.6. Pētījuma plānošana un dati.pptx")
    print("Slaidu skaits: %d  ->  %s" % (build(out), out))
