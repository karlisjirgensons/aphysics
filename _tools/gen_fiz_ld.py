# -*- coding: utf-8 -*-
"""Uzbūvē visus Fizika I laboratorijas darbus.

Palaiž:  .venv/Scripts/python.exe _tools/gen_fiz_ld.py
         .venv/Scripts/python.exe _tools/gen_fiz_ld.py 10.2 11.3
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import fiz_ld_common as C          # noqa: E402

VISI = ["10.%d" % i for i in range(1, 5)] + ["11.%d" % i for i in range(1, 5)]


def ieladet(kods):
    klase, nr = kods.split(".")
    return importlib.import_module("fizld%s_%s" % (klase, nr)).LD


def main(argv):
    for kods in (argv or VISI):
        C.build(ieladet(kods))


if __name__ == "__main__":
    main(sys.argv[1:])
