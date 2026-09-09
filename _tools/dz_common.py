# -*- coding: utf-8 -*-
"""
Kopīgā stundu prezentāciju veidne dabaszinību (fizikas daļas) stundām.

Izkārtojums, uzdevumu atklāšanas mehānika un teksta automātiskā ietilpināšana
nāk no gen_dabaszinibas_1_1.py; šeit ir tikai atkārtotie slaidi (titullapa,
mērķis, uzdevumu šķirlapa, kopsavilkums) un stundas būvēšanas funkcija.

Lieto tā:

    import dz_common as C

    META = dict(temats="1. temats. Pasaule ap mums un tās pētīšana",
                kicker="DABASZINĪBAS · 10. KLASE · 1. TEMATS: ...",
                stunda="1.3. stunda", virsraksts="...", jautajums="...",
                apaksraksts="...", foot="1.3. ...")
    ...
    C.build_lesson(META, [slaids_a, slaids_b], UZDEVUMI, KOPSAVILKUMS, out)
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_dabaszinibas_1_1 as S              # noqa: E402
from gen_dabaszinibas_1_1 import (            # noqa: E402
    SW, SH, MX, CW, NAVY, BLUE, LIGHTBLUE, GOLD, LIGHTGOLD, GREY, LINEGREY,
    LIGHTGREY, DARK, RED, LIGHTRED, GREEN, LIGHTGREEN, WHITE, PP_ALIGN,
    MSO_ANCHOR, RGBColor, new_deck, blank, box, rule, txt, put, panel,
    header, footer, est_h, fit, put_math, math_h, math_w, uid)

PALE = RGBColor(0xBD, 0xD7, 0xEE)
PALE2 = RGBColor(0x9D, 0xC3, 0xE6)


# ------------------------------------------------------------ atkārtotie slaidi
def slide_title(prs, m):
    s = blank(prs)
    box(s, 0, 0, SW, SH, fill=NAVY, rounded=False)
    box(s, 0, 6.10, SW, 1.40, fill=RGBColor(0x17, 0x2B, 0x4D), rounded=False)

    put(s, 1.05, 1.45, CW, 0.32,
        [{"t": "DABASZINĪBAS · 10. KLASE · FIZIKAS DAĻA", "size": 16,
          "bold": True, "color": PALE2}], autofit=False)
    put(s, 1.05, 2.00, 11.0, 0.70,
        [{"t": m["temats"], "size": 36, "bold": True, "color": WHITE}])
    rule(s, 1.05, 3.05, 3.60, GOLD, 0.03)

    put(s, 1.05, 3.45, 11.0, 2.10, [
        {"t": m["stunda"], "size": 21, "bold": True, "color": GOLD},
        {"t": m["virsraksts"], "size": 33, "bold": True, "color": WHITE,
         "space": 12},
        {"t": m["jautajums"], "size": 26, "color": PALE, "space": 8},
    ])
    put(s, 1.05, 6.50, 11.0, 0.55,
        [{"t": m["apaksraksts"], "size": 15, "color": PALE}])
    return s


def slide_merkis(prs, m):
    s = blank(prs)
    header(s, "Stundas mērķis un sasniedzamais rezultāts")

    panel(s, MX, 1.20, CW, 1.15, [
        {"t": "MĒRĶIS", "size": 12, "bold": True, "color": GOLD},
        {"t": m["merkis"], "size": 20, "space": 6},
    ], accent=GOLD, fill=LIGHTGOLD)

    put(s, MX, 2.62, CW, 0.32,
        [{"t": "Stundas beigās es protu:", "size": 16, "bold": True,
          "color": NAVY}], autofit=False)

    items = m["protu"]
    step = 0.70 if len(items) <= 4 else 0.60
    y = 3.10 if len(items) <= 4 else 3.02
    for i, it in enumerate(items, 1):
        box(s, MX, y, 0.44, 0.44, fill=BLUE, line=None)
        put(s, MX + 0.10, y + 0.09, 0.30, 0.28,
            [{"t": str(i), "size": 15, "bold": True, "color": WHITE,
              "align": PP_ALIGN.CENTER}], autofit=False)
        put(s, MX + 0.68, y + 0.05, CW - 0.80, step - 0.10,
            [{"t": it, "size": 19}])
        y += step

    if m.get("atkartojums"):
        panel(s, MX, 6.02, CW, 0.90, [
            {"t": "ATKĀRTOJUMS", "size": 12, "bold": True, "color": NAVY},
            {"t": m["atkartojums"], "size": 17, "space": 5},
        ], accent=NAVY)
    footer(s)
    return s


def slide_divider(prs, apaksvirsraksts):
    s = blank(prs)
    box(s, 0, 0, SW, SH, fill=NAVY, rounded=False)
    put(s, 1.05, 2.55, 11.0, 1.12,
        [{"t": "UZDEVUMI", "size": 56, "bold": True, "color": WHITE}])
    rule(s, 1.05, 3.90, 3.20, GOLD, 0.03)
    put(s, 1.05, 4.25, 11.0, 1.90, [
        {"t": apaksvirsraksts, "size": 24, "color": PALE},
        {"t": "Katrs jaunais solis vispirms parādās liels — pēc tam "
              "nostājas savā vietā risinājumā.", "size": 17, "space": 16,
         "color": PALE2},
    ])
    return s


def slide_kopsavilkums(prs, k):
    s = blank(prs)
    header(s, "Kopsavilkums un mājasdarbs")

    colw = (CW - 0.38) / 2
    kreisi = [{"t": "ŠODIEN IEMĀCĪJĀMIES", "size": 12, "bold": True,
               "color": BLUE}]
    for i, x in enumerate(k["iemacijamies"]):
        kreisi.append({"t": "•  " + x, "size": 17,
                       "space": 12 if i == 0 else 9})
    panel(s, MX, 1.20, colw, 3.94, kreisi, accent=BLUE)

    labi = [{"t": "MĀJASDARBS", "size": 12, "bold": True, "color": GOLD}]
    for i, x in enumerate(k["majasdarbs"], 1):
        labi.append({"t": "%d.  %s" % (i, x), "size": 17, "space": 12})
    panel(s, MX + colw + 0.38, 1.20, colw, 3.94, labi, accent=GOLD,
          fill=LIGHTGOLD)

    panel(s, MX, 5.30, CW, 1.62, [
        {"t": "PAŠVĒRTĒJUMS — atzīmē, cik droši jūties", "size": 12,
         "bold": True, "color": NAVY},
        {"t": "   ·   ".join(k["pasvertejums"]), "size": 17, "space": 9},
        {"t": k["nakama"], "size": 15, "space": 12, "color": GREY,
         "italic": True},
    ], accent=NAVY)
    return s


# ------------------------------------------------------------------- palīgrīki
def tabula_rowh(rows, size=17, rowh=0.52):
    """Rindas augstums; ar vertikālu daļu šūnā vajag vairāk vietas."""
    if any(S.MF.has_math(v) for row in rows for v in row):
        return max(rowh, math_h("a/b", size) + 0.16)
    return rowh


def tabula(slide, x, y, w, hdr, rows, colw, accent=NAVY, rowh=0.52,
           size=17, hsize=14, auto_rowh=True):
    """Vienkārša tabula ar krāsainu galvu."""
    if auto_rowh:
        rowh = tabula_rowh(rows, size, rowh)
    tid = uid("T")
    xs, acc = [], x
    for c in colw:
        xs.append(acc)
        acc += c
    for j, (h, xx, ww) in enumerate(zip(hdr, xs, colw)):
        box(slide, xx, y, ww, 0.46, fill=accent, line=None, rounded=False,
            name="TBLH:%s:%d" % (tid, j))
        put(slide, xx + 0.12, y + 0.10, ww - 0.24, 0.28,
            [{"t": h, "size": hsize, "bold": True, "color": WHITE}],
            name="TBLHT:%s:%d" % (tid, j))
    yy = y + 0.50
    for i, row in enumerate(rows):
        bg = WHITE if i % 2 == 0 else LIGHTBLUE
        for j, (val, xx, ww) in enumerate(zip(row, xs, colw)):
            box(slide, xx, yy, ww, rowh, fill=bg, line=LINEGREY, lw=0.75,
                rounded=False, name="TBLC:%s:%d:%d" % (tid, i, j))
            col = NAVY if j == 0 else DARK
            cn = "TBLCT:%s:%d:%d" % (tid, i, j)
            if S.MF.has_math(val):
                put_math(slide, xx + 0.12, yy, ww - 0.24, rowh, val, size,
                         color=col, bold=(j == 0), align=PP_ALIGN.LEFT,
                         name=cn)
            else:
                put(slide, xx + 0.12, yy + 0.09, ww - 0.24, rowh - 0.18,
                    [{"t": val, "size": size, "bold": (j == 0),
                      "color": col}], name=cn)
        yy += rowh
    return yy


def kartitas(slide, y, h, bloki, cols=3, gapx=0.30):
    """Vienādi lieli paneļi vienā rindā: (virsraksts, krāsa, rindas)."""
    w = (CW - (cols - 1) * gapx) / cols
    x = MX
    for virsr, c, rindas in bloki:
        lines = [{"t": virsr, "size": 20, "bold": True, "color": c}]
        for i, r in enumerate(rindas):
            lines.append({"t": r, "size": 17, "space": 10 if i == 0 else 5})
        panel(slide, x, y, w, h, lines, accent=c)
        x += w + gapx


# ------------------------------------------------------------------- būvēšana
def build_lesson(meta, theory_fns, uzdevumi, kopsavilkums, out_path):
    S.KICKER = meta["kicker"]
    S.FOOT = meta["foot"]
    S.UZDEVUMI = uzdevumi

    prs = new_deck()
    slide_title(prs, meta)
    slide_merkis(prs, meta)
    for fn in theory_fns:
        fn(prs)
    slide_divider(prs, meta["uzdevumu_apraksts"])
    for i in range(len(uzdevumi)):
        S.task_slides(prs, i)
    slide_kopsavilkums(prs, kopsavilkums)

    d = os.path.dirname(out_path)
    if d:
        os.makedirs(d, exist_ok=True)
    prs.save(out_path)
    return len(prs.slides._sldIdLst)


# =================================================== deklaratīvie satura slaidi
# Bloku veidi:
#   ("panelis", virsraksts_vai_None, [rindas], krāsa)
#   ("kartitas", [(virsraksts, krāsa, [rindas]), ...])
#   ("tabula", [galva], [rindas], [platumi])
#   ("formula", etikete, formula, skaidrojums, krāsa)
#   ("divi", (virsr, krāsa, [rindas]), (virsr, krāsa, [rindas]))

TOP_Y = 1.18
BOT_Y = 6.98
GAPY = 0.16


def _panel_lines(virsraksts, rindas, c):
    lines = []
    if virsraksts:
        lines.append({"t": virsraksts, "size": 12, "bold": True, "color": c})
    for i, r in enumerate(rindas):
        if isinstance(r, dict):
            lines.append(r)
        else:
            lines.append({"t": r, "size": 18,
                          "space": (9 if virsraksts else 0) if i == 0 else 7})
    return lines


def _dabiskais_h(b):
    kind = b[0]
    if kind == "tabula":
        return 0.50 + len(b[2]) * tabula_rowh(b[2], 16, 0.50)
    if kind == "kartitas":
        n = max(len(x[2]) for x in b[1])
        return 0.72 + n * 0.34
    if kind == "formula":
        # vertikālai daļai vajag vairāk augstuma nekā rindas pierakstam
        return 1.72 if S.MF.has_math(b[2]) else 1.32
    if kind == "divi":
        n = max(len(b[1][2]), len(b[2][2]))
        return 0.72 + n * 0.36
    return None            # panelis - elastīgs


def formula_panel(slide, x, y, w, h, etikete, formula, skaidrojums, c):
    """Formulas rāmis: dalījumus zīmē vertikāli (skaitītājs virs saucēja)."""
    n = uid("FORM")
    box(slide, x, y, w, h, fill=LIGHTGOLD if c is GOLD else WHITE,
        line=c, lw=1.25, name="BOX:" + n)
    pad = 0.24
    inner_x, inner_w = x + pad, w - 2 * pad
    put(slide, inner_x, y + 0.13, inner_w, 0.24,
        [{"t": etikete, "size": 12, "bold": True, "color": c}],
        autofit=False, name="TXT:" + n)

    skaidr_lines = [{"t": skaidrojums, "size": 16, "color": GREY,
                     "align": PP_ALIGN.CENTER}]
    sk_h = min(est_h(skaidr_lines, inner_w), h - 0.90)
    f_top = y + 0.40
    f_h = h - 0.40 - sk_h - 0.16
    put_math(slide, inner_x, f_top, inner_w, f_h, formula, 26,
             color=NAVY, bold=True, name="TXT:" + n)
    put(slide, inner_x, y + h - pad * 0.62 - sk_h, inner_w, sk_h,
        skaidr_lines, name="TXT:" + n)


def _mero_platumi(platumi):
    """Sleju platumus proporcionāli pieskaņo satura platumam CW.

    Ja saturā ierakstīto platumu summa atšķiras no CW, tabula iznāktu
    ārpus slaida (vai neaizpildītu to). Šeit tos vienmēr pārrēķina, tāpēc
    jau pareizi saskaņotās tabulas nemainās (koeficients ir 1,0).
    """
    kopa = sum(platumi)
    if kopa <= 0:
        return [CW / max(1, len(platumi))] * len(platumi)
    k = CW / kopa
    return [p * k for p in platumi]


def content_slide(prs, title, blocks, ar_footer=True):
    s = blank(prs)
    header(s, title)

    dabiskie = [_dabiskais_h(b) for b in blocks]
    fiksets = sum(h for h in dabiskie if h is not None)
    elastigi = sum(1 for h in dabiskie if h is None)
    kopa = BOT_Y - TOP_Y - GAPY * (len(blocks) - 1)

    # Ja fiksēto bloku dabiskais augstums neietilpst lapā (piem., tabula ar
    # vertikālām daļām), tos proporcionāli saspiež - nekas nepaliek ārpus
    # slaida.
    telpa_fiksetiem = kopa - elastigi * 0.72
    saspiedums = 1.0
    if fiksets > telpa_fiksetiem > 0:
        saspiedums = telpa_fiksetiem / fiksets
        dabiskie = [None if h is None else h * saspiedums for h in dabiskie]
        fiksets = telpa_fiksetiem

    atlikums = kopa - fiksets
    elast_h = max(0.72, atlikums / elastigi) if elastigi else 0.0

    y = TOP_Y
    for b, dh in zip(blocks, dabiskie):
        h = dh if dh is not None else elast_h
        kind = b[0]
        if kind == "panelis":
            _, virsr, rindas, c = b
            panel(s, MX, y, CW, h, _panel_lines(virsr, rindas, c), accent=c)
        elif kind == "kartitas":
            kartitas(s, y, h, b[1], cols=len(b[1]))
        elif kind == "tabula":
            n = max(1, len(b[2]))
            tabula(s, MX, y, CW, b[1], b[2], _mero_platumi(b[3]),
                   rowh=(h - 0.50) / n, size=16 * min(1.0, saspiedums),
                   hsize=13, auto_rowh=False)
        elif kind == "formula":
            _, etik, form, skaidr, c = b
            formula_panel(s, MX, y, CW, h, etik, form, skaidr, c)
        elif kind == "divi":
            colw = (CW - 0.38) / 2
            for i, blk in enumerate((b[1], b[2])):
                v, c, rindas = blk
                panel(s, MX + i * (colw + 0.38), y, colw, h,
                      _panel_lines(v, rindas, c), accent=c)
        y += h + GAPY

    if ar_footer:
        footer(s)
    return s


def build_theme(temats, kicker, mape, stundas):
    """stundas: saraksts ar vārdnīcām; katrai izveido vienu .pptx failu."""
    izveidoti = []
    for st in stundas:
        meta = dict(
            temats=temats, kicker=kicker,
            stunda="%s. stunda" % st["nr"],
            virsraksts=st["virsraksts"], jautajums=st["jautajums"],
            apaksraksts=st["apaksraksts"], foot="%s. %s" % (st["nr"],
                                                           st["virsraksts"]),
            merkis=st["merkis"], protu=st["protu"],
            atkartojums=st.get("atkartojums"),
            uzdevumu_apraksts=st["uzdevumu_apraksts"])

        def teorija(prs, st=st):
            for virsr, blocks in st["teorija"]:
                content_slide(prs, virsr, blocks)

        # Windows failu nosaukumos nedrīkst būt  \ / : * ? " < > |
        dross = re.sub(r'[\/:*?"<>|]', "-", st["virsraksts"])
        out = os.path.join(mape, "%s. %s.pptx" % (st["nr"], dross))
        n = build_lesson(meta, [teorija], st["uzdevumi"],
                         st["kopsavilkums"], out)
        izveidoti.append((out, n))
    return izveidoti
