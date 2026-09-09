# -*- coding: utf-8 -*-
"""Uzbūvē Fizika I stundu prezentācijas (.pptx).

Katrs temats ir sadalīts vairākos satura moduļos (fiz_tNNx.py), lai faili
paliktu pārskatāmi. Modulis definē TEMATS, KICKER, KURSS, MAPE un STUNDAS.

Palaiž:  .venv/Scripts/python.exe _tools/gen_fiz_stundas.py
         .venv/Scripts/python.exe _tools/gen_fiz_stundas.py 01 02
         .venv/Scripts/python.exe _tools/gen_fiz_stundas.py 01a
"""

import glob
import importlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import fiz_common as C          # noqa: E402

TOOLS = os.path.dirname(os.path.abspath(__file__))


def moduli():
    """Visi satura moduļi kārtībā: fiz_t01a, fiz_t01b, ..., fiz_t14x."""
    faili = glob.glob(os.path.join(TOOLS, "fiz_t[0-9][0-9]*.py"))
    vardi = sorted(os.path.splitext(os.path.basename(f))[0] for f in faili)
    return vardi


def atlasit(argv):
    if not argv:
        return moduli()
    out = []
    for a in argv:
        a = a.lower().lstrip("t")
        for m in moduli():
            sufikss = m[len("fiz_t"):]
            if sufikss == a or sufikss.rstrip("abcdefgh") == a:
                out.append(m)
    return out


def main(argv):
    vardi = atlasit(argv)
    if not vardi:
        raise SystemExit("Nav atrasts neviens satura modulis: %s" % argv)
    kopa = 0
    for v in vardi:
        m = importlib.import_module(v)
        print("--- %s  (%d stundas)" % (v, len(m.STUNDAS)))
        for path, n in C.build_theme(m.TEMATS, m.KICKER, m.MAPE, m.STUNDAS,
                                     kurss=getattr(m, "KURSS", None)):
            print("%3d slaidi  %s" % (n, os.path.basename(path)))
            kopa += 1
    print("\nIzveidotas %d prezentācijas." % kopa)


if __name__ == "__main__":
    main(sys.argv[1:])
