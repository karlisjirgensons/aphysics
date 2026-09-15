# -*- coding: utf-8 -*-
"""Uzbūvē visus ātros testus (ĀT).

Palaiž:  .venv/Scripts/python.exe _tools/gen_at.py
         .venv/Scripts/python.exe _tools/gen_at.py fiz10_1
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import at_common as C          # noqa: E402

VISI = ["fiz10_1", "fiz11_6", "dz_01"]


def ieladet(kods):
    return importlib.import_module("at_%s" % kods).AT


def main(argv):
    for kods in (argv or VISI):
        C.build(ieladet(kods))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
