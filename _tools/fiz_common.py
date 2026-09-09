# -*- coding: utf-8 -*-
"""
Kopīgā stundu prezentāciju veidne kursam FIZIKA I (10. un 11. klase).

Izkārtojums, uzdevumu atklāšanas mehānika un teksta automātiskā ietilpināšana
nāk no gen_dabaszinibas_1_1.py (tas pats dzinējs, kas /Dabaszinibas mapē);
šeit ir tikai fizikas kursa atkārtotie slaidi un stundas būvēšanas funkcija.

Failu nosaukumi: «n.n. Stundas tēma_tt.pptx» - «_tt» norāda, ka failu
izveidojis Claude Code (rules_fizika.txt).

Lieto tā:

    import fiz_common as C

    C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)
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

import dz_common as DZ                        # noqa: E402
from dz_common import (                       # noqa: E402
    PALE, PALE2, tabula, tabula_rowh, kartitas, formula_panel,
    TOP_Y, BOT_Y, GAPY)

# Kursa zīmols titullapā - to nomaina build_theme().
KURSS = "FIZIKA I · 10. KLASE"


# ------------------------------------------------------------ atkārtotie slaidi
def slide_title(prs, m):
    s = blank(prs)
    box(s, 0, 0, SW, SH, fill=NAVY, rounded=False)
    box(s, 0, 6.10, SW, 1.40, fill=RGBColor(0x17, 0x2B, 0x4D), rounded=False)

    put(s, 1.05, 1.45, CW, 0.32,
        [{"t": m.get("kurss", KURSS), "size": 16, "bold": True,
          "color": PALE2}], autofit=False)
    put(s, 1.05, 2.00, 11.0, 0.70,
        [{"t": m["temats"], "size": 34, "bold": True, "color": WHITE}])
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
        {"t": "Risinājumu pieraksta latviešu standartā: Dots → Jāaprēķina → "
              "Formulas → Aprēķins → Atbilde.", "size": 17, "space": 16,
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


# =================================================== deklaratīvie satura slaidi
# Bloku veidi (tie paši, kas dz_common.content_slide):
#   ("panelis", virsraksts_vai_None, [rindas], krāsa)
#   ("kartitas", [(virsraksts, krāsa, [rindas]), ...])
#   ("tabula", [galva], [rindas], [platumi])
#   ("formula", etikete, formula, skaidrojums, krāsa)
#   ("divi", (virsr, krāsa, [rindas]), (virsr, krāsa, [rindas]))
content_slide = DZ.content_slide


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
    if uzdevumi:
        slide_divider(prs, meta["uzdevumu_apraksts"])
        for i in range(len(uzdevumi)):
            S.task_slides(prs, i)
    slide_kopsavilkums(prs, kopsavilkums)

    d = os.path.dirname(out_path)
    if d:
        os.makedirs(d, exist_ok=True)
    prs.save(out_path)
    return len(prs.slides._sldIdLst)


def faila_vards(nr, virsraksts):
    """«2.5. Brīvā krišana_tt.pptx» — «_tt» = Claude Code veidots fails."""
    dross = re.sub(r'[\/:*?"<>|]', "-", virsraksts)
    return "%s. %s_tt.pptx" % (nr, dross)


def build_theme(temats, kicker, mape, stundas, kurss=None):
    """stundas: saraksts ar vārdnīcām; katrai izveido vienu .pptx failu."""
    izveidoti = []
    for st in stundas:
        meta = dict(
            temats=temats, kicker=kicker,
            kurss=kurss or KURSS,
            stunda="%s. stunda" % st["nr"],
            virsraksts=st["virsraksts"], jautajums=st["jautajums"],
            apaksraksts=st["apaksraksts"], foot="%s. %s" % (st["nr"],
                                                            st["virsraksts"]),
            merkis=st["merkis"], protu=st["protu"],
            atkartojums=st.get("atkartojums"),
            uzdevumu_apraksts=st.get("uzdevumu_apraksts", ""))

        def teorija(prs, st=st):
            for virsr, blocks in st["teorija"]:
                content_slide(prs, virsr, blocks)

        out = os.path.join(mape, faila_vards(st["nr"], st["virsraksts"]))
        n = build_lesson(meta, [teorija], st.get("uzdevumi", []),
                         st["kopsavilkums"], out)
        izveidoti.append((out, n))
    return izveidoti


def run(build_fn):
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build_fn():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
