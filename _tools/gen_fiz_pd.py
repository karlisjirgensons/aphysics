# -*- coding: utf-8 -*-
"""Uzbūvē visus Fizika I pārbaudes darbus.

Palaiž:  .venv/Scripts/python.exe _tools/gen_fiz_pd.py
         .venv/Scripts/python.exe _tools/gen_fiz_pd.py 10.2 11.5
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import fiz_pd_common as C          # noqa: E402

VISI = (["10.%d" % i for i in range(1, 7)]
        + ["11.%d" % i for i in range(1, 10)])


def ieladet(kods):
    klase, nr = kods.split(".")
    return importlib.import_module("fizpd%s_%s" % (klase, nr)).PD


def main(argv):
    for kods in (argv or VISI):
        C.build(ieladet(kods))


if __name__ == "__main__":
    main(sys.argv[1:])
