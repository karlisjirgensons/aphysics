# -*- coding: utf-8 -*-
"""Uzbuve visus dabaszinibu fizikas parbaudes darbus (PD1...PD9).

Palaiz:  .venv/Scripts/python.exe _tools/gen_pd.py        - visus
         .venv/Scripts/python.exe _tools/gen_pd.py 2 5    - tikai PD2 un PD5
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import pd_common as C          # noqa: E402

VISI = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def ieladet(nr):
    modulis = importlib.import_module("pd_%02d_saturs" % nr)
    return modulis.PD


def main(argv):
    numuri = [int(a) for a in argv] or VISI
    for nr in numuri:
        C.build(ieladet(nr))


if __name__ == "__main__":
    main(sys.argv[1:])
