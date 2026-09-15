# -*- coding: utf-8 -*-
"""Pārbauda, vai formulas pierakstītas formulu lapas formā.

Skatās gan uzdevumu sadaļu "Formulas:", gan teorijas formulu paneļus.

Noteikumu zina fiz_formulas.py, saraksts ir Fizika_1/Fizika_1_formulas.txt -
šis skripts tikai apstaigā stundu moduļus un izdrukā atrasto (SRP), tāpat kā
check_math.py dara ar aprēķiniem.

Palaiž:  .venv/Scripts/python.exe _tools/check_formulas.py
         .venv/Scripts/python.exe _tools/check_formulas.py fiz_t06a
"""

import glob
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import fiz_formulas as FF          # noqa: E402
import mathfmt as MF               # noqa: E402

TOOLS = os.path.dirname(os.path.abspath(__file__))


def moduli(argv):
    if argv:
        return list(argv)
    return sorted(os.path.splitext(os.path.basename(f))[0]
                  for f in glob.glob(os.path.join(TOOLS,
                                                  "fiz_t[0-9][0-9]*.py")))


def paneļa_formulas(rinda):
    """Teorijas panelī formulas atdala 2+ atstarpes; mērvienības izlaiž.

    Dalīšanas kārtulu zina mathfmt (tā pati, ar ko formulu zīmē), tāpēc
    šeit tā nav uzrakstīta otrreiz (DRY).
    """
    return [g.strip() for g in MF._CHUNK.split(rinda)
            if g.strip() and "[" not in g]


def piezimes(modulis):
    """[(stunda, kur, izteiktā, kanoniskā, veids), ...] vienam modulim."""
    m = importlib.import_module(modulis)
    out = []
    for st in m.STUNDAS:
        for _virsr, blocks in st.get("teorija", []):
            for b in blocks:
                if b[0] != "formula":
                    continue
                for izt, kanon, veids in FF.parbaudit(paneļa_formulas(b[2])):
                    out.append((st["nr"], "teorija «%s»" % b[1],
                                izt, kanon, veids))
        for u in st.get("uzdevumi", []):
            for izt, kanon, veids in FF.parbaudit(u.get("formulas", [])):
                out.append((st["nr"], "%d. uzd." % u["nr"], izt, kanon,
                            veids))
    return out


def main(argv):
    kopa = 0
    for v in moduli(argv):
        rindas = piezimes(v)
        if not rindas:
            continue
        print("--- %s" % v)
        for nr, kur, izteikta, kanon, veids in rindas:
            kapec = ("«%s» ir tikai aiz tās" if veids == "secība"
                     else "«%s» nav vispār")
            print(("  %s. stunda, %s:  «%s» lietota bez formulu lapas "
                   "formas - " + kapec) % (nr, kur, izteikta, kanon))
        kopa += len(rindas)
    print("\nKopā %d piezīme(-s)." % kopa)
    return 1 if kopa else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
