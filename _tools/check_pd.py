# -*- coding: utf-8 -*-
"""Parbauda, vai izveidoto PD .docx lapas ietilpst A4 lapa.

Palaiz:  .venv/Scripts/python.exe _tools/check_pd.py [Dabaszinibas|Fizika_1]

Novertejums ir aptuvens (rakstzimju platums x fonta izmers), bet pietiekams,
lai pamanitu parplusi. Palaiz:  .venv/Scripts/python.exe _tools/check_pd.py
"""

import glob
import os
import sys

import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.stdout.reconfigure(encoding="utf-8")

LAPA = 27.3
PLAT = 18.0
SAKNE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rindas(teksts, pt, plat):
    if not teksts:
        return 1
    w = len(teksts) * pt * 0.47 / 28.35
    return max(1, int(w / plat) + (1 if w % plat else 0))


def para_h(p):
    pt = 11.0
    for r in p.runs:
        if r.font.size:
            pt = r.font.size.pt
            break
    left = p.paragraph_format.left_indent
    left = left.cm if left else 0
    h = rindas(p.text, pt, PLAT - left) * pt * 1.25 / 28.35
    for sp in (p.paragraph_format.space_before, p.paragraph_format.space_after):
        if sp:
            h += sp.pt / 28.35
    if not p.text.strip() and not p.runs:
        h = 0.45
    return h


def table_h(t):
    h = 0.0
    for row in t.rows:
        rh = row.height.cm if row.height else 0
        ch = max(sum(para_h(p) for p in c.paragraphs) for c in row.cells)
        h += max(rh, ch, 0.55)
    return h


def parbaudi(cels):
    d = docx.Document(cels)
    lapas, augstums = [], 0.0
    for ch in d.element.body.iterchildren():
        if ch.tag.endswith("}p"):
            if "w:br" in ch.xml and 'type="page"' in ch.xml:
                lapas.append(augstums)
                augstums = 0.0
                continue
            augstums += para_h(Paragraph(ch, d))
        elif ch.tag.endswith("}tbl"):
            augstums += table_h(Table(ch, d))
    lapas.append(augstums)
    return lapas


def main():
    kludas = 0
    kurss = sys.argv[1] if len(sys.argv) > 1 else "Dabaszinibas"
    faili = sorted(glob.glob(os.path.join(SAKNE, kurss, "*", "PD*.docx")))
    for f in faili:
        lapas = parbaudi(f)
        slikti = [(i + 1, h) for i, h in enumerate(lapas) if h > LAPA]
        stavoklis = "ok" if not slikti else "PARPLUST: " + ", ".join(
            "%d. lapa %.1f cm" % x for x in slikti)
        if slikti:
            kludas += 1
        print("%-72s %2d lapas  %s"
              % (os.path.basename(f)[:72], len(lapas), stavoklis))
    print("\nParbaudīti %d faili, ar parplusi: %d" % (len(faili), kludas))
    return 1 if kludas else 0


if __name__ == "__main__":
    sys.exit(main())
