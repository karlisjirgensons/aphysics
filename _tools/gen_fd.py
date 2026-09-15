# -*- coding: utf-8 -*-
"""Uzbūvē formatīvo darbu ģeneratora lapas.

Katram tematam ir viens satura fails (fd_*.py) ar jautājumu grupām; šis
skripts no tā uzbūvē lapu temata mapē. Jaunu tematu pievieno, uzrakstot vēl
vienu fd_*.py un ierakstot tā kodu sarakstā VISI.

Palaiž:  .venv/Scripts/python.exe _tools/gen_fd.py
         .venv/Scripts/python.exe _tools/gen_fd.py fiz10_1
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import fd_common as C          # noqa: E402

VISI = ["fiz10_1"]


def ieladet(kods):
    return importlib.import_module("fd_%s" % kods).FD


def main(argv):
    for kods in (argv or VISI):
        C.build(ieladet(kods))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
