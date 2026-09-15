# -*- coding: utf-8 -*-
"""Uzbūvē matemātikas pārbaudes darbu ģeneratora lapas.

Katram tematam ir viens satura fails (mat_<klase>_<temats>.py) ar abiem
darbiem; šis skripts no tā uzbūvē divas lapas temata mapē un pēc tam
pārzīmē PD ģeneratora sarakstu un vietnes sākumlapu.

Jaunu tematu pievieno divos soļos: uzraksta mat_*.py ar FD un PD saturu un
ieraksta to mat_temati.SATURS. Pārējais - saraksts, pogas, faili - mainās
pats (DRY).

Palaiž:  .venv/Scripts/python.exe _tools/gen_mat.py
         .venv/Scripts/python.exe _tools/gen_mat.py 1.1.
"""

import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import mat_common as M           # noqa: E402
import mat_temati                # noqa: E402
import site_index                # noqa: E402


def ieladet(kods):
    """Temata koda satura modulis -> {"fd": ..., "pd": ...}."""
    return importlib.import_module(mat_temati.SATURS[kods]).DARBI


def main(argv):
    for kods in (argv or sorted(mat_temati.SATURS)):
        darbi = ieladet(kods)
        for veids, _ in mat_temati.VEIDI:
            M.build(darbi[veids])
    print("Saraksts:  %s" % os.path.relpath(site_index.build_pd_index(),
                                            site_index.SITE_ROOT))
    print("Sākumlapa: %s" % os.path.relpath(site_index.build_home(),
                                            site_index.SITE_ROOT))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
