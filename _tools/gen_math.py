# -*- coding: utf-8 -*-
"""Matemātikas plānu un lapu būvētājs.

    python gen_math.py            # visi plāni (Math/math_N.docx) un lapas
    python gen_math.py 3 5        # tikai 3. un 5. klases plāns

Gada plānu saturs ir math_1.py ... math_9.py, plāna izskats - math_plani.py,
atsevišķas stundas saturs - math_<klase>_<nr>.py, tās lapa - math_lapa.py un
math_stundas.py, klašu un tematu saraksti - math_vietne.py. Šis fails tikai
savieno tos un pastāsta, kas sanāca (SRP).

Secība ir svarīga: stundu lapas jāuzraksta pirms sarakstiem, jo stunda kļūst
par pogu tikai tad, kad tās fails ir vietā.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import math_plani                                   # noqa: E402
import math_stundas                                 # noqa: E402
import math_vietne                                  # noqa: E402
import site_index                                   # noqa: E402


def build_plans(numuri=None):
    klases = ([math_plani.klase(n) for n in numuri] if numuri
              else math_plani.klases())
    out = []
    for k in klases:
        out.append((k, k.dokuments()))
    return out


def main(argv):
    numuri = [int(a) for a in argv if a.isdigit()]
    if not os.path.isdir(math_plani.MAPE):
        os.makedirs(math_plani.MAPE)
    for k, path in build_plans(numuri or None):
        print("Plāns:      %-28s %3d stundas, %d PD"
              % (os.path.basename(path), k.stundu_skaits, len(k.temati)))
    for path in math_stundas.build_visas(numuri or None):
        print("Stunda:     %s" % os.path.relpath(path, math_plani.SAKNE))
    for path in math_vietne.build_vietne():
        print("Lapa:       %s" % path)
    print("Sākumlapa:  %s" % site_index.build_home())


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1:])
